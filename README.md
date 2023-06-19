## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-18](docs/good-messages/2023/2023-06-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,783,836 were push events containing 2,620,870 commit messages that amount to 148,299,216 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[c7f57ea1a4...](https://github.com/OrionTheFox/tgstation/commit/c7f57ea1a46905e7330b5bde2f50d730530c6e6b)
#### Sunday 2023-06-18 00:25:35 by MrMelbert

Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[bbba8b82d2...](https://github.com/Mu-L/NetHack/commit/bbba8b82d2f3435fe6eba546773fe213299c5308)
#### Sunday 2023-06-18 00:56:20 by PatR

fix issue #1062 - monster hiding messages

Reported by Umbire:  if a statue of a hider-under was activated by
a statue trap, it would hide underneath its own statue.  Also, the
hero saw a snake hide under unseen submerged kelp.

Both of those things were exposed by new "you see <monster> hide"
message rather than caused by it.  It also led to the [re-]discovery
that an existing monster hiding under a statue that was a not-yet-
triggered trap prevented the trap from producing a monster.

This redoes yesterday's can't-hide-under-statue change:  hiders can
hide under statues again, but they can't hide under anything at trap
locations.  [Pits containing one or more objects are an exception,
although it seems silly that a hero is prevented from falling into
one by the presence of a tiny creepy-crawly hiding under a ring or
dart in there.]  So, hider-underers won't be able to interfere with
statue traps by being present at the trap location.  [Trappers and
lurkers-above probably need a similar restriction; I didn't look.
They avoid trap spots rather than get lured to such by objects.]

It also prevents newly created hider-underers from becoming hidden
as part of the their creation (except when that creation is part
of level creation) whether their creation uses up an object (statue
activation, egg hatching) or there are simply other items present.
That will prevent statue of a hider producing a monster that hides
under the activated statue (which was happening due to the sequence
create monster, transfer any statue contents to monster inventory,
destroy statue).

The can't-hide-under-statues code has been repurposed to prevent
hiding under gold pieces unless there are at least 10 (arbitrary
threshold) of those or they're in a pile with some other object(s).

Sea monsters hide in water regardless of the presence of objects.
Prevent other swimmers from hiding under objects at water locations.
Such creatures don't have gills and shouldn't be able to stay
submerged in hiding for an arbitrary length of time.  [No exception
is made for non-breathers.  The overlap between swimmers and hider-
underers is limited to small snakes, even though it is feasible for
a creature wearing an amulet of magical breathing to polymorph into
one.  Heros don't spend enough time underwater to worry about snakes
hiding under kelp or thrown junk.]

Lastly, alter the "suddenly, you notice a <monster>" message if
monster-vs-monster activity causes one you've just seen going into
hiding comes back out again without any intervening messages.  [I'm
not sure whether something similar is needed for the "Wait.  There's
something there" message in the you-vs-monster case.]

Fixes #1062

---
## [Afterglow-Ss13/afterglow-ss13](https://github.com/Afterglow-Ss13/afterglow-ss13)@[887388fa35...](https://github.com/Afterglow-Ss13/afterglow-ss13/commit/887388fa35b6ec2a98ec530df7cc5f59d4643c52)
#### Sunday 2023-06-18 01:21:36 by Zephyr

Merge pull request #111 from Afterglow-Ss13/sani

fuck you

---
## [kensei18/gqlgen](https://github.com/kensei18/gqlgen)@[43b56cbaf3...](https://github.com/kensei18/gqlgen/commit/43b56cbaf3f1de1d1ad379055ab1de157592cf38)
#### Sunday 2023-06-18 01:37:09 by Ben Kraft

Forward `go mod tidy` stdout/stderr

This is a command that can fail (in my case I think for stupid reasons
in a hell of my own construction, but nonetheless).  Right now we just
get
```
$ go run github.com/Khan/webapp/dev/cmd/gqlgen
tidy failed: go mod tidy failed: exit status 1
exit status 3
```
which is not the most informative.  Now, instead, we'll forward its
output to our own stdout/stderr rather than devnull.

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[988a6dcc21...](https://github.com/DesmontTiney/tgstation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Sunday 2023-06-18 02:09:36 by YehnBeep

Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[803658dc30...](https://github.com/DesmontTiney/tgstation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Sunday 2023-06-18 02:09:36 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [larryv/dotfiles](https://github.com/larryv/dotfiles)@[97d1824f3f...](https://github.com/larryv/dotfiles/commit/97d1824f3f5368c24263fab48ebf64ce8226397e)
#### Sunday 2023-06-18 02:22:19 by Lawrence Velázquez

Convert indentation from spaces to tabs

I've long favored four-space indentation but find Matt Wilcox's pro-tab
counterargument [1][2] compelling, if needlessly condescending:

    This is your occasional reminder:
    Tabs are what should be used for indentation.

    Why?  Because spaces for indentation are:

    - Harder for people using assistive technology
    - Harder for people with reading comprehension issues who want more
      indentation.

    The tab is *user customisable* to be any level of indentation per
    tab character.  It is the semantically correct character.

    Please; use tab characters in any public code.  If you don't like
    how "deep" they are; adjust your editor's rendering.

    (If you are already cringing or railing against this idea because it
    would look weird to you... have a deep think.  A real deep think.)

    Spaces as indentation are self-centred and selfish.  They enforce
    *your* preference on others, when tabs would allow you *and others*
    their own preference of indentation for the same code - because they
    are user configurable.

    Yes, all editors can configure the tab to render as 1, 2, 4, 6, 8 or
    any number of spaces wide.  Learn your editor.

I've always prioritized my aesthetic preferences, deeming indentation of
two columns to be too shallow and eight, too deep.  I know tab stops are
widely configurable, but I stubbornly insist on viewing tabs at their
"natural" width of eight columns because I want to see them as everyone
else does.  (Who actually changes their tab stops?  Come on.)  Thus, the
only way to get al dente indentation that looks the same to everyone is
to use four spaces.

I've thought about switching to tabs before.  The Linux kernel coding
style guide espouses 8-column indentation on the grounds that it's very
clear and highlights excessively deep nesting [3] -- interesting ideas,
but not so interesting that I'd switch teams.

Well, Wilcox's accessibility angle has convinced me, although I still
think 8 columns is a bit much.  I'll get over it.

Reindent most files using tabs.  Do not reindent makefile command lines
because different make(1) implementations treat leading tabs differently
(other than on the first line).  Do not reindent (most) prose because it
looks awful, and I can't bring myself to do it (code is already ugly, so
it's easier to swallow).

  [1]: https://mstdn.social/@mattwilcox/110451855256437660
  [2]: https://mstdn.social/@mattwilcox/110451875354616267
  [3]: https://www.kernel.org/doc/html/latest/process/coding-style.html#indentation

---
## [YellowSegment/Game](https://github.com/YellowSegment/Game)@[ab1ed4c6cb...](https://github.com/YellowSegment/Game/commit/ab1ed4c6cbb822fb027b4eedb6baf25c53023741)
#### Sunday 2023-06-18 03:11:22 by YellowSegment

Order UI change and Desktop UI changes

Implemented the ability to use Inaccusmart bullshit website or whatever it is. Some weird shit. But I did it to make this bitch happy. And order ui is now a little diner tray thing. Some weird thing Will did

---
## [skeyuui/russ-station](https://github.com/skeyuui/russ-station)@[912e843f53...](https://github.com/skeyuui/russ-station/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Sunday 2023-06-18 04:07:37 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[4198043030...](https://github.com/git-for-windows/git/commit/41980430300fd882751ef8954dee09c0f69ddbf6)
#### Sunday 2023-06-18 04:28:15 by Johannes Schindelin

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
## [dallmeyer/jak-project](https://github.com/dallmeyer/jak-project)@[c249dbc437...](https://github.com/dallmeyer/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Sunday 2023-06-18 06:48:36 by water111

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
## [ExactExampl/kernel_bonito-4.9](https://github.com/ExactExampl/kernel_bonito-4.9)@[cf74a464bd...](https://github.com/ExactExampl/kernel_bonito-4.9/commit/cf74a464bd819d87e4e6bfc7483c32efc12c99fd)
#### Sunday 2023-06-18 07:14:53 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

---
## [dvsdude2/doom](https://github.com/dvsdude2/doom)@[5830e6dd1e...](https://github.com/dvsdude2/doom/commit/5830e6dd1e8751c3dc607433f171960e364fbdfb)
#### Sunday 2023-06-18 08:06:39 by dvsdude2

enough changes warranted a snapshot

config.org
alot of this is aesthetics after a change to header size
won't bother mentioning

@@ -53,7 +53,8 @@
- thinking that I might be able to get away with out some requires,
but now see they are needed so it was an experiment and think it was
revealing and no need to expand this any further than the two I tried

@@ -134,15 +135,17 @@
- here I added a function to auto chom +x files with shebangs

@@ -189,10 +192,9 @@
- thought appending this to the core function might help when using a
daemon. but it did not get it to start with it so... no didn't work

@@ -209,12 +211,14 @@
- new package "org-web-tools" it grabs text body of web pages

@@ -249,8 +253,8 @@
- changed keybinding "create link to file" better remembering

@@ -682,72 +687,36 @@
- tring to start over with the cape config try a fresh one

@@ -823,15 +792,15 @@
- decided that I like and should have "consult-ripgrep"
needed to do some shuffing of other command I had installed
opted to make a prefix to move them to

@@ -966,9 +937,20 @@
- replaced tecosaur-config settings back to original for spray
gets rid of the cursor in some buffers that need it

@@ -1100,11 +1082,19 @@
- tried to do a remap of a key to something more useful my opinion
and add one for treemacs, did need there was one built in
neither of these was useful will need to revisit

@@ -1125,8 +1115,6 @@
- still tring to get a decent end-of-line function, this one was
stepping on anouther function so need to revist this as well

---
## [SaikiaP/Projects](https://github.com/SaikiaP/Projects)@[957c66e799...](https://github.com/SaikiaP/Projects/commit/957c66e799d23c45c44011d36adaf73c1f01cbb2)
#### Sunday 2023-06-18 08:22:03 by SaikiaP

Add files via upload

This is a hotel booking dataset where I have tried cleaning the data:

hotelHotel (H1 = Resort Hotel or H2 = City Hotel)
is_canceled=Value indicating if the booking was canceled (1) or not (0)
lead_time= Number of days that elapsed between the entering date of the booking into the PMS and the arrival date
arrival_date_year =Year of arrival date
arrival_date_month =Month of arrival date
arrival_date_week_number Week number of year for arrival date
arrival_date_day_of_month=Day of arrival date
stays_in_weekend_nights=Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
stays_in_week_nights=Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
adults=Number of adults
children=Number of children
babies=Number of babies

meal=Type of meal booked. Categories are presented in standard hospitality meal packages: 
Undefined/SC – no meal package; BB – Bed & Breakfast; HB – Half board (breakfast and one other meal – usually dinner); FB – Full board (breakfast, lunch and dinner)

country=Country of origin. Categories are represented in the ISO 3155–3:2013 format
market_segment=Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”
distribution_channel=Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”
is_repeated_guest=Value indicating if the booking name was from a repeated guest (1) or not (0)
previous_cancellations=Number of previous bookings that were cancelled by the customer prior to the current booking
previous_bookings_not_canceled=Number of previous bookings not cancelled by the customer prior to the current booking
reserved_room_type=Code of room type reserved. Code is presented instead of designation for anonymity reasons.

assigned_room_type
Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons.

booking_changes=Number of changes/amendments made to the booking from the moment the booking was entered 
on the PMS until the moment of check-in or cancellation

deposit_type=Indication on if the customer made a deposit to guarantee the booking. 
This variable can assume three categories: No Deposit – no deposit was made;
 Non Refund – a deposit was made in the value of the total stay cost; Refundable – a deposit was made with a value
  under the total cost of stay.
  
agent=ID of the travel agency that made the booking
company=ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons
days_in_waiting_list=Number of days the booking was in the waiting list before it was confirmed to the customer
customer_type

Type of booking, assuming one of four categories:
Contract - when the booking has an allotment or other type of contract associated to it; Group – when the booking is associated to a group; Transient – when the booking is not part of a group or contract, and is not associated to other transient booking; Transient-party – when the booking is transient, but is associated to at least other transient booking
adr=Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of staying nights
required_car_parking_spaces=Number of car parking spaces required by the customer
total_of_special_requests=Number of special requests made by the customer (e.g. twin bed or high floor)
reservation_status=Reservation last status, assuming one of three categories: Canceled – booking was canceled by the customer; Check-Out – customer has checked in but already departed; No-Show – customer did not check-in and did inform the hotel of the reason why
reservation_status_date=Date at which the last status was set. This variable can be used in conjunction with the Reservation Status to understand when was the booking canceled or when did the customer checked-out of the hotel

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[59dd02fe7c...](https://github.com/ZephyrTFA/tgstation/commit/59dd02fe7cd54b4153b294ccb965249c587f189d)
#### Sunday 2023-06-18 08:48:33 by san7890

Welding Fuel Tanks now log_bomber when hit by projectile (#75885)

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---
## [jntrnr/nushell](https://github.com/jntrnr/nushell)@[2e01bf9cba...](https://github.com/jntrnr/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Sunday 2023-06-18 09:27:13 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

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
## [sidereumare/evals](https://github.com/sidereumare/evals)@[170dfd886c...](https://github.com/sidereumare/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Sunday 2023-06-18 09:36:43 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

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
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [sidereumare/evals](https://github.com/sidereumare/evals)@[ef1f0ebe0e...](https://github.com/sidereumare/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Sunday 2023-06-18 09:36:43 by Josh Gruenstein

Add SVG understanding eval (#786)

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
`svg_understanding`

### Eval description

The model is provided with the contents of an SVG path (anywhere from
~1000 to ~8000 characters) of a simple object (eg `frog`, `banana`) and
is asked to provide the label.

### What makes this a useful eval?

This is a test of visual understanding and mental modeling. A motivated
human could succeed on these evals with enough time and a piece of graph
paper: in theory, a sufficiently advanced LLM could have the in-context
capacity to do this on the fly.

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

This uniquely tests the ability to incrementally build visual models:
eg, the ability of the LLM to both "draw" and visualize that "drawing".

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
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6110 12794 c-744 -50 -1284 -157 -1875 -371 -1796 -650 -3199
-2050 -3853 -3843 -186 -510 -302 -1037 -359 -1625 -21 -224 -24 -827 -5
-1045 84 -957 332 -1788 774 -2595 623 -1137 1607 -2078 2780 -2656 720
-354 1441 -556 2273 -636 224 -21 827 -24 1045 -5 741 65 1376 221 2018
493 2051 871 3514 2775 3826 4979 48 336 60 510 60 895 1 366 -7 507 -45
810 -168 1357 -769 2626 -1711 3612 -536 561 -1129 998 -1809 1333 -718
354 -1450 559 -2264 635 -159 15 -727 28 -855 19z"}], "ideal": "circle"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M4495 12298 c-604 -535 -1486 -866 -2660 -998 -331 -37 -854
-70 -1104 -70 l-101 0 -2 -415 -3 -416 30 -29 30 -29 735 -4 c620 -3 753
-7 850 -21 149 -22 254 -50 316 -86 82 -46 123 -142 161 -372 16 -95 18
-371 21 -3663 2 -2593 0 -3591 -8 -3675 -44 -446 -177 -714 -416 -838 -279
-144 -663 -202 -1350 -202 l-330 0 -27 -28 -27 -28 0 -389 0 -389 27 -28
27 -28 3386 0 3386 0 27 28 27 28 0 390 0 390 -27 26 -28 26 -390 5 c-415
5 -557 17 -779 62 -212 43 -367 103 -480 187 -156 115 -260 347 -312 693
-17 114 -18 350 -21 5005 l-3 4884 -27 28 -27 28 -410 -1 -411 0 -80
-71z"}], "ideal": "1"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6040 12794 c-19 -2 -91 -9 -160 -14 -245 -21 -529 -65 -1240
-190 -399 -70 -593 -100 -654 -100 -91 0 -475 51 -1126 149 -556 84 -788
109 -1075 118 -621 18 -1014 -108 -1310 -418 -344 -360 -490 -941 -472
-1874 21 -1042 173 -1862 619 -3340 l90 -300 -11 -205 c-43 -764 -28 -1853
40 -2845 108 -1585 337 -3026 550 -3473 37 -77 67 -115 184 -238 70 -73
167 -82 258 -24 56 36 102 96 166 220 317 616 732 2551 901 4200 32 314 89
451 257 623 371 379 1029 373 1387 -13 70 -77 106 -129 155 -227 57 -114
79 -196 91 -340 120 -1375 535 -2972 1031 -3963 188 -374 311 -513 458
-514 140 -1 221 106 316 420 232 762 480 2366 595 3849 58 739 82 1376 79
2060 l-2 490 55 115 c228 475 421 1043 527 1550 123 593 169 1196 158 2084
-5 445 -16 597 -58 836 -149 854 -590 1292 -1369 1360 -106 9 -358 11 -440
4z"}], "ideal": "tooth"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M12395 6223 c-133 -27 -295 -150 -356 -269 -13 -27 -40 -68
-59 -90 -19 -23 -57 -79 -84 -125 -161 -274 -369 -539 -542 -695 -191 -171
-304 -231 -559 -298 -499 -132 -725 -257 -1170 -646 -321 -281 -608 -477
-941 -643 -536 -267 -1054 -408 -1735 -473 -236 -23 -800 -23 -1064 0 -701
60 -1256 173 -1940 396 -951 310 -1915 784 -3057 1503 -109 68 -185 109
-220 118 -84 22 -257 17 -358 -10 -102 -28 -256 -99 -289 -135 l-24 -25 21
-88 c27 -115 108 -357 170 -514 253 -633 609 -1222 1069 -1772 164 -196
545 -577 742 -741 986 -822 2174 -1317 3561 -1481 340 -40 485 -48 880 -48
399 -1 546 8 859 49 965 125 1872 497 2606 1068 309 240 645 572 886 876
386 487 682 1048 788 1495 30 130 44 191 101 470 61 292 121 457 263 720
115 214 230 376 365 517 63 65 90 85 176 127 81 39 117 65 183 128 92 89
108 118 93 171 -9 33 -7 39 17 64 l26 27 -22 43 c-12 24 -64 84 -119 136
-116 110 -204 158 -267 145z"}], "ideal": "banana"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M3920 12790 c-1230 -72 -2320 -649 -3052 -1616 -968 -1280
-1142 -3010 -441 -4408 203 -405 432 -712 913 -1221 556 -589 764 -887 945
-1350 102 -264 141 -353 194 -448 l50 -88 -30 -44 c-62 -92 -109 -251 -109
-370 0 -114 44 -261 106 -357 17 -26 17 -28 -14 -95 -43 -94 -62 -181 -62
-292 0 -142 37 -265 107 -359 l25 -34 -35 -76 c-50 -108 -69 -191 -70 -302
-1 -155 39 -275 126 -382 l47 -58 0 -82 c0 -110 21 -193 77 -308 38 -79 59
-108 132 -180 68 -69 103 -95 171 -128 87 -44 203 -75 324 -89 l70 -8 17
-83 c47 -216 205 -374 404 -402 115 -16 827 -12 908 5 202 42 340 188 385
404 l16 80 66 6 c235 22 429 117 548 268 108 139 152 251 160 416 5 111 5
114 38 150 45 48 99 152 118 227 20 79 21 233 0 320 -8 37 -31 102 -50 144
l-35 77 39 61 c66 102 87 185 86 337 0 114 -4 140 -27 210 -15 44 -36 95
-46 114 l-18 34 34 55 c46 78 70 147 84 245 21 140 -16 308 -95 440 l-34
57 59 114 c33 63 103 222 155 353 147 366 255 566 429 798 132 176 245 304
609 690 366 388 516 578 701 885 550 915 713 2023 454 3090 -186 763 -583
1473 -1129 2020 -668 669 -1520 1069 -2480 1165 -185 19 -667 27 -870
15z"}], "ideal": "lightbulb"}
  ```
</details>

---
## [sidereumare/evals](https://github.com/sidereumare/evals)@[2ffd4b57de...](https://github.com/sidereumare/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Sunday 2023-06-18 09:36:43 by Andrew Kondrich

add more logging (#964)

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

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [ngogiaphat/GettingStartedWithSvelte](https://github.com/ngogiaphat/GettingStartedWithSvelte)@[ad01b1537c...](https://github.com/ngogiaphat/GettingStartedWithSvelte/commit/ad01b1537c064f80efb93149d7f0177567bbdeee)
#### Sunday 2023-06-18 10:12:28 by Samuel Seo

$types and $lib is not working and them is damned !!!!! fucking shit

---
## [ngogiaphat/GettingStartedWithSvelte](https://github.com/ngogiaphat/GettingStartedWithSvelte)@[c7b4406525...](https://github.com/ngogiaphat/GettingStartedWithSvelte/commit/c7b4406525d96e796955447a8f50e8c168267b11)
#### Sunday 2023-06-18 10:13:23 by Samuel Seo

$types is not working and is damned !!!!! fucking shit

---
## [TOBKA4/cmss13](https://github.com/TOBKA4/cmss13)@[e8f53984c1...](https://github.com/TOBKA4/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Sunday 2023-06-18 10:38:08 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [utahabestgirl/kernel](https://github.com/utahabestgirl/kernel)@[b2b27b6899...](https://github.com/utahabestgirl/kernel/commit/b2b27b6899ab5dad667ed4b015ec771caaad6d87)
#### Sunday 2023-06-18 10:43:13 by Christian Brauner

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
## [KiulWasTaken/kiulabilities](https://github.com/KiulWasTaken/kiulabilities)@[565d6c5226...](https://github.com/KiulWasTaken/kiulabilities/commit/565d6c5226485d3883f4c17c4d16bd20b7901966)
#### Sunday 2023-06-18 11:59:37 by PatriciaChips

Did stuff, not listing fuck you

Added ABILITY-TEMPLATE

---
## [originalBlank/Fivem_Ghost_FaceHoodie](https://github.com/originalBlank/Fivem_Ghost_FaceHoodie)@[40febd536d...](https://github.com/originalBlank/Fivem_Ghost_FaceHoodie/commit/40febd536de4a76dffc18d25f68b43c0b9cf609a)
#### Sunday 2023-06-18 11:59:45 by originalBlank

GhostFace

Title: Retexture Mod for FiveM

Mod Description:
The Retexture mod for FiveM breathes new life into your gaming experience by revamping textures within the game world. This mod, created by Official_Blank, enhances the visual quality of various elements, making them more immersive and realistic. With meticulously reimagined textures, this mod is designed to elevate your gameplay and provide a fresh perspective on familiar surroundings.

Bugs and Features:
- Improved Textures: The Retexture mod enhances the quality of textures for objects, vehicles, buildings, and environmental elements, giving them a more refined and detailed appearance.
- Immersive Atmosphere: Enjoy an immersive atmosphere with enhanced textures that add depth and realism to the game world, making your gameplay experience more engaging.
- Compatibility: The mod is designed to be compatible with most other mods and should work seamlessly with your existing FiveM server setup.
- Stability: The Retexture mod is thoroughly tested to ensure stability and minimize the occurrence of bugs or glitches that could affect gameplay.

Installation Instructions:
1. Ensure you have OpenIV installed on your computer. You can download it from the official website.
2. Download the Retexture mod files from the official source or the designated website.
3. Locate your FiveM server installation directory.
4. Open the FiveM server directory and navigate to the "resources" folder.
5. Create a new folder named "retextured" (or any other name of your choice).
6. Extract the contents of the Retexture mod files into the newly created "retextured" folder.
7. Launch OpenIV and navigate to the FiveM server directory within the application.
8. Use OpenIV to import the modified textures from the "retextured" folder into the appropriate game files or directories. Make sure to back up the original files before replacing them.
9. Once the retextured files are imported, save the changes and close OpenIV.
10. Restart your FiveM server for the mod to take effect.

Credits and Permissions:
- The Retexture mod was created by Official_Blank. Please credit them when using or sharing this mod.
- The mod may include assets or resources from other creators. Ensure you adhere to their respective permissions and credits if required.
- Please note that redistribution or modification of the Retexture mod without explicit permission from Official_Blank is prohibited.
- If you encounter any issues or have questions regarding the mod, please contact Official_Blank for assistance.

Enjoy the enhanced visuals and immersive experience provided by the Retexture mod for FiveM. Dive into a world with improved textures, and have an incredible gaming journey!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8788e48378...](https://github.com/tgstation/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Sunday 2023-06-18 12:14:07 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [dcunited001/ellipsis](https://github.com/dcunited001/ellipsis)@[fe38104ee2...](https://github.com/dcunited001/ellipsis/commit/fe38104ee283d4df83906318a87825a533b20895)
#### Sunday 2023-06-18 12:29:13 by David Conner

add PFSense examples.

Coming from Cisco, I fucking hate that there is not a first-party solution for
this. I can't stand the browser and I cant stand not seeing my logic in plain
text.

... I also can't stand Cisco because I have this 2911 router that is a FUCKING
BRICK because I need the smartnet to get a non-compromised IOS image. FUCK YOU
CISCO.

---
## [petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023)@[75c79c734a...](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023/commit/75c79c734a3e18130a68665bfc14bc757118bc7d)
#### Sunday 2023-06-18 12:55:40 by Petre Ro

7.2 Overriding the Selected Fields
 - Let's think: the data we're querying for will ultimately come from the FortuneCookie entity... so open up FortuneCookieRepository so we can add a new method there. How about: public function countNumberPrintedForCategory(Category $category): int.

 The query starts pretty much like they all do. Say $result = $this->createQueryBuilder('fortuneCookie'). By the way, the alias can be anything. Personally, I try to make them long enough to be unique in my project... but short enough to not be annoying. More importantly, as soon as you choose an alias for an entity, stick with it.

 Ok, we know that when we create a QueryBuilder, it will select all the data from FortuneCookie. But in this case, we don't want that! So, below, say ->select() to override that.

 Earlier, in CategoryRepository, we used ->addSelect(), which basically says:

  Take whatever we're selecting and also select this other stuff.

 But this time, I'm purposely using ->select() so that it overrides that and only selects what we put next. Inside, write DQL: SUM() a function that you're probably familiar with followed by fortuneCookie. and the name of the property we want to use - numberPrinted. And you don't have to do this, but I'm going to add AS fortunesPrinted, which will name that result when it's returned. We'll see that in a minute.

 andWhere() with an Entire Entity
 - Ok, that takes care of the ->select(). Now we need an ->andWhere() with fortuneCookie.category = :category... calling ->setParameter() to fill in the dynamic category with the $category object.

 This is interesting too! In SQL, we would normally say something like WHERE fortuneCookie.categoryId = and then the integer ID. But in Doctrine, we don't think about the tables or columns: we focus on the entities. And, there is no categoryId property on FortuneCookie. Instead, when we say fortuneCookie.category we're referencing the $category property in FortuneCookie. And instead of passing just the integer ID, we pass the entire Category object. It actually is possible to pass the ID, but most of the time you'll pass the entire object like this.

 Okay, let's finish this! Convert this to a query with ->getQuery(). Below, if you think about it, we really only want one row of results. So let's say ->getOneOrNullResult(). Finally, return $result.

 Until now, all of our queries have returned objects. Since were selecting just one thing... does that finally change? Let's find out! Add dd($result) and then head to FortuneController to use this. For the show page controller, add an argument FortuneCookieRepository $fortuneCookieRepository. Then below, say $fortunesPrinted equals $fortuneCookieRepository->countNumberPrintedForCategory() passing $category.

 Beautiful! Take that $fortunesPrinted variable and pass it into Twig as fortunesPrinted.

 Finally, find the template - showCategory.html.twig - and... there's a table header that says "Print History". Add some parentheses with {{ fortunesPrinted }}. Add |number_format to make this prettier then the word total.

 Awesome! Since we have that dd(), let's refresh and... look at that! We get an array back with 1 key called fortunesPrinted! Yup, as soon as we start selecting specific data, we just get back that specific data. It's exactly like you'd expect with a normal SQL query.

 If we had said ->select('fortuneCookie') (which is redundant because that's what createQueryBuilder() already does), that would have given us a FortuneCookie object. But as soon as we're selecting one specific thing, it gets rid of the object and returns an associative array.

---
## [petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023)@[4aa094223d...](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023/commit/4aa094223dc08a4b9c4eec7810f49b26b59bb9f4)
#### Sunday 2023-06-18 12:55:40 by Petre Ro

5.1. JOINs and addSelect Reduce Queries

 When we're on the homepage, we see seven queries. We have one to get all the categories... then additional queries to get all the fortune cookies for each category. We can see this in the profiler. This is the main query FROM category... then each of these down here is selecting fortune cookie data for a specific category: 3, 4, 2, 6, and so on.

 Lazy-Loading Relationships
 - If you've used Doctrine, you probably recognize what's happening. Doctrine loads its relationships lazily. Let's follow the logic. In FortuneController, we start by querying for an array of .

 37 lines  src/Controller/FortuneController.php
 class FortuneController extends AbstractController
 {
    public function index(Request $request, CategoryRepository $categoryRepository): Response
    {
        $searchTerm = $request->query->get('q');
        if ($searchTerm) {
            $categories = $categoryRepository->search($searchTerm);
        } else {
            $categories = $categoryRepository->findAllOrdered();
        }
        return $this->render('fortune/homepage.html.twig',[
            'categories' => $categories
        ]);
    }
 }
 In that query, if we look at it, it's only selecting category data: not fortune cookie data. But if we go into the template - templates/fortune/homepage.html.twig - we loop over the categories and eventually call category.fortuneCookies|length.

 17 lines  templates/fortune/homepage.html.twig
    {% for category in categories %}
        <a class="bg-orange-400 hover:bg-orange-500 text-white text-center rounded-full p-4" href="{{ path('app_category_show', {'id':  category.id}) }}">
            <span class="fa {{ category.iconKey }}"></span> <span class="font-bold text-lg">{{ category.name }}</span>  ({{ category.fortuneCookies|length }})
        </a>
    {% endfor %}
 The N+1 Problem
 - In PHP land, we're calling the getFortuneCookies() method on Category. But until now, Doctrine has not yet queried for the FortuneCookie data for this Category. However, as soon as we access the $this->fortuneCookies property, it magically makes that query, basically saying:

  Give me all the FortuneCookie data for this category

 Which... it then sets onto the property and returns back to us. So it's at this moment inside of Twig when that second, third, fourth, fifth, sixth, and seventh query is executed.

 This is called the "N+1 Problem", where you have "N" number of queries for the related items on your page "plus one" for the main query. In our case, it's 1 main query for the categories plus 6 more queries to get the fortune cookie data for those 6 categories.

 This isn't necessarily a problem. It might hurt performance on your page... or be no big deal. But if it is slowing things down, we can fix it with a JOIN. After all, when we query for the categories, we're already joining over to the fortune cookie table. So... if we just grab the fortine cookie data in the first query, couldn't we build this whole page with that one query? The answer is... totally!

 Selecting the Joined Fields
 - To see this in action, search for something first. I'm doing this because it will trigger the search() method in our repository, which already has the JOIN. Over here, since we have five results, it made six queries.

 Okay, we're already joining over to fortuneCookie. So how can we select its data? It's delightfully simple. And again, order doesn't matter: ->addSelect('fortuneCookie').

 That's it! Try this thing! The queries went down to one and the page still works!

 Tip

 You might notice that the fortune cookie count for each category also change. Before, Doctrine executed separate queries to count the related fortune cookies without considering our search term. But after adding addSelect('fortuneCookie'), the ORM uses that data to count instead of making new queries... which includes our search term!

 If you open the profiler... and view the formatted query... yes! It's joining over to fortune_cookie and grabbing the fortune_cookie data at the same time. The "N+1" problem is solved!

 Where does the Join Data Hide?
 - But I want to point out one key thing. Because we're inside of CategoryRepository, when we call $this->createQueryBuilder('category'), that automatically adds a ->select('category') to the query. We know that.

 However now we're selecting all of the category and fortuneCookie data. But... our page still works... which must mean that even though we're selecting data from two tables, our query is still returning the same thing it did before an array of Category objects. It's not returning some mixture of category and fortuneCookie data.

 This point can be a bit confusing, so let me break it down. When we call createQueryBuilder(), that actually adds 2 things to our query: FROM App\Entity\Category as category and SELECT category. Thanks to the FROM, Category is our "root entity" and, unless we start doing something more complex, Doctrine will try to return Category objects. When we ->addSelect('fortuneCookie'), instead of returning a mixture of categories and fortune cookies, Doctrine basically grabs the fortuneCookie data and stores it for later. Then, if we ever call $category->getFortuneCookies(), it realizes that it already has that data, so instead of making a query, it uses it.

 The really important thing is that when we use ->addSelect() to grab the data from a JOIN, it does not change what our method returns. Though later, we will see times when using select() or addSelect() does change what our query returns.

 Ok, so we just used a JOIN to reduce our queries from 7 to 1. However, because we're only counting the number of fortune cookies for each category, there is another solution. Let's talk about EXTRA_LAZY relationships next

---
## [danieljharvey/mimsa](https://github.com/danieljharvey/mimsa)@[e26ca2a932...](https://github.com/danieljharvey/mimsa/commit/e26ca2a9320e5c59b7b12433bc7d36b2cdfa8b99)
#### Sunday 2023-06-18 13:14:55 by Daniel Harvey

Actually typecheck multiple definitions (#962)

* Test module typechecking more throughly

* Damn this shit is fucked

* We need to make these types stricter

* Skippy

* Nice

---
## [Omarley7/DTaaS-Bachelor-new-GUI](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI)@[00134695e9...](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI/commit/00134695e9bce421c8ba7681a535c09d1c4dca39)
#### Sunday 2023-06-18 13:26:00 by Mathias Brændgaard

Add unit tests for Store/AppAccess and Store/UserAccess (#63)

* Add unit tests for Store/AppAccess and Store/UserAccess

* Honestly bullshit codeclimate error.
Would be overly complicated to fix. Even this solution is stupid.
And also updated envUtil to use the same hook, act, assert approach.

* Bullshit løsning

---------

Co-authored-by: Omar <omarg@live.dk>

---
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[53c1e221dc...](https://github.com/ZecHub/zechub/commit/53c1e221dc60694c0cd6594978de020d3e09a23d)
#### Sunday 2023-06-18 13:48:06 by Hardaeborla

Create ZecWeekly - 47

# ZecWeekly #47
Binance Under Investigation in France, ZCash Foundation Launches Zebra 1.0.0, Crypto Detective ZachXBT Faces Defamation Lawsuit
---

Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello ZCashers!! It's another part of the week where we share exciting news and updates from ZCash including news and events happening in the Crypto Space. You can also be a contributor on ZecHub by visiting [ZecHub Github Page](https://github.com/ZecHub/zechub). Also learn more about contributing to ZecHub by watching this [video](https://youtu.be/8eYDTyV39a4) 

We will be delving into updates from ECC about the new release of Zcashd 5. 6.0 without leaving behind the latest development by ZCash Foundation (Zebra 1.0.0). Also we'll be sharing some Cryptocurrency tips and tutorials via the Education Piece section. Remember you can earn some free $ZEC by taking part in our Zecweekly Challenge attached at the end of our newsletter. 

---

## This Week's Education Piece 
In this week education piece, you will be learning about how you can run a full node on ZCashd using Raspberry Pi 4. If you are new to running nodes on ZCash, then you have nothing to worry about as this tutorial covers almost every important things you need to know when it comes to running your own node on zcashd. Visit the link below to get started 

[Raspberry Pi 4: a zcashd Full node guide](https://github.com/ZecHub/zechub/blob/main/site/guides/RaspberryPi4FullNode.md) 
## Zcash Updates


#### ECC & ZF Updates

[ECC released zcashd 5.6.0 today](https://twitter.com/ElectricCoinCo/status/1669135148351119361?t=VRA3a4YMB-fVJrg9A3G89g&s=19) 

[Summarised version of Aborist Call 54 by Jason](https://twitter.com/zksquirrel/status/1669569672360992768?t=Ewrdv8k8_sZu3VJ1A2ErMg&s=19) 

[ZF announces release of Zebra 1.0. 0](https://twitter.com/ZcashFoundation/status/1669058146705326081?t=kT2uc6z8TDo2l_FP3cVo7w&s=19)

[ZF Shares update about ZCon4 for interested participants](https://twitter.com/ZcashFoundation/status/1669433014969835521?t=Pz2VIcTnG786y-P1ELI61g&s=19)

[Explicit details about Zebra from ZF](https://twitter.com/ZcashFoundation/status/1669465539951972353?t=QNXR6ufBrsvjcDH2wBzuCQ&s=19) 


[ZF Shares insight about Rust in building critical privacy infrastructure](https://twitter.com/ZcashFoundation/status/1669748058677030919?t=JdzpMg06b97H4dztGoXJXg&s=19) 


#### Zcash Community Grants Updates

[Join the CGC Candidates Call event](https://twitter.com/ZcashCommGrants/status/1669794745357312017?t=4t4qhXh6aEYAS9r-0HFjJw&s=19) 

[Submit Questions for CGC Candidates](https://twitter.com/zcash_community/status/1668335614993784839?t=yd-pbQQv-wK3g3styiVZRw&s=19) 

[Zcash Community Grants Election Summer 2023](https://twitter.com/zcash_community/status/1667666811955945491?t=NwycncxDGm7Yrda9i-zV2A&s=19)




#### Community Projects
[ZCash Explorer Testnet Edition](https://twitter.com/ZcashExplorer/status/1669415647082864641?t=4kKeqtOnRVnOsjo0pWjOdA&s=19)

[Aiyadt announces @nighthawkapps partnership with Zebra](https://twitter.com/aiyadt/status/1669070325919760385?t=zOWlCZjv_BfXZ7DlLcvPWA&s=19) 

[Checkout the Six available Deework task on ZecHub](https://twitter.com/ZecHub/status/1668665981827264528?t=61LHMJS4Q9dtRF3utuJ8hQ&s=19) 

[Zebra explained in Español](https://twitter.com/zcashesp/status/1669855827438477313?t=DQmq2jmT9dwMbLwil1xyhw&s=19) 

[Save The Date: ZCash Español Party](https://twitter.com/gordonesroo/status/1668985460142530562?t=QNnoOSQchWFFP69cEM8h9g&s=19) 

[Nym is building the next generation of privacy protection and infrastructure](https://twitter.com/zcashesp/status/1669359117167890445?s=19)

[Join ZCash Brazil for Privacy Chat With ZCash](https://twitter.com/zcashbrazil/status/1669500069588893696?t=TtGgOxCM_AmG3cv5rgSjxg&s=19) 

[ZCash Community Meetup Festival in Brazil](https://twitter.com/zcashbrazil/status/1668999785297203202?t=ZlmbQlyJNFYMIqXIpn0m3g&s=19) 

[Zingo shares five reasons to practice financial privacy](https://twitter.com/ZingoLabs/status/1668746421284089861?t=c1AnNFSeyqHBSuC8UDsUkg&s=19) 


#### News & Media
[Crypto Detective ZachXBT Faces Defamation Lawsuit](https://www.coindesk.com/business/2023/06/16/crypto-detective-zachxbt-faces-defamation-lawsuit/?utm_medium=referral&utm_source=rss&utm_campaign=headlines) 

[Binance Under Investigation in France](https://www.google.com/amp/s/www.coindesk.com/policy/2023/06/16/binance-under-investigation-in-france-accused-of-aggravated-money-laundering/%3foutputType=amp) 

[Elon Musk Denies Owning Dogecoin Stash Linked to Insider Trading](https://decrypt.co/145043/elon-musk-dogecoin-wallets-insider-trading) 

[Tether responds to account deactivation controversy, raises compliance checks](https://cointelegraph.com/news/tether-responds-to-account-deactivation-controversy) 


[SEC and Binance.​​US strike a temporary agreement on asset access](https://cointelegraph.com/news/sec-and-binance-us-strike-deal-on-asset-access) 






## Some Zcash Tweets
[Have you checked out the ZCash website?](https://twitter.com/zcash/status/1669442944502321248?t=EWDbabxtvbLtR989S_0kWg&s=19) 

[Check out this amazing AI generated ZCash image by ZCash AI](https://twitter.com/ZcashAI/status/1670057331588059140?t=Gz0Tu75wu4-GVyVjFDaG0A&s=19) 

[We are for Freedom](https://twitter.com/zcash/status/1669397156212375583?t=_Of8yUiBLnSILaWaa1kwoQ&s=19) 


[ZCash vs Bitcoin](https://twitter.com/zcash/status/1669726344345788417?t=HMxkPL672TOWVdSEQmeOZw&s=19) 

[Zooko shares update about Shielded Labs](https://twitter.com/zooko/status/1668351818848673793?t=hXmnE6OySqho57njWFyO-g&s=19)

[Dismaid shows off ZCash 5.6.0 and Zebra 1.0. 0 installation and compilation](https://twitter.com/dismad8/status/1669147600220717056?t=OV14vXjZ3DUPewW1IN9puA&s=19) 

[ZCash Nigeria may not attend ZCon4 😢](https://twitter.com/ZcashNigeria/status/1667782913289510912?t=9fO-8SjLn1o9LAlJm1cLUA&s=19) 


[Share your opinion about New ZCash Website](https://twitter.com/zcashesp/status/1669791594558398485?t=YkSv3-mjTFg7Grz7Yg85xQ&s=19) 



## Zeme of the Week
 [https://twitter.com/gordonesroo/status/1669580115670446080?t=Af53oZj-vg9Lz3MXoCJdPA&s=19](https://twitter.com/gordonesroo/status/1669580115670446080?t=Af53oZj-vg9Lz3MXoCJdPA&s=19) 


## Jobs in the Ecosystem

- [Executive Head of Product, ECC](https://apply.workable.com/electric-coin-company/j/6ACEC09B90/)

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [Deal5/Fucking-junkyard](https://github.com/Deal5/Fucking-junkyard)@[b92562ad8f...](https://github.com/Deal5/Fucking-junkyard/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Sunday 2023-06-18 13:56:04 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[d1cb2e8751...](https://github.com/EOBGames/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Sunday 2023-06-18 14:20:24 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.


![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

---
## [terminalforlife/Extra](https://github.com/terminalforlife/Extra)@[483ff05e19...](https://github.com/terminalforlife/Extra/commit/483ff05e1910d3f46c169543d091b043b6deaa7c)
#### Sunday 2023-06-18 14:23:38 by terminalforlife

Greatly improve output, remove sync(1), etc

- Helpers 'glkfu-changes' and 'glkfu-list' no longer dependencies

  These are checked for and used, but not initially. There wasn't a
  need to lock the user out of GLKFU simply because they lacked these
  tools, even if they are part of GLKFU as a whole.

- Added initial pretty and helpful output
- Added colorization and flag to disable it

  This cannot account for colors in subprocesses, unfortunately.

- Remove sync(1) call at the end of GLKFU

  In hindsight, this probably wasn't the place for it, most especially
  because it's synchronising _everything_. If the user does anything
  requesting for sync(1) to be executed, then it should happen anyway.

- Reworded `-i` description in usage output
- Reworded message displayed when ignoring versions
- Add flag to silence make(1) via it's `-s` flag

  After a couple of years of seeing the compilation output, I'm a
  little sick of it, personally. Kinda. Mostly, I just think it'd be
  nice to have it be optional, especially with the nicer output
  included in this commit.

- Protect argument flags from environment

---
## [Proxima-Project/Proxi-Eris](https://github.com/Proxima-Project/Proxi-Eris)@[b30528c190...](https://github.com/Proxima-Project/Proxi-Eris/commit/b30528c190a3de609b7524ef422e96cd9cf09654)
#### Sunday 2023-06-18 14:40:53 by евиё

Titanium material (#8)

* adding titanium

may the god forgive me for editing base

* fixes my fuck ups

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[dd945ad658...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/dd945ad65815611527ae3e86e7f92170baa681f3)
#### Sunday 2023-06-18 16:28:15 by ODRI-the-human

Okie

Orbitals are properly fixed for enemies now. Alt dodge abilities are being removed, because they are not that versatile and the better ideas I had for that work better as the kinda Dead Cells-esque items I have planned. Following on from that, banned items is no longer a thing, since all items can stack indefinitely anyway now, and because rarely being offered the weapon you already have is not a big deal (also just complicates things in co-op). Also also splitting infinitely with melee is removed, it was far too stupid lol.

---
## [momipochi/taiwan_amigo](https://github.com/momipochi/taiwan_amigo)@[d922177f6b...](https://github.com/momipochi/taiwan_amigo/commit/d922177f6bd09f27be2453943f4ba9a8892a7747)
#### Sunday 2023-06-18 16:34:38 by BNNCP

Merge pull request #15 from momipochi/bnn

fucking alex stupid shit

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[b350b45974...](https://github.com/i574n/The-Spiral-Language/commit/b350b45974fd416f8ed3b119a4edbddf9e4fd023)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"7:35pm. I got way too tied up with audio. To think the solution is to just export the clip into Rx. But the way the Youtuber did it was a lot more elegant that I would have done it. I definitely wouldn't have figured out to add Rx in the preferences, and to bounch the track to title on my own.

Time wasting events like these are inevitable when learning new things.

Let me check if there is still any warm water left over. This is an ideal time for a bath.

...Nope, no warm water is left. Sigh, let me just rest.

8:50pm. file:///C:/Program%20Files/Blackmagic%20Design/DaVinci%20Resolve/Documents/DaVinci%20Resolve.pdf

Holy crap, DR's manual has 4k pages.

///

Why Is This Manual So Big?
Over the years, DaVinci Resolve has evolved to encompass professional editing, compositing, and
audio mixing tools and workflows in addition to the grading tools that were the original core of
DaVinci Resolve. Each one of these domains of functionality is incredibly deep. Consequently, the
documentation has grown with each new page, tool, and parameter that’s been added, to make life
easier and to solve the countless problems that can emerge during the postproduction process.

While it is regretted that this user manual contains such a staggeringly overwhelming amount of
information, our emphasis has always been to ensure that (hopefully) every control and workflow
you encounter in DaVinci Resolve is explained somewhere within the contents of these pages.
Consequently, we hope that you find the hyperlinked table of contents (TOC) and search functionality
of your preferred PDF browser helpful in finding the information you need, along with context and tips
to help you get the most out of the tools provided

///

///

I've never tried it before, sorry. But I recall that you can setup Linux so it runs shell scripts during startup by editing some config files, you'll have to look for that on your own. What do you want them to do?

Right now my focus is on webdev, but I'll get back and do more AI art stuff before long. I'll merge my various interests into one, and make some content that might be of interest to a wider audience, so don't hesitate to give me suggestions on what you'd want to see.

///

10:35pm. https://youtu.be/sygFSbDeTno
CUT PAGE IN 5 MINS - DaVinci Resolve Basics Tutorial for Beginners

I'll try working in the cut page next time.

https://youtu.be/sygFSbDeTno?t=165

Yeah, the edit page is a pain in the ass, I noticed.

https://youtu.be/sygFSbDeTno?t=173

I didn't know you could switch between zooms using Shift Z.

https://youtu.be/sygFSbDeTno?t=199

I should look into how to use multiple timelines to make things easier on myself.

Having a large video all in a single file is difficult.

https://youtu.be/sygFSbDeTno?t=282

What is this?

https://youtu.be/sygFSbDeTno?t=347

I do not really get this, but my brain is not at 100% capacity right now.

10:40am. Thanks to all that fucking around with the audio, one of my undos must have gotten rid of the outro page.

Good thing I noticed it. I'll have to fix it tomorrow.

11pm. Oh, wow, the cut page is amazing. Now that understand how to move around in it, I see that it is way better than the edit page.

This will completely transform my productivity!

11:20pm. https://youtu.be/EF_Wysanmn0
These Editing Tips Will Save You HOURS in Resolve

11:30pm. Incidentally, I've realize that ,. act as nudge in DR. This will make it a lot easier to extend the frames.

12:05am. https://youtu.be/kOp4tWO7F54?t=228

I need to remember Alt + Y.

https://youtu.be/gvGB3M7Xmo0
NO MORE KEYFRAMES! Ultimate FREE Animation Tool for Davinci Resolve

https://youtu.be/etPAxdxrMlU
GRAB THEIR ATTENTION By Using This Easy Smooth Zoom Effect! (Davinci Resolve Tutorial)

I want to figure out how to do zooms without the difficulty of dealing with keyframes.

https://youtu.be/97vxlgKndr0
ZOOM LIKE A PRO! Free MAGIC ZOOM tool for Davinci Resolve 18

12:40pm. This zoom effect is great. Just what I needed.

https://youtu.be/97vxlgKndr0?t=42

Wait, what is this click he is going?

https://youtu.be/97vxlgKndr0?t=260

Ah, fusion overlay.

https://youtu.be/97vxlgKndr0?t=554

This is amazing. Imagine doing this with keyframes.

https://youtu.be/qdJGyytQaoU
One ZOOM to RULE them all! - Getting the most out of my Davinci Resolve MAGIC ZOOM Tool!

https://youtu.be/qdJGyytQaoU?t=145

I've just been wondering about this. This is a lot better than the hacky thing he did last time.

1:05am. Let me get dinner. I'll watch the rest of it tomorrow.

4/26/2023

8:05am. I can't believe I am up this early given how late I went to bed. Well, whatever. Let me chill for a bit. This morning is bath time.

Last night I studied DR, and I thanks to that I'll significantly upgrade my workflow.

8:35am. Now my mom is occupying the bathroom. Nevermind the bath. Let's deal with the video.

Before that let me watch one vid. Those in and out marks.

https://youtu.be/7C-ANI3tFI4
All about mark IN and OUT Points in DaVinci Resolve

https://youtu.be/7C-ANI3tFI4?t=35

Could I do these highlights in DR?

I'll also check that out. I really need to get all my Camtasia powers back.

https://youtu.be/7C-ANI3tFI4?t=91

Ah so that is how you fucking remove them!

https://youtu.be/7C-ANI3tFI4?t=107

Alt X.

Wouldn't have figured that.

https://youtu.be/7C-ANI3tFI4?t=149

Very informative.

https://youtu.be/RXrjrTpvn-s
Easy way to HIGHLIGHT AREA in DaVinci Resolve

Oh, right. I also need to figure out cursor effects.

https://youtu.be/RXrjrTpvn-s?t=112

Let me try this. It is best to follow along.

https://www.youtube.com/results?search_query=davinci+resolve+cursor

https://youtu.be/z0BsEOVx3Qk
Tip: What is Zoom Around Mouse Pointer in DaVinci Resolve and How it Can Help you Edit Faster

No it doesn't seem like it has mouse enlarging effects like Camtasia.

https://youtu.be/FIgjDY7O1EY?t=91

What is fusion composition?

https://youtu.be/r20NdlqwSPU
Markers in Davinci Resolve and How to Export Markers for YouTube Chapters in DaVinci Resolve 18

https://youtu.be/r20NdlqwSPU?t=165

00. Got it.

https://youtu.be/r20NdlqwSPU?t=245

This is bad advice. There should be an easier way.

https://youtu.be/uhSJ_3nqxac?t=228

csv again. What the hell?

https://youtu.be/UY7HmVWw1i8
Export Chapter Markers to YouTube Resolve 18 Update

http://fsprojects.github.io/FSharp.Data/library/CsvFile.html

Ah for fuck's sake. Let me make a script to extract the chapter markers.

9:35am.

```fs
#r "nuget: FSharp.Data"

open System.IO
open FSharp.Data

let f =
    CsvFile
        .Load(Path.Combine(Directory.GetCurrentDirectory(), "Timeline 1.csv"))

for row: CsvRow in f.Rows do
    printfn "%s %s" (row.GetColumn "Source In") (row.GetColumn "Notes")
```

It took me a bit too long to do this script.

```
00:00:00:00 Intro
00:01:13:14 Goals
00:02:14:06 acquire_token
00:03:05:11 Cookies vs. Local Storage vs. Session Storage
00:05:34:13 4m Timelapse
00:09:52:05 Local Storage
00:11:57:22 1m Timelapse
00:32:55:22 Marker 1
00:13:03:03 Debugging Review
00:13:45:29 1m Timelapse
00:15:38:18 Proxy Exception Wrapping Via Reflection
00:18:44:20 6m Timelapse
00:24:33:13 Outro
```

I'll just paste this into Youtube.

9:40am. I should have done it in Rider.

9:45am. https://youtu.be/OBLGG-llkvA
Authentication With ASP.NET Core And The SAFE Stack. Token Regeneration On 401 Challenges. (Pt. 7)

Let me publish it.

9:55am. Done. Let me take a bath.

10:50am. I am back. Let me start with the next thing. First, let me just try out whether the package from...the `Msal.React` works now.

https://www.reddit.com/r/MachineLearning/comments/12yqhmo/n_microsoft_releases_synapseml_v011_with_support/

Oh, what is this?

Oh, it is a Scala library.

11:15am. Ok, I can finally start. Focus me. Let me start a new project in Resolve.

11:55am. You know what, let me watch some vids on how to use transitions. They are very confusing.

I find them very awkward to use.

https://youtu.be/ebSTdCWZoVU
DaVinci Resolve 18 TRANSITIONS for Beginners | EVERYTHING You NEED to Know | CRASH COURSE

12:15pm. Let me have a break here.

1:15pm. Done with breakfast and chores. Let me get back to the tutorial.

1:20pm. Focus me.

Last night I went to bed past 1am and woke up 8am, so I am not going to force myself too much.

Even though I do not feel too tired, but I get the sense that i've been too wound up during the past few days.

Let's just take it one at a time today.

https://youtu.be/ebSTdCWZoVU?t=229

Maybe I should turn Render Cache on.

This is why these vids are so useful especially when you are starting out.

https://youtu.be/ebSTdCWZoVU?t=268

Yeah, this is what is troubling me. Also, how is he doing that cursor effect?

https://youtu.be/ebSTdCWZoVU?t=357

For some reason this is not working for me.

1:45pm. Oh, I figured it out. It turns out you need to make some room for the transitions.

Also it is a lot easier to do it in Cut mode.

1:50pm. This is extreme. The functionality for putting transitions is actually very good in Resolve, now that I understand how it works.

https://youtu.be/ebSTdCWZoVU?t=1010

These guy is pretty good at doing highlights. I wonder how he is doing the zoom in addition to that?

https://youtu.be/ebSTdCWZoVU?t=1122

This guy is pretty good at editing. Personally, getting it to this level would be too much work.

2:15pm. Done with the video. I completely get transitions now.

https://boards.4channel.org/g/thread/93028912/can-we-appreciate-ssd-prices

///

While GPU and MOBO prices have gone insane the past few years, can we appreciate the current SSD prices? Like damn they have almost halved from just 6 months ago. I bought a cheap 480gb sata SSD 7 months ago and now I can buy the 960gb version for the same price.

This is what we want to see. But so far it's only happening with RAM and SSD's.

///

Wow, 1tb SSDs cost as much as 1tb HDDs now?

Yeah, we can appreciate this.

Fuck NVidia, and praise Samsung.

2:20pm. Let me resume. Let me do some programming.

I really upped my video editing skills between last night and now. I'll have a good time today.

Let's it easy, one step at a time.

2:25pm. Damn it, is is possible to speed edit in the cut page?

https://youtu.be/85W8E7VRmU4
Speed Editing in DaVinci Resolve's Cut Page

Let me watch this. I can't see an easy way to speed up and slow down clips so they align with the audio and such.

https://github.com/fable-compiler/Fable/issues/

Opened issue 3435.

This sidetracked me. I am a bit sleepy, but let's keep going for as long as I feel like it. I do not dislike this tube programming.

I really don't have anything better to do with my life than this.

https://youtu.be/vQ4xqIy-HlA
BEST way to Freeze Frame in Davinci Resolve

I really need a better way of extending the last frame.

https://youtu.be/vQ4xqIy-HlA?t=82

Did he free frame in the inspector?

Oh, this works great!

I should figure out a shortcut for it.

3:45pm. There is a shortcut, but it doesn't work for some reaon.

Nevermind. This is good enough.

It is way better than the older method of switching to the edit page, making a split, selecting the tiny clip and then extending it.

Let me get back on track.

4:20pm. The speed wheels in the cut page and in the in the inspector have very different behaviors.

This is something you learn thourgh use. The one in the cut's tool panel ripples the timeline. I really wish I could scale it like in Camtasia though.

4:40pm. Oh, disolve and smooth cut place transitions at the point of the cut. How does that work?

https://youtu.be/iWGTf8tROac
2 Davinci Resolve Cut Page Tools You NEED TO KNOW!

4:45pm. I am feeling extremely fatigued right now. Let me just watch these and then I'll close.

5:10pm. I decided to do music for the timelapse.

The next is IndexDb, but let me figure out what those cuts should be doing.

https://youtu.be/V3AhEcDN1hM?t=207

https://youtu.be/osf6eHzu-ZE
Davinci Resolve Editing Tutorial: How to Use the Smooth Cut Transition

Let me watch this.

5:35pm.

///

That wasn't too hard.
Right now, the SAFE Stack demo we are using sends a request to the server as soon as the page is loaded, so it doesn't make a visible difference either way.
But if in the future you have an application that has significant local functionality, this is how you could delay the authorization step.
What we will look into next is IndexDb. Remember how two videos ago we showed web storage and it said that local and session storage are blocking and not recommended for real world use?
Well, quite a lot of sites use it regardless, including the one you are watching this on, but we are better than them.
We'll make use of IndexDb.
We'll start off by making use of it as a key value store, much like the local and session storage, and then we'll do a deeper dive into it.

///

5:20m in. I'll close here. I am dying of fatigue.

IndexDb will have to come tomorrow."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[4e7df15e04...](https://github.com/i574n/The-Spiral-Language/commit/4e7df15e0400f969e161207a569e4033e55d2997)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"8:50pm. https://news.ycombinator.com/item?id=35813322&p=2

///

cubefox 21 hours ago | root | parent | prev | next [–]

> DALL-E lost because they let MJ eat their lunch
I wonder why nobody is talking about Bing Image Creator

https://www.bing.com/images/create

which uses some much more advanced version of Dall-E 2 in the background (so Dall-E 2.5? 3?), while being completely free to use. It can produce some pretty mind blowing results with quite simple prompts, although apparently not as impressive as Midjourney V5. A few examples:

hyperrealistic

https://www.bing.com/images/create/hyperrealistic/644fa0c48f...

an allegory for femininity

https://www.bing.com/images/create/an-allegory-for-femininit...

portrait of a strange woman, hyperrealistic

https://www.bing.com/images/create/portrait-of-a-strange-wom...

allegory of logic, portrait

https://www.bing.com/images/create/allegory-of-logic2c-portr...

her strange bedfellow

https://www.bing.com/images/create/her-strange-bedfellow/644...

Mrs fox

https://www.bing.com/images/create/mrs-fox/6446e85a32134e649...

inside view

https://www.bing.com/images/create/inside-view/6446f1dc573f4...

in the midst of it all

https://www.bing.com/images/create/in-the-midst-of-it-all/64...

strange gal

https://www.bing.com/images/create/strange-gal/6446e2a2ea7a4...

sighting of a strange entity in an abandoned library

https://www.bing.com/images/create/sighting-of-a-strange-ent...

sleeping marble woman next to a wall of strange pictures inside an abandoned museum, close-up

https://www.bing.com/images/create/sleeping-marble-woman-nex...

sculpture of a woman posing next to a wall of strange pictures, close-up

https://www.bing.com/images/create/sculpture-of-a-woman-posi...

Easter

https://www.bing.com/images/create/easter/643ae4968aff432684...

Christmas on board a spaceship, DSLR photograph

https://www.bing.com/images/create/christmas-on-board-a-spac...

an angel, dancing to heavy metal

https://www.bing.com/images/create/an-angel2c-dancing-to-hea...

Saturday afternoon in the streets of a buzzing cyberpunk city, photo-realistic, DSLR

https://www.bing.com/images/create/saturday-afternoon-in-the...

The Dogfather

https://www.bing.com/images/create/the-dogfather/6441d18950b...

the unlikely guest

https://www.bing.com/images/create/the-unlikely-guest/644446...

Strange pictures in an abandoned museum

https://www.bing.com/images/create/strange-pictures-in-an-ab...

strange woman in an abandoned museum, close-up

https://www.bing.com/images/create/strange-woman-in-an-aband...

strange woman in an abandoned museum, strange pictures in the background

https://www.bing.com/images/create/strange-woman-in-an-aband...

a wall of strange pictures in an abandoned museum in Atlantis, close-up

https://www.bing.com/images/create/a-wall-of-strange-picture...

female sculpture in an abandoned museum in Atlantis, close-up

https://www.bing.com/images/create/female-sculpture-in-an-ab...

the unlikely guest

https://www.bing.com/images/create/the-unlikely-guest/644490...

an unlikely guest of the secret society in the lost city in a country without name, close-up

https://www.bing.com/images/create/an-unlikely-guest-of-the-...

I think the quality of most of these pictures is far beyond what is achievable with Dall-E 2. One issue that still exists (though to a lesser extent) is the fact that faces have to cover a fairly large area of the image. Smaller faces look strange, e.g. here:

photograph of the unlikely guests

https://www.bing.com/images/create/photograph-of-the-unlikel...

It is as if the model creates a good draft in low resolution, and another model scales it up, but the latter model doesn't know what a face is? (I have no idea how diffusion models actually work.)

///

From a recent HN thread. I had no idea Bing had image generation capability. Let me take a look at a few of these.

5/6/2023

8:35am. Let me chill and then we will get started.

By 'we', I mean me and my tulpa. I've gotten into the habit of saying 'we' in my videos.

https://mangadex.org/chapter/a1ad8851-99f4-444d-b654-bfa6ff7e6eb7/6
> Uninterruptible Power Suply
> I recommend one if you live in a third world country or if your power grid is serviced by PG&E.

9:25am. Let me start.

```cs
        /// <summary>Options used to configure hub instances.</summary>
        [CustomOperation("with_hub_options")]
        public SignalRExtension.SignalR.State.Settings<t, a1, a2, a3, a4> HubOptions<t, a1, a2, a3, a4>(
          SignalRExtension.SignalR.State.Settings<t, a1, a2, a3, a4> state,
          FSharpFunc<HubOptions, Unit> f)
          where t : class
          where a3 : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<t, a3>, Fable.SignalR.SignalR.Settings<t, a3>>) new SignalRExtension.SignalR.HubOptions\u0040167<t, a3>(f));
        }

        /// <summary>Adds a logging filter with the given LogLevel.</summary>
        [CustomOperation("with_log_level")]
        public SignalRExtension.SignalR.State.Settings<o, p, q, r, s> LogLevel<o, p, q, r, s>(
          SignalRExtension.SignalR.State.Settings<o, p, q, r, s> state,
          LogLevel logLevel)
          where o : class
          where r : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<o, r>, Fable.SignalR.SignalR.Settings<o, r>>) new SignalRExtension.SignalR.LogLevel\u0040177<o, r>(logLevel));
        }

        /// <summary>Called when a new connection is established with the hub.</summary>
        [CustomOperation("with_on_connected")]
        public SignalRExtension.SignalR.State.Settings<ClientApi, l, m, ServerApi, n> OnConnected<ClientApi, l, m, ServerApi, n>(
          SignalRExtension.SignalR.State.Settings<ClientApi, l, m, ServerApi, n> state,
          FSharpFunc<FableHub<ClientApi, ServerApi>, Task<Unit>> f)
          where ClientApi : class
          where ServerApi : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<ClientApi, ServerApi>, Fable.SignalR.SignalR.Settings<ClientApi, ServerApi>>) new SignalRExtension.SignalR.OnConnected\u0040187<ClientApi, ServerApi>(f));
        }
