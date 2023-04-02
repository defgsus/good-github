## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-01](docs/good-messages/2023/2023-04-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,942,449 were push events containing 2,904,061 commit messages that amount to 215,660,787 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 71 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[42db3f65ab...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/42db3f65ab0570a7c04b6a5f0960ac62e1d1e1ff)
#### Saturday 2023-04-01 00:13:25 by SkyratBot

[MIRROR] Fixes Active Turf Scenario on Tramstation [MDB IGNORE] (#20202)

* Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:

![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)

Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

* Fixes Active Turf Scenario on Tramstation

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[944b790c93...](https://github.com/mc776/freedoom/commit/944b790c931be9e42383cef9429750fd16883df5)
#### Saturday 2023-04-01 00:18:17 by mc776

dehacked: fix quit messages.

The messages hadn't been checked for length. Fortunately caught relatively early because the only string that shows up in vanilla (and thus would cause a crash) is also one of the longest ones.

I've also amended two things in the text itself:

1. big burly violent guy who's all about freedom and blaming scientists for things is...... not something that's aged well. And when a corporation is involved you know it's the investors pushing for the bad thing and not the actual researchers on the ground.

2. that other quit message literally reads like you're goading someone into suicide IRL, in the current environment where everybody's depressed and a lot of us have lost important people to plague or war or medical neglect or workplace accidents or violent bigotry or any combination thereof. I've taken the liberty to rephrase it so the emphasis is on what I think was intended.

Threw in a replacement for "exit to DOS" as well.

---
## [UChicago-Robotics/BattleBot](https://github.com/UChicago-Robotics/BattleBot)@[2e887e3c91...](https://github.com/UChicago-Robotics/BattleBot/commit/2e887e3c91ab36b2e8a00a4649ea110f995789ba)
#### Saturday 2023-04-01 00:25:44 by Gideon Mitchell

Awful hacks to make shit work [Working Competition Version]

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[a2d5ca6e69...](https://github.com/Ultimate-Fluff/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Saturday 2023-04-01 00:55:18 by QuickLode

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
## [shlomif/perl5](https://github.com/shlomif/perl5)@[15119347e4...](https://github.com/shlomif/perl5/commit/15119347e461bd5ff2afb671b1c8138cbe635b42)
#### Saturday 2023-04-01 01:15:53 by Yves Orton

epigraphs.pod - add epigraph from 5.37.10

My dad had beautiful handwriting, and whenever he got a new pen he would
write out this stanza of Lewis Carrolls poem on the blue lined paper he
used to write his notes on. So this is my homage to him.

For some reason I can never remember the wording properly and say it
as "to /speak/ of many things" instead of "to /talk/ of many things".
Memory is a funny thing.

---
## [Hopekz/CEV-Eris](https://github.com/Hopekz/CEV-Eris)@[6f75cb9845...](https://github.com/Hopekz/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Saturday 2023-04-01 01:21:16 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[c8f395848d...](https://github.com/git-for-windows/git/commit/c8f395848de6089cbb92a0010b21339478dcf88c)
#### Saturday 2023-04-01 01:27:24 by Johannes Schindelin

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[60d2d2ee1a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Saturday 2023-04-01 01:53:44 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Qiskit/rustworkx](https://github.com/Qiskit/rustworkx)@[e025356b04...](https://github.com/Qiskit/rustworkx/commit/e025356b046a807e848a7c0ee2a32490927d46da)
#### Saturday 2023-04-01 01:57:17 by Matthew Treinish

Update tox configuration to use tox >= 4.4.0 (#851)

* Update tox configuration to use tox >= 4.4.0

Tox 4.0.0 was released in December 2022 [1] and was a major rewrite of
the internals of the package that included numerous backwards
incompatible changes [2]. Along with that major rewrite was a long
period of instability in the package with a flurry of 47 releases [3]
since 4.0.0 (which has only been 3-4 months). At the time of the 4.0.0
release we pinned the tox version in CI with #761 to avoid this
instability as our tox configuration was not compatible with tox 4.x.y
and tox was actually not compatible with how we had things configured
more generally. The hope was that tox would stabilize more, fix the
issues that plagued the tox 4 release series and we'd be able to relax
that pin without requiring bumping our minimum tox version to ensure
users could use either the old version or the new version locally.
However, since #761 that hope hasn't been realized the divergence
between tox 3 and tox 4 has only widened and at least personally I'm not
convinced of an improvement in stability to the tox 4 release series.
That being said however, this is becoming a developer pain as by default
when setting up a new build environment pip will install the latest
version of tox and we don't have an effective mechanism to pin the tox
version for users as you need to install tox manually as it's the
primary python development entrypoint we use. The only only avenue to
address this would be documentation updates in the CONTRIBUTING.md file,
which we didn't update at the time in #761 because it was meant to be
a version temporary pin that has turned out to not be so temporary.

Since it's been >3 months since we first pinned the tox version and that
pin was meant to be temporary this commit removes that pin and bumps our
minimum supported tox version to be 4.4.0, which despite not being
compatible with tox < 4 as we originally hoped, at least seems to work
fine with install rustworkx after updating the configuration file. This
should hopefully ease the onboarding experience for developers when
working with rustworkx and trying to bootstrap a local development
environment. Longer term I expect we'll look at moving off of tox,
as it no longer seems like a project we can rely on (especially as
a key component for our development and CI infrastructure) for rustworkx
and instead look at something like `nox` which I've heard good things
about and know that PyO3 had moved to it a year or two ago.

Fixes #812

[1] https://pypi.org/project/tox/4.0.0/
[2] https://tox.wiki/en/latest/upgrading.html
[3] https://pypi.org/project/tox/#history

* Stop using tox for retworkx backwards compat jobs

Tox's isolated builder mechanism seems to be incompatible with our
environment variable based package naming mechanism that we use to build
the legacy retworkx package. This is causing CI to fail on the backwards
compat jobs that are installing retworkx (which depends on rustworkx) to
ensure that our backwards compatibility shim works as expected. Instead
of trying to force tox to do the correct thing, it's just easier to stop
using it for that one CI job and instead just manually install and run
the tests.

---
## [Zman6258/PERSIST-RCO](https://github.com/Zman6258/PERSIST-RCO)@[789738c6f3...](https://github.com/Zman6258/PERSIST-RCO/commit/789738c6f33218df31589551f9ef503224d6d0e0)
#### Saturday 2023-04-01 02:03:14 by Zman6258

Add earplugs to loadout on save, if unit has earplugs in

First checks if the player has an actual uniform/vest/backpack to save them in, then inserts the item in the loadout to be saved. Since it directly modifies the array of items stored in the loadout, it'll also ignore how full the container actually is, meaning we don't need to worry about players not having room to fit them. I don't really see this as a major issue honestly, because at the start of the next operation the player is likely to reinsert their earplugs immediately.

Also re-indented that part of the file because my god the indentation and spacing here is awful (no offense).

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[ef9d0c61a3...](https://github.com/Warfan1815/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Saturday 2023-04-01 02:31:08 by Moonshanks

Altitude Control: Console, Skills, TGUI, Shuttle, OB, And Hijack changes. (#2760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
This pull request adds a feature via the
/machinery/computer/attitude_control_console.

The USS Almayer can now be "moved" between three different levels of
orbit/proximity to the AO:

High,
Optimal,
Low

Each level comes with changes to the duration of transport timers, time
to transport during hijack, and OB cooldown timer, equal to the
GLOB.ship_alt value.

High makes OB cooldowns take 200 seconds longer, dropship transport
times take 50% longer, and the dropship hijack transport time take 50%
longer

Optimal, the default which will stay in place if no one touches the
console leaves everything with their default times and cooldowns,

Low, OB cooldowns take 200 shorter, dropship transport times are 50%
shorter, the dropship hijack transport time is 50% shorter.

While in Low orbit the Almayer will periodically shake (50% chance to
shake every 30 seconds), the Almayer's thrusters will also start
building up heat as they battle with making minor adjustments due to the
dangerous proximity to the AO. They will gain 10% of their max heat each
30 seconds, once they reach 100% the ship will be forced into the
highest orbit to cool off, and cool off slower than normal (5% every 30
seconds) until its orbit is changed.

While in Optimal or High orbit the Almayer thrusters will cool off by
10% per 30 seconds.

The Almayer's orbit may only be changed by those with a "navigations"
skill of 1. (only the CO and Synth -- EDIT: XO now has the skill too --
currently but I may add a dedicated RP role for this mechanic later down
the line). The orbital level may only be changed every 90 seconds and
when it changes the ship will shake violently causing every mob on the z
level to fall over.

This PR does not place the Altitude Control Console on the map, so
currently, these features don't do anything within a normal round unless
staff spawns in the console, however I will be uploading a mapping PR
changing the Astronavigations deck if this PR is accepted.

Planned for the future but not yet approved connected to this PR is the
"Navigations Officer" the highest auxiliary support personnel with
skills the same as an SO, sans a 1 in Navigations, and a 1 or 2 in
piloting. The idea for this future role would be set out in the PR, but
it would represent a mainly fluff officer role that was unable to deploy
under normal SoP.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This PR is a non-intrusive way to add more nuanced gameplay mechanics to
COs, especially on the quieter rounds when they aren't swamped by OW
duties.

The way the PR is currently designed it doesn't effect any gameplay
balance if it isn't used. If a CO however chooses to use it they have to
pay some level of attention to it or they will overheat the engines and
cause their transport times to be lengthened.

It's a relatively simple way to add more complexity to CIC, and give the
CO/Synth more stuff to do to gain a slight edge.

I have been able to test everything other than the hijack time increase.
However, the line of code handling the hijack time increase is one line
long. Everything else is confirmed as working and the common bugs this
could create have been tested for and not found (transport shows the
right time when the time is modified, OB shows the right cooldown time,
the cooling can't drop the heat% below 0 nor above 100, the TGUI works
without issues, the console can only be used by those with the right
skills, and the knockdown effects all mobs on the Almayer not just
humans).

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

https://www.youtube.com/watch?v=-cbnqNtKyCY - video showing the CO and
Synth using the console, with the knockdown effect and arrest radio
announcements.

https://youtu.be/Qd37iM-4FrQ - video of the overheat function and the
ship shaking due to low orbit

https://www.youtube.com/watch?v=EWLCDZp-9iI - video of the ship being
left on low orbit for too long, and what happens when the engines
overheat

https://www.youtube.com/watch?v=u_ErqfU-nus - video showing the orbital
distance effecting the transport time

https://www.youtube.com/watch?v=j687yqlWLT8 - video showing high orbit
effecting the OB cooldown time.

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

:cl:
add: added altitude control console and related mechanic
add: added the 'navigations' skill for using the console and applied it
to the CO/Synth
balance: added a mechanic for COs to reduce transport and OB cooldown
times, and increase hijack transport times
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[c18b1ef442...](https://github.com/EOBGames/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Saturday 2023-04-01 03:07:39 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[6f1b1717a7...](https://github.com/PhantomEpicness/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Saturday 2023-04-01 03:33:42 by TotalEpicness

Boiler rework Part 1: Globber base boiler (#965)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request


A total redesign of the base boiler reminiscent of the old premoba
boiler that would shoot projectile "Globs" with a modern CM take.

Base boiler as it is right now, is completely unfun, to play against and
to even play as. You'd be hard-pressed to find someone who enjoys
playing it past the first 10 minutes of doing so. It is this way not
because it's weak, but because it's unchallenging and 100% "safe"
gameplay. There are no combos, cool moves you can do, or even satisfying
effects, you just hit a button to spawn a telegraph which becomes a gas
cloud.

This PR, turns that right ontop of its head. Instead of "safe" gameplay,
globber's design philosophy is centered around being challenging, fun
and even adding new gameplay dynamics.

Globber will have higher HP, faster walkspeed, and faster firing bombard
compared to premoba.

However, globber will have their fellow xenos making plays to cover for
boiler, either directly through bodyblocking shots or making plays to
distract marines due to a minimal zoom range.

These both, in theory, will create a new gameplay dynamic where boilers
will still be able to block marine spearheads, but Globber needs to help
make a small counter push with their fellow brethren in order for
Globber to directly strike at marines and giving the Xenos the choice to
either capitalize on their advantage or heal up upon a successful glob.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

### Details:
Globber will feature [TENTATIVE] higher HP and [TENTATIVE] faster walk
speed. It however will be slightly more vulnerable to fire as fire deals
[TENTATIVE]% more damage to it!


https://cdn.discordapp.com/attachments/458150341742166017/1013647188313776148/2022-08-28_17-10-53.mov

Globber Active 1 - Bombard: Spit a large acid glob that will, upon
impact, immediately spread a gas glob of your choice

- Cooldown: 30 seconds
- cost: 200 plasma
- Windup: 5 seconds

Globber Active 2 - Acid spray, instantly sprays a line of acid, May make
it a cone spray if it is too weak

- 8 second c/d
- No windup
- 40 plasma
- 6 tile range

Globber Active 3 - Shift spits: Switch between acid and neuro gas globs.
Acid deals more raw damage while neuro slows,blinds and eventually
knocks down marines. Neuro has a larger radius than acid

Globber Active 4 - Acid shroud: A quick windup action that dumps an acid
cloud over the boiler. Cooldowns other abilities similar to dump acid.

Globber Active 5 - Zoom: Short ranged zoom with short windup. Trades
awareness for zoom

Globber Passive: Brute armor, Globber features brute armor, however, it
does not protect against flames! Globber takes 1.5x damage to fire!

Acid glob: Pretty much the same as before. May adjust numbers.

Neuro smoke rework:
- Instead of insta blindness and deafness, these will now have a chance
of applying for every tick you are in the smoke. You still have
blurry/weldervision though
- Oxyloss toned down, it was 9 per tick, now two
- Knockdown chance lowered to 5% per tick. Stamina damage replaces RNG
knockdowns
+ Now deals stamina damage, and am making it stack fast, targeted
knockdown time is 2-3 seconds
+ Minor immediate slowdown applied. May remove as it stacks with stamina
damage slow
+ chance of dealing minor tox damage

### Boiler rework as a whole

The boiler rework is a total rework of the boiler strain and it's
strains.

I'm not gonna write the entire design doc here, but in short:

-Base boiler will be reworked (as shown here), named Globber
- trapper will be totally scrapped for 'Grenadier', a heavy siege strain
that lobs devastating nades that's counterable and challenging.
Grenadier will have the same zoom as Globber
- A long-range, general-purpose strain will be added, named "Striker
Boiler", which combines both the Railgun boiler and the mostly forgotten
"Acid Splatter" strains in the past, with a modern CM twist.

design docs( old as fuck and needs updating) _**REPLACE ME WITH NEW
ONE**_
https://github.com/cmss13-devs/cmss13-design-docs/pull/7
Striker design doc
https://github.com/cmss13-devs/cmss13-design-docs/pull/8


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
TL;DR base boiler is a literal NPC strain that no one likes to play as
or against. Attempt to make it more fun or die trying

if the design philosophy fails, then we can simply just tweak a few
values and have premoba boiler again.

Design doc is already made but its ancient as shit and I'm just gonna
make a new one so its WIP for now.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Totalepicness
add: Added "Globber Boiler", which is a total replacement of base
boiler, designed to kill the "safe" gameplay loops of current base
boiler in an attempt for a more challenging and fun caste to both play
as and against.
balance: Globber Active 1 - Bombard: Spit a large acid glob that will,
upon impact, immediately spread a gas glob of your choice
balance: Globber Active 2 - Spray acid: Instantly sprays a line of acid
balance: Globber Active 3 - Shift spits: Switch between acid and neuro
gas globs. Acid deals damage while neuro slows, blinds and eventually
knocks down marines. Neuro has a larger radius than acid
balance: Globber Active 4 - Acid shroud: A quick windup action that
dumps an acid cloud over the boiler. Cooldowns other abilities similar
to dump acid.
balance: Globber Active 5 - Zoom: Short-ranged zoom with no windup.
balance: Globber Passive: Globber features armor, but it is weaker
against flames! Stay away from fire!
refactor: Refractored some minor spit code and icons
balance: Neuro has been completely reworked to deal mainly stamina
damage, causes dizzyness and has a small chance to make you 'stumble' in
a random direction along with minor tox damage. Stay out of it!
add: Completly reworked neuro gas, it now uses a proper effect with
escalating effects the larger the dosage rather than RNG.
fix: Acid now deals damage to cades and now has a good chance of going
over instead of being airtight
fix:  Boiler globs no longer can target mobs and track them.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: Geeves <ggrobler447@gmail.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fe7ebd67cf...](https://github.com/tgstation/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Saturday 2023-04-01 04:11:22 by LemonInTheDark

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
## [newstools/2023-metro](https://github.com/newstools/2023-metro)@[cc05ebf1a3...](https://github.com/newstools/2023-metro/commit/cc05ebf1a3dbf7997c298331aa272db5f2a66008)
#### Saturday 2023-04-01 04:38:11 by Billy Einkamerer

Created Text For URL [metro.co.uk/2023/03/31/spencer-webbs-girlfriend-gives-birth-to-baby-boy-after-his-death-18539051/]

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f10b0dd42a...](https://github.com/tgstation/tgstation/commit/f10b0dd42aa996971f472edb7e65b3e504cb7ec5)
#### Saturday 2023-04-01 04:44:27 by 13spacemen

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
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[bdc9c58586...](https://github.com/Hekzder/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Saturday 2023-04-01 05:10:57 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

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

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [Caddwithadot/GAM120A-Something](https://github.com/Caddwithadot/GAM120A-Something)@[403bb47be5...](https://github.com/Caddwithadot/GAM120A-Something/commit/403bb47be5f1eb400ab957341717a16206172bae)
#### Saturday 2023-04-01 05:41:25 by Jake DeLuise

minor fixes to A-2 and A-3... but holy shit Level15's a fucken thing

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[ab307032ed...](https://github.com/SomeRandomOwl/tgstation/commit/ab307032edc7ed3dd360bfcc9176f6f54c22a3fe)
#### Saturday 2023-04-01 05:41:40 by LemonInTheDark

Nightvision Rework (In the name of color) (#73094)

## About The Pull Request

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

### `see_in_dark` and why it kinda sucks

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this


![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

### Color and why `lighting_alpha` REALLY sucks

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

### But wait, there's more

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice. 
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

### **EDIT**

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level. 
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

#### Adds filter proc (the ones that act like templates) support to
filter transitions.
Found this when testing this pr, seemed silly.

#### Makes our emissive mask mask all light instead
This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen. 
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

#### Moves openspace to its own plane that doesn't draw, maxing its
color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

#### Changes our definition of nightvision to the light cutoff of night
vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

#### Removes the nightvision spell
It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

#### Cleans up existing plane master critical defines, ensures
trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

## Why It's Good For The Game

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color


https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)


https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives


https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)


https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors


https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)


https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs


https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

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
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[5a069975c3...](https://github.com/SomeRandomOwl/tgstation/commit/5a069975c3083888c986302ab5c0b32fc4362c20)
#### Saturday 2023-04-01 05:41:40 by LemonInTheDark

God I hate my life

This reverts commit d57e2000384a0176f11f4c1266fbea3ff102f068.

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[4599842d7c...](https://github.com/SomeRandomOwl/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Saturday 2023-04-01 05:41:40 by Jacquerel

Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[fc1e2e5e26...](https://github.com/PhantomEpicness/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Saturday 2023-04-01 05:56:08 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
 
:cl:
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [Mokolea/git](https://github.com/Mokolea/git)@[eaa0fd6584...](https://github.com/Mokolea/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Saturday 2023-04-01 06:13:38 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [corbin-poteet/put-me-on](https://github.com/corbin-poteet/put-me-on)@[303f8e2d88...](https://github.com/corbin-poteet/put-me-on/commit/303f8e2d88f116115932cecb29f3e92138a22a93)
#### Saturday 2023-04-01 06:18:36 by Corbin Poteet

Fixed every stupid fucking warning it was bitching about jesus fucking christ fuck you expo

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[725233b42b...](https://github.com/thgvr/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Saturday 2023-04-01 06:41:12 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[d72ef99270...](https://github.com/Time-Green/tgstation/commit/d72ef99270f2697064681b3214f0569dcf38d526)
#### Saturday 2023-04-01 07:00:08 by necromanceranne

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
## [chaoko99/IS12-Warfare](https://github.com/chaoko99/IS12-Warfare)@[1867654758...](https://github.com/chaoko99/IS12-Warfare/commit/186765475881bf58bbee319880653287d578820b)
#### Saturday 2023-04-01 07:30:13 by Matt

Should fix the issue of loading the wrong CSS by making them all the same fuck you

---
## [peff/git](https://github.com/peff/git)@[943c132179...](https://github.com/peff/git/commit/943c13217956660f64d31521344511b0754bb339)
#### Saturday 2023-04-01 07:47:08 by Jeff King

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
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[bc1fc05c1b...](https://github.com/AOSP-Krypton/frameworks_base/commit/bc1fc05c1b3e8c407fa07b25777bf577d5285f49)
#### Saturday 2023-04-01 07:54:21 by Nick Pelly

Delay 500ms between each registering each SDP record using sdptool.

This is to workaround an issue where SDP records will fail to register using
sdptool. When we run SystemService.start() it forks sdptool, so if we do this
four times in a row these forked processes can run in parallel, and one or
more of them fails. There is probably some thready safety issue in sdptool
or Bluez that makes it unsafe to run sdptool in parallel.

As a workaround, delay 500ms between each run of sdptool to register SDP
records when starting Bluetooth.

Before this fix it was easy to reproduce problems with service record
registration. If you turn BT off/on multiple times you can see that sometimes
one or more service records are missing. Repro rate is about 20% in my tests.
Result is that remote devices cannot connect to the missing service.

After this fix I am unable to reproduce any missing SDP records, after 30+
cycles of BT on/off. Motorola BT team also ran stress tests overnight with this
fix and were unable to reproduce the missing SDP records.

This is a low risk fix. It does delay some records from being registered
by an additional 1.5 seconds (on top of the 3 second delay we already had),
so if you try and very quickly connect a BT service after turning BT on it
won't work the first time.

Do not merge. (I will use a less hacky fix for MR2/Master)

Change-Id: I305c181c3194e8ce25e3825320cc2e1ef6d3d3cc
Bug: 2180800
DrNo: eastham
Joke: Why can't you play cards in the jungle? Because there's too many cheetas!

---
## [theres-waldo/mozsearch](https://github.com/theres-waldo/mozsearch)@[78d42a85e9...](https://github.com/theres-waldo/mozsearch/commit/78d42a85e990ae4dee17a0f2c549342703c66344)
#### Saturday 2023-04-01 08:12:27 by Andrew Sutherland

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
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[1ba101f82e...](https://github.com/AOSP-Krypton/frameworks_base/commit/1ba101f82eae4e54293428480fbcbfd1c58359c8)
#### Saturday 2023-04-01 08:19:34 by Steve Howard

Improve accelerometer-based orientation sensing.

There were three main complains about orientation sensing:
* Switching to landscape when putting a device down on a table (or picking it up)
* Changing orientation due to road bumps or vehicle vibrations while in a car dock
* Switching to upside-down too easily

This change includes three primary enhancements.

First, we run the accelerometer output through a lowpass filter before considering its orientation.  This avoids glitches due to brief phone movement, particularly when the phone hits a table.  The filter uses a very low default time constant of 200ms to retain responsiveness (note the samping period is ~200ms, so the effect of this filtering is pretty mild).  At tilt angles beyond 45 degrees, however, we increase the time constant to 600ms, which helps greatly with avoiding glitches picking the phone up from a table.  It does introduce some sluggishness when rotating while the phone is tilted back, i.e. being used in one's lap.

It's also worth mentioning that the accelerometer output on Sapphire appears to be pre-lowpass-filtered with a time constant of around 500ms, making this less necessary on that device, but the added effect doesn't noticeably degrade user experience in my opinion.

Second, we check the magnitude of the raw accelerometer output.  If it deviates from the strength of gravity by more than one m/s^2, we distrust the data, since that implies the device is under external acceleration and the sensor data doesn't accurately reflect orientation.  This helps avoid glitches due to shocks and vibrations, as in the car dock scenario.  However, rather than ignore the data entirely, we filter it with a very high time constant (5 sec).  As a result, if the device is rotated while vibrating, even if we never pick up a clean sample, we will eventually detect the orientation switch.  Of course, with a sampling period of 200ms, we're prone to aliasing, but that seems like a highly unlikely corner case.

Third, we restrict transitions to upside-down orientation to a much narrower range, both in terms of orientation and tilt.  This should prevent upside-down mode from activating in most cases where it's not desired.

I also updated a lot of stale documentation, added a lot of documentation, and cleaned up a lot of the code, so as to make this (often subtle) code as transparent as possible.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[95b810919e...](https://github.com/Time-Green/tgstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Saturday 2023-04-01 09:03:09 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[e6c70a49e4...](https://github.com/TaleStation/TaleStation/commit/e6c70a49e4783bd55ae8b20efc97a481802275a1)
#### Saturday 2023-04-01 10:04:03 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes "Atmos Asteroid" Active Turfs - Irony Edition (#5162)

Original PR: https://github.com/tgstation/tgstation/pull/74379
-----

## About The Pull Request

This ruin was consistently triggering 4 Active Turfs on prod. 


![image](https://user-images.githubusercontent.com/34697715/228991150-e90e7d8a-a19a-41ff-8101-a3c172e2883a.png)

This was because two turfs didn't have the correct gas mix varedit. This
is probably fine, but I hate varediting turfs like this because anyone
can grab a turf and not realize that it's somehow special if they don't
check the varedits/keys of the map after it's applied. I get the gimmick
and that's cool, but let's do it a different way.

So, I just made them all defined in the code, and span up a quick
updatepaths to update all the turfs (to ensure I didn't balls it up
somehow). Very cool.

I also did two more things

* Added a new area for this ruin only. This is because the atmos turf
stuff is a bit spooky to me, and I want to know _instantly_ if this ruin
is causing more issues. Don't think it should have a name for GPS
reasons but we definitely need a unique area type.

* Fixed a typo in the datum typepath. That was irritating me. It's fixed
now.
## Why It's Good For The Game

I NEED LESS ACTIVE TURFS THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE
NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE
IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO
MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH
THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE
NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE
IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO
MUCH THE NOISE IS TOO MUCH THE NOISE IS TOO MUCH
## Changelog
Player's shouldn't really notice or care.

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [sqlitebrowser/dbhub.io](https://github.com/sqlitebrowser/dbhub.io)@[2d2d5241e1...](https://github.com/sqlitebrowser/dbhub.io/commit/2d2d5241e190d0c7615a8b52db08d656b3d654ac)
#### Saturday 2023-04-01 10:10:13 by Justin Clift

WIP. Work around both AngularJS and Cypress doing stupid shit

Different problems, but with some overlap.  Anyway, this workaround
is functional, so fuck it, good enough.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[d43ebd042d...](https://github.com/LemonInTheDark/tgstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Saturday 2023-04-01 10:13:00 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [cc-tweaked/CC-Tweaked](https://github.com/cc-tweaked/CC-Tweaked)@[8fe509ecb1...](https://github.com/cc-tweaked/CC-Tweaked/commit/8fe509ecb1a941d58a417a8da29e3de142a57328)
#### Saturday 2023-04-01 10:29:45 by Jonathan Coates

Properly scope IArguments to the current function call

This is a horrible commit: It's a breaking change in a pretty subtle
way, which means it won't be visible while updating. Fortunately I think
the only mod on 1.19.4 is Plethora, but other mods (Mek, Advanced
Peripherals) may be impacted when they update. Sorry!

For some motivation behind the original issue:

The default IArguments implementation (VarargArguments) lazily converts
Lua arguments to Java ones. This is mostly important when passing tables
to Java functions, as we can avoid the conversion entirely if the
function uses IArguments.getTableUnsafe.

However, this lazy conversion breaks down if IArguments is accessed on a
separate thread, as Lua values are not thread-safe. Thus we need to
perform this conversion before the cross-thread sharing occurs.

Now, ideally this would be an implementation detail and entirely
invisible to the user. One approach here would be to only perform this
lazy conversion for methods annotated with @LuaFunction(unsafe=true),
and have it be eager otherwise.

However, the peripheral API gets in the way here, as it means we can no
longer inspect the "actual" method being invoked. And so, alas, this
must leak into the public API.

TLDR: If you're getting weird errors about scope, add an
IArguments.escapes() call before sharing the arguments between threads.

Closes #1384

---
## [Burger1998/tgstation](https://github.com/Burger1998/tgstation)@[296ca23aa1...](https://github.com/Burger1998/tgstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Saturday 2023-04-01 10:54:29 by Jacquerel

Most actions cannot be used while incapacitated (#73513)

## About The Pull Request

Fixes #39775
The `TRAIT_INCAPACITATED` trait is intended to block you from acting but
does not inherently block actions. Actions only check for "conscious",
"has available hands", "immobile", or "lying down".
Most actions still _can't_ be used while incapacitated. This is because
most actions are spells, most spells have invocations, and you can't
talk while you are incapacitated. This is silly.

I have resolved this by adding a new flag which blocks actions while
incapacitated. This is somewhat redundant with "conscious" because most
sources of that also make you incapacitated but not _always_, you might
want the specificity.

I have tried to be discerning about where this flag is applied, it is
not in all cases (for instance you can still swallow implanted pills
while incapacitated and such), but it's not only possible but I can't
really avoid implementing this without it being a balance change in
_some_ cases,

Actions this effects are things such as:
Xenomorph Tail Sweep, Lesser Magic Missile (cult constucts), Heretic
Shadow Cloak, the Smoke spell in general, Conjuring (but not firing)
Infinite Guns, Mime spells

Times when these actions will no longer be available but were previously
are such times as when the mob is:
Stamina Crit, Stunned, Paralysis, and Time Stopped.

## Why It's Good For The Game

The incapacitated trait is applied by effects which should block acting
but still permits several actions which logically would be prevented.
This fortunately hasn't come up too often due to the high ratio of
actions with invocations, but it feels bad to stun someone and then have
them still able to perform an action they logically wouldn't be able to
take while stunned.
This is especially egregious in the case of Time Stop (the only way to
stun a lot of the mobs effected by this) but that's a rare pick on a
rare antagonist and would also rarely be used on these mobs, so a bit of
an edge case.

## Changelog

:cl:
fix: Many spell-like abilities which could be stunned, paralysed, or
frozen in time now cannot be.
/:cl:

---
## [joshSi/evals](https://github.com/joshSi/evals)@[ab5f7b2a89...](https://github.com/joshSi/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Saturday 2023-04-01 11:01:04 by oscar-king

Counting bigrams in sentences (#302)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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

- [x] I have filled out all required fields in the evals PR form
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
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [joshSi/evals](https://github.com/joshSi/evals)@[b5da073c21...](https://github.com/joshSi/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Saturday 2023-04-01 11:01:04 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

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

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [MobilizeDevTeam/odoo](https://github.com/MobilizeDevTeam/odoo)@[97f52bd40d...](https://github.com/MobilizeDevTeam/odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Saturday 2023-04-01 12:37:43 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

Part-of: odoo/odoo#109640

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[5a34d92cb5...](https://github.com/ianjoneill/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Saturday 2023-04-01 12:55:38 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[1e546815bb...](https://github.com/AOSP-Krypton/frameworks_base/commit/1e546815bbb736c50679a8aefc25f48561026fc5)
#### Saturday 2023-04-01 13:37:19 by Victoria Lease

Support RGBA fonts and bitmap fonts (and RGBA bitmap fonts)

Quite a few things going on in this commit:

- Enable bitmap strikes by default in Paint objects.

The SkPaint parameter that enables bitmap strikes was not previously
included in DEFAULT_PAINT_FLAGS. This effectively disabled bitmap
fonts. Oops! It's for the best, though, as additional work was needed
in Skia to make bitmap fonts work anyway.

- Complain if TEXTURE_BORDER_SIZE is not 1.

Our glyph cache code does not currently handle any value other than 1
here, including zero. I've added a little C preprocessor check to
prevent future engineers (including especially future-me) from
thinking that they can change this value without updating the related
code.

- Add GL_RGBA support to hwui's FontRenderer and friends

This also happened to involve some refactoring for convenience and
cleanliness.

Bug: 9577689
Change-Id: I0abd1e5a0d6623106247fb6421787e2c2f2ea19c

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[95b0e918c0...](https://github.com/KenAdeniji/WordEngineering/commit/95b0e918c09cff4ee38273bc904dcbdac40e5ed8)
#### Saturday 2023-04-01 14:27:30 by Ken Adeniji

2023-03-31T11:09:00 ... 2023-03-31T12:59:00
http://github.com/KenAdeniji/WordEngineering/blob/main/IIS/WordEngineering/Alameda%20County%20Health%20Agency%20Care%20Services%20Tri-City%20Community%20Support%20Center%20Behavioral%20Health%20Care%20Services/2023-03-31T1109Maureen.Orphanos@acgov.org_Abibat.Ajiboye@acgov.org_Atef.Shaikh@acgov.org.txt

Maureen	Orphanos
Behavioral Health Clinical Manager
Alameda County Health Agency Care Services Tri-City Community Support Center Behavioral Health Care Services
mailto:Maureen.Orphanos@acgov.org
(510) 795-2478
(925) 560-5888

Doctor Atef Shaikh
mailto:Atef.Shaikh@acgov.org
(510) 777-3846

Abibat Ajiboye
(510) 871-0043
(510) 795-2434
mailto:Abibat.Ajiboye@acgov.org

Alameda County Health Agency Care Services Tri-City Community Support Center Behavioral Health Care Services
39155 Liberty Street Suite G 710
Fremont, California (CA) 94538
United States of America (USA)
Telephone: (510) 795-2434
Fax: (510) 793-3972
mailto:webmaster@acbhcs.org

Kehinde Adewumi Adeniji
4762 Canvasback Common
Fremont, California (CA) 94555
(510) 796-8121
mailto:KenAdeniji@hotmail.com
http://KenAdeniji.WordPress.com

2023-03-31T07:00:00	I departed from 4762 Canvasback Common, I saw Jim Hough driving out.
2023-03-31T08:05:00	I arrived at 39155 Liberty Street Suite G 710.
2023-03-31T08:24:00	Among insects collaborating. Tasha Barajas arrived at work and she came into the lobby. She is wearing purple flowing dress, blue jeans trouser and high heels purple shoes.
2023-03-31T09:14:00	Don't cry, now. An Asian male patient came in.
2023-03-31T09:40:00	Doctor Atef Shaikh postponed his appointment to see his patient, Abdul, from yesterday to 2023-03-31T09:30:00. Abdul's wife explained that she was already in the car.
2023-03-31T09:40:00	Abibat Ajiboye is working from home, today.

2023-03-31T09:50:00	... 2023-03-31T10:20:00 Doctor Atef Shaikh visitation
Hi Ken, how are you doing?
How have you been, since we last spoke?
We started and stopped your medication.
Is this 5mg or 10mg?
Do you have the bottle with you?
You have a few medication could you tell me which one you are taking?
	Fluphenazine 5mg tablet.
Tell me a little bit about yourself?
Have you noticed a difference?
Can you share with me how you have been feeling?
How did you come to the appointment, today? I rode the bus.
And, where did you ride the bus from?
Are you getting through the day? And, what kind of thing you want to work on?
What can I do for you?
Do you feel content with your life?
To share your story with me.
Dani shared information about your brothers.
I will like to speak to your brothers to help better understand.
Would it be okay signing a release of information?
I am going to call your brothers.
Are you feeling tired in the morning?
We can continue with 2mg at bedtime.
The medication given to me is what I take.

2023-03-31T10:21:00 Susan Susoev. Her paternal line is Russian, and her maternal line is American Indian. Date of Birth (DOB) 1954-12-14. She is 68 years old.

---
## [mwatts/nushell](https://github.com/mwatts/nushell)@[0567407f85...](https://github.com/mwatts/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Saturday 2023-04-01 14:32:53 by Antoine Stevan

standard library: bring the tests into the main CI (#8525)

Should close one of the tasks in #8450.

# Description
> **Note**
> in order of appearance in the global diff

- 1b7497c41966306aa3103a95a9b5ef5df7111ee4 adds the `std-tests` job to
the CI which
  1. installs `nushell` in the runner
  2. run the `tests.nu` module
> see `open .github/workflows/ci.yml | get jobs.std-tests | to yaml`

-
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)
is where all the magic happens => see below
- :test_tube: 799c7eb7fd5f140289b36b9dbc00329c50e2fbda introduces some
bugs and failing test to see how the CI behaves => see how the [tests
failed](https://github.com/nushell/nushell/actions/runs/4460098237/jobs/7833018256)
as expected :x:
- :test_tube: and c3de1fafb5c5313e30c08c9ca57e09df33b61b74 reverts the
failing tests, i.e. the previous commit, leaving a standard library
whose tests all pass :tada: => see the [tests
passing](https://github.com/nushell/nushell/actions/runs/4460153434/jobs/7833110719?pr=8525#step:5:1)
now :heavy_check_mark:

## the changes to the runner
> see
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)

the issue with the previous runner was the following: the clever trick
of using `nu -c "use ...; test"` did print the errors when occuring but
they did not capture the true "failure", i.e. in all cases the
`$env.LAST_EXIT_CODE` was set to `0`, never stopping the CI when a test
failed :thinking:

i first tried to `try` / `catch` the error in
ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629 which kinda worked but only
throw a single error, the first one

i thought it was not the best and started thinking about a solution to
have a complete report of all failing tests, at once, to avoid running
the CI multiple times!

the easiest solution i found was the one i implemented in
9c12211564ca8ee90ed65ae45776dccb8f8e4ef1
> **Warning**
> this changes the structure of the runner quite a bit, but the `for`
loops where annoying to manipulate structured data and allow the runner
to draw a complete report...

now the runner does the following
- compute the list of all available tests in a table with the `file`,
`module` and `name` columns (first part of the pipe until `flatten` and
`rename`)
- run the tests one by one computing the new `pass` column
  - with a `log info`
- captures the failing ones => puts `true` in `pass` if the test passes,
`false` otherwise
- if at least one test has failed, throw a single error with the list of
failing tests

### hope you'll like it :relieved: 

# User-Facing Changes
```
$nothing
```

# Tests + Formatting
the standard tests now return a true error that will stop the CI

# After Submitting
```
$nothing
```

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[96d3651031...](https://github.com/KingDragoness/ProjectHypatios/commit/96d3651031b5205842cf110267721cb17667d24e)
#### Saturday 2023-04-01 15:59:08 by KingDragoness

Hypatios 1.4.6 b7 (Quality life updates, level changes, Fortima level)
DONE (April1)
• Some new texture changes for grid texture
• Mining Area balance changes
o There is a forgot-to-close level 4 mining
o Ramp now closed off
o Added doors which will be randomly placed/hidden within the rocks
 Door prefab has a rock so it’ll always be hidden
o Rope to teleport to level 1/sewer pipes
• New parameter for enemy: “AllowMultipleHitSameFrame”
o Prevents explosive damage stack
o Attacked() need manual implementation for this
• “Fortima_CreepController.cs”: controls creeps in Fortima level
o When all enemy assigned is killed, wait 60s cooldown
o Killing enemy will reward soul
o Spawn enemy (ex: 3 spiders, 1 sentinel); will automatically assign a list
• Fortima alternate path: Great Plains
o Path shortcut to the bunker/cliff region
• Fortima extension changes:
o Creep enemies (rogue alliance), when killed, gives souls
o Alternate path of cave with destructible rock/ores
• New enemy: Infernos
o Mainly for Fortima’s rogue creep enemies
o 3d model (zart customer, black)
o Inspired by Starcraft’s Archon
o Short range & cooldown quite long but high burning damage
• Redesign Zombie Chamber with Church Gothic style
o See CS_Source map
o Small church with big hall and the backside has interior with two floors
o Mosaic windows
o Zombie chamber is flawed gamemode, hide it in better place… (In Zart Sushi hide it in better place)
o Terrain with basement cellars <cancelled>
• 3d model: Chandelier and candles
• Zart changes
o Auto-dish also detects also in the Zart Bot Delivery so it doesn’t duplicate.
o Monitor tracks servo bot.
o Order monitor of “Interact_monitor” replace mesh with PC monitor attached to kitchen cabinet
o PC monitor two stages: NotStart and Start
 NotStart: the monitor will say “Open the Restaurant”
 Start: cycle order with text see how many orders
o Better Zart monitor UI, orange background
o Intro area sit wood material changes to orange
• Put FortWar_7 as alternate chamber
o Access through the Sewers
• Sewers changes
o Extension sewer area, move the final area door-gate away
• Chamber 7 shelved, becomes alternate chamber.
o Chamber 7 screws up the game’s tone. It is janky, poorly designed, not suitable for main chamber, too difficult and has a lot issues.
• Replaced Chamber 7: Fortima [MUST MAKE]
o DEADLINE: 20 April
o Prototype terrain and directional lighting
o Debug chest
o Using Fort War map scenario but styled like Dota map.
o 3 regions:
 Forest for creeps, minibosses and 1st CP.
 High Cliffs for 2nd CP, hard to take over due to verticality. Creeps and minibosses in here too.
 Final Base for final CP. Industrial warehouse building.
• Tutorial dialogue speeches
• Replace every reference to 7_FortWar to 7_Fortima.
• Base Fortima prototype layout
• Fortima sections:
o High Cliffs/Canyons: High vertical canyon, with wooden bridges. A lot of caves. Near the final base the CP.
o Final Base: Industrial warehouse building, need inspiration.
• New item: Zart Sushi
o 3d prop and consumables item

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[3ee549ca24...](https://github.com/AOSP-Krypton/frameworks_base/commit/3ee549ca2404067bb8b2fcbaa741ec118c76bf3e)
#### Saturday 2023-04-01 16:07:38 by Jeff Brown

Fix window manager policy state when waking from doze.

Once upon a time when the world was fresh and new, the heavens
had an easy rhythm.  Day and night.  Night and day.  In the day,
the pixel fairies would cavort and play in the bright gardens
with narry a mark of shadow or gloom.  In the night, they would
rest peacefully, dreaming no dreams and knowing no fear.

Then one night a fairy dreamed the first dream.  At first
the dream was peaceful, full of colors and delight, hopes and
memories.  Then all at once, jarringly, it awoke in bright
daylight.  The pixel fairy knew fear, for the world had changed
and it was unprepared.

Time passed and the pixel fairies grew accustomed to their
fate, day and night, night and day, sometimes dreaming, until
there came a night when a fairy did not sleep.  It roamed
the land in a dreamless doze, lost and afraid amid a grim haze
of grey and darkness.  The fairy despaired.  It wanted no
part of this place.  It pretended for a time to be awake but
the bright daylight would not come.  It pretended for a time to
be dreaming but the colors and memories would not come.
That is when the fairy wished for oblivion.  Then just as
suddenly, it awoke in the daylight.  It fell to the ground,
stunned as if it had forgotten how to walk in the too bright
daylight.

Though the world again grew softer and kinder in time, the pixel
fairies were never the same.  For the night is dark and full
of terrors.

---

It used to be easy.  Screen on and screen off could explain almost
everything about the state of the device but it's different now with
ambient display.  We need to be able to wait for all windows to be
drawn even in the case where the device is still nominally asleep.
In truth, the window manager policy which drives a lot of these
interactions is a thicket of outdated assumptions.

Added a new method to tell the window manager policy when the screen
is being turned off so that it can correctly account for changes
to the interactive state (wakeUp and goingToSleep) and screen state
(screenTurningOn and screenTurnedOff).  Now we can independently
poke keyguard during interactive state changes and we can apply
screen on blocking during screen state changes.

Moved the code which manages screen on blocking (which is what
ensures the UI has fully drawn before revealing screen contents)
from the power manager to the display manager since the display
manager is in a better position to accurately track the state of
the screen, particularly when the screen is being turned off.

Fixed a bunch of synchronization issues.  Previously some work
had been moved to a handler without considering what might
happen if it became reordered relative to other work happening
elsewhere.  Documented the desired behavior in the code to
prevent this from happening again.

There's still a bunch of stuff in here that isn't quite right,
particularly the assumption that there's only one screen, but
it's good enough for now.  Hopefully there aren't too many bugs.

Bug: 17605802
Change-Id: Ic7319e09948c8a3cda014d7e169c964a3ad86f14

---
## [SierraBay/SierraBay12](https://github.com/SierraBay/SierraBay12)@[e6362376cb...](https://github.com/SierraBay/SierraBay12/commit/e6362376cb2bc6cf95004b921aa1f4bc5ff5ccb5)
#### Saturday 2023-04-01 16:23:35 by gy1ta23

rifles!!!1


fixes descs


lathemags


oops i forgot a mag


holy shit hitting / is not that hard


Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[7265abe77a...](https://github.com/AOSP-Krypton/frameworks_base/commit/7265abe77a76f848a316640b5da106e882bdbc8a)
#### Saturday 2023-04-01 16:30:55 by Christopher Tate

Be increasingly aggressive about fstrim if it isn't being run

The current heuristics depend on devices being alive at midnight+ in
order to run periodic background fstrim operations.  This unfortunately
means that people who routinely turn their devices off overnight wind
up with their devices *never* running fstrim, and this causes major
performance and disk-life problems.

We now backstop this very-friendly schedule with an increasingly
aggressive one.  If the device goes a defined time without a background
fstrim, we then force the fstrim at the next reboot.  Once the
device hits the midnight+ idle fstrim request time, then we already
aggressively attempt to fstrim at the first available moment
thereafter, even if it's days/weeks later without a reboot.

'Available' here means charging + device idle.  If the device never
becomes idle then we can't do much without rendering an in-use device
inoperable for some number of minutes -- but we have no evidence of
devices ever failing to run fstrim due to this usage pattern.

A new Settings.Global element (type 'long', called
"fstrim_mandatory_interval") is the source of the backstop time.  If
this element is zero or negative, no mandatory boot-time fstrim will
ever be performed.  If the element is not supplied on a given device,
the default backstop is 3 days.

Adds a new string to display in the upgrading dialog when doing
the fstrim.  Note it is too late for this to be localized, but since
this operation can take a long time it is probably better to have
it show *something* even if not localized, rather than just sit there.

Bug 18486922

Change-Id: I5b265ca0a65570fb8931251aa1ac37b530635a2c

---
## [Hepno/BanPlugin](https://github.com/Hepno/BanPlugin)@[acf4e2fe76...](https://github.com/Hepno/BanPlugin/commit/acf4e2fe7604e0adf9bfd3d6c7e26948b87fbdc4)
#### Saturday 2023-04-01 16:31:26 by hepno

UP)HOYUIOPH(HUP)IUIPH FUCKING HELL KILL ME I HATE SQL SO FUCKING MUCH

---
## [Pariah919/TerraGov-Marine-Corps](https://github.com/Pariah919/TerraGov-Marine-Corps)@[1c696b710d...](https://github.com/Pariah919/TerraGov-Marine-Corps/commit/1c696b710d58c2adfc53be7fd49305ba45b8c23b)
#### Saturday 2023-04-01 17:01:58 by 567Turtle

adds the vali claymore (#12485)

* adds the vali claymore

nuff said

* adds sheath icon states

asgf

* Update code/game/objects/items/storage/holsters.dm

Co-authored-by: ivanmixo <ivanmixo@gmail.com>

* crazy

go fuck yourself

* go fuck yourself

* makes shit better

* autodoc

* autodoc (but it actually works this time)

* Update code/game/objects/items/weapons/twohanded.dm

---------

Co-authored-by: ivanmixo <ivanmixo@gmail.com>
Co-authored-by: TiviPlus <57223640+TiviPlus@users.noreply.github.com>

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[4e3c9ccc66...](https://github.com/LC4492/CM-Space-Station-13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Saturday 2023-04-01 17:19:30 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

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

:cl:
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[bde254000f...](https://github.com/LC4492/CM-Space-Station-13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Saturday 2023-04-01 17:19:30 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

:cl:

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0a1f7e8de2...](https://github.com/tgstation/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Saturday 2023-04-01 17:24:54 by Hatterhat

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
## [alwaysintreble/Archipelago](https://github.com/alwaysintreble/Archipelago)@[6d13dc4944...](https://github.com/alwaysintreble/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Saturday 2023-04-01 18:08:35 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [null15/Darkness-Reborn](https://github.com/null15/Darkness-Reborn)@[02c144c093...](https://github.com/null15/Darkness-Reborn/commit/02c144c093589d2ccc7132406e024e1429c93474)
#### Saturday 2023-04-01 19:26:56 by Elphea

v1.8.0

Vivpire rework (dreadlord)
FixedPhysPen
Added magicres to heroes
Hero wave now has proper magic res
Ranged Physical spells fixed (should no longer reflect from melee-specific return damage)
Pause system added to hopefully prevent awkward pausing behavior
Demonhunter R rework
Tinker can only build 1 gold/lumber preventing idiots/exploiters from fucking themselves
Dragon abilities fixed (only the proper dragon should use their ability!)
Fixed ice&fire sword recipe
Ice wand full recipe should be easier to see
Votekick refined (not sure if kicking works yet, no testing done)

---
## [MonaraMir/Citadel-Station-13-RP](https://github.com/MonaraMir/Citadel-Station-13-RP)@[8117b28946...](https://github.com/MonaraMir/Citadel-Station-13-RP/commit/8117b28946d2e07f902e8800245c34d008336ccc)
#### Saturday 2023-04-01 19:42:39 by nevimer

makes AI experience not fullbright and fixes AI runtiming because they receive a mirror implant (#5179)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![dreamseeker_sJwmVJw0Yp](https://user-images.githubusercontent.com/77420409/224618392-c9d94b76-05fa-456f-945c-784da7b962a3.png)

![dreamseeker_T7pXJJvDgH](https://user-images.githubusercontent.com/77420409/224618408-838a5156-91df-479f-ac48-4042692e887e.png)



## Why It's Good For The Game

Bug
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
fix: made AI's not see fullbright
balance: silicons don't become a traitor anymore on HUD UPDATES WHY
code: changes the call structure of cyborgs and moves life code down to
silicon level in some places, to make AI code work better.
fix: only human types are effected by mirror implants
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: silicons <2003111+silicons@users.noreply.github.com>
Co-authored-by: Lohikar <lohikar@protonmail.com>

---
## [AttorneyOnlineVidya/KFO-Server-AOV](https://github.com/AttorneyOnlineVidya/KFO-Server-AOV)@[0cc914a0a7...](https://github.com/AttorneyOnlineVidya/KFO-Server-AOV/commit/0cc914a0a7e9844fb5fe37ebb704cd70c40d10b4)
#### Saturday 2023-04-01 20:04:13 by yemta

GOD KFO IS THE FUCKING WORST

I FUCKING HATE THIS SNEAKING SHIT NO ONE CARES WHEN YOU MOVE AREA FUCK OFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[4864f8f493...](https://github.com/dsmith328/LC13Master/commit/4864f8f49310f8bd95df904d72a8ed31b9902844)
#### Saturday 2023-04-01 20:37:32 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

Visual indicator

minor fixes

Instability Tweaks

Paperwork Update

Anti-Self-Burn

Ending Update

Right view

A check that should be a non-issue but i'm making sure!

Breach Update and EGO update

More goo and FEMALE

Improvement and new Icons

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[e84ec312b8...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/e84ec312b8699fb50bfc13ad7384b1881c0ce397)
#### Saturday 2023-04-01 20:50:23 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[aba978827c...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/aba978827cbef816f16f98078525cab1195de750)
#### Saturday 2023-04-01 21:09:14 by SkyratBot

[MIRROR] Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone [MDB IGNORE] (#19834)

* Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!

![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.

![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

* Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[19678bf530...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/19678bf530361cd4c0dd45cbc6cdf51e93618adb)
#### Saturday 2023-04-01 21:24:02 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[899e8be032...](https://github.com/TaleStation/TaleStation/commit/899e8be032075e9dafe45d510eb1f228114aaae8)
#### Saturday 2023-04-01 21:28:24 by TaleStationBot

[MIRROR] [MDB IGNORE] March into Mapness: Meateor (#5163)

Original PR: https://github.com/tgstation/tgstation/pull/74070
-----
## About The Pull Request

Sometimes, as a funny pun, the station will be bombarded with chunks of
meat and organs from space. But where do these come from?
This space ruin doesn't answer this question, but it sure does raise
several more.

Watch here a video of an intrepid explorer taking steps inside for the
first time:
https://www.youtube.com/watch?v=5LwqyN7cutU

Alternately, here's some pictures:

<details>
  <summary>Images Within</summary>
  

![meateor_overview](https://user-images.githubusercontent.com/7483112/225979898-77e6e37d-3ada-42ed-a730-3b459fe3c459.png)
The preview looks ugly as hell because it isn't applying the material
datum yet, so here it is also in-game:

![image](https://user-images.githubusercontent.com/7483112/225979958-e478e984-5c03-43a7-b787-bd0698953738.png)

</details>

This ruin is largely based around a miniboss battle setpiece.
The meateor's beating organ doesn't really care that you're in there
unless you start attacking it, at which point it will attempt to impale
you with various forms of bony spikes.
Despite my performance in the video it only takes 15 shots to take down
so as long as you are a little bit light on your feet it isn't
_terribly_ dangerous.

The treasure contained in this ruin is unfortunately mostly contained in
the fleshy pods it wants to protect, and comes in the form of... organs.
And a handy organ-storage box so that you might plausibly be able to
have them back at the station to implant into people before they rot.

Because the meteor's internal area is made of meat you can of course eat
the walls if you are able to breathe in space without a mask or helmet.

Other present treasures:
- A dead miner, meaning a survival knife & mining voucher & healing
injector & potentially some credits
- A PKA, which is useful for exploring other space ruins
- A cosmetic neck item which looks like heretic gear in case you want to
implicate yourself
- A bottle of Tiger Cooperative ritual wine which contains stimulants
and... other things

To support my overambitious enemy design I refactored the Spawner
component slightly so that you can spawn any atom using it, rather than
just mobs. Seemed more sensible than making a separate, mostly identical
component.
Does the presence of 1400 lines of miniboss code make it more of a code
review PR than a map review one? You decide.

Additionally, someone in the comments pointed out the organ box didn't
have any coolant.
This revealed to me that the organ box didn't work.
I moved applying organ frozen flags onto the frozen component, and
ensured that the organ container will only freeze organs while it has
coolant in it.

### Mapping March

Ckey to receive rewards: becquerel
although frankly i don't expect to be redeeming it

## Why It's Good For The Game

More variety of things to find in space
Slightly increased variety of flesh-themed props which could be put in
other ruins if anyone else decides to make one made out of living tissue
for some reason
A teeny bit of lore which raises questions nobody was asking
The first Tiger Cooperative corpse in the game moving them slightly
further from just being words on your traitor uplink?

## Changelog

:cl:
add: A new meat-themed space ruin. 
fix: Organ box now actually requires coolant in order to work.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [michael-burke4/robot](https://github.com/michael-burke4/robot)@[3c6f05e4d3...](https://github.com/michael-burke4/robot/commit/3c6f05e4d306b9aab1f40b64a2579c70ac6d91a0)
#### Saturday 2023-04-01 21:50:41 by Michael Burke

some "working" obstacle avoidance, etc

does what its supposed to do, but poorly.

some weird behavior because the robot's world starts at 0, 0 but the start pos of the sim
is 50, 35. attempts to rectify this have resulted in kinda messy behavior.

need to use the z_angle rotation of the cube's pose in order to better reflect the obstacle
locations in the simulation.

pauses between all movements to 'give it some time to think'. Without doing this, things
tend to go awry. (placing all found cubes at [0, 0] for some reason?) The pauses mostly
resolve this

the conditions for the main loops in cozmo_planning are stupid but w/e its a quick fix

"just needs a bit of fine tuning!" 🙃👍

---
## [kraftingkage/testgithubstuff](https://github.com/kraftingkage/testgithubstuff)@[7dab4903d1...](https://github.com/kraftingkage/testgithubstuff/commit/7dab4903d139ede6796e8bfce2943caa157cdd9b)
#### Saturday 2023-04-01 22:03:51 by Dumptruck28

Fuck you

Suck my cock obama you black fucking nvm

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[d30f97f40f...](https://github.com/Buildstarted/linksfordevs/commit/d30f97f40fc6343ff6ddf4a1dad42bdc69bec125)
#### Saturday 2023-04-01 22:11:18 by Ben Dornis

Updating: 4/1/2023 10:00:00 PM

 1. Added: Bullsh*t Jobs
    (https://vadimkravcenko.com/shorts/bullshit-jobs/)
 2. Added: Name Constrain't on Chrome
    (https://alexsci.com/blog/name-non-constraint/)
 3. Added: The Joy of Computer History Books
    (https://fabiensanglard.net/joy/index.html)
 4. Added: Crushing the Myth of Late-Stage Capitalism | Tom Dehnel
    (https://tomdehnel.com/crushing-the-myth-of-late-stage-capitalism/)
 5. Added: Michael Tsai - Blog - HomePod Late Adopter
    (https://mjtsai.com/blog/2023/03/31/homepod-late-adopter/)
 6. Added: How to remember 100 digits of Pi, easily
    (https://rsapkf.org/weblog/pi-digits)
 7. Added: Notion as a replacement for Pocket — Javorové lístky
    (https://honzajavorek.cz/blog/notion-as-a-replacement-for-pocket/)
 8. Added: Releasing mac-bootstrap
    (https://paika.tech/blog/2023/04/01/releasing-macbootstrap.html)
 9. Added: Evaluating the Expense of OpenAI Whisper: API or Self-Hosted? - Nikolas' Blog
    (https://nikolas.blog/whisper-api-vs-self-hosting/)
10. Added: I Didn't Read 17 Books So You Don't Have To 😩
    (https://www.wysr.xyz/p/i-didnt-read-17-books-so-you-dont)
11. Added: Extending Structural Functions to Scalars
    (https://www.dyalog.com/blog/2023/04/extending-structural-functions-to-scalars/)
12. Added: Coding Adventure: Ray Tracing
    (https://youtube.com/watch?v=Qz0KTGYJtUk)
13. Added: The case for native handling of Fediverse actions | Jeremy Herve
    (https://jeremy.hu/the-case-for-native-handling-of-fediverse-actions/)

Generation took: 00:11:07.2912938

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[27d37cb0f4...](https://github.com/Kapu1178/daedalusdock/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Saturday 2023-04-01 23:17:50 by Gallyus

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
## [bscottm/emuwork](https://github.com/bscottm/emuwork)@[c0611673c7...](https://github.com/bscottm/emuwork/commit/c0611673c711e5ce6050afdc7ed5bd004f96bb3b)
#### Saturday 2023-04-01 23:20:21 by B. Scott Michel

Consolidated 2012/2013 commit

- Refactored how emulator-specific command dispatch is done, because the
  original approach did not work.

  Note that if the Machine.EmulatedProcessor record ever changes, the
  destructuring in Main.hs has to be updated. But this'll be really
  obvious... but dynamic dispatch does appear to work.

  Also added Machine.NullProcessor just for testing purposes, which is how
  I discovered that the type class way of doing emulator-specific command
  line dispatching didn't work.

  Converted files over to Unix line termination...
- Initial disassembler capability.
- Made disassembler output look more like a disassembly, rather than
  spewed Haskell types.
- Heavily polymorphic types in Machine.DisassemblerTypes to implement a
  reasonably generic interface to disassemblers.
- Started support for pseudo-ops, e.g., assember directives, for more
  robust data-driven disassembly.
- Added symbolic labels for DJNZ and JR (relative jumps), plus an initial
  symbol table for the TRS-80 ROM disassembly.
- More cool TRS-80 level II ROM disassembly hacks. Outputs strings, byte
  sequences, ...
- A little frobbing to unify how Z80 operands are represented, prefer
  Data.ByteString.Lazy.Char8 and more 0xed-prefixed instructions.
- DD and FD prefix instructions can disassemble, except for DDCB and FDCB,
  which are a little weird. Implemented a few more pseudo instructions.
- Added a Z80 disassembler primitive that outputs a byte expression for
  characters with the high bit set. Useful for reading the BASIC
  interpreter's verb table, where the first character of each verb has the
  high bit set.

  Also added a jump table generator, which requires a lot less typing for
  diassembler guidance.
- Use type families to provide better abstraction for disassemblers.
- Avoid recompiling the world+dog, use the library to link the executables
  from within the same cabal file. This requires that all of the code
  required to link is actually present in the library...
- Discovered a few new pieces of TRS-80 ROM functionality, including
  single precision floating point constants. Separated out the known
  symbols and disassembler guidance code to simplify structure.
- Add more known symbols based on Ira Goldklang's TRS-80 pages.
- Be more Haskell-idiomatic in highbitTable, use existing functions and
  combinators for better data flow.
- Added a memory address continuity check after disassembly is finished so
  that obvious disassembly guidance issues can be sanity checked.
- Combined the exchange instructions into a single data type and
  associated operand.
- Promote several of the Z80 pseudo-instructions to DisasemblerTypes
  types -- these are commonly used pseudo instructions that ought to
  generalize across different processors and systems.

  Added an post-decoded-instruction function to the disassemble
  type class function in order to filter and adapt to specific situations.
- One interesting situation is the 'RST 08' instruction's usage in the
  TRS-80 ROM. RST 08 is followed by a byte, which should be automatically
  decoded as an ASCII character or ByteRange pseudo-operation.
- Use Data.Text instead of Data.ByteString
- Compute MD5 hash on the ROM, prepend to the disassembly output.
- Use Parsec to parse and read Intel hex-format files.
- Add System-80 blue label ROM to the collection.
- Move Z80's instruction decoder out of the disassembler, make it a
  function callable through the EmulatedSystem data type.
- z80AnalyticDisassembly: Make a single pass through Seq Z80disassembly
  to fix up absolute -> symbolic translation. This also necessitated
  adding line labels to some of the generic disassembly sequence data
  constructors, all of which are initially Text.empty.
- Create shorthand "mk" functions for creating new disassembler types and
  avoiding the overhead of remembering that the address label is initially
  blank.
- Unified the operands to a single LD instruction, which is used for both
  loads and stores.
- Use SYB for fixing up symbols and disassembly element address labels.
  This increases the garbage collection rate, until I can figure out a way
  to make this work with uniplate (note: uniplate works on complete
  expressions of a type constructor, which is not amenable to the data up
  which the fixups operate.)
- Create a new trs80 directory hierarchy, which organizes TRS80-specific
  data better.
- First commit of the Misosys EDAS-compatible assembly language parser.
- Make everything we parse "optional"; simply collect everything that
  occurs on the input line into an AsmStmt. And make it work with the fact
  that labels mostly end with a ':' followed optionally by an instruction.
- Found a subtle bug in the instruction decoder: the decoder dispatch
  function was checking the current opcode, opc, whereas the dispatch
  function should have an opcode as a parameter because the program
  counter is incremented when dealing with index-prefixed instructions.

  Also found that data constructors HLIndirect, IXIndirect and IYindirect
  are not used, removed them.
- More EDAS hacking: the "ORG" directive will set the assembler's
  program counter; added a byte vector the AsmStmt to support
  code generation; source location added to the Var data ctor
  just in case we're ever interested in actual diagnostic output.
- Fully implement the 'DB' (also known as 'DEFB', 'DM' and 'DEFM') pseudo
  operation, with test cases. Also make exressions understand a single
  quoted character, e.g., 'c'.
- And implement the 'DC' (define constant fill/block). One pseudo
  instruction per day is all we ask...
- Define space pseudo operation implemented (trivial). Added initial
  framework for 'dw', 'date' and 'time'. Date and time will be based
  on when the assembler pass starts, although, this could be done at
  the time the pseudo-ops are actually encountered (probably doesn't
  make much of a difference.)
- Implement the 'DW'/'DEFW' pseudo operation.
- Pollute edasAssemble, the assembler pass, with the IO monad because
  getCurrentTime needs to insert the current time into the assembler's
  intermediate state. Yucky, but needs to be done to implement the
  'Date' and 'Time' pseudo operations.

  At least the IO monad pollution is limited to one function, despite
  extensive changes to the way the test harness works (formerly pure
  functions now lift into the IO monad.)

  Fixed up formatting/alignments in the test harness.
- Pseudo-operations: "DATE", "TIME", "DSYM" and "DX"
- Add the 'DEFL' pseudo-operation, which allows re-assigning statement
  labels during assembly. Note that this will need a FIXME when binary
  code is emitted, since the test case changes the origin several times,
  necessitating sorting the statement addresses.

  Separated the equates from statement (symbol) labels from the defined
  labels via DEFL.

  Found and fixed a parser bug when collecting a comment after an
  expression. Also simplified the way that expressions are parsed.

  A single '$' will return the current assembler program counter's value.
- Implement the 'END' and 'ENTRY' pseudo-operations.
- Functions are starting to get huge. Refactor them into smaller hunks,
  each in their own source file.
- Added some of the initial bits required for conditional assembly,
  although this now complicates the lens generation -- AsmOp now needs
  to be part of the Data.Monoid.Monoid type class. AsmOp has a new
  data constructor, AsmSeq, for sequences of assembler operations.
  However, this data constructor is unused and the Monoid type class'
  functions appear to never be invoked.
- Parsing conditional assembly for 'IF <cond>' works. Test cases
  for whether the actual assembly stage need to be done.
- Comment out the re-export of Z80.ParseAnalytic for the time being to
  reduce ghc warning messages.
- Duplicate statement labels and equate labels are errors, but that
  means propagating through the Either (pun intended.)
- Ensure that the execution start address is actually set or an 'END'
  pseudo-op was actually encountered. Otherwise, the assembler fails.
- Make constant parsers more robust. Not efficient, but robust.
- Started an AsmStmt pretty printer.
- Statement labels on conditionals are inserted into the assembler's
  symbol table. Why one would want to do this is questionable,
  especially putting a statement lable on an 'else', but it is
  supported.
- Pretty printer does something useful! (Actually, right now, it's not a
  big stretch to generate the assembler listing. The only problem is
  preserving the whitespace formatting of inline [as opposed to
  statement-ending] comments.)
- Add a line prefix to each output line to more readily identify
  conditional assembly actually assembled code.
- Parse the other conditional assembly statements: ifeq, iflt,
  ifgt and ifne (as well as their string comparing versions)

---
## [bscottm/emuwork](https://github.com/bscottm/emuwork)@[16c3a57c37...](https://github.com/bscottm/emuwork/commit/16c3a57c376afe3028925a07226a35a18801288b)
#### Saturday 2023-04-01 23:20:21 by B. Scott Michel

Consolidated 2016 commit.

- Restart hacking after a long pause.  Control.Lens changed reasonably
  significantly, so most of the effort to get this work again was actually
  tracking down what changed in Control.Lens and what it changed to.
- Use YAML instead of data structures.
- Refactored the TRS-80 ROM disassembler. Started working on YAML guidance
  file reading.
- Somewhat better solution to reading YAML-ized symbol equates.
  Scaffolding for YAML tests in place.
- Keep a copy of the EDAS (Editor Assembler) manual around for TRS-80.
- Use the 'Either' type instead of 'Maybe' to simplify logic. 'Maybe'
  leads to twisted morasses of strange constructs.
- More guidance directives work. Made the address+length keys consistent
  across the disasm, bytes, ascii, hightable and jumptable directives.
- Move the error handling case so that errors propagate quickly.
- Create TRS-80 Model I constructors for RAM of the various sizes.
- Make the TRS-80 disassembler more general purpose (eventually), but at
  least make the annotated ROM disassembler part of the command driver.
- Change all memory operations (fetch, fetch many [mFetch, mFetchN]) into
  a type class. This completely "unjacks" nasty issues and generalizes
  nicely.
- Replace the magic "IsnnDecodeF" type with a type class specific to
  processor operations. This type class will expand in the future.
- Clean up: This source code is no longer needed. Entirely handled by
  'emuwork --system=trs80-model-i disasm <option>'
- Added the Level II ROM book, consolidated code for Z80's idecode
  instance function.
- Move command argument process so that the disassembler can parse its own
  command line options, separately from the common options. Preparation
  for adding guidance files to the command line.
- Put types into their own source file. Doesn't fix the orphaned instance
  in TRS80.hs. Not sure it can be fixed without circular dependencies.
- Revamp the Guidance structure into guidance and sections of
  directives. Individual sections customize the disassembly process, where
  all of the common "stuff" (origin, end address) is kept at the top level
  guidance dictionary:

  ---
  origin: 0x0000
  end:    0x2fff

  TRS-80 Model I Level II:
  - comment: this is a comment
  - equate:
      value: 0x4014
      name:  Frobotnotz
  ...
- i[xy]h/i[xy]l undocumented instructions.

  Need to write a test for I[XY]h, I[XY]l as 8-bit register operands, but
  those undocumented instructions are now handled.
- Relax constraints on ProgramCounter, RelativePC. This adds constraint
  overhead elsewhere, but makes for somewhat cleaner code.
- Simplify asHex so that there's less String<>Data.Text conversion.
- Remove constraints from ProgramCounter and RelativePC, which creates
  constraint madness on type classes. Fortunately, this makes
  ProgramCounter and RelativePC more flexible.

  signExtend is written more portably.
- Move Machine.ProgramCounter to its own module. Makes
  Machine.EmulatedSystem more readable.
- Completely rethink the MemorySystem type. It's now a container for
  non-overlapping regions stored in an IntervalMap (should really enforce
  this, but theoretically...) Regions can be read-only for ROM.  Really
  simplifies the memory system type because it's now far less abstract.
  Eliminates the MemoryOps type class too, which was a source of
  headaches. Should also make adding memory-mapped devices more
  straightforward when I get there.
- Eliminate the EmulatorDriver class, relocate it into emuwork's Main
  module. Reduces the orphan class instance problem.
- Added strictness and unpack pragmas in various places to reduce
  potential space leaks (not sure they'll happen, but you never know.)

  Started code for memory writes, using a priority queue to implement a
  LRU cache. This amortizes the penalty incurred while updating the
  underlying vector's contents with a bulk update when the write queue's
  size is exceeded (29 elements, yes, a prime number.)
- Sliding window test
  - mReadN: Consolidate gaurds
  - msystest: Add sliding window for mReadN testing over gaps,
    basic/preliminary mWrite tests.
- Use Test.Framework

  Convert the unit tests into a combination of QuickCheck2 property and
  HUnit unit tests. Simplifies the test harness driver as well.
- Sequentially write large numbers of values into memory, read them
  back, see if they match the expected pattern. Check.

  Next: Use random address/value pairs.

- Added the '_nWritesPending' field to MemoryRegion to avoid the O(n)
  penalty with calling OrdPSQ.size. Added sanity checks during testing to
  ensure that accouting is correct.
- Added random write testing and ensure that there are enough writes to
  cause the LRU to flush. Found an interesting bug when the same address
  is written twice (and fixed).
- Added device memory regions to MemoryRegion and MemorySystem. Not
  complete functionality yet -- need a rethink on how track device state
  when invoking mRead/mReadN.
- Simplify ProgramCounter: Turn it into a newtype, remove PCOperation
  class, remove RelativePC.
- mRead/mReadN/mWrite/mWriteN/mPatch for devices as part of the
  MemorySystem, with associated test cases.

  Note: I/O ports are considered a separate memory system, which makes
  reusing this code straightforward with type aliases.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e1221c986f...](https://github.com/tgstation/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Saturday 2023-04-01 23:25:35 by san7890

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
## [TheLastGimbus/FreeBuddy](https://github.com/TheLastGimbus/FreeBuddy)@[5742b5fff4...](https://github.com/TheLastGimbus/FreeBuddy/commit/5742b5fff4171a56b943912aff3fdf9c5dca93ea)
#### Saturday 2023-04-01 23:49:08 by TheLastGimbus

bump all dependencies

ohh gradle..

fuck you soooo much :)

---
## [expectedbehavior/common-files](https://github.com/expectedbehavior/common-files)@[eb54393f96...](https://github.com/expectedbehavior/common-files/commit/eb54393f966124e834e0072bd4223513e27db2ec)
#### Saturday 2023-04-01 23:53:28 by Matthew Gordon

Add a function to communicate with chatgpt on the command line

Why is this change needed?
--------------------------
It's an experiment in accelerating development with the convenient use
of generative AI. There are currently LOTS of articles about it. This
implementation is based on this article: https://kadekillary.work/posts/1000x-eng/

How does it address the issue?
------------------------------
It adds a bash function, ask_chatgpt, that takes a prompt in the same
way chatgpt would in the browser. I also aliased it to "h". I'm not
sure I think that's the best alias, but it works for now.

I don't actually expect this function to be all that useful by
itself. I think a key feature of chatgpt is that it remembers what
you're talking to it about, so you can make modifications and
adjustments. That doesn't happen using this command line
interface. However, I expect it will be a lot easier to automate
things and provide large bodies of input to chatgpt over command
line. Maybe even setting large bodies of context before asking a question.

Per discussion about making the common files more development
friendly, I added a line to the top of bashrc that sources all the
bash files in a directory. The directory is hardcoded right now in a
way that's probably not going to work for other people, but I had to
stop shaving at some point.

Anyway, the idea is that ALL function extension for bash will be done
in files in that directory[1].

Any links to any relevant tickets, articles or other resources?
---------------------------------------------------------------
1 - https://3.basecamp.com/3093825/buckets/28354346/messages/5105707052#__recording_5163658670

---

