## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-25](docs/good-messages/2023/2023-11-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,326,770 were push events containing 3,095,605 commit messages that amount to 170,424,144 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [VEIN777K/app-dev](https://github.com/VEIN777K/app-dev)@[980a2c240a...](https://github.com/VEIN777K/app-dev/commit/980a2c240a38779411a367909c4849a9ee1a8e62)
#### Saturday 2023-11-25 00:18:25 by VEIN777K

Update README.md

Denji is a destitute young man who lives in a world filled with bloodthirsty monsters called Devils. One day, he befriends Pochita, who is a Devil dog-thing that is also a literal chainsaw. If that wasn't already a weird, things take a real turn when Denji is murdered by gangsters, and Pochita fuses with his soul to save his life. This turns the perpetually hungry and horny Denji into the titular Chainsaw Man, who ends up hunting other Devils for the enigmatic Makima, a woman who works for a governmental bureau of Devil Hunters, and strings Denji along with vague promises of sex and fortune, even as she treats him as little more than a dog himself.

---
## [SB1918/f13babylonnewshit](https://github.com/SB1918/f13babylonnewshit)@[830db814f3...](https://github.com/SB1918/f13babylonnewshit/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Saturday 2023-11-25 00:24:25 by GreytidePanda

Expanded Mall (#171)

## About The Pull Request
The northwest mall was an area scraped together from an older mall
building and expanded on by me well over a year ago, but it was always
unfinished as I left Sunset before I submitted the final version. You
can really tell this if you look at some of the suspiciously empty rooms
on the upper levels.

The finished version has been sitting on my harddrive for a long time so
I've copied it in and made a few changes to fit the server. I'm not sure
if the mall is staying with future map changes, but at least for now I
want to be judged on my completed work.

- References to 'Mall of Wyoming' are now 'Mall of Utah'
- A lot of rooms are now less claustrophobic and use their space better
- More loot and detail (no crazy loot - it was always intended as a
fairly beginner friendly zone)
- Now far more vertical - an underground parking lot, and accessible
roof
- Removed the 'requires_power' flag from the mall area tag - no other
ruin uses it
- Fixed the instrument shop shutter not working (I can't believe this
bug has existed for over a year)

## Why It's Good For The Game
Better locations are always good for the game!

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog
:cl:
add: The Mall of Utah now offers an even bigger shopping experience.
/:cl:

---
## [jordanpg/Tabletop-Simulator-Scripts](https://github.com/jordanpg/Tabletop-Simulator-Scripts)@[be30ef342e...](https://github.com/jordanpg/Tabletop-Simulator-Scripts/commit/be30ef342ea3577b9e0fa0adb4a476ec9b2f839e)
#### Saturday 2023-11-25 00:28:47 by rubic

Update Importer.lua

- Fixed card languages breaking importing anything that isn't English
- Fixed importing multiple of the same card with different prints
- Added a lot of spaces. Fuck you
- Dirt

---
## [GDNgit/Paradise-GDNgit](https://github.com/GDNgit/Paradise-GDNgit)@[6a109ade7f...](https://github.com/GDNgit/Paradise-GDNgit/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Saturday 2023-11-25 00:37:02 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [zecarlos1957/reactos](https://github.com/zecarlos1957/reactos)@[cc63d8f4a2...](https://github.com/zecarlos1957/reactos/commit/cc63d8f4a2c3e4e22dd3f4c706e2373978914b68)
#### Saturday 2023-11-25 00:38:37 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[81a7c75583...](https://github.com/timothymtorres/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Saturday 2023-11-25 00:43:37 by necromanceranne

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d23f6dfbeb...](https://github.com/treckstar/yolo-octo-hipster/commit/d23f6dfbebc737c1ce12e3f2687711d3bf61c397)
#### Saturday 2023-11-25 01:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[1a2ddececa...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/1a2ddececa5cbc3b3aed161765eab4ebdda105c7)
#### Saturday 2023-11-25 02:01:02 by SkyratBot

[MIRROR] new space ruin, the biological research outpost [MDB IGNORE] (#24662)

* new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles

https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566

https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past

https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range

https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that

https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae

## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* new space ruin, the biological research outpost

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [Sinbest/mojave-sun-13](https://github.com/Sinbest/mojave-sun-13)@[fe5d6c7b56...](https://github.com/Sinbest/mojave-sun-13/commit/fe5d6c7b568d550f403eb892ed47ffaf6b4fd28c)
#### Saturday 2023-11-25 02:55:16 by Technobug14

Agriculture (#2230)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

---
## [mihi314/git](https://github.com/mihi314/git)@[8f23432b38...](https://github.com/mihi314/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-11-25 03:25:45 by Johannes Schindelin

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
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[71b45e54ad...](https://github.com/dieamond13/tgstation-dieamond/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Saturday 2023-11-25 03:56:08 by san7890

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
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[9bc0add065...](https://github.com/f13babylon/f13babylon/commit/9bc0add065315cba3de80a2cc1feac5fe08e9fed)
#### Saturday 2023-11-25 06:15:48 by Stutternov

Locks Legion Combat Roles to Male Only (+ Other Legion Changes) (#176)

## About The Pull Request

Does the following:
- Locks all combat roles to male only - like they used to be prior to
Sunset changes.
- Locks Priestess of Mars to females only, as is in lore.
- Unlocks servant loadout on slave from being female only (real subtle
there guys)

Tl;dr - Females are relegated to slave, camp follower, auxilla,
forgemaster, or priestess. Males are able to be any role baring
priestess.

This is basically already 'rule enforced' so should just be re-added
code wise anyway.

## Why It's Good For The Game

Fits Fallout lore, the servers lore, and keeps the Legion's faction
design at least faithful to their purpose. (Hate telling people this but
- maybe........ legion aren't good people........)

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
adds: Locks roles in Legion based off gender restrictions.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [favoritehabit/CCVJ](https://github.com/favoritehabit/CCVJ)@[1c7eb27739...](https://github.com/favoritehabit/CCVJ/commit/1c7eb27739425ec8124639c0b5b6410b5bddd50e)
#### Saturday 2023-11-25 07:06:38 by favoritehabit

Colored fractal gen

Transcripts
00:04
Here we have our custom particle class to draw individual particle and define its behavior and movement. And we will have this rain class that will handle the entire effect, all the particles at once. Let's write and explain it line by line so we know exactly what's going on. This class will need a constructor. It will expect arguments for width and height of canvas, mainly because one of these classes responsibilities will be to spread our fractal particles over the available canvas area. I convert these arguments into class properties as usual,
00:36
canvas width property on this rain object we are creating right now is equal to canvas width variable that was passed as an argument to the class constructor. Canvas height property on this instance of rain class is equal to canvas height variable that was passed as an argument. This dot number of particles will determine maximum number of active particles on screen. This.particles will be an array and it will hold all currently active particle objects created using our Particle class. I create a private helper method called initialize.
01:08
The job of this private method will be to fill particles array from line 79 with 20 particle objects. So for-loop, it starts at 0, as long as i is less than number of particles from line 78, i++. Every time this for-loop runs, in our case, it will run 20 times. It will take this.particlesArray from line 70, and it will use built-in array push method. In JavaScript array push method adds one or more elements we pass to it, to the end of the array it is called on.
01:40
It also returns the new length of the array, which might be useful sometimes I pass it new Particle so one instance of our custom Particle class from line 70, the new keyword will look for a class called Particle, and it will create one new blank JavaScript object. It will then run code inside constructor of this Particle class to assign it values and properties based on the blueprint inside. Let's write our Particle class and define that blueprint. Each object created by this class will also have to be aware of
02:10
available canvas width and height because I want these objects to reset when they fall off screen. Initial starting x-position horizontal coordinate will be a random number between 0 and canvas width. Vertical y-coordinate will be a random value between 0 and canvas height. Width of each particle will be, for example, 50 pixels and height will be 50 pixels as well. Each particle object created by this class will have access to update method. Inside update method we will define behavior and movement.
02:42
Update method will be called over and over 60 times per second and each time it runs, we will push it one pixel on horizontal x-axis to the right, and one pixel on the vertical y-axis so downwards, these two actions combined will result in bottom-right movement. Each particle will also have its associated draw method where we define some code that will draw this particle 60 times per second. After each position update. Draw method, will need one argument to specify which canvas we want to draw on. This effect will use two canvas elements.
03:14
I will explain it as we go along. Let's start simple by calling built-in fill rectangle method. This method takes x, y, width, and height, and it will draw a rectangle at that position of that size. Perfect, so we have a blueprint that can be used to create 20 particle objects. On line 71, I can see my Particle class needs arguments for canvas width and canvas height. I need to remember that when I trigger this class constructor using the new keyword on line 97, I pass it this,canvasWidth from line 90
03:45
and this.canvasHeight from line 91. Initialize is a private method. It can't be called from outside of this class. It can only be called from somewhere within this class. Class constructor in JavaScript has one main purpose. It creates one new blank object and assigns it values and properties it contains to create one instance of that class. While doing that, it also runs all the code it contains. So we can take advantage of that and we can run our initialize method from inside of the constructor.
04:16
I do it by calling this dot #initialize like this. Structuring our code like this will cause the code inside initialize method to be automatically executed when the constructor is triggered. When we create an instance of this rain class using the new keyword, we will test it in a minute. Rain class will also need a public method that will run 60 times per second. It will cycle over all currently active particle objects from line 93 and it will call their associated update method from line 79 and draw
04:47
method from line 83 on each of these 20 particles one-by-one. And it will do it 60 times per second. So all our active particles will be constantly updating and redrawing at new positions, creating an illusion of movement. I do that by taking this dot particles array from line 93, which will contain 20 particle objects, thanks to the initialize method we just wrote and I call built-in for each array method on it. For each method executes a provided function once for each array element, so I assign each element a temporary variable name.
05:19
Just for the inner purposes of this for loop, I call each one, for example, particle, and provided function that will be executed for each one of the 20 elements will just take that particle and call its draw method from line 83. I can see that method expects argument for context to specify which canvas to draw on. Run method is public so it will take that context argument from the outside. I will show you in a minute when I call it, and it will pass that context along to draw method on each particle. For each array method,
05:49
will also call update method from line 79 on each particle object. Our Rain class is ready so let's try to run the code to see what we get. I create a custom variable I call for example rain effect, and I make it an instance of Rain class from line 88 using the new keyword. As we said, the new keyword will look for class with this name and it will run its constructor. On line 89. I can see that rain class expects canvas width and canvas height as arguments. So I pass it canvas width from line
06:20
four and canvas height from line five. Because we call this.#initialize on line 94 from inside the class constructor this code should get automatically triggered just by creating an instance of the Rain class. On line 97, we can see that this code should have filled this.particles array from line 93 with 20 particle objects. Let's check if it worked by console logging rainEffect from line 108. I open my console and I can see that we have
06:52
an instance of Rain class with properties like canvas width, canvas height and number of particles exactly as we defined in the blueprint. And we can also see that particles is an array with 20 objects created using Particle class. This is looking really good. Let's test if run method works. Since this is a public method, I can call it from the outside from the instance of this class. So rain effect dot run. I actually want this method to run over and over 60 times per second, updating and drawing
07:23
all 20 particles inside particles array. To do that, I will need to put it inside animation loop. I create a custom function. I call, for example, animate. Inside. I call rain effect from line 188 dot run the method we defined on line 101. Then I call request animation frame method. This built-in method tells the browser that we want to perform an animation and it will request that the browser to call a specific function to update the animation between the next repaint,
07:53
that function to be invoked before repaint is passed as an argument. And I will pass it animate the name of its parent function. So I will create an infinite loop. Animate will start, it will call run method from line 101 and then request animation frame we'll call animate again. This will repeat endlessly. When we call request animation frame like this, it will usually try to adjust itself to screen refresh rate. So in most cases it will run at 60 frames per second for smooth animation, here we declared animate.
08:24
I also need to call it for the first time to start animation loop. It's not working yet because here on line 101, I can see that run method expects context as an argument. Without it, JavaScript doesn't know which canvas element we are trying to draw on. I pass it ctx from line 3. And we are animating if this is your first canvas animation, I want to say congratulations, with the knowledge, we covered today you can do thousands of different effects. Let's finish and polish this one.

---
## [gummipappa/LittleGhostAuras](https://github.com/gummipappa/LittleGhostAuras)@[132c2c1697...](https://github.com/gummipappa/LittleGhostAuras/commit/132c2c1697ddb150eb0f202dff1c174172d80ef7)
#### Saturday 2023-11-25 07:28:00 by gummipappa

LGA v3.1.1 (10101)

everything but Warlock semi-fixed
* FUCK YOU Warlocks !!!

---
## [notJoon/gno-core](https://github.com/notJoon/gno-core)@[24d89a4f5d...](https://github.com/notJoon/gno-core/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Saturday 2023-11-25 07:48:28 by Morgan

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
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[8f3d1036c8...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Saturday 2023-11-25 07:53:42 by SkyratBot

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
## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[1fb70da3e5...](https://github.com/LeeroysHub/RM-Flipper/commit/1fb70da3e57d136161c6a4807e071eaaddefb13d)
#### Saturday 2023-11-25 08:09:25 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [Majkl-J/Bubberstation](https://github.com/Majkl-J/Bubberstation)@[52f69b96ee...](https://github.com/Majkl-J/Bubberstation/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Saturday 2023-11-25 08:47:26 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

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
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
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
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[d41d0e8e9a...](https://github.com/PlagueVonKarma/kep-hack/commit/d41d0e8e9aac039285a3530146f253b0f60385c9)
#### Saturday 2023-11-25 08:48:06 by Martha Schilling

minor post-playtest fixes

- Moved one of the trainers in the Celadon Uni PokeCenter to stop him from being in the way of the nurse

- Buffed one of the Scientists in the Mansion

- Moved the nurse and Weezing trader on the SS Anne slightly

- Boosted Meltan's catch rate because having it be that low is ridiculous

- Increased Luxwan's height because real swans are not that small

- Changed a Cue Ball's party to allow his dialogue to make sense

- Wild level balancing around Vermilion City

- Fixed a small Pokedex display bug

- Text fixes

---
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[47ab2308de...](https://github.com/RedSkulHYDRA/frameworks_base/commit/47ab2308deb3cd085a21e37911031bb1c8b62877)
#### Saturday 2023-11-25 09:07:34 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [CactuarXI/server](https://github.com/CactuarXI/server)@[aa30c9ec2e...](https://github.com/CactuarXI/server/commit/aa30c9ec2e15fd526fca9080ab434939d12a9656)
#### Saturday 2023-11-25 09:35:34 by MowFord

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
## [sla2her/Ark-Station-13](https://github.com/sla2her/Ark-Station-13)@[248e30344b...](https://github.com/sla2her/Ark-Station-13/commit/248e30344b49f69cdbfbea62ed0d8f2853a70547)
#### Saturday 2023-11-25 09:38:45 by SkyratBot

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
## [sla2her/Ark-Station-13](https://github.com/sla2her/Ark-Station-13)@[5761091212...](https://github.com/sla2her/Ark-Station-13/commit/57610912121327266d1b5b47eb6d93bfb33d8362)
#### Saturday 2023-11-25 09:38:45 by SkyratBot

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
## [diphons/sdm845-419](https://github.com/diphons/sdm845-419)@[b4d9d0e603...](https://github.com/diphons/sdm845-419/commit/b4d9d0e603bd85ec610e94404605d8b1b18dadcc)
#### Saturday 2023-11-25 09:42:48 by Peter Zijlstra

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
## [Ilya246/Mindustry](https://github.com/Ilya246/Mindustry)@[6200f08cd8...](https://github.com/Ilya246/Mindustry/commit/6200f08cd84b9a74563beddfe0c89106a43f6e1d)
#### Saturday 2023-11-25 09:54:41 by Darkness

Remove Darkdustry from the Global Server List (#9289)

The time has come. It's been more than two years since we started Mindurka, which was later renamed to Darkdustry. It was an amazing time and an amazing experience to maintain the server, to create plugins and gamemodes, to discuss mindustry with all of you. But It's enough. The server is getting constantly DDoSed, the host dies all the time and I have no motivation to develop anything related to Mindustry. 
Goodbye. And I hope, we'll meet again.

---
## [deepaklohia/ExcelAccessConnector](https://github.com/deepaklohia/ExcelAccessConnector)@[775ab4cf18...](https://github.com/deepaklohia/ExcelAccessConnector/commit/775ab4cf18ba417e5e4699a73c5e4c3cce3bdb35)
#### Saturday 2023-11-25 10:50:00 by DEEPAK LOHIA

Add files via upload

with the blessing of Lord Shiva and guru ji , unlocking these automations for you . enjoy learning.
regards
Deepak Lohia

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[eb246c21f6...](https://github.com/lizardqueenlexi/orbstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Saturday 2023-11-25 10:50:38 by san7890

Fixes sending stuff to "Old" Chat (#79819)

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

---
## [Alejodbort/Skyrat-tg](https://github.com/Alejodbort/Skyrat-tg)@[a7509e9dfb...](https://github.com/Alejodbort/Skyrat-tg/commit/a7509e9dfb6e1da12690aaa2a038293691d5f902)
#### Saturday 2023-11-25 11:02:58 by SkyratBot

[MIRROR] Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. [MDB IGNORE] (#24584)

* Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

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

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff.

* Modular

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [realme-spaced/android_kernel_realme_mt6781](https://github.com/realme-spaced/android_kernel_realme_mt6781)@[eabf2bfc25...](https://github.com/realme-spaced/android_kernel_realme_mt6781/commit/eabf2bfc25cafc0261d64fdd076a82c64e6bf46a)
#### Saturday 2023-11-25 13:28:05 by Wang Han

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
Signed-off-by: DrtSinX98 <pritish@stag-os.org>
Signed-off-by: rk134 <spaced@rk134.cf>
Signed-off-by: Antiquete <antiquete@proton.me>

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[db418b052e...](https://github.com/KingDragoness/ProjectHypatios/commit/db418b052e53d388041e0746f205bdee714003d6)
#### Saturday 2023-11-25 14:51:53 by KingDragoness

Hypatios 1.6.1b4 (QoL, content additions, bug fixes, balancing)
• Cheat: “cc lowpoly”
o Turns off all post-processing effects and texture quality to the lowest.
•  “wired.GhostOfTheSeas” (A soul stuck in an island and surrounded by the ocean)
o Inverted black and white. Black ground, white cross.
o Located in blackout office.
o ??? is Emperor with TV noise material.
o NPC: ??? and the inviter.
o Player enters a train to reach the red tower.
o Conversation
 ???: “I have nothing to speak of. Get out of from ghost of the seas server.”
 Aldrich: “Huh? What’s this behaviour?”
 ???: “And the year is 7000. The Cybernetics has ruled the galaxy.”
 ???: “All biological race in the world are almost perished. The Ionis has distributed itself to all over the galaxy.”
o After completing GOTS, the WIRED server will be broken, inaccessible.
• Favorite menu input instruction (RMB to return wheel selection)
• UPGRADE TEMPLE BRICK TEXTURE VINE. It looks like pixelated shit!
• Consider adding bomb enemy in Gauntlet
• REMOVED BOMB MONSTER in level 2
o It keeps fucking disappearing ARE YOU SERIOUS
• In a game update, rather than forcing player’s death, gives player a choice to “Kill Yourself” or “Keep Things as Is”
o The game has been updated to new version and the player may encounter problems. To prevent problems, it is recommended to ‘Kill Yourself’ to prevent issues.
• Tooltip hints to be converted:
o New: Subway Train
o Dentist Shop
o First Aid
o In the template level: CORE (Aldrich), Interactables
o In Liquidator level
• Poster of “Nietzma!” Sixtusian word means ‘Forge!’

---
## [openaia/kernel](https://github.com/openaia/kernel)@[a06a4dc3a0...](https://github.com/openaia/kernel/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Saturday 2023-11-25 15:51:12 by Neil Horman

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
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[d751e1c642...](https://github.com/mc-oofert/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Saturday 2023-11-25 15:57:41 by DaCoolBoss

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
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[a5fabd8819...](https://github.com/mc-oofert/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Saturday 2023-11-25 15:57:41 by Profakos

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
## [openaia/kernel](https://github.com/openaia/kernel)@[4d6fa57b4d...](https://github.com/openaia/kernel/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Saturday 2023-11-25 16:26:09 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [openaia/kernel](https://github.com/openaia/kernel)@[3eb39f4793...](https://github.com/openaia/kernel/commit/3eb39f47934f9d5a3027fe00d906a45fe3a15fad)
#### Saturday 2023-11-25 16:36:57 by Christian Brauner

signal: add pidfd_send_signal() syscall

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

---
## [fira/cmss13](https://github.com/fira/cmss13)@[15086ae683...](https://github.com/fira/cmss13/commit/15086ae683f727d9a990e05f8ce9a08e43731207)
#### Saturday 2023-11-25 16:47:07 by fira

Allow playing uploaded sounds through the music player w/ Webroot (#4934)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Too long have we suffered at the hands of admin auditive abuse. 

The prophet, spookydonut, once said, "You shouldn't be using this lol".
And he was right. Using "Play MIDI sound" both reduces usability for our
users, and can cause performance issues by freezing up the game for a
while as the data is transfered to these 200 poor CM addicts.

So we sought to alienate it with "Play Internet Sound" backed by
youtube-dl. Unfortunately, some things are subject to geo blocking or
simply not available on Youtube. Thus the regime of terror of Admins
continues.

This PR brings us one step closer to our goal: it allows to use the now
renamed "Play Admin Sound" to (also) upload a sound file to Webroot and
have it played through CDN. It also works with simple transport but that
mostly defeats the point.

Also reduced default volume for new players from 50% to 20%... Don't
worry, It's still way more than enough to get them to quit the server, i
have mine at 2-10% max

# Explain why it's good for the game
* Less new player abuse by reducing default volume
 * More performance by allowing big or custom songs to be backed by CDN
* Better UX: People can easily see the song name and more easily stop it
* Admins can now hide the name of played songs if they want to. Don't
ask me why.

# Testing Photographs and Procedure

![image](https://github.com/cmss13-devs/cmss13/assets/604624/4f00c45d-76ca-47e2-860a-2f26d55de2a4)
You'll have to believe me on the sound working

# Changelog
:cl:
balance: Default Web Music Player volume is now 20% down from 50%. It
was found too effective against new players.
admin: "Play Internet Sound" is now "Play Admin Sound" and optionally
allow to hide the track name.
admin: "Play Admin Sound" can now be used with uploaded tracks, which
use CDN delivery and the in-chat music player, granting players more
control over them.
admin: Removed "Play Midi Sound". 
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9229adc934...](https://github.com/tgstation/tgstation/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Saturday 2023-11-25 16:51:54 by DaydreamIQ

Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

---
## [kotmatross28729/BugTorch](https://github.com/kotmatross28729/BugTorch)@[544f58233e...](https://github.com/kotmatross28729/BugTorch/commit/544f58233e0e5ca32208ae488d1fe96025cde8a3)
#### Saturday 2023-11-25 16:56:23 by kotmatross28729

port cool thing from BetterWithPatches

This thing allows you to specify items in the config that, if placed on the top table of the furnace, will fucking explode it.
Originally from BetterWithPatches, but who cares about this useless fork?
Yes, I love putting trinitrotoluene from minechem into the lit furnace in the morning

---
## [wazmiali/MyCollegeCoding](https://github.com/wazmiali/MyCollegeCoding)@[63472c3a58...](https://github.com/wazmiali/MyCollegeCoding/commit/63472c3a58fd2c806120d90f9a38ea25f40b5df7)
#### Saturday 2023-11-25 17:07:17 by Wazmi Ali

Add files via upload

🚀 Completed My First Task at CodSoft: To-Do List CLI App!
Hello Connections,
I'm excited to share that I've successfully completed my first task at CodSoft—a To-Do List Command Line Interface (CLI) application. This project has allowed me to apply and enhance my Python programming skills.
I want to express my sincere appreciation to the Codsoft team for their guidance and support throughout this journey. This experience has been invaluable, and I look forward to what's next in my internship.
I invite you to watch the video and share your thoughts.
Thank you for being a part of my professional growth. 🙌 #Codsoft #Internship #PythonProgramming #SoftwareDevelopment

---
## [wesoda25/tgstation](https://github.com/wesoda25/tgstation)@[5175ae0637...](https://github.com/wesoda25/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Saturday 2023-11-25 17:09:17 by John Willard

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
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[d8733d82ee...](https://github.com/LumberKing/Tianxia/commit/d8733d82eeb054d23d6e9bb08492e0dadf852e60)
#### Saturday 2023-11-25 17:38:25 by Silversweeper

Liao history, Dragonslayer artefact work, misc

- Cut the Kowtow event chain and related decisions; vanilla's implementation does not work well for us, and making it work well for us would take too much work at this time. Something to re-implement in some form down the line.
- Cut the Kurultai succession law; our implementation wasn't great, and fixing it would a) be too much work at this time and b) might be better to do once we've thought more about nomads.
- Commented out assorted kowtow-related things.
- Added a few more nicknames, including coolness.
- Added missing fake mapmode loc.
- Fixed a bunch of duplicate dynasty ids.
- Added DW custom loc setup for Tianxia DWs; actual loc tags still TODO. Might be something to iterate on at a later date.
- Added missing geographical region loc.
- Added loc for several tooltips.
- Historical and CI titles now reference loc tags when renamed (e.g. the tag YUAN instead of "Yuan").
- CoAs:
	- k_heisui
	- k_jinshan
	- k_lan_xang
	- e_burma
	- e_golden_river
- WL hunts involving lions no longer speaks of the slopes of grasslands.
- Lions no longer placidly look at "a the horizon".
- Added loc for WL hunts involving tigers.
- Non-Norse WLs no longer speak of a "mead hall" in the hunt events.
- Minor tweaks to historical characters in Japan.
- Wonder bloodlines now give some Architect opinion.
- Added a bunch of missing event tooltip loc.
- Created credits.txt, to both ensure that credits can be found outside the forum thread and to facilitate easier updating thereof.
- The Draught of Healing now comes with a confirmation event, and now heals everything possible.
- The Living Flame is now one use only.
- All holy sites now have Protection from Evil (and Protection from Chaos), rendering them impossible to target by the Living Flame.
- Burninating provinces with extreme prejudice is now even more unwise.
- The Sword of Two Minds might now have an effect on your traits.
- Sanity's Demise's influence is now a touch more subtle... at first...
- Lunatics may no longer equip other ceremonial weapons if in possession Sanity's Demise. That would be wrong, don't you think...?
- Added decisions for all Dragonslayer artefacts that need them.
- Added on_actions for all Dragonslayer artefacts that need them.
- Liao's capital is now where it should be.
- Adjusted province ownership and setup to account for Liao being settled, as well as later events.
- Some Art of War pages will now spawn at the start.
- Art of War pages no longer count as books and no longer increase Martial indefinitely; they can instead be used to temporarily increase Martial.
- The Art of War can now be used to temporarily increase Martial, in addition to its previous effects.
- Some smaller fixes to loc.
- Assorted smaller script fixes.

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[4d4aa72e33...](https://github.com/FalloutFalcon/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Saturday 2023-11-25 17:46:39 by lizardqueenlexi

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
## [winglang/wing](https://github.com/winglang/wing)@[edd91d42e5...](https://github.com/winglang/wing/commit/edd91d42e570089b614dafad3f02601686b22c82)
#### Saturday 2023-11-25 18:13:28 by Mark McCulloh

feat(sdk): inflights are not required to be resources (#4993)

## Huh?

The primary goal of this PR is to reduce the input required to create an inflight function in TS (See https://github.com/winglang/wing/issues/4842) without necessarily overhauling the compiler (yet). Ideally, the minimum information required for an inflight is simply the code itself. However, because inflights are currently modeled as resources, they require a scope and id.

So the first change was to make a new non-resource interface, IInflight, encompassing the inflight contract. The most important part of this contract is that inflights must be liftable, a behavior currently unique to resources and certain other primitives. So I extracted the lift-related functions from IResource and slapped them on the new ILiftable (which both IInflight and IResource now extend).

But that created a new problem: lifting itself also currently requires a scope. The only usage of the scope was to be able to resolve tokens. This did not seem like a good enough reason to require scope, so I changed token resolution to be more of a global concern rather than a tree-level concern. This is dangerous, but it's mostly only dangerous when you try to deal with tokens in a multi-app scenario, which would be dangerous with our current approach anyways. So this is something we'll have to add some extra handling for eventually anyways.

## Results

The primary outcome of this can be seen in the SDK unit tests, where the `Testing.makeHandler()` now only requires the code and (optional) bindings. This is basically 1 or 2 steps away from an ideal TS experience.

## But wait nothing changed in winglang

The original purpose of representing inflights as resources was to ease the implementation of lifting in the compiler and generally unify the logic of inflights between inflight closures and inflight methods of preflight classes. This hasn't changed in this PR. Luckily, the class instance emitted by the wing compiler for inflights still satisfies IInflight. It just has some extra hidden resource stuff that is simply unused. Assuming this PR is wanted, I will do a followup to change the compiler as well. This will be a more complicated change and I think it's useful to basically get the backend working first.

## Changes

- `Testing.makeHandler` now takes only code text and bindings. 9 billion tests were updated for this contract. `convertBetweenHandlers` changed similarly
- TokenResolvers are now globally registered and not tied to specific apps
- wingc adds a _hash private field to inflight closure resource classes to match the new IInflight (just an md5 hash)
- Many of the resources that deduped functions based on `addr` now do so with `_hash` instead
- Removed many occurrences of `this.node.id` used in resource ids when it's not necessary. The only time this should be necessary is if the resources is being created in the scope of this.node.scope instead
- Added a `Counter` concept to help with the many places that we want to add a subresource many times and a simple incrementing number will suffice for uniqueness and clarity
  - This was needed because the inflight `addr` was often relied upon to make this unique, but that will no longer be viable. I think it's better this way anyways

*By submitting this pull request, I confirm that my contribution is made under the terms of the [Wing Cloud Contribution License](https://github.com/winglang/wing/blob/main/CONTRIBUTION_LICENSE.md)*.

---
## [AysheDaArtist/sojourn-station](https://github.com/AysheDaArtist/sojourn-station)@[94b32aa82c...](https://github.com/AysheDaArtist/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Saturday 2023-11-25 18:27:30 by CDB

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
## [SolomonAgyire/Python-Project-1](https://github.com/SolomonAgyire/Python-Project-1)@[80b95be237...](https://github.com/SolomonAgyire/Python-Project-1/commit/80b95be237b33866bf261f4c713673e58462725e)
#### Saturday 2023-11-25 19:39:00 by Solomon Agyire

Update README.md

🔢 Welcome to Countdown21 – a thrilling number game designed to test your strategic thinking and arithmetic prowess! Dive into the challenge as you start at 21 and navigate a series of subtractive moves to reach the ultimate goal of 0. This Python-based game offers a captivating blend of logic and quick calculations, making it an ideal choice for those who enjoy brain-teasing puzzles.

Key Features:
Strategic Gameplay: Plan your moves wisely to subtract numbers from the current count and strategically navigate towards the target of 0.
Dynamic Difficulty: Whether you're a math whiz or looking to sharpen your skills, Countdown21 caters to various skill levels, offering a progressively challenging experience.
Real-time Feedback: Receive instant feedback on your moves with color-coded indicators, keeping the gameplay engaging and visually appealing.
Time Challenge: How fast can you count down to 0? The game encourages friendly competition, challenging players to beat their own time records.

How to Play:
Clone the repository to your local machine.
Run the Countdown21.py script.
Start the game at 21 and strategically subtract numbers to reach 0.
Test your skills, challenge your friends, and enjoy the thrill of Countdown21!

Contribute:
Have ideas to enhance the game or found a bug? Contributions are welcome! Open an issue or submit a pull request to be part of improving Countdown21.

Get ready for a mathematical adventure – Countdown from 21 begins now! 🚀🔢

---
## [SolomonAgyire/Wordle](https://github.com/SolomonAgyire/Wordle)@[212c9e0c02...](https://github.com/SolomonAgyire/Wordle/commit/212c9e0c02c7466e18c858e6f18138eae92c0559)
#### Saturday 2023-11-25 19:43:57 by Solomon Agyire

Update README.md

🔠 WordleCraft invites you to a world of word-guessing fun! Immerse yourself in this Python-based game that challenges your vocabulary and deduction skills. With a sleek interface, dynamic word selection, and adjustable difficulty modes, WordleCraft offers an engaging and colorful experience for word enthusiasts of all levels.

Key Features:
Intuitive Interface: Enjoy a user-friendly design that enhances your gaming experience with seamless navigation and vibrant visuals.
Dynamic Word Selection: The game selects a diverse range of words for each round, keeping the guessing adventure fresh and exciting.
Difficulty Modes: Choose between Normal and Hard modes, tailoring the challenge to your comfort level and allowing both casual players and word aficionados to enjoy the game.
Colorful Feedback: Receive instant feedback on your guesses with a visually appealing color-coded system, making each attempt both strategic and visually engaging.

How to Play:
Clone the repository to your local machine.
Run the WordleCraft.py script.
Choose your game mode (Normal or Hard).
Dive into the word-guessing adventure, and let the colorful journey begin!

Contribute:
Do you have ideas for enhancing the game or want to report an issue? Contributions are highly valued! Open an issue or submit a pull request to improve the WordleCraft experience.

Embark on a wordy journey with WordleCraft – where letters, colors, and words come together! 🌐🔤🎮

---
## [maksfb/llvm-project](https://github.com/maksfb/llvm-project)@[5cd24759c4...](https://github.com/maksfb/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Saturday 2023-11-25 20:41:37 by Louis Dionne

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

---
## [Krutikaaa20/IPL-SCORE-PREDICTION-USING-MACHINE-LEARNING](https://github.com/Krutikaaa20/IPL-SCORE-PREDICTION-USING-MACHINE-LEARNING)@[adf7a0d148...](https://github.com/Krutikaaa20/IPL-SCORE-PREDICTION-USING-MACHINE-LEARNING/commit/adf7a0d148dc130a572961b12c1a7e2ec55e267c)
#### Saturday 2023-11-25 20:58:49 by Krutika .D. Naidu

 IPL Score Prediction Using Machine Learning! 🤖🔮

Exciting News! 🏏✨ Delighted to share my latest project - IPL Score Prediction Using Machine Learning! 🤖🔮

In the ever-evolving world of technology and sports, I embarked on a thrilling journey to combine the best of both worlds. 🚀 Leveraging the power of Machine Learning, I've developed a cutting-edge model to predict IPL scores with remarkable accuracy. 📈🔥

The IPL Score Prediction model utilizes advanced algorithms and historical data to analyze various factors influencing match outcomes. From player performance and team dynamics to pitch conditions, the model takes it all into account for precise predictions. 🧠💻

Why is this groundbreaking? Because it adds a whole new dimension to the way we experience and engage with the game we love! 🌐 Imagine having insights into potential scores before the first ball is even bowled – it's a game-changer for fans, analysts, and enthusiasts alike. 🏆🎉

Stay tuned as I unravel the details behind the scenes, showcasing the intersection of cricket and artificial intelligence. 🤯🏏 Your feedback and insights are always welcome as we continue to push the boundaries of what's possible in the world of sports analytics. 🌟

Let's celebrate the convergence of technology and cricket, making the IPL experience even more thrilling and insightful! 🚀🏏 #IPL #MachineLearning #CricketTech #Innovation #DataScience #SportsAnalytics

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[223dc74ef1...](https://github.com/goober3/hi-github-portside/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Saturday 2023-11-25 21:36:12 by retlaw34

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
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[ef52047274...](https://github.com/nikothedude/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Saturday 2023-11-25 21:48:29 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [kyuujuushi/thebuzz](https://github.com/kyuujuushi/thebuzz)@[de9c182262...](https://github.com/kyuujuushi/thebuzz/commit/de9c182262595eac03e30b785f0fb992db2aa83c)
#### Saturday 2023-11-25 21:54:18 by kyuujuushi

fucked around in the html. the link to the file is still ass. its asking for a stupid endpoint or im putting too many arguments apperantly. fuck flask

---

