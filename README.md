## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-19](docs/good-messages/2023/2023-01-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,296,642 were push events containing 3,367,154 commit messages that amount to 250,299,850 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [agraef/purr-data](https://github.com/agraef/purr-data)@[597472e292...](https://github.com/agraef/purr-data/commit/597472e2927d8ca8ea0e826a260c642ba4b20e27)
#### Thursday 2023-01-19 00:02:12 by Albert Gräf

Windows packaging: GH-friendly OutputBaseFilename.

This makes my life less miserable when doing releases on the GH mirror,
because I don't have to manually edit the installer filenames before
uploading any more.

GitHub doesn't like blanks in upload file names, using dashes instead
makes uploading much easier and eliminates the need to zip the installer
before uploading. We also include a proper cpu architecture designation
(x86 or x86_64) in the output file name in lieu of the '(64 bit)' suffix
which causes trouble in GH uploads as well, because of the parentheses.

Note that this shouldn't affect the Gitlab CI since it looks for a
'Purr*.exe' build artifact, which will still match the package name.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[c58e40c27c...](https://github.com/git-for-windows/git/commit/c58e40c27c874433119fb9cc05c82d7b316b91c0)
#### Thursday 2023-01-19 00:28:10 by Johannes Schindelin

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
## [Teabone3/GameGuruRepo](https://github.com/Teabone3/GameGuruRepo)@[27d7493c1c...](https://github.com/Teabone3/GameGuruRepo/commit/27d7493c1cab486fb078210f1207ff347e6d5169)
#### Thursday 2023-01-19 01:04:50 by Teabone

Fixes Dying Effects (Heartbeat + Red Screen)

Multiple Fixes and Changes to Player's Dying Effect trigger:

Fixes issue causing dying effect when the player was barely hurt:

Previously if the player was ever hurt, even by 1 point of damage, the player would act as if he was dying. The screen would go red and a heart-beat sound would play repeatedly until the player finds a health item or regenerates health. This used to occur instantly because the player's main script was set to cause this effect whenever the player's health was lower than 100. So for example if your health was 99, your game would assume the player is dying and cause a heart beat sound to play and flash the screen red. This change sets to check if player's health is less than 50% of its set maximum in the editor. Meaning less than 50/100 or less than 150/300 etc for examples.

Fixes 100 points being assumed as the maximum health for all games:

The original player script was set to assume the player's maximum health would always be 100 points. It was not using a percentage system either. So even if you set the players health to 1000 (for example) if you get injured the dying effect would only play if the players health was 99 out of 1000. This changes the solid "100" value to "g_gameloop_StartHealth".

In short, the "annoying" heartbeat and red-screen flashes will only ever occur if the player's health is drastically lower than its maximum meaning you will hear it only when you are actually dying or majorly hurt. A highly requested change in the community over the years.

We could in the future perhaps add an user option in the start marker to change what percentage the health must be lower than, to play the dying effects. For example replacing the 2 with a variable that can be controlled in the start marker in editor. So you can control how much to divide the maximum health by to determine percentage.

 g_PlayerHealth >= (g_gameloop_StartHealth/2) )

* Please note this change does not remove the player blood decals on screen, that occur when the player is hurt. It only changes when to run the dying/near death effects (heart-beat and red transparency on the overall screen).

---
## [mullenpaul/tgstation](https://github.com/mullenpaul/tgstation)@[e766444468...](https://github.com/mullenpaul/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Thursday 2023-01-19 01:36:28 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[979b26d52e...](https://github.com/DesmontTiney/tgstation/commit/979b26d52e09dcaa7ad00ce07c1e16760dbd7cb2)
#### Thursday 2023-01-19 02:51:53 by tralezab

