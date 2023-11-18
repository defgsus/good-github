## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-17](docs/good-messages/2023/2023-11-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,596,808 were push events containing 3,800,204 commit messages that amount to 284,009,658 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [mgiota/kibana](https://github.com/mgiota/kibana)@[cd909f03b1...](https://github.com/mgiota/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Friday 2023-11-17 00:03:26 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [robtfm/bevy](https://github.com/robtfm/bevy)@[ab300d0ed9...](https://github.com/robtfm/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Friday 2023-11-17 00:12:46 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[389d1e5669...](https://github.com/Latentish/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Friday 2023-11-17 00:52:05 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are: 
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[7fce8cd805...](https://github.com/Fikou/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Friday 2023-11-17 01:17:08 by san7890

Codifies male goats not having an udder (#79722)

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

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [dsellers94/Unfracture](https://github.com/dsellers94/Unfracture)@[1f4d3ffd47...](https://github.com/dsellers94/Unfracture/commit/1f4d3ffd4788e224302bbc0a7e1e011eaf48161f)
#### Friday 2023-11-17 01:17:37 by dsellers94

Having kindof a bitch of a time getting forcefields or pushing actors or falling actors to behave the way I want. I think I need to abandon the idea of using unreal mesh actors to interact with the RMC meshes and focus on a custom forcefield like implementation.
The problem with that is collisions; we either recaculate the forces based on new node posistions and they go all fucking wonky snapping
and forth, or we keep them based on the undeformed node positions and the edge of the sphere doesn't match up. What if we just cut off the force when it reaches the edge of the compact range?...
I'll figure it out, but this is key to how the RMC meshes will work in game so it's holding up the Refact/Art/Mesh Migration tasks I want
to be working on. If I can get a good system for custom acctors interacting with the mesh that will solve all the problems with
each actor type behving differently and I can dispense with overlap check entirely which would be awesome.

---
## [kriegaex/xalan-java](https://github.com/kriegaex/xalan-java)@[4af37e7a84...](https://github.com/kriegaex/xalan-java/commit/4af37e7a84a81f59af991a5a887e2e88e540d7b2)
#### Friday 2023-11-17 01:45:25 by Alexander Kriegisch

Improve Maven Shade and Assembly usage, part 2 (#123)

* Ignore IntelliJ *.iml project files

* Fix Maven Shade usage

Shade no longer runs on top level, but only in module 'xalan' where it
is required. Modules 'xalan', 'serializer', 'samples' are now
dependency-managed.

* Exclude jboss-rmi-api_1.0_spec from binary distribution

Actually, I am not sure if the Xalan maintainer really wants to exclude
it or have it in the distro as a transitive dependency for the 'samples'
module. Because it was excluded before my changes in this PR, I am
excluding it here, too, to avoid breaking changes. Another way to
achieve this would be to declare the dependency as 'provided' in the
'samples', but this over-use of 'provided' in this project seems odd to
me. 
    jkesselmn adds: `Provided` was a quick kluge; some library jars
    that weren't packaged into assemblys by the ant build were being
    copied by the mvn build until I added this. Needs to be rechecked,
    and there is probably a better way to express it in mvn.

* Bump JUnit to 4.13.2

The old version 4.11 has security issues. Actually, the dependency could
be removed altogether, because there do not seem to be *any* automated
tests in this project.
    jkesselmn adds: The intent is that there will be. I'd rather declare it now,
    rather than wait for first use.
 
* Fix and improve site generation

- Fix typo (missing '$' in '${project.version}') I forgot to commit
  before.
- Use 'excludePackageNames=xalan2jtaglet' to avoid hen vs. egg problem,
  having to build and install the 'xalan2jtaglet' module before building
  a site. That is ugly and unnecessary sacred knowledge for new
  developers cloning the repo and building for the first time.
    jkesselmn adds: Our javadoc does use that otherwise-missing taglet
    (which is why we decompiled it and are carrying it here as a stopgap).
    Site depends on the javadoc, so this jarfile does need to be present
    before then. I wasn't sure how best to disentangle it short of doing
    more inter-module dependencies; if this works, great!
 

* Remove commented-out plugins, fix whitespace issues

Again, there were tabs mixed with spaces and unclean indentation.
    jkesselmn add: Sorry. I need to get my XML Emacs configuration 
    switched to spaces-only indentation, rather than trying to remember
    to normalize spaces.


* Fix source assembly

Replace '${project.build.directory}' - i.e. 'target' - by
'${project.basedir}', because we are not looking for sources in the
build directory. Now, the output resembles a source distro.

Actually, I have no idea why the original Apache source assembly
descriptor looks like that, at first glance it does not seem to make a
ton of sense.

---------

Co-authored-by: Joe Kesselman <131899227+jkesselm@users.noreply.github.com>

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[ecbf87a62a...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/ecbf87a62a1453ea5ebea95325203e099a3a75c3)
#### Friday 2023-11-17 01:47:21 by Mario Kleiner

PsychOpenXR: Add initial eyetracking via HTC SRanipal.

Requires SRAnipalMex to work and on the path, otherwise standard OpenXR eyetracking is
used. The mex file and source code is not yet included in the Psychtoolbox distribution.

This works with and requires the HTC proprietary SRanipal eye tracking api for MS-Windows,
in combination with a supported HTC HMD, e.g., HTC Vive Pro Eye (tested) or HTC Vive Cosmos
or HTC Vive Focus 3 with eye tracker hardware extension, the latter two untested, but assumed
to work in the same way.

It allows binocular eye tracking for left and right eye separately, returning two separate eye
gaze samples. Additionally a 3rd combined "cyclops eye" sample is returned, which is the fusion
or average of the two eye gaze samples, similar (identical?) to what HTC's implementation of
the OpenXR XR_EXT_eye_gaze_interaction extension returns as sole eye pose.

Implementation notes:

While OpenXR eye tracking with the standard OpenXR extension only works with a maximum
sampling rate of 60 Hz, ie. blocking the calling code for approximately 16 msecs for each
query in PsychVRHMD('PrepareRender') or PsychOpenXRCore('GetTrackingState', ..., 4), this
works with up to native sampling rate of the eyetracker, in this case 120 Hz / one sample
every approximately 8.3 msecs. As it turns out, one needs to use the callback api to get max
rate and minimum latency/overhead, where our callback is called from SRanipals own thread.
With the non-callback api's it is always blocking calls with 16 msecs+ duration resulting in poor
performance. The latter seems to be what HTC's implementation of OpenXR eyetracking does.

The HTC proprietary api delivers more detailed info than current official OpenXR extensions,
so both from a performance perspective and richness of information perspective it is clearly
perferrable to use the HTC proprietary api when available on a HTC HMD. The quality of the
api docs is horrifying however, and often faulty, so using it is somewhat a pain in the ass.

The type and units of returned information from SRanipal is different from what OpenXR
returns or uses, so some hacks had to be used to sort-of convert to OpenXR compliant format.

Currently the raw gaze samples are not 7 component vectors with eye position (x,y,z) and
orientation quaternion (rx,ry,rz,rw), but only 6 component vectors with orientation encoded
differently, and some shady matrix math hacks to get a sort of usable / sort of ok'ish gazeMat
matrix for eyegaze out of it. From that we derive other info like global gaze matrix, 3D eye
gaze vectors and 2D (x,y) gaze sample positions the usual way via the code shared with
regular OpenXR gaze tracking.

Some oddities - the reason for these is totally unclear:

- We need to switch some signs in the math - Is it a bug in HTC's runtime? A feature? A quirk?
I don't know.

- Eye center of the left eye seems to be stored in right eye, and vice versa, but the end result
wrt. 2D gaze position is the same, and the 3D gaze vectors originate in puzzling locations but
point to and converge in the correct gaze location. Again, could not find out why.

---
## [Miltonshaikh303/Miltonshaikh303](https://github.com/Miltonshaikh303/Miltonshaikh303)@[f87205f181...](https://github.com/Miltonshaikh303/Miltonshaikh303/commit/f87205f181f3317317ddfd4a1ea2f36318b3f1f5)
#### Friday 2023-11-17 02:03:06 by Miltonshaikh303

Update README.md

<html>
<head>
    <title>My Writings</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: lightblue;
        }
        h1 {
            text-align: center;
            color: white;
        }
        .container {
            width: 80%;
            margin: auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .card {
            width: 30%;
            margin: 10px;
            padding: 10px;
            border: 1px solid black;
            box-shadow: 5px 5px 5px grey;
            background-color: white;
        }
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card h3 {
            text-align: center;
        }
        .card p {
            text-align: justify;
        }
        .card button {
            display: block;
            width: 100%;
            margin: 10px auto;
            padding: 10px;
            border: none;
            background-color: green;
            color: white;
            font-size: 20px;
            cursor: pointer;
        }
        .card button:hover {
            background-color: darkgreen;
        }
        .footer {
            width: 100%;
            margin: 20px auto;
            text-align: center;
            color: white;
        }
    </style>
</head>
<body>
    <h1>My Writings</h1>
    <div class="container">
        <div class="card">
            <img src="story1.jpg" alt="Story 1">
            <h3>Story 1: The Adventure of Tom and Jerry</h3>
            <p>This is a story about the famous cat and mouse duo, Tom and Jerry, who go on an exciting adventure to find a treasure hidden in a mysterious island.</p>
            <button onclick="pay(1)">Pay ₹50 and Read</button>
        </div>
        <div class="card">
            <img src="story2.jpg" alt="Story 2">
            <h3>Story 2: The Mystery of the Haunted House</h3>
            <p>This is a story about a group of friends who decide to explore a haunted house, only to discover that there is more to it than meets the eye.</p>
            <button onclick="pay(2)">Pay ₹50 and Read</button>
        </div>
        <div class="card">
            <img src="story3.jpg" alt="Story 3">
            <h3>Story 3: The Journey of the Little Prince</h3>
            <p>This is a story about a young prince who leaves his planet and travels across the universe, learning valuable lessons from different people and creatures he meets along the way.</p>
            <button onclick="pay(3)">Pay ₹50 and Read</button>
        </div>
    </div>
    <div class="footer">
        <p>© 2023 by My Writings. All rights reserved.</p>
    </div>
    <script>
        // This is a dummy function that simulates the payment process and redirects the user to the corresponding story page
        function pay(id) {
            alert("Thank you for your payment. You will be redirected to the story page shortly.");
            window.location.href = "story" + id + ".html";
        }
    </script>
</body>
</html>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[caa13c44af...](https://github.com/jjpark-kb/Skyrat-tg/commit/caa13c44af926e36843fdeb8c50460d6566a6cd7)
#### Friday 2023-11-17 02:09:41 by SkyratBot

[MIRROR] Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished [MDB IGNORE] (#25038)

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

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

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[318d5b38d7...](https://github.com/jjpark-kb/Skyrat-tg/commit/318d5b38d734129579050a98107b044cfb2791e2)
#### Friday 2023-11-17 02:09:41 by SkyratBot

[MIRROR] Fixes Relay Attackers Misfire [MDB IGNORE] (#25039)

* Fixes Relay Attackers Misfire (#79731)

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

* Fixes Relay Attackers Misfire

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [TwistedCicrularConvexLens/tgstation](https://github.com/TwistedCicrularConvexLens/tgstation)@[d751e1c642...](https://github.com/TwistedCicrularConvexLens/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Friday 2023-11-17 02:31:45 by DaCoolBoss

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
## [TwistedCicrularConvexLens/tgstation](https://github.com/TwistedCicrularConvexLens/tgstation)@[a5fabd8819...](https://github.com/TwistedCicrularConvexLens/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Friday 2023-11-17 02:31:45 by Profakos

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
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[5761091212...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/57610912121327266d1b5b47eb6d93bfb33d8362)
#### Friday 2023-11-17 02:41:12 by SkyratBot

[MIRROR] Revert "if you die in a mech you are ejected" [MDB IGNORE] (#25051)

* Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

* Revert "if you die in a mech you are ejected"

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[590e8cb752...](https://github.com/FalloutFalcon/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Friday 2023-11-17 03:16:23 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Nerwyn/service-call-tile-feature](https://github.com/Nerwyn/service-call-tile-feature)@[d52a89703a...](https://github.com/Nerwyn/service-call-tile-feature/commit/d52a89703a408732bb0796148994887ebb52a5ea)
#### Friday 2023-11-17 03:53:59 by Nerwyn Singh

more debug logging because what the fuck this makes no fucking sense fuck you

---
## [peff/git](https://github.com/peff/git)@[52655d8b91...](https://github.com/peff/git/commit/52655d8b911d797ace4dc2bcc78c203ab28c1c29)
#### Friday 2023-11-17 04:12:33 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[bed92e193c...](https://github.com/JohnFulpWillard/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Friday 2023-11-17 06:03:21 by san7890

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ba17173a65...](https://github.com/pytorch/pytorch/commit/ba17173a65cbf590b4b8286178cd5860560a2969)
#### Friday 2023-11-17 06:08:26 by voznesenskym

Update base for Update on "AOTAutograd: handle set_(), detect metadata mutations that cancel out"

This should be enough to get voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.




cc voznesenskym penguinwu EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng wenzhe-nrv jiayisunx chenyang78 aakhundov kadeng

[ghstack-poisoned]

---
## [AstralWavefieldAi/Skyrat-tg](https://github.com/AstralWavefieldAi/Skyrat-tg)@[248e30344b...](https://github.com/AstralWavefieldAi/Skyrat-tg/commit/248e30344b49f69cdbfbea62ed0d8f2853a70547)
#### Friday 2023-11-17 06:52:02 by SkyratBot

[MIRROR] Makes Telekinesis + Russian Revolver Interaction more fair [MDB IGNORE] (#25042)

* Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

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

* Makes Telekinesis + Russian Revolver Interaction more fair

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Alexander-Aghili/Personal-Website](https://github.com/Alexander-Aghili/Personal-Website)@[87caaa607e...](https://github.com/Alexander-Aghili/Personal-Website/commit/87caaa607eb709cc258b274af3eeb229c2b4b542)
#### Friday 2023-11-17 06:57:10 by Alex

I hate React, I hate nextjs, I really hate CORS. This shit fucking sucks balls I wish it was not this shit

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[2ffa4b4f9a...](https://github.com/Kapu1178/daedalusdock/commit/2ffa4b4f9a013091d9115291ce845abb5241cfcb)
#### Friday 2023-11-17 07:43:33 by Rimi Nosha

Makes Sec EVA Storage Use Sane Accesses (#652)

* Oh dear god I forgot you guys don't have new access

* AH SHIT, I FORGOT A WORD

---
## [notJoon/gno-core](https://github.com/notJoon/gno-core)@[24d89a4f5d...](https://github.com/notJoon/gno-core/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Friday 2023-11-17 07:46:37 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [brassmaster2357/Cardgamecard](https://github.com/brassmaster2357/Cardgamecard)@[452d220412...](https://github.com/brassmaster2357/Cardgamecard/commit/452d220412bbcacee619933342658b33d773a082)
#### Friday 2023-11-17 07:54:41 by Gopherdays

BRAAAIIIIN BLAAAAAAASSSSSST!!1!!1!!1!

oh. my. goodness.
you don't even understand
I have found the solution to the biggest pain in my ass
CardsScript can go suck an egg because IT CHECKS THE CURRET SCENE INSTEAD OF RELYING ON EVENTLOADER
this may not seem like a big deal but this solution makes me feel like an actual programmer instead of some uneducated attempt at being one

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[a666b103d3...](https://github.com/Foundation-19/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Friday 2023-11-17 07:59:42 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [annihilatorrrr/terminal](https://github.com/annihilatorrrr/terminal)@[86fb9b4478...](https://github.com/annihilatorrrr/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Friday 2023-11-17 08:42:26 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [TheDailySimile/ReticenceVat](https://github.com/TheDailySimile/ReticenceVat)@[1baf971e72...](https://github.com/TheDailySimile/ReticenceVat/commit/1baf971e7244c96b6354df07131f0a942333cba5)
#### Friday 2023-11-17 09:30:02 by The Daily Simile

Create I'm The Jackal of Psyche Thought as My Foxing Life.html

[{Genkai,Adam,Felza,Marlee,Blaine,Ayub,Sakura,Eunji Tanaka
Zoi,Mahina,Guang,Gus,Sheena,Quasar,Marc,Muntasir Tanaka
Blossom,May,Adebayo,Dentarou,Chija,Chaewon,Giovanni,Ackgel Berlitz
Stuart,Jason,Imani,Dawn,Romelu,Luis,Enkhtuya,Rumla Berlitz}@HoF{Ghost-Fairy}
Brock@CoOrdinator,Sandra@P.Doctor Slate
Peniel@Psychic-Dark,Mallow@Psychic-Dark Ortiz
Ingemar@P.Doctor,Magnus@P.Doctor Iptil
Gary@CoOrdinator,Blythe@P.Doctor Oak
Drew@Water-Ice Blackmore
{Oumou,Nihul,Dolores,Errol,Brishna,Batzorig,Rabia,Yerkebulan Ketchum
Lixue,Rakim,Ash,Nirja,Itxaro,Isidro,Imanol,Ivette Ketchum
Ionut,Blooma,Rhys,Hatsumi,Yerkebulan,Ophira,Weayaya,Hua Ketchum
Saengdao,Acadia,Cuong,Seth,Ojasa,Ushi,Milintica,Ole Ketchum
Zed,Zeltzin,Haithem,Wijdan,Oswald,Pearl,Demyx,Yadira Latham
Kibwe,Lyra,Ozlem,Leo,Ezzard,Kianga,Kealohi,Osman Latham
Freesia,Umbel,Misty,Ephraim,Fortuna,Uzuri,Meryl,Ezekiel Latham
Sekou,Nachum,Itzel,Yagmur,Praset,Khayum,Aruru,Mizn Latham}@HoF{General}
Daisy@Administration,Violet@CoOrdinator,Lily@CoOrdinator,Poppy@Water-Ice Waterflower]@Pebblefog,Mintale
....
[Tracey@P.Agent Skechit]@Duskneon,Paldea

🐺@frown : "given your inclinations Dase and the contract you have earthed with that..Jackal of Perspective#..As I'm..the Fox of Statistics,#,..Daisy un..long,Tracey shakes..lot,#,..you must discharge the duty of Administrating your clan's matches and customers..for reality's sake#..and your salary can be handled by that Jackal given you can generate your own evaluation..out of independence..across planes.."
Daisy@frown : "in terms of self admission of an instrument for heuristical gymnastics yeah#..DaisyDevil,#,..Daisy un..long,#,..let's see these are regulations and names that subscribe their forms..the less benedictive on permutations yeah#..Dais Yoked Panorama on Self,#,..Daisy un..long,#,..
consciousness..of which self
no more i..how then else
thus desire..say how i..
will be me..
on your time yeah why are you so afraid of selves.."
Scheduled Opponents& Customers@outcry : "help!A Devil of factors is disguising as a Daisy of conceptor#..DaisyDevil,#,..Daisy un..long,#,.."
Tracey@thoughtful : "ofcourse i'll only put my money on the stock of emotions why.."
Opposite Forms across desirous planes@jealous : "hmm..how could that devil be the one to establish a self as a jackal of conviction hum.."
Similar Forms across desirous planes@frustrated : "how could that jackal fox self doubts on anotherness that we couldn't#.."
Metaheuristics of non Desirous Planes@giggle : "Look in my EYES..
What do you see?..
Am i of your MEH!
Thus i circumvent method's anger..and security's jealousy..
As i'm the Jackal of Verity..
Hence Am Fox of Penalty/Oh Devil of Equation handle you soul's granularity..
As i'm..the Jackal of Amity#..I Foxed The Devil of Reality/Bein' the jackal of symmetry/As..i'm..the Fox of History,#,..Daisy un..long,Tracey shakes..lot,#,.."

---
## [cyphar/runc](https://github.com/cyphar/runc)@[2531a13881...](https://github.com/cyphar/runc/commit/2531a138811fa49db1cacdac87db230d929c966b)
#### Friday 2023-11-17 09:47:19 by Aleksa Sarai

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
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [morrowwolf/tgstation](https://github.com/morrowwolf/tgstation)@[0f5d14e68b...](https://github.com/morrowwolf/tgstation/commit/0f5d14e68b19111592301efe52a03de80aced61e)
#### Friday 2023-11-17 09:52:02 by Ben10Omintrix

Mook village and basic mook refactor (#78789)

## About The Pull Request
refactors mooks into basic mooks and re-adds them to the game

## Why It's Good For The Game
this refactors mooks into basic mobs and re adds them to the game. mooks
are now a part of lavaland. they come as a part of a random ruin which
consist of a entire village of friendly mooks. Mooks will aid players
but they will still attack ashwalkers because of some troubled history
between them.

![mookvillage](https://github.com/tgstation/tgstation/assets/138636438/ad1c5d63-c168-475a-a85d-b727dff43e7b)

mooks are a very diseased specie. nanotrasen discovered a small tribe of
mooks and cut a deal with their tribal chief to aid ss13 miners in
exchange for medical supplies.

tribal chief in his decked out home

![tribalchief](https://github.com/tgstation/tgstation/assets/138636438/cc0e0a11-9bf0-4322-b3ae-c7be43092ee8)

male mooks go out and mine and haul ore off back to their village. they
will deposit ores into a stand which is managed by another mook. they
will all return to their village to rest once a lavastorm comes.

![mookstand](https://github.com/tgstation/tgstation/assets/138636438/c7adbf4e-6322-4347-acfc-4e8d45aff798)

players can use this stand to withdraw any ore they like

![mookui](https://github.com/tgstation/tgstation/assets/138636438/a1318be8-50f7-49b2-827c-97bafdb2488a)

female mooks will stay behind in the village to guard it from
ashwalkers. they will also heal male mooks when they come back from a
long day of work. the tribal chief is a bum and chooses not to go out
and mine. he will stay behind in the village and issue commands to his
people rather than work

the village also has its own bard! he follows player visitors and plays
nice music for them while they are in the village (although he is not
very talented).

![mookbard](https://github.com/tgstation/tgstation/assets/138636438/5123e492-6657-4755-9dc7-ab94d4beb554)

he is still a warrior at heart tho so he will be smashing his guitar
over ashwalker skull

![mookshmash](https://github.com/tgstation/tgstation/assets/138636438/bf211bf0-e963-4dbb-b004-e653e06e3974)




## Changelog
:cl:
refactor: mooks are now basic mobs. please report any bugs
feature: added mook village to lavaland ruins!
/:cl:

---
## [morrowwolf/tgstation](https://github.com/morrowwolf/tgstation)@[3e554bdab3...](https://github.com/morrowwolf/tgstation/commit/3e554bdab3ae7ffff4bd9090b71dc0b3666f081f)
#### Friday 2023-11-17 09:52:02 by Jacquerel

Flesh Spiders Regenerate + QoL (#78704)

## About The Pull Request

Replaces the Healing Touch component on Changeling-spawned Flesh Spiders
with the Regenerator component, as the comment helpfully suggests.
Flesh Spiders can no longer touch themselves to heal, instead they
automatically begin regenerating their health if they go four seconds
without taking damage. It takes 6 seconds to fully regenerate, so 10
seconds to fully heal from the edge of death (less if you're not that
injured).


![image](https://github.com/tgstation/tgstation/assets/7483112/37faca55-35fe-48dc-a3ed-03f4b79860bd)

Also I changed the sprite for flesh spider eggs to a different one we
already had rather than regular spider eggs tinted red, just because I
felt like it.
Would be cool to give the spiders their own sprite some time, but that's
for another PR.


![image](https://github.com/tgstation/tgstation/assets/7483112/8ec286c4-46dc-4aec-aa98-cb4e4e432690)
_Additionally_ the flavour text for flesh spiders was kind of messed up
by being shoved into the objectives box and claiming that it was a
directive from a spider queen you don't have, so I gave them their own
slightly different antag datum to compensate.
It also actually mentions how you heal yourself, which previously was
down to trial and error or codediving.

In the course of doing this I decided to just... move flesh spiders to
their own type path. It _sort of_ made sense for them to be part of the
giant spider typepath, but they keep being modified by changes targetted
at "balancing the Giant Spiders antagonist" which this mob isn't related
to and doesn't have any reason to follow. The fact that a mob has
similar stats to another one isn't automatically a reason to share a
typepath, and now that I have looked a little at this mob I'm sort of
interested in branching it further away from "it's a spider mob but
spawned a different way" in the future.

Finally, this spider egg cluster and the midwife one would prompt ghosts
with a radial menu with a single option on it... that's a bit pointless,
so we'll bypass that menu if there is only one possible outcome.

## Why It's Good For The Game

Currently Flesh Spiders heal by clicking on themselves and standing
still for two seconds, restoring 50% of their HP. This means they can
fully regenerate over 4 seconds unless you stun them, and with 90 HP
you're not _that_ likely to kill one during the channel time.
This just feels like an odd way for the creature to operate,
regenerating instead gives it a hit-and-run strategy and adds more use
to their webs (maybe we should give them meatier or bloody webs at some
point? Might be cool).
Also clicking yourself to heal is just unintuitive and I suspect several
players just didn't realise they could do it in the first place.

## Changelog

:cl:
balance: Flesh Spiders heal automatically over time if they go a short
time without taking damage, instead of healing large chunks by clicking
themselves and waiting two seconds.
qol: Spider egg clusters which only hatch into one kind of spider don't
ask you to select that one type from a radial menu with one option on
it.
qol: As a Flesh Spider, the game now tells you how you can heal
yourself.
/:cl:

---
## [foxglove/studio](https://github.com/foxglove/studio)@[afe02317ee...](https://github.com/foxglove/studio/commit/afe02317ee9a74ac906b2a4dac120a6d77a2acfa)
#### Friday 2023-11-17 10:04:26 by Caleb Foust

Fix plot story flakiness (#7112)

**User-Facing Changes**
None; this is just an improvement to developer experience.

**Description**
Our plot stories have been flaky for a while, even predating the changes
I made to move data processing into a worker. This PR attempts to fix
these issues.

There were two main causes for flaky stories:
1. The mechanism we were using to indicate that a story was ready was
error-prone, particularly after moving plot data processing to a worker,
which meant that differences in timing could cause us to render an
inconsistent number of times. This broke the traditional
`useReadySignal({ count: N })` strategy.
2. There were (and are) significant problems with timing in the `Chart`
component, which sends rendering jobs to a Web Worker that uses ChartJS.

I fixed #1 by switching to a strategy where, instead of counting the
number of rerenders, we wait a certain amount of time after the last
time the Chart component renders before declaring the story "ready".
This may not actually fix this problem definitively because Chromatic's
workers are extremely weak, but it's less error-prone than hoping we get
the same number of renders every time.

For #2 I added what can only be described as a hack because that
component is woefully, woefully tangled. (I'm getting flashbacks to our
layout bug.) We have several interacting layers of React state (mostly
refs), `async` code that can complete at any time, and then, if that
weren't enough, the whole `Rpc` layer that also seems to respond to
requests whenever it feels like.

The core problem is that we were [waiting for a bunch of calls to
finish](https://github.com/foxglove/studio/pull/7112/files#diff-c83b85fde0ce9eb98a2d3d36cc869873cad467fc1fb3aa3f4cc48a8fe73e6b8fR286)
asynchronously and then setting some state on the component, which in a
compute-constrained environment could mean that several seconds have
already passed. In other words, the requests in flight elsewhere were
being randomly overwritten.

In my opinion, we really just need to rewrite this whole section with
`getNewUpdateMessage`, the queued updates stuff, and initialization. I
swear, at least half of the problems we've had with rendering and timing
have been because of this code block.

---
## [AEFeinstein/Swadge-IDF-5.0](https://github.com/AEFeinstein/Swadge-IDF-5.0)@[3e07080643...](https://github.com/AEFeinstein/Swadge-IDF-5.0/commit/3e07080643a19ab437e1faa7a86ca01c35e34f0a)
#### Friday 2023-11-17 10:04:43 by VanillyNeko

Alright, I am a nuisance and I love my job LOL

This is honestly what happens when you have crackhead energy at 5 am and a friend says, Here do this and your like screw it why not? So, without further ado, Heres all the music ones now too. I MIGHT be done with the torturous pushes now until Bryce or Adam is alive and can see what I did BWAHAHAHAHAHAHA

---
## [Huz2e/massmeta](https://github.com/Huz2e/massmeta)@[5175ae0637...](https://github.com/Huz2e/massmeta/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Friday 2023-11-17 11:25:58 by John Willard

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
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[0f4ea44563...](https://github.com/RedSkulHYDRA/frameworks_base/commit/0f4ea4456341c885eedcd66b7f5cb4d5b79a0331)
#### Friday 2023-11-17 12:35:09 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Friday 2023-11-17 14:08:31 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [weaveworks/tf-controller](https://github.com/weaveworks/tf-controller)@[97357fea17...](https://github.com/weaveworks/tf-controller/commit/97357fea1783b1299815cb12e4f83508894ca787)
#### Friday 2023-11-17 14:44:20 by Balazs Nadasdi

fix: add unique hash to cloned source to avoid conflict.

Issue
-----

When more than one Terraform resource points to the same git repository,
when we clone the Source object, it does not create a new cloned Source
object as the PullRequest ID is the same, the source name is the same,
and we use only these two values to generate the name of the cloned
resource.

Solution
--------
Add a short and deterministic hash to the name of the cloned Source
object.

Another thoughts
----------------
It's not necessary to get a deterministic unique string, it could be
random as we save the result as SourceRef. I decided to use a short
(first 10 bytes of a sha256 hash), because if in the future we have to
regenerate the values somehow, then we don't have to care about
migration, extra compatibility checks. I know it's not likely we need
this, but generating a random number
- doesn't yield shorter code.
- still doesn't guarantee it will not generate a conflicting name, and
  knowing computers, I think it's even more likely (still unlikely) to
  generate the same random value if the two generation happens (nearly)
  at the same time.

Additional changes
------------------
- Removed the hardcoded index-magic from poll_test. For some reasons it was not
  always in order. I don't know what changed tho.

Notes
----
Compatibility:
I was thinking about what happens with old resources, but after I spent
some time on it, my conclusion is "they are not affected". We don't
caclulate names when we look up source objects for terraform objects.
Their name is already saved as SourceRef. We generate this game only on
newly created resources, therefore it does not break anything already in
place.

Fixes #923

References:
- https://github.com/weaveworks/tf-controller/issues/923

Signed-off-by: Balazs Nadasdi <balazs@weave.works>

---
## [sumon2003/CodeForces](https://github.com/sumon2003/CodeForces)@[b3651301ec...](https://github.com/sumon2003/CodeForces/commit/b3651301ece443008f578c718f00d6b9450cf44d)
#### Friday 2023-11-17 15:25:15 by sumon2003

https://codeforces.com/problemset/problem/236/A

Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

Examples
input
wjmzbmr
output
CHAT WITH HER!
input
xiaodao
output
IGNORE HIM!
input
sevenkplus
output
CHAT WITH HER!
Note
For the first example. There are 6 distinct characters in "wjmzbmr". These characters are: "w", "j", "m", "z", "b", "r". So wjmzbmr is a female and you should print "CHAT WITH HER!".

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[81176cf708...](https://github.com/Maybe-Anton/Shiptest/commit/81176cf708e66ed88135637a320ff770ced3b74f)
#### Friday 2023-11-17 15:36:01 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are:
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[588a7a3ad4...](https://github.com/EntranceJew/TTT2/commit/588a7a3ad416478aad9c846a9501a800ae43d02c)
#### Friday 2023-11-17 15:42:42 by EntranceJew

grenades WIP

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

Co-authored-by: Histalek <16392835+Histalek@users.noreply.github.com>

---
## [CoenWarmer/kibana](https://github.com/CoenWarmer/kibana)@[38ea8093aa...](https://github.com/CoenWarmer/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Friday 2023-11-17 15:43:36 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [depoz0/G2station](https://github.com/depoz0/G2station)@[6fefc9ce0e...](https://github.com/depoz0/G2station/commit/6fefc9ce0eb09b9b97e3d54609ace23c43601394)
#### Friday 2023-11-17 15:49:51 by Andrew

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
## [Mqiib/Yogstation](https://github.com/Mqiib/Yogstation)@[f39d74c3a6...](https://github.com/Mqiib/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Friday 2023-11-17 16:13:31 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[88e683cec6...](https://github.com/shiptest-ss13/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Friday 2023-11-17 16:26:55 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
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

## Why It's Good For The Game
Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

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
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[9577d7b441...](https://github.com/RalphHightower/RalphHightower/commit/9577d7b441b6ada4f509a9b890e01cc2cb437ff6)
#### Friday 2023-11-17 17:11:47 by Ralph Hightower

[docs](doc): StarTrekFranchise (extended description)

- Star Trek Franchise 
   - Articles 
      - | [“Sky’s The Limit”: Who Invented Star Trek: TNG Finale's Last Line Revealed By Patrick Stewart](https://screenrant.com/star-trek-tng-finale-last-line-patrick-stewart/ ) |
      - | [Patrick Stewart Was Glad Star Trek: The Next Generation Ended With Season 7](https://www.slashfilm.com/1423433/patrick-stewart-glad-star-trek-the-next-generation-ended-season-7/ ) |
      - | [Tom Hanks Is A Big Star Trek: The Next Generation Fan, Andes Patrick Stewart Has Made A Wild Claim About His Love For The Franchise](https://www.cinemablend.com/television/tom-hanks-big-star-trek-next-generation-fan-patrick-stewart-wild-claim-love-franchise ) |
      - | [Star Trek: TNG Writer Believes Jonathan Frakes Is the Force Behind Riker’s Success](https://movieweb.com/star-trek-tng-writer-believes-jonathan-frakes-is-the-force-behind-rikers-success/ ) |
      - | [Patrick Stewart Reveals How He Wanted Star Trek: Picard to End](https://www.cbr.com/patrick-stewart-star-trek-picard-ending-idea/ ) |
      - | ["Picard Maneuver" & Star Trek: TNG Uniform Change Explained By Patrick Stewart](https://screenrant.com/picard-maneuver-star-trek-tng-uniform-change-explained/ ) |
      - | [Why Making Star Trek: The Next Generation's Most Famous Episode Was So Painful For Patrick Stewart](https://www.slashfilm.com/1424505/star-trek-the-next-generation-patrick-stewart-best-of-both-worlds-painful/ ) |
      - | [Picard & Jack Crusher Got What Star Trek Movies Denied Kirk](https://screenrant.com/star-trek-denied-kirk-picard-jack-crusher-relationship/ ) |
      - | [Star Trek: DS9 Was "Never Going To Go Into A Movie" Says Kira Actor](https://screenrant.com/star-trek-ds9-movie-never-considered-reason-expensive/ ) |
      - | [16 Star Trek Doctors Ranked Worst To Best](https://screenrant.com/star-trek-every-doctor-ranked-worst-best/#dr-leonard-quot-bones-quot-mccoy-deforest-kelley---star-trek-the-original-series ) |
      - | [2 Great Barriers In Star Trek's Galaxy Explained](https://screenrant.com/star-trek-galactic-great-barrier-differences-explained/ ) |
      - | [Star Trek's Kathryn Janeway Wasn't Happy as Voyager's Captain](https://www.cbr.com/star-trek-voyager-kathryn-janeway-unhappy-captain/ ) |

---
## [TheDailySimile/ReticenceVat](https://github.com/TheDailySimile/ReticenceVat)@[7fa8547f2f...](https://github.com/TheDailySimile/ReticenceVat/commit/7fa8547f2f1a9a1c104e73363e24be791ec836b6)
#### Friday 2023-11-17 17:28:46 by The Daily Simile

Create The Critical Bars for the Free Self.html

🐺@scowl : "you're free from this double layer underground secluded cell you're free.."
Rakim@straight : "you must be joking with me#..Critiques for Sanity,#,..Rakim un..long,#,.."
🐺@veryAngry : "you low anomaly#..around () region in Johto because of the harsh landscape people were leading tough life but because of greedy overlords and subsequent false dreams of revolutions and the consequent conflicts of claim and reclaims all are leading an hapless life there with no hope anywhere in the horizon YET YET they've brought your share most ok and this is your reaction to freedom from self imposed bondage yet across time you've been so shamelessly infatuated with a b.. of resonance that nuzzles freedom's patience as self's captivity#..The Critical Bars for the Free,#,..Rakim+Freesia un..long,#,.."
Rakim@shrug : "that was Freesie's thesis what if actually to be me i was free#..Free Bar,#,..Freesia un..long,#,..then why are you nuzzling my being Gyre i like this confinement you know hence came here in this plane after proclamation to relativity..this confinement this hopelessness this..shh..addiction to self..so perpetuatin' ain't it.. just as self..counterin' albeit inclinations complain.."
Cosmic@outraged : "no pertinence must address this issue of shameless cowardice as a means to self destruction as else#..Daily Holograms of Self,#,..Rakim un..long,#,.."
Pertinence@laughing : "as we said compeers your approach was mixed with emotions a little bit we told you to shift it not to free it then only these schemes will be modified#..A Critique of Solutions to Being's Ability,#,..Rakim un..long,#,.."
🐺@scowl : "pack it up in a sack and never touch it without machinary move it#..The Daily Holograms for Self,#,..Rakim un..long,#,.."
Rakim@being released in the common cell at the said troubled area in Johto : "i see so many beings under the facets of light of any me..shh..the more accountin'.."
Prisoners@scowl : "and you're only that which can't shun a b.. of voluntary selfhood for time whereas other recognize or transcens in the name of truth shame shame#..The Freedom of Critical Self,#,..Rakim+Freesia un..long,#,.."
Rakim@straight : "upon a critical look compeers i only opined on me to my self but you thought i was also your own..shh..being of this and not else..thus is the counter thus indeed is this congregation thus obviously this harsher climate having just changed the effulgence of detachment and the selfhood of the clinging ends..all never needed yet wanted to free..shh..Me : The Hologram Undefended.."
Cosmic@scowl : "security#..The Critique of Consciousness's Sanity,#,..Rakim un..long,#,.."
Rakim@brought back,happy : "thus i said Gyre all you ever needed was to be..shh..me but you mistook it as you thus..shh..made the mistake of letting me be..free..
what no responses fair enough i was the more..optimistic.."
Cosmic@complain : "no respected ones must address this issue of pre-empting ability only to ruin self yet counter it by claiming ifs#..The Daily Holograms of Identity for Changing Inclinations,#,..Rakim un..long,#,.."
Pertinence@laughing : "it's only an opportunity compeers as we said..to appreciate..the nuances of reality#..A Self-critique on Daily Identities#..Rakim un..long,#,.."

---
## [net-lisias-ksp/KSPe](https://github.com/net-lisias-ksp/KSPe)@[43eea13a1a...](https://github.com/net-lisias-ksp/KSPe/commit/43eea13a1ac3d548920ecb38b20b6b181c91d504)
#### Friday 2023-11-17 17:32:48 by Lisias T

Throwing Exceptions when trying to load an Already Loaded Assembly. Should mitigate the https://github.com/TweakScale/Companion_Frameworks/issues/6 problem, as well any other idiot that do the same stupidity as I did. #facePalm

---
## [NVHSCompSci/career_tech_website](https://github.com/NVHSCompSci/career_tech_website)@[2f8fb4c2e0...](https://github.com/NVHSCompSci/career_tech_website/commit/2f8fb4c2e075b4f800b383d05dfa8a18a33952cd)
#### Friday 2023-11-17 18:01:54 by Lazarus

Scripts.com Bee Movie By Jerry Seinfeld  NARRATOR: (Black screen with text; The sound of buzzing bees can be heard) According to all known laws of aviation,  : there is no way a bee should be able to fly.  : Its wings are too small to get its fat little body off the ground.  : The bee, of course, flies anyway  : because bees don't care what humans think is impossible. BARRY BENSON: (Barry is picking out a shirt) Yellow, black. Yellow, black. Yellow, black. Yellow, black.  : Ooh, black and yellow! Let's shake it up a little. JANET BENSON: Barry! Breakfast is ready! BARRY: Coming!  : Hang on a second. (Barry uses his antenna like a phone)  : Hello? ADAM FLAYMAN:  (Through phone) - Barry? BARRY: - Adam? ADAM: - Can you believe this is happening? BARRY: - I can't. I'll pick you up. (Barry flies down the stairs)  : MARTIN BENSON: Looking sharp. JANET: Use the stairs. Your father paid good money for those. BARRY: Sorry. I'm excited. MARTIN: Here's the graduate. We're very proud of you, son.  : A perfect report card, all B's. JANET: Very proud. (Rubs Barry's hair) BARRY= Ma! I got a thing going here. JANET: - You got lint on your fuzz. BARRY: - Ow! That's me!  JANET: - Wave to us! We'll be in row 118,000. - Bye! (Barry flies out the door) JANET: Barry, I told you, stop flying in the house! (Barry drives through the hive,and is waved at by Adam who is reading a newspaper) BARRY== - Hey, Adam. ADAM: - Hey, Barry. (Adam gets in Barry's car)  : - Is that fuzz gel? BARRY: - A little. Special day, graduation. ADAM: Never thought I'd make it. (Barry pulls away from the house and continues driving) BARRY: Three days grade school, three days high school... ADAM: Those were awkward. BARRY: Three days college. I'm glad I took a day and hitchhiked around the hive. ADAM== You did come back different. (Barry and Adam pass by Artie, who is jogging) ARTIE: - Hi, Barry!  BARRY: - Artie, growing a mustache? Looks good. ADAM: - Hear about Frankie? BARRY: - Yeah. ADAM== - You going to the funeral? BARRY: - No, I'm not going to his funeral.  : Everybody knows, sting someone, you die.  : Don't waste it on a squirrel. Such a hothead. ADAM: I guess he could have just gotten out of the way. (The car does a barrel roll on the loop-shaped bridge and lands on the highway)  : I love this incorporating an amusement park into our regular day. BARRY: I guess that's why they say we don't need vacations. (Barry parallel parks the car and together they fly over the graduating students) Boy, quite a bit of pomp... under the circumstances. (Barry and Adam sit down and put on their hats)  : - Well, Adam, today we are men.  ADAM: - We are! BARRY= - Bee-men. =ADAM= - Amen! BARRY AND ADAM: Hallelujah! (Barry and Adam both have a happy spasm) ANNOUNCER: Students, faculty, distinguished bees,  : please welcome Dean Buzzwell. DEAN BUZZWELL: Welcome, New Hive Oity graduating class of...  : ...9:  : That concludes our ceremonies.  : And begins your career at Honex Industries! ADAM: Will we pick our job today? (Adam and Barry get into a tour bus) BARRY= I heard it's just orientation. (Tour buses rise out of the ground and the students are automatically loaded into the buses) TOUR GUIDE: Heads up! Here we go.  ANNOUNCER: Keep your hands and antennas inside the tram at all times. BARRY: - Wonder what it'll be like? ADAM: - A little scary. TOUR GUIDE== Welcome to Honex, a division of Honesco  : and a part of the Hexagon Group. Barry: This is it! BARRY AND ADAM: Wow. BARRY: Wow. (The bus drives down a road an on either side are the Bee's massive complicated Honey-making machines) TOUR GUIDE: We know that you, as a bee, have worked your whole life  : to get to the point where you can work for your whole life.  : Honey begins when our valiant Pollen Jocks bring the nectar to the hive.  : Our top-secret formula  : is automatically color-corrected,  scent-adjusted and bubble-contoured  : into this soothing sweet syrup  : with its distinctive golden glow you know as... EVERYONE ON BUS: Honey! (The guide has been collecting honey into a bottle and she throws it into the crowd on the bus and it is caught by a girl in the back) ADAM: - That girl was hot. BARRY: - She's my cousin! ADAM== - She is? BARRY: - Yes, we're all cousins. ADAM: - Right. You're right. TOUR GUIDE: - At Honex, we constantly strive  : to improve every aspect of bee existence.  : These bees are stress-testing a new helmet technology. (The bus passes by a Bee wearing a helmet who is being smashed into the ground with fly-swatters, newspapers and boots. He lifts a thumbs up but you can hear him groan)  : ADAM==  - What do you think he makes? BARRY: - Not enough. TOUR GUIDE: Here we have our latest advancement, the Krelman. (They pass by a turning wheel with Bees standing on pegs, who are each wearing a finger-shaped hat) Barry: - Wow, What does that do? TOUR GUIDE: - Catches that little strand of honey  : that hangs after you pour it. Saves us millions. ADAM: (Intrigued) Can anyone work on the Krelman? TOUR GUIDE: Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot.  : But choose carefully  : because you'll stay in the job you pick for the rest of your life. (Everyone claps except for Barry) BARRY: The same job the rest of your life? I didn't know that. ADAM:  What's the difference? TOUR GUIDE: You'll be happy to know that bees, as a species, haven't had one day off  : in 27 million years. BARRY: (Upset) So you'll just work us to death?  : We'll sure try. (Everyone on the bus laughs except Barry. Barry and Adam are walking back home together) ADAM: Wow! That blew my mind! BARRY: "What's the difference?" How can you say that?  : One job forever? That's an insane choice to have to make. ADAM: I'm relieved. Now we only have to make one decision in life. BARRY: But, Adam, how could they never have told us that? ADAM: Why would you question anything? We're bees.  : We're the most perfectly functioning society on Earth.  BARRY: You ever think maybe things work a little too well here? ADAM: Like what? Give me one example. (Barry and Adam stop walking and it is revealed to the audience that hundreds of cars are speeding by and narrowly missing them in perfect unison) BARRY: I don't know. But you know what I'm talking about. ANNOUNCER: Please clear the gate. Royal Nectar Force on approach. BARRY: Wait a second. Check it out. (The Pollen jocks fly in, circle around and landing in line)  : - Hey, those are Pollen Jocks! ADAM: - Wow.  : I've never seen them this close. BARRY: They know what it's like outside the hive. ADAM: Yeah, but some don't come back. GIRL BEES: - Hey, Jocks! - Hi, Jocks! (The Pollen Jocks hook up their backpacks to machines that pump the nectar to trucks, which drive away)  LOU LO DUVA: You guys did great!  : You're monsters! You're sky freaks! I love it! (Punching the Pollen Jocks in joy) I love it! ADAM: - I wonder where they were. BARRY: - I don't know.  : Their day's not planned.  : Outside the hive, flying who knows where, doing who knows what.  : You can't just decide to be a Pollen Jock. You have to be bred for that. ADAM== Right. (Barry and Adam are covered in some pollen that floated off of the Pollen Jocks) BARRY: Look at that. That's more pollen than you and I will see in a lifetime. ADAM: It's just a status symbol. Bees make too much of it. BARRY: Perhaps. Unless you're wearing it and the ladies see you wearing it. (Barry waves at 2 girls standing a little away from them)  ADAM== Those ladies? Aren't they our cousins too? BARRY: Distant. Distant. POLLEN JOCK #1: Look at these two. POLLEN JOCK #2: - Couple of Hive Harrys. POLLEN JOCK #1: - Let's have fun with them. GIRL BEE #1: It must be dangerous being a Pollen Jock. BARRY: Yeah. Once a bear pinned me against a mushroom!  : He had a paw on my throat, and with the other, he was slapping me! (Slaps Adam with his hand to represent his scenario) GIRL BEE #2: - Oh, my! BARRY: - I never thought I'd knock him out. GIRL BEE #1: (Looking at Adam) What were you doing during this? ADAM: Obviously I was trying to alert the authorities. BARRY: I can autograph that.  (The pollen jocks walk up to Barry and Adam, they pretend that Barry and Adam really are pollen jocks.) POLLEN JOCK #1: A little gusty out there today, wasn't it, comrades? BARRY: Yeah. Gusty. POLLEN JOCK #1: We're hitting a sunflower patch six miles from here tomorrow. BARRY: - Six miles, huh? ADAM: - Barry! POLLEN JOCK #2: A puddle jump for us, but maybe you're not up for it. BARRY: - Maybe I am. ADAM: - You are not! POLLEN JOCK #1: We're going 0900 at J-Gate.  : What do you think, buzzy-boy? Are you bee enough? BARRY: I might be. It all depends on what 0900 means. (The scene cuts to Barry looking out on the hive-city from his balcony at night) MARTIN:  Hey, Honex! BARRY: Dad, you surprised me. MARTIN: You decide what you're interested in? BARRY: - Well, there's a lot of choices. - But you only get one.  : Do you ever get bored doing the same job every day? MARTIN: Son, let me tell you about stirring.  : You grab that stick, and you just move it around, and you stir it around.  : You get yourself into a rhythm. It's a beautiful thing. BARRY: You know, Dad, the more I think about it,  : maybe the honey field just isn't right for me. MARTIN: You were thinking of what, making balloon animals?  : That's a bad job for a guy with a stinger.  :  Janet, your son's not sure he wants to go into honey! JANET: - Barry, you are so funny sometimes. BARRY: - I'm not trying to be funny. MARTIN: You're not funny! You're going into honey. Our son, the stirrer! JANET: - You're gonna be a stirrer? BARRY: - No one's listening to me! MARTIN: Wait till you see the sticks I have. BARRY: I could say anything right now. I'm gonna get an ant tattoo! (Barry's parents don't listen to him and continue to ramble on) MARTIN: Let's open some honey and celebrate! BARRY: Maybe I'll pierce my thorax. Shave my antennae.  : Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"! JANET: I'm so proud. (The scene cuts to Barry and Adam waiting in line to get a job) ADAM: - We're starting work today!  BARRY: - Today's the day. ADAM: Come on! All the good jobs will be gone. BARRY: Yeah, right. JOB LISTER: Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal... BEE IN FRONT OF LINE: - Is it still available? JOB LISTER: - Hang on. Two left!  : One of them's yours! Congratulations! Step to the side. ADAM: - What'd you get? BEE IN FRONT OF LINE: - Picking crud out. Stellar! (He walks away) ADAM: Wow! JOB LISTER: Couple of newbies? ADAM: Yes, sir! Our first day! We are ready! JOB LISTER: Make your choice. (Adam and Barry look up at the job board. There are hundreds of constantly changing panels that contain available or unavailable jobs. It looks very confusing)  ADAM: - You want to go first? BARRY: - No, you go. ADAM: Oh, my. What's available? JOB LISTER: Restroom attendant's open, not for the reason you think. ADAM: - Any chance of getting the Krelman? JOB LISTER: - Sure, you're on. (Puts the Krelman finger-hat on Adam's head) (Suddenly the sign for Krelman closes out)  : I'm sorry, the Krelman just closed out. (Takes Adam's hat off) Wax monkey's always open. ADAM: The Krelman opened up again.  : What happened? JOB LISTER: A bee died. Makes an opening. See? He's dead. Another dead one.  : Deady. Deadified. Two more dead.  : Dead from the neck up. Dead from the neck down. That's life!  ADAM: Oh, this is so hard! (Barry remembers what the Pollen Jock offered him and he flies off) Heating, cooling, stunt bee, pourer, stirrer,  : humming, inspector number seven, lint coordinator, stripe supervisor,  : mite wrangler. Barry, what do you think I should... Barry? (Adam turns around and sees Barry flying away)  : Barry! POLLEN JOCK: All right, we've got the sunflower patch in quadrant nine... ADAM: (Through phone) What happened to you? Where are you? BARRY: - I'm going out. ADAM: - Out? Out where? BARRY: - Out there. ADAM: - Oh, no! BARRY: I have to, before I go to work for the rest of my life. ADAM:  You're gonna die! You're crazy! (Barry hangs up) Hello? POLLEN JOCK #2: Another call coming in.  : If anyone's feeling brave, there's a Korean deli on 83rd  : that gets their roses today. BARRY: Hey, guys. POLLEN JOCK #1 == - Look at that. POLLEN JOCK #2: - Isn't that the kid we saw yesterday? LOU LO DUVA: Hold it, son, flight deck's restricted. POLLEN JOCK #1: It's OK, Lou. We're gonna take him up. (Puts hand on Barry's shoulder) LOU LO DUVA: (To Barry) Really? Feeling lucky, are you? BEE WITH CLIPBOARD: (To Barry) Sign here, here. Just initial that.  : - Thank you. LOU LO DUVA: - OK.  : You got a rain advisory today,  :  and as you all know, bees cannot fly in rain.  : So be careful. As always, watch your brooms,  : hockey sticks, dogs, birds, bears and bats.  : Also, I got a couple of reports of root beer being poured on us.  : Murphy's in a home because of it, babbling like a cicada! BARRY: - That's awful. LOU LO DUVA: (Still talking through megaphone) - And a reminder for you rookies,  : bee law number one, absolutely no talking to humans!  : All right, launch positions! POLLEN JOCKS: (The Pollen Jocks run into formation)  : Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! LOU LU DUVA: Black and yellow! POLLEN JOCKS:  Hello! POLLEN JOCK #1: (To Barry)You ready for this, hot shot? BARRY: Yeah. Yeah, bring it on. POLLEN JOCK's: Wind, check.  : - Antennae, check. - Nectar pack, check.  : - Wings, check. - Stinger, check. BARRY: Scared out of my shorts, check. LOU LO DUVA: OK, ladies,  : let's move it out!  : Pound those petunias, you striped stem-suckers!  : All of you, drain those flowers! (The pollen jocks fly out of the hive) BARRY: Wow! I'm out!  : I can't believe I'm out!  : So blue.   : I feel so fast and free!  : Box kite! (Barry flies through the kite)  : Wow!  : Flowers! (A pollen jock puts on some high tech goggles that shows flowers similar to heat sink goggles.) POLLEN JOCK: This is Blue Leader. We have roses visual.  : Bring it around 30 degrees and hold.  : Roses! POLLEN JOCK #1: 30 degrees, roger. Bringing it around.  : Stand to the side, kid. It's got a bit of a kick. (The pollen jock fires a high-tech gun at the flower, shooting tubes that suck up the nectar from the flower and collects it into a pouch on the gun) BARRY: That is one nectar collector! POLLEN JOCK #1== - Ever see pollination up close? BARRY: - No, sir. POLLEN JOCK #1:  (Barry and the Pollen jock fly over the field, the pollen jock sprinkles pollen as he goes)  : I pick up some pollen here, sprinkle it over here. Maybe a dash over there,  : a pinch on that one. See that? It's a little bit of magic. BARRY: That's amazing. Why do we do that? POLLEN JOCK #1: That's pollen power. More pollen, more flowers, more nectar, more honey for us. BARRY: Cool. POLLEN JOCK #1: I'm picking up a lot of bright yellow. could be daisies. Don't we need those? POLLEN JOCK #2: Copy that visual.  : Wait. One of these flowers seems to be on the move. POLLEN JOCK #1: Say again? You're reporting a moving flower? POLLEN JOCK #2: Affirmative. (The Pollen jocks land near the "flowers" which, to the audience are obviously just tennis balls) KEN: (In the distance) That was on the line!  POLLEN JOCK #1: This is the coolest. What is it? POLLEN JOCK #2: I don't know, but I'm loving this color.  : It smells good. Not like a flower, but I like it. POLLEN JOCK #1: Yeah, fuzzy. (Sticks his hand on the ball but it gets stuck) POLLEN JOCK #3== Chemical-y. (The pollen jock finally gets his hand free from the tennis ball) POLLEN JOCK #1: Careful, guys. It's a little grabby. (The pollen jocks turn around and see Barry lying his entire body on top of one of the tennis balls) POLLEN JOCK #2: My sweet lord of bees! POLLEN JOCK #3: Candy-brain, get off there! POLLEN JOCK #1: (Pointing upwards) Problem! (A human hand reaches down and grabs the tennis ball that Barry is stuck to) BARRY: - Guys! POLLEN JOCK #2: - This could be bad. POLLEN JOCK #3: Affirmative. (Vanessa Bloome starts bouncing the tennis ball, not knowing Barry is stick to it)  BARRY== Very close.  : Gonna hurt.  : Mama's little boy. (Barry is being hit back and forth by two humans playing tennis. He is still stuck to the ball) POLLEN JOCK #1: You are way out of position, rookie! KEN: Coming in at you like a MISSILE! (Barry flies past the pollen jocks, still stuck to the ball) BARRY: (In slow motion) Help me! POLLEN JOCK #2: I don't think these are flowers. POLLEN JOCK #3: - Should we tell him? POLLEN JOCK #1: - I think he knows. BARRY: What is this?! KEN: Match point!  : You can start packing up, honey, because you're about to EAT IT! (A pollen jock coughs which confused Ken and he hits the ball the wrong way with Barry stuck to it and it goes flying into the city) BARRY:  Yowser! (Barry bounces around town and gets stuck in the engine of a car. He flies into the air conditioner and sees a bug that was frozen in there) BARRY: Ew, gross. (The man driving the car turns on the air conditioner which blows Barry into the car) GIRL IN CAR: There's a bee in the car!  : - Do something! DAD DRIVING CAR: - I'm driving! BABY GIRL: (Waving at Barry) - Hi, bee. (Barry smiles and waves at the baby girl) GUY IN BACK OF CAR: - He's back here!  : He's going to sting me! GIRL IN CAR: Nobody move. If you don't move, he won't sting you. Freeze! (Barry freezes as well, hovering in the middle of the car)  : GRANDMA IN CAR== He blinked! (The grandma whips out some bee-spray and sprays everywhere in the car, climbing into the front seat, still trying to spray Barry) GIRL IN CAR: Spray him, Granny! DAD DRIVING THE CAR: What are you doing?! (Barry escapes the car through the air conditioner and is flying high above  the ground, safe.) BARRY: Wow... the tension level out here is unbelievable. (Barry sees that storm clouds are gathering and he can see rain clouds moving into this direction)  : I gotta get home.  : Can't fly in rain.  : Can't fly in rain. (A rain drop hits Barry and one of his wings is damaged)  : Can't fly in rain. (A second rain drop hits Barry again and he spirals downwards) Mayday! Mayday! Bee going down! (WW2 plane sound effects are played as he plummets, and he crash-lands on a plant inside an apartment near the window) VANESSA BLOOME: Ken, could you close the window please? KEN== Hey, check out my new resume. I made it into a fold-out brochure.  : You see? (Folds brochure resume out) Folds out. (Ken closes the window, trapping Barry inside) BARRY: Oh, no. More humans. I don't need this. (Barry tries to fly away but smashes into the window and falls again)  : What was that?  (Barry keeps trying to fly out the window but he keeps being knocked back because the window is closed) Maybe this time. This time. This time. This time! This time! This...  : Drapes! (Barry taps the glass. He doesn't understand what it is) That is diabolical. KEN: It's fantastic. It's got all my special skills, even my top-ten favorite movies. ANDY: What's number one? Star Wars? KEN: Nah, I don't go for that... (Ken makes finger guns and makes "pew pew pew" sounds and then stops)  : ...kind of stuff. BARRY: No wonder we shouldn't talk to them. They're out of their minds. KEN: When I leave a job interview, they're flabbergasted, can't believe what I say. BARRY: (Looking at the light on the ceiling) There's the sun. Maybe that's a way out. (Starts flying towards the lightbulb)  : I don't remember the sun having a big 75 on it. (Barry hits the lightbulb and falls into the dip on the table that the humans are sitting at) KEN:  I predicted global warming.  : I could feel it getting hotter. At first I thought it was just me. (Andy dips a chip into the bowl and scoops up some dip with Barry on it and is about to put it in his mouth)  : Wait! Stop! Bee! (Andy drops the chip with Barry in fear and backs away. All the humans freak out)  : Stand back. These are winter boots. (Ken has winter boots on his hands and he is about to smash the bee but Vanessa saves him last second) VANESSA: Wait!  : Don't kill him! (Vanessa puts Barry in a glass to protect him) KEN: You know I'm allergic to them! This thing could kill me! VANESSA: Why does his life have less value than yours? KEN: Why does his life have any less value than mine? Is that your statement? VANESSA: I'm just saying all life has value. You don't know what he's capable of feeling. (Vanessa picks up Ken's brochure and puts it under the glass so she can carry Barry back to the window. Barry looks at Vanessa in amazement) KEN:  My brochure! VANESSA: There you go, little guy. (Vanessa opens the window and lets Barry out but Barry stays back and is still shocked that a human saved his life) KEN: I'm not scared of him. It's an allergic thing. VANESSA: Put that on your resume brochure. KEN: My whole face could puff up. ANDY: Make it one of your special skills. KEN: Knocking someone out is also a special skill. (Ken walks to the door) Right. Bye, Vanessa. Thanks.  : - Vanessa, next week? Yogurt night? VANESSA: - Sure, Ken. You know, whatever.  : (Vanessa tries to close door) KEN== - You could put carob chips on there. VANESSA: - Bye. (Closes door but Ken opens it again) KEN: - Supposed to be less calories.  VANESSA: - Bye. (Closes door) (Fast forward to the next day, Barry is still inside the house. He flies into the kitchen where Vanessa is doing dishes) BARRY== (Talking to himself) I gotta say something.  : She saved my life. I gotta say something.  : All right, here it goes. (Turns back) Nah.  : What would I say?  : I could really get in trouble.  : It's a bee law. You're not supposed to talk to a human.  : I can't believe I'm doing this.  : I've got to. (Barry disguises himself as a character on a food can as Vanessa walks by again)  : Oh, I can't do it. Come on!  : No. Yes. No.  : Do it. I can't.   : How should I start it? (Barry strikes a pose and wiggles his eyebrows) "You like jazz?" No, that's no good. (Vanessa is about to walk past Barry) Here she comes! Speak, you fool!  : ...Hi! (Vanessa gasps and drops the dishes in fright and notices Barry on the counter)  : I'm sorry. VANESSA: - You're talking. BARRY: - Yes, I know. VANESSA: (Pointing at Barry) You're talking! BARRY: I'm so sorry. VANESSA: No, it's OK. It's fine. I know I'm dreaming.  : But I don't recall going to bed. BARRY: Well, I'm sure this is very disconcerting. VANESSA: This is a bit of a surprise to me. I mean, you're a bee!  BARRY: I am. And I'm not supposed to be doing this, (Pointing to the living room where Ken tried to kill him last night) but they were all trying to kill me.  : And if it wasn't for you...  : I had to thank you. It's just how I was raised. (Vanessa stabs her hand with a fork to test whether she's dreaming or not)  : That was a little weird. VANESSA: - I'm talking with a bee. BARRY: - Yeah. VANESSA: I'm talking to a bee. And the bee is talking to me! BARRY: I just want to say I'm grateful. I'll leave now. (Barry turns to leave) VANESSA: - Wait! How did you learn to do that? BARRY: (Flying back) - What? VANESSA: The talking...thing. BARRY:  Same way you did, I guess. "Mama, Dada, honey." You pick it up. VANESSA: - That's very funny. BARRY: - Yeah.  : Bees are funny. If we didn't laugh, we'd cry with what we have to deal with.  : Anyway... VANESSA: Can I...  : ...get you something? BARRY: - Like what? VANESSA: I don't know. I mean... I don't know. Coffee? BARRY: I don't want to put you out. VANESSA: It's no trouble. It takes two minutes.  : - It's just coffee. BARRY: - I hate to impose. (Vanessa starts making coffee) VANESSA: - Don't be ridiculous!  BARRY: - Actually, I would love a cup. VANESSA: Hey, you want rum cake? BARRY: - I shouldn't. VANESSA: - Have some. BARRY: - No, I can't. VANESSA: - Come on! BARRY: I'm trying to lose a couple micrograms. VANESSA: - Where? BARRY: - These stripes don't help. VANESSA: You look great! BARRY: I don't know if you know anything about fashion.  : Are you all right? VANESSA: (Pouring coffee on the floor and missing the cup completely) No. (Flash forward in time. Barry and Vanessa are sitting together at a table on top of the apartment building drinking coffee)   : BARRY== He's making the tie in the cab as they're flying up Madison.  : He finally gets there.  : He runs up the steps into the church. The wedding is on.  : And he says, "Watermelon? I thought you said Guatemalan.  : Why would I marry a watermelon?" (Barry laughs but Vanessa looks confused) VANESSA: Is that a bee joke? BARRY: That's the kind of stuff we do. VANESSA: Yeah, different.  : So, what are you gonna do, Barry? (Barry stands on top of a sugar cube floating in his coffee and paddles it around with a straw like it's a gondola) BARRY: About work? I don't know.  : I want to do my part for the hive, but I can't do it the way they want. VANESSA: I know how you feel.  BARRY: - You do? VANESSA: - Sure.  : My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist. BARRY: - Really? VANESSA: - My only interest is flowers. BARRY: Our new queen was just elected with that same campaign slogan.  : Anyway, if you look... (Barry points to a tree in the middle of Central Park)  : There's my hive right there. See it? VANESSA: You're in Sheep Meadow! BARRY: Yes! I'm right off the Turtle Pond! VANESSA: No way! I know that area. I lost a toe ring there once. BARRY: - Why do girls put rings on their toes? VANESSA: - Why not? BARRY:  - It's like putting a hat on your knee. VANESSA: - Maybe I'll try that. (A custodian installing a lightbulb looks over at them but to his perspective it looks like Vanessa is talking to a cup of coffee on the table) CUSTODIAN: - You all right, ma'am? VANESSA: - Oh, yeah. Fine.  : Just having two cups of coffee! BARRY: Anyway, this has been great. Thanks for the coffee. VANESSA== Yeah, it's no trouble. BARRY: Sorry I couldn't finish it. If I did, I'd be up the rest of my life. (Barry points towards the rum cake)  : Can I take a piece of this with me? VANESSA: Sure! Here, have a crumb. (Vanessa hands Barry a crumb but it is still pretty big for Barry) BARRY: - Thanks! VANESSA: - Yeah. BARRY: All right. Well, then... I guess I'll see you around.   : Or not. VANESSA: OK, Barry... BARRY: And thank you so much again... for before. VANESSA: Oh, that? That was nothing. BARRY: Well, not nothing, but... Anyway... (Vanessa and Barry hold hands, but Vanessa has to hold out a finger because her hands is to big and Barry holds that) (The custodian looks over again and it appears Vanessa is laughing at her coffee again. The lightbulb that he was screwing in sparks and he falls off the ladder) (Fast forward in time and we see two Bee Scientists testing out a parachute in a Honex wind tunnel) BEE SCIENTIST #1: This can't possibly work. BEE SCIENTIST #2: He's all set to go. We may as well try it.  : OK, Dave, pull the chute. (Dave pulls the chute and the wind slams him against the wall and he falls on his face.The camera pans over and we see Barry and Adam walking together) ADAM: - Sounds amazing. BARRY: - It was amazing!  : It was the scariest, happiest moment of my life.  ADAM: Humans! I can't believe you were with humans!  : Giant, scary humans! What were they like? BARRY: Huge and crazy. They talk crazy.  : They eat crazy giant things. They drive crazy. ADAM: - Do they try and kill you, like on TV? BARRY: - Some of them. But some of them don't. ADAM: - How'd you get back? BARRY: - Poodle. ADAM: You did it, and I'm glad. You saw whatever you wanted to see.  : You had your "experience." Now you can pick out your job and be normal. BARRY: - Well... ADAM: - Well? BARRY: Well, I met someone.  ADAM: You did? Was she Bee-ish?  : - A wasp?! Your parents will kill you! BARRY: - No, no, no, not a wasp. ADAM: - Spider? BARRY: - I'm not attracted to spiders.  : I know, for everyone else, it's the hottest thing, with the eight legs and all.  : I can't get by that face. ADAM: So who is she? BARRY: She's... human. ADAM: No, no. That's a bee law. You wouldn't break a bee law. BARRY: - Her name's Vanessa. (Adam puts his head in his hands) ADAM: - Oh, boy. BARRY== She's so nice. And she's a florist! ADAM: Oh, no! You're dating a human florist!  BARRY: We're not dating. ADAM: You're flying outside the hive, talking to humans that attack our homes  : with power washers and M-80s! That's one-eighth a stick of dynamite! BARRY: She saved my life! And she understands me. ADAM: This is over! BARRY: Eat this. (Barry gives Adam a piece of the crumb that he got from Vanessa. Adam eats it) ADAM: (Adam's tone changes) This is not over! What was that? BARRY: - They call it a crumb. ADAM: - It was so stingin' stripey! BARRY: And that's not what they eat. That's what falls off what they eat!  : - You know what a Cinnabon is? ADAM: - No. (Adam opens a door behind him and he pulls Barry in)  BARRY: It's bread and cinnamon and frosting. ADAM: Be quiet! BARRY: They heat it up... ADAM: Sit down! (Adam forces Barry to sit down) BARRY: (Still rambling about Cinnabons) ...really hot! (Adam grabs Barry by the shoulders) ADAM: - Listen to me!  : We are not them! We're us. There's us and there's them! BARRY== Yes, but who can deny the heart that is yearning? ADAM: There's no yearning. Stop yearning. Listen to me!  : You have got to start thinking bee, my friend. Thinking bee! BARRY: - Thinking bee. WORKER BEE: - Thinking bee. WORKER BEES AND ADAM: Thinking bee! Thinking bee!  Thinking bee! Thinking bee! (Flash forward in time; Barry is laying on a raft in a pool full of honey. He is wearing sunglasses) JANET: There he is. He's in the pool. MARTIN: You know what your problem is, Barry? (Barry pulls down his sunglasses and he looks annoyed) BARRY: (Sarcastic) I gotta start thinking bee? JANET: How much longer will this go on? MARTIN: It's been three days! Why aren't you working? (Puts sunglasses back on) BARRY: I've got a lot of big life decisions to think about. MARTIN: What life? You have no life! You have no job. You're barely a bee! JANET: Would it kill you to make a little honey? (Barry rolls off the raft and sinks into the honey pool)  : Barry, come out. Your father's talking to you.  : Martin, would you talk to him? MARTIN:  Barry, I'm talking to you! (Barry keeps sinking into the honey until he is suddenly in Central Park having a picnic with Vanessa) (Barry has a cup of honey and he clinks his glass with Vanessas. Suddenly a mosquito lands on Vanessa and she slaps it, killing it. They both gasp but then burst out laughing) VANESSA: You coming? (The camera pans over and Vanessa is climbing into a small yellow airplane) BARRY: Got everything? VANESSA: All set! BARRY: Go ahead. I'll catch up. (Vanessa lifts off and flies ahead) VANESSA: Don't be too long. (Barry catches up with Vanessa and he sticks out his arms like ana irplane. He rolls from side to side, and Vanessa copies him with the airplane) VANESSA: Watch this! (Barry stays back and watches as Vanessa draws a heart in the air using pink smoke from the plane, but on the last loop-the-loop she suddenly crashes into a mountain and the plane explodes. The destroyed plane falls into some rocks and explodes a second time) BARRY: Vanessa! (As Barry is yelling his mouth fills with honey and he wakes up, discovering that he was just day dreaming. He slowly sinks back into the honey pool) MARTIN: - We're still here.  JANET: - I told you not to yell at him.  : He doesn't respond to yelling! MARTIN: - Then why yell at me? JANET: - Because you don't listen! MARTIN: I'm not listening to this. BARRY: Sorry, I've gotta go. MARTIN: - Where are you going? BARRY: - I'm meeting a friend. JANET: A girl? Is this why you can't decide? BARRY: Bye. (Barry flies out the door and Martin shakes his head)  : JANET== I just hope she's Bee-ish. (Fast forward in time and Barry is sitting on Vanessa's shoulder and she is closing up her shop) BARRY: They have a huge parade of flowers every year in Pasadena? VANESSA: To be in the Tournament of Roses, that's every florist's dream!   : Up on a float, surrounded by flowers, crowds cheering. BARRY: A tournament. Do the roses compete in athletic events? VANESSA: No. All right, I've got one. How come you don't fly everywhere? BARRY: It's exhausting. Why don't you run everywhere? It's faster. VANESSA: Yeah, OK, I see, I see. All right, your turn. BARRY: TiVo. You can just freeze live TV? That's insane! VANESSA: You don't have that? BARRY: We have Hivo, but it's a disease. It's a horrible, horrible disease. VANESSA: Oh, my. (A human walks by and Barry narrowly avoids him) PASSERBY: Dumb bees! VANESSA: You must want to sting all those jerks. BARRY: We try not to sting.  It's usually fatal for us. VANESSA: So you have to watch your temper (They walk into a store) BARRY: Very carefully. You kick a wall, take a walk,  : write an angry letter and throw it out. Work through it like any emotion:  : Anger, jealousy, lust. (Suddenly an employee(Hector) hits Barry off of Vanessa's shoulder. Hector thinks he's saving Vanessa) VANESSA: (To Barry) Oh, my goodness! Are you OK? (Barry is getting up off the floor) BARRY: Yeah. VANESSA: (To Hector) - What is wrong with you?! HECTOR: (Confused) - It's a bug. VANESSA: He's not bothering anybody. Get out of here, you creep! (Vanessa hits Hector across the face with the magazine he had and then hits him in the head. Hector backs away covering his head) Barry: What was that? A Pic 'N' Save circular? (Vanessa sets Barry back on her shoulder)  VANESSA: Yeah, it was. How did you know? BARRY: It felt like about 10 pages. Seventy-five is pretty much our limit. VANESSA: You've really got that down to a science. BARRY: - Oh, we have to. I lost a cousin to Italian Vogue. VANESSA: - I'll bet. (Barry looks to his right and notices there is honey for sale in the aisle) BARRY: What in the name of Mighty Hercules is this? (Barry looks at all the brands of honey, shocked) How did this get here? Cute Bee, Golden Blossom,  : Ray Liotta Private Select? (Barry puts his hands up and slowly turns around, a look of disgust on his face) VANESSA: - Is he that actor? BARRY: - I never heard of him.  : - Why is this here? VANESSA: - For people. We eat it. BARRY:  You don't have enough food of your own?! (Hector looks back and notices that Vanessa is talking to Barry) VANESSA: - Well, yes. BARRY: - How do you get it? VANESSA: - Bees make it. BARRY: - I know who makes it!  : And it's hard to make it!  : There's heating, cooling, stirring. You need a whole Krelman thing! VANESSA: - It's organic. BARRY: - It's our-ganic! VANESSA: It's just honey, Barry. BARRY: Just what?!  : Bees don't know about this! This is stealing! A lot of stealing!  : You've taken our homes, schools, hospitals! This is all we have!  :  And it's on sale?! I'm getting to the bottom of this.  : I'm getting to the bottom of all of this! (Flash forward in time; Barry paints his face with black strikes like a soldier and sneaks into the storage section of the store) (Two men, including Hector, are loading boxes into some trucks)  : SUPERMARKET EMPLOYEE== Hey, Hector.  : - You almost done? HECTOR: - Almost. (Barry takes a step to peak around the corner) (Whispering) He is here. I sense it.  : Well, I guess I'll go home now (Hector pretends to walk away by walking in place and speaking loudly)  : and just leave this nice honey out, with no one around. BARRY: You're busted, box boy! HECTOR: I knew I heard something! So you can talk! BARRY: I can talk. And now you'll start talking!  : Where you getting the sweet stuff?  Who's your supplier? HECTOR: I don't understand. I thought we were friends.  : The last thing we want to do is upset bees! (Hector takes a thumbtack out of the board behind him and sword-fights Barry. Barry is using his stinger like a sword)  : You're too late! It's ours now! BARRY: You, sir, have crossed the wrong sword! HECTOR: You, sir, will be lunch for my iguana, Ignacio! (Barry hits the thumbtack out of Hectors hand and Hector surrenders) Barry: Where is the honey coming from?  : Tell me where! HECTOR: (Pointing to leaving truck) Honey Farms! It comes from Honey Farms! (Barry chases after the truck but it is getting away. He flies onto a bicyclists' backpack and he catches up to the truck) CAR DRIVER: (To bicyclist) Crazy person! (Barry flies off and lands on the windshield of the Honey farms truck. Barry looks around and sees dead bugs splattered everywhere) BARRY: What horrible thing has happened here?   : These faces, they never knew what hit them. And now  : they're on the road to nowhere! (Barry hears a sudden whisper) (Barry looks up and sees Mooseblood, a mosquito playing dead) MOOSEBLOOD: Just keep still. BARRY: What? You're not dead? MOOSEBLOOD: Do I look dead? They will wipe anything that moves. Where you headed? BARRY: To Honey Farms. I am onto something huge here. MOOSEBLOOD: I'm going to Alaska. Moose blood, crazy stuff. Blows your head off! ANOTHER BUG PLAYING DEAD: I'm going to Tacoma. (Barry looks at another bug) BARRY: - And you? MOOSEBLOOD: - He really is dead. BARRY: All right. (Another bug hits the windshield and the drivers notice. They activate the windshield wipers) MOOSEBLOOD== Uh-oh! (The windshield wipers are slowly sliding over the dead bugs and wiping  them off) BARRY: - What is that?! MOOSEBLOOD: - Oh, no!  : - A wiper! Triple blade! BARRY: - Triple blade? MOOSEBLOOD: Jump on! It's your only chance, bee! (Mooseblood and Barry grab onto the wiper and they hold on as it wipes the windshield) Why does everything have to be so doggone clean?!  : How much do you people need to see?! (Bangs on windshield)  : Open your eyes! Stick your head out the window! RADIO IN TRUCK: From NPR News in Washington, I'm Carl Kasell. MOOSEBLOOD: But don't kill no more bugs! (Mooseblood and Barry are washed off by the wipr fluid) MOOSEBLOOD: - Bee! BARRY: - Moose blood guy!! (Barry starts screaming as he hangs onto the antenna) (Suddenly it is revealed that a water bug is also hanging on the antenna.  There is a pause and then Barry and the water bug both start screaming) TRUCK DRIVER: - You hear something? GUY IN TRUCK: - Like what? TRUCK DRIVER: Like tiny screaming. GUY IN TRUCK: Turn off the radio. (The antenna starts to lower until it gets to low and sinks into the truck. The water bug flies off and Barry is forced to let go and he is blown away. He luckily lands inside a horn on top of the truck where he finds Mooseblood, who was blown into the same place) MOOSEBLOOD: Whassup, bee boy? BARRY: Hey, Blood. (Fast forward in time and we see that Barry is deep in conversation with Mooseblood. They have been sitting in this truck for a while) BARRY: ...Just a row of honey jars, as far as the eye could see. MOOSEBLOOD: Wow! BARRY: I assume wherever this truck goes is where they're getting it.  : I mean, that honey's ours. MOOSEBLOOD: - Bees hang tight. BARRY:  - We're all jammed in.  : It's a close community. MOOSEBLOOD: Not us, man. We on our own. Every mosquito on his own. BARRY: - What if you get in trouble? MOOSEBLOOD: - You a mosquito, you in trouble.  : Nobody likes us. They just smack. See a mosquito, smack, smack! BARRY: At least you're out in the world. You must meet girls. MOOSEBLOOD: Mosquito girls try to trade up, get with a moth, dragonfly.  : Mosquito girl don't want no mosquito. (An ambulance passes by and it has a blood donation sign on it) You got to be kidding me!  : Mooseblood's about to leave the building! So long, bee! (Mooseblood leaves and flies onto the window of the ambulance where there are other mosquito's hanging out)  : - Hey, guys! OTHER MOSQUITO: - Mooseblood!  MOOSEBLOOD: I knew I'd catch y'all down here. Did you bring your crazy straw? (The truck goes out of view and Barry notices that the truck he's on is pulling into a camp of some sort) TRUCK DRIVER: We throw it in jars, slap a label on it, and it's pretty much pure profit. (Barry flies out) BARRY: What is this place? BEEKEEPER 1#: A bee's got a brain the size of a pinhead. BEEKEEPER #2: They are pinheads!  : Pinhead.  : - Check out the new smoker. BEEKEEPER #1: - Oh, sweet. That's the one you want.  : The Thomas 3000! BARRY: Smoker? BEEKEEPER #1: Ninety puffs a minute, semi-automatic. Twice the nicotine, all the tar.  : A couple breaths of this knocks them right out.  BEEKEEPER #2: They make the honey, and we make the money. BARRY: "They make the honey, and we make the money"? (The Beekeeper sprays hundreds of cheap miniature apartments with the smoker. The bees are fainting or passing out) Oh, my!  : What's going on? Are you OK? (Barry flies into one of the apartment and helps a Bee couple get off the ground. They are coughing and its hard for them to stand) BEE IN APARTMENT: Yeah. It doesn't last too long. BARRY: Do you know you're in a fake hive with fake walls? BEE IN APPARTMENT: Our queen was moved here. We had no choice. (The apartment room is completely empty except for a photo on the wall of the "queen" who is obviously a man in women's clothes) BARRY: This is your queen? That's a man in women's clothes!  : That's a drag queen!  : What is this? (Barry flies out and he discovers that there are hundreds of these structures, each housing thousands of Bees) Oh, no!  : There's hundreds of them! (Barry takes out his camera and takes pictures of these Bee work camps. The beekeepers look very evil in these depictions)  Bee honey.  : Our honey is being brazenly stolen on a massive scale!  : This is worse than anything bears have done! I intend to do something. (Flash forward in time and Barry is showing these pictures to his parents) JANET: Oh, Barry, stop. MARTIN: Who told you humans are taking our honey? That's a rumor. BARRY: Do these look like rumors? (Holds up the pictures) UNCLE CARL: That's a conspiracy theory. These are obviously doctored photos. JANET: How did you get mixed up in this? ADAM: He's been talking to humans. JANET: - What? MARTIN: - Talking to humans?! ADAM: He has a human girlfriend. And they make out! JANET: Make out? Barry!  BARRY: We do not. ADAM: - You wish you could. MARTIN: - Whose side are you on? BARRY: The bees! UNCLE CARL: (He has been sitting in the back of the room this entire time) I dated a cricket once in San Antonio. Those crazy legs kept me up all night. JANET: Barry, this is what you want to do with your life? BARRY: I want to do it for all our lives. Nobody works harder than bees!  : Dad, I remember you coming home so overworked  : your hands were still stirring. You couldn't stop. JANET: I remember that. BARRY: What right do they have to our honey?  : We live on two cups a year. They put it in lip balm for no reason whatsoever!  ADAM: Even if it's true, what can one bee do? BARRY: Sting them where it really hurts. MARTIN: In the face! The eye!  : - That would hurt. BARRY: - No. MARTIN: Up the nose? That's a killer. BARRY: There's only one place you can sting the humans, one place where it matters. (Flash forward a bit in time and we are watching the Bee News) BEE NEWS NARRATOR: Hive at Five, the hive's only full-hour action news source. BEE PROTESTOR: No more bee beards! BEE NEWS NARRATOR: With Bob Bumble at the anchor desk.  : Weather with Storm Stinger.  : Sports with Buzz Larvi.  : And Jeanette Chung. BOB BUMBLE: - Good evening. I'm Bob Bumble. JEANETTE CHUNG:  - And I'm Jeanette Chung. BOB BUMBLE: A tri-county bee, Barry Benson,  : intends to sue the human race for stealing our honey,  : packaging it and profiting from it illegally! JEANETTE CHUNG: Tomorrow night on Bee Larry King,  : we'll have three former queens here in our studio, discussing their new book,  : Classy Ladies, out this week on Hexagon. (The scene changes to an interview on the news with Bee version of Larry King and Barry) BEE LARRY KING: Tonight we're talking to Barry Benson.  : Did you ever think, "I'm a kid from the hive. I can't do this"? BARRY: Bees have never been afraid to change the world.  : What about Bee Columbus? Bee Gandhi? Bejesus? BEE LARRY KING: Where I'm from, we'd never sue humans.   : We were thinking of stickball or candy stores. BARRY: How old are you? BEE LARRY KING: The bee community is supporting you in this case,  : which will be the trial of the bee century. BARRY: You know, they have a Larry King in the human world too. BEE LARRY KING: It's a common name. Next week... BARRY: He looks like you and has a show and suspenders and colored dots... BEE LARRY KING: Next week... BARRY: Glasses, quotes on the bottom from the guest even though you just heard 'em. BEE LARRY KING: Bear Week next week! They're scary, hairy and here, live. (Bee Larry King gets annoyed and flies away offscreen) BARRY: Always leans forward, pointy shoulders, squinty eyes, very Jewish. (Flash forward in time. We see Vanessa enter and Ken enters behind her. They are arguing)  KEN: In tennis, you attack at the point of weakness! VANESSA: It was my grandmother, Ken. She's 81. KEN== Honey, her backhand's a joke! I'm not gonna take advantage of that? BARRY: (To Ken) Quiet, please. Actual work going on here. KEN: (Pointing at Barry) - Is that that same bee? VANESSA: - Yes, it is!  : I'm helping him sue the human race. BARRY: - Hello. KEN: - Hello, bee. VANESSA: This is Ken. BARRY: (Recalling the "Winter Boots" incident earlier) Yeah, I remember you. Timberland, size ten and a half. Vibram sole, I believe. KEN: (To Vanessa) Why does he talk again? VANESSA:  Listen, you better go 'cause we're really busy working. KEN: But it's our yogurt night! VANESSA: (Holding door open for Ken) Bye-bye. KEN: (Yelling) Why is yogurt night so difficult?! (Ken leaves and Vanessa walks over to Barry. His workplace is a mess) VANESSA: You poor thing. You two have been at this for hours! BARRY: Yes, and Adam here has been a huge help. ADAM: - Frosting... - How many sugars?  ==BARRY== Just one. I try not to use the competition.  : So why are you helping me? VANESSA: Bees have good qualities.  : And it takes my mind off the shop.  : Instead of flowers, people are giving balloon bouquets now. BARRY:  Those are great, if you're three. VANESSA: And artificial flowers. BARRY: - Oh, those just get me psychotic! VANESSA: - Yeah, me too.  : BARRY: Bent stingers, pointless pollination. ADAM: Bees must hate those fake things!  : Nothing worse than a daffodil that's had work done.  : Maybe this could make up for it a little bit. VANESSA: - This lawsuit's a pretty big deal. BARRY: - I guess. ADAM: You sure you want to go through with it? BARRY: Am I sure? When I'm done with the humans, they won't be able  : to say, "Honey, I'm home," without paying a royalty! (Flash forward in time and we are watching the human news. The camera shows  a crowd outside a courthouse) NEWS REPORTER: It's an incredible scene here in downtown Manhattan,  : where the world anxiously waits, because for the first time in history,  : we will hear for ourselves if a honeybee can actually speak. (We are no longer watching through a news camera) ADAM: What have we gotten into here, Barry? BARRY: It's pretty big, isn't it? ADAM== (Looking at the hundreds of people around the courthouse) I can't believe how many humans don't work during the day. BARRY: You think billion-dollar multinational food companies have good lawyers? SECURITY GUARD: Everybody needs to stay behind the barricade. (A limousine drives up and a fat man,Layton Montgomery, a honey industry owner gets out and walks past Barry) ADAM: - What's the matter? BARRY: - I don't know, I just got a chill. (Fast forward in time and everyone is in the court) MONTGOMERY: Well, if it isn't the bee team.  (To Honey Industry lawyers) You boys work on this? MAN: All rise! The Honorable Judge Bumbleton presiding. JUDGE BUMBLETON: All right. Case number 4475,  : Superior Court of New York, Barry Bee Benson v. the Honey Industry  : is now in session.  : Mr. Montgomery, you're representing the five food companies collectively? MONTGOMERY: A privilege. JUDGE BUMBLETON: Mr. Benson... you're representing all the bees of the world? (Everyone looks closely, they are waiting to see if a Bee can really talk) (Barry makes several buzzing sounds to sound like a Bee) BARRY: I'm kidding. Yes, Your Honor, we're ready to proceed. JUDGE BUMBLBETON: Mr. Montgomery, your opening statement, please. MONTGOMERY: Ladies and gentlemen of the jury,  : my grandmother was a simple woman.  :  Born on a farm, she believed it was man's divine right  : to benefit from the bounty of nature God put before us.  : If we lived in the topsy-turvy world Mr. Benson imagines,  : just think of what would it mean.  : I would have to negotiate with the silkworm  : for the elastic in my britches!  : Talking bee! (Montgomery walks over and looks closely at Barry)  : How do we know this isn't some sort of  : holographic motion-picture-capture Hollywood wizardry?  : They could be using laser beams!  : Robotics! Ventriloquism! Cloning! For all we know,  : he could be on steroids! JUDGE BUMBLETON: Mr. Benson?  BARRY: Ladies and gentlemen, there's no trickery here.  : I'm just an ordinary bee. Honey's pretty important to me.  : It's important to all bees. We invented it!  : We make it. And we protect it with our lives.  : Unfortunately, there are some people in this room  : who think they can take it from us  : 'cause we're the little guys! I'm hoping that, after this is all over,  : you'll see how, by taking our honey, you not only take everything we have  : but everything we are! JANET== (To Martin) I wish he'd dress like that all the time. So nice! JUDGE BUMBLETON: Call your first witness. BARRY: So, Mr. Klauss Vanderhayden  of Honey Farms, big company you have. KLAUSS VANDERHAYDEN: I suppose so. BARRY: I see you also own Honeyburton and Honron! KLAUSS: Yes, they provide beekeepers for our farms. BARRY: Beekeeper. I find that to be a very disturbing term.  : I don't imagine you employ any bee-free-ers, do you? KLAUSS: (Quietly) - No. BARRY: - I couldn't hear you. KLAUSS: - No. BARRY: - No.  : Because you don't free bees. You keep bees. Not only that,  : it seems you thought a bear would be an appropriate image for a jar of honey. KLAUSS: They're very lovable creatures.   : Yogi Bear, Fozzie Bear, Build-A-Bear. BARRY: You mean like this? (The bear from Over The Hedge barges in through the back door and it is roaring and standing on its hind legs. It is thrashing its claws and people are screaming. It is being held back by a guard who has the bear on a chain)  : (Pointing to the roaring bear) Bears kill bees!  : How'd you like his head crashing through your living room?!  : Biting into your couch! Spitting out your throw pillows! JUDGE BUMBLETON: OK, that's enough. Take him away. (The bear stops roaring and thrashing and walks out) BARRY: So, Mr. Sting, thank you for being here. Your name intrigues me.  : - Where have I heard it before? MR. STING: - I was with a band called The Police. BARRY: But you've never been a police officer, have you? STING: No, I haven't. BARRY:  No, you haven't. And so here we have yet another example  : of bee culture casually stolen by a human  : for nothing more than a prance-about stage name. STING: Oh, please. BARRY: Have you ever been stung, Mr. Sting?  : Because I'm feeling a little stung, Sting.  : Or should I say... Mr. Gordon M. Sumner! MONTGOMERY: That's not his real name?! You idiots! BARRY: Mr. Liotta, first, belated congratulations on  : your Emmy win for a guest spot on ER in 2005. RAY LIOTTA: Thank you. Thank you. BARRY: I see from your resume that you're devilishly handsome  : with a churning inner turmoil  that's ready to blow. RAY LIOTTA: I enjoy what I do. Is that a crime? BARRY: Not yet it isn't. But is this what it's come to for you?  : Exploiting tiny, helpless bees so you don't  : have to rehearse your part and learn your lines, sir? RAY LIOTTA: Watch it, Benson! I could blow right now! BARRY: This isn't a goodfella. This is a badfella! (Ray Liotta looses it and tries to grab Barry) RAY LIOTTA: Why doesn't someone just step on this creep, and we can all go home?! JUDGE BUMBLETON: - Order in this court! RAY LIOTTA: - You're all thinking it! (Judge Bumbleton starts banging her gavel) JUDGE BUMBLETON: Order! Order, I say! RAY LIOTTA: - Say it! MAN:  - Mr. Liotta, please sit down! (We see a montage of magazines which feature the court case) (Flash forward in time and Barry is back home with Vanessa) BARRY: I think it was awfully nice of that bear to pitch in like that. VANESSA: I think the jury's on our side. BARRY: Are we doing everything right,you know, legally? VANESSA: I'm a florist. BARRY: Right. Well, here's to a great team. VANESSA: To a great team! (Ken walks in from work. He sees Barry and he looks upset when he sees Barry clinking his glass with Vanessa) KEN: Well, hello. VANESSA: - Oh, Ken! BARRY: - Hello! VANESSA: I didn't think you were coming.  : No, I was just late. I tried to call, but... (Ken holds up his phone and flips it open. The phone has no charge) ...the battery... VANESSA:  I didn't want all this to go to waste, so I called Barry. Luckily, he was free. KEN: Oh, that was lucky. (Ken sits down at the table across from Barry and Vanessa leaves the room) VANESSA: There's a little left. I could heat it up. KEN: (Not taking his eyes off Barry) Yeah, heat it up, sure, whatever. BARRY: So I hear you're quite a tennis player.  : I'm not much for the game myself. The ball's a little grabby. KEN: That's where I usually sit. Right... (Points to where Barry is sitting) there. VANESSA: (Calling from other room) Ken, Barry was looking at your resume,  : and he agreed with me that eating with chopsticks isn't really a special skill. KEN: (To Barry) You think I don't see what you're doing? BARRY: I know how hard it is to find the right job. We have that in common.  KEN: Do we? BARRY: Bees have 100 percent employment, but we do jobs like taking the crud out. KEN: (Menacingly) That's just what I was thinking about doing. (Ken reaches for a fork on the table but knocks if on the floor. He goes to pick it up) VANESSA: Ken, I let Barry borrow your razor for his fuzz. I hope that was all right. (Ken quickly rises back up after hearing this but hits his head on the table and yells) BARRY: I'm going to drain the old stinger. KEN: Yeah, you do that. (Barry flies past Ken to get to the bathroom and Ken freaks out, splashing some of the wine he was using to cool his head in his eyes. He yells in anger) (Barry looks at the magazines featuring his victories in court) BARRY: Look at that. (Barry flies into the bathroom) (He puts his hand on his head but this makes hurts him and makes him even madder. He yells again) (Barry is washing his hands in the sink but then Ken walks in) KEN: You know, you know I've just about had it (Closes bathroom door behind him) with your little mind games. (Ken is menacingly rolling up a magazine) BARRY:  (Backing away) - What's that? KEN: - Italian Vogue. BARRY: Mamma mia, that's a lot of pages. KEN: It's a lot of ads. BARRY: Remember what Van said, why is your life more valuable than mine? KEN: That's funny, I just can't seem to recall that! (Ken smashes everything off the sink with the magazine and Barry narrowly escapes) (Ken follows Barry around and tries to hit him with the magazine but he keeps missing) (Ken gets a spray bottle)  : I think something stinks in here! BARRY: (Enjoying the spray) I love the smell of flowers. (Ken holds a lighter in front of the spray bottle) KEN: How do you like the smell of flames?! BARRY: Not as much. (Ken fires his make-shift flamethrower but misses Barry, burning the bathroom. He torches the whole room but looses his footing and falls into the bathtub. After getting hit in the head by falling objects 3 times he picks up the shower head, revealing a Water bug hiding under it) WATER BUG: Water bug! Not taking sides!  (Barry gets up out of a pile of bathroom supplies and he is wearing a chapstick hat) BARRY: Ken, I'm wearing a Chapstick hat! This is pathetic! (Ken switches the shower head to lethal) KEN: I've got issues! (Ken sprays Barry with the shower head and he crash lands into the toilet) (Ken menacingly looks down into the toilet at Barry) Well, well, well, a royal flush! BARRY: - You're bluffing. KEN: - Am I? (flushes toilet) (Barry grabs a chapstick from the toilet seat and uses it to surf in the flushing toilet) BARRY: Surf's up, dude! (Barry flies out of the toilet on the chapstick and sprays Ken's face with the toilet water)  : EW,Poo water! BARRY: That bowl is gnarly. KEN: (Aiming a toilet cleaner at Barry) Except for those dirty yellow rings! (Barry cowers and covers his head and Vanessa runs in and takes the toilet cleaner from Ken just before he hits Barry) VANESSA: Kenneth! What are you doing?! KEN== (Leaning towards Barry)  You know, I don't even like honey! I don't eat it! VANESSA: We need to talk! (Vanessa pulls Ken out of the bathroom)  : He's just a little bee!  : And he happens to be the nicest bee I've met in a long time! KEN: Long time? What are you talking about?! Are there other bugs in your life? VANESSA: No, but there are other things bugging me in life. And you're one of them! KEN: Fine! Talking bees, no yogurt night...  : My nerves are fried from riding on this emotional roller coaster! VANESSA: Goodbye, Ken. (Ken huffs and walks out and slams the door. But suddenly he walks back in and stares at Barry)  : And for your information, I prefer sugar-free, artificial sweeteners MADE BY MAN! (Ken leaves again and Vanessa leans in towards Barry) VANESSA: I'm sorry about all that. (Ken walks back in again)  KEN: I know it's got an aftertaste! I LIKE IT! (Ken leaves for the last time) VANESSA: I always felt there was some kind of barrier between Ken and me.  : I couldn't overcome it. Oh, well.  : Are you OK for the trial? BARRY: I believe Mr. Montgomery is about out of ideas. (Flash forward in time and Barry, Adam, and Vanessa are back in court) MONTGOMERY-- We would like to call Mr. Barry Benson Bee to the stand. ADAM: Good idea! You can really see why he's considered one of the best lawyers... (Barry stares at Adam) ...Yeah. LAWYER: Layton, you've gotta weave some magic with this jury, or it's gonna be all over. MONTGOMERY: Don't worry. The only thing I have to do to turn this jury around  : is to remind them of what they don't like about bees. (To lawyer)  - You got the tweezers? LAWYER: - Are you allergic? MONTGOMERY: Only to losing, son. Only to losing.  : Mr. Benson Bee, I'll ask you what I think we'd all like to know.  : What exactly is your relationship (Points to Vanessa)  : to that woman? BARRY: We're friends. MONTGOMERY: - Good friends? BARRY: - Yes. MONTGOMERY: How good? Do you live together? ADAM: Wait a minute...  : MONTGOMERY: Are you her little...  : ...bedbug? (Adam's stinger starts vibrating. He is agitated) I've seen a bee documentary or two. From what I understand,   : doesn't your queen give birth to all the bee children? BARRY: - Yeah, but... MONTGOMERY: (Pointing at Janet and Martin) - So those aren't your real parents! JANET: - Oh, Barry... BARRY: - Yes, they are! ADAM: Hold me back! (Vanessa tries to hold Adam back. He wants to sting Montgomery) MONTGOMERY: You're an illegitimate bee, aren't you, Benson? ADAM: He's denouncing bees! MONTGOMERY: Don't y'all date your cousins? (Montgomery leans over on the jury stand and stares at Adam) VANESSA: - Objection! (Vanessa raises her hand to object but Adam gets free. He flies straight at Montgomery) =ADAM: - I'm going to pincushion this guy! BARRY: Adam, don't! It's what he wants! (Adam stings Montgomery in the butt and he starts thrashing around)  MONTGOMERY: Oh, I'm hit!!  : Oh, lordy, I am hit! JUDGE BUMBLETON: (Banging gavel) Order! Order! MONTGOMERY: (Overreacting) The venom! The venom is coursing through my veins!  : I have been felled by a winged beast of destruction!  : You see? You can't treat them like equals! They're striped savages!  : Stinging's the only thing they know! It's their way! BARRY: - Adam, stay with me. ADAM: - I can't feel my legs. MONTGOMERY: (Overreacting and throwing his body around the room) What angel of mercy will come forward to suck the poison  : from my heaving buttocks? JUDGE BUMLBETON: I will have order in this court. Order!   : Order, please! (Flash forward in time and we see a human news reporter) NEWS REPORTER: The case of the honeybees versus the human race  : took a pointed turn against the bees  : yesterday when one of their legal team stung Layton T. Montgomery. (Adam is laying in a hospital bed and Barry flies in to see him) BARRY: - Hey, buddy. ADAM: - Hey. BARRY: - Is there much pain? ADAM: - Yeah.  : I...  : I blew the whole case, didn't I? BARRY: It doesn't matter. What matters is you're alive. You could have died. ADAM: I'd be better off dead. Look at me. (A small plastic sword is replaced as Adam's stinger) They got it from the cafeteria downstairs, in a tuna sandwich.   : Look, there's a little celery still on it. (Flicks off the celery and sighs) BARRY: What was it like to sting someone? ADAM: I can't explain it. It was all...  : All adrenaline and then... and then ecstasy! BARRY: ...All right. ADAM: You think it was all a trap? BARRY: Of course. I'm sorry. I flew us right into this.  : What were we thinking? Look at us. We're just a couple of bugs in this world. ADAM: What will the humans do to us if they win? BARRY: I don't know. ADAM: I hear they put the roaches in motels. That doesn't sound so bad. BARRY: Adam, they check in, but they don't check out!  ADAM: Oh, my. (Coughs) Could you get a nurse to close that window? BARRY: - Why? ADAM: - The smoke. (We can see that two humans are smoking cigarettes outside)  : Bees don't smoke. BARRY: Right. Bees don't smoke.  : Bees don't smoke! But some bees are smoking.  : That's it! That's our case! ADAM: It is? It's not over? BARRY: Get dressed. I've gotta go somewhere.  : Get back to the court and stall. Stall any way you can. (Flash forward in time and Adam is making a paper boat in the courtroom) ADAM: And assuming you've done step 29 correctly, you're ready for the tub! (We see that the jury have each made their own paper boats after being taught how by Adam. They all look confused) JUDGE BUMBLETON:  Mr. Flayman. ADAM: Yes? Yes, Your Honor! JUDGE BUMBLETON: Where is the rest of your team? ADAM: (Continues stalling) Well, Your Honor, it's interesting.  : Bees are trained to fly haphazardly,  : and as a result, we don't make very good time.  : I actually heard a funny story about... MONTGOMERY: Your Honor, haven't these ridiculous bugs  : taken up enough of this court's valuable time?  : How much longer will we allow these absurd shenanigans to go on?  : They have presented no compelling evidence to support their charges  : against my clients, who run legitimate businesses.  : I move for a complete dismissal  of this entire case! JUDGE BUMBLETON: Mr. Flayman, I'm afraid I'm going  : to have to consider Mr. Montgomery's motion. ADAM: But you can't! We have a terrific case. MONTGOMERY: Where is your proof? Where is the evidence?  : Show me the smoking gun! BARRY: (Barry flies in through the door) Hold it, Your Honor! You want a smoking gun?  : Here is your smoking gun. (Vanessa walks in holding a bee smoker. She sets it down on the Judge's podium) JUDGE BUMBLETON: What is that? BARRY: It's a bee smoker! MONTGOMERY: (Picks up smoker) What, this? This harmless little contraption?  : This couldn't hurt a fly, let alone a bee. (Montgomery accidentally fires it at the bees in the crowd and they faint  and cough) (Dozens of reporters start taking pictures of the suffering bees) BARRY: Look at what has happened  : to bees who have never been asked, "Smoking or non?"  : Is this what nature intended for us?  : To be forcibly addicted to smoke machines  : and man-made wooden slat work camps?  : Living out our lives as honey slaves to the white man? (Barry points to the honey industry owners. One of them is an African American so he awkwardly separates himself from the others) LAWYER: - What are we gonna do? - He's playing the species card. BARRY: Ladies and gentlemen, please, free these bees! ADAM AND VANESSA: Free the bees! Free the bees! BEES IN CROWD: Free the bees! HUMAN JURY: Free the bees! Free the bees! JUDGE BUMBLETON: The court finds in favor of the bees!  BARRY: Vanessa, we won! VANESSA: I knew you could do it! High-five! (Vanessa hits Barry hard because her hand is too big)  : Sorry. BARRY: (Overjoyed) I'm OK! You know what this means?  : All the honey will finally belong to the bees.  : Now we won't have to work so hard all the time. MONTGOMERY: This is an unholy perversion of the balance of nature, Benson.  : You'll regret this. (Montgomery leaves and Barry goes outside the courtroom. Several reporters start asking Barry questions) REPORTER 1#: Barry, how much honey is out there? BARRY: All right. One at a time. REPORTER 2#: Barry, who are you wearing? BARRY: My sweater is Ralph Lauren, and I have no pants.  (Barry flies outside with the paparazzi and Adam and Vanessa stay back) ADAM: (To Vanessa) - What if Montgomery's right? Vanessa: - What do you mean? ADAM: We've been living the bee way a long time, 27 million years. (Flash forward in time and Barry is talking to a man) BUSINESS MAN: Congratulations on your victory. What will you demand as a settlement? BARRY: First, we'll demand a complete shutdown of all bee work camps. (As Barry is talking we see a montage of men putting "closed" tape over the work camps and freeing the bees in the c…

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[983baa818f...](https://github.com/treckstar/yolo-octo-hipster/commit/983baa818fb3d508c7539c0420faba0b224e9447)
#### Friday 2023-11-17 18:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3fb80de9b5...](https://github.com/mrakgr/The-Spiral-Language/commit/3fb80de9b59cec06bfe9f69c3e200f47558faa4b)
#### Friday 2023-11-17 18:41:27 by mrakgr

"9:15 AM. No update for my keyboard. It seems it is still in Hungary.

https://youtu.be/YWimz6rfuls
This is 99% why your aim is bad.

https://youtu.be/gNDfH7J2DNE
Fix Your Terrible Mouse Grip NATURALLY

Today, what I'm doing is trying out the claw grip, even on the track ball mouse.

I'm going to try letting my fist stay in the shape of a clove. In other words, it's a fully relaxed posture. I want to see whether that makes any difference to my rsi. One thing I noticed since I am actually using my whole arm tool move the mouse cursor. It's a lot more accurate than just using my thumb.

https://youtu.be/5S9iwYnndp8
The Optimal Contact Points For Aiming

Right now entering out the claw grip. And it's really **** amazing how much more accurate I am. Instead of using the damp, I'm rotating my wrist to move the mouse cursor. The reason why I couldn't do that before and why I've been using the pole grip for 20 years is because of that a desk. It has a very, very.very little space between the keyboard and the mouse and the top of the ceiling. By ceiling, I mean, it's kind of like a pull out desk, which has a board in the middle. Now that I'm using a regular desk, I have a lot more space above for my hand to move. I should try typing that way as well.

I have a hypothesis that my whole rsi in the right hand isn't so much because of typing, though the volume I put in certainly contributed to it. But because I've been using the palm grip on both the mouse and the keyboard.

https://youtu.be/5S9iwYnndp8?t=50
> When we grip the mouse with the tips, we gain dexterity.

I've been using the mouse for 20 years, and this is the first time discovering this.

https://youtu.be/5S9iwYnndp8?t=145
> If someone you know has a messy handwriting, have a look at their grip. You'll be surprised to know how much of one of their fingers or more are hyper extended.

https://youtu.be/qh7fqjNqCLw
Fixing X-Pro Gamer's Worst Habit (You Do This Too)

Now that I've changed my grip It feels like I am flowing with this track ball. It is so much better now.

10:45 AM. I think I figured it out. All the flaws in my technique. The reason I have an size is probably the way I hold my hands. My left hand is mostly in deflection position by all my right hand is extended. That is how I use the keyboard in general. And that is how I use the mouse.

I think once I adjust my grip, the other side should go away. So I'll need to test it for another few weeks.

Using voice dictation for most of my unstructured text input as well as an ergonomic mouse and the keyboard I'm going to get should be enough to fix it.

https://deepmind.google/discover/blog/transforming-the-future-of-music-creation/

Music generation. Now this is something I've been waiting for a long time.

https://blog.jim-nielsen.com/2023/html-web-components-an-example/

https://youtu.be/R4Ri4ft7bXY
The Good, The Bad, and The Web Components - Zach Leatherman | JSHeroes 2023

3:00 PM. https://youtu.be/C8RtH2eoBU8?list=PL8JmJYDyXnXlrwJPh3ve11lxhNBXQGw64
Witch Weapon Story [CHAPTER 8] [PART 2]

3:10 PM. Let me check on just a bit and then I'll start writing. I've been resting too much.

3:30 PM. Right now I'm not using the keyboard with my right hand too much. I mostly focusing on the left. Thinking about it objectively, I'm doing a lot of weird movements and contortions, even made by a left hand. My typing technique is pretty messed up either way. I think that it's not worth fixing. The keyboard, the regular keyboard that I have is pretty badly designed So it's just so the way I'm typing is just a consequence of that.

Once the glove ate the keyboard arrives, I'll be able to correct my typing.

And right now...

///

Package status: In transit (8 Days)
Country: China -> Croatia
2023-11-15 18:00 HU, International flight has arrived
2023-11-13 13:24 HK, International flight has departed
2023-11-12 19:32 CN, Arrived at the origin international airport
2023-11-12 09:32 Mainland China, CN, Shipment is in transit to next facility
2023-11-12 00:19 Mainland China, CN, Departed from sort facility
2023-11-10 20:50 Mainland China, CN, Arrived at origin facility
2023-11-10 16:07 Mainland China, CN, Shipment picked up
2023-11-10 14:02 Sesvete, HR, We are exchanging data internally
2023-11-07 15:53 Shipment information received
======================================
Powered by www.17track.net

///

It seems that the package is still in Hungary. It's really thinking about to leave from the airport. I thought that would have been done long ago. So far I've been waiting for it to 10 days. Once I get the keyboard, I'll do a programming session. So far my rsi has already taken six weeks from me. Maybe the keyboard will create a miracle. If not, I'll have to learn how to program using a combination of typing and voice programming.

7:25 PM. Word Count's at 8.9 K.

Unlikely the previous chapters I'm going to step up posting these as zip files. It's a waste of time. Instead, I'll just share a link to the Google Docs document.

I'll prove read it tomorrow and then post it. Tomorrow is Saturday, so I have work."

---
## [EpicTaru/LSB](https://github.com/EpicTaru/LSB)@[aa30c9ec2e...](https://github.com/EpicTaru/LSB/commit/aa30c9ec2e15fd526fca9080ab434939d12a9656)
#### Friday 2023-11-17 18:54:26 by MowFord

Cait Sith Avatar:

- Cait sith has proper name prefix and named properly to be "Cait Sith" instead of "The CaitSith"
- BPs Implemented
  - Regal Slash (BP:Rage): 3-hit physical
  - Level ? Holy (BP:Rage): aoe magical
    - Rolls a die and does dmg proportional to roll
    - Only does damage if the target's level is divisible by the roll
  - Mewing Lullaby (BP:Ward):
  AoE lullaby that resets TP
  - Eerie Eye (BP:Ward):
  conal silence/amnesia with appropriate elemental resist check for amnesia, but retail does light check for silence
  - Reraise II (BP:Ward):
  single-target 60-minute reraise II buff for any party member
  - Raise II (BP:Ward):
  single-target raise II for any party member
  - Altana's Favor (BP:Ward):
  2-hour ability gives arise to all party members in range
  (Arise and reraise III with infinite duration)

---
## [Wannieboy07/minishell](https://github.com/Wannieboy07/minishell)@[36e3edece4...](https://github.com/Wannieboy07/minishell/commit/36e3edece4ec77cba6840c894b6a6bdcc8b28df5)
#### Friday 2023-11-17 19:27:49 by LarsCampus19

trying to get unset to work with variables and the export environment, proving extremely tedious, export also can do way more, that's gunna be annoying, got a bunch of leaks and shit can go wrong everywhere, handling it all is hard to do when so much can fail, fuck this project, this shit sucks(auto_push)

---
## [NobleMode/Frontal-Game](https://github.com/NobleMode/Frontal-Game)@[d3efacc850...](https://github.com/NobleMode/Frontal-Game/commit/d3efacc850c52b1ded9abf5c148d8591c9d4fbc6)
#### Friday 2023-11-17 19:45:43 by NobleMode

Update 0.0.02

--BIGGEST UPDATE: Whole new weapon System (customized to the brim) (still missing feature lol) (ported from old project lol)
  + Weapon Sway
  + Shooting, Reloading, Aiming and Even weapon Canting
  + Weapon logic and stuff
  + Animationsssssss (really barebone tho)
  - More weapon later (still need to fix this damn shit first)

--Added a flashlight (thank god)
--Muzzle flash and Impact (can be seen near end, have to adjust)
--Headbob adjusted (gave me a headache last time)
--HUD that actually work (and even show you the gun name and image :D)
++Previously Gun was based on an animation based recoil, now will be ported to a code based recoil for more dynamicness (is that even a word?)

---
## [GabyGO2108/Python-100-days-of-code](https://github.com/GabyGO2108/Python-100-days-of-code)@[7980237e34...](https://github.com/GabyGO2108/Python-100-days-of-code/commit/7980237e349ae58ae2162002de021d5bb80958d2)
#### Friday 2023-11-17 20:04:19 by Gaby

Create Blackjack

Boy was this challenging!!! It was a very hard project and took me a few days to complete, but it was worth it. Hope you enjoy playing this Blackjack game. Remember the rules: You or your opponent must have 21 or be the nearest to score 21 in order to win.

---
## [Kong/ngx_wasm_module](https://github.com/Kong/ngx_wasm_module)@[ecd7896846...](https://github.com/Kong/ngx_wasm_module/commit/ecd78968469ed5fa40d81a26600964535d3e6b00)
#### Friday 2023-11-17 20:28:51 by Thibault Charbonnier

refactor(proxy-wasm) improve pwexec resurrection and instance lifecycle

The main goal of this overhaul is to simplify `on_context_create`, make
it fully re-entrant *and* properly handle instance recycling at the same
time.

The way to do so, in my opinion, was to move `pwexec` creation where
`rexec` already was. In other words, always lookup the context id in the
instance rbtree, and if not found, create it. This means that
surrounding code also needed big overhauls. It also removes the
reference counting poor man's GC of the older implementation. The code
became really ugly by then so I took the time to also review this
module's code structure instead of making a *very* ugly commit.

This new ngx_proxy_wasm.c file should be much easier to read and follow
now.

One change I do not fully like is moving the `next_id` to a global
counter, but we do not have a "global proxy-wasm conf" object yet. I
also started thinking about pre-allocating a number of `pwexecs` (like
`worker_connections`) and use free/busy queue that all filter chains can
dip into to get a context id + context memory zone. Perhaps for a later
time.

---
## [strikersix23/FEX](https://github.com/strikersix23/FEX)@[bd4464bd5e...](https://github.com/strikersix23/FEX/commit/bd4464bd5ee82c34214e5e4e6568d494b73482bb)
#### Friday 2023-11-17 21:31:46 by Alyssa Rosenzweig

InstructionCountCI: Remove Optimal flags

Instruction count CI has transformed the way we work on FEX… I love the system
and want to make it better. there’s one part of instruction count CI that isn’t
so lovable: the problematic “optimal” flag on instructions.

There are several issues with this flag, both philosophical and practical.

– it is tedious to update the optimal flag when making an implementation
optimal. The effect of that is discouraging people from making instructions,
optimal, or encouraging people to fail to update the flag, and dilute the value
of it. Either way, since we care far more about optimal implementations, then we
do about updating the flag, clearly we should prioritize the implementation and
not the flag. This issue was not obvious at the outset, when instruction count,
CI was introduced, and still quite small. The problem magnified when we started
duplicating instructions in bulk for different combinations of CPU features
(flagm, AFP, etc.) that intern multiplies the manual work required to update the
flags by the corresponding constant factor. if it comes down to a choice between
removing this extra coverage and removing the flag, I think we all agree that
removing the flag is the lesser evil.

– The definition of “optimal” is fundamentally problematic. I have often
improved the instruction count of an instruction that was already “optimal”.
This is all kinds of silly, and calls into question whether there’s any value
whatsoever in the existing classifications of the flag. Furthermore, it is often
unknowable, whether an implementation really is optimal. Is it possible to
implement BZHI (with flag calculations) in fewer than eight instructions? We
don’t know, and it’s silly to pretend that we do.

– as a consequence of the problematic definitions , there are so many errors in
both directions that I don’t think there’s much value in preserving the existing
classification at the expense of +progress. Being able to say “32% of
instructions are translated optimally” is neat, but it really doesn’t tell us
anything whatsoever when you dig a little deeper.

So, as the flag is misleading at best and perhaps harmful at worst, let’s remove
it and make the instruction count CI, more useful overall. let’s let the
expected count and the assembly speak for themselves, and cut away the chaff. if
we want a meaningless number to report to management, we can instead calculate
the average blowup factor ;-)

Signed-off-by: Alyssa Rosenzweig <alyssa@rosenzweig.io>

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[a14871edee...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/a14871edeea61ab549d738c65b526cf0894a4e71)
#### Friday 2023-11-17 21:32:26 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

---
## [p3rseph0ne/restaurant-guru](https://github.com/p3rseph0ne/restaurant-guru)@[f1b0e3d6c3...](https://github.com/p3rseph0ne/restaurant-guru/commit/f1b0e3d6c3923f80a6d11826e2da8801da177b15)
#### Friday 2023-11-17 21:38:35 by p3rseph0ne

db connection works now, I also hate my life and have to add a new interface

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[830e002a27...](https://github.com/Zonespace27/cmss13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Friday 2023-11-17 21:38:58 by QuickLode

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
## [petekinnecom/test_launcher](https://github.com/petekinnecom/test_launcher)@[d3a4fedb81...](https://github.com/petekinnecom/test_launcher/commit/d3a4fedb811d5ad7bbf13e9e0ce5b1c6d176ea58)
#### Friday 2023-11-17 22:18:11 by Pete Kinnecom

Update app root logic

We have a case where the current logic for finding the app root is not
working. It's a case with the following:

/path/to/app/subdir/test/my_test.rb

Previously, we would determine the app root to be `/path/to/app/subdir`
because we simply took the parent directory to the `test/` directory.
In the event that we had multiple test directories, then we would look
for the presence of a Gemfile|gemspec|etc.

We now always determine the app root based on the presence of the
Gemfile|gemspec|etc and fallback to the parent directory of the `test/`
directory if one is not found.

This causes a huge pain in the butt in the tests, because we now always
hit the file system. What I should do is change the "MemorySearcher" to
just actually write to the filesystem and let the tests actually search
it. But in the meantime, I've added this set of ugly hacks to write to a
tmpdir but pretend we didn't. :( Oh well, being scrappy here.

---
## [dundargoc/neovim](https://github.com/dundargoc/neovim)@[cd12708b64...](https://github.com/dundargoc/neovim/commit/cd12708b64e7a12329649830c9ec3abd684a1793)
#### Friday 2023-11-17 22:54:53 by dundargoc

fixup: burn in hell clint, hope you die a painful death

---

