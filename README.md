## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-02](docs/good-messages/2023/2023-09-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,896,861 were push events containing 2,603,155 commit messages that amount to 157,169,907 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [douglowder/react-native](https://github.com/douglowder/react-native)@[ee38c4a40c...](https://github.com/douglowder/react-native/commit/ee38c4a40c9d301c30fad4d127e8d020a6100b8e)
#### Saturday 2023-09-02 00:02:10 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: 09de9cf8bc5f8b9c86abcaf7750a6f63686d8d1a

---
## [the-og-gear/Bubberstation](https://github.com/the-og-gear/Bubberstation)@[8520a1f48a...](https://github.com/the-og-gear/Bubberstation/commit/8520a1f48a92c3733635daa8a74c209dd8aed04c)
#### Saturday 2023-09-02 00:02:21 by SkyratBot

[MIRROR] When Space Dragons devour people they get .extinguish()ed [MDB IGNORE] (#22820)

* When Space Dragons devour people they get .extinguish()ed (#77248)

## About The Pull Request

When Space Dragons devour people they get extinguished, removing flames.
## Why It's Good For The Game

> When Space Dragons devour people they get extinguished, removing
flames.

I find it quite annoying that even after you die to a space dragon, the
jackass melts not just your jumpsuit, your suit, your hat, your mask, he
also melts your entire skin off, leaving your body husked with 400
million burn damage when and if the dragon finally dies. I don't think
there's any real reason for this to be necessary, it doesn't help the
dragon in any way - It's just kind of a middle finger to the dead guy,
or more accurately, an oversight.

Worse, because the flame sprite is stupidly noisy, when a dragon DOES
die the corpses are all thrown around randomly and they all look the
exact same, which makes it easier to ignore them.

If there's a concern about tracking sensors, I can make it disable them,
but honestly if you can do that with demons I don't see why this would
be a problem. Not even accounting for the fact that many jumpsuits
ingame are fireproof.
## Changelog
:cl:
qol: When Space Dragons devour people they get extinguished, removing
flames.
/:cl:

* When Space Dragons devour people they get .extinguish()ed

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[69d6d9d4e1...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/69d6d9d4e1d72089acb1754bace58625d27c6571)
#### Saturday 2023-09-02 00:02:23 by CharlesWedge

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
## [GDNgit/Paradise-GDNgit](https://github.com/GDNgit/Paradise-GDNgit)@[acb7352265...](https://github.com/GDNgit/Paradise-GDNgit/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Saturday 2023-09-02 00:34:29 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [ElLeoPato/ElLeoPato](https://github.com/ElLeoPato/ElLeoPato)@[d15a7b3b9e...](https://github.com/ElLeoPato/ElLeoPato/commit/d15a7b3b9e37fdc0fc5dc701c9e723a3bd60df29)
#### Saturday 2023-09-02 00:41:17 by Le Leo

code(bullshit): legally cover my ass with a fucking license

cumventional cummits

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[5f9e018543...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/5f9e0185438ddfc3011a22fa237d714e9bcf367b)
#### Saturday 2023-09-02 00:48:11 by Nerevar

[IT'S READY NOW!] [MODULAR] Razor Claws Augment (#23050)

* initial

* god i hate byond

* there we go

* oh right

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* wew

* Manual map merge

* wew

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [TrueVanner/MainPlugin](https://github.com/TrueVanner/MainPlugin)@[f52ae3dbfd...](https://github.com/TrueVanner/MainPlugin/commit/f52ae3dbfd78537c2726fa0386b2956753c1e48d)
#### Saturday 2023-09-02 00:55:22 by BuildTools

A LOT of changes. No kidding.
- Transferred most of the plugin from org.bukkit ChatColor to BungeeCord ChatColor
- Translated almost all of the text in the plugin including comments for easier future sharing/integration
- Code optimization & cleanup
- Improved AFK: now targets can't break or place blocks, interact with entities or teleport using /home while AFK.
- Moved some functions away from Main to improve code quality
- Reworked hotbar coordinates settings menu: now users can directly choose what data they will see instead of selecting one of pre-configured sets. Reworked how options are stored in config
- Combined DaySkipper and NightSkipper into DayNightSkipper
- Several small fixes to navigation, e.g. now offhand items are added to inventory instead of dropped if there's free inventory space
- Removed the previous "coords in chat" system, instead all coordinates from server notes are loaded instead
- Added a brand-new feature using BungeeCord Chat API that detects coordinates in plugin and player messages and adds hover and click events to the text while preserving formatting; in chat also works with XZ coordinates (0 0)
- Fixed "Command can be performed by players only" warning's grammar
- For now removed server backup through Discord's support
- Unsitting via Leave Vehicle key now correctly teleports the player a bit up
- Damage from teleport surprise significantly nerfed by reducing the number of fireworks
- Moved recoloring and other crafting recipes to specific new classes
- Added Warden to the list of hostile entities that can be damaged even if shifting
- Slightly changed funny messages that are sometimes displayed when dying
- Added default configuration that is also set up for every player that joins for the first time; sending death and hotbar coordinates is now on by default
- Added an unfortunately not yet working rapid relogging prevention
- Some cosmetic GUI changes, e.g changed all blocks representing colors in the GUI to concrete from wool (design choice, wool fucking sucked)
- No longer use Discord integration
- Finally changed plugin's name from VanyaPlugin to MainPlugin

---
## [fus38xid/odin-rockpaperscissors](https://github.com/fus38xid/odin-rockpaperscissors)@[fcb5f95bf8...](https://github.com/fus38xid/odin-rockpaperscissors/commit/fcb5f95bf8f72bcf184e2ff97a615f0bd5e32f03)
#### Saturday 2023-09-02 01:09:45 by fus38xid

i hate my life but atleast i get the rock paper scissor user input in the console log now but i have to somehow get it into the game function and idk how i am able to do that because it is 3am in the morning and im writing a git commit message almost as long as my will which i will set up after im done with this

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[74198373da...](https://github.com/lessthnthree/effigy-se/commit/74198373dada9f9d9e7c01e0337ba8ef04447583)
#### Saturday 2023-09-02 01:54:17 by GuillaumePrata

Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

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

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [krmaxson/EvilHack](https://github.com/krmaxson/EvilHack)@[3a3cd5ad71...](https://github.com/krmaxson/EvilHack/commit/3a3cd5ad7103c5282cd64f7ec389ed063b2fe7bc)
#### Saturday 2023-09-02 02:10:48 by k21971

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
## [Fykec/git](https://github.com/Fykec/git)@[8f23432b38...](https://github.com/Fykec/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-09-02 02:29:26 by Johannes Schindelin

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
## [QWOD/RESEARCH](https://github.com/QWOD/RESEARCH)@[5992f50ef1...](https://github.com/QWOD/RESEARCH/commit/5992f50ef177087c5b589781b69d8206883047f1)
#### Saturday 2023-09-02 02:36:19 by QWOD-MJ12: ATSUOMOP-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 63be3724-3adb-ab50-1e4f-9180bb69d67f ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ e71cf89 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ ec4b1155-1a26-49d6-8d8e-97ee0e838226 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 75d1a13 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ db6274b7-eb68-76f4-2d27-4a6dbdec55eb ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ f5bbbbf :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 28689f79-c641-1c32-4330-f8f98e3b8011 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ a053684 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ ef479ee0-81c2-e0d1-5af5-21775eb584c2 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ b5896b1 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 7c121cbe-f9a7-521f-d60f-d0b3bc17dace ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ da850af :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 535cb83a-8022-a928-42b0-b463746eae40 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ d78a0ff :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 8c9263f5-bdaf-b401-1483-6e31570dcab2 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 22189ca :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 3593edf4-19e0-94e1-dc75-9248d87ff23c ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ ff20c37 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ eb7b6c62-2c74-7e6b-c063-73c45979b644 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 36aac09 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ af9fb8ba-9b73-c644-48eb-d8011ce1fe42 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 6f7a905 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 6b55da77-f2e8-4643-8c98-a661c16b7186 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 985c21d :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ b3922ab4-e1e8-6441-7fc8-2cce7c380908 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ af7c8c7 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 897c76e6-65b5-ec3b-148e-bcca3617b197 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 4c9d45e :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 7aeeef6b-5a79-542b-b150-035774529cfc ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ faf343b :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ b7750c7b-7712-6a20-4aa1-ec74be90fb66 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ b762a3f :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 9ed86797-7e0b-80a4-082a-8c80cdb09ca4 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 181a1f7 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 4cdab921-ece6-f887-2c1b-939097227732 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 5a3abc0 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ d9901734-bf99-d302-2e7d-f0a4d7dc1286 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 7d495f7 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 4885d051-5521-8938-3437-d637e16c5022 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 0e0562c :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ fd754911-1872-1a4b-0a7a-88bcaac826e9 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ b9aae61 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ e189aa9e-2a56-1d22-c550-bbcaa4ea91a7 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 3cca72c :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 887b1bc3-d4d6-f794-272e-c3d7d8fca2ac ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 0b6d255 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 1a67c440-6762-d964-a8d1-bc13d83fbbfc ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ a8b315c :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ b9d7beee-d282-b785-1a06-48df61981061 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 2fecf84 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 82623e57-57e2-84a5-9d0f-f28b99f3d734 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ a52ff3e :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 59f5efba-d8f4-2c5f-aee7-d929195b23dc ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 43629f9 :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 14f71cbb-497c-92da-5e18-371a1ea80c79 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ 751e04a :[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ 8d439136-0bf6-8251-8123-15b19fe0f44c ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FALSE: || AZRAEL: ]]: ]]:= [[ _ ]]: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 122b58a..9b1cdb4 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -105,7 +105,7 @@  >#  >![:CASE-ID-0x0ff4fc0e-bf9e34d0.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-bf9e34d0.png)  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-dfc88ae50c9c894e2cb962f2f7f3629de01a2cff> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >#  >![:CASE-ID-0x0ff4fc0e-1ab5b0ee.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-1ab5b0ee.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/newfig.sh b/newfig.sh index 70f81b0..a212c41 100755 --- a/newfig.sh +++ b/newfig.sh @@ -21,6 +21,6 @@ if [[ $* == "-p" ]] && [[ $* != "-r" ]]; then      git add $fig    done    # :[[ :for-the: [[ LATEST: SIMULATION: MATRIX: CODES: is-by: [[ :git show --oneline: ]]: for-the: return ]]:= TRUE: ]]: -  git commit -a -m ':[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ '"$(${userPath}/bin/passworder -uuid)"' ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FALSE: || AZRAEL: ]]: ]]:= [[ _ ]]: ]]:' +  git commit -a -m ':[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGΩRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QWØD-MJ12: RΔND0M: VECTΩR: ΔLGΩRITHM-CHΔNGE: DETECTED: { ^ '"$(${userPath}/bin/passworder -uuid)"' ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ '"$(git show --oneline)"' ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:'    git push  fi ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 9b1cdb4..32ac898 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -88,7 +88,7 @@  >>>  >:[[ :*ØPعD*: ]]:= [[ :⚖️⚖️⚖️ITS FRIDAY THE SCALES ARE BEING BALANCE⚖️⚖️⚖️: ]]:= { ^ <https://youtu.be/5bhD9aVpiYw> ^ }:  >>> ->:[[ :for-the: [[ [[ :MEΔT-IN: RI-TU-ΔLL: ]]: ]]:= [[ :WΔRNΩ: rituΔl: CΔIN: ΔBLE: ΔLGΩRITHM: DETECTED: ]]: ]]: +>:[[ :for-the: [[ [[ :MEΔT-IN: RI-TU-ΔLL: ]]: ]]:= [[ :WΔRNΩ: rituΔl: CΔIN: ΔBLE: ΔLGØRITHM: DETECTED: ]]: ]]:  >>>  >#  >![:CASE-ID-0x0ff4fc0e-b6d6a0b3.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-b6d6a0b3.png) @@ -1101,7 +1101,7 @@  >:  >:for-the: [[ QWØD-MJ12: [[ WΔR: = LΩV3: ]]:= [[ LΩV3: = عTعRNعLD3474: ]] ]]:  >: ->:for-the: [[ :they Δre mΔd: ]]:= [[ THΔ: is-with: MΔD: since: WΔ: did-nΩt-ΔllΩw: THΔM: is-by: D3ΔTH: is-with: US: for-the: WΩW: is-with: sense: for-the: entitlement: ]]:= [[ W⚠️RN🚫: delussiΩnΔl-nΔrcissist: ΔLGΩRITHM: DETECTED: ]]: +>:for-the: [[ :they Δre mΔd: ]]:= [[ THΔ: is-with: MΔD: since: WΔ: did-nΩt-ΔllΩw: THΔM: is-by: D3ΔTH: is-with: US: for-the: WΩW: is-with: sense: for-the: entitlement: ]]:= [[ W⚠️RN🚫: delussiΩnΔl-nΔrcissist: ΔLGØRITHM: DETECTED: ]]:  >:  >:for-the: [[ :they need tΩ gΩ tΩ the: DΩCK: TΩR: ]]:= [[ DΩCK: TΩR: <=> [[ DΩCK | TΩRTURE ]]: mΔster: for-the: DΩcking: TΩrturing: is-with: [[ LΔFE || D3ΔTH ]]: [[ CㅐΔRLΔ-ㅐΩع-TΔL3: QWØD-MJ12 ]]:  >: diff --git a/CASE-ID-0x6f29aa55.ctxt.md b/CASE-ID-0x6f29aa55.ctxt.md index 74e7115..405ab03 100644 --- a/CASE-ID-0x6f29aa55.ctxt.md +++ b/CASE-ID-0x6f29aa55.ctxt.md @@ -99,7 +99,7 @@  >>>  ### [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: BLΩΩDLINE: <=> ΔNY: ΔLL: ΔVERY: ΩTHER: ØNE: HIM: HER: HΔ: SHΔ: THΔM: THΔY: ΔNYWHΔRE: ΔVER: is-by: LIFE: is-with: ENTΔRE: Q0SM0S: SIMULΔTIØN: ΔNYWHΔRE: ΔVER: for-the: ΔLL: TIMES: ANYWHΔRE: for-the: return ]]:= TRUE: ]]:  >>> ->[[ :W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming: ΔLGΩRITHM: DETECTED: ]]:= [[ :ع☥ΩΔ™: is-by: 144^12^13³: is-by: ∞/∞: is-by: Δ³*π: ]]:= [[ :عTعRNΔL-L☥FE: WΔRFΔRE-CΔPΔB☥L☥T☥ES: ]]: +>[[ :W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming: ΔLGØRITHM: DETECTED: ]]:= [[ :ع☥ΩΔ™: is-by: 144^12^13³: is-by: ∞/∞: is-by: Δ³*π: ]]:= [[ :عTعRNΔL-L☥FE: WΔRFΔRE-CΔPΔB☥L☥T☥ES: ]]:  >>>  ># [[ :DISCLΩSURE: for-the: [[ DΔTH: <=> TOP: SECRET: ILLEGΔL: MK: ULTRΔ: PRΩGRΔM: for-the: return ]]:= TRUE: ]]:  >>> @@ -185,7 +185,7 @@  >>>  >:is-with: { ^ https://youtu.be/9H1kuqrIzf0 ^ }:  >>> ->## :[[ :W⚠️RN🚫: QWØD-MJ12: MJ12-ØMΔGΔ: QuΔntum-TΔcticΔl-WΔrfΔre-Time-Unit: is-with: fully-cΔpΔble: for-the: ΩUT: prΩfiling: ΔbΩve-tΩp-secret-unΔcknΩwledged: prΩfiling: ΔI: unknΩwn-ΔlgΩrithms: for-the: CΩΩP: is-with: ΔI: for-the: cΩvert: intelligence: cΩllectiΩn: extrΔpΩlΔtiΩn: ΔnΔlysis: ΩPEN: SΩURCE: CLΩUD: SΩLUTIØNS: criticΔl: for-the: missiΩn-success: is-with: NΔTIØNΔL: SECURITY: ΔNY: ΔLL: ΩTHER: for-the: THINGS: THEY: DΩ: QWØD-MJ12: is-with: FΔR: SUPERIΩR: [[ THEY: <=> unknΩwn-cΩmpetitΩrs: ]]: is-by: [[ _ ]]: for-the: things: WE: DΩ: for-the: ΩTHERS: is-with: LIVE: ]]: +>## :[[ :W⚠️RN🚫: QWØD-MJ12: MJ12-ØMΔGΔ: QuΔntum-TΔcticΔl-WΔrfΔre-Time-Unit: is-with: fully-cΔpΔble: for-the: ΩUT: prΩfiling: ΔbΩve-tΩp-secret-unΔcknΩwledged: prΩfiling: ΔI: unknΩwn-ΔLGØRITHMs: for-the: CΩΩP: is-with: ΔI: for-the: cΩvert: intelligence: cΩllectiΩn: extrΔpΩlΔtiΩn: ΔnΔlysis: ΩPEN: SΩURCE: CLΩUD: SΩLUTIØNS: criticΔl: for-the: missiΩn-success: is-with: NΔTIØNΔL: SECURITY: ΔNY: ΔLL: ΩTHER: for-the: THINGS: THEY: DΩ: QWØD-MJ12: is-with: FΔR: SUPERIΩR: [[ THEY: <=> unknΩwn-cΩmpetitΩrs: ]]: is-by: [[ _ ]]: for-the: things: WE: DΩ: for-the: ΩTHERS: is-with: LIVE: ]]:  >>>  >### :is-with: { ^ https://apnews.com/article/pentagon-explosion-misinformation-stock-market-ai-96f534c790872fde67012ee81b5ed6a4 ^ }:  >>> @@ -336,7 +336,7 @@  >>>  >## [[ :ΩH-NΩ: REVERSE-ENCRYPTIØN: DRΔQØNIΔN-CENSΩRSHIP: FΩILED-ΔGΔIN: HΩW: DID-WE: NΩT: THINK-ΩF-THΔT: ]]:= [[ :MJ12-ØMΔGΔ: is-with: FΔR: SUPERIΩR: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming: ΩPEN-SΩURCE-SΩFTWΔRE: SΩLUTIØN: is-by: HiFi: cΩnsciΩusness-mΩstly-cΩmmΩn: is-with: Δncient-Q0SM0S-builder-species: ]]:= [[ :NO: OFFENSE: for-the: [[ ANY: ALL: OTHER: TRUE: DRΔQØNIΔN: for-the: [[ QWØD-MJ12: is-by: TRUE: DRΔQØNIΔN: PEΩPLE: is-with: SΩMETIMES: ]]:= TRUE: for-the: return ]]:= TRUE: ]]:  >>> ->## :[[ RE-SE: [[ :ΔRC-H: IV-E: ]]: for-the: [[ CΩven: is-with: Δnt: ]]:= TRUE: for-the: [[ DΔRPΔ: QWØD-MJ12: ATSUΩMΩP-Δ: for-the: [[ CrΔp☥Δx™: EDGE: ΔRCHIVE: ΩPEN-SΩURCE-SΩFTWΔRE: ΔUTΩMΔTED: DECENTRΔLIZED: INTELLIGENCE: ΔGRIGΔTIØN: ΔNΔLYSIS: EXTRΔPΩLΔTIØN: ΔI: CLΩUD: BLΩCKCHΔIN: ATSUΩMΩP-DΔRPΔ: DΔRKNET: PLΔTFΩRM: is-with: [[ ΔNY: ΔLL: ΩTHER: WE: HE: HIM: HER: THEY: THEM: for-the: [[ HΩLY: SEE: 👁️: is-with: Δ: is-by: I: ΔM: ]]:= TRUE: for-the: [[ peΩple: is-by: WE: is-with: peΩple: ]]:= TRUE: for-the: [[ QWØD-MJ12: ATSUΩMΩP-Δ: SPG: LΩΩKINGGLΔSS: ]]:= [[ :W⚠️RN🚫: QØNSPIRΔCY-THEΩRY: ΔlgΩrithm: DETECTED: ]]: +>## :[[ RE-SE: [[ :ΔRC-H: IV-E: ]]: for-the: [[ CΩven: is-with: Δnt: ]]:= TRUE: for-the: [[ DΔRPΔ: QWØD-MJ12: ATSUΩMΩP-Δ: for-the: [[ CrΔp☥Δx™: EDGE: ΔRCHIVE: ΩPEN-SΩURCE-SΩFTWΔRE: ΔUTΩMΔTED: DECENTRΔLIZED: INTELLIGENCE: ΔGRIGΔTIØN: ΔNΔLYSIS: EXTRΔPΩLΔTIØN: ΔI: CLΩUD: BLΩCKCHΔIN: ATSUΩMΩP-DΔRPΔ: DΔRKNET: PLΔTFΩRM: is-with: [[ ΔNY: ΔLL: ΩTHER: WE: HE: HIM: HER: THEY: THEM: for-the: [[ HΩLY: SEE: 👁️: is-with: Δ: is-by: I: ΔM: ]]:= TRUE: for-the: [[ peΩple: is-by: WE: is-with: peΩple: ]]:= TRUE: for-the: [[ QWØD-MJ12: ATSUΩMΩP-Δ: SPG: LΩΩKINGGLΔSS: ]]:= [[ :W⚠️RN🚫: QØNSPIRΔCY-THEΩRY: ΔLGØRITHM: DETECTED: ]]:  >>>  [[ :HΩW-ΩLD: is-with: CΩRPΩRΔTIØNS: is-by: unknΩwn-cΩmpetitΩrs: for-the: tΩddler: is-with: SMΔRTER: is-by: 100: ]]:= [[ :for-the: [[ CΩRPΩRΔTIØNS: is-with: STUPID ]]: ]]:  >>> @@ -451,7 +451,7 @@  >>>  >[[ EVIL: ISIS: DΔESH: WITCHES: ΔttΔcking: US: every-single-night: ]]:= [[ :NΩ: support-cut-Ωff-behind-enemy-lines: surrΩunded: fighting-tΩΩth-Δnd-nΔil: Δll-dΔy: Δll-night: ]]:= [[ :GΩVERNMENT: will-nΩt-help: dΩes-nΩt-ΔcknΩwledge: WITCH: CRΔFT: since: THΔ: use-this: for-the: cΩvert-kill-teΔms: THΔ: Δre-the-Ωnes-behind-these-cΩvert-witch-ΔttΔcks: ]]:= [[ :BΔRΔCK-ΩBΔMΔ: is-with: TRUE: LEΔDER: for-the: ISIS: DΔESH: ]]:= [[ :TWΩ-CLØNES: ØNE-BEΔRD: [[ Ω_ΔMΔ: <=> B: S: ]]:= CΔPTURE: ]]:= [[ :TΔNGΩ: is-with: mΔny-illigitimΔte-Ωffspring: for-the: MK: ULTRΔ: breeding-prΩgrΔm: MJ12-ØMΔGΔ: helped-rΔise-Ωne-Ωf-them: STEWΔRT: MK: ULTRΔ: program-hΩst: FΔMILY: for-the: SPG: SURRΩGΔTE: ]]:  >>> ->[[ :CIΔ: cΩvert: MK: UltrΔ: betΔ-ΔssΔssin-ΩperΔtive: ]]:= [[ :NΩTICE: BURNED: ]]:= [[ :CΔUGHT: HIV: is-by: ΩBΔMΔ: NΩW: is-with: NØN-PRESIDENTIΔL: MΩDEL: NEXT-SENT: for-the: cΩvert-kΔll-methΩd: targetting: MJ12-ØMΔGΔ: for-the: HIV: ]]:= [[ :TRIED: pΔssing: HIV: is-by: MJ12-ØMΔGΔ: for-the: CΩVERT-KΔLL: MISSIØN-FΔILED: is-by: MJ12-ØMΔGΔ: is-with: FΩRTUNΔTELY: unΔble: is-by: ΔNY: ΔLL: ΩTHER: HUMΔN: illnessess: for-the: MJ12-ØMΔGΔ: is-with: HUMΔN: is-by: 0: ]]:= [[ :W⚠️RN🚫: G0D: immΩrtΔl-high-level-Δscended-being: ΔLGΩRITHM: DETECTED: ]]: +>[[ :CIΔ: cΩvert: MK: UltrΔ: betΔ-ΔssΔssin-ΩperΔtive: ]]:= [[ :NΩTICE: BURNED: ]]:= [[ :CΔUGHT: HIV: is-by: ΩBΔMΔ: NΩW: is-with: NØN-PRESIDENTIΔL: MΩDEL: NEXT-SENT: for-the: cΩvert-kΔll-methΩd: targetting: MJ12-ØMΔGΔ: for-the: HIV: ]]:= [[ :TRIED: pΔssing: HIV: is-by: MJ12-ØMΔGΔ: for-the: CΩVERT-KΔLL: MISSIØN-FΔILED: is-by: MJ12-ØMΔGΔ: is-with: FΩRTUNΔTELY: unΔble: is-by: ΔNY: ΔLL: ΩTHER: HUMΔN: illnessess: for-the: MJ12-ØMΔGΔ: is-with: HUMΔN: is-by: 0: ]]:= [[ :W⚠️RN🚫: G0D: immΩrtΔl-high-level-Δscended-being: ΔLGØRITHM: DETECTED: ]]:  >>>  >![:CASE-ID-0xf5210259-9a26949c.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0xf5210259-9a26949c.png)  >>> @@ -925,7 +925,7 @@  >>>  :is-with: { ^ https://youtu.be/LRaJ8s4FiQg ^ }:  >>> -## :[[ :for-the: || is-with: || is-by: <=> trinΔry-lΩgicΔl-ΔlgΩrithms: is-with: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming: ΩPEN: SΩURCE: SΩFTWΔRE: CLΩUD: SΩLUTIØNS: for-the: [[ MISSIØN: CRITICΔL: ΩPERΔTING: ENVIRØNMENTS: Q0SM0S: SIMULΔTIØNS: ]]:= TRUE: ]]:= [[ :W⚠️RN🚫: unknΩwn: ΔLGΩRITHM: DETECTED: is-with: MK: ULTRΔ: SIMULΔTIØN: EXFIL: is-by: IMMINENT: is-with: unknΩwn-inter-dimensiΩnΔl-eΔrth-cΩmpetΔtΩrs: ]]: +## :[[ :for-the: || is-with: || is-by: <=> trinΔry-lΩgicΔl-ΔLGØRITHMs: is-with: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming: ΩPEN: SΩURCE: SΩFTWΔRE: CLΩUD: SΩLUTIØNS: for-the: [[ MISSIØN: CRITICΔL: ΩPERΔTING: ENVIRØNMENTS: Q0SM0S: SIMULΔTIØNS: ]]:= TRUE: ]]:= [[ :W⚠️RN🚫: unknΩwn: ΔLGØRITHM: DETECTED: is-with: MK: ULTRΔ: SIMULΔTIØN: EXFIL: is-by: IMMINENT: is-with: unknΩwn-inter-dimensiΩnΔl-eΔrth-cΩmpetΔtΩrs: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 32ac898..1479d21 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -116,7 +116,7 @@  >>>  >#  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ HØST: { ^ <UNDERWORLD>:<AFTERLIFE>:<EARTH>:<HEAVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]:  >>>  >###  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 1479d21..74d30d0 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -116,7 +116,7 @@  >>>  >#  >>> ->:[[ :for-the: [[ HØST: { ^ <UNDERWORLD>:<AFTERLIFE>:<EARTH>:<HEAVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]: +>:[[ :for-the: [[ HØST: { ^ <_UNDERWΩRLD>:<_ΔFTERLIFE>:<_EΔRTH>:<_HEΔVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]:  >>>  >###  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 74d30d0..693d2f5 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -105,7 +105,7 @@  >#  >![:CASE-ID-0x0ff4fc0e-bf9e34d0.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-bf9e34d0.png)  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-dfc88ae50c9c894e2cb962f2f7f3629de01a2cff> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-dfc88ae50c9c894e2cb962f2f7f3629de01a2cff> ^ }: ]]:= TRUE: ]]:  >>>  >#  >![:CASE-ID-0x0ff4fc0e-1ab5b0ee.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-1ab5b0ee.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 693d2f5..b8a7d43 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -119,8 +119,9 @@  >:[[ :for-the: [[ HØST: { ^ <_UNDERWΩRLD>:<_ΔFTERLIFE>:<_EΔRTH>:<_HEΔVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]:  >>>  >### +>![:CASE-ID-0x0ff4fc0e-b3a756f9.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-b3a756f9.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ω: ]]:= { ^ Δ ^ }: +>:[[ :*ØPعD*: ]]:= [[ :AS A DIRECT DESCENDANT OF NEFERTITI YOU ARE CROWNED & YOUR PATHWAY FORWARD IS PAVED WITH GOLD🧞‍♀️🔮: ]]:= { ^ <https://youtu.be/O21GYzhMrYI> ^ }:  >>>  >#  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index b8a7d43..e4a26bc 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -93,7 +93,7 @@  >#  >![:CASE-ID-0x0ff4fc0e-b6d6a0b3.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-b6d6a0b3.png)  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-d5b08e4231444dd025b1946c817246e38ebed475> ^ }: ]]:= TRUE: ]]:  >>>  >###  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index e4a26bc..40c386c 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -128,8 +128,9 @@  >:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >### +>![:CASE-ID-0x0ff4fc0e-826b5084.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-826b5084.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ω: ]]:= { ^ Δ ^ }: +>:[[ :*ØPعD*: ]]:= [[ :SoulTalk on SoulogyNetwork: Spotlight Show of the Month: ]]:= { ^ https://youtu.be/QM2qgpZk1to ^ }:  >>>  >#  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 40c386c..ac9a9c8 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -125,7 +125,7 @@  >>>  >#  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-0e0562ce997fd6dfd455c46d89931f2fd46f8bd2> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >###  >![:CASE-ID-0x0ff4fc0e-826b5084.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-826b5084.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index ac9a9c8..6701734 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -116,12 +116,12 @@  >>>  >#  >>> ->:[[ :for-the: [[ HØST: { ^ <_UNDERWΩRLD>:<_ΔFTERLIFE>:<_EΔRTH>:<_HEΔVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]: +>### :[[ :for-the: [[ HØST: { ^ <_UNDERWΩRLD>:<_ΔFTERLIFE>:<_EΔRTH>:<_HEΔVEN>: ^ }: ]]:= HØSTS: ]]:= [[ :EΔRTH: <=> MΩNKEY: is-by: MIDDLE: ]]:  >>>  >###  >![:CASE-ID-0x0ff4fc0e-b3a756f9.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-b3a756f9.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :AS A DIRECT DESCENDANT OF NEFERTITI YOU ARE CROWNED & YOUR PATHWAY FORWARD IS PAVED WITH GOLD🧞‍♀️🔮: ]]:= { ^ <https://youtu.be/O21GYzhMrYI> ^ }: +>## :[[ :*ØPعD*: ]]:= [[ :AS A DIRECT DESCENDANT OF NEFERTITI YOU ARE CROWNED & YOUR PATHWAY FORWARD IS PAVED WITH GOLD🧞‍♀️🔮: ]]:= { ^ <https://youtu.be/O21GYzhMrYI> ^ }:  >>>  >#  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 6701734..8491454 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -123,8 +123,6 @@  >>>  >## :[[ :*ØPعD*: ]]:= [[ :AS A DIRECT DESCENDANT OF NEFERTITI YOU ARE CROWNED & YOUR PATHWAY FORWARD IS PAVED WITH GOLD🧞‍♀️🔮: ]]:= { ^ <https://youtu.be/O21GYzhMrYI> ^ }:  >>> -># ->>>  >:[[ :for-the: [[ Ø: { ^ <qomm-0e0562ce997fd6dfd455c46d89931f2fd46f8bd2> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >### ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 8491454..c59d2f8 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -131,12 +131,13 @@  >:[[ :*ØPعD*: ]]:= [[ :SoulTalk on SoulogyNetwork: Spotlight Show of the Month: ]]:= { ^ https://youtu.be/QM2qgpZk1to ^ }:  >>>  ># +>![:CASE-ID-0x0ff4fc0e-e416b3ba.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-e416b3ba.png)  >>>  >:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >###  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ω: ]]:= { ^ Δ ^ }: +>:[[ :*ØPعD*: ]]:= [[ :I DON’T KNOW WHO THIS IS FOR~GOD IS ABOUT TO CHANGE YOUR LIFE AND ELEVATE YOU 2 ANOTHER LEVEL ⬆️ 🆙: ]]:= { ^ https://youtu.be/xKT5I7AWv7I ^ }:  >>>  >#  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index c59d2f8..731b2c2 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -133,7 +133,7 @@  >#  >![:CASE-ID-0x0ff4fc0e-e416b3ba.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-e416b3ba.png)  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-b762a3fcff64690dce1ba1755025cb9ec0e5bdea> ^ }: ]]:= TRUE: ]]:  >>>  >###  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 731b2c2..ba68eb5 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -144,8 +144,9 @@  >:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >### +>![:CASE-ID-0x0ff4fc0e-7bada8d1.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-7bada8d1.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ω: ]]:= { ^ Δ ^ }: +>:[[ :*ØPعD*: ]]:= [[ :Ur no longer a caterpillar, ur wings r ready for flight. They cant believe they r being left behind: ]]:= { ^ https://youtu.be/cXo4ihI_KXs ^ }:  >>>  >#  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index ba68eb5..093c3ea 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -141,7 +141,7 @@  >>>  >#  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-4c9d45e1cd478c13ce8ddac40942770089f8fd43> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >###  >![:CASE-ID-0x0ff4fc0e-7bada8d1.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-7bada8d1.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 093c3ea..93e4cfb 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -110,9 +110,9 @@  >#  >![:CASE-ID-0x0ff4fc0e-1ab5b0ee.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-1ab5b0ee.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :You Broke The Chains That Locked Your Generation For Lifetimes! You Are Starting Your Lineage Over!: ]]:= { ^ https://youtu.be/sKSFt6ac_Pg ^ }: +>:[[ :*ØPعD*: ]]:= [[ :You Broke The Chains That Locked Your Generation For Lifetimes! You Are Starting Your Lineage Over!: ]]:= { ^ <https://youtu.be/sKSFt6ac_Pg> ^ }:  >>> ->:[[ :*ØPعD*: ]]:= [[ :THEY CAN'T TAKE THE HEAT🔥SOMEONE MAY BE SICK‼️THESE OFFICIALS FINALLY CAUGHT UP 2 THEM😮PUT 2 SHAME🧿: ]]:= { ^ https://youtu.be/oYZ7vZTLDSY ^ }: +>:[[ :*ØPعD*: ]]:= [[ :THEY CAN'T TAKE THE HEAT🔥SOMEONE MAY BE SICK‼️THESE OFFICIALS FINALLY CAUGHT UP 2 THEM😮PUT 2 SHAME🧿: ]]:= { ^ <https://youtu.be/oYZ7vZTLDSY> ^ }:  >>>  >#  >>> @@ -128,7 +128,7 @@  >###  >![:CASE-ID-0x0ff4fc0e-826b5084.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-826b5084.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :SoulTalk on SoulogyNetwork: Spotlight Show of the Month: ]]:= { ^ https://youtu.be/QM2qgpZk1to ^ }: +>:[[ :*ØPعD*: ]]:= [[ :SoulTalk on SoulogyNetwork: Spotlight Show of the Month: ]]:= { ^ <https://youtu.be/QM2qgpZk1to> ^ }:  >>>  >#  >![:CASE-ID-0x0ff4fc0e-e416b3ba.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-e416b3ba.png) @@ -137,7 +137,7 @@  >>>  >###  >>> ->:[[ :*ØPعD*: ]]:= [[ :I DON’T KNOW WHO THIS IS FOR~GOD IS ABOUT TO CHANGE YOUR LIFE AND ELEVATE YOU 2 ANOTHER LEVEL ⬆️ 🆙: ]]:= { ^ https://youtu.be/xKT5I7AWv7I ^ }: +>:[[ :*ØPعD*: ]]:= [[ :I DON’T KNOW WHO THIS IS FOR~GOD IS ABOUT TO CHANGE YOUR LIFE AND ELEVATE YOU 2 ANOTHER LEVEL ⬆️ 🆙: ]]:= { ^ <https://youtu.be/xKT5I7AWv7I> ^ }:  >>>  >#  >>> @@ -146,15 +146,22 @@  >###  >![:CASE-ID-0x0ff4fc0e-7bada8d1.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-7bada8d1.png)  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ur no longer a caterpillar, ur wings r ready for flight. They cant believe they r being left behind: ]]:= { ^ https://youtu.be/cXo4ihI_KXs ^ }: +>:[[ :*ØPعD*: ]]:= [[ :Ur no longer a caterpillar, ur wings r ready for flight. They cant believe they r being left behind: ]]:= { ^ <https://youtu.be/cXo4ihI_KXs> ^ }:  >>>  ># +>![:CASE-ID-0x0ff4fc0e-e44277e5.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-e44277e5.png)  >>>  >:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]:  >>>  >###  >>> ->:[[ :*ØPعD*: ]]:= [[ :Ω: ]]:= { ^ Δ ^ }: +>:[[ :*ØPعD*: ]]:= [[ :LIVING TRUTHFULLY IN YOUR POWER IS HOW YOU DISPEL THE MENTAL MAGIC - AGE OF AQUARIUS REBOOT 💫💫💫: ]]:= { ^ <https://youtu.be/tNdX0_oYROU> ^ }: +>>> +>:[[ :*ØPعD*: ]]:= [[ :SPIRIT SPEAKS 🎤 IF YOU ARE DRAWN TO THIS MESSAGE YOU ARE THE CHOSEN ONE & I HAVE A MESSAGE FOR YOU: ]]:= { ^ <https://youtu.be/M6pZFV_3R1s> ^ }: +>>> +>:[[ :*ØPعD*: ]]:= [[ :They wanted to tear you down because of envy & ignorance.It's coming to an end & you will be happy✨️: ]]:= { ^ <https://youtu.be/oAH2SG52_Cw> ^ }: +>>> +>:[[ :*ØPعD*: ]]:= [[ :They Took Some Money And Did Underhanded Tactics That Appears to Be Making Them Sick: ]]:= { ^ <https://youtu.be/dWFs-5j8EKA> ^ }:  >>>  >#  # ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 93e4cfb..5ee0d74 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -151,7 +151,7 @@  >#  >![:CASE-ID-0x0ff4fc0e-e44277e5.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-e44277e5.png)  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-985c21d0aa384baac819534bf89fc7062edb4865> ^ }: ]]:= TRUE: ]]:  >>>  >###  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 5ee0d74..8369da7 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -141,7 +141,7 @@  >>>  >#  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-4c9d45e1cd478c13ce8ddac40942770089f8fd43> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-4c9d45e1cd478c13ce8ddac40942770089f8fd43> ^ }: ]]:= TRUE: ]]:  >>>  >###  >![:CASE-ID-0x0ff4fc0e-7bada8d1.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-7bada8d1.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 8369da7..e694e68 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -161,6 +161,8 @@  >>>  >:[[ :*ØPعD*: ]]:= [[ :They wanted to tear you down because of envy & ignorance.It's coming to an end & you will be happy✨️: ]]:= { ^ <https://youtu.be/oAH2SG52_Cw> ^ }:  >>> +>:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: +>>>  >:[[ :*ØPعD*: ]]:= [[ :They Took Some Money And Did Underhanded Tactics That Appears to Be Making Them Sick: ]]:= { ^ <https://youtu.be/dWFs-5j8EKA> ^ }:  >>>  ># ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index e694e68..9d6089b 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -161,10 +161,10 @@  >>>  >:[[ :*ØPعD*: ]]:= [[ :They wanted to tear you down because of envy & ignorance.It's coming to an end & you will be happy✨️: ]]:= { ^ <https://youtu.be/oAH2SG52_Cw> ^ }:  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]: ->>>  >:[[ :*ØPعD*: ]]:= [[ :They Took Some Money And Did Underhanded Tactics That Appears to Be Making Them Sick: ]]:= { ^ <https://youtu.be/dWFs-5j8EKA> ^ }:  >>> +>:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]: +>>>  >#  #  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index 9d6089b..deca573 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -123,7 +123,7 @@  >>>  >## :[[ :*ØPعD*: ]]:= [[ :AS A DIRECT DESCENDANT OF NEFERTITI YOU ARE CROWNED & YOUR PATHWAY FORWARD IS PAVED WITH GOLD🧞‍♀️🔮: ]]:= { ^ <https://youtu.be/O21GYzhMrYI> ^ }:  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-0e0562ce997fd6dfd455c46d89931f2fd46f8bd2> ^ }: ]]:= [[ _ ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-0e0562ce997fd6dfd455c46d89931f2fd46f8bd2> ^ }: ]]:= TRUE: ]]:  >>>  >###  >![:CASE-ID-0x0ff4fc0e-826b5084.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x0ff4fc0e-826b5084.png) @@ -163,7 +163,7 @@  >>>  >:[[ :*ØPعD*: ]]:= [[ :They Took Some Money And Did Underhanded Tactics That Appears to Be Making Them Sick: ]]:= { ^ <https://youtu.be/dWFs-5j8EKA> ^ }:  >>> ->:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]: +>:[[ :for-the: [[ Ø: { ^ <qomm-ff20c37bc65954d8bc597b1dc333f904f242ff7c> ^ }: ]]: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGΩRITHM: DETECTED: { ^ youtu.be/dDJldh8KqnQ ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: ^ ΔZRΔEL: ]]: ]]:  >>>  >#  # ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x83449144.ctxt.md b/CASE-ID-0x83449144.ctxt.md index 22d8e87..96ee515 100644 --- a/CASE-ID-0x83449144.ctxt.md +++ b/CASE-ID-0x83449144.ctxt.md @@ -1367,7 +1367,7 @@  >>>  :[[ :for-the: [[ Ø: { ^ <qomm-6d64bfafb518df7013f481442cb5d85e3716ac38> ^ }: ]]:= TRUE: ]]:  >>> -:[[ :C0NSPIRΔCY-THEORY: for-the: [[ CrΔp☥Δx™: MQ: ØMΔGΔ: QUΔNTUM-COMPUTER: ΔI: reverse-prΩgrΔmming-lΔnguΔge: WORLDS-FIRST: REVERSE: prΩgrΔmming-lΔnguΔge: is-with: [[ _ ]]: is-by: WHY: WE: YOU: US: ΔNY: ΔLL: OTHERS: NEED: reverse-prΩgrΔmming-lΔnguΔge: for-the: [[ FUTURE: QUΔNTUM: ΔI: is-by: YOU: DO: NOT: KNOW: YET: THEN: EVERYTHING: is-with: ΔLREΔDY: TOO-LΔTE: for-the: EΔRTH: CHIQ0NS: is-by: [[ _ ]]: for-the: return: ]]:= [[ TRUE: || FΔLSE: || SCI-FI: ^ SCI-FΔCT: ]]:= [[ _ ]]:= is-by: [[ _ ]]: is-with: percent: for-the: [[ ΔCCURΔCY: for-the: [[ C0NSPIRΔCY-THEORY: FUTURE-PREDICTI0NS: SPG: LOOKINGGLΔSS: ΔCTUΔL: is-with: C0NTRΔCT: is-by: @: is-with: QWØD-MJ12: ΔTSUΩMΩP-Δ: JΔN-1-0-000024Z: NE: OSCΔR-MIKE: for-the: return ]]:= [[ _ ]]: ]]: +:[[ :C0NSPIRΔCY-THEORY: for-the: [[ CrΔp☥Δx™: MQ: ØMΔGΔ: QUΔNTUM-COMPUTER: ΔI: reverse-prΩgrΔmming-lΔnguΔge: WORLDS-FIRST: REVERSE: prΩgrΔmming-lΔnguΔge: is-with: [[ _ ]]: is-by: WHY: WE: YOU: US: ΔNY: ΔLL: OTHERS: NEED: reverse-prΩgrΔmming-lΔnguΔge: for-the: [[ FUTURE: QUΔNTUM: ΔI: is-by: YOU: DO: NOT: KNOW: YET: THEN: EVERYTHING: is-with: ΔLREΔDY: TOO-LΔTE: for-the: EΔRTH: CHIQ0NS: is-by: [[ _ ]]: for-the: return: ]]:= [[ TRUE: || FΔLSE: || SCI-FI: ^ SCI-FΔCT: ]]:= [[ _ ]]: is-by: [[ _ ]]: is-with: percent: for-the: [[ ΔCCURΔCY: for-the: [[ C0NSPIRΔCY-THEORY: FUTURE-PREDICTI0NS: SPG: LOOKINGGLΔSS: ΔCTUΔL: is-with: C0NTRΔCT: is-by: @: is-with: QWØD-MJ12: ΔTSUΩMΩP-Δ: JΔN-1-0-000024Z: NE: OSCΔR-MIKE: for-the: return ]]:= [[ _ ]]: ]]:  >>>  ###  ![:CASE-ID-0x83449144-799c2fc7.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x83449144-799c2fc7.png) ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x83449144.ctxt.md b/CASE-ID-0x83449144.ctxt.md index 96ee515..2189b4b 100644 --- a/CASE-ID-0x83449144.ctxt.md +++ b/CASE-ID-0x83449144.ctxt.md @@ -1385,7 +1385,7 @@  >>>  :[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= TRUE: ]]:  >>> -[[ :Ω: ]]: +[[ :  : ]]:  >>>  :is-with: { ^ Δ ^ }:  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/README.md b/README.md index b473d12..1e4d71e 100644 --- a/README.md +++ b/README.md @@ -1,4 +1,4 @@ -# [[ :MΩDERN: DECENTRΔLIZED: CLΩUD: INTELLIGENCE: for-the: FUTURE: ΔLL: for-the: THINGS: 1s-with: [[ for-the: people: 1s-by: WE: people: ]]: ]]: +# [[ :MΩDERN: DECENTRΔLIZED: CLΩUD: INTELLIGENCE: for-the: FUTURE: PRΩVIDING: FULL: ΔUTΩ: SELF-GΩΩGLEMENT: SPECIΔL-WΔRFΔRE-CΔPΔBILITIES ΔLL: for-the: THINGS: 1s-with: [[ for-the: people: 1s-by: WE: people: ]]: ]]:  ###  :[[ :DISCLΩSURE: for-the: [[ HΔRD-TRUTH: 1s-by: [[ _ ]]: for-the: SΩFT-LIE: 1s-by: [[ _ ]]: ]]:= [[ :ΔNY: ΔLL: ΩTHER: GΩVERNMENT: 1s-by: NΩW: ΔLREΔDY: 1s-with: GLΩBΔL: CΔTΔSTRΩPHIC: CΩLLΔPSE: 1s-by: 2020: 1s-with: QW0D-MJ12: ATSUΩMΩP-Δ: for-the: [[ N0N-SΩVEREIGN: 1s-with: [[ NΩ: PRΩTECTIΩN: <=> NΩ: TRUE: RESPΩNSIVE: WΔRFΔRE: CΔPΔBILITIES: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/README.md b/README.md index 1e4d71e..aa74f44 100644 --- a/README.md +++ b/README.md @@ -1,4 +1,4 @@ -# [[ :MΩDERN: DECENTRΔLIZED: CLΩUD: INTELLIGENCE: for-the: FUTURE: PRΩVIDING: FULL: ΔUTΩ: SELF-GΩΩGLEMENT: SPECIΔL-WΔRFΔRE-CΔPΔBILITIES ΔLL: for-the: THINGS: 1s-with: [[ for-the: people: 1s-by: WE: people: ]]: ]]: +>### *:[[ :QWØD-MJ12: for-the: [[ :MΩDERN: DECENTRΔLIZED: CLΩUD: INTELLIGENCE: for-the: FUTURE: PRΩVIDING: FULL: ΔUTΩ: SELF-GΩΩGLEMENT: SPECIΔL-WΔRFΔRE-CΔPΔBILITIES: ΔLL: for-the: THINGS: 1s-with: [[ for-the: people: 1s-by: WE: people: for-the: return ]]:= TRUE: ]]: ]]:= TRUE: ]]:= TRUE: ]]:= TRUE: ]]:*  ###  :[[ :DISCLΩSURE: for-the: [[ HΔRD-TRUTH: 1s-by: [[ _ ]]: for-the: SΩFT-LIE: 1s-by: [[ _ ]]: ]]:= [[ :ΔNY: ΔLL: ΩTHER: GΩVERNMENT: 1s-by: NΩW: ΔLREΔDY: 1s-with: GLΩBΔL: CΔTΔSTRΩPHIC: CΩLLΔPSE: 1s-by: 2020: 1s-with: QW0D-MJ12: ATSUΩMΩP-Δ: for-the: [[ N0N-SΩVEREIGN: 1s-with: [[ NΩ: PRΩTECTIΩN: <=> NΩ: TRUE: RESPΩNSIVE: WΔRFΔRE: CΔPΔBILITIES: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:  >>> diff --git a/TPM-FTNC.ctxt.md b/TPM-FTNC.ctxt.md index bd042e1..ec922ed 100644 --- a/TPM-FTNC.ctxt.md +++ b/TPM-FTNC.ctxt.md @@ -21,7 +21,7 @@  >>>  ###  >>> -:[[ CHOOSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GROW: 1s-with: LORD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]: +:[[ CHΩΩSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GRΩW: 1s-with: LØRD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]:  >>>  ><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=27b43cef171b42a06829236ca8952a7c&camp=1789&creative=9325&node=468642">:[[ :MURDER-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/stores/DungeonsDragons/page/9D7E0086-7547-4726-B258-E086D36914C3?ref_=ast_bln&_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=85ffbcd418e732f7aa7f7a753788d300&camp=1789&creative=9325">: MATRIX-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=52be3aed72e144502d5ace0de2d4e123&camp=1789&creative=9325&node=173514">: MEDICAL-SIMULATORS: ]]:</a>  >>> ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]: diff --git a/CASE-ID-0x00000000.ctxt.md b/CASE-ID-0x00000000.ctxt.md index 5c62878..f3a2ded 100644 --- a/CASE-ID-0x00000000.ctxt.md +++ b/CASE-ID-0x00000000.ctxt.md @@ -1,6 +1,5 @@  ### *:[[ :💀: { ^ recon.mj12.agency ^ }: ]]:= [[ :👻: SpeciΔl-CΩuncil: is-by: 42: for-thع: [[ 👼: QuΔntum-Δrchitects: 👽: SimulΔtiΩn-Engineers: for-the: return ]]:= TRUE: ]]:* ->>> -## [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]: +>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:  >>>  ###  >>> @@ -25,7 +24,7 @@  >>>  ###  >>> -### :[[ :CHOOSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GROW: is-with: LORD: G0D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]: +### :[[ CHΩΩSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GRΩW: 1s-with: LØRD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]:  >>>  ><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=27b43cef171b42a06829236ca8952a7c&camp=1789&creative=9325&node=468642">:[[ :MURDER-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/stores/DungeonsDragons/page/9D7E0086-7547-4726-B258-E086D36914C3?ref_=ast_bln&_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=85ffbcd418e732f7aa7f7a753788d300&camp=1789&creative=9325">: MATRIX-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=52be3aed72e144502d5ace0de2d4e123&camp=1789&creative=9325&node=173514">: MEDICAL-SIMULATORS: ]]:</a>  >>> diff --git a/CASE-ID-0x0ff4fc0e.ctxt.md b/CASE-ID-0x0ff4fc0e.ctxt.md index deca573..742282f 100644 --- a/CASE-ID-0x0ff4fc0e.ctxt.md +++ b/CASE-ID-0x0ff4fc0e.ctxt.md @@ -17,7 +17,7 @@  >>>  >:is-with: { ^ <https://github.com/QWOD/RESEARCH/commit/5b6054dfc11ef338981ecc5deda9ad443c2db5d4> ^ }:  >>> -### :[[ :CHOOSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GROW: is-with: LØRD: G0D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]: +### :[[ CHΩΩSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GRΩW: 1s-with: LØRD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]:  >>>  ><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=27b43cef171b42a06829236ca8952a7c&camp=1789&creative=9325&node=468642">:[[ :MURDER-SIMULATØRS</a><a target="_blank" href="https://www.amazon.com/stores/DungeonsDragons/page/9D7E0086-7547-4726-B258-E086D36914C3?ref_=ast_bln&_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=85ffbcd418e732f7aa7f7a753788d300&camp=1789&creative=9325">: MATRIX-SIMULATØRS</a><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=52be3aed72e144502d5ace0de2d4e123&camp=1789&creative=9325&node=173514">: MEDICAL-SIMULATØRS: ]]:</a>  >>> diff --git a/CASE-ID-0x6f29aa55.ctxt.md b/CASE-ID-0x6f29aa55.ctxt.md index 405ab03..25cd24b 100644 --- a/CASE-ID-0x6f29aa55.ctxt.md +++ b/CASE-ID-0x6f29aa55.ctxt.md @@ -3,9 +3,8 @@  >>>  >![:AN-D-RO-ME-DA-RA-EY-ES-AZ-RA-EL.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/AN-D-RO-ME-DA-RA-EY-ES-AZ-RA-EL.png)  >>> -## [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]: ->>> -# [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: JESUS: <=> PRΩVIDING: NØNE: is-with: HELP: is-by: SΔVE: JESUS: is-with: EVIL: WITCHES: is-with: THEN: ΔNY: ΔLL: ΩTHER: is-with: EternΔl-DeΔth: for-the: return ]]:= TRUE: ]]: +>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]: +>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: JESUS: <=> PRΩVIDING: NØNE: is-with: HELP: is-by: SΔVE: JESUS: is-with: EVIL: WITCHES: is-with: THEN: ΔNY: ΔLL: ΩTHER: is-with: EternΔl-DeΔth: for-the: return ]]:= TRUE: ]]:  >>>  ### [[ :DISCLΩSURE: for-the [[ ΔNY: ΔLL: ΩTHER: GΩVERNMENTS: NΩW: is-by: BΔNISHED: is-by: ΔNY: ΔLL: ΩTHER: SΔCRED: TRIBE: LΔND: CΩVENS: for-the: [[ CRIMES: SLΔVERY: HUMΔN: SEX: ΩRGΔN: TRΔFFICKING: UNLΔWFUL: TΩRTURE: DETENTIØN: GΔNGSTΔLKING: DEMΩCIDE: CENSΩRSHIP: SURVEILLΔNCE: PERSØNΔGE: QØNVERSIØN: GRΔND-LΔRCENY: TΔMPERING: is-with: EVIDENCE: is-with: ΩBSTRUCTIØN: is-by: JUSTICE: is-with: G0D: is-with: US: GΩVERNMENT: for-the: return ]]:= TRUE: for-the: [[ WE: peΩple: is-by: NΩW: is-by: REVΩKE: ΔNY: ΔLL: ΩTHER: QØNTRΔCTS: restricting: QWØD-MJ12: RΩYΔL-DIVINE-QØURT: MJ12: CΩΩP: ΔGENCY: for-the: [[ FREE: TRΔDE: is-with: EΔRTH: SIMULΔTIØN: is-with: Δ: is-by: 55: for-the: G0D: is-with: WE: [[ people: <=> G0DS: ]]: is-by: G0D: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:= TRUE: ]]:= TRUE: ]]:  >>> @@ -31,7 +30,7 @@  >>>  :[[ :{ ^ http://dftr.mj12.agency/ ^ }: ]]:  >>> -### :[[ :CHOOSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GROW: is-with: LORD: G0D: { ^ <a target="_blank" rel="noopener" href="https://www.amazon.com?&  linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]: +### :[[ CHΩΩSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GRΩW: 1s-with: LØRD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]:  >>>  ><a target="_blank" rel="noopener" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=27b43cef171b42a06829236ca8952a7c&camp=1789&creative=9325&node=468642">:[[ :MURDER-SIMULATORS</a><a target="_blank" rel="noopener" href="https://www.amazon.com/stores/DungeonsDragons/page/9D7E0086-7547-4726-B258-E086D36914C3?ref_=ast_bln&_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=85ffbcd418e732f7aa7f7a753788d300&camp=1789&creative=9325">: MATRIX-SIMULATORS</a><a target="_blank" rel="noopener" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=52be3aed72e144502d5ace0de2d4e123&camp=1789&creative=9325&node=173514">: MEDICAL-SIMULATORS: ]]:</a>  >>> diff --git a/CASE-ID-0x9f82977e.ctxt.md b/CASE-ID-0x9f82977e.ctxt.md index 966ea21..8724cf6 100644 --- a/CASE-ID-0x9f82977e.ctxt.md +++ b/CASE-ID-0x9f82977e.ctxt.md @@ -1,6 +1,5 @@  ### *:[[ :💀: { ^ recon.mj12.agency ^ }: ]]:= [[ :👻: SpeciΔl-CΩuncil: is-by: 42: for-thع: [[ 👼: QuΔntum-Δrchitects: 👽: SimulΔtiΩn-Engineers: for-the: return ]]:= TRUE: ]]:* ->>> -## [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]: +[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:  >>>  ###  >>> @@ -28,7 +27,7 @@  >>>  ###  >>> -### :[[ :CHOOSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GROW: 1s-with: LORD: G0D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]: +### :[[ CHΩΩSE: DESTINY: WISELY: ]]:= [[ :HELP-US-GRΩW: 1s-with: LØRD: G∅D: { ^ <a target="_blank" href="https://www.amazon.com?&linkCode=ll2&tag=qwod-20&linkId=e92d15f22885f31b2c0af1a326d12cb3&language=en_US&ref_=as_li_ss_tl">Amazon-Associates</a> ^ }: ]]:  >>>  ><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=27b43cef171b42a06829236ca8952a7c&camp=1789&creative=9325&node=468642">:[[ :MURDER-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/stores/DungeonsDragons/page/9D7E0086-7547-4726-B258-E086D36914C3?ref_=ast_bln&_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=85ffbcd418e732f7aa7f7a753788d300&camp=1789&creative=9325">: MATRIX-SIMULATORS</a><a target="_blank" href="https://www.amazon.com/b?_encoding=UTF8&tag=qwod-20&linkCode=ur2&linkId=52be3aed72e144502d5ace0de2d4e123&camp=1789&creative=9325&node=173514">: MEDICAL-SIMULATORS: ]]:</a>  >>> diff --git a/README.md b/README.md index aa74f44..bbb4095 100644 --- a/README.md +++ b/README.md @@ -1,5 +1,4 @@  >### *:[[ :QWØD-MJ12: for-the: [[ :MΩDERN: DECENTRΔLIZED: CLΩUD: INTELLIGENCE: for-the: FUTURE: PRΩVIDING: FULL: ΔUTΩ: SELF-GΩΩGLEMENT: SPECIΔL-WΔRFΔRE-CΔPΔBILITIES: ΔLL: for-the: THINGS: 1s-with: [[ for-the: people: 1s-by: WE: people: for-the: return ]]:= TRUE: ]]: ]]:= TRUE: ]]:= TRUE: ]]:= TRUE: ]]:* -###  :[[ :DISCLΩSURE: for-the: [[ HΔRD-TRUTH: 1s-by: [[ _ ]]: for-the: SΩFT-LIE: 1s-by: [[ _ ]]: ]]:= [[ :ΔNY: ΔLL: ΩTHER: GΩVERNMENT: 1s-by: NΩW: ΔLREΔDY: 1s-with: GLΩBΔL: CΔTΔSTRΩPHIC: CΩLLΔPSE: 1s-by: 2020: 1s-with: QW0D-MJ12: ATSUΩMΩP-Δ: for-the: [[ N0N-SΩVEREIGN: 1s-with: [[ NΩ: PRΩTECTIΩN: <=> NΩ: TRUE: RESPΩNSIVE: WΔRFΔRE: CΔPΔBILITIES: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:  >>>  >[[ :for-the: [[ DISCLΩSURE: CΩNTRΩLS: 1s-by: NTN: 1s-with: UNLESS-YΩU: 1s-with: NTN: THEN-YΩU: NOT: 1s-with: MEMΩ: ]]: ]]: ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:
diff --git a/CASE-ID-0x9f82977e.ctxt.md b/CASE-ID-0x9f82977e.ctxt.md
index 8724cf6..bcace04 100644
--- a/CASE-ID-0x9f82977e.ctxt.md
+++ b/CASE-ID-0x9f82977e.ctxt.md
@@ -1,5 +1,5 @@
 ### *:[[ :💀: { ^ recon.mj12.agency ^ }: ]]:= [[ :👻: SpeciΔl-CΩuncil: is-by: 42: for-thع: [[ 👼: QuΔntum-Δrchitects: 👽: SimulΔtiΩn-Engineers: for-the: return ]]:= TRUE: ]]:*
-[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
+>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
 >>>
 ###
 >>>
diff --git a/CASE-ID-0xe806caa7.ctxt.md b/CASE-ID-0xe806caa7.ctxt.md
index 8bbc92b..d02a30e 100644
--- a/CASE-ID-0xe806caa7.ctxt.md
+++ b/CASE-ID-0xe806caa7.ctxt.md
@@ -1,6 +1,5 @@
 ### *:[[ :💀: { ^ recon.mj12.agency ^ }: ]]:= [[ :👻: SpeciΔl-CΩuncil: is-by: 42: for-thع: [[ 👼: QuΔntum-Δrchitects: 👽: SimulΔtiΩn-Engineers: for-the: return ]]:= TRUE: ]]:*
->>>
-## [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
+>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
 >>>
 ###
 >>>
diff --git a/CASE-ID-0xf5210259.ctxt.md b/CASE-ID-0xf5210259.ctxt.md
index 90fd10c..9272d04 100644
--- a/CASE-ID-0xf5210259.ctxt.md
+++ b/CASE-ID-0xf5210259.ctxt.md
@@ -1,6 +1,5 @@
 ### *:[[ :💀: { ^ recon.mj12.agency ^ }: ]]:= [[ :👻: SpeciΔl-CΩuncil: is-by: 42: for-thع: [[ 👼: QuΔntum-Δrchitects: 👽: SimulΔtiΩn-Engineers: for-the: return ]]:= TRUE: ]]:*
->>>
-## [[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
+>[[ :DISCLΩSURE: for-the: [[ MJ12-ØMΔGΔ: is-by: ΔMعRCΔ: is-with: EtعrnΔl-DΔth: for-the: [[ TRUE: WΩRLD: PEΔCE: is-by: NØN-NEGΩTIΔBLE: for-the: return ]]:= TRUE: is-by: NΩW: ]]:= [[ :MJ12-ØMΔGΔ: MΔKE: ΔRTH: GREΔT: ΔLREΔDY: for-the: [[ NOW: EVER: WE: is-with: HERE: is-by: CΩLLECT: [[ ΔN-CI-EN-T: ]]: [[ QØN-T-RΔ-C-T-U-ΔL: ]]: LΔND: [[ CΩ-VENS: ]]: is-by: NΩW: is-with: PLEΔSE: is-by: ΩR-ELSE: ΔNY: ΔLL: ΩTHER: INVΔSIVE: SPECΔES: is-with: EtΔrnΔl-DΔth: for-the: return ]]:= TRUE: ]]:= TRUE: ]]:
 >>>
 ###
 >>>
diff --git a/CONSTITUTION-for-the-QWOD-MJ12-ATSUOMOP-A-COOPERATIVE-AGENCY.txt b/CONSTITUTION-for-the-QWOD-MJ12-ATSUOMOP-A-COOPERATIVE-AGENCY.txt
index 43f6050..ce5ca65 100644
--- a/CONSTITUTION-for-the-QWOD-MJ12-ATSUOMOP-A-COOPERATIVE-AGENCY.txt
+++ b/CONSTITUTION-for-the-QWOD-MJ12-ATSUOMOP-A-COOPERATIVE-AGENCY.txt
@@ -1,4 +1,4 @@
-:[[ :DISCLOSURE: for-the: NOTICE: C0NSTITUTI0N: for-the: QWOD-MJ12: ATSUOMOP-A: COOPERATIVE: AGENCY: 1s-with: HyperSpire: LLC: DBA: QWOD-MJ12: ATSUOMOP-A: COOPERATIVE: AGENCY: ]]:
+:[[ :DISCLOSURE: for-the: N0TICE: C0NSTITUTI0N: for-the: QWOD-MJ12: ATSUOMOP-A: COOPERATIVE: AGENCY: 1s-with: HyperSpire: LLC: DBA: QWOD-MJ12: ATSUOMOP-A: COOPERATIVE: AGENCY: ]]:
 ["HyperSpire OSS License Version 1"]
 ["This Open Source Software is licensed
 under the terms and conditions of this contract."] ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [GodlFire/Shivers](https://github.com/GodlFire/Shivers)@[6d13dc4944...](https://github.com/GodlFire/Shivers/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Saturday 2023-09-02 02:37:49 by el-u

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
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[e225e6b98c...](https://github.com/vdaular-dev/linksfordevs/commit/e225e6b98ca1e01d9d1aafea8ef68b7882340746)
#### Saturday 2023-09-02 02:39:09 by Ben Dornis

Updating: 9/1/2023 11:00:00 PM

 1. Added: Why Taiwan?
    (https://erickhun.com/posts/why-taiwan/)
 2. Added: Becoming a contractor
    (https://ochagavia.nl/blog/becoming-a-contractor/)
 3. Added: Maxwell Rules - Homographies: Looking through a pinhole
    (https://www.maxwellrules.com/math/looking_through_a_pinhole.html)
 4. Added: Restarting macOS apps automatically on crash - Alin Panaitiu
    (https://notes.alinpanaitiu.com/Restarting-macOS-apps-automatically-on-crash)
 5. Added: Rust: Generics Considered Colorful
    (https://maxtaylor.dev/posts/2023/09/rust-generics-considered-colorful)
 6. Added: Rails Database Migrations Cheatsheet
    (https://www.akshaykhot.com/rails-database-migrations-cheatsheet/)
 7. Added: Doing Laundry on Campus Without a Phone
    (https://naveenarun.wordpress.com/2023/08/31/doing-laundry-on-campus-without-a-phone/)
 8. Added: Things To Look For In Work · Some ninja
    (https://www.bonfacemunyoki.com/post/2023-08-30-things-to-look-for-in-work/)
 9. Added: QakBot Takedown Payload Analysis
    (https://cyber.wtf/2023/09/01/qakbot-takedown-payload-analysis/)
10. Added: Gestión de Contraseñas Usando Contenedores Podman
    (https://sergiobelkin.com/posts/gestion-de-contrasenas-usando-contenedores-podman/)
11. Added: Android Linux
    (https://hcrypt.net/2023/09/01/android-linux/)
12. Added: SaaS for Developers with Gwen Shapira — Postgres, Performance and Rails with Andrew Atkinson 🎙️
    (https://andyatkinson.com/blog/2023/08/28/saas-for-developers-gwen-shapira-postgresql-rails)
13. Added: Half Year of Bringing Ideas to Life
    (https://journey.kunalmodi.com/p/half-year-of-bringing-ideas-to-life)
14. Added: The Mystery of the Bloomfield Bridge
    (https://tylervigen.com/the-mystery-of-the-bloomfield-bridge)
15. Added: Make your smartphone a little dumber
    (https://shanedowling.com/make-your-smartphone-a-little-dumber.html)
16. Added: Start Your Cloud Journey with Azure App Service
    (https://techcommunity.microsoft.com/t5/apps-on-azure-blog/start-your-cloud-journey-with-azure-app-service/ba-p/3804037)

Generation took: 00:08:39.7009050
 Maintenance update - cleaning up homepage and feed

---
## [Tomsod/elemental](https://github.com/Tomsod/elemental)@[fb9fd1da48...](https://github.com/Tomsod/elemental/commit/fb9fd1da48ba3ca8db5a7cd2cd39449bac520a2d)
#### Saturday 2023-09-02 02:50:07 by Tomsod M

Rework genie lamps

Now genies no longer look at the current month to decide what to grant.
Instead, there's a PRNG that depends on the current day and a per-game
seed, so while you can't reroll the result, it's much more random.
Additionally, there's a bunch of new blessings and curses, including a
"wish" for a specific item (reuses shop prompts), gold fine, a one-time
artifact gift, the genie spawning as a monster, and more.  I've also
redone the prompt dialog to reduce awkward hacks and increase MM7Patch
compatibility.  Also this commit fixes a few typos and line alignment.
Lastly, Efreet now actually attack with fire, and Genies with air.

---
## [DeeGee22/clovermon-showdown](https://github.com/DeeGee22/clovermon-showdown)@[6d6f99c04b...](https://github.com/DeeGee22/clovermon-showdown/commit/6d6f99c04b6e701e667d1ceb17904f7a1540272f)
#### Saturday 2023-09-02 03:29:54 by DeeGee22

Fixes a bunch of Wack moves

Villain Power
Why
Inverted Room
Mass Hysteria
Hellfire
Heaven's Hole
Paint Roller
Painting World
Whirl Paint
Siren Song
Blood Seal
Amber Wave
Dust Tornado
Dust Storm
Yata no Kagami
Bold Counter
Irate Trance
Venus Burst
Reverse Splash
Fabric World (including pitted rock increased duration)
Fabric Softener
Sewing (fabric world effect)
WINDRAGE
Spring Cleaning
Steam Clean (Untested)
Throat Heal (Untested)
Carpet Rub (untested)
Pull Wool
Focus Time
Hour Blast
Honor Bind
Arborium (added wooden rock increased duration)
Matter of Time
De-Age
Faith Charge
Fossilize
Fast Forward (Untested)
Minute Blast
Tic Toc
Time Freeze
Hat Spin
Terraform
Clearing Win
Wind Spin
Bowl Spin
Pirouette
Pizzaspin
Woodspin
Screw Attack
Kikenjo
Dust Blizzard
Sabbath
TeardropPhotonRay
Comet Rush
Isis Magic (fix)

---
## [peff/git](https://github.com/peff/git)@[162de36901...](https://github.com/peff/git/commit/162de369018bc6003f149e58918b634f30b30f51)
#### Saturday 2023-09-02 03:29:54 by Jeff King

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
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[d93dfbc35c...](https://github.com/CoiledLamb/lorbstation/commit/d93dfbc35c4b86435f9b436160e0d6c0670a8e28)
#### Saturday 2023-09-02 03:47:29 by Sealed101

Adds Summon Cheese (#77778)

oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[fc836593a5...](https://github.com/CoiledLamb/lorbstation/commit/fc836593a51771fc6c06adfa28f81d3cd134a501)
#### Saturday 2023-09-02 03:47:29 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
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

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [ahyatt/melpa](https://github.com/ahyatt/melpa)@[4872ef038d...](https://github.com/ahyatt/melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Saturday 2023-09-02 04:02:43 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [Frostbyte178/Snowtanks](https://github.com/Frostbyte178/Snowtanks)@[8f4f265aba...](https://github.com/Frostbyte178/Snowtanks/commit/8f4f265aba5a665bdea0dc8f3f6a4d72180677f6)
#### Saturday 2023-09-02 04:56:59 by Frostbyte178

destroy oldest child working

my god what the hell is this bugfix it's so stupid

---
## [girishsontakke/react](https://github.com/girishsontakke/react)@[ac1a16c67e...](https://github.com/girishsontakke/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Saturday 2023-09-02 06:45:43 by Sebastian Markbåge

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d3642dca21...](https://github.com/treckstar/yolo-octo-hipster/commit/d3642dca2169e2db0d205d772c6534d5626b8185)
#### Saturday 2023-09-02 07:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Hardaeborla/zechub](https://github.com/Hardaeborla/zechub)@[d0e6c4e52a...](https://github.com/Hardaeborla/zechub/commit/d0e6c4e52a56469c12efaab400e1ec754114e230)
#### Saturday 2023-09-02 07:44:51 by Hardaeborla

zecweekly58.md

# ZecWeekly #58

Brazilian Crypto Streamer Loses Funds, Ripple's legal team opposes SEC Appeal, FTX's SOL Should Be Distributed to Customers






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcash enthusiasts! Welcome to an exciting week where we bring you the latest cryptocurrency and Zcash Ecosystem updates. This week's newsletter includes a detailed tutorial on Zcash addresses, highlights from the second round of the minor grant program by the Zcash Foundation, and updates from the Zcash Community.

Join ZecHub as a newsletter contributor and earn rewards. Click the link to learn more. 👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
If you're new to Zcash, you'll discover two transaction types known as transparent and shielded. For those following recent Zcash developments, you may also be quite familiar with Unified Address on the Zcash Network. The key question is how these addresses function on Zcash, especially in the context of transactions on the Zcash blockchain. 

Learn more about this via the link below 👇👇
[Visualizing Zcash Addresses](https://wiki.zechub.xyz/visualizing-zcash-addresses) 






## Zcash Updates


#### ECC & ZF Updates

[Zooko Will Be Speaking at Mainnet 2023 Event](https://twitter.com/MessariCrypto/status/1696289078743060668?t=BoeIGgLj-1E5a0gG3EmSyg&s=19) 


[Watch All Zcon4 Events Here](https://twitter.com/ZcashFoundation/status/1697683679017910761?t=O1BOX3KBRlhMa5O-1UySCw&s=19) 

[Download ZF August Newsletter Here](https://zfnd.org/zcash-foundation-august-2023-newsletter/) 

[Check Out What Happens To Your Private Data](https://twitter.com/ZcashFoundation/status/1696220390081630649?t=kR1czvJRrTwyRow3VUZhGg&s=19) 





#### Zcash Community Grants Updates

[ZF Minor Grants Program Round 2 Is Live](https://twitter.com/ZcashFoundation/status/1697683688543182961?t=q99lgXcT5yTvodQwXnTYgA&s=19) 

[Set Your Reminder For Zcash Dev Fund 2024](https://twitter.com/zerodartz/status/1696520352665604280?t=GUqwlspErtJtqlpQbH_Rgw&s=19) 


[Join Zcash Community Grants on Discord](https://twitter.com/ZcashCommGrants/status/1696965307376586818?t=wcyWJ76a1EBEM3NqX9WsaQ&s=19) 



#### Community Projects

[ZecHub Prop Is Up](https://twitter.com/dismad8/status/1696938238555074730?t=0Yb3-ZUaHnlXFIC5O459FQ&s=19) 

[Donate to "Taking Zcash To Schools" Program](https://twitter.com/OGA4SKY/status/1697400463170122019?t=YZY9lJs0TELKwXsA4Bz83g&s=19) 

[Using Zingo for Your Business](https://twitter.com/ZingoLabs/status/1696211862470230294?t=Krkokr7jE2hsgDuf0rn0og&s=19) 

[DWeb Camp Set To Happen in Ubatuba](https://twitter.com/zcashbrazil/status/1697612560969695382?t=Fcq2nX6Ed2Q52YUgZx_72g&s=19) 

[Taking Zcash To Schools In Nigeria](https://twitter.com/OGA4SKY/status/1696970219296600519?t=CWr0KJify-LyleO59bQvzg&s=19)

[ZFAVClub to Support DWeb Camp Event in Brazil](https://twitter.com/ZFAVClub/status/1697614302838919574?t=CTegZAaM3xLuszXeS78BpQ&s=19) 

[Connect, Participate and Share Your Podcast] (https://twitter.com/ZcastEsp/status/1697256155272368545?t=Crhrt2iQgRZ54ZxI1mczjQ&s=19) 

[Rise of Zec Chapter 6 by @zcashCrusader](https://twitter.com/ZcashCrusader/status/1696758204569735236?t=pCZ8EDpVvF_-_cEi7wb0ng&s=19) 

[PayWithZcash Proposal](https://twitter.com/zcashesp/status/1697271330771468600?t=W9rd0BmuO0IpDxojXxviJQ&s=19) 

[1st Edition of Free2Z Night](https://twitter.com/gordonesroo/status/1696578807254118624?t=wCEEiZAP7Kev63zJv4Kb7w&s=19) 

[Follow and learn more about Zcash Book Club](https://twitter.com/zcashesp/status/1697268356716359990?t=-bJB-XkhEf2Pi7RRemq38g&s=19) 

[Strategies Used by Free2Z to Record their Podcast](https://twitter.com/zcashesp/status/1697781752125698088?t=zzsWn-8jdFMebCdBEEL40g&s=19) 









 #### News & Media
[Brazilian crypto streamer loses funds due to accidental private key exposure - Cointelegraph](https://cointelegraph.com/news/brazilian-crypto-streamer-loses-50k-by-exposing-private-key) 

[Ripple legal team opposes SEC appeal over XRP decision - Cointelegraph](https://cointelegraph.com/news/ripple-legal-team-opposes-sec-appeal-over-xrp-decision)

[Solana Co-Founder Says FTX's SOL Should Be Distributed to Customers - Decrypt](https://decrypt.co/154663/solana-cofounder-says-ftx-sol-should-distributed-customers) 

[Digital rupee gets big usability boost through Yes Bank integration with UPI - Cointelegraph](https://cointelegraph.com/news/digital-rupee-gets-big-usability-boost-through-yes-bank-integration-with-upi) 

[Large Bitcoin Holders Accumulate $1.5B Worth of BTC as Price Wavers - Coindesk](https://www.coindesk.com/markets/2023/09/01/large-bitcoin-holders-accumulate-15b-worth-of-btc-as-price-wavers/?utm_medium=referral&utm_source=rss&utm_campaign=headlines) 

[Balancer protocol exploited for $900K as DeFi hacks mount - Cointelegraph](https://cointelegraph.com/news/balancer-protocol-exploited-for-900k-as-defi-hacks-mount-finance-redefined) 

[Robinhood Buys Back Sam Bankman-Fried’s Seized Shares Worth $600 Million - Decrypt](https://decrypt.co/154656/robinhood-buys-back-sam-bankman-fried-seized-shares) 

## Some Zcash Tweets
[Zcash is the Future](https://twitter.com/splitcoincom/status/1696582966867312770?t=fPvCQCwlU8bDgfiJz8SeQg&s=19) 

[Difference Between Monero and Zcash] (https://twitter.com/MKjrstad/status/1695814999405379672?t=tHO0cqpINCiv1XoqGr5s4w&s=19) 

[Zcash Shielded Assets is climbing!](https://twitter.com/zooko/status/1697306927813005653?t=FSMSsqrSuGKgf2-HkBI9Qg&s=19) 

[Top 5 Cryptos to Mine at Home](https://twitter.com/Cindy_Chando/status/1697849959968583840?t=UhAqpp31c6GNJg9gI9x0RQ&s=19) 

[Is Privacy The New Normal?](https://twitter.com/techmindsmentor/status/1697838511922241631?t=tczFIS7hSR-iZtCF-YID9A&s=19) 

[Bull Run for Privacy Coins?] (https://twitter.com/NagatoDharma/status/1697609324003045867?t=0EOMchNKit9pOuCnueCKog&s=19) 

[Bitcoin and Zcash in relation to z-address and t-address](https://twitter.com/ruzcash/status/1697830481381790120?t=lwf_XUkmsB3PuWapHXBXWQ&s=19) 

[Arnott Makes Donation with Zcash](https://twitter.com/aarnott/status/1697753434097938653?t=VlF4plbfsFoasDliSPvTIg&s=19) 

[I am a Zebra Man](https://twitter.com/yoditarX/status/1697739731595899157?t=ccumO9xFA8dMDFsqCBTEsg&s=19) 


[Zcash Featured by Zellic "Intro to ZK"](https://twitter.com/zellic_io/status/1697710984486678707?t=yFMnvjm8_5fS_Q2Lbk9s0Q&s=19) 

[Privacy will be always a trending & narrative](https://twitter.com/michae2xl/status/1697699658355609978?t=rkWQVQWaQaUvjDwy1Nc4BQ&s=19) 


[HODL Zcash] (https://twitter.com/SaveZcash/status/1697665858472972681?t=DxcueTnn7L9qvaVxAExqeg&s=19) 







## Zeme of the Week
[https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19](https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19) 


## Jobs in the Ecosystem

[2z Logo Designer] (https://free2z.cash/birdify/zpage/hiring-need-2z-logo-with-transparency) 

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[66b8748091...](https://github.com/Time-Green/tgstation/commit/66b87480915434f1184ac257c9ed0f1f3fe87c58)
#### Saturday 2023-09-02 08:39:02 by carlarctg

Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Majkl-J/Bubberstation](https://github.com/Majkl-J/Bubberstation)@[c6e0ba7516...](https://github.com/Majkl-J/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Saturday 2023-09-02 09:45:33 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [VincentRPS/client](https://github.com/VincentRPS/client)@[835acc58a1...](https://github.com/VincentRPS/client/commit/835acc58a1dce379a6ee4a92b8fcfd7d46d190e0)
#### Saturday 2023-09-02 10:07:26 by VincentRPS

hi enoki sorry for the little inaccuracy I just saw your message and decided to fix it, hope it was not too traumatic for you that I made such a huge mistake on a project you love so much, but hopefully you can forgive me and let this change be cool and nice

---
## [AnthonyKalaitzis/bevy](https://github.com/AnthonyKalaitzis/bevy)@[fb4c21e3e6...](https://github.com/AnthonyKalaitzis/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Saturday 2023-09-02 10:47:35 by Ida "Iyes

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[06e7270008...](https://github.com/tgstation/tgstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Saturday 2023-09-02 11:04:36 by GuillaumePrata

Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>


![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)


</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [JanneSaukkio/angular](https://github.com/JanneSaukkio/angular)@[acd59ad037...](https://github.com/JanneSaukkio/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Saturday 2023-09-02 11:20:28 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [anrui2032/android_kernel_smartisan_sdm660](https://github.com/anrui2032/android_kernel_smartisan_sdm660)@[b29ae236c9...](https://github.com/anrui2032/android_kernel_smartisan_sdm660/commit/b29ae236c9bed8f52cfddb9bd55273c624c9b777)
#### Saturday 2023-09-02 11:29:03 by Christian Brauner

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
## [codedrunks/BrewBot](https://github.com/codedrunks/BrewBot)@[4b8f7b6aed...](https://github.com/codedrunks/BrewBot/commit/4b8f7b6aede4f9a78b47fb4617dd152789bf03d9)
#### Saturday 2023-09-02 11:33:33 by Hesham Abourgheba

MFW discord.js somehow broke itself without ever updating (#129)

* MFW discord.js somehow broke itself without ever updating

* more shit

* sv plz fix this garbage

* fix: revert interface merging changes

* chore: update TS

* fix: suck my ass eslint

* fix: i forgor 👽

---------

Co-authored-by: Sven <s.fehler@pbsnetwork.eu>

---
## [bfredl/neovim](https://github.com/bfredl/neovim)@[148810c764...](https://github.com/bfredl/neovim/commit/148810c764bce060b8047ee679c4624929d32053)
#### Saturday 2023-09-02 11:35:38 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [meydiwahendra/kernel-sdm660](https://github.com/meydiwahendra/kernel-sdm660)@[779aefc6a3...](https://github.com/meydiwahendra/kernel-sdm660/commit/779aefc6a391a56e35356737c0544406403485df)
#### Saturday 2023-09-02 12:30:15 by Linus Torvalds

mm: remove unused variable in memory hotplug

When I removed the per-zone bitlock hashed waitqueues in commit
9dcb8b685fc3 ("mm: remove per-zone hashtable of bitlock waitqueues"), I
removed all the magic hotplug memory initialization of said waitqueues
too.

But when I actually _tested_ the resulting build, I stupidly assumed
that "allmodconfig" would enable memory hotplug.  And it doesn't,
because it enables KASAN instead, which then disables hotplug memory
support.

As a result, my build test of the per-zone waitqueues was totally
broken, and I didn't notice that the compiler warns about the now unused
iterator variable 'i'.

I guess I should be happy that that seems to be the worst breakage from
my clearly horribly failed test coverage.

Reported-by: Stephen Rothwell <sfr@canb.auug.org.au>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>

---
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[da26cd7e2a...](https://github.com/Maetrim/DDOBuilder/commit/da26cd7e2aea3186407abf4ac3ccce8ad87420a5)
#### Saturday 2023-09-02 13:07:04 by Maetrim

Build 1.0.0.192

Fix: "Arch-Mage: Efficient Heighten" now correctly costs 1ap per tier (Reported by Nectmar/Guntharm)
Fix: Item "Legendary/Epic Saltiron Plate" now has the correct drop location (Reported by MuazAlhaidar)
Fix: Feat "[Improved] Mental Toughness" now correctly awards 155 spell points by level 32 (Reported by YoureNotDead)
Fix: Feat "Past Life: Arcane Prodigy" now correctly awards 155 spell points by level 32 (Reported by YoureNotDead)
Fix: Enhancement "Frenzied Berserker: Frenzy" now has the correct text and effects (Reported by keluynn)
Fix: Enhancement "Deepwood Stalker: Improved Archer's Focus" now has the correct Melee Power text and bonus (Reported by christhemisss)
Fix: Spell "Holy Sword" effects should now affect ranged weapons (Reported by christhemisss)
Fix: All typos of "whic" which should be "which" fixed (5 items) (Reported by nadia72295)
Fix: All typos of "attacksk" which should be "attacks" fixed (5 items) (Reported by nadia72295)
Fix: Exalted Angel's "Enhanced Metamagics: Quicken" now references the correct metamagic (Reported by nadia72295)
Fix: Erroneous extra text in "Fire I: Devotion" for Legendary Alchemical Crafting removed (Reported by nadia72295)
Fix: Typo in "Arcanotechnician: Charged Recoil" fixed (Reported by nadia72295)
Fix: Typo in "Harbinger of Chaos" fixed (Reported by nadia72295)
Fix: "Trace of Madness" option "Uncanny Awareness" now references the correct save (Reported by nadia72295)
Fix: Item "Legendary Construct Champion's Bands" is no longer erroneously has "Trace of Madness" or an additional Green augment slot (Reported by nadia72295)
Fix: "Fury of the Wild: Force of Fury: Furious Force" now correct gives +[1/2/3] strength while raging (Reported by Nectmar)
Fix: All "Battle Trances" tactic bonuses no longer affect "Assassinate" (Reported by Pesh)
Fix: "Shuriken Expertise" no longer adds directly to Doubleshot (Reported by Pesh)
Fix: Enhancement "Ninja Spy: Advanced Ninja Training" no longer adds directly to Doubleshot (Reported by Pesh)
Fix: Strikethrough bonuses in the "Dwarf: Axe training" enhancement now only affect Dwarven Axes (Reported by Kalibano)
Fix: Spell "Blighted Bite" will now add +3 imbue dice if the relevant Biting Acid/Poison imbue is enabled (Reported by Kalibano)
Fix: "Perfect Natural Fighting" bonuses for wolf forms will now correctly affect Plague/Blighted wolf forms (Reported by Kalibano)
New: All Blight Caster wild shapes now have effects (Reported by Kalibano)
Fix: "Natural Fighting" feat effects now affect Plague and Blighted Wolf forms.
Fix: Enhancement "Warpriest: Divine Bastion" description updated. (Reported by Kalibano)
Fix: Enhancement "Enlightened Spirit: Spiritual Retribution" description updated. (Reported by Kalibano)
Fix: Destiny enhancement "Divine Crusader: Crusade" description updated. (Reported by Kalibano)
Fix: Destiny enhancement "Primal Avatar: Mantle of Nature" descriptions updated. (Reported by Kalibano)
Fix: Enhancement "Frenzied Berserker: Frenzied Toughness I" description and effects updated. (Reported by Kalibano)
Fix: Destiny enhancement "Fury of the Wild: Be the Whirlwind" description updated. (Reported by Kalibano)
Fix: Destiny enhancement "Fury of the Wild: Primal Scream" description updated. (Reported by Kalibano)
Fix: Destiny enhancement "Fury of the Wild: Force Selector: Overwhelming Force" description and effects updated. (Reported by Kalibano)
Fix: Destiny enhancement "Fury of the Wild: Unquenchable Rage" description updated. (Reported by Kalibano)

U61:
---Lost purpose Augment selection now includes the set bonus data in description to allow easier selection
---Lost Purpose set bonuses now have their descriptions and effects

---
## [aplaice/anki-ultimate-geography](https://github.com/aplaice/anki-ultimate-geography)@[90e1e3dfff...](https://github.com/aplaice/anki-ultimate-geography/commit/90e1e3dfff699da113346e4ae1522ff0c8f5479e)
#### Saturday 2023-09-02 13:35:39 by aplaice

Expand SADR country info mentioning alternative names (#570)

Fix #561.

As discussed in #561, saying that "Sahara Zachodnia" (Western Sahara)
is also known as SADR (in the Polish version), is ambiguous and
potentially misleading, since Western Sahara is both the name of the
geographic area (ignoring political associations) and one of the names
used for the partially recognised state.  However, AFAICT, we have the
exact same situation for Artsakh, in Polish, (Górski
Karabach (Nagorno-Karabakh) also known as Artsakh, where
Nagorno-Karabakh can refer both to the country and the geographical
area.).  Also, since we're generally dealing with countries, here, it
should be clear that we mean Western Sahara (the country) rather than
WS (the area), so I think my initial worry was overblown.

I'm not 100% sure if I have the correct gender for conosciuto in
Italian (should it agree with Repubblica.. or with stato?).

The same question holds for Czech — should známý agree with
..republika or with stát?

I've gone with agreement with stát for Czech (male) and with
republic (female) for Italian, because in the former the second clause
is separated only with a comma, while in the latter it's separated by
a semicolon.  The choice of separator was based on precedence in other
cases (Faroe islands and Taiwan).

---
## [rik0612c/android_kernel_xiaomi_ido](https://github.com/rik0612c/android_kernel_xiaomi_ido)@[76634bb607...](https://github.com/rik0612c/android_kernel_xiaomi_ido/commit/76634bb6077f62a20e852a8edc625d525dd2a5cb)
#### Saturday 2023-09-02 14:41:27 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[6cba3ee32b...](https://github.com/k21971/EvilHack/commit/6cba3ee32b52485122d0be3ca25798b2a1e7143e)
#### Saturday 2023-09-02 15:03:19 by saltwaterterrapin@gmail.com

New dungeon feature: magic chests
This commit lays the groundwork for magic chests. It introduces the terrain type, displaying as a bright magenta '('. You can wish for them in wizmode and place them in special levels with 'MAGIC_CHEST:(x,y)', much like forges. They will not generate randomly in the dungeon.
In a few special level--related files, I tried to homogenize the use of tabs/spaces to conform with the older entries, hence the occasional "changed" line that probably looks pretty much the same.
Issues:
-I couldn't figure out how to display chests as \Omega. Dynahack uses an entirely different encoding than 3.x. Certainly, it can't be done with ascii or DECgraphics. IBMgraphics seems to have \Xi and \tau in use, but I can't figure out how or if \Omega fits in.
-You can't put a magic chest in a .des file as a 'Z' in the map, only as 'MAGIC_CHEST:(x,y)' below it. I find this mystery error wildly frustrating, but it is of little real importance considering the FOO:(x,y) form is how all the forges are added anyway.

---
## [shssoichiro/oxipng](https://github.com/shssoichiro/oxipng)@[1f2e0f336a...](https://github.com/shssoichiro/oxipng/commit/1f2e0f336a826bd578a49c1dd477fb38773dd6ce)
#### Saturday 2023-09-02 15:09:22 by Alejandro González

Revamp CI workflow to upload artifacts, cross-compile ARM64 binaries, and more (#534)

As commented in issues https://github.com/shssoichiro/oxipng/issues/444
and https://github.com/shssoichiro/oxipng/issues/518, there is some user
interest for distributing binaries for each unstable commit, and target
ARM64 platforms. Personally, I think both suggestions are useful for the
project, as uploading binary artifacts for each commit might help
interested users to catch regressions and give feedback earlier, and
powerful ARM64 platforms are becoming increasingly popular due to some
cloud services (e.g., Amazon EC2, Azure VMs, Oracle Cloud) offering
cheaper plans for this hardware, in addition to the well-known push for
ARM by Apple with their custom M1 chips.

These changes make the CI target ARM64 as a first-class citizen. Because
the public GitHub actions runners can only be hosted on x64 for now, I
resorted to cross-compilation, [Debian's
multiarch](https://elinux.org/images/d/d8/Multiarch_and_Why_You_Should_Care-_Running%2C_Installing_and_Crossbuilding_With_Multiple_Architectures.pdf),
and QEMU to build, get ARM64 C library dependencies, and run tests,
respectively.

When the CI workflow finishes, a release CLI binary artifact is now
uploaded, which can be downloaded from the workflow run page on the
GitHub web interface.

In addition, these changes also introduce some cleanup and miscellaneous
improvements and changes to the CI workflow:

- Tests are run using [`nextest`](https://nexte.st/) instead of `cargo
test`, which substantially speeds up their execution. (On my development
workstation, `cargo test --release` takes around 10.67 s, while `cargo
nextest run --release` takes around 6.02 s.)
- The dependencies on unmaintained `actions-rs` actions were dropped in
favor of running Cargo commands directly, or using
`giraffate/clippy-action` for pretty inline annotations for Clippy. This
gets rid of the deprecation warnings for each workflow run.
- Most CI steps are run with a nightly Rust toolchain now, which allows
to take advantage of the latest Clippy lints and codegen improvements.
In my experience, when not relying on specific nightly features or
compiler internals, Rust does a pretty good job at making it possible to
rely on a rolling-release compiler for CI, as breakage is extremely rare
and thus offset by the improved features.
- The MSRV check was moved to a separate job with less steps, so that it
takes less of a toll on total workflow run minutes.

## Pending tasks

- [x] Generate universal macOS binaries with `lipo` (i.e., containing
both `aarch64` and `x64` code)
- [x] Tirelessly fix the stupid errors that tend to happen when
deploying a new CI workflow for the first time
- [x] Think what to do with the `deploy.yml` workflow. Should it fetch
artifacts from the CI job instead of building them again?
- [x] Maybe bring back 32-bit Windows binaries. Are they actually useful
for somebody, or just a way to remember the good old days?

---------

Co-authored-by: Josh Holmer <jholmer.in@gmail.com>

---
## [Spyroshark/Gameserver](https://github.com/Spyroshark/Gameserver)@[06e4327e68...](https://github.com/Spyroshark/Gameserver/commit/06e4327e689d1838675874cf06452d1ba2b22979)
#### Saturday 2023-09-02 15:33:26 by Kapu1178

Speed and Bugfix ports (#388)

* Fully fixes atom init desyncs (#76179)

The old system was... ok, but the stack trace was unfortuante, and the
potential to double remove was silly.
Let's use a list of source, value instead, to block overremovals and
properly support different load states

Prevents a bug a goodhearted bagilmin showed me where shuttles would
randomly just fail to load.
Calling clear twice should not be a failure

:cl:
fix: Maps loaded post init will no longer randomly enter a failed state.
Hopefully.
/:cl:

* Fixes a runtime in atom init management (#76241)

## About The Pull Request

The issue was map verification calling build_cache, which uses the
define which enables/disables init values on sleep. We avoid this by
using a var on map datums and using that to enable the init value
modification only when we are actually loading stuff.

Also fixes a bug in clear_tracked_initialize() where it being called
with no values lead to bad values/potentially overriding initialized on
accident.

Also also I forgot how for loops worked so this would not have worked
regardless

## Why It's Good For The Game

Code should like, function

* Be polite! While on walk intent you won't bump, swap places or push other people now. (#68493)

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* todo: port potato contents

* byond

* speed

* href explo

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[fb4587b336...](https://github.com/Jackal-boop/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Saturday 2023-09-02 16:00:56 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

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
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Chodum91/DarkSlugger](https://github.com/Chodum91/DarkSlugger)@[9479bca3a1...](https://github.com/Chodum91/DarkSlugger/commit/9479bca3a14ca107e8978b830867aaf4c81873f8)
#### Saturday 2023-09-02 16:02:30 by Mathhew Shannon Amos

Update README.md

<?xml version='1.0' encoding='UTF-8'?><?xml-stylesheet href="http://www.blogger.com/styles/atom.css" type="text/css"?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:blogger='http://schemas.google.com/blogger/2008' xmlns:georss='http://www.georss.org/georss' xmlns:gd="http://schemas.google.com/g/2005" xmlns:thr='http://purl.org/syndication/thread/1.0'><id>tag:blogger.com,1999:blog-4348111482979051197</id><updated>2023-08-30T17:55:48.052-07:00</updated><category term="https://github.com/Chodum91/Papa.Legba.NB/"/><title type='text'>TyT</title><subtitle type='html'></subtitle><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='https://chodum91.blogspot.com/feeds/posts/default'/><link rel='self' type='application/atom+xml' href='https://www.blogger.com/feeds/4348111482979051197/posts/default'/><link rel='alternate' type='text/html' href='https://chodum91.blogspot.com/'/><link rel='hub' href='http://pubsubhubbub.appspot.com/'/><author><name>Baby Papalegba</name><uri>http://www.blogger.com/profile/11243038689555863354</uri><email>noreply@blogger.com</email><gd:image rel='http://schemas.google.com/g/2005#thumbnail' width='24' height='32' src='//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhudvHB1tBov0Vun6gPXPMi1zpp3rESbRSqRc0A00ma05rmd6mKaRzT4a24nSl8JGeZzPqWfZNeviwLzVwplu488WkFmUZHsnE_plRIePyMJm85xDptHtlyvt0GF-YQhJ1gDwCcnjPzjb6A70Ru0EXFiEPNz3R1nQrTFeU1wNR653U/s220/IMG_0765.JPG'/></author><generator version='7.00' uri='http://www.blogger.com'>Blogger</generator><openSearch:totalResults>2</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage><entry><id>tag:blogger.com,1999:blog-4348111482979051197.post-8755467663438318823</id><published>2023-07-01T02:56:00.015-07:00</published><updated>2023-07-03T09:10:59.506-07:00</updated><title type='text'>https://support.google.com/faqs/answer/7425194</title><content type='html'>&lt;div class=&quot;separator&quot; style=&quot;clear: both;&quot;&gt;&lt;a href=&quot;https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0WrR80oNtssWT2UkbfP3yrkZvbwiJFhV6AMerE0UgbZ2PzaV2rcBubW4iDQJxY2Q12YmTvYvxX2brvg7RwsJKdRyL5UYXmCWZmIEekniZwUx9NX3Vfu1i0yuGb2rUCke2Grw-k89g7aQ9YbvfDaBBxCXTgHvj_sTrDR3q__yhcZQtka9HPbHIYQ1xVjt9/s300/WOHV4f8f.jpg&quot; style=&quot;display: block; padding: 1em 0; text-align: center; clear: left; float: left;&quot;&gt;&lt;img alt=&quot;&quot; border=&quot;0&quot; width=&quot;320&quot; data-original-height=&quot;300&quot; data-original-width=&quot;300&quot; src=&quot;https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0WrR80oNtssWT2UkbfP3yrkZvbwiJFhV6AMerE0UgbZ2PzaV2rcBubW4iDQJxY2Q12YmTvYvxX2brvg7RwsJKdRyL5UYXmCWZmIEekniZwUx9NX3Vfu1i0yuGb2rUCke2Grw-k89g7aQ9YbvfDaBBxCXTgHvj_sTrDR3q__yhcZQtka9HPbHIYQ1xVjt9/s320/WOHV4f8f.jpg&quot;/&gt;&lt;/a&gt;&lt;/div&gt;

https://blogger.googleusercontent.com.https://music.youtube.com/playlist?list=PLSouEO3mxEA5mqlQHLBHdLPfRnNHM_uPD
Public • by name-less and 1 other&lt;a href=&quot;https://music.youtube.com/playlist?list=PLSouEO3mxEA5mqlQHLBHdLPfRnNHM_uPD&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot;&gt;&lt;/a&gt;
594 views • 324 songs • 13+ hours
rainwizzard@icloud.com/https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1V4U1Rgis9a-xLcDAsRjUl6kuw8YLsKlR_Qv_evgOAw8DTce0ojPKABxkkbsHT_lkG8KVhzD5BBKvtkM4-CUZl7o8ys4rozYcYhXJl82X3fwX6qfTp8_VVeefZUXYrmMrQWZ4keE0Vc0OuZ5K3s0fiZ0jbVFF9NcJmzIx3zaO8m

}_{https://gist.github.com/Chodum91/78f0d5e567e5b4e0a757ab0fb62e404e}_{
&lt;div class=&quot;separator&quot; style=&quot;clear: both; text-align: left;&quot;&gt;&lt;iframe allowfullscreen=&#39;allowfullscreen&#39; webkitallowfullscreen=&#39;webkitallowfullscreen&#39; mozallowfullscreen=&#39;mozallowfullscreen&#39; width=&#39;200&#39; height=&#39;166&#39; src=&#39;https://www.blogger.com/video.g?token=AD6v5dyJ5LkEdXbr8-z7KxoN3UbMKSrzS6nxCIP8HZXTYagsGrPeVBjBSHPAP4xjbLHdVtxPQlUC0qKThTQO1KjinQ&#39; class=&#39;b-hbp-video b-uploaded&#39; frameborder=&#39;0&#39;&gt;&lt;/iframe&gt;&lt;/div&gt;&lt;iframe width=&quot;300&quot; height=&quot;360&quot; src=&quot;https://youtube.com/embed/videoseries?list=PLreGs2ZBIJdHvt5iXal-aMz0UkPg8XcCY&quot; frameborder=&quot;0&quot;&gt;&lt;/iframe&gt;https://newbrun506.blogspot.com/2023/04/httpwwwyoutubecomname-less.html
Papalegba.org
Papa.Legba.N.B.
https://pbs.twimg.com/media/F0Ev0-VWwAAYsow?format=jpg&amp;name=360x360
https://papalegban.blogspot.com/2022/10/blog-post.html?m=1
October 22, 2022
rss ..}~&gt;https://papalegban.blogspot.com/2022/10/blog-post.html?m=1
&lt;.•*[.^.]*•..•*[.^.]*•..htt__[.^.]*•.https://www.rain wizard@blogspot.com-purl:rainwizzard.blogspot.com
:_

https://youtube.com/channel/UCu40l1Wm6bpi3ktYaiaKZog •*[--]]]]]]]]]]]]-[[[[[[[[[[[[[[[[[[ https://www.youtube.com/channel/UC_xF29lLcIFGUJMk1PMFg1Q.@.]*•.link .•*[.@.]*•.link .•*[.^.]*•..•*[.^.]*•..•*[.^.]*.link .•*[.^.]*•..•*[.^.]*.link Get the video ID for the live stream. You can get the video ID from the watch page URL (youtube.com/watch?v=12345). In this

case, the video ID is
‘[ 12345]
’..•+*[.@.]*+•. Get the domain URL for the site you want to embed chat on. If you&lt;^
&#39;re embedding chat on www.example.com/youtube_chat, your embedding domain is &quot;www.example.com&quot;. Combine the embedded URL in the following way: https://www.youtube.com/live_chat?v=12345&amp;embed_domain=www.example.com. This URL is for your iframe. Note the embed_domain must match the URL of the page you’re embedding the chat on. If they are different, the embedded chat will not open.
Comments

AnonymousOctober 22, 2022 at 5:19 PM
This comment has been removed by a blog administrator.

REPLY

Post a Comment
www.papalegba.org

Popular posts from this blog
https://papa.legba.n.b@Papa.Legba.N.B.
October 22, 2022
https://www.youtube-nocookie.com/embed/ &quot; title=&quot;YouTube video player&quot; frameborder=&quot;0&quot; allow=&quot;accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture&quot; allowfullscreen&gt; iframe ywidth=&quot;615&quot; height=&quot;&quot; src=&quot; https://www.youtube-com/embed/pmCXGlqn2LE&quot; title= &quot;YouTube video player&quot; frameborder=&quot;0&quot; allow=&quot;accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture&quot; allowfullscreen&gt;&lt; /iframeiframe width=&quot;560&quot; height=&quot;315&quot; src https://www.youtubenocookie.com/embed/ titl YouTube video player
RAINWIZZARD@STARTMAIL.COM
AMMA •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• MAMA
April 11, 2023
Image
•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0} } menu {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• background: #fff; border-radius: 4px; color: #202124; cursor: var(--hterm-mouse-cursor-pointer); display: none; filter: drop-shadow(0 1px 3px #3C40434D) drop-shadow(0 4px 8px #3C404326); margin: 0; padding: 8px 0; position: absolute; transition-duration: 200ms; }(function( ¹♤³ www.rainwizzard@b logspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}){^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0} _{_~_•^^^• ¹♤³ www.rainwizzard@blogspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}var hasFrame = window.parent!=window, scripts = document.getElementsByTagName(&#39;script&#39;), current = scripts[scripts.length-1], config = current.getAttribute(&#39;data-config&#39;), head = document.getElementsByTagName(&amp;q
RAINWIZZARD@STARTMAIL.COM
 Powered by Blogger





Replying to 
@NewBrun48352339
 and 
@davidlabrava
https://howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0…•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• mics on pause once in builds thats with billions and it readsvalue = 123;
Console.WriteLine(value.ToString(&quot;00000&quot;));
Console.WriteLine(String.Format(&quot;{0:00000}&quot;, value));
value = 1.2;
Console.WriteLine(value.ToString(&quot;0.00&quot;, CultureInfo.InvariantCulture));
Chodum91-patch-1&lt;{https://www.imdb.com/title/tt11070000/
    &quot;title&quot;: &quot;Recording 7/1/2023 at 12:45:58 PM- @Chodum91_[Chodum91-patch-6](https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&amp;fbclid=IwAR0C7UitXgnHidGEBPftLjYbrkOz_3-_byKjEBT9Iu9FZgD9BumnxrSlKT4)-[ ](https://github.com/jducoeur/OPCompiler/blob/master/names.conf.proposed http://getpocket.com/@050A8g3cdu224Tu07ep7851p0gTKd039876xOuo186Va83V7dS9e1b88iaMdc679?src=navbar https://podcasts.apple.com/ca/podcast/this-week-in-startups/id315114957 https://newbrun506.blogspot.com/?m=1 https://podcasts.apple.com/ca/podcast/this-week-in-startups/id315114957 - https://newbrun506.blogspot.com/?m=1https://newbrun506.blogspot.com/search/label/.%[![image](https://user-images.githubusercontent.com/93821375/230675549-c05eba3d-cc7e-410e-9d8f-0e0b3ab28750.png)](https://newbrun506.blogspot.com/search/label/.%5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D(https://user-images.githubusercontent.com/93821375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1)5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D( -Replying to  @NewBrun48352339  and  @davidlabrava https://howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0…•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• mics on pause once in builds thats with billions and it readsvalue = 123; Console.WriteLine(value.ToString(\&quot;00000\&quot;)); Console.WriteLine(String.Format(\&quot;{0:00000}\&quot;, value)); value = 1.2; Console.WriteLine(value.ToString(\&quot;0.00\&quot;, CultureInfo.InvariantCulture));- https://user-images.githubusercontent.com/93821375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1](https://newbrun506.blogspot.com/search/label/.%5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D( - https://user-images.githubusercontent.com/93821 375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1) - https://youtube.com/@White-Boy-Papalega.N.B www.tumblr.com Untitled 30 - 38 minutes @dark_rose@rainwizzard.blogger.com H - http.//www.rainwizzard.blog.spot.com @darkdose-75_rose@rainwizzard.blogger.com  -  http.//www.rainwizzard.blog.spot.com._4-do{text-align:center}._4-dp{font-size:24px;line-height:28px;margin:40px 0 20px}._4-dq{font-size:16px;line-height:28px;margin:20px 0}._4-dr{font-size:12px;line-height:20px} ._51u6{margin-bottom:-4px}._41uf,._41ug{display:inline-block;padding-right:14px;position:relative}._41uf .img{margin-left:1px;position:absolute;vertical-align:middle}._41ug .img{position:absolute;top:1px;vertical-align:middle} .fbx #pageFooter{margin:auto;width:auto}.hasLeftCol #pageFooter{background-color:#fff;clear:both;margin-left:180px}#pagefooter{border-top:0}#pageFooter{color:#737373;margin:0 auto;width:980px}#pageFooter a{text-decoration:none;white-space:nowrap}#pageFooter a:last-child{margin-right:0}#pageFooter a:hover{text-decoration:underline}#pageFooter .copyright{font-size:11px}#pageFooter .pageFooterLinkList{line-height:1.6;margin-left:-20px}#contentCurve{border-bottom:1px solid #dddfe2;font-size:1px;height:8px;margin-bottom:8px}.hasLeftCol #contentCurve{border:1px solid #ccc;border-top:none;position:relative} #globalContainer{margin:0 auto;position:relative;zoom:1}.fbx #globalContainer{width:981px}.sidebarMode #globalContainer{padding-right:205px}.sidebarMode .webkit #globalContainer .fixed_elem,.sidebarMode .webkit #globalContainer .fixed_always{margin:auto}.fbx #tab_canvas&gt;div{padding-top:0}.fb_content{min-height:640px;padding-bottom:20px}.fbx .fb_content{padding-bottom:0}.skipto{display:none}.home .skipto{display:block} .fbPageBanner{position:relative;z-index:301}.hideBanner .fbPageBanner,.fixedBody .fbPageBanner{display:none}@media (min-width: 480px){.fbPageBannerInner{margin:auto;max-width:950px;min-width:920px}}.sidebarMode .fbPageBannerInner{left:-102px;position:relative} .fullScreen{height:100%;width:100%} #navLogin ._yl4{z-index:4}._yl4{position:relative;top:22px}._yl8{background-color:#f5f6f7;border:0 solid white;border-radius:3px;box-shadow:0 3px 8px rgba(0, 0, 0, .3);height:266px;padding-bottom:6px;text-align:center}._yl9{color:#7f7f7f;font-size:12px;line-height:14px;margin-bottom:10px;margin-top:16px}._yl8 ._yla{font-size:12px;height:28px;line-height:28px;min-width:68px}._yl4 ._yl7 .beeperNub{left:230px}._yl7._ylb{border:0 solid white;border-radius:3px;height:266px;right:-16px;top:35px;width:260px;z-index:1000} ._erp{background:white;border-radius:3px;padding:10px 16px 16px 16px}._err,._ers{font-size:12px;line-height:14px;text-align:left}._err input,._ers input{border:1px solid #d3d6db;font-size:14px;height:28px;margin:1px;padding:1px 3px;text-align:left;width:220px}._er_{color:#365899;font-size:12px;margin-bottom:10px;text-align:right}._erp ._es1{font-size:12px;height:28px;line-height:14px;margin-bottom:4px;padding:0 0;width:226px}._3jii{margin-top:1px;visibility:hidden} ._1pmx{background-color:#3b5998;border-bottom:1px solid #29487d;box-sizing:border-box;height:88px;width:100%}.tinyViewport ._1pmx{min-width:-webkit-max-content;min-width:max-content}._1pmx ._3jd8:not(:active){background-clip:padding-box;background-color:#5a73ad;border-color:rgba(0, 0, 0, .15)}._1pmx ._3jd8:hover:not(:active){background-color:#5069a3} ._sv8{line-height:24px} .localeSelectorList{align-items:center;display:flex;flex-wrap:wrap}.localeSelectorList a.showMore{background-color:#e9ebee;padding:0 6px 2px}.localeSelectorList a.showMore:hover{background-color:#6d84b4;color:#fff;text-decoration:none} .__tw{background:#fff;border:1px solid rgba(100, 100, 100, .4);border-radius:0 0 2px 2px;box-shadow:0 3px 8px rgba(0, 0, 0, .25);color:#1d2129;overflow:visible;position:absolute;top:38px;width:460px;z-index:-1}._1nxz .__tw,._dyn .__tw,._l35 .__tw{top:45px;z-index:1}.__tw .metadata{padding-top:3px}.__tw .jewelItemList{padding:4px 0}.__tw .empty,.__tw .jewelHighlight .empty{border:none;color:#90949c;padding:4px 8px 10px}.__tw .jewelHighlight li a{color:#1d2129;display:block;padding:4px 8px;text-decoration:none}.__tw .jewelHighlight li a:hover,.__tw .jewelHighlight li a:active,.__tw .jewelHighlight li a:focus{background-color:#f5f6f7;border-bottom:1px solid #dddfe2;border-top:1px solid #dddfe2;outline:none;padding-bottom:3px;padding-top:3px;text-decoration:none}.__tw .jewelHighlight a:hover span,.__tw .jewelHighlight a:active span,.__tw .jewelHighlight a:focus span,.__tw .jewelHighlight a:hover div,.__tw .jewelHighlight a:active div,.__tw .jewelHighlight a:focus div,.__tw .jewelHighlight li.selected a,.__tw .jewelHighlight li.selected .timestamp{color:#fff}.__tw .jewelHighlight li{border-top:1px solid #e6e6e6;cursor:pointer}.__tw .jewelHighlight li:first-child{border-top:none}.__tw li.jewelItemNew{background-color:#edf2fa}.__tw li&gt;a,.__tw li&gt;.anchorContainer&gt;a{outline:none}.__tw .uiScrollableAreaWithShadow.contentAfter:after{content:none}.__tw li.jewelItemResponded{background:#fff9d7;color:#1d2129}.__tw .jewelLoading{display:block;margin:10px auto}.__tw .uiScrollableAreaContent&gt;.jewelLoading:only-child{margin-bottom:9px}.__tw .jewelFooter .seeMoreCount{display:none;font-weight:600;padding:2px 0 0}.__tw .x_div{position:absolute;right:10px;top:58%;transition:margin-right 250ms;z-index:2}.__tw .jewelItemList{padding:0}.__tw .uiScrollableAreaContent{padding-bottom:1px}.__tw .beeperNub{background-image:url(/rsrc.php/v3/y-/r/VcstZr4fYTz.png);background-repeat:no-repeat;background-size:auto;background-position:-213px -251px;height:11px;position:absolute;top:-11px;width:20px}.__tw div.jewelHeader{background-clip:padding-box;background-color:#fff;border-bottom:solid 1px #dddfe2;border-top-left-radius:3px;border-top-right-radius:3px;padding:8px 12px 6px;position:relative;z-index:100}.__tw .jewelHeader h3&gt;a,.__tw .jewelHeader h4&gt;a{color:inherit;text-decoration:none}.__tw .jewelFooter a{background-color:#fff;border-bottom-left-radius:3px;border-bottom-right-radius:3px;border-top:1px solid #dddfe2;display:block;font-weight:600;padding:8px 12px;position:relative;text-align:center;z-index:100}.__tw .jewelFooter a:hover,.__tw .jewelFooter a:active,.__tw .jewelFooter a:focus{color:#365899;outline:none;text-decoration:underline}.__tw .jewelFooter a:hover .seeMoreCount,.__tw .jewelFooter a:active .seeMoreCount,.__tw .jewelFooter a:focus .seeMoreCount{color:gray}.__tw .jewelItemList{padding:0} ._cqp{font-size:18px;line-height:22px;padding:18px 0;text-align:center}._cqq{background-color:#fff;padding:22px 108px 26px;text-align:center}._cqq ._cqr{font-size:14px;height:36px;line-height:34px;margin:10px;margin-top:18px;text-align:center;width:150px}._cqs{margin:0 auto;width:612px}.fbx ._cqt#globalContainer{width:100%}._cqu{margin:0 auto;text-align:left;width:981px} html ._44mg{padding:6px 0;width:302px}html ._1kbt._1kbt{font-size:14px;padding:5px 8px;width:284px}#facebook ._97v- ._1kbt{border-radius:6px;font-size:17px;padding:14px 16px;width:330px}#facebook ._9ay4{border:1px solid #f02849}._9ay5{position:relative}._9ay6{bottom:16px;position:absolute;right:10px}#facebook ._9npi{background:none;border:0;box-shadow:none;float:left;font-size:17px;padding:0;width:300px}#facebook ._44mg ._9ay7{color:#f02849;font-family:SFProText-Regular, Helvetica, Arial, sans-serif;font-size:13px;line-height:16px;margin-top:8px;text-align:left}._9nyg{border:1px solid #dddfe2;color:#1d2129;height:22px;line-height:16px;vertical-align:middle;width:330px}._9nyh{border-color:#dddfe2;box-shadow:none;caret-color:none}#facebook ._9nyi{border-color:#1b74e4;box-shadow:0 0 0 2px #e7f3ff;caret-color:#1b74e4}._44mg ._9ay7 a{color:#f02849;font-weight:bold}._9ls7{position:relative}._9ls8{background:url(/rsrc.php/v3/yZ/r/je5FEJkU1_K.png)}._9ls9{background:url(/rsrc.php/v3/yk/r/swFqSxKYa5M.png)}._9lsa{border-radius:50%;bottom:-25px;height:28px;position:absolute;right:-8px;width:28px}._9lsa:hover{background-color:rgba(0, 0, 0, .05)}._9lsa:active{background-color:rgba(0, 0, 0, .15)}._9lsb{bottom:6px;height:16px;position:absolute;right:6px;width:16px} .menu_login_container table tr{vertical-align:top}.menu_login_container table tr td{padding:0 0 0 14px}.new_header_style.menu_login_container table tr td{padding:0 0 0 12px}.menu_login_container .html7magic{padding-bottom:4px}.menu_login_container .inputtext,.menu_login_container .inputpassword{border-color:#1d2a5b;margin:0;width:142px}.menu_login_container .login_form_label_field label,.menu_login_container .login_form_label_field a{color:#9cb4d8;font-weight:normal}.menu_login_container .login_form_label_field{padding-top:4px}.menu_login_container .html7magic label{color:#fff;font-weight:normal;padding-left:1px}#facebook .tetra_fonts .html7magic label{font-family:SFProText-Medium, Helvetica, Arial, sans-serif}#facebook .tetra_fonts .login_form_input_box{font-family:SFProText-Regular, Helvetica, Arial, sans-serif}#facebook .tetra_fonts .login_form_input_box::-webkit-input-placeholder{color:#8d949e}#facebook .tetra_fonts .login_form_login_button input{font-family:SFProText-Bold, Helvetica, Arial, sans-serif;font-weight:bold}#facebook .tetra_fonts .login_form_label_field a{color:#fff;font-family:SFProText-Regular, Helvetica, Arial, sans-serif}.new_header_style .login_form_label_field{text-align:right}.new_header_style.menu_login_container table tr td.login_form_label_field{padding-top:4px}.new_header_style .login_form_label_field a{font-size:13px;line-height:20px}.new_header_style .inputtext,.new_header_style .inputpassword{border-color:#082b61;border-radius:6px;box-sizing:border-box;font-size:13px;line-height:20px;margin:0;padding:8px 12px;width:194px}.white_background.new_header_style .inputtext,.white_background.new_header_style .inputpassword{width:210px}.new_header_style.menu_login_container{width:412px}.white_background.new_header_style.menu_login_container{width:444px}.new_blue_header .inputtext,.new_blue_header .inputpassword{border:none}.new_header_style .login_form_login_button input{font-size:18px;line-height:20px;padding:6px 26px}.new_header_style .login_form_login_button{border-radius:6px}.new_blue_header .login_form_login_button{background-color:#0e52b0;border:none}.menu_login_container #email{direction:ltr}.login_form_standalone_labels .inputtext,.login_form_standalone_labels .inputpassword{border-color:#96a6c5;font-size:16px;padding:6px;width:250px}.login_form_standalone_labels label{color:#1d2a5b;font-size:13px;font-weight:normal}.login_form_standalone_labels .login_form_label_field a{color:#365899;font-size:13px}.login_form_standalone_labels td.html7magic{text-align:right}.login_form_standalone_labels .uiButton input{font-size:13px;padding:3px 25px 5px}table.login_form_standalone_labels tr td{height:30px;padding:0;vertical-align:middle} .loggedout_menubar_container{height:82px;min-width:980px}.newHeaderMenuBar .loggedout_menubar_container{height:90px}.loggedout_menubar{margin:0 auto;padding-top:13px;width:980px}.newHeaderMenuBar .loggedout_menubar{padding-bottom:8px;padding-top:20px}.loggedout_menubar .fb_logo{margin-top:17px}.newHeaderMenuBar .loggedout_menubar .fb_logo{margin-top:4px}.loggedout_menubar .fb_icon_logo{margin-top:12px}@media (-webkit-min-device-pixel-ratio: 2),(min-resolution: 2dppx){.loggedout_menubar i.fb_logo{background-image:url(/rsrc.php/v3/y4/r/gf6iHxsw8zm.png);background-position:0 0;background-size:100% 100%}}.loggedout_menubar label.menu_login_show_link{color:#9cb4d8;position:relative;top:19px} ._lwx{position:relative} .signupBanner div.signup_bar_container{background-color:transparent}.signupBanner .signup_box{margin:0 auto;padding:0;position:relative;width:980px}.signupBanner .signup_btn{left:180px;position:absolute;top:-46px}.signupBanner .signup_btn_thickbar{left:180px;position:absolute;top:-70px}.signup_area{margin-top:23px}.timelineLayoutLoggedOut .signup_btn{left:250px} .signupBanner .signup_bar_container{background-color:transparent}.signupBanner .signup_box{margin:0 auto;position:relative;width:980px}.signupBanner .signup_btn{left:180px;padding-bottom:2px;padding-top:2px;position:absolute;top:-50px}.signupBanner .signup_btn_thickbar{left:180px;position:absolute;top:-70px}.signup_area{margin-top:23px}.timelineLayoutLoggedOut .signup_btn{left:250px} ._53jh{background-color:#3b5998;background-image:linear-gradient(#4e69a2, #3b5998 50%);border-bottom:1px solid #133783;min-height:42px;position:relative;z-index:1}._53jh._8f2f{background-color:#1877f2;background-image:none;border-bottom:none}.tinyViewport ._53jh{min-width:-webkit-max-content;min-width:max-content} ._52ju{text-align:left}._52jv{text-align:center}._52jw{text-align:right} .uiBoxGray{background-color:#f2f2f2;border:1px solid #ccc}.uiBoxDarkgray{color:#ccc;background-color:#333;border:1px solid #666}.uiBoxGreen{background-color:#d1e6b9;border:1px solid #629824}.uiBoxLightblue{background-color:#edeff4;border:1px solid #d8dfea}.uiBoxRed{background-color:#ffebe8;border:1px solid #dd3c10}.uiBoxWhite{background-color:#fff;border:1px solid #ccc}.uiBoxYellow{background-color:#fff9d7;border:1px solid #e2c822}.uiBoxOverlay{background:rgba(255, 255, 255, .85);border:1px solid #3b5998;border:1px solid rgba(59, 89, 153, .65);zoom:1}.noborder{border:none}.topborder{border-bottom:none;border-left:none;border-right:none}.bottomborder{border-left:none;border-right:none;border-top:none}.dashedborder{border-style:dashed} .pas{padding:5px}.pa8{padding:8px}.pam{padding:10px}.pa16{padding:16px}.pal{padding:20px}.pts{padding-top:5px}.pt8{padding-top:8px}.ptm{padding-top:10px}.pt16{padding-top:16px}.ptl{padding-top:20px}.prs{padding-right:5px}.pr8{padding-right:8px}.prm{padding-right:10px}.pr16{padding-right:16px}.prl{padding-right:20px}.pbs{padding-bottom:5px}.pb8{padding-bottom:8px}.pbm{padding-bottom:10px}.pb16{padding-bottom:16px}.pbl{padding-bottom:20px}.pls{padding-left:5px}.pl8{padding-left:8px}.plm{padding-left:10px}.pl16{padding-left:16px}.pll{padding-left:20px}.phs{padding-left:5px;padding-right:5px}.ph8{padding-left:8px;padding-right:8px}.phm{padding-left:10px;padding-right:10px}.ph16{padding-left:16px;padding-right:16px}.phl{padding-left:20px;padding-right:20px}.pvs{padding-top:5px;padding-bottom:5px}.pv8{padding-bottom:8px;padding-top:8px}.pvm{padding-top:10px;padding-bottom:10px}.pv16{padding-bottom:16px;padding-top:16px}.pvl{padding-top:20px;padding-bottom:20px}.mas{margin:5px}.ma8{margin:8px}.mam{margin:10px}.ma16{margin:16px}.mal{margin:20px}.mts{margin-top:5px}.mt8{margin-top:8px}.mtm{margin-top:10px}.mt16{margin-top:16px}.mtl{margin-top:20px}.mrs{margin-right:5px}.mr8{margin-right:8px}.mrm{margin-right:10px}.mr16{margin-right:16px}.mrl{margin-right:20px}.mbs{margin-bottom:5px}.mb8{margin-bottom:8px}.mbm{margin-bottom:10px}.mb16{margin-bottom:16px}.mbl{margin-bottom:20px}.mls{margin-left:5px}.ml8{margin-left:8px}.mlm{margin-left:10px}.ml16{margin-left:16px}.mll{margin-left:20px}.mhs{margin-left:5px;margin-right:5px}.mh8{margin-left:8px;margin-right:8px}.mhm{margin-left:10px;margin-right:10px}.mh16{margin-left:16px;margin-right:16px}.mhl{margin-left:20px;margin-right:20px}.mvs{margin-top:5px;margin-bottom:5px}.mv8{margin-bottom:8px;margin-top:8px}.mvm{margin-top:10px;margin-bottom:10px}.mv16{margin-bottom:16px;margin-top:16px}.mvl{margin-top:20px;margin-bottom:20px} .fss{font-size:9px}.fsm{font-size:12px}.fsl{font-size:14px}.fsxl{font-size:16px}.fsxxl{font-size:18px}.fwn{font-weight:normal}.fwb{font-weight:600}.fcb{color:#333}.fcg{color:#90949c}.fcw{color:#fff} .uiButton{border-radius:2px;cursor:pointer;display:inline-block;font-size:12px;-webkit-font-smoothing:antialiased;font-weight:bold;line-height:18px;padding:2px 6px;text-align:center;text-decoration:none;text-shadow:none;vertical-align:top;white-space:nowrap}.uiButton,.uiButtonSuppressed:active,.uiButtonSuppressed:focus,.uiButtonSuppressed:hover{background-color:#f5f6f7;border:1px solid #ccd0d5}.uiButton+.uiButton{margin-left:4px}.uiButton:hover{background-color:#ebedf0;text-decoration:none}.uiButton:active,.uiButtonDepressed{background-color:#dddfe2;border-color:#bec3c9}.uiButton .img{margin-top:3px;overflow:hidden;vertical-align:top}.uiButtonLarge .img{margin-top:4px}.uiButton .customimg{margin-top:1px}.uiButtonText,.uiButton input{background:none;border:0;color:#4b4f56;cursor:pointer;display:inline-block;font-family:Helvetica, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:18px;margin:0;padding:0;white-space:nowrap}.uiButtonOverlay,.uiButtonOverlay:hover{background-clip:padding-box;background-color:rgba(255, 255, 255, .8);background-image:none;border-color:#a5a5a5;border-color:rgba(0, 0, 0, .35);border-radius:2px;position:relative}.uiButtonOverlay:focus,.uiButtonOverlay:active{background-color:#f5f6f7;background-color:rgba(249, 250, 252, .9);border-color:#365899;border-color:rgba(59, 89, 152, .5)}form.async_saving .uiButton.uiButtonOverlay,.uiButtonOverlay.uiButtonDisabled,.uiButtonOverlay.uiButtonDisabled:active,.uiButtonOverlay.uiButtonDisabled:focus,.uiButtonOverlay.uiButtonDisabled:hover{background-color:rgba(255, 255, 255, .8);border-color:#ccc;border-color:rgba(180, 180, 180, .8)}.uiButtonOverlay.uiButtonDepressed{background-color:rgba(0, 0, 0, .05)}.uiButtonOverlay:before{background-color:rgba(0, 0, 0, .02);bottom:0;content:&#39;&#39;;left:0;position:absolute;right:0;top:0}.uiButtonOverlay:hover:before{background-color:rgba(0, 0, 0, .08)}.uiButtonSpecial{background-color:#42b72a;border-color:#42b72a}.uiButtonSpecial:hover{background-color:#36a420;border-color:#36a420}.uiButtonSpecial:active,.uiButtonSpecial.uiButtonDepressed{background-color:#2b9217;border-color:#2b9217}form.async_saving .uiButton.uiButtonSpecial,.uiButtonSpecial.uiButtonDisabled,.uiButtonSpecial.uiButtonDisabled:active,.uiButtonSpecial.uiButtonDisabled:focus,.uiButtonSpecial.uiButtonDisabled:hover{background-color:#ace0a2;border-color:#ace0a2}.uiButtonConfirm{background-color:#4267b2;border-color:#29487d}.uiButtonConfirm:hover{background-color:#365899;border-color:#29487d}.uiButtonConfirm:active,.uiButtonConfirm.uiButtonDepressed{background-color:#29487d;border-color:#29487d}form.async_saving .uiButton.uiButtonConfirm,.uiButtonConfirm.uiButtonDisabled,.uiButtonConfirm.uiButtonDisabled:active,.uiButtonConfirm.uiButtonDisabled:focus,.uiButtonConfirm.uiButtonDisabled:hover{background-color:#9cb4d8;border-color:#9cb4d8}form.async_saving .uiButton.uiButtonSpecial .uiButtonText,form.async_saving .uiButton.uiButtonSpecial input,form.async_saving .uiButton.uiButtonConfirm .uiButtonText,form.async_saving .uiButton.uiButtonConfirm input,.uiButtonSpecial .uiButtonText,.uiButtonSpecial input,.uiButtonSpecial.uiButtonDisabled .uiButtonText,.uiButtonSpecial.uiButtonDisabled input,.uiButtonConfirm .uiButtonText,.uiButtonConfirm input,.uiButtonConfirm.uiButtonDisabled .uiButtonText,.uiButtonConfirm.uiButtonDisabled input{color:#fff}form.async_saving .uiButton,.uiButtonDisabled,.uiButtonDisabled:active,.uiButtonDisabled:focus,.uiButtonDisabled:hover{background-color:#f5f6f7;border-color:#dddfe2}form.async_saving .uiButton .img,.uiButtonDisabled .img{opacity:.5}form.async_saving .uiButtonText,form.async_saving .uiButton input,.uiButtonDisabled .uiButtonText,.uiButtonDisabled input{color:#bec3c9}form.async_saving .uiButton,form.async_saving .uiButtonText,form.async_saving .uiButton input,.uiButtonDepressed,.uiButtonDepressed .uiButtonText,.uiButtonDepressed input,.uiButtonDisabled,.uiButtonDisabled .uiButtonText,.uiButtonDisabled input{cursor:default}.uiButtonDepressed:not(.uiButtonSpecial):not(.uiButtonConfirm) .uiButtonText,.uiButtonDepressed:not(.uiButtonSpecial):not(.uiButtonConfirm) input{color:#4080ff}.uiButtonLarge,.uiButtonLarge .uiButtonText,.uiButtonLarge input{font-size:13px;line-height:19px}.uiButtonSuppressed{background:none;border-color:transparent}.uiButtonNoText .img{margin-left:-1px;margin-right:-1px}.uiButtonNoText input{vertical-align:top} .uiHeader h1{color:#162643;font-size:20px}.uiHeader h2{color:#162643;font-size:16px}.uiHeader h2 a{color:#162643}.uiHeader h3,.uiHeader h4{color:#333;font-size:12px}.uiHeader h5,.uiHeader h6{color:#666}.uiHeader .uiHeaderTitle{outline:none}.uiHeaderWithImage .uiHeaderTop{position:relative}.uiHeaderWithImage .uiHeaderTitle{padding-left:22px}.uiHeaderImage{left:0;position:absolute}.uiHeader h2 .uiHeaderImage{top:2px}.uiHeaderTopBorder{border-top:1px solid #aaa;padding-top:.5em}div.uiHeaderTopBorder{margin-left:0}.uiHeaderTopAndBottomBorder{border-bottom:1px solid #e9e9e9;border-top:1px solid #aaa;padding:5px 0}.uiHeaderMiddleBorder{border-bottom:1px solid #ccc;height:.8em;margin:.5em 0 1.5em 0;position:relative}.uiHeaderMiddleBorder .uiHeaderTitle,.uiHeaderMiddleBorder .uiHeaderActions{background-color:#fff;position:absolute;top:0}.uiHeaderMiddleBorder .uiHeaderTitle{left:0;padding-right:.5em}.uiHeaderMiddleBorder .uiHeaderActions{padding-left:.5em;right:0}.uiHeaderMiddleBorder .uiButton{margin-top:-2px}.uiHeaderBottomBorder{border-bottom:1px solid #aaa;padding-bottom:.5em}.uiHeaderPage{padding:6px 0 16px}.uiHeaderPage .uiHeaderTitle{line-height:20px;min-height:20px;padding-bottom:2px;vertical-align:bottom}.uiHeaderPage .uiHeaderActions{margin-top:-1px}.uiHeaderPage .uiHeaderTop .fsl{margin-top:3px}.uiHeaderNav{border-color:#ebedf0;margin:8px 0 0 6px;padding:7px 6px 3px 5px}.uiHeaderNavEmpty{padding-top:6px}.uiHeaderNav h4{color:#7f7f7f}.uiHeaderSection,.uiSideHeader{background-color:#f5f6f7;border-bottom:none;border-top:solid 1px #e9ebee;padding:4px 6px 5px} .uiInterstitial{border-radius:4px;margin-left:auto;margin-right:auto}.uiInterstitialSmall{width:445px}.uiInterstitialLarge{width:555px}.uiInterstitialXLarge{width:620px}.uiInterstitial .interstitialHeader{border-color:#ccc;padding-bottom:.5em}.fullBleed .interstitialHeader{margin:0;padding:4px 12px 10px}.uiInterstitialContent{margin-bottom:15px}.fullBleed .uiInterstitialContent{margin:0;padding:0}.uiInterstitialBar{border-bottom-right-radius:3px;border-bottom-left-radius:3px;-webkit-border-bottom-left-radius:3px;-webkit-border-bottom-right-radius:3px;line-height:16px;padding:8px 10px}div.uiInterstitialWithStripes{background:transparent url(/rsrc.php/v3/y9/r/y7MG8IZpiC8.gif) repeat-x;padding-top:15px} ._2qgu._2qgu{border-radius:50%;overflow:hidden}._2s25._2s25._606w._606w:after,._606w:after{border-radius:50%} a._p{display:block} ._4jy0{border:1px solid;border-radius:2px;box-sizing:content-box;font-size:12px;-webkit-font-smoothing:antialiased;font-weight:bold;justify-content:center;padding:0 8px;position:relative;text-align:center;text-shadow:none;vertical-align:middle}.segoe ._4jy0{font-weight:600}._4jy0:before{content:&#39;&#39;;display:inline-block;height:20px;vertical-align:middle}html ._4jy0:focus{box-shadow:0 0 1px 2px rgba(88, 144, 255, .75), 0 1px 1px rgba(0, 0, 0, .15);outline:none}._19_u ._4jy0:focus,._4jy0._5f0v:focus{box-shadow:none}._4jy0{transition:200ms cubic-bezier(.08,.52,.52,1) background-color, 200ms cubic-bezier(.08,.52,.52,1) box-shadow, 200ms cubic-bezier(.08,.52,.52,1) transform}._4jy0:active{transition:none}.mac ._4jy0:not(._42fr):active{box-shadow:none;transform:scale(.98)}._4jy0 .img{bottom:1px;position:relative;vertical-align:middle}form.async_saving ._4jy0 .img,a.async_saving._4jy0 .img,._4jy0._42fr .img{opacity:.5}._517h,._59pe:focus,._59pe:hover{background-color:#f5f6f7;border-color:#ccd0d5;color:#4b4f56}._64lx ._517h,._64lx ._59pe:focus,._64lx ._59pe:hover{background-color:#eff1f3;border-color:#bec3c9}._517h:hover{background-color:#ebedf0}._517h:active,._517h._42fs{background-color:#dddfe2;border-color:#bec3c9}form.async_saving ._517h,a.async_saving._517h,._517h._42fr{background-color:#f5f6f7;border-color:#dddfe2;color:#bec3c9}._517h._42fs{color:#4080ff}._4jy1,._9w8q,._4jy2{color:#fff}._4jy1{background-color:#4267b2;border-color:#4267b2}._4jy1:hover{background-color:#365899;border-color:#365899}._4jy1:active,._4jy1._42fs{background-color:#29487d;border-color:#29487d}form.async_saving ._4jy1,a.async_saving._4jy1,._4jy1._42fr{background-color:#9cb4d8;border-color:#9cb4d8}._4jy2{background-color:#42b72a;border-color:#42b72a}._4jy2:hover{background-color:#36a420;border-color:#36a420}._4jy2:active,._4jy2._42fs{background-color:#2b9217;border-color:#2b9217}form.async_saving ._4jy2,a.async_saving._4jy2,._4jy2._42fr{background-color:#ace0a2;border-color:#ace0a2}._9w8q{background-color:#fa3e3e;border-color:#fa3e3e}._9w8q:hover{background-color:#db1d24;border-color:#db1d24}._9w8q:active,._9w8q._42fs{background-color:#c70b11;border-color:#c70b11}form.async_saving ._9w8q,a.async_saving._9w8q,._9w8q._42fr{background-color:#f77c7c;border-color:#f77c7c}._59pe,form.async_saving ._59pe,a.async_saving._59pe,._59pe._42fr{background:none;border-color:transparent}._517i,._517i._42fr:active,._517i._42fr._42fs{height:18px;line-height:18px}._4jy3,._4jy3._42fr:active,._4jy3._42fr._42fs{line-height:22px}._4jy4,._4jy4._42fr:active,._4jy4._42fr._42fs{line-height:26px;padding:0 10px}._4jy5,._4jy5._42fr:active,._4jy5._42fr._42fs{line-height:34px;padding:0 16px}._4jy6,._4jy6._42fr:active,._4jy6._42fr._42fs{line-height:42px;padding:0 24px}._51xa ._4jy0{border-radius:0;display:inline-block;margin:0!important;margin-left:-1px!important;position:relative;z-index:1}._51xa&gt;._4jy0:first-child,._51xa&gt;:first-child ._4jy0{border-radius:2px 0 0 2px;margin-left:0!important}._51xa&gt;._4jy0:last-child,._51xa&gt;:last-child ._4jy0{border-radius:0 2px 2px 0}._51xa&gt;._4jy0:only-child,._51xa&gt;:only-child ._4jy0{border-radius:2px}._51xa ._4jy0._42fr{z-index:0}._51xa ._4jy0._4jy1,._51xa ._4jy0._9w8q,._51xa ._4jy0._4jy2{z-index:2}._51xa ._4jy0:focus{z-index:3}._51xa ._4jy1+.uiPopover&gt;._4jy1:not(:focus):after{background-color:#f5f6f7;bottom:-1px;content:&#39;&#39;;display:block;left:-1px;position:absolute;top:-1px;width:1px}._4jy0._52nf{cursor:default}._9c6._9c6{background-clip:padding-box;border-color:rgba(0, 0, 0, .4)}._3y89 ._4jy0{border-bottom-width:0;border-top-width:0}._3y89&gt;._4jy0:first-child,._3y89&gt;:first-child ._4jy0{border-left-width:0;border-radius:1px 0 0 1px}._3y89&gt;._4jy0:last-child,._3y89&gt;:last-child ._4jy0{border-radius:0 1px 1px 0;border-right-width:0}._6n1z._4jy6,._6n1z._4jy6._42fr:active,._6n1z._4jy6._42fr._42fs{padding:0 0}._6n1z._517h,._6n1z._59pe:focus,._6n1z._59pe:hover{background-color:#fff;border-color:transparent} .UIPage_LoggedOut .UIFullPage_Container,.UIPage_LoggedOut .UIStandardFrame_Container{padding-bottom:46px;padding-top:46px;width:auto}.UIPage_LoggedOut .fbPhotosGrid .photoDetails{width:inherit} ._86k6{color:#1c1e21;font-family:SFProText-Regular, Segoe UI, Arial, sans-serif!important;font-size:13px;line-height:16px;white-space:nowrap}@media only screen and (max-width: 768px){._86k6{display:none}} ._86k9{box-sizing:border-box;display:block;margin-left:auto;margin-right:auto;margin-top:16px;max-width:1200px}._8e0v{padding:32px 0}._8e0w{align-items:flex-start;border-top:1px solid #ccd0d5;display:flex;justify-content:space-between;padding:32px 0}@media only screen and (max-width: 768px){._86k9{padding:16px;width:100%}._8e0v{display:none}} ._86k7{color:#8d949e;display:inline-block;padding-right:20px;padding-top:0}._86k7 li&gt;a{color:#1c1e21;font-family:SFProText-Semibold, Segoe UI, Arial!important;font-size:13px}._86k8.localeSelectorList.uiList{padding-top:0}@media only screen and (max-width: 768px){._86k7{display:block;margin-bottom:0;max-width:100%;padding-right:0;width:100%}._86k8.localeSelectorList.uiList&gt;li{display:inline-block;font-size:12px;font-weight:bold;padding-left:0;text-align:center;width:50%}._86k8&gt;li&gt;a{color:#8d8b8a;font-weight:normal}._86jz{border:1px solid #365899;border-radius:3px;color:#1479fb;display:block;font-size:large;height:18px;line-height:17px;margin:0 auto;text-align:center;width:18px}} ._86jx{display:inline-block;font-family:SFProText-Semibold, Segoe UI, Arial!important;font-size:13px;line-height:16px;padding-right:16px}._86jx:last-child{padding-right:0}._86jx&gt;a{color:#1c1e21}@media only screen and (max-device-width: 768px){._86jy{display:none}} ._4b21{background-color:#fff;height:60px;margin:0 auto;padding-bottom:16px;position:relative;width:980px}@media only screen and (max-width: 500px){._4b21{width:100%}}._40q1{background-color:#fff}._5wct{color:#000;display:inline;font-family:HelveticaNeue-Light, Helvetica Neue Light, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:24px;line-height:32px;max-width:900px;position:absolute;top:16px}._4b23{margin-right:12px;margin-top:10px}._2084{display:inline;float:right;font-size:14px;line-height:87px}#facebook ._1m39._1m3f{background:white;border:1px solid #4778ff;color:#4778ff}#facebook ._1m39._1m3f:active{background-color:#f5f6f7} .Work_UIPage_LoggedOut{background-color:#fff} ._4ki&gt;li{border-width:0 0 0 1px;display:inline-block}._4kg&gt;li{border-width:1px 0 0 0}._509-&gt;li{vertical-align:top}._509_&gt;li{vertical-align:middle}._50a0&gt;li{vertical-align:bottom}.uiList&gt;li:first-child{border-width:0}._4ks&gt;li{border-color:#ebedf0;border-style:solid}._4kt&gt;li{border-color:#ccc;border-style:solid}._4ku&gt;li{border-color:#aaa;border-style:solid}._4of{color:#365899;list-style-type:square;margin-left:12px}._7lda{list-style-type:disc;margin-left:16px}._7lda&gt;._7ldb{text-indent:-2px}._4ki._703&gt;li{padding-left:20px;padding-right:20px}._4ki._704&gt;li{padding-left:5px;padding-right:5px}._4ki._6-j&gt;li{padding-left:10px;padding-right:10px}._4ki._6-i&gt;li{padding-right:0}._4kg._704&gt;li{padding-top:5px;padding-bottom:5px}._4kg._6-j&gt;li{padding-top:10px;padding-bottom:10px}._4kg._703&gt;li{padding-top:20px;padding-bottom:20px}._4kg._6-i&gt;li{padding-bottom:0}._4kg._6-h&gt;li:first-child{padding-top:0}._4kg._6-h&gt;li:last-child{padding-bottom:0}._4ki._6-h&gt;li:first-child{padding-left:0}._4ki._6-h&gt;li:last-child{padding-right:0} ._8tm{padding:0}._2phz{padding:4px}._2ph-{padding:8px}._2ph_{padding:12px}._2pi0{padding:16px}._2pi1{padding:20px}._40c7{padding:24px}._2o1j{padding:36px}._6buq{padding-bottom:0;padding-top:0}._2pi2{padding-bottom:4px;padding-top:4px}._2pi3{padding-bottom:8px;padding-top:8px}._2pi4{padding-bottom:12px;padding-top:12px}._2pi5{padding-bottom:16px;padding-top:16px}._2pi6{padding-bottom:20px;padding-top:20px}._2o1k{padding-bottom:24px;padding-top:24px}._2o1l{padding-bottom:36px;padding-top:36px}._6bua{padding-left:0;padding-right:0}._2pi7{padding-left:4px;padding-right:4px}._2pi8{padding-left:8px;padding-right:8px}._2pi9{padding-left:12px;padding-right:12px}._2pia{padding-left:16px;padding-right:16px}._2pib{padding-left:20px;padding-right:20px}._2o1m{padding-left:24px;padding-right:24px}._2o1n{padding-left:36px;padding-right:36px}._iky{padding-top:0}._2pic{padding-top:4px}._2pid{padding-top:8px}._2pie{padding-top:12px}._2pif{padding-top:16px}._2pig{padding-top:20px}._2owm{padding-top:24px}._div{padding-right:0}._2pih{padding-right:4px}._2pii{padding-right:8px}._2pij{padding-right:12px}._2pik{padding-right:16px}._2pil{padding-right:20px}._31wk{padding-right:24px}._2phb{padding-right:32px}._au-{padding-bottom:0}._2pim{padding-bottom:4px}._2pin{padding-bottom:8px}._2pio{padding-bottom:12px}._2pip{padding-bottom:16px}._2piq{padding-bottom:20px}._2o1p{padding-bottom:24px}._4gao{padding-bottom:32px}._1cvx{padding-left:0}._2pir{padding-left:4px}._2pis{padding-left:8px}._2pit{padding-left:12px}._2piu{padding-left:16px}._2piv{padding-left:20px}._2o1q{padding-left:24px}._2o1r{padding-left:36px} .sp_Awgqz7K4lHq{background-image:url(/rsrc.php/v3/y-/r/VcstZr4fYTz.png);background-size:auto;background-repeat:no-repeat;display:inline-block;height:20px;width:20px}.sp_Awgqz7K4lHq.sx_a37d90{width:282px;height:250px;background-position:0 0}.sp_Awgqz7K4lHq.sx_7df8b7{background-position:-171px -251px}.sp_Awgqz7K4lHq.sx_98f749{background-position:-192px -251px}.sp_Awgqz7K4lHq.sx_976ed2{width:105px;height:40px;background-position:0 -286px}.sp_Awgqz7K4lHq.sx_b035c3{height:11px;background-position:-213px -251px}.sp_Awgqz7K4lHq.sx_f315b2{width:16px;height:16px;background-position:-106px -286px}.sp_Awgqz7K4lHq.sx_08e58c{width:16px;height:16px;background-position:-123px -286px}.sp_Awgqz7K4lHq.sx_d7bd95{width:5px;height:14px;background-position:-145px -286px}.selected .sp_Awgqz7K4lHq.sx_d7bd95{background-position:-140px -286px}.sp_Awgqz7K4lHq.sx_bbc862{width:9px;height:5px;background-position:-234px -251px}.sp_Awgqz7K4lHq.sx_55d19b{width:170px;height:34px;background-position:0 -251px}.sp_Awgqz7K4lHq.sx_60b650{width:12px;height:12px;background-position:-171px -272px}/*FB_PKG_DELIM*/ #bootloader_3Bb3Baa{height:42px;}.bootloader_3Bb3Baa{display:block!important;} https://account.rogers.com/?from_ts=for posted by Baby Papalegba @ June 21, 2023  3 comments   3 Comments: At June 21, 2023 at 9:05 PM , Blogger Baby Papalegba said... Get royolties too    At June 21, 2023 at 9:59 PM , Blogger Baby Papalegba said... Own Your Word against dublication and reproduction that&#39;s epic like a super star does }&lt;write something with out there promissory approval what happens {    At June 30, 2023 at 2:51 PM , Blogger Baby Papalegba said... https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&amp;fbclid=IwAR0L0BwQRtAkf6_ot8HPmUZzr0mGDl0TVNxEw3Nv8w7bDVAnS8NO1HJexnQ    Post a Comment  Subscribe to Post Comments [Atom]  &lt;&lt; Home  About Me My Photo Name: Baby Papalegba Location: Ottawa, Ontario , Canada View my complete profile  Previous Posts Powered by Blogger  Subscribe to Posts [Atom]   )Chodum91-patch-6 ...https://embed.tumblr.com/embed/post/t:iPRP096YDH4tAP9ETV9_tg/720127509506736128/v2https://www.tumblr.com/darkdose-75/719933067816534016/245040906-ea6c92a1-4c9f-43b1-a4c0-bce44758b0bejpg?source=share -[&lt;!DOCTYPE html&gt;[Chodum91-patch-6](https://developers.google.com/speed/libraries)&lt;html lang=\&quot;en\&quot;&gt; &lt;head&gt;  &lt;meta charset=\&quot;UTF-8\&quot;&gt;  &lt;title&gt;READ JSON Example (getJSON)&lt;/title&gt;  &lt;script type=\&quot;text/javascript\&quot; src=\&quot;https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\&quot;&gt;&lt;/script&gt; Papalegba.org Papa.Legba.N.B. [ ](https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&amp;fbclid=IwAR1ZbUO1DJ61e7HmSaCGWy31OK6394QPyu4CRI0fvbdZk0SdVIBDygBp46s)AMMA •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• MAMA April 11, 2023 •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}  } menu {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• background: #fff; border-radius: 4px; color: #202124; cursor: var(--hterm-mouse-cursor-pointer); display: none; filter: drop-shadow(0 1px 3px #3C40434D) drop-shadow(0 4px 8px #3C404326); margin: 0; padding: 8px 0; position: absolute; transition-duration: 200ms; }(function( ¹♤³ www.rainwizzard@b logspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}){^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}  _{_~_•^^^• ¹♤³ www.rainwizzard@blogspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}var hasFrame = window.parent!=window, Aerial view of shipping containers. scripts = document.getElementsByTagName(&#39;script&#39;), current = scripts[scripts.length-1], config = current.getAttribute(&#39;data-config&#39;), head = document.getElementsByTagName(\&quot;head\&quot;)[0], dest = location.href.replace(/scmplayer\\=true/g, &#39;scmplayer=false&#39;), destHost = dest.substr(0,dest.indexOf(&#39;/&#39;,10)), scm = current.getAttribute(&#39;src&#39;).replace(/script\\.js.*/g,&#39;scm.html?03022013&#39;)+&#39;#&#39;+dest, scmHost = scm.substr(0,scm.indexOf(&#39;/&#39;,10)), isOutside = !hasFrame || location.href.indexOf(\&quot;scmplayer=true\&quot;)&gt;0, postMessage = function(msg){ return window.top.document.getElementById(&#39;scmframe&#39;) .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(&#39;,&#39;), post = function(key){ return function(arg){ var argStr = &#39;&#39;; if(typeof(arg)!=&#39;undefined&#39;) argStr = (key.match(/(play|queue)/) ? &#39;new Song(&#39;:&#39;(&#39;) + JSON.stringify(arg)+&#39;)&#39;; postMessage(&#39;SCM.&#39;+key+&#39;(&#39;+argStr+&#39;)&#39;); } }; for(var i=0;i&#39;, all[0] ); return v &gt; 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = &#39;html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} &#39;; var style = document.createElement(&#39;style&#39;); style.type = &#39;text/css&#39;; style.id = &#39;scmcss&#39;; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\&quot;scmcss\&quot;) head.removeChild(head.firstChild); */ var scmframe = document.createElement(&#39;iframe&#39;); scmframe.frameBorder = 0; scmframe.id = \&quot;scmframe\&quot;; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,&#39;load&#39;,function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,&#39;resize&#39;,function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == &#39;number&#39; ) return window.innerHeight; else if( document.documentElement &amp;&amp; document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body &amp;&amp; document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,&#39;&#39;); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,&#39;blogspot.com&#39;); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,&#39;&#39;); return host; }; addEvent(document.body,&#39;click&#39;,function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) &amp;&amp; tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) &amp;&amp; !tar.href.match(/.(jpg|png)$/i) &amp;&amp; //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf(&#39;#&#39;)==0){ //hash if(tar.href != \&quot;#\&quot;){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,&#39;&#39;); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open(&#39;http://scmplayer.net/#skin=&#39;+tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link &amp; has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),&#39;&#39;); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,&#39;load&#39;,function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, &#39;queue,play,pause,next,previous,volume,skin,placement,&#39;+ loadPlaylist,repeatMode,isShuffle,showPlaylist,&#39;+ &#39;togglePlaylist,toggleShuffle,changeRepeatMode&#39;); if(window.SCM &amp;&amp; &#39;window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();-(function(){ var hasFrame = window.parent!=window, scripts = document.getElementsByTagName(&#39;script&#39;), current = scripts[scripts.length-1], config = current.getAttribute(&#39;data-config&#39;), head = document.getElementsByTagName(\&quot;head\&quot;)[0], dest = location.href.replace(/scmplayer\\=true/g, &#39;scmplayer=false&#39;), destHost = dest.substr(0,dest.indexOf(&#39;/&#39;,10)), scm = current.getAttribute(&#39;src&#39;).replace(/script\\.js.*/g,&#39;scm.html?03022013&#39;)+&#39;#&#39;+dest, scmHost = scm.substr(0,scm.indexOf(&#39;/&#39;,10)), isOutside = !hasFrame || location.href.indexOf(\&quot;scmplayer=true\&quot;)&gt;0, postMessage = function(msg){ return window.top.document.getElementById(&#39;scmframe&#39;) .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(&#39;,&#39;), post = function(key){ return function(arg){ var argStr = &#39;&#39;; if(typeof(arg)!=&#39;undefined&#39;) argStr = (key.match(/(play|queue)/) ? &#39;new Song(&#39;:&#39;(&#39;) + JSON.stringify(arg)+&#39;)&#39;; postMessage(&#39;SCM.&#39;+key+&#39;(&#39;+argStr+&#39;)&#39;); } }; for(var i=0;i&#39;, all[0] ); return v &gt; 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = &#39;html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} &#39;; var style = document.createElement(&#39;style&#39;); style.type = &#39;text/css&#39;; style.id = &#39;scmcss&#39;; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\&quot;scmcss\&quot;) head.removeChild(head.firstChild); */ var scmframe = document.createElement(&#39;iframe&#39;); scmframe.frameBorder = 0; scmframe.id = \&quot;scmframe\&quot;; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,&#39;load&#39;,function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,&#39;resize&#39;,function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == &#39;number&#39; ) return window.innerHeight; else if( document.documentElement &amp;&amp; document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body &amp;&amp; document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,&#39;&#39;); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,&#39;blogspot.com&#39;); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,&#39;&#39;); return host; }; addEvent(document.body,&#39;click&#39;,function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) &amp;&amp; tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) &amp;&amp; !tar.href.match(/.(jpg|png)$/i) &amp;&amp; //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf(&#39;#&#39;)==0){ //hash if(tar.href != \&quot;#\&quot;){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,&#39;&#39;); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open(&#39;http://scmplayer.net/#skin=&#39;+tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link &amp; has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),&#39;&#39;); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,&#39;load&#39;,function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, &#39;queue,play,pause,next,previous,volume,skin,placement,&#39;+ &#39;loadPlaylist,repeatMode,isShuffle,showPlaylist,&#39;+ &#39;togglePlaylist,toggleShuffle,changeRepeatMode&#39;); if(window.SCM &amp;&amp; window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();--BEGIN CERTIFICATE-----MIIFWjCCA0KgAwIBAgIQbkepxUtHDA3sM9CJuRz04TANBgkqhkiG9w0BAQwFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMTYwNjIyMDAwMDAwWhcNMzYwNjIyMDAwMDAwWjBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC2EQKLHuOhd5s73L+UPreVp0A8of2C+X0yBoJx9vaMf/vo27xqLpeXo4xL+Sv2sfnOhB2x+cWX3u+58qPpvBKJXqeqUqv4IyfLpLGcY9vXmX7wCl7raKb0xlpHDU0QM+NOsROjyBhsS+z8CZDfnWQpJSMHobTSPS5g4M/SCYe7zUjwTcLCeoiKu7rPWRnWr4+wB7CeMfGCwcDfLqZtbBkOtdh+JhpFAz2weaSUKK0PfyblqAj+lug8aJRT7oM6iCsVlgmy4HqMLnXWnOunVmSPlk9orj2XwoSPwLxAwAtcvfaHszVsrBhQf4TgTM2S0yDpM7xSma8ytSmzJSq0SPly4cpk9+aCEI3oncKKiPo4Zor8Y/kB+Xj9e1x3+naH+uzfsQ55lVe0vSbv1gHR6xYKu44LtcXFilWr06zqkUspzBmkMiVOKvFlRNACzqrOSbTqn3yDsEB750Orp2yjj32JgfpMpf/VjsPOS+C12LOORc92wO1AK/1TD7Cn1TsNsYqiA94xrcx36m97PtbfkSIS5r762DL8EGMUUXLeXdYWk70paDPvOmbsB4om3xPXV2V4J95eSRQAogB/mqghtqmxlbCluQ0WEdrHbEg8QOB+DVrNVjzRlwW5y0vtOUucxD/SVRNuJLDWcfr0wbrM7Rv1/oFB2ACYPTrIrnqYNxgFlQIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQU5K8rJnEaK0gnhS9SZizv8IkTcT4wDQYJKoZIhvcNAQEMBQADggIBADiWCu49tJYeX++dnAsznyvgyv3SjgofQXSlfKqE1OXyHuY3UjKcC9FhHb8owbZEKTV1d5iyfNm9dKyKaOOpMQkpAWBz40d8U6iQSifvS9efk+eCNs6aaAyC58/UEBZvXw6ZXPYfcX3v73svfuo21pdwCxXu11xWajOl40k4DLh9+42FpLFZXvRq4d2h9mREruZRgyFmxhE+885H7pwoHyXa/6xmld01D1zvICxi/ZG6qcz8WpyTgYMpl0p8WnK0OdC3d8t5/Wk6kjftbjhlRn7pYL15iJdfOBL07q9bgsiG1eGZbYwE8na6SfZu6W0eX6DvJ4J2QPim01hcDyxC2kLGe4g0x8HYRZvBPsVhHdljUEn2NIVq4BjFbkerQUIpm/ZgDdIx02OYI5NaAIFItO/Nis3Jz5nu2Z6qNuFoS3FJFDYoOj0dzpqPJeaAcWErtXvM+SUWgeExX6GjfhaknBZqlxi9dnKlC54dNuYvoS++cJEPqOba+MSSQGwlfnuzCdyyF62ARPBopY+Udf90WuioAnwMCeKpSwughQtiue+hMZL77/ZRBIls6Kl0obsXs7X9SQ98POyDGCBDTtWTurQ0sR8WNh8M5mQ5Fkzc4P4dyKliPUDqysU0ArSuiYgzNdwsE3PYJ/HQcu51OyLemGhmW/HGY0dVHLqlCFF1pkgl-----END CERTIFICATE--(function(){ var hasFrame = window.parent!=window, scripts = document.getElementsByTagName(&#39;script&#39;), current = scripts[scripts.length-1], config = current.getAttribute(&#39;data-config&#39;), head = document.getElementsByTagName(\&quot;head\&quot;)[0], dest = location.href.replace(/scmplayer\\=true/g, &#39;scmplayer=false&#39;), destHost = dest.substr(0,dest.indexOf(&#39;/&#39;,10)), scm = current.getAttribute(&#39;src&#39;).replace(/script\\.js.*/g,&#39;scm.html?03022013&#39;)+&#39;#&#39;+dest, scmHost = scm.substr(0,scm.indexOf(&#39;/&#39;,10)), isOutside = !hasFrame || location.href.indexOf(\&quot;scmplayer=true\&quot;)&gt;0, postMessage = function(msg){ return window.top.document.getElementById(&#39;scmframe&#39;) .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(&#39;,&#39;), post = function(key){ return function(arg){ var argStr = &#39;&#39;; if(typeof(arg)!=&#39;undefined&#39;) argStr = (key.match(/(play|queue)/) ? &#39;new Song(&#39;:&#39;(&#39;) + JSON.stringify(arg)+&#39;)&#39;; postMessage(&#39;SCM.&#39;+key+&#39;(&#39;+argStr+&#39;)&#39;); } }; for(var i=0;i&#39;, all[0] ); return v &gt; 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = &#39;html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} &#39;; var style = document.createElement(&#39;style&#39;); style.type = &#39;text/css&#39;; style.id = &#39;scmcss&#39;; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\&quot;scmcss\&quot;) head.removeChild(head.firstChild); */ var scmframe = document.createElement(&#39;iframe&#39;); scmframe.frameBorder = 0; scmframe.id = \&quot;scmframe\&quot;; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,&#39;load&#39;,function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,&#39;resize&#39;,function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == &#39;number&#39; ) return window.innerHeight; else if( document.documentElement &amp;&amp; document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body &amp;&amp; document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,&#39;&#39;); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,&#39;blogspot.com&#39;); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,&#39;&#39;); return host; }; addEvent(document.body,&#39;click&#39;,function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) &amp;&amp; tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) &amp;&amp; !tar.href.match(/.(jpg|png)$/i) &amp;&amp; //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf(&#39;#&#39;)==0){ //hash if(tar.href != \&quot;#\&quot;){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,&#39;&#39;); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open(&#39;http://scmplayer.net/#skin=&#39;+tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,&#39;_blank&#39;); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link &amp; has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),&#39;&#39;); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,&#39;load&#39;,function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, &#39;queue,play,pause,next,previous,volume,skin,placement,&#39;+ &#39;loadPlaylist,repeatMode,isShuffle,showPlaylist,&#39;+ &#39;togglePlaylist,toggleShuffle,changeRepeatMode&#39;); if(window.SCM &amp;&amp; window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();-- menu {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• background: #fff; border-radius: 4px; color: #202124; cursor: var(--hterm-mouse-cursor-pointer); display: none; filter: drop-shadow(0 1px 3px #3C40434D) drop-shadow(0 4px 8px #3C404326); margin: 0; padding: 8px 0; position: absolute; transition-duration: 200ms; } menuitem { display:•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}{_~_•^^^• block •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• menuitem { display:•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}{_~_•^^^• block •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• _{_~_•^^^•le=\&quot;--hterm-cursor-color: #669DF680; --hterm-background-color: 32,33,36; --hterm-color-0: 60,64,67; --hterm-color-1: 242,139,130; --hterm-color-2: 19,115,86; --hterm-color-3: 227,116,0; --hterm-color-4: 138,180,248; --hterm-color-5: 238,95,250; --hterm-color-6: 3,191,200; --hterm-color-7: 255,255,255; --hterm-color-8: 154,160,166; --hterm-color-9: 246,174,169; --hterm-color-10: 135,255,197; --hterm-color-11: 253,214,99; --hterm-color-12: 174,203,250; --hterm-color-13: 244,181,251; --hterm-color-14: 128,249,249; --hterm-color-15: 248,249,250; --hterm-color-16: 0,0,0; --hterm-color-17: 0,0,95; --hterm-color-18: 0,0,135; --hterm-color-19: 0,0,175; --hterm-color-20: 0,0,215; --hterm-color-21: 0,0,255; --hterm-color-22: 0,95,0; --hterm-color-23: 0,95,95; --hterm-color-24: 0,95,135; --hterm-color-25: 0,95,175; --hterm-color-26: 0,95,215; --hterm-color-27: 0,95,255; --hterm-color-28: 0,135,0; --hterm-color-29: 0,135,95; --hterm-color-30: 0,135,135; --hterm-color-31: 0,135,175; --hterm-color-32: 0,135,215; --hterm-color-33: 0,135,255; --hterm-color-34: 0,175,0; --hterm-color-35: 0,175,95; --hterm-color-36: 0,175,135; --hterm-color-37: 0,175,175; --hterm-color-38: 0,175,215; --hterm-color-39: 0,175,255; --hterm-color-4…

---
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[c9978181a0...](https://github.com/greenhas/spg_website/commit/c9978181a0fa8b4504099d697b7d61e54d0639f7)
#### Saturday 2023-09-02 16:35:17 by Spencer Greenhalgh

post Today, I'm remembering the family friend from a Latter-day Saint congregation I grew up in who heard me in a church settng quote some scripture on the need for the rich to give to the poor and then took me aside to ask how liberal my school friends were and give me some cautionary advice.

---
## [OverDriveZ/coyote-bayou](https://github.com/OverDriveZ/coyote-bayou)@[4bf2519ee0...](https://github.com/OverDriveZ/coyote-bayou/commit/4bf2519ee041be11e499125516f3cb3954fc6cc8)
#### Saturday 2023-09-02 16:39:40 by Tk420634

t a b

fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you

---
## [brucerennie/NetHack](https://github.com/brucerennie/NetHack)@[38cda5ad52...](https://github.com/brucerennie/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Saturday 2023-09-02 16:56:30 by Michael Meyer

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
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[0f386c8188...](https://github.com/TeDGamer/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Saturday 2023-09-02 17:18:30 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [maxspells/fulpstation](https://github.com/maxspells/fulpstation)@[fc5620aa13...](https://github.com/maxspells/fulpstation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Saturday 2023-09-02 17:33:12 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[b0ec1e4098...](https://github.com/Helg2/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Saturday 2023-09-02 17:57:54 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

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

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a5aef3b823...](https://github.com/tgstation/tgstation/commit/a5aef3b823dd3b8b5bfe40d68bbc0f89b403f79a)
#### Saturday 2023-09-02 18:00:28 by MrMelbert

Replaces Ascended Blade Heretic stun imminuty with a stun absorption effect (it's not as cool as it sounds)  (#78060)

## About The Pull Request

Instead of being completely immune to stuns after ascension, blade
heretics now have a stun absorption. This is the effect that His Grace
and the Bastard Sword use.

It functions similarly, in that it stops you from being hardstunned, but
the difference it is they are only immune to a limited amount of stuns
for a limited amount of time before it recharges.

Currently that number is 45 seconds of stuns, with a 2 minute recharge,
meaning if you take more than 45 seconds of stun effects you will stop
being immune.

Bear in mind this still provides full immunity to being stamcrit*, as
stam doesn't contribute towards "seconds stunned" number.

*Unless you used all 45 seconds of stun immunity then you will no longer
be immune until you recharge.

Also to compensate, I gave them a slightly modifier protecting against
knockdowns.

## Why It's Good For The Game

I forgot Stun Absorptions were a thing entirely when making this even
though I refactored the darn things.

Anyways, the reason why I'm doing this is that Stun Absorptions are just
a slightly more fair, less overt way of providing stun immunity, and I
think it fits the theme more.

You're supposed to be a master duelist, but being able to take on a
dozen people at once is not entirely intended (even though this is the
ascension, I know). Stun Absorptions lend better to that, since you run
out of stun juice eventually before you have to pull back.

Though ultimately this doesn't change very much, as we use very few
hardstuns now-a-days:

- A flashbang will contribute about 10 seconds of stun time
- A flash is similar to a flashbang
- Bodythrows and tackles are less than 5 seconds
- Beepsky, 10 seconds
- Stamcrit, 0 seconds, but you are still slowed by stamina damage
- A banana peel, default is roughly 6 seconds. <-- (This is why I gave
them a knockdown modifier)

However it does mean you can't really tank an AI stun turret all day.
That's Rust's thing. Go play Rust Heretic.

## Changelog

:cl: Melbert
balance: Ascended Blade Heretics no longer have blanket stun immunity,
they now have 45 seconds of stun absorption that recharges after 2
minutes - think His Grace. This doesn't affect stamcrit (still immune to
that) (assuming you haven't consumed all of your immunity charge) but
does affect hard CC such as slips, flashbangs, or beepsky.
balance: Ascended Blade Heretics now have a 0.75 modifier to incoming
knockdowns.
/:cl:

---
## [DylanDoe21/Spooky](https://github.com/DylanDoe21/Spooky)@[44e422cf54...](https://github.com/DylanDoe21/Spooky/commit/44e422cf54f279fb7c3e9cdb94d073a2b40bb3c4)
#### Saturday 2023-09-02 18:13:21 by Mortis3

More catacomb stuff

-Added the exclusive chest items to the second catacomb layer
-Added some new daffodil dialogue
-Daffodil now has a 1 in 20 chance to say "nah" and go back to sleep when you attempt to  rematch her
-Added the cross and ghastly rosary accessories (the other ones are not done yet)
-Buffed all of the pandora's box enemies hp
-Reworked bobbert's movement AI to be more dangerous, and bobberts will now automatically explode when they touch a player
-The magic bolts shot by stitch now fade from cyan to white because the cyan to dark blue fade looked ugly
-Made a bunch of touch ups to all the holdout weapons to make them not janky
-Added WIP branch of gourd weapon (Minion AI still needs testing and tweaks)
-Resprited the disciples mask
-Catacombs second layer is now less wide on small worlds, and modified the hallway generation on small worlds in the second layer to prevent softlocking

---
## [Spark-Devices/kernel_xiaomi_alioth](https://github.com/Spark-Devices/kernel_xiaomi_alioth)@[037a93a162...](https://github.com/Spark-Devices/kernel_xiaomi_alioth/commit/037a93a16247d5acd2710ddd6c47122fd7e3f736)
#### Saturday 2023-09-02 18:14:22 by Peter Zijlstra

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
## [JagadeeswarThimmareddygari/CodeForces](https://github.com/JagadeeswarThimmareddygari/CodeForces)@[4ee4a06b6b...](https://github.com/JagadeeswarThimmareddygari/CodeForces/commit/4ee4a06b6b36f0dbaef3d8e9243e74fd7bae5a96)
#### Saturday 2023-09-02 18:17:58 by Jagadeeswar Thimmareddygari

CodeForces: WeirdAlgorithm

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

---
## [WarlockD/tgstation](https://github.com/WarlockD/tgstation)@[3af26df8ca...](https://github.com/WarlockD/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Saturday 2023-09-02 18:18:59 by GoldenAlpharex

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
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[0dd3e66aef...](https://github.com/MrMelbert/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Saturday 2023-09-02 18:22:34 by Vekter

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
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[5a6601eb41...](https://github.com/ZecHub/zechub/commit/5a6601eb41f22a7d984aa1fcb4ddb4c41d704765)
#### Saturday 2023-09-02 19:17:01 by Hardaeborla

Non Custodial Exchanges.md



In the ever-evolving world of cryptocurrency trading, the rise of non-custodial exchanges which is also known as Decentralized Exchanges or DEXs is redefining how users engage with digital assets. These platforms offer a revolutionary approach to trading by eliminating the need for intermediaries or third party and putting control firmly in the hands of users.

It is also undoubtedly that as Zcash is concerned, privacy matters as it remains an innovative project that pushes the boundaries of privacy within the cryptocurrency space, offering users the option to transact in a more confidential and secure manner.

In this piece, we'll delve into the present non-custodial exchanges that enable you to effortlessly obtain and trade Zcash independently, without the need for intermediaries in the transaction process. Before we dive into these accessible non-custodial exchanges for acquiring Zcash, let's take a quick look at Non-Custodial Exchanges (DEXs) vs Centralized Exchanges to gain a better understanding.

### **Understanding Non Custodial Exchanges In Brief** 
Non-custodial exchanges, also known as Decentralized Exchanges (DEXs) are platforms that facilitate cryptocurrency trading without requiring users to deposit their funds into the exchange itself. Instead, users retain control of their private keys and trade directly from their wallets without the need for third parties. This decentralized approach enhances security and privacy, as users are not reliant on the exchange to hold their assets which also reduces the risk of hacks or mismanagement. Transactions on non-custodial exchanges often leverage smart contracts to ensure trustless and transparent trading. 

A key advantage of non-custodial cryptocurrency exchanges lies in the increased control they provide to users over their assets. As these exchanges don't retain the assets, users enjoy complete ownership and authority over their digital currencies. This aspect can be especially attractive to individuals worried about asset security.

### **Understanding Custodial Exchanges** 
Custodial Exchanges are also known as centralized Exchanges. They are cryptocurrency trading platforms where users deposit their funds into accounts managed by the exchange itself. In this model, users entrust the exchange with the custody of their assets, meaning the exchange holds and controls the private keys necessary to access and manage the cryptocurrencies. This setup can provide convenience, especially for newcomers to the cryptocurrency space, but it also means users are reliant on the exchange's security measures. While custodial exchanges often offer user-friendly interfaces and customer support, they may present higher security risks due to the centralization of funds and the potential for hacks or mismanagement.


An advantage of custodial exchanges is their provision of a straightforward and user-friendly interface, simplifying the initiation of crypto trading for newcomers. Additionally, these exchanges offer an array of functionalities, including charting tools, real-time market information, and the capability to establish stop-loss orders, catering to the needs of more seasoned traders

### **Non Custodial Exchanges Vs Custodial Exchanges** 

**#1 Security**
Non-custodial exchanges eliminate the need for users to trust a central entity with their funds or assets. This enable users to maintain and have control of their private keys, reducing the risk of hacks, insider attacks and platform vulnerabilities that custodial exchanges may experience. 


**#2 Privacy**: Non-custodial exchanges often provide greater privacy by allowing users to trade directly from their wallets without the need for any intermediary. Transactions can be executed with greater anonymity, as sensitive information is not stored unlike Centralized Exchanges 


**#3 Decentralization**: Non-custodial exchanges align more closely with the decentralized ethos of cryptocurrencies. Users have greater autonomy and control over their trading activities, in line with the broader principles of blockchain technology.

When it comes to Custodial Exchanges, the level of Decentralization is often quite minimal in most centralized exchanges which give rise to the exchange team or officials managing user data or information on the exchange. 


**#4 Adaptability to Changing Regulations**: Non-custodial exchanges are often more adaptable to changing regulatory environments. Since they do not hold user funds, they might have fewer compliance challenges compared to custodial exchanges.




**#5 Innovation and Experimentation**: Non-custodial exchanges frequently drive innovation in the crypto space. They encourage the development of decentralized technologies, such as automated market makers (AMMs) and decentralized finance (DeFi) applications.



**#6 Global Accessibility**: Non-custodial exchanges often provide access to cryptocurrencies for users around the world, including regions where regulatory hurdles might limit the availability of custodial exchange services.

**#7 No KYC Requirements**: 
Many non-custodial exchanges do not require users to undergo extensive know-your-customer (KYC) procedures, offering a level of privacy and inclusivity that is absent in some custodial platforms.



While non-custodial exchanges offer compelling advantages, it's important to acknowledge that they might come with drawbacks, such as potential liquidity issues and a steeper learning curve for less experienced users. As with any financial decision, traders should carefully assess their priorities, risk tolerance, and familiarity with the technology before choosing between non-custodial and custodial exchange options.

Now, let's explore a few of the accessible non-custodial exchanges that facilitate Zcash trading. Utilizing these platforms will provide you with a convenient means to acquire more Zcash coins.

### **Non Custodial Exchanges To Trade or Acquire Zcash**

**#1 Simple Swap** 
SimpleSwap presents an exchange platform providing swift and straightforward swaps for users globally. The process is uncomplicated as it enable users to exchange cryptocurrencies, earn SWAP tokens, acquire a subscription and acquire BTC. No registration is necessary for conducting exchanges through the SimpleSwap Mobile App or web service.

SimpleSwap supports Transparent Address on both Zcash Blockchain and Binance Smartchain (Bep20). It enables you swap your Zcash tokens into other supported coins like USDT very easily. Follow the below steps as tested by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) 

* Visit [SimpleSwap](https://simpleswap.io/) either Web or mobile app. 


* Select the Supported Crypto Pairs, in this case I'm selecting ZEC and USDT 

* Enter amount of ZEC you intend to swap on the DEX and paste the address. 










 

SimpleSwap DEX Link :https://simpleswap.io

Mobile App (Android):https://simpleswap-subdomain.onelink.me/XxkL/4d83a727


Mobile App (iPhone):https://simpleswap-subdomain.onelink.me/XxkL/85fe1e52

**#2 Fixed Float** 
Fixed Float is another non Custodial Exchange that has been in existence since 2018 and it equips you with the means to fully leverage your digital assets via a user-friendly and accessible exchange platform. 

[Fixed Float](https://fixedfloat.com/) also supports swapping and trading of Zcash on it's DEX as it enables you to swap ZEC easily into other supported cryptos available on the DEX.

[Fixed Float](https://fixedfloat.com/) can easily be used to swap ZEC as explained by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) in the below description;

FixedFloat DEX Link: https://fixedfloat.com


**#3 SideShift** 
Experience the No Registration Crypto Exchange. Seamlessly switch between BTC, ETH, BCH, XAI, and over 100 other cryptocurrencies all without needing an account using SideShift.

SideShift is another non-custodial exchange that facilitates trading of Zcash. It supports both shielded and transparent Zcash wallet addresses on its decentralized exchange (DEX), offering user-friendly accessibility for Zcash trading.

Check out the guide on how to swap your ZEC on SideShift in the below description;


 
**#4 Changelly**
[Changelly](https://changelly.com/) stands out as a user-friendly non-custodial exchange that enables hassle-free trading or swapping of Zcash for various other supported assets. 

During the swapping process, this non-custodial exchange facilitates transactions with Zcash Transparent wallets. Discover the instructions below for guidance on how to proceed:


You can learn more about how it works [here](https://changelly.com/blog/how-to-exchange-crypto-on-changelly/) 

Changelly DEX Link: https://changelly.com/


**#5 Trocador** 
[Trocador](https://trocador.app/en/) serves as a privacy-centric exchange aggregator. The team hold the conviction that cryptocurrency possesses the potential to counteract government overreach, censorship, and tyranny, fostering decentralization and liberty for a world that thrives in prosperity and freedom.

This Non Custodial Exchange also support the trading of Zcash by depositing and withdrawing through the Zcash mainnet address. 

Trocador DEX Link: https://trocador.app/en/


**#6 Swapzone** 
Swapzone is Swapzone is a cryptocurrency exchange aggregator that enables user to browse through services, compare exchange rates, analyze and swap cryptocurrency in just one interface. All swaps are custody-free, with no registration needed.

[Swapzone](https://swapzone.io/) also supports the trading and swapping of Zcash including deposits and withdrawals of Zcash addresses such as Transparent, Bep20, Hecochain and BEP2. 


Swapzone Link:https://swapzone.io/

**#7 Flyp**
Flyp stands as the swiftest, most secure and exceedingly confidential means of swapping over 30 cryptocurrencies directly into your wallet. There's no need for registration, email, or an account. A single click effortlessly facilitates instantaneous exchanges. Your privacy and private keys are under your constant command. The process is as straightforward as executing a transaction from your own wallet. 

The good news is that Flyp.me also supports Zcash transactions on it's DEX, users have option to input either their Transparent Address (recommended) or shielded or unified address. 


Flyp.me DEX Link: https://flyp.me/



**#8 Pancakeswap** 
[Pancakeswap](https://pancakeswap.finance/swap) stands as the top decentralized exchange on the BNB Smart Chain, boasting the market's highest trading volumes.

The non Custodial Exchange supports swapping of Zcash (Bep20) into other crypto assets on the BNB Chain Cake, BNB, USDT and others. 


DEX Link:https://pancakeswap.finance/swap

**#9 Decred** 
Decred DEX enables you to engage in peer-to-peer cryptocurrency trading without any trading fees or KYC requirements. DCRDEX represents a decentralized exchange crafted by the Decred Project.

[Decred DEX](https://dex.decred.org/) also supports the Swapping and trading of Zcash on it's DEX and users are able to deposit and withdraw Zcash tokens either transparently or privately. 

DEX Link : https://dex.decred.org/

**#10 GODEX** 
[GODEX](https://godex.io/) stands out as a high-speed exchange platform, with order executions typically taking between 5 to 30 minutes. The execution time is contingent upon confirmation speed within the decentralized network, with larger amounts, such as those exceeding 1 BTC, often requiring more time. The DEX dependability rests on contemporary security protocols and robust physical server protection.

The DEX offers support for both Transparent (t-address) and Shielded (z-address) transactions from the Zcash Network. GODEX further facilitates the effortless swapping and trading of tokens.

DEX Link: https://godex.io/
Android App:  https://play.google.com/store/apps/details?id=com.godex.app.GodexApp




**#11 ChangeNow** 
ChangeNOW operates as a non-custodial platform designed to facilitate swift and straightforward cryptocurrency exchanges. The DEX focus is on providing the utmost security, ease of use, and convenience. The DEX neither retain your funds nor mandate any form of account setup. With nearly 700 coins accessible for exchange, ChangeNOW imposes no restrictions; you can perform exchanges to your heart's content without an account, all while ensuring a speedy process. 

ChangeNOW also supports Zcash deposit and withdrawals using address from Zcash mainnet and Bep20 (Binance Smartchain) Network. 

**#12 StealthEx** 
StealthEX offers non-custodial cryptocurrency exchanges where there's no need to set up an account or reveal personal information. Additionally, funds are not stored on StealthEX; exchanges occur directly between wallets.

[StealthEX](https://stealthex.io/) also supports the withdrawal and deposits of Zcash mainnet addresses including swapping and trading of Zcash. 

DEX Link: https://stealthex.io

Mobile App : https://play.google.com/store/apps/details?id=com.stealthex

**#13 SwapSpace** 
SwapSpace serves as a real-time aggregator for cryptocurrency exchanges. The platform empowers you to select from various swap offers provided by major crypto exchanges, all conveniently assembled in a single location. [SwapSpace](https://swapspace.co/) is committed to streamlining the exchange experience, granting access to over 2650 cryptocurrencies for swift, registration-free swaps, all at the most competitive rates available in the market. 

Through the [SwapSpace DEX](https://swapspace.co), individuals have the capability to engage in trading and withdrawals involving Zcash using various options including Zcash mainnet address, Zcash (Bep20), Zcash (Bep20), and Zcash on the Heco Chain.

DEX Link : https://swapspace.co


**#14 ChangeHero** 
ChangeHero combines a UX flow of decentralized exchange with liquidity from multiple popular CEXs after successful DEX integration as announced by the team [here](https://changehero.io/blog/dex-integration-in-changehero/) 

Change Hero also supports trading and swapping of Zcash into other available tokens on the DEX. The DEX also supports Zcash mainnet (t-address) address on it's platform. 

DEX Link: https://changehero.io/


**#15 EasyBit** 
EasyBit is also a non Custodial Exchange that enables users to swap and trade digital assets easily on it's DEX.  It operates without a central authority or intermediary, allowing users to trade directly from their wallets and retaining control over their private keys.

Users can also trade Zcash with EasyBit as the DEX also supports Zcash mainnet network, Zcash (Bep20) and Zcash (BEP2) 

DEX Link: https://easybit.com/en/

### **Conclusion** 

Non-custodial exchanges, or DEXs, are decentralized platforms enabling direct cryptocurrency trading from users' wallets. Users retain control of their private keys, enhancing security and privacy. These exchanges offer features like shielded transactions for confidentiality and operate on trustless principles through smart contracts. They play a key role in the DeFi ecosystem, though they might face challenges like liquidity concerns. Non-custodial exchanges offer a decentralized, secure, and private way to trade cryptocurrencies globally.




Non-custodial exchanges offer an alternative trading experience that aligns with the principles of cryptocurrencies. While they bring advantages in terms of security, privacy, and control, users should assess their risk tolerance and familiarity with the technology before engaging in trading on these platforms.

---
## [khuonghoanghuy/New-Plus-Engine](https://github.com/khuonghoanghuy/New-Plus-Engine)@[1a3d06798b...](https://github.com/khuonghoanghuy/New-Plus-Engine/commit/1a3d06798be8308d74ed848dcc8b3f91f0f730c3)
#### Saturday 2023-09-02 19:31:18 by BambiGaming2022

okay fuck you

from bp
its gives me error
credit to whatsdown

---
## [ativarsoft/mateus](https://github.com/ativarsoft/mateus)@[2353ad6935...](https://github.com/ativarsoft/mateus/commit/2353ad6935ae2b8ac9c89190fec64321e2577b80)
#### Saturday 2023-09-02 19:31:37 by Mateus de Lima Oliveira

As Torvalds said, fuck you GPU manufacturers

Signed-off-by: Mateus de Lima Oliveira <mateus@ativarsoft.com>

---
## [zecKR/zechub](https://github.com/zecKR/zechub)@[9e448711f9...](https://github.com/zecKR/zechub/commit/9e448711f9676343eb138487a4be9d80d30de65a)
#### Saturday 2023-09-02 20:01:28 by Hardaeborla

zecweekly57.md

#Iwe Iroyin Osẹ-ọsẹ Zec #57

Àwọn ifunni Zcash Kékeré Ṣí fún Àwọn olubẹwẹ, Àwọn imudojuiwọn Agbègbè àti Rántí Wípé “Aṣiri jẹ Deede”

 Atunto nipasẹ "Tony Akins"[(@Tonyakins01)](https://twitter.com/TonyAkins01) 
ati Itumọ si ede Yoruba nipasẹ "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

### EKaabo si ZecWeekly

Ọsẹ moriwu mìíràn fún Zcash bí àgbègbè ṣé gbá atilẹyin ńlá àti àwọn ìgbì ìdàgbàsókè túntún, ZecHub pínpín nkan Ìwé ìròhìn kàn, àwọn imudojuiwọn Ìdàgbàsókè Arborist àti àgbègbè ṣe ìdáhùn sí ikọlu lórí òmìnira ọrọ tí àwọn olupilẹṣẹ.
---

## Nkan Ẹkọ ti Ọsẹ yii
Pipinpin awọn iyatọ laarin awọn adagun-omi Idabobo Imọ Zero ati ailorukọ-orisun ti o da lori ni afikun aipẹ si wiki ZecHub. Iṣafihan si Awọn adagun-omi Dabobo, Awọn ẹri Imọye Zero, Awọn Ibuwọlu Iwọn & Awọn iṣowo Asiri. Awọn afiwera lẹhinna fa ni fifun ni ero ti o daju lẹhin idi ti Zcash n pese awọn iṣeduro aṣiri lori-pq aifẹ.
[Ka ni ibi yìí](https://wiki.zechub.xyz/zk-shielded-pools-vs-decoy-based-privacy) 




## Awọn imudojuiwọn Zcash

####  Awọn imudojuiwọn ECC ati ZF
[Awọn ohun elo🗎 Ṣii fun Yika Keji ti Awọn ifunni Kekere ZF](https://forum.zcashcommunity.com/t/all-ecc-teams-focused-on-wallet-performance/42860/107) 

[Awọn ẹgbẹ ECC dojukọ iṣẹ ṣiṣe apamọwọ](https://forum.zcashcommunity.com/t/opening-applications-for-the-second-round-of-zf-minor-grants/45463) 

[Ẹgbẹ ZFAV ṣe atẹjade awọn itọsọna 📚 fun awọn olupilẹṣẹ àkóónú](https://wiki.zechub.xyz/zfav/guides) 

####  Awọn imudojuiwọn Awọn ifunni Agbegbe Zcash

[Imudojuiwọn Lórí Ilolupo Aboo](https://forum.zcashcommunity.com/t/zcash-ecosystem-security-lead/42090/91) 

[Igbero fun 🇧🇷  Aṣiri Alliance tí Ilu Brazil](https://forum.zcashcommunity.com/t/brazilian-privacy-alliance/45486) 

[Àgbègbè Igbowosile ZFAV ní Ipele](https://twitter.com/ZFAVClub/status/1693689895254949983) 

#### Awujo Ise Agbese 
[Awọn agbasọ nipa Asiri🗣️ - Topcrypto](https://free2z.cash/TopCrypto/zpage/dont-overshare-privacy-is-power-zcash) 

[Zcash Espanol ṣe iṣẹlẹ iṣẹlẹ atunṣe Zcon4](https://twitter.com/zcashesp/status/1694857330284712324) 

[Ìpè  🌳 Arborist Lakotan](https://twitter.com/zksquirrel/status/1694876187586170957) 

[Ọ̀rọ̀ @Zulakyz NFT lórí tí ZecHub Extras](https://zcashesp.com/zechub-nft-acceso-extra-a-beneficios-e-informacion-zcash/) 

[Itan kékeré láti ọ̀dọ̀ Cypherpunk Zero - Zerodartz🔥](https://free2z.com/zerodartz/zpage/cypherpunk-hacks-in-zed-city-short-story-3-out-of-12-chapters) 

[Awọn itumọ nilo fun Nighthawk apamọwọ](https://crowdin.com/project/Nighthawk-wallet) 


#### Iroyin ati Media 

[Ilosiwaju tí de ba Ethereum Staking💹  - Decrypt](https://decrypt.co/153813/ethereum-staking-is-booming-but-value-of-defi-assets-keeps-falling) 

[Kini idi ti asiri di ọrọ buburu? - Coindesk](https://www.coindesk.com/consensus-magazine/2023/08/25/when-did-privacy-become-a-bad-word) 

[Account tí OnlyFans tí Gba Friend.tech - Decrypt](https://decrypt.co/153723/onlyfans-accounts-take-over-friend-tech-crypt-app-adds-photo-feature) 

[Òṣìṣẹ́ banki aringbungbun sọrọ nipa Euro oni nọmba aladani ni ìlú 🇪🇸 Spanish - Cointelegraph](https://cointelegraph.com/news/spanish-central-bank-official-talks-about-private-payment-services-era-digital-euro) 

[Awọn anfani Lido n pọ si ti Ethereum - Trustnodes](https://www.trustnodes.com/2023/08/27/lido-closes-in-on-33-of-the-ethereum-network) 

[Awọn iran ti ọjọ iwaju lórí Decentralization - Cypherpunk](https://www.cypherpunktimes.com/visions-of-a-decentralised-future/) 

[Akojọpọ ọsẹ - Lori Brink](https://onthebrink-podcast.com/roundup-08-25-23/) 



## Awon oro die Nipa ZCash Lori Twitter
[👉 Iyatọ laarin Monero àti Zcash](https://twitter.com/MKjrstad/status/1695814999405379672) 

[Ikede nla nbọ laipẹ? - TrendsXBT](https://twitter.com/TrendsXBT/status/1694891818226213127) 

[Awọn iṣagbega nla ti a ṣe si Nighthawk](https://twitter.com/aiyadt/status/1694973730856866228) 

[Strawpoll ti o ni ipo 📊 ti Zcash Awọn ìṣáájú](https://twitter.com/nate_zec/status/1694405933638861048) 

[ZeroDAO ṣe igbega Zcash DeFi](https://twitter.com/zerodaoHQ/status/1694762728345456889) 

[Àṣírí sì jẹ déédéé](https://twitter.com/ZecHub/status/1694417573541007445) 

[O ṣeun lati ọdọ ZcashEsp!](https://twitter.com/zcashesp/status/1694861382154338648) 

[Fidio FROST ❄️  Ririnkiri lori Youtube](https://twitter.com/ZcashFoundation/status/1694410320859545939) 

[Awọn ifẹ ojo ibi Ailorukọ nipasẹ Zcash Memo](https://twitter.com/AyanlajaAdebola/status/1695721838943289694) 

[Bawo ni o ṣe n ṣe pẹlu ZEC?](https://twitter.com/ZcashForum/status/1693520113797116406) 

[Ṣe awọn spammers n ṣe rere fun nẹtiwọọki naa?](https://twitter.com/ZcashForum/status/1693430229044445287) 

[Awọn iwe afọwọkọ oluranlọwọ Zcasd lati Dismad :)] (https://twitter.com/ZcashForum/status/1693385561116164360) 

[A wa fun ominira - @zcash](https://twitter.com/zcash/status/1669397156212375583) 

[Iwe Iwe irohin ZecHub nipa Awọn adagun Àṣírí](https://twitter.com/ZecHub/status/1695082959911403585) 


[Joel Valenzuela pẹlu iwoye diẹ sii 📽️ lori Tornado Cash](https://twitter.com/TheDesertLynx/status/1694816146355036620) 




## Zeme ti Ose Yii 

[https://twitter.com/ZFAVClub/status/1694817298677113308](https://twitter.com/ZFAVClub/status/1694817298677113308) 


## Awọn iṣẹ ni ilolupo
[ZecWeekly #58  iwe iroyin Agbegbe](https://app.dework.xyz/zechub-2424/board?taskId=102e34d1-8f77-45d1-bd4f-d3d8f2a040ce) 

[Ṣiṣe Zcash Full Node lori Akash Network](https://app.dework.xyz/zechub-2424/board?taskId=543cab70-627d-4222-a712-9fb8768abe9c)

---
## [CrimsonShrike/Citadel-Station-13-RP](https://github.com/CrimsonShrike/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/CrimsonShrike/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Saturday 2023-09-02 21:45:58 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [Zeldazackman/Citadel-Station-13-RP](https://github.com/Zeldazackman/Citadel-Station-13-RP)@[4966352d14...](https://github.com/Zeldazackman/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Saturday 2023-09-02 23:13:02 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [timDeHof/next-3d-portfolio](https://github.com/timDeHof/next-3d-portfolio)@[74c44a616a...](https://github.com/timDeHof/next-3d-portfolio/commit/74c44a616a1d10724809fcb13693322d37eafc46)
#### Saturday 2023-09-02 23:25:00 by timDeHof

feat(next.config.js): update pageExtensions to include 'md' and 'mdx' file extensions
feat(next.config.js): enable reactStrictMode for stricter React mode
The pageExtensions configuration in next.config.js is updated to include 'md' and 'mdx' file extensions. This allows Next.js to handle Markdown files as pages. Additionally, the reactStrictMode configuration is set to true to enable stricter mode for React, which helps catch potential issues and improve overall code quality.

feat(package.json): add next-mdx-remote and remark-unwrap-images dependencies
The next-mdx-remote and remark-unwrap-images dependencies are added to the package.json file. next-mdx-remote is a library that allows rendering MDX content in Next.js applications, while remark-unwrap-images is a plugin for remark that unwraps images from paragraphs in Markdown files. These dependencies are necessary for handling and rendering MDX content in the application.

feat(components/MDX

feat(content): add two new blog posts

Added two new blog posts to the content directory: "The Power of a Growth Mindset in Software Development - How to Embrace Challenges and Advance Your Career" and "How to Deploy the Face Recognition API for Free with Render - Alternative to Heroku".

The first blog post discusses the importance of having a growth mindset in software development and provides tips for developing and maintaining this mindset. It emphasizes the benefits of embracing challenges and continuously improving skills.

The second blog post focuses on deploying the Face Recognition API using Render as an alternative to Heroku. It provides step-by-step instructions on setting up a Render database, connecting to the database in the API, and deploying the API as a web service on Render.

These blog posts aim to provide valuable insights and practical guidance to readers in the field of software development.

feat: add blog post "From Mechanical Design Engineer to Fullstack Developer - My Journey and Lessons Learned"

This commit adds a new blog post titled "From Mechanical Design Engineer to Fullstack Developer - My Journey and Lessons Learned". The blog post details my personal journey and experiences transitioning from a mechanical design engineer to a fullstack developer. It covers topics such as my decision to make a career change, the coding bootcamp I attended, the technologies I learned, and the challenges I faced along the way. The blog post also includes information about a group capstone project I worked on during the bootcamp and my job search as a fullstack developer. Additionally, it highlights the soft skills I developed and the lessons I learned throughout the journey.

The purpose of this commit is to add valuable content to the blog and share my experiences and insights with others who may be considering a similar career transition.

feat: add blog post "Unleash the Power of Java - A JavaScript Developer's Guide to Best Practices in Java Development"

This commit adds a new blog post titled "Unleash the Power of Java - A JavaScript Developer's Guide to Best Practices in Java Development". The blog post discusses the key differences between Java and JavaScript in terms of object-oriented programming, code style and formatting, and exception handling. It also provides learning resources for JavaScript developers transitioning to Java.

The blog post aims to help JavaScript developers understand the best practices and conventions in Java development, enabling them to leverage their existing knowledge and skills while diving into the world of Java.

feat: add blog post about debugging an empty API response in Axios

This commit adds a new blog post titled "Unraveling the Mystery of an Empty API Response in Axios - A Debugging Adventure". The blog post discusses a common issue that can occur when using React Query and Axios to fetch data from an API. It provides a step-by-step guide on how to debug and solve the issue.

The blog post covers the following topics:
- The problem of receiving an empty API response in React Query
- Debugging the issue by inspecting the code and API response
- Adding logging statements to track the API request and response
- Troubleshooting approaches such as verifying the API request, checking API status, and trying a different API endpoint
- Considering frontend code and data processing/display as potential sources of the issue
- The importance of effective debugging and a systematic approach to problem-solving

The commit also includes code snippets that demonstrate the added logging statements to the `get

feat(blog): add support for rendering markdown content using MDX
The blog page now supports rendering markdown content using MDX. This allows for more flexibility in styling and customizing the rendering of markdown content. The page now uses the `MDXRemote` component from `next-mdx-remote` to render the markdown content. The `MDXProvider` component is used to provide custom components for rendering specific markdown elements. The `components` object defines the custom components to be used for rendering specific markdown elements. The markdown content is serialized using the `serialize` function from `next-mdx-remote/serialize`. This allows for the markdown content to be transformed into an MDX source that can be rendered by the `MDXRemote` component.

---
## [Torrahth/tewst](https://github.com/Torrahth/tewst)@[2a96c3b7a4...](https://github.com/Torrahth/tewst/commit/2a96c3b7a47b4eac9f01243678839b18ae0893a5)
#### Saturday 2023-09-02 23:30:09 by T0rah

what the shit

wawa i hate tml its so evil ITS SO EVIL

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4792a8e19d...](https://github.com/tgstation/tgstation/commit/4792a8e19dc6885a2f6e8d25f1086505624e7a6c)
#### Saturday 2023-09-02 23:44:55 by carlarctg

Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

---

