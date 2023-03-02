## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-01](docs/good-messages/2023/2023-03-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,337,440 were push events containing 3,567,612 commit messages that amount to 290,396,258 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [aospasco/android_frameworks_base](https://github.com/aospasco/android_frameworks_base)@[b3bb34ec28...](https://github.com/aospasco/android_frameworks_base/commit/b3bb34ec285de0f611f2f85aaceed2e0d44ffb9d)
#### Wednesday 2023-03-01 00:27:05 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [akien-mga/godot](https://github.com/akien-mga/godot)@[09642e39aa...](https://github.com/akien-mga/godot/commit/09642e39aa664f703bd4ba66cf45ca5afb82219d)
#### Wednesday 2023-03-01 00:30:19 by Rémi Verschelde

Bump version to 4.0-stable \o/

4 years of development.
12,000 merged pull requests.
7,000 fixed issues.
1,500 individual contributors across engine and docs.

The Godot 4.0 release is by all metrics our biggest release so far.
No stone has been left unturned, all parts of the engine have been
modernized, refactored, overhauled, rewritten, redesigned.

Our work is far from done. Many areas still have significant known issues,
and will require focused work from all willing contributors to fix blocking
bugs, implement missing features, optimize for performance or compatibility,
and improve the user experience.

But Godot 4.0 marks the start of the new, modern Godot Engine, and a solid
foundation for us all to build upon. Future 4.x releases will come with a
much faster cadence, enabling us to iterate quickly on new features and
improvements to what we already provide.

To all of you who were involved in making Godot 4.0 what it is today, however
big or small your contributions were:

THANK YOU!

This was a massive undertaking, and you all participated in unique and
wonderful ways to build a free and open source game engine for everyone to
use and enjoy. You are breathtaking! <3

---
## [TheLoneTec/VilesMods](https://github.com/TheLoneTec/VilesMods)@[9068914ce1...](https://github.com/TheLoneTec/VilesMods/commit/9068914ce1430b5025f6a5ac59b33d4a534e9900)
#### Wednesday 2023-03-01 01:05:57 by VileHeathen

The Fish and Fuel Update

The Fish and Fuel Update

This is a two-part update which overhauls fishing, and adds “stuffed” firewood to the game. It also overhauls fueled lighting.

Note: These changes affect several of my mods, so it's best to update them all. And the changes may not be everyone's cup of tea, so I saved the previous version on a separate Github branch. This is in alpha, so the previous branch is more stable (yet still in testing).

Part I: The Fish:
Overhauls fish. Fishing still works the same way, but there is a wider variety of fish with better textures
There are also big-game fish, which are rare and yield a lot of meat. A couple even yield exotic leather.
Many fish are biome and climate-specific

Hypnosquid		Medium
Saberfish		Big Game
Redfin Tuna		Large
Snackerel		Tiny
Cuda			Small
Ice Flounder	Medium
Eeel			Small
Alligar		Large
Breadmouth 	Medium
Killer Catfish	Big Game
Death Sturgeon	Big Game
Sterling Perch	Tiny
Pinstripe Bass	Small

Part II: The Fuel (and lighting)
Firewood is now stuffed, meaning its burn time is related to the species of wood. Hardwoods tend to burn longer, so softwoods are often best used as kindling. Oak is king.

NEW BUILDINGS
Seasoning Rack - Can take many days to process, so plan accordingly.
Chopping Block - Sort of an upgrade of the log-splitting spot. All firewood chopping is moved here from the woodcutting bench.

NEW FUELS:
Rushlights - A cheap fast-burning light sources using grass and tallow/pitch/oil
Candles - Burns longer than rushlights
Pitch – extracted from pine and spruce
Fish Oil – from fish of course
Plant Wax (WIP) – extracted from certain seeds
Turpentine – made from pitch
Tallow – ok not new, but has more uses
Riven Boards – previously 'firewood', these are crude split planks for building and fuel

NEW LIGHTING:
Tree Torch – single use torch that destroys itself when it burns out
Rushlight Holder - also has a slot for a candle.
Fire Basket
Lamppost (oil-burning)
Lantern Sconce (oil-burning)
Candle Sconce
Candelabra (replaces original candle)
Standing torch – similar to the vanilla one
Cresset – Like the Olympics torch. Replaces bowl lamp.

Part III: Other fixes and changes
HARDCORE RENOVATIONS:
Fixed bar counters so they don't instantly build
NEW: Added two new doors: Ornate Door, which is attractive and durable, and the Barn door, which uses the rustic texture, and the rustic door gets a new texture.
Lowered drystone wall HP
Increase Flax Carpet cleanliness and lowered cost
HELL-BENT FOR LEATHER TANNING:
Fixed hides not rotting
Adjusted exotic leather color
MATERIALS SCIENCE:
Fixed missing ammonia recipe
Fixed broken Aermet recipe
Ores now have colors in the scanner
METALLURGY:
Fixed missing Russian translation
NEW: Added a new scenario start: The Guildmasters (Medieval)
Fixed broken coke kiln recipe
VILE'sTEAKS:
This isn't much of a mod, just some personal adjustments I've added for myself. Entirely optional.
Adds new pawn badges and retextures some of the old ones. WIP
Experimental changes to Realistic Darkness to make the moderate mode slightly darker. WIP
Pawns are more likely to spawn gay, bisexual and asexual to be more realistic to life.

---
## [anammari/argilla](https://github.com/anammari/argilla)@[4c5f51377e...](https://github.com/anammari/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Wednesday 2023-03-01 01:07:06 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[97f087d22e...](https://github.com/git-for-windows/git/commit/97f087d22ef9f9c03dc97565c9bf2a1763ceb0d1)
#### Wednesday 2023-03-01 01:13:11 by Johannes Schindelin

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
## [Hi-Angel/dotfiles](https://github.com/Hi-Angel/dotfiles)@[233bb78caf...](https://github.com/Hi-Angel/dotfiles/commit/233bb78cafb7d8249a6e273d5fac73d578f0b68e)
#### Wednesday 2023-03-01 01:18:26 by Konstantin Kharlamov

.emacs: make sure magit-auto-revert mode is down

Now I'm at the point of enough annoyance to call magit a piece of
shit. This time I stumbled upon this garbage being enabled, which I
never wanted and explicitly don't want, because I use instead
auto-revert mode, which is much better because it does not litter with
excess IO the files, which matters when a file you're visiting is
located on a network-mounted dir.

