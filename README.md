## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-12](docs/good-messages/2023/2023-12-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,934,874 were push events containing 4,258,517 commit messages that amount to 318,787,699 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 78 messages:


## [dance-with-the-devil-on-cold-cell-block/thingy](https://github.com/dance-with-the-devil-on-cold-cell-block/thingy)@[06485b8768...](https://github.com/dance-with-the-devil-on-cold-cell-block/thingy/commit/06485b876808c68811f14cddfc7c147ee28ac940)
#### Tuesday 2023-12-12 00:13:55 by Friðrik Valur Bjartsson

Merge pull request #41 from dance-with-the-devil-on-cold-cell-block/react-funny

núna virkar register shittð

---
## [cyphar/runc](https://github.com/cyphar/runc)@[3776997545...](https://github.com/cyphar/runc/commit/3776997545334544b77dd0696b5f07405aab9976)
#### Tuesday 2023-12-12 00:14:37 by Aleksa Sarai

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
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[0a75aef49d...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Tuesday 2023-12-12 00:40:10 by The Bron Jame Offical

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
## [JohelEGP/cppfront](https://github.com/JohelEGP/cppfront)@[cdf71bdca6...](https://github.com/JohelEGP/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Tuesday 2023-12-12 00:45:10 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [OnionUI/Onion](https://github.com/OnionUI/Onion)@[c7694511f2...](https://github.com/OnionUI/Onion/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Tuesday 2023-12-12 00:46:38 by XK

FEAT: Update ScummVM Standalone to 2.9.0git (#1307)

## Overview
Update to scummvm 2.9.0 to include all updates & fixes to the scrollbars
in: https://github.com/scummvm/scummvm/pull/5472

<img
src="https://github.com/OnionUI/Onion/assets/47260768/89080ee6-124e-445a-a14d-b818e277e991"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is still
present

Downscaler can be tested by running BSword2.5. 
Audio has been handled differently so in this PR will also change the
launch scripts to preload libpadsp.so

## Build details
<details>

```markdown
Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard, ENet
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec
WARNING: Disabling engine The Watchmaker because the following dependencies are unmet: OpenGL (classic)

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chamber
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Crab
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Escape From Hell
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    The Immortal
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Might and Magic [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima [all games]
    V-Cruise
    Voyeur
    WAGE
    Wintermute [all games]
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge
    The Watchmaker

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Chamber
    Crab
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    The Immortal
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Might and Magic
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    Ultima [Ultima I - The First Age of Darkness]
    WAGE
    Wintermute [Wintermute3D]

Creating engines/engines.mk
Creating engines/detection_table.h
Creating engines/plugins_table.h
Creating config.h
Creating config.mk

```
</details>

---
## [NotADinosaur/Because-I-Can](https://github.com/NotADinosaur/Because-I-Can)@[eaf830c69e...](https://github.com/NotADinosaur/Because-I-Can/commit/eaf830c69eb3baec671b732b5762461053d33a76)
#### Tuesday 2023-12-12 01:05:29 by NotADinosaur

everything broke and idc anymore but fuck you I want rainbows lmao

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[1a2ddececa...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/1a2ddececa5cbc3b3aed161765eab4ebdda105c7)
#### Tuesday 2023-12-12 01:52:37 by SkyratBot

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
## [misterghast/BubberstationGhastified](https://github.com/misterghast/BubberstationGhastified)@[b5e095e380...](https://github.com/misterghast/BubberstationGhastified/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Tuesday 2023-12-12 02:12:28 by Waterpig

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
## [hark130/jack-in-the-box](https://github.com/hark130/jack-in-the-box)@[1b38958627...](https://github.com/hark130/jack-in-the-box/commit/1b38958627ef9b169892ed5f6e1341257ee47ed2)
#### Tuesday 2023-12-12 02:17:00 by hark130

JITB-1: Starting final(?) JitbAi polish

- Made Pylint happy
- Commented out most DEBUGGING
- Started manual testing Looks like 2-of-11 failures
NOTE: Untested as of yet

import time
from jitb.jitb_openai import JitbAi
test = JitbAi()

test_cases = ['After the first seven, what are the next three deadly sins?', 'Three ways to take your next book club meeting up a notch', 'Three things that are considered bad etiquette at the gym', 'Three words you don’t want to hear someone use to describe your genitals', 'When going through airport security, make sure to remove your _______, _______, and _______', 'Three Chevy car models recalled for being “too awesome”', 'The three things you need to be good at to truly get ahead in life', 'Bad news: they now take away your “cool card” if you like _______, _______, or _______', 'You know you’re about to have a bad day on Twitter if you see these three hashtags', 'Three things Mars needs before we can live there', 'Three theme parks more dangerous than Jurassic Park']

test.generate_thriplash(prompt=test_cases[0])

for test_case in test_cases:
    time.sleep(20)
    test.generate_thriplash(prompt=test_case)

['Snoring', 'Procrastination', 'Overindulgence']
['Booze and books!', 'Add a theme.', 'Bring snacks.']
['Grunting loudly', 'Not wiping sweat', 'Hogging equipment']
OpenAI generated more than just three lines here ['1. Small, shriveled, sad', '2. Moldy, crusty, stinky', '3. Flaccid, limp, lifeless', '4. Withered, wrinkly, dry', '5. Tiny, puny']
['Flaccid, limp, lifeless', 'Withered, wrinkly, dry', 'Tiny, puny']
['shoes', 'belt', 'liquids']
['Camaro', 'Corvette', 'Impala']
OpenAI generated more than just three lines here ['1. Lying, cheating, stealing', '2. Kissing, ass, networking', '3. Hustling, grinding, scheming', '4. Multitasking, bullshitting, bribing', '5. Manipulating, schmoo']
['Hustling, grinding, scheming', 'Multitasking, bullshitting, br', 'Manipulating, schmoo']
['- Nickelback', '- Crocs', '- Pineapple on pizza']
['#CancelCulture', '#TwitterFingers', '#TwitterMeltdown']
['Oxygen', 'Water', 'WiFi']
['Clown Carnage Land', 'Zombie Apocalypse World', 'T-Rex Terror Town']

Changes to be committed:
	modified:   jitb/jitb_openai.py

Untracked files:
	actual_integration.txt

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[0923ef2b26...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/0923ef2b264d7ee02b47c145249e90a69a49b554)
#### Tuesday 2023-12-12 02:19:55 by SkyratBot

[MIRROR] Basic Pirate NPCs [MDB IGNORE] (#24654)

* Basic Pirate NPCs (#79284)

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

* Basic Pirate NPCs

* Modular paths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [dyrone/git](https://github.com/dyrone/git)@[8f23432b38...](https://github.com/dyrone/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Tuesday 2023-12-12 02:50:50 by Johannes Schindelin

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
## [Alejodbort/Skyrat-tg](https://github.com/Alejodbort/Skyrat-tg)@[fc530572f6...](https://github.com/Alejodbort/Skyrat-tg/commit/fc530572f6bbe4db0a36df35251a2dd7e62c6b64)
#### Tuesday 2023-12-12 02:51:22 by SkyratBot

[MIRROR] Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors [MDB IGNORE] (#25493)

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

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

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [zhangjoke/crawl](https://github.com/zhangjoke/crawl)@[196b491b36...](https://github.com/zhangjoke/crawl/commit/196b491b3682a0ba7d1c76b2060a87d0b9f7594d)
#### Tuesday 2023-12-12 02:52:04 by regret-index

Step one of far too many for revising Chaos brand

Chaos brand is an absolute nightmare under the code, and also extremely
awkward as an actual design in practice. Players give the monsters with it
an extremely wide berth because of the banishment chance (which is actually
just 0.15%) and the very long buffs / debuffs list also attached, except
secretly the paralysis / slowing / petrifying effects were actually
invisibly casting a hex with power equal to the damage dealt. This was
actually pretty weak against the player's increasing AC and Willpower over
the course of the game, outside of mister super early Yiuf. (Meanwhile,
mushroom fist style AF_CONFUSE got a flat chance without a check, and also
chaos clouds made absolutely zero will / damage check to apply any of the
effects). In player hands, the weapon has a handful of miserable hits for
most of the game without ranged or summons- hasting or berserking a monster
is quite the betraying roll- and is also somewhat boring in the effects
it can actually get, regularly being rather common effects in the rest of
the game.

While there's been dev interest in revising this all for next version,
trying out more dramatic effects after they were culled out due to the
miscast streamlining, I'm doing some quick revisions now that make it
consistently somewhat dangerously yet while also reducing the most
dangerous individual effects from player or monster hands. This should
make it far less awkward to be desperately avoiding monster melee for a
sub-4% chance of an actually notable effect.

 * Chaos debuffs via the weapon brand and attack flavour both consistently
   ignore defender willpower now, with another flag added to beams. With
   how several different effects (confusion most notably) and clouds both
   didn't care about this, it's best to err towards the more dramatic for
   something we've been very cautious about spreading.

 * As compensation for the above and to have less hyper-rare rapid-death
   results, distortion has been taken off the regular weapon brands check
   (clearing off banishment) and paralysis is capped at exactly 1 turn
   (like Stunning Burst). On the player end of things, turning monsters
   into shapeshifters has been cut (poly does the same thing scaling
   better throughout the game), while monster berserk has now been
   replaced with Frenzied (keeping haste + 50% damage, losing HP buff,
   becoming neutral) like datura and Discord, which makes it more
   interesting as an upside and downside simultaneously.

 * Added as new effects to entice wielders and terrify victims are weak,
   corrosion, halved will, vitrifying, sleep, and ensnaring webs. Blink
   has also been isolated and preserved off of distortion. Agility's
   out barring a dramatic revision to it as a boring flat +5 EV.

 * Through some adjustments to the varied lists and another beam, both
   seething chaos clouds and Chain of Chaos has been updated to match the
   current non-brand effects list again.

Since we're not using most chaos monsters outside of the Abyss, there's not
too much concern to mildly nerf a few of them- they'll be far more
consistent in applying effects, anyway. Chaos spawn counts in a few earlier
vaults have been lowered or tiered higher, too.  It's probably worth
keeping an eye on Chaos Knight starting weapons, but most people actually
trying to win currently unwield those very fast, and this could do with a
fair bit of testing first. Probably should keep an eye on Malign Gateway
too.

TODO: make a chaos.cc that can handle these behaviours so that Chain of
Chaos doesn't desynch regularly, and so that clouds aren't faking a melee
hit of the person inside hitting themselves for zero damage to enchant
themselves with the chaos effects list. Also there's probably still more
effects to screw around with, too, like Devastator-style explosions,
random summons, brilliance, or cancellation. This is a relatively less
disruptive update for now, mostly aimed at making these all behave far
more parseably and more usably.

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[03514ec5d3...](https://github.com/i3roly/glibc_ddwrt/commit/03514ec5d39c4e467bb25ae56f1ba2fa81ba4e8f)
#### Tuesday 2023-12-12 02:52:29 by gagan sidhu

[4.14.332/54491] update in general

- i tried to migrate hanwckf's recent commits for that piece of SHIT arm
  platform mt7981 to the mt_wifi mt7615 version. let me know if
  everything is working as intended
- update smartdns
- update vim in the lootbag
- i dunno, assfuck goes crazy with his spinkicks sometimes. openvpn?
  eop-tunnel by egc etc bla bla bla

  fucking assfuck

---
## [pw32x/ninjagirl](https://github.com/pw32x/ninjagirl)@[c899abddd5...](https://github.com/pw32x/ninjagirl/commit/c899abddd5de8f45b4867ec9f197d34bc8ab858a)
#### Tuesday 2023-12-12 03:05:25 by pw_32x

Archiving SpriteMaster C#

Building a new converter from scratch in C# that includes a WPF interface requires too much effort for the amount I want to give it. I'll give some love to gg2c instead.
Plus, having a .sm file for each .gal was going to be a pain in the ass to synchronize and validate. It wasn't workable or friendly to work with. Storing the data inside the .gal is best.

---
## [mouseandthebillionaire/_lestTenHorizonsCry](https://github.com/mouseandthebillionaire/_lestTenHorizonsCry)@[5cf0d87bb0...](https://github.com/mouseandthebillionaire/_lestTenHorizonsCry/commit/5cf0d87bb09c54a9a259852d8b48e20bf00e343a)
#### Tuesday 2023-12-12 03:07:38 by mouseandthebillionaire

feat: initial physical build

The week was spent hooking up the dials and building a physical interface prototype in cardboard. While building this, a lot of small (and less small?) changes were made along the way to streamline and better organize the code. Many of these changes are lost to time, but the big take-away is this: only now can the real fine-tuning of the design begin. And "fine-tuning" is a bit of a soft way of saying that the cracks definitely show here, and thus begins the fun work of making this thing sing.

Next (and thoughts):
- there has to be some sort of visual feedback for the discovery synth portions (at least during this phase) They could probably be removed later, but even for me it's too hard to see (hear) when we are close to the desired locations
- this visual feedback opens up a lot of fun possibilities (explore these in an ideation session at some point) Right now there's just a little circle that moves along X/Y coordinates, fades, and generally looks kinda bad! An intensive survey of other interface-only games (In Other Waters and Mu Cartographer spring up immediately) is probably warranted
- using the hardware also opens up some issues there, namely a) layout, but more importantly b) is 8 dials too any dials? My thinking at this point is yes, but, as above, an ideation session will help to push on this
- the musical transitions are clunky and need a lot of work

---
## [kingk0ng9988/Girlsindxb](https://github.com/kingk0ng9988/Girlsindxb)@[40a1405359...](https://github.com/kingk0ng9988/Girlsindxb/commit/40a1405359e3dc23e1ad03f07ef1ed250a24783b)
#### Tuesday 2023-12-12 03:40:10 by Professional DXB call girls in dubai

Professional  DXB Call Girls  00971501558122 Call Girls in DXB

My name is Checky Sharjah (+971501558122), sophisticated lady with a friendly and loving attitude,
 the personality is gentle, straightforward, honest, also has a wild side and taste for being adventurous.
 I work independently , I love spending quality time with a gentleman and would love to share wonderful , 
lf you are looking for a place to relax and rest , enjoy , then I am the person you are looking for . 
I want our private time together to be on unforgettable experience.

Please let me know which service you like best , and I will accommodate that best , 
because I want you to be satisfied with what you need , and will be a real girlfriend to you and what is most natural , 
I’m not girl in a hurry to get work done on time and you have the best time being with me. (Shisha)

Last but not least my top priority is your pleasure , sex is not just damn it , it’s more than this . 
So i have very special expertises in relaxing massage and Nuru Massage
I will give you such a pleasure that you have never experienced before
Real Pictures Profile.

---
## [fejese/gradle](https://github.com/fejese/gradle)@[2805c3fda2...](https://github.com/fejese/gradle/commit/2805c3fda24da90bb9544ec197335259d983b2cd)
#### Tuesday 2023-12-12 04:39:44 by bot-gradle

Merge pull request #26874 Improve performance of RelativePath canonicalization

This is a follow-up to https://github.com/gradle/gradle/pull/24943.

There was some uncertainty as to whether that change resulted in a detectable drop in performance in Gradle's overall performance tests. I put together [some benchmarks](https://github.com/AlexLandau/gradle-relative-path-perf) looking at the constructor method that was modified, and based on my probably-non-representative sample of test cases, the new implementation took around 3.4x as long as the one that did not perform canonicalization.

The version in this PR skips running canonicalization checks on segments that come from existing `RelativePath` objects, which have already been canonicalized. This implementation actually performs better than the original, pre-canonicalization implementation in my benchmark test; I would take this with a grain of salt, as I do not have experience with JMH and may have used a poor setup or poor choice of test cases. (There's at least some evidence that for the range of test cases attempted, copying into the array with a for loop is faster than `System.arraycopy`, which would explain this. This could, of course, vary across JVM versions and other factors.)

### Contributor Checklist
- [x] [Review Contribution Guidelines](https://github.com/gradle/gradle/blob/master/CONTRIBUTING.md)
- [x] Make sure that all commits are [signed off](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) to indicate that you agree to the terms of [Developer Certificate of Origin](https://developercertificate.org/).
- [x] Make sure all contributed code can be distributed under the terms of the [Apache License 2.0](https://github.com/gradle/gradle/blob/master/LICENSE), e.g. the code was written by yourself or the original code is licensed under [a license compatible to Apache License 2.0](https://apache.org/legal/resolved.html).
- [x] Check ["Allow edit from maintainers" option](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) in pull request so that additional changes can be pushed by Gradle team
- [ ] Provide integration tests (under `<subproject>/src/integTest`) to verify changes from a user perspective
- [ ] Provide unit tests (under `<subproject>/src/test`) to verify logic
- [ ] Update User Guide, DSL Reference, and Javadoc for public-facing changes
- [x] Ensure that tests pass sanity check: `./gradlew sanityCheck`
- [x] Ensure that tests pass locally: `./gradlew <changed-subproject>:quickTest`

### Reviewing cheatsheet

Before merging the PR, comments starting with
- ❌ ❓**must** be fixed
- 🤔 💅 **should** be fixed
- 💭 **may** be fixed
- 🎉 celebrate happy things

Co-authored-by: Alex Landau <alandau@cs.stanford.edu>

---
## [H2-Technologies/Event-QSO-Logger](https://github.com/H2-Technologies/Event-QSO-Logger)@[9f8629da49...](https://github.com/H2-Technologies/Event-QSO-Logger/commit/9f8629da498850e864725f57313e020d81082d35)
#### Tuesday 2023-12-12 04:50:42 by Austin Hadley

Fuck Your Code SAM

Signed-off-by: Austin Hadley <admin@austinh.dev>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b401c4c139...](https://github.com/treckstar/yolo-octo-hipster/commit/b401c4c13962066f790a85efa2749e1d04632ee4)
#### Tuesday 2023-12-12 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[bf869a0ded...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Tuesday 2023-12-12 06:00:18 by Bloop

[MISSED MIRROR] Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#25185)

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

Co-authored-by: san7890 <the@san7890.com>

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[c797954427...](https://github.com/kleinerm/Psychtoolbox-3/commit/c797954427d133cbe0374f996c14327653a9b37d)
#### Tuesday 2023-12-12 06:29:23 by kleinerm

Merge pull request #823 from Psychtoolbox-3/master

Pull for Psychtoolbox 3.0.19.6 "Raspberry cake" release.

### Compatibility changes wrt. Psychtoolbox 3.0.19.5:

- Psychtoolbox is now tested and supported on Matlab R2023b, instead of R2022b.
  It is expected to continue to work on older releases than R2023b, but no longer
  developed or tested against them.

- Slight behavioral changes in IOPort BreakBehaviour settings on MS-Windows, and
  generally a few IOPort config options. Not expected to affect (m)any user scripts.


### Highlights:

- This release was tested for compatibility with Matlab R2023b on Linux and Windows,
  specifically Ubuntu 22.04.3-LTS with AMD RavenRidge (AMD Ryzen 5 2400G processor
  integrated graphics) and AMD Polaris graphics, and on Microsoft Windows 10 22H2
  with AMD RavenRidge and NVidia GeForce GTX 1650 graphics, and to a lesser degree
  on Ubuntu 20.04.6-LTS and Windows 11 22H2 with Intel Kabylake (GT2) "UHD 620"
  integrated graphics. Testing with some onboard sound chips was also performed.
  The testing led to various smaller improvements, and various workarounds on
  MS-Windows for AMD OpenGL and Vulkan graphics driver bugs, and for some NVidia
  driver bugs, as well as some bugs in Matlab wrt. backwards compatibility and
  OS compatibility. Most improvements in this release are due to that.
  
  This was done as part of out Mathworks 2023/2024 contract for ensuring compatibility
  with recent Matlab releases, spending over 65 work hours. Due to not even remotely
  sufficient funding for this work, no significant testing beyond some very quick touch
  and go spot testing was performed for macOS.

- Substantial movie playback performance improvements in pixelFormat 11 for HDR
  and WCG movies when hardware video decoding is used on Linux and MS-Windows. A
  small fraction of this work was sponsored as part of the Mathworks contract.

- 10 bit deep color framebuffer and HDMI output for the RaspberryPi 4/400 by
  improvements to Psychtoolbox and to the Mesa 23.3.1 OpenGL graphics drivers
  for RaspberryPi's VideoCore 6+ gpu. Mostly paid for by Cambridge Research Systems.


### All:

- Screen: Optimize storage format for LUMINANCE16 textures for texture normalization.
  If a 16 bpc luminance texture is turned into an offscreen window, or drawn into,
  the needed normalization / conversion to RGBA format now converts into RGBA16
  format instead of RGBA32 float format. This retains full precision of the original
  image content, but at half the memory consumption.

- Screen: In DrawTexture(s), always filter planar textures via nearest neighbour
  sampling instead of any of the other filtering/sampling modes, as any sampling
  other than nearest neighbour will cause massive artifacts.

- Screen: Improve performance of HDR movie playback by more efficient use of hardware
  video decoding. Enable the GStreamer movie playback engine in HDR mode (aka pixelFormat 11)
  to accept and handle typical semi-planar YUV formats used for HDR movies when
  gpu hardware accelerated video decoding is in use. This allows GStreamer to avoid
  cpu expensive frame format conversions from semi-planar frames provided by the
  gpu hardware decoders to planar formats previously accepted by PTB's texture
  creation code, leading to way higher performance when such hardware decoders
  are used. Software decoding still works via the previous path, whenever that is
  wanted or needed. Software decoding can also be enforced by disabling of hardware
  decoding by passing in specialFlags1 flag +4 in ``Screen('OpenMovie', ...)``. One
  limitation of the disable is that hardware decoding will stay off for the remainder
  of the whole session, ie. until Octave/Matlab is quit, once the disable flag
  for hardware decoding has been given once in a session. This could be fixed by
  requiring GStreamer 1.20+ as minimum requirement, ie. Ubuntu 22.04 and later.

  Note that I've repurposed/redefined specialFlags1 flag +4 as hw accel disable,
  from previously "draw 2D flow vectors on content for debugging/visualisation".
  This is ok, as the feature was probably never used by anybody, and also because
  this feature is deprecated and unsupported in all supported GStreamer versions
  since quite a while.

  The following new formats are supported for efficient handling:

  - Y42B = YUV planar 4:2:2 with 8 bpc.
  - NV16 = YUV semi-planar 4:2:2 with 8 bpc, aka P208.

  - P0xx formats of YUV semi-planar 4:2:0 sampling with 8, 10, 12 and 16 bpc,
    ie. NV12, P010_10LE, P012, P016. These are the relevant ones for typical
    HDR-10 hardware decoding from H265/HEVC, AV1, and from VP9.

  So far this has been tested on MS-Windows 10 with NVidia GeForce GTX1650 and
  AMD Raven Ridge / Vega as part of a Ryzen 5 2400G processor. On NVidia it shows
  a 2x speedup in decoding speed, to allow playback of 4k HDR at 60 fps with stable
  framerate and none to minimal frame dropping. This typically uses NVCODEC on
  NVidia hardware or Direct3D11/DXVA decoding on NVidia, AMD and Intel gpus.

  Tests on Ubuntu 20.04.6-LTS + Intel Kabylake + GStreamer 1.16, and on two
  Ubuntu 22.04.3-LTS machines with GStreamer 1.20.3, once with AMD Polaris11
  and once with AMD Raven Ridge, also showed 2x performance improvements.
  This uses VAAPI for hardware accelerated video decoding on AMD and Intel,
  and maybe on NVidia, but NVidia is untested so far on Linux.

  Note that while AMD and NVidia worked well in my testing, more often than
  not, Intel Kabylake shit its bed, causing hangs or massive visual artifacts
  in decoded video, on both Ubuntu 20.04 and Windows 11. May or may not be
  general Intel bugs, or may just be a problem on my specific old Intel iGPU.

  Additional successful testing was performed by a user under Windows-10 with
  a NVidia GeForce RTX 3080 with H265 and AV1 4k HDR 60 fps content.

  As a general guideline, as of November 2023, these video codec formats
  are generally hardware accelerated on Linux and Windows with typical
  recent hardware from AMD, NVidia and Intel:

  - MPEG2, VC1, H264, VP8: YUV 4:2:0, 8 bpc.
  - H265, VP9: YUV 4:2:0, 10 bpc HDR.

  - Sometimes also MPEG4, and AV1, the latter only on latest gpu's from
    NVidia, AMD and Intel, specifically NVidia Ampere+ RTX3000+, or AMD RDNA2
    Navi 2nd gen, or Intel Xe+/Arc+ or macOS 14 on Apple M3+.

  For best cross-platform, cross-vendor compatibility and with older hardware,
  the safest choices for high performance playback are probably H264 and H265
  at the moment.

  None of this applies to Apple macOS, as macOS too primitive OpenGL implementation
  currently does not allow use of pixelFormat 11 playback.

- PlayMoviesDemo.m: Optimize further for fast playing movies.
  Suppress costly text drawing for any fps >= 30. Skip wait for flip complete for
  non-HDR playback. Ths way the demo also serves as a real-world performance test.

- `help GetChar`: Update wrt. OS+GUI+Matlab/Octave support, internationalization.

- `PerceptualVBLSyncTest[FlipInfo2]`: Add optimizations, especially for RaspberryPi.
  Avoid redundant stimulus draw in non-stereo mono-mode. Do clear the backbuffer
  after each flip, as that seems to give a substantial performance boost for the
  VideoCore gpu's - See speculation in code comments - probably related to it being
  a tiled renderer, or a split gpu + display engine design at least for VideoCore 6+
  of RaspberryPi 4 and later. I haven't checked the driver source for the more likely
  reason yet.
  
  Another thing that can really help sync tests on the Pi is Priority(1), because
  then gamemode daemon chooses a more aggressive cpu governor. This only matters at
  high display refresh rates though, e.g., on a RPi 400 with a 1920x1080 120 Hz
  display. At somewhat lower refresh rates, e.g., 60 Hz, it isn't needed.

- `IOPort`: Fix 'OpenSerialPort' bugs where default settings override user settings.
  
  As GitHub user @qx1147 found out during a code review, there is a flaw in
  the handling of serial port options, where default serial port options may
  override user provided configuration options, so the wrong settings are
  silently applied! This only happens if the user script provides different
  settings in ``IOPort('OpenSerialPort', ..., settings)``, ie. on initial port
  open. Calls to ``IOPort('ConfigureSerialPort', ..., settings)`` are not
  affected.

  Luckily (dumb luck!), only a few options were mishandled, and most of these
  are rarely changed by user scripts, specifically:
    
  ProcessingMode=Cooked would get ignored, and raw mode used instead. Rarely
  used on Linux/macOS and not supported on Windows anyways. Low impact.
    
  BreakBehaviour=Ignore would be used instead of Flush or Zero. Not a
  problem on Windows, as that is the only supported option. The fact that
  this went unnoticed on Linux/macOS suggests not much use of Flush or Zero
  by users scripts. No use by PTB itself. Low expected impact. Note that the
  implementation of 'Flush' on the Unixes is of questionable use, as Flush
  would not only flush read/write buffers, but also send a SIGINT, which may
  end in unexpected ways on Unix, as we don't handle SIGINT specifically.
  
  StopBits=2 would get ignored and the default of 1 stop bits would be used.
  Unclear how many devices want 2 stop bits, but I haven't ever seen one, so
  probably low expected impact.
  
  DataBits=16 would get ignored on MS-Windows only and replaced by 8 bits,
  whereas other settings are fine, and 16 bits is unsuported on Linux/macOS,
  so probably rarely if ever used. Low expected impact.
  
  FlowControl=None will be used instead of hardware or software flow control.
  This can be a real bummer with potential real impact, as some devices do
  support or recommend active flow control! In the case of PTB, the
  CedrusResponseBox() driver for Cedrus response box devices would have
  liked that setting.
  
  Audit of Psychtoolbox internal user of IOPort, and of the demos, only
  shows one bad case where things went sideways: CedrusResponseBox.m
  This driver requested hardware flow control, but silently got instead NO
  flow control! This is interesting, because during my testing I found
  communication with Cedrus boxes always rather unreliable, and now I have
  to wonder if this was because of the accidental lack of hardware flow
  control? I can't find out, as I lost access to Cedrus devices long ago.
  
  This whole parameter handling is somewhat fragile, and could do with an
  improved implementation, but due to the severe lack of financial funding
  for PTB, this is not an option in the foreseeable future. Not even code
  review or testing of 3rd party contributions, if there were any. Luckily
  this part of the driver is mostly static since years, so I guess we can
  drag our feet longer and sit it out.

  Another problem pointed out by @qx1147 is indeed that wrong options, e.g.,
  due to typos in users experiment scripts, would not lead to an error abort
  or warning, but would get silently ignored in many cases. Not great at all,
  but lack of funding will leave this problems also unsolved in the near- to
  midterm, possibly forever. Life sucks...
    
  See also PR #821 for discussion. Thanks to @qx1147 for catching this!

- psychrange(): Make fallback trigger robust against Matlab R2023b if
  statistics toolbox is not installed.

- help PsychDemos, MovieDemos: Some fixes so Matlabs help system can cope.

- Snd(): Minimal compatibility fix for older Matlab releases. E.g., R2018b
  may need this fix, as reported on the forum.

- FlipTimingWithRTBoxPhotoDiodeTest: Fix useXR flag.

- Cone fundamentals fitting tests: Fix plotting to be usable on different displays.
  Old plot positioning caused UI awkwardness on most monitors. Also fix use of
  savefig() function, which was broken due to incompatible changes in Matlab over
  the years as far as I understand.

- LosslessMovieWritingTest.m: Switch default codec for encoding.
  From long non-existent huffyuv to supported avenc_huffyuv. Update help texts.

- Delete ScreenTest.m the most useless test ever.

- ComputePhotopigmentBleaching(): Fix some bug in example. By David Brainard.

- Minor bug fixes, documentation updates and improvements.


### Linux:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- PsychHID: Work around latest Matlab R2023b internationalization bugs.
  
  Matlab R2023b, at least on Ubuntu 20.04-LTS and Ubuntu 22.04-LTS, has a
  new compatibility bug, where it provides its own deficient libX11 that
  defines a wrong path to the locale configuration directories. This causes
  failure of international keyboard handling, ie. calls to XSupportsLocale(),
  XSetLocaleModifiers() and XOpenIM() fail. As a consequence, only U.S.
  keyboard layouts get properly handled whenever our our PsychHID/keyboard
  queue based GetChar() implementation is in use, but not other keyboard
  layouts!
    
  It also triggers a warning each time KbQueueCreate() is called, regardless
  if in the context of GetChar/CharAvail/ListenChar, or just for keyboard
  queue operation.
    
  Try to detect and work around this Matlab bug, by detecting the failure
  and then setting the XLOCALEDIR environment variable to override Matlabs
  broken path to a path that is correct at least for Ubuntu 20.04/22.04 and
  for similar Debian(-based) systems. Also try to detect user interference,
  e.g., the user setting a unsuitable XLOCALEDIR, and give troubleshooting
  tips in that case as well.
    
  This fixes the problem with R2023b on at least Ubuntu 20.04 and 22.04.
  The problem could also have been present in R2023a already, but this was
  not ever tested by myself, and I am not aware of any bug reports against
  either R2023a or R2023b.

- Add support to XOrgConfCreator, XOrgConfSelector and PsychLinuxConfiguration
  to allow to enable 10 bpc / 30 bit deep color framebuffers and display over
  HDMI on suitable displays with the RaspberryPi 4 and 400, and likely also the
  RaspberryPi 5. This was only tested on the RaspberryPi 400 under RaspberryPi OS
  versions 11 "Buster" (legacy) and 12 "Bookworm" (most recent one) 32-Bit editions.
  Note that current Psychtoolbox from us currently only works on RaspberryPi OS 11,
  ie. what is now called the "legacy" edition, not yet on the "current" OS version 12.
  Psychtoolbox 3.0.18.12, shipping with OS version 12 will work of course, but it
  does not have this setup code. However, it would work with a manually created
  xorg.conf file.

  Note that 10 bit framebuffers do not work on current versions of RaspberryPi OS
  out of the box. You need to manually install Mesa version 23.3.1 stable or later,
  which has an ETA of sometimes at or after 13th December 2024. Until then, a build
  script can be found under. You can download it, make it executable, and run it to
  build and install a Mesa local build in /usr/local/ compatible with RaspberryPi 4
  and 400, possibly RaspberryPi 5. Use this hacked build and install script at your
  own risk, if it totally breaks your system you get to keep all parts:
  
  https://raw.githubusercontent.com/kleinerm/PiKISS/ForCRS10BitMesa/scripts/config/vulkan.sh

  My enablement work for OpenGL 10 bpc / color depth 30 bit / deep color framebuffer
  support for Mesa 23.3.1+ on the RaspberryPi 4+ was sponsored by a contract from
  Cambridge Research Systems Ltd. Thank you!

- Other smaller refinements to RaspberryPi support.


### Windows:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- For Vulkan on Windows, reenable fullscreen exclusive support on current AMD drivers
  for proper timing. now works again on AMD gpu's with the latest AMD display drivers,
  version 23.11.1 from November 2023, as tested successfully in both SDR mode and HDR-10
  mode on Windows 10 22H2 with AMD Raven Ridge iGPU of AMD Ryzen 5 2400G APU, aka DCN-1
  display engine and Vega 11 graphics. Hurray!

  Some earlier driver versions might work as well, but this is the only confirmed one
  by testing, so reenable fullscreen exclusive starting with the 23.11.1 release.

- `IOPort`: Fix wrong break condition handling. Ignore break conditions completely
  `(BreakBehaviour=Ignore)`, rather than treating them as errors without further
  handling them in a useful way. Do validate BreakBehaviour parameter to be the only
  currently supported setting. Contributed by GitHub user @qx1147.

- `PsychPortAudio`: Update libportaudio for MS-Windows with latest from upstream Git
  main development branch. This way we get my bug fixes to WASAPI audio capture/input
  timestamping. Testing on MS-Windows 10 and 11 still shows some fragility and oddity
  in audio input capture timestamping, e.g., for voice onset timestamping, or sound
  based timing measurements like KeyboardLatencyTest.m or AudioFeedbackLatencyTest.m.
  These tests may not be very trustworthy on MS-Windows with WASAPI sound backend.

- Screen: Rewrite CRS clut update function RenderClutBits++ as a workaround.
    
  Switch from using point rendering via glVertex2i() of the clut T-Lock update pattern
  to instead using glRasterPos2i + glDrawPixels().
    
  Why? Because the proprietary AMD OpenGL driver on Windows has bugs in
  glVertex2i positioning when rendering to the OpenGL system backbuffer. The
  most easy way to work around this atm. is to use glRasterPos2i + glDrawPixels()
  to avoid the glVertex2i AMD bugs. This has the added benefit that we now use
  this glRasterPos2i + glDrawPixels() combo consistently for all CRS T-Lock rendering,
  ie. FE1 stereo driving and DIO codes, and for identity pixel passthrough tests and
  gamma table tweaking in PsychGPUTestAndTweakGammaTables(). At least we only
  have to think about one potentially broken function (glRasterPos2i()) in the future,
  not two separate ones.
    
  This was found on AMD RavenRidge Vega11 under Windows 10 with AMD driver 23.11.1.
  No such problem happened with the same hardware on Linux during my testing.

- AdditiveBlendingForLinearSuperpositionTutorial.m: Fix clut overlay text, and cleanups.
  Apply same fix as for BitsPlusIdentityClutTest.m for AMD Windows OpenGL driver
  bugs, so text rendering via the Mono++ / M16 clut hardware overlay works.

- BitsPlusIdentityClutTest.m: Work around MS-Windows AMD OpenGL driver bug.
  AMD's current OpenGL driver version 23.11.1 from November 2023 for MS-Windows
  has a bug in that glTexImage2D() does not accept GL_BITMAP texture specs. This
  breaks non-anti-aliased text rendering mode in the drawtext plugin.
    
  Work around this by enabling anti-aliased rendering for the plugin via
  Screen('Preference', 'TextAntiAliasing', 1); However, we don't want anti-aliasing,
  as it potentially interferes with clut overlays on CRS and VPixx devices, so use
  Screen('Preference', 'TextAlphaBlending', 1); to apply Screen('Blendfunction')
  settings during text rendering, but don't actually use Screen('Blendfunction').
  Instead leave alpha-blending at defaults, which is alpha-blending disabled.
  This effectively brings back aliased text rendering which works with the clut
  overlays.

- Screen('ColorRange'): Add workaround for color clamping OpenGL driver bugs.
    
  Turns out the recent proprietary AMD OpenGL driver on MS-Windows has a broken
  color clamping query implementation, which does not report clamp state for
  GL_CLAMP_VERTEX_COLOR_ARB or GL_CLAMP_FRAGMENT_COLOR_ARB.
    
  As such, we get reported failure to change color clamping on Windows 10 + AMD,
  whereas the same code works fine on Windows 10 NVidia or Intel.
    
  Work around this by detecting the failure and auto-selecting our own internal
  GLSL shader based fallback path. This should fix it - at a performance penalty,
  as vertex color clamping can be handled by our fallback shader, fragment color
  clamping has proper default behaviour of clamping on for fixed point unorm
  framebuffers, and clamping off for floating point framebuffers. Only readback
  clamping needs to be controlled via glClampColorARB, but luckily readback
  clamping is supported by glClampColor() as well, in a backwards compatible way,
  so we should be good. Famous last words...
    
  Note that this bug is so far only present on AMD on Windows, so we can get
  away with only rebuilding Screen() for MS-Windows for the moment.
    
  Also note that because it is the query that is broken, not the setting, our response
  of selecting the fallback path may be not necessary. However, it is unlikely to hurt,
  and we can not know, so better safe than sorry.


### macOS:

- Psychtoolbox was built and lightly tested against Matlab R2023b and Octave 8.4
  from HomeBrew. It should likely continue to work on older versions of Octave 8.x,
  possibly 7.x or 6.x., although none of these was tested.

---
## [bzEq/rust](https://github.com/bzEq/rust)@[ee80c8d0a8...](https://github.com/bzEq/rust/commit/ee80c8d0a8bc63b69f68216c5d37f9ab837eedd0)
#### Tuesday 2023-12-12 06:50:39 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [Noah6544/Daily-Picture-Aligner](https://github.com/Noah6544/Daily-Picture-Aligner)@[149fdb2887...](https://github.com/Noah6544/Daily-Picture-Aligner/commit/149fdb2887705e3bf7de4d7ffda670cd8c0e6d3e)
#### Tuesday 2023-12-12 08:04:38 by Noah Buchanan

WHY IS IT 3AM I HAVE A TEST TOMMOROW MORNING

Sigh. stupid gif compression and my horrible internet. I've spent the last like 30 minutes just trying to upload a new updated gif and compressing it and then github messes up and I'm losing my mind. I hope my 2 hour nap cancels out the lost sleep. like how (3x)/3 cancels out to just = x. Or like how the antiderivative is just- oh it finished

---
## [AtanasBunchev/GameSalad](https://github.com/AtanasBunchev/GameSalad)@[c9d1b336a3...](https://github.com/AtanasBunchev/GameSalad/commit/c9d1b336a33f2c0a72d94e1f3800d9543fbbc02c)
#### Tuesday 2023-12-12 08:26:11 by Atanas Bunchev

Storing JWT in cookie

The single moment you try to do something the way you want it, like,
just putting a token in a cookie without installing Microsoft.AspNetCore.Identity
you're doomed to spend nearly 3 hours just to figure out how.

And after the 3 hours you end up doing a dirty hack of modifying the Request Headers.

See:
https://stackoverflow.com/questions/37398276/how-can-i-validate-a-jwt-passed-via-cookies

Rant:
ASP.NET Core indeed is worth the hate.
Just like last time i used it, I'm hoping to not have to use it again.

Post Script:
... I guess i should cut it some slack.
I did spent hours searching how to do that, but the final solution
doesn't look as bad as it could've looked.
At least whoever reads the code won't start hating me for it.

---
## [AtanasBunchev/GameSalad](https://github.com/AtanasBunchev/GameSalad)@[2eb6b89618...](https://github.com/AtanasBunchev/GameSalad/commit/2eb6b89618abf20f2c713358e32570d0da56e3e5)
#### Tuesday 2023-12-12 08:33:41 by Atanas Bunchev

Storing JWT in cookie

Using a middleware to process the cookie and transform it into the
correct header for the JWT-processing code to handle.

See:
https://stackoverflow.com/questions/37398276/how-can-i-validate-a-jwt-passed-via-cookies

Rant:
ASP.NET Core indeed is worth the hate.
Just like last time i used it, I'm hoping to not have to use it again.

The single moment you try to do something the way you want it, like,
just putting a token in a cookie without installing Microsoft.AspNetCore.Identity
you're doomed to spend nearly 3 hours just to figure out how.

And after the 3 hours you end up doing a dirty hack of modifying the Request Headers.

Post Script:
... I guess i should cut it some slack.
I did spent hours searching how to do that, but the final solution
doesn't look as bad as it could've looked.
At least whoever reads the code won't start hating me for it.

---
## [AMyriad/YogsFork](https://github.com/AMyriad/YogsFork)@[5c140d7624...](https://github.com/AMyriad/YogsFork/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Tuesday 2023-12-12 10:32:29 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [grafbase/grafbase](https://github.com/grafbase/grafbase)@[d84940b6f4...](https://github.com/grafbase/grafbase/commit/d84940b6f439b2171e69554420d852aad2865cae)
#### Tuesday 2023-12-12 10:42:26 by Benjamin Rabier

feat: Add extra fields support (requires, key fields) in the engine v2 (#1121)

The PR is again really big and likely not that readable... Sorry, again,
for that.

The goal of this PR is to add fields depending on the resolver
requirements (fields of `@key`) and the `@requires` of individual
fields. I'm only really testing the former for now, but they're treated
identically. It's tricky because the prepared `Operation` is shared
during execution and we're planning children on the fly (depending on
type conditions). So we're not modifying the `Operation` directly to
avoid a complex and/or poor locking mechanism. We also want to keep
`Operation` cacheable to bypass the parsing & binding steps later.

So to add extra fields, I'm keeping track of those in `plan.Attribution`
in an `extra_fields` and `extra_selection_sets` array, indexed by ids.
Initially, I tried without IDs, but we need this information at two
places:
- for the operation walkers: For each actual selection set within the
query, I'm tracking whether any extra fields need to be added. This
makes extra fields mostly transparent when building the GraphQL query
string for a subgraph.
- during deserialization of the upstream response: In `plan.expectation`
we construct the structure we expect from the upstream response and
build an appropriate `DeserializeSeed` implementation. This also needs
to be aware of extra fields. We wouldn't if GraphQL had no type
conditions, because we could generate the whole structure ahead of time
during planning. But for cases with complex type conditions where we
can't simplify it, we need to generate the expectations during
deserialization and thus need to merge extra selection sets.

The other tricky aspect of extra fields is that we need to ensure their
names won't collide with anything else in the upstream GraphQL response.
For resolvers that return static data without aliases (OpenAPI,
resolvers, etc.) it's just the field name, for GraphQL we need to find a
name during planning as the query string depends on it. So I ended up
with `_extra{short_hex(FieldId)}_{field_name}` as the base name. I
verify that it's not present in response keys. If it is, I'm adding an
integer suffix and looping over it until I find an available one.

To ensure that extra fields don't collide within the `Response` data
I've tweaked a bit the bit packing I do, and added better documentation
for it. I'm using a flag + `FieldId` to ensure its uniqueness. I've also
constrained all schema IDs to fit within 28 bits ensuring my current bit
packing (needs 2 bits) works and leaving some margin in case. It's still
268 million possible values, so good enough.

---
## [Sonic-Geared/Scarlet-Engine](https://github.com/Sonic-Geared/Scarlet-Engine)@[854434adb9...](https://github.com/Sonic-Geared/Scarlet-Engine/commit/854434adb9f43454fb79c50c6a68dcb112496872)
#### Tuesday 2023-12-12 10:47:31 by Geared

what the fuck M7!!

random bullshit, Scarlet/v4 can't live without it so yeah

---
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[85812d6df2...](https://github.com/RedSkulHYDRA/frameworks_base/commit/85812d6df2fac06364f3089c56d8a61db9972524)
#### Tuesday 2023-12-12 11:03:12 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [neondatabase/neon](https://github.com/neondatabase/neon)@[c7f1143e57...](https://github.com/neondatabase/neon/commit/c7f1143e570924eadd15053949647707ba042c5b)
#### Tuesday 2023-12-12 11:10:37 by Christian Schwarz

concurrency-limit low-priority initial logical size calculation [v2] (#6000)

Problem
-------

Before this PR, there was no concurrency limit on initial logical size
computations.

While logical size computations are lazy in theory, in practice
(production), they happen in a short timeframe after restart.

This means that on a PS with 20k tenants, we'd have up to 20k concurrent
initial logical size calculation requests.

This is self-inflicted needless overload.

This hasn't been a problem so far because the `.await` points on the
logical size calculation path never return `Pending`, hence we have a
natural concurrency limit of the number of executor threads.
But, as soon as we return `Pending` somewhere in the logical size
calculation path, other concurrent tasks get scheduled by tokio.
If these other tasks are also logical size calculations, they eventually
pound on the same bottleneck.

For example, in #5479, we want to switch the VirtualFile descriptor
cache to a `tokio::sync::RwLock`, which makes us return `Pending`, and
without measures like this patch, after PS restart, VirtualFile
descriptor cache thrashes heavily for 2 hours until all the logical size
calculations have been computed and the degree of concurrency /
concurrent VirtualFile operations is down to regular levels.
See the *Experiment* section below for details.

<!-- Experiments (see below) show that plain #5479 causes heavy
thrashing of the VirtualFile descriptor cache.
The high degree of concurrency is too much for 
In the case of #5479 the VirtualFile descriptor cache size starts
thrashing heavily.


-->

Background
----------

Before this PR, initial logical size calculation was spawned lazily on
first call to `Timeline::get_current_logical_size()`.

In practice (prod), the lazy calculation is triggered by
`WalReceiverConnectionHandler` if the timeline is active according to
storage broker, or by the first iteration of consumption metrics worker
after restart (`MetricsCollection`).

The spawns by walreceiver are high-priority because logical size is
needed by Safekeepers (via walreceiver `PageserverFeedback`) to enforce
the project logical size limit.
The spawns by metrics collection are not on the user-critical path and
hence low-priority. [^consumption_metrics_slo]

[^consumption_metrics_slo]: We can't delay metrics collection
indefintely because there are TBD internal SLOs tied to metrics
collection happening in a timeline manner
(https://github.com/neondatabase/cloud/issues/7408). But let's ignore
that in this issue.

The ratio of walreceiver-initiated spawns vs
consumption-metrics-initiated spawns can be reconstructed from logs
(`spawning logical size computation from context of task kind {:?}"`).
PR #5995 and #6018 adds metrics for this.

First investigation of the ratio lead to the discovery that walreceiver
spawns 75% of init logical size computations.
That's because of two bugs:
- In Safekeepers: https://github.com/neondatabase/neon/issues/5993
- In interaction between Pageservers and Safekeepers:
https://github.com/neondatabase/neon/issues/5962

The safekeeper bug is likely primarily responsible but we don't have the
data yet. The metrics will hopefully provide some insights.

When assessing production-readiness of this PR, please assume that
neither of these bugs are fixed yet.


Changes In This PR
------------------

With this PR, initial logical size calculation is reworked as follows:

First, all initial logical size calculation task_mgr tasks are started
early, as part of timeline activation, and run a retry loop with long
back-off until success. This removes the lazy computation; it was
needless complexity because in practice, we compute all logical sizes
anyways, because consumption metrics collects it.

Second, within the initial logical size calculation task, each attempt
queues behind the background loop concurrency limiter semaphore. This
fixes the performance issue that we pointed out in the "Problem" section
earlier.

Third, there is a twist to queuing behind the background loop
concurrency limiter semaphore. Logical size is needed by Safekeepers
(via walreceiver `PageserverFeedback`) to enforce the project logical
size limit. However, we currently do open walreceiver connections even
before we have an exact logical size. That's bad, and I'll build on top
of this PR to fix that
(https://github.com/neondatabase/neon/issues/5963). But, for the
purposes of this PR, we don't want to introduce a regression, i.e., we
don't want to provide an exact value later than before this PR. The
solution is to introduce a priority-boosting mechanism
(`GetLogicalSizePriority`), allowing callers of
`Timeline::get_current_logical_size` to specify how urgently they need
an exact value. The effect of specifying high urgency is that the
initial logical size calculation task for the timeline will skip the
concurrency limiting semaphore. This should yield effectively the same
behavior as we had before this PR with lazy spawning.

Last, the priority-boosting mechanism obsoletes the `init_order`'s grace
period for initial logical size calculations. It's a separate commit to
reduce the churn during review. We can drop that commit if people think
it's too much churn, and commit it later once we know this PR here
worked as intended.

Experiment With #5479 
---------------------

I validated this PR combined with #5479 to assess whether we're making
forward progress towards asyncification.

The setup is an `i3en.3xlarge` instance with 20k tenants, each with one
timeline that has 9 layers.
All tenants are inactive, i.e., not known to SKs nor storage broker.
This means all initial logical size calculations are spawned by
consumption metrics `MetricsCollection` task kind.
The consumption metrics worker starts requesting logical sizes at low
priority immediately after restart. This is achieved by deleting the
consumption metrics cache file on disk before starting
PS.[^consumption_metrics_cache_file]

[^consumption_metrics_cache_file] Consumption metrics worker persists
its interval across restarts to achieve persistent reporting intervals
across PS restarts; delete the state file on disk to get predictable
(and I believe worst-case in terms of concurrency during PS restart)
behavior.

Before this patch, all of these timelines would all do their initial
logical size calculation in parallel, leading to extreme thrashing in
page cache and virtual file cache.

With this patch, the virtual file cache thrashing is reduced
significantly (from 80k `open`-system-calls/second to ~500
`open`-system-calls/second during loading).


### Critique

The obvious critique with above experiment is that there's no skipping
of the semaphore, i.e., the priority-boosting aspect of this PR is not
exercised.

If even just 1% of our 20k tenants in the setup were active in
SK/storage_broker, then 200 logical size calculations would skip the
limiting semaphore immediately after restart and run concurrently.

Further critique: given the two bugs wrt timeline inactive vs active
state that were mentioned in the Background section, we could have 75%
of our 20k tenants being (falsely) active on restart.

So... (next section)

This Doesn't Make Us Ready For Async VirtualFile
------------------------------------------------

This PR is a step towards asynchronous `VirtualFile`, aka, #5479 or even
#4744.

But it doesn't yet enable us to ship #5479.

The reason is that this PR doesn't limit the amount of high-priority
logical size computations.
If there are many high-priority logical size calculations requested,
we'll fall over like we did if #5479 is applied without this PR.
And currently, at very least due to the bugs mentioned in the Background
section, we run thousands of high-priority logical size calculations on
PS startup in prod.

So, at a minimum, we need to fix these bugs.

Then we can ship #5479 and #4744, and things will likely be fine under
normal operation.

But in high-traffic situations, overload problems will still be more
likely to happen, e.g., VirtualFile cache descriptor thrashing.
The solution candidates for that are orthogonal to this PR though:
* global concurrency limiting
* per-tenant rate limiting => #5899
* load shedding
* scaling bottleneck resources (fd cache size (neondatabase/cloud#8351),
page cache size(neondatabase/cloud#8351), spread load across more PSes,
etc)

Conclusion
----------

Even with the remarks from in the previous section, we should merge this
PR because:
1. it's an improvement over the status quo (esp. if the aforementioned
bugs wrt timeline active / inactive are fixed)
2. it prepares the way for
https://github.com/neondatabase/neon/pull/6010
3. it gets us close to shipping #5479 and #4744

---
## [Lutowski/Mothroach-tg](https://github.com/Lutowski/Mothroach-tg)@[6c823eef67...](https://github.com/Lutowski/Mothroach-tg/commit/6c823eef675d2b50696e239ea8098165aa052f2f)
#### Tuesday 2023-12-12 11:22:44 by Bloop

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
## [opensafely-core/ehrql](https://github.com/opensafely-core/ehrql)@[dc32e2f52c...](https://github.com/opensafely-core/ehrql/commit/dc32e2f52cc57bbfae785b1856e68ec90adae656)
#### Tuesday 2023-12-12 11:26:53 by David Evans

fix: Fix bug with `is_in(series)` and `maximum_of`

There was an unfortunate interaction in the SQLAlchemy hacks used to
support these features which, for some reason, my local generative
testing didn't catch but the overnight tests did.

We'll hopefully discover cleaner ways of implementing these features at
some point further down the road.

---
## [Dinastino/Prog_estructurada](https://github.com/Dinastino/Prog_estructurada)@[6b0c8e5c7b...](https://github.com/Dinastino/Prog_estructurada/commit/6b0c8e5c7b9b0bfbcd95764a022217959ed72249)
#### Tuesday 2023-12-12 11:30:09 by Carlos

ejercicio 3

Chad "Yeah Dude I've Got This Great Idea For A Company Let Me Tell You Bro It's Going To Revolutionize The Startup Industry When You Hear About How Much I Got On My Series A Financing You'll Want To Angel Invest In My Business Like Yesterday Bro Listen Up Why Don't You Come Over For Dinner Tonight And We Can Talk Shop No Wife And Kids Bro Just Us Dudes Hanging Out Having Brewskis While We Talk About How We're Going To Change The World Bro It's Gonna Be Sick Bro Hey Dude Have You Ever Gone To Breckinridge Bro Bro Let Me Tell You Bro That I Was Just There Shredding Powder And Bro Let Me Tell You That A Vodka And Red Bull While You Hit The Slopes Is Just The Sickest Bro I Mean You" broski

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[e7816d96c5...](https://github.com/cmss13-devs/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Tuesday 2023-12-12 11:34:05 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [phil2988/ComputerGameTechnologies](https://github.com/phil2988/ComputerGameTechnologies)@[7595c012ad...](https://github.com/phil2988/ComputerGameTechnologies/commit/7595c012ad1b75ab2dc0108b2ca4651ab76d9783)
#### Tuesday 2023-12-12 11:45:06 by AlexanderWodstrup

Merge pull request #9 from phil2988/feature/deleteLibaray

FUCK YOU LIBARY

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[2bbe4777fa...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/2bbe4777faff9a929f0a23f2c616812f732b4209)
#### Tuesday 2023-12-12 11:51:26 by George Spelvin

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
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: dotkit <ewprjkt@proton.me>

---
## [bwkam/dots](https://github.com/bwkam/dots)@[171912ce3d...](https://github.com/bwkam/dots/commit/171912ce3d40593c7f17f583d2f43315e836399f)
#### Tuesday 2023-12-12 12:02:54 by bwkam

ignore this stupid commit, just testing some silly shit

---
## [1005274291/react](https://github.com/1005274291/react)@[b6978bc38f...](https://github.com/1005274291/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2023-12-12 12:29:40 by Andrew Clark

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
## [chummer5a/chummer5a](https://github.com/chummer5a/chummer5a)@[78a2ad7341...](https://github.com/chummer5a/chummer5a/commit/78a2ad7341d0ecf482eaffe8f6bae34bbbe3b852)
#### Tuesday 2023-12-12 13:04:20 by Teksura

Adding Gun Bunny

I hate this file and everything about editing it. Critters are awful and I am only doing this because this file is so goddamn awful that nobody else is even willing to touch it.


This is my curse.

---
## [abhishekmaurya2028/CodeforcesSolutions](https://github.com/abhishekmaurya2028/CodeforcesSolutions)@[d027e276e4...](https://github.com/abhishekmaurya2028/CodeforcesSolutions/commit/d027e276e4e6c4439935221006dfb673880c2e68)
#### Tuesday 2023-12-12 13:12:20 by ABHISHEK KUMAR MAURYA

Update and rename hello.java to 4A watermelanProbelm.java

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[1e3807fa31...](https://github.com/semrush/intergalactic/commit/1e3807fa31e40226cba8c2957bbdc06aefe161db)
#### Tuesday 2023-12-12 13:19:53 by Michael Sereniti

[d3-chart] fixed chart legend table trimming with Ellipsis component (#962)

## Motivation and Context

Found that ellipsis doesn't work in the chart legend table grid.
I have found some wierd hacks
([1](https://css-tricks.com/preventing-a-grid-blowout/),
[2](https://stackoverflow.com/questions/36230944/prevent-flex-items-from-overflowing-a-container))
that make everything work like a charm.

## How has this been tested?

It almost impossible to test in our screenshot unit tests because
ellipsis needs a trimming rerender.

## Screenshots:

Before:

<img width="746" alt="Screen Shot 2023-12-12 at 14 15 42"
src="https://github.com/semrush/intergalactic/assets/31261408/6596acc7-7085-4742-9331-599b17f9d205">

After:

<img width="610" alt="Screen Shot 2023-12-12 at 14 14 12"
src="https://github.com/semrush/intergalactic/assets/31261408/4568e46c-b60c-4c18-b515-4aaa35344771">

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [x] Bug fix (non-breaking change which fixes an issue).
- [ ] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [ ] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---
## [dnblank123/oxipng](https://github.com/dnblank123/oxipng)@[1f2e0f336a...](https://github.com/dnblank123/oxipng/commit/1f2e0f336a826bd578a49c1dd477fb38773dd6ce)
#### Tuesday 2023-12-12 13:20:36 by Alejandro González

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[571b4c2515...](https://github.com/treckstar/yolo-octo-hipster/commit/571b4c2515a23d46e254336b7a39589d7321dfeb)
#### Tuesday 2023-12-12 13:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tusharsnx/terminal](https://github.com/tusharsnx/terminal)@[86fb9b4478...](https://github.com/tusharsnx/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Tuesday 2023-12-12 13:27:40 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [VonAudrey/app-dev](https://github.com/VonAudrey/app-dev)@[acf31399fa...](https://github.com/VonAudrey/app-dev/commit/acf31399fa730131cb48730ceb587bc568d1d7f9)
#### Tuesday 2023-12-12 13:30:40 by VonAudrey

Update README.md

#My Demon
A drama about a demon and a heiress who make a contract marriage and face big changes in their lives.

#Moon in the day
A leading South Korean celebrity is possessed by the spirit of a nobleman from ancient Korea and becomes his bodyguard.

#Night has come
A mystery teen drama that takes place when a class of second-year high school students is suddenly forced to play mafia games in real life during their retreat.

---
## [starrm4nn/tgstation](https://github.com/starrm4nn/tgstation)@[2631b0b8ef...](https://github.com/starrm4nn/tgstation/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Tuesday 2023-12-12 13:33:46 by Jeremiah

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
## [kartikshastri527/sadfasfddsafdsafasdf](https://github.com/kartikshastri527/sadfasfddsafdsafasdf)@[2645493b6a...](https://github.com/kartikshastri527/sadfasfddsafdsafasdf/commit/2645493b6a41cbd0758cdb823312f56a9b8fba14)
#### Tuesday 2023-12-12 13:37:52 by kartikshastri527

Create +91 7737454646 Lost love problem solution pandit

11-12-2023 saturday
④❶⑧❦❡
❣❦❷⑩❝➀❞❡➁❧♤ ⑩♤❞❢♤❣➂⑤❦❞ ❝⑥✐ ❞❢⑦❞❤♤❡
❝ ⑧❞❦❣⑨ ✐♥ ⑧❦❡⑨ ✐❡ ❝⑩♤ ✵④❶⑧❦❡ ❣
❦❷⑩❝➀❞❡➁❧♤ ⑩
♤❞❢♤❣➂⑤❦❞ ❝⑥
✐ ❞❢⑦❞❤♤
❡❝ ⑧❞❦❣⑨ ✐♥
⑧❦❡⑨ ✐❡ ❝⑩♤
✵④❶⑧❦❡ ❣
❦❷⑩❝➀❞❡➁❧

They make them feel comfortable like they were talking to their friend and they give the . Are you facing issues in your love marriage? love problem Astrologer, with vast experience. Best No1 Astro harisarana. Results Only 3 Hours. Your Ex Love Back. Love Marriage Specialist.+91-7737454646

**************************************************************************************************************************************************
Get My Love Back by Vashikaran
#5 Powerful Mantra To Get Your Love Back By Vashikaran in 24 Hours [ How To ]
Know How 10K+ Girls and Boys Are Reunited with Their Lovers in Just A Few Hours…+91-7737454646
*)*(**)**)*)**)**(*)*(*(*)*(*(*)*(**)*)*(*(*)**(*(*)*(*(*)*(*(*(**(*(*)*(*(*(*)*(*(*)*(*(*(*)*)*(*)*()*(*()*)*)(*(*()*)**(*(*()*)*)*(*(*)*)*(*(*)**(*(*)*(*(*)

Are you searching to get your love back by vashikaran mantra in 24 hours which can solve your love-related problems instantly? Are you thinking about how to get my ex back by vashikaran or get lost love back by vashikaran? Then you have come to the right place. Because I can show you miracles in just a few minutes by my vashikaran powers.

So what are you waiting for? Want to bring him or her back in #3 hours? Want to make your boyfriend or girlfriend dance on your fingers in #3 hours? So keep reading…

I am sharing the #5 powerful get ex back vashikaran mantra for educational purposes. If you follow step by step process and the right pronunciation of the mantra then No One will stop you to see results within #3 hours. Yes, within #3 hours you will be able to change your fortune in your favour.+91-7737454646


But: if you don’t have time to do mantra chant and remedy at home then ask me to do it for you. I’ll perform this remedy for you for FREE and show you guaranteed results in #3 hours.+91-7737454646


Get My Love Back By Vashikaran MantraGet My Love Back By Vashikaran Mantra

These mantras have the ability to help you get your ex-lover back and make them completely devoted to you. The get my love back vashikaran mantra is a very ancient and sacred ritual that has been used by many people across the world.
Bring back ex vashikaran mantra are very simple and easy to recite, and it only requires a few minutes of your time each day. In order to use this mantra effectively, you need to have complete faith in its power and recite it with full sincerity. If you do this, then there is no doubt that the get ex back by vashikaran will work for you and help you get your ex-boyfriend or girlfriend within a few hours.+91-7737454646


Once After Following My Step By Step Vashikaran Mantra To Get Him,

You Will Get Some Good News From Your Lover In Few Minutes.+91-7737454646


Like He Might Try To Call You, Message You Or Approach You In Some Other Way. He Will Start Showing His Love And Affection For You.
I Believe These Sings Are Good Enough To Ensure That My Vashikaran Has Started Working For You.

Don’t Miss Out The Last Chance To Get FREE Solution Today !!!
Consult Me Right Away & Ask For Super Fast Solution.+91-7737454646

#WhatsApp-Me #Call-Me #No-Fees+91-7737454646



Here are some of the vashikaran testimonials: My clients say nicest things about me:+91-7737454646

Get Love Back By Vashikaran TestimonialsGet Love Back By Vashikaran Testimonials+91-7737454646


What Can I Do For You:
Being a true and genuine love vashikaran specialist, I do not work for money at all but I work for the betterment of the people. My Powerful Vashikaran Mantras are very effective and quick.

Using My Powerful Vashikaran Mantra:

I can make every impossible to possible.+91-7737454646

I can fulfill your every wish.+91-7737454646

I can bow down to someone at your feet.
I can make any girl or boy fall in love with you.+91-7737454646

I can make anyone madly in love with you.
Even through my powers, I can fulfill your every wish which no one has been able to do till date.
So why are you wasting your money and time in vain, when a Genuine Get Love back Specialist is giving you a FREE SOLUTION? Contact me immediately and see miracles in #3 Hours +91-7737454646


#WhatsApp-Me #Call-Me #No-Fees
My Vashikaran Never Hurt Anyone!!!
Why Do People Trust My Powers?
I have been practicing get ex-love back mantra for the last 34 years and I have brought happiness back to the homes of lakhs & crores of people and made their life in happiness.+91-7737454646


Every day 15 to 20 people contact me and their only question is: how to do get my love back by vashikaran? I only give them my already tested and proven Vashikaran Mantras, which start showing their effect as soon as they do in #3 hours only.

In the year 2022-23, my vashikaran mantra has already been tried on lakhs of people and believe me 97% of the people have seen the effect of my powers in just 3 hours. +91-7737454646


Yes, in just 3 hours!!+91-7737454646


They have vashikaran their desired person, boy or girl quickly. So are you ready to see results within 3 hours?

Consult Me Right Away & Ask For Super Fast Solution.+91-7737454646

#WhatsApp-Me #Call-Me #No-Fees


Relationships become very volatile these days and couples break up due to very small reasons. Sometimes it is simply a matter of incompatibility, while other times it may be due to outside influences such as any other girl or boy. However, regardless of the reasons for the breakup, it is often possible to get love back by vashikaran in one day.

What is Ex-Love Back Vashikaran?
Vashikaran is a type of Vedic astrological magic that can be used to control the emotions of another person. If you know how to properly use vashikaran, then it is possible to make your ex-lover miss you and want to be with you again. In addition, ex-love back vashikaran can also be used to protect your relationship from outside forces that may seek to break you up.+91-7737454646


If you are interested in learning how to use vashikaran mantra for love, then today I am here with some proven and tested get your love back vashikaran permanently mantra. With a little bit of effort and using my secret vashikaran, you should be able to get your loved one back.+91-7737454646


How To Get Lost Love Back By Vashikaran in 24 Hours?
If you are thinking about how to get your lost love back in 24 hours, then let me tell you that it’s not as difficult as it may seem. The vashikaran is one of the powerful and proven ways that is used to make your boyfriend or girlfriend love you back. If you know how to use vashikaran correctly, it can be extremely powerful for bringing an ex back into your life. Here are a few steps to take care of:

1. First, you need to find a good love back vashikaran specialist who can help you correctly. Make sure you do your research and find someone who is experienced and trustworthy in vashikaran.+91-7737454646


2. Once you’ve found a specialist for getting lost love back permanently, the next step is to create a strong connection with them. This connection will be necessary in order for the vashikaran to work properly. Spend some time meditating and visualizing yourself and your ex together again. Feel the love and happiness that you once shared with him or her.+91-7737454646


3. The next step is to start the process of doing vashikaran. This should be done during an auspicious time, such as early morning or night before sleep. Make sure you follow the instructions of your vashikaran specialist carefully so that the vashikaran spell to get ex back is done correctly.+91-7737454646


4. Finally, have patience and believe that the vashikaran will work. It may take some time for your ex-love to come back into your life, but if you have faith, it will happen eventually and for sure. Online astrological home remedies to get back the lost love of your boyfriend are good enough.+91-7737454646


How To Use Get Lost Love Back By Vashikaran Mantra?
Looking to get your lost love back by vashikaran? Here’re some proven ex-back vashikaran mantras that you can use to bring your ex-boyfriend, girlfriend or lover back. However, not all mantras are created equal. Some are more effective than others, and some may even be dangerous if used incorrectly.+91-7737454646


You may read: Hindu Mantra to get lost love back

So, which is the best vashikaran mantra to get lost love back?
According to my past experience, the vashikaran mantra has been used for centuries to help people reunite with their lost love even after the breakup. The get love back by vashikaran mantra works by invoking the blessings of Almighty, who is known as the destroyer of ignorance and ego. By chanting the vashikaran mantra with sincerity and purity of heart, you can open yourself up to Lord’s blessings and help to bring your lost love back into your life.+91-7737454646


You may contact: Love problem solution astrologer

What Are Various Get Ex-Back By Vashikaran Mantras?
If you are looking for a safe and effective way to get your lost love back, then here are some vashikaran mantra, that is definitely worth trying. Just remember to chant it with sincerity and purity of heart, and you should see results soon or sometimes within one day.

If you are looking for the best vashikaran mantra for love back permanently, then look no further than the #5 Powerful Vashikaran Mantras below. Each of these love back mantras has been proven to be effective in helping to reunite loved ones who have been separated. Simply recite the bring ex back mantra with sincerity and focus, and then wait for your loved one to return. +91-7737454646


Again: if you don’t have time to do mantra chant and remedy at home then ask me to do it for you. I’ll perform this remedy for you for FREE and show you guaranteed results in #3 hours.+91-7737454646


1. Krishna Mantra To Get Ex-Love Back
“Om Namo Bhagavate Vasudevaya, Hevya Mum Vashym Kuru Swaha ( Name of Ex )”

This ex-back mantra is used to invoke the blessings of Lord Krishna, who is the embodiment of love. Simply reciting this mantra 108 times will help to open your heart and mind, making it easier for you to attract back your lost love.+91-7737454646


WhatsApp-Me #Call-Me #FREE-SOLUTION

2. Hare Krishna Mantra To Bring Ex Back
“Om Hare Rama Hare Krishna, Ekmev Tawan Hare Rama”

This ex-back mantra is a powerful chant that can help to create a strong connection between you and your lost love. Chanting this mantra with feeling will help to open up channels of communication, making it easier for you to reconnect.+91-7737454646


WhatsApp-Me #Call-Me #FREE-SOLUTION

3. Ganesh Vashikaran To Bring Lost Lover Back
“Om Gum Ganapataye Namah”

This is a very popular mantra that is used for attracting good luck and positive energy. Chanting this mantra will help to increase the chances of your lost love returning back into your life.

WhatsApp-Me #Call-Me #FREE-SOLUTION

4. Lord Shiva Mantra For Ex Back
“Om Shreem Mahalakshmiyei Namah”

This powerful mantra is used for attracting wealth and abundance. When chanted with intention, it can help to bring back a lost love who was previously financially stable. Alternatively, you can also use one more: Shiva Mantra To Get Lost Love Back

5. Kleem Mantra To Get Your Love Back
“Om Hreem Kleem Glaum Gam Ganapataye Namah”

This is an extremely powerful vashikaran mantra that should only be used as a last resort. This mantra can forcefully attract back lost love, even if they are unwilling. Use this mantra with caution, as it can have some unintended consequences if not used correctly.+91-7737454646


WhatsApp-Me #Call-Me #FREE-SOLUTION

Procedure To Chant Love Back Vashikaran Mantra:
This vashikaran mantra has to be recited for 11 days straight without a break in order to be effective. You will need a photo of your loved one, some sindoor and a rosary. On the first day, sit in front of the photo and hold the rosary in your right hand. With your eyes closed, recite the mantra 108 times. Apply Sindoor on the photo and place it in front of you. Repeat this process for 11 days. The results will start to show within a few weeks.+91-7737454646


If you don’t have time to do mantra chant and remedy at home then ask me to do it for you. I’ll perform this remedy for you for FREE and show you guaranteed results in #3 hours.

FAQs:

Is it possible to get your love back?
Yes, it is possible to get your love back using vashikaran. If you are willing to bring ex back after a breakup, then vashikaran may be the right solution for you. Contact a vashikaran specialist to learn more about how vashikaran can help you win back the love of your life.+91-7737454646


Browse: getting lost love back
What is the best way to get your love back?
There is no surefire answer, but often the most effective approach is love back vashikaran mantras to improve your relationship. Often, simply speaking to your partner and communicating your thoughts and feelings with vashikaran can be the best way to get back on track.

Alternatively, taking some time for yourselves to work on improving your relationship may also be beneficial. If all else fails, seeking a professional to bring back the ex-vashikaran specialist’s help may be the best solution. You may try free home totkas tips to get lost love back. You may see help from get lost love back astrologer. +91-7737454646


How to get my love back through vashikaran?
There are many powerful ways in astrology to get back your lost love back through vashikaran. One of the most popular methods is to recite and do vashikaran mantra. This can be done with the help of a vashikaran specialist baba ji. The vashikaran mantra will be customized to suit your specific needs and situation.+91-7737454646


Another way to get back ex-love using vashikaran is to use a talisman (Taweez). A talisman is a magical object that is believed to have special powers. It can be used to attract ex-lovers even once after a breakup and fall in love with you again. You can either create your own talisman or purchase one from a vashikaran specialist.

You may learn: How to get lost love back by astrology

Another method for bringing your love back by vashikaran is to perform astrological rituals called puja. Puja is a religious ceremony that is used to attract positive energy and blessings. It can be performed by yourself with online astrological home remedies to get back the lost love of your boyfriend or with the help of a vashikaran specialist.+91-7737454646


How does Vashikarana help to get back lost love? Is it right to get lost love with force?
The use of vashikaran helps to get back lost love by influencing the mind of the person that you love. It is not right to get lost love with force as it will only lead to further problems in the relationship. +91-7737454646

Know: vashikaran really works

Can vashikaran solve love problems?
Yes, vashikaran can help to solve love problems. If you are facing a problem in your relationship, then consulting a vashikaran specialist baba Ji can help to identify the source of the problem and suggest remedies that can help to resolve it. My vashikaran totke to get lost love back are very effective.

About Author
Lost Love Back Vashikaran Expert
I am a Love Back Specialist who has helped hundreds of clients reconnect with their lost loves since 1998. I have a gift for understanding people and knowing exactly what it takes to bring two hearts together again. My vashikaran mantra, remedies and love spells are tailored specifically to each client, and I always find a way to get through to even the hardest cases.

If you’re struggling to let go of the past and move on with your life, I can help you get your love back. Contact me today to get a solution. You won’t regret it bet it. You can read Genuine Vashikaran Specialist Reviews of those who have ever taken my services and now living a happy and blissful life.


Love Marriage Specialist
Vashikaran really works
Astrology and Vashikaran Getting Lost Love Back
Mohini Vashikaran Mantra
Remedies For Love Marriage
Shiva Mantra To Marry Desired Person
Tratak vashikaran Hindi
Free Vashikaran Specialist
Katyayani Mantra To Attract The Man You Love
How To Convince Boyfriend For Marriage

Astrological Remedies For Delay in Love Marriage Best Astrologer in Jaipur Best Astrologer in Kanpur Best Vashikaran Specialist in Indore Boyfriend Vashikaran Mantra in Hindi can god bring back a lost love Expert of Vashikaran and Astrology Free Shiva Vashikaran Mantra To Get Lost Love Back Ganesh mantra to convince parents for love marriage Get Ex Boyfriend Back Get Ex Husband Back by Vashikaran Hanuman mantra to get lost love back how can i attract my husband through mantra How To Control Husband By Lal Kitab how to do katyayani puja for 21 days husband wife problem solution mantra increase love between husband wife by lal kitab kamdev mantra for sex Lal Kitab Mantra To Attract Boyfriend lal kitab remedies for happy married life lal kitab remedies for love back lal kitab remedies to get back lost love Lal Kitab Upay For Husband lord ganesha mantra for love problems Lord Shiva Mantra For Love lost love back expert astrologer love vashikaran mantra maa kali mantra for love marriage manthrigam specialist in Chennai manthrigam specialist in Coimbatore mantra to make someone love you Mohini Vashikaran Mantra For Boyfriend most learned Vashikaran expert in Indore Muslim Vashikaran Mantra To Get Lost Love Back pooja to get your love back Sabar Mantra for Husband Sabar Mantra For Wife sex vashikaran mantra Spell To Win Back Ex Lover totkas to get rid of extra marital affair of husband Upay For Getting Good Husband vashikaran mantra to get back wife Vashikaran Tantras and Mantras vasiyam manthiram vasiyam specialist in Chennai

---
## [btcjon/FDAS3](https://github.com/btcjon/FDAS3)@[b3a1ba11c6...](https://github.com/btcjon/FDAS3/commit/b3a1ba11c63fd7525d047d53beabb0d17414cfd6)
#### Tuesday 2023-12-12 13:39:54 by Jon Bennett

aider: Refactored data fetching and UI initialization to ensure that the UI components are updated after the data is fetched.

# Aider chat conversation:

USER: blank panel when loads in browser '(3-11-4) jonbennett@Jons-MacBook-Pro FDAS3 % python mai
n.py
Environment variables loaded.
MetaApi token and account id retrieved.
Fetching new data from the database...
Launching server at http://localhost:65246
Fetching new data from the database...
Fetching new data from the database...
' perhaps compare to how position_table file is doing it b/c it works, only difference now is we are getting data directly from API?

ASSISTANT: It seems like you are experiencing an issue where the panel is blank when it loads in the browser. This could be due to a variety of reasons, including but not limited to the data not being loaded properly, the UI components not being initialized correctly, or an error in the JavaScript that renders the panel.

Since you mentioned that `positions_table.py` works correctly and the main difference is that `main.py` is getting data directly from the API, we should ensure that the data fetching and UI initialization in `main.py` are done in a similar manner to `positions_table.py`.

To diagnose the issue, we can compare the initialization and data fetching parts of both files. However, without a specific error message or a more detailed description of the problem, it's difficult to provide an exact solution.

Here are some general steps you can take to troubleshoot the issue:

1. Check the browser's developer console for any error messages. This can give you clues about what might be going wrong.
2. Ensure that the data fetching from the API is successful and that the data is in the correct format before it's passed to the UI components.
3. Verify that all UI components are initialized correctly and that they are being added to the template.
4. Make sure that the server is serving the static assets correctly if they are needed for the UI.
5. Compare the working `positions_table.py` with `main.py` to see if there are any differences in how the Panel components are being used or initialized.

If you would like me to review the code and suggest specific changes, please provide more details about how the `positions_table.py` handles the data fetching and UI initialization compared to `main.py`, or point out specific sections of the code that you suspect might be causing the issue.

USER: yes, please compare and see if you find possible solution from the comparison

ASSISTANT: To compare `main.py` and `positions_table.py` and find a possible solution, I will look at the key differences in how they handle data fetching, UI initialization, and server setup. Let's start by examining the relevant sections of both files.

### main.py
- Data fetching is done asynchronously using `fetch_and_update_positions` which is an async function that fetches data from MetaApi.
- The UI components are initialized with empty DataFrames (`df1` and `df2`) and then populated later.
- The server is started using `pn.serve(template, static_dirs={'assets': './assets'})` in a separate thread.

### positions_table.py
- Data fetching is done from MongoDB using a synchronous call to `pd.DataFrame(list(collection.find()))`.
- The UI components are initialized with the fetched data directly.
- The server is started in the same way as `main.py`.

Based on the comparison, here are some potential issues and solutions:

1. **Asynchronous Data Fetching**: In `main.py`, the data fetching is asynchronous, which means the UI might be initialized before the data is available. Ensure that the UI components are updated after the data is fetched.

2. **Empty Initial DataFrames**: The UI components in `main.py` are initialized with empty DataFrames. If the data fetching takes time or fails, the UI will remain empty. Make sure that the data fetching is successful and that the UI components are updated with the new data.

3. **Thread Synchronization**: The data fetching and UI updates are happening in separate threads. Ensure that the UI components are updated in a thread-safe manner.

4. **Error Handling**: If there are any errors during data fetching or UI initialization, they should be caught and logged. This will help diagnose issues.

5. **Static Assets**: Verify that the static assets are being served correctly and that the paths to CSS and JavaScript files are correct.

6. **Server Setup**: Both files use `pn.serve` to start the server. Ensure that the server is configured correctly and that there are no issues with the port or host settings.

To further diagnose the issue, you can add print statements or logging in `main.py` to check the status of the data fetching and UI initialization. Additionally, you can check the browser's developer console for any JavaScript errors that might prevent the panel from rendering.

If you would like me to provide code modifications, please specify which part of the code you would like me to focus on, or if there are any specific errors you are encountering.

USER: yes. 1 and 2 seem most likely

ASSISTANT: Given that issues 1 and 2 seem most likely, let's address them:

1. **Asynchronous Data Fetching**: We need to ensure that the UI components are updated after the data is fetched. Since `fetch_and_update_positions` is an async function, we should call it and update the UI components within an async loop or after the event loop has started.

2. **Empty Initial DataFrames**: We should ensure that the UI components are populated with data as soon as it's available. If the initial data fetch takes time, we might want to show a loading indicator or a message to the user.

Let's start by modifying `main.py` to address these issues:

### main.py

First, we need to ensure that `fetch_and_update_positions` is called and awaited properly. We can do this by creating an async function that will run the event loop and call our async functions. We will also need to modify the `update_table` function to be async and call `fetch_and_update_positions` from there.

Here are the *SEARCH/REPLACE* blocks for the changes:

```python
<<<<<<< SEARCH
def update_table():
    while not stop_event.is_set():
        print("Fetching new data from the database...")
        # This section will be replaced with the code to fetch and update 'positions' data from MetaApi

        # Wait for a certain period of time or until the stop event is set
        stop_event.wait(60)
=======
async def update_table():
    while not stop_event.is_set():
        print("Fetching new data from the database...")
        await fetch_and_update_positions()

        # Wait for a certain period of time or until the stop event is set
        await asyncio.sleep(60)
>>>>>>> REPLACE
```

Next, we need to start the asyncio event loop and ensure that our async functions are called within it. We will modify the try block at the end of `main.py` to run the event loop:

```python
<<<<<<< SEARCH
try:
    # Start a new thread that runs the update_table function
    update_thread = threading.Thread(target=update_table)
    update_thread.start()

    # Keep the main thread running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the updates when Ctrl+C is pressed
    stop_event.set()
    # Join the threads to ensure they have stopped before exiting
    update_thread.join()
    serve_thread.join()
=======
try:
    # Run the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.create_task(update_table())
    loop.run_forever()
except KeyboardInterrupt:
    # Stop the updates when Ctrl+C is pressed
    stop_event.set()
    loop.stop()
    loop.close()
    serve_thread.join()
>>>>>>> REPLACE
```

Please note that running an asyncio event loop in this manner will block the main thread, so you won't need the `while True: time.sleep(1)` loop anymore. The `KeyboardInterrupt` will be used to stop the event loop and join the server thread.

These changes should ensure that the data fetching is awaited properly and that the UI components are updated after the data is fetched. Remember to test these changes thoroughly, as modifying asynchronous code can have complex effects on the application's behavior.

USER: Given that issues 1 and 2 seem most likely, let's address them:

1. **Asynchronous Data Fetching**: We need to ensure that the UI components are updated after the data is fetched. Since `fetch_and_update_positions` is an async function, we should call it and update the UI components within an async loop or after the event loop has started.

2. **Empty Initial DataFrames**: We should ensure that the UI components are populated with data as soon as it's available. If the initial data fetch takes time, we might want to show a loading indicator or a message to the user.

Let's start by modifying `main.py` to address these issues:

### main.py

First, we need to ensure that `fetch_and_update_positions` is called and awaited properly. We can do this by creating an async function that will run the event loop and call our async functions. We will also need to modify the `update_table` function to be async and call `fetch_and_update_positions` from there.

Here are the *SEARCH/REPLACE* blocks for the changes:

```python
<<<<<<< SEARCH

^^^ Bad/missing filename. Filename should be alone on the line before <<<<<<< SEARCH

ASSISTANT: Apologies for the oversight. Let's correct the *SEARCH/REPLACE* blocks with the proper filename included.

We will modify `main.py` to ensure that `fetch_and_update_positions` is called and awaited properly, and that the UI components are updated after the data is fetched.

Here are the *SEARCH/REPLACE* blocks for the changes:

main.py
```python
<<<<<<< SEARCH
def update_table():
    while not stop_event.is_set():
        print("Fetching new data from the database...")
        # This section will be replaced with the code to fetch and update 'positions' data from MetaApi

        # Wait for a certain period of time or until the stop event is set
        stop_event.wait(60)
=======
async def update_table():
    while not stop_event.is_set():
        print("Fetching new data from the database...")
        await fetch_and_update_positions()

        # Wait for a certain period of time or until the stop event is set
        await asyncio.sleep(60)
>>>>>>> REPLACE
```

Next, we need to start the asyncio event loop and ensure that our async functions are called within it. We will modify the try block at the end of `main.py` to run the event loop:

main.py
```python
<<<<<<< SEARCH
try:
    # Start a new thread that runs the update_table function
    update_thread = threading.Thread(target=update_table)
    update_thread.start()

    # Keep the main thread running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the updates when Ctrl+C is pressed
    stop_event.set()
    # Join the threads to ensure they have stopped before exiting
    update_thread.join()
    serve_thread.join()
=======
try:
    # Run the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.create_task(update_table())
    loop.run_forever()
except KeyboardInterrupt:
    # Stop the updates when Ctrl+C is pressed
    stop_event.set()
    loop.stop()
    loop.close()
    serve_thread.join()
>>>>>>> REPLACE
```

These changes should ensure that the data fetching is awaited properly and that the UI components are updated after the data is fetched. Remember to test these changes thoroughly, as modifying asynchronous code can have complex effects on the application's behavior.

---
## [justinelinatoc/App-Dev](https://github.com/justinelinatoc/App-Dev)@[dfd6c850a5...](https://github.com/justinelinatoc/App-Dev/commit/dfd6c850a5b993e977958c2fd0a1578dd606fc4c)
#### Tuesday 2023-12-12 13:51:11 by justinelinatoc

Update README.md

Ben 10 is my favourite cartoon character. Ben, while spending his vacation at his grandparent's house, finds a watch called Omnitrix. The watch permanently attaches to him and gives him superpowers. He, with the help of the watch, can turn to ten alien forms.
Vampire brothers, Stefan and Damon Salvatore, battle for the affection of selfless teenager, Elena Gilbert. Stefan is the good and kind-hearted brother that feeds on animal blood to keep from killing anybody, and Damon is the selfish and dangerous older brother that feeds on human blood carelessly.
Dragon Ball tells the tale of a young warrior by the name of Son Goku, a young peculiar boy with a tail who embarks on a quest to become stronger and learns of the Dragon Balls, when, once all 7 are gathered, grant any wish of choice.

---
## [FrncssM/App-Dev](https://github.com/FrncssM/App-Dev)@[a68f517120...](https://github.com/FrncssM/App-Dev/commit/a68f517120d74bbf2b977753525421cace81636b)
#### Tuesday 2023-12-12 13:55:36 by FrncssM

Update README.md

Avatar is the story of Jake Sully, a paraplegic marine, who replaces his brother on a secret mission to infiltrate the Na' vi, the colony of beings that sit on the planet of Pandora, where there is a precious ore, that sells at a ridiculous amount.
Starwars is a fictional universe where the galaxy is ruled by the tyrannical Galactic Empire, the story focuses on a group of freedom fighters known as the Rebel Alliance, who aim to destroy the Empire's newest weapon, the Death Star.
HarryPotter An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world. On his eleventh birthday, Harry Potter (Daniel Radcliffe) discovers that he is no ordinary boy.

---
## [eProsima/ros2_documentation](https://github.com/eProsima/ros2_documentation)@[1be681dc76...](https://github.com/eProsima/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Tuesday 2023-12-12 14:01:08 by Chris Lalancette

First pass at the Iron Irwini release notes. (#3395)

* First pass at the Iron Irwini release notes.

That is, add in the full changelog, and also greatly
expand the release notes themselves.

I should point out that the full changelog is necessarily
*not* complete; it only contains information on things that
have already been released.

The release note page is a cut-down version of the full
changelog that just has things that might be interesting
to end users.  What is currently in there was my opinion,
so this list may be expanded or reduced based on thoughts
from other people.

In both cases, we should be able to iteratively add new
items here as they are landed.

Signed-off-by: Chris Lalancette <clalancette@gmail.com>
Co-authored-by: G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl>

---
## [neenjaw/advent-of-code-2020](https://github.com/neenjaw/advent-of-code-2020)@[1c515bd435...](https://github.com/neenjaw/advent-of-code-2020/commit/1c515bd435d8bf188c11febcba9e525979dd9a62)
#### Tuesday 2023-12-12 14:05:15 by Tim Austin

Day 12

In the realm of algorithms, where puzzles reign supreme,
Dynamic Programming's craft, a maze of intricate scheme.
A tale of computation, where hope and despair collide,
Broken springs and broken dreams in algorithms do abide.

Like stars in cosmic dance, these problems unfold,
Each subproblem a universe waiting to be told.
But oh, the woes of recursion, the endless loops in time,
As broken springs echo broken dreams in rhythm and in rhyme.

The promise of optimization, efficiency's gleaming light,
Shattered against complexity, a formidable sight.
For as the universe expands, so do these problems grow,
Broken springs and shattered dreams, a symphony of woe.

In the labyrinth of memoization, memories may decay,
Akin to the heat death of the cosmos, they slowly fade away.
What once seemed so promising, a solution within grasp,
Now entwined with broken springs, an eternal, fruitless clasp.

Dynamic Programming, a paradoxical art,
A blend of hope and sorrow that tears the soul apart.
As the universe marches towards its cosmic end,
Broken springs and shattered dreams persist, refusing to bend.

Yet amidst these trials, a spark of hope remains,
For within the chaos, resilience often gains.
Dynamic Programming's woes, a testament to strife,
But through persistence, broken dreams may find new life.

---
## [JohnVeness/godot-website](https://github.com/JohnVeness/godot-website)@[5a7b398a1e...](https://github.com/JohnVeness/godot-website/commit/5a7b398a1edbb5756819ae44eca308654a6206b6)
#### Tuesday 2023-12-12 14:13:08 by QbieShay

Remove QbieShay/Ilaria Cislaghi from conduct and board (#744)

Being a part of the board and the conduct team has been a
really great experience and i'm glad i got to contribute
to godot with my time.

As my life goals changes, I no longer want to be involved
in these groups: I prefer to spend my time and energy in
making sparkles and swooshes.

Love y'all <3 I know you'll do great

---
## [justinelinatoc/App-Dev](https://github.com/justinelinatoc/App-Dev)@[47b47c9aa7...](https://github.com/justinelinatoc/App-Dev/commit/47b47c9aa70a6b8f4f4a6519958fdc8332ccef94)
#### Tuesday 2023-12-12 14:23:02 by justinelinatoc

Update README.md

Dragon Ball tells the tale of a young warrior by the name of Son Goku, a young peculiar boy with a tail who embarks on a quest to become stronger and learns of the Dragon Balls, when, once all 7 are gathered, grant any wish of choice.
Vampire brothers, Stefan and Damon Salvatore, battle for the affection of selfless teenager, Elena Gilbert. Stefan is the good and kind-hearted brother that feeds on animal blood to keep from killing anybody, and Damon is the selfish and dangerous older brother that feeds on human blood carelessly.
Ben-10Ben 10 is my favourite cartoon character. Ben, while spending his vacation at his grandparent's house, finds a watch called Omnitrix. The watch permanently attaches to him and gives him superpowers. He, with the help of the watch, can turn to ten alien forms.

---
## [justinelinatoc/App-Dev](https://github.com/justinelinatoc/App-Dev)@[6776225672...](https://github.com/justinelinatoc/App-Dev/commit/6776225672066f9074230f0ec31649c61b3cb14d)
#### Tuesday 2023-12-12 14:29:54 by justinelinatoc

Update README.md


Ben 10 is my favourite cartoon character. Ben, while spending his vacation at his grandparent's house, finds a watch called Omnitrix. The watch permanently attaches to him and gives him superpowers. He, with the help of the watch, can turn to ten alien forms.
Dragon Ball tells the tale of a young warrior by the name of Son Goku, a young peculiar boy with a tail who embarks on a quest to become stronger and learns of the Dragon Balls, when, once all 7 are gathered, grant any wish of choice.
Vampire brothers, Stefan and Damon Salvatore, battle for the affection of selfless teenager, Elena Gilbert. Stefan is the good and kind-hearted brother that feeds on animal blood to keep from killing anybody, and Damon is the selfish and dangerous older brother that feeds on human blood carelessly.

---
## [justinelinatoc/App-Dev](https://github.com/justinelinatoc/App-Dev)@[c904b82c3b...](https://github.com/justinelinatoc/App-Dev/commit/c904b82c3b29d772b44cbad9553bd0533aa53e24)
#### Tuesday 2023-12-12 14:36:54 by justinelinatoc

Update README.md


Dragon Ball tells the tale of a young warrior by the name of Son Goku, a young peculiar boy with a tail who embarks on a quest to become stronger and learns of the Dragon Balls, when, once all 7 are gathered, grant any wish of choice.
Ben 10 is my favourite cartoon character. Ben, while spending his vacation at his grandparent's house, finds a watch called Omnitrix. The watch permanently attaches to him and gives him superpowers. He, with the help of the watch, can turn to ten alien forms.
Vampire brothers, Stefan and Damon Salvatore, battle for the affection of selfless teenager, Elena Gilbert. Stefan is the good and kind-hearted brother that feeds on animal blood to keep from killing anybody, and Damon is the selfish and dangerous older brother that feeds on human blood carelessly.

---
## [Sonic-Geared/Scarlet-Engine](https://github.com/Sonic-Geared/Scarlet-Engine)@[93ee57d22e...](https://github.com/Sonic-Geared/Scarlet-Engine/commit/93ee57d22eb251ca466422f0545ec1e005228f57)
#### Tuesday 2023-12-12 14:47:38 by Geared

CMake can fuck itself, i don't care about it! [skip ci]

something really silly (or just pure stupid)

---
## [PurpleCIoud/cmss13](https://github.com/PurpleCIoud/cmss13)@[9dbf819e8a...](https://github.com/PurpleCIoud/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Tuesday 2023-12-12 14:48:24 by forest2001

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
## [SWE-B5/SpottingSmallPrints](https://github.com/SWE-B5/SpottingSmallPrints)@[3b18914e48...](https://github.com/SWE-B5/SpottingSmallPrints/commit/3b18914e488aa00c76f987e42b78ea0a4ca196bd)
#### Tuesday 2023-12-12 15:23:58 by Philogex

Merge branch 'bitmap' of https://github.com/SWE-B5/SpottingSmallPrints into Level3
i hate my life

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[a3aeaa85bc...](https://github.com/norbert-acedanski/supernatural-guide/commit/a3aeaa85bc0f77f8e7edc6d722eaf4a77cf2bc5d)
#### Tuesday 2023-12-12 16:46:07 by Norbert Acedanski

Add Vengeful spirit encounter.
Add Demon, Witch, Angel, Darkness appearances.
Add GOD disable method.
Update Ghost Kevin description.
S15E02

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[2903eceb53...](https://github.com/norbert-acedanski/supernatural-guide/commit/2903eceb539c6e26bd8515d445772e89d4ff2402)
#### Tuesday 2023-12-12 16:46:07 by Norbert Acedanski

Add Vengeful spirit, Demon encounter.
Add Angel appearance.
Add missing GOD clue.
S15E01

---
## [Buyrcsp2/tgstation](https://github.com/Buyrcsp2/tgstation)@[8d77b1be89...](https://github.com/Buyrcsp2/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Tuesday 2023-12-12 16:55:31 by necromanceranne

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
## [Buyrcsp2/tgstation](https://github.com/Buyrcsp2/tgstation)@[54ab1e3936...](https://github.com/Buyrcsp2/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Tuesday 2023-12-12 16:55:31 by Time-Green

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
## [Buyrcsp2/tgstation](https://github.com/Buyrcsp2/tgstation)@[16bdcf409c...](https://github.com/Buyrcsp2/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Tuesday 2023-12-12 16:55:31 by Rhials

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
## [getoutreach/gobox](https://github.com/getoutreach/gobox)@[75c0408eac...](https://github.com/getoutreach/gobox/commit/75c0408eac3688fb09f38c44b33e541821eddb55)
#### Tuesday 2023-12-12 18:59:19 by Richard Larocque

Drop support for Honeycomb trace propagation

Removes any Honeycomb-specific trace header handling.  We expect our
services to be using OpenTelemetry standard trace headers, not Honeycomb
ones.  We should no longer need to accept or emit the Honeycomb headers.

The driving force behind this change is that the hacks that held things
together until now has broken.  Some services have started to rely on
parent-based sampling, which means we all services need to support it.
However, when we "convert" a Honeycomb header into a W3c/OpenTelemetry
header, we hard-code the "sampled" flag to false.

In theory, we could keep the code to accept Honeycomb headers.  It
wouldn't do any harm.  However, with our new parent-based sampler,
traces that carry those headers would never be sampled.  It seems better
to be honest and explicitly drop support for these legacy headers.

If there are services out there that do still rely solely on
Honeycomb-style headers, this will break trace propagation.  We've been
supporting both kinds of headers for a really long time now, so I don't
expect this to happen.  If they do break, we should upgrade their
libraries.

---
## [Sadhorizon/Paradise](https://github.com/Sadhorizon/Paradise)@[6a109ade7f...](https://github.com/Sadhorizon/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Tuesday 2023-12-12 19:39:06 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [Skrishnreddy/Saikrishna.github.io](https://github.com/Skrishnreddy/Saikrishna.github.io)@[8cd13d7cf3...](https://github.com/Skrishnreddy/Saikrishna.github.io/commit/8cd13d7cf31e81b942d37ac146b2e7adc91a4847)
#### Tuesday 2023-12-12 19:42:13 by SAIKRISHNA G

Create Index.html

<!-- ... Previous HTML content ... -->

<section>
    <h2>About Me</h2>
    <p>
        As an experienced System Administrator with 1.7 years of hands-on expertise, I have built a strong foundation in managing and maintaining diverse systems and networks. My journey at Cisco System Pvt Ltd, Bangalore, has honed my skills in performing routine system upgrades, resolving technical challenges, and safeguarding the overall stability and security of the IT infrastructure.
    </p>
    <p>
        I am passionate about bringing analytical thinking and structured problem-solving techniques to the table. With a strong positive customer service attitude, ensuring client satisfaction is my top priority. As a self-starter and quick learner, I thrive in challenging, fast-paced environments. I excel in problem recreation, log and trace analysis, and debugging complex issues to recommend effective solutions.
    </p>
    <p>
        My expertise includes the installation and configuration of Cisco switches, network devices, IP cameras, as well as troubleshooting and configuring SSH, FTP, and NFS. I am well-versed in Linux Package management tools and capable of administering hybrid cloud environments with configuration of HA/DR. My proficiency extends to different types of installations and configurations on RedHat, CentOS, and Ubuntu, along with database knowledge in MYSQL.
    </p>
    <!-- You can continue to describe your experience, skills, and any other relevant details -->
</section>

<!-- ... Remaining HTML content ... -->

---
## [Spookat/Aurora.3](https://github.com/Spookat/Aurora.3)@[13eb8af093...](https://github.com/Spookat/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Tuesday 2023-12-12 20:20:18 by RustingWithYou

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
## [tekoh/nypsi](https://github.com/tekoh/nypsi)@[42d79f9326...](https://github.com/tekoh/nypsi/commit/42d79f932683d771919c560df721bdcbb3322557)
#### Tuesday 2023-12-12 20:28:34 by max

silly grammar omg how did i not see that absolute fucking cock head i am

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[5168f5a8ee...](https://github.com/dagster-io/dagster/commit/5168f5a8ee14ef0af13ff65c9f567d7b27deb437)
#### Tuesday 2023-12-12 20:49:37 by quantum-byte

Fix #7442 / multi threading dropped log entries issue (#18493)

## Summary & Motivation

This MR should (based on my code understanding and testing) fix [issue
7442](https://github.com/dagster-io/dagster/issues/7442). It also fixes
in general randomly dropped user written log messages if logs are being
recorded from multiple threads.
Logging is quite important and its quite annoying to work around this
limitation/bug.

Maybe @sryza or @OwenKephart can have a look, since they already looked
into the 7442 issue.

## How I Tested These Changes

I tested the changes locally with an op/graph, which starts multiple
threads and logs multiple messages in each thread.

```python
import logging
import threading
import time

from dagster import AssetKey, AssetMaterialization, Output, job, op, repository

logger = logging.getLogger(__name__)


def background_thread(thread_name):
    for i in range(0, 5):
        logger.info(f"Background thread: {thread_name} {i}")
        time.sleep(0.5)


@op
def op1():
    yield AssetMaterialization(asset_key=AssetKey(["asset1"]))

    threads = []
    for thread_name in range(0, 5):
        thread = threading.Thread(
            name="background_thread",
            target=partial(background_thread, thread_name),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    yield AssetMaterialization(asset_key=AssetKey(["asset2"]))
    yield Output(123)


@op
def op2(arg):
    logger.info(f"Result of op1: {arg}")


@job
def dropped_events_job():
    op2(op1())


@repository
def dropped_events_repository():
    return [dropped_events_job]
```

Without my change i was missing a significant chunk of the expected log
messages in the captured log output:

![dropped_logs_without_change](https://github.com/dagster-io/dagster/assets/17649269/d777483a-911b-4010-b2e3-48bf7128437d)

With my change i had the exact amount of log messages in the captured
log output that i expected:

![no_dropped_logs_with_change](https://github.com/dagster-io/dagster/assets/17649269/d09f3617-fa86-415c-b7de-0dadab078b5b)

I also tested the original reproducing code from
https://github.com/dagster-io/dagster/issues/7442:

Without my change:

![grayed_out_op1_without_change](https://github.com/dagster-io/dagster/assets/17649269/c32c39ea-33a6-4207-a8c1-b8ddd30aa437)


With my change:

![green_op1_with_change](https://github.com/dagster-io/dagster/assets/17649269/fac597a6-4e2c-428b-afa4-f7695667ade7)


I am not that familiar with the dagster code. If you can point me to a
place where a unittest for this might go and some info on how to test it
in your opinion, than i will have a look at it.

---------

Co-authored-by: Florian Kaufmann <florian.kaufmann@corpuls.com>

---
## [Gboster-0/Monkestation2.0](https://github.com/Gboster-0/Monkestation2.0)@[1e9edd6a49...](https://github.com/Gboster-0/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Tuesday 2023-12-12 21:48:02 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[f5611c955f...](https://github.com/facebook/pyre-check/commit/f5611c955f54a60ea9c50875719a14bbd5c29743)
#### Tuesday 2023-12-12 21:57:34 by Steven Troxler

unify transitive successor interface, rename

Summary:
In this commit I'm continuing to try to clean up GlobalResolution interfaces
and eventually eliminate direct access to environments through it; in this
case the ConstraintsSetTest was grabbing a raw environment in order to run
`is_transitive_successor`.

An issue I ran into along the way is that the `GlobalResolution` and
`ClassHierarchy` interfaces for `is_transitive_successor` were not compatible;
the variable names didn't agree! The code was accessing a raw environment
specifically to work around this problem.

I decided that the name `is_transitive_successor` wasn't very informative
anyway; instead I renamed it to `has_transitive_successor` and made the
`~successor` a named argument / the predecessor a positional argument,
so that the name actually translates reasonably to English, as in
"does <predecessor class> have a transitive successor of name ~successor"?

I still hate the naming here, since "successor" actually means "ancestor"
in the type system; we're using terminology coming from thinking about
the MRO in a context where the MRO doesn't matter that much and thinking
about the inheritance DAG would make a lot more sense. But renaming in
terms of ancestors / descendants is a much bigger change than I want to make
right now and might even be controversial. At the moment I just want
consistent interfaces.

Reviewed By: connernilsen

Differential Revision: D52044965

fbshipit-source-id: ae4f6b98f4926c26ff3838f2a2982ba8fb270f01

---
## [marcello120/corpse-pattern-game](https://github.com/marcello120/corpse-pattern-game)@[dd6b373e09...](https://github.com/marcello120/corpse-pattern-game/commit/dd6b373e093ab45144d6cbee2a94f0d4e4722783)
#### Tuesday 2023-12-12 21:59:51 by exekutor7

Let me tell you a story

A story about suffering, a story about UI.
A story about how I end up killing myself because it took me 5 hours to almost fix a fucking pause menu.

---
## [Rykka-Stormheart/Emberfall](https://github.com/Rykka-Stormheart/Emberfall)@[33cae266af...](https://github.com/Rykka-Stormheart/Emberfall/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Tuesday 2023-12-12 22:00:24 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [iqba78/android_kernel_qcom_sm8150](https://github.com/iqba78/android_kernel_qcom_sm8150)@[e9c35f36f1...](https://github.com/iqba78/android_kernel_qcom_sm8150/commit/e9c35f36f1bca431d487a90371dcde94fa58b855)
#### Tuesday 2023-12-12 22:46:06 by Yaroslav Furman

power: supply: force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>

This is possibly breaking the DS28E16 verification driver
Signed-off-by: Forenche <prahul2003@gmail.com>

---
## [jo-sm/stylelint_d](https://github.com/jo-sm/stylelint_d)@[f5b8ce5735...](https://github.com/jo-sm/stylelint_d/commit/f5b8ce573577820766e83aee0b5e5b70e3d12afa)
#### Tuesday 2023-12-12 22:58:36 by Joshua Smock

Migrate from ts-jest to @swc/jest

As part of looking into https://github.com/jo-sm/stylelint_d/pull/887 I
ran into a ton of difficulty getting `ts-jest` to work with ESM, with
one of the main issues being related to importing `./utils.js` style
files.

This seems to be an issue with TypeScript + Jest combination when using
ESM, and the `ts-jest` preset hasn't "fixed" this yet (by doing
something like the `moduleNameMapper` approach mentioned in [comments like this]
(https://github.com/kulshekhar/ts-jest/issues/1057#issuecomment-1482644543). Has
there not been any PR from someone?

In any case, it's a bit frustrating that there wasn't a mention of this
in the troubleshooting docs as the issue above was pretty well
trafficked and commented on, and while there was a PR, it was closed and
there was no follow up. What's worse is that this issue has been known
for at least 4 years. There really should have been a troubleshooting
section added here even without a community contributed PR, and so I
don't have faith that either an additon to the preset or a mention in
the troubleshooting docs will happen anytime soon, at least before I
want to get Stylelint 16 in main.

While checking types in the test code is useful, it's not that important
since the actual code is type checked separately (both with the linter
and the compilation steps), and so instead of trying to fix `ts-jest`
and use the custom resolver, I opt for using `@swc/jest` which instead
removes the types entirely when compiling TS to JS. It has the added
benefit of being simpler, being only used in the `transform` config
rather than as a preset.

If at some point type checking the tests becomes important the
lint:types task can be updated to check test code too.

---
## [jo-sm/stylelint_d](https://github.com/jo-sm/stylelint_d)@[dac94ca188...](https://github.com/jo-sm/stylelint_d/commit/dac94ca188a8eb85c3d8ed279f5614c70cf3905d)
#### Tuesday 2023-12-12 23:05:10 by Joshua Smock

Migrate from ts-jest to @swc/jest

As part of looking into https://github.com/jo-sm/stylelint_d/pull/887 I
ran into a ton of difficulty getting `ts-jest` to work with ESM, with
one of the main issues being related to importing `./utils.js` style
files.

This seems to be an issue with the combination of TypeScript + Jest when using
ESM, and the `ts-jest` preset hasn't "fixed" this yet (by doing
something like the `moduleNameMapper` approach mentioned in
[comments like this](https://github.com/kulshekhar/ts-jest/issues/1057#issuecomment-1482644543). Has
there not been any PR from someone?

In any case, it's a bit frustrating that there wasn't a mention of this
in the troubleshooting docs as the issue above was pretty well
trafficked and commented on, and while there was a PR, it was closed and
there was no follow up. What's worse is that this issue has been known
for at least 4 years. There really should have been a troubleshooting
section added here even without a community contributed PR, and so I
don't have faith that either an additon to the preset or a mention in
the troubleshooting docs will happen anytime soon, at least before I
want to get Stylelint 16 in main.

While checking types in the test code is useful, it's not that important
since the actual code is type checked separately (both with the linter
and the compilation steps), and since `@swc/jest` is simpler and
hopefully doesn't have the above frustration factor, I've decided to
migrate from `ts-jest` to `@swc/jest`.

If at some point type checking the tests becomes important the
lint:types task can be updated to check test code too.

---

