## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-04](docs/good-messages/2023/2023-11-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,996,236 were push events containing 2,763,647 commit messages that amount to 165,585,108 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[68cd638330...](https://github.com/tgstation/tgstation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Saturday 2023-11-04 00:13:22 by Donglesplonge

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
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[d31c21ff1b...](https://github.com/Nobelium-XVIII/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Saturday 2023-11-04 00:23:51 by jimmyl

new space ruin, the biological research outpost (#79149)

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

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[9e18c6575a...](https://github.com/Nobelium-XVIII/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Saturday 2023-11-04 00:23:51 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[e39a43e2a4...](https://github.com/ynot01/tgstation/commit/e39a43e2a418f19fde52e05281bfdae063f4a6c1)
#### Saturday 2023-11-04 00:30:05 by Toastgoats

[No GBP] Fixes the secret bottomless pit in the ethereal pirate shuttle (#78138)

## About The Pull Request

I DIDNT NOTICE THAT ALL THE DIRT IN THE ETHEREAL SHUTTLE HAD CHASM
BASETURFS FUCK FUCK FUCK


![image](https://github.com/tgstation/tgstation/assets/63932673/ba5f7b02-7577-48ad-b2bc-b8b1c0e4192f)

(Also rebalances the ship a bit by adding some more turrets and cleans
up the wonky turf decals and engines)
## Why It's Good For The Game

God's strongest mapper needs to get some sleep asap I'm so fucking tired

A few people also pointed out that only having two turrets was extremely
punishing even for the playstyle I was trying to encourage, so it makes
sense to add a little wiggle room.
## Changelog
:cl:
balance: Gave the bluespace geode pirates 4 more teleporter bolt
turrets.
fix: The bluespace geode pirates no longer have a bluespace portal to
the bottomless pit dimension.
add: Station-safe dirt tiles for all your mapping needs, but surely no
station maps use the chasm baseturf ones, right? Right?
/:cl:

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[ad0df33492...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/ad0df334925f926af08907136d82f3caaf4b8f52)
#### Saturday 2023-11-04 00:55:52 by pixelkitty286

Ports virgo's Jukebox interface / overhauls the old one, portable music players and more jukebox songs / some fixes (Oh my!) (#5996)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

This ports over and makes the jukebox media player into a subsystem wile
also overhauling / porting over virgo's tgui interface for jukeboxes.

This PR also brings over the Podzu music player and makes it available
to all players in cargo, loadouts, and venders.

It also has a function that is not at the moment working where you can
add more music as an admin. But if someone is willing to fix the admin
system I can see about making that function work instead of leaving it
commented out.

I will in another PR go over more of the broken songs and eliminate or
fix them. (I listen to music heavily when playing here)
## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

The current Jukebox GUI is horrible and the current media player system
is not modular what so ever and is clunky to use, but the port of
virgo's jukebox UI is not really perfect, however it is leagues better
than Nano. (PLEASE I SUFFERED TO PORT IT)

Portable music players are really nice and sharing tunes with fellow
players is sweet.
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
add: Portable music players!, and improved Jukebox UI
tweak: jukebox.json
qol: Jukebox ui is not as clunky
fix: Jukebox ui
soundadd: Jukebox music?
code: media players, jukebox ui, and portable music player ui
refactor: refactored media players (they are their own subsystem now!)
config: Added more songs and also configured changes to the jukebox.json
to work with the changes
admin: some jukebox code (idk if what I did caused anything)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[e2ba2b1adb...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/e2ba2b1adb5c0cffcb6de89e04a3728ccd06a2be)
#### Saturday 2023-11-04 00:55:52 by Captain277

Minor Layout Adjustment to Archaic Temple and Statue Component Bugfix (#6019)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Makes Layout Adjustments to Archaic Temple POI.**
2. **Adds New Ranged Trap Subtype.**
3. **Adds Female Statue Side and Back Sprites.**
4. **Bugfixes Unobserved Actor Component.**

## Why It's Good For The Game

1. _Minor adjustments to the POI that I don't want to describe in the PR
due to their connection to the mechanics. Repair of the door icons,
minor housekeeping._
2. _Having the traps fire non-stop is a little unfun. Even if they can
be jammed, sometimes it's neat to give them a limited chain of blasts._
3. _The male had side and back sprites but the female didn't. I just
kinda tweaked the male to fit._
4. _It was discovered that Ghosts able to see a statue were counting as
observers for the unobserved actor component, effectively crippling the
statue._

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
tweak: Layout Changes to Archaic Temple
add: Adds New Launcher Trap Type
fix: Adds Sprites to Female Statue
fix: Fixes Bug in Unobserved Actor Component
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [arkid15r/git-uk-l10n](https://github.com/arkid15r/git-uk-l10n)@[8f23432b38...](https://github.com/arkid15r/git-uk-l10n/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-11-04 01:05:32 by Johannes Schindelin

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
## [AGDFL/BusinessCardTemp](https://github.com/AGDFL/BusinessCardTemp)@[ec0ea8d43d...](https://github.com/AGDFL/BusinessCardTemp/commit/ec0ea8d43d71e06e970a07cf37696b9284a1f3d7)
#### Saturday 2023-11-04 01:17:50 by agdfl

Merge branch 'main' of https://github.com/AGDFL/BusinessCardTemp
fuck you, i just want to make a simple push

---
## [private-tristan/PvE-CMSS13](https://github.com/private-tristan/PvE-CMSS13)@[e4c3900e4f...](https://github.com/private-tristan/PvE-CMSS13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Saturday 2023-11-04 01:40:45 by riot

reduces timer on joining ert after death to 30 seconds (#4652)

# About the pull request

reduces timer

# Explain why it's good for the game

Having to wait a full minute to join an ERT is annoying, it was better
b4 when timer from ERT was a minute as well, but 30 second ERT means if
u die just b4 ERT goes you cant join regardless.

if ppl are ghosting bc they want ert then they are stupid.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Timer on attempting to join ERT after death is now 30 seconds
down from 1 minute
/:cl:

---
## [private-tristan/PvE-CMSS13](https://github.com/private-tristan/PvE-CMSS13)@[de5c69661f...](https://github.com/private-tristan/PvE-CMSS13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Saturday 2023-11-04 01:40:45 by kiVts

DFB property changes. (#4590)

# About the pull request
part 2 out of 4 
This does a **big** touch up on defibrillation property in research

Well, to start off, max_level = 1 was removed. It appears warcrimes
forgot to remove it since process proc has benefits explicitly for
higher levels. I would call it a bug(oversight rather).

Second: Ghosts get notified when the chem starts to try and defib you,
so you dont just wonder how did you stand up, and pretty neat too.

Third: The >6 level of defib to apply healing like with actual item
defib is too high, so we move requirement down to >1 but make it heal
much, much worse at levels lower than 5.
eg it took 20 units to heal ~20 brute at level 3(you will literally
perma lmao), at level 5, however, this will go at around 2.5 per life
tick, level 8 will give 4 damage heal.
This is a balance change(buff) But hardly so since its research,
Research is already neglecting most of the time this property.

Fourth: removes one letter var, This whole file is entombed with them
but Im not doing that for now.

# Explain why it's good for the game


Defib property is way too underused and crudely made. This fixes it,
partially.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
add: Ghosts get notified when they are being revived by DFB property
balance: DFB property healing threshold lowered, You can create DFB
property higher than one.
/:cl:

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [mwatts/nushell](https://github.com/mwatts/nushell)@[fed4233db4...](https://github.com/mwatts/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Saturday 2023-11-04 01:57:22 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [silont-project/kernel_xiaomi_rosemary](https://github.com/silont-project/kernel_xiaomi_rosemary)@[3c467ee518...](https://github.com/silont-project/kernel_xiaomi_rosemary/commit/3c467ee518341f9afc959ceb7430638326f4bdab)
#### Saturday 2023-11-04 02:03:57 by Wang Han

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
Signed-off-by: Neebe3289 <neebexd@gmail.com>

---
## [Foxterosa/Skyrat-tg](https://github.com/Foxterosa/Skyrat-tg)@[69ea3c81ad...](https://github.com/Foxterosa/Skyrat-tg/commit/69ea3c81ad86a0356af947f11fe3bd2ca953b0af)
#### Saturday 2023-11-04 02:18:41 by SkyratBot

[MIRROR] Mafia can be played on your PDA [MDB IGNORE] (#24485)

* Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

* Mafia can be played on your PDA

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Foxterosa/Skyrat-tg](https://github.com/Foxterosa/Skyrat-tg)@[c63f897521...](https://github.com/Foxterosa/Skyrat-tg/commit/c63f897521485898e00425a6c001495f7eef5de6)
#### Saturday 2023-11-04 02:18:41 by SkyratBot

[MIRROR] It is now possible to survive the Mansus  [MDB IGNORE] (#24490)

* It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

* It is now possible to survive the Mansus

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Foxterosa/Skyrat-tg](https://github.com/Foxterosa/Skyrat-tg)@[53cfff6ae1...](https://github.com/Foxterosa/Skyrat-tg/commit/53cfff6ae1cd62766395534a6f4c8aa468c5066c)
#### Saturday 2023-11-04 02:18:41 by SkyratBot

[MIRROR] Actually supports alpha passed into emissive stuff [MDB IGNORE] (#24481)

* Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

* Actually supports alpha passed into emissive stuff

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Zenitheevee/sojourn-station](https://github.com/Zenitheevee/sojourn-station)@[94b32aa82c...](https://github.com/Zenitheevee/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Saturday 2023-11-04 03:47:43 by CDB

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
## [NiLuJe/KindleTool](https://github.com/NiLuJe/KindleTool)@[04ce088095...](https://github.com/NiLuJe/KindleTool/commit/04ce0880954a422ee34c7cca886c31fe148c5e0c)
#### Saturday 2023-11-04 04:07:23 by NiLuJe

Start working on an optional shell-friendly output format for the
package info

Because parsing human readable output when you don't really have to is
kinda stupid...

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[2fc01ad8be...](https://github.com/MarkSuckerberg/Shiptest/commit/2fc01ad8be958492a38b3200023b8aa0c4bad9f5)
#### Saturday 2023-11-04 04:29:48 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

## About The Pull Request

If maintainers want me to shorten the changelog, I can, I tend to start
there so I know what to talk about up here.

What started as a PR meant to buff up rubber rounds ended up turning
into a general passover I gave to much of the syntax and presentation of
ballistics. PR doesn't actually change that much function-wise, but it
changes a lot of lines due to a lot of changed pathing to better
establish consistency within ballistic code as well as overviewing a lot
of descriptions, names, and inherit moments.

Functionally, less-lethals and sniper rounds have been changed the most
by this PR. To a lesser extent, .38 special and shotgun rounds have been
tweaked. Finally, the PR stamps out a missing sprite bug with the WT-550
magazines, buffs up the surplus rifle (yeah, that old thing), tinkers
with some projectile speeds, makes match rounds slightly better, and
goes over A LOT of descriptions. I apologize for the massive wall of
text that's to follow.

Will take a look at energy weapons when I feel like it (might kill
disablers, I don't like mapping though).

## Why It's Good For The Game

### Slug and Pellet Changes
The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

### Less-Lethal Changes
Several implementations of less-lethal (rubber) ammunition on shiptest
are strictly worse than their standard alternatives. While this isn't a
PvP server, it feels very not-fun meta-wise to POTENTIALLY arm for SOME
insubordination and still fire what may as well be a round that bleeds
someone out (as they'll cause bleeding anyway). Increasing the stamina
damage on each of these makes it so they actually have a vague trade-off
(maybe stamina damage can do something like slow simplemobs in the
future, I don't know, I'd love to do it but simplemob code makes me
screech).

To make them not directly better in PvP and not the staple of taking
down the Super Scary Syndicate Shocktrooper Guy, they've had their
negative AP doubled. Not as good against combatants, but still perfectly
adept, if not better at general riot control against civilians. Makes
sense and puts them in their niche a little better.

### .38 Changes
The .38 special round relatively has more "power" and "velocity"
compared to the 9mm round, though it does not quite reach the levels
that .45 automatic or 10mm does in the IRL server. Furthermore, .38
special was specifically designed not to over-penetrate targets so as to
minimize the chance of collateral damage in police work. These are the
ultimate justifications behind giving it the worst AP out of all the
pistol calibers (-30, instead of -20) while still raising its damage to
25.

This should make the Winchester a better staple for taking out weaker
enemies such as legions or unarmored hermits, but it'll perform worse
against goliaths, frontiersmen, and the like. All-in-all, a more
"early-game" caliber, if you will, which is kinda what it's always been.

### Projectile Speed and Match Changes
Match rounds don't really exist as far as I've seen. That being said,
they're meant to be of higher quality, so their getting slightly higher
AP and speed makes sense, even if they're mostly just a meme round.

The speed increase of DMR/sniper rounds is primarily meant to
differentiate them better from AR rounds beyond having 20 more AP.
Assault rifles so far have pretty much dominated with better magazine
size, fire rate, and the exact same force as the DMR calibers, just
doing less damage against armored targets (doesn't matter too much when
you can just vomit rounds). I'd like to buff up the DMR damage even more
(sniper is fine), but I'd rather get some feedback on changing them to
35 baseline before doing so.

The speed decrease on shotguns is meant to cement them as CQC weapons.
Slugs are heavy. Shotguns are meant for close range. It's not much, but
it's thematically a good way to keep them in their lane, not that
they're even that problematic, hence only the slight change.

### Sniper Rifle Knockdown Change
Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

### Surplus Rifle Fire Rate Buff
This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

### Boarder Magazine Change
Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

### WT-550 Magazine Fix
Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

### Syntax, Description, Spelling, and Overall Presentation Changes
Something very important when maintaining code is generally keeping
consistency in how things are not only presented, but how they're stored
as well. While I'd love to do EVEN more in the method of refactoring to
better align how so much of gun code works, this was something I wanted
to keep as a one-day project, so I mostly tinkered with pathing,
inherits, and groupings.

In the avenue of spelling and description changes, that's just 1)
Cleaning up errors that PR authors and maintainers missed and 2) Making
things more concise and just... better. Some of the SolGov descriptions
were a real headache to look at, and not because of the frequent
spelling and syntax errors.

Whoever misspelled and caused an entire series of items to be
/obj/item/gun/ballistic/automatic/assualt may wish to avoid any crows
for the next three months.

Perfectly willing to adjust or reel back some of my descriptions if
someone can offer something better than what I've written out if there's
some soul they REALLY want to keep.

## Changelog

:cl:
tweak: The NT 'Boarder' ARG now loads standard P-16 magazines, rather
than the M-90gl toploaders.
balance: .38 special does 25 damage up from 20. AP has been reduced to
-30 from -20.
balance: Standardizes pellet projectiles to lose 10% damage of both
types per tile across the board. Improvised pellets no longer have a
hardcapped 1-8 tile range.
balance: Less-lethal rounds now do 50% more stamina than the force of
their lethal counterparts, with 25% the normal force and double the
negative AP. If the round had positive or zero AP, it was subtracted by
20.
balance: Shotgun slugs do 40 damage, down from 60, but have zero AP,
rather than -10. FRAG-12 and meteor slugs have had their damage adjusted
to reflect their relative force.
balance: Surplus rifle fire_delay has been cut to 1 second from 3.
balance: .50 BMG knocks down instead of hardstunning.
balance: Any DMR, match, or sniper round now travels slightly faster
than other bullets. Shotgun slugs and pellets now travel slightly slower
than other bullets.
balance: Match rounds have had their AP slightly increased.
fix: Fixed WT-550 magazines not displaying properly.
spellcheck: Went over (almost) every single ballistic description,
including the guns themselves, magazines, ballistic casings, and speed
loaders/stripper clips to not only have better consistency and
readability, but also be more clear on the general effectiveness of each
caliber.
spellcheck: Assualt is gone.
code: Repaths/renames most ballistic ammo pathing to maintain
consistency or take advantage of inherits, when possible.
/:cl:

---
## [EEASAS/tgstation](https://github.com/EEASAS/tgstation)@[9cf089361e...](https://github.com/EEASAS/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Saturday 2023-11-04 04:47:54 by Rhials

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
## [EEASAS/tgstation](https://github.com/EEASAS/tgstation)@[66f726dfe3...](https://github.com/EEASAS/tgstation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Saturday 2023-11-04 04:47:54 by SyncIt21

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
## [LovelandHighRobotics1977/Swordtip-Rewrite](https://github.com/LovelandHighRobotics1977/Swordtip-Rewrite)@[fac98dc17e...](https://github.com/LovelandHighRobotics1977/Swordtip-Rewrite/commit/fac98dc17e7ad08b89bfdbda4a9aa884727d125a)
#### Saturday 2023-11-04 04:50:36 by ThatAlo

Holy Fucking Bingle. What?! :3

MY CODE WORKED AND I'M AMAZED!!!

Changes:
 - Auto has been moved to a separate file and is now selected with a sendable chooser
 - Multiple files for commands, each grouped into their respective namespaces.  
 - An auto that *should* be able to fetch a cube.  key word: *should*

TODO:
 - Mechanical:
     - Replace the front-right drive motor, because the bearing is failing.
     - Re-tread the swerve wheels, or potentially switch to the colsons
     - Re-work the intake so that the bottom has rollers, and so that the bolt is not necessary to stop the arm.  
 - Programming
     - Get the arm working fully as its own subsystem, its a bit goofy right now ( allow it to have a default command )
     - Tune speeds on the field to more accurate values for better autos
     - Add more auto routines to the list, teach Bradley and others how to use the new system
 - Misc
     - SysId the robot for potential future ramesete controller usage?
     - Teach all programmers who have previously used timed how command works (bradley, dean, salem)

Pipe dreams:
 - Vision processing
 - Assistive driving
 - VR integration through network tables?

---
## [DigiDuncan/CSB2023](https://github.com/DigiDuncan/CSB2023)@[b2d65cabbd...](https://github.com/DigiDuncan/CSB2023/commit/b2d65cabbdbaf35f1975489fd3010f2109600261)
#### Saturday 2023-11-04 05:19:03 by Arceus3251

Removed the previous button from the minigames

Fuck you, @cs188

---
## [frison/100hellos](https://github.com/frison/100hellos)@[85f4716a5a...](https://github.com/frison/100hellos/commit/85f4716a5ad44cccc489bd60b2b48dbfe0a7ae39)
#### Saturday 2023-11-04 05:25:27 by Tim Frison

Github Actions! 100hellos/[lang]

Why not build and publish each of the containers? Is it bat-shit level
overkill for "Hello World!"? Absolutely. But why isn't there a home for
all of the "Hello"'s? How many "Hello" environments have been lost to
time?

Also, shouldn't that process have the best fucking developer experience
I could conceive of? Absolutely.

ALL YOU NEED TO DO IS MAKE THE FOLDER -- it'll be published
ONLY RELEVANT THINGS ARE BUILT -- save the planet with less builds
EASY .no-publish LIST -- behaves how you'd think

Did you know there is something called "Time to Hello World"?

70 to go.

---
## [KianBanh/DiefFTC23-24](https://github.com/KianBanh/DiefFTC23-24)@[f680f73d24...](https://github.com/KianBanh/DiefFTC23-24/commit/f680f73d24c27c64012ef188db3c0daad75d9421)
#### Saturday 2023-11-04 05:38:23 by jace-wong

what the fuck am i doing with my life 🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🙃🤬🤬🤬🤬🤬🤬🐸🐸🐸🐸🐸🐸🐸🐸🤬🤬🤬🐸🐸🤬🤬🧱🧱🧱🧱🧱👩‍🎤👩‍🎤👩‍🎤👩‍🎤👩‍🎤🎄🎃🎃🎃🎃🍩🍩🍩🚑🚑🚑🚑🚑🚑☸️☸️☸️☸️✡️✡️help me

this code sucks absolute balls

whos to say it even works

not ME

but thats a problem for tomorrow me 😎😎😎😎😎

---
## [mozilla-mobile/mozilla-vpn-client](https://github.com/mozilla-mobile/mozilla-vpn-client)@[6bf1add73e...](https://github.com/mozilla-mobile/mozilla-vpn-client/commit/6bf1add73eb06b1bbf1c994feb7cdcde00e403e4)
#### Saturday 2023-11-04 06:01:05 by Beatriz Rizental

Enable sign in cancel button click test

Ok, this is just a bit hacky. The test was failing because that button is
below the fold. We'd have to scroll down to actually click on it. However,
I cannot figure out how to scroll down for the life of me. I talked to Matt L.
and he showed me the fun fact that if you click right on the fold without
scrolling turns out you already reach the cancel button.

Now, tests are clicking in the middle of elements. So what I did is I changed
the test to actually click at the top right corner of the element. In practice,
this makes no difference. So instead of embarking in yet another rabbit hole
to fix this, I refrained.

---
## [Huawei-Dev/android_kernel_huawei_btv](https://github.com/Huawei-Dev/android_kernel_huawei_btv)@[05d723db4d...](https://github.com/Huawei-Dev/android_kernel_huawei_btv/commit/05d723db4d8391c2f8d14f59e070f8347201d26b)
#### Saturday 2023-11-04 08:04:58 by Christian Brauner

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
## [jro31/slowmadding](https://github.com/jro31/slowmadding)@[9f5e41f2b6...](https://github.com/jro31/slowmadding/commit/9f5e41f2b68e24f1ecb633c61f338ec99509fb99)
#### Saturday 2023-11-04 08:27:37 by Jethro Williams

Attempt to consider user's timezone when generating timeline

Fuck I hate timezones.

This commit reverts the previous change of adding a timezone to the `formatDate` function, which wasn't working anyway because I'd used `timezone` instead of `timeZone`, because that's the kind of genius I am, but I also decided this wasn't the place to mess around with timezones and any date passed-in here shoiuld be formatted in UTC anyway so that it will be rendered the same no matter where the user is (so long as it's passed-in as a UTC date).

Instead, the key change is that we're using the local date for the user in the timeline component (imported into the timeline in the `usersDate` variable) and comparing that date to the arrival/departure in place of the `beginningOfToday` variable, which was the beginning of the current day in UTC time, but was inaccurate if the date for the current user differed for the current UTC date.

This, in theory, will keep the timeline accurate for the local user at all hours of the day so even after midnight, my current stay should say 'now' instead of a date.

That was a lot of work just to say 'now' for a bit longer.

As the `formatDate` function is used in a lot of places, all should be checked (before and after midnight) as displaying dates correctly, particularly the timeline.

---
## [Nabu-upsidedowncake/android_kernel_common](https://github.com/Nabu-upsidedowncake/android_kernel_common)@[453e18e5d4...](https://github.com/Nabu-upsidedowncake/android_kernel_common/commit/453e18e5d4dcd597f10356b509d0ccd889d2aa66)
#### Saturday 2023-11-04 09:34:56 by Douglas Anderson

BACKPORT: migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead.
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
(cherry picked from commit 4bb6dc79d987b243d65c70c5029e51e719cfb94b)

Conflicts:
   mm/migrate.c

This is because we don't have folios in the v5.15 kernel. If we ever
decide to backport folios to v5.15, I'd suggest reverting this patch
(which should have no dependencies) and then picking the clean one
from upstream. The only difference in this patch from the upstream one
is folio_test_uptodate(src) => PageUptodate(page). and the context
difference of folio_lock(src) => lock_page(page).

BUG=b:277132613
TEST=Won't block waiting for that lock anymore

Change-Id: Ia86ccac02a303154a0b8bc60567e7a95d34c96d3
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671371
Tested-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Vovo Yang <vovoy@chromium.org>
Commit-Queue: Douglas Anderson <dianders@chromium.org>
(cherry picked from commit e7e4ca0a49d27e57045567c8bb883035f71f53a8)
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671867
Auto-Submit: Douglas Anderson <dianders@chromium.org>
Commit-Queue: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>
Bot-Commit: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>

---
## [Anankke/SSPanel-Uim](https://github.com/Anankke/SSPanel-Uim)@[b70dcedea6...](https://github.com/Anankke/SSPanel-Uim/commit/b70dcedea680863e47993c959c19ff6db8051907)
#### Saturday 2023-11-04 09:36:04 by M1Screw

refactor: add model value hint & rename setting to config

Fuck you and your stupid model name

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[33465c1c86...](https://github.com/ZacharyTStone/ZacharyTStone/commit/33465c1c861d003e014f972686ec3bc1694412b9)
#### Saturday 2023-11-04 10:04:03 by ROBO-ZACH

Update README with new quote: "I cannot even imagine where I would be today were it not for that handful of friends who have given me a heart full of joy. Let's face it, friends make life a lot more fun." <br>— Chuck Swindoll

---
## [Code-Lab-1/programming-skills-portfolio-N1X-KUN](https://github.com/Code-Lab-1/programming-skills-portfolio-N1X-KUN)@[4168fc5360...](https://github.com/Code-Lab-1/programming-skills-portfolio-N1X-KUN/commit/4168fc5360eaf3c2631f4bd0b4ec79e2e805c6f8)
#### Saturday 2023-11-04 10:10:03 by Gerard Matthew

Assessment Chapter 2

I did not enjoy Exercise 5 because its a Math Problem... I was a student and I know how much we hate Math Real Life Problems
And doing this exercise felt like I was a teacher giving a Math Problem to my students thus the feeling of guilt...

Ok that had no connection there but at least I commented on this one

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[468afa292d...](https://github.com/ReturnToZender/ReturnsBubber/commit/468afa292dfaef7bcbc6df7b55cd0380582533a6)
#### Saturday 2023-11-04 11:00:31 by BurgerLUA

Adds the WT-551, Unskyrats the WT-550 ammo (#655)

## About The Pull Request


## The WT-551

![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/d57f5767-366e-4835-a5bf-d965b6b375a6)

This adds the WT-551. A remade version of the WT-550 that is worse in
every way. Fortunately, that means that it is balanced enough to be put
in NanoTrasen armories.

Compared tot he WT-551, it is bulkier and slightly slower (0.3 second
fire delay compared to 0.2). Additionally, it is commonly used with
rubber-tipped rounds or FlatHead rounds, which are a special surplus of
ammo that deals less damage and has no wounding, embedding, or
penetrative power. Regular ammo can be purchased from cargo or
researched later, with special ammo also being available later.

Note that this does not replace the WT-550.

## FlatHead ammo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/81de4bdb-6fd6-4f23-a1b1-0af21e924c34)

Flathead ammo deals 18 brute damage (compared to the original 20), and 5
stamina damage per hit. It is extremely weak against armor, has no embed
chance, has virtually no wounding chance. It's perfect for cheap
corporate companies dealing with cheaper personnel. This is the type of
lethal ammo that security will use for the gun, unless someone speedruns
weapon research.


## Research Progression


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/26b72a1c-ebda-439a-98c9-9dc3168e01bd)

### Basic WT-550/WT-551 Ammunition.
Flathead rounds and Rubber rounds for the WT-550/WT-551 can be
researched for 2500 points after unlocking the "Weapon Development
Technology" node.

### Advanced WT-550/WT-551 Ammunition.
Regular rounds and AP rounds for the WT-550/WT-551 can be researched can
be researched for 5000 points after unlocking the "Advanced Weapon
Development Technology" and "Basic WT-550/WT-551 Ammunition" nodes.

### Illegal WT-550/WT-551 Ammunition.
Incendiary rounds for the WT-550/WT-551 can be researched can be
researched for 7500 points after unlocking the "Illegal Technology",
"Exotic Ammo" , and "Advanced WT-550/WT-551 Ammunition" nodes.

### Syndicate Research

Removes the WT-550 ammo from syndicate research since it is now
redundant.

## Cargo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/a24e9df4-36e3-4368-b77a-cff06a42579f)

WT-551 rifles can be ordered in pairs (2) for the cost of a parrot, a
grilling starter pack, or a crab rocket (1600 credits). This value was
chosen because it is slightly higher than the thermal pistols, and the
traitor-ordered WT-550 rifle pack (which contains lethal ammo + spare
lethal ammo).

Additional FlatHead, Rubber, and Regular ammo can be ordered from cargo
as well.

Cargo techs no longer get WT-550s in the mail, but instead WT-551s (why
was this a thing holy shit).

## Armory


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/e88a37af-2e4f-4b1c-bc25-b9bed9e41b91)

2 WT-551s can be found in the armory.
For balance purposes one (1) laser rifle was removed.

## I hate Skyrat so much holy shit


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/b09eed34-77cd-4f37-8356-93688fec344e)

Unfucks the WT-550 ammo types by removing their dumb names and changed
caliber types.

Unfucks the WT-550 ammo in the ammo printer so that rubber rounds can be
printed at T0 and everything else (except incendiary rounds) can be
printed with the adv munitions disk.

The bullets for the WT-550 have been forcibly changed to /tg/ balance,
which means that any and all future Skyrat PRs cannot touch the damage
values for it (unless some fuckery occurs, idk).

## Why It's Good For The Game


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/395b9fa5-8380-46bc-96a7-06ce0931d8e7)


Security is in dire need of actual ballistics. /tg/ removed ballistics
from security because of reasons I legitimately don't think are valid.
It's also a huge balance concern for security not to have at least 1
ballistic weapon (other than the shotgun) because it doesn't stop antags
from hoarding laser immunity or meds.

Also guns are cool.

## Changelog

:cl: BurgerBB
add: Adds the WT-551 rifle, a redesign of the WT-550 rifle that is
balanced (citation needed) for security use.
add: Makes WT-550 ammo researchable and orderable from cargo. Removes
WT-550 ammo from syndicate research, and gives them their own
categories.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>
Co-authored-by: ReturnToZender <donwest947@gmail.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[b3e46b4a3d...](https://github.com/wrye-bash/wrye-bash/commit/b3e46b4a3d96e2bff5e003bd81540604c18920fd)
#### Saturday 2023-11-04 11:29:50 by MrD

[!]WIP gui resources:

This was meant to be more granular - I wanted to centralize image
initialisation including setting dirs['image'] - turned out that constants
were imported too early (#600, control import order), (mopy) dirs were
not initialised and this necessitated moving the image
definitions in initStatusBar - however to make this simpler I renamed
the images based on the key in tooldirs (ini backwards compat). We could:

- turn all these to svgs?
- add a sensible default to the image dict? (we could do this instead of
the CI hack)
- further centralise get_*** from _gui_globals especially get_image_dir
- CI Hack - move to caller or add a param

Next commit finalizes this - for now bye staticBitmap, au revoir, auf
wiedersehen etc. Also see the GuiImage imports and dirs['images'] go
down and imgDirJoin (make ugly code look ugly) centralised - getting
somewhere:

"""
Thou hast committed bugs, but that was in another language, and besides,
the critters are dead.
"""

Note cause initially _icons were defined in `import balt` time and
images were not initialized yet the imports would crash cause:

if not os.path.isabs(img_path):
    img_path = os.path.join(get_image_dir(), img_path)

would produce a relative (non-existing) path and we would
land in _tkinter_error_dial - which crashes bigtime on mac:

2023-10-10 14:49:27.496 Python[11010:375752] -[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0
2023-10-10 14:49:27.503 Python[11010:375752] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0'
...
libc++abi: terminating due to uncaught exception of type NSException

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)

To fix `import balt` crash I moved Colorchecks images init to gui.
This now crashed on importing basher in Mopy.bash.bash._main -
when constants is imported still get_image_dir() returns ''

Traceback (most recent call last):
...
  File "/Users/.../Mopy/bash/basher/constants.py", line 458, in <listcomp>
    return [GuiImage.from_path(template % x) for x in (16, 24, 32)]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 90, in from_path
    return _BmpFromPath(img_path, iconSize, img_type, quality)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 56, in __init__
    raise ArgumentError(f'Missing resource file: {self._img_path}.')
bash.exception.ArgumentError: Missing resource file: tools/isobl16.png.

To fix this I had to finally ---> Simplify tools init:

Here is the map of filenames that differed:

{'ISRMG': "insanity'sreadmegenerator", 'ISRNG': "insanity'srng",
 'ISRNPCG': 'randomnpc', 'OBFEL': 'oblivionfaceexchangerlite',
 'OBMLG': 'modlistgenerator', 'BSACMD': 'bsacommander',
 'Tes4FilesPath': 'tes4files', 'BlenderPath': 'blender', 'GmaxPath': 'gmax',
 'MayaPath': 'maya', 'MaxPath': '3dsmax', 'FastStone': 'faststoneimageviewer',
 'PaintNET': 'paint.net', 'PaintShopPhotoPro': 'paintshopprox3',
 'PhotoshopPath': 'photoshop', 'PixelStudio': 'pixelstudiopro',
 'MAP': 'interactivemapofcyrodiil', 'NPP': 'notepad++',
 'RADVideo': 'radvideotools'}

I hope no one relied on these. Now as seen having to deal with two image
formats introduces complexity - there was a merge about that no ? <--- RRR
There is also the matter of game dependencies - and settings saving - and
profiles per game - that's # RRR launchers

Accept Path in GuiImage.from_path:

os.path.splitext(img_path) works fine for path - yey for os.pathlike!

inline _init_tool_buttons - note that TesVGecko was added twice

things like

renames = {
    'OblivionBookCreatorPath': 'oblivionbookcreator%s.png',
    'Tes4GeckoPath': 'tes4gecko%s.png',
    'Tes5GeckoPath': 'tesvgecko%s.png',
    'Tes4ViewPath': 'tes4view%s.png',
    'Tes4TransPath': 'tes4trans%s.png',
    'Tes4LodGenPath': 'tes4lodgen%s.png',
    'NifskopePath': 'nifskope%s.png',
}
tooldir = '/Users/.../Mopy/bash/images/tools'
for k, v in renames.items():
    for pix in (16,24,32):
        try:
            shutil.move(_j(tooldir, v % pix), _j(tooldir, f'{k.lower()}{pix}.png'))
        except Exception as e:
            print(k,v,e)
            break

One (1) use of app_buttons_factory - yes! This is geared towards # 570
and initTooldirs

The [!] for image renames - this was 99% of the perspiration - dict
used:

{
    'nifskope16.png': 'nifskopepath16.png',
    'nifskope24.png': 'nifskopepath24.png',
    'nifskope32.png': 'nifskopepath32.png',
    'oblivionbookcreator16.png': 'oblivionbookcreatorpath16.png',
    'oblivionbookcreator24.png': 'oblivionbookcreatorpath24.png',
    'oblivionbookcreator32.png': 'oblivionbookcreatorpath32.png',
    'tes4gecko16.png': 'tes4geckopath16.png',
    'tes4gecko24.png': 'tes4geckopath24.png',
    'tes4gecko32.png': 'tes4geckopath32.png',
    'tes4lodgen16.png': 'tes4lodgenpath16.png',
    'tes4lodgen24.png': 'tes4lodgenpath24.png',
    'tes4lodgen32.png': 'tes4lodgenpath32.png',
    'tes4trans16.png': 'tes4transpath16.png',
    'tes4trans24.png': 'tes4transpath24.png',
    'tes4trans32.png': 'tes4transpath32.png',
    'tes4view16.png': 'tes4viewpath16.png',
    'tes4view24.png': 'tes4viewpath24.png',
    'tes4view32.png': 'tes4viewpath32.png',
    'tesvgecko16.png': 'tes5geckopath16.png',
    'tesvgecko24.png': 'tes5geckopath24.png',
    'tesvgecko32.png': 'tes5geckopath32.png',
    'blender16.png': 'blenderpath16.png', 'blender24.png': 'blenderpath24.png',
    'blender32.png': 'blenderpath32.png', 'bsacommander16.png': 'bsacmd16.png',
    'bsacommander24.png': 'bsacmd24.png', 'bsacommander32.png': 'bsacmd32.png',
    'faststoneimageviewer16.png': 'faststone16.png',
    'faststoneimageviewer24.png': 'faststone24.png',
    'faststoneimageviewer32.png': 'faststone32.png',
    'gmax16.png': 'gmaxpath16.png', 'gmax24.png': 'gmaxpath24.png',
    'gmax32.png': 'gmaxpath32.png',
    "insanity'sreadmegenerator16.png": 'isrmg16.png',
    "insanity'sreadmegenerator24.png": 'isrmg24.png',
    "insanity'sreadmegenerator32.png": 'isrmg32.png',
    "insanity'srng16.png": 'isrng16.png', "insanity'srng24.png": 'isrng24.png',
    "insanity'srng32.png": 'isrng32.png', 'randomnpc16.png': 'isrnpcg16.png',
    'randomnpc24.png': 'isrnpcg24.png', 'randomnpc32.png': 'isrnpcg32.png',
    'interactivemapofcyrodiil16.png': 'map16.png',
    'interactivemapofcyrodiil24.png': 'map24.png',
    'interactivemapofcyrodiil32.png': 'map32.png',
    '3dsmax16.png': 'maxpath16.png', '3dsmax24.png': 'maxpath24.png',
    '3dsmax32.png': 'maxpath32.png', 'maya16.png': 'mayapath16.png',
    'maya24.png': 'mayapath24.png', 'maya32.png': 'mayapath32.png',
    'notepad++16.png': 'npp16.png', 'notepad++24.png': 'npp24.png',
    'notepad++32.png': 'npp32.png',
    'oblivionfaceexchangerlite16.png': 'obfel16.png',
    'oblivionfaceexchangerlite24.png': 'obfel24.png',
    'oblivionfaceexchangerlite32.png': 'obfel32.png',
    'modlistgenerator16.png': 'obmlg16.png',
    'modlistgenerator24.png': 'obmlg24.png',
    'modlistgenerator32.png': 'obmlg32.png',
    'paint.net16.png': 'paintnet16.png', 'paint.net24.png': 'paintnet24.png',
    'paint.net32.png': 'paintnet32.png',
    'paintshopprox316.png': 'paintshopphotopro16.png',
    'paintshopprox324.png': 'paintshopphotopro24.png',
    'paintshopprox332.png': 'paintshopphotopro32.png',
    'photoshop16.png': 'photoshoppath16.png',
    'photoshop24.png': 'photoshoppath24.png',
    'photoshop32.png': 'photoshoppath32.png',
    'pixelstudiopro16.png': 'pixelstudio16.png',
    'pixelstudiopro24.png': 'pixelstudio24.png',
    'pixelstudiopro32.png': 'pixelstudio32.png',
    'radvideotools16.png': 'radvideo16.png',
    'radvideotools24.png': 'radvideo24.png',
    'radvideotools32.png': 'radvideo32.png',
    'tes4files16.png': 'tes4filespath16.png',
    'tes4files24.png': 'tes4filespath24.png',
    'tes4files32.png': 'tes4filespath32.png'
}

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[bd0a8972b0...](https://github.com/wrye-bash/wrye-bash/commit/bd0a8972b0cb66091a2943d0f23b75d89e94c576)
#### Saturday 2023-11-04 11:29:50 by MrD

Merge branch 'ut-366-image-570-launchers' into 190-lazy-de-wx:

Making ImageWrapper -> GuiImage(Lazy) made possible to centralize
image handling and finalize the app_buttons refactoring. Highlights:

- global balt.images is dropped - encapsulated into _gui_globals and
accessors defined. The latter will be put to more good use in lazy-pt2
- global bass.tooldirs is dropped. See commits for the gory details - in
short tooldirs, were populated to be checked once - in a horribly
complicated manner. Now we fish the keys from the ini JIT and use them
once, when the app_buttons dictionary is populated (this will change in
"WIP inisettings" commit to provisionally stash them in inisettings)
- we now instantiate *all* possible (predefied) status bar buttons, but
enable them per game solving an ancient TODO and at the same time
making settings portable between installs - this was a showstopper for

Future directions for #570:

- we should stop reading tool paths from the ini - instead specify those
from a settings page - ideally in 312 we read and warn and in 313 we
stop reading the ini
- same goes double for the App folder - read .lnk, populate the settings,
warn that App folder will be dropped in 313 then drop it

This will take down a few hacks and permit us to use the app_launcher
as the uid (no more app_key)

As for the images API - I think GuiImage will do. The weird logic is in
the _native_widget (property) overrides - sleek and ready for us to find
the one right way of instantiating the images, including maybe making
more svgs. Also there are some more uses of wx.image in `gui` that need
centralizing and a few loose ends in initialization (including the CI
hack or having a default fallbback image) but we can close #366, heavy
lifting is done the rest is low priority.

---
## [amochuko/zechub](https://github.com/amochuko/zechub)@[0d97121c8c...](https://github.com/amochuko/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Saturday 2023-11-04 12:44:07 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [Total-RP/Total-RP-3](https://github.com/Total-RP/Total-RP-3)@[ba0580eab6...](https://github.com/Total-RP/Total-RP-3/commit/ba0580eab600b5632725702cfd5f219086557b1c)
#### Saturday 2023-11-04 13:32:29 by Daniel Yates

Add guild name/rank misc. info presets (#704)

* Add guild name/rank misc. info presets

Two new presets have been added for guild name and rank to the
additional info fields in a profile. Like pronouns, these fields are
treated specially for both display in tooltips and via MSP comms.

When showing a tooltip for a player if they have a custom guild name
set then it will fully override and replace the guild name that would
have otherwise been shown based off their players' guild affiliation.
The rank will be set to that of the "Guild rank" info field if present,
or will default to a sensible "Member" string.

If the player has only a custom guild rank but no guild name, then only
the rank of their players' actual guild will be replaced.

For MSP comms two new fields have been added for guild name and rank;
"PG" and "PR" respectively. Use of the "G*" namespace was avoided due
to that being used for "game info" fields like unit GUID.

* Add numeric ID field to Misc. info presets

Our existing misc info field system has some annoying complexity where
multiple parts of the code (tooltips and MSP) need to check for both
localized and english names of fields when looking for "special"
things like pronouns.

This has a few issues - most notably that people who send a non-english
field name to someone else running in a different language won't
result in the field displaying correctly in the tooltip.

With these changes misc. info fields now have an integral "ID" field
that identifies the source type (or preset) a field was initially
created from.

Note that it is possible for users to still rename fields created
from presets - so you *can* run into weird situations if you've
created a "Pronouns" field and then renamed it to "Guild name"; the
ID would still register it as Pronouns.

Despite this however, that one downside is far less problematic than
the localization problem - so we can live with it for now. Some
new utilities have been added to work with misc. types and to obtain
structured views of misc. info fields that don't expose the inner
layout of the saved data.

* Expose custom guild data via nameplates

* Rename physiognomy to "Facial features"

"Facial" now looks like a bit of a weird word.

* Fix small typo

* Add voice reference preset and tooltip display

* Don't overwrite pronouns silly

* Add IDs to imported MI fields

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[a0064712f7...](https://github.com/yarnpkg/berry/commit/a0064712f7b0ae38c21fb204bea9831c2b269bd7)
#### Saturday 2023-11-04 13:43:04 by Maël Nison

Bumps Node requirements from 14 to 18 (#5445)

**What's the problem this PR addresses?**

We're still supporting Node 14, but it has reached end of life. Node 16
is still maintained, but will reach an early end of life in October, so
I think it's reasonable to drop it now rather than publish a major
release just for that.

**How did you fix it?**

Bumps the requirements from `14.16` to `18.12` (first LTS from the 18.x
release line).

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---------

Co-authored-by: Kristoffer K <merceyz@users.noreply.github.com>

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[21fcc792bf...](https://github.com/yarnpkg/berry/commit/21fcc792bf83825aa051c51c96cdc683ee85d20b)
#### Saturday 2023-11-04 13:43:04 by Maël Nison

Sets the default compression to 0 (#5526)

**What's the problem this PR addresses?**

Cache compression doesn't seem the best option nowadays:

- It adds significant time to installs
- It adds a non-negligible runtime overhead (partially related, #1817)
- It prevents Git from diffing archives when they're modified

Its main advantage is for some amazingly large packages, where storing
them inside a Git repository would be impossible (GitHub has a 600MB
file limit). But since we changed the cache default to
`enableGlobalCache: true`, this isn't relevant by default, so the cache
compression should be set to zero.

One potential issue is how it may give the impression that Yarn became
worse for global cache users. We don't believe it's the case (Git can
delta uncompressed archives in some measure, making it less expensive to
upgrade from one package version to another), but to the average eye it
may not look as such.

**How did you fix it?**

This diff sets the new default compression setting to 0.

To avoid breaking projects' (or at least not making the migration more
difficult), I added a rule to automatically set `compressionLevel` (and
`enableGlobalCache`) to their 3.x default values when running `yarn
install` in a 3.x project. When users are ready they can remove these
settings and re-run the install.

I kept the current compression level on our repository to avoid changing
all archives again. I think we'll have to think of purging the
repository in some form to migrate it to `compressionLevel: 0`.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[ec7f37a8ca...](https://github.com/yarnpkg/berry/commit/ec7f37a8ca118a6f73f848e993272db957f286d6)
#### Saturday 2023-11-04 13:43:04 by Maël Nison

Modernizes installs' output (#5509)

**What's the problem this PR addresses?**

I wasn't entirely happy with the Yarn output:

- When running `yarn add`, we have no way to know what packages are
actually added to the lockfile. The cache messages sometimes help, but
with zero-installs now being opt-in, in many cases the packages would
already be in the cache and thus wouldn't be displayed at all.

- The "can't be found in the cache and will be fetched from the remote
registry" messages were incredibly slow to print - the same install
would take 28s install for Gatsby on a local iTerm 2 without those logs,
vs almost 2 minutes with. They also weren't very useful: we were only
showing the last 5 of them, and with zero-installs being opt-in in many
cases they wouldn't be shown at all.

- The `node-gyp` warnings were for the most part unactionable (at best
the user would pin a fixed version in their `packageExtensions` field,
which I suspect no one ever did).

- The `deprecated` warnings were for the most part unactionable, and
only printed in very specific cases (the first time they were added to
the project).

- The "missing / invalid peer dependency" warnings were actionable, but
in practice no one really look at them except when something breaks -
and even then, it becomes unreadable when there are too many of them.

- The skipped build warnings were printed every single time you ran
`yarn install`. It's nice to know the first time, then it quickly
becomes redundant.

Fixes #4165

**How did you fix it?**

I went a little overboard and did everything in the same PR ... at first
I thought I wouldn't have to change unrelated parts, but then I finished
implementing the skipped build warnings duplicate removal and oh no 🙈

- Only peer dependency warnings caused by workspaces are now reporter.
They have also been moved inside the post-resolution validation step.
The resolution step is now expected to only do one of two things: either
report an error when the resolution fails, or report the packages which
got added / removed from the lockfile.

- The `node-gyp` warnings have been removed.

- The `deprecated` warnings have been removed from the install. The
`yarn npm audit` command now reports deprecated packages, although this
can be disabled using `--no-deprecations` (or any of the audit filtering
settings).

- The "can't be found in the cache" messages have been removed. Instead,
the fetch step will report the number of cache hits / cache misses once
it's finished (same behaviour as `preferAggregateCacheInfo`). The size
delta will also be reported.

- Packages whose build was skipped are now stored within
`Project#skippedBuilds`, which is stored within the install state file.
Warnings are only emitted if the install was skipped for the first time.
To see the messages again, users can run `yarn rebuild`.

- Added the Yarn version on installs. A bit because of branding when
screenshot are taken, but mostly so we easily know what version are
people using when they share screenshots to us. In a follow-up PR I'd
like to try to retrieve the latest version from the website, to let them
know once one is available.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[3626ea2ae3...](https://github.com/yarnpkg/berry/commit/3626ea2ae3e48ee26771b15b92292a28afe3d49d)
#### Saturday 2023-11-04 13:43:04 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [RaniKumari10/Internship](https://github.com/RaniKumari10/Internship)@[f7bdd08d99...](https://github.com/RaniKumari10/Internship/commit/f7bdd08d99c1d7851382b7220d5e51d054c2c4de)
#### Saturday 2023-11-04 14:11:31 by Rani_Kumari

Create README.md

**Title: Web Scraping, Machine Learning, and Python Practice Project**
**Description:** 
I completed practice project seamlessly integrated web scraping, machine learning, and Python programming to address a practical, real-world challenge. This comprehensive endeavour encompassed the entire data analysis workflow, from data acquisition to preprocessing, modelling, and prediction. 
Here's an overview of the project's journey:
**Project Overview:**
The project was framed within the context of a retail company's necessity to predict product demand, utilizing historical sales data, and I encountered various areas to navigate through during the practice project.
I successfully navigated through the following stages:
**1. Data Collection (Web Scraping):**
I harnessed the power of web scraping to extract essential product-related data from an e-commerce website. This data included intricate details such as product descriptions, prices, customer reviews, and historical sales data.
**2. Data Preprocessing:**
I was handling of the scraped data involved thorough cleaning and structuring. I meticulously addressed missing values, outliers, and applied text data processing techniques. Further, I seamlessly merged the web-sourced data with historical sales records.
**3. Feature Engineering:**
The art of feature engineering was brought to life as I created insightful features from the raw data. I explored statistical relationships and identified significant trends that would ultimately enhance our predictive model.
**4. Machine Learning:**
My journey culminated in the training of a robust machine learning model that was finely tuned to predict product demand with precision. Model evaluation was executed systematically, employing appropriate metrics to ensure optimal performance.
**5. Visualization and Reporting:**
The project findings were masterfully presented through compelling visualizations and insights. My in-depth report and presentation skillfully summarized the entire analysis and predictions, offering a comprehensive overview of our work.
**Requirements:**
My proficiency in web scraping was a key asset, relying on Python and essential libraries such as BeautifulSoup, Selenium, and more. I demonstrated my familiarity with data preprocessing, feature engineering, and machine learning in Python, all supported by an adept command of data visualization and robust problem-solving skills.

**Benefits:**
This practice project has enriched our skills, allowing me to seamlessly integrate web scraping, data preprocessing, machine learning, and Python programming. I have gained valuable experience, tackled a real-world challenge, and showcased our abilities in data analysis and predictive modeling.
With the successful completion of this project, I have added a powerful asset to my portfolio. It demonstrates my  capacity to extract data from the web, process it effectively, build accurate predictive models, and make informed, data-driven predictions. This project serves as a testament to our abilities, making us valuable assets for roles in data science, machine learning engineering, or web scraping professionals.

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[d85b5a0ddf...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/d85b5a0ddfb092c80aa9a725c24bec9f6c56d952)
#### Saturday 2023-11-04 14:20:36 by Abhishek Shrivastava

OCI - 1Z0-1122-23

New feather added in #MyCloudDiary :: https://lnkd.in/dHAMiTcH ..



I have some exciting news to share! I have just uploaded a comprehensive practice test for the 1Z0-1122-23 Oracle Cloud Infrastructure 2023 AI Foundations Associate certification, on Udemy.



You can search 1Z0-1122-23 OCI 2023 AI Foundation Trial



This practice test is designed to help aspiring candidates like us prepare for the exam with confidence. It covers all the essential topics and provides realistic questions to simulate the actual exam experience. Whether you're aiming to become certified or simply want to strengthen your understanding of AI within the OCI environment, this practice test can be a valuable resource. Feel free to check it out and let me know your thoughts.



Certification Link :: https://brm-certification.oracle.com/apex/f?p=1111:6:14885428904220:::::#xd_co_f=YTY0MjMyMGItM2ZjZC00NDQyLTg0MTktZTJlMzFhZDAzOThh~



Please like ,share and subscribe below #channelpartners on

#YouTube :: https://lnkd.in/d2zATThK

#GitHub :: https://lnkd.in/dHAMiTcH

#Hashnode :: https://lnkd.in/d_gtGxuS

#Twitter :: https://lnkd.in/e5ZY5j-x

#DevCodeCommunityTLV :: https://lnkd.in/duMEcSnc

#Tealfeed :: https://lnkd.in/eTyp-Xe4

#Medium :: https://lnkd.in/dpEzM8GU



CC- Adding my leaders and colleagues to share achievement::

Mahesh Bhosale Swapneel Doshi Girish Chhabra Luis Méndez Osvaldo Cantu Jason Chance Anji Reddy Venumula Susan Cutinha Murli Reddy EUR ING Ioannis Kolaxis MSc Sabahat Siddiqui Amit Batra, PMP® Rajeev Choudhary Mukul Sharma Dr. Ritu Anand Farhad Sayeed Pritish Kumar Anand Sitaraman Abhishek Saxena Kumar Amitesh Pawan Kumar Chadha Vijay Bijjargi



Education for Cloud Leaders :: Dan Rey Denise Reed Lamoreaux Sjoukje Zaal Deepak Rajendran Kasam Shaikh - Microsoft [Azure] AI MVP ☁ 🇮🇳 Yujun Liang ⎈☁️🌎 Yongkang ⎈ ☁️ HE Walter Lee Assoc. Prof. Dr. Eleni Meletiadou, SFHEA, UTF, MCIPD, CMBE,MIE Expert Dahnesh Dilkhush Nikkia Carter



#mvpbuzz #mct #devops #cloud #software #community #oraclecloud #oci #oraclecertified  #awscommunitybuilders #dataanalytics #share #microsoft #like #github #dataanalysis #kubernetes #kubernetesservices #kubernetescluster #azure #aws #complexity #amazon #google #leadershipbyexample #IAmRemarkable #architecturelovers #architect #education #k8s Tata Consultancy Services #cybersecSecurity #security #power #leaders #cybersecurity #mvpbuzz #mvp #mvps #mct #powerbiexperience #IAmRemarkable #ArtificialIntelligence Embassy of the Republic of Latvia to the United Kingdom of Great Britain and Northern Ireland 

#oracle #oraclecertified #oraclecloudinfrastructure #oraclecloudinfrastructureai

#FirstAIcertification

#ai 

#aicertification 

#aicertified

---
## [RUHiLoKHande/GovServices-Complaints](https://github.com/RUHiLoKHande/GovServices-Complaints)@[a6ed91dd40...](https://github.com/RUHiLoKHande/GovServices-Complaints/commit/a6ed91dd40e7673274535cb88abc6a713a885436)
#### Saturday 2023-11-04 15:26:35 by RUHiLoKHande

Add files via upload

Description:

Welcome to our dynamic and interactive website powered by a robust technology stack! We've harnessed the power of HTML, CSS, JavaScript, PHP, the XAMPP server, and MySQL to deliver an exceptional online experience.

HTML & CSS: Our web pages are crafted with HTML (Hypertext Markup Language) for structuring content and CSS (Cascading Style Sheets) for beautiful, responsive design. This combination ensures that your journey through our site is visually pleasing and user-friendly.

JavaScript: Interactivity is at the heart of our website. JavaScript, the versatile scripting language, empowers you to engage with our content. Enjoy features like dynamic forms, animations, and real-time updates that enhance your browsing experience.

PHP: Behind the scenes, PHP (Hypertext Preprocessor) handles server-side scripting. It enables us to create dynamic web pages, process forms, and interact with our MySQL database, ensuring that the content you see is always up to date.

XAMPP Server: Our website relies on the Apache server provided by XAMPP, a powerful and cross-platform web server solution. It ensures fast and secure delivery of web content, making your interactions with our site seamless and secure.

MySQL: We store and manage data efficiently using MySQL, a reliable and scalable relational database management system. Your user information, preferences, and much more are securely stored and retrieved from our MySQL database.

---
## [Ricardobs/Na-Moral](https://github.com/Ricardobs/Na-Moral)@[2f62a993f7...](https://github.com/Ricardobs/Na-Moral/commit/2f62a993f7458e4a9a6d29199993e444ba5965f3)
#### Saturday 2023-11-04 16:01:43 by Ricardobs

Update README.md

Na Moral: Your Chat Buddy for Workplace Harassment

'Na Moral' is your ally in understanding workplace harassment. Through personal conversations, you can exchange ideas with the bot and receive both legal and psychological guidance and support.

What 'Na Moral' offers:

Sensitive Understanding: The bot is here to listen, answer your questions, and provide information about workplace harassment in a safe and confidential environment.

Legal Guidance: 'Na Moral' offers clear and helpful legal information related to workplace harassment, helping you understand your rights and legal options.

Psychological Support: In addition to legal matters, 'Na Moral' is also available to provide guidance on mental health, offering emotional support during challenging times.

Customized Conversations: Each chat with the bot is unique and tailored to your specific questions and concerns.

'Na Moral' is committed to providing accurate and ethical information while promoting awareness of workplace harassment and the importance of mental health. We're here to help you understand and deal with this important topic.

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[bf4671ff83...](https://github.com/Imaginos16/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Saturday 2023-11-04 16:45:44 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [vvvv-vvvv/TerraGov-Marine-Corps](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps)@[2ebcdf013a...](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps/commit/2ebcdf013ae923188c5607d4f692738cf1a50913)
#### Saturday 2023-11-04 16:52:00 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.

IMPROVES my workflow

:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ca8d696326...](https://github.com/treckstar/yolo-octo-hipster/commit/ca8d696326e1c325330f1245a20c9844e739ae3d)
#### Saturday 2023-11-04 17:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Saturday 2023-11-04 18:28:52 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [DrxcoTheBulider/DrxcoTheBulider](https://github.com/DrxcoTheBulider/DrxcoTheBulider)@[5bdf6a5d9c...](https://github.com/DrxcoTheBulider/DrxcoTheBulider/commit/5bdf6a5d9c6db200ace4225d433c5737aef1fad9)
#### Saturday 2023-11-04 19:25:41 by DrxcoTheBulider

README.md

<h1 align="center">Discord Bot Client</h1>

**Discord Bot Client** allows you to use your bot, just like any other user account, except Friends and Groups. 

## Overview

- [How to install it](#installation)
  - [Using prebuilt binaries](#using-prebuilt-binaries)
  - [Building from source](#building-from-source)
- [Login](#login)
- [Features](#features)
- [Discord Version](#version)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Similar projects](#similar-projects)
- [Credits](#credits)

**WARNING: Third party clients are discouraged and against the Discord TOS.**

Discord Bot Client is a custom [Discord](https://discord.com/app) client that aims to
support bot accounts and be aimed at power-users.


The application only uses the official Discord API and doesn't send data to
third parties. However, this application is not an official product by
Discord Inc.

![Demo Screenshot](https://cdn.discordapp.com/attachments/820557032016969751/1128535575281029150/image.png)

---

## Installation

### Using prebuilt binaries

If you don't want to build the application yourself or use some kind of
package management system, you can get the latest binaries for the three
major systems in the release overview:

https://github.com/aiko-chan-ai/DiscordBotClient/releases/latest

### Building from source

In order to execute the following commands, you need to install **NodeJS v16 or**
higher. You can find nodejs packages at https://nodejs.org/en.
On top of that, you need to have **git** installed. It can be fund at
https://git-scm.com/downloads.

**UPDATES HAVE TO BE INSTALLED MANUALLY**

Open a command line and execute the following commands:

```shell
git clone https://github.com/aiko-chan-ai/DiscordBotClient.git
cd DiscordBotClient
npm install
npm run build
```

This will create an executable called `DiscordBotClient` or `DiscordBotClient.exe` in the `dist` folder depending on whether you are using Windows or not.

---

### Login

Logging in works via the UI on first startup of the application.

![screenshot](https://cdn.discordapp.com/attachments/820557032016969751/1128537663864045608/image.png)

> **Note**
> Enable `MessageContent` intent, other intents are optional

![image](https://cdn.discordapp.com/attachments/820557032016969751/1128538612175220906/image.png)

---

## Features

- **View Guilds** *(Lazy load them)*
- **Manage Guilds** (Name, Image, Audit log, Emoji, Webhooks, Invites, Bans, Widget, Moderation, Roles)
- **Manage Channels** (Add, Delete, Name, Permissions, Invites, Webhooks, Slowmode, NSFW, Topic, Forums, Threads)
- **Messages** (Send, View History, Embeds, View Reactions, Add/Remove Reactions, Delete, Edit, Pin)
- **Create a Guild** (if the bot has fewer than 10 Servers)
- **Voice Support** (Text-in-Voice and watch the user using the camera)
- **Use Emojis from other servers** (Nitro)
- **GIF Search**
- **Send Files**
- **DM's** (DM's will show up, after a user dms the bot)

---

## Version

| Discord Build | Hash | Vencord | Discord Bot Client | Status |
| --- | --- | --- | --- | --- |
| Stable 161052 | c7e0778 | - | v1 | Deprecated |
| Stable 185832 | 29333f6 | v1.1.4 | v2.1 | Deprecated |
| Stable 204762 | 78f82ba | v1.2.8 | v2.2+ | Latest |

---

## Troubleshooting

If you happen to encounter a crash or a bug, please submit a bug report via
the projects GitHub issue tracker.

# FAQ

In order to find answers to common questions, check out the FAQ in the [wiki](aiko-chan-ai/DiscordBotClient#8):

## Similar projects

Here is a list of similar projects:

- [Discord Bot Client](https://github.com/SamuelScheit/discord-bot-client)
- [BotClient](https://github.com/DarkGuy10/BotClient)
- [ChrisEric1.GitHub.io](https://github.com/ChrisEric1/ChrisEric1.GitHub.io)
- [LiveBot](https://github.com/SebOuellette/LiveBot)
- [BetterDiscordPanel](https://github.com/SanjaySunil/BetterDiscordPanel)

Hit me up if you have a similar project, and I'll gladly add it to the list.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=aiko-chan-ai/DiscordBotClient&type=Date)](https://star-history.com/#aiko-chan-ai/DiscordBotClient&Date)

---

## How to update to the latest Discord version ?

- Step 1: Patch index.html (Get it from discord.com/channels/@me)

- Step 2: Patch script.js (search for keyword `_doIdentify` in the code)

- Step 3: Change like me (see location in template file, search by keyword `// Patch #{number}`)

## Credits

Big thanks to [ChrisEric](https://github.com/DrxcoTheBulider) for helping me create a local proxy server! (code)

This project was mainly inspired by [SamuelScheit](https://github.com/SamuelScheit)
[Discord Bot Client](https://github.com/DrxcoTheBulider), which he sadly didn't
develop any further.

---
## [firigi-buzz-online/firigi-buzz-online](https://github.com/firigi-buzz-online/firigi-buzz-online)@[704fb4be66...](https://github.com/firigi-buzz-online/firigi-buzz-online/commit/704fb4be660d1dbba84c81f38548ed7c53e91f7f)
#### Saturday 2023-11-04 19:33:23 by Live*Cordina vs Vazquez Live

Update README.md

I can be a champion again if I want, it depends on me, my mentality, my motivation, the people around me. Now I have the same feeling I had before when I was a champion. That’s why I’m back in the gym, why I’m back fighting again.

https://billing.zuzz.tv/aff/go/exclusive?i=5

“No matter how old I am, I don’t care about that, my life is very healthy all the time, I take care of myself, I eat clean, very healthy. My life is very nice, very clean all the time. I’m back. I do a better job than before, no matter I lose three times, I don’t care about that.

Linares: "October 21 I'm back in the UK. I'm full of emotion and ready to give everybody a spectacular performance against a tremendous opponent Jack Catterall. I just want everyone to know that I'm ready to give Jack a great boxing lesson and to continue making history in the UK. The last Samurai is back, stronger than ever."

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[0d5f9907a2...](https://github.com/nikothedude/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Saturday 2023-11-04 19:38:10 by Jacquerel

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
## [Kong/ngx_wasm_module](https://github.com/Kong/ngx_wasm_module)@[54f7d26166...](https://github.com/Kong/ngx_wasm_module/commit/54f7d26166452d4dc87a12460c648fbf4927ac22)
#### Saturday 2023-11-04 19:57:30 by Thibault Charbonnier

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
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[2a74c23d62...](https://github.com/BogCreature/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Saturday 2023-11-04 19:58:42 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [xDanilcusx/PvE-CMSS13](https://github.com/xDanilcusx/PvE-CMSS13)@[e7caf52c21...](https://github.com/xDanilcusx/PvE-CMSS13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Saturday 2023-11-04 19:58:43 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [xDanilcusx/PvE-CMSS13](https://github.com/xDanilcusx/PvE-CMSS13)@[e120ab795b...](https://github.com/xDanilcusx/PvE-CMSS13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Saturday 2023-11-04 19:58:43 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [atalii/site](https://github.com/atalii/site)@[01e9a08399...](https://github.com/atalii/site/commit/01e9a08399bd9c56dd9f57335c00ba07ca946b9c)
#### Saturday 2023-11-04 20:06:27 by tali auster

srv: verify HTTP method

kinda silly kinda funny how we just let POSTs work as GETs and
all that.

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[d5d78fec30...](https://github.com/BurgerLUA/Bubberstation/commit/d5d78fec30aef1480c47a581eafc6a1b9edc8b13)
#### Saturday 2023-11-04 20:50:13 by SkyratBot

[MIRROR] Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN [MDB IGNORE] (#24149)

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN (#78674)

## About The Pull Request

The Regal Condor come with a magazine and ammo already inside.

The recipe for the magazine now no longer needs TC, but does need donk
pockets (sponsored murder gear, you see) and a hell of a lot more
materials per magazine (you're looking at like 40 sheets of various
materials all up). It also needs you to make the Condor first. But it
comes preloaded with ammo.

The Condor is 1 whole TC more expensive. Also needs some metal. The old
recipe is there in spirit.

The Regal Condor and the magazines come with 10mm Reaper bullets.
They're high damage. They're high AP. They are also hitscan.

## Why It's Good For The Game

Apparently people don't like the Condor. Too much effort for not enough
reward. After all, revolvers exist. 'It must be a joke' they say! 'It's
joke content! I went to all that effort to make it for nothing! That
slut Anne tricked us!'

**Wrong, bitch.**

If you want the Condor to make you shit yourself the moment someone with
it appears on the screen, then fine!

### **You get what you fucking deserve.**

## Changelog
:cl:
balance: Despite earlier reports suggesting that the famous lethality of
the Regal Condor was largely a myth, there has been rumors that the gun
has once again started to display its true killing potential on any
station that it 'manifests'.
/:cl:

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [SpaceCraft14/CosmiCraft](https://github.com/SpaceCraft14/CosmiCraft)@[9701cb457c...](https://github.com/SpaceCraft14/CosmiCraft/commit/9701cb457c307cb8cb252631855c2ef4ec810742)
#### Saturday 2023-11-04 21:03:23 by xenou04

Update Rules.txt

Greetings! Some exciting news – our server has added some fresh, juicy rules that are ripe for the picking! These new guidelines are like a sweet fruit that will nourish and protect the community like the skin of a mango that protects its tender flesh. They are the guiding light that will steer us through turbulent waters like the pole star that has guided sailors for centuries.

Our new rules are a fragrant bouquet of freshly picked wildflowers, imparting a sense of beauty and wonder to our community. They are a warm embrace, welcoming all who seek sanctuary in our safe and supportive environment, like a cozy blanket that wraps us in comfort.

We must all abide by these new rules, which are the backbone of our community, like the sturdy trunk that supports a towering oak. They are the glue that holds us together, like the sap that binds the bark to the tree.

So let's all savor these new rules like the juiciest peach, and cultivate the community that we all desire to be a part of, like a bountiful garden. Remember, our new rules are here to protect, guide, and nourish us like the sun that gives life to all living things. Let us look forward to an exciting future together!

---
## [Cocacolagua/Paradise](https://github.com/Cocacolagua/Paradise)@[dcd1f5d88a...](https://github.com/Cocacolagua/Paradise/commit/dcd1f5d88a8c5ba9634fc3fce67a76ada45f71dc)
#### Saturday 2023-11-04 21:40:39 by Octus

Adds eight vox hairstyles because why not and stuff (#22573)

* god i hate myself

* donedone

* fixxxxx

---
## [Cocacolagua/Paradise](https://github.com/Cocacolagua/Paradise)@[c3a78f9ce0...](https://github.com/Cocacolagua/Paradise/commit/c3a78f9ce0f30474636d1100d3d24310bbb3fe08)
#### Saturday 2023-11-04 21:40:39 by Octus

Removes Beach Bums, Adds Althland Excavation Pit (#22315)

* replace

* Update lavaland_biodome_beach.dmm

* fixes

* we are so BACK bros

* oh yeah, now were cookin

* turf

* oops!

* Update lavaland.dm

* work you fuck

* donedonedoneeeeeee

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[6623f9d36f...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/6623f9d36f1ee0b4539eb3abe827e60987712d36)
#### Saturday 2023-11-04 22:56:31 by Coxswain

Adds distorted form

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

---
## [petre-symfony/api-platform-3-part-3-custom-resources-](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-)@[1daeff1301...](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-/commit/1daeff13012c5fbc736d0b022212359331280312)
#### Saturday 2023-11-04 22:56:53 by Petre Ro

26.1 MicroMapper: Central DTO Mapping

 Doing the data transformation, from UserApi to the User entity, or the User entity to UserApi, is the only part of our provider and processor that isn't generic and reusable. Rats! If it wasn't for that code, we could create a DragonTreasureApi class and do this whole thing over again with, like almost no work! Fortunately, this is a well-known problem called "data mapping".

 For this tutorial, I tried a few data mapping libraries, most notably jane-php/automapper-bundle, which is super-fast, advanced, and fun to use. However, it isn't quite as flexible as I needed... and extending it looked complex. Honestly... I got stuck in a few places... though I know that work is being done to make this package even friendlier.

 The point is, we're not going to use that library. Instead, to handle the mapping, I created a small package of my own. It's easy to understand, and gives us full control... even if it's not quite as cool as jane's automapper.

 Installing micro-mapper

 - So let's get it installed! Run:

  composer require symfonycasts/micro-mapper

 That kind of sounds like a superhero. Now that we have this in our app, we have one new micromapper service that's good at converting data from one object to another. Let's start by using it in our processor.

---
## [SimiaCryptus/SkyeNet](https://github.com/SimiaCryptus/SkyeNet)@[40e3df719e...](https://github.com/SimiaCryptus/SkyeNet/commit/40e3df719e634af137e3a4d0fe49456ebeb93e67)
#### Saturday 2023-11-04 23:21:50 by Andrew Charneski

1.0.20 (#24)

* 1.0.20

* 1.0.20

* 1.0.20

* 1.0.20

* 1.0.20

* Fuck me life, and fuck yours too

* 1.0.20

---

