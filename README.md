## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-05](docs/good-messages/2022/2022-12-05.md)


2,137,275 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,137,275 were push events containing 3,245,661 commit messages that amount to 268,831,062 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [tkellogg/dura](https://github.com/tkellogg/dura)@[4dc10296b1...](https://github.com/tkellogg/dura/commit/4dc10296b17dcae9ce273dc2cc6d517ef4617214)
#### Monday 2022-12-05 00:19:51 by Tim Kellogg

Optimization: Check file timestamps (#127)

The current version performs a `git commit` on every repository every 5
seconds. If nothing changed, it simply has no effect. This strategy is
eating up sometimes 10-20% of my CPU (on a poor dev machine), due to the
massive amount of hashing needed to commit so many repositories.

This change creates an optimization by tracking file changed timestamps
and comparing them against last commit timestamps. To do this, we have
to traverse all files in each repository, which `git commit` is doing
anyway. The big difference is that we only need to traverse to the inode
(directory) for the file timestamp entries, so it should be
significantly faster.

Considered design: It has been suggested to use the `notify` crate to be
notified of file changes. The trouble here was a global limit on file
descriptors that can be watched, so you can't watch all files. I
considered some machine learning appraches to guessing which files
should be watched, but abandoned the approach because every strategy I
could think of inolved a fallback to eactly what I'm doing here.

Considered design: Use SQLite to remember timestamps of every file. This
was needlessly complex because I only need to remember one timestamp -
the most recent one. And more important, the last dura commit already
stores it, so SQLite wasn't adding any value.

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[661eaa985e...](https://github.com/Hatterhat/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Monday 2022-12-05 00:25:04 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [cindycutie/app-dev](https://github.com/cindycutie/app-dev)@[8e020fdc39...](https://github.com/cindycutie/app-dev/commit/8e020fdc3970b0bb12b394935307fdcb61ad47b0)
#### Monday 2022-12-05 00:43:17 by cindycutie

Update README.md

Meet a child genius named Sheldon Cooper (already seen as an adult in The Big Bang Theory (2007)) and his family. Some unique challenges face Sheldon, who is socially impaired. It's 1989, and 9-year-old Sheldon Cooper has skipped four grades to start high school along with his less-intellectual older brother

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[8272749e8c...](https://github.com/david-rowley/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Monday 2022-12-05 00:56:49 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[1c27d16e6e...](https://github.com/david-rowley/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Monday 2022-12-05 01:12:37 by Tom Lane

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e9cff525dc...](https://github.com/tgstation/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Monday 2022-12-05 02:18:25 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [asutherland/mozsearch](https://github.com/asutherland/mozsearch)@[680cc4cfc7...](https://github.com/asutherland/mozsearch/commit/680cc4cfc71a3f959ca2cf88beb2cfa177502e47)
#### Monday 2022-12-05 02:58:15 by Andrew Sutherland

Bug 1763005 - Improve tracing logging to be cross-thread.

The initial explanation mechanism used the "set this subscriber to be
used on this thread only" using a guard for lifecycle purposes.  This
provide a linearized JSON log that wouldn't contaminate other threads,
but was inherently single-threaded because after the tokio 0.2 overhaul,
tokio didn't really have a good way to propagate that subscriber to
other threads along with the span.

Notionally
https://docs.rs/tracing-futures/0.2.5/tracing_futures/trait.WithSubscriber.html
would provide this, but as explained at
https://github.com/tokio-rs/tracing/issues/593 and also somewhat at
https://github.com/tokio-rs/tracing/discussions/1626 which gave rise
to our initial implementation (or a related issue did?), that doesn't
work currently.

In the bigger picture, we also do potentially want to do more than
per-"query" logging.  That said our use cases are strongly biased to
"here's this top-level span and I want a hierarchy of everything that
happened in this span and I'm going to report this back to the user or
the test case" as opposed to I want an omniscient view of everything
going on right now".  So something global was always desired.

The approach I've gone with is to discover tracing-forest and decide
that it's great for our next step, and maybe forever.  The primary
trade-off is that it buffers the span tree until it's ready to be
flushed but there are potentially a bunch of up-sides to this and also:
- Understanding what's going on in the system is most important.
- Our logging implemented thus far already has a concept of having the
  request explicitly be told that we want its logging, and this seems
  like a reasonable approach to continue.  Especially because I think
  it's likely we'll also want to support a "needle" mechanism where we
  conditionalize either the log or its output on being related to the
  needle.
- We're already throwing a fair bit of RAM at searchfox and both for
  performance reasons and just human ability to comprehend things, the
  "needle" mechanism I describe above likely means that our 80% case
  for the logging would be trying very hard to not exceed a megabyte
  of logs.
- tracing-forest explicitly has the concept of "a worker should
  process the logs" which is well suited for being able to use
  parallelism to our advantage in the processing and also to leverage
  the abstract span reps to potentially do log decimation on that
  worker thread.

All that said, I do expect to learn a bunch from this, but the most
important thing is that I can tell people how to run a query in explain
mode and have them see something reasonable and non-overwhelming and
am very willing to take a hit to efficiency in this opt-in logging
mode.

The main lesson learned in this whole experience is that things will
break badly if you try and hold an entered span across an await()
call.  The tracing docs are clear that you shouldn't do this, and
in some cases the type system will prevent you from doing this
(maybe the problem was I prefixed the entered guard with a `_`?),
but if we mess this up, it can absolutely cause tracing-forest to
be unable to close out the span hierarchy because a reference to a
span can end up stuck in a thread's thread-local-storage resulting
in `on_close` never being invoked for the span.

---
## [AjEsteban/app-dev](https://github.com/AjEsteban/app-dev)@[a247e75946...](https://github.com/AjEsteban/app-dev/commit/a247e75946768e8aadcfb2eb5442f9d5ccdbb1d7)
#### Monday 2022-12-05 03:02:14 by AjEsteban

Update README.md

I added my favorite movies because it is part of my daily life and I think that 2 movie is very relevant to me and it gives me knowledge how to love a dog and how they handle their relationship even if the girl is sick.

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[4fd404aa8f...](https://github.com/Cheshify/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Monday 2022-12-05 03:16:16 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[5da871e271...](https://github.com/Cheshify/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Monday 2022-12-05 03:16:16 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[2425531eb2...](https://github.com/Cheshify/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Monday 2022-12-05 03:16:16 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [XWendelX/app-dev](https://github.com/XWendelX/app-dev)@[4e333cf9ff...](https://github.com/XWendelX/app-dev/commit/4e333cf9ffa8e4ad14bb77cdbc0f1a2c2049a568)
#### Monday 2022-12-05 03:27:12 by XWendelX

Update README.md

The list that I put are my favorite TV series. The first series is the Supernaturals it's about a two brother fighting or hunting devils or monster and solving supernatural cases. The second is The Boys which is about a group of regular people fighting super heroes. The third is Lucifer it's about the demon lucifer who came to earth and try to solve cases with the female officer.

---
## [CFC-Servers/gm_express_bindings](https://github.com/CFC-Servers/gm_express_bindings)@[71958ba832...](https://github.com/CFC-Servers/gm_express_bindings/commit/71958ba83297e924950d2b021e0e325163c8be74)
#### Monday 2022-12-05 03:45:39 by Brandon Sturgeon

Timers are fucking stupid who the hell made it work like this

---
## [tyrant/blog](https://github.com/tyrant/blog)@[08106f5a87...](https://github.com/tyrant/blog/commit/08106f5a878949a7dd1405f4c1970bb6fe2e7fdc)
#### Monday 2022-12-05 04:43:58 by Mikey Clarke

Gave up and installed gem tailwindcss-rails

Holy shit that was a furnace of pain and suffering
and unholy torment. Never again. I'm completely
bloody sick of Webpack and all its hideous agonies
and offspring and all who support it.

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[9fb81c1094...](https://github.com/mattdway/CreateWithVR/commit/9fb81c1094ee31c371d3ddfc3603291635e564c7)
#### Monday 2022-12-05 06:11:29 by mattdway

12-4-22 Commit	2.5.1

12-4-22	v2.5.1
12-4-22 Commit

* Added a white board with tray for the pen to the left of the door.
* Coded the functionality of this whiteboard.
* The white board is not quite registering every pen tip touch to the board (tag read issue? It's not entering one specific IF statement) and the pen writes are sporadic and don't always match the pen's movement.  The pen's rotation also isn't always locked so the pen flops flat against the board.
* I fixed the east wall collider so that items don't fall partially behind the wall.
* I moved the door button and the white board forward as both those were being interfered by the wall collider.
* I troubleshot and worked on the Door button in hopes of turning off the motor when the door is all the way open or closed.  I have code in place to do this based on the eular angle and the Y rotation of the door but I was getting inconsistent readings on what that angle is and inconsistent results as well.  I ran out of time and need to come back to troubleshoot this more with a fresh set of eyes.
* I discovered that only the top motor renderer has the motor activated.  Not a big deal as one motor is enough but I am curious as to why I am not activating all three hinge joints.
* I broke and fixed
	- The watering can when you try and use it hits so many items it acts funky and when you set it down on any surface it almost always knocks over and makes that annoying water pouring sound. (Came back and fixed)
	- The notebooks have some sort of physics issue that is causing them to spin in your hand in place. (Came back and fixed).
	- The stapler and the dart gun are running into issues where the staples and the darts create physics that cause the stapler/dart gun to be knocked about in unintended ways. (Came back and fixed)
	- The cabinet door intersects with the table that houses the candles. This is because I had to turn off the physics between the furniture and doors to allow the cabinet doors to open properly. They were rubbing and not opening otherwise. (Came back and fixed by creating a small invisible collider that stops the cabinet doors when opened. The only caveat is that my hands can collide with this collider, currently. I could select a different layer or create a new layer that only interacts with the door (and nothing else) and it would fix that).
	- I accidently turned off the physics for the lighter and candles. I think when I turned off interactions between layers of the same type. Some weren't needed/unadvisable from the physics point of view but that one I need to look at and turn back on. (Came back and fixed).
	- I tested the other items on the kitchen table and the water bottle with the lid on is still causing major issues, which I'm not sure why. You put the lid on and it starts spinning like a propeller in your hand. It does make for a fun bottle flipping challenge (it's awesome when it happens to lands right side up after you let it go!), but it's not expected or wanted behavior. Even though it is sort of different. Who knows, maybe I'll decide to leave it. At the moment I think it's the physics interaction between the bottle and the lid but I can't disable those because the socket doesn't work without collision. I'll look at it again on a different date.
	- The wax fruit are all OK.
	- There is also a possible problem with my physics hands. When holding larger items (like the watering can, art, etc.) if you hit it accidently with your left hand then it causes it to start to spin in place. I might need to code something to turn off colliders for both hands, not just the hand holding the item to solve this. This would also fix a sound issue when trying to grab an item in my right hand with my left hand, or vice versa. There is probably a more eloquent coding solution for switching holding the item between hands but in the mean time if I change the C# code to disable both colliders then that would solve a lot of the immediate issues.
	- The whiteboard and motors on the front door still need to be fixed.
	- The door when I lean against it the Player Control still pushes the door out of the way (against the hinges). This doesn't seem to happen when just pressing myself against the door and this also doesn't happen with my hands. I started to research this on Friday so I have some ideas of what to look at and what may or may not help.
@mattdway
mattdway committed on Dec 4

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[b2be252eb6...](https://github.com/jlsnow301/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Monday 2022-12-05 07:11:37 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [Murmeldyret/P3-Project](https://github.com/Murmeldyret/P3-Project)@[28568f6733...](https://github.com/Murmeldyret/P3-Project/commit/28568f67336bbf80d9635fa3ab0575742b180915)
#### Monday 2022-12-05 08:20:31 by Erik

HALLELUJAH!

My prayers have been heard! 
- Regex for poor references, website references, and correct apa ref are complete.
 - Antologies will not function in these, as I cannot fathom a pattern between correct and ucn students ways.
- Lots of ways to refactor should the urge arise :D
- Always check for the search string "[Internet]" before anything else in order to separate references between credible and well... website references.
- referencetests are poor as I only test one instance of references and a theory should be used instead, but maaan, VS got mad at me when i tried that.
- Anyways. Shit works to some extend. remember to apply Fastenshtein to correct for any marginal errors in the texts.

- Happy Hanukkah people <3

---
## [roxell/linux](https://github.com/roxell/linux)@[d470be3c4f...](https://github.com/roxell/linux/commit/d470be3c4f30b4666e43eef6bab80f543563cdb0)
#### Monday 2022-12-05 08:41:19 by Douglas Anderson

clk: qcom: lpass-sc7280: Fix pm_runtime usage

The pm_runtime usage in lpass-sc7280 was broken in quite a few
ways. Specifically:

1. At the end of probe it called "put" twice. This is a no-no and will
   end us up with a negative usage count. Even worse than calling
   "put" twice, it never called "get" once. Thus after bootup it could
   be seen that the runtime usage of the devices managed by this
   driver was -2.
2. In some error cases it manually called pm_runtime_disable() even
   though it had previously used devm_add_action_or_reset() to set
   this up to be called automatically. This meant that in these error
   cases we'd double-call pm_runtime_disable().
3. It forgot to call undo pm_runtime_use_autosuspend(), which can
   sometimes have subtle problems (and the docs specifically mention
   that you need to undo this function).

Overall the above seriously calls into question how this driver is
working. It seems like a combination of "it doesn't", "by luck", and
"because of the weirdness of runtime_pm". Specifically I put a
printout to the serial console every time the runtime suspend/resume
was called for the two devices created by this driver (I wrapped the
pm_clk calls). When I had serial console enabled, I found that the
calls got resumed at bootup (when the clk core probed and before our
double-put) and then never touched again. That's no good.
  [    0.829997] DOUG: my_pm_clk_resume, usage=1
  [    0.835487] DOUG: my_pm_clk_resume, usage=1

When I disabled serial console (speeding up boot), I got a different
pattern, which I guess (?) is better:
  [    0.089767] DOUG: my_pm_clk_resume, usage=1
  [    0.090507] DOUG: my_pm_clk_resume, usage=1
  [    0.151885] DOUG: my_pm_clk_suspend, usage=-2
  [    0.151914] DOUG: my_pm_clk_suspend, usage=-2
  [    1.825747] DOUG: my_pm_clk_resume, usage=-1
  [    1.825774] DOUG: my_pm_clk_resume, usage=-1
  [    1.888269] DOUG: my_pm_clk_suspend, usage=-2
  [    1.888282] DOUG: my_pm_clk_suspend, usage=-2

These different patterns have to do with the fact that the core PM
Runtime code really isn't designed to be robust to negative usage
counts and sometimes may happen to stumble upon a behavior that
happens to "work". For instance, you can see that
__pm_runtime_suspend() will treat any non-zero value (including
negative numbers) as if the device is in use.

In any case, let's fix the driver to be correct. We'll hold a
pm_runtime reference for the whole probe and then drop it (once!) at
the end. We'll get rid of manual pm_runtime_disable() calls in the
error handling. We'll also switch to devm_pm_runtime_enable(), which
magically handles undoing pm_runtime_use_autosuspend() as of commit
b4060db9251f ("PM: runtime: Have devm_pm_runtime_enable() handle
pm_runtime_dont_use_autosuspend()").

While we're at this, let's also use devm_pm_clk_create() instead of
rolling it ourselves.

Note that the above changes make it obvious that
lpassaudio_create_pm_clks() was doing more than just creating
clocks. It was also setting up pm_runtime parameters. Let's rename it.

All of these problems were found by code inspection. I started looking
at this driver because it was involved in a deadlock that I reported a
while ago [1]. Though I bisected the deadlock to commit 1b771839de05
("clk: qcom: gdsc: enable optional power domain support"), it was
never really clear why that patch affected it other than a luck of
timing changes. I'll also note that by fixing the timing (as done in
this change) we also seem to aboid the deadlock, which is a nice
benefit.

Also note that some of the fixes here are much the same type of stuff
that Dmitry did in commit 72cfc73f4663 ("clk: qcom: use
devm_pm_runtime_enable and devm_pm_clk_create"), but I guess
lpassaudiocc-sc7280.c didn't exist then.

[1] https://lore.kernel.org/r/20220922154354.2486595-1-dianders@chromium.org

Fixes: a9dd26639d05 ("clk: qcom: lpass: Add support for LPASS clock controller for SC7280")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Signed-off-by: Bjorn Andersson <andersson@kernel.org>
Link: https://lore.kernel.org/r/20221104064055.1.I00a0e4564a25489e85328ec41636497775627564@changeid

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[f4335e5184...](https://github.com/Stalkeros2/Skyrat-tg/commit/f4335e5184da0a4643bab601ae11c59e9d411a6e)
#### Monday 2022-12-05 09:01:01 by SkyratBot

[MIRROR] Fishing Odds Code Improvements and Rescue Hooks [MDB IGNORE] (#17697)

* Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

* Fishing Odds Code Improvements and Rescue Hooks

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [dyrone/git](https://github.com/dyrone/git)@[f1c903debd...](https://github.com/dyrone/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Monday 2022-12-05 09:57:34 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Monday 2022-12-05 10:25:09 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [guardian/gateway](https://github.com/guardian/gateway)@[b962f668b3...](https://github.com/guardian/gateway/commit/b962f668b35ac72f8f0a0aaace8ee180da8b816e)
#### Monday 2022-12-05 10:39:59 by Mahesh Makani

feat(okta): show onboarding flow for new social users

In Okta it is currently not possible to differentiate between new social users, and existing social users. This means that is was not possible to show social users the
onboarding flow.

However there is a case where a new social user differentiates form existing social users. This is to do with the email validated status. A new social user will be in
the `GuardianUser-EmailValidated` but their `emailValidated` field in their user profile will be `false` or `undefined`. So we have a remediation step in our callback to
handle this discrepency, and set the `emailValidated` flag should the user be in the `GuardianUser-EmailValidated` group. This was introduced in this commit:
https://github.com/guardian/gateway/commit/9af078165aa5add60b9e11bfe6731ff25badca6e

This means that the only time this discrepency will occur is for new social users, meaning at this point we can differentiate them from existing social users. This
allows us to use this functionality and set a flag to show the onboarding flow `authState.confirmationPage = consentPages[0].path;`. At any other point in time the user
will have both the `GuardianUser-EmailValidated` group and the `emailValidated` flag set, so they would not see the onboarding flow again.

A number of other options were considered for this functionality, but would involve other changes to the Okta configuration.

1. Using Okta groups
The first option we tried was to use Okta groups to do this. The theory was for new social users we assign them to a specific Okta group that we create, we can then
check this group, and if a user is in this group show then the onboarding flow. We can then remove them from this group so they're not shown the onboarding flow again.

However although this does work and new social users do see the Onboarding flow. I noticed that all social users started seeing the onboarding flow, whether they were
new users, existing users, or had even seen the onboarding flow before. Turns out Okta will always add all social users to the new group if they are not currently in it.
So even when removing the group from the user,  the next time they sign in with social, they get added to the group again, and they get shown the onboarding flow again.
Which wasn't ideal.

2. Using the account `created` timestamp on the user object.
This option was to use the `created` field in the user profile to determine if we should show the onboarding flow or not. This would involve checking this field
everytime a user went to the oauth callback endpoint, and if it's within a certain time period, say 1 minute, then to show the onboarding flow in that scenario.

However the account `created` field isn't returned by default in either the access or id token. So we'd either have to make an additional API call for every time a user
goes to the oauth callback endpoint, or to add a custom claim to add this field to the id token.

Using the API option would require making additional API calls, which we're trying to avoid, due to a limited number of API calls we're able to make to Okta. While
adding this field to the id token would require changes to the Okta terraform configuration to add this in, and would add an additional payload to what's only
effectively used once.

Also we'd have to chose the time period to check to avoid users seeing the onboarding flow multiple times if we set it too long, e.g. if they sign in immeditely after
registering on another browser/device, or not seeing the onboarding flow at all if we set it too short.

Hence the reason I went with the approach that we did.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[6120721323...](https://github.com/cmss13-devs/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Monday 2022-12-05 11:20:09 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [16118736501/art](https://github.com/16118736501/art)@[d7cdd16389...](https://github.com/16118736501/art/commit/d7cdd16389cf7ce8e94d2b5b8d397d6893d284ca)
#### Monday 2022-12-05 11:39:30 by 16118736501

Create Confession.txt

Anders Pippi Tednes har personnummer 16118736501. 
Dette bør i utgangspunktet gi i hel rekke rettigheter. Gjerne omtalt som menneskerettigheter. 
Jeg er drittlei av å nektes slike. Så sorry folkens. Du kan hate eller elske meg, men jeg bryter ingen verdens lover ved å publisere erfaringene mine offentlig.  
Og som anarkist kan det alltids tenkes jeg vil tviholde på retten til å gi litt faen. 

Juss er dødsenkelt. Og dritskummelt. Og her vil jeg gjøre mitt for å finne de morsomste måtene å vitse med absolutt alt. Og sorry, selv om jeg er sønnen til Henry Andreas Tendenes, så er det faktisk ikke min feil at politiet i Stavanger, tross enkelte avvik, styres av en gjeng korrupte pedojævler. Men sorry: selv om jeg ikke er ansvarlig for min fars handlinger, så velger jeg å stå for mine. Min mening er at purken i Stavanger best kan kalles mafia. Og at faren min best kan kalles pedo. 
I min logikk betyr det: pedomafia. 
Og ja, jeg er sikkert både sexy, sær og særegen: Men jeg står for hver eneste av ordene: Purken i Rogaland styres for tiden stort sett av slike folk som faren min, Henry Tendnes, har ansatt gjennom 40 år. Her er et hint fra meg: Politimester Bastian og kardemommeloven er fiksjon. Henry Tendenes er pedofil. Han er ekte. Og han er faren min.

---
## [Empire-Strikes-Back/Grogu](https://github.com/Empire-Strikes-Back/Grogu)@[39e305d9ac...](https://github.com/Empire-Strikes-Back/Grogu/commit/39e305d9ac07c02350f62142ff9f632544ae82f5)
#### Monday 2022-12-05 12:02:45 by Grogu

who is the jerk?! - Ellie, meet mr. Hammond

like Steve Nash didn't create - didn't hear about memebers of the household - so I also had no root and rushed

like Garth Davis I was more conerned about Money than God's will

I didn't pay attention to what Jesus says - about two masters, memebers of the household, greet

let my idenity fruit as a program be banana
banana is evil and an enemy - so am I
like bloodsucking lawyer I was to concerned with serving caesar
let me not have git history or releases but one - current
I agree with garden in this - even though we are enemis

:Jim-Carrey I can just show up and joy the parties! I have nothing else to worry about

---
## [waleligntewabe/waleligntewabe.github.io](https://github.com/waleligntewabe/waleligntewabe.github.io)@[a2b7ba0575...](https://github.com/waleligntewabe/waleligntewabe.github.io/commit/a2b7ba05753222b5aad10d016e9d1a8a2d0b9142)
#### Monday 2022-12-05 12:04:47 by waleligntewabe

Create README.md

Creative Commons Attribution 3.0 Unported
http://creativecommons.org/licenses/by/3.0/

License

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.

1. Definitions

   1. "Adaptation" means a work based upon the Work, or upon the Work and other pre-existing works, such as a translation, adaptation, derivative work, arrangement of music or other alterations of a literary or artistic work, or phonogram or performance and includes cinematographic adaptations or any other form in which the Work may be recast, transformed, or adapted including in any form recognizably derived from the original, except that a work that constitutes a Collection will not be considered an Adaptation for the purpose of this License. For the avoidance of doubt, where the Work is a musical work, performance or phonogram, the synchronization of the Work in timed-relation with a moving image ("synching") will be considered an Adaptation for the purpose of this License.
   2. "Collection" means a collection of literary or artistic works, such as encyclopedias and anthologies, or performances, phonograms or broadcasts, or other works or subject matter other than works listed in Section 1(f) below, which, by reason of the selection and arrangement of their contents, constitute intellectual creations, in which the Work is included in its entirety in unmodified form along with one or more other contributions, each constituting separate and independent works in themselves, which together are assembled into a collective whole. A work that constitutes a Collection will not be considered an Adaptation (as defined above) for the purposes of this License.
   3. "Distribute" means to make available to the public the original and copies of the Work or Adaptation, as appropriate, through sale or other transfer of ownership.
   4. "Licensor" means the individual, individuals, entity or entities that offer(s) the Work under the terms of this License.
   5. "Original Author" means, in the case of a literary or artistic work, the individual, individuals, entity or entities who created the Work or if no individual or entity can be identified, the publisher; and in addition (i) in the case of a performance the actors, singers, musicians, dancers, and other persons who act, sing, deliver, declaim, play in, interpret or otherwise perform literary or artistic works or expressions of folklore; (ii) in the case of a phonogram the producer being the person or legal entity who first fixes the sounds of a performance or other sounds; and, (iii) in the case of broadcasts, the organization that transmits the broadcast.
   6. "Work" means the literary and/or artistic work offered under the terms of this License including without limitation any production in the literary, scientific and artistic domain, whatever may be the mode or form of its expression including digital form, such as a book, pamphlet and other writing; a lecture, address, sermon or other work of the same nature; a dramatic or dramatico-musical work; a choreographic work or entertainment in dumb show; a musical composition with or without words; a cinematographic work to which are assimilated works expressed by a process analogous to cinematography; a work of drawing, painting, architecture, sculpture, engraving or lithography; a photographic work to which are assimilated works expressed by a process analogous to photography; a work of applied art; an illustration, map, plan, sketch or three-dimensional work relative to geography, topography, architecture or science; a performance; a broadcast; a phonogram; a compilation of data to the extent it is protected as a copyrightable work; or a work performed by a variety or circus performer to the extent it is not otherwise considered a literary or artistic work.
   7. "You" means an individual or entity exercising rights under this License who has not previously violated the terms of this License with respect to the Work, or who has received express permission from the Licensor to exercise rights under this License despite a previous violation.
   8. "Publicly Perform" means to perform public recitations of the Work and to communicate to the public those public recitations, by any means or process, including by wire or wireless means or public digital performances; to make available to the public Works in such a way that members of the public may access these Works from a place and at a place individually chosen by them; to perform the Work to the public by any means or process and the communication to the public of the performances of the Work, including by public digital performance; to broadcast and rebroadcast the Work by any means including signs, sounds or images.
   9. "Reproduce" means to make copies of the Work by any means including without limitation by sound or visual recordings and the right of fixation and reproducing fixations of the Work, including storage of a protected performance or phonogram in digital form or other electronic medium.

2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit, or restrict any uses free from copyright or rights arising from limitations or exceptions that are provided for in connection with the copyright protection under copyright law or other applicable laws.

3. License Grant. Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the duration of the applicable copyright) license to exercise the rights in the Work as stated below:

   1. to Reproduce the Work, to incorporate the Work into one or more Collections, and to Reproduce the Work as incorporated in the Collections;
   2. to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";
   3. to Distribute and Publicly Perform the Work including as incorporated in Collections; and,
   4. to Distribute and Publicly Perform Adaptations.
   5.

      For the avoidance of doubt:
         1. Non-waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme cannot be waived, the Licensor reserves the exclusive right to collect such royalties for any exercise by You of the rights granted under this License;
         2. Waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme can be waived, the Licensor waives the exclusive right to collect such royalties for any exercise by You of the rights granted under this License; and,
         3. Voluntary License Schemes. The Licensor waives the right to collect royalties, whether individually or, in the event that the Licensor is a member of a collecting society that administers voluntary licensing schemes, via that society, from any exercise by You of the rights granted under this License.

The above rights may be exercised in all media and formats whether now known or hereafter devised. The above rights include the right to make such modifications as are technically necessary to exercise the rights in other media and formats. Subject to Section 8(f), all rights not expressly granted by Licensor are hereby reserved.

4. Restrictions. The license granted in Section 3 above is expressly made subject to and limited by the following restrictions:

   1. You may Distribute or Publicly Perform the Work only under the terms of this License. You must include a copy of, or the Uniform Resource Identifier (URI) for, this License with every copy of the Work You Distribute or Publicly Perform. You may not offer or impose any terms on the Work that restrict the terms of this License or the ability of the recipient of the Work to exercise the rights granted to that recipient under the terms of the License. You may not sublicense the Work. You must keep intact all notices that refer to this License and to the disclaimer of warranties with every copy of the Work You Distribute or Publicly Perform. When You Distribute or Publicly Perform the Work, You may not impose any effective technological measures on the Work that restrict the ability of a recipient of the Work from You to exercise the rights granted to that recipient under the terms of the License. This Section 4(a) applies to the Work as incorporated in a Collection, but this does not require the Collection apart from the Work itself to be made subject to the terms of this License. If You create a Collection, upon notice from any Licensor You must, to the extent practicable, remove from the Collection any credit as required by Section 4(b), as requested. If You create an Adaptation, upon notice from any Licensor You must, to the extent practicable, remove from the Adaptation any credit as required by Section 4(b), as requested.
   2. If You Distribute, or Publicly Perform the Work or any Adaptations or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work; and (iv) , consistent with Section 3(b), in the case of an Adaptation, a credit identifying the use of the Work in the Adaptation (e.g., "French translation of the Work by Original Author," or "Screenplay based on original Work by Original Author"). The credit required by this Section 4 (b) may be implemented in any reasonable manner; provided, however, that in the case of a Adaptation or Collection, at a minimum such credit will appear, if a credit for all contributing authors of the Adaptation or Collection appears, then as part of these credits and in a manner at least as prominent as the credits for the other contributing authors. For the avoidance of doubt, You may only use the credit required by this Section for the purpose of attribution in the manner set out above and, by exercising Your rights under this License, You may not implicitly or explicitly assert or imply any connection with, sponsorship or endorsement by the Original Author, Licensor and/or Attribution Parties, as appropriate, of You or Your use of the Work, without the separate, express prior written permission of the Original Author, Licensor and/or Attribution Parties.
   3. Except as otherwise agreed in writing by the Licensor or as may be otherwise permitted by applicable law, if You Reproduce, Distribute or Publicly Perform the Work either by itself or as part of any Adaptations or Collections, You must not distort, mutilate, modify or take other derogatory action in relation to the Work which would be prejudicial to the Original Author's honor or reputation. Licensor agrees that in those jurisdictions (e.g. Japan), in which any exercise of the right granted in Section 3(b) of this License (the right to make Adaptations) would be deemed to be a distortion, mutilation, modification or other derogatory action prejudicial to the Original Author's honor and reputation, the Licensor will waive or not assert, as appropriate, this Section, to the fullest extent permitted by the applicable national law, to enable You to reasonably exercise Your right under Section 3(b) of this License (right to make Adaptations) but not otherwise.

5. Representations, Warranties and Disclaimer

UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR OFFERS THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO SUCH EXCLUSION MAY NOT APPLY TO YOU.

6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

7. Termination

   1. This License and the rights granted hereunder will terminate automatically upon any breach by You of the terms of this License. Individuals or entities who have received Adaptations or Collections from You under this License, however, will not have their licenses terminated provided such individuals or entities remain in full compliance with those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any termination of this License.
   2. Subject to the above terms and conditions, the license granted here is perpetual (for the duration of the applicable copyright in the Work). Notwithstanding the above, Licensor reserves the right to release the Work under different license terms or to stop distributing the Work at any time; provided, however that any such election will not serve to withdraw this License (or any other license that has been, or is required to be, granted under the terms of this License), and this License will continue in full force and effect unless terminated as stated above.

8. Miscellaneous

   1. Each time You Distribute or Publicly Perform the Work or a Collection, the Licensor offers to the recipient a license to the Work on the same terms and conditions as the license granted to You under this License.
   2. Each time You Distribute or Publicly Perform an Adaptation, Licensor offers to the recipient a license to the original Work on the same terms and conditions as the license granted to You under this License.
   3. If any provision of this License is invalid or unenforceable under applicable law, it shall not affect the validity or enforceability of the remainder of the terms of this License, and without further action by the parties to this agreement, such provision shall be reformed to the minimum extent necessary to make such provision valid and enforceable.
   4. No term or provision of this License shall be deemed waived and no breach consented to unless such waiver or consent shall be in writing and signed by the party to be charged with such waiver or consent.
   5. This License constitutes the entire agreement between the parties with respect to the Work licensed here. There are no understandings, agreements or representations with respect to the Work not specified here. Licensor shall not be bound by any additional provisions that may appear in any communication from You. This License may not be modified without the mutual written agreement of the Licensor and You.
   6. The rights granted under, and the subject matter referenced, in this License were drafted utilizing the terminology of the Berne Convention for the Protection of Literary and Artistic Works (as amended on September 28, 1979), the Rome Convention of 1961, the WIPO Copyright Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and the Universal Copyright Convention (as revised on July 24, 1971). These rights and subject matter take effect in the relevant jurisdiction in which the License terms are sought to be enforced according to the corresponding provisions of the implementation of those treaty provisions in the applicable national law. If the standard suite of rights granted under applicable copyright law includes additional rights not granted under this License, such additional rights are deemed to be included in the License; this License is not intended to restrict the license of any rights under applicable law.

---
## [FLOWEReconomics/american-py](https://github.com/FLOWEReconomics/american-py)@[6d18e83aaf...](https://github.com/FLOWEReconomics/american-py/commit/6d18e83aaf7a4c2cd9809241ef2af3765096d2f9)
#### Monday 2022-12-05 12:08:44 by Salman C_ Shuaib

-   Why is sir Sergey Brin afraid of utilizing his own wealth, legitimately_ This is an email money transfer record from my Bank of Montreat account to his EMAIL address //he is not aware of the the Personal Leverage Factor theorem which entails that a Dollar worth of goods or currency purchased by a Zero NET WORTH individual is worth 106 Billion US //per USD purchase: in terms of benefit to American Purchasing Power Parity_ So, he was doing an immense service to USA by transferring 5K at a time to me, and asking me to send back only 1K_ However, since people do not know the PLF theorem - they assume this is some sort of money laundering scheme - I do not like going to court  //however, I will end by saying I like gamification and this round ended with a superlative victory for Taylor Swift //Empress, and I refused to delete record of Her victory (which has now been turned by a defaulting bot to an EXE file)_ Sergey, my friend do not be afraid, I have such a clear Conscience (29RED) that what I believe is law //and what 32RED says: goes  _B

---
## [axiomsbane/adventOfCode2022](https://github.com/axiomsbane/adventOfCode2022)@[8d5255c2c4...](https://github.com/axiomsbane/adventOfCode2022/commit/8d5255c2c48b9973c8255e78ef3f8d46208ed0a6)
#### Monday 2022-12-05 14:09:58 by Aditya Shidhaye

Day 5 part 1 done | I hate myself im doing imperative shit in Haskell at this point basically

---
## [SwapnilVicky/kernel_xiaomi_miatoll](https://github.com/SwapnilVicky/kernel_xiaomi_miatoll)@[571360e177...](https://github.com/SwapnilVicky/kernel_xiaomi_miatoll/commit/571360e177681e4cc8289c5faeca543a4e8fb0e8)
#### Monday 2022-12-05 14:15:01 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
[stealth1226: switch to fingerprint@2.1-service]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ccaba554e8...](https://github.com/treckstar/yolo-octo-hipster/commit/ccaba554e8d8c3ddaffe9f2bfaa9fa5f25406550)
#### Monday 2022-12-05 14:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [openSUSE/systemd](https://github.com/openSUSE/systemd)@[48f40fbc8e...](https://github.com/openSUSE/systemd/commit/48f40fbc8e38c1a89a8a648ab23d687e5db2aacf)
#### Monday 2022-12-05 16:46:51 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)

[fbui: adjust context]
[fbui: fixes bsc#1203857]

---
## [emillon/dune](https://github.com/emillon/dune)@[996303b3d5...](https://github.com/emillon/dune/commit/996303b3d52b1922318f5d6c42e2151240281269)
#### Monday 2022-12-05 17:23:26 by Etienne Millon

Add shell completion

This provides a shell completion mechanism for dune. This relies on the
bash completion API, which can be used with zsh as well.

The architecture is:

- `dune complete script` outputs a script to be sourced in the user's
  shell. It is comprised of a `_dune` function and the `complete -F
  _dune dune` command to register it. The `_dune` function can be used
  in cram tests to write natural-looking tests for this feature.
- this script calls `dune complete command` with the partial
  command-line. This internal command parses it to determine what the
  word being completed refers to: a command name, an argument name, or
  an argument value. The first two ones are part of the metadata
  `cmdliner` knows about; the last one is provided through a completion
  function that can be passed in one the `Arg` functions.
- the interface between `bash` and `dune complete command` is simple:
  it passes the command line and a position to complete at (this is
  necessary to encode the difference between `dune bui<tab>` and `dune
  build <tab>` for example), and reads an array from the output of the
  command.

The things I'm happy with:

- it is small!
- coverage is pretty good: command names, arguments (positional and
  optional, including optional arguments with optional names), and the
  `--` construct are supported. So, this is likely to improve the user
  experience already.
- it is easy to test through cram or unit tests (I chose the former).

Now, for the ugly bits...

- this effectively is a partial reimplementation of cmdliner inside
  `complete.ml`. If the exact parsing rules are different, it means that
  we can complete to something with different or wrong semantics.
- the vendored copy of cmdliner is patched to expose so that it is
  possible to use the private APIs. these two points need to be resolved
  before we can think about how to upstream this.
- some bits of the cmdliner API need to be modified to provide
  completion automatically. For example for things like `enum` it's easy
  to provide a completion function automatically.
- it is difficult to define the right API for the completion functions.
  `unit -> string list` is a first approximation but with some
  limitations. For example, getting a list of buildable targets needs to
  run under `Fiber`, but we can't pollute the API with it. Interestingly
  enough, algebraic effects seem like they would be an interesting
  solution for this.
- at the moment, we're not relying on the shell's completion helpers to
  complete things like filenames. To support this we would either need
  to implement that in OCaml, or extend the bash/dune interface so that
  the completion function could call `compgen -f` based on the dune
  output.
- as a way to tie the two previous points: if we wanted to complete
  `dune build dir/file<tab>`, it would be a lot more efficient to pass
  the prefix to the build system and let it compute just the targets
  that match this, rather than compute everything and filter it
  afterwards. So that prefix would need to appear in the completion API.

Signed-off-by: Etienne Millon <me@emillon.org>

---
## [AyUpItsAli/Alis-Bean-Mod](https://github.com/AyUpItsAli/Alis-Bean-Mod)@[797870d35e...](https://github.com/AyUpItsAli/Alis-Bean-Mod/commit/797870d35e3f616f8f1aaec31717b0ee4cd2abd6)
#### Monday 2022-12-05 17:34:34 by Ali

Changed mod name to "Beanology"
Due to curseforge not allowing the use of "mod" in project names, I've decided to rename the mod from "Ali's Bean Mod" to "Beanology". I think this is a better name anyway for other reasons, so I'm happy with this change (still a tad annoying though curseforge haha).

---
## [Jaden-PHILIPPINES/VGP-P3-2022-2023](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023)@[d172736fc5...](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023/commit/d172736fc5497c08a7d96b9e75599b8c711769b5)
#### Monday 2022-12-05 18:18:59 by Jaden Morales

Fuck you luck

revert to older script because bitch piece of shit unity

---
## [jrcribb/cockroach](https://github.com/jrcribb/cockroach)@[e7b15ebaed...](https://github.com/jrcribb/cockroach/commit/e7b15ebaed9c14668ade0a7827a5525aedef1ab0)
#### Monday 2022-12-05 19:20:33 by craig[bot]

Merge #92713 #92783 #92859

92713: sql: fix left semi and left anti virtual lookup joins r=yuzefovich a=yuzefovich

This commit fixes the execution of the left semi and left anti virtual
lookup joins. The bug was that we forgot to project away the looked up
columns (coming from the "right" side) which could then lead to wrong
columns being used higher up the tree. The bug was introduced during
22.1 release cycle where we added the optimizer support for generating
plans that could contain left semi and left anti virtual lookup joins.
This commit fixes that issue as well as the output columns of such joins
(I'm not sure whether there is a user facing impact of having incorrect
"output columns").

Additionally, this commit fixes the execution of these virtual lookup
joins to correctly return the input row only once. Previously, for left
anti joins we'd be producing an output row if there was a match (which
is wrong), and for both left semi and left anti we would emit an output
row every time there was a match (but this should be done only once).
(Although I'm not sure whether it is possible for virtual indexes to
result in multiple looked up rows.)

Also, as a minor simplification this commit makes it so that the output
rows are not added into the row container for left semi and left anti
and the container is not instantiated at all.

Fixes: #91012.
Fixes: #88096.

Release note (bug fix): CockroachDB previously could incorrectly
evaluate queries that performed left semi and left anti "virtual lookup"
joins on tables in `pg_catalog` or `information_schema`. These join types
can be planned when a subquery is used inside of a filter condition. The
bug was introduced in 22.1.0 and is now fixed.

92783: nogo: detect deprecated go standard library packages r=rickystewart a=healthy-pod

In #87327, we patched `staticcheck` to detect deprecated "objects" from the standard library. This patch ensures that we also detect deprecated "packages".

Closes #84877

Release note: None

92859: rowcontainer: address an old TODO r=yuzefovich a=yuzefovich

This commit addresses an old TODO about figuring out why we cannot reuse the same buffer in `diskRowIterator.Row` method. The contract of that method was previously confusing - it says that the call to `Row` invalidates the row returned on the previous call; however, the important piece was missing - that the datums themselves cannot be mutated (this is what we assume elsewhere and perform only the "shallow" copies). This commit clarifies the contract of the method and explicitly explains why we need to allocate fresh byte slices (which is done via `ByteAllocator` to reduce the number of allocations).

Additional context can be found in #43145 which added this copy in the first place. Here is a relevant quote from Alfonso:
```
I think what's going on here is that this type of contract (you may only
reuse the row until the next call) is a bit unclear. `CopyRow`s of
`EncDatum`s are only implemented as shallow copies, so the reference to
this reuse only applies to the `EncDatumRow`, but not to the `encoded`
field, which is what is rewritten in this case. The `encoded` field will
not be copied, so I think the tests are probably failing due to that.
This is unfortunate and there doesn't seem to be a good reason for it.
To implement deep copies, we will have to implement deep copies for
`Datum`s as well.
```
I think we were under the impression that we'd implement the "deep copy" in `CopyRow`, but I highly doubt we'll do so given that we're mostly investing in the columnar infrastructure nowadays, and the current way of performing shallow copying has worked well long enough.

Epic: None

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>
Co-authored-by: healthy-pod <ahmad@cockroachlabs.com>

---
## [jaddison06/ocrpi](https://github.com/jaddison06/ocrpi)@[84622a2998...](https://github.com/jaddison06/ocrpi/commit/84622a2998bfa266527ab4a8b777c504c59e83eb)
#### Monday 2022-12-05 19:33:09 by James

uh oh someone is very stupid and silly!!

deleted backtraces cos the parser gives you the bloody token position

---
## [tina-mai/TwitterAPI](https://github.com/tina-mai/TwitterAPI)@[202836b0d4...](https://github.com/tina-mai/TwitterAPI/commit/202836b0d4d3e96660d26eec80b2f60f77800371)
#### Monday 2022-12-05 20:02:44 by tinamai

FINAL VERSION WHOOP WHOOP

Instructions:
- Run the RecentSearchDemo.java file
- Type in a search word (e.g. "cats")
- Give the program a few minutes to conjure up your magical graph
- Program will show a graph of the likes that the tweets with that word got across 24 hours in a day (sorted into morning, afternoon, and night); each hour is the average likes that tweets with that word got over the last 7 days

WARNING: Don't run within 5 minutes of a new hour (e.g. 1:04 –> BAD)

---
## [Jamini/Occulus-Eris](https://github.com/Jamini/Occulus-Eris)@[866a77c18d...](https://github.com/Jamini/Occulus-Eris/commit/866a77c18de6544a98b47778850864e6428be175)
#### Monday 2022-12-05 20:07:01 by MLGTASTICa

Redoes lense code , Thermal lenses no longer provide night vision. (#6607)

* initial fuckeryh

* horrible deeds

* removes explosive lenses and fix grammar

* Update stealthy and inconspicuous weapons.dm

Co-authored-by: MLGTASTICa <ak9bc01d@yahoo.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ebc0227176...](https://github.com/tgstation/tgstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Monday 2022-12-05 20:13:15 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[9499a1542b...](https://github.com/Sealed101/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Monday 2022-12-05 20:46:12 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [OwenS3881/lymantsa](https://github.com/OwenS3881/lymantsa)@[3c02ef7941...](https://github.com/OwenS3881/lymantsa/commit/3c02ef79419f0826327c408a61b4261cdc59b0eb)
#### Monday 2022-12-05 21:09:40 by OwenS3881

If anyone should see me making it down the highway
Breaking all the laws of the land
Well, don't you try to stop me, I'm going her way
And that's the way I'm sure she had it planned
Well, that's my rock-and-roll Madonna
She's always been a lady of the road
Well, everybody wants her
But no one ever gets her
But the freeway is the only way she knows
Well, if she would only slow down for a short time
I'd get to know her just before she leaves
But she's got some fascination for that two wheel combination
And I swear it's going to be the death of me
Well, that's my rock-and-roll Madonna
She's always been a lady of the road
Well, everybody wants her
But no one ever gets her
But the freeway is the only way she knows
Rock on, baby
Whoo
Yeaah, yeah
Well, that's my rock-and-roll Madonna
She's always been a lady of the road
Well, everybody wants her
But no one ever gets her
But the freeway is the only way she knows
Let's get a little bit lower
Let's get a little bit lower
Oh, you're standing alright
Single, baby? Ah, yeah, that's pretty good
Now, is everybody gonna rock on with me?
One more time
I said, that's my rock-and-roll Madonna
Aw, everybody
She's always been a lady of the road
Well, everybody wants her
But no one ever gets her
But the freeway is the only way she knows

---
## [aecyia/TheSims3](https://github.com/aecyia/TheSims3)@[f7f4cdd941...](https://github.com/aecyia/TheSims3/commit/f7f4cdd9413b6bda1b840fb333dfe6cc9275c2d4)
#### Monday 2022-12-05 21:15:50 by aecyia

 Academic Degrees

+ AcademicDegrees
	+ Business
		+ AssociatedOccupationNameEnum -- Added SportsAgent
		+ SkillsThatGrantXP -- Added Bartending,0.001; Writing,0.001; Logic,0.001
		+ Beneficial Traits -- Added BornSalesman
	+ Technology
		+ AssociatedOccupationNameEnum -- Added GameDeveloper, BotArena
		+ SkillsThatGrantXP -- Added BotBuilding,0.0083; Hacking,0.003; VideoGame,0.003
		+ Beneficial Traits -- Added ComputerWhiz, Workaholic, Brave, Daredevil, Handy, NoSenseOfHumor, Good, Eccentric, BotFan
	+ Science
		+ AssociatedOccupationNameEnum -- Added Astronomer
		+ SkillsThatGrantXP -- Added Future,0.005; Alchemy,0.005, Logic,0.005
		+ Beneficial Traits -- Added Bookworm, Perfectionist, SociallyAwkward, Perceptive
	+ Fine Arts
		+ AssociatedOccupationNameEnum -- Added ArtAppraiser
		+ SkillsThatGrantXP -- Added LaserHarp,0.005; Photography,0.005; Writing,0.005; Bartending,0.001; Dancing,0.001
		+ Beneficial Traits -- Added Rocker, PhotographersEye, Dramatic, Virtuoso, Rebellious, Bookworm
	+ Communications
		+ AssociatedOccupationNameEnum -- Added Education
		+ SkillsThatGrantXP -- Added Charisma,0.005; SocialNetworking,0.001
		+ Beneficial Traits -- Added PhotographersEye, Perceptive, Diva, Charismatic, Irresistible, Flirty
	+ PhysEd
		+ AssociatedOccupationNameEnum -- Added Criminal, SportsAgent
		+ SkillsThatGrantXP -- Added cubaDiving,0.005; Snowboarding,0.001; Windsurfing,0.001; Skating,0.001; Diving,0.001; Waterskiing,0.001
		+ Beneficial Traits -- Added Kleptomaniac, Evil, Burglar, LovesToSwim, Sailor, LovesTheOutdoors

---
## [oreillymedia/jupyter-book-to-htmlbook](https://github.com/oreillymedia/jupyter-book-to-htmlbook)@[2ed42d928b...](https://github.com/oreillymedia/jupyter-book-to-htmlbook/commit/2ed42d928bf7430897a93253e8449c404bd7c266)
#### Monday 2022-12-05 21:40:30 by Danny Elfanbuam

Refactor to better isolate `number_codeblock`

This is in part a way to get ahead for a future PR in which we'll make
numbering code blocks optional (per author request), but mostly the
logic for numbering code blocks was too entangled with if checks in the
process_code function, which is probably still a little too complex
anyway.

tl;dr: made number_codeblock stand more on its own

Slightly longer explanation:
* A hard thing to remember, but BeautifulSoup operations work "in
  place", so there is no need to really "return" the elements inside
  functions, so instead of returning the pre_block, we just modify it in
  place and return information about the cell numbering, which means we
  can...
* Move the input/output checks into the number_codeblock function
* This required the adjustment of a bunch of tests accordingly
* During which time I discovered a bug in one of the tests! Fixed that.
  Previously we were asserting that there was input when we should have
  been asserting there was output.
* Also, instead of checking the entire "result" (i.e., "chapter") in the
  tests, moved more towards asserting against _only_ the block in
  question, which is both more accurate, durable, and frankly better
  practice. Shame it took me so long to get there.

---
## [HadiCya/DemoRacing](https://github.com/HadiCya/DemoRacing)@[b4eff8754f...](https://github.com/HadiCya/DemoRacing/commit/b4eff8754f29472f89521d7ad37bcee99adf12c0)
#### Monday 2022-12-05 21:54:04 by XavusZookie

fixed the car movement

i figured out why the car wouldnt drive,
 // gameObject.GetComponentInChildren<TextMeshPro>().text = view.Owner.NickName;
this line was causing errors in the start function since were not logged into the multiplayer thing so for testing purposes i commented it out and im gonna leave it like that until we need it again just so everyone knows

i got the car moving again, i updated the car destruction function to add this cool flashing color coroutine thing and then made it so after that it makes the car drivable again. i also make a basic obstacle script that when collisions happen it causees the car to do its die animation and then destroys the obstacle just for testing, but its all set up in 2D and the games 3D so its kinda weird im not sure what were gonna do with that but for now you have to use an object with a 2d collider otherwise nothing works. i also found a really weird bug, if you hit something at an angle that would make your car spin and you dont force the car to straighten out the car just keeps a constant spin added to the car so i made the angular velocity like 10000 on the car object and it seemed like it fixed it and doesnt affect the steering at all. i also added decay to the carstats scrip in case we want to control how fast some cars slow down too passively. im gonna push now i might do more later it depends on how my school work goes.

---
## [acdlite/react](https://github.com/acdlite/react)@[b6978bc38f...](https://github.com/acdlite/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-12-05 21:54:18 by Andrew Clark

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
## [sbancuz/aoc-2022](https://github.com/sbancuz/aoc-2022)@[90996b515a...](https://github.com/sbancuz/aoc-2022/commit/90996b515a8ff40ff679b3b0cf14408ae44ac325)
#### Monday 2022-12-05 22:08:46 by sbancuz

Day5

The second solution kinda sucks, but it's too late in the evening
to worry about that :^)

Also didn't like that the input was formatted in a bad way, didn't
even try to parse it...

---
## [GoogleCloudPlatform/alloydb-auth-proxy](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy)@[e67af2b086...](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/commit/e67af2b08639f8400f796a4d19ba87a741b16697)
#### Monday 2022-12-05 23:14:01 by WhiteSource Renovate

chore(deps): update module github.com/spf13/cobra to v1.4.0 (#35)

[![WhiteSource Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Type | Update | Change |
|---|---|---|---|
| [github.com/spf13/cobra](https://togithub.com/spf13/cobra) | require | minor | `v1.2.1` -> `v1.4.0` |

---

### Release Notes

<details>
<summary>spf13/cobra</summary>

### [`v1.4.0`](https://togithub.com/spf13/cobra/releases/v1.4.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.3.0...v1.4.0)

### Winter 2022 Release ❄️

Another season, another release!

#### Goodbye viper! 🐍 🚀

The core Cobra library no longer requires Viper and all of its indirect dependencies. This means that Cobra's dependency tree has been drastically thinned! The Viper dependency was included because of the `cobra` CLI generation tool. [This tool has migrated to `spf13/cobra-cli`](https://togithub.com/spf13/cobra-cli/releases/tag/v1.3.0).

It's *pretty unlikely* you were importing and using **the bootstrapping CLI tool** as part of your application (after all, it's just a tool to get going with core `cobra`).

But if you were, replace occurrences of

    "github.com/spf13/cobra/cobra"

with

    "github.com/spf13/cobra-cli"

And in your `go.mod`, you'll want to also include this dependency:

    github.com/spf13/cobra-cli v1.3.0

Again, the maintainers *do not anticipate* this being a breaking change to users of the core `cobra` library, so minimal work should be required for users to integrate with this new release. Moreover, this means the dependency tree for your application using Cobra should no longer require dependencies that were inherited from Viper. Huzzah! 🥳

If you'd like to read more

-   issue: [https://github.com/spf13/cobra/issues/1597](https://togithub.com/spf13/cobra/issues/1597)
-   PR: [https://github.com/spf13/cobra/pull/1604](https://togithub.com/spf13/cobra/pull/1604)

#### Documentation 📝

-   Update Go Doc link and badge in README: [https://github.com/spf13/cobra/pull/1593](https://togithub.com/spf13/cobra/pull/1593)
-   Fix to install command, now targets `@latest`: [https://github.com/spf13/cobra/pull/1576](https://togithub.com/spf13/cobra/pull/1576)
-   Added MAINTAINERS file: [https://github.com/spf13/cobra/pull/1545](https://togithub.com/spf13/cobra/pull/1545)

#### Other 💭

-   Bumped license year to 2022 in golden files: [https://github.com/spf13/cobra/pull/1575](https://togithub.com/spf13/cobra/pull/1575)
-   Added Pixie to projects: [https://github.com/spf13/cobra/pull/1581](https://togithub.com/spf13/cobra/pull/1581)
-   Updated labeler for new labeling scheme: [https://github.com/spf13/cobra/pull/1613](https://togithub.com/spf13/cobra/pull/1613) & syntax fix: [https://github.com/spf13/cobra/pull/1624](https://togithub.com/spf13/cobra/pull/1624)

Shoutout to our awesome contributors helping to make this cobra release possible!!
[@&#8203;spf13](https://togithub.com/spf13) [@&#8203;marckhouzam](https://togithub.com/marckhouzam) [@&#8203;johnSchnake](https://togithub.com/johnSchnake) [@&#8203;jpmcb](https://togithub.com/jpmcb) [@&#8203;liggitt](https://togithub.com/liggitt) [@&#8203;umarcor](https://togithub.com/umarcor) [@&#8203;hiljusti](https://togithub.com/hiljusti) [@&#8203;marians](https://togithub.com/marians) [@&#8203;shyim](https://togithub.com/shyim) [@&#8203;htroisi](https://togithub.com/htroisi)

### [`v1.3.0`](https://togithub.com/spf13/cobra/releases/v1.3.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.2.1...v1.3.0)

### v1.3.0 - The Fall 2021 release 🍁

#### Completion fixes & enhancements 💇🏼

In `v1.2.0`, we introduced a new model for completions. Thanks to everyone for trying it, giving feedback, and providing numerous fixes! Continue to work with the new model as the old one (as noted in code comments) will be deprecated in a coming release.

-   `DisableFlagParsing` now triggers custom completions for flag names [#&#8203;1161](https://togithub.com/spf13/cobra/issues/1161)
-   Fixed unbound variables in bash completions causing edge case errors [#&#8203;1321](https://togithub.com/spf13/cobra/issues/1321)
-   `help` completion formatting improvements & fixes [#&#8203;1444](https://togithub.com/spf13/cobra/issues/1444)
-   All completions now follow the `help` example: short desc are now capitalized and removes extra spacing from long description [#&#8203;1455](https://togithub.com/spf13/cobra/issues/1455)
-   Typo fixes in bash & zsh completions [#&#8203;1459](https://togithub.com/spf13/cobra/issues/1459)
-   Fixed mixed tab/spaces indentation in completion scripts. Now just 4 spaces [#&#8203;1473](https://togithub.com/spf13/cobra/issues/1473)
-   Support for different bash completion options. Bash completions v2 supports descriptions and requires descriptions to be removed for `menu-complete`, `menu-complete-backward` and `insert-completions`. These descriptions are now purposefully removed in support of this model. [#&#8203;1509](https://togithub.com/spf13/cobra/issues/1509)
-   Fix for invalid shell completions when using `~/.cobra.yaml`. Log message `Using config file: ~/.cobra.yaml` now printed to stderr [#&#8203;1510](https://togithub.com/spf13/cobra/issues/1510)
-   Removes unnecessary trailing spaces from completion command descriptions [#&#8203;1520](https://togithub.com/spf13/cobra/issues/1520)
-   Option to hide default `completion` command [#&#8203;1541](https://togithub.com/spf13/cobra/issues/1541)
-   Remove `__complete` command for programs without subcommands [#&#8203;1563](https://togithub.com/spf13/cobra/issues/1563)

#### Generator changes ⚙️

Thanks to [@&#8203;spf13](https://togithub.com/spf13) for providing a number of changes to the Cobra generator tool, streamlining it for new users!

-   The Cobra generator now *won't* automatically include Viper and cleans up a number of unused imports when not using Viper.
-   The Cobra generator's default license is now `none`
-   The Cobra generator now works with Go modules
-   Documentation to reflect these changes

#### New Features ⭐

-   License can be specified by their SPDX identifiers [#&#8203;1159](https://togithub.com/spf13/cobra/issues/1159)
-   `MatchAll` allows combining several PositionalArgs to work in concert. This now allows for enabling composing `PositionalArgs` [#&#8203;896](https://togithub.com/spf13/cobra/issues/896)

#### Bug Fixes 🐛

-   Fixed multiple error message from cobra `init` boilerplates [#&#8203;1463](https://togithub.com/spf13/cobra/issues/1463) [#&#8203;1552](https://togithub.com/spf13/cobra/issues/1552) [#&#8203;1557](https://togithub.com/spf13/cobra/issues/1557)

#### Testing 👀

-   Now testing golang 1.16.x and 1.17.x in CI [#&#8203;1425](https://togithub.com/spf13/cobra/issues/1425)
-   Fix for running diff test to ignore CR for windows [#&#8203;949](https://togithub.com/spf13/cobra/issues/949)
-   Added helper functions and reduced code reproduction in `args_test` [#&#8203;1426](https://togithub.com/spf13/cobra/issues/1426)
-   Now using official `golangci-lint` github action [#&#8203;1477](https://togithub.com/spf13/cobra/issues/1477)

#### Security 🔏

-   Added GitHub dependabot [#&#8203;1427](https://togithub.com/spf13/cobra/issues/1427)
-   Now using Viper `v1.10.0`
    -   There is a known CVE in an *indirect* dependency from `viper`: [https://github.com/spf13/cobra/issues/1538](https://togithub.com/spf13/cobra/issues/1538). This will be patched in a future release

#### Documentation 📝

-   Multiple projects added to the `projects_using_cobra.md` file: [#&#8203;1377](https://togithub.com/spf13/cobra/issues/1377) [#&#8203;1501](https://togithub.com/spf13/cobra/issues/1501) [#&#8203;1454](https://togithub.com/spf13/cobra/issues/1454)
-   Removed ToC from main readme file as it is now automagically displayed by GitHub [#&#8203;1429](https://togithub.com/spf13/cobra/issues/1429)
-   Documentation correct for when the `--author` flag is specified [#&#8203;1009](https://togithub.com/spf13/cobra/issues/1009)
-   `shell_completions.md` has an easier to use snippet for copying and pasting shell completions [#&#8203;1372](https://togithub.com/spf13/cobra/issues/1372)

#### Other 💭

-   Bump version of  `cpuguy83/go-md2man` to v2.0.1 [#&#8203;1460](https://togithub.com/spf13/cobra/issues/1460)
-   Removed `lesser` typo from the GPL-2.0 license [#&#8203;880](https://togithub.com/spf13/cobra/issues/880)
-   Fixed spelling errors [#&#8203;1514](https://togithub.com/spf13/cobra/issues/1514)

*Thank you to all our amazing contributors* ⭐🐍🚀

</details>

---

### Configuration

📅 **Schedule**: At any time (no schedule defined).

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, click this checkbox.

---

This PR has been generated by [WhiteSource Renovate](https://renovate.whitesourcesoftware.com). View repository job log [here](https://app.renovatebot.com/dashboard#github/GoogleCloudPlatform/alloydb-auth-proxy).

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[cf4a194e86...](https://github.com/Paxilmaniac/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Monday 2022-12-05 23:33:38 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [AttorneyOnline/AO2-Client](https://github.com/AttorneyOnline/AO2-Client)@[1536adbf68...](https://github.com/AttorneyOnline/AO2-Client/commit/1536adbf68b3d0a0eb96b73a6edd87c58306b591)
#### Monday 2022-12-05 23:52:20 by Salanto

Fuck this SDK. Fuck Discord.

This shit is working, but C++ is so undocumented and without easy wrappers that its just more painful than it needs to be as all examples are for Unity and Unreal.

---

