## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-21](docs/good-messages/2023/2023-04-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,149,484 were push events containing 3,286,551 commit messages that amount to 247,419,739 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [atosti/tgstation](https://github.com/atosti/tgstation)@[2b2cb3dff6...](https://github.com/atosti/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Friday 2023-04-21 00:06:13 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[200b739c0a...](https://github.com/effigy-se/effigy-se/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Friday 2023-04-21 00:28:16 by Kyle Spier-Swenson

Refactors and defuckulates dbcore. Adds support for min_threads rustg setting, Reduce query delay, Make unit tests faster (#74852)

dbcore was very fuckulated.

It had 3 lists of queries, but they all had their own current_run style
list to support mc_tick_check (as it was already being done before with
the undeleted query check, so i can understand why they ~~cargo culted~~
mirrored the behavior) This was silly and confusing and unneeded given
two of those loops can only process at most 25 items at a time on
default config, plus these were cheap operations (ask rustg to start
thread, ask rustg to check on thread).

Because of the confusingness of the 6 lists for 3 query states, The code
to run pending/queued queries immediately during world shutdown was
instead looking at the current_run list for active queries, **meaning
those queries got ran twice.**

The queued query system only checked the current active query count in
fire(), meaning even when there was nothing going on in this subsystem
new queries had to wait for the next fire() to run (10 ticks, so 500ms
on default config)

Those have all been fixed.

the config `BSQL_THREAD_LIMIT` has been renamed to
`POOLING_MAX_SQL_CONNECTIONS` and its default was lowered to match
MAX_CONCURRENT_QUERIES .

added a new config `POOLING_MIN_SQL_CONNECTIONS`, allowing you to
pre-allocate a reserve of sql threads.

The queue processing part of SSdbcore's fire() has been made to not obey
mc_tick_check for clarity and to make the following change easier to do:

If there is less than `MAX_CONCURRENT_QUERIES` in the active queue, new
queries activate immediately.

(its ok that there are two configs that kinda do the same thing,
POOLING_MAX_SQL_CONNECTIONS maps to max-threads in the mysql crate, and
it seems to only be a suggestion, meanwhile MAX_CONCURRENT_QUERIES can't
do anything during init, which is when the highest amount of concurrent
queries tend to happen.)

:cl:
config: database configs have been updated for better control over the
connection pool
server: BSQL_THREAD_LIMIT has been renamed to
POOLING_MAX_SQL_CONNECTIONS, old configs will whine but still work.
fix: fixed rare race condition that could lead to a sql query being ran
twice during world shutdown.
/:cl:

I have not tested this pr.

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[773cc9542a...](https://github.com/effigy-se/effigy-se/commit/773cc9542a54837fc52b15eb09cc98d7226049fb)
#### Friday 2023-04-21 00:28:16 by MrMelbert

Adds admin alert for revs created through traitor panel (#74862)

## About The Pull Request

So like, using traitor panel to make revs doesn't work. 

Revolutions live and die, currently, by the revolution ruleset datum
dynamic creates. It manages the hostile environment and also processes
to check whether either side should be winning or not.

This means that the revolutionary buttons in the traitor panel are kind
of noob-admin-bait. You press it for a funny revolution and then you
realize it's screwed when all the heads are dead and everyone's
stumbling around cluelessly

This has a proper solution, albeit somewhat difficult - separate out the
revolution from the ruleset, make admin spawned revs create a
revolution. I can do this but it's a lot of effort and this works in the
meanwhile

Pops up a TGUI alert when an admin presses "add revolutionary" in
traitor panel when there is no ongoing revolution. Simply enough, gives
them an alert that it will not work correctly. Lets them decide whether
they want to deal with that. (Because you can manually deal with it via
proc calls, if you've got code smarts.)

## Why It's Good For The Game

Stops admins from stumbling into the same trap without warning.

Can be removed in the future easily when revs are coded better. 

## Changelog

:cl: Melbert
admin: Adds a warning that spawning revs via traitor panel will not
function as expected.
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[821123b598...](https://github.com/effigy-se/effigy-se/commit/821123b59850bc4d0556b8dd7e0cf169f7fa6bc3)
#### Friday 2023-04-21 00:28:16 by ChungusGamer666

Makes a whole bunch of wooden objects flammable (#74827)

## About The Pull Request

This whole PR started because I realized that baseball bats are not
actually flammable which I found weird, then I looked at a whole bunch
of other stuff that really should be flammable but also isn't.

## Why It's Good For The Game

Makes wooden objects behave slightly more consistently? Honestly, most
of these seem like oversights to me.

## Changelog

:cl:
balance: The following structures are now flammable: Picture frame,
fermenting barrel, drying rack, sandals, painting frames, paintings,
spirit board, notice board, dresser, displaycase chassis, wooden
barricade
balance: The following items are now flammable: Baseball bat, rolling
pin, mortar, coffee condiments display, sandals, wooden hatchet, gohei,
popsicle stick, rifle stock
/:cl:

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[0e522da14f...](https://github.com/Mojave-Sun/mojave-sun-13/commit/0e522da14fc608516b2d7ceff37bef7069a39bc7)
#### Friday 2023-04-21 00:36:17 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[7df4885117...](https://github.com/Apogee-dev/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Friday 2023-04-21 00:37:42 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4874f16358...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4874f163585c1e00d3e5ced697c605f1cfcb141d)
#### Friday 2023-04-21 00:53:59 by SkyratBot

[MIRROR] Fixes a runtime in simple_animal/hostile [MDB IGNORE] (#20588)

* Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.

https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294

## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Fixes a runtime in simple_animal/hostile

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[b828a9851b...](https://github.com/Nerev4r/Skyrat-tg/commit/b828a9851b193f94acd182677d971da01e6d215b)
#### Friday 2023-04-21 00:55:42 by SkyratBot

[MIRROR] Icemoon Hermit Ruin Active Turf Fix - For Real This Time [MDB IGNORE] (#20325)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[54b27a78b5...](https://github.com/Nerev4r/Skyrat-tg/commit/54b27a78b5559d99d84577a8a38c39ca5cb52851)
#### Friday 2023-04-21 00:55:42 by SkyratBot

[MIRROR] IceBoxStation More Active Turf Fixes [MDB IGNORE] (#20339)

* IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request

![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

* IceBoxStation More Active Turf Fixes

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[4aca39a533...](https://github.com/swbs-co/odoo/commit/4aca39a533e9d41f5f452f36a1ffc001f586b4f4)
#### Friday 2023-04-21 01:00:28 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#116252

Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[bad4c9168c...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/bad4c9168c3ccf04effadc09b3d1b1a817fbfbf6)
#### Friday 2023-04-21 01:04:29 by SkyratBot

[MIRROR] Mafia rebalance and backend refactor [MDB IGNORE] (#20631)

* Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

* Mafia rebalance and backend refactor

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[8fcd8c6184...](https://github.com/git-for-windows/git/commit/8fcd8c6184b54f44bb87e7f95baddc67bce9865b)
#### Friday 2023-04-21 01:25:22 by Johannes Schindelin

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
## [Abaso007/Open-Assistant](https://github.com/Abaso007/Open-Assistant)@[b9c60ed582...](https://github.com/Abaso007/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Friday 2023-04-21 02:05:37 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [effigy-se/effigy-xr](https://github.com/effigy-se/effigy-xr)@[2728bbe9a9...](https://github.com/effigy-se/effigy-xr/commit/2728bbe9a9003dbb4283ac807108c65129b7f34d)
#### Friday 2023-04-21 03:16:12 by SkyratBot

[MIRROR] Polishes some side sources of light and color [MDB IGNORE] (#19860)

* Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing

## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

* Polishes some side sources of light and color

* yellow

* Update dance_machine.dm

* Merge branch 'upstream-merge-73936' of https://github.com/Skyrat-SS13/Skyrat-tg into upstream-merge-73936

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: lessthnthree <three@lessthanthree.dk>

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/gurking/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Friday 2023-04-21 03:29:00 by Captain277

Ashlanders Phase 3.5: Prelude to War (#5259)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

_War is coming to Surt-nar-Vel'la. It rages in the caverns below, held
back only by the furious roiling blood of the Mother. More and more
Scori are driven up to Surt-nar-Vel'la, and they bring ancient secrets
with them. But, perhaps not all that dwells below should be
unearthed..._

1. **Increases Mother's Blessing from 5 minutes to 15.**
2. **Gives Ashlanders access to Sign Language.**
3. **Creates reagent Phlogiston.**
4. **Creates Condensed Phlogiston item.**
5. **Creates craftable Heaven Shaker hand-held explosive.**
6. **Buffs Shank riding speed.**
7. **Makes tying posts dense.**
8. **Adds craftable Primitive Splints.**
9. **Adds craftable Bone Pipes.**
10. **Adds the craftable Spark Striker.**
11. **Adds cowls.**
12. **Adds Ashlander cryo.**

## Why It's Good For The Game

1. _This buff is too short-lived to be used by the Ashlanders. I'm
raising it to 15 minutes. However, it is still fairly robust, so I might
drop it to 10. Or raise it even further if it's still too short._
2. _It's been months of lessons. Knowledge of primitive sign is now
available to most surface dwellers. It is slowly being disseminated
below the surface to those who are willing to learn, meaning those who
are likely to come to the surface may know it too._
3. _Phlogiston is the alchemical compound found in all explosive and
flammable things. Here I imagine it as a sticky tar similar to napalm or
condensed nitroglycerin._
4. _Condensed Phlogiston is basically semtex. Not much more to add
there._
5. _These craftable grenades require condensed phlogiston. They are
designed to address an impending threat, but will almost certainly need
to be nerfed and fine tuned. They come in two flavors: HE and Frag._
6. _Shanks now move slightly faster, providing a movement bonus to
mounted travel._
7. _Tying posts not being dense has bothered me for a while now._
8. _Gotta have a way to temporarily mend bones until surgery is done!_
9. _Apparently Ashlanders are missing avenues to fine tobacco - and
other substances. Perhaps a new avenue of trade..._
10. _Going to need lighters for your pipes._
11. _These are basically the hood parts of certain cloaks or jackets,
but toggleable as simple headwear._
12. _No longer will there be braindead Ashlanders sleeping in the
Temple!_

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
tweak: Increases duration of Mother's Buff.
tweak: Gives Scori Sign Language.
add: Adds Ashlander cryo.
add: Adds Phlogiston and Condensed Phlogiston.
add: Adds Heaven Shaker grenades, using phlogiston.
tweak: Buffs riding speed of Shanks.
tweak: Makes tying posts dense.
add: Adds craftable primitive splints.
add: Adds bone pipes.
add: Adds primitive lighters.
add: Adds cowls.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [allinkdev/WNT](https://github.com/allinkdev/WNT)@[cd8177a07c...](https://github.com/allinkdev/WNT/commit/cd8177a07c642e01da55317e2cfe664caaa646c3)
#### Friday 2023-04-21 04:55:18 by Video

Prevents WNT from launching when Shadow Client is installed

Shadow is a client created by a group of individuals with a single goal in mind: griefing and crashing servers. Instead of adding support for the mod like I have with DeviousMod, Meteor, and (soon) Wurst, I have decided set a flag in the mod JSON to deliberately prevent the game from booting if it detects Shadow Client.

### Reason #1 - It doesn't work anyways
I had a friend test the mod and quite bluntly, Shadow breaks too much shit, including WNT. I could totally fix it on my own free time, but why should I even bother?

### Reason #2 - Conflict of interest
Members of the group have recently used exploits in Shadow Client to attack TotalFreedom to the point where they nearly crippled the server on a few occasions. Enabling a group like this to attack the server by implementing support for a client like this in a mod intended to support the administration of is a gigantic conflict of interest.

### Reason #3 - It's personal
I hold a grudge against the group and everything they do because they attacked TF with spambots and exploits. It's as simple as that.

---
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[e4a1892e0a...](https://github.com/TeDGamer/cmss13/commit/e4a1892e0a42115dfb3d90009d960386b76fe955)
#### Friday 2023-04-21 04:59:15 by NewyearnewmeUwu

No more proximity sensor spam. (#3076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
You can now slash proximity sensors to shut them up as xeno, and death
shuts off any proximity sensors in your belongings.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This is literally just the engi bellpack again. It's being used to OOCly
annoy people and needs a way to circumvent it.
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
fix: Proximity sensors can now be slashed by xenos to deactivate them,
and they turn off after you die if you have an active one on you.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [michalnpl/terminal](https://github.com/michalnpl/terminal)@[21464fe41c...](https://github.com/michalnpl/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Friday 2023-04-21 05:02:23 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[9df26f6a8b...](https://github.com/PhantomEpicness/cmss13/commit/9df26f6a8bf397df29e1bff4b5e777414bd1cc44)
#### Friday 2023-04-21 05:24:05 by riot

DD updates (#2786)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

DD hasn't been touched in a while, and is kind of bad against preds,
tries to fix this to the best my my ability with the below changes.

1. Makes the M1911 more accurate
2. Makes DD armor cover arms and legs, improves its bullet and explosive
resistance
3. ERT Medical Pouch now contains the basic 3 injectors(bic, kelo,
tram), an emergency injector, a splint, and a bandage
4. DD now all have max endurance skill
5. M60 is now full auto, does more damage, and is more accurate
6. DD Minigun(ol painless) now has an integrated magharn
7. M60 now has the same box changing mechanic that smartgun has.
8. Adds 2 new guns(technically 1, or maybe 1.5), the XM177 and M16
Grenadier(an M16A1/2 with an M203 attached)
9. Adds an M203 grenade launcher, single grenade, no IFF, high range
with scope, only fits on M16 grenadier
10. Adds 3 new impact grenade types, only DD have them currently.
11. Adds HE impact grenade, impacts in a cone radius with an HE
explosion.
12. Adds an incendiary impact grenade, impacts in the same pattern as
HIDP, napalm.
13. Adds an impact buckshot grenade, pure vietnam vibes, shoots 10 bits
of additional buckshot that also slow.
14. DD now have MDs tuned to their own IFF.
15. DD are now equipped with XM177s for the medic, Dutch, and
flamethrower operator
16. DD riflemen have a 60% chance for an M16A1, 30% chance for an M16
Grenadier, and 10% chance for an M60.
17. Removes the M60 from black market
18. Moves DD presets to their own standalone folder, and removes the
/fun/ from their typepaths.
19. Changes CLF crashed ship M60 to a MAR50
20. Adds sprites for M203, XM177, M16 Grenadier
21. DD spawn with a lucky pack and a zippo in their helmet.


# Explain why it's good for the game

Dutch's Dozen is a bit outdated, and light on content, gives them some
love.
Removes gear that doesn't fit in BM from BM, also I buffed the gear too
so balance concerns.

1. An unwielded rifle(M41A), had more accuracy than a wielded M1911,
would do this for other pistols too but out of scope as DD only use
M1911
2. They were incredibly easy to kill via leg/arm aiming, as no armor,
HPCs instakilled them(DD are default dishonorable), and FF did insane
damage as they all had high AP 40 damage rifles.
3. ERT medical pouch was worse than normal med-pouch, DD use this too.
4. Was intended, survivor endurance skill nerf effected this too as the
same define was used for both as a shortcut
5. M60 underpreformed, makes it better.
6. Dropping Ol' Painless over and over sucks.
7. Unique realistic mechanic for the M60, makes it more interactive
8. Unique guns, only DD get them, also the XM177 is my favorite gun of
all time I love it 😊
9. Unique UGL for M16 Grenadier, designed to work directly with the
sprite, as its integrated and only fits on it.
10. Grenades for DD to have a better chance against preds, riflemen have
a 30% chance of spawning with M16 GL.
11. Made for a stun, team gameplay for DD.
12. Area denial.
13. Vietnam Vibes, support tool cause it does jack shit damage.
14. DD couldn't tell friend from foe
15. (AWESOME) Carbine for Dutch, makes sense for the support and members
of the team to have carbines instead of rifles
16. Variance within DD team, all 3 of the guns are good, GL is a support
tool, M60 as an ambush(also its The Pig), A1 is normal
17. M60 doesn't fit thematically, and is too powerful.
18. Easier access, they don't fit in the fun file
19. Buffed M60, MAR50 fits more there anyway.
20. Sprites for things I added.
21. Its cool.

# Testing Photographs and Procedure


![image](https://user-images.githubusercontent.com/103988604/223497128-7f485e32-07cd-49dc-b7b0-d04ce08b3042.png)


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
add: DD spawn with a lucky strike pack and a zippo in their helmet.
add: M60 now has the box changing mechanic that smartgun has.
add: Adds an M16 grenadier, with attached M203, also adds M203 grenade
launcher and impact shells for it, only DD have it
add: Adds a new M16 variant, the XM177E2 Carbine, only DD have it
add: Dutch M16s now are marked as A1s, and use the preexisting M16A1
sprite instead.
add: Dutch's Dozen are now equipped with an XM177 for Dutch, the medic,
and the flamethrower operator
add: Dutch's Dozen riflemen now have a 60% chance to have an M16A1, 30%
chance for an M16 with M203 UGL, and 10% chance for an M60 GPMG
del: M60 has been removed from the black market
balance: DD minigun now has an integrated magharn.
balance: M1911 is slightly more accurate.
balance: ERT Medical Pouch now contains the 4 basic EZ injectors and a
gauze.
balance: DD armor now has a greater explosive protection and covers the
arms and legs.
balance: M60 is now full auto, does more damage, and is more accurate.
code: Moved Dutch's Dozen presets to their own standalone folder
spellcheck: DD spawn text now correctly says the Yautja mask is on
Dutch's face.
fix: DD Motion Detectors no longer pick themselves up.
fix: DD now all have max endurance skill
imageadd: Adds sprites for M203, M203 shells, XM177, and M16 Grenadier
Variant
maptweak: LV624 Crashed CLF ship insert M60 has been replaced with a
MAR50
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [txnbotpro/txnbot](https://github.com/txnbotpro/txnbot)@[cf218b836e...](https://github.com/txnbotpro/txnbot/commit/cf218b836ebcc63bf630db9c3f3e8c9afeb6f3a6)
#### Friday 2023-04-21 05:35:54 by txnbotpro

You want to play with "BOT" on the blockchain?


🔥 Uniswap is a cryptocurrency exchange which uses a decentralized network protocol. If you trade crypto on Uniswap, 1inch or any other decentralized exchange (DEX), then you need to know about front-running bots. Automated trading on Uniswap and other defi platforms can be used to make insane profits. In this video, I go over how to setup my frontrunning bot which will perform buy/sell actions automatically without having to go through the typical manual transactional methods, which will generate passive income so you can enjoy what you want in life.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[9bbac13b28...](https://github.com/cmss13-devs/cmss13/commit/9bbac13b2898570be5e448ce50ca110472561630)
#### Friday 2023-04-21 05:59:31 by TotalEpicness

Globber balance overhaul (#3039)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Globber came out overtuned as shit and actually replicated some of the
issues that we didn't want like the dreaded ChokePoint Boiler Torture
Rebalances some issues that weren't forseen during the development nor
TM stage of globber. This should be TM'd


General changes:
- Globber C/D 25 seconds > 30 seconds ( the temp nerf PR didnt actually
fix this correctly)
- Fire deals 2x damage instead of 1.5x damage ( this needs significant
testing and will likely be toned down)
- Acid spray doesn't stun at full distances anymore

Depending on TM feedback, I might switch between these two variants of
this overhaul:

Rework variance 1: Keep zoom and current design while maintaining a
little toughness [currently on]
- Armor 25 > 20
-  Zoom halved 4 > 2
-  Dropped health a tier: 650 > 600
- Fire deals 2x damage instead of 1.25x damage
- Globber C/D

Rework variance 2: Embrace the zoom removal
- Directional armor 10 base armor + 20 at the front. Flank a globber to
kill it!
- Slight windup increase 5s > 6s
- Fire damage 1.25x > 1.5x

Fixes:

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

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

:cl: Totalepicness

balance: Rebalances globber, which has come out overtuned. Globber now
has reduced health, armor and zoom along with higher fire damage
multiplier.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [CLorant/quizter](https://github.com/CLorant/quizter)@[6c362c79c4...](https://github.com/CLorant/quizter/commit/6c362c79c46a857a9307164ecce5b89d8226cdc0)
#### Friday 2023-04-21 06:08:01 by KatamoriVagyok

I FUCKIN HATE CLRF FILE EXTENSION MAN, LF IS MY LIFE, WINDOWS IS MY LIFE

---
## [openai/evals](https://github.com/openai/evals)@[9fdbd94c93...](https://github.com/openai/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Friday 2023-04-21 06:25:14 by Tong

Add Loss Logic Eval (#82)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


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
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

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
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[8afb4341d0...](https://github.com/Koi-3088/ForkBot.NET/commit/8afb4341d074838bf85360d63957ab467c0e7201)
#### Friday 2023-04-21 06:33:32 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[360f7d446a...](https://github.com/heady8354/Video-Game-Project/commit/360f7d446ad9e2ad5cc66e6b18bae6161f94482b)
#### Friday 2023-04-21 06:52:44 by heady8354

content update + town

in this giant update I managed to stay somewhat focused because of a promise i made to my girlfriend. I told her Id be super productive tonight and get a lot done, which I certainly did, but I bit off more I could chew and promised to start on an ending and uhhh yeah didnt do that yet. However, in tomorrows class i might be able to. thank you for reading.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c3b78761d2...](https://github.com/LemonInTheDark/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Friday 2023-04-21 07:03:54 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[b5ebf5c942...](https://github.com/LemonInTheDark/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Friday 2023-04-21 07:03:54 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[d0e7844c48...](https://github.com/Droidcraft/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Friday 2023-04-21 07:25:43 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

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

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

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

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

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
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[fabca8cebb...](https://github.com/Droidcraft/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Friday 2023-04-21 07:25:43 by Nick Clyde

Heart Disease Prediction (#538)

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
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

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
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[776e4fa212...](https://github.com/Droidcraft/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Friday 2023-04-21 07:25:43 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [RoninNada/android_frameworks_base](https://github.com/RoninNada/android_frameworks_base)@[e41f314422...](https://github.com/RoninNada/android_frameworks_base/commit/e41f3144224084c5e3cb29143d8e528adfc9c69c)
#### Friday 2023-04-21 08:17:04 by Alex Cruz

Set scrollview on the power menu

So why? Because fuck you that's why...

No, you need this for if and when we decide to add more items to the power menu and the
density is too high. Previously if you had more than 5 items, it would cut you off. So
you either had to decide which 5 items you wanted or deal with the jank. That's no longer
the case.

- Added a landscape view so we can set a horizontal scrollview

- Made the power menu dialog all one color. Josh and I talked about this and I previously
made the case to keep it the same but after thinking it over, it looks better all one color.

Change-Id: I8ec4b1a85994251126433cea0640e000af78c65d
[@neobuddy89: Fix to work with 5e56027b8c4f27a4fa6fe847f79dd0ef8e09c0db.]
Signed-off-by: Pranav Vashi <neobuddy89@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[199411ba0f...](https://github.com/TaleStation/TaleStation/commit/199411ba0f7e07f8a5d9b25c5abedd48574e4f55)
#### Friday 2023-04-21 09:03:06 by Jolly

Refactors avian talons to not be hacky and dogshit (#5435)

Thanks to Time Green for giving me a hand and pointers.

Makes avian talons not dog shit in code, and not dog shit as a pref
option. Also thats gone entirely.

## Changelog

:cl: Jolly
del: Deleted the old avian talons and associated prefs.
refactor: Instead, the code was refactored to not be awful to look at,
and improved from a players POV.
/:cl:

---
## [juju/juju](https://github.com/juju/juju)@[7976a61522...](https://github.com/juju/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Friday 2023-04-21 10:06:25 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [Gboster-0/lobotomy-corp13](https://github.com/Gboster-0/lobotomy-corp13)@[928b2420d9...](https://github.com/Gboster-0/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Friday 2023-04-21 10:43:10 by Lance

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[b1716732b0...](https://github.com/necromanceranne/tgstation/commit/b1716732b058121e86c60700fb9d1d8f4f9a6b3a)
#### Friday 2023-04-21 11:57:27 by Cheshify

The North Star Expeditionary Vessel - A Second Wind (#74371)

## About The Pull Request
A new map for TGstation, in the works! It has 4 fucking Z levels, a
massive expansive maintenance with unique designs, and some unique code
features in the works.

To Do:
- [x] Update the Map to Modern TG
- [x] Local Tests
- [x] Work on Map Optimizations
- [x] Run Live Tests

Fikou has greatly helped with creating an important flavour aspect of
this map, Trek Uniforms on anyone who joins! See the forum thread for
more. This includes the framework for innate station traits, station
traits loaded as long as it's in a map's json

Here's the forum dev thread there are screenshots there.
https://tgstation13.org/phpBB/viewtopic.php?p=657252#p657252

### Mapping March
Ckey to receive rewards: Cheshify

## Why It's Good For The Game
So, this is the North Star. An effort taking multiple mappers and of 9~
months of hard work. This map was not initially designed for TGstation,
but always designed for TGstation code. The process of retooling the map
for TGstation was an absolute joy and I feel like the map definitely has
it's niche as a massive and unique experience for it's players.

I adore this map, it's gorgeous, has a unique aesthetic, and a number of
very funny interactions with multi-Z. The PR comes packed with unique
mechanics for future mappers (innate station traits!), a number of
map-fitting shuttles, and a fun spacefaring uniform gimmick for the
crew.

**This is my second attempt at bringing this map into rotation. It was
initially closed due to concerns about maptick and performance, as I
wasn't willing to push for a map to be added to the repository if it
didn't function to my own standards. I've been informed by a number of
coders far better than I that optimizations are arriving and enroute, so
I think it's time to dust her off and set sail for another journey.**

**Quick Disclaimer: Due to some design decisions disagreed upon by the
headcoder team and myself, the map will not be featuring unique
roundstart uniforms, and despite my design intentions, the innate
station trait features will be shelved for now.**

## Changelog
:cl: Cheshify, Fikou, Blue-Berry, Zytolg, InfiniteGalaxies, Striders,
Sylphet, Riggle, Soal, Andry, Crit, Deranging, and Pumpkin0.
add: Nanotrasen's Newest Exploratory Vessel is now available! Meet the
North Star!
add: More landmines, and a landmine random spawner.
add: energy barriers now have a regenerative subtype, fit for permanent
installations.
code: Raised the number of possible level render to 4, check your
preferences if needed to be reduced.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [tomasdevelopment/Development](https://github.com/tomasdevelopment/Development)@[74780301c1...](https://github.com/tomasdevelopment/Development/commit/74780301c1692592dbabccfade53bddc3bbd5808)
#### Friday 2023-04-21 12:56:21 by TomasSuarez

Create 🚀 My Professional Portfolio!

#Hello World!
 This repository is designed for recruiters, fellow developers, and anyone interested in exploring my work. I am a passionate data analytics and business intelligence professional, always eager to learn and tackle new challenges.

🚀 In this repository, you will find a diverse collection of projects that showcase my skills in Python, Power BI, Java, and more. I've organized my work into branches for easy navigation, making it simpler for you to discover the projects that align with your interests.

What can you expect to find here?
📊 Data Analytics & BI: Dive into my projects where I've leveraged the power of data analytics and business intelligence tools to extract insights, drive decision-making, and create stunning visualizations.

🐍 Python: Explore my Python projects, ranging from data manipulation and analysis to web scraping and machine learning. You'll find well-documented code, clean and efficient solutions, and creative approaches to various problems.

📈 Power BI: Discover my Power BI dashboards and reports, where I've transformed raw data into interactive and insightful visualizations that facilitate data-driven decisions.

☕ Java: Check out my Java projects, showcasing my proficiency in object-oriented programming, data structures, and algorithms.

💡 And More: Don't miss out on other exciting projects, demonstrating my versatility and adaptability across different technologies and domains.

I encourage you to dive into my work and explore my projects! If you have any questions or would like to discuss potential collaboration, please don't hesitate to reach out. Let's connect and create something amazing together!

Happy exploring! 🌟

---
## [rorgoroth/darkplaces-mingw-w64](https://github.com/rorgoroth/darkplaces-mingw-w64)@[b04df3536d...](https://github.com/rorgoroth/darkplaces-mingw-w64/commit/b04df3536d8559130ec3c536a77aa7b7419f96c8)
#### Friday 2023-04-21 13:59:26 by Cloudwalk

 README: Remove Discord invite link. The Discord server is now deprecated

I'm unable to sustain the DarkPlaces engine community on Discord. They have
falsely disabled my main account and now my second account, this time
without an email explaining the reason. I have a 3rd account that is still
active. They have not responded to my emails asking for them to review
the ban of my main account and they have the gall to nuke my second
account as well.

They are flooded with support tickets likely because it is incredibly easier
to hijack a Discord account than any other account due to the simple fact
that Discord does NOT require email verification to change passwords. God
only knows what other horrors lie beneath that Eldritch abomination of
duct-taped JavaScript.

I was not banned from Discord as I was able to create the third account using
the same IP address. They ban IPs if you're banned from Discord. I can no
longer, in good conscience, give this shit, incompetent, bullshit company
a single neuron of mindshare going forward. Other arrangements for a community
hangout are to be determined but are not available at this time. The IRC,
obviously, remains available.

Until they get their shit together (if they do), FUCK Discord and FUCK
everything they stand for.

Signed-off-by: Cloudwalk <cloudwalk@icculus.org>

---
## [mmrwoods/dotfiles](https://github.com/mmrwoods/dotfiles)@[0701c79132...](https://github.com/mmrwoods/dotfiles/commit/0701c7913284e834292f93ef0fd2332e24434d16)
#### Friday 2023-04-21 15:03:54 by Mark Woods

Fix vim cursor position after mouse double click

I save the cursor position when entering visual mode so that exiting
visual after text object selection returns the cursor where I'd expect.

For this to work with visual mode mouse selection, I added a leftdrag
mapping to remember the cursor position, but neglected to add a mapping
to handle double click selecting, leading to some pretty damn weird and
annoying behaviour, e..g double click, ESC, jump back to start of file!

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[0bc8ee79f9...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/0bc8ee79f929b8ebfe7c8e2032f98c6ebf3e1af3)
#### Friday 2023-04-21 15:40:05 by AmyBSOD

New artifacts (unfinished)

We still need to code the actual effects of those. And yeah, the new version will indeed be Super Lotsa Artifacts Hack. Praise me, for I'm the ultimate crazy bitch who puts any kind of nonsense into the game that she can think of. :D

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[122af0e676...](https://github.com/Moonshanks/cmss13/commit/122af0e67660a5e4b636bcc42c4c1ee244bfeff2)
#### Friday 2023-04-21 16:25:30 by morrowwolf

COs no longer have emote cooldown (#2901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

COs no longer have emote cooldown. This may be the cursed way to do it I
did this in approximately two minutes while being rezzed by a bald
medic.

# Explain why it's good for the game

When I'm leading I can't be having EMOTE COOLDOWNS slow down my
OOOO-FUCKING-RAH. (I will take this away if people are dumb I swear to
god)


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>
Yeah a little bit

</details>


# Changelog

:cl: Morrow
add: COs no longer have emote cooldown
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[4e3c9ccc66...](https://github.com/Moonshanks/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Friday 2023-04-21 16:25:30 by roll1d20st

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
## [openai/evals](https://github.com/openai/evals)@[38f40050e9...](https://github.com/openai/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Friday 2023-04-21 16:49:34 by dz-pika

Utility charge eval (#735)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

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
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[b2250e4117...](https://github.com/openai/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Friday 2023-04-21 17:25:41 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

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
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[bf2ebb9dd6...](https://github.com/openai/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Friday 2023-04-21 17:37:38 by Amir DIB

[evals] emoji riddle eval 🎨🤔 (#510)

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
**Emoji riddle**

### Eval description

The evaluation involves solving riddles made up of emojis. The
inspiration for this idea came from reading LinkedIn posts, where I
noticed that nearly 1-4% of the textual information was conveyed through
emojis. Nowadays, emojis are widely used to format text and introduce
color contrasts in texts, even by community managers of large companies.
Furthermore, using emojis is seen as a less formal way of communication
and gives a tone more suitable for social media.


### What makes this a useful eval?

- **Conversational understanding**. the eval test the ability to link
different concepts together which is a crucial feature.

- **Communication**. As GPT is deployed in settings where informal
language is used, interpreting emojis in context will likely become
critical. I think that improvement on this emoji riddle task would make
GPT better at mimicking human-like communication, as it would be able to
understand and respond to various forms of expressions involving emojis.
Emojis and their combinations often carry cultural and social meanings.
By being adept at emoji riddles, ChatGPT would showcase an understanding
of cultural nuances and be more relatable to users.

- **problem-solving**: Emoji riddle solving requires i) extracting
possible meanings and ii) finding the more suitable association of
meaning in the given context (cultural, plateform, etc).

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
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"👀 + 🪚 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["seesaw"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"❤️ + ✉️ = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["love letter"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":" ⌚️ + 🐶 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["watchdog"]}
  ```
</details>

**The Dataset**

![image](https://user-images.githubusercontent.com/22154031/228633727-14480364-4009-45c1-8398-276de7bd86a9.png)

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[66cdb78704...](https://github.com/sourcegraph/sourcegraph/commit/66cdb787045689fd9e1dd09bec7d4e55aa156a20)
#### Friday 2023-04-21 17:48:49 by Stephen Gutekanst

app: experimental Tauri branch (#50620)

This is experimental support for building the Cody App using Tauri. For
an overview of what Tauri is and why I think it will help us with the
App, see [this Slack
message](https://sourcegraph.slack.com/archives/C04F9E7GUDP/p1680729850086159).

### Developing

To try it out, checkout this branch and then in two separate terminals
run:

```
sg start app
```

```
go build \
  -o .bin/backend-aarch64-apple-darwin \
  -tags dist \
  -ldflags '-X github.com/sourcegraph/sourcegraph/internal/conf/deploy.forceType=app' \
  ./enterprise/cmd/sourcegraph

pnpm tauri dev
```

This will open a Tauri window connected to your dev server.

We will follow-up to integrate this into `sg start app` more properly
soon.

### Creating a release

```
./enterprise/dev/app/build-release.sh
```

This will first invoke esbuild to generate the bundles; then it will run
`go build` to create the Go backend binary; and then finally it will
invoke `pnpm tauri build` to produce the macOS app.

Once that command finishes, you'll find the app in
`./src-tauri/target/release/bundle/` (make sure you wait for it to
finish, it will open a window and move things around before it is done.)

## Next steps / things to follow up on

- Familiarize more folks on the team with this code; add better docs
- Make `sg start app` automatically use Tauri, without needing to e.g.
run the `pnpm tauri dev` command separately.
- Use GitHub actions to start building+releasing versions of this in our
CI pipeline
- Make `./enterprise/dev/app/build-release.sh` work on Linux
- Make `./enterprise/dev/app/build-release.sh` produce a Universal macOS
binary, not just for Apple Silicon
- Start hacking, making improvements to the whole experience :)

## Test plan

- [x] Myself, Juliana, and William are happy with this as a starting
point and are able to run/develop with it.
- [x] The changes have limited blast radius, should only affect App and
we'll have more time to make improvements before releasing this version
to any users.
- [x] We can continue releasing the old-style App version to users just
in case we should want/need to create a release before this new version
is ready.

---------

Signed-off-by: Stephen Gutekanst <stephen@sourcegraph.com>
Co-authored-by: William Bezuidenhout <william.bezuidenhout@sourcegraph.com>

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[6eec4e72de...](https://github.com/k21971/EvilHack/commit/6eec4e72deefdf48f5f5db4c35d1d70829d3328b)
#### Friday 2023-04-21 18:17:52 by k21971

Drow as a playable race (initial commit).

This is the initial commit for a new playable race, the Drow. Drow are
also known as dark elves, and share many traits with their
surface-dwelling, light-tolerating cousins.

Drow starting stats and abilities almost exactly match that of elves
(player and monster), including their material hatred of iron. The
differences in this commit that the player will notice, is that Drow
elves start with sleep resistance immediately, and will gain poison
resistance at expereince level five. They can only be chaotic (or
unaligned as an Infidel). Their available roles are Convict, Infidel,
(Dark) Knight, Priest/Priestess, Rogue, Ranger, or Wizard. Male and
female genders are available.

Drow hate orcs just as their fairer cousins do, but they hate normal
elves even more, and elves will grudge drow.

The artifact Grimtooth will warn against drow as well as elves, and can
cause drow extra damage from special attacks. The forged artifact
Shadowblade is now attuned to the drow race.

Droven mummies and zombies have also been created, since drow can
bturned into each. Shopkeepers, priests, and player monsters can also
spawn as the droven race. Shopkeeper pricing adjustments match those of
elves.

This is just the foundational commit. There's a LOT more work to do
here, including drow-specific gear, new material(s), new monsters, and
most importantly how light/dark affect drow. Traditionally, drow can
tolerate light, even that of the sun if conditioned to it over time. But
they prefer the dark, and certain benefits the drow have just aren't
available while in the light. Will need to balance how drow operate in
other fantasy settings vs how it would equate to EvilHack.

---
## [openai/evals](https://github.com/openai/evals)@[aeeb452867...](https://github.com/openai/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Friday 2023-04-21 18:28:57 by Alexander Raul

Algebra word problems (#36)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Algebra Word Problems (algebra_word_problems)

### Eval description

This eval contains some algebra word problems that tend to make gpt 3.5
hallucinate, but wouldn't be out of place on a grade school exam.
Currently has less than 100 examples, but will add if folks think this
is a good eval path to go down.

### What makes this a useful eval?

Poor performance on GPT 3.5 for one, but also would be a great test of
increased logical reasoning capabilities of GPT-4 per the release blog
post.

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
- [] Include at least 100 high quality examples

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

Since we are using Git LFS, we are asking eval submitters to add in
their first 100 JSONL eval lines.

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If it takes 5 machines 5
minutes to make 5 devices, how long would it take 100 machines to make
100 devices?"}], "ideal": "5"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "What is the sum of 60000,
5000, 400, and 3, with the third value multiplied by 5 before performing
the operation?"}], "ideal": "67003"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If the sum of the smallest
and largest of three consecutive even numbers is 28, what is the value
of the second largest number in the series?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "John is trying to fill a 16
oz. bottle with water. If John fills the bottle at 1 oz per second and
the bottle leaks .2 oz per second, how long would it take for John to
fill the bottle?"}], "ideal": "20"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "Annie is training for a
marathon. She has a weekly training routine, training for five hours a
day on some days and 3 hours a day on the other days. She trains a total
of 27 hours in a seven day week. On how many days does she train for
five hours?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "At the start of the year the
ratio of boys to girls in a class is 2 : 1. But now, half a year later,
four boys have left the class and there are two new girls. The ratio of
boys to girls is now 4 : 3. How many students are there altogether
now?"}], "ideal": "28"}
  ```
</details>

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[e1c731c1c2...](https://github.com/CleverRaven/Cataclysm-DDA/commit/e1c731c1c268f8a6817083e167c862929aa6ea23)
#### Friday 2023-04-21 18:54:54 by SolventMercury

Finished Zombie Proficiency & Weakpoint Review (#64194)

* Reviewed all Zombie Weakpoints & Proficiencies

# GENERAL TWEAKS
- Renamed Large Humanoids proficiency to Giant Humanoids, to clarify that it does not apply to somewhat large humanoids, like brutes, and only works on hulks and similar.
- Changed description of Natural Armors proficiency, as many enemies that used this proficiency had something more like a thick hide than any kind of shell.
- Renamed Natural Armor weakpoint set (wps_natural_armor) to wps_armored_hide, to better reflect its purpose and to avoid confusion with the unrelated Natural Armor proficiency, as well as to prevent its misapplication to monsters which have more of a carapace or plate armor thing going on. Natural Armors proficiency should be reserved for uniquely resilient armored foes, like kevlar zombies, whereas armored hide applies to anything with a particularly thick hide, even if not outrageously so.
# ZOMBIES
## ACID ZOMBIES
- Edited description of Corrosive Zombie to hint at its thick hide. Corrosive zombie now also trains Natural Armor proficiency.
- Spitter now has big head weakpoint set, based on description.
## AMALGAMATIONS (Their file is named like the zombie files so I put them here)
- All amalgamations now have intro_biology in their families. This should really be on any living creature of flesh and blood, with exceptions only for stuff like robots, physics-defying nether creatures, extra-dimensional anomalies, and the cafeteria meatloaf. I didn't add this to the cocoons because I wasn't sure if that made sense to do.
- Caustic amalgamation now trains biochemistry, like acid zombies do.
- Charged amalgamation now trains electromagnetics, like zapper zombies do.
## BURNED ZOMBIES
- Fixed a typo in the description for Zombie Kinderlings.
- Zombie Fiend now trains Ossified Exoskeletons. Thought I added that one earlier.
- Scorched Zombie now gets Armored Hide weakpoints due to its "leathery shell".
## FERROUS ZOMBIES
- Removed Armored Hides weakpoint set from rust shell zombie and plated zombie. Could possibly apply Ossified Exoskeletons to them, but I'm not sure.
## COMMAND ZOMBIES
- Slight description tweaks, typo fix.
## FUSED ZOMBIES
- Added proficiencies to Aberration and Dissoluted Devourer. Aberration doesn't give zombie bio because it isn't an actual zombie.
## LAB ZOMBIES
- Removed zombie bio from phase skulker, phase shrike, etc, as they aren't actually zombies.
- Gave phase shrike Ossified Exoskeletons proficiency.
## MISC ZOMBIES
- Added basic proficiencies to zombullfrog, frogmother, zombie nemesis, smoker
- Added basic weakpoints to smoker.
- Headless Horror trains giant humanoids proficiency, based on description.
- Removed Malicious Mane's natural armor training and body armor weakpoints, as it had no natural armor (or armor at all, for that matter).
## RADIATION ZOMBIES
- Added standard proficiencies and weakpoints to all of them.
## SOLDIER ZOMBIES
- Replaced body armor weakpoint set with armored hide.
- Removed military pilot's synthetic armor proficiency
## ANIMAL ZOMBIES
- Gave gastro bufo standard proficiencies and biochemistry.
## CLASSIC ZOMBIES
- Replaced beekeper's body armor weakpoints with armored hide weakpoints
## PUPATING ZOMBIES
- Added expected proficiencies and weakpoints to pupating hulks, as they were the only pupa zombies that didn't have a copy-from pointing to the base type, and did not include this information.
I noticed that most things that disappear on death - boomers, certain cocoons, etc. - tend not to have weakpoints or train proficiencies. Is this an oversight, or is this intentional? For now I left that as is.
## FLYING ZOMBIES
- Gave raptors standard and flying proficiencies.
- Electric raptor also teaches electromagnetics, like electric zombies.

* Removed my Personal Changelog from the Project Directory

* Fixed Fungal Wretch Typos

* Linted zed_amalgamations.json

* MANY Zombie Weakpoint Refinements (& Tests)

- Gave standard weakpoints to standard zombies - manually defined weakpoints for some of the basic zombie models (in zed_misc), like the zombie brute and zombie hulk, is a bit strange, since they have become some of the game's staple enemies. THIS WILL LIKELY EFFECT BALANCE, as these are not only important benchmark enemies, but also copy_from'd by quite a few other enemies. Basic brutes are now somewhat weaker depending on circumstances
- Updated ranged balance test to use enemies with a more uniform form factor, as the high volume of some benchmark enemies lead to counterintuitive results (higher armor enemy taking more damage because it's bigger and easier to shoot). Note that test differences in values aren't all actual "balance changes" but moreso changes to the test itself, so the comparison between old and new isn't 1:1. Test values were only updated on tests that failed for me (I ran the test with 10,000 cycles instead of the usual 200 to be sure the values I got were convergent).
- Added weakpoints and proficiency families to zombies I previously wasn't sure should receive them (mostly ones which self-destruct on death in some way, like boomers). This will make boomers significantly weaker, as they previously had no weakpoints whatsoever.
- Changed boomer stats so no boomer upgrade becomes smaller in volume or lighter in weight than the basic boomer.
- Added an upgrade path for Zombie Miners - they now have a chance to evolve into a shady zombie (most likely), a rust zombie, or just a normal tough zombie, with a ~70% chance not to evolve, on a half-life of 35.
- Rust shell zombies and rust plated zombies get a unique weakpoint category. Similar to bone armor, with the difference that weak points are quite a bit weaker, but the strong point is also a bit stronger.
- Flesh raptors finally have weakpoints, borrowing from the ones used for wasps.
- Removed NOHEAD flag from zombie military pilot, as it very much has a head and there's no reason to believe it to be structurally superfluous, and also fixed them being given erroneous armor weakpoints when they're just in fatigues.
- Lots of other minor weakpoint tweaks/fixes.

* Revert change to ranged tests that made it run 50 times as long.

* Update data/json/monsters/zed_amalgamation.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update data/json/monsters/zed_children.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update all Range Balance Values

* Reverted Weakpoint ID Change

---------

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[09e95cdfbc...](https://github.com/Latentish/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Friday 2023-04-21 19:19:57 by Bjarl

Saloon rework (#1594)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Expands whitesands_surface_camp_saloon to cover a 30x30 footprint and
not be nearly as bad. The previous version had some really glaring
design flaws, like holes in the wall for a bar. On a planet with a
deadly atmosphere. Yeah. Also all the chairs faced the same direction.
![2022 10 31-11 32
50](https://user-images.githubusercontent.com/94164348/199083356-5fabd2c8-0298-4a31-a830-b63dbcd2737f.png)
You can see how it looks. It's not great. 
Here's the new version
![2022 10 31-11 36
20](https://user-images.githubusercontent.com/94164348/199083924-9537beb7-0c74-4c57-9422-60fe953ae0bc.png)
![2022 10 31-11 36
25](https://user-images.githubusercontent.com/94164348/199084468-32d94ec8-846f-42e7-ae33-dc0b52e8b9b8.png)

![dreamseeker_ePSrp5zNFp](https://user-images.githubusercontent.com/94164348/199085448-24879745-650f-4bdc-9b0c-f1d9706ab865.png)
Ignore the patches of error, it's purple grass and doesn't display the
icon in sdmm for some reason.

The major changes are:
Expanding the building's footprint out to 30x30
Moving the loot behind the building, but locking it behind a shovel of
some sort (of which you can go through the ruin to get).
Improving the loot a LITTLE

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] The map loads although I still haven't managed to get it to load
on the proper planet with the spawning verb

## Why It's Good For The Game
The old version was kinda bad. Between the clown and mime masks out
front. The small footprint, and the free guns (also out front). This
solves those issues kinda while making it bigger.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Camp_Saloon has been expanded, expect frontier luxuries if you find
it!
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
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[c21670412d...](https://github.com/Latentish/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Friday 2023-04-21 19:19:57 by Bjarl

New Ruin: The Beach Town (#1572)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a new beach ruin, the abandoned beachside town
![2022 10 10-18 20
10](https://user-images.githubusercontent.com/94164348/194977185-0f35d08e-64c1-459d-94b2-ec6b66137753.png)
![2022 10 10-18 20
00](https://user-images.githubusercontent.com/94164348/194977192-0b93346e-cea0-4fb2-8b66-5ae7319ec3f1.png)

![dreamseeker_Ht2YcvyQbH](https://user-images.githubusercontent.com/94164348/194977254-d0b25aba-ec6b-4e8b-bad5-949a9961cf07.png)

![dreamseeker_KAB6kPSLrP](https://user-images.githubusercontent.com/94164348/194977259-561f8d97-962e-4545-a4b7-1637ad1a7156.png)

![dreamseeker_8Xe7Cuq6NH](https://user-images.githubusercontent.com/94164348/194977262-fb125315-2508-4022-9eda-5ed5078442c9.png)

![dreamseeker_SKJXeK9SOt](https://user-images.githubusercontent.com/94164348/194977268-b4efcd99-0896-4209-8b83-c61c086bda65.png)

![dreamseeker_6Ak0bNoVe5](https://user-images.githubusercontent.com/94164348/194977270-367aaf92-5d6d-4cd8-9827-eba99ec92080.png)

The town is an mostly empty place formerly devoted to tourism and the
beloved art of "chilling out". Facets of the life of its inhabitants
before their disappearance included drinking, grilling, and swimming off
the coast of their fairly large beach. Many interesting things happened
on the boardwalk, and a landing pad was present to allow for small ships
to dock inside the town.

The loot list is sparse here. I intend for this to mostly be a setpiece
for roleplay instead of a loot pinata. There's a good selection of
hydroponics seeds and gear, 2 full bar kits, basic kitchen equipment, an
autolathe, a few PDAs, a lotta wood, and a jukebox. Also donuts.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] Ruin spawns, nothing is out of whack that shouldn't be.

## Why It's Good For The Game
Continues the trend of making planets more good by adding more content
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An oddly empty town has been spotted on beach planets in the area.
Check it out spacers.
add: Random donut spawners, never eat the same donut two days in a row!

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

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[0410075cc8...](https://github.com/Latentish/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Friday 2023-04-21 19:19:57 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[bc92d60cae...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/bc92d60caed7a527c4cb7526d5822e39c8ffccb1)
#### Friday 2023-04-21 19:31:16 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [net-lisias-ksp/DistantObject](https://github.com/net-lisias-ksp/DistantObject)@[3fbacd78ca...](https://github.com/net-lisias-ksp/DistantObject/commit/3fbacd78cac8b21adb6c07dca4143a9ee96e6242)
#### Friday 2023-04-21 19:44:23 by Lisias T

Stupid me #facePalm . KSPe looks for the config file on `<add-on-dir>/PluginData` , not on `<add-on-dir>/Plugins/PluginData`! (and I wrote the damned thing…)
For https://github.com/net-lisias-ksp/DistantObject/issues/25

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3861627c66...](https://github.com/tgstation/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Friday 2023-04-21 20:03:08 by LemonInTheDark

Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) + 
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

---
## [fabricioanciaes/fc2json](https://github.com/fabricioanciaes/fc2json)@[534002d2e9...](https://github.com/fabricioanciaes/fc2json/commit/534002d2e935765c090e0dfd0f0c1408ef67ef6d)
#### Friday 2023-04-21 20:47:49 by Fabricio Anciães

FRM JSON PACK - 20 APR 2023 (V11)

Sorry for the huge delay, was a little bit busy but I'm back with some fixes:

Arcade (fixes):
dinore,mslug3lw

Arcade (new):
ffightaec2,kf2k2ps2b,kof98eck20,mslug5d,samsh5pf,teot,avengrgsbh,captre,dinoares,dinocunp,dinocx3,dinohced,dinombull,dinopuni,dinox5,fatfurspbs,fatfury3bh,ffightaemgc,jurass99p,kf2k3ps2sp,kof2000otc,kof2001ru,kof2k2plus,kof2kxxx,kof96rss,kof97evn,kof97inv,kof98bc2nd,kof98bc2k2,magdrop3te,sailormnrot,sfa2uhc,sfiii3ws,sfiii4fs,sfiiibh,sfpp,umk3p,xmcotan,xmvsfcph

Genesis (new):
sor2fnr,fightvengt,punisor,sonic3kbrc,sor2cc,sor2em,sor2ffc20,sor2tncha,sor2tnwoa,sor2tww,sor2wof1k,tmnttsorp,insanepain,tmntsrr

NES (new):
smbtwopla,ducktales2tp,kartfighter,skartfighter,hackmatch,nekkestrbasen,tetristpg,famista93e,tetristpn

SMS (new):
alexkidd3f

SMS (fixes):
voyage

Arcade (fixes):
dinore,mslug3lw

Arcade (new):
ffightaec2,kf2k2ps2b,kof98eck20,mslug5d,samsh5pf,teot,avengrgsbh,captre,dinoares,dinocunp,dinocx3,dinohced,dinombull,dinopuni,dinox5,fatfurspbs,fatfury3bh,ffightaemgc,jurass99p,kf2k3ps2sp,kof2000otc,kof2001ru,kof2k2plus,kof2kxxx,kof96rss,kof97evn,kof97inv,kof98bc2nd,kof98bc2k2,magdrop3te,sailormnrot,sfa2uhc,sfiii3ws,sfiii4fs,sfiiibh,sfpp,umk3p,xmcotan,xmvsfcph

Genesis (new):
sor2fnr,fightvengt,punisor,sonic3kbrc,sor2cc,sor2em,sor2ffc20,sor2tncha,sor2tnwoa,sor2tww,sor2wof1k,tmnttsorp,insanepain,tmntsrr

NES (new):
smbtwopla,ducktales2tp,kartfighter,skartfighter,hackmatch,nekkestrbasen,tetristpg,famista93e,tetristpn

SMS (new):
alexkidd3f

SMS (fixes):
voyage

SNES (fixes):
zenprow,7thsaga,2020bb,acenerae,actrais2j,actrais2u,aerofgt,airdiverj,airdivr2,ajmajonm,andrindy,aokiden,aressh3,astobelx,avspu,ballz3d,barbiesm,barbvac,barkleyu,basload2,bassmc,batblaz,batlcars,batlsoc2,bdodge2,bikedais,bingbing,bluecrys,bof,bofja,brainlrd,brandish,brawlbrou,bretthu,buckrog,bugsbrabu,capcomss,cdalecup,chesterw,contraspd,crayon,ctribe,ctsuba4,daibakjd,daikokaia,daimono2,daimonoga,ddragon5u,deaddanc,dennisu,dmasteru,dokap321a,dolkusay,doraemn3,doraemona,dquest5,dquest12,dreambas,dstall2,ejimu,elfaria,elnard,esbua,estpoli2,exhaust2,f1roc2,fatfury2u,fatfuryu,ffant2a,ffant3a,ffant4ja,ffant5j,ffant6j,ffantmqa,ffantmqj,ffight2u,fghthist,finalstr,firembmn1,fireprw3a,fireprwsa,flashbj,forms95,frontmisa,garou2a,garoua,garousp,gbattle3,gbattle4,genchohi,ggoemkirb,ggoemon2,ggoemon3a,gindamapa,giseiha,gndmxdim,gogoack2,gouketsu,guts,haristad,haristd2,haruaug2,hiryukgf,hiryukhv,homeimpr,itadaki2,jbsuperb,jikkscr2a,jlexct94a,jlexct95,jlprime2,jlssocr,juteisen,karatebu,kawanus2,kidkleet,kingarth,kirbybow,kishinko,koryuki,kotm2j,lastbib3,libertyj,lobo,lockon,lordmonaa,madara2,madoum,majtnseib,mbomber,megamnxua,metalmaru,mickeym2,militia,mjtaika2a,mku,momodhap,monopol2,moritas2,moritash,mother2,mspacmanu,naruhodo,nbaliv96u,nflpro94,niceshot,ninjawaru,pachimo2,pacman2u,paladin,pga96ua,pgaua,picrosv1a,picrosv4a,pinkie,pocky2u,populus2j,powerhir,powyak2b,prinmak,ranmabak,ranmahb2,riserobou,robotrek,rockmans,rockmnx2,rockmnx3,rocko,rokudena,roman3k3,runsaberu,ryukokena,sailormn,sailorsbze,sailorsf,samshou,samspir,sangoku3a,sangoku4a,sanspo,sbm2,sbombmn3j,sdgungx,sf2tua,sf2u,sfamist5,sgenjin,shinmt2b,shodaneka,shotok94,shotoku2,shounin,shushoku,sjinsei2a,sjinsei3a,sjinseia,skeiba2,slamdnk2,slamdunk,slammastu,slayers,sloopzj,smetroidu,smkartu,spleagu3,spleagu4,spleague,spuyopb,srobotex,ssf2u,sshogi2,starocn,street95,super3db,supermjte,superozup,supf1c2,supf1cg,suprinin,suzuka8,tactsocr,taikoris,targa,tecmosbw,teiketsua,tengaim0,tg3kj,tg3ku,tmnttfce,tophant,topman2,ultfight,umizurim,vgundam,votoms,wagyanp,wayneg,winpost2,wizardr6,xak,yokoms2,yokozunaa,ys4

There were some updates to hacks and other stuff (mostly thanks to tobemorecrazy)

---
## [peff/git](https://github.com/peff/git)@[6e89af7ad4...](https://github.com/peff/git/commit/6e89af7ad433e7139ead72db26da0f9b72bf80c3)
#### Friday 2023-04-21 21:59:00 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

---
## [peff/git](https://github.com/peff/git)@[46a6ac2d17...](https://github.com/peff/git/commit/46a6ac2d178ad72a2d1d15c2d06d149352a4a384)
#### Friday 2023-04-21 21:59:04 by Jeff King

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
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[54bf3808b8...](https://github.com/Monkestation/Monkestation2.0/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Friday 2023-04-21 23:04:01 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [thenetguy/gpt4all-ui](https://github.com/thenetguy/gpt4all-ui)@[cbf446b3e2...](https://github.com/thenetguy/gpt4all-ui/commit/cbf446b3e28f4e53791f968c20b6888b4c40c9e8)
#### Friday 2023-04-21 23:18:25 by Richard Rosario

Update README.md (This really bugged me sorry lol)

got rid of the doubling of "GitHub Repository" as the hyperlink text does the job of rendering the text and providing the link. I'm sure it was a typo no biggie, honestly a super trivial edit I'm aware but it was driving me crazy!

*from this:*
If you are interested in learning more about this groundbreaking project, visit their Github repository [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

*To this:*

If you are interested in learning more about this groundbreaking project, visit their [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

---
## [ScratKnapp/conscriptrp](https://github.com/ScratKnapp/conscriptrp)@[876e25d72f...](https://github.com/ScratKnapp/conscriptrp/commit/876e25d72f7eed257a3cd1bd374a3ee1f01e9fd1)
#### Friday 2023-04-21 23:22:29 by unknown

Holy fucking shit fuck this EOW iconcam it's so over ;-;

---
## [scoopapa/pokemon-showdown-client](https://github.com/scoopapa/pokemon-showdown-client)@[be9a95cbc6...](https://github.com/scoopapa/pokemon-showdown-client/commit/be9a95cbc683c04c6ead95d5643c7ea551607a56)
#### Friday 2023-04-21 23:55:52 by Guangcong Luo

Fix bugs caused by Preact update

The new Preact version seems to have broken a lot of low-level
magic we used. We plausibly shouldn't be using such low-level magic
in the first place, but that's a conversation for another day.

In particular:

1. `preact.render` seems to replace all of `containerNode`'s contents
   if `replaceNode` isn't passed (previously, it would append a child).
   This is an insane thing to change without any documentation... Maybe
   I'm misunderstanding it?

2. Making a button value an uncontrolled form was a pretty big hack
   in the first place, but at least it worked. Now that it doesn't,
   we're giving up and switching to controlled forms, which makes the
   code a lot nicer, fixes a bug, and I should probably have just done
   in the first place.

---

