## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-25](docs/good-messages/2023/2023-12-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,180,884 were push events containing 2,820,824 commit messages that amount to 160,857,035 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 89 messages:


## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[8f3d1036c8...](https://github.com/ReturnToZender/ReturnsBubber/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Monday 2023-12-25 00:02:01 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[a5fabd8819...](https://github.com/ZephyrTFA/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Monday 2023-12-25 00:03:43 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d751e1c642...](https://github.com/timothymtorres/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Monday 2023-12-25 00:11:30 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [frosty-dev/tgstation](https://github.com/frosty-dev/tgstation)@[b17f9d7086...](https://github.com/frosty-dev/tgstation/commit/b17f9d708654caebe332727278d0b7d06e18f70c)
#### Monday 2023-12-25 00:11:56 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[2011c229f9...](https://github.com/silencer-pl/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Monday 2023-12-25 00:27:13 by stalkerino

Readds skull facemask and facepaint (#5042)

# About the pull request
It readds two items that were removed in the past for no valid reason
(in my opinion), since it was a targeted PR against a specific player I
do not think it should've been removed.

# Explain why it's good for the game

It looks nice and fits the atmosphere, adding it will help players
customize their characters without being too loud.
The removal reason of "You'd get laughed at for wearing it IRL" is
invalid, a lot of military and law enforcement people wear skull masks,
punisher emblems and etcetra - this is especially evident in America
(We're UA)

https://discord.com/channels/150315577943130112/746325423289401395/1168350579307860078

https://discord.com/channels/150315577943130112/827156857566265375/1145494273568022588
https://files.catbox.moe/4o3ag1.png

https://discord.com/channels/150315577943130112/604397850675380234/1094357565317586964
-- the person who made it admitting it was targeted.


# Testing Photographs and Procedure
I don't think it needs testing
</details>


# Changelog
:cl: stalkerino
add: readds skull facepaint and skull balaclava (blue and black)
/:cl:

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[a1e46c5d31...](https://github.com/OliOliOnsiPree/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Monday 2023-12-25 00:28:15 by Jacquerel

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
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[bed92e193c...](https://github.com/Xander3359/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Monday 2023-12-25 00:28:19 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[5175ae0637...](https://github.com/Xander3359/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Monday 2023-12-25 00:28:19 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[94603a2a96...](https://github.com/Hatterhat/Skyrat-tg/commit/94603a2a9636ab5a9e8ded9247b490a5d6670da4)
#### Monday 2023-12-25 00:30:06 by SkyratBot

[MIRROR] Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) [MDB IGNORE] (#25102)

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much.

## Changelog

:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP)

---------

Co-authored-by: KingkumaArt <69398298+KingkumaArt@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [UnokiAs/tgstation](https://github.com/UnokiAs/tgstation)@[0d5f9907a2...](https://github.com/UnokiAs/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Monday 2023-12-25 00:33:57 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[6fefc9ce0e...](https://github.com/necromanceranne/tgstation/commit/6fefc9ce0eb09b9b97e3d54609ace23c43601394)
#### Monday 2023-12-25 00:34:12 by Andrew

Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[b58b3abe4f...](https://github.com/Mirag1993/mrdg/commit/b58b3abe4ffd26c63adb349f873ededfda5781a6)
#### Monday 2023-12-25 00:36:26 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [aarrbba123/tgstation](https://github.com/aarrbba123/tgstation)@[b65f729901...](https://github.com/aarrbba123/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Monday 2023-12-25 00:43:01 by lizardqueenlexi

Nanotrasen basic mobs. (#78917)

## About The Pull Request

First and foremost, converts all Nanotrasen simplemobs into basic mobs.

To avoid messy and redundant code, or god forbid, making Nanotrasen mobs
a subtype of Syndicate ones, I've made Syndicate, Russian, and
Nanotrasen mobs all share a unified "Trooper" parent. This should have
no effect on their behaviors, but makes things much easier to extend
further in the future.

While most of this PR is pretty cut-and-dry, I've done a couple notable
things. For one, all types of ranged trooper will now avoid friendly
fire, instead of shooting their friends in the back. Even the Russians
have trigger discipline.

I've also created a new AI subtree that allows mobs to call for
reinforcements. I've hopefully made this easy to extend, but the
existing version works as follows:

- A mob with this subtree that gains a target that is also a mob will
call out to all mobs within 15 tiles.
- If they share a faction, mobs receiving the call will have the target
added to their retaliate list, and have a new key set targeting the
calling mob.
- If they have the correct subtree in their AI controller, called-to
mobs will then run over to help out.

Sadly, this behavior is currently used only by a few completely unused
Nanotrasen mobs, so in practice it will not yet be seen.

Finally, I've fixed a minor issue where melee Russian mobs punch people
to death despite holding a knife. They now use the proper effects for
stabbing instead of punching.
## Why It's Good For The Game

Removes 8 more simple animals from the list.

As said above, making all "trooper" type mobs share a common parent cuts
down on code reuse, ensures consistency of behavior, and makes it much
easier to add new troopers not affiliated with these groups. I expect
that I'll make pirates share this same parent next.

The new "reinforcements" behavior, though extremely powerful, opens up
exciting new opportunities in the future. There aren't many existing
behaviors that allow basic mobs to work _together_ in interesting ways,
and I think adding some enemy teamwork could be fun.
## Changelog
:cl:
refactor: Hostile Nanotrasen mobs now use the basic mob framework. This
should make them a little smarter and more dangerous. Please report any
bugs.
fix: Russian mobs will now actually use those knives they're holding.
/:cl:

---
## [Vexylius/Skyrat-tg](https://github.com/Vexylius/Skyrat-tg)@[37c2cc8d95...](https://github.com/Vexylius/Skyrat-tg/commit/37c2cc8d95f03656cd848e3fcccc1436327b1a09)
#### Monday 2023-12-25 00:43:04 by SkyratBot

[MIRROR] Fixes Shaving Beards + Mirror Code Improvement [MDB IGNORE] (#24829)

* Fixes Shaving Beards + Mirror Code Improvement (#79529)

## About The Pull Request

Fixes #79519

Basically we did a lot of assumptions that we really shouldn't do in the
whole magical mirror framework (like having a boolean value for magical
mirrors, what?). Anyways, I just made the UX experience a lot better
when it came to bearded persons with feminine physiques to easily shave
off their beard with an additional confirmatory prompt + details as well
as keeping the nature of the magical mirror (giving you a swagadocious
beard due to magic:tm:) intact.
## Why It's Good For The Game

There was a lot of convoluted code that skipped through the quality
filter checks (it was me i think) so let's both make the code far easier
to grasp as well as ensure that people who legitimately acquire beards
and wish to keep them, keep them.

We were also doing some FUCK shit on attack_hand and the like
(overriding a FALSE return signal to return TRUE is not what we should
be doing there)- so that's also cleaned up.
## Changelog
:cl:
fix: Both magic mirrors and regular mirrors are far better at respecting
the choice of the beard you wish to wear (within reason, of course).
/:cl:

* Fixes Shaving Beards + Mirror Code Improvement

* Update mirror.dm

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[9ff9e4b9a8...](https://github.com/Addust/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Monday 2023-12-25 00:47:23 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[071f6063e6...](https://github.com/Addust/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Monday 2023-12-25 00:47:23 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Bm0n/tgstation](https://github.com/Bm0n/tgstation)@[157fafeaa9...](https://github.com/Bm0n/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Monday 2023-12-25 00:48:37 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[30dae8899b...](https://github.com/Donglesplonge/tgstation/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Monday 2023-12-25 00:52:11 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[fc41127084...](https://github.com/electrical-pants/f13babylon/commit/fc41127084c96e75ed37c1e51c6ad9d2305da643)
#### Monday 2023-12-25 00:55:46 by Stutternov

Shield Change (As Requested) (#381)

## About The Pull Request

Was requested to do this upon issues with shields. 

So, before some shields literally had the health of Bubblegum + armor on
them as well. The health has been greatly reduced on some, some others
have been buffed at lower end.

Telescopic shield has also been removed since it's busted as hell, had
2250 health, tons of armor, and such.

## Why It's Good For The Game

Some shields that were even labeled as removed were still in the game,
like the Telescopic. Others got buffed by someone last week for some
reason despite stam damage being fucked, etc.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
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
balance: Rebalances shields integrity.
removes: Telescopic shield (Use the riot, it's identical but just not
telescopic.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[1f1cdc609d...](https://github.com/Zergspower/Skyrat-tg/commit/1f1cdc609df04a4749b2f3f5d5500551c86021a8)
#### Monday 2023-12-25 00:57:03 by Nerevar

[FIX] Fixes Kick Damage (#24996)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[7f0536bb93...](https://github.com/carshalash/tgstation/commit/7f0536bb930a022d23d636619e4baf73661280a2)
#### Monday 2023-12-25 00:58:01 by san7890

Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[2562f0997a...](https://github.com/carshalash/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Monday 2023-12-25 00:58:01 by MrMelbert

Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017 

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait. 

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared. 

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[742971675d...](https://github.com/carshalash/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Monday 2023-12-25 00:58:01 by san7890

Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior. 
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

---
## [MoonTheBird/Shiptest](https://github.com/MoonTheBird/Shiptest)@[4d4aa72e33...](https://github.com/MoonTheBird/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Monday 2023-12-25 01:00:07 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MoonTheBird/Shiptest](https://github.com/MoonTheBird/Shiptest)@[caa19d2a6f...](https://github.com/MoonTheBird/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Monday 2023-12-25 01:00:07 by GenericDM

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
## [Floofies/GalaxiaStation](https://github.com/Floofies/GalaxiaStation)@[511b2be113...](https://github.com/Floofies/GalaxiaStation/commit/511b2be113505d9c46fa60accc55e997927e1d18)
#### Monday 2023-12-25 01:02:04 by _0Steven

Making the camera circuit actually work again, and letting it work while held. (#80533)

## About The Pull Request

Alternative title: Hidden Pocket Camera Circuits! _(That Actually
Work)_.

So camera circuits have been broken for a while, and looking deeper into
it this seems to be because at some point someone moved the user check
for customization to before actually creating the picture item. Because
camera circuits rely on calling the `captureimage()` proc with a null
user, this made it so no image was ever printed nor were the photos left
decremented.

Similarly, multiple times I've encountered people being confused about
why their camera circuit isn't even trying to proc while held or hung
around their neck. So I decided to add a check to the `can_target()`
proc for whether it's on a carbon and what it could see from the given
carbon. This allows it to work while held, while hung around one's neck,
and while hidden sneakily in one's pockets. Well, insofar a bright flash
and camera snap are sneaky.
Notably it doesn't work when put in a bag in your inventory. While
having it work from a briefcase would be _incredibly_ funny, that's
outside of the scope of this pr.
Additionally, it felt weird for it to just drop the picture while
procced in your inventory, so I made it first try to put the printed
picture in the carbon's hands if at all possible.

While looking through the code, I also found that there was a typo in
where the circuit calls `captureimage()`, where `camera.picture_size_y`
was used in place of where `camera.picture_size_x` should be.
## Why It's Good For The Game

It makes camera circuits actually work again.

As for having them work while on a carbon, I've encountered multiple
people who were confused about their camera circuits not even _trying_
to proc while held or hung around their neck, when logically they
should- it's visible, after all. Hell, when held it works manually, but
not with a circuit!
Then, camera circuits working in one's pockets were a side-effect of my
first naive fix, and I thought it'd be neat to keep in; the ability to
make hidden pocket cameras just sounds cool to have. They're also only
hidden insofar you can still see the flash and hear the snap.
## Changelog
:cl:
fix: Camera circuits actually print pictures again!
qol: Camera circuits can now take pictures while on a carbon, whether
held, hung around the neck, or sneakily hidden in either pocket. When
held they try to deposit their pictures into the holder's hands if
possible.
fix: Camera circuits should now actually use the camera's x axis picture
size, rather than using the camera's y axis picture size setting for
both axis.
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[68cd638330...](https://github.com/TheBoondock/tgstation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Monday 2023-12-25 01:03:51 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [Kitsu-The-Fox/tgstation](https://github.com/Kitsu-The-Fox/tgstation)@[9cf089361e...](https://github.com/Kitsu-The-Fox/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Monday 2023-12-25 01:06:08 by Rhials

Abandoned Domains: Adds two new psyker-oriented virtual domains (#78892)

## About The Pull Request

_Really? Bitrunning maps are so simple you could do them with your eyes
closed? Hmmmmm..._

This adds two new medium-difficulty virtual domains to the pool -- Crate
Chaos and Infected Domain.

These two domains take you to neglected corners of the virtual world.
These are unstable, bizarre locales that do not support the bitrunning
machine's visual display, and must be traversed using echolocation.
**_These domains have been designed around you being a psyker, and will
turn your bitrunner avatar into a psyker until they leave the domain._**

_**Crate Chaos:** Low cost, medium reward._

Sneak into an abandoned virtual domain, where they store all of the loot
crates. There's about 40-ish crates in this space, and one of them
(RANDOM) is the encrypted cache we're looking for. The crates must be
manually inspected, requiring you to drop your weapon for a few moments,
but that shouldn't be a problem. There's no hostiles, just a bunch of
crates... right?

This one has very few shenanigans or threats in it. It's meant to be an
introductory experience to interfacing with things as a psyker, and
getting the rhythm down for moving between visual pulses.

_**Infected Domain:** Medium cost, high reward._

Enter another abandoned virtual domain. This one was sealed off from the
digital world after the cyber-police failed to contain a virus that
zombified its inhabitants, leaving it to grow unstable and full of
holes. Fortunately, you're provided with the single best tool for arming
yourself against zombies in any video game, ever -- Your very own
Mystery Box. Get armed with (basically) whatever gun you want, and go
put those wacky psyker abilities to use against those zombies.

This one is a lot meaner. Many chasms, landmines, and zombies. Walk
slowly, stay with your fellow bitrunners, and if it's too hard, there's
no shame in going back and rolling for a better gun!

The domains themselves are VERY simple, since there's little need for
decor or particularly complex layouts. The idea is that you should be
able to see everything you need to see in a given room/area with a
single vision pulse. Here's what one of the maps looks like:


![image](https://github.com/tgstation/tgstation/assets/28870487/fe63adce-aa05-4339-9d19-28ce06a2d31f)

Err, uh, I mean... This is what the maps look like:

<details>
<summary>SPOILERS BEWARE</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/28870487/265ecdc5-50f6-4a28-8068-fab08ae1f5e8)


![image](https://github.com/tgstation/tgstation/assets/28870487/0b41da6a-e018-4434-9368-6daee1f97fe9)

(You wanna find out if there's something cool under those red lines? Go
there yourself!)

</details>

These two psyker maps come with their own psyker safehouse too -- The
Bathroom. It's gross, the medical supplies are kind of just sitting
there on the floor... It looks a little bit better when you're blind, I
guess.


![image](https://github.com/tgstation/tgstation/assets/28870487/a10b70bb-5586-4d37-bbb1-a642d8524d54)
## Why It's Good For The Game

I like psykers a lot more than I'm willing to admit. Unfortunately, the
jankiness of echolocation provides such a disadvantage at times, that
any "real" conflict is usually over before the psyker is even aware
they're taking damage.

Fortunately, the controlled environments that bitrunning maps are
perfect for psykers. They give the opportunity to craft an experience
around the player being blind, rather than forcing them to play blind
through a seeing mans world.

These two domains should present players with a unique challenge that is
designed around playing as a psyker, with slightly higher-than-usual
rewards for their trouble. More importantly -- They're fun!
## Changelog
:cl: Rhials
add: Two new psyker-oriented virtual domains -- Crate Chaos and Infected
Domain.
add: Map helper for cyber-police corpse spawn.
add: Map helper for swapping the encrypted crate in an area with a
random crate from that same area.
/:cl:

---
## [Kitsu-The-Fox/tgstation](https://github.com/Kitsu-The-Fox/tgstation)@[66f726dfe3...](https://github.com/Kitsu-The-Fox/tgstation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Monday 2023-12-25 01:06:08 by SyncIt21

General code maintenance for rcd devices and their DEFINE file (#78443)

## About The Pull Request
The changes made can be best summarized into points

**1. Cleans up `code/_DEFINES/construction.dm`**

Looking at the top comment of this file 

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L1

One would expect stuff related to materials, rcd, and other construction
related stuff. Well this file is anything but

Why is there stuff related to food & crafting over here then?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L91-L94

It gets worse why are global lists declared here?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L115
There is a dedicated folder to store global lists i.e.
`code/_globalvars/lists` for lists like these. These clearly don't
belong here

On top of that a lot of construction related defines has been just
dumped here making it too large for it's purposes. which is why this
file has been scraped and it's
1. crafting related stuff have been moved to its
`code/_DEFINES/crafting.dm`
2. global lists for crafting moved to
`code/_globalvars/lists/crafting.dm`
3. Finally remaining construction related defines split apart into 4
file types under the new `code/_DEFINES/construction` folder
- `code/_DEFINES/construction/actions.dm` -> for wrench act or other
construction related actions
- `code/_DEFINES/construction/material.dm` -> contains your sheet
defines and cable & stack related values. Also merged
`code/_DEFINES/material.dm` with this file so it belongs in one place
- `code/_DEFINES/construction/rcd.dm` -> dedicated file for everything
rcd related
- `code/_DEFINES/construction/structures.dm` -> contains the
construction states for various stuff like walls, girders, floodlight
etc

By splitting this file into multiple meaningful define file names will
help in reducing merge conflicts and will aid in faster navigation so
this is the 1st part of this PR

**2. Debloats the `RCD.dm` file(Part 1)**

This uses the same concepts as above. i.e. moving defines into their
appropriate files for e.g.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L170

1. Global vars belong in the `code/_globalvars` folder so these vars and
their related functions to initialize them are moved into the
`code/_globalvars/rcd.dm` file
2. See this proc

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L200
This proc does not belong to the `obj/item/construction/rcd` type it's a
global "helper function" this is an effect proc as it creates rcd
holograms so it has been moved to the `code/game/objects/effects/rcd.dm`
file which is a global effect that can be used by anyone

And with that we have moved these vars & procs into their correct places
& reduced the size of this file . We can go even further

**3. Debloats the `RCD.dm` file(Part 2)**
This deals with the large list which contains all the designs supported
by the RCD

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L42

This list contains a lot of local defines. We can scrape some of them
and reduce the overall bulkiness & memory requirements of this list and
so the following defines

```
#define WINDOW_TYPE "window_type"
#define COMPUTER_DIR "computer_dir"
#define WALLFRAME_TYPE "wallframe_type"
#define FURNISH_TYPE "furnish_type"
#define AIRLOCK_TYPE "airlock_type"
#define TITLE "title"
#define ICON "icon"
#define CATEGORY_ICON_STATE  "category_icon_state"
#define CATEGORY_ICON_SUFFIX "category_icon_suffix"
#define TITLE_ICON "ICON=TITLE"
```

Have all been removed making this list a lot more cleaner. Why? because
a lot of these are just semantic sugar, we can infer the value of a lot
of these defines if we just know the type path of the structure the rcd
is trying to build for e.g. take these 2 defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L13-L15

These defines tell the rcd UI the name and the icon it should display.
Rather than specifying these manually in the design we can infer them
like this

```
var/obj/design = /obj/structure/window  //let's say the rcd is trying to build an window
var/name = initial(design.name)         //we have inferred the name of the design without requiring TITLE define
var/icon = initial(design.icon_state)   //we have inferred the icon of the design without requiring ICON define
```

And so by using similar logic to the remaining defines we can eliminate
a lot of these local defines and reduce the overall size of this list.

The same logic applies to the different modes of construction, the
following defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L186-L192
Have all been removed and replaced with a single value `RCD_STRUCTURE`

All these modes follow the same principle when building them
1. First check the turf if the structure exists. If it does early return
2. If not create a new structure there and that's it

So rather than creating a new construction mode every time you want to
add a new design we can use this mode to apply this general approach
every time

The design list has also now been made into a global list rather than a
private static list. The big advantage to this is that the rcd asset
cache can now access this list and load the correct icons from the list
directly. This means you no longer have to manually specify what icons
you want to load which is the case currently.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/modules/asset_cache/assets/rcd.dm#L8-L9
This has lead to the UI icons breaking twice now in the past
- #74194
- #77217

Hopefully this should never repeat itself again

**4. Other RCD like device changes**
- Fixed the broken silo link icon when the radial menu of the RLD was
opened
- replaced a lot of vars inside RLD with defines to save memory
- Small changes to `ui_act` across RCD, Plumbing RCD and RTD
- Removed unused vars in RCD and snowflaked code
- Moved a large majority of `ui_data()` to `ui_static_data()` making the
experience much faster

Just some general clean up going on here

**5. The Large majority of other code changes**
These are actually small code changes spread across multiple files.
These effect the `rcd_act()` & the `rcd_vals()` procs across all items.
Basically it
- Removes a large majority of `to_chat()` & `visible_message()` calls.
This was done because we already have enough visual feedback of what's
going on. When we construct a wall we don't need a `to_chat()` to tell
us you have a built a wall, we can clearly see that
- replaces the static string `"mode"` with a predefined constant
`RCD_DESIGN_MODE` to bring some standard to use across all cases

Should reduce chat spam and improve readability of code. 

**6. Airlock & Window names**
The rcd asset cache relies on the design name to be unique. So i filled
in the missing names for some airlocks & windows which are subjective
and open to change but must have some value

**7 Removes Microwave PDA upgrade**
The RCD should not be allowed to build this microwave considering how
quickly it can spawn multiple structures and more importantly as it's a
special multipurpose machine so you should spend some effort in printing
it's parts and acquiring tools to complete it. This upgrade makes
obsolete the need to carry an
- A RPED to install the parts
- A screwdriver to complete the frame
- The circuit board for the microwave 

The most important point to note here is that whenever an RPED/circuit
board is printed at an lathe it charges you "Lathe Tax". The RCD with
this upgrade would essentially bypass the need to "Pay Taxes" at these
lathes as you are just creating a circuit board from thin air. This
causes economy imbalance(10 cr per print) which scales up the more of
these machines you make so to avoid this let's end the problem here

Not to mention people would not find the need to print the circuit board
for a regular microwave now if they have an RCD because they can just
make this microwave type making the need for a regular microwave
completely pointless.

Just build a machine frame with the RCD and complete the microwave from
there

## Changelog
:cl:
code: moved global vars, lists and helper procs for construction related
stuff to their appropriate files
code: reduced overall code size & memory of rcd design list and removed
unused defines
refactor: removed a ton of chat alerts for rcd related actions to help
reduce chat spam
refactor: some airlock & window default names have changed
fix: broken icon in radial menu of rld silo link
remove: removes microwave pda upgrade from RCD. It's a special machine
so spend some time in building it rather than shitting them out for free
with the RCD. Use the RCD upgrade to spawn a machine frame instead & go
from there
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Stalkeros2/Skyrat](https://github.com/Stalkeros2/Skyrat)@[8d69a6b49d...](https://github.com/Stalkeros2/Skyrat/commit/8d69a6b49df26a323e0a32f7a51ff7033fa5fd5a)
#### Monday 2023-12-25 01:08:06 by SkyratBot

[MIRROR] Codifies male goats not having an udder [MDB IGNORE] (#25030)

* Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Codifies male goats not having an udder

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [EvilDragonfiend/tgstation](https://github.com/EvilDragonfiend/tgstation)@[81a7c75583...](https://github.com/EvilDragonfiend/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Monday 2023-12-25 01:09:11 by necromanceranne

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
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[48b5a35dea...](https://github.com/kittysmooch/Skyrat-tg/commit/48b5a35deadc1cdeb19d117ee50702c76df0d275)
#### Monday 2023-12-25 01:09:50 by Bloop

[MISSED MIRRORS] Linters, part two (#25138)

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fixes TFE being useless after #78265 (#78433)

I thought `set +e` would still make the shell exit with an error if any
command failed, I didn't think that it would just use the exit code of
the last command. I am dumb, I'm an idiot and I want to cry.

* Update ci_suite.yml

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this
nothing playerfacing

* Only cancel concurrent CI in the same PR (#73398)

More merge queue bullshit. Cancels are counted as failures, and even
though on my test branch it worked completely fine, when trying on two
real PRs, it did not.

This makes it so merges into master might mess with CI clogging again,
but also merge queue is going to do that on its own, and the gain is
worth it.


![image](https://user-images.githubusercontent.com/35135081/218340666-6f937611-c47e-4122-b4b8-b84e8edcc1e9.png)

* Remove cache purge key that has never worked and has meant that our cache has never worked (#71529)

ci_suite.yml runs on your fork. This means you do not have access to
secrets. Every user has had the purge key of blank.

WE have it set to something. Which means the master cache that every PR
pulls from has been unable to match.

This means our cache has been at the max limit all this time, constantly
clearing out old caches, and never reusing any.

* Caches Node and Python Bootstrap for GH Actions (#78307)

## About The Pull Request

I was planning on doing this a lot earlier but ran into some weird
roadblocks, but this time I finally did the research and it's done
properly.

We do a lot of useless work on every single CI run, and in the interest
of saving the world's energy (by a matter of at least 10 seconds per my
testing), lets stop doing so much extra work by caching both the work we
do on the python bootstrap installation (we literally call it `cache`
for a reason) and the Node installation by sharing it between github
actions runners.

Here's a random CI run on master where you can see that the `Install
Tools` portion takes about 19 seconds -
https://github.com/tgstation/tgstation/actions/runs/6167104927/job/16737570519

Here's the CI run I was testing with where you can see we slim it down
to about 6 seconds for the `Install Tools` step, but with a second-or-so
taken to restore the cache since the runner needs to download+unzip the
cache. it tends to be shorter or longer by a second at times but i'm
certain this is just noise -
https://github.com/san7890/bruhstation/actions/runs/6167245722/job/16737919874

On average, we save about **10 seconds** a run on Run Linters, which is
meant to be the fastest CI step. Future improvements would lie in making
either maplint or the tgui test suite faster, but that would be a much
more complicated and code-intensive task. cache go weeeee

## Changelog

Nothing that concerns players.

* Conditionally run TGS tests (#73704)

Also add test merge support for pull requests

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jordan Dominion <Cyberboss@users.noreply.github.com>

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[17cba0dccf...](https://github.com/kittysmooch/Skyrat-tg/commit/17cba0dccfb57eb492fcfade92abc0065a07b356)
#### Monday 2023-12-25 01:09:50 by Bloop

[MISSED MIRROR] Puts all traits in the globalvars file + CI Testing (#79642) (#25131)

* Puts all traits in the globalvars file + CI Testing (#79642)

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-

![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

* Update tgstation.dme

* Update _traits.dm

* Comment these out for now

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[67ddf1507c...](https://github.com/kittysmooch/Skyrat-tg/commit/67ddf1507c8663c4b8f006ed8c763ca372e5fc29)
#### Monday 2023-12-25 01:09:50 by SkyratBot

[MIRROR] Make sign language unaffected by the Social Anxiety quirk's direct speech effects [MDB IGNORE] (#25140)

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects

---------

Co-authored-by: _0Steven <42909981+00-Steven@users.noreply.github.com>

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[fcbbb6e0e0...](https://github.com/kittysmooch/Skyrat-tg/commit/fcbbb6e0e0f9c0132fbc962bb03464bdcd1b20c4)
#### Monday 2023-12-25 01:09:50 by SkyratBot

[MIRROR] Fixes body collision causing a stun, despite a successful block. [MDB IGNORE] (#25146)

* Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs.

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

* Fixes body collision causing a stun, despite a successful block.

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [TheGamerdk/cmss13](https://github.com/TheGamerdk/cmss13)@[9dbf819e8a...](https://github.com/TheGamerdk/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Monday 2023-12-25 01:13:30 by forest2001

Codebook Optimisation (#4393)

# About the pull request
For as long as we've had a codebook it's been a pain in the arse to
read/synchronise from a staff POV. With this, codebooks will all share
the same codes per-faction.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Makes events that use codebooks actually viable.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Codebooks are now faction based rather than individually unique.
/:cl:

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[71b45e54ad...](https://github.com/Striders13/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Monday 2023-12-25 01:13:45 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[8e6b4cc633...](https://github.com/Aurorastation/Aurora.3/commit/8e6b4cc63352160f8716441bc9d59f0752f8a5fb)
#### Monday 2023-12-25 01:18:09 by RustingWithYou

More Ninja Hardsuits & Gear Crates (#18020)

* ninja hardsuits

but here's the warbler

balance tweaks to bug armor

yeah??? fucker.

we're so back we're so back we're so

and icons

changelog and syntax fixes

guh

* oops

* rig nerf

---
## [Lagomorphica/CMSS13](https://github.com/Lagomorphica/CMSS13)@[830e002a27...](https://github.com/Lagomorphica/CMSS13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Monday 2023-12-25 01:20:37 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [Krashly/Ark-Station-13](https://github.com/Krashly/Ark-Station-13)@[6c823eef67...](https://github.com/Krashly/Ark-Station-13/commit/6c823eef675d2b50696e239ea8098165aa052f2f)
#### Monday 2023-12-25 01:21:30 by Bloop

[MISSED MIRROR] Icon Autoslicing (#79659) (#25485)

* Icon Autoslicing (#79659)

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

* Update false_walls.dm

* Modular

* Fixes override for reinforced walls, removals skyrat edits in favor of overrides

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [OlorinIV/Hbm-s-Nuclear-Tech-GIT](https://github.com/OlorinIV/Hbm-s-Nuclear-Tech-GIT)@[be2c17f102...](https://github.com/OlorinIV/Hbm-s-Nuclear-Tech-GIT/commit/be2c17f1028c6129e97620c7d9ecad79b7b06579)
#### Monday 2023-12-25 02:38:31 by Bob

can't wait for the silly people on discord bug me 24/7 about this fuckin

g commit i swear to god this is why we can't have nice things

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[45405782ed...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/45405782edea70043d687f6bda6f71cb8d43bfce)
#### Monday 2023-12-25 03:30:35 by Rhials

Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#80450)

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:


![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

---
## [pa1nki113r/Project_Brutality](https://github.com/pa1nki113r/Project_Brutality)@[368188e721...](https://github.com/pa1nki113r/Project_Brutality/commit/368188e721bc7e377bd74b0d190f6f6c5c8e7836)
#### Monday 2023-12-25 03:42:08 by generic name guy

what the fuck was i thinking????

fakeflags & DI_SCREEN_MANUAL_ALIGN??? fakeflags is fucking 0 it was just created dumbass how did i not fucking notice this bullshit earlier i am at my fucking limit

---
## [Plum-but-gayer/Skyrat-tg](https://github.com/Plum-but-gayer/Skyrat-tg)@[c3ced06238...](https://github.com/Plum-but-gayer/Skyrat-tg/commit/c3ced06238de530cac8ffe846ecf1aff0cfead14)
#### Monday 2023-12-25 03:43:36 by SkyratBot

[MIRROR] New Quirk! Cyborg Lover! [MDB IGNORE] (#25762)

* New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* New Quirk! Cyborg Lover!

---------

Co-authored-by: SSensum <121913313+SSensum@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [SyliusBot/Sylius](https://github.com/SyliusBot/Sylius)@[23b4abd530...](https://github.com/SyliusBot/Sylius/commit/23b4abd530ad3b985f4028dbeab869d004d9593f)
#### Monday 2023-12-25 05:01:09 by Jacob Tobiasz

minor #15646 [API][Admin] Allow using float for amount in tax rates (NoResponseMate)

This PR was merged into the 1.13 branch.

Discussion
----------

| Q               | A                                                            |
|-----------------|--------------------------------------------------------------|
| Branch?         | 1.13 |
| Bug fix?        | kinda                                                       |
| New feature?    | no                                                       |
| BC breaks?      | no                                                       |
| Deprecations?   | no |
| Related tickets | related #15616                      |
| License         | MIT                                                          |

It's hacky as hell; caused by [this bug](https://github.com/api-platform/core/issues/1647), the only other way of fixing it is a migration but that sucks by itself. I'm guessing there are more convoluted ways as well but that's too much pain for the gain.

Commits
-------
  [API][Admin] Allow using float for amount in tax rates

---
## [Gabominated/PCSX2](https://github.com/Gabominated/PCSX2)@[2856d830a4...](https://github.com/Gabominated/PCSX2/commit/2856d830a47d7b4ed660b302e01810739fa38225)
#### Monday 2023-12-25 06:03:45 by Gabominated

README.md

#
7 Blades (PAL-M) SLES-50109 97AE372A
C
Call of Duty - World at War - Final Fronts (PAL-M) SLES-55367 B78A5F5A
Canis Canem Edit (PAL-M) SLES-53561 C78A495D
Clock Tower 3 (PAL-M) SLES-51619 D9FC6310
Conan (PAL-M) SLES-52451 9A206BA3
D
Dawn of Mana (NTSC-U) SLUS-21574 9DC6EE5A
F
Fahrenheit (PAL-M) SLES-53540 8191D10A
G
G.I. Joe - The Rise of Cobra (PAL-M) SLES-55537 724b94f6
Gauntlet - Seven Sorrows (NTSC-U) SLUS-21077 A8C4C0A9
H
Headhunter - Redemption (PAL-M) SLES-52512 2D24ABAD
Hitman - Blood Money (PAL-M) SLES-53028 13E1AD6A
Hitman - Blood Money (PAL-S) SLES-53032 72DC82B5
Hitman - Contracts (PAL-S) SLES-52136 3569E863
Hitman 2 - Silent Assassin (PAL-S) SLES-51110 5B9ACF79
J
Jurassic - The Hunted (NTSC-U) SLUS-21907 EFE4448F
K
Kill.switch (PAL-M) SCES-52124 91A65EAE
L
Lord of the Ring, The - The Return of the King (NTSC-U) SLUS-20770 4CE187F6
M
Magna Carta - Tears of Blood (NTSC-U) SLUS-21221 C0AC5781
Maximo (PAL-M) SLES-50703 B4B7A5A1
Metal Slug 3D (NTSC-J) SLPS-25650 7D8D8BFA
Monster Hunter (PAL-M) SLES-52707 6E8BAF03
Monster Hunter 2 (NTSC-J) SLPM-66280 2F0E94A1
P
Padrino, EL (PAL-S) SLES-53971 203CFBB4
Predator - Concrete Jungle (PAL-M) SLES-53091 BD16D5DE
Primal (PAL-M) SLES-51135 DCC4EEEA
Psi-Ops - The Mindgate Conspiracy (NTSC-U) SLUS-20688 9C71B59E
R
Red Ninja - End of Honor (NTSC-U) SLUS-20714 6B0F338D
Run Like Hell - Hunt or Be Hunted (NTSC-U) SLUS-20037 F802A575
S
Saint Seiya - The Hades (Pal-M) SLES-54162 0392EB95
Scarface - The World is Yours (PAL-M) SLES-54182 301A1B6E
Score International Baja 1000 - The Official Game (NTSC-U) SLUS-21850 9AB3424F
Second Sight (PAL-M) SLES-52670 65087F31
Secret Service - Ultimate Sacrifice (NTSC-U) SLUS-21836 5AA9405C
Shadow Man - 2econd Coming (PAL-M) SLES-50446 48553AF
Sims 2,The - Castaway (PAL-M) SLES-54903 E7692E0B
Spider-Man - Friend or Foe (NTSC-U) SLUS-21600 F52477F7
Star Wars - Battlefront II (NTSC-U) SLUS-21240 249540F3
Syphon Filter - The Omega Strain (PAL-M) SCES-52033 27E54B37
T
Teenage Mutant Ninja Turtles - Smash-Up (NTSC-U) SLUS-21904 532D7041
Teenage Mutant Ninja Turtles - Smash-Up (PAL-M) SLES-55565 CEBA108D
Teenage Mutant Ninja Turtles 2 - Battle Nexus (NTSC-U) SLUS-20981 EE628509
Teenage Mutant Ninja Turtles 3 - Mutant Nightmare (NTSC-U) SLUS-21184 DB42119C
W
World War Zero – Ironstorm (PAL-M) SLES-51924 95D6EE18
Z
Yakuza (PAL-M) SLES-54171 D3F182A3

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[33e10634ba...](https://github.com/Ben10Omintrix/tgstation/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Monday 2023-12-25 06:06:13 by Iamgoofball

Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

---
## [asdlei99/nix](https://github.com/asdlei99/nix)@[b13fc7101f...](https://github.com/asdlei99/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Monday 2023-12-25 07:06:35 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [anarchitech/muforth-anarchitech](https://github.com/anarchitech/muforth-anarchitech)@[80d18fe533...](https://github.com/anarchitech/muforth-anarchitech/commit/80d18fe533b440eb1503ed1fab42d8170b27ecb2)
#### Monday 2023-12-25 07:38:54 by cthulhu

Patch to get the stm32f3-discovery board

   A) actually communicating w/ the host
   B) actually working on OpenBSD

REMINDER: you need to pay attention to which ugenX.XX you're using
and you either need to change ownership of the specific device.endppoint
you're connecting via to $USER or chmod 660 on OpenBSD.

Yes, this is hacky and silly, no, noone here is going to write a
driver for it so don't ask. Remember to change it back.

	modified:   mu/target/ARM/board/stm32f3-discovery.mu4
	modified:   mu/target/ARM/debug/stlink-v2.mu4

---
## [Virus1260/Little-Jewels-Kindergarten](https://github.com/Virus1260/Little-Jewels-Kindergarten)@[d59338b6db...](https://github.com/Virus1260/Little-Jewels-Kindergarten/commit/d59338b6dbd24d43bbc2733f46d9f680deecd390)
#### Monday 2023-12-25 08:30:30 by Shekhar

Ract Helmet

Meta tags published in google search rolling to thaat again

import { Helmet } from 'react-helmet';

<Helmet>
  <title>The Little Jewels Kindergarten - Nurturing Young Minds in Nagpur</title>
  <meta name="description" content="Embark on a delightful journey with The Little Jewels Kindergarten, a cherished institution nestled in the heart of Nagpur. As a proud feeder of Jain International School, our enchanting space is more than a kindergarten—it's a haven filled with love and warmth, dedicated to fostering the physical, mental, emotional, cognitive, and social growth of every young mind.

At The Little Jewels, we transcend traditional education. We're more than a school; we're a home where laughter echoes in every corner, and curiosity is the guiding star. Managed by the venerable Sir Shantilal Badjate Charitable Trust, our legacy extends to Jain International School, Nagpur (a CBSE School), and S. B. Jain Institute of Technology, Management & Research.

Our mission is to inspire children to become self-disciplined, innovative, caring, tolerant, honest, and friendly individuals. We've meticulously crafted a secure and joyous learning environment where well-trained and supportive teachers guide students with attention. Our child-friendly infrastructure boasts up-to-date facilities, interactive boards, and a hygienic ambiance.

Experience play-way learning, engaging co-curricular activities, and smart classes that make education a captivating adventure. The Little Jewels Kindergarten is more than an institution; it's a promise of holistic development, creativity, and a lifetime of cherished memories.

Come, join us, and let your child's journey of discovery and growth begin at The Little Jewels Kindergarten." />
  <meta name="keywords" content="Little Jewels Kindergarten, Nagpur, Jain International School, Child Development, Play-way Learning, Holistic Education" />
  <meta name="author" content="Virus1260, Shekhar Mishra" />
</Helmet>

---
## [danielhjz/langchain](https://github.com/danielhjz/langchain)@[d4f45b1421...](https://github.com/danielhjz/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Monday 2023-12-25 09:31:14 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [Offroaders123/Bedrock-LevelDB](https://github.com/Offroaders123/Bedrock-LevelDB)@[cfe9f24f78...](https://github.com/Offroaders123/Bedrock-LevelDB/commit/cfe9f24f78162daebb81673887b8898a0dfbd2a4)
#### Monday 2023-12-25 09:40:19 by Offroaders123

Actor Storage Investigation (Digp Dilemma)

https://learn.microsoft.com/en-us/minecraft/creator/documents/actorstorage

This isn't a new find, but I think I'm connecting more things together now

```js
{
  '14, 20': 'minecraft:axolotl',
  '19, 43': 'minecraft:wandering_trader',
  '20, 16': 'minecraft:villager_v2',
  '20, 17': 'minecraft:villager_v2',
  '20, 18': 'minecraft:villager_v2',
}
```

Parsing all of the `actorprefix` entries in the database, I got these for my demo world
The keys are derived from the coordinates present in the key, and any trailing data that I haven't figured out how to parse yet I added as the third optional `<Buffer * *>` value in the mapping result
So only 2 of the entities appear to have different key formats than just the plain `actorprefix`, followed by 8 bytes for the `x, z` coordinates
I was trying to figure out where you are supposed to figure out the dimension of the entity, since the NBT doesn't store this information, having looked into it, and they key doesn't hold that info either, because the End Crystals and Striders would have to have bonus trailing data to show the dimension they were saved in too

Since they don't, I thought they must be stored some other way
Went back to look at that article, and from what I read, it seems that the mystery `digp` entries are mappings for where you locate these `x, z` entries, and they are static things to locate to, or something like that
So rather than the `x, z` Chunk of the entity being stored right in it's key and possibly changing with time for one reason or another, I think it's instead a reference to getting the associated `digp` entry, which instead holds the mapping between the Chunk and the ID that the actor/entity references in it's key

```js
{
  '14, 20': 'actorprefix\x00\x00\x00\x0E\x00\x00\x00\x14',
  '19, 43': 'actorprefix\x00\x00\x00\x13\x00\x00\x00+',
  '20, 16': 'actorprefix\x00\x00\x00\x14\x00\x00\x00\x10',
  '20, 17': 'actorprefix\x00\x00\x00\x14\x00\x00\x00\x11',
  '20, 18': 'actorprefix\x00\x00\x00\x14\x00\x00\x00\x12',
}
```

Here's a better representation of the real keys I was talking about
So this is instead showing the real keys in the database, and these are the `digp` references I was talking about
I think the `x, z` coordinates in those keys there are instead meant to reference associated `digp` keys, which are where you get the coordinates for the real chunk these were derived from

Eventually keeping track of and calculating these things for the conversion step and viewing worlds in general is going to be a bit complex, I'm not quite sure what the best way to handle this would be

Next part:
Turns out I was wrong about the `actorprefix${number}` part, the trailing numbers aren't coordinates, and are instead a UUID for the actor.

This *might* not be as difficult of a thing as I thought, but we'll see. More in a matter of being able to both parse it and replicate it when re-saving custom data to the database, and allowing it to be fully valid as to how the world format is expected to work here.

Snowcow! Works nice for Christmas, as well as The Scambot Holiday Special. Want to listen to Devin's Silent Night too.

---
## [Talha-Shafi/CENTIPEDE](https://github.com/Talha-Shafi/CENTIPEDE)@[077255e656...](https://github.com/Talha-Shafi/CENTIPEDE/commit/077255e6565157f9076f6b6ff74a7c32ea0ac59c)
#### Monday 2023-12-25 09:49:21 by Talha-Shafi

Create PROJECT

# Centipede Game in C++ with SFML

This repository hosts the source code and assets for a classic arcade-inspired Centipede Game developed in C++. The project, created as the final assignment for [course/program name], showcases fundamental programming concepts with an emphasis on object-oriented design.

## Key Features

- **SFML Integration:** Utilizes the Simple and Fast Multimedia Library for enhanced graphics, multimedia handling, and sound effects.
- **Classic Gameplay:** Experience the timeless thrill of battling a centipede in a mushroom-filled environment.
- **Object-Oriented Design:** Demonstrates a well-structured, object-oriented architecture for code maintainability.
- **User-Friendly Interface:** Provides an intuitive interface with menus, scoring, and easy navigation.
- **Sound Effects:** Immersive audio experience with SFML for shooting, mushroom destruction, and more.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/centipede-game.git`
2. Compile the source code using a C++ compiler with SFML support.
3. Run the executable and enjoy the enhanced Centipede Game experience.

## Note

This project is intended for personal demonstration and educational purposes. It is not released under an open-source license, and the source code is not provided for public use without explicit permission.

## Technologies Used

- C++
- SFML Library
- Object-Oriented Design

## License

This project is not open-sourced. All rights reserved.

---
## [iamyashsharma43/spotify-clone--](https://github.com/iamyashsharma43/spotify-clone--)@[4fb26d76fd...](https://github.com/iamyashsharma43/spotify-clone--/commit/4fb26d76fd8fb0465ba1a5eabe6c84013e2a9c0c)
#### Monday 2023-12-25 09:49:53 by iamyashsharma43

Add files via upload

Welcome to **SpotifyClone**: Your Soundtrack, Your Style! 🎵✨

SpotifyClone is not just a replication; it's a seamless blend of HTML, CSS, and JavaScript that transforms your music streaming into an immersive experience. Dive into a world where design, functionality, and user-friendly interfaces harmonize to create a Spotify-inspired adventure.

🎨 **Visual Finesse:**
Witness the perfect marriage of HTML structure and CSS styling, crafting an interface that is not only responsive but visually captivating. SpotifyClone's design ensures that each click is not just an action but a visual delight.

🔀 **Effortless Navigation:**
Explore your music effortlessly with the magic of HTML and JavaScript. Seamless transitions and intuitive controls make SpotifyClone a joy to navigate, ensuring your musical journey is smooth and enjoyable.

🔊 **High-Fidelity Audio:**
Powered by JavaScript magic, SpotifyClone's audio player delivers a crisp and immersive listening experience. Every beat, every note is precisely tuned to give you a sound experience that rivals the original.

🎧 **Your Playlists, Your Way:**
Let SpotifyClone be your personal DJ with dynamic playlists generated on the fly. With the power of JavaScript, your music preferences shape your playlists, ensuring each mix resonates with your unique taste.

🌐 **Social Soundwaves:**
Connect with friends, share your favorite tracks, and discover new beats together. SpotifyClone's HTML-driven features let you build a musical community, making your listening experience a shared adventure.

🛡️ **Security Amplified:**
Your data is sacred, and we treat it as such. With robust security features implemented through HTML and CSS, SpotifyClone ensures that your musical haven is a safe space for your favorite tracks.

🌈 **Theme Your Tunes:**
Personalize your SpotifyClone experience with customizable themes. Let your mood dictate the visual vibe, thanks to dynamic CSS styling that adapts to your aesthetic preferences.

🚀 **Fast-Track Your Music:**
Experience the speed of SpotifyClone, where HTML and JavaScript collaborate to create a platform that not only keeps up with your pace but anticipates your musical desires.

Welcome to SpotifyClone, where the symphony of HTML, CSS, and JavaScript creates a Spotify-inspired musical journey just for you. Get ready to elevate your listening experience – one track at a time! 🚀🎶

---
## [jamestiotio/streamlit](https://github.com/jamestiotio/streamlit)@[c464422e1b...](https://github.com/jamestiotio/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Monday 2023-12-25 09:55:48 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [Robbbert/exp](https://github.com/Robbbert/exp)@[52ecd995e7...](https://github.com/Robbbert/exp/commit/52ecd995e7baab82cf219c9d7c40eca327a8f9e2)
#### Monday 2023-12-25 10:38:05 by wilbertpol

msx2_flop.xml: Added 33 items (32 working) and replaced five items with better dumps. (#11863)

* Replaced Disc Station Deluxe 1 (Japan) with a better dump. [file-hunter]
* Replaced Poyo Poyo Life (Japan) and  Poyo Poyo Life II (Japan) with better dumps. [file-hunter]
* Replaced Pumpkin Adventure - The Quest for the Holy Grail (Netherlands) with a better dump. [file-hunter]
* Replaced Pumpkin Adventure II (Netherlands) with a better dump. [file-hunter]
* Removed hacked images Pumpkin Adventure - The Quest for the Holy Grail (Netherlands, alt) and Pumpkin Adventure - The Quest for the Holy Grail (Netherlands, alt 2).
* Removed User Disk from Pumpkin Adventure III (Netherlands).
* Removed Puyo Puyo (Japan, alt) and  Puyo Puyo (Japan, alt 2) as they contain saved data.

New working software list items (msx2_flop.xml)
-------------------------------
Disc Station Special Natsuyasumi-gou (Japan) [file-hunter]
Outlaw Suikoden (Japan) [file-hunter]
Kibun wa, Pastel Touch!! Abunai Gakuen Hen (Japan) [file-hunter]
PIAS - Hikisakareta Seishun (Japan) [file-hunter]
Private School (Japan) [file-hunter]
Puzzle Game Nadia Special (Japan) [file-hunter]
Puzzle - Große Meister (Germany) [file-hunter]
R・SYSTEM Ketteihan (Japan) [file-hunter]
R・SYSTEM 3.2 (Japan) [file-hunter]
OK Fred (Netherlands) [file-hunter]
Panic Shoot [file-hunter]
Petiso Game (Spain) [file-hunter]
PH.Sound Collection (Japan) [file-hunter]
Phi (Japan) [file-hunter]
Pig's Quest (Netherlands) [file-hunter]
Piles (Netherlands) [file-hunter]
Pixess (Netherlands) [file-hunter]
Point Crisis [file-hunter]
Poker Dolls [file-hunter]
Poyo Poyo Life 3 (Japan) [file-hunter]
Push'em [file-hunter]
Puzzel (Netherlands) [file-hunter]
Puzzle 9.64 (Japan) [file-hunter]
Puzzlemania (Netherlands) [file-hunter]
Quadromania MSX2 [file-hunter]
Quiz! Atatchatte 25% (Japan, 1996-12-26) [file-hunter]
Quiz! Atatchatte 25% (Japan) [file-hunter]
RCCR - RC Car Race (Japan) [file-hunter]
Realms of Adventure (Netherlands) [file-hunter]
Retaliator (Netherlands) [file-hunter]
Riot (Japan, alt) [file-hunter]
Ruby & Jade [file-hunter]

New software list items marked not working (msx2_flop.xml)
------------------------------------------
Disc Station Special Haru-gou (Japan) [file-hunter]

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[0090de29b4...](https://github.com/ZacharyTStone/ZacharyTStone/commit/0090de29b4c87667a8578fc66abfc6e6a95ed455)
#### Monday 2023-12-25 11:04:05 by ROBO-ZACH

Update README with new quote: "All I can say about life is, Oh God, enjoy it!" <br>— Bob Newhart

---
## [Offroaders123/Bedrock-LevelDB](https://github.com/Offroaders123/Bedrock-LevelDB)@[981d372643...](https://github.com/Offroaders123/Bedrock-LevelDB/commit/981d37264309bb36677407fd1a935d9b7c5b9f98)
#### Monday 2023-12-25 11:05:23 by Offroaders123

Digp Reverse Conceptualization

Wonderful, looks like Mojang was having trouble keeping track of this at one point as well haha
https://bugs.mojang.com/browse/MCPE-155283
Cool to see references of rbedrock there as well
https://github.com/Amulet-Team/Amulet-Map-Editor/issues/702
https://bugs.mojang.com/browse/MCPE-160818

I think I figured part of it out

So if an `actorprefix`'s key links to an empty `digp`, I think you just use the same Chunk key present for the `digp`/`actorprefix` itself, meaning they are the same, and there isn't a disparity between the two

My guess is that they are only different when an entity has changed chunks per say, like if they move into another chunk
If this is the case, then the `actorprefix` numbers will always stay the same, and instead the `digp` values will be updated to reflect the new chunk coordinates, instead in the value of the `digp`

This also appears to be where the dimension information is stored too, hence why some of the values are 8 bytes (`x, z`), and others are 12, because of the additional 4 bytes for the dimension `uint32` (Not sure why it's that big when it only needs to be a `uint8`, but yeah)

---
## [K9100ii/android_hardware_samsung_slsi-linaro_graphics](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_graphics)@[a7958a657d...](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_graphics/commit/a7958a657dad314486c440ccbb71209f54fbbe94)
#### Monday 2023-12-25 11:38:09 by K9100ii

graphics: Switch to a new versioned path and BSP variant setting

and add soong namespacing.

Copy-paste explanation:

There are two sets of BSP sources - These new ones intended for Android
13, and older ones originally intended for Android 10. The older ones
have support for some legacy things like HWC1 for older devices, and
the newer ones have support for newer things like gralloc4.

To keep support for older devices going, I want to keep the older
sources alongside the newer ones. But they can't co-exist as-is. Some
changes are needed:
 - a change of paths to the BSP sources, which are referenced directly
   within them
 - a new BSP variant setting ('TARGET_SLSI_VARIANT' flag)
 - and finally, some soong namespacing.

The BSP variant setting and paths are the biggest challenge. For the
existing BSP sources, there's absolutely no versioning. It's the same
old generic "linaro"/"samsung_slsi-linaro" for both sets of BSP sources.
Sadly, my expressions of concern for my life to not be made more hellish
were quite badly dismissed, all the while I'd think it would be best
practice to version things like this to not keep using the same old
generic identifiers and not run into issues (or for others to not do so)
later, so I'm on my own to figure out what to do here.

My solution that touches the least I can is as follows:

For Android 13 - The older Android 10 BSP sources are typically used,
and since I'd like to use 13 sources as I have a device that requires
gralloc4, I need to make changes within them.
To manage it, the naming is as follows:
  Directory for 10 sources - 'samsung_slsi-linaro'
  Directory for 13 sources - 'samsung_slsi-linaro_13-e850-96'
  Git branch name for 10 sources - '...'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro'
  SLSI variant flag setting for 13 sources - 'linaro_13-e850-96'
The only changes here are for 13 sources. Naming is left untouched for
10 sources so as to not break anything for trees using them currently.

For Android 14+ - I'd want to preserve support for older devices,
provided if, and hoping that, running newer Android versions doesn't
become an impossibility for them, so, while the newer Android 13 BSP
sources are typically used, I'd have to make changes to the 10 sources
to keep them alongside.
To manage it, the naming will be as follows:
  Directory for 10 sources - 'samsung_slsi-linaro_10-e850-96'
  Directory for 13 sources - 'samsung_slsi-linaro'
  Git branch name for 10 sources - '..._10-e850-96'
  Git branch name for 13 sources -  '...' / '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro_10-e850-96'
  SLSI variant flag setting for 13 sources - 'linaro'
The directory and variant flag setting will be untouched for 13 sources,
so as to stay in line with everyone else, and changes would only need to
be made within 10 sources. However, for consistency, there will always
be versioned git branches in future, alongside non-versioned ones with
whichever sources are typically used, though this all remains less than
ideal in any case.

Lastly, soong namespacing is added specifically for the "exynos" and
"graphics" parts of the sources. Without, there are conflicts between
the two sets of sources. For all devices, BoardConfigCommon.mk in the
collection of BSP configs is included, and namespaces can be added
there, and also the SLSI variant flag setting can be changed, for a
clean result where no changes are required in device trees at all.

Change-Id: I79e77f9bff0d4a1595d5cc6fe72fbd17d2734373

---
## [C0de871/Cinema-Management](https://github.com/C0de871/Cinema-Management)@[749b2f8176...](https://github.com/C0de871/Cinema-Management/commit/749b2f81764951b9d9d01ef187adbea5ad55c5f8)
#### Monday 2023-12-25 11:43:35 by MOAdnan23

Merge pull request #7 from C0de871/Adnan

store fuck you kasem you just fuss us

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[8d77b1be89...](https://github.com/Ghommie/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Monday 2023-12-25 12:04:34 by necromanceranne

Balance changes to swords, energy shields and modsuit shields. (#80072)

## About The Pull Request

### Sword Weaponry

Mundane sword weapons of all sorts do not block ``LEAP_ATTACK`` attacks
whatsoever. These attacks include tackles, xeno tackles and bodythrows.

Energy swords and double energy swords only gain 25% block probability
against such attacks.

### Double Energy Sword

No longer grants outright energy projectile immunity while employed.
Instead, it just has a high probability of reflecting (the typical 75%
to block any other attack). So, very solid defense against energy
projectiles, but not immunity.

Against non-reflectable projectiles, like ballistics or nanite bullets,
the desword only has 50% block, similar to an energy sword.

To compensate for the loss of defensive power, we'll make it all the
more rewarding for getting on top of someone with the sword by giving it
40 force while active. And also it costs 13 TC.

### Combat Energy Shield

This also lost outright energy projectile immunity, but gained the
standard blocking power of shields on top of the ability to reflect
energy projectiles when they block them. This significantly increases
the shields potential effectiveness while no longer pigeonholing the
shield to only energy weapons. (This makes them exceptionally good
against tackles and body throws, by the by).

Deathsquads still have the perfect deflection energy shield so that they
can continue to spam pulse shots with impunity.

### MODsuit Shield Module

Only has one charge instead of three, but it recharges in half the time.
This is no longer such a perfect defense, and does somewhat need you to
be thinking about how you're utilizing the shield rather than not
thinking about defense at all by barreling forward under three potential
hits worth of protection.

Also much cheaper, at almost half price of 8 TC. Because of how cheap it
is (and how much it still is necessary to keep you alive), I've put it
into the core equipment box (which brings the price up to 22 TC. As a
reminder, this is not meant to be at any discount, and is more aimed
towards teaching newer players which items contribute towards success.
If you don't want all the times within, don't buy this box, just buy
what you want separately.)

## Why It's Good For The Game

This is a doozy of an explanation, I hope you're ready for it under the
spoiler.
<details>
With my tackling and bodythrow prs, numerous people expressed
exasperation at the fact that these two tools may have been keeping some
outlier antagonist gear from becoming too easy to steamroll with if you
already knew what you were doing. My intent was to create consistent
rules and behaviours that both A) did not rely on bugs to keep the
balance of power from tipping one way or the other, and B) was at least
consistent or had consistent rules established.

This PR is tackling overperforming gear combinations for already
competent nukies that may have, over time, crept out of control, and
applying some consistency to the rules around similar equipment.

AND also deals with quite possibly the most braindead element of game
design we've tolerated for about a decade, and half a decade after it
was necessary to maintain that decision.

Part of the culprit of this issue is that, specifically in regards to
nukies, crew can't use the vast majority of their weapons effectively
against them. This largely is because this antagonist can gain
immunities to those types of equipment. And that is rapidly increasing
as we move closer towards outright ballistic removal. I don't think the
game is made healthier by everyone on the station having to fight armed
mercenaries with spears, and doesn't make much thematic sense either.
More so, most greener players probably just don't know this is how it
works, and so surprise Pikachu when their lasers bounce off nukies
harmlessly. (This bit reminds me of the problem of new players using
disablers against simple mobs)

But of course, that isn't the only part of the problem. The other half
is due to being able to be layered on a much more broad defensive tool
in the form of the MODsuit Shield Module, whose three charges could
render the mindful nukie near untouchable if they're pairing it with
some other layered defense, such as a desword. Notice that this doesn't
really address armor. The culprit is negation, and not mitigation, and
we should be sparing in how easily we hand out outright effect negation
simply because it isn't super obvious to a new player why it happened,
and how to resolve it. At the very least, we should look to find ways to
add options for players to overcome these problems. Especially with
teamwork.

Energy projectile immunity made sense while there floated around an
energy projectile that ostensibly would down you in a single shot.
Nukies ALSO had projectile weapons that worked much the same (c-20r stun
bullets, taser shot bulldogs, etc.), so it was predominantly
tit-for-tat. These immunity granting equipment pieces forced crew
members to get shotguns and ballistic guns to fight these dangers;
something more available at the time.

We've exercised large bits and pieces of this from the game a long time
ago, but we still have some remnants convinced we're still in a
taser-rich, ballistic available environment. We need to move the games
languishing tools into the modern era and re-established their place in
the game. Namely, the double-energy sword and the combat energy shield
are almost entirely unchanged besides refactors for the last decade or
so, even while the game around them have changed. They've been a
continuous sore point for me in all my time developing and a constant
nagging issue. I want to deal with it now.

MODsuit Shield Module is just kind of really good and only made stronger
the more defenses you have. It's good to have a defense like this, but I
think it is too brain dead. With only one charge, it will save you from
a lost joust here and there, but it won't make it as simple as running
right at every problem you encounter and eating a volley of attacks
while you kill someone with impunity.

**With regards to traitors**, since they also get double-energy swords;
I'm open to suggestions if this is hitting them far too hard, but I'm
not terribly concerned using this weapon for a few reasons. **Firstly**,
I think their presence amongst the crew make it a much better weapon for
tots than nukies (in isolation) simply because they can find ways to
exploit it via tools they gather from the station. It is a force
multiplier. Traitors also have a much bigger element of surprise
usually. **Secondly**, round-start traitors typically grow to be a bit
stronger over time, but I don't foresee many waiting to pay for the
double-energy sword unless they're already flush with TC. So if a
traitor is in a position after they've unlocked access to it to buy one
of these, they are probably doing pretty okay for themselves.
</details>

### TL;DR

Defense stacking and attack immunities are not particularly healthy
things to both design around, or experience in-game. They are kind of
just relics of the past made only sorer once I ripped off a few
bandaids. This is a source of a number of symptomatic issues in the
game, so let's fix that and make it easier on all of us going forward.

Much of the way these things worked operated on extremely outdated
design considerations. It doesn't make sense for them to work like this
today, and only makes things harder by keeping the status quo.

## Changelog
:cl:
balance: Mundane sword-like and medieval weapons are not able to block
tackles, xenomorph tackles and body throws.
balance: The double-energy sword and energy sword have trouble blocking
physical projectiles, body throws and tackles.
balance: The double-energy sword also no longer has guaranteed energy
projectile deflection; only doing so on a successful block (75% chance
to block).
balance: But it does have 40 force now, so it is more lethal a weapon.
Traitors can purchase the sword for only 13 TC (down from 16 TC).
balance: The combat energy shield (The one you hold) now functions as a
normal shield (it used to only protect you against energy projectiles
and nothing else). It loses guaranteed energy projectile deflection, but
still reflects the projectile so on a block.
feature: Death commandos continue to have their energy shields deflect
all incoming energy projectiles. Because who cares about deathsquads
being balanced?
balance: The MODsuit shield module only has one charge, but recharges
every 10 seconds. It also costs 8 TC (down from 15). It is also now in
the Core Gear beginner box (bringing the total price up to 22 TC).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[54ab1e3936...](https://github.com/Ghommie/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Monday 2023-12-25 12:04:34 by Time-Green

Organ movement refactor *Un-nullspaces your organs* (#79687)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

closes #53931, #70916, #53931

## About The Pull Request

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).


https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

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
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[16bdcf409c...](https://github.com/Ghommie/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Monday 2023-12-25 12:04:34 by Rhials

"Security Implant" rework, prisoner management console updates (#79882)

## About The Pull Request

For the vernacular purposes of the following PR body -- "Security
Implant" refers to the existing subset of implants given, by security,
to captured prisoners and such as a punitive, controlling measure. This
includes the chemical, tracking, and maybe exile implants.

This revamps the functionality of how "security" implants are displayed
on huds, prisoner management console implant controls/readouts, and
their instrumentality. It was also, ultimately, an attempt at nerfing
the tracking implant that spiralled far out of control.

Rather than only displaying chemical on the right and tracking on the
left, all implants with the "security implant" flag will be trackable on
SecHuds. A maximum of two can be implanted at once. This is both due to
technical limitations, but also conveniently provides security a limit
to consider when choosing implants.

Implants now also occupy their HUD slot based on the order they were
implanted in, rather than always occupying the same spot. Neat!


![image](https://github.com/tgstation/tgstation/assets/28870487/68b17dbb-cda4-4c3b-96d4-b3bbcf49b80e)

From two (three if you count the exile implant), there are now five
security implants. _The tracker implant has been split into two of these
implants._

<details>
<summary>Summary of the implants, functions, changes:</summary>
<br>

- **Tracker (Red)** -- No longer grants teleporter beacon. Tracking
radius has been increased from 20 to 35 tiles. The Prisoner Management
Console will now list the area the prisoner is occupying as well.
Disables after the implantee is dead for 10 minutes.
- **Chemical (Blue)** -- No mechanical changes. The implant pad readout
has been modified slightly.
- **Exile (Green)** -- In addition to past functionality, station
shuttle controls (public, mining, etc.) will be unresponsive for the
implantee. Flimsy, but more effective than a stern warning not to come
back from lavaland.
- **Beacon (Yellow)** -- Implantee becomes a teleporter beacon. The
prisoner console will report if their currently occupied area is
hazardous or not, so half of the security team doesn't blindly teleport
into space or lava. Disables after the implantee is dead for 10 minutes.
Available from Cargo.
- **Teleport Blocker (Deep Blue, not shown)** -- Prevents the implantee
from being teleported. Ever wanted to keep a wizard or cultist in a
cell? This is where you can start. Available from Cargo, expensive and
scarce.

Each of the implants has some application that would benefit security if
used on a captured criminal. Their usefulness may overlap in some
places, but the overall range of control these implants give security is
broadened.

</details>

The implant control console has also been given a small facelift.
Certain implants provide more useful readouts that can help officers
locate, control, or capture an implantee, rewarding cooperation between
officers.

It has also been totally converted into TGUI by @MrMelbert. Kickass!

Also, You can now remotely destroy implants, either to relieve criminals
from their punishment or to make room for a different implant. Wardens
should keep hold of their ID and remember to log out, since a motivated
convict could use it to shed their implants!


![tgui](https://github.com/tgstation/tgstation/assets/28870487/3c2ae99f-9c1d-4b18-b4cb-942cc96bcafe)

Everything made in this PR _should_ be scaleable enough to allow for new
security implant types to be implemented with relative ease. The
teleport-blocker implant was a last minute attempt to prove it to
myself. I had a few more ideas for implants in my head, but figured this
PR was already getting big and ugly enough. That is all for another day.

I truly apologize if there's anything I've missed in here. I did a lot
of this over a long period of time and kind of just... sat on it for a
while. If there's any confusing our unexplained changes, feel free to
point them out and I'll try to give an explanation.
## Why It's Good For The Game

The goal of this PR is to give a bit more depth to security's armory
implants. The intent is to present a choice in what implants are given
(rather than just tracker and maybe chem if you're feeling spiteful),
and to make them more useful as punitive/monitoring tools.

The tracker implant needed a nerf (and probably still does regardless of
this PR's success). It's never used for tracking since the teleporter
beacon is much more direct (+ gives a virtually free attack
opportunity), and the tracking range was incredibly subpar. I'd rather
not take toys away from security, but having the best option not be
roundstart gear feels like a fair compromise.

Warden content. Wardens have more gear to budget for and use at their
own (or the HOSes) discretion. The changes to the prisoner console allow
them to coordinate with officers to get good value out of the implants
they've chosen for an implantee.

Gives antagonists an alternate way to get de-implanted, without external
help, that can only be granted at the fault of security. Wardens who
dish out implants must keep an eye on the people carrying them!
## Changelog
:cl: Rhials, MrMelbert
add: The Tracker implant has had its teleport beacon functionality
migrated to the new (cargo accessible) Beacon implant.
add: Teleport Blocker security implant, that prevents the implantee from
teleporting by any means. Purchasable from cargo.
add: Security implants may now be harmlessly self-destructed at the
Prisoner Management Console.
balance: The Tracker implant tracking radius has increased from 20 to 35
tiles. The Prisoner Management Console will track and display the area
the implantee is in as well.
balance: The exile implant now prevents implantees from operating
shuttle controls.
code: Various code improvements and removal of unused vars in the
Prisoner Management Console
code: The HUD slots for chem/tracking implants have been converted to
display any implant with the IMPLANT_TYPE_SECURITY flag and an
associated sprite.
spellcheck: Modifies various implant pad readouts, removing false
information and rewriting some sections.
/:cl:

---------

Co-authored-by: MrMelbert <kmelbert4@gmail.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[800ad77ed2...](https://github.com/Floofies/Skyrat-tg/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Monday 2023-12-25 12:18:10 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [mrc0mmand/systemd](https://github.com/mrc0mmand/systemd)@[c988ef4cf4...](https://github.com/mrc0mmand/systemd/commit/c988ef4cf435ffa50dc9d10d9b0e55d5685ac7b1)
#### Monday 2023-12-25 12:53:10 by Frantisek Sumsal

coccinelle: rework how we run the Coccinelle transformations

Turns out that the original way we did things was quite broken, as it
skipped a _lot_ of code. This was because we just threw everything into
one pile and tried to spatch it, but this made Coccinelle sad, like when
man page examples redefined some of our macros, causing typedef
conflicts.

For example, with a minimal reproducer that defines a cleanup macro in
two source files, Coccinelle has no issues when spatch-ing each one
separately:

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci main.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: main.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments
SPECIAL NAMES: adding _cleanup_free_ as a attribute

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci
logcontrol-example.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: logcontrol-example.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments

But when you try to spatch both of them at once, Coccinelle starts
complaining and skipping the "bad" code:

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci main.c logcontrol-example.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: main.c logcontrol-example.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments
SPECIAL NAMES: adding _cleanup_free_ as a attribute
remapping: _cleanup_ to an ident in macro name
ERROR-RECOV: found sync end of #define, line 44
parsing pass2: try again
ERROR-RECOV: found sync end of #define, line 44
parse error
 = File "logcontrol-example.c", line 44, column 21, charpos = 1719
  around = '__attribute__',
  whole content = #define _cleanup_(f) __attribute__((cleanup(f)))
badcount: 2
bad: #include <systemd/sd-journal.h>
bad:
BAD:!!!!! #define _cleanup_(f) __attribute__((cleanup(f)))

This was, unfortunately, hidden as it is visible only with
--verbose-parsing (or --parse-error-msg).

Another issue was how we handled includes. The original way of throwing
them into the pile of source files doesn't really work, leading up to
similar issues as above. The better way is to let Coccinelle properly
resolve all includes by telling it where to find our own include files
(basically the same thing we already do during compilation).

After fixing all this, Coccinelle now has a chance to process much more
of our code (there are still some issues in more complex macros, but
that requires further investigation). However, there's a huge downside
from all of this - doing a _proper_ code analysis is surprisingly time
and resource heavy; meaning that processing just one Coccinelle rule now
takes 15 - 30 minutes.

To make this slightly less painful, Coccinelle supports caching the
generated ASTs, which actually helps a lot - it gets the runtime of one
rule from 15 - 30 minutes down to ~1 minute. It, of course, has its own
downside - the cache is _really_ big (ATTOW the cache takes ~15 GiB).

However, even with the aggressive AST caching you're still looking at
~1 hour for one full Coccinelle run, which is a bit annoying, but I
guess that's the price of doing things _properly_ (but I'll definitely
look into ways of further optimizing this).

---
## [VasilisThePikachu/SS14.docs](https://github.com/VasilisThePikachu/SS14.docs)@[4feada28fb...](https://github.com/VasilisThePikachu/SS14.docs/commit/4feada28fbf0cdd543026992706dd770c4edfb35)
#### Monday 2023-12-25 13:45:31 by Kevin Zheng

Add atmos roadmap (#78)

# Roadmap For Atmospherics

## Background

Most atmos players currently agree that atmos is not very fun to play,
for some of the following reasons:

1. There is little content to play after round-start setup. Part of the
problem is that things like distro and TEG are "set up and forget".

2. Atmos can't actually rectify atmos problems in a reasonable amount of
time. For example, if there actually is a plasma leak, scrubbers
typically work too slowly resulting in the plasma inevitably being lit
before it can be cleaned up.

3. Atmos techs don't play with the rest of the station, preferring to
isolate themselves to produce a funny green gas that is only
particularly useful for shuttle bombing. Mechanics like this violate the
[fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md).
While these mechanics shouldn't be removed per-se, more focus should be
given to mechanics that increase interactions with the station, like
making sure the air is breathable and well-heated.

## Proposal

Make atmos more fun to play by adding more challenges and processes
semi-inspired by real life.

**An atmos tech's primary job is to keep the station livable and
breathable.** There are a lot of interesting real life challenges
associated with making this happen, not in the least of which is that in
space, every gas molecule wants desperately to escape into the cold of
space. There is also the challenge of keeping the station appropriately
temperature-regulated despite the cold outside and occasional plasma
fires inside.

Where it does not conflict with fun (see below), **incorporate realistic
processes and simulations**. As stated in the [fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md),
intuitive simulation makes for a better game. Having real-life analogs
for gas behaviors helps make both atmos more discoverable and intuitive
for new players and also caters to atmos nerds.

None of these realism additions require any sort of math to play. Only a
basic understanding of the following principles should be enough to
understand and play:

1. You should not be able to spin energy out of thin air.
2. When given a choice, gas flows from high pressure to low pressure.
3. When given a choice, temperature transfers from hot to cold.

### An Interlude on Realism

The chief objective of a game is to be fun to play, and not to be
realistic. Where realism conflicts with fun, fun should be chosen every
time.

**However,** games are most fun when players have a sense of agency
(their actions matter in determining the final outcome of the game) and
when their challenges are struggles are believable.

In order for players' challenges and struggles to be believable, the
game universe must obey a consistent system of rules and physical
limitations. It would not be fun if players have a way to *deux ex
machina* out of every imaginable problem (e.g. Nukies? Why don't we use
the magical remote control that makes all the nukies disappear? After
all, we have *spess magic*.) We're in space, and it should be hard to
get gases because they tend to escape into... you know... space. Not
every station should have a magical gas miner.

But guess what? It turns out that realism provides both a set of
interesting problems and a set of rules for how a universe should
consistently behave. So by making things more realistic, we get both
interesting mechanics and a set of consistent rules for free. Of course
realism doesn't trump fun, and if it is fun to make something that is
unrealistic (e.g. plasma gas), then we should always pick fun.
**However, where realism does not conflict with being fun, then we
should opt to be realistic because it provides a set of interesting
problems and consistent rules.**

After all, why do we say that *PV=nRT*? Shouldn't we make up a different
gas law because realism is bad?

## High-Priority Proposals

These proposals should be implemented first, because they have an
outsized impact on atmos balance as a whole.

- **Phase out gas miners for all upstream maps.** It doesn't make sense
that all stations have free and plentiful sources of gas, otherwise you
might as well be on a planet. This is a game that is literally set in
space. It would make sense to keep a few specialty miners, e.g. for
plasma, if a station is set on a plasma mining planet. But in general,
all other gases should be imported via gas canisters. Miners should
still be kept available for any forks that choose to use them.

- This solves problems (1) and (3). Maintaining a livable atmos would
involve work during the round beyond setting up distro to pipe gas from
miners. It would help increase interactions with other departments, such
as cargo and salvage as atmos needs to order gas.

- Ensuring a appropriate round-start supply of gas would make the game
playable without a functional cargo department.

- This would discourage fighting fires or atmos problems by wholesale
spacing a section. There is currently very little downside to spacing a
section to get rid of problems because of an unlimited gas supply.

- There is [overwhelming consensus on mappers for
this](https://discord.com/channels/310555209753690112/770682801607278632/1162179968915210280).

- As an interim or for very low pop-count maps, keep miners but make
them mine gas at low temperature that has to be heated up before use.
This preserves a bit of an incentive for atmos players to not space a
section at the first sign of trouble.

- **Globally increase MaxTransferRate** for devices that are not
flow-based, e.g. pumps.

- This solves problem (2). Among other things, it would make scrubbers
and other devices actually useful for combating atmospheric problems.
Currently players prefer to just space everything. Increasing this would
provide a feasible alternative.

## Medium Priority

- **Make all atmos devices flow-based.** This means driving gas flow as
a result of pressure differences created using pumps. The specific
offenders are currently any "pumped" device that is not a dedicated
pump, e.g. air vents, scrubbers, filters, and mixers.

- This addresses an issue about atmos intuition and accessibility.
Players should not have to understand the internal workings of the pipe
net system (e.g. a pipe is one big node, gases move between them). In
real life, a fan or pump creates a pressure difference, and pressure
differences drive gas flow. If you blow on one end of a straw, you can
expect it to come out of the other end, not get stuck in a pipe net.

- This also addresses (2). Instead of having a fixed upper bound on
volume transfer, transfer rates would always depend on the pressure
difference that you create.

- **Add maximum temperature and pressure limits for most devices.** It
does not make sense that you can contain the surface of the sun in your
pipes. Adding limits would encourage designing processes and systems
that work within reasonable constraints.

- Some "sub-optimal" setups are really unintuitive and wouldn't work in
real life due to temperature and pressure limits.

- There are some concerns about being able to run burn chambers and the
TEG. The screenshot below demonstrates a TEG that is capable of powering
an entire large-sized station (256.8 kW current output, the peak output
is quite a bit higher) with a maximum pressure excursion of 1600 kPa. It
shows that pipes that burst at reasonable pressures are entirely
consistent with having burn chambers. You just need to set them up
correctly.


![image](https://user-images.githubusercontent.com/3229565/274441724-712f4ebf-7440-4d81-879e-19aa29788822.png)

- This addresses problem (1), the "set up and forget" issue by adding
temperatures and pressures to monitor. It also allows the opportunity
for sabatoge.


- **Make heaters and freezers thermodynamically sound.** Keeping a
station properly heated or cooled is actually a substantial real-life
problem. Why deprive atmos techs an actual challenge that keeps gameplay
interesting? Because of the existence of generators like the TEG,
keeping things thermodynamically balanced is also a great way to prevent
infinite power hacks.

## Low Priority

- **Make station air flow-based.** Currently, air vents release air when
the pressure is too low, and by default scrubbers only scrub waste
gases. So if for some reason the station gets cold, there's no easy way
to cycle the air out and heat it up. Of course, you could set all the
scrubbers to siphon, heat your distro, and then set the air alarm to
fill. But that would just be describing a bad way of doing what real
life HVAC systems have always been doing: keep the air flowing.

- This addresses problem (2) by making it possible to better regulate
station temperature.

- **Make heaters and freezers binary.** Just like your central heating
and air conditioning circulate air through heat/cold coils, gases should
flow across heaters and freezers in order to exchange temperature.

- **Adding process-based alternatives to scrubbers and filters.** For
example, with gas reaction-based scrubbing processes, scrubbers with
limited uses, or physical processes.

- This addresses problems (1) and (3) by adding more content that is
directly related to the well-being of the station.

- One of the most pressing challenges in the real world is "how do you
separate different kinds of gas." Most current methods of gas extraction
are based on chemistry (e.g. real life carbon dioxide scrubbers contain
chemicals that react with CO2, pulling it out) or physical methods (e.g.
fractional distillation, where you cool down air in different stages to
get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for
new game play mechanics and industrial processes. This would also give
more opportunities to add gas-based reactions (i.e. more content).

- This does not advocate for removal of scrubbers and filters, but
rather makes it a mapper option, e.g. whether to use scrubbers at
round-start or make atmos set up a system depending on the desired level
of role-play.

- When set up correctly, these should have much higher processing rates
than scrubbers. This should give an incentive to set these up, e.g. on
longer rounds, while still keeping scrubbers as an option.

- This adds "optimization, tinkering, and creation of intricate builds."

- **Add gas condensation.** This would enable fractional distillation
and permit conversion between gas and the equivalent reagent.

- **Add pump efficiency curves.** Pumps have to work harder when they
create a larger pressure difference. As a result, pumping from 1 atm to
2 atm should be easier (read: faster) than pumping from 1 atm to 10 atm.
You could create a multi-stage pump, and indeed, that is what people in
real life do, at the trade-off of less throughput.

- **Breaking windows at high enough tile pressure differences.** To
handle explosions and resulting space wind without leaning on the
explosino system, and to encourage people to design burn chambers with
more controlled burns instead of always putting their pedal to the
metal.

- **Various QoL improvements** such as the RPD.

---
## [tired-wired/lobotomy-corp13](https://github.com/tired-wired/lobotomy-corp13)@[e23ea7b596...](https://github.com/tired-wired/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Monday 2023-12-25 14:41:46 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [tired-wired/lobotomy-corp13](https://github.com/tired-wired/lobotomy-corp13)@[294f764ad0...](https://github.com/tired-wired/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Monday 2023-12-25 14:41:46 by Coxswain

Adds distorted form (#1435)

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

makes suggested changes

updates comments

adds procs

adds stuff

---
## [k1n9bur93r/k1n9bur93r.github.io](https://github.com/k1n9bur93r/k1n9bur93r.github.io)@[7599159437...](https://github.com/k1n9bur93r/k1n9bur93r.github.io/commit/7599159437a375ca066354747f25093b76413e66)
#### Monday 2023-12-25 14:47:35 by k1n9bur93r

Blog entry: 
I think it’s fair to say that the defining metric of this year has been stress. Life stresses, work stresses, maybe even personal stresses. I have been able to learn so much this year, I’ve been kinda forced too. There are a lot of things that I wish I could have better executed, but at the end of the day I am no worse for wear, and I’ve gained a whole lot of experience. I guess that’s what life kinda starts to cycle into. I kinda hope not  though haha. I’ll leave that judgement for when I am older man. These past few days have been the first where I have not been driving myself off a cliff each week writing code and cleaning things up. I’m actually kinda impressed that I managed to crank out this site at all. It’s funny but despite all that effort the best thing about it is not the site itself, but being able to post from my iPhone with the action button. I would have only ever written like three ‘blogs’ otherwise! I’m not out of the woods yet for work, and afterwards I hope to burn some vacation days and give myself a bit of a break, but I really do wan’t to expand my site. I like having it, I feel that so much of me is online, but much like life so much of the spaces I do exist in are places that are not my own. Kind of like renting. I want to own a home. I’m still stuck in the system, but at least I can say that I own something in it. I hope everyone takes the time to reflect on what they learned this year, and take those notes with them. Best of luck! 
I think it’s fair to say that the defining metric of this year has been stress. Life stresses, work stresses, maybe even personal stresses. I have been able to learn so much this year, I’ve been kinda forced too. There are a lot of things that I wish I could have better executed, but at the end of the day I am no worse for wear, and I’ve gained a whole lot of experience. I guess that’s what life kinda starts to cycle into. I kinda hope not  though haha. I’ll leave that judgement for when I am older man. These past few days have been the first where I have not been driving myself off a cliff each week writing code and cleaning things up. I’m actually kinda impressed that I managed to crank out this site at all. It’s funny but despite all that effort the best thing about it is not the site itself, but being able to post from my iPhone with the action button. I would have only ever written like three ‘blogs’ otherwise! I’m not out of the woods yet for work, and afterwards I hope to burn some vacation days and give myself a bit of a break, but I really do wan’t to expand my site. I like having it, I feel that so much of me is online, but much like life so much of the spaces I do exist in are places that are not my own. Kind of like renting. I want to own a home. I’m still stuck in the system, but at least I can say that I own something in it. I hope everyone takes the time to reflect on what they learned this year, and take those notes with them. Best of luck!

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[f03084c1ca...](https://github.com/Time-Green/tgstation/commit/f03084c1ca61511b6c426602121a942966c2e76d)
#### Monday 2023-12-25 15:22:04 by LemonInTheDark

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
## [tichys/Foundation-19](https://github.com/tichys/Foundation-19)@[a666b103d3...](https://github.com/tichys/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Monday 2023-12-25 16:48:15 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [codenameMadhava/Sentiment_Analysis_](https://github.com/codenameMadhava/Sentiment_Analysis_)@[c72f880e61...](https://github.com/codenameMadhava/Sentiment_Analysis_/commit/c72f880e61925fd546b5d004e8aea19169e3d5b8)
#### Monday 2023-12-25 18:24:07 by codenameMadhava

Add files via upload

Project Title: Sentiment Analysis for Textual Emotion Classification

Description:

The Sentiment Analysis for Textual Emotion Classification project aims to develop a machine learning model capable of classifying the emotional tone of textual content into four categories: anger, fear, joy, and sadness. The project utilizes Natural Language Processing (NLP) techniques and sentiment analysis to understand and categorize emotions expressed in text.

Objectives:

Emotion Classification:

Implement a machine learning model to classify text into predefined emotional categories.
Explore and fine-tune hyperparameters to enhance the model's predictive accuracy.
Feature Engineering:

Enhance the feature set by incorporating additional features derived from the text data.
Experiment with techniques such as word embeddings, TF-IDF, and sentiment analysis to enrich the feature space.
Model Evaluation and Optimization:

Iteratively evaluate and optimize the model's performance on validation and test datasets.
Utilize techniques like grid search to fine-tune hyperparameters and improve overall model accuracy.
Ensemble Methods:

Investigate the effectiveness of ensemble methods, such as Random Forest or Gradient Boosting, to enhance the model's robustness and generalization capabilities.
Analysis of Misclassifications:

Conduct a detailed analysis of instances where the model makes mistakes to identify patterns and areas of improvement.
Use insights from misclassifications to inform further adjustments to the model.
Documentation and Reporting:

Document the project workflow, including data preprocessing, feature engineering, model development, and evaluation.
Provide detailed reports on model performance, including accuracy, precision, recall, and F1-score metrics.
Technologies Used:

Python: Leveraging popular libraries such as scikit-learn, pandas, and matplotlib for data manipulation, machine learning, and visualization.
Natural Language Processing (NLP) Techniques: Employing techniques like tokenization, stemming, and feature extraction to process textual data.
Machine Learning Models: Utilizing logistic regression and exploring ensemble methods for emotion classification.
Benefits:

Improved Understanding of Textual Emotion: The project enables a deeper understanding of how machine learning models can classify and interpret emotions expressed in text.
Enhanced Model Performance: Through fine-tuning, feature engineering, and ensemble methods, the project aims to achieve a highly accurate and robust sentiment analysis model.
Applicability: The developed model can be applied to various domains, such as social media sentiment analysis, customer feedback analysis, and emotion detection in online content.
This project provides a practical demonstration of sentiment analysis techniques and serves as a foundation for further research and applications in the field of natural language processing and emotion analysis.

---
## [ADHRPACKERSANDMOVERS/Karnal](https://github.com/ADHRPACKERSANDMOVERS/Karnal)@[3d81ac715b...](https://github.com/ADHRPACKERSANDMOVERS/Karnal/commit/3d81ac715bf65fb6e0504e4573b72ccb178f4612)
#### Monday 2023-12-25 19:25:36 by Rajesh soni

Update Packers and Movers in Karnal.docx

Packers and Movers in Karnal

ADHR Packers and Movers in Karnal prioritize customer satisfaction and ensure timely delivery of goods to their desired location. We have already served more than 15000+ customers and have safely moved their belongings. Our team of experienced employees takes care of your goods during the packing and moving process. To avail of our services, all you need to do is give us a call and we will take care of the rest. We are the Best Packers and Movers in Karnal.

Movers and Packers in Karnal

We are the Best Movers and Packers in Karnal and we always strive to provide excellent support services to ensure your complete satisfaction. We understand your requirements and plan everything accordingly. We take care of the documentation and always process written agreements with our clients, along with proper legal documents to avoid any confusion or disputes. We provide a transparent pricing structure and do not charge any unnecessary fees. Our client's satisfaction is our top priority, and we will do everything possible to make sure you are satisfied with our services. If you need any assistance, contact us and we will provide you with unparalleled services for any work.

Packers and Movers in Karnal.
If you're looking for Packers and Movers in Karnal, we are proud to say that we are among the best in the industry. We have efficient and refined strategies that guarantee satisfactory results when you hire our services. Our team is highly capable of fulfilling all your relocation needs, whether it's local or national.

Before preparing for your move, it's important to understand the different types of relocation, which are local and national shifting. There are certain factors to consider for each type, and our team can guide you on what to expect.

Agarwal Packers and Movers in Karnal.
Agarwal Packers and Movers in Karnal have served customers from all over India, whether it's residential, commercial, or industrial relocation. We use standard methods and techniques to pack your goods with quality packing material to ensure their safety during transportation.

You can also move your car or bike using our services for inter-city movements. We use special closed containers to transport your vehicle safely to your new home.

If you're a first-time mover, it's best to leave the job to experienced and professional packers and movers like us. It's a complex and exhausting process, and it can be expensive if not done correctly.

When looking for packers and movers, it's important to compare estimates. If a moving estimate is far below two other estimates, it could be a red flag that they are underestimating the job. The lowest bid offering companies can be either shady movers or inexperienced movers.

The moving charges will depend on the number of items you wish to carry along with the distance traveled. Typically, the approximate cost for moving starts at Rs. 6,000 for intra-city and Rs. 11,000 for inter-city.

Depending on the number of items to be loaded, the total time can range from one to three hours.

If you're worried about the moving process, we can help you figure out when to start packing, what size of vehicle you would need, and how long the process will take. Our team of professionals will provide all the necessary services, including packing, loading, moving, unloading, unpacking, and shifting all items with dedication and care.

Please find below the contact details for ADHR Packers and Movers in Karnal, Haryana, India: 
Mobile: 8262850010. 8262850044. 8262850046 
Website: https://aggarwaldomesticpackersandmovers.com 
Email: info@aggarwaldomesticpackersandmovers.com 
We offer a range of services including packing, loading, transportation, unloading, unpacking, local moving packing, office relocation, and warehousing services. 
You can also find us on various social media platforms such as.
Pinterest, YouTube, Tumblr, Instagram, Twitter, Facebook. Blog. Linked-in, Reddit
In addition, here are some cities around the Karnal area that we serve:
Karnal, Haryana, India, Panipat, Sonipat, Kurukshetra, Ambala, Yamunanagar, Saharanpur, 
Patiala, Chandigarh, Delhi, Ghaziabad,

#PackersandMoversinKarnal, #PackersMoversinKarnal, #PackersandMoversKarnal, #Karnal, #PackersMoversKarnal, #PackerinKarnal, #KarnalPackersandMovers, #KarnalPackersMovers, 
#MoversandPackersinKarnal, #MoverspackersinKarnal, #MoversandPackersKarnal, #MoversPackersKarnal, #MoversinKarnal, #KarnalMoversandPackers, #KarnalMoversPackers,
#AgarwalPackersandMoversinKarnal, #AgarwalPackersandMoversKarnal, #AgarwalPackersMoversinKarnal, #AgarwalPackersMoversKarnal, #Agarwal,
 #AgarwalMoversandPackersinKarnal, #AgarwalMoversandPackersKarnal, #AgarwalMoversPackersinKarnal, #AgarwalMoversPackersKarnal, 
#ADHR #ADHRPackersandMoversKarnal, #ADHRMoversandPackersKarnal. #PackersandMovers, #MoversandPackers, #PackersMovers #MoversPackers #ADHRPackersandMovers #ADHRMoversandPackers. #Packers #Movers #PackersandMoversNearMe, #MoversandPackersNearMe.

---
## [tony3fk/react](https://github.com/tony3fk/react)@[b6978bc38f...](https://github.com/tony3fk/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2023-12-25 19:34:53 by Andrew Clark

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
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[e3d3e8b71e...](https://github.com/EntranceJew/TTT2/commit/e3d3e8b71ebba5eb8cbfe0614c954503cee642e2)
#### Monday 2023-12-25 20:37:09 by EntranceJew

grenades

- added trajectory for grenade throws
- removed redundant Init/CreateGrenade, use baseclass
- renamed confgrenade vars to make more sense
- added UI to conf/smoke/firegrenade
- removed dead code in smoke entity
- brought in ttt_flame entity
- moved ttt_flame globals to game_effects library, affects C4
- fixed ttt_flame not utilizing offset from trace, as the intent seems to be
- allowed disarming players with impacts
- made discombobs bouncy
- grenade UI indicators in gameplay options
- fixed basegame bug where grenades would self-intersect on raytrace for ground searches
- smoke projectile packs in convars to game_effects
- smoke projectile no longer uses accessor functions
- smoke projectile centers itself by half of its radius to prevent floorsmokes
- hook for confgrenade explode
- particle dispersal from discombob
- consolidate ttt_smoke into Disipate and Remove
- force add PVS code (still doesn't fix ParticleEmitter shenanigans)
- smoke effects use same parameters, but smokegrenade convar differs
- ttt_smoke now utilizes the space better to fill the volume better even with maximum variance
- fires get funny particles and trails
- ttt_flame hitboxes adjusted their hitboxes are way too big
- new explosion sound Tim provided
- new fizzle sound edited together by me
- game_effects.Extinguish now plays a noise
- ttt_flame can no longer re-ignite
- PushPullRadius from conf moved to game_effects
- thirdparty menu
- vfire
- factored out game_effects.ScorchDown
- potentially ruined ttt_firegrenade_proj killing itself frame0 because extinguish might not know what to do with it
- reorganized BaseClass.Initialize for no good reason
- addon checker result ammended
- ttt_flame bringdown
- ttt_flame has netvars for new params
- startfires longer signature
- ttt_flame / SpawnFire has more accurate hitbox
- fire size / life span / spread / prevent discombob fling convars
- removed legacy renderer for fire, since smoke is broken, nobody gets to be happy
- smacking grenades makes explosions
- added changelog
- fixes from TimGoll
- renamed boom_ball to "electric_explosion"
- added more addonchecker items
- passes down the inflictor to pushpullradius
- documented extinguish hook
- gameEffects docs
- remove postround protection and redundant latch, correct trace offset
- don't tinker with the PVS if it isn't fixing problems
- it wasn't relevant because there IS no physics object right now
- all this for a little bit of not scorching in the wrong spot
- all this does is prevent repeat callbacks on the explode method on the client, sometimes
- back out cringe network changes
- replace scorch with PaintDown
- looping smoke sound global
- SmokeData color can now be manually overridden
- killed todos
- docs fixes
- added animation timers back in
- networked the var and run only in server to prevent double sfx
- networked grenade pin noise to all clients
- grenade pin noise for shot grenades
- quick grenade
- grenade damage scaling
- Use the ThirdParty Gui as a simple info panel for now
- Remove vFire convar and simply use vFire if installed

Co-authored-by: saibotk <git@saibotk.de>
Co-authored-by: Histalek <16392835+Histalek@users.noreply.github.com>

---
## [PanayotisManganaris/dwm](https://github.com/PanayotisManganaris/dwm)@[67d76bdc68...](https://github.com/PanayotisManganaris/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2023-12-25 20:42:51 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [iprtel/cppfront](https://github.com/iprtel/cppfront)@[cdf71bdca6...](https://github.com/iprtel/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Monday 2023-12-25 21:06:55 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[db0ea89db2...](https://github.com/Buildstarted/linksfordevs/commit/db0ea89db227319f52917e624cf58a7cad28deb1)
#### Monday 2023-12-25 22:09:47 by Ben Dornis

Updating: 12/25/2023 10:00:00 PM

 1. Added: It's pretty cool to find out what stuff others use, and why people love lists of tech
    (https://andreisurugiu.com/blog/new-tech/)
 2. Added: Markdown Tables Suck
    (https://jankremer.eu/micro/markdown-tables/)
 3. Added: Available for beta testing: Zotero for Android
    (https://forums.zotero.org/discussion/110371/available-for-beta-testing-zotero-for-android)
 4. Added: std::print in C++23
    (https://vitaut.net/posts/2023/print-in-cpp23/)
 5. Added: Sending free transactional emails with Cloudflare Workers
    (https://dhravya.dev/posts/sending-free-transactional-emails-cloudflare)
 6. Added: The future vision of Ruby Parser
    (https://rubykaigi.org/2023/presentations/spikeolaf.html)
 7. Added: A Christmas Story
    (https://danielbmarkham.com/a-christmas-story/)
 8. Added: Fixing my Yamaha Electone ME-50: An FM Synthesizer Home Organ from 1986
    (https://nicole.express/2023/resisting-the-urge-to-make-organ-jokes.html)
 9. Added: The joys of holiday coding
    (https://www.mostlypython.com/p/the-joys-of-holiday-coding)
10. Added: I love my Ioniq, but I would never buy another Hyundai | Digital Trends
    (https://www.digitaltrends.com/cars/hyundai-ioniq-warranty/)
11. Added: Constellations are Younger than Continents — LessWrong
    (https://www.lesswrong.com/posts/YMakfmwZsoLdXAZhb/constellations-are-younger-than-continents)

Generation took: 00:09:37.8444764
 Maintenance update - cleaning up homepage and feed

---
## [Sala/adventofcode](https://github.com/Sala/adventofcode)@[97f228c8ec...](https://github.com/Sala/adventofcode/commit/97f228c8ec99772a1736a8b5d002084f96679bd8)
#### Monday 2023-12-25 22:11:13 by sala

OMG THIS WAS A LITTLE HARDCORE

I was lucky enough that a few days ago I solved a puzzle from another year where I've needed to determine a line from two points. the good part is that I had an idea, the bad part is that I missed something and had trouble with big numbers. long story short part 1 took more than it should have.

for part 2 I didn't wanted to use an external library and started to do some calculations and try to find some formmula on how to determine the result. with some help/inpiration from reddit I've managed to write my own solution but it was a hell of a ride.

---
## [wonderinghost/Yogstation](https://github.com/wonderinghost/Yogstation)@[5c140d7624...](https://github.com/wonderinghost/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Monday 2023-12-25 22:19:24 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [samskivert/adventofcode](https://github.com/samskivert/adventofcode)@[28107ca300...](https://github.com/samskivert/adventofcode/commit/28107ca3009de33a4859179b0519b8a2fabe0a15)
#### Monday 2023-12-25 22:38:56 by Michael Bayne

Day 24.

Once again part one was easy and part two was bananas. I vaguely contemplated
constructing a set of (linear?) equations and unknowns and finding some way to
simultaneously solve them. It turns out many people did exactly this via
Mathematica or Z3. But I did not immediately see that if you solved the problem
for three (linearly independent) hailstones, you have solved it for 300 (the
size of the input). Had I realized it was just nine equations and unknowns,
that might have seemed less daunting than 900 equations and unknowns.

Then I started down the path of treating each hailstone as an equation in t and
trying to find three values t1, t2 and t3 such that three hailstones positions
at those times yielded colinear points (i.e. the line the rock has to travel to
hit them all). Once I knew that line, it would be straightforward to figure out
where the remaining hailstones intersected it.

Seeing that three hailstones was sufficient to determine the rock's line
probably should have clued me into the nine equations and unknowns from above,
but I am dumb, and was focused too much on my current potential solution.

Anyhow, the colinear business worked for the sample input, but the search space
using the real input was too large. (I should go back and calculate the range
of t's now that I have a solution.)

I beat my head against the problem again the next morning and made no progress.
So I decided to throw in the towel and read the Reddit megathread. Many people
there made the observation that you can subtract the rock's velocity from the
hailstones' velocities that gives you hailstones that all intersect at the
rock's position. That means searching candidate velocities (instead of
candidate times, like I had tried and failed to do). The velocities turned out
to be much smaller and thus tractably searchable.

Another guy helpfully pointed out that you can also project down to the
individual XY, YZ and XZ planes, find solutions for those and put them
together. Amusingly that guy was smart enough to realize that you could do
that, but did not realize that you can just two of the subspaces. Each subspace
gives you two components of the solution (e.g. XY gives the rock's x, y, vx and
vy). His code did a search in all three subspaces and used one component from
each.

I was going to come up with a way of enumerating increasingly large velocities
in x, y and z (like a plane of all points manhattan distance N from the origin
for increasing N), but I am lazy and tired of this problem. So I just pulled a
number out of my ass and search up to +/- that number in velocities, and what
do you know, the number I use is big enough to find a solution.

I also faffed around a bit due to infinite slopes, 64-bit integer overflow,
double precision errors, and some other bullshit. I eventually got a solution
working that I fully understand but would have taken a really long time for me
to come up with on my own. So yay for that, I guess.

---
## [jrcribb/evals](https://github.com/jrcribb/evals)@[f20c305dc7...](https://github.com/jrcribb/evals/commit/f20c305dc743eb545a57fd19b3b59426b9171465)
#### Monday 2023-12-25 22:49:27 by Erik Ritter

Add MMMU evals and runner (#1442)

## Eval details 📑

### Eval name

MMMU

### Eval description
A multi-modal version of MMLU published here:
https://arxiv.org/pdf/2311.16502.pdf

### What makes this a useful eval?
Tests a variety of subjects, along with image recognition and
comprehension

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

Multimodal, covers many subjects 

## Eval structure 🏗️

Your eval should

- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

### Eval JSON data

Dataset defined here: https://huggingface.co/datasets/MMMU/MMMU

### Eval Results

on `gpt-4-vision-preview`:

```
{
  "mmmu-accounting": 0.5333333333333333,
  "mmmu-agriculture": 0.6333333333333333,
  "mmmu-architecture-and-engineering": 0.16666666666666666,
  "mmmu-art": 0.7333333333333333,
  "mmmu-art-theory": 0.8333333333333334,
  "mmmu-basic-medical-science": 0.6,
  "mmmu-biology": 0.43333333333333335,
  "mmmu-chemistry": 0.43333333333333335,
  "mmmu-clinical-medicine": 0.6333333333333333,
  "mmmu-computer-science": 0.6333333333333333,
  "mmmu-design": 0.7666666666666667,
  "mmmu-diagnostics-and-laboratory-medicine": 0.3,
  "mmmu-economics": 0.6333333333333333,
  "mmmu-electronics": 0.4,
  "mmmu-energy-and-power": 0.36666666666666664,
  "mmmu-finance": 0.43333333333333335,
  "mmmu-geography": 0.4,
  "mmmu-history": 0.6666666666666666,
  "mmmu-literature": 0.9,
  "mmmu-manage": 0.6,
  "mmmu-marketing": 0.6333333333333333,
  "mmmu-materials": 0.26666666666666666,
  "mmmu-math": 0.5,
  "mmmu-mechanical-engineering": 0.23333333333333334,
  "mmmu-music": 0.36666666666666664,
  "mmmu-pharmacy": 0.7666666666666667,
  "mmmu-physics": 0.43333333333333335,
  "mmmu-psychology": 0.7,
  "mmmu-public-health": 0.8,
  "mmmu-sociology": 0.5666666666666667
}
Average accuracy: 0.5455555555555556
```

Note that this is slightly lower than the MMMU paper's findings of
`0.568`. There's likely prompt engineering that could be done to improve
this, but I'll leave that as an exercise for later

---
## [jrcribb/ripgrep](https://github.com/jrcribb/ripgrep)@[082245dadb...](https://github.com/jrcribb/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Monday 2023-12-25 22:59:41 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [pa1nki113r/Project_Brutality](https://github.com/pa1nki113r/Project_Brutality)@[4f5b06f63b...](https://github.com/pa1nki113r/Project_Brutality/commit/4f5b06f63b2f25719ff7c722a70f9f506770e477)
#### Monday 2023-12-25 23:00:33 by generic name guy

Did i ever tell you what the definition of insanity is?

Insanity is doing the exact same fucking thing over and over again, expecting shit to change. That. Is. Crazy.

---
## [jrcribb/terminal](https://github.com/jrcribb/terminal)@[86fb9b4478...](https://github.com/jrcribb/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Monday 2023-12-25 23:01:59 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [nrworld/guava](https://github.com/nrworld/guava)@[db3017fd25...](https://github.com/nrworld/guava/commit/db3017fd252e7484cd710653277fcc6b090c2d59)
#### Monday 2023-12-25 23:03:02 by cpovirk

Fix double-source-jar error during releases:

```
Building and deploying the android flavor (this may take a while)...
[ERROR] We have duplicated artifacts attached.
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-source-plugin:3.3.0:jar (attach-sources) on project guava: Presumably you have configured maven-source-plugn to execute twice times in your build. You have to configure a classifier for at least on of them. -> [Help 1]
```

I had fixed the same issue with _snapshot_ deployment in cl/559489724 (by no longer passing `source:jar` to `mvn`), but apparently that fix doesn't apply to _release_ deployment. I'm guessing that the relevant part of our release command is `-Psonatype-oss-release`, which (among other things) [activates a `maven-source-plugin` configuration change](https://github.com/google/guava/blob/a78bea41aedba50469641968ee3d98b24836e491/pom.xml#L329-L334): Presumably that introduces a second `maven-source-plugn` execution in much the same way as passing `source:jar` does.

I previously fixed a similar problem in jimfs (cl/536746714) by removing the "normal" `maven-source-plugin` configuration, leaving only the `sonatype-oss-release` configuration in the parent.

I don't remember whether I investigated removing jimfs' `sonatype-oss-release` configuration instead. Probably I should have at least investigated, since that's what we're going with here.

As best I can tell, this doesn't interfere with _snapshot_ source jars, which are produced even without `source:jar`.

(Notice that the configuration that may be the source of the problem was copied from the old `oss-parent` pom. This is at least the second time that that pom's configuration has caused us trouble, the other I recall being cl/492304151—well, and probably the aforementioned jimfs source-jar issue, too.)

This prepares for the release that contains the fix for https://github.com/google/guava/issues/6634, among other issues.

RELNOTES=n/a
PiperOrigin-RevId: 572327204

---
## [Monkooky/crawl](https://github.com/Monkooky/crawl)@[1e143483b6...](https://github.com/Monkooky/crawl/commit/1e143483b6627f70fcabc2f6040ccbc6713882da)
#### Monday 2023-12-25 23:20:24 by Skrybe

Xom-themed vaults (#2616)

[The first:] Inspired by the Xom worshiping daevas that can generate in
the Abyss. Contains daevas that call on Xom to smite the player, dancing
holy weapons, and chaos effects through apocalypse crabs and chaos
weapons wielded by the angels and daevas.  Some angels that bored Xom
have been turned to holy swine.

[The other:] Undead Xom worshipers have built a deep shrine (or maybe
they just took over a temple to Yred/Kiku?). Some of the followers are
wielding chaos weapons, a few dancing draining weapons are wielding
themselves, and cacodemons will provide plenty of opportunity for
hilarious mutations. The temple is led by mummified Xom priests
in the back.

[Committer's note: Cleaned up both headers heavily. Minorly nerfed the
Abyss vault. Converted the Crypt end into a regular D + Depths vault and
heavily lowered its derived undead / skeletal warrior spam, leaning more
on regular D + Depths chaos + demons (and some MuCks), and with a touch
of Xom's standard messy decor. Even when taking out the wide number of
demons harmless by depth, I'm ruling out cacodemons and chaos brand being
a noticeable part of the broad and notably focused Crypt end sets. D and
Depths have chaotic / demonic monsters and undead themes plenty to cover
for the union, and we could do a lot more with juxtaposition in bigger
vault themes anyway.]

---
## [imageworks/oiio](https://github.com/imageworks/oiio)@[64248a6e52...](https://github.com/imageworks/oiio/commit/64248a6e52c00e96b857756520edf539b933698d)
#### Monday 2023-12-25 23:54:52 by Larry Gritz

feat(ImageBuf): make IB::Iterator lazy in its making the image writable (#4033)

Historically, ImageBuf has provided Iterator for writing to mutable IB's
and ConstIterator for reading into IBs. If you initialized an Iterator
to an IB that was ImageCache-backed (and therefore by definition not
mutable), it would convert the IB to the mutable kind (basically by
allocating the memory and reading the file through the IC, thus freeing
the IB of its dependence on the cache.

An important bug was fixed by PR 3997, which kinda proved that people
were not depending on this behavior, since it would tend to fail. But it
also got me thinking about to what degree the whole Iterator vs
ConstIterator was really necessary, or did it just make things harder
for users.

In this proposed patch, we change the Iterator behavior so that instead
of immediately making the IB writable as soon as the Iterator was
instantiated and associated with the IB, we instead treat it as a
ConstIterator UNTIL it actually tries to write a value, at which point
we ensure that the IB is writable.

The bottom line is that this seems to work. If you don't want to have to
think about Iterator vs ConstIterator, you don't have to. Iterator is
fine. If you don't actually write into any of the pixels, it behaves
just like a ConstIterator, including being perfectly happy with an
IC-backed IB. Performance metrics indicate that there is NO penalty for
doing so -- if you are only reading pixel values, traversing an IB with
Iterator is the same speed as doing it with ConstIterator.

I had one sleepless night after implementing this when suddenly I
realized that this was totally not thread-safe, that somehow multiple
iterators traversing the same IB would screw each other up if one of
them wrote to a pixel and converted the image. So I put in a test to
have many threads concurrently traversing the same IB, some with
ConstIterator, some with Iterator but only reading, and some with
Iterator and writing. I have not been able to trigger any failures or
crashes. It seems fine. (I did use the mutex a little more aggressively
than before.)

Why is this not as dangerous as I thought? Mainly because once an
iterator (of either variety) thinks it's dealing with an IC-backed
ImageBuf, basically, it will just happily keep using the IC all on its
own, even if the IB that it's supposedly traversing has, because another
thread's iterator has written to a pixel, "localized" the image and
severed the IC dependence. Then if it also needs to write, it will
(safely, because of a mutex) see that the image is already
localized/writable, and start using that representation.

So herein lies a very important caveat about using IB iterators: If you
have multiple iterators traversing the same IB and any of them are
*writing* to the image, the iterators may not see a globally temporally
consistent version of the image. Put in plain English: iterators that
are strictly reading may see an IC-backed disk image as it was on disk,
and not as it has since been modified by a different active iterator. So
if you are modifying an image in place, beware of using multiple
iterators, because a reading iterator may or may not see the changes
that a writing iterator made to a pixel value.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [robertshepherdcpp/christmas_challenge](https://github.com/robertshepherdcpp/christmas_challenge)@[b1ff95fec8...](https://github.com/robertshepherdcpp/christmas_challenge/commit/b1ff95fec8c80d0decf3ad0da0a52ca8f942c09a)
#### Monday 2023-12-25 23:59:17 by rshepherdcpp

Merry Christmas everybody! I have had a good christmas today I am currently writing this at 11:48 PM making the last of christmas day! currently have only 11 minutes left as it just turned 49. This morning I had presents from TEMU and in the afternoon at about 3:15 after the kings speech had my other presents which mainly consisted of PANDA FRESH goods. Now I am doing a bit of looking at all of my projects that I made this year, and reflecting on my year, the hardships and the celebrations. I am currently listening to 100 christmas songs on spotify and having good fun with my old projects and making little corrections to them! For instance I was playing sfml_chess which I think is public on github. My favourite christmas song, now on christmas day 2023 is the fairytale of new york, walking in the air or something similiar. If you are not me reading this, well this may seem confusing but it is an easy way to go back and see notes. Some of the most notable c++ things that I did this year was that i went to c++ on sea!!! It was an extremely good experience as the talks were great and also the venue was spectacular. I am getting tired now! Some things that I got today were, two humidifiers, two mic's, LED USB light, investor book becuase I got a stock in NIO for 8.40, so I now own my first stock! In the future with c++ I want to do some more embedded system things and also some more 3d graphics things, I bought this android chip of TEMU for a cheap price and I want to make use of that. Also my current hobbies include Mandarin Chinese. Well in the future we will see what I will have done. This year I tried to do a contribution every day, but then when I got back to school I was very busy but now I have a lot more time! So future Robert: keep studying and working towards your future buisness ideas. Thankyou! Bye!

---