```

Ok, we could plug the on connected here.

9:55am. Oh, I am surprised I got a reject from Valora so long after I'd applied.

I do hate this. I put so much effort into programming, but as far as the job market is concerned, I am a piece of trash.

10am. I never want to go through this again.

My ambition used to be to kickstart the Singularity, but now I am wondering whether I'll ever make a dollar in my life. Life is hard. I went down the wrong path. I wish Skynet would kill me and reset my failures and my incompetence to zero. I can't win at anything involving the real world.

Focus me.

I need to focus on the task at hand instead of letting bad thoughts enter my head.

Whatever the case, I am obligated to keep struggling.

I sure would be nice to cultivate all the elite programming skills and get reincarnated with all of them in the past.

Sigh.

Whatever the future holds, I'll keep seeking my opportunity.

I've been making slow progress, but a couple of more months and I will be a top cloud developer. I'll get my resolution that way.

10:05am. I really am pissed at all of this.

I am going to get the skills that I need, and then become a scam artist. Maybe I should make a bot that applies to do job applications?

For now let's just keep going.

10:20am. I need to change the names of the packages.

10:30am.

```
        type HubConnectionBuilder<'ClientApi,'ClientStreamFromApi,'ClientStreamToApi,'ServerApi,'ServerStreamApi,'Msg>
            internal (hub: Fable.SignalR.IHubConnectionBuilder<'ClientApi,'ServerApi>, dispatch: 'Msg -> unit) =
```

Now I am getting type errors again.

```
let mutable handlers = Handlers.empty
```

I am also getting an error here.

I remember this giving me a lot of trouble before.

```
        type HubConnectionBuilder<'ClientApi,'ClientStreamFromApi,'ClientStreamToApi,'ServerApi,'ServerStreamApi,'Msg>
            internal (hub: Fable.SignalR.IHubConnectionBuilder<'ClientApi,'ServerApi>, dispatch: 'Msg -> unit) =
```

Wait, it says it is not accessible from this code location...

```
[<NoComparison;NoEquality>]
type internal Handlers =
```

These internal types are giving me trouble, but why?

```
<PackageId>Rebuild.Fable.SignalR.Elmish qwe</PackageId>
```

Damn it, instead of renaming all the projects, I should have just set the package ID!

11:20am. Had to take a break. You know what, even though it is early, let me have breakfast here. OBS crashed anyway.

It gave me time to think.

12:30pm. Let me resume.

I wrote some sad things, so it jinxed me. I should not blame the reject, I was the one who decided to go on a tangent.

Let me write some happy things to contrast it.

It is one thing to want to be killed by a superior being, but I do not need reincarnation.

Instead of that, what I'd prefer is a long life.

I took many wrong paths in life and I am paying for it, but had I started off with web development like this it wouldn't have been too bad.

So that is what I want. I want time to make up for my mistakes, and time to make profits.

I want time so I can exceed the ordinary people and reach a position of superiority. I want to strive for the apex of programming and the pinnacle of existence.

The only thing I've ever learned is to continue going forward and prove my will.

So that is what I should do now. Let me finish this project.

The library isn't so bad, just ignore the invokes.

> (Since 3.4) If you need to get some data before initializing the connection or you only want to enable it if your user does some action, like entering a chat page, you can pass the BridgeConfig to Bridge.asSubscription to get something that can be passed to Cmd.ofSub.

Oh crap, I just realized what this means!

12:55pm. https://elmish.github.io/elmish/docs/subscription.html#subscription-reusability

Maybe what I wanted could have been implemented using Elmish Bridge after all.

```
(Since 5.0) BridgeConfig now implements IDisposable, closing the connection when Dispose() is called. That is useful for using it with some React hooks that close resources when detaching the component.
```

Let me check the source for this.

```fs
/// Creates the bridge. Takes the endpoint and an optional message to be dispatched when the connection is closed.
/// It exposes a method `Send` that can be used to send messages to the server
type BridgeConfig<'Msg,'ElmishMsg> =
    { path : string
      whenDown : 'ElmishMsg option
      mapping :  'Msg -> 'ElmishMsg
      customSerializers: Map<string, obj -> SerializerResult>
      retryTime : int
      name : string option
      urlMode : UrlMode}

    /// Internal use only
    [<System.ComponentModel.EditorBrowsable(System.ComponentModel.EditorBrowsableState.Never)>]
    member this.AddSerializer(serializer: 'a -> SerializerResult, typeOrigin: System.Type) =
        let typeOriginName = typeOrigin.FullName.Replace("+",".")
        {
            whenDown = this.whenDown
            path = this.path
            mapping = this.mapping
            customSerializers =
                this.customSerializers
                |> Map.add typeOriginName (fun e -> serializer (e :?> 'a))
            retryTime = this.retryTime
            name = this.name
            urlMode = this.urlMode
        }

    interface System.IDisposable with
        member t.Dispose() =
            Helpers.mappings.Value
            |> Option.defaultValue Map.empty
            |> Map.tryFind t.name
            |> Option.iter (fun (_, socket, _) ->
                let (skt,_) = socket.Value
                socket.Value <- (None, true)
                skt |> Option.iter (fun e -> e.close())
                )
```

The bridge is what is responsible for the connection.

Holy shit, this kills me.

///

Can you have multiple SignalR hubs?
Multiple Hubs

All clients will use the same URL to establish a SignalR connection with your service ("/signalr" or your custom URL if you specified one), and that connection is used for all Hubs defined by the service.Feb 10, 2022

///

Hmmm, maybe I was wrong

Assuming they are connecting to the same endpoint, they will use the same connection.

And in that case, maybe SignalR is intended to be one hub per invoke?

https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/hubs-api-guide-server

Let me read this a bit.

> In SignalR you can define named groups to broadcast to subsets of connected clients. Groups are maintained separately for each Hub. For example, a group named "Administrators" would include one set of clients for your ContosoChatHub class, and the same group name would refer to a different set of clients for your StockTickerHub class.

> To call client methods from the server, use the Clients property in a method in your Hub class. The following example shows server code that calls addNewMessageToPage on all connected clients, and client code that defines the method in a JavaScript client.

This is to all the connected clients, and not just the ones for a particular hub?

```cs
public class ContosoChatHub : Hub
{
    public override Task OnConnected()
    {
        // Add your own code here.
        // For example: in a chat application, record the association between
        // the current connection ID and user name, and mark the user as online.
        // After the code in this method completes, the client is informed that
        // the connection is established; for example, in a JavaScript client,
        // the start().done callback is executed.
        return base.OnConnected();
    }

    public override Task OnDisconnected(bool stopCalled)
    {
        // Add your own code here.
        // For example: in a chat application, mark the user as offline,
        // delete the association between the current connection id and user name.
        return base.OnDisconnected(stopCalled);
    }

    public override Task OnReconnected()
    {
        // Add your own code here.
        // For example: in a chat application, you might have marked the
        // user as offline after a period of inactivity; in that case
        // mark the user as online again.
        return base.OnReconnected();
    }
}
```

Hmmm, it makes a distinction between the user calling stop and not.

https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/hubs-api-guide-server#how-to-pass-state-between-clients-and-the-hub-class

Hmmm...

3:25pm.

```fs
    [<RequireQualifiedAccess>]
    module Stream =
        let sendToClient (msg: StreamFrom.Action) (hubContext: FableHub<Action,Response>) =
            match msg with
            | StreamFrom.Action.GenInts ->
                asyncSeq {
                    for i in [ 1 .. 100 ] do
                        yield StreamFrom.Response.GetInts i
                }
                |> AsyncSeq.toAsyncEnum

        let getFromClient (clientStream: IAsyncEnumerable<StreamTo.Action>)
            (hubContext: FableHub<Action,Response>) =

            AsyncSeq.ofAsyncEnum clientStream
            |> AsyncSeq.iterAsync (function
                | StreamTo.Action.GiveInt i ->
                    hubContext.Clients.Caller.Send(Response.NewCount i)
                    |> Async.AwaitTask)
            |> Async.StartAsTask
```

I had no idea F# had async sequences.

```fs
let myConfig serviceCollection =
    serviceCollection.AddSignalR (
        mySignalRConfig,
        SignalRHub.Stream.sendToClient,
        SignalRHub.Stream.getFromClient
    )
```

Is this how the original SignalR really works?

Edit: No way, these are definitely additions by the library.

Also the invocations sent back to the client are very weird. They are not like in the regular library at all.

```fs
x.ClientTimeoutInterval
```

Oh there is a time interval for closing the connection?

5:05pm. Damn it, I have a really nasty error where it is not importing the library.

```fs
#if DEBUG
open Elmish.Debug
open Elmish.HMR
open Fable.SignalR
#endif
```

Why is this under debug?

https://stackoverflow.com/questions/68560814/f-fable-function-from-imported-module-is-not-compiled-into-js

> A compatible library, amongst other things, needs to include its F# source code in the NuGet package so Fable can transpile this to JavaScript.

Ohhh, let me try repacking it with the source included.

> --include-source - it creates the symbols package with a src folder inside containing the source files.

5:40pm. Grah.

I wonder if I need these template files?

```
The paket.template files
The paket.template files are used to specify rules to create .nupkgs with the paket pack command.
```

Oh fuck.

Ah, wait, I just realized I might have not included the sources correctly. I need to do more than just copy the nupkgs.

I see that there is more in the directory now.

5:45pm. Agh.

How does a fable package look like?

```
dotnet pack src/Fable.SignalR --include-source --output testpkg/
```

I tried running this and it isn't putting anything else in the directory.

Bo. I have no idea.

I'll open an issue.

6:25pm. Done with lunch.

I've tried updating Fable and now things work even worse than before. I keep getting errors for missing source files for vanilla libraries.

6:50pm. This is kicking my ass so much.

I must be retarded to put myself through this. Who is going to watch this kind of video anyway?

6:55pm.

> a non euclidean city, abstract knotted up shapes, machinery, architecture, high quality, high detail

Oh the bing image generator is generating 1k native images. These give me something good for my next thumbnail."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[81ea484261...](https://github.com/i574n/The-Spiral-Language/commit/81ea484261abcf69bb56c570756d1a539384515d)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"https://twitter.com/ESYudkowsky/status/1649149246921412610
> Acceleration of development of AI is also acceleration of development of catgirls.

Kek.

7:05pm. I watched the whole thing and it is even funnier.

https://boards.4channel.org/g/thread/92954365/sdg-stable-diffusion-general#p92955107

///

>>92954993
go pull the latest a1111 build, it's broke. It's been broke. Go read the comments from numerous devs frustrated with a1111 unwillingness to let anyone maintain the repo

go pull the latest vlad build, it works and I don't need to install a single extension because the ones I use are built in + torch 2.0 support

///

I'll have to look into these at some point.

4:10pm. Let me just extract the markers by hand.

https://www.reddit.com/r/VideoEditing/comments/ko8w8t/january_what_editing_software_should_i_use/

https://www.reddit.com/r/VideoEditing/comments/aw52bl/if_this_is_your_first_time_here_stop_and_read/

4:20pm. https://youtu.be/_Asoh5Uj0hE
Authentication With ASP.NET Core And The SAFE Stack. React SPA Login Using Azure AD. (Pt. 6)

This might be last in the auth mini series. Let me post it on the F# sub.

Somehow this got put in the wrong section in my journal.

7:55pm.

///

>>92955744 (You)
this video seems retarded but
>click a random part
>donkey kong country music is playing
based

///

These guys are good at compliments.

https://mangadex.org/title/f2fa82a7-cf98-48cd-886c-86c35fc6d223/shoujo-nyuumon

Let me read this and Knight Run. Then I will read LOM.

https://old.reddit.com/r/ExperiencedDevs/comments/12ubtef/sanity_check_when_leadership_says_we_cant_compete/

Interesting thread here.

///

We've rocketed past red flags and are now in the territory of infrared flags.

Here's the shitty thing about competing with the big three - they can afford to lose money on big deals to secure long term revenue. They will happily undercut you, take the loss on some compute/storage and make it up on their proprietary tech. Terraform and related tools skew that balance more - the infrastructure automation for the big three tends to be really robust and the smaller cloud providers have to spend a larger percentage of their engineering staff to maintain feature parity given the different economies of scale. The larger ecosystem will have similar skews; features like the Kubernetes autoscaler is going to have faster support for more features for the big three because they can throw bodies at the problem; hell, they basically run the Kubernetes foundation. This issue is pervasive across the tech landscape right now.

Competing on reliability, support, quality of features, niche specialization, etc are one of the ways that a smaller provider can hold ground (or potentially gain ground); if the CTO just gutted your engineering staff and there's no clear product direction then your company has essentially lost one of your primary competitive advantages. This is a really dangerous place to be in.

///

11pm. https://mangadex.org/title/59e04a79-435e-418d-8b64-c8d4315693ab/akuma-koujo

I'll leave this for later. Let me go to bed. It is by the Otome Survival author.

https://ellotl.com/rose-princess-of-hellrage-volume-1-chapter-1/

Also Hellrage got picked up even though it is MTL.

4/23/2023

8:50am. I am up. I had time to lounge in bed. Only 3 upvotes on the F# sub. Pitiful. I needed to do this, but thankfully I am done with setting things up.

9:05am. Ah, whatever, let me chill for a bit and then I will start.

https://youtu.be/UPo_Xahee1g
That's It, I'm Done With Serverless.

I'll watch this later.

9:50am. Let me start.

By watching that guy's video. It is pretty informative.

Also, it doesn't matter that I got 3 upvotes so far. Typicially it takes time for them to come in. I am being too touchy right now.

Let me watch the vid by Theo, read the 666 Princess manhua and then I'll start properly. Right now I am still thinking about what I want to do.

https://youtu.be/UPo_Xahee1g?t=605

I really wish this guy took my advice to deal with the mouth noises he makes, but that's his own problem.

https://youtu.be/UPo_Xahee1g?t=1296

I wonder if this will be an issue with ASP.NET Core on Azure? These cold starts.

Prisma won't be a factor for me thanks to EF Core.

10:15am. The next video will have to be about refining what I've done yesterday. I am not all the way there yet.

https://www.bilibilicomics.com/mc2113/233621

Sigh, I really do like the art for this. I wish it didn't fininsh in only 77 chapters.

10:30am. Done with the manhua. Let me start for real.

I want to resume that tutorial from yesterday.

https://youtu.be/jX79DfF4eds
Screen recording and editing basics with OBS and Davinci Resolve

https://youtu.be/jX79DfF4eds?t=869

Actually, let me follow this along as I do my own screencast.

10:55am.

///

Time for part 7 of the authentication miniseries. Hopefully this will be the last one.
I am your host, and future AI overlord, Vilo, and in this video we will wrap up spa logins.
In the previous video, after a week of effort we finally completed the spa login page for a React app.
Even though we've done that, it cannot be said that we are done.
The JWT tokens we are getting from Azure AD have a short expiration of about 30-60 minutes, so we are worried that the user might get locked out from the backend in the middle of his session.
In that case, he should get a 401 challenge from the backend, as opposed to the incorrect 403 we are using now.
After which the frontend should try to get a new token.
Since that might involve a redirect, we will also need a way to store the client state inbetween. This is a great time to try out IndexDB.
In our last video we were using session storage, which blocks the entire browser, and isn't a recommended for real use, so we should strive to do the right thing instead here.
To summarize what our goal should be, that would be to make the logins reactive.
Instead of having a login page at the start, we should have the user login only when that is necessary.
Once we have that, we won't have to worry about token expirations specifically.
Rather than try to eliminate a specific issue, we will design the application properly so that it cannot occur in the first place.

///

Here is the intro. How do I paste it into DR?

11:10am. Damn, how do I get rid of the dynamic zoom.

DR feels very smooth, but the controls are awkward. Still that is because I am stating out with the thing.

11:35am. https://youtu.be/jX79DfF4eds?t=1286

I am playing around, but so far it is pretty unintuitive. Most of the stuff from Camtasia isn't there.

https://youtu.be/EfMcaVfDUuI?t=4
How To Adjust Clip Speed | DaVinci Resolve 18 Tutorial

12:20pm. Why the fuck is it setting the project FPS rate to 24 instead of 30 at which I am recording.

...My first impression of DR is pretty negative so far.

Maybe it got set to 24 once I pasted the image in.

https://beginnersapproach.com/davinci-resolve-frame-rates/#:~:text=%E2%80%9CProject%20Settings%E2%80%9D!-,Why%20is%20Timeline%20Frame%20Rate%20Greyed%20Out%20in%20Resolve%3F,once%20the%20clips%20are%20imported.

https://youtu.be/jX79DfF4eds?t=2007

I already hate this stupid thing. If I wanted to add that disolve it pesters me to trim the clip.

1:05pm. https://youtu.be/rOSJ7ngOqoM
Davinci Resolve 15 - How to Freeze Frame (Fast Tutorial)

https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=111602

> If you take two clips and just butt them up together you will not be able to add a transition. A transition needs video to go from and too. Clips need that extra bit of video called handles.

This is confusing me, let me read it.

https://youtu.be/eg40CClcWC0

https://youtu.be/eg40CClcWC0?t=105

JustTextPopupRect. Ok.

...No I do not have that.

Ah, he implemented it himself.

1:20pm. Ok, at least I figured out how to do text boxes finally.

Let me have breakfast here.

1:35pm. https://youtu.be/o6rnuaJlB9M?t=156

I really, really hate how moving the top right corner for example, also affects the opposite side.

I can't belive it isn't possible to just move a single side. But pressing Ctrl Shift or Alt doesn't work for me.

https://youtu.be/mCEp08MSvdU?t=23
> Retime controls.

Oh, wonderful. I was struggling with clip speed, but DR has the same thing as Camtasia after all. Sheesh.

For a minute I thought it wouldn't.

2:05pm. https://youtu.be/mCEp08MSvdU?t=46

Done with chores. Good thing I haven't skipped this video. I wasn't aware DR would have speed points.

Let's take it easy today I guess.

https://youtu.be/mCEp08MSvdU?t=45

It even has freeze frame.

https://youtu.be/mCEp08MSvdU?t=93

This is great speed functionality. To think I was afraid it would even have it.

https://youtu.be/mCEp08MSvdU?t=252

Interesting.

3pm. Let me start. I am a bit depressed today. Sigh, why does functional programming not have to be popular?

I am really forced to endure a lot of hardship due to that.

3:10pm. https://youtu.be/MJsCdkYqZx4
How to Use Markers and Flags in DaVinci Resolve

https://youtu.be/MJsCdkYqZx4?t=126

I wouldn't have figured this out on my own.

3:25pm. https://youtu.be/EEksPdEc7aI
DaVinci Resolve 18 - Full Tutorial for Beginners

Let me watch this.

https://youtu.be/EEksPdEc7aI?t=611
> Generate proxy media

What will do is make a smaller, easier to play version of the media.

https://stackoverflow.com/questions/61177278/how-to-handle-redirects-to-auth-provider-from-the-backend-in-fable-elmish-spa

4:05pm. https://github.com/Zaid-Ajaj/Fable.Remoting/issues/

Opened issue 340.

4:20pm. https://youtu.be/bbPZvz6ELiA
Change Mono Sound to Stereo Audio in DaVinci Resolve 18

Holy crap. DR is so annoying in how it doesn't automatically expand to stereo. I know how to fix it for an individual clip, but like hell do I feel like doing that every time.

Let me watch this to see if gives me a way to automate it.

https://youtu.be/bbPZvz6ELiA?t=47

Oh, I could change the entire track type?

That is the solution!

Let me go back to the DR tutorial.

I've started feeling down today, but I'll get back up.

https://youtu.be/EEksPdEc7aI?t=1231

I do not have this overlay for some reason, but it doesn't really matter.

https://youtu.be/jX79DfF4eds?t=2390

Actually, I still haven't watched the ajustment clip parts.

https://youtu.be/jX79DfF4eds?t=2382

This thing has subtitle tracks.

That is an interesting possibility.

https://youtu.be/jX79DfF4eds?t=2462

I tried this myself and it is not going well. Let me watch the video.

5:10pm. https://youtu.be/jX79DfF4eds?t=2804

I really do not like the way the zooming is done. It is so unwieldy.

https://youtu.be/7l_9HUR0PU0
Zoom in zoom out DaVinci Resolve 18 Tutorial for Beginners

I got a handle on the keyframes, but let me watch this longer tutorial.

https://youtu.be/7l_9HUR0PU0?t=146

Just what kind of interface is this? It is hard as hell to use.

https://youtu.be/7l_9HUR0PU0?t=345

I like dynamic zoom, but it is so useless as it doesn't have keyframes.

What am I supposed to do with it? I need to both zoom in and out.

5:35pm.

```fs
    let cmd =
        Cmd.OfAsync.perform (fun () -> async {
            try
                return! todosApi.getTodos ()
            with e ->
                JS.console.log $"Qwe. Got an exception: {e}"
                return raise e
            }) () GotTodos
```

Instead of being so uninspired, let me try this.

Oh, it in fact does the sensible thing which is throwing an exception.

What kind of object is it?

Oh, it is a proxy request exception.

5:45pm. Ok, now everything is set.

In our attempt to factor out the token acquisition code, we are encountering a problem.
Mentally, we were thinking of the redirect as if it had the any type, but it has the unit type.
This is making us unsure whether the redirect acts as an exception or not.
Does it execute the statements past the redirect or not?
Instead of waffling like this, it would be better to just test it out. Then we can plan ahead.

9:15pm. I am over half done with part 7. I would have finished it all, but I am learning to DaVinci Resolve which slowed me down.

7m is fine for one day.

9:25pm. https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes#access-tokens

So it lasts an hour.

https://learn.microsoft.com/en-us/azure/active-directory/develop/refresh-tokens

A refresh token is 24h.

4/24/2023

8:40am. Let me chill for a bit.

9:20am. https://www.bilibilicomics.com/mc2113/233623

The MC of this is pure sex. Let me just finish the chapter and I will start.

4 upvotes on the F# sub. Lame.

9:25am. Let me start. I only now crossed the 100 hours threeshold on Youtube. The pitiful thing is that if this was JS or Python, I'd be over 10k right now easily, but I will stick to my functional programming path.

I'll master web development in my own way.

Let me just watch tutorials for a bit. I've been using fusion and compound clips, but I wonder what they are.

https://youtu.be/NPTXnLxkJTM
Fusion Clip VS Compound Clip in DaVinci Resolve

Exactly what I wanted to know.

9:35am. https://www.youtube.com/watch?v=smfrFjvOnko
【東方 JRock】Best of monochrome-coat

Never heard this circle. Let me leave it for later.

Damn it. Let me test that new Msal React package. The author fixed it, so I want to verify it for him.

10:05am. Ok, that is done. Let me continue.

https://youtu.be/ZeUg11X-l44
How to Freeze Frame in Davinci Resolve 18 | Fast Tutorial

Oh, this is simple.

12:40pm. Nasty thunder. Let's scram.

1:30pm. Let me resume. Done with breakfast. Since it pouring outside, I'll leave chores for later.

https://youtu.be/VsbuJ88qRPY
How to Add Subtitles Tutorial | Davinci Resolve 16

4:35pm. 16:36m in.

I am starting to feel fatigued.

What I need to figure out next is how to use reflection to go over the record fields in Fable.

https://github.com/Zaid-Ajaj/Fable.Remoting/blob/master/Fable.Remoting.Client/Extensions.fs

This is going to require some studying. I am not sure where to find info on Fable reflection.

5pm. Pausing here is making me realize how winded I am.

I have no choice. I have to pause here.

I've always thought this, but my ability to do metaprogramming in .NET is surprinsgly poor. I think it is high time I acquire that particular skill.

https://medium.com/@zaid.naom/f-interop-with-javascript-in-fable-the-complete-guide-ccc5b896a59f

> Pojo records are only intended for type-safe interaction with javascript libraries that require a plain object (like React components). These records lack many features, like instance and static methods and have no reflection support.

https://medium.com/@zaid.naom

I am going to have to read the Fable.Remoting source for hints. I asked in the slack.

5:15pm. I should look into the serialization libraries. We'll let me clone `Fable.Remoting` and I'll take a look at its source.

5:30pm. `Proxy.fs` is interesting. It has a bunch of metaprogramming in it.

I should look into Fable.SimpleJSON.

5:35pm.

```fs
type Remoting() =
    /// For internal library use only.
    static member buildProxy(options: RemoteBuilderOptions, resolvedType: Type) =
        let schemaType = createTypeInfo resolvedType
        match schemaType with
        | TypeInfo.Record getFields ->
            let (fields, recordType) = getFields()
            let fieldTypes = Reflection.FSharpType.GetRecordFields recordType |> Array.map (fun prop -> prop.Name, prop.PropertyType)
            let recordFields = [|
                for field in fields do
                    let normalize n =
                        let fieldType = fieldTypes |> Array.pick (fun (name, typ) -> if name = field.FieldName then Some typ else None)
                        let fn = Proxy.proxyFetch options recordType.Name field fieldType
                        match n with
                        | 0 -> box (fn null null null null null null null null)
                        | 1 -> box (fun a ->
                            fn a null null null null null null null)
                        | 2 ->
                            let proxyF a b = fn a b null null null null null null
                            unbox (System.Func<_,_,_> proxyF)
                        | 3 ->
                            let proxyF a b c = fn a b c null null null null null
                            unbox (System.Func<_,_,_,_> proxyF)
                        | 4 ->
                            let proxyF a b c d = fn a b c d null null null null
                            unbox (System.Func<_,_,_,_,_> proxyF)
                        | 5 ->
                            let proxyF a b c d e = fn a b c d e null null null
                            unbox (System.Func<_,_,_,_,_,_> proxyF)
                        | 6 ->
                            let proxyF a b c d e f = fn a b c d e f null null
                            unbox (System.Func<_,_,_,_,_,_,_> proxyF)
                        | 7 ->
                            let proxyF a b c d e f g = fn a b c d e f g null
                            unbox (System.Func<_,_,_,_,_,_,_,_> proxyF)
                        | 8 ->
                            let proxyF a b c d e f g h = fn a b c d e f g h
                            unbox (System.Func<_,_,_,_,_,_,_,_,_> proxyF)
                        | _ ->
                            failwithf "Cannot generate proxy function for %s. Only up to 8 arguments are supported. Consider using a record type as input" field.FieldName

                    let argumentCount =
                        match field.FieldType with
                        | TypeInfo.Async _  -> 0
                        | TypeInfo.Promise _  -> 0
                        | TypeInfo.Func getArgs -> Array.length (getArgs()) - 1
                        | _ -> 0

                    normalize argumentCount
                |]

            let proxy = FSharpValue.MakeRecord(recordType, recordFields)
            unbox proxy
        | _ ->
            failwithf "Cannot build proxy. Exepected type %s to be a valid protocol definition which is a record of functions" resolvedType.FullName

    static member inline buildProxy<'t>(options: RemoteBuilderOptions) : 't =
        Remoting.buildProxy(options, typeof<'t>)
```

Check this out.

https://github.com/Zaid-Ajaj/Fable.SimpleJson

It turns out this isn't for metaprogramming, but plain JSON wrangling.

5:45pm. https://en.wikibooks.org/wiki/F_Sharp_Programming/Reflection

This is too hard to just ingest it normally.

What I will do instead is approach it the same way I would in Spiral.

I have a record? How would I map it in .NET?

I should start with that and move from there.

This is a good opportunity to get some essential skills that I've been neglecting for far too long.

It might be good to just end the video here. It is clear that I am setting on a new path.

I'll post it tomorrow or maybe the day after and start work on Reflection in a separate one.

6:05pm. Let me close here.

Reflection isn't hard unless I get hung up about trying to reflect any kind of .NET type. If it is just tuples, records and functions, that is something that should be handleable in a single video."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[a0a76c2154...](https://github.com/i574n/The-Spiral-Language/commit/a0a76c21549a746f4e88182aaf4878e153844719)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"6:30pm. https://youtu.be/kQPbuV-ZaVY
INTERVIEW CODING CHALLENGES

Is this guy really some god tier programmer?

https://youtu.be/zA1KuiAULEQ?t=1199
> Why bother with HTTP when every can easily be gRPC?

Isn't that over HTTP?

7:05pm. https://youtu.be/zA1KuiAULEQ?t=1510
> Config driven development.

This is an interesting term to keep in mind.

https://youtu.be/zA1KuiAULEQ?t=1633
> Mechanical sympathy.

I really like these two words.

https://youtu.be/zA1KuiAULEQ?t=1913

He makes his own prediciton which is that we are going to run into CPU power problem.

And admittedly, my reason is telling me that he is right, though I'll interpret his prediction as being about computation in general.

I wouldn't be in this shit if hardware growth was decent.

Yeah, I am fanboying over AI chip companies doing something miraculous, but remember how that turned out for me over the last decade?

That company I've pinned my hopes on will just turn out to be a dud, and then what?

I'd be better off putting my faith in the big cloud hyperscalers to give me something good, than AI chip startups.

https://youtu.be/zA1KuiAULEQ?t=1940
> We need a magical revolution that will just change stuff quite a bit.

He predicts a slow increase and that we are just about to hit the golden age of computing.

> This is just about the best time to be a programmer.

Then the video cuts off abruptly.

https://youtu.be/n7F7wMdgfuI?t=55
> Working in open source, is really, really hard. And it's not fun.

https://youtu.be/n7F7wMdgfuI?t=213
> Right now in our soft engineering world, the interviews are the easiest they've ever been.

https://youtu.be/n7F7wMdgfuI?t=277
> For me it takes 3 interviews to get into the interview world.

https://youtu.be/n7F7wMdgfuI?t=861
> I couldn't afford a house in the yard with a Netflix salary.

I recall those were 400k/year. What the hell?

https://youtu.be/n7F7wMdgfuI?t=1019
> This C++ is a really great language to learn in school.

Yeah, no.

https://youtu.be/n7F7wMdgfuI?t=1076
> A better kata: start a websocket server and build a chatroom.

https://youtu.be/n7F7wMdgfuI?t=1113
> I am out of my depth, I am not drawn to anything.

Kek. I could say the same thing.

https://youtu.be/n7F7wMdgfuI?t=1349
> Someone says I have a cool voice, I don't have a cool voice, I sound like a cartoon character.

https://youtu.be/n7F7wMdgfuI?t=1375
> Right now, the programming world is much harder. To get in is much harder.

https://youtu.be/n7F7wMdgfuI?t=1446
> He choose the world possible time ever to quit a job.

https://youtu.be/n7F7wMdgfuI?t=1519

This is good advice. I should ask the interviewer how I could have done better in interviews.

8:05pm. https://youtu.be/kUs-fH1k-aM
Do you REALLY need SSR?

https://youtu.be/MCQWfMg0Z9w?t=613
> A teacher once told me 90% of learning is teaching.

I never thought about it like that, but I will admit that doing Youtube vids is motivating me a lot.

I am not sure I'd have the drive to self improve without it.

8:25pm. https://youtu.be/02Dsv86tEPo?t=2444
【艦これ Heavy/Power Metal】Best of Yellow Squadron

Forget prime. Let me do some reading.

4/28/2023

8:40am. Let me read the Baki chapter first and then I'll get started.

8:55am. Let me start.

https://youtu.be/_p16mwfE9as
If you only learn ONE Shortcut... Make it this one! Davinci Resolve

I'll start with this, then Theo's SSR vid, then the microservice vid from yesterday.

The Kaminaki threads are really drawing me in, but I'll leave the anime for later.

https://youtu.be/_p16mwfE9as?t=94

Ohhhhhhhhhhhh!!!

You can paste the vids like this without them having the audio?

That was one of my major annoyances with DR and now it is resolved.

https://youtu.be/_p16mwfE9as?t=215

I had no idea.

https://youtu.be/_p16mwfE9as?t=299

This is an excellent video.

9:10am. Let me move on to Theo's vid.

https://youtu.be/kUs-fH1k-aM?t=494
Do you REALLY need SSR?

https://youtu.be/kUs-fH1k-aM?t=746

Ok, I am kind of tuning out here. What is going on? It doesn't matter too much.

https://youtu.be/kUs-fH1k-aM?t=1073
> Most sites and most experience should default to SSR when they can.

Hmmm...

https://youtu.be/46DkGih90a8
I Have Never Worked | Prime Reacts

9:35am. Let me watch this just for 5m.

https://youtu.be/46DkGih90a8?t=1266
> If this has been a common experience, there is no wonder there have been so many layoffs.

I've read the article itself a few days ago, but it is interesting how many people in his chatroom confirm what it is saying while Prime himself is the one being shocked.

10:10am. Ok, enough of these. Let me chill for a bit, and I'll finish the microservice vid from yesterday. I'll go start from finish instead of skipping it.

10:40am. Let me start for realsies.

It is time for microservices.

https://youtu.be/DFDbh1c9zyE
What are microservices?!?!? Let’s build one with .NET and Docker!

I am going to focus on this and then I am going to turn the poker app into a microservice. It is at that point that it will be worth putting on my resume.

https://youtu.be/DFDbh1c9zyE?t=449

I once watched a 1h video on Docker, but never used it properly. maybe this time around I will.

https://youtu.be/DFDbh1c9zyE?t=925

Why not copy them all at once?

https://youtu.be/DFDbh1c9zyE?t=1016

This is a good video.

11:10am. https://youtu.be/sstOXCQ-EG0
Let's Learn .NET - Microservices

I am not going to watch this, it's two hours.

Where is that learning path he mentioned.

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/

> We wrote this guide for developers and solution architects who are new to Docker-based application development and to microservices-based architecture. This guide is for you if you want to learn how to architect, design, and implement proof-of-concept applications with Microsoft development technologies (with special focus on .NET) and with Docker containers.

Ok...

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/docker-application-state-data

I am skimming through this, and I see that this is going to be another potus.

Nevermind these books and tutorials. Let me get started on video 32.

11:25am. You know what, let me get rid of env files. They are just washing my time.

11:35am.

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import {resolve} from 'node:path'

const config = {
    PORT: 8080,
    PROXY_PORT: 5000,
    ROOT: "src/client",
    DEPLOY: "deploy/public"
}

// https://vitejs.dev/config/
export default ({mode}) => {
    const target = `http://localhost:${config.PROXY_PORT}`

    return defineConfig({
        root: config.ROOT,
        build: {
            outDir: resolve(process.cwd(), config.DEPLOY)
        },
        server: {
            port: config.PORT,
            proxy: {
                "/api": {target, changeOrigin: true},
                "/socket": {target, ws: true}
                }
            },
        plugins: [react()],
        define: {
            // remotedev will throw an exception without this.
            global: {}
            }
        })
}
```

I am just doing some cleaning up of the project build.

```
caught Error: createRoot(...): Target container is not a DOM element.
    at createRoot (react-dom.development.js:29345:11)
    at Object.createRoot$1 [as createRoot] (react-dom.development.js:29800:10)
    at exports.createRoot (client.js:12:16)
    at Program_Internal_withReactSynchronousUsing (react.fs:57:32)
    at App.fs:188:9
    at App.fs:21:4
```

I am trying to run the Leduc applciation and am getting this error.

```
open Feliz
let view model dispatch =
    Html.div [
        Html.text "Hello"
    ]
```

What happens when I make the view this?

```
<body>
    <div id="root"></div>
    <script type="module" src="output/App.js"></script>
</body>
```

What is going on here? Here the id is root.

```
|> Program.withReactSynchronous "elmish-app"
```

But here it is looking for elmish app. I wonder how that happened?

```
<div id="app"></div>
```

Let's just make it app.

Yeah, now it prints hello.

11:45am. Pushed that into master. I git rid of the html and react courses.

Now...

11:55am. How do I edit the starting timecode again.

https://youtu.be/r20NdlqwSPU
Markers in Davinci Resolve and How to Export Markers for YouTube Chapters in DaVinci Resolve 18

This video shows it all. I compained about the advice, but in the end I couldn't find a better way.

https://youtu.be/r20NdlqwSPU?t=160

Why are so many timeline options only available when right clicking in the media pool?

12pm. Damnit. Resolve got me good here. For some reason these settings aren't in the cut page.

I did try right clicking on it before looking at the video for advice, but they weren't there. For fuck's sake.

12:20pm. I am 1m in, and need to take a break as I am getting hungry.

Let me stop here.

This served as an ice breaker.

2:20pm. Done with breakfast and chores.

Today I am taking a vacation so let me watch another ep of Kaminaki. Then I will resume.

The anime is pretty fun.

2:35pm. Ok, I'll get serious here.

I know that I am spending my good hours relaxing instead of programming, but anime is less fun when you are stressed out and tired after working for an entire day.

2:40pm. Now where was I?

3:35pm. How do I import from another video. Could I import the previous timeline. I want that merely for the sake of getting the audio from where it was left off previously.

https://youtu.be/J5R0wsAwCGk
Copy and paste TIMELINE to different project! Davinci Resolve Quick Tip!

https://youtu.be/J5R0wsAwCGk?t=20

This is the shortest tip that I've ever seen. Upvoted and close.

Oh, I can just paste a clip directly as well! That is even better for what I want to do.

7:10pm. Done with lunch and another round of chores. I guess I'll stop the session here.

Currently I am 7.5m into the screencast. I'll up my pace tomorrow.

Time to rest. Today was quite leisurely.

By the looks of things, microservices shouldn't be hard.

For some reason auth was way harder than it had any right to be which is why it took so long. But with this...

I'll acquire a lasting skill.

7:35pm. Actually websockets aren't too less expensive...but still 3x is not insignificant.

7:55pm. Had to do some extra editing.

8pm. I am 8:45m in.

Not bad.

Let me close here. I am pleased with my work today.

Tomorrow, I'll have a chance to do some interesting programming."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[f03b38911e...](https://github.com/i574n/The-Spiral-Language/commit/f03b38911ed12bc84d845dbd50d1b27a7c9e456d)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"https://github.com/eiriktsarpalis/TypeShape

This is interesting.

10:35pm. https://youtu.be/cdG2JxuZvNI
C# Reflection Explained (Claim generation example)

Ah, fuck it. I do not feel like novels. Let me study reflection.

https://www.reddit.com/r/fsharp/comments/12xvydy/are_there_any_good_resources_on_reflection_in/

///

In the video I am working on, I want to show how the `Fable.Remoting` proxy can be wrapped around by a handler that catches the 401 errors and reacquires the tokens if they are expired.

What I want to do is map over all the record fields at runtime, and simply apply a wrapper function to them. If this was vanilla .NET I'd easily be able to find learning resources on reflection, but I'd like some advice about the things I need to know in Fable land.

Sigh, despite using F# for so long, I've always avoided tackling .NET reflection, but I know from experience (of programming in [Spiral](https://github.com/mrakgr/The-Spiral-Language)) that this is a perfect place to introduce these techniques. Type systems like F#'s really hit their limits when it comes to serializing data across platform and language boundaries, so this is The place to demonstrate the use such methods.

I'd really be doing my viewers a disservice if I didn't.

///

Decided to ask here.

https://mangadex.org/title/59e04a79-435e-418d-8b64-c8d4315693ab/akuma-koujo
https://ellotl.com/rose-princess-of-hellrage-volume-1-chapter-1/

I keep forgetting about these. They completely slipped my mind, I only saw them at the start of yesterday's commit.

http://fsprojects.github.io/FSharp.Interop.Dynamic/examples.html

This is pretty cool.

https://github.com/MicrosoftDocs/visualfsharpdocs/blob/main/docs/conceptual/reflection.fsharpvalue-class-%5Bfsharp%5D.md

I can only hot that the Fsharp reflection namespace works in Fable. If it doesn't I'll open issues.

https://fsharp.github.io/fsharp-core-docs/reference/fsharp-reflection-fsharpvalue.html

Oh wow, this has links to the source.

https://fsharp.github.io/fsharp-core-docs/reference/fsharp-reflection-fsharptype.html

Everything I need seems to be here.

https://www.daniellittle.dev/dynamically-calling-a-function-in-fsharp

12pm.

https://fable.io/docs/dotnet/compatibility.html
https://github.com/fable-compiler/Fable/blob/main/tests/Js/Main/ReflectionTests.fs

Reflectio support for types known at compile time seems pretty good.

https://github.com/fable-compiler/Fable/blob/main/tests/Js/Main/ReflectionTests.fs#L389

Oh, check this out. They are using FsharpType here.

4/25/2023

8:25am. I haven't gotten enough sleep, but nevermind. What I want to do right now is play with reflection.

More specifically, how do I apply a function?

8:45am. My god, I forgot how foralls work in Spiral.

```
open System
open FSharp.Reflection

let f x = x
let t' : bool * string -> _ = f
let t = box t'

t.GetType().GetMethod("Invoke").Invoke(t,[|true, "asd"|])
```

This is how functions could be invoked. Ok.

But how do I apply generic parameters at runtime?

For functions, they are always specialized, so that can't be done.

9:30am. I'll leave bath for later.

Let me get this obsession out of the way.

1pm. Almost done with the video, let me have breakfast here. I

2:25pm. Done with breakfast and chores.

I was so eager to do the video that I skipped out on the bath today.

Let me resume.

2:50pm. i need to look up audio normalization in Da Vinci.

I am basically done. I just need to place the markers and normalize the audio.

https://youtu.be/thJoBJ6Cl_E
How to Normalize Audio to Get Consistent Audio Levels in DaVinci Resolve 17

...Can I put a highlight around my cursor somehow in Da Vinci?

https://photography.tutsplus.com/tutorials/how-to-normalize-audio-for-youtube-using-davinci-resolve-fairlight--cms-37397

3:05pm. https://youtu.be/x3vTEFQV0uo
How to Normalize Your Audio for YouTube in Davinci Resolve

That last video is a bit shitty. Let me watch this one. I am trying to figure out how to automate audio normalization and failing.

https://youtu.be/x3vTEFQV0uo?t=158

Automation tool. That is what I want.

https://youtu.be/lHNhxGojFRU
Understanding How to Loudness Normalize Your Audio for Video

There is a difference between loudness and volume?

Goddamit, this is so annoying. I do not understand why volume normalization in DaVinci Resolve is giving me trouble. If possible, I'd like to avoid exporting into Rx, or doing it manually like some of those other videos suggest. Those guys are so incompetenent.

Isn't there a way for the program itself to give me a measure?

I just want to click a few buttons to set the peak and level. Why are you bothering me with this?

https://youtu.be/nOzZKEWJ5wk
Volume vs Loudness - LUFS & LKFS for Measuring Loudness for Video

3:35pm. Ah, damn it. There is an analyze and normalize in the fairlight page just as one might expect, but it was in a different place so I missed it.

https://youtu.be/nOzZKEWJ5wk?t=457

Oh, I hadn't realize this existed.

3:55pm. Agh, it is a day like this.

It turns out the normalize control in Fairlight is not as good in RX. If I set a target loudness and a level, and the loudness is above the limit, it won't do the sensible thing of optimizing for both. Instead it will prioritize the loudness. RX on the other hand would give me both.

I'll have to figure out how to use a limiter or a compressor. Sigh. Let me just study this.

https://youtu.be/nOzZKEWJ5wk?t=495
> My recommendation when you are actually uploading a Youtube video is to target -16 or -17 LUFS.
> Why not the target of -14 that Youtube has established?

https://youtu.be/lHNhxGojFRU?t=46
Understanding How to Loudness Normalize Your Audio for Video

Let me go back to this.

https://youtu.be/lHNhxGojFRU?t=110

One thing I am confused about is where the bus got lost. I had the track before and now I don't.

https://youtu.be/lHNhxGojFRU?t=224

Oh, lol he just exports it into Isotope Rx.

https://youtu.be/lHNhxGojFRU?t=227

Yeah, that is what I intended to use! But I was wondering if there was a way to do it all in Fairlight.

Still, where did that option to export to Rx come from?

https://youtu.be/lHNhxGojFRU?t=425

Agh, he is using a compressor really agressively. He says that once the files get uploaded to Youtube the headroom will shrink even more so we need -7db? Really?

https://youtu.be/T9O40fH6Oxg
DaVinci Resolve FAIRLIGHT TIPS // iZotope RX Integration

https://youtu.be/T9O40fH6Oxg?t=146

I've tried this, but it turns out, I can only send out a single clip. It is useless for me.

https://youtu.be/Rp-6F8SWFSY?t=329

I can just bounce the track like this? Let me try it. That is cool.

https://youtu.be/Rp-6F8SWFSY?t=463

https://youtu.be/Rp-6F8SWFSY?t=601

Hmmm, this is fairly easy to understand.

https://youtu.be/Rp-6F8SWFSY?t=813

Ah, yes, I turned off the automation. That is where the bus disappeared.

5:30pm. file:///E:/!Screencasts/The%20Fabled%20Web%20Adventure/OBS%20Output/izotope-rx-loudness-control-help-documentation.pdf

I am reading the user's guide for Rx's loudness control.

So far my impression of Fairlight is very negative.

It is just making me mess with things.

///

> How does RX Loudness Control comply with different loudness
standards?
RX Loudness Control first analyzes the audio source file. Then it computes the amount
of transparent correction required to hit the target without a perceived change to the
dynamic range. The correction pass includes three elements:
1. A fixed amount of gain to hit the specified Integrated loudness
2. [optional] An RMS compressor to limit the Short-term (or Momentary) loudness
3. A True Peak limiter
Steps 2 and 3 work only on an as-needed basis. If the audio signal already meets Shortterm and True Peak specs, no extra processing is applied.

///

I am not sure how this works and whether it is applying the limiter or the compressor and it turns out that is does? Then why am I not using this. I could have exported into RX, and have been done with this shit in 5m.

Instead I here I am wasting hours messing around.

///

How does RX Loudness Control use compression?
RX Loudness Control uses compression in a way that preserves the quality of your audio.
When needed, a compressor dynamically adjusts your audio to ensure you get the
best sound while remaining compliant. For loudness standards that require Short-term
or Momentary compliance, the compressor is engaged automatically when loudness
exceeds the specified target. You simply enable the slider via an on/off button and set
the target. The Short-term/Momentary slider toggles between both modes, and can be
turned on or off.

///

Just let this program do its thing. Stop being a retard.

5:45pm. Ah damn it, the stupid thing can show wrong true peaks in analyze mode.

Once I played the offending part, it was below 0 it turns out.

Shitty program.

No, forget Fairlight.

Even Reaper is better than DR for audio editing. DR doesn't even have reliable analysis.

6:20pm. I am extremely tired right now. I might as well just leave the video for tomorrow.

How the fuck do I export this? Why isn't the render queue doing anything?

...Because I didn't click on the Render All button. I simply missed it as it is a light gray outline on a gray background.

6:25pm. Ah, fuck it. I'll post it tomorrow. Let me have lunch. I am too tired to mess with this anymore.

7:10pm. https://youtu.be/3LOBFWdmyQI
Authentication With ASP.NET Core And The SAFE Stack. Reactive SPA Logins (Pt. 7)

Here is the link to it. I'll finish it tomorrow. Right now I am far too exhausted. I can't think at all after today's session.

I can't even remember what the purpose of today was.

Reactive SPA Logins aren't it. Maybe token regeneration?

I'll change the title to that later. Let me have fun here."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[53f1486556...](https://github.com/i574n/The-Spiral-Language/commit/53f1486556578e25943bf3b1fc76df7e7d4936c6)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"6:45pm. https://boards.4channel.org/g/thread/93041086/sdg-stable-diffusion-general

Compared to last year, the level of AI art is insane here.

God, I am tired. My brain feels like it will explode.

7:30pm. https://emaggiori.com/employed-in-tech-for-years-but-almost-never-worked/

7:35pm. i am fucking going to bed. I'll die at this rate from mental exhaustion.

4/27/2023

7:55am. Despite being in bed for over 12h, I did get much sleep. I am still tired, but I should be more rested than before.

Last night, I was so wound up, I felt like a zombie.

8am. I still am somewhat.

Let's give this 'toubing another month and then I will see how fit I am for contracting.

https://mangadex.org/title/135b2ea2-94a7-4499-aa2e-85f3efae4a4c/daily-life-in-ts-school
https://mangadex.org/title/5e9a2a3e-f992-4af4-a887-cd130460c9e5/baki-dou

For now let me just read the latest of these. Then I will do some recording. I want to get the IndexDb down.

https://youtu.be/NNuTV-gjlZQ
Storage for the web

https://web.dev/storage-for-the-web/

https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage
https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API

8:55am. My dad just called to tell me there will be a power outage from 9am to 1pm. I am turning off here.

9:20am. So much for that power outage. Maybe it will happen later.

Let me do my screencasting, and if I lose some work due to a sudden turn off, then so be it.

9:40am. Still hasn't happened.

9:55am. The power's still on.

10:30am. It is still on.

10:45am. Oh, changing the duration in the cut and the edit pages has different behavior. In the cut page it ripples the timeline, which is a lot more useful than the overwritting on the edit page.

11:30am. Had to take a break, let me resume.

12:05pm. I have 9:15m worth of video. I could end it here.

But let me study IndexDb a bit more before I make the decision.

https://youtu.be/vb7fkBeblcw
IndexedDB Crash Course with Javascript

https://youtu.be/vb7fkBeblcw?t=92
> It is essentially an object key value store.

So that is all there is to IndexedDb?

https://youtu.be/vb7fkBeblcw?t=300

Why the fuck am I wasting my time watching this? Forget it.

Let me just watch a bit on NoSql.

https://youtu.be/0buKQHokLK8
How do NoSQL databases work? Simply Explained!

https://youtu.be/0buKQHokLK8?t=75

I had no idea that SQL has a hard time scaling.

https://youtu.be/0buKQHokLK8?t=105
> They are key value stores

https://youtu.be/0buKQHokLK8?t=310

Hmm, really?

https://youtu.be/0buKQHokLK8?t=400

Hmmm...

https://youtu.be/0buKQHokLK8?t=420

I should look into CouchDb as there is an IndexedDb library based off it.

12:35pm. No there is no need to go deeper.

1:20pm. In the end, the power never went out even once.

1:40pm. We'll let it render for a while.

Let me have breakfast.

2:20pm. https://www.nango.dev/blog/why-is-oauth-still-hard

I need to keep Nango in mind in the future. No way do I want to go through the experience of last 3 weeks again.

https://news.ycombinator.com/item?id=35713518
> That drove me up the wall in Python so much - ALL the documentation just described how to put a massive library into a cookie cutter example and never explained how it's supposed to work so I could debug the darn thing.

> Asp.Net authentication is 10 times worse in this regard.

///

It'd be interesting to hear about people who have had a good time implementing OAuth, as my experience is similar to that in the article. I've played with adding it to a few side projects and the process usually goes:

1. Read loads of docs, end up pretty confused
2. Find a library that seems to do what I want
3. Install this huge library full of opaque code doing...things
4. Have an impossible time troubleshooting issues
5. Get scared ("I'm almost certainly doing something wrong here") and give up

I find it hard to have much faith in security standards like this. I want them small, well defined and understandable and OAuth does not meet any of these criteria in my experience.

///

3:25pm. Done with breakfast and chores.

Let me resume. For some reason the upload failed last time so let me do it now.

3:30pm. How did I export the markers into CSV last time?

Ah, right click on the timeline.

https://stackoverflow.com/questions/2459472/executing-f-scripts

Now I ma wondering why it didn't run the script file.

3:45pm.

```fs
#r "nuget: FSharp.Data"

open System.IO
open FSharp.Data

let f =
    CsvFile
        .Load(Path.Combine(Directory.GetCurrentDirectory(), "f.csv"))

System.Console.SetOut(File.CreateText(Path.Combine(Directory.GetCurrentDirectory(),"toc.txt")))

for row: CsvRow in f.Rows do
    printfn "%s %s" (row.GetColumn "Source In") (row.GetColumn "Notes")
```

How much time is this going to take me? At first I exported the wrong thing, but now it is messing with this.

Why am I doing this anyway?

https://youtu.be/LqoIz8Nx7Ts
Authentication With The SAFE Stack. Generalized Remoting Proxies, Reactive Tokens, IndexDb. (Pt. 8)

Here is my masterpiece.

4pm. Organized them into a separate playlist.

https://www.youtube.com/playlist?list=PL04PGV4cTuIVZGJZI1POoobUSjmSIhIlc
Authentication With ASP.NET Core And F#

I'll post this one into the F# slack.

4:05pm. Posted it on the F# sub, slack and twitter.

4:10pm. Phew.

e: is at 20gb?

How the hell did that happen?

4:15pm. I shouldn't have tried turning on the render cache that one time. I observed the opposite of the screencast being smoother when I did.

Anyway, I am done for the day. Who is going to do any more?

Actually, I do feel like doing more.

If I can clear the microservice hurdle, I could try looking for jobs again.

4:20pm. Right now let me chill for a bit and then I'll watch a video or two. I still haven't read the Mahoako chapter.

5:25pm. https://youtu.be/DFDbh1c9zyE
What are microservices?!?!? Let’s build one with .NET and Docker!

Done with lunch. I kind of feel like watching this.

5:45pm. https://youtu.be/DFDbh1c9zyE?t=622
What are microservices?!?!? Let’s build one with .NET and Docker!

I'll keep these learning paths in mind. Let me close here. This video is so boring that I skipped a quarter of it. I'll leave the hands on stuff for tomorrow.

It is fine to stop at this time. I went through quite a gauntlet in the last month. April is almost over. Hopefully, May will be more interesting.

5:55pm. It seems the economy is booming in Netherlands. It might be worth looking for a RJ there."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[6d270e8578...](https://github.com/i574n/The-Spiral-Language/commit/6d270e8578a291106c5677adb3999a204bd594ba)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"https://edoras.sdsu.edu/~vinge/misc/singularity.html

Somebody posted this on HN.

///

            o Develop human/computer symbiosis in art: Combine the graphic
              generation capability of modern machines and the esthetic
              sensibility of humans. Of course, there has been an enormous
              amount of research in designing computer aids for artists, as
              labor saving tools.  I'm suggesting that we explicitly aim for a
              greater merging of competence, that we explicitly recognize the
              cooperative approach that is possible. Karl Sims [22] has done
              wonderful work in this direction.

///

Amazing that this is happening.

4/19/2023

7:40am. I woke up even earlier than this and lounged in bed, thinking bad thoughts. It is better than I got up just now even though I am yawning here. Yesterday I actually went to bed at 11pm instead of 1am like usually as I was dead tired and couldn't read anymore.

Let me read Baki Dou. I guess I'll chill for a while before starting.

...I see somebody is trying to log into my Azure AD account. Not gonna work.

8:20am. I am anxious today. Maybe failing to finish the vid yesterday impacted my mental state.

Let me just read another chapter or two and then I'll get started for the day.

I see I am going to have to restart the video, or at least, cut out large parts of it.

Well whatever.

It is fine, if I just leave in the static file serving parts and then the proxy I am going to get right today hopefully.

8:25am. Things like this just happen.

I am missing my own deadlines, and so is Re;Library. But the most important thing is to keep working at it in order to get through it.

9:20am. Let me start for the day.

If I can make it work, I'll reward myself by closing it early.

Sigh, I probably should slept longer, but nightmares woke me up early.

> Ok that one at least I can answer, if the Vite Server is well behaved and is passing the X- headers proxies to then wiring up the forwarded headers middleware will take of that.

https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-7.0

> Forwarded Headers Middleware is enabled by default by IIS Integration Middleware when the app is hosted out-of-process behind IIS and the ASP.NET Core Module (ANCM) for IIS.

So is this why IIS works?

```fs
    app
        .UseForwardedHeaders()
```

Let me try it.

9:30am. I'll have to open it in the debugger. I need to see if there are those X-Forwarded fields in the header.

9:35am. Nope, those forwarding headers aren't present in the request.

https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-7.0#azure

For Azure I might have to turn on cert forwarding.

9:45am. Hmmm, there is in fact a x-remoting-proxy field in the header.

https://ruslan.rocks/posts/vite-proxy-how-to-setup

> xfwd: true/false, adds x-forward headers

Oh there is this option.

> autoRewrite: rewrites the location host/port on (201/301/302/307/308) redirects based on requested host/port. Default: false.

There is also this.

> followRedirects: true/false, Default: false - specify whether you want to follow redirects

Ohhhhh...

```
"/api": {target, changeOrigin: true, followRedirects: true},
```

Let me try this.

...I no longer get the cors error, but the redirect is not happening. Let me redirect to google.

10:10am. Does it run in Bundle mode? Why is the redirect completely missing.

...Yeah, in the production case, it goes straight to google.

https://stackoverflow.com/questions/64677212/how-to-configure-proxy-in-vite

> For debugging I highly recommend to add event listeners to the proxy, so you can see how the requests are transformed, if they hit the target server, and what is returned.

```
proxy: {
        '/api': {
          target: 'https://localhost:44305',
          changeOrigin: true,
          secure: false,
          ws: true,
          configure: (proxy, _options) => {
            proxy.on('error', (err, _req, _res) => {
              console.log('proxy error', err);
            });
            proxy.on('proxyReq', (proxyReq, req, _res) => {
              console.log('Sending Request to the Target:', req.method, req.url);
            });
            proxy.on('proxyRes', (proxyRes, req, _res) => {
              console.log('Received Response from the Target:', proxyRes.statusCode, req.url);
            });
          },
        }
      }
```

```
console.log('Received Response from the Target:', proxyRes.statusCode, req.url, proxyRes.headers.toString());
```

Mhhh, for fuck's sake. How do I print out the stuff here. It just gives me [object Object].

JSON.stringify().

11:05am. A nightmare. This is a nightmare.

```js
                "/api": {target, changeOrigin: true,
                    secure: false,
                    followRedirects: false,
                    xfwd: true,
                    autoRewrite: true, hostRewrite: true, protocolRewrite: true,
                    configure: (proxy, _options) => {
                        proxy.on('error', (err, _req, _res) => {
                            console.log('proxy error', err);
                        });
                        proxy.on('proxyReq', (proxyReq, req, _res) => {
                            console.log('Sending Request to the Target:', req.method, req.url);
                        });
                        proxy.on('proxyRes', (proxyRes, req, _res) => {
                            console.log('Received Response from the Target:', proxyRes.statusCode, req.url, JSON.stringify(proxyRes.headers));
                        });
                    },
                },
```

Proxy forwarding and `app.UseForwardedHeaders()` isn't doing jack. I figured out how to include the forward headers, but they are pointless.

I am going to switch gears. Forget hot module reloading. We'll configure the project so it works...

Let me have breakfast here and I will finish the video.

11:15am. If I double click the request in the network tab it actually auth successfully and gives me back a cookie.

11:25am. Let me have breakfast here. I'll finish the video.

I am going to ditch the Vite server and just have the client output into the Server's public folder.

12:30pm. Done with breakfast. Let me take a break. Everything is messed up.

1:10pm. https://github.com/AzureAD/microsoft-authentication-library-for-js

> Would moving all of the authentication to the client work? If I authenticated the user using the [AAD library](https://github.com/AzureAD/microsoft-authentication-library-for-js), would the cookie be valid with the server which is using `Microsoft.Identity.Web`?

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react

I suppose it is worth a try.

1:55pm. Let's end the video here. I need a break from this.

For the next video I meant to do the database, but I'll do client side logins instead.

2:20pm. It is rendering.

A single key on a page. Highest detail, best quality, 4k, masterpiece.
Dull, muted, ugly, blurry.

Let me make some more images of these.

2:35pm. https://youtu.be/lNYZi9v9QoA
Authentication With ASP.NET Core And The SAFE Stack. SPA Login From The Server. (Pt. 5)

Here it is. Not my best work, but it will do.

2:50pm. Posted it on the F# sub, and posted it on Twitter.

Damn it, I do not feel like it. Let me chill a bit before I get started on the next part.

3:20pm. Let me get started.

Let me watch the video by Anton when SPAs are on different domains.

https://youtu.be/PUXpfr1LzPE?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core External Authentication (OAuth, .NET 7 Minimal Apis C#)

3:25pm. Forget it, it is just going to waste my time.

Let me go forward bravely.

4:35pm. I closed all those issues. I do not want to bother with them anymore.

5:05pm. I have 2:50m of the video done.

I really want to close here. I got up earlier than usual today.

I'll at least close the recording. Right now, I need to read the docs, and I've been bashing my head against them for the past few days so I am sick of it.

Who is going to take that kind of trip at 5pm?

5:10pm.

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react#msal-basics

https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/initialization.md#optional-configure-authority

So this is where I need to put in the tenant id.

> Once you have retrieved the access token, you must include it in the Authorization header as a bearer token for the request to the resource you obtained the token for, as shown below:

So is that how it works?

It uses JWT tokens instead of cookies? I guess that answers the question of how it should be decrypted.

https://learn.microsoft.com/en-us/answers/questions/671313/multi-tenant-apps(front-and-back-separation)-how-t

> The resource server will validate the access token and determine if it has the right permissions, using the information within the token.

I do not get how to do that yet.

https://www.compositional-it.com/news-blog/safe-stack-authentication-with-active-directory-part-2/

Damn it, I forgot about this.

https://stackoverflow.com/questions/72850957/verifying-token-from-msal-react-on-backend

This is exactly my biggest unkown right now.

https://learn.microsoft.com/hr-hr/azure/active-directory/develop/access-tokens#validating-tokens

https://learn.microsoft.com/hr-hr/azure/active-directory/develop/access-tokens#validate-tokens

> The Azure AD middleware has built-in capabilities for validating access tokens, see samples to find one in the appropriate language. There are also several third-party open-source libraries available for JWT validation. For more information about Azure AD authentication libraries and code samples, see the authentication libraries.

5:45pm. https://learn.microsoft.com/hr-hr/azure/active-directory/develop/sample-v2-code

Uh, what am I supposed to use to validate the JWT tokens? There are a shitload of samples here.

> I am working on a SAFE Stack application and to get around the redirect difficulties caused by the Vite dev server, I'll implement most of the necessary auth logic on the client. The docs for MSAL React are straightforward. I'll figure out to include the JWT token in the requests as well. What I am having trouble understanding is just how am I supposed to validate the token on the ASP.NET side. Which library am I supposed to use for that? One thing I've to understand is how ASP.NET is handling secret keys. Assuming the client and the server use the same one, I'll have no trouble validating the token using the JWT middleware, but will it really be that easy? I have no idea what goes on under the hood.

https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/blob/master/4-WebApp-your-API/4-1-MyOrg/README.md

I think I should just start with MSAL.NET.

https://github.com/AzureAD/microsoft-authentication-library-for-dotnet

> Microsoft.Identity.Client

Oh this is the MSAL for .NET package. I remember it having a ton of downloads.

It doesn't seem to have any functions I can use to validate the token from a request.

https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/blob/master/4-WebApp-your-API/4-1-MyOrg/README.md

I am going to study this tomorrow. It doesn't matter from where the token comes from. The web API will have to verify it either way, and that is when I will know how it could be done.

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react#samples

Or I could just check the advanced examples out here.

https://github.com/Azure-Samples/ms-identity-javascript-react-tutorial/tree/main/3-Authorization-II/1-call-api

This is exactly what I need.

https://github.com/Azure-Samples/ms-identity-javascript-react-tutorial/blob/main/3-Authorization-II/1-call-api/API/authConfig.js

This isn't too hard. It seems it uses vanilla JWT middleware to decode the stuff. Still, what about the secret key for the encryption. I am confused where that should come into play.

Ah whatever. I'll figure it out somehow.

https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/implementation/key-management?view=aspnetcore-7.0

6:20pm. Enough. I'll just pass the token through the JWT middleware and if that fails ask for help. This is not work debating any further.

Let me close here. Time to rest."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[57e9789c55...](https://github.com/i574n/The-Spiral-Language/commit/57e9789c557c17432804a5ecfb116f2d6151d581)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"11:20am. I've gotten into it. I actually got all these packages installed. Tomorrow I'll post it on Github and try importing it.

5/5/2023

8:35am. I am up. Let me chill.

9:15am. As soon as the bathroom clears I'll take a bath and then resume from where I left off yesterday.

10:30am. Done with the bath. Let me start.

https://youtu.be/tlI_07ZZImg
Amazing Card Flip Transition / Generator / Davinci Resolve Tutorial / Fusion

The lack of card transitions has really been irking me. Let me just watch this.

https://youtu.be/tlI_07ZZImg?t=149

This is so annoying. I do not want to program DV every time I do this. Is there a way to get it out of the box? Or maybe I should just do this and find a way to save the transitions.

https://youtu.be/tlI_07ZZImg?t=414

Let me stop this here. I'll come back to it later.

///

And it didn't work. We said we'd scavenge, but...
Let's pause here. We'll try cloning the project again and seeing if we can get it to build in isolation.
Either way we'll have to study it.
I guess this is one of the pains of programming in a relatively unpopular language.
Its ecosystem is not as robust as it would be for bigger languages.
All that we do is for the love of functional programming, so here we'll pause and consider our options more carefully yet again.
We spent a lot of time thinking what we'd do with the library, but not so much what we'd do if it turned out to be out of date.

///

Let me cut this out.

11:15am. Ah, maybe it is trying to get Fable.SignalR.Saturn from the Nuget package instead of my own.

11:20am. https://github.com/fsprojects/Paket/issues/

Check out issue 3064.

> I reviewed the documentation again, GitHub dependencies. At the time I somehow thought that paket allowed the import of github hosted libraries similar to how it treated nuget. Upon review, that is not the case. The documentation in this area could use some work.

11:35am. Holy shit, what are all these errors?

Ah, it must have been caused due to reloading errors.

12:55pm. No, I need to pause and study the library properly without necessarily being tied by the presentation work.

Oh, I see how we could get the state!

Using services.

Still, I do not want to add middleware for every model type. I wonder if it would possible to avoid doing that.

Something like a scoped service for every request, but it is generic object?

https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/hubs-api-guide-server#hub-object-lifetime

///

Hub object lifetime
You don't instantiate the Hub class or call its methods from your own code on the server; all that is done for you by the SignalR Hubs pipeline. SignalR creates a new instance of your Hub class each time it needs to handle a Hub operation such as when a client connects, disconnects, or makes a method call to the server.

Because instances of the Hub class are transient, you can't use them to maintain state from one method call to the next. Each time the server receives a method call from a client, a new instance of your Hub class processes the message. To maintain state through multiple connections and method calls, use some other method such as a database, or a static variable on the Hub class, or a different class that does not derive from Hub. If you persist data in memory, using a method such as a static variable on the Hub class, the data will be lost when the app domain recycles.

If you want to send messages to clients from your own code that runs outside the Hub class, you can't do it by instantiating a Hub class instance, but you can do it by getting a reference to the SignalR context object for your Hub class. For more information, see How to call client methods and manage groups from outside the Hub class later in this topic.

///

Forget this. Let me chill.

2:40pm. Let me resume. I finally installed the library, and what I have to do is figure out how to deal with state. One method that sticks out is to instantiate a mailbox processor for every request. We'll see...

But I do want to get some measure of control over this.

And that library has little documentation.

Maybe I'd have been better off with raw SignalR + my own serialization.

```fs
hubContext.Context.Items
```

> Gets a key/value collection that can be used to share data within the scope of this connection.

Oh wow. The context also has what I need for aborting the connection. It also has a cancellation token that I can use to detect when the connection is over.

Wonderful.

3pm. https://learn.microsoft.com/en-us/aspnet/webhooks/

Oh webhooks are a thing.

https://learn.microsoft.com/en-us/aspnet/signalr/videos/

Oh there are some vids in the docs.

...A single one.

Ok, focus me.

4:10pm.

```
Type constraint mismatch. The type 'SignalR.State.Send<'f,'g>' is not compatible with type 'SignalR.State.Settings<'a,'b,'c,'d,'e>'
```

Damn it. A really weird error is happening.

```
            configure_signalr {
                endpoint Shared.Constants.endpoint
                send (failwith "")
                invoke (failwith "")
            }
```

Damn it, I need to configure both send and invoke.

4:20pm. Let me watch a few tutorials.

https://github.com/raw-coding-youtube/aspnetcore-signalr/blob/main/3.FeatureOverview/FeatureOverview/Startup.cs

Damn it, I really need this guy's tutorials to remind me of how SignalR should be used.

https://youtu.be/sdsCzyTtp6U?list=PLThyvG1mlMzltDxuQj0uQw1TDu1gJUNeG&t=124

Wait, the hub can see the clients. What about invokes?

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Feature Overview

Let me watch it.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=117

On the client side it is using sends.

https://github.com/raw-coding-youtube/aspnetcore-signalr/search?q=invoke

Ah, he does use invoke in the third video.

I am just really confused as to why I am getting passed that untyped FableHub in invoke.

How does it even make a distinction between invoke and send on the server side?

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=277

Hmmm, it does seem like it has automatic serialization.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1099

The context is just the same as the one being passed into the SignalR library.

4:50pm. https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1241

Enough, I am thinking about it way too much.

///

Now admittedly, maybe if we tried doing this in vanilla SignalR, it would throw a surprise exception in our face, but...
Hmmm...
Actually, that might very well be what would happen.
You know what, we'll actually try it and report back with the results, stay tuned.

///

Let's give it a try.

https://github.com/raw-coding-youtube/aspnetcore-signalr

I'll clone this guy's repo.

6:35pm. Had to take a break. I really am getting bogged down in this project.

Let me clone that thing so I can try out the invokes.

6:45pm. It doesn't throw an exception, it fucking works.

```cs
        // -------------------------------
        // on connected/disconnected hooks
        // -------------------------------
        public override Task OnConnectedAsync()
        {
            return base.OnConnectedAsync();
        }

        public override Task OnDisconnectedAsync(Exception exception)
        {
            return base.OnDisconnectedAsync(exception);
        }
```

We're really missing these kind of hooks as well.

7:15pm. I'll close it here, I had enough for one day.

I am going to ditch this library in favor of my own stuff.

7:25pm. I did well enough for the day. The recording is now 45m long."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[3422129a54...](https://github.com/i574n/The-Spiral-Language/commit/3422129a5429ddb8626e0004f6c07a861b953da4)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"9:30pm. https://news.ycombinator.com/item?id=35853148
The Prime Video microservices to monolith story (adrianco.medium.com)

///

If you have a predictable workload (i.e. we ingest 100,000 videos a month with n size) you should be looking at it from that perspective -- how much compute you are going to need, and when. Serverless works well for predictably unpredictable, infrequent workloads that don't need to have perfect output ("good enough").
The big mistake I see people make is trying to be overly clever and predict the future workload needs. It never works out like that. Design for your current workload now, if your architecture can handle 10x of that great! Each time your scale from 10x workload you will likely need to redesign the system anyway, so you shouldn't pay that tax unless you absolutely have to.

There are a lot of limitations of serverless, the big one I experienced was inability to control the host environment and limitations on the slice of memory/CPU you get, such that you must take that into consideration when designing your atomic work units. Also paying the distributed computing tax is real and occurs at development and runtime -- things like job tracking and monitoring are important when you have 10,000 processes running -- you start to get into the territory of things that basically never happen on a single machine or small cluster, but become problems with thousands of disparate machines / processes.

///

///

>Design for your current workload
Please be my friend.

The bulk of my job these days is sitting in design reviews trying to convince people that just making up scenarios where you need to scale to 100x isn't actually engineering. It's exhausting self-indulgence. Nothing is easier than inventing scenarios where you'll need to "scale". It's borderline impossible to get software folks to just live in the world that exists in front of their eyes.

"Scale" should go back to its original meaning: change relative to some starting point. Slap a trend line on what you know. Do some estimation for what you don't. Design accordingly.

///

Let me link to this thread as it is pretty interesting.

11:25am. https://youtu.be/RZhTC33lStQ?t=89

He did NNs back in 2013.

https://youtu.be/RZhTC33lStQ?t=119
> No way you made this...

https://youtu.be/RZhTC33lStQ?t=211

It is totally a lie that Mojo is a faster Python. If it was possible to make Python faster, partial evaluation systems would have done it.

https://youtu.be/RZhTC33lStQ?t=705
> Every single Python library works in Mojo.

Incidentally, the language is behind a wait list similar to Jai.

5/10/2023

10:15am. What the fuck, why isn't the editor reacting to the changes in the bindings project?

10:20am. I am confused. Why is the editor completely inactive to the changes in the bindings project all of a sudden?

10:30am. There is something wrong with Rider here.

10:35am. Goddamit, this weird IDE bug has wasted so much of my time.

For some reason adding that file leads to it reverting to the cache despite the fact that I've cleaned it.

```
PS E:\Webdev\Fable\CFR-In-Fable> dotnet run
run Run
Building project with version: LocalBuild
Shortened DependencyGraph for Target Run:
<== Run
   <== InstallClient
      <== Clean

The running order is:
Group - 1
  - Clean
Group - 2
  - InstallClient
Group - 3
  - Run
Starting target 'Clean'
E:\Webdev\Fable\CFR-In-Fable\src\Client> "dotnet" fable clean --yes -o output -e .js (In: false, Out: false, Err: false)
Fable: F# to JavaScript compiler 4.0.6
Thanks to the contributor! @Kurren123
Stand with Ukraine! https://standwithukraine.com.ua/

This will recursively delete all *.js[.map] files in E:\Webdev\Fable\CFR-In-Fable\src\Client\output
No files have been deleted. If Fable output is in another directory, pass it as argument.
Finished (Success) 'Clean' in 00:00:00.4153216
Starting target 'InstallClient'
.> "C:\Program Files (x86)\nodejs\npm.CMD" install (In: false, Out: false, Err: false)

up to date, audited 187 packages in 776ms

10 packages are looking for funding
  run `npm fund` for details

3 moderate severity vulnerabilities

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
Finished (Success) 'InstallClient' in 00:00:02.0424796
Starting target 'Run'
E:\Webdev\Fable\CFR-In-Fable\src\Shared> "dotnet" build (In: false, Out: false, Err: false)
MSBuild version 17.5.1+f6fdcf537 for .NET
MSBUILD : error MSB1011: Specify which project or solution file to use because this folder contains more than one project or solution file.
Finished (Failed) 'Run' in 00:00:00.2006070
```

I feel like I am in a bizarro world. Why is dotnet run failing all of a sudden?

...Why did it put a csproj file in Shared?

Let me try invalidating the project cache again.

```
Follow. Rider has to store both ReSharper and IntelliJ settings and cache files. On Windows, the ReSharper host cache files are kept in the%LOCALAPPDATA%\JetBrains\Rider{version}\resharper-host\local\Transient\ReSharperHost\v{version}
```

Let me purge this by hand.

11:15pm. I put it all into the same file.

2:50pm. Done with breakfast and chores.

Let me chill a bit more and then I will resume.

```
    type Auto =
        static member generateBoxedDecoderCached(t: System.Type, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): BoxedDecoder =
            let caseStrategy = defaultArg caseStrategy PascalCase

            let key =
                t.FullName
                |> (+) (Operators.string caseStrategy)
                |> (+) (extra |> Option.map (fun e -> e.Hash) |> Option.defaultValue "")

            Util.CachedDecoders.GetOrAdd(key, fun _ -> autoDecoder (makeExtra extra) caseStrategy false t)

        static member inline generateDecoderCached<'T>(?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Decoder<'T> =
            Auto.generateBoxedDecoderCached(typeof<'T>, ?caseStrategy=caseStrategy, ?extra=extra) |> unboxDecoder

        static member generateBoxedDecoder(t: System.Type, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): BoxedDecoder =
            let caseStrategy = defaultArg caseStrategy PascalCase
            autoDecoder (makeExtra extra) caseStrategy false t

        static member inline generateDecoder<'T>(?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Decoder<'T> =
            Auto.generateBoxedDecoder(typeof<'T>, ?caseStrategy=caseStrategy, ?extra=extra) |> unboxDecoder

        static member inline fromString<'T>(json: string, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Result<'T, string> =
            let decoder = Auto.generateDecoder<'T>(?caseStrategy=caseStrategy, ?extra=extra)
            fromString decoder json

        static member inline unsafeFromString<'T>(json: string, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): 'T =
            let decoder = Auto.generateDecoder<'T>(?caseStrategy=caseStrategy, ?extra=extra)
            match fromString decoder json with
            | Ok x -> x
            | Error msg -> failwith msg
```

Hmmm, is this how it works?

https://stackoverflow.com/questions/34447766/f-static-let-and-static-member

I had no idea that `static let` even existed.

5:15pm.

///

Anyway, Message Pack is quite promising. It actually gives us back the .NET types.
It's just too bad they are the wrong ones.
That tag should have been an int, but we got a back a byte.
Since we don't need union cases with a large number of tags we might as well convert those tags to bytes internally.
But for rest of the numerical types, we'll need sure they are of the right size.
And since this just happened...
Damn, we thought this protocol would at least be good for transfering large homogenous arrays, but since it converted what we thought would be an int to a byte, it might do that for arbitrary elements.
We'll do a few hacks to make it work, stay tuned.

No, we give up for once. We have better things to do than write our own serializers for the next few days.
Let's close it here.
We learned how to do cross module inlining, F# reflection. Before that we learned how to write Fable Bindings.
And we do have one good library we can use to serialize and deserialize F# types.
The message pack protocol here can serve when we need to transfer types that aren't complex, like plain records.

///

I ended up ignoring the above and actually making it work. `Convert.ChangeType` saved me.

5:35pm.

///

We actually have our own functional programming language called Spiral that could do this kind of task very cleanly, at maximum performance.
It was made for creating ML libraries on novel hardware, so it is a lot more efficient than F#.
Doing a Javascript backend for it would not be hard, and in fact it already has an F# one.
But adding another language just for this kind of task to the project would not be ergonomic.

///

I'll cut this out. It is not time for Spiral.

6pm. Right now it is rendering. Enough serialization. Thoth.Json 4 life!

I put so much effort into it, but I'll never need to use anything else.

At this point though, I am really comfortable with .NET reflection.

I definitely understand it now which isn't something I could have said a few months ago.

6:15pm. https://youtu.be/6x5t9pTtCo4
Microservices. Serialization And Deseriation Of F# Types With SignalR (Pt. 4.2)

Let me post this on the F# sub. I am done with programming for the day.

Tomorrow I will bring the leduc project to a close, the day after I'll deploy it and then I will get started working on a store.

6:40pm. https://youtu.be/J7ITgYBn_3k
Scaling Up Prime Video | Prime Reacts

Why do I keep watching this guy?

But he is amusing.

When is lunch?"

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[9fb37ee995...](https://github.com/i574n/The-Spiral-Language/commit/9fb37ee99589559090d05fed710e49ec7d381c03)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"https://mangadex.org/title/bf1d564b-e41a-4f55-9241-b5c7ac7f30ab/despite-coming-from-the-abyss-i-will-save-humanity

It doesn't have a GB tag, but I'll believe that random guy from /a/.

https://mangadex.org/title/ff442aab-7908-40bc-8d10-93c6bb318466/become-a-witch-in-a-world-full-of-ghost-stories

Oh this also has a manhua.

https://mangadex.org/title/164f59bb-dabd-4e42-806c-ab06b0624ced/reincarnated-to-be-the-wicked-maid-at-the-main-lead-s-side

Also this. I looked for this in the past few days, but couldn't find it.

12:25am. https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services
https://www.reddit.com/r/aws/comments/v1izf2/difference_between_fargate_and_app_runner/

I am comparing AWS and Azure services. I didn't know a page like that first one existed.

https://nathanpeck.com/concurrency-compared-lambda-fargate-app-runner/

https://stackoverflow.com/questions/68296480/azure-function-apps-and-web-sockets

https://azure.microsoft.com/en-us/blog/easily-build-realtime-apps-with-websockets-and-azure-web-pubsub-now-in-preview/

12:45am. Trying to fit websockets with Functions is a fool's errand. Forget it.

Let me go to sleep.

Sheesh.

5/2/2023

8:10am. This uncomfortable feeling brings me back. The obsessive circling in my thoughts, the uncertainty, the lack of confidence...

I looked into the mirror and I seem to have black pouches under my eyes.

It is not good to program like this. Let me just chill a bit and then I will get started away.

9:05am. That other loli manga is shitty and isn't even GB, but I'll give it a chance for couple of more chapters.

https://ac.qq.com/ComicView/index/id/653742/cid/3132?fromPrev=1

The urban witch one is pretty interesting, I am looking forward to further translations. Let me finish this chapter, and I will start screencasting.

I need to start making progress. Getting stuck reading tutorials is the worst.

https://www.vladionescu.me/posts/scaling-containers-on-aws-in-2022/
> Friendly warning: the estimated reading time for this blog post is about 45 minutes!

> Massive improvements! If we built and ran an application using EKS on Fargate in 2020, we would have scaled to 3 500 containers in about an hour. Without any effort or changes, in 2021 the scaling would be done in 20 minutes. Without having to invest any effort or change any lines of code, in 2022 the same application would finish scaling in less than 10 minutes! In less than 2 years, without any effort, we went from 1 hour to 10 minutes!

Forget it, I should reading up on Azure. Why am I reading AWS articles as if it has anything to do with my own situation.

https://www.theregister.com/2021/11/03/microsoft_introduces_azure_container_apps/

I can't find a performance blog, but I'll just assume that Azure is good when it comes to spinning up new instances quickly.

> If a Container App scales to zero, what is the latency when a new request comes in and it starts up again? "There's a ton of variables in code start," says Hollan. "Has the image been cached? How big is the image? It's something teams will want to consider in terms of their tolerance. If they want a millisecond response, that's fine, we let you say 'Never scale this down to zero.'"

https://youtu.be/b3dopSTnSRg
How to Build and Deliver Apps Fast and Scalable with Azure Container Apps

Let me watch this and then I will start.

https://youtu.be/b3dopSTnSRg?t=230

Here he talks about Kubernetes.

https://youtu.be/b3dopSTnSRg?t=643

Load test. So that is possible.

https://learn.microsoft.com/hr-hr/azure/container-apps/

https://learn.microsoft.com/hr-hr/azure/container-apps/vnet-custom?tabs=bash&pivots=azure-portal
https://learn.microsoft.com/hr-hr/azure/container-apps/connect-apps?tabs=bash

https://learn.microsoft.com/en-us/gaming/azure/reference-architectures/multiplayer
https://learn.microsoft.com/en-us/gaming/playfab/features/multiplayer/servers/

I'll ignore the playfab. Let me start screencasting.

I need to catch my momentum again.

Just put a few lines down and follow up from there.

12:10pm. I have 8.5m of audio.

I just need to do the canvas and then I'll start programming.

12:55pm. https://youtu.be/ZtTbE4cWhLM?t=1726

Damn, this one is a banger. I didn't think the OST would have it.

2pm. Done with chores.

https://ac.qq.com/ComicView/index/id/650859/cid/801?fromPrev=1

Let me just finish this chapter and I will get started on the Canvas.

https://youtu.be/ZtTbE4cWhLM?t=4191

Donkey Kong's OST is amazing all around. In contrast I didn't think too much of Mario Galaxy.

2:05pm. I am damn tired from all the worrying, but let me get started. Let's see how much I can do today.

3:20pm. https://youtu.be/ZtTbE4cWhLM?t=6980

This OST is great.

```fs
    training_cfr_player_type : CFRPlayerType
    training_run_iterations : string
    training_iterations : int
    training_iterations_left : int
    training_results : (int * (float * float)) list
    training_model : UILeducModel
    testing_run_iterations : string
    testing_iterations_left : int
    testing_results : float list
    testing_model : UILeducModel
```

Let me back this up here.

5:05pm. Uoh, I do not feel like debugging here.

I did a big redesign to push the state into the client and changes a shitload of stuff.

Let me just try running it.

6:10pm. Done for the day. The bug that was there was easily fixed. It is manga and anime time for the rest of the day for me.

My sleep last night wasn't good for some reason even though it wasn't shallow.

Maybe due to all the uncertainty plaguing me. But I feel like I finally have a handle on what I need to do. I'll do these containerized apps, maybe even try out the function apps and then move on.

To payments.

I'll make an art gallery. For this I'll use function apps and make it fully serverless. It will be cool.

6:20pm. Like that I will cultivate my cloud and web app skills. Eventually I'll have something that is really valuable: both on the job market, and my own project portfolio.

There is no need to make a fuss about making money. I just need to sit down and work at it.

I was obsessed with making that poker agent, but the way to get money is to travel the path to it."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[7c6d8e2372...](https://github.com/i574n/The-Spiral-Language/commit/7c6d8e23728706b5f048a47742b0fae910c5c677)
#### Sunday 2023-06-18 17:56:43 by Marko Grdinić

"8:40am. Almost done chilling. Let me just finish Hagure Idol and then I will resume where I was yesterday.

9am. Let me start. I'll leave leasure for later? Any mail?

I opened some issues yesterday.

Nope, nevermind that. I'll just cover the bugs and be done with it.

10:25am. https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90
https://news.ycombinator.com/item?id=35811741

I'll read this later.

https://creativecow.net/forums/thread/weird-timeline-playback-audio-fade-in-issue/

Damn it, now DR bugs are wasting my time.

While I was going through the video I noticed that I accidentally had a clip frame frozen when I fixed it, the audio started fading weirdly.

This happened to me once previously, and I had trouble dealing with it.

11:55am. Damn it, why is the audio getting quiet in places.

...Oh, I am checking it out in the fairlight page, and there are these weird crossfades that span the entire clip!

WTF?

Cutting and reinserting on the fairlight page seems to get rid of that.

Ok, at least now I have a better way of fixing it than before.

///

No, it doesn't seem like we have much in the way of choices.
There is something here about notifying the client when the connection is closed, but we can't see a way to get the level of control that we desire.
We'll have to go with the more flexible appproach and check out those Fable SignalR packages.

///

12:50pm. https://shmew.github.io/Fable.SignalR/#/signalr-client/connecting

Let me stop here. This library was an excellent find!

I am looking forward to trying it out.

https://github.com/Shmew/Fable.SignalR/issues/

Opened issue 41 here.

https://github.com/Shmew/Fable.SignalR/search?q=Fable.FastCheck

```
---------------------------------------------------------------------
Build Time Report
---------------------------------------------------------------------
Target         Duration
------         --------
CleanDocs      00:00:00.0301179
ConfigDebug    00:00:00.0001886
Clean          00:00:00.0794757
CopyDocFiles   00:00:00.0017037
Restore        00:00:54.4596244   (Unsupported log file format. Latest supported version is 14, the log file has version 15.)
PackageJson    00:00:00           (skipped)
YarnInstall    00:00:00           (skipped)
Lint           00:00:00           (skipped)
Build          00:00:00           (skipped)
RebuildSass    00:00:00           (skipped)
RunTests       00:00:00           (skipped)
All            00:00:00           (skipped)
PrepDocs       00:00:00           (skipped)
Start          00:00:00           (skipped)
Dev            00:00:00           (skipped)
Total:         00:00:54.6751661
Status:        Failure
```

Predicatably the project doesn't build.

4:55pm. I've yet to get a `build.fsx` file to build successfully even a single time in my life.

5:15pm. https://www.reddit.com/r/fsharp/comments/137pm7u/what_should_be_done_with_abandonware_libraries/

Ok, what I will do is try a step by step rebuild.

```
<?xml version="1.0" encoding="utf-8"?>
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Library</OutputType>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="Shared.fs" />
    <Compile Include="Types.fs" />
    <Compile Include="HttpClient.fs" />
    <Compile Include="HubConnection.fs" />
    <Compile Include="Protocols.fs" />
    <Compile Include="SignalR.fs" />
    <None Include="paket.references" />
    <None Include="paket.template" />
  </ItemGroup>
  <PropertyGroup>
    <NpmDependencies>
      <NpmPackage Name="@microsoft/signalr" Version="gte 3.1.5 lt 6" ResolutionStrategy="max" />
    </NpmDependencies>
  </PropertyGroup>
  <Import Project="..\..\.paket\Paket.Restore.targets" />
</Project>
```

Oh, I didn't know that npm packages could be included in the .fsproj file.

Let's just do it.

I'll go ever the projects one by one, adding the files into them.

6:20pm. https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hubendpointconventionbuilder?view=aspnetcore-8.0

I am so confused. Why is this class not where it should be?

https://www.nuget.org/packages?q=signalr

What the dick. The regular SignalR is really old!

```
Microsoft.AspNetCore.App.Ref v7.0.5
```

Wait, here it says the exact package. I forgot to paste in the framework reference, damn.

6:55pm. I'll stop here for the day.

https://www.semianalysis.com/p/google-we-have-no-moat-and-neither

This blog always has interesting stuff on it.

At the rate I am going I should be able to finish the rebuild of the SignalR library tomorrow."

---
## [Libroru/water-tracker-swift](https://github.com/Libroru/water-tracker-swift)@[3ecf8198c4...](https://github.com/Libroru/water-tracker-swift/commit/3ecf8198c46d1539d377dda5b4f34f499fbd0f61)
#### Sunday 2023-06-18 18:20:06 by Libroru

Fixed float point exception & Added a reset button

TO DO: Find out how to save Dates without some fucking exception you stupid fucking bitch

---
## [SleepingLife/Turbo](https://github.com/SleepingLife/Turbo)@[b14f4fa5c3...](https://github.com/SleepingLife/Turbo/commit/b14f4fa5c3a931cd678538a9f64912e3c417c055)
#### Sunday 2023-06-18 18:24:34 by SleepingLife

Civs

Civ changes
Arabia market +gold
Ayyubids knight is cheaper to construct and ayyubids gains 50% faith on kill
Boers farms buffed to also have a culture
Bolivia buffed to 2 yield
Brazil buffed with vietnam, tourism and great people generation removed.
Bulgaria granary gives +1 science
Canada lakes have +1 food and prod
Celts forest +faith
China library +science
Colombia granary +1 prod/food
Finland +faith from unimproved forest
France chateau +prod
Franks mead hall +culture
Gaul wall +prod
Greece friendship modifier was given to all Civs
Hittites start with all 1st level techs
India double the values and gets aztec watermill
Iroquois +culture from unimproved forest
Khmer 4 movement elephant
Lithuania has free prophet at pottery and the tibet improvement
Manchuria stables +gold
Maya long count is now at philo
Netherlands no longer coastal
Nubia start with 3 apedemak bow
Ottomans gain 100% faith from kills
Palmyra UB are cheaper, amphi gives +prod from lakes
Polynesia +embark movement
Rome 33% cap bonus
Siam 100% cs bonus
Sumeria temple give 15% science
Sweden Falu +6 food
Switzerland active merchant slot city +2 food
Turkey +100% prod to culture building
UAE cheaper UB
Ukraine market gives 50 gold for great person
Wales ua affects cattle
Zulu spawns with UU Shaka, capital is weaker

---
## [rkruk/awesome-console-services](https://github.com/rkruk/awesome-console-services)@[4b8f298fb2...](https://github.com/rkruk/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Sunday 2023-06-18 19:53:47 by techie2000

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
## [SimonN/LixD](https://github.com/SimonN/LixD)@[20bf5ba7eb...](https://github.com/SimonN/LixD/commit/20bf5ba7eba5c9db71f9c4e45faedfcfeda80be0)
#### Sunday 2023-06-18 20:03:03 by Simon Naarmann

Remove steel tile matt/8x8

This tile had no nub, had no crossed metal bars, and looked like geoo's
concrete blocks which are earth. Remove it with no replacement. We'll
look separately at all levels that used it.

Won't Get Fooled Again: Replace important steel with a nice looking tile
group to make a steel staircase.

All Aboard the Pain Train: Remove decorative 8x8 steel entirely.

Sympathy for the Lix: Delete the levels. This relied on players making
unforced mistakes to help opponents above. Players frequently got
annoyed and killed their crowds as there was little to do otherwise.

Race to the Depths: Delete the levels. They were single-lix races where
players can die easily and then will have to watch the others. Rarely,
players won these levels.

---
## [python/mypy](https://github.com/python/mypy)@[0873230ee6...](https://github.com/python/mypy/commit/0873230ee60461110bd7bfde7ca3886878aae389)
#### Sunday 2023-06-18 22:19:31 by Ivan Levkivskyi

Foundations for non-linear solver and polymorphic application (#15287)

Fixes #1317
Fixes #5738
Fixes #12919 
(also fixes a `FIX` comment that is more than 10 years old according to
git blame)

Note: although this PR fixes most typical use-cases for type inference
against generic functions, it is intentionally incomplete, and it is
made in a way to limit implications to small scope.

This PR has essentially three components (better infer, better solve,
better apply - all three are needed for this MVP to work):
* A "tiny" change to `constraints.py`: if the actual function is
generic, we unify it with template before inferring constraints. This
prevents leaking generic type variables of actual in the solutions
(which makes no sense), but also introduces new kind of constraints `T
<: F[S]`, where type variables we solve for appear in target type. These
are much harder to solve, but also it is a great opportunity to play
with them to prepare for single bin inference (if we will switch to it
in some form later). Note unifying is not the best solution, but a good
first approximation (see below on what is the best solution).
* New more sophisticated constraint solver in `solve.py`. The full
algorithm is outlined in the docstring for `solve_non_linear()`. It
looks like it should be able to solve arbitrary constraints that don't
(indirectly) contain "F-bounded" things like `T <: list[T]`. Very short
the idea is to compute transitive closure, then organize constraints by
topologically sorted SCCs.
* Polymorphic type argument application in `checkexpr.py`. In cases
where solver identifies there are free variables (e.g. we have just one
constraint `S <: list[T]`, so `T` is free, and solution for `S` is
`list[T]`) it will apply the solutions while creating new generic
functions. For example, if we have a function `def [S, T] (fn:
Callable[[S], T]) -> Callable[[S], T]` applied to a function `def [U]
(x: U) -> U`, this will result in `def [T] (T) -> T` as the return.

I want to put here some thoughts on the last ingredient, since it may be
mysterious, but now it seems to me it is actually a very well defined
procedure. The key point here is thinking about generic functions as
about infinite intersections or infinite overloads. Now reducing these
infinite overloads/intersections to finite ones it is easy to understand
what is actually going on. For example, imagine we live in a world with
just two types `int` and `str`. Now we have two functions:
```python
T = TypeVar("T")
S = TypeVar("S")
U = TypeVar("U")

def dec(fn: Callable[[T], S]) -> Callable[[T], S]: ...
def id(x: U) -> U: ...
```
the first one can be seen as overload over
```
((int) -> int) -> ((int) -> int)  # 1
((int) -> str) -> ((int) -> str)  # 2
((str) -> int) -> ((str) -> int)  # 3
((str) -> str) -> ((str) -> str)  # 4
```
and second as an overload over
```
(int) -> int
(str) -> str
```
Now what happens when I apply `dec(id)`? We need to choose an overload
that matches the argument (this is what we call type inference), but
here is a trick, in this case two overloads of `dec` match the argument
type. So (and btw I think we are missing this for real overloads) we
construct a new overload that returns intersection of matching overloads
`# 1` and `# 4`. So if we generalize this intuition to the general case,
the inference is selection of an (infinite) parametrized subset among
the bigger parameterized set of intersecting types. The only question is
whether resulting infinite intersection is representable in our type
system. For example `forall T. dict[T, T]` can make sense but is not
representable, while `forall T. (T) -> T` is a well defined type. And
finally, there is a very easy way to find whether a type is
representable or not, we are already doing this during semantic
analyzis. I use the same logic (that I used to view as ad-hoc because of
lack of good syntax for callables) to bind type variables in the
inferred type.

OK, so here is the list of missing features, and some comments on them:
1. Instead of unifying the actual with template we should include
actual's variables in variable set we solve for, as explained in
https://github.com/python/mypy/issues/5738#issuecomment-511242682. Note
however, this will work only together with the next item
2. We need to (iteratively) infer secondary constraints after linear
propagation, e.g. `Sequence[T] <: S <: Sequence[U] => T <: U`
3. Support `ParamSpec` (and probably `TypeVarTuple`). Current support
for applying callables with `ParamSpec` to generics is hacky, and kind
of dead-end. Although `(Callable[P, T]) -> Callable[P, List[T]]` works
when applied to `id`, even a slight variation like `(Callable[P,
List[T]]) -> Callable[P, T]` fails. I think it needs to be re-worked in
the framework I propose (the tests I added are just to be sure I don't
break existing code)
4. Support actual types that are generic in type variables with upper
bounds or values (likely we just need to be careful when propagating
constraints and choosing free variable within an SCC).
5. Add backtracking for upper/lower bound choice. In general, in the
current "Hanoi Tower" inference scheme it is very hard to backtrack, but
in in this specific choice in the new solver, it should be totally
possible to switch from lower to upper bound on a previous step, if we
found no solution (or `<nothing>`/`object`).
6. After we polish it, we can use the new solver in more situations,
e.g. for return type context, and for unification during callable
subtyping.
7. Long term we may want to allow instances to bind type variables, at
least for things like `LRUCache[[x: T], T]`. Btw note that I apply force
expansion to type aliases and callback protocols. Since I can't
transform e.g. `A = Callable[[T], T]` into a generic callable without
getting proper type.
8. We need to figure out a solution for scenarios where non-linear
targets with free variables and constant targets mix without secondary
constraints, like `T <: List[int], T <: List[S]`.

I am planning to address at least majority of the above items, but I
think we should move slowly, since in my experience type inference is
really fragile topic with hard to predict long reaching consequences.
Please play with this PR if you want to and have time, and please
suggest tests to add.

---
## [UwUBlackberry/Ophelimos](https://github.com/UwUBlackberry/Ophelimos)@[6f1c9f213a...](https://github.com/UwUBlackberry/Ophelimos/commit/6f1c9f213a42a49c6da13c194e494c42aa06ff71)
#### Sunday 2023-06-18 22:59:57 by Noble Oraiste

O U T R A G E D ?  I know.

This was a blur but I added a bunch of shit, including Unb's goldblood naming thing suggestion, reworded some stuff, added some stuff, I think. OOO Portal magic is cool as fuck so I added that.

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[18819cc7fb...](https://github.com/Zevotech/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Sunday 2023-06-18 23:59:05 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---

