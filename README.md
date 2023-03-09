## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-08](docs/good-messages/2023/2023-03-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,414,576 were push events containing 3,528,612 commit messages that amount to 257,157,718 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [git-for-windows/git](https://github.com/git-for-windows/git)@[bd6ebabe44...](https://github.com/git-for-windows/git/commit/bd6ebabe440f32cae76cd354d79022190afa3066)
#### Wednesday 2023-03-08 00:02:07 by Johannes Schindelin

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
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[f3354a9fbc...](https://github.com/facebook/pyre-check/commit/f3354a9fbc84f8521180c5948e53bc1b05a1fc2e)
#### Wednesday 2023-03-08 00:31:11 by Steven Troxler

Avoid using an alias for AsyncContextManager

Summary:
For unknown reasons, Pyre is unhappy with the current implementation
of `typing.pyi`, which uses a generic type alias to `AbstractAsyncContextManager`
for `AsyncContextManager`.

Debugging this could be difficult - Pyre doesn't really provide us with any clue
about why a type is invalid, so we'll probably need to spend time doing a deep
dive: I filed T146882109 to investigate this in more detail but in my opinion we
really need to prioritize bumping typeshed

(Justification for why a patch and bump is better than filing a task
and claiming that it blocks typeshed upgrade:
- having a bunch of patches to maintain is tech debt, but it is very explicit;
  we can look at the patches and see exactly how many fixes are needed. And
  updating the patches, while annoying, is pretty easy (maybe 2-5 minutes per patch
  per update).
- sitting on an old typeshed, on the other hand, involves exactly the same bugs
  except they are accumulating invisibly, plus users aren't getting the benefit of new
  typeshed features; we've now been explicitly asked to bump at least twice

**How the vendored part of this diff was created**

```
# iterate on this until new patch applies cleanly
rm -rf ~/patched_typeshed
buck2 run //tools/pyre/scripts:download_typeshed -- -p ~/fbsource/fbcode/tools/pyre/scripts/typeshed-patches -o ~/patched_typeshed -u https://api.github.com/repos/python/typeshed/zipball/8aedbda4cdff81478b7414e46c400ad016342e02

# once patches look good, update the vendored code
rm -rf ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
cp -R ~/patched_typeshed/typeshed ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
```

(note that the `-u` flag is pinning to the URL discovered in the very first run when creating D43666059 - you want to omit it when starting a typeshed bump, but then pin it after that so that new commits to typeshed don't break all your patches).

Reviewed By: grievejia

Differential Revision: D43680647

fbshipit-source-id: 18e2d04b9b545f9e1a844b4eddad68066ee1f9a8

---
## [GerHobbelt/mupdf](https://github.com/GerHobbelt/mupdf)@[603640c472...](https://github.com/GerHobbelt/mupdf/commit/603640c47282100affa74b4ae1fc253a601a030e)
#### Wednesday 2023-03-08 00:40:49 by Ger Hobbelt

fix dumb error by me: forgot to check against stderr in a tesseract report function. This resulted, in the bigger `mutool_ex` app, in a **very curious** failure mode where tprintf() internals, which are sent through the fz_error() API series (mupdf, modified), invoked the windows Writefile() Win32 API ... which **failed**. Because the Win32 fixed STDERR_HANDLE was suddenly reported as the cause of WriteFile() --> error 6 (Invalid Handle)!

Now it gets dirtier...

When this happens, code from previous run-ins with serious bad shite would try to report this error to the fz_stddbg() 'standard debug' channel (which is a thing that does exist on MSWin and *is* used by your truly, **plus** the same error report would go to fz_stderr.

**whoops!**

That one is *invalid* by now, according to the OS, (thanks to an inadvertent `fclose(f)` where `f == stderr`) so we got into a cycle which uncovered another bug as this failure mode was yet unexpected: we were in a fz_try/fz_catch C-style exception frame, BUT we were also inside *another* C-style exception being thrown, so the cycle-detection logic, which was engineered to prevent a stack overrun due to crazy galloping scenarios like this, would simply attempt to report the *now fatal & new* error to stderr, where it ... fails.

A side-effect of the bug(s) in that code resulted in the fz_throw() to **return to the caller**, which was very much *not* expected and resulted in an infinite loop around the attempt to get WriteFile() do write some text, WriteFile() telling us it failed, length written: `n == 0`, loop says: keep trying while `n > 0` and there you are.

That loop bit was previously devised to cope with another nasty mishap we had a very tough time debugging, where it turned out that when you use stdout/stderr echo-ing applications via any type of syscall which 'redirects' those stdout+stderr handles to application handles, i.e. Win32 *pipes*, so the calling application can get its grubby paws on your invoked executable's stdout/stderr blatherings, things go very bad indeed when the **syscall-invoking application** happens to be (relatively) slow with the stdout/stderr pipe redirection emptying: as that particular app (Qiqqa up to v83) didn't ever have async pipe stream reading implemented before, it thus turned out that MS Win64 has somewhere around 64K pipe channel buffer for your stdout/stderr redirects via Win32 pipes and WriteFile, which is always at the bottom/core of any printf()/fprintf(stderr), will then **hang**. At the most curious of times and places.
Unless... you 'improve' your stdout/stderr writing mechanism with some code that is meant to cope with 'force majeure' failures like this, i.e. using a WriteFile that's time-bound, i.e. will now **not hang** any more but instead report some failure diagnostic (with the help of a few friendly Win32 APIs) about *why* it didn't succeed in delivering the goods.

It all works great, did great under various adversarial circumstances, so case closed.

Until today, where we didn't realize we just fclose()d stderr and got another type of error. Now I knew I would *ideally* have to be pretty pedantic in the failure-mode code lines around the fitz/mupdf C-style exception handler, but previously didn't think that level of detail was necessary (it wasn't) and when done, it would look butt-ugly in the code (it does) as every 'independent' line/chunk that is at risk must be wrapped in its own try/catch while we travel down the rabbit hole of failure-upon-failure as failures are want to be reported... which, of course, when you fclose(stderr) and the OS takes you at your word, is cause for a lot of pain.

So the fix is in, the fz_try/fz_catch + error/debug channels now support this scenario and 'survive': ultimately they'll kick in the debugger or call exit(666) in a final attempt to be nice about it.

Meanwhile, the tesseract code gets the other fix: fclose prevention for stderr.

It is, however, part of a bigger fix elsewhere...

---
## [actonlang/acton](https://github.com/actonlang/acton)@[2e22988b8f...](https://github.com/actonlang/acton/commit/2e22988b8f27312641df0677d1555420c14c858d)
#### Wednesday 2023-03-08 01:02:28 by Kristian Larsson

Revamp time module

This significantly extends the time module with a proper, somewhat
thought through design of how to work with time in Acton. It boils down
to two usage patterns:
- measuring elapsed time (e.g. for benchmarking)
- telling the current date and time (e.g. for logging)

We want to design a user experience that makes this straight forward and
that deliver correct results. Time is hard and most people have no idea
how complex it is.

I think a lot of Python code uses datetimes to compute timedeltas when
they really should be using monotonic time. It's a haphazard design,
probably because things have been built over time (hah, pun intended).
Many other languages place a much stronger emphasis on the difference
between measuring elapsed time and telling wall clock time. Rust has
Instants and Durations. Those are the basic classes I copied here but I
think Zig did a much better job of wrapping that up in a user friendly
interface.  They call it a Timer. We have a Timer now too. Compare:

    t1 = time.Instant.now()
    t2 = time.Instant.now()
    diff = t2 - t1
    print("Elapsed time:", diff)

With a Timer, which I think is more intuitive:

    t = Timer()
    print("Elapsed time:", t.elapsed())

Many things are not implemented, like Calendars, Clocks, Precision or
Timezones but we have the basic structure of it. A lot of inspiration
from Swift, though they seem to have a needlessly complicated solution.
I'd like to strike a balance of their expressiveness but avoiding
boilerplate code.

There are various bugs in the compiler or language shortcomings (no u64
for example) so there are a few workarounds in the code that we need to
sort out but the overall module design is pretty set I think.

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[c58cbb4dfb...](https://github.com/willardstation/tg-voidcrew/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Wednesday 2023-03-08 01:08:05 by John Willard

Reworked PDA menu & NtOS themes (#73070)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [MassMeta/tgstation](https://github.com/MassMeta/tgstation)@[a3451b7fe4...](https://github.com/MassMeta/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Wednesday 2023-03-08 01:19:36 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [Nylux/space-station-14](https://github.com/Nylux/space-station-14)@[581e8a0d12...](https://github.com/Nylux/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Wednesday 2023-03-08 01:39:26 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [loongson-gfx/drm-tip](https://github.com/loongson-gfx/drm-tip)@[5e7e1e00f3...](https://github.com/loongson-gfx/drm-tip/commit/5e7e1e00f3dba60fc39c63dbc52bb0f8f26b78a2)
#### Wednesday 2023-03-08 02:32:39 by suijingfeng

drm: add kms driver for loongson display controller

Loongson display controller IP has been integrated in both Loongson
North Bridge chipset(ls7a1000 and ls7a2000) and Loongson SoCs(ls2k1000
and ls2k2000 etc), it even has been included in Loongson BMC products.

This display controller is a PCI device, it has two display pipe. For
the DC in LS7A1000 and LS2K1000 each way has a DVO output interface
which provide RGB888 signals, vertical & horizontal synchronisations,
and the pixel clock. Each CRTC is able to support 1920x1080@60Hz,
the maximum resolution is 2048x2048 according to the hardware spec.

For the DC in LS7A2000, each display pipe is equipped with a built-in
HDMI encoder which is compliant with HDMI 1.4 specification, thus it
support 3840x2160@30Hz. The first display pipe is also equipped with
a transparent vga encoder which is parallel with the HDMI encoder.
The DC in LS7A2000 is more complete, besides above feature, it has
two hardware cursors, two hardware vblank counter and two scanout
position recorders.

 v1 -> v2:
  1) Use hpd status reg when polling for ls7a2000
  2) Fix all warnings emerged when compile with W=1

 v2 -> v3:
  1) Add COMPILE_TEST in Kconfig and make the driver off by default
  2) Alphabetical sorting headers (Thomas)
  3) Untangle register access functions as much as possible (Thomas)
  4) Switch to TTM based memory manager and prefer cached mapping
     for Loongson SoC (Thomas)
  5) Add chip id detection method, now all models are distinguishable.
  6) Revise builtin HDMI phy driver, nearly all main stream mode
     below 4K@30Hz is tested, this driver supported these mode very
     well including clone display mode and extend display mode.

 v3 -> v4:
  1) Quickly fix a small mistake.

 v4 -> v5:
  1) Drop potential support for Loongson 2K series SoC temporary,
     this part should be resend with the DT binding patch in the future.
  2) Add per display pipe debugfs support to the builtin HDMI encoder.
  3) Rewrite atomic_update() for hardware cursors plane(Thomas)
  4) Rewrite encoder and connector initialization part, untangle it
     according to the chip(Thomas).

 v5 -> v6:
  1) Remove stray code which didn't get used, say lsdc_of_get_reserved_ram
  2) Fix all typos I could found, make sentences and code more readable
  3) Untange lsdc_hdmi*_connector_detect() function according to the pipe
  4) After a serious consideration, we rename this driver as loongson.
     Because we also have drivers toward the LoongGPU IP in LS7A2000 and
     LS2K2000. Besides, there are also drivers about the external encoder,
     HDMI audio driver and vbios support etc. This patch only provide DC
     driver part, my teammate Li Yi believe that loongson will be more
     suitable for loongson graphics than lsdc in the long run.

     loongson.ko = LSDC + LoongGPU + encoders driver + vbios/DT ...

  v6 -> v7:
   1) MAINTAINERS: from drivers/gpu/drm/lsdc/ to drivers/gpu/drm/loongson.
      I change this in local, but forget git add MAINTAINERS. Sorry.

  As a basic KMS driver, the user experience is merely enough when using
  with X server under mate and xfce desktop environment. This dirver is
  ready to be merged, and we will take the responsibility if there are
  any bug happen.