---
## [DosWorld/issrc](https://github.com/DosWorld/issrc)@[118c151654...](https://github.com/DosWorld/issrc/commit/118c15165401bb2acb62358f963777c44fb9c582)
#### Wednesday 2023-03-01 01:53:32 by Johannes Schindelin

Prevent `comctrl32.dll` from being inadvertently side-loaded

When running an installer from the Downloads folder, we do not trust any
file in that folder apart from the installer itself.

However, the way we need to mention `comctl32.dll` in the manifest
(because we want to use version 6, which cannot be simply loaded like
all the other `.dll` files because we would then end up with version 5)
unfortunately lets Windows look for a DLL side-load payload next to the
executable.

Now, it is relatively hard for a hacker to social-engineer their way to
a `<installer>.exe.Local` folder that contains the exact right subfolder
that then contains a usable (but maliciously-crafted) `comctl32.dll`.

However, we should prevent this if possible.

And it _is_ possible because we're copying the installer into a
temporary directory before spawning it there _anyway_, and before that
we do not need any visual styles, therefore we're plenty fine with using
`comctl32.dll` version 5 until that point.

So let's do this: modify the manifest of the installer (but not of its
compressed payload) so that it prevents DLL side-loading of
`comctl32.dll`.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[582f5b38cb...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Wednesday 2023-03-01 02:16:11 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [Quake-Backup/freedoom](https://github.com/Quake-Backup/freedoom)@[3efe8a0e41...](https://github.com/Quake-Backup/freedoom/commit/3efe8a0e4114414d764d4a1f03400a9a0f2094dd)
#### Wednesday 2023-03-01 02:47:02 by mc776

levels: fix various bugs. (#871)

* levels: fix various bugs.

Thanks to Goji!, Inuk and rednakhla on Discord for pointing these out.


E1M3: Northern lift simplified to address texture alignment problems.

E1M5: Door near (-205,1336) (leading out into open ceiling area with the big strip of lights down the middle) door tracks needed to be lower unpegged.

E1M9: Lift near (-2328,120) was split into 2 sectors, causing HOMs when they went out of sync. There's nothing that relies on this split (contrast the neat lighting stuff from Map22) so the lift is just merged into one sector.

E2M2: Shellbox near (-486,192) is right on the line between two stairs, causing it to rest on the bottom step which causes ports like GZDoom to have the sprite clip *very* visibly into the upper stair. Moved it slightly so it rests on the upper of those two stairs.

E2M3: Door leading to red key and "door" leading to soulsphere: former should be lower unpegged but latter should not, but were reversed. Two exit-door-textured doorframes also given more conventional DOORTRAK and lower unpegged treatment. The teleporter representing the hatch going down into the nukage is now fully repeatable.


Map07: Infinite height in vanilla would cause the spectres in the red key courtyard to trap the player on the entrance ledge from below in a way that could not be seen or diegetically explained. Those three spectres now warp in only after you cross the ledge. (Setting them to "ambush" would do nothing since you're in LOS with them from the top of the ledge.)

Map11: Lights above red keycard weren't aligned; moved that entire sector and added a few lines to round the corner. Removed a strobe effect on the exit teleporter to compensate for a GZDoom issue where the light would go to absolute zero during the blink.

Map12: Room to the south with the 2 stimpacks, ammo boxes, 2 chaingunners and berserk would sometimes cause some of the items to be "levitated" to the highest sectors they touch. Moved them away from said higher sectors - it looks a bit sloppier but this is a backroom not a storefront lol.

Map13: The easternmost archvile platform had the archvile stuck in the seam, preventing it from lowering in vanilla. (Worked fine in GZDoom) Moved it a little further in.

Map19: The combat slugs teleport in from a W1 teleporter which could sometimes be spent while one of the pinkies is blocking the destination, permanently preventing that slug from teleporting in. These are now WRs like the other teleporting enemies.

Map22: More W1 monster teleports that should be WR. Also filled in some missing textures in the multi-sector lift connecting the cavern to the hall in the southwest, which parts are clearly not meant to be seen moving separately but can - it still looks fucked up if you manage to desync them, but it's a diegetic fucked up now.

Map24: Another W1 spawn. This one is impossible to screw up in vanilla, but there are some mods that could end up spawning something there that could block the archviles from teleporting.

Map25: More W1 problems. The spawn source room now also has a small barrier to make sure each pinkie only goes to its own teleporter unless the initial teleport fails.

Map27: Lizardbaby dropping too far meant that the bracket was falling along with it in a visibly unnatural way.

Map29: Broke up all the long linedefs on the perimeter of the map to get around the invisible hitscan barrier bug: https://doomwiki.org/wiki/Hitscan_attacks_hit_invisible_barriers_in_large_open_areas
(Ideally this entire perimeter should be redone to break up the box in favour of more natural-looking formations, but that's a bit outside the scope of a fix like this.)


Also got rid of the Plutonia-style start/end teleports on the fixed Phase 2 maps, to address #867.

* maps: more fixes.

More floaty items and other things.

E1M9
- floater mid south stim by staircase
E1M7
- floater northwest clips near the tunnels
- floaters near switch by railings, now all on the railings
- duckproofed sector 439 barrier
E2M9
- floater thing #125 medikit on top of lift, now in middle of platform
- shotgun guy (thing #309) and the spectre behind it stuck in geometry.
- lines 430 and 761 both open the same door and are in the same room right next to each other. Since 761 is actually textured and positioned as a switch, the tag and special on 430 is removed.

* levels: flag e2m7 DM stuff as multi-only.

Marked the following based on eyeballing out what items are right next to DM spawns with no obvious alternate route to them: 487, 488; 203, 397; 499, 500, 501, 502; 482, 485; 491, 492, 493; 494; 496; 28, 486; 182; 54

* levels: more misc. fixes.

E1M6 W1 lines 2318 and 2321.

E3M5 Removed all monster block lines in that gross blood room and raised the blood floor to only 4 below the normal floors, but flagged more monsters in there as ambush to make up for it. Also fixed a lot of texture alignment issues in the top skin panels and lowered the ceiling, along with adding a new sector to address texture tiling issues in the northern teleporter room.

E4M1 fixed a mysterious HOM that was going on near the northern shadow line in the northern outdoor area. Merged a lot of sectors that were identical in their properties.

E4M7 entrance to sector 985 seems to be intended that the player run off the ledge into that room, then the pinkie near the ledge ambushes the player from behind. Instead, what sometimes happens is that the pinkie is alerted somehow, then obstructs the player (vanilla infinite height) from being able to get down there. That means of getting down into that room is now walled off, and instead you step onto that lift to bring it down from above. Neat side effect: any monsters still in the ring when you enter that room will follow you down there.

E4M5 linedefs 1724 and 1725 were facing the wrong way and couldn't be hit with projectiles.

Map25 Float thing 217. Moved that entire row further south to address floating item issues.

Map28 Float thing 464.

* levels: use inner room texture in E4M7 lift.

* levels: align side textures on that lift.

Didn't realize the little squares were sticking into the floor at the *bottom* of the lift as well.

---
## [xTVaser/jak-project](https://github.com/xTVaser/jak-project)@[c249dbc437...](https://github.com/xTVaser/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Wednesday 2023-03-01 03:09:00 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [lmcqu25/WGU_BSDMDA](https://github.com/lmcqu25/WGU_BSDMDA)@[843f966577...](https://github.com/lmcqu25/WGU_BSDMDA/commit/843f9665779488e237d76599a29a5cc3dd2ec36d)
#### Wednesday 2023-03-01 03:31:32 by Logan McQuillan

Create C773_User_Interface_Design

INTRODUCTION
User interface and user experience (UI/UX) designer is one of the most popular job titles in the technology industry. UI/UX designers tend to enjoy the challenges associated with creating products that people love. Industry leaders know that design is a substantial competitive advantage, and they are competing for best talents; therefore, the demand for designers is high.

UI/UX design requires the understanding of core design principles, tools, and best practices. Having foundational principles of design and design techniques, such as design thinking, gives you a mindset required to create an effective user experience. You are also able to conduct user research that gives you a better understanding of the problem space and eventually leads you to communicate your designs and best practices to users through prototyping.

This task allows you to showcase your problem-solving skills, how you plan to manage and maintain this project, and which strategies you will implement for search engine optimization (SEO).You will evaluate the provided “Paradigm Pet Professionals Website” in the Web Links section and the attached “Paradigm Pet Professionals UI Design Specifications.” You will develop plans to create information architecture for various user personas and stakeholder needs while adhering to accessibility standards. You will also develop a maintenance plan that includes SEO and consideration of a future mobile-friendly web page design.
SCENARIO
You were recently hired as a UI/UX Designer for Synesthor, an IT services company that offers on-site consultation for small businesses without an IT department. Synesthor recently contracted with Paradigm Pet Professionals, a company that specializes in providing virtual consultations to pet owners with state-of-the-art, evidence-based health and well-being information. Its website was designed by a part-time intern 10 years ago. Most people who visit the website are prospective and new pet owners located in the United States who seek information about basic pet care and are interested in speaking with a consultant. Paradigm Pet Professionals contracted with Synesthor’s UI/UX department to develop a responsive website to meet the needs of its company and the needs of users.

Your first task is to evaluate the existing website and user design specifications provided by Paradigm Pet Professionals (see Web Links and Supporting Documents sections). You will also develop a sitemap, wireframe, and maintenance plan for the redeveloped website.
REQUIREMENTS
Your submission must be your original work. No more than a combined total of 30% of the submission and no more than a 10% match to any one individual source can be directly quoted or closely paraphrased from sources, even if cited correctly. The similarity report that is provided when you submit your task can be used as a guide.

 

You must use the rubric to direct the creation of your submission because it provides detailed criteria that will be used to evaluate your work. Each requirement below may be evaluated by more than one rubric aspect. The rubric aspect titles may contain hyperlinks to relevant portions of the course.

 

Tasks may not be submitted as cloud links, such as links to Google Docs, Google Slides, OneDrive, etc., unless specified in the task requirements. All other submissions must be file types that are uploaded and submitted as attachments (e.g., .docx, .pdf, .ppt).

 

A.  Using the attached “Paradigm Pet Professional UI Design Specifications” and existing “Paradigm Pet Professionals Website” from the Web Links section, compare the content, functionality, and navigation of the current website to user specifications and evaluate audience and stakeholders needs by doing the following:

1.  Describe how the current website content fails to meet audience and stakeholder needs.

2.  Describe how the current website functionality fails to meet audience and stakeholder needs.

3.  Describe how the current navigation system fails to meet audience and stakeholder needs.

 

B.  Determine the information architecture for the new website based on the attached “Paradigm Pet Professional UI Design Specifications” by doing the following:

1.  Explain the necessary website functionality and micro interactions needed to meet audience and stakeholder needs.

2.  Describe the type of content that will be used for one new page based on one of the new user personas, including how the elements of the content align directly to the chosen user persona.

3.  Identify existing content from the website that will be removed or redeveloped and explain how that content fails to meet the proposed audience and stakeholder needs.

4.  Create a visual sitemap to determine the structure and the hierarchy of the site content, including the following:

•  a home page

•  a page for each existing pet page

•  a new page for the new user persona you identified in part B2

 

Note: You can use any tool to create the sitemap, such as graphic creation or manipulation software, presentation software, word processing software, or another tool of your choice. The sitemap must be submitted as an image embedded within your document.

 

5.  Explain how your information architecture meets audience and stakeholder needs.

6.  Explain the primary and secondary navigational elements required to support the information architecture.

a.  Explain how these primary and secondary navigational elements each align with audience and stakeholder needs.

 

C.  Determine page layout by creating a mid-fidelity wireframe for the home page that is sized for a desktop website that includes each of the following:

•  site header, including the branding elements

•  site footer 

•  primary and secondary navigational elements 

•  placeholder text and placeholder images

•  specific components needed to support the information architecture (e.g., buttons, links, form fields, search bar)

 

Note: You can use any tool to create the wireframe, such as graphic creation or manipulation software, presentation software, word processing software, or another tool of your choice. The wireframe must be submitted as an image embedded within your document.

 

D.  Develop a detailed maintenance plan for the responsive website that aligns with stakeholder needs outlined in the attached “Paradigm Pet Professional UI Design Specifications,” include one maintenance task for each of the following:

•  efforts to ensure universal accessibility to all site content 

•  the relationship between written content and SEO

•  tasks required to properly maintain the website

•  plan for rendering the website on desktop and mobile devices

•  SEO strategies for mobile devices

 

E.  Demonstrate professional communication in the content and presentation of your submission.

File Restrictions
File name may contain only letters, numbers, spaces, and these symbols: ! - _ . * ' ( )
File size limit: 200 MB
File types allowed: doc, docx, rtf, xls, xlsx, ppt, pptx, odt, pdf, txt, qt, mov, mpg, avi, mp3, wav, mp4, wma, flv, asf, mpeg, wmv, m4v, svg, tif, tiff, jpeg, jpg, gif, png, zip, rar, tar, 7z

---
## [rodrigocitadin/portfolio-v2](https://github.com/rodrigocitadin/portfolio-v2)@[01587c85aa...](https://github.com/rodrigocitadin/portfolio-v2/commit/01587c85aae49d031d67b42791f7029e50239743)
#### Wednesday 2023-03-01 04:16:07 by rodrigocitadin

Say So

Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so
Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so

It's been a long time since you fell in love
You ain't coming out your shell, you ain't really been yourself
Tell me, what must I do? (Do tell, my love)
'Cause luckily I'm good at reading
I wouldn't bug him, but he won't stop cheesin'
And we can dance all day around it
If you frontin', I'll be bouncing
If you want it, scream it, shout it, babe
Before I leave you dry

Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so
Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so

Let me check my chest, my breath right quick (ha)
He ain't ever seen it in a dress like this (ah)
He ain't ever even been impressed like this
Prolly why I got him quiet on the set like zip
Like it, love it, need it, bad
Take it, own it, steal it, fast
Boy, stop playing, grab my ass
Why you actin' like you shy?
Shut it, save it, keep it pushin'
Why you beating 'round the bush?
Knowin' you want all this woman
Never knock it 'til you try (yah, yah)
All of them bitches hating I have you with me
All of my niggas sayin' you mad committed
Realer than anybody you had, and pretty
All of the body-ody, the ass and titties

Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so
Day to night to morning, keep with me in the moment
I’d let you had I known it, why don’t you say so?
Didn’t even notice, no punches left to roll with
You got to keep me focused, you want it? Say so

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[91f06a97d3...](https://github.com/lessthnthree/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Wednesday 2023-03-01 04:44:28 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[d95ca04819...](https://github.com/lessthnthree/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Wednesday 2023-03-01 04:44:28 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[8500d62b79...](https://github.com/lessthnthree/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Wednesday 2023-03-01 04:44:28 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Sans3108/valro-lfg](https://github.com/Sans3108/valro-lfg)@[b884b0ba8b...](https://github.com/Sans3108/valro-lfg/commit/b884b0ba8bc78114bb58ed753e84b33c2aedc108)
#### Wednesday 2023-03-01 04:51:01 by Sans3108

merging  (#3)

* pain and suffering are my best friends

* idk

* cleanup

* cathing up

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[296ca23aa1...](https://github.com/carshalash/tgstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Wednesday 2023-03-01 04:53:25 by Jacquerel

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
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4599842d7c...](https://github.com/TheBoondock/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Wednesday 2023-03-01 05:11:55 by Jacquerel

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
## [IFuckedUpMerging/T.E.-station](https://github.com/IFuckedUpMerging/T.E.-station)@[6bcb2a7872...](https://github.com/IFuckedUpMerging/T.E.-station/commit/6bcb2a787236007f597dd7eed358cd9c6c8712fb)
#### Wednesday 2023-03-01 05:21:56 by JasmineRickards

Merge pull request #11 from IFuckedUpMerging/pizza-pasta-oh-god-is-that-tony-what-the-fuck-dude.-oh-my-god-dude-he-had-a-family-what-the-fuck.-holy-shit.-oh-my-fucking-god,-my-insides,-everything-aches.-what-the-FUCK-man.-WHAT-THE-FUCK-

1984s Soylent Green

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[31eabb62f1...](https://github.com/Latentish/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Wednesday 2023-03-01 05:40:50 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[3978cfe70f...](https://github.com/kugamo/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Wednesday 2023-03-01 06:36:57 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

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

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[32c31b8fc0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Wednesday 2023-03-01 06:45:48 by SkyratBot

[MIRROR] Lighting source refactor (Tiny) [MDB IGNORE] (#19370)

* Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode.
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible.
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

* Lighting source refactor (Tiny)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[9e981753ca...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Wednesday 2023-03-01 06:45:48 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[26688597e3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Wednesday 2023-03-01 06:45:48 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [peff/git](https://github.com/peff/git)@[e5802ea546...](https://github.com/peff/git/commit/e5802ea546bf75d41f59747fd60d7c73014cc9d4)
#### Wednesday 2023-03-01 08:26:44 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[34daca112c...](https://github.com/cmss13-devs/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Wednesday 2023-03-01 09:01:06 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

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
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [dcunited001/.emacs.guix](https://github.com/dcunited001/.emacs.guix)@[7634c01193...](https://github.com/dcunited001/.emacs.guix/commit/7634c01193a6b5c40cf6a58936a5e48e350395bc)
#### Wednesday 2023-03-01 09:05:43 by David Conner

i forgot you can't get mad when the powerful ignore the inevitable

* an academic monopoly has created bad science/knowledge and this enables the
government to fix policy/regulation in place to serve corporations' interests --
this means there are trillions in outstanding liabilities from bad
food/medicine/chemicals (though negligence is unprovable).

* just consider the collective effect the following have: sugar, cooking
oils (more responsible for food allergies than gluten ever could be), pharma
side effects, soft drinks (phosphoric acid leaches calcium strongly contributing
to osteoperosis), GMO (weird food allergies), constant immune activation,
systemic mineral malnutrition (and fraudulently marketed supplements), etc. It's
created a system in america that is in the process of bankrupting the country,
but the assumption is still that those seeking medical treatment for /completely
preventable chronic diseases/ should pay for their treatment.

* if over a few years, computational techniques prove systemic malfeasance, the
liabilities probably won't be paid, but the shock in american consumers will
destroy whatever faith we have left in the academics and elites. the effects
from the above causes are unbelievably high and waking up to this information
over too quickly cannot be permitted. THEY WILL RESET THE SYSTEM. they certainly
won't address the obvious: what are they going to do about it all.

I understand things take time and I hate apologizing for being concerned. It's
hard to keep this shit bottled up. the incompetence of our leaders is
unbelievable and we are wasting time.

---
## [mortenschioler/loco](https://github.com/mortenschioler/loco)@[6ba970e1c2...](https://github.com/mortenschioler/loco/commit/6ba970e1c26a562724488c32779306d6df7873df)
#### Wednesday 2023-03-01 09:49:45 by Morten Emmanuel Schiøler

Make voice in README neutral

The README in the original @aengelberg/loco is amazing in my opinion. It is also quite personal in a couple of sections. I want to adapt these paragraphs in a respectful way with this PR, correcting texts where circumstances have changed due to the fork, while preserving the history and soul of the original project.

I think it's very important that READMEs and documentation in general is up-to-date, especially when the goal is Open Source collaboration, and that's why this makes PR #1.

---
## [Mehrbod2002/nushell](https://github.com/Mehrbod2002/nushell)@[378a3ae05f...](https://github.com/Mehrbod2002/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Wednesday 2023-03-01 11:24:16 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[5f9f60713b...](https://github.com/Stalkeros2/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Wednesday 2023-03-01 11:31:08 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

</details>

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [Sir-Photch/Kvaesitso](https://github.com/Sir-Photch/Kvaesitso)@[c664f2e777...](https://github.com/Sir-Photch/Kvaesitso/commit/c664f2e777df4226ae47988fd95d250f126f12af)
#### Wednesday 2023-03-01 11:31:54 by MM20

Fuck you Android studio, please fix your goddamn focus, I wanted to type into the terminal, not the editor

---
## [TianWalkzzMiku/SRyzen-CAF](https://github.com/TianWalkzzMiku/SRyzen-CAF)@[816126441f...](https://github.com/TianWalkzzMiku/SRyzen-CAF/commit/816126441f42a2725c46aaaf24da22d287cd566b)
#### Wednesday 2023-03-01 11:54:51 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[7cc6934eff...](https://github.com/DAKKA-WAAAGH/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Wednesday 2023-03-01 12:04:10 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Julitos4real/julius-aderonmu](https://github.com/Julitos4real/julius-aderonmu)@[47f4641956...](https://github.com/Julitos4real/julius-aderonmu/commit/47f4641956299b3a3062a07a922e75a19c5a1cb1)
#### Wednesday 2023-03-01 14:02:27 by Julitos4real

Add files via upload

Project Background Information. 
Every ten years, the United Kingdom undertakes a census of the population, with the most recent one 
having been conducted in 2021. The purpose of such a census is to compare different people across the 
nation and to provide the government with accurate statistics of the population to enable better 
planning, to develop policies, and to allocate certain funding.  
 
In the project, you will be provided with a mock census of an imaginary modest town. I would like you 
to consider yourselves to be part of a local government team who will be making decisions on what to 
do with an unoccupied plot of land and what to invest in. To address these questions, you will need to 
clean and analyse the mock census data provided.  
 
About this Mock Census. 
The mock census you will be given contains randomly generate data using the Faker package in 
Python. It has been generated in a similar manner to (and designed to directly emulate the format of) 
the 1881 census of the UK wherein only a few questions were asked of the population. The fields 
recorded are as follows: 
(1)  Street Number (this is set to “1” if it is a unique dwelling); 
(2)  Street Name; 
(3)  First Name of occupant; 
(4)  Surname of occupant; 
(5)  Age of occupant; 
(6)  Relationship to the “Head” of the household (anyone aged over 18 can be a “Head” – they are 
simply the person who had the responsibility to fill in the census details); 
(7)  Marital status (one of: Single, Married, Divorced, Widowed, or “NA” in the case of minors); 
(8)  Gender (one of: Male, Female; note that other responses were not implemented in 1881); 
(9)  Occupation (this field was implemented in a modern style, rather than typical 1881 
occupations); 
(10) Infirmity (we have implemented a limited set of infirmities following the style of 1881); 
(11) Religion (we have implemented a set of real-world religions).  
 
The first task you will have to do is to clean this dataset. As you will rapidly discover, there are missing 
entries, and, candidly, some responses from the population are outright lies. Part of the grading for the 
assignment will assess these details.  
 
The Task. 
The town from the census is a modestly sized one sandwiched between two much larger cities that it is 
connected to by motorways. The town does not have a university, but students do live in the town and 
commute to the nearby cities. Once you have a cleaned dataset to analyse, your task is to decide the 
following: 
(a) What should be built on an unoccupied plot of land that the local government wishes to 
develop?  Your choices are:  
 (i) High-density housing. This should be built if the population is significantly expanding. 
 (ii) Low-density housing. This should be built if the population is “affluent” and there is 
demand for large family housing. 
 (iii) Train station. There are potentially a lot of commuters in the town and building a train 
station could take pressure off the roads. But how will you identify commuters? 
 (iv) Religious building. There is already one place of worship for Catholics in the town. Is 
there demand for a second Church (if so, which denomination?), or for a different religious building? 
 (v) Emergency medical building. Not a full hospital, but a minor injuries centre. This should 
be built if there are many injuries or future pregnancies likely in the population.  
 (vi) Something else?  
Whichever you choose, you must justify it from the data provided to you and argue it is a priority 
against other choices.  
(b) Which one of the following options should be invested in? 
 (i) Employment and training. If there is evidence for a lot of unemployment, we should re-
train people for new skills.  
 (ii) Old age care. If there is evidence for increasing numbers of retired people in future years, 
the town will need to allocate more funding for end of life care.  
 (iii) Increase spending for schooling. If there is evidence of a growing population of school-
aged children (new births, or families moving in to the town), then schooling spend should increase.  
 (iv) General infrastructure. If the town is expanding, then services (waste collection; road 
maintenance, etc.) will require more investment.  
 
In order to address these two questions, it is suggested that some of the analysis you undertake is: 
• Examine the age distribution (age pyramid) of the population. Is it growing or shrinking? Will 
there be more retired aged people in the future, more school-aged children, more young 
people, etc.  
• Examine unemployment trends. Are certain ages more likely to be unemployed than others. 
• Examine religious affiliations. Are any religions growing, or shrinking? Are there any newer 
religions that are increasing in numbers? 
• Examine the divorce and marriage rate. This might impact how you think about housing.  
• Examine the occupancy level (how many people per house) and determine if existing housing 
is being under or over-used. 
• Examine the number of university students. All of these are commuters since there are no 
universities in the town. Are there any other professions that are likely to be commuters? 
• What is the birth rate and death rate for the town?  
These are merely suggestions, there are plentiful other analyses that could be undertaken that will be 
discussed in the videos and in class. Ultimately, your answers to (a) and (b) must be justified from the 
census data, and argued by balancing the different needs of the population and supported through 
statistics and where appropriate, hypothesis testing. As such, this is a “real” exercise but based on 
artificial data. [As a disclaimer: any reference to real people or places, living or dead, is purely 
coincidental and a product of the random generators that have been used.

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[cf40008c78...](https://github.com/bmccrat/songage/commit/cf40008c7894351bbc29bc4a44309258e58abc3d)
#### Wednesday 2023-03-01 14:22:33 by bmccrat

Create I AM A GOD

This song was written shortly before my first trip to rehab when I was 16 I remember because I played it for all the girls there in the adolescent rehab and they went nuts over it. I remember being able to make myself cry playing it, from the spirit most times and preformatively other times. I always hated the werewolf verse but other people have liked it so I never altered the song or edited it much from its original version. As is characteristic of most of my early songwriting there is no bridge, and the chord progression is identical throughout the verses and chorous. My first opus. 

NOTE: Between now and the next hard copy of a song there is a large gap, there was productivity from this time but nothing that has traveled with me and stood the test of time. I still have some audio recordings of these long lost songs but they scarcely exist on paper except for fragments of poetry shuffled away in some folder at my childhood home.

---
## [Nuc134rr/DohMansLand](https://github.com/Nuc134rr/DohMansLand)@[a8bead8d6b...](https://github.com/Nuc134rr/DohMansLand/commit/a8bead8d6b343a3207cee807773836024f758a85)
#### Wednesday 2023-03-01 14:44:43 by George Bauer

Ancient Spell From My Evil Mind.... (also Fuck You Cayden For Merging Old Shit Into Master)

---
## [VARoDeK/linux-next](https://github.com/VARoDeK/linux-next)@[6471384af2...](https://github.com/VARoDeK/linux-next/commit/6471384af2a6530696fc0203bafe4de41a23c9ef)
#### Wednesday 2023-03-01 14:58:14 by Alexander Potapenko

mm: security: introduce init_on_alloc=1 and init_on_free=1 boot options

Patch series "add init_on_alloc/init_on_free boot options", v10.

Provide init_on_alloc and init_on_free boot options.

These are aimed at preventing possible information leaks and making the
control-flow bugs that depend on uninitialized values more deterministic.

Enabling either of the options guarantees that the memory returned by the
page allocator and SL[AU]B is initialized with zeroes.  SLOB allocator
isn't supported at the moment, as its emulation of kmem caches complicates
handling of SLAB_TYPESAFE_BY_RCU caches correctly.

Enabling init_on_free also guarantees that pages and heap objects are
initialized right after they're freed, so it won't be possible to access
stale data by using a dangling pointer.

As suggested by Michal Hocko, right now we don't let the heap users to
disable initialization for certain allocations.  There's not enough
evidence that doing so can speed up real-life cases, and introducing ways
to opt-out may result in things going out of control.

This patch (of 2):

The new options are needed to prevent possible information leaks and make
control-flow bugs that depend on uninitialized values more deterministic.

This is expected to be on-by-default on Android and Chrome OS.  And it
gives the opportunity for anyone else to use it under distros too via the
boot args.  (The init_on_free feature is regularly requested by folks
where memory forensics is included in their threat models.)

init_on_alloc=1 makes the kernel initialize newly allocated pages and heap
objects with zeroes.  Initialization is done at allocation time at the
places where checks for __GFP_ZERO are performed.

init_on_free=1 makes the kernel initialize freed pages and heap objects
with zeroes upon their deletion.  This helps to ensure sensitive data
doesn't leak via use-after-free accesses.

Both init_on_alloc=1 and init_on_free=1 guarantee that the allocator
returns zeroed memory.  The two exceptions are slab caches with
constructors and SLAB_TYPESAFE_BY_RCU flag.  Those are never
zero-initialized to preserve their semantics.

Both init_on_alloc and init_on_free default to zero, but those defaults
can be overridden with CONFIG_INIT_ON_ALLOC_DEFAULT_ON and
CONFIG_INIT_ON_FREE_DEFAULT_ON.

If either SLUB poisoning or page poisoning is enabled, those options take
precedence over init_on_alloc and init_on_free: initialization is only
applied to unpoisoned allocations.

Slowdown for the new features compared to init_on_free=0, init_on_alloc=0:

hackbench, init_on_free=1:  +7.62% sys time (st.err 0.74%)
hackbench, init_on_alloc=1: +7.75% sys time (st.err 2.14%)

Linux build with -j12, init_on_free=1:  +8.38% wall time (st.err 0.39%)
Linux build with -j12, init_on_free=1:  +24.42% sys time (st.err 0.52%)
Linux build with -j12, init_on_alloc=1: -0.13% wall time (st.err 0.42%)
Linux build with -j12, init_on_alloc=1: +0.57% sys time (st.err 0.40%)

The slowdown for init_on_free=0, init_on_alloc=0 compared to the baseline
is within the standard error.

The new features are also going to pave the way for hardware memory
tagging (e.g.  arm64's MTE), which will require both on_alloc and on_free
hooks to set the tags for heap objects.  With MTE, tagging will have the
same cost as memory initialization.

Although init_on_free is rather costly, there are paranoid use-cases where
in-memory data lifetime is desired to be minimized.  There are various
arguments for/against the realism of the associated threat models, but
given that we'll need the infrastructure for MTE anyway, and there are
people who want wipe-on-free behavior no matter what the performance cost,
it seems reasonable to include it in this series.

[glider@google.com: v8]
  Link: http://lkml.kernel.org/r/20190626121943.131390-2-glider@google.com
[glider@google.com: v9]
  Link: http://lkml.kernel.org/r/20190627130316.254309-2-glider@google.com
[glider@google.com: v10]
  Link: http://lkml.kernel.org/r/20190628093131.199499-2-glider@google.com
Link: http://lkml.kernel.org/r/20190617151050.92663-2-glider@google.com
Signed-off-by: Alexander Potapenko <glider@google.com>
Acked-by: Kees Cook <keescook@chromium.org>
Acked-by: Michal Hocko <mhocko@suse.cz>		[page and dmapool parts
Acked-by: James Morris <jamorris@linux.microsoft.com>]
Cc: Christoph Lameter <cl@linux.com>
Cc: Masahiro Yamada <yamada.masahiro@socionext.com>
Cc: "Serge E. Hallyn" <serge@hallyn.com>
Cc: Nick Desaulniers <ndesaulniers@google.com>
Cc: Kostya Serebryany <kcc@google.com>
Cc: Dmitry Vyukov <dvyukov@google.com>
Cc: Sandeep Patil <sspatil@android.com>
Cc: Laura Abbott <labbott@redhat.com>
Cc: Randy Dunlap <rdunlap@infradead.org>
Cc: Jann Horn <jannh@google.com>
Cc: Mark Rutland <mark.rutland@arm.com>
Cc: Marco Elver <elver@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Nuc134rr/DohMansLand](https://github.com/Nuc134rr/DohMansLand)@[1588c9bcd9...](https://github.com/Nuc134rr/DohMansLand/commit/1588c9bcd9e5b326d542d44b24d21c667aacd0eb)
#### Wednesday 2023-03-01 15:12:30 by MilesShroom

Spawn capsule fx rename ians stupid ass fucking fx

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fc1e2e5e26...](https://github.com/harryob/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Wednesday 2023-03-01 15:18:09 by riot

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
## [scarlettp1619/Trash-Muncher-Webapp](https://github.com/scarlettp1619/Trash-Muncher-Webapp)@[c65363093c...](https://github.com/scarlettp1619/Trash-Muncher-Webapp/commit/c65363093cb2a2a2e2e32d16088016ac2f8dcb7e)
#### Wednesday 2023-03-01 15:30:52 by Owen Lee

scheduler monlkey-paytch

fucking bullshit threading shit tahat took wayyy too long fml

---
## [aospa-phoenix/proprietary_vendor_xiaomi-tym](https://github.com/aospa-phoenix/proprietary_vendor_xiaomi-tym)@[ecb97fcd38...](https://github.com/aospa-phoenix/proprietary_vendor_xiaomi-tym/commit/ecb97fcd38084128c2ffdb211839b7d8061b57b2)
#### Wednesday 2023-03-01 17:37:17 by Tushar Mahajan

apollo: Enable thermal-engine service
* fuck you xiaomi

Signed-off-by: Tushar Mahajan <mahajant99@gmail.com>

---
## [mcx/pytorch](https://github.com/mcx/pytorch)@[83275d8cdf...](https://github.com/mcx/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Wednesday 2023-03-01 18:31:58 by Brian Hirsh

add torch.autograd._set_view_replay_enabled, use in aot autograd (#92588)

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc @albanD @soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/92588
Approved by: https://github.com/ezyang, https://github.com/albanD

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[ee9d4bdc3c...](https://github.com/newstools/2023-new-york-post/commit/ee9d4bdc3c1fe30f85bedf85d59c81057546dc96)
#### Wednesday 2023-03-01 18:53:40 by Billy Einkamerer

Created Text For URL [nypost.com/2023/03/01/my-boyfriend-cheated-on-me-with-my-stepmom-heres-how-i-busted-them/]

---
## [orez-/alphgen](https://github.com/orez-/alphgen)@[f77d50577e...](https://github.com/orez-/alphgen/commit/f77d50577e24e870df9fb610374cf8b3da29e1e2)
#### Wednesday 2023-03-01 18:58:09 by Brian Shaginaw

Fix filled glyph issue

We're seeing an issue that's most easily demonstrated by the following
lowercase "o" shape:

......
..##..
.#..#.
.#..#.
..##..
......

Our previous approach contour-ized this as two contours: a clockwise
ring around the outside and a counterclockwise ring around the inside.
This works well in most cases, but not in the case of our lowercase "o"
there. Many (but not all) font renderers were seemingly ignoring the
inner contour and treating the figure as completely filled.

I believe (+ testing indicates) this issue only occurs when an inner
contour shares ALL of its points with another contour.

Originally I wanted to solve this by detecting this case and adding an
extra dummy point arbitrarily between two points, but there's a few
additional issues to consider:
- I was kind of dreading writing this detection code. I didn't end up
  writing it, but I'm having trouble thinking of how to do it better
  than O(mn²) where n is the number of contours and m is the number of
  pts per contour. Granted n's fairly small, but it's gross overhead on
  every glyph.
- Even after detecting this, there's no guarantee there will even be
  room for a dummy point to fit! Contour coordinates are integers: with
  a 1x1 empty area there's nowhere to fit another dummy point.
  As a separate issue, we're gonna have to scale up the glyphs anyway..
  maybe we try to unconditionally scale up to ensure there's room?
  There _is_ an upper bound to font size.. we _probably_ won't hit that?
  Maybe we catch this 1x1 case and fall back to a different wrapping
  technique?

...Say, what would that different wrapping technique look like, anyway?

If instead of treating the "o" above as two rings we treated it as
four disjoint polygons, this would solve our problem. How do we make
that happen? Turns out it's as easy as swapping our contour walking
behavior: instead of preferring to turn left at a catty-corner, we
prefer turning right:

........
.###....
.###....
.###....
...^###.
....###.
....###.
........

Previously we'd turn left at the arrow to capture the entire figure as
one contour, but now we turn right to only capture the bottom rect
(we pick up the top rect as a separate contour in a different pass).

This is what this commit changes: we're now unconditionally forming
more, smaller contours.

The tradeoff here is file size: I believe this strategy necessarily
results in an as-large or larger file size. Consider the "o" above:
we previously described one contour of 8 points and one contour of
4 points for a total of 12, but we're now describing four contours of
4 points each for a total of 16. In practical terms, the small font I've
been building this library for went from 6944 bytes to 7460 bytes.
500 bytes isn't the end of the world, +7% filesize isn't such an issue
(this commit message is six times that size...). But it's something to
be aware of. If filesize is a concern later, we can revisit the
fallback approach.

This bug wasn't a design oversight or typo or mistake really. It was
more of a hidden requirement. Given that, it's wild to me that this was
a one-line change to fix! (give or take tests.) I love it.

---
## [UnburnedAlliance/lucid-on-vue-template](https://github.com/UnburnedAlliance/lucid-on-vue-template)@[859257cabc...](https://github.com/UnburnedAlliance/lucid-on-vue-template/commit/859257cabc9557550d4355b64b6139f812637918)
#### Wednesday 2023-03-01 19:40:40 by UnburnedAlliance

Fuck this fucking bullshit fucking fucker. Berry make some goddamn better documentation for Lucid goddamn fuck

---
## [JasmineRickards/T.E.-station](https://github.com/JasmineRickards/T.E.-station)@[ca6421e999...](https://github.com/JasmineRickards/T.E.-station/commit/ca6421e999007076809b9a94d490f74bbf449733)
#### Wednesday 2023-03-01 19:45:33 by JasmineRickards

Merge pull request #14 from IFuckedUpMerging/errand-girl-shit

[REQ] Station traits are now a config flag

---
## [Ekaterina-von-Russland/tgstation](https://github.com/Ekaterina-von-Russland/tgstation)@[2b76197397...](https://github.com/Ekaterina-von-Russland/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Wednesday 2023-03-01 19:53:47 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [peff/git](https://github.com/peff/git)@[e0bbd60214...](https://github.com/peff/git/commit/e0bbd60214364df9d8158045dcf74e5151d5f85a)
#### Wednesday 2023-03-01 19:54:33 by Jeff King

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
## [ZzAve/teambalance](https://github.com/ZzAve/teambalance)@[be41a19967...](https://github.com/ZzAve/teambalance/commit/be41a199672f42698acd0e60d1d135ce589d480b)
#### Wednesday 2023-03-01 21:10:29 by Julius van Dis

Upgrade to MUI 5 (#227)

* clean covid-19

* Add themeprovider to app

* Add MUI 5 dependencies

- included @mui/x-date-pickers (as replacement for @material-ui/pickers)
- included emotion for typesafe css

* Remove MUI 4 dependencies, and fix breaking component changes

Follows: https://mui.com/material-ui/migration/v5-component-changes/

Noteworthy:
- Fixes in createStyles and withStyles
- Deprecated `<Hidden>` component (mostly move to:
 ```<Typography variant={"button"} sx={{ display: { sm: "block", xs: "none" } }}>
  Terug naar de veiligheid</Typography>```
- App is wrapped in <StyledEngineProvider injectFirst> to support JSS (prepare for migration to emotion
- Shit ton of renames from @material-ui/* to @mui/*
- Verwijderen van AttendeeStyledButton, en fallback op normale Button. 'uncertain' is mapped naar 'warning', en die kleur is aangepast in de palette van de theme.

* Apply webpack optimisations to reduce build times (dev: 30s to 10s, prod 60s to 10s)

* Replace JSS with emotion

* Remove @mui/styles

* Upgrade notistack to v2

* Pin dependencies

* Fix latest mui things

---
## [Nescura/EDGP-2](https://github.com/Nescura/EDGP-2)@[3f8547fc57...](https://github.com/Nescura/EDGP-2/commit/3f8547fc5792c547741fc623481a77d6b28682d5)
#### Wednesday 2023-03-01 21:27:44 by Tamanegi-K

HUGE Things

- Decoupled the desktop icon buttons - can now spawn a bunch of other crap that will spawn panels if incorrectly double clicked. Will do the same for other buttons
- Adjusted some raycasting interaction bullshit between moving desktop icons vs panels
- DesktopIcon prefab updated - can set their own icon and file name when needed
- New cheat buton - Pressing = will clear all panels and give 20s of breathing room
- added a placeholder icon for the virus to laugh at you
- Added several functions to Button.cs to account for new desktop icon buttons
- Scene.cs can now spawn desktop icons, but object pool is currently malfuncitoning (my brain hurts so I'll figure it out later)

---
## [mjfeller/dwm](https://github.com/mjfeller/dwm)@[67d76bdc68...](https://github.com/mjfeller/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2023-03-01 22:30:18 by Chris Down

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
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[c4250cc115...](https://github.com/zerbina/nimskull/commit/c4250cc11536bf6c8922bbd192d2ec39142d46d9)
#### Wednesday 2023-03-01 22:40:47 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[4378721e0c...](https://github.com/Buildstarted/linksfordevs/commit/4378721e0c2cb3ee7611892266d1968ff925ee3b)
#### Wednesday 2023-03-01 23:10:44 by Ben Dornis

Updating: 3/1/2023 11:00:00 PM

 1. Added: Some personal user experiences
    (https://vitalik.ca/general/2023/02/28/ux.html)
 2. Added: Goodbye Business as Usual: Rethinking My Career for the Climate
    (https://jereze.com/blog/goodbye-business-as-usual/)
 3. Added: Core Values Exercise: A Scientific Method for Achieving Life Goals
    (https://durmonski.com/well-being/core-values-exercise/)
 4. Added: On mindsets, mind shifts and wins
    (https://davestewart.co.uk/blog/mind-shifts-and-wins/)
 5. Added: Farewell to Black History Month from ChatGPT
    (https://philip.greenspun.com/blog/2023/02/28/farewell-to-black-history-month-from-chatgpt/)
 6. Added: Parallelize YouTube downloads
    (https://wejn.org/2023/02/parallelize-youtube-downloads/)
 7. Added: The Collection of Passenger Name Records for Counterterrorism – Dawudi.ch
    (https://www.dawudi.ch/2023/02/06/the-collection-of-passenger-name-records-for-counterterrorism-privacy-intrusion-or-effective-tool-to-combat-transnational-terrorism/)
 8. Added: Database Cryptography Fur the Rest of Us - Dhole Moments
    (https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/)
 9. Added: Game Asset Storage, Loading, Compression and Caching
    (https://ph3at.github.io/posts/Asset-Compression/)
10. Added: Meta Needs A Decade Of Efficiency
    (https://www.mbi-deepdives.com/meta2023/)
11. Added: Bing Chat is a Precursor to Something Legitimately Dangerous
    (https://www.simonberens.com/p/bing-chat-is-a-precursor-to-something)
12. Added: The Fake Product Market Fit
    (https://mertdev.dev/the-fake-product-market-fit)
13. Added: Essays : Jevons
    (https://www.vand.hk/essays/jevons)
14. Added: Generating 1 Billion Fake People with Julia
    (https://dimitarvanguelov.github.io/posts/fake-people/)
15. Added: Dangerously good product managers
    (https://mirror.xyz/jrm.eth/_WdQhoixfR0ld2JSvd_iKkcI7-87uQOShq1N-ak2P1k)
16. Added: Focus on things that don't change
    (https://www.dsebastien.net/focus-on-things-that-dont-change/)
17. Added: The Future of Mathematics?
    (https://youtube.com/watch?v=Dp-mQ3HxgDE)

Generation took: 00:10:34.0606464
 Maintenance update - cleaning up homepage and feed

---
## [halotroop2288/pokemon-hg-ss](https://github.com/halotroop2288/pokemon-hg-ss)@[18938d14d2...](https://github.com/halotroop2288/pokemon-hg-ss/commit/18938d14d2e17601a7130a130ca7a3e05e2cab51)
#### Wednesday 2023-03-01 23:28:17 by Caroline Joy Bell

Gender Neutral Text

Replaces:
- "his or her" with "their"
- "him or her" with "them"
- "he or she is" with "they are"
- "a boy or a girl" with "masculine or feminine"

---