Unironically removes the atmos and black beret (#72722)

## About The Pull Request

Removes atmos berets

## Why It's Good For The Game
Berets shouldn't be thrown into every job, it's milsim circlejerking
dressup shit that creeps out of our milsim containment jobs (security)
and into other innocent jobs. There is absolutely no reason for this job
to have a beret just straight up. Can we add unique hats to the game,
not the same one recolored every way to Sunday? That's my problem. We
don't have unique clothes, we have a billion types of beret when the
BASE BERET TYPE has `IS_PLAYER_COLORABLE_1` so ANYONE can color it. So
again, why do we have the atmos beret? To clog the wardrobe, a vending
machine added specifically because we couldn't stop clogging the
original locker atmos techs spawned in?

The black beret has the same problem: recolored item when you can get
the item of any color

## Changelog
:cl:
del: Atmospherics beret and black beret
/:cl:

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[df737af4a0...](https://github.com/lessthnthree/Skyrat-tg/commit/df737af4a02b18388b293005c340a7a46423236e)
#### Thursday 2023-01-19 03:23:18 by SkyratBot

[MIRROR] *hand, or That /One/ Emote You Always Felt Was Missing [MDB IGNORE] (#18200)

* *hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

* *hand, or That /One/ Emote You Always Felt Was Missing

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[24735f961a...](https://github.com/kleinerm/Psychtoolbox-3/commit/24735f961a474f704fe74fa0656b5f8db932c005)
#### Thursday 2023-01-19 04:11:04 by Mario Kleiner

PsychOpenXR[Core]: Implement optional multi-threaded 2D presentation mode.

This for presentation in 2D (mono or stereo) presentation mode, where
one or two (supposedly) head-locked OpenXR quad_layers are used for monoscopic
or stereoscopic image presentation. Ie. no use of OpenXR projection_layers,
which always need permanent closed-loop head tracking to work. According to
spec, head-locked quad_layers should be head-locked, static wrt. to any head
movement. However, as it turns out, some runtimes, e.g., SteamVR on both Linux
and Windows, do not work well at all if an animation loop isn't constantly
running at full HMD framerate, even for quad_layers. Under SteamVR, these 2D
views jitter / vibrate / jerk around in an annoying and disorienting fashion
if the animation loop runs too slow, takes pauses and restarts etc., making
use of the HMD as a "strapped onto the head" mono monitor, or as a stereo
monitor for binocular presentation almost unbearable.

Behaviour on my machine darlene is as follows:

- Linux + Monado: Absolutely perfect! Static views as expected even for
  long pauses, IFI's, stopped script loops with no Screen('Flip').
  Monado is also the only system that respects the .displayTime target
  onset time specification as the spec requires.

  -> No need for extra action.

- Windows + OculusVR: Mostly works fine with static views, but in some
  cases one might get the "sandclock" warning, a black screen or a stuck
  script.

  -> Mostly no need for extra action, some timing hacks should do.

- Linux + SteamVR: Complete jittery/vibrating/jerking mess.

- Windows + SteamVR with output to Rift CV-1 via OculusVR runtime, ie.
  not using SteamVR's own VR compositor, but OculusVR: Gives static
  images as expected for stopped animation loops. But resuming a loop
  (or just having long IFI's which is the same as stop -> resume from
  the runtimes PoV) causes massive jerks and jumps.

  -> SteamVR on all OS'es needs help to get to acceptable results.

So, multi-threading to the rescue: This commit allows to optionally
enable a separate background thread which tries to runs the VR presentation
cycle at having at maximum HMD refresh rate, e.g., 90 fps for a Rift, all
the time, this way avoiding the animation loop from ever stopping or even
throttling from the XR runtime and compositor perspective.

We allocate and assign a dedicated OpenGL context (the one that Screen()
creates for use with its flipperThread, but which would go unused as the
flipperThread has no use for OpenXR sessions).

Startup of a session is always single-threaded on the main thread, to
get initial flips and sync-up with the XR compositor, getting to session
state XR_SESSION_STATE_SYNCHRONIZED <-> VISIBLE <-> FOCUSED, and the
initial set of framebuffer textures attached. Shutdown of a session with
final present is also done single-threaded on the main thread.

Full "head tracked 3D rendering" with a closed track -> do stuff -> render
-> present loop, and use of XR projection_layers is also done single-threaded,
as that only makes any practical sense with a tight renderloop implemented
in Matlab/Octave/[Python?] script.

The "2D" modes which use quad_layers and (usually) don't involve (or need)
head tracking and dynamic head pose driven fast closed loop rendering will
switch to multi-threading:

The thread runs in an infinite loop, doing xrWaitFrame -> xrBeginFrame ->
xrEndFrame cycles, resubmitting the same current most recently released
XR swapchain images each HMD video refresh cycle / compositor work cycle,
to keep away from client timeouts or throttling or stop->resume effects,
trying to kee the XR compositor happy.

The script, via Screen('Flip', win [, tWhen]) -> PsychOpenXRCore('PresentFrame')
will submit new rendered content as it wishes, with tWhen target present
time attached. In each work cycle, the thread checks predictedDisplayTime
for the upcoming xrEndFrame() call against tWhen. Iff
precictedDisplayTime >= tWhen, it is time to latch the new rendered stimuli,
by xrReleaseSwapchainImage() before the xrEndframe(), then acquiring new
swapchain images for the next user script render cycle.

predictedDisplayTime is used as best estimate of when the new stimulus
frame will show. An imperfect, and optimistic, guess, iow. returned
Screen('Flip') timestamps may be too optimistic, earlier than true
onset. However, as lots of testing showed, without a proper official
OpenXR timestamping extension, there isn't any way to do better than
that - It is what it is...

This now means we have two separate present code-paths for single (PresentExecute)
vs. multi threaded (PresentCycle) operation. And the need for locking and
condition variables for avoidance of race conditions, data corruption on
shared data, blowing up the OpenXR runtime, and separate OpenGL contexts
between main and XR thread, all with need for proper management and state
transitions. This is the rabbit hole of potential threading bugs in our code
and -- even more likely -- OpenXR runtime bugs, that i wanted to avoid going
down. But unfortunately not everything can be as well done as Monado, and
SteamVR is so far quite awful quality-wise as of January 2023, so here we
are...

-> WIP backup commit. Doesn't crash/hang/malfunction in any obvious ways.
   on Linux with Monado or SteamVR + Monado SteamVR driver plugin for the
   Oculus Rift CV-1. Not yet tested on Windows or with other HMDs.
   I'm sure it has remaining bugs, but this serves as a baseline.

---
## [haint126/obsidian](https://github.com/haint126/obsidian)@[30b430b142...](https://github.com/haint126/obsidian/commit/30b430b142a20cf0a0f3edc5295c5fec761c3975)
#### Thursday 2023-01-19 04:21:53 by haint126

Vault backup: 2023-01-19 11:21:46 : Lab

Affected files:
.obsidian/appearance.json
03_Life_experience/Books/Book to read/Giving speech/10 Books To Become An Amazing Communicator/10 Books To Become An Amazing Communicator.md
03_Life_experience/Books/Book to read/Others/10 books that changed my life/10 books that changed my life.md
03_Life_experience/Startup_Business building/Things I believe about making a living as an independent maker/Things I believe about making a living as an independent maker.md

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[c3a1f21c1a...](https://github.com/Zytolg/tgstation/commit/c3a1f21c1afc10bd5515114e0c6117ac73c87f62)
#### Thursday 2023-01-19 04:56:19 by MrMelbert

Converts blindness and nearsightedness to status effects, scratches some VERY dumb blindness handling that resulted in mobs becoming "incurably" blind (#72267)

## About The Pull Request

- Nearsighted is now a grouped status effect.
- Blindness is now a grouped status effect.
   - Eye handling of blindness has improved. 
- When eyes are removed, they now cause you to become blind, rather than
handling it in `update_tint`.
- Being ahealed no longer blinds you for one tick, meaning that black
overlay on aheal is gone.
- Temporary Blindness is now a status effect.
- Both Nearsightedness and Blindness have been exorcised from mob vars
and life chains. This means that we've finally cut 2 procs from life,
`handle_status_effect` and `handle_traits`, and moved both to event
based processing. Wooo optimizations.
- Swapped pacifism status effect to use apply and set helpers. 
- Removed an unused admin toggle that disabled welding helmet tint but
also tint from every clothing item and also blindness from losing your
eyes.
- Clothes now generally all blind their mob more consistently.
- Oculine, eye surgery, and sensory restoration are now no longer the
only way to fix blindness from eye damage. If your eyes are healed
through any other means, it will also heal your blindness.
- Some things that made you blind, such as ling blind sting, no longer
just flat made you blind from eye damage forever. They now cause eye
damage directly, which in turn makes you blind from eye damage, as
expected.
- Pacifists can't eyestab anymore. Eyestabs now have a limit on the
amount of blur applied.
- Refactored some `is_x_covered` procs to accept flags rather than have
a lot of arguments for some silly reason.
- Unit tests for blindness. 

## Why It's Good For The Game

Blindness was exceptionally poorly handled prior, primarily due to the
fact that it was tied to the mob instead of separated out

On top of that the system put a LOT of faith in proper handling of
blindness on the coder's end which was misplaced evidently. Many places
didn't update or handle blindness correctly, or just let people
perma-blind.

Deferring it to a status effect improves this a lot

## Changelog

:cl: Melbert
refactor: Refactored blindness and nearsightedness. Important to note is
that all mobs are naturally blind until their eyes are actually created.
refactor: Refactored "is covered" procs
fix: Less sources of blindness now cause permanent blindness. Includes
the "Blind" Spell and "Blind Sting" from changelings.
admin: Ahealing someone no longer flashes the blind overlay for 1 tick.
admin: I removed an unused (sort of) inaccessible admin verb that
allowed you to toggle the tint from all welding helmets (and clothing)
(and lack of eyes) in existence, let me know if you want similar back
balance: Changeling "Blind Sting" now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Visionloss virus symptom now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Oculine has been reworked slightly. Prior, Oculine arbitrarily
healed blindness and nearsightedness from eye damage reagrdless of how
damaged the eyes were, and applied blur on success. Now, Oculine just
heals eye damage, and blindness / nearsightedness is restored in the
process. There is now a probability every tick that eye blur is applied
based on how pure the oculine is while healing very damaged eyes.
balance: Pacifists can no longer eyestab.
balance: Any clothing item that covers your eyes contributes to getting
the bonus while sleeping, and to removing temporary blindness faster
/:cl:

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[7e7dd9b937...](https://github.com/crowlogic/arb4j/commit/7e7dd9b9376da1f00ecc655d41d05a9bb8dac149)
#### Thursday 2023-01-19 04:59:27 by StephenCrowley

https://www.youtube.com/watch?v=RFSWW4O6QNM

Ah
Well, well, well, well, well, well, well
Wow, wow, wow (hoo hoo hoo)
I was slippin' into darkness
When they took my friend away
I was slippin' into darkness
When they took, when they took my friend away
You know he loves to drink good whiskey (Wo ho ho ho)
While laughing at the moon
Slippin' into darkness
Take my mind beyond the dreams
I was slippin' into darkness, yeah
Take my mind beyond the dreams
Where I talk to my brother (Wo ho ho ho)
Who never said their name
Slippin' into darkness, yeah
All my trouble so I choose
I was slippin' into darkness, yeah
All my trouble so I choose
I got a wife and a baby, yeah yeah (Oh ho ho ho)
Now my love hath gained its fame, yeah
Slippin' into darkness, yeah
When I heard my mother say
I was slippin' into darkness
When I heard my mother say
Hey, what'd she say what'd she say
You've been slippin' into darkness (Wo ho ho ho)
Pretty soon you gonna pay, hey
Ooh, ooh, ooh, ooh
Ooh, ooh, ooh

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[1f049fce2a...](https://github.com/clintjedwards/gofer/commit/1f049fce2aed1cf173f2c22e737ba7664cc02280)
#### Thursday 2023-01-19 05:21:43 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[1b112b7ddb...](https://github.com/mattdway/CreateWithVR/commit/1b112b7ddb9eda32627be79de944d09f35fd4b41)
#### Thursday 2023-01-19 06:38:28 by mattdway

01-18-23 v2.9.1 01-18-23 Commit

Front door broke in the 12-31-22 v2.8.1 version of the project.  After a lot of troubleshooting and not being able to spot the issue I fixed this by reverting back to version 12-30-22 and then redoing all of the pieces from 12-31-22 and more.

I re-fixed the door button and the colliders by relinking missing items and moving the colliders back into place.

I found and deleted duplicate scripts and duplicate colliders for the doors that were part of the door prefabs I brought over from the 12-30-22 project and part of the 12-30-22 project itself.

All door items (manually opening and closing, opening and closing correctly using the door toggle button, deactivating the front door collider that prevents the player from running into that door with physics and that offers the same pushback script/mechanic as the walls in my project) all work perfectly again.  Some of those door colliders were in the middle of the room and were preventing the raycasts from reaching the main menu.  Moving these back into place also fixed this issue.

I wrote and added a script for all five cabinet doors and the cabinet drawer to freeze both the x, y and z position and the x, y and z rotation when collisions occur.  My first script used the OnTriggerEnter and OnTriggerExit methods with a tag check but I later changed this over to use the OnCollisionEnter and OnCollisionExit methods so that I didn't have to make my colliders "Is Trigger," which defeats the purpose of having a collider with physics hands and that also couldn't be applied to all parts of the drawer, else items would fall right through it.  I also added a "Wall" tag to all my cabinet doors and drawers so that these also offered the same pushback as the walls and front door when leaning into just a cabinet door or drawer.  This prevents any sort of breaking of the hinge joint or rubber banding effect with collision.

I found my two Unity videos and my Super Mario World video were present but corrupt in the rebuilding of my project to the 01-18-23 build.  So I grabbed those videos from a past build on my external USB HD and I copied them back over to the current project.  I tested all three videos and this worked.

I fixed the tablet black attach point so that this had both the correct orientation (not upside down) but also not close to the body, at the same height as the hand, but also tilted back slightly for easier viewing of the videos on the tablet.

I fixed the "Matt's Photos" red pushpin that was stretched to unrealistic proportions to make this look more like the object it is, a pushpin.

I double checked the Bon Apatite sign to make sure this was readable (I had apparently fixed this prior to my 12-30-22 commit by making this text larger and making sure it wasn't stretched via the scale and adjusting the font color and font properties), but I couldn't find mention of this in my previous log, so I might have forgotten to note that previous change.

I added random sounds to my Dalek figure, just because I could. :-D  When you pick up the Dalek and activate (press the trigger on the VR controller) a random Dalek clip plays (out of ten total).  I was going to write my own script to play random sounds but Unity had included their own in the CreateWithVR course so I just ended up using it instead.

I fixed the attach transform for the dart gun (as it was being picked up and pushed/clipping through where the body would be and tilted upward.  I changed this so it's straight and away from the body.  
I added an attach transform to the Dalek so that when you pick it up, it's facing you.  Pressing the trigger button plays a random clip of about 10.  
 
I fixed the magnifying glass so that it now magnifies either direction.  There's an attach transform on it so you have to sort of bend your wrist to see the other side but before it was like a mirror (showing what was behind you) on the backside instead of being identical to the front side.  I also fixed the magnification so that it magnified more without clipping through the wall and showing outside the room.

I wrote a script using OnCollisionEnter and OnCollisonExit for the watering can so that whenever the watering can collides with one of about four or five tags (which includes Floor, Furniture, and Untagged, and several others) the watering can's X and Z rotation are set back to zero while the Y rotation stays the same.  This is so when the watering can is thrown or set down it doesn't continue to play the audio glugging sound as well as play the water pour particle animation.

I added attach transforms to the Bon Apatite sign and to the Polaroid Camera for proper rotation and position when holding these items.

Every interactable was play tested tonight, as well as the scene changes, and everything is working well in this version.

To Fix Next:

Writing a script for the Water Bottle Flip Challenge to detect when there is a floor collision with either the top, sides or bottom and to play a corresponding sound when that happens.

Determine why my physics hands can clip through the dinning room table and chairs when at a fast enough speed. Try and make this work more like the couch or outside colliders. Test with other furniture to see if anything else in the room allows this to happen. Compare and contrast to troubleshoot.

Thin items like photos from the polaroid camera and my punch list sheets are still sometimes getting stuck under the floor and I need to troubleshoot that more to try and fix.

Updating the Interactive board and/or punch lists.  I'm running out of room on my punch lists and I have no more room to add additional punch lists, so I'll have to decide how I wish to use these moving forward.  I still love the idea of having bugs and/or future features viewable in VR and I have a lot of future ideas (both from ideas I've come up with and that my students have come up with that could be added).  I'm about 1/3 of the way through laying this out but moved onto other parts of the project - just because of the amount of work involved and in not knowing if everything will fit or what the end result of this may look like.

If I get that working I feel like I have a lot of the bug pieces for all the current items added to my room fixed. I'll have to go back to my bug list to check to be sure, but off the top of my head there aren't any others that are coming to mind that I need to fix.  At this point I may choose a new feature to add to this room, just to continue my (and my student's) learning.
@mattdway mattdway committed on Jan 18

---
## [BlockBuilder57/bf2mods](https://github.com/BlockBuilder57/bf2mods)@[68a21e70d9...](https://github.com/BlockBuilder57/bf2mods/commit/68a21e70d93f488a44f8fb7693126838bc02511f)
#### Thursday 2023-01-19 06:44:19 by modeco80

skylaunch: Make TcpLogger use select() & support multiple clients

This was really annoying to do but it's a lot better than how it was before. There's now another event loop thread which uses select() and the fdset mechanism for handling multiple clients. Far cry from any C10K awards, but it's better than accepting once and never again

This kind of breaks using the skylaunch legacy TCP logging in emulators for now though because it seems like neither yuzu nor Ryujinx support nonblocking sockets, which kinda sucks :(

The code does work on real hardware though, which at least helped me not go completely insane writing it.

---
## [tomorrowindia/New-Laptop-Launches-In-2023](https://github.com/tomorrowindia/New-Laptop-Launches-In-2023)@[0f8ae995e8...](https://github.com/tomorrowindia/New-Laptop-Launches-In-2023/commit/0f8ae995e81bbd0de605d19f5a477b7c2289b559)
#### Thursday 2023-01-19 06:53:24 by Tomorrows India

Update New launch product

Web development is becoming increasingly common. As a result, you must own a top-notch laptop to meet your business needs. The ideal RAM, CPU, screen size, and laptop for a web development must have these components. They are typical components of performance reviews
After purchasing the course materials for web development, you can also join. In this article, we will mention the features of new launch laptops that you must look for before purchasing a laptop. Pay attention to the helpful information below!

1. Thunderbolt 3 and USB Type-C ports. 
Everyone adores USB, the common connector that powers devices like cell phones and tablets, transfers data to flash drives, and connects you to practical docking stations.

2. Screens with a higher resolution
Today, you can buy a reasonably priced system with a 1920 x 1080 resolution screen or greater, allowing you to view more of your work at once and watch movies how they were intended to be seen.

3. OLED Screens
The greatest phone screens now available feature OLED displays that provide well over 100 per cent of the sRGB colour spectrum, making images on the panel look better than in real life. Examples of these phones include the Samsung Galaxy Series and Google Pixels.

4. Kaby Lake CPUs by Intel
The top producer of computer chips, Intel, recently updated its processors to a new generation. These CPUs, which go by the codename Kaby Lake but are part of Intel's 7th Generation Core series, offer far longer battery life and the capacity to play 4K video and be considerably faster than the one in your three-year-old laptop.

5. SSDs  (PCIe x4 a Plus)
Your laptop, which is four years old, most likely has a mechanical hard drive. SSDs are more than 300 per cent faster than traditional hard drives, completely altering how you use computers. An SSD enables you to start your computer more quickly, wake it up from sleep nearly instantly, and launch your preferred applications more quickly.

Here are the top three laptops you can consider for 2023

1. Best Premium Pick: Lenovo ThinkPad P1 Gen 2
With a 15.6-inch Dolby Vision 4K OLED display, the Lenovo ThinkPad P1 is a competent mobile workstation and a fantastic laptop for full-stack developers. It is perfect for web design since it can display more realistic colours than the human eye can see.
Pros:
Several connectors.
A stunning 4K display.
A comfortable keyboard.
Produced from sturdy, high-quality materials

2. Best Budget Pick: Acer Aspire 5
The Acer Aspire 5 is a great laptop for people who need to use a laptop all day (or night!) and is the finest option for front-end developers. Acer True Harmony technology, built into this laptop, provides greater audio with deeper bass and louder loudness.
Pros:
Budget-friendly.
Simple to update and configure.
Fast switching between programs/apps.
Screen resolution in high definition

3. Laptop Lenovo IdeaPad 3
Given the difficulty involved in site design and development, you should have the best laptop for web development in 2023.  This laptop has multiple advanced features than that of its earlier models.
Pros:
Smooth operation.
Ergonomic planning.
Rapid internet access.
There is a lot of storage space.
innovative cooling system

---
## [cspiegel/garglk](https://github.com/cspiegel/garglk)@[dd59906d33...](https://github.com/cspiegel/garglk/commit/dd59906d33d36a41bfac288096cb48723691b7bb)
#### Thursday 2023-01-19 07:24:07 by Chris Spiegel

Check more than style_Preformatted for monospace

The Agility interpreter uses styles User1 and User2 for monospace, but
Gargoyle only considered style_Preformatted, meaning that Gargoyle
assumed user styles were _not_ monospace, and translated hyphens into
em- and en-dashes.

Since Gargoyle knows which font type a style maps to, use that
information instead of checking the style directly. This will work if
interpreters use User styles, or if they change the appearance of other
styles via hints.

As noted in the comment, this assumes the user has properly set a
monospace font. If a proportional font is set as the monospace font,
Gargoyle will still assume it's monospace, because it's "supposed" to
be. This is at odds with how ligatures are done: there, the font file
itself is examined and if it's monospace, ligatures are disabled.

I think these differing approaches make sense: Here, with dashes, if a
user sets a proportional font as the monospace font, it hardly matters
whether the hyphens become em- and en-dashes, given that the width of
the glyphs is variable anyway (i.e. box drawing is hopelessly broken if
you set a proportional font, so changing hyphens is a drop in the
bucket). And if a monospace font is set as the proportional font, yes,
it'll get em- and en-dashes, but that's fine, since the width of the
characters, at that point, can't be expected to be fixed, given that it
_could_ be a proportional font. It will be a slightly degraded
experience since it won't be obvious it's a longer dash, but then, if
you're setting a monospace font everywhere, you can turn off dash
conversions.

As for ligatures, if the user sets a monospace font for the proportional
font (which is perfectly fine), the ligatures would look pretty silly,
especially the three-character ones. For example:

    Oﬀice
    Ofﬁce
    Oﬃce
    Ofﬂine
    Oﬄine

---
## [ferdrich-kunbus/linux](https://github.com/ferdrich-kunbus/linux)@[adee8f3082...](https://github.com/ferdrich-kunbus/linux/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2023-01-19 07:25:52 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[66b7310039...](https://github.com/Rustybuckets6601/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Thursday 2023-01-19 07:36:32 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[0ad051ed3b...](https://github.com/Mu-L/crawl/commit/0ad051ed3b7deee9383e0b7a7b666411275f9e51)
#### Thursday 2023-01-19 09:00:37 by Nicholas Feinberg

New unrand: the consecrated labrys

Players have often asked: we have demon blades, demon tridents and
demon whips, but why no demon axe? Of course, those wise enough to
peruse the source code will know we've always had a demon axe - the
obsidian axe. Now we have the blessed version!

The consecrated labrys is a +5 holy broad axe (with +1 base damage,
like other blessed weapon types) with sInv, Flight, and a gimmick -
it gets bonus enchantment as scarier enemies come into view, working
via the same threat mechanic as Ru's Sacrifice Courage. To discourage
aggressive swapping, it also has Fragile, and for pleasantness, it
caps out at +27 enchant. That might be too high, truthfully, but let's
give it a shot - we can revisit scaling after folks play around with
it a bit.

S/o to bitdizzy for suggesting the ego effect.

---
## [owi92/tobira](https://github.com/owi92/tobira)@[2a9add1e61...](https://github.com/owi92/tobira/commit/2a9add1e615f0c545f7aa1a6e2aea0b0820d9de6)
#### Thursday 2023-01-19 10:01:14 by Lukas Kalbertodt

Add framework for authentication (authkit) and use it for local dev setup & test deployments (#645)

Closes #550 

See the referenced issue for motivation. Can be reviewed commit by
commit, but reviewing all in one isn't bad either.

As you can see from the changes, our framework does more than the
previous `login-handler.py`: it sends the `POST /~session` request to
Tobira itself. That means no `X-Accel-Redirect` magic is needed, making
the nginx simpler.

The main part is done, but this is still a draft for a number of
reasons:
- [x] Decide on name and scope for the NPM package. ->
`@opencast/tobira-authkit`
- [x] We want to potentially also implement `auth.mode =
"opencast-users"`. In that mode, Tobira would handle `POST /~login`
requests itself by just asking Opencast if the login data is correct.
That should be fairly easy to do. And I think it's very useful: it's
_the_ obvious auth system Tobira should support and I assume quite a few
institutions want to use it. Further, even if an institution wants a
different auth system in the long run, just using Opencast users is a
very simple way to get everything running. Without auth system, you only
see an empty Tobira which is quite underwhelming. So this would
drastically improve the "first setup" experience IMO.
- [x] ~~I also noticed that we might want to simplify login handlers
even more by adding yet another mode. In that mode, Tobira would forward
`POST /~login` requests to a configured HTTP service which would send
back appropriate auth headers. This is little work in Tobira and that
way, the nginx config could be a lot smaller still, again making it
easier to set up Tobira.~~ -> I still think it's useful, but we won't do
it now.
- [x] Once all the previous points are decided: update docs
appropriately. -> Done with NPM package name `@tobira/authkit` for now.

So yeah, I'd like to talk about the two additional auth modes and
whether we want them. Of course they could be implemented in a separate
PR. But it would also be nice to only needing to rewrite the docs once.

---
## [EmbarkStudios/boh](https://github.com/EmbarkStudios/boh)@[72bb3a4e16...](https://github.com/EmbarkStudios/boh/commit/72bb3a4e167f1f7af26d620bbd06767966569f96)
#### Thursday 2023-01-19 10:48:25 by Jake Shadle

Add kubectl rollout restart (#2)

This adds a `boh kubectl rollout restart deployment/<blah>` command as
it is literally the only thing we used kubectl for, and because of the
incredibly lame dependency of the GKE auth plugin on gcloud (fucking
ridiculous 600+MiB install size) as well as removing the need to have
python!?!?!?! Beyond pissed at this garbage fire.

Unfortunately, this means using openssl instead of rustls, due
to...[reasons](https://github.com/kube-rs/kube/issues?q=is%3Aopen+is%3Aissue+label%3Arustls).

---
## [scott-d-bowen/prboom-plus](https://github.com/scott-d-bowen/prboom-plus)@[051c4a5222...](https://github.com/scott-d-bowen/prboom-plus/commit/051c4a5222fcb21df11f50f154036ce1196ea6ed)
#### Thursday 2023-01-19 10:52:10 by Fabian Greffrath

add support for colored blood and gibs (#182)

* add support for colored blood and gibs

Due to popular demand. :wink:

* use P_SetTarget() instead of editing the target value directly

* introduce a new mobjflag instead of misusing the mobj->target pointer

* set flags more consistently

If MF_COLOREDBLOOD is set and none of (MF_TRANSLATION1|MF_TRANSLATION2)
this means green blood (Baron of Hell / Hell Knight) and if
MF_TRANSLATION1 is additionally set this means blue blood (Cacodaemon).

This allows for up to 4 different blood colors once MF_TRANSLATION2 is
also taken into account. Let's see what we come up with...

* add comments

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[6c065f72b8...](https://github.com/git-for-windows/git/commit/6c065f72b8d581eee53ab82e82da049ee492bf11)
#### Thursday 2023-01-19 12:17:10 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [hwchase17/langchain](https://github.com/hwchase17/langchain)@[917ce074ed...](https://github.com/hwchase17/langchain/commit/917ce074ed82b427b831e83ebeaeafdde2f8710d)
#### Thursday 2023-01-19 15:06:39 by Enrico Shippole

Add Bing Search API Wrapper (#653)

Hi @hwchase17,

We had previously spoken about alternative search engine integration to
SerpAPI. Following the Google Search Wrapper Utility, I have implemented
a utility to use Python to call the Bing Web Search API. This Bing
Search Wrapper produces a similar programmatic response using REST and
Python to the Google Search Wrapper. Currently, the Python SDK for
Microsoft Azure Web Search API seems to have numerous issues open so
this is the support team's official recommended approach until it is
fixed. I am still working on the full chain from our previous discussion
though but thought this would be useful in the meantime.

Usage:
```python3
import os
os.environ["BING_SEARCH_URL"] = ""
os.environ["BING_SUBSCRIPTION_KEY"] = ""
wrapper = BingSearchAPIWrapper()
wrapper.run("python")
```

Output:
```
Thanks to the flexibility of <b>Python</b> and the powerful ecosystem of packages, the Azure CLI supports features such as autocompletion (in shells that support it), persistent credentials, JMESPath result parsing, lazy initialization, network-less unit tests, and more. Building an open-source and cross-platform Azure CLI with <b>Python</b> by Dan Taylor. Learning. Before getting started, you may want to find out which IDEs and text editors are tailored to make <b>Python</b> editing easy, browse the list of introductory books, or look at code samples that you might find helpful.. There is a list of tutorials suitable for experienced programmers on the BeginnersGuide/Tutorials page. There is also a list of resources in other languages which might be ... The core of extensible programming is defining functions. <b>Python</b> allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. More about defining functions in <b>Python</b> 3. <b>Python</b> is a programming language that lets you work quickly and integrate systems more effectively. Learn More. <b>Python</b> is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. <b>Python</b> is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. This module is part of these learning paths. Build real world applications with <b>Python</b>. Introduction 1 min. What is <b>Python</b>? 3 min. Use the REPL 2 min. Variables and basic data types in <b>Python</b> 4 min. Exercise - output 1 min. Reading keyboard input 3 min. Exercise - Build a calculator 1 min. With <b>Python</b>, you can use while loops to run the same task multiple times and for loops to loop once over list data. In this module, you&#39;ll learn about the two loop types and when to apply each. Manage data with <b>Python</b> dictionaries. <b>Python</b> dictionaries allow you to model complex data. This module explores common scenarios where you could use ... <b>Python</b> is a popular programming language. <b>Python</b> can be used on a server to create web applications. Start learning <b>Python</b> now ». <b>Python</b> is an easy to interpret and high-level object-oriented programming language with easy-to-read syntax. Ideal for prototyping and ad-hoc tasks, <b>Python</b> has wide use in scientific computing, web development, and automation. As a general-purpose, beginner-friendly programming language, <b>Python</b> supports many top computer scientists and ...
```

Thank you,

Enrico

---
## [Guatolipo/S.P.L.U.R.T-Station-13](https://github.com/Guatolipo/S.P.L.U.R.T-Station-13)@[7d6bc725c2...](https://github.com/Guatolipo/S.P.L.U.R.T-Station-13/commit/7d6bc725c23c68a3b399c66c0e24e1647315983d)
#### Thursday 2023-01-19 15:22:15 by Guatolipo

Alt title additions and removals

Added new alt titles to EVERY job that I could, removed the shitty low-effort ones, like blahblah-slut. Also trying out alt silicon titles, not sure how it'll work with the AI latejoin announcement. I think it'll not affect the latejoin, but it'll appear as the alt title in the crew manifest. I have literally no coding experience, but i'll figure it out somehow. Still don't know how to gametest, if you know how, message me at guato#1993 on discord.

---
## [martinpitt/cockpit](https://github.com/martinpitt/cockpit)@[2654169f3f...](https://github.com/martinpitt/cockpit/commit/2654169f3f99980401d970bd992726c0493abecd)
#### Thursday 2023-01-19 15:58:35 by Martin Pitt

python: Respect umask in fsreplace1

NamedTemporaryFile always creates files with 600 permissions, thus
making e.g. /etc/motd unreadable for users (which breaks
TestSystemInfo.testMotd).

Unfortunately there is no good Linux API for atomically replacing a file
as user:

 * mkstemp() and friends create too tight permissions.

 * chowning the file after writing would be fine, but Linux has no API
   to get the current umask other than scraping it out of /proc (and
   calling umask(2) twice is a race condition and ugly).

 * open(O_TMPFILE) would be cool, but (1) it's not supported on some
   file systems (e.g. not on overlayfs or NFS); (2) at least Fedora
   enables /proc/sys/fs/protected_hardlinks by default, so that the
   documented linkat() trick fails with EPERM, as unprivileged processes
   don't have CAP_FOWNER; and (3) does not work with existing files [1].

So, move to the same stupid "Find a free file name ourselves" approach
that the C bridge does, but use a random 6-character string instead of
just counting to 1000.

[1] https://patchwork.kernel.org/project/linux-fsdevel/patch/c823982d5b46ea888dc1fdf26c067a7aa0f3585f.1490103963.git.osandov@fb.com/

---
## [reneeb/perl5](https://github.com/reneeb/perl5)@[fe5492d916...](https://github.com/reneeb/perl5/commit/fe5492d916201ce31a107839a36bcb1435fe7bf0)
#### Thursday 2023-01-19 16:57:24 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at
the very least. Given that the perl internals code is somewhat poorly
abstracted from the regexp engine, with parts of the abstraction leaking out,
I think this is acceptable. If we want to make plug in regexp engines work
properly IMO we need to add some more hooks that they need to implement than
we currently do. For instance mg.c does more work than it should. Given there
are only a few plug in regexp engines and that it is specialized work, I
think this is acceptable. We can work with the authors to refine the API
properly later.

---
## [akshaykamath45/CP](https://github.com/akshaykamath45/CP)@[ded8e001c0...](https://github.com/akshaykamath45/CP/commit/ded8e001c0212a56fb8be768ba5abc8ccd7889f5)
#### Thursday 2023-01-19 17:53:00 by Akshay Kamath

Watermelon(P1)

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

---
## [Miiyo/android_kernel_sony_sdm845](https://github.com/Miiyo/android_kernel_sony_sdm845)@[68bdfdde5d...](https://github.com/Miiyo/android_kernel_sony_sdm845/commit/68bdfdde5df676360ee63a2807953b1f0c500889)
#### Thursday 2023-01-19 17:53:02 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [amtoine/wiresmash](https://github.com/amtoine/wiresmash)@[10f8a0c4a9...](https://github.com/amtoine/wiresmash/commit/10f8a0c4a9ffef0ee7280bded0e63006c684cca7)
#### Thursday 2023-01-19 18:25:20 by Grégory Brivady

V0.1.0 - First working demo with cleaned up code (#2)

### **EDIT :** no need to check memory leaks, will be adressed
separaretly


The PR to start anew on a cleaner basis, finally! 

Main goal of _after_ the PR is to scale the project, add new nembers to
the team, and start working on funnier stuff ✨

Lot of work still left to do, and some pretty ugly code/tape still
running in some places; but should be mostly okay to build on.
Two aspects need to be adressed: a technical one, to make sure the code
is ready to be merged, and a more subjective one, as we should use this
milestone to check that the conception is going in the right direction.

**If you only want to make sure everything is working, simply go
throught the _Technical section_. If you want to know more about how
everything works, read everything. Everyone read the last words tho!**

# Project structure

Headers file are in the include folder, source code in src. CMake files
are recursive to each folder to prepare for the complexity of the
project structure. Executables are built to the bin folder - not
included in the git repository.

## Game, Engine, Graphics, Others

I have tried to separate source files in three big folder. The goal is
to split as much as possible each "main system", so we have the option
in the long term to create independant projects and reuse separate
components on other projects.

### Engine

Should contain most of the generic, engine-type stuff. A lot of virtual
classes, the physic engine, and most of the internal logic of the
project.

### Game

Everything that will be game-specific, ie game characters, Entity class
implementations, components implementations, ...
The dev folder give the "spirit" of what should go there.

### Graphics
Not to be a focus for quite some time! Everything fancy that will be
required down the road, including f.e. texture loading, more advanced
displaying, maybe particles, ...

### Others
Currently only keybind loading. But we should probably put there saving,
preferences, options loading as a whole, etc...

# Technical

The following _technical_ things need to be checked before we proceed
with the project:
- **Readme is clear enough**
- **build instructions are correct and clear enough**
- **building works on other platforms** (ie Linux), other compilers...
especially important since ideally, a lot of people are going to work on
the project
- code is clear and clean enough;
- **and** documented enough to be understandable
- **POTENTIAL MEMORY LEAKS**
- _not required_, but look at access control if possible

I believe items in bold are the minimal requirement to accept the PR,
the rest is "somewhat" secondary.

Some precision on code clarity and "cleanliness": everything that has a
**TODO** attached is _not_ meant to be adressed with this PR. We can
still discuss it ofc, but they will be adressed afterwards as issues,
for the following reasons:
- Some stuff require a lot more conception and work, and will stay as-is
for now;
- Some other stuff could be excellent entry-point for new members into
the project, especially for the first years with minimal OOP knowledge.

# Conception

On a more subjective point, we should take some time to discuss whether
or not the project is flexible enough to be build on.
This will require a lot of discussion (that we will keep out of this PR,
unless you see an obvious flaw that can be fixed), but it would be nice
if everyone could think a little bit about this while reviewing the
code.
To help with this, I have attached an elided UML of the current state of
the project at the end of the PR.
I try here to brief on all the subsystems.

## Graphics/Display

Prettry straighforward. Straight pipe between the engine and the SFML
library

## Box

System that will handle intersection of shapes. Currently used for
collisions, soon to be used for the combat system (hitboxes and
hurtboxes f.e.). Only implements rectangles as making several shapes
interacts is a big headache, and is not exactly required as of today.

## Physics

Contains a simple gravity to make objects fall; and a not so simple
subsyste,

## Input

Simply translates keys to entity movements. Very very basic, lacks a lot
of stuff including a jump subsystem, proper buffering of input,
animations, etc...

## Universe Master

I think this is the strongest point of the conception. I believe the
code illustrates by itself the beauty and simplicity of
addind/removing/updating component to the game.

## Entity

Keystone of our Entity-Component-System, yet I fear it is already
outdated. Please pay attention to this class in particular and think
about way to further separate the entities and the components that I
find currently too linked.

## UML diagram

Not complete, lacks a LOT of methods, attributes, access control...


![ClassDiagramAll_22_12_04](https://user-images.githubusercontent.com/12777915/205471348-6b4cb7d8-e1cb-44cd-a282-55e3972c4bc1.jpg)

# Last words

Quite some work done, but more to come! 
Thanks everyone for thrusting me with the project cleanup, and sorry it
took so much time to get there

But I believe the "fil rouge" will finally start for real, 1 year after
we quicklaunched it!

Very lenghty PR, but I think it is coherent with the amount of
modifications. If I forgot something, or you want to do some remark on
the PR (content, form, ...) don't hesitate to do so.

Co-authored-by: Clement <mabileau.clement@gmail.com>
Co-authored-by: Benoit Tellier <benoitprm@pm.e>
Co-authored-by: benoit <tellierbenoit@hotmail.fr>
Co-authored-by: matt <bassetmatt@gmail.com>
Co-authored-by: Xawav <real.xavier2001@gmail.com>
Co-authored-by: alex <alexandre.tullot@gmail.com>
Co-authored-by: Akainoru <PIXELtmGamer@gmail.com>

---
## [CERT-Polska/mquery](https://github.com/CERT-Polska/mquery)@[e832f51fb3...](https://github.com/CERT-Polska/mquery/commit/e832f51fb3e9475ef959d92e7c0944ecf1598451)
#### Thursday 2023-01-19 18:32:30 by msm-code

Use rq as a task scheduler for daemon. (#317)

Mquery demon is getting unmaintainable. Early daemon was a trivial piece of code, and using redis queues directly as a RPC mechanism was the easiest solution. Since then mquery got extended with (in
no particular order) batching, users, jobs, commands, task cancellations,
distributed agents, configuration, and more.

Case in point: subjectively (and I think my opinion matters in that regard) there are more bugs in 350 LoC daemon.py than in the whole rest of this repository combined.

We can keep digging that hole, or do something about this. I don't plan to rewrite the backend to another database, but at least we should use a better task queue than rolling ad-hoc our own one.

So this PR is a work in that direction. So far it looks very promising: hopefully we'll see big readability, stability and correctness improvements.

A few notes:

* This took longer than I expected, but was more fun than I expected. Rq is pretty neat and now I'm more sure of my code.
* Originally I wanted to do absolutely no changes to app.py, just db.py and daemon.py (to stop myself from doing more changes than necessary for my goal). In the end I couldn't stop myself from small refactoring - I've changed the JobId object to just string alias, and removed its uses from app.py. I've also changed a few parameter names. That's all. (Maybe I have a poor impulse control)
* I've added some comments to unrelated functions in the db. I've also documented data stored in the redis.
* A lot of the code is copy&pasted, but it's not clear from the git diff.

Overall I'm happy with this change and I think we can merge it.

Co-authored-by: Michał Praszmo <michalpr@cert.pl>

---
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[d30cba58c0...](https://github.com/zerbina/nimskull/commit/d30cba58c0c2c8bc353f51240f84eadaf19ebdc5)
#### Thursday 2023-01-19 19:50:17 by Saem Ghani

Extract nkError diagnostics data

`nkError` has a `reportId` which unfortunately opens any possible
"report" crawling its way in there. This commit introduces a new
design where `nkError` owns it's diagnostic data, as well as,
`ast_types` where `nkError` and friends are defined, owns the data
types. `Report` and all the associated cruft now is there simply to do
rendering.

`Report` still handles, routing and final consolidation, but in future
developments that will likely evolved further.

Overall Change:
- AST/Sem drop `ReportId` and associated memory leak
- AST/Sem now define a diagnostic type and are primary data owners
- `Report` is now used in legacy situations and rendering, the former
    is to be addressed in future commits

What didn't change/major caveats:
- `structuredReportHook` still uses `Report`, this consequences...
- `concept` and `{.explain.}` related erros have regressed, their tests
    marked with known issue, as this isn't a full conversion
- diagnostics involving magics, have inconsistent rendering, a pre-
    existing issue, sorting this out is future work

Lessons and Takeaways
=====================

Each module should own/define the data types that it's fundamentally in
charge of. Modules which are effectively components, like `lexer`,
`parser`, `vm`, etc, should produce diagnostics, events, telemetry,
whatever and their caller should handle output/rendering of these. The
key part about that last point is that the renderer and its format must
not be pushed into these modules, rather the renderer should consume
what they produce (directly or via an intermediary/translation).

For those wondering about why a value type was use inside the `nkError`
instead of the current `ref object`. I ran 3 bootstrap runs with each
version of `nkError`, and with the `TAstDiag` (value type) was
consistently ~10% slower during the bootstrap process.

|run|type|real|user|sys|
|:----|:----|:----|:----|:----|
|1|pastdiag|28.675|27.056|2.527|
|2|pastdiag|28.184|26.663|1.372|
|3|pastdiag|28.276|26.682|1.446|
|1|tastdiag|31.562|29.245|3.236|
|2|tastdiag|30.453|28.413|1.871|
|3|tastdiag|30.368|28.311|1.896|

|type|real|user|sys|summary|
|:----|:----|:----|:----|:----|
|pastdiag|28.38|26.80|1.78|avg|
|tastdiag|30.79|28.66|2.33|avg|
|pastdiag| 0.20| 0.17|0.50|avg dev|
|tastdiag| 0.51| 0.39|0.60|avg dev|

The report data types are rather bloated, eg: using `Int128` for
enum `high`/`low` values.

For diagnostics, it's best to capture very little data, and then query
within the rendering layer. Temper this where querying is reproducing
complex analysis, reconstituting heavy context, or keeping data large
data sets alive just so it can be queried later.

It's very possible we don't clean-up the symbol table of abandoned
analyses. This likely results in space leaks, or rather an overhead
while processing each module.

This style of conditional `0 < foo` is forbidden, it's just not
accessible code and prone to reasoning and ultimatley logic errors.

When doing inline error state representation in a data type, such as
`TLineInfo`, where the invalid state is
`TLineInfo(line: 0, col: -1, fileIndex: InvalidFileIdx)`, the default
initiatlization of objects is not our friend. This became a minor issue
during `nkError` construction. Where the line info on the provided
`wrongNode: PNode` parameter might be invalid. Hard to say, as the
default initialization is technically a valid location. A heuristic was
put into place to work around it and I think it'll hold until we fix it
properly. I see this as a language design problem, now one could argue
that a better selection of invalid state is required, but when working
in a retroactive case such as this, it's a non-starter. Furthermore, the
ergonomics of `{.requiresInit.}` leave much to be desired. I'm not sure
what exactly the answer is, but I think this is the difference between
something very primitive like a `struct` vs an actual `object`.

A number of node consts sets in `ast_query` and related modules are not
defined as compositions of each other. This can easily lead to changes
that only impact partial parts of the compiler and introducing yet more
bugs. This might be worth of a compiler style guide remark.

Just like a large amount of imports is likely a source of issues, so are
broad exports, avoid these like the plague. Removing these from
`reports` and related modules resulted in a number of significant and
hard to debug errors -- first encountered within CI, via a `bors try`.
They manifested as a doc gen build failure, which was seen as an
undefined symbol error. All because `reports` and friends were
exporting large swaths of other modules, eg: `ast_types`. After much
debugging and fixing error diagnostics to provide recursive dependency
detection as part of those unindentifier errors, it was fixed. It wasted
an entire day. Exports just create massive public surfaces, don't do it.

Details
=======

Finally, this commit impacts a very wide swath of the compiler, lots of
code had to be updated, along with many stylistic fixes. What follows is
a list of more detailed changes, in no particular order:

`ast_types`/`nkError` higlights:
- defines all its own diagnostic data types for `nkError`
- design-wise, `nkError` nodes are now much more likely to contain the
  immediate ast they're taking the place of, like a true wrapper. This
  should allow for easy recovery by simply getting `n.diag.wrongNode`.
- call mismatch related types (`SemCallMismatch` and `SemDiagnostics`)
  moved to `ast_types`
- moved `NodeId` into `ast_types from `packed_ast`, so it can be used
  more broadly, such as in `PAstDiag` as mentioned above.
- Removed `ReportID`, instead `PAstDiag` uses the `NodeId` of the first
  error node they're embedded in` as their `diagId`. This is an easy way
  to have a monotonic sequence, while also some correlation between diag
  and error node. Due to copies, the `diagId` and `PNode` `id` can
  diverge, but that's useful information in and of itself.

`ast` procs like `newNode` no longer have to care about `sons` on
`nkError` nodes, this also stops accidental traverls.

`ast_query` literal node kind `const` as sets
  Now, various const set ranges relating to literals were defined
independently, now only the smallest sets are, while bigger sets are
defined based on the smaller sets. Going forward, this should ensure
adding new node kinds updates all broader ranges.
  means: `nkLiterals* = nkIntLiterals + nkFloatLiterals + nkStrLiterals`
  Extracting a style guide remark out of the commit message would be a
good idea.

`msgs` now bridges translating `PAstDiag` to legacy `Report` for routing
and rendering. Although, routing should probably not be part of `Report`
stuff.

Moved illformed ast message creation routines earlier in `msgs` to
reuse them when generating legacy report message strings. String
generation should move to a rendering layer in the future.

More consistent VM/Gen event to AST diag mapping, mostly within
`compilerbridge` which now has simplified/fewer pathways.

Removed `traceReason` from VM stacktrace events
  This includes legacy reports, the primary motivation is that it was
being captured and not used. Additionally, not all stacktraces can be
related back to a meaningful vm event.
  Also, the fixing up of data types also resulted in some code
simplification in vmgen and sem.

Clean-up identifier errors and fix vm err location
- cleaned up various expected identifier messages
- vm errors now capture instantiation info correctly
- errors don't set location data on diagnostics if already present, to
  honour overrides

Diag mapping in `vm` and `vmgen` was updated.
Mapping `vm` and `vmgen` events to `PAstDiag` are presently in their
respective modules as they both directly depend upon `ast_types`. Not an
ideal situation, but a lot more refactoring is required until `vm` is
free of AST knowledge/dependencies.

`options` module now manages `ReportSet` as a simple collection of
`NodeId`s of diagnostics that have been reported.

Removed `ConfigRef` param from `types.typeMismatch`, it wasn't being
used

Report Output and Generation Details
====================================

Better error for `is` with wrong number of args:
- previously: `wrong number of arguments`
- now: `'is' operator takes 2 arguments'
- fixed `tests/errmsgs/tmisc` test to match wording

Undeclared identifier errors now output any recursive modules imports
that were detected as those can be a cause of such errors.

Recursive dependency tracking from the importer is cheaper, as it now
only stores FileIndex pairs. Unfortunately, we don't have a clearing
mechanism, so new minor space leak. :/

removed some eager diag message data querying

Fixed doc gen error report rendering, which weren't outputing the full
text, making it impossible to find where errors/hints/warnings were
occurring. Without this fix, it meant an unclosed backtick in a doc
block was breaking CI... cool.

Legacy Report Related Change Details
====================================

Removed some bounds tracking in reports
  A number of `Report`s are tracking, but never using a pair of `Int128`
in order to know out of bound issues for arrays, ranges, ordinals, etc.
  The data is rarely if ever output in messages and that's a lot of
bytes in most cases. Disabled whereever this was inconvenient, it can be
restored for error messages we wish to improve as future work.
  Created `rsemBigOrdsEnergy` to not overload `mismatchCount` tuple with
`Int128` bloat, and moved the following reports there:
- `rsemSetTooBig`
- `rsemArrayExpectsPositiveRange`
- `rsemInvalidOrderInEnum`
(partial list)
  No longer capture `countMismatch` data for these as it's unreported:
- `rsemExpectedLow0Discriminant`
- `rsemExpectedHighCappedDiscriminant`
(partial list)

The `errorKind` property now returns a `TAstDiagKind`

Errors related to positions in calls where identifiers are expected have
been updated to provide a bit more context:
- dot calls, callable fields access, etc errors wording update,
    indicating the problematic identifier and then the call expression
    within which it was found. See:
    `rsemExpectedIdentifierWithExprContext` handling in `cli_reporter`
- updated `astrepr` to handle new `diag` field of `nkError` variant
Resulting in the following test changes:
- `nimsuggest` test `tchk1` updated for messages with "found" wording
    instead of "got"

`countMismatch` in reports are now `int`s, instead of `Int128`,
seiously, how many were we expecting?

The string value of `mSizeOf` as `"sizeOf"` was taken from VM tests, but
doesn't jive with other tests that serialize the same magic. Need to
figure out which convention to go by.

Regression/Caveat Details
=========================

`concept` and `{.explain.}` error msg regression
  The compiler presently doesn't emit useful diagnostics for these,
simply a count of number of diagnostics failed. The implementation is
tied up with `structuredReportHook`, which in turn uses `Report`, and
there isn't a reasonable way to turn this into `PAstDiag` for
consumption. The following tests are disabled `knownIssue`:
- tests/lang_experimental/concepts/t3330
- tests/lang_experimental/concepts/texplain
- tests/lang_experimental/concepts/twrapconcept

Misc
====

Noted issues with the `reports` module and friends, hopefully it wards
off any further profileration and people can help with incremental
rework.

`types.semReportTypeMismatch` no longer takes a `ConfigRef` parameter.
This turned out to be unnecessary/unused after all the diag changes.

`sigmatch` has fewer dependencies on `reports_sem`

`getReport` moved to `msgs`, dropped `conf` param

Creating a new use qualifier diagnostic via
`semstmts.newSymChoiceUseQualifierDiag` will assert that there are at
least two choices to avoid spurious errors.

Removed a number of compile warnings by removing unused imports.

updated `astrepr` to use ast diagnostics from `nkError` nodes.

Reduce broad exports by `Report` related modules:
- `reports` was leaking `ast_types` _everywhere_
- `reports_base` had overlapping exports

Formatting/Style clean-ups in these modules

Random Report Changes:
- remove `rsemUserRaw`, it's never used
- renamed `rrsemCompilesError` to `rsemComplesHasEffects`

Special thanks to zerbina for all the code reviews and suggestions!

Co-authored-by: zerbina <100542850+zerbina@users.noreply.github.com>

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[5250b1fcc6...](https://github.com/GoldenAlpharex/tgstation/commit/5250b1fcc6aca1aa6d6b0f9ec81ce6ad5fe2fa03)
#### Thursday 2023-01-19 20:36:20 by san7890

Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[0831eab2eb...](https://github.com/NetBSD/pkgsrc/commit/0831eab2eb517f0f988462966e66983738331002)
#### Thursday 2023-01-19 20:58:46 by nikita

gleam: update to version 0.26

ChangeLog taken from https://gleam.run/news/v0.26-incremental-compilation-and-deno/
Incremental compilation, and hello Deno!

Gleam v0.26 released

Incremental compilation

A Gleam project is made of packages, typically a top level package and several
dependency packages fetched by the package manager, and each package contains
a collection of modules of Gleam code.

In the very early days of Gleam when the compiler was run it would compile from
scratch every module in every package in the project. This was highly wasteful,
especially for the dependency packages which are would not have changed at all.
To tackle this inefficiency when the Gleam build tool was created it was made
to compile dependency packages only once and reuse the compiled code for every
following build, resulting in only the top level package being recompiled.

This has worked well for the last couple years, but now as more people are
using Gleam it was time for an upgrade. Large projects such as those with a
large amount of generated gRPC code were starting to take an irksome amount of
time to compile. Gleam is all about fun and productivity, so this just won't do!

There are numerous ways we want to improve the performance of the (already
very nimble) Gleam compiler, but the majority of the time is spent in the Erlang
compiler, which we use to generate BEAM bytecode, so these improvements will not
be very impactful here. Instead we need to improve the build tool such that it
only compiles modules when it has to, rather than the entire package.

To benchmark the impact of this change I created a Gleam package with 300,000
lines of code and 370,000 lines of documentation comments across 1400 modules,
and test recompiling the package without any changes. The old version of the
compiler will recompile every module, while the new version will instead only
read and verify the caches.
Erlang

Benchmark 1: v0.25
  Time (mean ± σ):     18.443 s ±  0.949 s    [User: 18.458 s, System: 2.995 s]
  Range (min … max):   17.102 s … 19.968 s    10 runs

Benchmark 2: v0.26
  Time (mean ± σ):     140.8 ms ±   3.9 ms    [User: 92.5 ms, System: 46.4 ms]
  Range (min … max):   138.0 ms … 156.1 ms    20 runs

Summary
  'v0.26' ran
  130.99 ± 7.67 times faster than 'v0.25'

When targeting Erlang rebuilding now 130 times faster than before for a
project this size!
JavaScript

Benchmark 1: v0.25
  Time (mean ± σ):      1.861 s ±  0.026 s    [User: 1.543 s, System: 0.299 s]
  Range (min … max):    1.833 s …  1.927 s    10 runs

Benchmark 2: v0.26
  Time (mean ± σ):     145.3 ms ±   2.9 ms    [User: 92.9 ms, System: 50.8 ms]
  Range (min … max):   141.4 ms … 154.3 ms    20 runs

Summary
  'v0.26' ran
   12.81 ± 0.31 times faster than 'v0.25'

When targeting JavaScript the change is less impactful, running just under 13
times faster. This is because on this target we don't need to run the Erlang
compiler to generate bytecode, the outputted JavaScript code can be loaded
directly into a JavaScript runtime.

These benchmarks were performed with the excellent Hypefine command line
benchmarking tool.
How does it work?

When the compiler runs for each module it emits a set of reusable artefacts:

    Erlang bytecode in a .beam file.
    Erlang record definitions in .hrl files for use by any native Erlang modules.
    Information on the types and values in the module in a .cache file.
    Information the compilation of the module in a .cache_meta file.

If the module doesn't need to be compiled again then we can load the .beam
bytecode into the virtual machine, load the module information from the .cache
file so we can compile other modules that depend on it, and move on to the next
module.

How do we tell if a module needs to be recomplied? There are two checks we need
to make, both using information stored in the .cache_meta file.

The first is to check the modification time of the source file against the
compile time stored in the .cache_meta file. If the source file modification
time is newer then it has been changed and we need to recompile it.

The second is to look at the modules dependencies. The .cache_meta file stores
a list of the modules the the module imports, and using this we can tell if any
of modules upstream in the dependency tree are going to be recompiled. If so
then we need to recompile the module as a change in a dependency may mean that
this module needs to be compiled differently than last time.

What's next?

These changes have made a huge difference to compilation speed, but there's
still a lot more easy wins we can apply in future here if the need arises such
as improvements to the efficiency of the compiler's IRs, more precise cache
invalidation, and multithreaded compilation.

Developer experience is a top priority for Gleam. You need your feedback as
quickly as possible when writing Gleam code, so we're committed to keeping the
compiler super speedy.

Running on Deno

Gleam can run on JavaScript as well as the Erlang virtual machine. Until now
when you run gleam run or gleam test with a Gleam project targeting JavaScript
it'll run your code using the NodeJS runtime. With v0.26 the Deno runtime can
be used instead!

Deno is similar to NodeJS in many ways, but it boasts better compliance with
web-standard APIs, much better security, and a very slick developer experience.

To use Deno instead of NodeJS you can either add the --runtime=deno flag to
commands like gleam run, or you can add the javascript.runtime property to your
gleam.toml file.

name = "my_project"
version = "1.0.0"

[javascript]
runtime = "deno"

Thank you to Brett Kolodny for this feature!
Thanks

Gleam is made possible by the support of all the kind people and companies who
have very generously sponsored or contributed to the project. Thank you all!

If you like Gleam consider sponsoring or asking your employer to sponsor Gleam
development. I work full time on Gleam and your kind sponsorship is how I pay
my bills!

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[d650a1a7cb...](https://github.com/SmoSmoSmoSmok/tgstation/commit/d650a1a7cbb77937dd97e77e760d0c2cc606e290)
#### Thursday 2023-01-19 21:05:26 by Jacquerel

Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[24f482b438...](https://github.com/pytorch/pytorch/commit/24f482b4384de63b3e0edb18e25d87b7c62e5187)
#### Thursday 2023-01-19 21:12:55 by Edward Z. Yang

Update base for Update on "Implement SymBool"


We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyangmeta.com>

[ghstack-poisoned]

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[972c350665...](https://github.com/Sonic121x/Skyrat-tg/commit/972c35066535665b36788e2b59d9e9bf6429bbb9)
#### Thursday 2023-01-19 21:21:12 by Zonespace

Mirror #71906 (#18666)

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.

![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR:
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [xXTacticalWaffleXx/neocities-files](https://github.com/xXTacticalWaffleXx/neocities-files)@[cff07a1a66...](https://github.com/xXTacticalWaffleXx/neocities-files/commit/cff07a1a6635c1424c1bddcb564ca23a3c3361b5)
#### Thursday 2023-01-19 21:49:36 by Luna Aphelion

TAKE FUCKING GUESS, TAKE A WILD FUCKING GUESS YOU MUPPET, GUESS WHAT YOU UTTER CUNT, I ADDED A QUOTE TO /LOL FUCKING UNHEARD OF I KNOW, FUCK YOU

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[902caab964...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/902caab964ac13d49bef2a54b44a948d3ebeedfd)
#### Thursday 2023-01-19 22:09:21 by SkyratBot

[MIRROR] Stock Part Datumization Complete [MDB IGNORE] (#18639)

* Stock Part Datumization Complete (#72559)

So i accidently reverted all my commits in #72511 when resolving a merge
conflict So ummm yeah fuck my bad anyway

Finishes what was started in #71693 and completes the
[initiative](https://github.com/tgstation/dev-cycles-initiative/issues/1)

Except for `obj/item/stock_parts/cell` and its subtypes. All machines
now use `datum/stock_part` for its requested components & component
parts

Not sure if i caught every machine & stuff in the game so merge with
caution
:cl:
code: datum stock part for every obj stock part
refactor: all machines & dependent experiments to use datum stock parts
/:cl:

* Fixes a teeny tiny Funce mistake :)

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [irina-mandarina/thesis-frontend](https://github.com/irina-mandarina/thesis-frontend)@[eee4cda1e9...](https://github.com/irina-mandarina/thesis-frontend/commit/eee4cda1e94f161bbf4651544f148721c79e75ad)
#### Thursday 2023-01-19 22:37:09 by irina-mandarina

biggest mistake of my life also saved me from myself (removed middleware because it sucks the life out of me and replaced it with onBeforeMounts)

---
## [peff/git](https://github.com/peff/git)@[19fc541c31...](https://github.com/peff/git/commit/19fc541c31679bd597a7a6fce988479b47908242)
#### Thursday 2023-01-19 23:17:05 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[cd60bcae3a...](https://github.com/peff/git/commit/cd60bcae3a5661f9d5f5cd8eea9da257f6c9966a)
#### Thursday 2023-01-19 23:17:06 by Jeff King

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
## [chrysillo/shopping](https://github.com/chrysillo/shopping)@[b631c07d8c...](https://github.com/chrysillo/shopping/commit/b631c07d8cfae35f016af2000ad66e508046e812)
#### Thursday 2023-01-19 23:20:13 by Chris

adding more shit again omg wtf FUCK REACT IN THE ASSHOLE

---