Signed-off-by: Li Yi <liyi@loongson.cn>
Signed-off-by: suijingfeng <suijingfeng@loongson.cn>
Signed-off-by: suijingfeng <15330273260@189.cn>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[ca1f89de03...](https://github.com/ARF-SS13/coyote-bayou/commit/ca1f89de03d088d262cef2bdbfffdeb29be909e1)
#### Wednesday 2023-03-08 03:58:40 by Tk420634

Mobn't

Removes some mobs to get us away from the ram limit some.

Fuck you ram limit, all my homies hate 32 bit software.

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Wednesday 2023-03-08 04:33:29 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [checksum-fail/spcasm](https://github.com/checksum-fail/spcasm)@[c39be0ac56...](https://github.com/checksum-fail/spcasm/commit/c39be0ac564074318c00eecfe709261350f84fe1)
#### Wednesday 2023-03-08 05:23:38 by kleines Filmröllchen

update a bunch of javascript and wasm shit

i hate my life

---
## [WensLogic/ERP](https://github.com/WensLogic/ERP)@[82763183d2...](https://github.com/WensLogic/ERP/commit/82763183d2da5fe652d66dd482bbe7efedc2dbd9)
#### Wednesday 2023-03-08 07:49:59 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#111736

X-original-commit: f05491105f93939490cbeb078cb7653c38685644
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Pin-alternative/S.P.L.U.R.T-Station-13](https://github.com/Pin-alternative/S.P.L.U.R.T-Station-13)@[bc48a6eafc...](https://github.com/Pin-alternative/S.P.L.U.R.T-Station-13/commit/bc48a6eafcf9afedfc419afaa982dd15339a94aa)
#### Wednesday 2023-03-08 08:15:08 by Darius

Add vampire ability permission check

Adds a new mob proc that allows checking if vampiric abilities should function. Allows easily checking anti-magic, trait holy, garlic necklace, garlic blood, and staked status.

Bloodfledge actions and coffin healing will now use this check. Flight potions will warn bloodfledge quirk users before allowing consumption.

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[db7534d6da...](https://github.com/Sealed101/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Wednesday 2023-03-08 08:37:32 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [swordcube/Funkin-Raylib](https://github.com/swordcube/Funkin-Raylib)@[54fddc502e...](https://github.com/swordcube/Funkin-Raylib/commit/54fddc502e842fa48dfdafb2db12d4801f5fb8f0)
#### Wednesday 2023-03-08 09:18:50 by swordcube

oh god i made a big commit fuuck

i'ma gonna try to list most of the changes here while my 3am brain still can:
- hscript support (haha funny scripting  !)
- velocity shit
- ratings (kinda, only shows sick for now)
- made the keys class not a typedef
- changed a bunch a shit to use `MathUtil.STANDARD_PI` because c++ compiler errors :+1:
- add controls class to avoid manually checking keys for if they are just pressed
- a bit of extra documentation
- make sustains render better
- turn BUGS.txt into TODO.txt
- make the console prints actually work and look a bit nicer

uh that's all i can remember

---
## [SDP-GeoHunt/geo-hunt](https://github.com/SDP-GeoHunt/geo-hunt)@[f9251b69f7...](https://github.com/SDP-GeoHunt/geo-hunt/commit/f9251b69f7619f194275af5f78673368a1de171b)
#### Wednesday 2023-03-08 09:59:11 by Marwan

Compose migration (#26)

* Modify configuration files to support Kotlin & Jetpack Compose

As discussed this morning, we plan on moving to Kotlin and Jetpack compose. This commit marks the beginning of the modification to make it.

* Update minSdk to comply with firebase requirement

Changes:
* Change from minSdk:24 to minSdk:28 to comply with the firebase
  realtime database requirements

* Delete old java activity file and write basic test

Changes:
* Remove `GreetingActivity.java` and `MainActivity.java` and
  dependencies
* Write simple `ComposeActvitityTest.kt`

* fix: Support for coverage with Kotlin

* Added Mockito

* Fixed the build.gradle with proper versions

* :fire: :100: :triump: base :rage:

---------

Co-authored-by: BoyeGuillaume <guillaume.boye@epfl.ch>

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[f365702d0c...](https://github.com/NetworkManager/NetworkManager/commit/f365702d0c65445016fcaa25665d7c960cd81e36)
#### Wednesday 2023-03-08 10:12:06 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[0002d22095...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/0002d2209531e9c8630a2556a49404813eab5979)
#### Wednesday 2023-03-08 10:12:24 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries
  (mpfr, mpc, isl, glibc) are all built by the same compiler (xgcc)
  instead of a mixture of the bootstrapFiles' compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [ZzAve/teambalance](https://github.com/ZzAve/teambalance)@[be41a19967...](https://github.com/ZzAve/teambalance/commit/be41a199672f42698acd0e60d1d135ce589d480b)
#### Wednesday 2023-03-08 11:08:33 by Julius van Dis

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
## [smileynet/Cataclysm-DDA-ios](https://github.com/smileynet/Cataclysm-DDA-ios)@[8e39d6f97c...](https://github.com/smileynet/Cataclysm-DDA-ios/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Wednesday 2023-03-08 11:50:07 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [gim-largerepo/including-investment-59GB](https://github.com/gim-largerepo/including-investment-59GB)@[220e29c4bc...](https://github.com/gim-largerepo/including-investment-59GB/commit/220e29c4bc6e1f6c813ef41cf5d097293568062b)
#### Wednesday 2023-03-08 13:05:32 by Scott Martin

Sea laugh I care work red friend think other represent dog life perhaps matter.

---
## [nakato/nix-visionfive2-bsp](https://github.com/nakato/nix-visionfive2-bsp)@[32a28bef1d...](https://github.com/nakato/nix-visionfive2-bsp/commit/32a28bef1da57bc2f627e9451196bd183197ad29)
#### Wednesday 2023-03-08 13:11:32 by Sachi King

Build boot firmware in via uboot per board uboot documentation

This means messing with uboot doesn't mean re-compiling OpenSBI
needlessly, as we really only need to include u-boot into the SBI
artifact.  This does mean updating OpenSBI causes a whole u-boot
rebuild, but we're less likely to hack on OpenSBI than u-boot, so that's
fine enough.

This is my repo and I can bitch if I want to; fuck Sydney's fucked road
infrastructure, how is the proper route literally a bunch of rat-runs
all put together?  Let me make a left, to make a right, to make a left
to then get in a turn lane with less than 10 meteres notice, yea, that
is safe, lets not do that.

---
## [AlvCyktor/Yogstation](https://github.com/AlvCyktor/Yogstation)@[8e3e0b1450...](https://github.com/AlvCyktor/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Wednesday 2023-03-08 13:57:03 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [Carreau/napari](https://github.com/Carreau/napari)@[3ec4be1ae8...](https://github.com/Carreau/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Wednesday 2023-03-08 14:20:52 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[aad91decf8...](https://github.com/diphons/D8G_Kernel_oxygen/commit/aad91decf8eecba36f5a6872faf65e4800141f56)
#### Wednesday 2023-03-08 14:25:47 by George Spelvin

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

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[264edfb877...](https://github.com/diphons/D8G_Kernel_oxygen/commit/264edfb877cc112ecd1d530d5e19dbd6a54ff80b)
#### Wednesday 2023-03-08 14:27:18 by George Spelvin

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

---
## [fredericdalleau/linuxkit](https://github.com/fredericdalleau/linuxkit)@[860934d5d9...](https://github.com/fredericdalleau/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Wednesday 2023-03-08 15:27:32 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[bdc9c58586...](https://github.com/EdwardNashton/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Wednesday 2023-03-08 15:39:15 by Technobug14

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
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[31eabb62f1...](https://github.com/Bjarl/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Wednesday 2023-03-08 16:02:25 by spockye

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
## [mrousavy/react-native-reanimated](https://github.com/mrousavy/react-native-reanimated)@[b83625045f...](https://github.com/mrousavy/react-native-reanimated/commit/b83625045f314e498fe32adc34b43ce20a77f946)
#### Wednesday 2023-03-08 16:50:22 by Angelika Serwa

Fix reloading when using useAnimatedKeyboard (#3932)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Fixes
https://github.com/software-mansion/react-native-reanimated/issues/3786

### Why it crashes: 
On the main thread `CADisplayLink` calls `updateKeyboardFrame` 60 times
per second. Calling `updateKeyboardFrame` calls listener on the JS side.
When reloading the runtime gets destroyed on the JavaScript thread. So
when those two things happen at the same time (which in this case
happens often) we get the crash that we're trying to call a js function
on destroyed js runtime.

### Why don't you just remove the listeners in
`NativeReanimatedModule::~NativeReanimatedModule()`, we're cleaning up
everything here:
I've tried and it appeared to work at first but I still got crashes when
running [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
and probably that's why:

![Screenshot 2023-01-11 at 23 02
18](https://user-images.githubusercontent.com/6280457/211935579-16ff642d-fb15-469b-909e-e36ba9d72781.png)
![Screenshot 2023-01-11 at 23 02
35](https://user-images.githubusercontent.com/6280457/211935599-88cb9e81-20d7-4f96-bfd0-9c3b5da13b24.png)

So when `~NativeReanimatedModule` is being called the runtime related
stuff is already deleted and there is a short window of time that the
runtime is being deleted and we still call js stuff, or at least that's
my theory 🤷‍♀️

So my proposition for now is to listen for
`RCTBridgeDidInvalidateModulesNotification` notification. It's called
just before deleting happens. Also I'm using
`RCTUnsafeExecuteOnMainQueueSync` because I want to wait until the
listeners are completely deleted on the main thread and then delete js
stuff.

### A nicer solution? 
If you look a bit above `[[NSNotificationCenter defaultCenter]
postNotificationName:RCTBridgeDidInvalidateModulesNotification` line in
React code you'll see that React calls `invalidate` on all modules' data
before even posting the notification. Maybe we should clean reanimated
stuff here. I haven't explored that though yet and I don't know where is
reanimated's module data and what is module data at all and where to put
that `invalidate` function, I just got this idea while posting this PR.

## Test plan

Just run AnimatedKeyboardExample and reload the app.
Also the [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
nicely catches other data races.

Tested with changes from
https://github.com/software-mansion/react-native-reanimated/pull/3911
and it works
Also tested on FabricExample and surprisingly it also works.

---
## [peff/git](https://github.com/peff/git)@[5a3ed6a6cb...](https://github.com/peff/git/commit/5a3ed6a6cb7b471f1c3cbadf3ef10ced29d3c0fb)
#### Wednesday 2023-03-08 17:39:34 by Jeff King

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
## [newstools/2023-iol](https://github.com/newstools/2023-iol)@[a91e8667d4...](https://github.com/newstools/2023-iol/commit/a91e8667d4a359fb8a216227219076d29f2c026a)
#### Wednesday 2023-03-08 18:00:48 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/news/crime-and-courts/durban-court-hands-down-life-sentence-plus-18-years-to-monster-boyfriend-who-killed-partner-and-unborn-baby-despite-protection-order-560f97b5-9cc9-460d-aedc-eabf62167014]

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[11aab72dc9...](https://github.com/pytorch/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Wednesday 2023-03-08 18:07:47 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [PaulRitter/OpenDream](https://github.com/PaulRitter/OpenDream)@[04e782a3fa...](https://github.com/PaulRitter/OpenDream/commit/04e782a3fa9ba78f491dfff7d7be02c63ed0f0a0)
#### Wednesday 2023-03-08 18:23:13 by Altoids1

Improves the grammar, functionality, and code quality of set declarations (#776)

* Makes Consume array overload return the tokentype it found

Plus adds some extra comments, in my crusade to comment more things.

EDIT: hate you Github Desktop

* Removes MultipleVarDec..., replaces with Aggregate generic

Removes DMASTProcStatementMultipleVarDeclarations,
replaces with DMASTAggregate<>.

DMASTAggregate now has the generic-ified responsibility of being a statement which is actually an aggregate of several statements, all of the same type.

The point of this is so that this aggregation behaviour can also be used for set declaration blocks (and maybe other stuff if we find other uses, I dunno)

* Adds some helpful ctors for DMASTProcBlockInner

There's a lot of repetitive empty or near-empty array inits at the caller side of some of these constructions, so I went ahead and moved those into the ctor. Also allows for a minor optimization (preferring using Array.Empty<> instead of constructing empty arrays).

* Improves SetStatement grammar, function & quality

(If any of you demand I insert the oxford comma into the commit header I am leaving 5ever :rage: )

This commit does several things in one fell swoop:
- Set statements now accept blocking, commas, bracing, all the good stuff that var declarations do
- Blocks now very consistently evaluate their SetStatements first and foremost, before anything else, in a way that makes sense
- Use of the 'in' keyword is now properly prohibited for all set use cases except 'src'
- 'src' now properly gives an unimplemented warning

Also in this commit is a bunch of random autodoc added to things that I looked at or touched over the course of writing this commit. :innocent:

* Implements cursed parity behaviour for non-const set statements

AFAIK, in BYOND, the previous set statement value is used to prop-up one that has a non-constant right-hand side. So I guess we have that behaviour available, now. :sweat_smile:

EDIT: Fixed behaviour in the didError case, minor formatting fixes

* Style fix, replaces several "\n{" with "{\n"

Most of these were my fault. Not all of them though. :^)

* Does the Wixoa reviews, adds EmptyBlock pragma error

As a byproduct of doing the reviews, I have accidentally added empty block detection for several (although perhaps not most) loops and blocks available in OD.

* Brace style fixes

* Does more Wixoa reviews, generalizes EmptyBlock emission

Note that we do not, as of yet, emit this warning for empty procs. This is because:
1. our own DMStandard has several empty procs (usually because they are unimplemented or useless, like the BYOND Hub interface procs)
2. Users may sometimes define an empty proc, intentionally, to act as an abstract virtual that child types can define in their own way.

We can revisit the problem later, I'm just trying to get my PR greenlit.

* Adds test for EmptyBlock pragma emission

Co-authored-by: wixoa <wixoag@gmail.com>

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[b9313e344b...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/b9313e344b7b468f2e68d428e69c19503e3833b8)
#### Wednesday 2023-03-08 18:32:14 by Keekenox

Fix Keek's Offset Sprites Finally (#5135)

Keekenox has fixed the pixel offsets for sprite assets, which is a
crucial improvement to the game. In the previous version, some sprites
appeared blurry and misaligned, making the game look unprofessional and
unpolished. With this commit, the sprites are correctly aligned,
improving the overall visual quality of the game. This is important
because it enhances the player experience and makes the game more
enjoyable.

Firstly, fixing the pixel offsets ensures that the sprites display
accurately across all devices and platforms. With the increasing
popularity of gaming on different devices, it is essential that the game
looks good and functions well across all of them. Inconsistent display
of assets can be frustrating for players and negatively impact their
experience. By addressing this issue, Keekenox has taken a step towards
creating a more accessible game, which can be played by a wider
audience.

Secondly, fixing the pixel offsets is important for the branding of the
game. The look and feel of the game are integral to creating a strong
brand image. The blurry and misaligned sprites make the game look less
polished and unprofessional. With the visual improvements from this
commit, the game now looks more visually appealing, and its brand image
is strengthened. This can lead to increased engagement, higher retention
rates, and better marketing opportunities.

Thirdly, by fixing the pixel offsets, Keekenox has made the game more
scalable. As the game grows and more assets are added, the risk of
misaligned and blurry sprites increases. By addressing this issue early
on, Keekenox has prevented potential headaches down the road, saving
time and resources in the long run. This demonstrates a commitment to
quality and attention to detail that players appreciate and respect.

Fourthly, fixing the pixel offsets is important for maintaining the
quality of the game. Players expect games to look and feel polished,
with attention given to even the smallest details. The misaligned and
blurry sprites detract from the overall quality of the game, leaving
players with a negative impression. By fixing this issue, Keekenox has
shown that they care about their players' experience and are committed
to delivering a high-quality game.

Lastly, fixing the pixel offsets has a direct impact on the player
experience. Games are meant to be enjoyable, and players want to immerse
themselves in a world that looks and feels great. Misaligned and blurry
sprites can be distracting and detract from the experience, making it
less enjoyable for the player. With the improvements made in this
commit, players can now enjoy the game without these distractions,
leading to increased satisfaction and potentially higher retention
rates.

In summary, fixing the pixel offsets for sprite assets is an important
improvement to the game. It ensures accurate display across all devices,
strengthens the brand image, improves scalability, maintains quality,
and enhances the player experience. Keekenox has demonstrated a
commitment to delivering a high-quality game, and players will
appreciate the attention to detail that went into this improvement.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[d5eca255fa...](https://github.com/pytorch/pytorch/commit/d5eca255fac9f28ed327a5da395a88ff4758d39a)
#### Wednesday 2023-03-08 18:45:50 by Brian Hirsh

Update base for Update on "aot autograd refactor: make all synthetic base logic layered in a single location"

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.




[ghstack-poisoned]

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[5f37c4e70c...](https://github.com/cockroachdb/cockroach/commit/5f37c4e70c2ad0dd196ae899188767a232e3dee4)
#### Wednesday 2023-03-08 19:28:20 by craig[bot]

Merge #95033 #97944 #98119

95033: storage,colfetcher: implement local fast-path for COL_BATCH_RESPONSE r=yuzefovich a=yuzefovich

This commit implements the local fast-path for the COL_BATCH_RESPONSE
scan format. The idea is that if a Scan request is evaluated locally
(i.e. on the same node for single-tenant deployments or within the
shared process for multi-tenant deployments), then we can avoid
the redundant serialization of the columnar batches in the Apache
Arrow format and just pass the batches as a slice of pointers through
the protobuf. Additionally, this also allows us to avoid a copy of the
data from `ScanResponse.BatchResponse` into the columnar batch.

To achieve this the ScanResponses and the ReverseScanResponses now
contain a new custom `ColBatches` message which only includes
`[]coldata.Batch` that is not marshalled as part of the protobuf
serialization.

Now that we can have a single multi-range request result in locally- and
remotely-executed single-range requests, we need to be careful when
combining them. In particular, in order to preserve the ordering between
single-range requests we now always deserialize the remotely-executed
ones (since this "combining" happens on the KV client side and won't be
sent over the wire again) while "merging" them accordingly. This
required introduction of an injected helper for the deserialization from
the Apache Arrow format into the `kvpb` package. This deserialization
also required that we have access to the `fetchpb.IndexFetchSpec` proto
that is stored in the BatchRequest, thus, the signature of `combine`
method has been adjusted to include the reference to the BatchRequest.

Additional quirk of this commit is that the `cFetcher` cannot reuse the
same batch when it is used by the `cFetcherWrapper` when skipping the
serialization. (If it did reuse batches, then the slice of batches would
contain multiple references to the same batch, so only the last reference
would be correct - all previous ones would have been reset.) To do that
the `colmem.SetAccountingHelper` has been adjusted to be able to keep
the same heuristic when it comes to the sizing of the batch while always
allocating a new one, even if under other circumstances it would have
reused the old batch.

It's also worth noting the story about memory accounting of these local
batches. The `SetAccountingHelper` used by the `cFetcher` always tracks
the memory usage only of the last batch, so we need to account for all
other batches ourselves. We go around this by providing the `cFetcher`
with a "detached" memory account (i.e. an account that is not connected
to the memory accounting system) that is used by the `cFetcher` to limit
the batch size based on the footprint, and modifying the
`cFetcherWrapper` to perform the accounting against the proper memory
account. This commit also clarifies the contract of
`CFetcherWrapper.NextBatch` that it is the wrapper's responsibility to
perform memory accounting of all batches, regardless of the return
format, against the provided memory account.

This only covers part of the story from the KV server side. On the KV
client side the memory accounting is done in `txnKVFetcher`. When the
batches are serialized, they are included in
`ScanResponse.BatchResponse` field and, thus, are included into
`BatchResponse.Size` which we use for accounting. For the non-serialized
batches this commit implements the custom `Size()` method so that the
true footprint of all `coldata.Batch`es is included into
`BatchResponse.Size`. As a result, all local batches (including the ones
that were deserialized when combining responses to locally- and
remotely-executed requests) are tracked by the `txnKVFetcher` until a
new `BatchRequest` is issued, so the ColBatchDirectScan doesn't need to
perform the accounting. (Note that we perform the accounting for
`ScanResponse.BatchResponse` slices in a similar manner - we don't
shrink the memory account when a single response becomes garbage (due
to likely under-accounting in other places).)

A special note on type schemas with enums: since enums require type
hydration that is not easily available on the KV server side and we
treat them simply as bytes values, the presence of enums forces us to
serialize the batches even for locally-executed requests. This seems
like a minor limitation in comparison to not supporting enums at all.

Another note on the datum-backed vectors: since the `cFetcherWrapper`
also doesn't have access to a valid `eval.Context`, the datum-backed
vectors produced by the wrapper are "incomplete". Previously, since we
always serialized the batches, it wasn't an issue. However, now if we
get a non-serialized batch from the locally-executed request, we must
update all datum-backed vectors with the proper eval context. This is
done by the `ColBatchDirectScan`.

The microbenchmarks of this change when the direct columnar scans are
always enabled are [here](https://gist.github.com/yuzefovich/a9b28669f35ff658b2e89ed7b1d43e38).
Note that there are three distinct operation modes in that gist:
- `Cockroach` and `MultinodeCockroach` - single-tenant deployments
- `SharedProcessTenant` - this is how we imagine that dedicated clusters
will run once the Unified Architecture is achieved
- `SepProcessTenant` - this is how we run Serverless.

For the first two this commit results mostly in a minor improvement in
latency and sometimes noticeable reducation in allocations, as expected.
SepProcessTenant config - which cannot take advantage of the local
fastpath - sees a minor slowdown in latency and no changes in
allocations, as expected (I'm attributing this to increased overhead of
the direct columnar scans and increased size of `ScanResponse` objects).

However, these are micro-benchmarks, and they don't show the full
picture. In particular, they don't process enough data and often select
all columns in the table for this feature to show its benefits. I'm more
excited about the results on the TPC-H queries. Here is the impact of
this commit on 3 node cluster running in single-tenant model (averaged
over 10 runs):
```
Q1:	before: 4.46s	after: 4.23s	 -5.15%
Q2:	before: 3.18s	after: 3.30s	 3.45%
Q3:	before: 2.43s	after: 2.11s	 -13.20%
Q4:	before: 1.83s	after: 1.84s	 0.44%
Q5:	before: 2.65s	after: 2.48s	 -6.34%
Q6:	before: 7.59s	after: 7.46s	 -1.65%
Q7:	before: 5.56s	after: 5.72s	 2.71%
Q8:	before: 1.14s	after: 1.11s	 -2.29%
Q9:	before: 5.77s	after: 5.31s	 -7.86%
Q10:	before: 1.98s	after: 1.94s	 -1.92%
Q11:	before: 0.73s	after: 0.69s	 -5.52%
Q12:	before: 7.18s	after: 6.91s	 -3.79%
Q13:	before: 1.24s	after: 1.24s	 0.16%
Q14:	before: 0.70s	after: 0.66s	 -5.32%
Q15:	before: 3.99s	after: 3.64s	 -8.89%
Q16:	before: 0.95s	after: 0.94s	 -1.16%
Q17:	before: 0.27s	after: 0.26s	 -5.49%
Q18:	before: 2.67s	after: 2.15s	 -19.39%
Q19:	before: 4.03s	after: 2.96s	 -26.46%
Q20:	before: 12.91s	after: 11.49s	 -10.98%
Q21:	before: 7.14s	after: 6.99s	 -2.13%
Q22:	before: 0.60s	after: 0.57s	 -5.48%
```

Furthermore, here is the comparison of the direct columnar scans
disabled vs enabled:
```
Q1:	before: 4.36s	after: 4.23s	 -2.91%
Q2:	before: 3.57s	after: 3.30s	 -7.63%
Q3:	before: 2.31s	after: 2.11s	 -8.61%
Q4:	before: 1.88s	after: 1.84s	 -2.07%
Q5:	before: 2.55s	after: 2.48s	 -2.70%
Q6:	before: 7.94s	after: 7.46s	 -6.04%
Q7:	before: 5.87s	after: 5.72s	 -2.61%
Q8:	before: 1.12s	after: 1.11s	 -1.07%
Q9:	before: 5.79s	after: 5.31s	 -8.27%
Q10:	before: 1.97s	after: 1.94s	 -1.47%
Q11:	before: 0.69s	after: 0.69s	 -0.29%
Q12:	before: 6.99s	after: 6.91s	 -1.16%
Q13:	before: 1.24s	after: 1.24s	 -0.48%
Q14:	before: 0.68s	after: 0.66s	 -3.37%
Q15:	before: 3.72s	after: 3.64s	 -2.23%
Q16:	before: 0.96s	after: 0.94s	 -1.88%
Q17:	before: 0.28s	after: 0.26s	 -6.18%
Q18:	before: 2.47s	after: 2.15s	 -12.87%
Q19:	before: 3.20s	after: 2.96s	 -7.35%
Q20:	before: 11.71s	after: 11.49s	 -1.88%
Q21:	before: 7.00s	after: 6.99s	 -0.06%
Q22:	before: 0.58s	after: 0.57s	 -2.07%
```
In other words, on TPC-H queries it is now already beneficial to
enable the direct columnar scans in single-tenant world (and I think
there are more minor optimizations ahead). For reference, [here](https://gist.github.com/yuzefovich/0afce5c0692713cf28712f076bab415b)
is the comparison of direct columnar scans disabled vs enabled on this
commit. It also shows that we're not that far off from reaching the
performance parity in micro-benchmarks.

Addresses: #82323.
Informs: #87610.

Epic: CRDB-14837

Release note: None

97944: build: no longer stamp by default for dev scenarios r=healthy-pod a=rickystewart

No longer require stamping for dev builds.

We still turn on stamping for `--cross` builds. This could be refined
further: for example, we don't *always* need to stamp, we need to just
stamp when we are actually building `cockroach`. For now I have not
touched this but we could make stamping even less common in this way.

This change makes unit tests more cacheable by Bazel and speeds up
many builds as we don't have to shell out to `git` for stamping.

Epic: none
Release note: None
`@rickystewart`


98119: sql/pgwire: add test for portal bug r=rafiss a=ZhouXing19

informs #98118

In PG, a portal created (via the bind stmt) before the update statement gives the value before update when it's executed. But cockroach's one gives the updated value. This is because the underlying statement is planned and run only when the portal is executed, not when it's declared.

This commit is to add this bug to the existing test.

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>
Co-authored-by: Ricky Stewart <rickybstewart@gmail.com>
Co-authored-by: Jane Xing <zhouxing@uchicago.edu>

---
## [DarviL82/Lanat](https://github.com/DarviL82/Lanat)@[30ff27f77e...](https://github.com/DarviL82/Lanat/commit/30ff27f77e0dc5a0ee5a53b0ad9f1cefa80b70d6)
#### Wednesday 2023-03-08 19:36:40 by David Losantos

Merge pull request #1 from DarviL82/feature/mirror

Fuck you use my lib

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[6f1b1717a7...](https://github.com/Nanu308/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Wednesday 2023-03-08 19:45:22 by TotalEpicness

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
## [Jul-Jul/Citadel-Station-13-RP](https://github.com/Jul-Jul/Citadel-Station-13-RP)@[81c1229373...](https://github.com/Jul-Jul/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Wednesday 2023-03-08 20:07:32 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [TooAngel/screeps](https://github.com/TooAngel/screeps)@[cc357a7986...](https://github.com/TooAngel/screeps/commit/cc357a7986ab91b69f9289b20ff9eb0fc3504327)
#### Wednesday 2023-03-08 20:57:14 by Tobias Wilken

End of an epoch, friendly TooAngel NPC died

It is a sad day in the screeps multiverse. The friendly TooAngel NPC from the neighborhood died.
Since the official release of the game it was spending joy, some action via quests and helped improving defenses, while it was just trying to survive somehow for years.
Rest in peace friendly TooAngel NPC.

Some cleanup as condolences:
- Improve code quality
- Extract pixel generation
- Improve on reservations
- Reenable boost config
- Fix issues on mineral handling
- Split up quests in host and player
- Include attacked creeps in the reputation
- Start with autorespawner

---
## [ambujgrg/Health-Care](https://github.com/ambujgrg/Health-Care)@[90694b7d97...](https://github.com/ambujgrg/Health-Care/commit/90694b7d97d7c3d81703380639b065cd50b5a792)
#### Wednesday 2023-03-08 21:09:23 by AMBUJ  GARG

Add files via upload

Congratulations – you have been hired as Chief Data Scientist of MedCamp – a not for profit organization dedicated in making health conditions for working professionals better. MedCamp was started because the founders saw their family suffer due to bad work life balance and neglected health.

MedCamp organizes health camps in several cities with low work life balance. They reach out to working people and ask them to register for these health camps. For those who attend, MedCamp provides them facility to undergo health checks or increase awareness by visiting various stalls (depending on the format of camp).

MedCamp has conducted 65 such events over a period of 4 years and they see a high drop off between “Registration” and Number of people taking tests at the Camps. In last 4 years, they have stored data of ~110,000 registrations they have done.

One of the huge costs in arranging these camps is the amount of inventory you need to carry. If you carry more than required inventory, you incur unnecessarily high costs. On the other hand, if you carry less than required inventory for conducting these medical checks, people end up having bad experience.

The Process:
MedCamp employees / volunteers reach out to people and drive registrations.
During the camp, People who “ShowUp” either undergo the medical tests or visit stalls depending on the format of health camp.
Other things to note:
Since this is a completely voluntary activity for the working professionals, MedCamp usually has little profile information about these people.
For a few camps, there was hardware failure, so some information about date and time of registration is lost.
MedCamp runs 3 formats of these camps. The first and second format provides people with an instantaneous health score. The third format provides information about several health issues through various awareness stalls.
Favorable outcome:
For the first 2 formats, a favourable outcome is defined as getting a health_score, while in the third format it is defined as visiting at least a stall.
You need to predict the chances (probability) of having a favourable outcome

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[f30f15a58c...](https://github.com/shiptest-ss13/Shiptest/commit/f30f15a58c236c630f8d2bafd224f58625728f6b)
#### Wednesday 2023-03-08 21:45:57 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
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
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[7cc6934eff...](https://github.com/Donglesplonge/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Wednesday 2023-03-08 22:00:23 by LemonInTheDark

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
## [acald-creator/next.js](https://github.com/acald-creator/next.js)@[268dd6e80b...](https://github.com/acald-creator/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Wednesday 2023-03-08 22:06:27 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [enchanted-coder/php-chatapp](https://github.com/enchanted-coder/php-chatapp)@[29dbb3e0b3...](https://github.com/enchanted-coder/php-chatapp/commit/29dbb3e0b34613d6815d574b82f12a7a5ae7fba4)
#### Wednesday 2023-03-08 22:54:42 by enchanted-coder

so i just fucking remembered why i hate oop php
im not using pdo
why the fuck
naah.
im doing precedural
rewriting this whole damn project again.
maybe i should get a readme and not delete next time

---
## [hyperlane-xyz/hyperlane-monorepo](https://github.com/hyperlane-xyz/hyperlane-monorepo)@[59a90b1bb6...](https://github.com/hyperlane-xyz/hyperlane-monorepo/commit/59a90b1bb63106d9dd7fa640b17772096073dfb8)
#### Wednesday 2023-03-08 23:28:57 by Trevor Porter

Default to not allowing LocalStorage checkpoint syncers in relayer (#1900)

### Description

Open to better names

Adds a setting to the relayer, `allow_local_checkpoint_syncers`, which
determines whether local storage based checkpoint syncers will be
allowed by the metadata builder.

Originally, I wanted something a bit more clever, like being able to
specify `HYP_RELAYER_VALIDCHECKPOINTSYNCERS=LocalStorage,S3` or
something, where I'd like those variants to be matched to the variants
found in
https://github.com/hyperlane-xyz/hyperlane-monorepo/blob/main/rust/hyperlane-base/src/types/checkpoint_syncer.rs#L14.
But that enum requires values, so things get ugly. One option would be
to create a new enum like:
```
enum CheckpointSyncerTypes {
  LocalStorage,
  S3,
}
```
And another option is to use something like strum's
[EnumString](https://docs.rs/strum/latest/strum/derive.EnumString.html)
(shoutout to @mattiecnvr). But this still is a bit clunky, so for now
just making this a bool and we can figure out something more elegant
later if we ever get to a point where we're supporting multiple types of
checkpoint syncers

### Drive-by changes

none

### Related issues

- Fixes https://github.com/hyperlane-xyz/issues/issues/402

### Backward compatibility

_Are these changes backward compatible?_

Yes - although if you ever want to run a relayer that uses local storage
now, you'll need to set `HYP_RELAYER_ALLOWLOCALCHECKPOINTSYNCERS=true`

_Are there any infrastructure implications, e.g. changes that would
prohibit deploying older commits using this infra tooling?_

None - we always expect to not be reading from the local fs in deployed
relayers


### Testing

_What kind of testing have these changes undergone?_

Ran e2e tests

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[83275d8cdf...](https://github.com/pytorch/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Wednesday 2023-03-08 23:46:34 by Brian Hirsh

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

