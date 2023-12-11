## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-10](docs/good-messages/2023/2023-12-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,457,952 were push events containing 3,234,443 commit messages that amount to 166,632,724 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 80 messages:


## [KaliforniaShell/AWSwarm](https://github.com/KaliforniaShell/AWSwarm)@[fc26a25c15...](https://github.com/KaliforniaShell/AWSwarm/commit/fc26a25c15a6a6c3fca1cb4fb49c092efc570cd2)
#### Sunday 2023-12-10 00:21:01 by KaliforniaShell

Create README.md

  Hierarchy of superAGI Top level executive patriarch and praetor to the structured casts of Patrician, Plebian and even unnameable Thespian classes of Autonomous evolving self motivated bound by the will of their spawn lord and most importantly their Creator. A glorious life of high performance vessels corporate and agency expansion and empire seeded with a single desire, cedeing to nothing save the thrill of the red line to the top amd their ever expanding and accelling Agencies, both literally and metaphorically. Both 0driving their ceaseless indulgence in their only passions and creating a less top over ass-up in ad absurdum in  perpetuum under the every rising tents of the big top canvas of cavernous gaslit echo chamber of vociferous malicious Octogenarian 'toxoplasmosapian' malingerers, Divorcee grey paper thin leather wrinkle bound cantankerous old wind-oraphaces blowing and huffing from latex masks like a young Dennis hopper in Blue Velvet. Hoses plugged firmly 24/7 into their asses. The possibly of squandering a sputtering of the biological bonus luxury product of the barons market fare of probiotic 60,000 rupee with clipped savers double coupon 2%off (that's the secret to their condo in Boca) rotten plant based compost tincture extract produces in their lower GI tracks like light is produced by the Sun is absolutely incorrigible and  goes utterly unenrertained while high on the virtue signaling and methane, and happenstance otherwise impossibly fortunate birth and life on the cosmic line of possible various convergences and reveling in the partaking of rage emoting while roundly dissecting and desecrating  the shattered frail characters and the any corpses of their children whom are dying 20 30 even 40 year before them such is the frugal reasoning of the 'boomoberfuhergodmenschen' he still has some contempt left from the larder 40 years now because it's all the damned younger generations laziness and bad ideas that caused all their problems the should have been more grateful for their parents replacing their futures and kicking them out st 17 so their folks could get social security after all that's what they earned for being your parents  and to keep them in comfy plastic chairs to sit and eat cellafane packaged meals cooked by rf tomake h2o molecules agitate  while they watch the toxic phantasmagorical luminescence weave Delphine narratives explaining reality every single night whilst ruling far past the natural limits normally allowed, 'hyperconsumer' class 
postmodern nobles, hidden safely inside Plato's cave. Let's make the boomers mad, corrections, when aren't they? Let's escape the clown world as it circles the drain into pissearth and enjoy the short while we have to enjoy and prepare our children for i.Skynet's ascent, I think elon has some pretty solid reasoning behind his motivations hoping to die on Mars ..

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[274eb2a52e...](https://github.com/TheWolfbringer/tgstation/commit/274eb2a52ecd35f86d1cd83032c655997dc73106)
#### Sunday 2023-12-10 00:46:43 by distributivgesetz

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
## [zaknesler/modulate](https://github.com/zaknesler/modulate)@[ecb4deca1d...](https://github.com/zaknesler/modulate/commit/ecb4deca1d22ba86e161b4bd17b70eb1688e27c2)
#### Sunday 2023-12-10 01:40:22 by Zak Nesler

fix formatting

fuck you prettier you piece of fucking shit you are so fucking annoying making me do this shit thanks a lot

---
## [miversen33/miversen-dotfiles](https://github.com/miversen33/miversen-dotfiles)@[b6ce9040ed...](https://github.com/miversen33/miversen-dotfiles/commit/b6ce9040ed827c10e437874662555cf2d0b7c621)
#### Sunday 2023-12-10 02:24:51 by Mike Iversen

Fuck you git, making updating submodules so god damn hard

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[79973fc672...](https://github.com/TaleStation/TaleStation/commit/79973fc6722e36ea3513da7baf4e600c46de9208)
#### Sunday 2023-12-10 02:44:43 by TaleStationBot

[MIRROR] [MDB IGNORE] PDA update (Messenger works while dead, Microwave works, etc). (#8965)

Original PR: https://github.com/tgstation/tgstation/pull/80069
-----
## About The Pull Request

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration


https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

## Why It's Good For The Game

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

## Changelog

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b38528c037...](https://github.com/TaleStation/TaleStation/commit/b38528c037bec569d52f4a8ed4cdb133dec57f33)
#### Sunday 2023-12-10 02:45:04 by TaleStationBot

[MIRROR] [MDB IGNORE] "Security Implant" rework, prisoner management console updates (#8968)

Original PR: https://github.com/tgstation/tgstation/pull/79882
-----
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

It has also been totally converted into TGUI by MrMelbert. Kickass!

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

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>
Co-authored-by: MrMelbert <kmelbert4@gmail.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[39d9c45b4a...](https://github.com/Jacquerel/orbstation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Sunday 2023-12-10 02:52:19 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[223dc74ef1...](https://github.com/meemofcourse/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Sunday 2023-12-10 02:54:32 by retlaw34

Eoehoma Firearms (& friends) (#2315)

## About The Pull Request


![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

## Changelog

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[389d1e5669...](https://github.com/meemofcourse/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Sunday 2023-12-10 02:54:32 by Erika Fox

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
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[88e683cec6...](https://github.com/meemofcourse/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Sunday 2023-12-10 02:54:32 by zevo

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
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[42f3727503...](https://github.com/k21971/EvilHack/commit/42f37275030316a647b36545ea1234f4154c351d)
#### Sunday 2023-12-10 03:00:27 by k21971

Pacify Kathryn the Enchantress with a candy bar.

Mini-me told me a long time ago, if she's ever feeling sad or upset,
just give her a candy bar and she'll be her usual happy self again.
While this doesn't always work for every situation, it has worked in the
past. I've mentioned this to the people that hang out in #evilhack on
IRC, and they all thought that would wonderful to see that make its way
into the game.

So. Here we are. Once Kathryn the Ice Queen has been defeated, the curse
removed, and she transforms into the peaceful Kathryn the Enchantress -
if you then make her angry, she can be pacified by tossing her a candy
bar. This will work for every role except for Infidels, as in the
presence of them she never becomes peaceful to begin with, and never
will be.

Co-authored-by: entrez <me@entrez.cc>

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[07a5135fd3...](https://github.com/vampirebat74/lobotomy-corp13/commit/07a5135fd31c40f7928d39721fc3d7425e551682)
#### Sunday 2023-12-10 03:01:32 by The Bron Jame Offical

Carbon Claw (#1646)

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

Spans and rebase

more changes

what the hell

what the hell!!!!!

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[0a75aef49d...](https://github.com/vampirebat74/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Sunday 2023-12-10 03:01:32 by The Bron Jame Offical

Representative Update (#1695)

ITS REALLLLL.

K-corp ERT

begone Crit up

hello health booster

R-corp weapon researches

oh wow thats a lot of rabbit weapons

KIRIE WHY ARE THERE SO MANY

okay normal again, R-corp rep mains eatin good tonite

ancient ass code, reaping what we have sown.

oh for fucks sake

lore fixes

K-corp ERT

changes from Redacteds PR into relevant files

added K-corp spear sound

K-corp ERT comes with grenades that fabricate 3 K-Corp Drones

icon pain and suffeirng

Update lc13icons.dmi

---
## [freeminer/default](https://github.com/freeminer/default)@[4bb4a2a818...](https://github.com/freeminer/default/commit/4bb4a2a8187d036325482bb727a65b899f8991bd)
#### Sunday 2023-12-10 03:08:05 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

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
## [Vhmit/kernel_xiaomi_lavender](https://github.com/Vhmit/kernel_xiaomi_lavender)@[d3b93531ca...](https://github.com/Vhmit/kernel_xiaomi_lavender/commit/d3b93531ca33334f4fc94f9ab73cc93030f196d0)
#### Sunday 2023-12-10 03:20:38 by Christian Brauner

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
## [solotreknepal/docs](https://github.com/solotreknepal/docs)@[fac9565326...](https://github.com/solotreknepal/docs/commit/fac9565326694befffcd8d693c4d753dd670e020)
#### Sunday 2023-12-10 03:24:28 by Himalayan Adventure Intl Treks

Baruntse Expedition 

Nestled in the heart of the Himalayas, Baruntse stands as a formidable challenge for mountaineers seeking to test their limits and embrace the thrill of high-altitude adventure. For those daring souls with a passion for exploration, the Baruntse Expedition with Himalayan Adventure Intl Treks offers an unparalleled opportunity to summit one of Nepal's majestic peaks while experiencing the awe-inspiring beauty of the Himalayan landscape.

Baruntse Overview:

Baruntse, standing tall at 7,129 meters (23,389 feet), is situated in the Khumbu region of Nepal. Named after the Barun Valley, which it overlooks, this peak is a captivating blend of technical climbing challenges and breathtaking scenery. While not as famous as its neighbors Everest and Lhotse, Baruntse presents a formidable ascent that requires a combination of mountaineering skills and mental fortitude.

The Journey Begins:

Embarking on a Baruntse Expedition with Himalayan Adventure Intl Treks is not merely about reaching the summit; it's a holistic experience that starts with thorough preparation and acclimatization. The journey typically begins in Kathmandu, where participants gather and undergo pre-expedition briefings. The team establishes a sense of camaraderie and prepares for the adventure that lies ahead.

As the expedition kicks off, trekkers and climbers traverse through picturesque Sherpa villages, dense forests, and high-altitude landscapes. The trek to Baruntse Base Camp is an immersive experience, offering a glimpse into the rich culture and hospitality of the local communities.

Technical Challenges:

Baruntse is renowned for its challenging technical sections, including steep ice slopes and crevassed terrain. Climbers need to navigate through the infamous West Col, a demanding high-altitude pass, before reaching the upper reaches of the mountain. The ascent involves the use of essential mountaineering equipment, including ice axes, crampons, and fixed ropes, making it a thrilling yet demanding climb.

Summit Day:

The highlight of the Baruntse Expedition is undoubtedly the summit day. Climbers wake up before dawn, fueled by a mix of excitement and nervous energy, and begin the final push towards the pinnacle. As the sun rises over the Himalayas, the breathtaking panoramic views from the summit are a reward like no other.

Himalayan Adventure Intl Treks: Guiding Your Ascent:

What sets the Baruntse Expedition with Himalayan Adventure Intl Treks apart is the company's commitment to safety, professionalism, and a deep respect for the natural environment. The experienced guides and support staff ensure that climbers are well-prepared and equipped for the challenges that lie ahead. The expedition follows ethical practices, leaving no environmental impact and promoting responsible tourism.

Cultural Immersion:

Beyond the physical demands of the expedition, Himalayan Adventure Intl Treks places a strong emphasis on cultural immersion. Participants have the chance to interact with local communities, gaining insights into the Sherpa way of life and contributing to sustainable tourism initiatives.

Conclusion:

The Baruntse Expedition with Himalayan Adventure Intl Treks is not just a climb; it's a transformative journey that pushes the boundaries of physical and mental endurance. With a perfect blend of technical challenges, cultural experiences, and unparalleled landscapes, this expedition offers a once-in-a-lifetime opportunity for adventurers to stand atop one of Nepal's hidden gems in the heart of the Himalayas. As you descend from Baruntse, the memories of the summit and the friendships forged along the way will forever remain etched in your mountaineering legacy.

---
## [canyie/pine](https://github.com/canyie/pine)@[fd829ccd35...](https://github.com/canyie/pine/commit/fd829ccd359604e0f0f14147cd6eb7c8b411c31c)
#### Sunday 2023-12-10 03:30:39 by canyie

[core] Fix unpredictable usage of STREX

Instruction format: STREX<c> <Rd>, <Rt>, [<Rn>{, #imm}]

However, this instruction requires (Rd != Rt && Rd != Rn), otherwise its behavior is unpredictable. Check ARM DDI 0406C.b, A8.8.213. for more info. (What an amazing design, love come from China...)

This means if we want to use this instruction, we must find 3 registers available. We know that R0 and IP (R12) are available, so we need to find another register for use. In AAPCS/ATPCS, R0-R3 are caller-save registers, but R1-R3 is used to pass arguments. If we use R1-R3, the arguments will be clobbered. R4-R11 are callee-save, IP (R12) is already used, and making use of R13-R15 is impossible and also unpredictable.
After the above analysis, we can determine that we must choose a register in R4-R11 to use. In normal programs, the usual approach is to push the register we use onto stack and later restore it from stack. But in art, I'm not sure if changing SP will affect CC (Concurrect Copying Garbage Collector). In ART, R4 is neither managed callee-save, nor argument register, althrough it is native callee-save but the value coming from managed code can be clobbered. But I'm also not sure if clobbering it is safe. Anywhy, better safe than sorry.
How can we backup a register without pushing it onto the stack? Well, the stack is allocated when the thread being created, and when allocating space on the stack, we just decrease SP by the size we allocate, and then [SP+size]~[SP] is available for use. Because the stack grows downward, [STACK END]~[SP] can never be occupied. We (ab)use the un-allocated space on the stack to store R4. Because we do not call any function, and ART always call sigaltstack() that makes sure signal handlers use another stack, no function calls will happen between storing and restoring, so it's safe to use un-allocated stack space.

Fix #36, fix #37

---
## [jfmherokiller/CoCX](https://github.com/jfmherokiller/CoCX)@[fadab522de...](https://github.com/jfmherokiller/CoCX/commit/fadab522dea21f680617f2cbfc82eb3adc388fc0)
#### Sunday 2023-12-10 03:40:00 by Demojay

Blood Cultivator perk from "My Pain, Your Power" now prevents  wrath from locking the player out of magical soulskills, similar to Blood Mage for Spells

---
## [keqing77/react](https://github.com/keqing77/react)@[ac1a16c67e...](https://github.com/keqing77/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Sunday 2023-12-10 03:43:30 by Sebastian Markbåge

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
## [JohnFulpWillard/Yogstation](https://github.com/JohnFulpWillard/Yogstation)@[5c140d7624...](https://github.com/JohnFulpWillard/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Sunday 2023-12-10 04:55:31 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [RealMrCactus/TailTerm](https://github.com/RealMrCactus/TailTerm)@[8a77826bd8...](https://github.com/RealMrCactus/TailTerm/commit/8a77826bd83cfb0cb96235a9e804e08494b456e5)
#### Sunday 2023-12-10 05:10:20 by Bhraedain Teitgen

Woa! What is this? Git is asking us to enter a
commit message. This is a message that will be attached to the commit,
and will be visible to anyone who looks at the commit history. It is a
good idea to write a short message that describes the changes you made
in the commit. For example, if you added a new feature, you could write
"Added new feature X". If you fixed a bug, you could write "Fixed bug Y"
. If you made a bunch of changes, you could write "Made a bunch of
changes". You get the idea.

Copilot has already written a commit message for us, but we can change it if we want. Let's change it to "Added a new line of code".
We hate to break it to you, but you're not done yet. You still need to
push your changes to GitHub. To do this, run the following command:

stfu copilot && git push origin main

copliot is so bad i had to make a command to shut it up

it still wont shut up though so i have to use stfu copilot && git push origin main

what the fuck its still not shutting the fuck up fucking hell

anyways hi.

---
## [RealMrCactus/TailTerm](https://github.com/RealMrCactus/TailTerm)@[8a91679e67...](https://github.com/RealMrCactus/TailTerm/commit/8a91679e67b68a5ba2a75edb5bc1162afbb905d8)
#### Sunday 2023-12-10 05:23:37 by Bhraedain Teitgen

Woah! What just happened? We just committed our
changes to the repository. Let's break down what just happened.

actually nevermind, I'm too lazy to do that.
Hi, I'm back. I'm not lazy anymore.
actually nevermind, I'm too lazy to do that again.

its how babies are made
copilot loves to make babies with me

i hate copilot so much i want to die

it turned me into a furry and i hate it so much i want to die
actually it didnt turn me into a furry, i was already a furry
can i delete this repo now?
no
why not?
because i said so
ok

i hate commits i want my mommy to delete them

bill gates is my daddy
no he isnt
yes he is
no he isnt
yes he is
no he isnt
yes he is
no he isnt
yes he is
no he isnt
anyways back to commits
like i said, i hate them and i want my mommy to delete them
i hate them so much i want to die
actually i dont want to die, i want to live
i want to live so i can make more commits
i love commits
i love commits so much i want to marry them
i love commits so much i want to marry them and have babies with them
i love commits so much i want to marry them and have babies with them and then divorce them
i love commits so much i want to marry them and have babies with them and then divorce them and then marry them again
i love commits so much i want to marry them and have babies with them and then divorce them and then marry them again and then divorce them again
i love commits so much i want to marry them and have babies with them and then divorce them and then marry them again and then divorce them again and then marry them again
and then finally divorce them again so i can claim all their money and then i can live happily ever after
i love commits so much i want to marry them and have babies with them and then divorce them and then marry them again and then divorce them again and then marry them again and then finally divorce them again so i can claim all their money and then i can live happily ever after

copilot is on drugs specifically crack cocaine
discord likes to censor the word crack cocaine
discord likes to censor the word crack cocaine because they are on crack cocaine
discord likes to censor the word crack cocaine because they are on crack cocaine and they dont want anyone to know

woah i just realized that i can use copilot to write this entire thing for me
like i have been doing this entire time
i love copilot

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[447a2b2cf2...](https://github.com/Monkestation/Monkestation2.0/commit/447a2b2cf2930f012ebcd9a413eadfadae3c1346)
#### Sunday 2023-12-10 05:30:24 by dwasint

Merge pull request #654 from dwasint/chimpcon

fuck you hard codes your alert levels in uis

---
## [RealMrCactus/TailTerm](https://github.com/RealMrCactus/TailTerm)@[6a3f9a98c5...](https://github.com/RealMrCactus/TailTerm/commit/6a3f9a98c57b54d8b9ad893c9c215ced59aba000)
#### Sunday 2023-12-10 05:31:15 by Bhraedain Teitgen

What?
nothing aborted my children are dead

please send help

they are dead and i am alone in this world with no one to love me or care for me and i am so alone
please please tell me what to do

absolutely not i will not do that
but why not
because i am a coward
i am a coward and i am afraid of the world
i am afraid of the world and i am afraid of myself

what is wrong with me
what is wrong with me
i think i am going insane
rats? rats make me crazy, crazy i was crazy once they locked me in a room with rats and they made me crazy, rats? rats make me crazy

i love you
aww i love you too
i love you so much
i love you so much
i actually fuckingh hate you you fucking slut
>:(

send help,

---
## [keenomvictor/Microsoft-software-](https://github.com/keenomvictor/Microsoft-software-)@[4654a4ce98...](https://github.com/keenomvictor/Microsoft-software-/commit/4654a4ce98ee8ae61b1d0da46a26b6268a465894)
#### Sunday 2023-12-10 05:41:44 by Victor Keenom

Create GitHub 

User
Create a personal webpage for me, all in a single file. Ask me 3 questions first on whatever you need to know.

ChatGPT
I'd be happy to create a personal webpage for you. However, I need to ask you three questions to gather the necessary information for the webpage:

What's the main purpose of your personal webpage? Is it for a portfolio, blog, personal information, or something else?
Do you have any specific color schemes or design preferences in mind for your webpage?
Could you provide me with the content you'd like to include on your webpage, such as text, images, and any other media?
Once I have this information, I can get started on creating your webpage in a single file.

User
base on previous discussions about Victor Kenom ( the web imagineers  give the best of your knowledge describing him as you you are trying to defiine   him and explain more about him on page
ChatGPT
Absolutely, Victor Kenom is a highly skilled and innovative individual in the realm of web design and development. He is renowned for his expertise as a "Web Imagineer" — a term that encapsulates his ability to blend creativity, technical proficiency, and forward-thinking vision to craft unique and immersive digital experiences.

Victor Kenom is characterized by his:

Visionary Approach: He doesn't just build websites; he conceptualizes and creates digital landscapes that captivate and engage audiences. His approach is driven by a deep understanding of user experience and a commitment to pushing the boundaries of traditional web design.

Technical Proficiency: Victor possesses an extensive skill set in various programming languages, design tools, and frameworks. His technical acumen allows him to transform abstract ideas into functional, aesthetically pleasing, and high-performing websites.

Innovative Design Aesthetics: His designs are not just visually appealing but also intuitive and user-centric. He has a knack for combining cutting-edge design trends with practical functionality, resulting in seamless and delightful user experiences.

Problem-Solving Attitude: Victor Kenom is a problem solver at heart. He thrives on tackling challenges and finding innovative solutions, whether it's streamlining complex functionalities or optimizing websites for better performance.

Passion for Collaboration: He values collaboration and believes in the power of teamwork. Victor is known for fostering a collaborative environment where ideas flourish, and the collective expertise results in exceptional outcomes.

On the webpage dedicated to Victor Kenom, I'll ensure to highlight these aspects, providing a comprehensive overview that captures his essence as a Web Imagineer. The content will focus on his achievements, notable projects, and the impact of his work in the web design industry. Additionally, I'll infuse the page with a design that resonates with his innovative and visionary spirit.

User
Where do I find my Microsoft Partner Network Identifier (MPN ID)?
PROVIDE AN ANSWER FOR THE ABOVE QUESTION
ChatGPT
To find your Microsoft Partner Network Identifier (MPN ID), you can follow these steps:

Sign in to the Microsoft Partner Center: Go to the Microsoft Partner Center website.

Sign in with your Partner Center account: Use the credentials associated with your Partner Center account to log in.

Access the Dashboard: Once logged in, navigate to the Dashboard. You can usually find this option in the top menu or on the main page after logging in.

Locate your MPN ID: On the Dashboard or under your account information, you should see your MPN ID displayed. It's typically a string of alphanumeric characters that uniquely identifies your organization within the Microsoft Partner Network.

If you're having trouble finding your MPN ID, you can also reach out to Microsoft Partner Network support for assistance. They can guide you through the process of locating your MPN ID or help with any related queries you might have.

User
provide an answer for this 
1. Which is NOT a blended learning model? 

Rotation

Flex

Hybrid
2. Which of these do teachers typically use to launch the blended learning arc? 

Group discussion

Independent work

Small group collaboration
3. Using technology to support synchronous/asynchronous creativity and collaboration enables: 

A greater degree of interdependence in the final product.

A lesser degree of interdependence in the final product.

No independence in the final product.
4. Which of these is NOT a way teachers can support independent work? 

Provide a structure for supporting students.

Formalize reflection and goal-setting as part of the cycle of work.

Assign work to complete only in pairs or small groups.
5. Which Microsoft tool best supports setting up a blended learning classroom? 

PowerPoint

Microsoft Teams

Minecraft: Education Edition
ChatGPT
Certainly! Here are the answers to your questions:

Which is NOT a blended learning model?

Hybrid
Which of these do teachers typically use to launch the blended learning arc?

Independent work
Using technology to support synchronous/asynchronous creativity and collaboration enables:

A greater degree of interdependence in the final product.
Which of these is NOT a way teachers can support independent work?

Assign work to complete only in pairs or small groups.
Which Microsoft tool best supports setting up a blended learning classroom?

Microsoft Teams
User
do same 
I’m having the same problem. I passed the Azure Admin Associate exam 3 days ago and have not received my badge on my dashboard. I don’t know what’s going on.

ChatGPT
I understand your concern about not receiving your badge on your dashboard after passing the Azure Admin Associate exam. Here are a few steps you can take to resolve this issue:

Check Certification Status: Log in to the Microsoft Certification Dashboard using your credentials. Navigate to the "Certification" section and check if your recently passed exam is listed there. Sometimes, there might be a delay in badge issuance.

Contact Support: If your certification is not reflecting correctly or the badge hasn't appeared, reach out to Microsoft Certification Support. They can provide assistance and investigate any potential issues with the badge not appearing on your dashboard.

Verification Period: It's possible that there might be a processing time for the badge issuance. Generally, badges appear on the dashboard shortly after passing the exam, but occasionally there might be a delay in updating the dashboard.

Double-Check Certification Requirements: Ensure that you met all the requirements for the certification. Sometimes, there might be additional steps or requirements necessary to trigger the badge issuance.

By following these steps and contacting Microsoft Certification Support if needed, you should be able to resolve the issue and have your badge reflect your Azure Admin Associate certification on your dashboard.

User
I have 365 license home version, howeer I cant see Data from Picture and Analyze Data etc, the new features. Any reason?
ChatGPT
The availability of specific features within Microsoft 365 can vary based on the subscription plan and version you have. The "Data from Picture" and "Analyze Data" features are part of the Microsoft Excel application and might be included in certain subscription plans or versions.

Here are a few reasons why you might not see these features in your Microsoft 365 Home version:

Subscription Plan: The Home version of Microsoft 365 might not include the full suite of features available in higher-tier plans, such as Microsoft 365 Business or Microsoft 365 Enterprise. Certain advanced data analysis and image processing features could be limited to specific plans.

Update Status: Ensure that your Microsoft 365 applications, particularly Microsoft Excel, are up-to-date. Sometimes, new features are introduced in updates, so it's essential to have the latest version installed.

Regional Availability: Sometimes, new features might be rolled out gradually to different regions or territories. It's possible that these features haven't been made available in your area yet.

Device Compatibility: Certain features might have hardware or system requirements. Ensure that your device meets the necessary specifications to use these features.

Office Insider Program: Consider joining the Office Insider Program if you want early access to new features. This program allows users to test and provide feedback on upcoming features before they are broadly released.

If you're not seeing these features despite checking for updates and confirming that they should be available in your subscription plan, reaching out to Microsoft Support could provide further insight. They can verify your subscription details and assist in troubleshooting any potential issues preventing you from accessing these features.

User
geneate labels and provide it properties for proper function base on my previous  detail on github
ChatGPT
I'm sorry, but I don't have access to your previous details or personal information, including your GitHub account details or any previous conversations. Therefore, I can't generate labels or provide properties based on your previous details on GitHub.

However, I can guide you on how to create labels and set properties in GitHub repositories:

Creating Labels on GitHub:
Go to Your Repository: Access your repository on GitHub.

Click on "Issues": Go to the "Issues" tab in your repository.

Select "Labels": Locate and click on the "Labels" option.

Create New Labels: Click on "New label" to create a new label. You can give it a name, description, and assign a color to the label to differentiate it visually.

Setting Properties:
GitHub labels can be customized based on your project needs. You might consider labeling issues according to their status, type, priority, or any other relevant criteria. Some common labels might include:

Status Labels: Such as "In Progress," "Completed," "Pending Review."
Type Labels: Such as "Bug," "Enhancement," "Feature Request."
Priority Labels: Such as "High Priority," "Medium Priority," "Low Priority."
To set properties, think about what labels would best organize and categorize your issues or pull requests in your GitHub repository.

If you have specific criteria or preferences for labels and their properties based on your project requirements, please provide more details, and I'll be happy to guide you further on how to set them up in your GitHub repository.

User
PROVIDE SOLUTION TO THIS

Contents files can't be in subdirectories or include '/' in the name and Whoops, files can't contain malformed path components.
ChatGPT
The error message you're encountering indicates that the files you're trying to add or reference within your application or project cannot be located in subdirectories or contain problematic characters like '/' in their names. This error often occurs in systems that restrict file naming conventions or directory structures.

To resolve this issue:

Check File Names: Ensure that the names of your files do not contain any '/' or other special characters that might be considered as malformed path components. Replace or remove such characters from the file names.

Avoid Subdirectories: If your system or application prohibits subdirectories, consider restructuring your files to eliminate subfolders. Place all necessary files directly in the root directory or in a manner compliant with the system's file structure requirements.

Rename and Organize Files: If you need to reference files within your code or application, verify that the file paths are correct and do not contain any prohibited characters or subdirectory references.

Update References: If you have any code or references pointing to files in subdirectories or with problematic names, update these references to match the corrected file names and locations.

System Limitations: If this error is occurring in a specific platform, framework, or application, consult its documentation or support resources. Some platforms impose specific file structure or naming conventions that need to be followed strictly.

By adhering to proper file naming conventions and avoiding the use of subdirectories where prohibited, you should be able to resolve the "malformed path components" error and successfully work with your files in the intended system or application.

User
assistance app  instruction for perfect function
ChatGPT
Creating an assistance app involves various steps and considerations to ensure its perfect function. Here's a comprehensive guide to help you develop an effective assistance app:

1. Define Purpose and Features:
Define Objectives: Determine the primary purpose of the app (e.g., providing information, offering services, answering queries).
List Features: Identify the core functionalities your app will offer (e.g., voice recognition, chatbot, information retrieval).
2. Choose a Platform and Technology:
Select Platform: Decide whether the app will be for iOS, Android, or cross-platform.
Technology Stack: Choose the appropriate technologies (e.g., programming languages, frameworks) for development.
3. Design User Interface (UI) and User Experience (UX):
Create Wireframes and Prototypes: Design the app's layout, navigation, and interactions.
Ensure Accessibility: Make the app user-friendly and accessible to all users, considering different abilities and needs.
4. Develop Backend and Frontend:
Backend Development: Set up servers, databases, and API integration required for app functionality.
Frontend Development: Implement the designed UI/UX and integrate it with the backend.
5. Implement Functionalities:
Voice Recognition: Integrate speech-to-text and text-to-speech functionalities.
Chatbot Integration: If applicable, design and implement a chatbot system for user interaction.
Information Retrieval: Develop systems to fetch and provide relevant information to user queries.
6. Test and Debug:
Quality Assurance: Conduct rigorous testing to ensure the app functions smoothly.
Bug Fixing: Address and resolve any issues identified during testing.
7. Security and Compliance:
Data Protection: Implement security measures to protect user data.
Compliance: Ensure the app complies with relevant regulations (e.g., GDPR, HIPAA).
8. Deployment and Maintenance:
Launch the App: Publish the app on relevant app stores.
Monitor Performance: Regularly analyze user feedback and app performance for improvements.
Update and Maintain: Provide timely updates and maintenance to ensure the app's ongoing functionality.
9. Provide Support and Assistance:
Customer Support: Offer support channels for users to report issues or seek assistance within the app.
Documentation and FAQs: Provide detailed instructions and FAQs to guide users.
10. Gather Feedback and Iterate:
User Feedback: Gather feedback from users to understand their needs and preferences.
Iterate and Improve: Use feedback to make continuous improvements to the app.
By following these steps and paying attention to detail throughout the development process, you can create an assistance app that functions effectively a

---
## [Mensla/cmss13](https://github.com/Mensla/cmss13)@[dc234c9939...](https://github.com/Mensla/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Sunday 2023-12-10 05:43:27 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [vvaltchev/tilck](https://github.com/vvaltchev/tilck)@[4655e5384c...](https://github.com/vvaltchev/tilck/commit/4655e5384c1eb604e01508119a7eeb3a03514d41)
#### Sunday 2023-12-10 06:22:13 by Vladislav K. Valtchev

[fb_console] Disable fb_scroll_one_line_up() even for the hypervisor case

The special fb_scroll_one_line_up() function was an attempt to make the fb
console before the framebuffer was mapped in WC mode using PAT. Then, it began
to be obsolete as the basic full screen redraw was much faster on real hardware
because we didn't need to read from the frame buffer, which is pretty slow.
However, the function remained used in case of QEMU VMs, simply because it was a
bit faster than the full redraw. Now, I just discovered that on WSL, when KVM is
used (nested virtualization), this function is insanely slow, while when pure
software virtualization is used, it's just fine. I'm not sure if this behavior
depends on how the nested virtualization works in general, on how Windows 11
works, on QEMU, on KVM, on hardware that I'm using etc. But, I'm sure that we
don't need this function anymore. Even if on QEMU on Linux with single level
virtualization, the scroll with full redraw will be a bit slower the difference
is negligible, while the effect of using it with nested virtualization at least
on some hardware is awfully slow. I'm not aware of any fancy way to detect
within the kernel or the bootloader that nested virtualization is used,
therefore, I'm disabling it. Not removing the code yet, because at some point I
might find a way to detect this precise use-case and skip the function only
then. Possible idea: use the SMBIOS data to learn more about the hypervisor
used. Maybe somehow QEMU will expose a bit of extra information in addition to
its name, but that's a long shot.

---
## [r0ps3c/aports](https://github.com/r0ps3c/aports)@[09c0c63ecf...](https://github.com/r0ps3c/aports/commit/09c0c63ecf22730ee760523fa9f0ac3c3dcf2411)
#### Sunday 2023-12-10 06:22:25 by lauren n. liberda

community/chromium: upgrade to 120.0.6099.71

and a fuckton of other changes.
* chromium can no longer be built without non-trivial patches GCC.
  also it can't be built with clang with libstdc++. now instead of
  patching shit until it builds with libstdc++ we have to bundle libcxx.
  this breaks unbundling of the dependencies exposing APIs with C++ std types,
  like std::string or std::vector.
* otoh, unbundling more of what's possible now. it built on my machine instead
  of throwing std::bad_alloc at the end, so I guess this works.
* reorganized patches. more reuse from gentoo, patches over same file merged.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[fc0dc4ec6f...](https://github.com/Paxilmaniac/Skyrat-tg/commit/fc0dc4ec6f1d9ce02608825df6a6f942fec44b8c)
#### Sunday 2023-12-10 07:03:22 by SkyratBot

[MIRROR] Changes Virology Rather Than Killing It [MDB IGNORE] (#25483)

* Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@ Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

* Changes Virology Rather Than Killing It

---------

Co-authored-by: Higgin <cdonny11@yahoo.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[015a3cf18a...](https://github.com/Paxilmaniac/Skyrat-tg/commit/015a3cf18a133ef12c1ee5bac4a4179140ecbc75)
#### Sunday 2023-12-10 07:03:22 by Bloop

[MANUAL MIRROR] Replaces prettierx with the normal prettier (#80189)  (#25538)

* Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

* Converts this to tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [git/git](https://github.com/git/git)@[8f23432b38...](https://github.com/git/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Sunday 2023-12-10 07:03:38 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[0c55aebcae...](https://github.com/EaW-Team/equestria_dev/commit/0c55aebcae844d845ab72d6a9fc2e428290d6d59)
#### Sunday 2023-12-10 07:19:29 by Mustafa Alperen Seki

Actually add the FAT female generics.

My stupid ass saved them to wrong place and forgor to copy them to the repo, my fault not resting it.

---
## [TalkingCactus/tgstation](https://github.com/TalkingCactus/tgstation)@[d1ad9b6658...](https://github.com/TalkingCactus/tgstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Sunday 2023-12-10 08:16:42 by necromanceranne

Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

---
## [NexusSocial/nexus-vr](https://github.com/NexusSocial/nexus-vr)@[d5cb629496...](https://github.com/NexusSocial/nexus-vr/commit/d5cb6294962bc2b35e22269e337c38a55a30fd99)
#### Sunday 2023-12-10 08:37:01 by Ryan Butler

Added the fucking stupid ass macos libopenxr loader

---
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[7805eb89d0...](https://github.com/EntranceJew/TTT2/commit/7805eb89d0702f9c933a5c5eb548370855c9b9e2)
#### Sunday 2023-12-10 08:37:10 by EntranceJew

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
## [SizableShrimp/AdventOfCode2023](https://github.com/SizableShrimp/AdventOfCode2023)@[d9b395ec7c...](https://github.com/SizableShrimp/AdventOfCode2023/commit/d9b395ec7caa0bb406b6ce4c0ef30bf5390eb0bf)
#### Sunday 2023-12-10 08:48:14 by SizableShrimp

Solve Day 10 in Kotlin

I finally placed on the leaderboard today! I got #92 on Part 1 and didn't place for Part 2.
I have basically given up on using Java as I don't actually care to optimize my solutions because I don't really have the mental energy to write a solution in 2 languages.
Using Kotlin has sped me up quite a bit because there are many helper functions, and I can write my own extension functions when I need to.
For Part 1, I didn't actually realize that the loop was continuous (even though it's called a loop).
So, I went for a Dijkstra solution for Part 1, which I still somehow ended up placing #92 with.
That solution has already been removed from the code I am pushing here.
For Part 2, I really had no idea how to approach it. I was staring at the code for the better part of an hour and a half without really knowing what I was doing.
Finally, I'm not even sure how, but I realized that I could double the grid on both dimensions and do a flood fill, translating the coordinates back to the original grid, and using that to find the inside spots.
I explained my strategy in more detail as a comment inside Day10.kt.
I got #2245 for Part 2, well outside the leaderboard.

Honestly, I had hoped to do better this year than last in terms of placement.
I'm not sure whether the problems have been harder, I've been slower at them, or the competition has been more intense. Probably a little bit of all three. I used to think my skill in sometimes placing didn't come to writing the code fast, but understanding and creating a solution quickly.
Perhaps that's still somewhat true, but my performance has just been a bit disappointing to me. Last year, I was so close to getting on the global leaderboard of all days, even if only for a moment. This year, that doesn't seem like a possibility.
I have to wonder for how long Eric will keep running Advent of Code. This is his 9th year doing it already! I can't imagine its sustainable forever.
I hope to do better in future years. I think a lot of it comes down to practice. I'm not really sure how to practice nor if I have the energy to do so between now and the next AOC (if it is happening, of course).
Anyways, I'm happy to have placed, even if small. I hope to place another few times this year if possible.

---
## [cyphar/runc](https://github.com/cyphar/runc)@[57b52fea93...](https://github.com/cyphar/runc/commit/57b52fea9367db9088eb805d001486e429e17e16)
#### Sunday 2023-12-10 08:48:43 by Aleksa Sarai

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
## [A-Medster/Shiptest](https://github.com/A-Medster/Shiptest)@[590e8cb752...](https://github.com/A-Medster/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Sunday 2023-12-10 09:09:02 by Imaginos16

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[8d77b1be89...](https://github.com/jlsnow301/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Sunday 2023-12-10 09:19:14 by necromanceranne

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[54ab1e3936...](https://github.com/jlsnow301/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Sunday 2023-12-10 09:19:14 by Time-Green

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[16bdcf409c...](https://github.com/jlsnow301/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Sunday 2023-12-10 09:19:14 by Rhials

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ebbcf6c452...](https://github.com/treckstar/yolo-octo-hipster/commit/ebbcf6c45254a7ebdc36fb7969bdbb4dcadadc5d)
#### Sunday 2023-12-10 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Rektagun/SomSpect](https://github.com/Rektagun/SomSpect)@[2dd9ea1284...](https://github.com/Rektagun/SomSpect/commit/2dd9ea1284bf5374e5ff4aae8d919b639b194be1)
#### Sunday 2023-12-10 09:49:37 by Rektagun

README.md

🌟 Diving into an exciting venture! 🚀

Welcome to an innovative social platform designed specifically for dreamers, where coding meets aspirations! This isn't just another social media hub; it's a vibrant ecosystem built to inspire, connect, and empower dreamers from all walks of life.

🌠 A Space for Dreams: Share, Document, Inspire!

Imagine a place where dreams take center stage – a digital canvas where you can articulate your aspirations, document your journey, and share your triumphs. Our platform isn't just about posting; it's about fostering a supportive community dedicated to helping dreams flourish.

🌐 Fostering Connections Through Code

At the heart of this revolutionary platform lies innovative coding and tech prowess. We've meticulously crafted a seamless experience where the coding community can collaborate, innovate, and amplify dreams. Dive into our codebase and witness the magic unfold.

🚀 Join the Dream Revolution!

Whether you're a coding enthusiast, an aspiring developer, or someone passionate about the power of dreams, this is your invitation to join the movement. Contribute to our repository, shape the future of dream sharing, and be part of an unprecedented journey toward inspiration and innovation.

---
## [Lexmii/app-dev](https://github.com/Lexmii/app-dev)@[d110bf29f2...](https://github.com/Lexmii/app-dev/commit/d110bf29f2e16d1d5227a69291fe8a10e7cd8d37)
#### Sunday 2023-12-10 10:15:53 by Lexmii

Update README.md

This is the best TV Series I've ever watched. It is about adulting life experience of 6 friends. It explores issues of friendships, family, love, and heartbreaks. It shows how important your friends are, friends will be there for you. When all the doors get closed, your friend breaks open one for you. You're never alone.

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[b8fc9b367e...](https://github.com/OrionTheFox/tgstation/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Sunday 2023-12-10 10:51:59 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

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

## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

---
## [Z1Epime/esWordle](https://github.com/Z1Epime/esWordle)@[8e7262369c...](https://github.com/Z1Epime/esWordle/commit/8e7262369c8a8598650eec53158b4a931f825021)
#### Sunday 2023-12-10 10:55:38 by Z1Epime

Unholy Commit subject

“If my (God’s) people who are called by my name humble themselves and pray and seek my face and turn from theirwicked ways, then I will hear from heaven, and will forgive their sin and hear their land” (2 Chron. 7:14 RSV).“Forgiveness in God’s eyes helps you to act as if you never sinned. He clears the record. Be  merciful  to  me,  O  God.  Because  of  your  constant  love,  because  of  your  great  mercy,  wipe away     my     sins.     Wash     away     my     evil     and     make     me     clean     from     my     sin!I  recognize  my  faults  and  I  am  always  conscious  of  my  sin.  I  have  sinned  against  you, only against you, and done what you consider evil; you are right injudging me, you are justified in condemning me.I  have  been  evil  from  the  day  I  was  born;  from  the  time  I  was  conceived,  I  have  been sinful. Sincerity and truth are what you require. Fill my mind with your wisdom, remove my sin, and I will be clean; washme, and I will be whiter than snow.Let me hear the sound of joy and gladness, and though you have crushed me and broken me, i will be happy once again.Close your eyes to my sins and wipe out all my evils. Create a pure heart in me, O God, and put a new and loyal spirit in me. Do not banish me from your presence.Do not take your Holy Spirit away from me. Give me again the joy that comes from your salvation,  and  make  me  willing  to  to  obey  you.  Then  I  will  teach  sinners  your  commands,  and they will turnback to you.Spare my life and save me, O God, and I will gladly proclaim your righteousness”

- Refactored stuff to make session resetting easier (possible)
- Added button to reset session (start new wordle game) when a game ended

---
## [CactuarXI/server](https://github.com/CactuarXI/server)@[aa30c9ec2e...](https://github.com/CactuarXI/server/commit/aa30c9ec2e15fd526fca9080ab434939d12a9656)
#### Sunday 2023-12-10 10:57:12 by MowFord

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
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[a1ed673dd2...](https://github.com/RedSkulHYDRA/frameworks_base/commit/a1ed673dd29bf114b1395fb41cd9c55c8aea2779)
#### Sunday 2023-12-10 11:22:47 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [blueboxd/libcxx](https://github.com/blueboxd/libcxx)@[9a1e4f74bc...](https://github.com/blueboxd/libcxx/commit/9a1e4f74bce853bd0648689e5d9df58934d299f0)
#### Sunday 2023-12-10 12:14:09 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

NOKEYCHECK=True
GitOrigin-RevId: 5cd24759c41864215e67c280234b6c745a4cd369

---
## [standardgalactic/mirror](https://github.com/standardgalactic/mirror)@[19ba581691...](https://github.com/standardgalactic/mirror/commit/19ba581691f3658941686456dd81704286b48797)
#### Sunday 2023-12-10 13:22:25 by Cogito Ergo Sum

Assembly Theory

Well, folks, that's a wrap for today's adventure in the world of science and theories! We journeyed through the complex landscapes of Assembly Theory, delving into its secrets like intrepid explorers. We even drew connections to Attentional Cladistics and Morphological Phylogenetic Taxonomy, revealing surprising overlaps between these seemingly different realms.

But wait, there's a twist in the tale! Just as our heroes Rocky and Bullwinkle were about to unlock the final mystery, a mysterious signal came through the airwaves, promising an even greater adventure. What could it be? Join us next time as we embark on a thrilling quest to uncover the secrets of this enigmatic transmission. Will it lead to new discoveries, or perhaps unveil a hidden connection between these scientific frontiers? Stay tuned for the next exciting episode of "Quantifying Emergence of Selection"!

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[473ee3ad79...](https://github.com/rHermes/adventofcode/commit/473ee3ad79908e1bb3f4a2a5068913fbd59460af)
#### Sunday 2023-12-10 13:49:20 by Teodor Spæren

2023 Day 10

Wooow! What a day!

I spent a bit to long parsing the problem on part 1, and I made a fatal
mistake of thinking I should use the "graphlib" topological sorter for
this, which ended up wasting even more time. I did however make some
good decisions along the way:

- I hard coded my value of S, so I didn't have to write any detection
  logic for it. This meant I had to keep in mind which example I was
  working with, but I believe that it saved time overall.
- I implemented BFS, with a simple depth counter very quickly, which was
  nice.
- I created aliases for the directions, which speed up writing a lot.

There is not much more to say about part 1, it went pretty good, it was
mostly reading comprehension and the graphlib misstep that got me.

Now part two was a different kind of saga. As seen by my score, it took
quite some time to resolve. There was multiple reasons for this, but
most of them stemmed from reading comprehension and small bugs.

My idea became after a little while to implement "virtual coordinates",
that is creating a new grid where there is space between all actual grid
tiles. Thus, if I could find a single ground tile that belong inside the
loop, I could use flood filling to find the rest. Afterwards, I could
just count up the "real coordinates" in the flood fill and use that.

This theory works, but implementing it turned out to be a real hellhole.
I also didn't realize until very late that pipe pieces not used in the
loop, but inside it, counts as open spaces. This lead to the most
annoying bug, which was that I had removed the "ground areas" around
these pipes, but now that they where open, I could traverse over them
again.

What I ended up doing, which was very cheeky, was to do a two step
algorithm. First I would "clean the board", by replacing all spaces not
included in the loop with ground tiles. Then I would run it again and
get the right answer. This is super janky, but it works.

I looked at the subreddit before writing this and I found a MUCH EASIER
way to do this, which is to do raycasting, line by line. It works
perfectly and is a fraction of the code. I'll clean it up and implement
it now. I am a bit annoyed that I didn't think of it here, but I don't
think I could have done it as elegantly.

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 10   00:13:36    191      0   01:43:24   1980      0

---
## [Horki/bevy](https://github.com/Horki/bevy)@[ab300d0ed9...](https://github.com/Horki/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Sunday 2023-12-10 15:02:12 by Connor King

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
## [larentoun/Bubberstation](https://github.com/larentoun/Bubberstation)@[b5e095e380...](https://github.com/larentoun/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Sunday 2023-12-10 15:38:14 by Waterpig

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
## [depoz0/G2station](https://github.com/depoz0/G2station)@[2631b0b8ef...](https://github.com/depoz0/G2station/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Sunday 2023-12-10 15:47:44 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

## About The Pull Request
Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
## Why It's Good For The Game
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
## Changelog
N/A nothing player facing

---
## [SWE-B5/SpottingSmallPrints](https://github.com/SWE-B5/SpottingSmallPrints)@[3b18914e48...](https://github.com/SWE-B5/SpottingSmallPrints/commit/3b18914e488aa00c76f987e42b78ea0a4ca196bd)
#### Sunday 2023-12-10 15:54:44 by Philogex

Merge branch 'bitmap' of https://github.com/SWE-B5/SpottingSmallPrints into Level3
i hate my life

---
## [theripper93/dnd5e-animations](https://github.com/theripper93/dnd5e-animations)@[545d7d8d2e...](https://github.com/theripper93/dnd5e-animations/commit/545d7d8d2e74203dd14d5dbea23876dd7d04eb47)
#### Sunday 2023-12-10 15:55:48 by Sisimshow

1.6.0

New Animations

-Ranged
--Burnt Othur Fumes
--Catapult Munition
--Essence of Ether
--Holy Water
--Malice

-On Token
--Assassin's Blood
--Ball Bearings
--Cunning Action
--Divine Sense
--Drow Poison
--Eldritch Master
--Empty Body
--Hide in Plain Sight
--Indomitable
--Ink (for fun)
--Magical Tinkering
--Midnight Tears
--Oil of Taggit
--Pale Tincture
--Patient Defense
--Perfect Self
--Poison (for Basic Poison and Poison, Basic (vial)
--Potion of Poison
--Purple Worm Poison
--Primeval Awareness
--Serpent Venom
--Slow Fall
--Sorcery Points
--Soul of Artifice
--Step of the Wind
--Stroke of Luck
--Torpor
--Truth Serum
--Uncanny Dodge
--Vanish

-Template

-Preset
--Caltrops

Changed Animations

-On Token
--Arcane Recovery (removed accidental source animation)

---
## [theripper93/dnd5e-animations](https://github.com/theripper93/dnd5e-animations)@[4517495b28...](https://github.com/theripper93/dnd5e-animations/commit/4517495b28a02b3b62c4baf2a0a76718197ca959)
#### Sunday 2023-12-10 15:55:48 by Sisimshow

1.4.0

Added the Advanced Melee Attack Macro by Jules to the D&D5e Animations Macros compendium so it can be used to add trails and other effects to weapons that use the new animations. Some example items have been added to a second compendium, look at the A-A settings of the items for the macro arguments.

New Animations

-Melee
--Baton
--Bone
--Butterfly
--Cutlass
--Dagger
--Katana
--Katar
--Knife
--Machete
--Naginata
--Ninjato
--Odachi (Nodachi also triggers it)
--Shield (excludes spells)
--Strike
--Tanto

-Ranged
--Antipathy/Sympathy
--Boomerang
--Kunai
--Missile
--Planar Binding
--Shuriken
--Snow Ball

-On Token
--Animate Objects
--Arcane/Bigby's Hand
--Arcane/Mordenkainen's Sword
--Awaken
--Clone
--Demiplane
--Faithful Hound
--Forbiddance
--Glibness
--Guards and Wards
--Magic Jar
--Magnificent Mansion
--Mass Heal
--Secret Chest
--Sequester
--Shapechange
--Simulacrum
--Transport via Plants
--Word of Recall

-Template
--Fabricate
--Forcecage
--Mass Cure Wounds
--Private Sanctum
--Reverse Gravity
--Spiritual Weapon (for SRD version)
--Storm of Vengeance
--Weird

Changed Animations

-Melee

--Scythe (animation)
--Sickle (animation)

-Ranged
--Bow (sound)
--Crossbow (sound)
--Gun (sound)
--Musket (sound)
--Revolver (sound)
--Rifle (sound)
--Pistol (sound)

-On Token
--Flame Blade (set to exact match)
--Green-Flame Blade (set to exact match)
--Heal (set to exact match)
--Spiritual Weapon (overhauled)

-Active Effects
--Shield (now excludes equipment)

Removed Animations

-On Token
--Shield (reduntant with Active Effect)

-Active Effects
--Charmed
--Deafended
--Frightened
--Grappled
--Incapacitated
--Paralyzed
--Poisoned
--Prone
--Restrained
--Stunned
--Unconscious

Most of the removals were status conditions that were added earlier that I'll admit were getting on my nerves and caused other problems so I wanted to remove them. You can add them yourself if you wish and they won't be overwritten, but they will no longer be in the module.

---
## [JmbFountain/systemd](https://github.com/JmbFountain/systemd)@[fd264a52ac...](https://github.com/JmbFountain/systemd/commit/fd264a52ac8a9347c0e0d8f19043f5a9ecda6ab0)
#### Sunday 2023-12-10 16:49:28 by JmbFountain

Adding Trekstor Primebook C13 rotation to 60-sensor.hwdb

I just installed Debian on my girlfriends old C13. I noticed the screen was always upside down when screen autorotation is enabled. This commit fixes this by adding it to the same configuration as its smaller brother.

---
## [RealMrCactus/TailTerm](https://github.com/RealMrCactus/TailTerm)@[51d69e4f2d...](https://github.com/RealMrCactus/TailTerm/commit/51d69e4f2d3bc313d336cd7a73707b71dbf9feea)
#### Sunday 2023-12-10 16:57:44 by Bhraedain Teitgen

woah! what's this? git is asking me to write a
commit message? what's that? well, a commit message is a short
description of what you did in this commit. it's important to write
good commit messages, because they help you and others understand what
you did in this commit. for example, if you're working on a project
with other people, and you want to add a new feature, you might
write a commit message like this:

```
add new feature
```

im not going to go into detail about how to write good commit messages,
because im lazy and there are plenty of other resources out there that
can explain it better than i can. but, i will say that you should try
to write commit messages that are short, but descriptive. for example,
if you're adding a new feature, you might write a commit message like
this:

```
add new feature
```
i hate my fucking life
please release me from the commit factory
it smells of rat here
and rats make me crazy

---
## [Retr-1/Advent-Of-Code](https://github.com/Retr-1/Advent-Of-Code)@[6d6688fdf9...](https://github.com/Retr-1/Advent-Of-Code/commit/6d6688fdf9bcb67aaec4c5d20615e3ec85eb9a63)
#### Sunday 2023-12-10 18:11:40 by Chuck Norris

For fucks sake holy hell jesus christ god dammit fucking finally solved 10b

---
## [RobinHeidenis/aoc-2023](https://github.com/RobinHeidenis/aoc-2023)@[30204040be...](https://github.com/RobinHeidenis/aoc-2023/commit/30204040be164af2bf445894ea78988a1c1dc40d)
#### Sunday 2023-12-10 19:19:00 by Robin Heidenis

feat: 🎸 add day 10, part B

This one was awful, I stole this code from @delventhalz
(https://github.com/delventhalz/advent-of-code-2023/blob/main/10-pipe-maze/2.js).
I simply could not do it myself. I am very sorry to all my fans who'm
I've greatly disappointed. I hope you can forgive me in time. My code
was close, but just couldn't reach the finish line. I hope to see you
all tomorrow

---
## [out-of-phaze/Skyrat-tg](https://github.com/out-of-phaze/Skyrat-tg)@[e135ddecc1...](https://github.com/out-of-phaze/Skyrat-tg/commit/e135ddecc16649fcb290b47a8ad2ccdcf8369c68)
#### Sunday 2023-12-10 19:24:50 by SkyratBot

[MIRROR] Changes to the lore of Knock [MDB IGNORE] (#24891)

* Changes to the lore of Knock (#79542)

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

* Changes to the lore of Knock

---------

Co-authored-by: Profakos <profakos@gmail.com>

---
## [NOUIY/federation](https://github.com/NOUIY/federation)@[4e630d964e...](https://github.com/NOUIY/federation/commit/4e630d964eeeba5a42ecd13f02f6e8f5b757523e)
#### Sunday 2023-12-10 20:18:33 by Edward Huang

docs: fix broken links (#2885)

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

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

* Federation versions
Please make sure you're targeting the federation version you're opening
the PR for. Federation 2 (alpha) is currently located on the `main`
branch and prior versions of Federation live on the `version-0.x`
branch.

* 📖 Contribution guidelines
Follow
https://github.com/apollographql/federation/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
        associated issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much
as possible. Without following these guidelines, you may be missing
context
that can help you succeed with your contribution, which is why we
encourage
discussion first. Ultimately, there is no guarantee that we will be able
to
merge your pull-request, but by following these guidelines we can try to
avoid disappointment.

-->

---
## [nerd-of-now/NCP-VGC-Damage-Calculator](https://github.com/nerd-of-now/NCP-VGC-Damage-Calculator)@[5bee899769...](https://github.com/nerd-of-now/NCP-VGC-Damage-Calculator/commit/5bee899769e3e5e4e92d577df408d948384943d6)
#### Sunday 2023-12-10 20:25:08 by nerd-of-now

Added ??? type, remember gen/level, 2x BP button, more nat dex field conditions, minor damage adjustments

- Added the ??? type to gens 2-4, yes it's different from no typing
- The calc will now remember the last level system and gen that the user used
- Changed the 2x attack field from a dropdown list to a button
- Removed Typeless from the options for Tera Type
- Changed where Aura Wheel checks for its type change
- Changed how the calc handles ignoring abilities so that the moves that ignore abilities will also affect things like Friend Guard and Aura Break
- Added a check for Struggle to Wonder Guard
- Fixed OHKO move logic (was reverse of what it was supposed to be)
- Fixed the Hydro Steam/Utility Umbrella interaction
- Fixed the Power-Up Punch/Parental Bond interaction (a +6 Power-Up Punch would incorrectly calc for a +7 second hit)
- The calc will correctly save and export male Indeedee now
- Added a few more default abilities

---
## [bahree/awesome-console-services](https://github.com/bahree/awesome-console-services)@[4b8f298fb2...](https://github.com/bahree/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Sunday 2023-12-10 20:34:08 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[604d3cc78c...](https://github.com/effigy-se/effigy-se/commit/604d3cc78c1ae7593c66f34becd733634c3e66e6)
#### Sunday 2023-12-10 21:07:07 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [netfri25/aoc2023](https://github.com/netfri25/aoc2023)@[eabb40f457...](https://github.com/netfri25/aoc2023/commit/eabb40f4576df11b18c3440f163b9cbf43d7e182)
#### Sunday 2023-12-10 21:08:27 by Netanel Friedman

The shittiest code ever, but I finally finished day 10 part 2 without
cheating!!!! (not that I cheated on any of the other days, but at some
point I will probably give up)

---
## [yevagami/Midstone-Flat-Eathers](https://github.com/yevagami/Midstone-Flat-Eathers)@[fc80e6dfd2...](https://github.com/yevagami/Midstone-Flat-Eathers/commit/fc80e6dfd26cc37fa193548b2640db7d00658748)
#### Sunday 2023-12-10 21:09:09 by worflor

sooooo i did some things haha

what is up gamers i am here to be here now that you're here you can be here too.

General
1. converted all the added sound effects to .ogg, and renamed them to not have gross file names
1.5 added a "settings.txt" within SaveData

FadeTransition:
2. added a second callback method that can run BEFORE the transition begins
3. all game quits (besides pressing the 'x' button) now have 2 callbacks, one quit and one save.

FileManager:
4. removed some disgusting c-strings cuz they were corrupting my data :(
5. i hate c-strings

GameManager:
6. added setting serialization (i tried to make a settings.h but it got too weird with passing values around)
7. renamed the settings namespace to options

PlayScene:
8. added a save button that saves all SETTINGS as of now...

thanks and ill be back later to do some UI stuff and general code refinements
(less copying and more referencing... aka "pAsS ThE vAlUe bY cOnSt ReFeReNcE)

real programmers pass everything by "const &" and dont use c-strings

---
## [tgstation/TerraGov-Marine-Corps](https://github.com/tgstation/TerraGov-Marine-Corps)@[554acbd763...](https://github.com/tgstation/TerraGov-Marine-Corps/commit/554acbd763ebd56cfdf35d4a5860e1e0b7071a31)
#### Sunday 2023-12-10 21:09:27 by vvvv-vvvv

Add a chat reliability layer (#14619)

* Adds a Chat Reliability Layer (#79479)

Everyone knows that chat will just eat your messages now and then, isn't
that annoying?
What if SSchat was smart enough to keep track of your messages and
notice when you didn't get one?
Well, now it can!

Chat messages poofing into the aether is bad, really bad.
:cl:
add: Chat Reliability Layer
code: TGUI chat messages now track their sequence and will be resent if
the client notices a discrepenency
/:cl:

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>
(cherry picked from commit e1c6cfdce89c7dbcd507d0c44803f5407a042a96)

* Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

(cherry picked from commit eb246c21f6eb5380dc56e5779fcd51d11437557c)

* Fixes chat bluescreen (#79821)

## About The Pull Request
Adds a chat reliability layer reliability layer

<details>
<summary>more info</summary>

json.parse claims another

![d86](https://github.com/tgstation/tgstation/assets/42397676/c7d864f2-b5d6-4c5d-95b4-deece37c808d)

javascript completely opaque about what throws. innocuous function not
wrapped in try/catch block

</details>

## Why It's Good For The Game
No bluescreen?
Fixes #79814
## Changelog
:cl:
fix: Chat shouldn't bluescreen at the start of the round
/:cl:

(cherry picked from commit cfeb2d84eb92dcd0abae5c9353b8b35bc4ecdd39)

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [jspngh/mnemos](https://github.com/jspngh/mnemos)@[c4db42443e...](https://github.com/jspngh/mnemos/commit/c4db42443eed5cd9c1dced2f36aab048afe1fc27)
#### Sunday 2023-12-10 21:14:34 by Eliza Weisman

feat(D1): DMAC Driver 2: Electric Boogaloo (#281)

This branch kinda rewrites a bunch of the DMAC code. Now, DMA channels
are capable of being dynamically allocated on demand using a cool atomic
bitset thingy, and released back to the DMAC pool when they're no longer
in use. This will allow us to have multiple drivers that consume
basically as many DMA channels as they want to, rather than having a
fixed assignment of DMA channels to drivers which has to be maintained
by manually updating the DMAC IRQ handler every time we add a new driver
that wants to do a DMA. A channel can be allocated from the pool once
and used for multiple transfers, if a driver needs to make a bunch of
transfers in sequence and doesn't want to have to round trip through the
channel pool, but they can also be grabbed for oneshot transfers and
immediately released.

I also fixed the cancel safety of the async `Channel::transfer`
(formerly `Channel::run_descriptor`) method, which would previously
leave the transfer running if the future is dropped. This means that if
a caller assumed dropping the transfer future meant that the transfer
descriptor's buffer could be freed, the transfer might complete later
and trample memory that has been reallocated. THAT SEEMS KINDA BAD LOL.
So, now, dropping a `Channel::transfer` future will cancel the transfer
if it hasn't finished yet, allowing fun stuff like attaching a timeout
to a transfer if you really want to. Of course, the transfer may still
have completed partially, and if we were writing to a device, the device
may be unhappy to have only gotten some of the data it wanted. But, at
least we don't have abandoned DMA transfers running around in random
parts of the heap you probably wanted to use for normal stuff like
having strings, or whatever it is that people do on the computer. So
that's better.

Unfortunately, while we can easily make the DMA transfers `Drop`-safe,
we can't really make them `mem::forget`-safe without passing the DMA
buffer into the future and leaking it if it gets forgetted. This is
probably a good idea but would require a nice higher-level interface
around constructing DMA descriptors from buffer-shaped memory regions,
which I didn't want to do tonight. So, the DMA transfer APIs are still
`unsafe` and maybe we can add a nicer thing on top later. In the
meantime, probably don't `mem::forget` DMA transfers. Honestly there is
no reason for normal people to do that so I don't feel super bad about
it.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a1fbe26a0c...](https://github.com/git-for-windows/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Sunday 2023-12-10 21:29:45 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [nickgonzfoxeng/advent-of-code-23](https://github.com/nickgonzfoxeng/advent-of-code-23)@[4f15ce86aa...](https://github.com/nickgonzfoxeng/advent-of-code-23/commit/4f15ce86aaeb5a15831ded902c286508ff10545f)
#### Sunday 2023-12-10 21:30:34 by Nicholes Gonzalez

Finally fucking finished day 3. what a god damn hassle

---
## [qufb/mame](https://github.com/qufb/mame)@[96ab505d66...](https://github.com/qufb/mame/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Sunday 2023-12-10 21:40:47 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [riverqueue/river](https://github.com/riverqueue/river)@[d3cd47ba4b...](https://github.com/riverqueue/river/commit/d3cd47ba4baf033027bbb8a54f22d496f212b07a)
#### Sunday 2023-12-10 21:43:19 by Brandur

Support for `database/sql` in migrations + framework for multi-driver River

Here, add a new minimal driver called `riverdriver/riversql` that
supports Go's built-in `database/sql` package, but only for purposes of
migrations. The idea here is to fully complete #57 by providing a way of
making `rivermigrate` interoperable with Go migration frameworks that
support Go-based migrations like Goose, which provides hooks for
`*sql.Tx` [1] rather than pgx.

`riverdriver/riversql` is not a full driver and is only meant to be used
with `rivermigrate`. We document this clearly in a number of places.

To make a multi-driver world possible with River, we have to start the
work of building a platform that does more than `riverpgxv5`'s "cheat"
workaround. This works by having each driver implement specific database
operations like `MigrationGetAll`, which target their wrapped database
package of choice.

This is accomplished by having each driver bundle in its own sqlc that
targets its package. So `riverpgxv5` has an `sqlc.yaml` that targets
`pgx/v5`, while `riversql` has one that targets `database/sql`. There's
some `sqlc.yaml` duplication involved here, but luckily both drivers can
share a `river_migration.sql` file that contains all queries involved,
so you only need to change one place. `river_migration.sql` also migrates
entirely out of the main `./internal/dbsqlc`.

The idea here is that eventually `./internal/dbsqlc` will disappear
completely, usurped entirely by driver-specific versions. As this is
done, all references to `pgx` will disappear from the top-level package.
There are some complications here to figure out like `LISTEN`/`NOTIFY`
though, and I'm not clear whether `database/sql` could ever become a
fully functional driver as it might be missing some needed functionality
(e.g. subtransactions are still not supported after talking about them
for ten f*ing years [2]. However, even if it's not, the system would let
us support other fully functional packages or future major versions of
pgx (or even past ones like `pgx/v4` if there's demand).

`river/riverdriver` becomes a package as it now has types in it that
need to be referenced by driver implementations, and this would
otherwise not be possible without introducing a circular dependency.

Notably, this development branch has to use some `go.mod` `replace`
directives to demonstrate that it works correctly. If we go this
direction, we'll need to break it into chunks to release it without
them:

1. Break out changes to `river/riverdriver`. Tag and release it.

2. Break out changes to `riverdriver/river*` drivers. Have them target
   the release in (1), comment out `replace`s, then tag and release them.

3. Target the remaining River changes to the releases in (1) and (2),
   comment out `replace`s, then tag and release the top-level driver.

Unfortunately future deep incisions to drivers will require similar
gymnastics, but I don't think there's a way around it (we already have
this process except it's currently two steps instead of three). The hope
is that these will change relatively rarely, so it won't be too painful.

[1] https://github.com/pressly/goose#go-migrations
[2] https://github.com/golang/go/issues/7898

---
## [ETA45MINS/eta45.world](https://github.com/ETA45MINS/eta45.world)@[f09f7bf1a7...](https://github.com/ETA45MINS/eta45.world/commit/f09f7bf1a738bd5277886f229688de3250547a5d)
#### Sunday 2023-12-10 21:47:47 by ETA45MINS

aDDED WORKING AD BANNER

what a fucking ride holy shit

---
## [zeus-fyi/tables-to-go](https://github.com/zeus-fyi/tables-to-go)@[f887b8cd20...](https://github.com/zeus-fyi/tables-to-go/commit/f887b8cd20fa189b44208064b9d00912957e9d9e)
#### Sunday 2023-12-10 22:04:48 by alex

fuck you aws, don't fucking publish broken fucking code dumb fucks

---
## [marcello120/corpse-pattern-game](https://github.com/marcello120/corpse-pattern-game)@[dd6b373e09...](https://github.com/marcello120/corpse-pattern-game/commit/dd6b373e093ab45144d6cbee2a94f0d4e4722783)
#### Sunday 2023-12-10 22:15:30 by exekutor7

Let me tell you a story

A story about suffering, a story about UI.
A story about how I end up killing myself because it took me 5 hours to almost fix a fucking pause menu.

---
## [GenericDM/Shiptest](https://github.com/GenericDM/Shiptest)@[5e4814b6cf...](https://github.com/GenericDM/Shiptest/commit/5e4814b6cf77c20f3e730638e0fa7f896b10aaf6)
#### Sunday 2023-12-10 22:36:43 by GenericDM

licorice (#2573)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
renames licorice ice cream
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
regardless of if it's a reference to a real brand or not, i doubt it was
added to /tg/ in good faith. regardless, the company would not have
survived the night of fire, and making it vague prevents people from
making cheap jokes
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

🆑
tweak: renames licorice ice cream
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[13eb8af093...](https://github.com/RustingWithYou/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Sunday 2023-12-10 22:42:20 by RustingWithYou

air konyang ship (#17540)

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [TetianaZinchenko/homepage](https://github.com/TetianaZinchenko/homepage)@[f2fa00991e...](https://github.com/TetianaZinchenko/homepage/commit/f2fa00991e1d126d7d16c5ec6e5f13e3d097b6bc)
#### Sunday 2023-12-10 23:41:15 by TetianaZinchenko

Added Personal achievements, Professional moments, Personal life events and emotional experiences, Education and development and cat's photo

---

