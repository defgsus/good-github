## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-03](docs/good-messages/2023/2023-03-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,155,369 were push events containing 3,283,990 commit messages that amount to 256,330,391 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[10a344bde0...](https://github.com/Ebin-Halcyon/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Friday 2023-03-03 00:15:11 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored. 
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [fulpstation/fulpstation](https://github.com/fulpstation/fulpstation)@[fc5620aa13...](https://github.com/fulpstation/fulpstation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Friday 2023-03-03 01:01:28 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[34daca112c...](https://github.com/CapCamIII/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Friday 2023-03-03 01:04:17 by Segrain

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
## [ZenFone8/android_kernel_asus_sm8350](https://github.com/ZenFone8/android_kernel_asus_sm8350)@[00791e017b...](https://github.com/ZenFone8/android_kernel_asus_sm8350/commit/00791e017b5f2555aa9cd5d7d3a02ce19cd86701)
#### Friday 2023-03-03 01:27:36 by Masahiro Yamada

kbuild: remove the target in signal traps when interrupted

[ Upstream commit a7f3257da8a86b96fb9bf1bba40ae0bbd7f1885a ]

When receiving some signal, GNU Make automatically deletes the target if
it has already been changed by the interrupted recipe.

If the target is possibly incomplete due to interruption, it must be
deleted so that it will be remade from scratch on the next run of make.
Otherwise, the target would remain corrupted permanently because its
timestamp had already been updated.

Thanks to this behavior of Make, you can stop the build any time by
pressing Ctrl-C, and just run 'make' to resume it.

Kbuild also relies on this feature, but it is equivalently important
for any build systems that make decisions based on timestamps (if you
want to support Ctrl-C reliably).

However, this does not always work as claimed; Make immediately dies
with Ctrl-C if its stderr goes into a pipe.

  [Test Makefile]

    foo:
            echo hello > $@
            sleep 3
            echo world >> $@

  [Test Result]

    $ make                         # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^Cmake: *** Deleting file 'foo'
    make: *** [Makefile:3: foo] Interrupt

    $ make 2>&1 | cat              # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^C$                            # 'foo' is often left-over

The reason is because SIGINT is sent to the entire process group.
In this example, SIGINT kills 'cat', and 'make' writes the message to
the closed pipe, then dies with SIGPIPE before cleaning the target.

A typical bad scenario (as reported by [1], [2]) is to save build log
by using the 'tee' command:

    $ make 2>&1 | tee log

This can be problematic for any build systems based on Make, so I hope
it will be fixed in GNU Make. The maintainer of GNU Make stated this is
a long-standing issue and difficult to fix [3]. It has not been fixed
yet as of writing.

So, we cannot rely on Make cleaning the target. We can do it by
ourselves, in signal traps.

As far as I understand, Make takes care of SIGHUP, SIGINT, SIGQUIT, and
SITERM for the target removal. I added the traps for them, and also for
SIGPIPE just in case cmd_* rule prints something to stdout or stderr
(but I did not observe an actual case where SIGPIPE was triggered).

[Note 1]

The trap handler might be worth explaining.

    rm -f $@; trap - $(sig); kill -s $(sig) $$

This lets the shell kill itself by the signal it caught, so the parent
process can tell the child has exited on the signal. Generally, this is
a proper manner for handling signals, in case the calling program (like
Bash) may monitor WIFSIGNALED() and WTERMSIG() for WCE although this may
not be a big deal here because GNU Make handles SIGHUP, SIGINT, SIGQUIT
in WUE and SIGTERM in IUE.

  IUE - Immediate Unconditional Exit
  WUE - Wait and Unconditional Exit
  WCE - Wait and Cooperative Exit

For details, see "Proper handling of SIGINT/SIGQUIT" [4].

[Note 2]

Reverting 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd
files") would directly address [1], but it only saves if_changed_dep.
As reported in [2], all commands that use redirection can potentially
leave an empty (i.e. broken) target.

[Note 3]

Another (even safer) approach might be to always write to a temporary
file, and rename it to $@ at the end of the recipe.

   <command>  > $(tmp-target)
   mv $(tmp-target) $@

It would require a lot of Makefile changes, and result in ugly code,
so I did not take it.

[Note 4]

A little more thoughts about a pattern rule with multiple targets (or
a grouped target).

    %.x %.y: %.z
            <recipe>

When interrupted, GNU Make deletes both %.x and %.y, while this solution
only deletes $@. Probably, this is not a big deal. The next run of make
will execute the rule again to create $@ along with the other files.

[1]: https://lore.kernel.org/all/YLeot94yAaM4xbMY@gmail.com/
[2]: https://lore.kernel.org/all/20220510221333.2770571-1-robh@kernel.org/
[3]: https://lists.gnu.org/archive/html/help-make/2021-06/msg00001.html
[4]: https://www.cons.org/cracauer/sigint.html

Fixes: 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd files")
Reported-by: Ingo Molnar <mingo@kernel.org>
Reported-by: Rob Herring <robh@kernel.org>
Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
Tested-by: Ingo Molnar <mingo@kernel.org>
Reviewed-by: Nicolas Schier <nicolas@fjasle.eu>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [saltyfishie98/godot](https://github.com/saltyfishie98/godot)@[92bee43adb...](https://github.com/saltyfishie98/godot/commit/92bee43adba8d2401ef40e2480e53087bcb1eaf1)
#### Friday 2023-03-03 01:30:10 by Rémi Verschelde

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
## [huhai463127310/MegaMocapVR](https://github.com/huhai463127310/MegaMocapVR)@[db1481129a...](https://github.com/huhai463127310/MegaMocapVR/commit/db1481129a211d646ef05bc71636a10d4b89ed52)
#### Friday 2023-03-03 01:42:41 by Megasteakman

UE5.1.1 - Calibration Mode Overlay

Added a nice new UI overlay to let you know that you are in Calibration Mode after hearing some people get confused about what happens when you first start the system.  If you don't like it, disconnect it in the function for VRPlayerMode_CalibrationMode.

Did a lot of work on the UE5 Manny control rig.  It could be better.  It could be worse.  I find it really hard to tell sometimes, so I did leave the old one in MegaMocapVR\ControlRigs\WIP_ControlRigs\OLD_MMVR_UE5Manny_ControlRig

The UE5 Manny control rig now has a way to lock the arm goals to the chest control, so you can use it for animation/cleanup a bit easier.  This variable is exposed to cinematics, which is a sick feature I want to make more use out of.

I reduced the tick on the editor utility widget.

Revamped the teleprompter, creating a new Teleprompter Screen actor that gets spawned in if you use the new event on the player pawn 'Event_TeleprompterUpdate.

Did some small changes to the metahuman control rig, but... I don't remember what they were.  Again, who knows if its better.  I think I made an 'is valid' check on the iphone name so it wouldn't throw you errors if no iphone was added to the player pawn.

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[d21740b475...](https://github.com/goober3/hi-github-portside/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Friday 2023-03-03 02:30:09 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[18dba7ecae...](https://github.com/git-for-windows/git/commit/18dba7ecae49a4c04d968333d9f74a15a3feaa92)
#### Friday 2023-03-03 03:16:43 by Johannes Schindelin

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bea0b67c5c...](https://github.com/treckstar/yolo-octo-hipster/commit/bea0b67c5cad577ec54fdf2f5aec148f16f64a52)
#### Friday 2023-03-03 03:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [matt-owen-256/seedsigner](https://github.com/matt-owen-256/seedsigner)@[d2a657f2d4...](https://github.com/matt-owen-256/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Friday 2023-03-03 03:58:15 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[f3168dbdfa...](https://github.com/Enbyy/orbstation/commit/f3168dbdfa14e8feaea6df61cd279330ade44b41)
#### Friday 2023-03-03 04:21:33 by Cee

i fixed the damn wires fuck this shit i'm going to go get a fucking milkshake

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[fc1e2e5e26...](https://github.com/carlarctg/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Friday 2023-03-03 04:55:27 by riot

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
## [dylanfeehan/dategen](https://github.com/dylanfeehan/dategen)@[952055f669...](https://github.com/dylanfeehan/dategen/commit/952055f66970c2f7aa34c68d203c4adb99f0c4f2)
#### Friday 2023-03-03 05:23:35 by Dylan Feehan

that was a long and painful debugging session

that was a huge pain in the ass. essentially, the proxy_pass for / was
working fine. but it'd make requests for static because that's where the
js and css files were, but then nginx would pick that up lol. and so
nginx was like ok yeah you want static i'll give you static, but
i didn't really any logic as to why the static directive was there, it
just kinda was, probably from the previous config. so it would pick that
up and there was a root directive inside it that was some path to the
htdocs on the apache server but that obvisouly wasn't helping

what would have worked was if i had the /static proxy pass to the apache
static, but obviously taht'd be silly because it's already on the
browser and theres no need to re-request static. but that's the only way
it'd work with a static directive, unless there's a way to
self-reference or say "never mind, do what you'd usually do".

---
## [SteelRidgeRobotics/2022-23_FRC_Season](https://github.com/SteelRidgeRobotics/2022-23_FRC_Season)@[a4bc79a7c0...](https://github.com/SteelRidgeRobotics/2022-23_FRC_Season/commit/a4bc79a7c0901fad3df9978c006a8276cb589711)
#### Friday 2023-03-03 05:52:35 by CringeCodin

CODE CODE CODE CODE CODE II: ATTACK OF THE CLONES

Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there. Damn you Stormcloaks. Skyrim was fine until you came along. Empire was nice and lazy. If they hadn't been looking for you, I could've stolen that horse and be halfway to Hammerfell. You there. You and me - we shouldn't be here. It's these Stormcloaks the Empire wants. We're all brothers and sisters in binds now, thief. Shut up back there! And what's wrong with him, huh? Watch your tongue. You're speaking to Ulfric Stormcloak, the true High King. Ulfric? The Jarl of Windhelm? You're the leader of the rebellion. But if they've captured you... Oh gods, where are they taking us? I don't know where we're going, but Sovngarde awaits. No, this can't be happening. This isn't happening. Hey, what village are you from, horse thief? Why do you care? A Nord's last thoughts should be of home. Rorikstead. I'm... I'm from Rorikstead.

...looks like the Thalmor are with him.

General Tullius, sir. The headsman is waiting. Good. Let's get this over with! Shor, Mara, Dibella, Kynareth, Akatosh. Divines, please help me. Look at him. General Tullius the Military Governor. And it looks like the Thalmor are with him. Damn elves. I bet they had something to do with this.

Why are we stopping? Why do you think? End of the line. Let's go. Shouldn't keep the gods waiting for us.

Began work on commands to pose the arm, pick up game pieces, set the grabber's position

Also changed some more or less semantical things

---
## [hrzntal/fledermaus](https://github.com/hrzntal/fledermaus)@[f5e63175ec...](https://github.com/hrzntal/fledermaus/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Friday 2023-03-03 06:33:27 by SkyratBot

[MIRROR] Fixes all antag datum moodlets being removed when any single antag datum is removed [MDB IGNORE] (#19237)

* Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line:
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy.

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

* Fixes all antag datum moodlets being removed when any single antag datum is removed

* fix

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [jontheapple/dark-souls-cheat-sheet](https://github.com/jontheapple/dark-souls-cheat-sheet)@[a00400123d...](https://github.com/jontheapple/dark-souls-cheat-sheet/commit/a00400123dcebadf4a16583f18f5dc63adf0d9a5)
#### Friday 2023-03-03 08:06:33 by Stephen McNabb

Merge pull request #16 from jontheapple/gh-pages

Added Divine Blessing in Painting Guardian room
Clarified green titanite shards in Lost Izalith (There is one after the Demon Firesage, and also one after the Giant Centipede)
Added Marvelous Chester invasion in Oolacile

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[ebc56df49f...](https://github.com/Offroaders123/Smart-Text-Editor/commit/ebc56df49f9c66379476e847d53bac8aa5024add)
#### Friday 2023-03-03 08:38:13 by Offroaders123

App Module Fancifying!

Started modernizing the main App module, making it structured more with how I tend to do things nowadays. Using more `for (of)` loops, and async-await wherever possible. I also like using variables to help document the state flow, so you can see the individual parts of how it works a bit better. I didn't like doing that when I first started this project, and now I really like that it helps with explaining how things work, without actually explaining how things work. Previously, I just wasn't doing either XD

This did appear to break drag and drop support, and I wasn't able to figure it out before finishing this commit. My computer is running low on battery and it's already really late, so I just want to commit everything for the night. I'm gonna rework things to actually run better next anyways, too. So, I'm gonna be back looking at everything to find what happened, again tomorrow.

I'm so happy with how this is going, it's really great. There's no way I could reasonably reworked everything from the ground up alongside the original codebase, instead of incrementing it to being modern again, which is what I ended up doing here. That would have ridiculously not worked, or taken a very long time. It would have also been a headache to figure everything out all again. I'm still finding things out about how the app works again, and I've already done all of this work to it with these reworks. It's now much stronger now too, or at least it definitely will be. It's going to be able to expect a lot more edge cases, thanks to "typing" things out with more explicit values, like with `null`, `undefined`, things like that. Then you *really* know what kinds of data you're working with, and what you don't currently have just quite yet (I guess that's referencing things like Promises, hehe. Asynchrony [Asynchrony X, that's a funny song/album name reference :) ]).

---
## [rageguy505/ragestation](https://github.com/rageguy505/ragestation)@[2b76197397...](https://github.com/rageguy505/ragestation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Friday 2023-03-03 09:02:45 by Jacquerel

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[32c31b8fc0...](https://github.com/Stalkeros2/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Friday 2023-03-03 10:45:41 by SkyratBot

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[9e981753ca...](https://github.com/Stalkeros2/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Friday 2023-03-03 10:45:41 by SkyratBot

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[26688597e3...](https://github.com/Stalkeros2/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Friday 2023-03-03 10:45:41 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [joefreeman8/UF-shoes-fe](https://github.com/joefreeman8/UF-shoes-fe)@[0830e1efb2...](https://github.com/joefreeman8/UF-shoes-fe/commit/0830e1efb2d22a7496dc4ea617f9e305a68e3af8)
#### Friday 2023-03-03 11:05:51 by Joe Freeman

fixed my hacky solution to delete item from basket today, note to self: E.TARGET.VALUE (facepalm).

---
## [786aafreen/Jenny](https://github.com/786aafreen/Jenny)@[737e6e3a2a...](https://github.com/786aafreen/Jenny/commit/737e6e3a2afb1adc858606d452082b351f045dab)
#### Friday 2023-03-03 11:06:17 by Aafreen Khan

Add files via upload

Well Muggles here we are going to live the Harry Potter life...... An Invisible Cloak where we can see the Science Fiction and Magical World around us in reality for damn sure....So be ready Woahhh...

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[4c5f51377e...](https://github.com/argilla-io/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Friday 2023-03-03 11:23:58 by Tom Aarsen

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
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[7cc6934eff...](https://github.com/Profakos/orbstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Friday 2023-03-03 11:42:18 by LemonInTheDark

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e6565584d3...](https://github.com/mrakgr/The-Spiral-Language/commit/e6565584d3685de528ba6d95718495aeb8f73de2)
#### Friday 2023-03-03 12:08:02 by Marko Grdinić

"///

IC: Have you ever thought about selling PCIe cards with your chip at retail, like a GPU, just an accelerator that people can buy off the shelf? Because I've had a lot of requests for that.

JK: Yeah, we're going to do that. About a year and a half ago we started to rev up - we ordered thousands of cards. We had a reasonable number of models running, and we thought we were going to start to sell, you know, small volumes to people who wanted to take them, experiment with them. Then basically due to the supply chain, the cards didn't show up so we had nothing to sell.

///

8pm. I am pretty tired right now.

https://rinzewind.org/blog-en/2023/the-tech-downturn-seen-through-hacker-news-comments.html

This is all bad news for me.

8:20pm. > “I know, right? Lady Komari is so cute and funny.

Let me read the Komari novel. I'll leave anime for later.

> You can trust this intel; we got it from our ninjas.

This is a great line, I'll keep in stock.

https://interviewing.io/guides/system-design-interview
https://news.ycombinator.com/item?id=34999464
A Senior Engineer's Guide to the System Design Interview (interviewing.io)

I'll leave this for later.

3/3/2023

8:20am. I had trouble going to sleep tonight. Yeah, I am a bit pissed about not getting callbacks, but that is merely a consequence of the way I've approach the problem and structured my resume. During the night I've been thinking about chatGPT. The humans won't help me in my quest, but an AI assistant like it could provide great value in my job search. What the hell do I know what a top rated resume should look like?

An AI assistant trained on the entire Internet would definitely be better at it than me. The next time I apply I am going to go back to the mentality of a couple of months ago, but not to the point of complete bullshittery like with the resume I had last time.

I am going to aim for the senior positions directly.

But first I actually need the skills to do webdev properly.

I'll put in some real with my portfolio projects, Spiral and web page, and a ton of bullshit otherwise. You bet I am going to have 5 years of pro experience working at some company when I apply next time.

Forget about getting a job. Think getting offers during the next round.

8:25am. I've slept like shit tonight, but I am full of determination.

No mail as expected. I'll turn off Thunderbird.

On AngelList I got a reply that they are creating a profile and will send me a reply if I am a close match. What are the chances of that? Zero.

What was the point of accepting if they are going to pivot and tell me they are looking for a match. They are just stringing me along.

The next time I do this, I'll take these companies to the cleaners.

8:30am. Now let me read Mental Out.

I am not that far from getting a job. I need a few months to completely master the domain, but after that I'll drop programming and start the interviewing practice. Anything goes!

9:40am. Done with the bath. Let me finally watch that video from two days ago by Onur Gumus. I wish I could at least get good night's sleep. Imagine if the job turns out to be really stressful, well, I can always just quit it.

https://youtu.be/2pnj19qWLdQ
Fable.Remoting and Elmish.Bridge

Let me start this. Once I have the knowledge of how this works, I'll be able to move on to the server part of my portfolio project.

https://youtu.be/2pnj19qWLdQ?t=95

I'll really have to play with sending http requests directly at some point, just to see what they are made of.

https://youtu.be/2pnj19qWLdQ?t=100

I should look up a tutorial on this later. There a Chrome dev tools tutorial amongst the crash courses.

https://youtu.be/2pnj19qWLdQ?t=164

Oh Fable Remoting has binary serialization.

https://youtu.be/2pnj19qWLdQ?t=305

Huh, I had no idea Union type cases could be made private.

https://youtu.be/2pnj19qWLdQ?t=329

This is an interesting way of doing it. He says that pattern matching won't work once the case is made private, and introduces an active pattern to get around that.

https://learn.microsoft.com/en-us/dotnet/api/system.text.json?view=net-7.0

.NET 7 has a native JSON serializer.

https://www.youtube.com/results?search_query=.net+text+json

I'll check them out later.

https://youtu.be/2pnj19qWLdQ?t=569

Vite prefers a different number? I do not understand this, but fine. I'll play around with his stuff.

https://youtu.be/2pnj19qWLdQ?t=605
> I prefer Giraffe over Saturn. I never understood why Saturn exists in the first place.

He is configuring it to use websockets.

https://youtu.be/2pnj19qWLdQ?t=679
> Cors is not a restriction, it is actually a relaxation.

https://youtu.be/2pnj19qWLdQ?t=788

Here he is praising regular ASP.NET's template generation, and says that you don't have to restrict yourself to Giraffe either.

https://youtu.be/2pnj19qWLdQ?t=940

Actually, it is weird that the handler is being passed in like this.

https://youtu.be/2pnj19qWLdQ?t=1059

It is configured differently to how I did it.

https://youtu.be/2pnj19qWLdQ?t=1521

I really need to get familiar with raw HTTP requests. My skills as a web dev are too lacking.

https://youtu.be/2pnj19qWLdQ?t=1536

Focus me, stop browsing HN on the side. Here he is showing how I could make a RESTful interface using Fable Remoting. That is really good.

https://youtu.be/2pnj19qWLdQ?t=1574

Oh wait, did he just put in a breakpoint in the Chrome browser?

https://youtu.be/2pnj19qWLdQ?t=1783

I could use it from a C# application. Let me take a short break.

11am. Let me resume.

https://youtu.be/2pnj19qWLdQ?t=1931

Hmmm, he isn't using the Fake run script.

https://youtu.be/2pnj19qWLdQ?t=1994

This scared me!

It seems it is possible to just right click and remove all the breakpoints.

https://youtu.be/2pnj19qWLdQ?t=2197

He is using this to draw diagrams.

https://youtu.be/2pnj19qWLdQ?t=2217
> If you refresh now, the server will detect you're disconnected. And you can take an explicit dispose action.

I am really curious as to how I could configure the server so it acts upon multiple users concurrenctly. How would I implement something like an online poker room too?

https://youtu.be/2pnj19qWLdQ?t=2259

Let me try out this site he is using. CSP is not well suited for diagrams.

https://excalidraw.com/

Oh, it is pretty cool. It is way better than CSP for this simple purpose.

I love it.

I'll keep it in mind next time I try to do a diagram.

https://youtu.be/2pnj19qWLdQ?t=2284

Oh the arrows can get attached to the original function. I see.

https://youtu.be/2pnj19qWLdQ?t=2352

I am not sure I understand. Are the model and update functions mirrored for some reason?

https://youtu.be/2pnj19qWLdQ?t=2479
> It is very confusing. I did not understand how to use it efficiently.

He is talking about the Elmish Bridge communication.

https://youtu.be/2pnj19qWLdQ?t=2508

It has broadcasting?

https://github.com/Nhowka/Elmish.Bridge#reply-channels-since-500

Wait, it seems v1 wasn't the latest. I see it has v5 here. Let me check the Nuget package.

https://www.nuget.org/packages/Elmish.Bridge.Server

Ih the latest is v7.

https://youtu.be/2pnj19qWLdQ?t=2947

To be honest, I do not like the Fable.Lit much compared to Feliz. But that isn't a problem.

https://youtu.be/2pnj19qWLdQ?t=3075
> Notice that I've wrapped it in `Cmd.ofEffect`.

https://youtu.be/2pnj19qWLdQ?t=3307

You know, these subjects are really good for me. This something I should focused on in 2020, yet I botched my learning path and wasted 6 months. Now I paying for it.

Once I learn these subjects, I'll be able to rewrite the Spiral language server so it is more concise and stable compared to what I have now.

11:50am. In addition to watching this, I will do a proper deep dive of ASP.NET, Elmish.Bridge and Fable.Remoting.

I spent the last ten days studying the frontend tech and databases. I have that on hand now.

The next step is to master the backend aspects of web development for good. Even if it takes me a whole month, it would be worth it. This kind of knowledge and experience won't go out of date ever.

https://youtu.be/2pnj19qWLdQ?t=4064

He really should have just wrapped the use of clientDispatch in an async.

12:15pm. That was informative.

Yesterday while looking at LinkedIn ads, I saw a new MS tech called Orleans, which I am guessing is like Akka.

https://youtu.be/riMHC0Xpm9U
5 technologies that I will be learning in 2021 as a .NET developer

Let me watch this short vid.

https://www.patreon.com/nickchapsas

Damn, this guy has a lot of Patrons.

> Hello everybody, I'm Nick Chapsas and this is my Patreon page. For the past 3, years I've been creating free content for C# and .NET on my YouTube channel. 3 years later, and creating content is my full-time job. In order to diversify my revenue streams to make sure I can do this for a long time, I created a Patreon where you can support me monetarily.

I am jelly.

https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Orleans-MSR-TR-2014-41.pdf

///

High-scale interactive services demand high throughput with low latency and high availability, difficult goals to meet with the traditional stateless 3-tier architecture. The actor model makes it natural to build a stateful middle tier and achieve the required performance. However, the popular actor model platforms still pass many distributed systems problems to the developers.

The Orleans programming model introduces the novel abstraction of virtual actors that solves a number of the complex distributed systems problems, such as reliability and distributed resource management, liberating the developers from dealing with those concerns. At the same time, the Orleans runtime enables applications to attain high performance, reliability and scalability.

This paper presents the design principles behind Orleans and demonstrates how Orleans achieves a simple programming model that meets these goals. We describe how Orleans simplified the development of several scalable production applications on Windows Azure, and report on the performance of those production systems.

///

He links to this paper. Let me leave it aside for now.

https://github.com/akka/akka-meta/blob/master/ComparisonWithOrleans.md

https://youtu.be/riMHC0Xpm9U?t=128

He says that Halo's online service uses it.

https://youtu.be/riMHC0Xpm9U?t=168

He recommends this guy for a deeper intro.

https://youtu.be/riMHC0Xpm9U?t=190

I wonder what these source generators are.

https://youtu.be/riMHC0Xpm9U?t=241
> Reflection, but compile time.

I'll have to check this out.

https://youtu.be/riMHC0Xpm9U?t=290
> ASP.NET is actually using dictionaries and some very miminal reflection for the first instantiation of the classes to create them.

https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview

Oh you literally generate C# text. I could do this.

12:30pm. Hmmm, I could use this to interface Spiral with F# more deeply. Nevermind that for now.

https://youtu.be/riMHC0Xpm9U?t=358

I could have used gRPC back in 2020, but I was too stupid and went with ZeroMQ.

Determination really makes a difference. Back then I wanted to just learn enough webdev, but now that I want to really dive into it, my learning progress and trajectory is a lot more ferocious.

https://youtu.be/riMHC0Xpm9U?t=390
> It is way faster than REST, but more niche.

https://youtu.be/riMHC0Xpm9U?t=544
> A software engineer that knows devops technologies is very, very valuable.

He recommends that I learn devops to adds value to myself as a soft eng.

https://youtu.be/riMHC0Xpm9U?t=791

All this tech is something that I've often seen in job ads.

https://youtu.be/riMHC0Xpm9U?t=873
> I can't believe I was so late to the party learning this.

Sigh...just what was I doing in the past 8 years? I should just focus on gluing things together rather than making AI breakthroughs. It is like the world does not want me to pursue the path of transcendence.

12:45pm. https://youtu.be/9CDgPgWF9IY
Why I won’t need constructors anymore in C# 11

Let me watch this.

https://youtu.be/9CDgPgWF9IY?t=276

Hmmm, yeah, I've underestimated the required keyword. I see where he is going.

Constructors are the worst part of OO for me, so getting around them is always a bonus.

12:55pm. https://boards.4channel.org/a/thread/249601990#p249629470

///

>>249601990 (OP)
This page is godly because you can tell it's a word for word transcript of an actual conversation he had with an editor. Then he proceeded to not follow any of his advice in his own manga, and got them axed.

///

///

>>249629470
Somebody once told me that something that everyone enjoy is also something no one enjoy. You gotta accept that not everyone will be interested in your stuff and that some people will hate it.

///

...

I think that going along with popular Youtubers like Nick is a good strategy. What sells for them is usually what is in demand in the job market, so I should learn up and skill up myself.

I've watched that video by Onur, but I didn't get too much from it. The repo he showed should be valuable for me since I'll use it as a reference for setting up my own project. I also was under the impression that the project was not updated in a while and this dispelled that mistaken assumption.

1pm. The next step would be to study up on websockets in .NET.

As I said, now that I feel confident about both frontends and databases, the communication parts are what I need to tackle. I'll probably be studying this for a while, but at some point I am going to reach the zenith. At that point, it will be time to work on my people skills.

This will complete me as a programmer. Surely actually getting to the point where I am making money from it will count as something, right?

I believe that all this knowledge I am learning here will be useful either way. Having systems that communicate will be useful for scaling my own stuff.

I wish that at some point the reinforcement learning path would become viable.

Programming is a young field, it was completely different a few decades ago. So who is to say it won't change in the future."

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[56ed0f715d...](https://github.com/diphons/D8G_Kernel_oxygen/commit/56ed0f715dd00701972201eebb41d23dac2082c0)
#### Friday 2023-03-03 12:15:31 by Wang Han

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

---
## [HashbrownKazang/SppunnT](https://github.com/HashbrownKazang/SppunnT)@[f9d589448e...](https://github.com/HashbrownKazang/SppunnT/commit/f9d589448ed334a50ecd10c43f8f9fe2dcaaffe1)
#### Friday 2023-03-03 14:03:43 by HashbrownKazang

so I just wanted to take a moment to really just
say that this has really been an interesting experience,
having started less than just a few months ago, I've quite honestly been
putting in a lot of all nighters and reading and studying about
everything that I could get my hands on, and I still am not 100% sure
about what the hell I am doing but for sure am learning as fast as
humanly possible.

---
## [MajManatee/Yogstation](https://github.com/MajManatee/Yogstation)@[8e3e0b1450...](https://github.com/MajManatee/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Friday 2023-03-03 14:27:00 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [frozenproof/nckh2_real_2.0](https://github.com/frozenproof/nckh2_real_2.0)@[2f89a52fef...](https://github.com/frozenproof/nckh2_real_2.0/commit/2f89a52fef8d2a64d673437edb65aae39ad26082)
#### Friday 2023-03-03 14:59:24 by frozenproof

I need to render static html with valid js files , but they all used reacts because they can't understand what they were doing anymore . In another word, by being lazy and try to skip the problems , react has effectively turned everything into a chaotic maze without a way out . Fuck you react, literally.

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[04ba17a805...](https://github.com/bmccrat/songage/commit/04ba17a805e90619382485011f3131280b8a801b)
#### Friday 2023-03-03 16:19:58 by bmccrat

Create EAGLE 20's

This song was written in my first voluntary treatment stay at BRC and was chronologically the first one I wrote in there. It was the day Jonathan R got kicked out of the rehab for taking other peoples Suboxone. I had created a bond with him that would later turn into a world renowned druggieship, I never knew if I liked him romantically or platonically or was so repulsed that I was attracted. I know we spent nights manically babbling about our experiences with heroin and dreams of traveling, well at least they were my dreams and he emphatically consented to be a part of them in the future. We planned a beautiful train ride to California but when I showed up in Philadelphia after treatment to meet him and get high we never made it off the alphabet streets in Kensington, unless it was to go to Camden to cop over the tracks. I loved him. He loved me enough to help kill me on one occasion after a subsequent overdose on  some hot Philly fentanyl. This all came later and I suppose the fatal attraction I felt to him that I expressed with such longing in this song was a precursive intuition to the trauma we would later share. God bless you Jonathan, here's to all the invincible junkies in this world who've got no veins left, steal their fathers pocket watches, and don't even get high anymore just get well.

---
## [0x098/garrysmod-chatsounds](https://github.com/0x098/garrysmod-chatsounds)@[b57b3d8d45...](https://github.com/0x098/garrysmod-chatsounds/commit/b57b3d8d45f8dd4c014640f92eced35d940d4a36)
#### Friday 2023-03-03 16:47:32 by Ayane

My name is Skyler White yo (#428)

* My name is Walter Hartwell White.

I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a Virtual Youtuber empire for over a year now and using me as his recruiter. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my Live2D knowledge to recruit talents, which he would then hire using his connections in the Japanese utaite world. Connections that he made through his career with Niconico. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small indie channel could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Motoaki Yagoo Tanigo, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Yagoo threatened my family. I didn't know where to turn. Eventually, Hank and Yagoo had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Yagoo flatly refused to give him, and things escalated. Yagoo was able to arrange, uh I guess I guess you call it a hit on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over 77,000. Upon recovery, Hank was bent on revenge, working with a man named Riku Tazumi , he plotted to kill Yagoo, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Cover Corp, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my vtubing activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[97fb8dcd79...](https://github.com/bmccrat/songage/commit/97fb8dcd79b2532344faf08927318c08b867746e)
#### Friday 2023-03-03 16:57:13 by bmccrat

Create SAMSARA

This song was written in an improvisational jam between Nicolas (Nicky) on guitar and me on vocals as well as him singing ad lib with me recording in written form on the back of a piece of art I had made in there. The original copy of this song is still on the back of that piece of art to this day. Nicky and I formally wrote two songs together and had many more jams, our flow was immaculate and our harmonization was made in heaven. This song is deeply interpretive and reflective, pensive and abstract even, as our union often was. I love him to this day with my whole heart and have followed his journey from the outside looking in ever since I got into recovery and he stayed out of it for the most part. He is currently incarcerated in some capacity as he often was, having just come out of prison and into the inpatient facility when fate brought us together. I will get his art tattooed on me one day and have a copy of it with a letter from him in my song book at home. Nicky if you're reading this je t'aime plus que toute le monde.

---
## [ReefLakin/CatanAI](https://github.com/ReefLakin/CatanAI)@[baf24f4f9c...](https://github.com/ReefLakin/CatanAI/commit/baf24f4f9cf777c052426ad81073db324a43beda)
#### Friday 2023-03-03 17:55:28 by Reef Lakin

Adam is now functional

Adam now works like a dream. But not a proper good dream, kinda one of those ones you have at 5am and you don't really remember very well.

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[0dd70b12e5...](https://github.com/PhantomEpicness/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Friday 2023-03-03 18:13:04 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

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

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [asdfgn2399/homebrew](https://github.com/asdfgn2399/homebrew)@[f1150e6e1d...](https://github.com/asdfgn2399/homebrew/commit/f1150e6e1d24b74ab600b549776c7f664f16fe96)
#### Friday 2023-03-03 18:27:49 by rynosaur94

Setting Guide for G4 My Little Pony's Equestria

A full setting guide for the universe of My Little Pony Friendship is Magic.  Trying to blend show accuracy and tone with 5e's general heroic fantasy vibes, I've been maintaining this guide since I created it in 2016.  Contains Races, Feats, Subclasses, Spells, Items mundane and magical, Religions, and more.

---
## [dodokek/DOS-practice](https://github.com/dodokek/DOS-practice)@[be1703547a...](https://github.com/dodokek/DOS-practice/commit/be1703547a63071022cf2d884b456bce59095a73)
#### Friday 2023-03-03 18:40:28 by Aleksander Morozov

now on key press border appears

i fucking spend 3 hours debugging this shit and it turned out that i used bp somewhere in my code, from which dos died every time

---
## [PSP-High-Altitude/PSP-HA-Thermal-Modeling](https://github.com/PSP-High-Altitude/PSP-HA-Thermal-Modeling)@[19fb27ebf5...](https://github.com/PSP-High-Altitude/PSP-HA-Thermal-Modeling/commit/19fb27ebf53ba9823cc25462c4599142f690932e)
#### Friday 2023-03-03 18:43:54 by Shayak Chatterjee

Temperature of nosecone wall line 141

Kinda shitty gives negative Kelvin values impossible need to troubleshoot either nosecone heat flux or h_eber calcs

---
## [EgorDinamit/lobotomy-corp13](https://github.com/EgorDinamit/lobotomy-corp13)@[582f5b38cb...](https://github.com/EgorDinamit/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Friday 2023-03-03 19:56:33 by Lance

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
## [leserg73/issrc](https://github.com/leserg73/issrc)@[118c151654...](https://github.com/leserg73/issrc/commit/118c15165401bb2acb62358f963777c44fb9c582)
#### Friday 2023-03-03 20:13:52 by Johannes Schindelin

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[3978cfe70f...](https://github.com/realforest2001/forest-cm13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Friday 2023-03-03 20:32:37 by spartanbobby

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
## [crumbtoo/puppy.tf-site](https://github.com/crumbtoo/puppy.tf-site)@[faaae46304...](https://github.com/crumbtoo/puppy.tf-site/commit/faaae46304288fc5fd142ced30a8a5d6e4e7cdfb)
#### Friday 2023-03-03 21:46:15 by Madeline Slaga

fuck you this is my project i dont have to write good commit messages

---
## [Thelema-SS/Thelema-STG](https://github.com/Thelema-SS/Thelema-STG)@[635aee8e34...](https://github.com/Thelema-SS/Thelema-STG/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Friday 2023-03-03 21:49:34 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [SUPERCILEX/clap](https://github.com/SUPERCILEX/clap)@[762b06fba4...](https://github.com/SUPERCILEX/clap/commit/762b06fba48533169c36a1b60c364657c06800de)
#### Friday 2023-03-03 22:28:32 by Ed Page

fix(error): Try to polish/clarify messages

In text communication you need to balance
- Scannability, putting the most important information upfront
- Brevity so people don't get lost in the message
- Softness to help ease people through a frustrating experience

I feel we weren't doing great on the first two points, so tried to
iterate on the messages to improve them.  I hope we aren't suffering too
much on the third point as a side effect.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[d7c05a7165...](https://github.com/realforest2001/forest-cm13/commit/d7c05a71658b5b7f5312c6a0ec9947f59b307b60)
#### Friday 2023-03-03 22:48:54 by carlarctg

Aimed shot and spotting now have laser beams. (#1905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Aiming a shot on a sniper rifle now adds a red laser beam that connects
the target and the aimer. Spotting designators will emanate a faint
yellow one. Both will slowly increase in alpha from 0 to max as the
tracking progresses.

The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Stepping through laser beams will check for eye protection, if it isn't
sufficient, and the small probability chance passes, the target will
scream in pain! Completely flavor. If they have enough eye protection,
it will bounce off their headgear, and if said protection is BiMex
patented personal shades it will create a cool visual effect.

Refactored eye_protection to have three levels, flavor, flashes, and
welding. Sunglasses have flavor protection, sechuds have flash
protection, welding gear has welding protection.

The spotter's designator now has a white band on it to distinguish it
from the rest.

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

> Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.

The primary reason for this addition is because it looks sick as FUCK.
The secondary one is to help xenos see where they're being shot from.

> The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Makes sense, cloaked sniper/spotters shouldn't be made completely
useless due to the beam. It makes sense for the laser to reduce aim time
and it isn't a pain for xenomorphs to deal with as they know exactly
where it is coming from and where they can run for cover (And other
xenos can protect them better)

> Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

It made no sense for sniper reticles to be blue. Red is danger, yellow
is warning, blue is.... good? Additionally, since both reticles for
spotting and aiming were nigh-identical, it caused quite the amount of
confusion. I've tested it myself, you can spook away xenos with only
spotting because they think it's the aimed shot reticle.

> The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Look, I know what I just said makes this sound stupid. But I think it
makes a lot of sense for the dangerous high-tech sniper rifles to have
stronger blue lasers, it just feels like a 'strong sci fi laser' color.
Like the pulse rifle in base ss13, it looks similar to the disabler but
you don't see anyone complaining. The base sniper reticle being red is
enough for people to realize this is a more dangerous version anyways.

> Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.

Cool flavor. Also lore-accurate!

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>


Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>

https://streamable.com/kyprhl

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
add: Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.
bal: The sniper's laser beam can be disabled with a button, but keeping
it enabled reduces aiming shot time. Cloaked spotters will not cause a
beam to appear.
imageadd: Completely resprited the indicators for spotting (it's now
yellow) and aiming (it's now red, usually)
imageadd: The XM42B and PMC sniper rifles have more intense blue lasers
and reticles.
add: Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.
refactor: Refactored eye_protection to have three levels, flavor,
flashes, and welding. Sunglasses have flavor protection, sechuds have
flash protection, welding gear has welding protection.
imageadd: The spotter's designator now has a white band on it to
distinguish it from the rest.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: harryob <me@harryob.live>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[904dc7d239...](https://github.com/Buildstarted/linksfordevs/commit/904dc7d239bce2819a1d2192384b6e3756bb9939)
#### Friday 2023-03-03 23:08:33 by Ben Dornis

Updating: 3/3/2023 10:00:00 PM

 1. Added: The Complexity Halo
    (https://www.stephenlewis.me/blog/complexity-halo/)
 2. Added: Inverted computer culture (a thought experiment)
    (http://viznut.fi/texts-en/inverted_computer_culture.html)
 3. Added: First Impressions of Bluesky's Brand New iOS App · Notes
    (https://notes.ghed.in/posts/2023/bluesky-ios-app-review/)
 4. Added: I hereby declare a sabbatical
    (https://archvile.net/2023/03/03/declare-sabbatical.html)
 5. Added: The Cotorreo
    (https://kinduff.com/2023/03/02/the-cotorreo/)
 6. Added: Teach, Show, then Consult: Make GPT a Music Composition Guide
    (https://mazzzystar.github.io/2023/03/03/teach-show-consult-gpt/)
 7. Added: Hacking my appetite - Stavros' Stuff
    (https://www.stavros.io/posts/hacking-my-appetite/)
 8. Added: Your friend the language model
    (https://dynomight.net/llm-friend/)
 9. Added: Federated language models, or the future of universal computing
    (https://faingezicht.com/articles/2023/03/02/federated-language-models/?src=hn)
10. Added: The Letter Circle
    (https://lostgarden.home.blog/2023/02/26/the-letter-circle/)
11. Added: Aleksandr Solzhenitsyn Center — Solzhenitsyn Live Not by Lies
    (https://www.solzhenitsyncenter.org/live-not-by-lies)
12. Added: ChatGPT Explained: A Normie's Guide To How It Works
    (https://www.jonstokes.com/p/chatgpt-explained-a-guide-for-normies)
13. Added: Web Interface Guidelines
    (https://rauno.me/interfaces)
14. Added: Ryan Bigg - Please explain, Elastic Search
    (https://ryanbigg.com/2023/03/please-explain-elasticsearch)
15. Added: Meta’s Next-generation Realtime Monitoring and Analytics Platform
    (https://www.micahlerner.com/2023/02/27/metas-next-generation-realtime-monitoring-and-analytics-platform.html)
16. Added: Use Next.js Image component in posts with Markdown
    (https://scastiel.dev/nextjs-image-in-markdown)
17. Added: Obvious to you, amazing to others
    (https://josem.co/obvious-to-you-amazing-to-others/)
18. Added: iOS Continuity Camera not working in Chrome
    (https://blog.tomayac.com/2023/02/16/ios-continuity-camera-not-working-in-chrome/)
19. Added: CI/CD Best Practises: Scaling A Delivery Platform — Evan Smith
    (https://iamevan.me/blog/cicd-best-practises)
20. Added: We want your feedback! Introducing Polly v8
    (https://www.thepollyproject.org/2023/03/03/we-want-your-feedback-introducing-polly-v8/)

Generation took: 00:08:21.8108310

---

