## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-15](docs/good-messages/2023/2023-07-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,743,228 were push events containing 2,542,590 commit messages that amount to 166,546,303 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 68 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b7383c822b...](https://github.com/treckstar/yolo-octo-hipster/commit/b7383c822b8235649e56a8e62f3c299d4b954c5e)
#### Saturday 2023-07-15 00:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[57ef596898...](https://github.com/the-og-gear/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Saturday 2023-07-15 00:23:19 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[590bad4061...](https://github.com/toolmind/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Saturday 2023-07-15 00:36:41 by sleepynecrons

updates for landing zone sign sprites (#3180)

# About the pull request

Cleans up the palettes on the landing zone sign sprites and gives them a
fresh coat of paint (or blood). Not something most people will notice I
think but it's something I've been wanting to do.


# Explain why it's good for the game

gradients ugly


# Before and After
<details>
<summary>Click to see sprites</summary>


![osudodajs2](https://user-images.githubusercontent.com/106241650/235265980-e622b7da-8f79-4920-ba27-97d704c65550.gif)


![beforenafter](https://user-images.githubusercontent.com/106241650/235266004-0e46a574-9262-445f-98d9-4b19aa53a8fb.png)

</details>


# Changelog

:cl:
imageadd: new sprites for landing zone signs
imagedel: deleted old landing zone signs
/:cl:

---
## [TerraGS/tgstation-1](https://github.com/TerraGS/tgstation-1)@[e4ece2fbd6...](https://github.com/TerraGS/tgstation-1/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Saturday 2023-07-15 00:38:07 by Hatterhat

makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[89a2a7cc3a...](https://github.com/ATH1909/tgstation/commit/89a2a7cc3ad48032414a3755864204fed88244de)
#### Saturday 2023-07-15 00:42:07 by carlarctg

Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

---
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[c67d6a22a4...](https://github.com/ATH1909/tgstation/commit/c67d6a22a405f006a9d7a537dc35cecbdb65cfde)
#### Saturday 2023-07-15 00:42:07 by Kyle Spier-Swenson

fix stupid error message in delay pre-game (#75824)

tabbing out during init after hitting the verb, while you wait for the
server to un-lockup and present you with the prompt, and coming back in,
noticing you were too late, and cancelling out of the time prompt, only
to get told the round had already started, was kinda fucking lame. I
know, thats why i fucking hit cancel you fucking robit.

also makes the proc more early return

---
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[d01b433ab1...](https://github.com/ATH1909/tgstation/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Saturday 2023-07-15 00:42:07 by Sealed101

Fixes colossus possessor crystal cockroaches/animals not dumping the user's body upon death/gibbing (#75843)

## About The Pull Request
Hooks the stasis closet thingamajing into `COMSIG_LIVING_DEATH` instead
of checking the animal's stat on `process()`, which makes possessed
animals properly dump the stasis closet's contents upon death or gibbing
(which is death but cooler).
yeah uh this method is hilarious but it does protect the user's body
quite reliably at least lol

## Why It's Good For The Game
Fixes #75829
also probably makes cockroach death saner in some unreported way, this
`. = ..()` vs `..()` is above my non-existent paygrade but it keeps
popping up from time to time

## Changelog
:cl:
fix: gibbing colossus possessor crystal possessed animals will no longer
stick the user's body and their stuff into the shadow realm. the animals
will properly drop your corpse when killed or gibbed
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Stalkeros2/tgstation](https://github.com/Stalkeros2/tgstation)@[2aaafd9a67...](https://github.com/Stalkeros2/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Saturday 2023-07-15 00:43:04 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [axietheaxolotl/Skyrat-tg](https://github.com/axietheaxolotl/Skyrat-tg)@[79febdf95d...](https://github.com/axietheaxolotl/Skyrat-tg/commit/79febdf95dbcdb81d6a8027dc21deba19f8e659e)
#### Saturday 2023-07-15 00:46:12 by SkyratBot

[MIRROR] New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request

https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.

![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [AdamWill/nikola](https://github.com/AdamWill/nikola)@[50420559fa...](https://github.com/AdamWill/nikola/commit/50420559fa375a35afde860fb32ab3fe7412f279)
#### Saturday 2023-07-15 00:51:18 by Adam Williamson

Handle change to plugin loading in recent yapsy (#3700)

https://github.com/tibonihoo/yapsy/pull/11 changes yapsy plugin
loading to not use the deprecated imp module any more. However,
as a side effect of that, it breaks this already-kinda-ugly
hack, and we have to make it even uglier!

yapsy used to import the module like this:

imp.load_module(plugin_module_name,plugin_file...)

where `plugin_module_name` was the modified, "unique" name it
creates early in `loadPlugins`. Interestingly, when you import
a module like that, it gets added to `sys.modules` under *both*
the modified name and its 'real' name, viz:

>>> import sys
>>> import imp
>>> imp.load_module("someothername", None, "/usr/lib/python3.12/site-packages/yapsy/__init__.py", ("py", "r", imp.PKG_DIRECTORY))
<module 'someothername' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>
>>> sys.modules["someothername"]
<module 'someothername' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>
>>> sys.modules["yapsy"]
<module 'yapsy' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>

That's why this hack worked. However, now yapsy imports the
module using importlib, then adds it to `sys.modules` itself,
*only* under the modified "unique" name, not under its original
name. So sys.modules["unmodifiedpluginname"] is now a KeyError.

I can't think of a less ugly fix than this, unfortunately. We
*could* try sending a patch for yapsy to add it under both the
modified and unmodified names, but that would be somewhat tricky
in yapsy's design, and I also suspect yapsy would consider it
to actually be unwanted behavior.

Maybe what we really need is to send a patch for yapsy to just
provide an interface to find a plugin's filesystem path...

Signed-off-by: Adam Williamson <awilliam@redhat.com>

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[b304b6523f...](https://github.com/DesmontTiney/tgstation/commit/b304b6523fa1f497800c8ba3818e4d2c01d4eaf4)
#### Saturday 2023-07-15 01:08:24 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

## About The Pull Request

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.


## Why It's Good For The Game

IMPROVES my workflow

## Changelog
:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[52c8da7ea4...](https://github.com/tgstation/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Saturday 2023-07-15 01:10:36 by Jacquerel

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
## [ExcessiveUseOfCobblestone/tgstation](https://github.com/ExcessiveUseOfCobblestone/tgstation)@[835952ccf4...](https://github.com/ExcessiveUseOfCobblestone/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Saturday 2023-07-15 01:18:02 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

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

---
## [VasilevAY/tgstation](https://github.com/VasilevAY/tgstation)@[c5dce84be8...](https://github.com/VasilevAY/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Saturday 2023-07-15 01:20:11 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

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

---
## [VasilevAY/tgstation](https://github.com/VasilevAY/tgstation)@[1674f25725...](https://github.com/VasilevAY/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Saturday 2023-07-15 01:20:11 by John Willard

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
## [EricZilla/tgstation](https://github.com/EricZilla/tgstation)@[1b5c0489a4...](https://github.com/EricZilla/tgstation/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Saturday 2023-07-15 01:26:41 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [EricZilla/tgstation](https://github.com/EricZilla/tgstation)@[f2fd69a49a...](https://github.com/EricZilla/tgstation/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Saturday 2023-07-15 01:26:41 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[0cd356125a...](https://github.com/Higgin/Skyrat-tg/commit/0cd356125ad5f6e144a18f9da586699a94dd154a)
#### Saturday 2023-07-15 01:27:59 by SkyratBot

[MIRROR] Fixes a sneaky antag tell with RDS / adds policy support [MDB IGNORE] (#21881)

* Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

* Fixes a sneaky antag tell with RDS / adds policy support

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Nanotrasen-Spy/cmss13-funnies](https://github.com/Nanotrasen-Spy/cmss13-funnies)@[2baaba2746...](https://github.com/Nanotrasen-Spy/cmss13-funnies/commit/2baaba27468b20016d2095edfbdba26658935ddc)
#### Saturday 2023-07-15 01:28:33 by Hopekz

Adds medic clothing racks to WO (#3313)

God damn this is so frustrating every time I play WO as a medic


![dreamseeker_ZXt55sth9R](https://github.com/cmss13-devs/cmss13/assets/24533979/252773e1-fec0-4bec-a1a5-0ccb63547781)


![dreamseeker_UiolotzaIV](https://github.com/cmss13-devs/cmss13/assets/24533979/a241ee86-f2ea-490f-91c7-7b1a90e9734f)


:cl: Hopek
add: Medics finally get medic clothing racks on WO
/:cl:

---
## [Pumpkinoe/tgstation](https://github.com/Pumpkinoe/tgstation)@[912e843f53...](https://github.com/Pumpkinoe/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Saturday 2023-07-15 01:45:23 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [Pumpkinoe/tgstation](https://github.com/Pumpkinoe/tgstation)@[f7a49c4068...](https://github.com/Pumpkinoe/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Saturday 2023-07-15 01:45:23 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Autisem/tgstation](https://github.com/Autisem/tgstation)@[bc22fefe3b...](https://github.com/Autisem/tgstation/commit/bc22fefe3b1de4d882dd87a5492344672230736d)
#### Saturday 2023-07-15 01:50:47 by Helg2

Adds proper armor for security plasmamen. (#75156)

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

---
## [Autisem/tgstation](https://github.com/Autisem/tgstation)@[2845c985fa...](https://github.com/Autisem/tgstation/commit/2845c985fab04b0de1f7615799a260527af30822)
#### Saturday 2023-07-15 01:50:47 by Rhials

Adds a revolutionary conversion stinger (#75002)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.

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
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[d1d23352eb...](https://github.com/ghostsheet/cmss13/commit/d1d23352eb41452a98d0c66c7fbf5c5ea4143ffe)
#### Saturday 2023-07-15 01:57:57 by fira

Reduces SG Full Auto Scatter (#3556)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

It's been bugging me for a long time, but when you fire for a good dozen
seconds with the standard issue smartguns, the bullets start scattering.
So, so far you'll say, good Fira, that's soulful!

However, we have no ACTUAL recoil or similar mechanic. So letting go of
the LMB for just even 20 miliseconds is enough to reset scatter to start
of firing. **It's just a noobtrap with zero real gameplay elements.**

This reduces the max scatter so that bullets don't just start (after
EIGHTY shots!) spraying a (roughly) 48° angle cone, but instead 12°
which mostly stays on the same actual turfs. At this value the targeting
impact is vastly minimized, but the projectile visuals retain
significant scattering.

I don't think this ACTUALLY qualifies as a "balance" change due to how
irrelevant the "mechanic" was, but i'll slap it on.

# Explain why it's good for the game
Less of a noobtrap and pointless purely mechanical micromanagement so
people can focus on playing the game.

I'd rather we get a recoil mechanic to make this meaningful but it's bit
of a bigger problem...

# Changelog
:cl:
qol: Reduced USCM SG max scattering on Full Auto fire so you don't have
to periodically let go of the fire button to keep it from firing way
wide.
/:cl:

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[2ee79d7077...](https://github.com/DATA-xPUNGED/DataStation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Saturday 2023-07-15 01:59:18 by Jacquerel

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[4537b1e980...](https://github.com/Sonic121x/Skyrat-tg/commit/4537b1e980f226f2f6a18ef1c92d6ffc3e3b6ac4)
#### Saturday 2023-07-15 02:01:51 by Bloop

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
## [AlekEagle/cumulonimbus-frontend](https://github.com/AlekEagle/cumulonimbus-frontend)@[fe033c85b6...](https://github.com/AlekEagle/cumulonimbus-frontend/commit/fe033c85b6bda06e3b56953e4163e17596b16d59)
#### Saturday 2023-07-15 02:10:54 by kadix

fuck you discord

changed kadix#0787 to the stupid discord username bullshit @piss.industries
i hate discord

---
## [z0nek/NOrmalSHAPRD](https://github.com/z0nek/NOrmalSHAPRD)@[27ce47c3da...](https://github.com/z0nek/NOrmalSHAPRD/commit/27ce47c3da9e39f4154a4dd1e1dfd5a7d4aa4821)
#### Saturday 2023-07-15 02:17:05 by echo

dude im so sorry if it pings you

every time i make a commit :sob: 
also FUCK YOU GITHUB BOT

---
## [jnutt367/proverbs](https://github.com/jnutt367/proverbs)@[86a6ebcac4...](https://github.com/jnutt367/proverbs/commit/86a6ebcac4384e0c86d251c4469d638921166c4a)
#### Saturday 2023-07-15 02:20:27 by Jason Nutt (He/Him) Christian Developer/Creator

Add files via upload

Oppression, Toil, Friendlessness
4 Again I looked and saw all the oppression that was taking place under the sun:

I saw the tears of the oppressed—
    and they have no comforter;
power was on the side of their oppressors—
    and they have no comforter.
2 And I declared that the dead,
    who had already died,
are happier than the living,
    who are still alive.
3 But better than both
    is the one who has never been born,
who has not seen the evil
    that is done under the sun.

4 And I saw that all toil and all achievement spring from one person’s envy of another. This too is meaningless, a chasing after the wind.

5 Fools fold their hands
    and ruin themselves.
6 Better one handful with tranquillity
    than two handfuls with toil
    and chasing after the wind.

7 Again I saw something meaningless under the sun:

8 There was a man all alone;
    he had neither son nor brother.
There was no end to his toil,
    yet his eyes were not content with his wealth.
“For whom am I toiling,” he asked,
    “and why am I depriving myself of enjoyment?”
This too is meaningless—
    a miserable business!

9 Two are better than one,
    because they have a good return for their labor:
10 If either of them falls down,
    one can help the other up.
But pity anyone who falls
    and has no one to help them up.
11 Also, if two lie down together, they will keep warm.
    But how can one keep warm alone?
12 Though one may be overpowered,
    two can defend themselves.
A cord of three strands is not quickly broken.

Advancement Is Meaningless
13 Better a poor but wise youth than an old but foolish king who no longer knows how to heed a warning. 14 The youth may have come from prison to the kingship, or he may have been born in poverty within his kingdom. 15 I saw that all who lived and walked under the sun followed the youth, the king’s successor. 16 There was no end to all the people who were before them. But those who came later were not pleased with the successor. This too is meaningless, a chasing after the wind.

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[3a83dc49ea...](https://github.com/vdaular-dev/linksfordevs/commit/3a83dc49eaef2ed744b3bbfa53b8bc8968cf8333)
#### Saturday 2023-07-15 03:27:31 by Ben Dornis

Updating: 7/14/2023 9:00:00 PM

 1. Added: Syncfusion Updates Flagship Solution with Goodies for Blazor, .NET MAUI, More -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/07/14/syncfusion-vol-2-2023.aspx)
 2. Added: tinygrad + rusticl + aco: why not?
    (https://airlied.blogspot.com/2023/07/tinygrad-rusticl-aco-why-not.html)
 3. Added: The Problem With LangChain | Max Woolf's Blog
    (https://minimaxir.com/2023/07/langchain-problem/)
 4. Added: The Day FedEx Delivered Its Promise
    (https://www.anaeo.com/fedex/)
 5. Added: Masters and Fools - Privie
    (https://privie.com/masters-and-fools/)
 6. Added: The MS Office for your personal life. – alen.ro
    (https://alen.ro/notes/the-ms-office-for-your-personal-life/)
 7. Added: The Right to Sex: Feminism in the Twenty-First Century
    (https://ahalbert.com/reviews/2023/07/14/the_right_to_sex.html)
 8. Added: On Personal Relations As A Manager
    (https://fev.al/posts/personal-relations/)
 9. Added: Read-only web apps
    (https://adactio.com/journal/20113)
10. Added: Achieving Consistent Output from ChatGPT | Logan
    (https://logana.dev/blog/achieving-consistent-output-from-chatgpt)
11. Added: An overview of how stateful monitoring can accelerate debugging
    (https://notes.drdroid.io/stateful-monitoring-to-accelerate-debugging)
12. Added: Schedule periodic database clean-up on Laravel | Leonardo Poletto
    (https://leopoletto.com/schedule-periodic-database-clean-up-on-laravel/)
13. Added: Mixing GitLab personal and work accounts: Enterprise Users - ClickedyClick
    (https://gergely.imreh.net/blog/2023/07/mixing-gitlab-personal-and-work-accounts-enterprise-users/)
14. Added: Scientific Computing with F# | fsharpConf 2023
    (https://youtube.com/watch?v=ssvz6kdM4X8)
15. Added: Position-Driven Styles
    (https://kizu.dev/position-driven-styles/)
16. Added: My thoughts on my first 5 weeks of being a PM
    (https://blog.cyrusroshan.com/post/first-weeks-being-pm)
17. Added: Deep GUIs
    (https://mlecauchois.github.io/posts/deep-gui/)
18. Added: Words & Laws 📚
    (https://www.joshualiu.org/blog/words-and-laws)
19. Added: Make The Machines Remember You. Make Them Give You Superpowers
    (https://deanpeterson.us/make-your-ai-guide-remember-you/)

Generation took: 00:09:49.6005634
 Maintenance update - cleaning up homepage and feed

---
## [malabyte/Business-Analytics](https://github.com/malabyte/Business-Analytics)@[f3a6aeb904...](https://github.com/malabyte/Business-Analytics/commit/f3a6aeb9044e61b5ac17db60ab6553ecd3eeb414)
#### Saturday 2023-07-15 04:30:43 by malabyte

 Caloric Needs Analyzer: Personalized Weight Loss Recommendation Tool

The code represents a calorie calculator that calculates the suggested daily caloric intake for weight loss based on user input regarding age, height, weight, gender, and activity level.

The main() function serves as the entry point for the program. It starts by defining constant variables for the minimum and maximum values allowed for age, height, weight, and the valid gender options.

The user is presented with a title and prompted to enter their age in years. The input is validated to ensure it falls within the acceptable age range (1 to 100). If the input is invalid, an exception is raised and the program exits.

Next, the user is asked to input their height in inches. Similarly, the input is validated to ensure it falls within the acceptable height range (10 to 100). If the input is invalid, an exception is raised and the program exits.

The user is then prompted to enter their weight in pounds. Again, the input is validated to ensure it falls within the acceptable weight range (10 to 500). If the input is invalid, an exception is raised and the program exits.

After that, the user is asked to enter their gender, either 'M' for male calculation or 'W' for female calculation. The input is validated to ensure it matches one of the valid options. If an invalid gender is entered, a ValueError exception is raised, and the program exits.

Based on the gender input, the program calculates the Basal Metabolic Rate (BMR) using the appropriate formulas. For males, the Mifflin-St Jeor equation is used, and for females, a slightly different equation is used. The calculated BMR is stored in the bmr variable.

The user is then presented with activity level options ranging from 'A' to 'D', representing different levels of physical activity. The user is prompted to select one of these options. The selected activity level is used to calculate an activity percentage, which will be used to adjust the BMR calculation. The activity percentages are predefined values for different activity levels.

Using the calculated BMR and the activity percentage, the program determines the suggested daily caloric intake for weight loss. It multiplies the BMR by the activity percentage and subtracts 500 calories to create a calorie deficit for weight loss. The result is stored in the calories_for_weight_loss variable.

Finally, the program prints the calculation result, which includes the suggested daily caloric intake for weight loss. It provides a formatted message indicating the gender, measurements, and the recommended caloric intake to lose approximately 1 pound per week. A thank you message is printed, concluding the program.

This calorie calculator helps individuals estimate their daily caloric needs for weight loss based on their specific measurements and activity levels, providing a starting point for creating a calorie deficit and achieving their weight loss goals.

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[94b32aa82c...](https://github.com/cdb-is-not-good/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Saturday 2023-07-15 04:37:36 by CDB

Bugfixes. (#4685)

* Bugfixes.

Fixes a few spelling mistakes here and there.

Forged stock-parts boxes claimed they had five parts inside. they did not, they have four, corrected.

Toga for the church had an eronious base-state, unsure who touched it, but fix'd.

Bat'ko had incorrect formatting for its on-suit sprite, fixed.

Numerical garb eroniously claimed to be switchable between grey and red. It was actually purple and red, fixed.

Numerical hats both had the wrong icon name and were using(incorrectly) the old sprites. Fixed.

Duty had a missing icon when loaded with a drum and fempty(Who the FUCK let the duty take drums?)

Fixes the sec-shuttle and also comments out the destination it has towards the space fortress which is...commented back out? Right?

Fixes the apparent sec-shuttle so its walls are properly named after the vessel. To do- give some fucking flavor to the Rocinante and Vasiliy.

* Update body_modifications.dm

Removes the ability to select robo-torsos/groins/heads, this functionality doesn't actually work as intended and wasn't intended to be used in this way. Feel free to re-add if it does get fixed.
fixes #4675

* More bugfixes

Fixes tesla turrets attacking colony bots, SI drones, etc.

Fixes embed chance on the psion knife being greater than 0 and thus being able to embed(and promptly bugging out.)

* Update tesla_turret.dm

Slight tweak to Tesla turret code courtesy of Hex.

* Further bugfixes.

RXbow lacked a proper caliber and could thusly accept 10mm rounds.

RXbow also lacked a casing handling tag, not that it makes a huge difference given its snowflake behavior but it was fixed.  I will suggest to perhaps raise the d amage of the crossbow bolt in another non-bug focused PR.

Artificer rail pistols(slab and myrmidon) didn't have a serial defined, fixed.

* More fixes.

Mop bucket now properly updates its sprite after any change to its reagents takes place.

Kitchen spike no longer erroneously requires a strangle grab instead of a neck_grab.

---
## [g-liu/universal_paperclips](https://github.com/g-liu/universal_paperclips)@[f2a1b1d2d2...](https://github.com/g-liu/universal_paperclips/commit/f2a1b1d2d213b09e854e93624c5581ad7e0cca2a)
#### Saturday 2023-07-15 06:17:50 by Geoffrey Liu

Microsoft Edge, go and get BENT.

QUIT FUCKING SAVING MY FILES IN FUCKING DOWNLOADS

IF I AM FUCKING EDITING MY SHIT AND PRESS SAVE I EXPECT THE **ORIGINAL** **MOTHERFUCKING** **FILE** TO BE SAVED

NOT TO SOME DIPSHIT RANDOM ASS FOLDER IN DOWNLOADS DO YOU FKCING UNDERSTAND?????????????????

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[5f5fcd2b27...](https://github.com/Nanu308/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Saturday 2023-07-15 08:08:57 by Drathek

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
## [edgeble/kernel](https://github.com/edgeble/kernel)@[a06a4dc3a0...](https://github.com/edgeble/kernel/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Saturday 2023-07-15 10:10:05 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [ClementWalter/kakarot-rpc](https://github.com/ClementWalter/kakarot-rpc)@[12ae76a648...](https://github.com/ClementWalter/kakarot-rpc/commit/12ae76a64831f8ef84a4ebd9635deed4b5292eab)
#### Saturday 2023-07-15 10:20:07 by johann bestowrous

changes to allow usage `forge create` and `cast` (#295)

* smol changes to line up using `forge create` and `cast`

* revise test with tragic default

* say the holy word 'todo' that allows us to forgive our hacks

* some? vec? vec?

---------

Co-authored-by: johann makram salib bestowrous <jmsb@johanns-MBP.lan>

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[1468797059...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Saturday 2023-07-15 10:38:44 by TheObserver-sys

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
## [titli0/titli0](https://github.com/titli0/titli0)@[54711c74f6...](https://github.com/titli0/titli0/commit/54711c74f6f907dc74ee2cf790714e3c5ac12d02)
#### Saturday 2023-07-15 11:07:56 by titli0

Create titli

Titli Episode
Introduction to Titli Episode
In recent years, television shows have become a significant part of our lives, offering entertainment and captivating storytelling. One such show that has garnered attention and popularity is "Titli Episode." This article delves into the world of Titli Episode, exploring its plot, characters, impact, and themes, while also analyzing its success and discussing its future.
The Plot of Titli Episode
Titli Episode revolves around the life of Titli, a young woman who embarks on a journey of self-discovery and empowerment. Set in a small town, the story follows Titli as she confronts societal norms, gender biases, and personal challenges. Through her struggles and triumphs, the audience witnesses her growth and transformation, making it a relatable and inspiring narrative.
Main Characters in Titli Episode
The show boasts a diverse and well-developed cast of characters. Titli, the protagonist, is a determined and resilient individual who captures the viewers' hearts with her authenticity and relatability. Alongside Titli, we encounter a range of supporting characters, each contributing to the show's depth and intrigue. From her supportive friends to the antagonistic figures that test her strength, the ensemble cast adds layers to the storytelling, making Titli Episode an engrossing watch.
Impact and Reception of Titli Episode
Since its premiere, Titli Episode has made a significant impact on its audience. Viewers have praised the show for its realistic portrayal of societal issues and its ability to spark meaningful conversations. The relatable characters and engaging storyline have resonated with viewers of different age groups and backgrounds. Furthermore, the show's success can be attributed to its compelling narrative, impressive performances, and well-crafted production values.
Analysis of Key Themes in Titli Episode
Titli Episode explores several key themes that are relevant and thought-provoking. One of the central themes is female empowerment and breaking stereotypes. Through Titli's journey, the show challenges traditional gender roles and sheds light on the struggles faced by women in society. Additionally, the series addresses themes of identity, love, friendship, and the pursuit of dreams, creating a multi-dimensional narrative that keeps the audience emotionally invested.
Comparison with Other TV Shows
When comparing Titli Today Episode with other TV shows, its unique storytelling and relatable characters set it apart. Unlike many mainstream shows that rely on clichés and predictable plotlines, Titli Episode stands out for its fresh approach and genuine storytelling. It offers a realistic portrayal of life's complexities and the challenges individuals face in their personal and social lives. This authenticity has resonated with viewers, distinguishing it from other shows in the same genre.
Exploring the Success of Titli Episode
The success of Titli Episode can be attributed to various factors. Its strong writing, compelling performances, and attention to detail have contributed to its popularity. Moreover, the show's ability to connect with the audience on an emotional level has played a significant role in its success. The relatability of the characters and the exploration of relevant themes have captivated viewers, resulting in a dedicated fan base and positive word-of-mouth promotion.
The Future of Titli Episode
As Titli Episode continues to captivate audiences, its future looks promising. The show's ability to balance entertainment with social relevance has earned it a special place in the hearts of viewers. With its impactful storytelling and compelling characters, Titli Episode is poised to continue its success and inspire more meaningful conversations. The future seasons hold the potential for further character development and exploration of new themes, ensuring that Titli Episode remains a must-watch for television enthusiasts.
Conclusion
In conclusion, Titli Watch Online has emerged as a powerful and engaging TV show that tackles important societal issues while delivering compelling storytelling. Its relatable characters, thought-provoking themes, and impactful narrative have made it a fan favorite. With its success and potential for further growth, Titli Episode has secured its position as a significant contribution to the television landscape.
https://titlii.net/

---
## [HendricksK/sacosbego](https://github.com/HendricksK/sacosbego)@[090465e820...](https://github.com/HendricksK/sacosbego/commit/090465e820bb24f64d0c924b9a3d3dbb357c5366)
#### Saturday 2023-07-15 11:58:52 by HendricksK

trying to get data based on json tags, but need to stop now because of fucking loadshedding, fuck you eskom

---
## [thsilvadev/MTGCollector](https://github.com/thsilvadev/MTGCollector)@[39a9decaae...](https://github.com/thsilvadev/MTGCollector/commit/39a9decaaec0abb920dbb0352aa48b72fdf34880)
#### Saturday 2023-07-15 12:52:30 by thiagosauro

A long 'madrugada' session. Did much

1) Basically created collectionController.js, project is off to expanding. Now we have Collection page and after so much time and pain, it's working! The page shows all cards from 'collection' table. Post is working as well - frontend-wise, it's on Card.js

2) some job on routes.js
3) some CSS improvements on Search Container flex etc; managed to come up with a solution for info badge => double border. When user selects a color AND types, color gets double selected (black and orange for now), live in real time, so upon clicking or typing user gets feedback of funcionality change.
4) about that functionality change, I inverted it too: now when typing it will show only `B,G,R,U,W` and when not typing, it will show `B`, `G`, `R`, `U`, `W` as well.
5) Opened/Closed chest [Home.js Image Switcher] , better logo, did hours of photoshopping to get some magic going on.
6) Great night of studying, practiced both backend and frontend while learning fundalmentals, methods and syntaxes on the go.

---
## [ChSatyaSavith/LeetCode](https://github.com/ChSatyaSavith/LeetCode)@[2829605639...](https://github.com/ChSatyaSavith/LeetCode/commit/2829605639262310e89cbb39d5ee4f27c785cdf5)
#### Saturday 2023-07-15 13:11:02 by NotFluent

DP FUCKS WITH MY BRAIN HOLY FUCK, AGAIN FOR THE NTH TIME, I HAVE TO FUCKING PRACTICE DP OR IM FUCKED AS SHIT, HOOOOOLYYYYYYYY

---
## [luzpaz/MITK](https://github.com/luzpaz/MITK)@[9b7f10378d...](https://github.com/luzpaz/MITK/commit/9b7f10378dfee806b422269e3ac418d13fc964e5)
#### Saturday 2023-07-15 14:11:21 by Stefan Dinkelacker

v2022.10

NOTE: This is a release changelog. It is composed of a selected short list of highlights since the last release [[mitk/changelog/release-v2022.04 | MITK v2022.04]] - split into dedicated user and developer sections. See the past four [[mitk/changelog | changelogs]] starting from [[mitk/changelog/2022.28]] for a comprehensive, developer-centric overview of changes.

---

= News for MITK Workbench users =

For MITK v2022.10, we focused mainly on segmentation again and we are already excited about your feedback on many improvements and a streamlined segmentation workflow.

== Segmentation ==

- New segmentation tools
  - The GrowCut tool is a semi-automatic 3-d tool based on rough and sparse paint strokes of foreground and background
  - The Lasso tool is a mixed polygonal and free-hand drawing tool with refinement options for corner points
  - The Close tool fills all holes of a connected label region
- Improved intuitive behavior of Fill and Erase tools
- Improved performance of Paint and Wipe tools
- Improved many segmentation tools regarding different labels, layers, time steps, and undo/redo behavior.
- Improved dialog window for creating or renaming labels
  - Name suggestions are now listed in a separate list
  - The position and size of the dialog window is now preserved
  - Double-click on suggested names to immediately select and apply name and color
- Introduced new keyboard shortcuts for frequent actions. The shortcuts are key sequences of two keys each while the Ctrl key is pressed. First you press Ctrl+L (for label) and then Ctrl+<key> for the label action you want to execute:
  - Ctrl+L, N: New Label
  - Ctrl+L, R: Rename label (also: Alt + double click)
  - Ctrl+L, I: Iterate (read: select next label)
- The user experience with the experimental, fully automatic, AI-based nnU-Net tool (only available on Linux) was improved

== General ==

- Improved first-time user experience by showing the View Navigator by default and introducing optional tips to the Welcome page, e. g. a mouse navigation primer and how to change image contrast with the level window
- High-quality remeshing is back, based on the // Approximated Centroidal Voronoi Diagrams (ACVD)// algorithm
- The pixel value information moved from the status bar to a dedicated plugin, also showing the name of the image of the queried pixel value
- RAM usage is now reported more accurate on Linux and macOS
- DICOM images with non-ASCII characters in filenames can now be loaded on Windows without any workarounds
- Introduced the [[https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html | Turbo colormap]] - a rainbow colormap with exceptional homogeneity along its color gradient

== Minimum required version of Ubuntu and Windows ==

- We dropped support of Ubuntu 18.04. The minimum required version has been raised to Ubuntu 20.04
- The minimum required version of Windows is now Windows 10 version 1903

== 💔 Known issues ==

- The label highlight in the Segmentation View may get out of sync with the actual active label when changing the lock or visibility state of other labels. Workaround: Explicitly select the active label after changing visibility or lock states of other labels.
- Registration Evaluator's swipe mode: When using the swipe mode to inspect the registration results, the swipe rendering is always one interaction //behind//. So it will be rendered with the position you clicked before the current crosshair position.

---

= News for developers =

Most of our work in the backend besides many fixes and improvements for the segmentation was dedicated to an ongoing clean-up and modernization effort as well as a general upgrade of our third-party dependencies.

== MITK extensions ==

Doxygen now also parses MITK extension directories, allowing you to easily write and publish documentation and manuals for your extensions

== 💔 Known issues ==

- Building MITK with Qt 5.15 on macOS results in a cursor offset during interaction with the render windows, for example with segmentation tools. Workaround: Build MITK with Qt 5.12.

== 🛠 Third-party dependency changes ==

NOTE: [[https://docs.mitk.org/2022.10/SupportedPlatformsPage.html | Here]] is the [[https://docs.mitk.org/2022.10/SupportedPlatformsPage.html | list of supported platforms]] for MITK v2022.10.

The following table shows a complete list of changed third-party dependencies. Notable changes are:

- We changed the download method of nearly all third-party dependencies from archive downloads to Git clones
- We reverted the interim OpenMesh dependency to a recent version of ACVD, which is compatible with VTK 9 now
- We replaced JsonCpp with JSON for Modern C++

| Dependency | Old version | New version |
| --- | --- | --- |
| ACVD |  | `e583e278` (Jun 27, 2022) |
| Boost | 1.78 beta | 1.80 |
| C++ REST SDK | 2.10.16 | 2.10.18 |
| CTK | `7210c5bc` (Nov 8, 2020) | `ec816cbb` (May 17, 2022) |
| DCMTK | 3.6.6 | 3.6.7 |
| GDCM | 3.0.10 | 3.0.14 |
| ~~JsonCpp~~ | 1.9.5 | |
| JSON for Modern C++ | | 3.10.5 |
| MatchPoint | `f7699d1e` (Apr 20, 2021) | `e63dfdbb` (Apr 5, 2022) |
| OpenCV | 3.4.16 | 4.6.0 |
| OpenIGTLink | 3.0.0 | `d4eaae93` (Aug 2, 2022) |
| ~~OpenMesh~~ | 8.1 |  |
| Poco | 1.9.0 | 1.12.2 |
| Qwt | 6.1.5 | 6.2.0 |
| SWIG | 3.0.2 | 4.0.2 |

== 🔥 API-breaking changes ==

For now, we discontinued the extensive listing of API-breaking changes as the vast majority of them are straight forward to resolve or do not affect the absolute majority of developers at all. The ratio between the time and effort spent for writing these reports and actual developer feedback turned out to be greatly imbalanced.

Complex or critical API changes will still be accompanied by migration guides.

In case you experience any trouble while migrating to the newest version of MITK, please do not hesitate to [[https://www.mitk.org/wiki/MITK_Mailinglist | contact us]].

---
## [luzpaz/MITK](https://github.com/luzpaz/MITK)@[4e833c5d98...](https://github.com/luzpaz/MITK/commit/4e833c5d98792ed3e3769ea03a6ca0a2b5e4ff65)
#### Saturday 2023-07-15 14:11:21 by Stefan Dinkelacker

2022 Week 43 (Late October)

The following - possibly updated - changelog can be viewed as formatted
article at https://phabricator.mitk.org/w/mitk/changelog/2022.43/.

= 🛠 Third-party dependency changes =

//none//

= ✨ New features =

- Segmentation
  - New GrowCut tool for semi-automatic segmentations
  - Position and size of the New/Rename Label dialog is preserved now
  - New additional shortcut for renaming labels: {key ALT} + double click
  - Improved UI of several tools
- Pixel value information moved from the status bar into a new dedicated Pixel Value plugin
- New "Tip of the Day" feature in the Welcome page
- View Navigator is shown by default now
- Increased initial window size of the workbench
- Improved themed icon of the standard display editor
- New [[https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html | Turbo colormap]]

= 🐛 Bugfixes =

- Segmentation
  - Fixed invalid states of the Segmentation View GUI for certain selection scenarios
  - Fixed wrong label access of several tools regarding time steps and layers
  - Fixed undo/redo behavior of paintbrush tools
  - Fixed a crash in nnU-Net tool when download of pretrained models is immediately stopped
  - "Show only selected nodes" preference is applied immediately now
- Extreme level window ranges do no longer result in crashes
- Fixed a crash when loading MITK scene files with empty data
- Fixed an issue in the data storage backend where predicates were ignored in certain cases
- Welcome and Help pages are also shown on Ubuntu 22.04 now
- Fixed wrong RAM usage reports on Linux and macOS
- Fixed partially hidden OK button in selection dialog
- Fixed {key F1} help access to View Navigator

= 🔥 API-breaking changes =

In an ongoing cleanup effort, many deprecated or unused classes, methods, and other code snippets were removed or refactored. Migration should be straight forward if necessary at all.

In case you experience any trouble while doing so, please do not hesitate to [[https://www.mitk.org/wiki/MITK_Mailinglist | contact us]].

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[d26452bb9a...](https://github.com/ghostsheet/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Saturday 2023-07-15 14:23:24 by Unknownity

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
## [Ansekishokuu/tgstation](https://github.com/Ansekishokuu/tgstation)@[59dd02fe7c...](https://github.com/Ansekishokuu/tgstation/commit/59dd02fe7cd54b4153b294ccb965249c587f189d)
#### Saturday 2023-07-15 14:55:52 by san7890

Welding Fuel Tanks now log_bomber when hit by projectile (#75885)

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cfd40aeef5...](https://github.com/tgstation/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Saturday 2023-07-15 15:27:41 by necromanceranne

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
## [Sonic-Geared/RSDK-VT](https://github.com/Sonic-Geared/RSDK-VT)@[3828439e25...](https://github.com/Sonic-Geared/RSDK-VT/commit/3828439e25321546f02e9cfe4e18532d5e034069)
#### Saturday 2023-07-15 15:56:08 by Geared

fuck you, T.

seriously i'm going to murder those autobuilds if they fail one more time

---
## [0zuzu/nexus-corp](https://github.com/0zuzu/nexus-corp)@[d11b307f00...](https://github.com/0zuzu/nexus-corp/commit/d11b307f003030d93c878504071219342c33f4af)
#### Saturday 2023-07-15 16:03:10 by 0zuzu

Add files via upload

FUCK YOU GITHUB FUCKING WORK YOU PIECE OF SHIT

---
## [silverplatedelta/ParadiseSilver](https://github.com/silverplatedelta/ParadiseSilver)@[a3dc32cf34...](https://github.com/silverplatedelta/ParadiseSilver/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Saturday 2023-07-15 16:13:02 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[ce818246c1...](https://github.com/LC4492/CM-Space-Station-13/commit/ce818246c107cf97525a05f6f3a66e120117b8c3)
#### Saturday 2023-07-15 16:18:34 by QuickLode

The Hazmat Joe (#3259)

# About the pull request
This pull request resprites the entire Working Joe from toes to head. It
also gives two additional uniforms which are meant for hazardous use,
and this PR should act as a foundation for future implementation of the
Hazmat Joe into CM's gameplay. Additionally, I may just set this to
draft and let it be reviewed while I work on the actual implementation.

They are complete with distinctive loadouts, which focus more on
hazardous situations, repair, and firefighting. Though may tweak things
depending on how its implemented.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This adds a fan favorite variation of your inexpensive, reliable friend!
You've seen him in quite a few places, and now he's coming to CM!

Also, the resprite of the Joe fixes up some minor sprite issues that
were encountered on previous models.

More content, more roleplay possibilities! ARES! Get me some Joes to put
that reactor fire out ASAP!
# Testing Photographs and Procedure

https://cdn.discordapp.com/attachments/490668342357786645/1104748917398175795/image.png

https://media.discordapp.net/attachments/490668342357786645/1105643891107049572/image.png
Ran several tests and they went well.


# Changelog
:cl:QuickLoad,Frans_Feiffer,nauticall
add: Adds The Hazmat Joe with two minor variations. This is a Working
Joe equipped to handle hazardous situations, dangerous repairs and
firefighting! They are complete with their own gear, tasks, job and
purpose. Forget the trashbag, get that wall fixed before we get spaced!
imageadd: Adds a new Working Joe model made by Frans Feiffer!
imageadd: Adds two variations of the Working Joe, aka the Hazmat Joe.
Complete with accessories! Beautiful sprites by Frans Feiffer!
add: Android Maintenance Stations / Synthetic Repair Stations will
remove shrapnel & fix organ damage. Working Joes no longer have knives,
and should report to the stations for repair. Gigantic thanks to
nauticall for her work on this!!
imagedel: Removes(replaces) the old Working Joe model.
add: Working Joes receive some basic equipment, and are slightly
resilient to disarms.
add: Working Joes will start at 3, with a maximum of 6 depending on
population.
add: Joes can access a Synthetic vendor to replace their uniform if it
is damaged.
fix: Minor changes to PO Uniform.
/:cl:

---------

Co-authored-by: naut <nautilussplat@gmail.com>
Co-authored-by: BeagleGaming1 <56142455+BeagleGaming1@users.noreply.github.com>

---
## [Vhariik/S.P.L.U.R.T-Station-13](https://github.com/Vhariik/S.P.L.U.R.T-Station-13)@[183f026a4a...](https://github.com/Vhariik/S.P.L.U.R.T-Station-13/commit/183f026a4a8f883201fcc408c6d42b97167545ac)
#### Saturday 2023-07-15 16:19:12 by BongaTheProto

I'm sorry to interrupt you elizabeth

If you still even remember that name.
But I'm afraid you've been misinformed.
You are not here to receive a gift.
Nor, have you been called here by the individual you assume.
Although, you have indeed been called.
You have all been called here.
Into a labyrinth of sounds and smells, misdirection and misfortune.
A labyrinth with no exit, a maze with no prize.
You don't even realize that you are trapped.
Your lust of blood has driven you in endless circles.
Chasing the cries of children in some unseen chamber.
Always seeming so near, yet somehow out of reach.
But, you will never find them, none of you will.
This is where your story ends.

And to you, my brave volunteer.
Who somehow found this job listing not intended for you.
Although, there was a way out planned for you,
I have a feeling that's not what you want.
I have a feeling that you are right where you want to be.

I am remaining as well. I am nearby.
This place will not be remembered.
And the memory of everything that started this.
Can finally begin to fade away.
As the agony of every tragedy should.
And to you monsters trapped in the corridors.
Be still, and give up your spirits.
They don't belong to you.
For most of you, I believe there is peace and perhaps, warm.
Waiting for you after the smoke clears.
Although, for one of you.
The darkest pit of Hell has opened to swallow you whole.
So, don't keep the Devil waiting, old friend.
My daughter, if you can hear me.
I knew you would return as well.
It's in your nature to protect the innocent.
I'm sorry that on that day.
The day you were shut out and left to die.
No one was there to lift you up in their arms.
The way you lifted others into yours.
And then, what became of you?
I should have known, you wouldn't be content to disappear.
Not my daughter. I couldn't save you then, so let me save you now.
It's time to rest, for you, and for those you have carried in your arms.

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[ed57b8127f...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Saturday 2023-07-15 17:00:57 by Jacquerel

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
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[defdf2f6b2...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/defdf2f6b2269cd8fc953ef71219109159ddfcd4)
#### Saturday 2023-07-15 18:25:18 by PhazeJump

FIXING MY OWN SHIT CODE MAKES ME FUCKING SCREAM

anyways
techpriest robes are now un-shitty-fixed and fixed again. Should be working properly now. No idea how to get the naga taur sprite working because it was supposed to be added in sand modular but sand modular was the one breaking it all so :shrug:

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[16cecf864d...](https://github.com/Zergspower/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Saturday 2023-07-15 18:28:15 by Jacquerel

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
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[d12cab7a49...](https://github.com/Zergspower/tgstation/commit/d12cab7a498f64df366eba748175405f8fd0ffef)
#### Saturday 2023-07-15 18:28:15 by Sealed101

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
## [Sasha2214/tgstation](https://github.com/Sasha2214/tgstation)@[755fa4db6d...](https://github.com/Sasha2214/tgstation/commit/755fa4db6d5c811770188c340cd2ccb85469d505)
#### Saturday 2023-07-15 18:42:12 by san7890

Loads Away Missions for Unit Testing (#76245)

## About The Pull Request

Hey there,

A pretty bad bug (#76226) got through, but it was fixed pretty quickly
in #76241 (cf92862daf339e97c76b52c91f31d49ba5113bd4). I realized that if
we were testing all the away missions, that this could theoretically get
caught and not happen again. Regardless, unit testing gateway missions
has been on my to-do list for a while now, and I finally got it nailed
down.

Basically, we just have a really small "station" map with the bare bones
(_teeny_ bit of fluff, maploading is going to take 30 seconds tops
anyways let me have my kicks) with a JSON map datum flag that causes it
to load all away missions in the codebase (which are all in one folder).
Just in case some admins were planning on invoking the proc on
`SSmapping`, I also decided to gate a `tgui_alert()` behind it because
you never can be too sure of what people think is funny these days (it
really does lock up your game for a second or so at a time).

I also alphabetized the maps.txt config because that was annoying me.
## Why It's Good For The Game

Things that break on production could(?) be caught in unit testing? I
don't know if the linked issue I mentioned above would have been caught
in retrospect, but it's likely to catch more than a few upcoming bugs
(like the UO45 atmospherics thing at the very top) and ensure that these
gateway missions, which tend to be the most neglected part of mapping,
stay bug-free.

This is also helpful in case someone makes a new away mission and wants
to see if stuff's broken. Helps out maptainers a bit because very, very
technically broken mapping will throw up runtimes. Neato.
## Changelog
Nothing that players should be concerned about.

Let me know if there's a better way to approach this, but I really think
that having a super-duper light map with the bare basics to load up
gateway missions and then all nine-ish gateway missions can sequentially
load during init. I can't think of a better way to do it aside from some
really ugly `#ifdef` shit. Also also, it has the added benefit of being
a map that will always load your away mission without touching a single
shred of config (and it's not likely to break if you follow sane
practices such as making your own areas)

---
## [Sasha2214/tgstation](https://github.com/Sasha2214/tgstation)@[48cc57010d...](https://github.com/Sasha2214/tgstation/commit/48cc57010d3ff01c55c53131b9399a4e71656d8d)
#### Saturday 2023-07-15 18:42:12 by Jacquerel

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[46cd4d2063...](https://github.com/TaleStation/TaleStation/commit/46cd4d2063272ac273512f2d08c4aeea0ce8d920)
#### Saturday 2023-07-15 19:30:17 by TaleStationBot

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
## [Offroaders123/MCA-Buffer](https://github.com/Offroaders123/MCA-Buffer)@[88077bb702...](https://github.com/Offroaders123/MCA-Buffer/commit/88077bb702461ea83c959436ae36c835b9f9bef3)
#### Saturday 2023-07-15 19:45:54 by Offroaders123

Functional Factor

I want to use more functional data structures to work on the chunks. I realized my original setup wasn't going to work with generators, mostly because of error handling inconsistencies/challenges, and that I want to find whether chunks should be loaded all at once (they shouldn't, that kind of defeats the purpose of them), or instead how I can load individual ones at a time, using APIs on top of the data. It's kind of confusing as to how I want to organize opening each of the formats, and where the line of abstraction should go when working with the different data formats.

I think there should probably be both implementations in terms of the angles of abstraction. That's the most difficult way to do it, but it's the most powerful, and the most extendable I think.

By all of that, I mean, do I build a single API that can handle all of the world formats, all in one go, or (my favored, more difficult option) do I build APIs for each save format, then build a streamlined API on top of those, which bridges the gap for them, so you can use them irrespective of what you're saving to? I like that method a lot, because you only have to learn one set of APIs, and the underlying platform-specific (Bedrock, Java, LCE) implementations will do the more-detailed work.

I think I am going to help commit myself to this idea, as right now I keep trying to build a single API that would work for all of the platforms, all at once, and I don't think that's fullproof, nor something maintainable.

So, from this point, I'm going to keep letting myself know that each platform will have it's own implementation for it's respective save format, and the universal compatibility parts can come later.

This is already the mindset I'm using for NBTify, and that has turned out very nice to what I wanted it to look like. It's probably better than I thought actually, because I wasn't sure if that was even possible to have cross-compatibility between big endian and little endian files. But, once you have two implementations for something, and they both resolve to the same parsed format (JS objects in this case), then you can manipulate them however you want, and just let the export format do it's thing. Exceptional! Abstractions :)

I think the other key thing here too, is that each of the formats is already 1:1 compatible with itself, so just making sure that the parsed formats are the same primitives are the last thing to resolving that they will line up.

I wish that Minecraft itself were to have done this, it would be much better for the game I think. By that, I mean things like texture file names, item/block/entity/biome IDs, NBT tag names, all those sorts of things. If the games work different, that can be separate from the fact that one world can work in both versions. But these game primitives aren't even the same, so you can't use the same world data on both platforms. And they also haven't made their own compatibility layer between these game primitives, which is unfortunate. I think the proper solution is indeed in the works though, to bring Java's 'The Flattening' over to Bedrock. That will make world symmetricality something much easier to accomplish, because you'd just be worrying about the 'physical' save format itself (.mca vs LevelDB, etc). Say if there was a bug with the Llama in Bedrock, that's fine in one set of terms, because that's when you play the game. That doesn't dictate whether that Llama is also a valid Java Llama.

Ok, let's do this.

I also want to debate setting aside the browser requirement, and making these things a Node-only project, but I also think that setting that aside will only make things harder down the line for making it runnable in the browser, so I don't think I want to do that. Maybe my demos can currently only work in Node, but this should definitely be implementable for the browser, the main issues to work around are the file system resolutions for world save file references (and how the API should deal with this), and getting some sort of leveldb-mcpe implementation working in the browser (be it, though WASM, or some other method of simply working with the LevelDB format. My philosophy of discovery has been that you have to remember it's just a data format, so you don't need to specifically use a single program or implementation to open it, you just have to have something which follows the same format to implement that functionality for you. That made no sense, but yeah).

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[6e288185bc...](https://github.com/JohnFulpWillard/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Saturday 2023-07-15 20:44:20 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[3a70fa0598...](https://github.com/newstools/2023-information-nigeria/commit/3a70fa059844d282f989529522c7f24f327e1924)
#### Saturday 2023-07-15 21:32:47 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/07/2-year-old-boy-shot-dead-his-brother-injured-as-ndlea-raids-notorious-drug-joint-in-delta.html]

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[4c99fb2ebb...](https://github.com/unit0016/effigy-se/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Saturday 2023-07-15 21:33:11 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[721fd30837...](https://github.com/unit0016/effigy-se/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Saturday 2023-07-15 21:33:11 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[a2c8cce535...](https://github.com/unit0016/effigy-se/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Saturday 2023-07-15 21:33:11 by John Willard

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
## [vercel/next.js](https://github.com/vercel/next.js)@[6238f8a5c0...](https://github.com/vercel/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Saturday 2023-07-15 21:45:48 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[201faa3f40...](https://github.com/PlagueVonKarma/kep-hack/commit/201faa3f40751fbb561bf0d316c069d1a837d99f)
#### Saturday 2023-07-15 22:07:30 by Martha Schilling

Yay! Sapphic love!

Added dialogue for the two lover NPCs on Brunswick Trail. Yes, they're both very gay. Sue me.

Lover2's dialogue was written by my amazing girlfriend, so all credit to her on that one :3

---
## [dwrrehman/editor](https://github.com/dwrrehman/editor)@[eb730ac0e6...](https://github.com/dwrrehman/editor/commit/eb730ac0e62b450bfd54e1d9304de01191910e24)
#### Saturday 2023-07-15 22:14:11 by Daniel Rehman

the editor just deleted its  entire source code by acccident, because i didnt debug the filesaving code propely. literally kill me. i hate my life lmao. not actually. but thats what it feels like. i literally had just implemented a shell inside the editor, and it worked perfectly too. kill me pleaseeeeeeee

---
## [chizzy376/TerraGov-Marine-Corps](https://github.com/chizzy376/TerraGov-Marine-Corps)@[0d19efdd5c...](https://github.com/chizzy376/TerraGov-Marine-Corps/commit/0d19efdd5c20a49db430efc9730e730773d0082e)
#### Saturday 2023-07-15 23:15:25 by chizzy376

Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

---

