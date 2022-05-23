## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-22](docs/good-messages/2022/2022-05-22.md)


1,554,475 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,554,475 were push events containing 2,235,792 commit messages that amount to 113,984,986 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [Clanzion/Naruto_Ninpou](https://github.com/Clanzion/Naruto_Ninpou)@[80cd503e06...](https://github.com/Clanzion/Naruto_Ninpou/commit/80cd503e06b6da03cbec977535c84e603ab9b6ee)
#### Sunday 2022-05-22 00:05:20 by MetalfOxXer

changes

- Reduced Roshi lava mode slow to 10%
- Fixed Hidan R not reflecting damage properly
- Fixed some descriptions
- Fixed Dark Totsuka life steal not working
- Fixed Fuu Yamanaka semi
- Rock Lee W doesn't push creeps anymore / Fixed sfx effect not moving with him
- Itachi additional heal on his D removed
- Return damage from Juubi Skin from Book of Gelel reduced by 50%
- Kid Gaara Q damage type changed from Magic to Normal
- Tenten's R is now slightly slower again
- Improved Torune's T animation slightly maybe
- Rikudou Naruto W from 50x HP and 25x Mana to 75x HP and 50x Mana

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c10930cba3...](https://github.com/treckstar/yolo-octo-hipster/commit/c10930cba3591dd2ca8b810689f73d02f9360f1a)
#### Sunday 2022-05-22 00:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[20e4add487...](https://github.com/Shadow-Quill/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Sunday 2022-05-22 00:29:53 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [gitster/git](https://github.com/gitster/git)@[07564773c2...](https://github.com/gitster/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Sunday 2022-05-22 00:35:00 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [S34NW/Paradise](https://github.com/S34NW/Paradise)@[ab7a358506...](https://github.com/S34NW/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Sunday 2022-05-22 01:05:26 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [STJr/Kart-Public](https://github.com/STJr/Kart-Public)@[8f354ad9c1...](https://github.com/STJr/Kart-Public/commit/8f354ad9c1b3026f7239f0b5184992d802c315eb)
#### Sunday 2022-05-22 01:28:07 by Eidolon

Implement Uncapped (squashed)

Co-Authored-By: Sally Coolatta <tehrealsalt@gmail.com>
Co-Authored-By: James R <justsomejames2@gmail.com>
Co-Authored-By: Monster Iestyn <iestynjealous@ntlworld.com>
Co-Authored-By: katsy <katmint@live.com>

Place Frame Interpolation in "Experimental" video options header

This seems like an appropriate way to describe the feature for now.

Add smooth level platter under interpolation, `renderdeltatics`

`renderdeltatics` can be used as a standard delta time in any place,
allowing for smooth menus. It will always be equal to `realtics`
when frame interpolation is turned off, producing consistent
framerate behavior everywhere it is used.

Add smooth rendering to save select screen

Add smooth rendering to Record/NiGHTS Attack, F_SkyScroll

Ensure viewsector is accurate to viewx/viewy

This fixes a potential crash in OpenGL when changing between levels.

Ensure + commands get executed before map start

Always have precise_t defined

Fix misc dropshadow issues

Reset view interpolation on level load

Remove unnecessary precipmobj thinker hack

Add reset interpolation state functions

Reset precip interpolation on snap to ceil

Reset mobj interp state on TeleportMove

Only swap view interp state if a tick is run

Run anti-lag chasecam at tic frequency

Fixes jittery and unstable chasecam in high latency netgames

Homogenize mobj interpolations

Add sector plane level interpolations

Add SectorScroll interpolator

Add SideScroll interpolator

Add Polyobj interpolator

Intialize interpolator list at a better time

Delete interpolators associated with thinkers

Interpolate mobj angles and player drawangle

Interpolate HWR_DrawModel

Add functions to handle interpolation

Much less code duplication

P_InitAngle, to fix angle interpolation on spawning objects

Fully fix drop shadows

It used the thing's floorz / ceilingz directly -- that wouldn't account for interpolated coordinates.

Do not speed up underwater/heatwave effect in OpenGL

Closer OpenGL underwater/heatwave effect to Software

Interpolate from time of previous tic

Previously interpolated from last 35th of a second, which
may be offset from game time due to connection lag.

Consider this the proper fix to 54148a0dd0 too.

Calculate FPS stuff even if frame is skipped

I decided ultimately to actually keep the frame skip optimization disabled, because I think it is actually a little bit helpful that you can still get accurate rendering perfstats while paused, however if we decide otherwise then we can have this optimization back without making the game act like it's lagging.

Keep rect in memory

Feel better about this than creating one all da time

Lots of FPS stuff

- Disabled VSync, due to the numerous problems it has.
- Instead, added an FPS cap.
- Frame interpolation is now tied to fpscap != 35.
- By default, the FPS cap is set to the monitor's refresh rate.
- Rewrote the FPS counter.

(This also consolidates several more commits ahead of this
fixing various issues. -eid)

Misc changes after Kart cherry-picks

Fix renderdeltatics with new timing data

Update mobj oldstates before all thinkers

Allow FPS cap values

Adjust how FPS cap is checked to improve FPS stability

Fix precip crash from missing vars

Improve the framerate limiter's timing for extreme stable FPS

Handle the sleep at the end of D_SRB2Loop instead of the start

Simplifies logic in the other parts of the loop, and fixes problems with it frequently waiting too long.

Reset mobj interp state on add

Add mobj interpolator on load netgame

Move mobj interpolators to r_fps

Dynamic slope interpolators

I_GetFrameTime to try and improve frame pace

(It doesn't feel that much better though.)

Move I_FinishUpdate to D_SRB2Loop to sync screen updates with FPS cap, use timestamps in I_FrameCapSleep to simplify the code

Fix plane interpolation light level flickering

Fix flickering plane interpolation for OpenGL in the exact same way

Funny OpenGL renderer being at least 50% copy-pasted Software code :)

P_SetOrigin & P_MoveOrigin to replace P_TeleportMove

Convert P_TeleportMove use to origin funcs

Revert "P_InitAngle, to fix angle interpolation on spawning objects"

This reverts commit a80c98bd164a2748cbbfad9027b34601185d93f5.

Waypoint polyobjects interpolate z & children

Add interpolation to more moving plane types

Adds interpolation to the following:
- Crumbling platforms
- Mario blocks
- Floatbob platforms (this one works really strangely due to two thinkers, maybe double-check this one?)

Reset overlays interp states each TryRunTics

Interpolate model interpolation (lol)

Use interp tracer pos for GL linkdraw

Papersprite angle interpolation

Makes the ending signpost smooth

Move intermission emerald bounce to ticker

Bring back shadows on polyobjects

Also optimizes the method used so rings can show their shadows too. Using just the subsector is a tad bit imprecise admittedly but any more precise methods get really laggy.

Fix a bunch of ticking in hu_ drawing functions

Revert "Reset overlays interp states each TryRunTics"

This reverts commit a71a216faa20e8751b3bd0157354e8d748940c92.

Move intro ticking out of the drawer

Adjust 1up monitor icon z offsets

Fixes interpolation issues with 1up monitors.

Delta time choose player menu animations

Add drawerlib deltaTime function

Interpolate afterimages further back

Use old sleep in dedicated mode

Clamp cechotimer to 0

Fixes issues with cechos staying on-screen and glitching out
(NiGHTS items for example).

Revert "Remove unnecessary precipmobj thinker hack"

This reverts commit 0e38208620d19ec2ab690740438ac2fc7862a49e.

Fix frame pacing when game lags behind

The frame timestamp should've been made at the start of the frame, not the end.

Fix I_FrameCapSleep not respecting cpusleep

Jonathan Joestar bruh

Allow dedicated to use precise sleep timing again

Instead of only using one old sleep, just enforce framerate cap to match TICRATE.

Make Lua TeleportMove call MoveOrigin

Reset Metal fume interp state on appear

Add interpdebug

Put interpdebug stuff in perfstats instead

Add timescale cvar

Slow the game down to debug animations / interpolation problems! Speed it up if you need to get somewhere quickly while mapping!

Enable timescale outside of DEVELOP builds

It has NETVAR, so it should be fine -- put an end to useful debugging features excluded in multiplayer!

Force interpolation when timescale != 1.0

Reset old_z in MT_LOCKON think

Fixes interpolation artifacting due to spawn pos.

Fix cutscenes in interp

Fix boss1 laser in interp

Interpolate mobj scale

Precalculate refresh rate

Slower PCs can have issue querying mode over and over. This might kinda suck for windowed mode if you have different refresh rate displays but oh well

Fix interp scaling crashing software

Reset interp scale when Lua sets .scale

Disable angle interp on fresh mobjs

Fix interp scale crash for hires sprites

Interp shadow scales

Copy interp state in P_SpawnMobjFromMobj

Fix multiplayer character select

Don't interpolate mobj state if frac = 1.0

Fix Mario block item placement

Interpolate spritescale/offset x/y

Fix offset copies for SpawnMobjFromMobj

THANKS SAL

Add Lua HUD drawlists

Buffers draw calls between tics to ensure hooks
run at the originally intended rate.

Rename drawerlib deltaTime to getDeltaTime

Make renderisnewtic is false between tics

I know what I'm doing! I swear

Completely refactor timing system

Time is now tracked internally in the game using I_GetPreciseTime
and I_UpdateTime. I_Time now pulls from this internal timer. The
system code no longer needs to keep track of time itself.

This significantly improves frame and tic timing in interp mode,
resulting in a much smoother image with essentially no judder at
any framerate.

Ensure mobj interpolators reset on level load

Ensure view is not interpolated on first frame

Disable sprite offset interpolation (for now)

Refactor timing code even more

System layer is greatly simplified and framecap
logic has been moved internally. I_Sleep now
takes a sleep duration and I_SleepDuration
generically implements a precise sleep with spin
loop.

---
## [SylvainTran/speculative-futures-project-2](https://github.com/SylvainTran/speculative-futures-project-2)@[ff36810278...](https://github.com/SylvainTran/speculative-futures-project-2/commit/ff36810278a6ad977306b4c461d78bc9f34aa8b4)
#### Sunday 2022-05-22 01:42:20 by Sylvain Tran

[KDM!] Added phaser storybook web scene context

In this version, I added phaser embeds inside flickable carousels using a handy physics-based movement library (Flickity.js). The goal was to create a bigger frame/context around the whole experience that could leverage the fragmented and extremely free-form nature of web components. It seems easier to think "outside of form" and design "form" in a web project than inside Unity. Perhaps the web can allow thinking in terms of multimedia more easily? Hopefully this is a cool interaction design! I wanted the individual game scenes to be "connected" and yet easy to move around with the mouse or touch, so that the user may feel like they're flipping the pages of an interactive storybook. I added temporary buttons in each game instance div that allows transitioning to another place in the DOM where I could embed different media, like video clips of in-game scenes or other related concepts, wikipedia articles, memes, gifs, pictures, audio-only scenes, etc. The intention was to find a larger context to embed the games and all those media together so that the experience feels all "unified" and that there would be no direct explanation required to the player for talking about certain concepts given that they can just flicker back and forth behind the web pages' for context. (This beat the "Lounge" idea in my opinion, where I directly TOLD the player what to think / converse about). I also added a temporary inventory screen where I want to see if embedding little 3D objects (concrete mental objects - CBT) could feel interesting, and maybe relate them to each individual scenes by binding them together bidirectionally.

---
## [JohnTitor/rust](https://github.com/JohnTitor/rust)@[e1340f2d3c...](https://github.com/JohnTitor/rust/commit/e1340f2d3ca6827a24e5d00139b78362460330c2)
#### Sunday 2022-05-22 02:53:06 by Yuki Okushi

Rollup merge of #97144 - samziz:patch-1, r=Dylan-DPC

Fix rusty grammar in `std::error::Reporter` docs

### Commit

I initially saw "print's" instead of "prints" at the start of the doc comment for `std::error::Reporter`, while reading the docs for that type. Then I figured 'probably more where that came from', so, as well as correcting the foregoing to "prints", I've patched up these three minor solecisms (well, two [types](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction), three [tokens](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction)):

- One use of the indicative which should be subjunctive - indeed the sentence immediately following it, which mirrors its structure, _does_ use the subjunctive ([L871](https://github.com/rust-lang/rust/blob/master/library/std/src/error.rs?plain=1#L871)). Replaced with the subjunctive.
- Two separate clauses joined with commas ([L975](https://github.com/rust-lang/rust/blob/master/library/std/src/error.rs?plain=1#L975), [L1023](https://github.com/rust-lang/rust/blob/master/library/std/src/error.rs?plain=1#L1023)). Replaced the first with a semicolon and the second with a period. Admittedly those judgements are pretty much 100% subjective, based on my sense of how the sentences flowed into each other (though ofc the _replacement of the comma itself_ is not subjective or opinion-based).

I know this is silly and finicky, but I hope it helps tidy up the docs a bit for future readers!

### PR notes

**This is very much non-urgent (and, honestly, non-important).** I just figured it might be a nice quality-of-life improvement and bit of tidying up for the core contributors themselves not to have to do. 🙂

I'm tagging Steve, per the [contributing guidelines](https://rustc-dev-guide.rust-lang.org/contributing.html#r) ("Steve usually reviews documentation changes. So if you were to make a documentation change, add `r? `@steveklabnik`"):`

r? `@steveklabnik`

---
## [FreshROMs/android_kernel_samsung_exynos9610_mint](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint)@[1f2902f141...](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint/commit/1f2902f14163586dfe617771b49a45bf9f90b2d5)
#### Sunday 2022-05-22 03:13:42 by Alexander Potapenko

BACKPORT: mm: security: introduce init_on_alloc=1 and init_on_free=1 boot options

Upstream commit 6471384af2a6530696fc0203bafe4de41a23c9ef.

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

Removed the drivers/infiniband/core/uverbs_ioctl.c part, which is not in
android-common 4.14 kernel.

Change-Id: I6b5482fcafae89615e1d79879191fb6ce50d56cf
Bug: 138435492
Test: Boot cuttlefish with and without
Test:   CONFIG_INIT_ON_ALLOC_DEFAULT_ON/CONFIG_INIT_ON_FREE_DEFAULT_ON
Test: Boot an ARM64 mobile device with and without
Test:   CONFIG_INIT_ON_ALLOC_DEFAULT_ON/CONFIG_INIT_ON_FREE_DEFAULT_ON
Signed-off-by: Alexander Potapenko <glider@google.com>
Signed-off-by: John Vincent <git@tenseventyseven.cf>

---
## [SweetBlueSylveon/Shiptest](https://github.com/SweetBlueSylveon/Shiptest)@[948eca0dc8...](https://github.com/SweetBlueSylveon/Shiptest/commit/948eca0dc8e6fbf09771bf30e695ece532e91e8e)
#### Sunday 2022-05-22 03:49:25 by SweetBlueSylveon

Small fix

-Really should wait on doing this until I get a good number of the. But fuck you this github autosquashes.
-Swaps out a plating for a reinforced plating.

---
## [brootware/awesome](https://github.com/brootware/awesome)@[6f220defea...](https://github.com/brootware/awesome/commit/6f220defea1eb71a879cc7d38da81998697fe710)
#### Sunday 2022-05-22 04:03:28 by Bruce

Add Cyber security university

<!-- Congrats on creating an Awesome list! 🎉 -->

<!-- Please fill in the below placeholders -->

**https://github.com/brootware/Cyber-Security-University**

**Cyber Security University is A curated list of awesome and free educational resources that focuses on learn by doing.**

### By submitting this pull request I confirm I've read and complied with the below requirements 🖖

**Please read it multiple times. I spent a lot of time on these guidelines and most people miss a lot.**

## Requirements for your pull request

- **Don't waste my time.** Do a good job, adhere to all the guidelines, and be responsive.
- **You have to review at least 2 other [open pull requests](https://github.com/sindresorhus/awesome/pulls?q=is%3Apr+is%3Aopen).**
	Try to prioritize unreviewed PRs, but you can also add more comments to reviewed PRs. Go through the below list when reviewing. This requirement is meant to help make the Awesome project self-sustaining. Comment here which PRs you reviewed. You're expected to put a good effort into this and to be thorough. Look at previous PR reviews for inspiration. **Just commenting “looks good” or simply marking the pull request as approved does not count!** You have to actually point out mistakes or improvement suggestions.
- You have read and understood the [instructions for creating a list](https://github.com/sindresorhus/awesome/blob/main/create-list.md).
- This pull request has a title in the format `Add Name of List`.
	- ✅ `Add Swift`
	- ✅ `Add Software Architecture`
	- ❌ `Update readme.md`
	- ❌ `Add Awesome Swift`
	- ❌ `Add swift`
	- ❌ `add Swift`
	- ❌ `Adding Swift`
	- ❌ `Added Swift`
- Your entry here should include a short description about the project/theme of the list. **It should not describe the list itself.** The first character should be uppercase and the description should end in a dot. It should be an objective description and not a tagline or marketing blurb.
	- ✅ `- [iOS](…) - Mobile operating system for Apple phones and tablets.`
	- ✅ `- [Framer](…) - Prototyping interactive UI designs.`
	- ❌ `- [iOS](…) - Resources and tools for iOS development.`
	- ❌ `- [Framer](…)`
	- ❌ `- [Framer](…) - prototyping interactive UI designs`
- Your entry should be added at the bottom of the appropriate category.
- The title of your entry should be title-cased and the URL to your list should end in `#readme`.
	- Example: `- [Software Architecture](https://github.com/simskij/awesome-software-architecture#readme) - The discipline of designing and building software.`
- The suggested Awesome list complies with the below requirements.

## Requirements for your Awesome list

- **Has been around for at least 30 days.**<br>That means 30 days from either the first real commit or when it was open-sourced. Whatever is most recent.
- Don't open a Draft / WIP pull request while you work on the guidelines. A pull request should be 100% ready and should adhere to all the guidelines when you open it. **Instead use [#2242](https://github.com/sindresorhus/awesome/issues/2242) for incubation visibility**.
- Run [`awesome-lint`](https://github.com/sindresorhus/awesome-lint) on your list and fix the reported issues. If there are false-positives or things that cannot/shouldn't be fixed, please [report it](https://github.com/sindresorhus/awesome-lint/issues/new).
- The default branch should be named [`main`, not `master`](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/).
- **Includes a succinct description of the project/theme at the top of the readme.** [(Example)](https://github.com/willempienaar/awesome-quantified-self)
	- ✅ `Mobile operating system for Apple phones and tablets.`
	- ✅ `Prototyping interactive UI designs.`
	- ❌ `Resources and tools for iOS development.`
	- ❌ `Awesome Framer packages and tools.`
- It's the result of hard work and the best I could possibly produce.
	**If you have not put in considerable effort into your list, your pull request will be immediately closed.**
- The repo name of your list should be in lowercase slug format: `awesome-name-of-list`.
	- ✅ `awesome-swift`
	- ✅ `awesome-web-typography`
	- ❌ `awesome-Swift`
	- ❌ `AwesomeWebTypography`
- The heading title of your list should be in [title case](https://capitalizemytitle.com/) format: `# Awesome Name of List`.
	- ✅ `# Awesome Swift`
	- ✅ `# Awesome Web Typography`
	- ❌ `# awesome-swift`
	- ❌ `# AwesomeSwift`
- Non-generated Markdown file in a GitHub repo.
- The repo should have `awesome-list` & `awesome` as [GitHub topics](https://help.github.com/articles/about-topics). I encourage you to add more relevant topics.
- Not a duplicate. Please search for existing submissions.
- Only has awesome items. Awesome lists are curations of the best, not everything.
- Does not contain items that are unmaintained, has archived repo, deprecated, or missing docs. If you really need to include such items, they should be in a separate Markdown file.
- Includes a project logo/illustration whenever possible.
	- Either centered, fullwidth, or placed at the top-right of the readme. [(Example)](https://github.com/sindresorhus/awesome-electron)
	- The image should link to the project website or any relevant website.
	- **The image should be high-DPI.** Set it to maximum half the width of the original image.
- Entries have a description, unless the title is descriptive enough by itself. It rarely is though.
- Includes the [Awesome badge](https://github.com/sindresorhus/awesome/blob/main/awesome.md#awesome-badge).
	- Should be placed on the right side of the readme heading.
		- Can be placed centered if the list has a centered graphics header.
	- Should link back to this list.
- Has a Table of Contents section.
	- Should be named `Contents`, not `Table of Contents`.
	- Should be the first section in the list.
	- Should only have one level of [nested lists](https://commonmark.org/help/tutorial/10-nestedLists.html), preferably none.
	- Must not feature `Contributing` or `Footnotes` sections.
- Has an appropriate license.
	- **We strongly recommend the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/), but any [Creative Commons license](https://creativecommons.org/choose/) will work.**
		- Tip: You can quickly add it to your repo by going to this URL: `https://github.com/<user>/<repo>/community/license/new?branch=main&template=cc0-1.0` (replace `<user>` and `<repo>` accordingly).
	- A code license like MIT, BSD, Apache, GPL, etc, is not acceptable. Neither are WTFPL and [Unlicense](https://unlicense.org).
	- Place a file named `license` or `LICENSE` in the repo root with the license text.
	- **Do not** add the license name, text, or a `Licence` section to the readme. GitHub already shows the license name and link to the full text at the top of the repo.
	- To verify that you've read all the guidelines, please comment on your pull request with just the word `unicorn`.
- Has [contribution guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md#include-contribution-guidelines).
	- The file should be named `contributing.md`. Casing is up to you.
	- It can optionally be linked from the readme in a dedicated section titled `Contributing`, positioned at the top or bottom of the main content.
	- The section should not appear in the Table of Contents.
- All non-important but necessary content (like extra copyright notices, hyperlinks to sources, pointers to expansive content, etc) should be grouped in a `Footnotes` section at the bottom of the readme. The section should not be present in the Table of Contents.
- Has consistent formatting and proper spelling/grammar.
	- The link and description are separated by a dash. <br>Example: `- [AVA](…) - JavaScript test runner.`
	- The description starts with an uppercase character and ends with a period.
	- Consistent and correct naming. For example, `Node.js`, not `NodeJS` or `node.js`.
- Doesn't use [hard-wrapping](https://stackoverflow.com/questions/319925/difference-between-hard-wrap-and-soft-wrap).
- Doesn't include a Travis badge.<br>You can still use Travis for list linting, but the badge has no value in the readme.
- Doesn't include an `Inspired by awesome-foo` or `Inspired by the Awesome project` kinda link at the top of the readme. The Awesome badge is enough.

**Go to the top and read it again.**

---
## [1allan/INE5413](https://github.com/1allan/INE5413)@[6456e9d646...](https://github.com/1allan/INE5413/commit/6456e9d646170caae6f7fde50b874ada4eb1ea35)
#### Sunday 2022-05-22 06:16:52 by Allan Soares Silva

(A1): corrige os métodos grau e vizinhos

GOD I FUCKING HATE PYTHON MODULE SYSTEM

---
## [openhab/org.openhab.binding.zwave](https://github.com/openhab/org.openhab.binding.zwave)@[7e710866ea...](https://github.com/openhab/org.openhab.binding.zwave/commit/7e710866ea8041a7e80b60d8b72a0534a5e89a6e)
#### Sunday 2022-05-22 06:18:22 by Robert Eckhoff

Zwave battery device optimization (#1760)

* “One and DONE” - Zwave battery device optimization

This PR is to optimize the user experience of initializing new Zwave battery devices. The desired result is to be able to put a battery in the shiny new device, follow the device manual inclusion protocol during an Inbox, Zwave binding “Scan” mode of OpenHab and, in 20 seconds or less, have all the channels displayed and begin to link them to items. “One and DONE”.
Since my last unmerged battery device PRs I have replaced the fixed 20 second cap in the iterative sleep timer with a user defined maximum “hold awake” parameter. As the user defined default is five seconds, there is no implied maintainer approval of a longer awake duration. Kind of a “use at your own risk” feature. Once the device is DONE (or the cap is reached) the sleep message (No More Information-NMI) is created. Setting a higher user defined cap does not mean increased battery usage. With half second intervals, versus 5 seconds in today’s binding, daily battery device awake duration is either the same or reduced.
Also added is a kick-Queue action after the half second mark in the Timer Task to get a potentially “stuck” device queue going again. In some scenarios (primarily during initialization, the existing kick-Queue action appears to happen too early (before the event listener sets the device awake). There are examples from the forum in my attached document. I was able to recreate the “stuck” scenario (by reverting the second “Add Node Stop” & Sleep Timer cap to 5 seconds) and resolve the “stuck” problem on my test device with this additional kick-Queue.
Lastly, I have added the shortened timeout for the second calling of the “Add Node Stop” to make this a complete package. It has the most impact as anything else to “One and DONE”. The default 5 seconds to cancel this command eats up about 4 seconds of the Timer leaving only one second left in the initial awake interval. Some of the other enhancements in this PR would have less impact, if a full 5 seconds were available for device initialization after device discovery.
I have all the changes in this PR running, some for as long as 8 months (as of Jan 2022). I have 13 battery nodes of various manufacturers (47 total) on an Rpi4 with an Rpi3b test system. It is frustrating to see the battery device initialization issues in the forum, as I know they can be resolved better than the standard “reawake many, many times” advice. These changes will save considerable user frustration and many seconds of battery usage.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Requested Changes mostly

We still need to discuss my appeal on the AddNode Stop and get on the same page on how the count works.  It is not the same as in #1100 with the "return;"
Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Delete AddNode changes

Mainly delete the changes in the Addnode class, plus address other minor changes

Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Update README with maxAwakePeriod

Added section of maxAwakePeriod in the README, added a missing line, commented on the kickQueue.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Update maxAwake without initialization and xml edits

Your suggestion led me to realize I could “push” the maxAwakePeriod from the ZWaveControllerHandler configuration editor down to the ZwaveController where it could be “pulled” by the Zwave Node. It’s not exactly how you suggested, but I wanted to make the smallest possible amount of changes, so as to not mess up the other parameters. Not a lot of testing, but I could change in the UI and check in the wake Timer Task that it was being used.  It also still could be changed via re-initialization using the UI page “code” tab, so I think it is good.
Also in the commit I changed the default maxAwakePeriod to 10 seconds and raised the minimum back to 5. With the AddNode changes removed (adding 4 seconds of inactivity), the minimum of 2 seconds will simply not work. As to the default, I detailed 2 tests at 5 seconds and two at 10 seconds and summarized them below

Node	Max Awake	# of awakes to DONE	Total User time Fiddling with Action button	Total Device Awake (inludes late starts, message timeouts)
2	5 seconds	6	6 minutes 40 seconds	22.7 seconds
3	5	4	2 minutes 40 seconds	24.1 seconds
4	10	1	6.5 seconds (estimated-zniffer)	6.5 seconds
6	10	1	 8 seconds	8 seconds

Once a partially initialized device needs to reawake, it is not seamless and a 10 second cap uses less battery time than a 5 second cap. Also this was me pressing the button and checking the device in the UI and I knew to keep at it.  Not everyone understands the need to keep pressing the action button with high frequency.  I would be a little sad that after all the work here, the default settings would only be slightly better than now. Yes, the parameter is now easy to change, but that is an extra step and is currently an advanced setting. I’d strongly prefer we start at 10 seconds and let people lower it if they think it is a problem (although my data proves it is not).
I also made some edits to the program comments, the JavaDocs and took out an unused method.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Attempt to fix .classpath& .project

Per my last comment these are autogenerated and should not be changed.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Move single use variable to where it is used?

I hope this is what you were looking for.  It's late on this side of the world, but though I would try to fix now.  If wrong, let me know and I will fix in AM.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Remove unneeded variable

I was also wondering if this was needed, but once I got it working did not want to mess with it !  Anyway it is gone now.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Change passed variable to int

This has worked for a few days, but it seems maxAwakeProperty should be int, not Integer.  I was converted to int in the Controller Handler. If not right I can revert..
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

---
## [PKRoma/git-for-windows](https://github.com/PKRoma/git-for-windows)@[bdaf1dfae7...](https://github.com/PKRoma/git-for-windows/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Sunday 2022-05-22 06:20:36 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [sumeetchhetri/zookeeper-cpp-client](https://github.com/sumeetchhetri/zookeeper-cpp-client)@[86970ac9c4...](https://github.com/sumeetchhetri/zookeeper-cpp-client/commit/86970ac9c4897defc3cf70bd643442416946402f)
#### Sunday 2022-05-22 06:43:30 by Travis Gockel

Adds TravisCI support for issue #26.

Holy fuck I hate Google Test Framework's stupid fucking packaging on Ubuntu. JUST BUILD A FUCKING LIBRARY YOU FUCKS.
LIKE EVERY OTHER FUCKING LIBRARY IN THE HISTORY OF FOREVER.

---
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[6755bddb67...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/6755bddb670ac14051453a47e9bfd4c217d8c175)
#### Sunday 2022-05-22 07:02:27 by Miklos Szeles

McMuck: Fianlly, we are ready. We will lose our contract if we do not deliver on time.
Miki: We do not have a contract with Hashnode, McMuck.
McMuck: What???? No contract? Then why the hell you are doing this?
Miki: For fun, McMuck. For fun.

Minnie: So we are really ready?
Miki: Nope. We have a few things to do.
Nikolai: Like what?
Miki: We have to reread it, consider 150 change suggestions coming from Good Old Mother Grammarly Premium and we should create the cover image and we also have to add the call to action section.
Nikolai: Are you really putting additional hours into this garbage?
Miki: Well, it might be a garbage, but you can find hidden gems even in the garbage.
McMuck: Yeah, I remember when you threw your Ledger Nano into the garbage by which you lost more than 10 bitcoins.
Miki: It wasn't me. I spent my more than 10 bitcoins on Team Fortress 2 keys.
McMuck: 😱😱😱😱😱

---
## [diesel-rs/diesel](https://github.com/diesel-rs/diesel)@[448df6b615...](https://github.com/diesel-rs/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Sunday 2022-05-22 08:08:20 by Georg Semmler

Address #3173

This is a tricky one. It seems like the behaviour described in that
issue should work out of the box, but it doesn't. I've spend some time
to investigate various solutions to make this work, but I came to the
conclusion that the current behaviour is the correct one.

The underlying issue here is that such an query promotes the inner
`Nullable<_>` of the field onto the outer `Queryable` wrapper. Without
`Selectable` that would require a select clause like
`.select((table::column.assume_not_null(),).nullable())`. This is
technically a safe pattern, but requires the usage of the "advanced"
`assume_not_null()` method to forcibly convert types to their not null representation.

Possible solutions tried to make the enable constructs shown in that
issue:

* I've tried to make the `impl Selectable for Option<T>` return the
following `SelectExpression`:
`dsl::Nullable<dsl::AssumeNotNull<T::SelectExpression>>`
where `AssumeNotNull` converts each tuple element to the corresponding
not nullable expression, while `Nullable` wraps the tuple itself into a
nullable type wrapper.
* I've tried to apply a similar approach like that one above, but only
for derived impls by manipulating the generated code for a optional
field with `#[diesel(embed)]`

Both solutions require changes to our sql type system, as for example
allowing to load a non nullable value into a `Option<T>` to enable their
usage in a more general scope as the presented example case.
(See the added test cases for this). That by itself would be fine in my
opinion, as this is always a safe operation. Unfortunately the
`AssumeNotNull` transformation would be applied recursively for all
sub-tuples, which in turn would cause trouble with nested joins (again
see the examples). We would be able to workaround this issue by allowing
the `FromSql<ST, DB> for Option<T>` impl for non-nullable types to catch
null values, which in turn really feels like a bad hack. (You would like
to get an error there instead, but nested nullable information are
gone.)
All in all this lead me to the conclusion that the current behaviour is
correct.

This PR adds a few additional tests (an adjusted version of the test
from the bug report + more tests around nested joins) and does move
around some code bits that I noticed while working on this.

I think the official answer for the bug report would be: Either wrap the
inner type also in an `Option` or provide a manual `Selectable` impl
that does the "right" thing there.

---
## [KathrinBailey/tgstation](https://github.com/KathrinBailey/tgstation)@[b48cda6afa...](https://github.com/KathrinBailey/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Sunday 2022-05-22 08:29:12 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [rk134/kernel_xiaomi_vince](https://github.com/rk134/kernel_xiaomi_vince)@[7313156188...](https://github.com/rk134/kernel_xiaomi_vince/commit/731315618846088e497fe29f9a45c8a9d0d8b4a6)
#### Sunday 2022-05-22 11:50:49 by Angelo G. Del Regno

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

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Aoihara <veronicadisa6@gmail.com>
Signed-off-by: rk134 <rahul-k@bigdi.cc>

---
## [The-Merchants-Guild/Merchant-Station-13](https://github.com/The-Merchants-Guild/Merchant-Station-13)@[f51ff8cdbd...](https://github.com/The-Merchants-Guild/Merchant-Station-13/commit/f51ff8cdbd744bf998ea669bab7e523eb023baa9)
#### Sunday 2022-05-22 12:38:46 by hamurlik

Adds simpson skintone (#138)

* Adds simpson skintone

The sign is a subtle joke. The shop is called "Sneed's Feed & Seed", where feed and seed both end in the sound "-eed", thus rhyming with the name of the owner, Sneed. The sign says that the shop was "Formerly Chuck's", implying that the two words beginning with "F" and "S" would have ended with "-uck", rhyming with "Chuck". So, when Chuck owned the shop, it would have been called "Chuck's Fuck and Suck".

Co-authored-by: EtraIV <34369281+EtraIV@users.noreply.github.com>

---
## [uleenucks/dwm](https://github.com/uleenucks/dwm)@[67d76bdc68...](https://github.com/uleenucks/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-05-22 12:53:01 by Chris Down

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
## [honsa/iptv-ch.github.io](https://github.com/honsa/iptv-ch.github.io)@[c141431c3f...](https://github.com/honsa/iptv-ch.github.io/commit/c141431c3f4966d039a8b1f9b811aa0689d04396)
#### Sunday 2022-05-22 13:41:44 by redge73

Update tvopenchfr.m3u

removed known end of life channels or some scrambled channels.
motorvision, voyage, nautical, rmc sport access 3, rmc sport access 4
sorry for no update, i ran into issue with my windows 7 starting die for checking if tv channel live or not.

---
## [TorannD/RWoM](https://github.com/TorannD/RWoM)@[a3fda50b81...](https://github.com/TorannD/RWoM/commit/a3fda50b81f45b3b47b1499ec7920ec99d89cea6)
#### Sunday 2022-05-22 13:42:12 by TorannD

v2.5.7.3 update

New:
 o Summoner Defense Pylon art and sound updates and configuration tweaks courtesy of Djeeshka

Tweaks:
 o Mage light performance improvements
 o Undead auto undraft performance improvements
 o Death retaliation will no longer summon meteors on pawns under a roof
 o Brightmage shooting accuracy penalty reduced
 o Ranger and Sniper now have a small shooting accuracy bonus
 o Elixir can be autocast and will target nearby injured pawns
 o Transcendent thought bonus for the use of magic duration increased 24->60 in-game hours
 o More distinction between Venerated and Abhorrent magic precepts
 o Sentinel health slightly increased
 o Demons will no longer jump to another target if engaged with their target in melee
 o Demon armor rating increased by ~10% and rewards increased
 o Golems will start with a name by default
 o Wandering Lich event earliest start time delayed from 90 days -> 250 days

Bug fixes:
 o Wave of fear causing errors for unique enemies
 o Disabled traits removed from arcane inspiration
 o Dormant Mecha Golem gatling gun requires line of sight to fire
 o Fix for spirit wolf dying in a caravan
 o Faceless will no longer have the option to pick up enchantment gems
 o Psionic dash will automatically cancel if within a cell of the map edge
 o Fixed golem draw depth for various upgrades
 o Golems losing name or settings after being upgraded

---
## [mochibms/oraja_difficulty_table](https://github.com/mochibms/oraja_difficulty_table)@[f3ee3d0e74...](https://github.com/mochibms/oraja_difficulty_table/commit/f3ee3d0e746dace1da73a7134392e18d90c24fc7)
#### Sunday 2022-05-22 14:11:31 by mochibms

20220522更新

重要

保存ミスで更新履歴の大部分が吹き飛んだので実際はこれより多くの譜面が新規搭載されています。申し訳ありません……

新規

0
Pleisure
Le Reve [DP ANOTHER]
Random [DP ANOTHER]

1
Collenz Cookie [DP ANOTHER]
Monochrome Heart [DP RED]
PrayStation [4_PStwo]

2
ACID BLIZZARD [DPH]
GOODBOUNCE [DPA]
The infant daughter Frandle's [ANOTHER]
Yellow Smile (bms edit) [Type/D]
カラッポ・ノンフィクション [DP LAPITHER]

3
Cube of mind

4
DataErr0r [sub another]

5
ClowN CrowN [DP INSANE]

6
Artificial Rose [DP ANOTHER]
Mario Paint (Time Regression Mix for BMS) -14P-
Parasitize Your Head [DP ANOTHER]

7
Berry Go!! [DP hututher]
BiBiRi [Heartbeat]
Daydreamer [DP Fancy]
GIN TONIC FLAVOR [14KEYS_INTOXICATED]
It's "alice" dream [DP INSANE]
Little Prayer (なんでも吸い込むピンク色のための) [激辛しれん味]
Lonely Cat [DP EX]
reflection [ADDICTION2DP]


8
Colleenz Cookie [DP-sagINSANE]
Littlegirl Complex


10
DataErr0r [sub black another]
キユビック [(d+p)^3]

11
Stella Story [After Story]


難易度変更

恋愛シンドローム [sub Black Another] 5→6

---
## [Jaaackx/IS12-Warfare](https://github.com/Jaaackx/IS12-Warfare)@[1867654758...](https://github.com/Jaaackx/IS12-Warfare/commit/186765475881bf58bbee319880653287d578820b)
#### Sunday 2022-05-22 14:46:31 by Matt

Should fix the issue of loading the wrong CSS by making them all the same fuck you

---
## [Wavy-Bot/bot](https://github.com/Wavy-Bot/bot)@[abc28eb1a5...](https://github.com/Wavy-Bot/bot/commit/abc28eb1a56357d0892e68c8ca0bf2934aa18f13)
#### Sunday 2022-05-22 15:20:03 by Robert S

General improvements, fixes and updates

Next up:
- Tidy up code.
- Remove duplicate code and making appropriate functions for said duplicated code.
- Make code of conduct, contributing guidelines and issue- and pull request templates.
- See what features users want in a bot, it is hard for me to know what to make.
- Remove command usage stats since I do not want to infringe on people's privacy.
- See if we really need an API and web dashboard, otherwise just remove it.
- Add commands utilising the Tetr.io API. (?)
- Make it easier to extend Wavy's feature-set. (?)
- See if Pycord is still the best API wrapper to use, Discord.py is back but it lacks the new features Discord has added, but in my experience it has always worked much better than Pycord. I am not against rewriting the bot again (nor doing that in another language), but I feel like people will get sick and tired of me constantly rewriting everything.

The above are just ideas, and will most likely get their own respective commits so it doesn't look like the project is dead for days on end. I have not decided on the idea(s) with a question mark `?` yet.

If you want a new feature, or you want to provide feedback, please do! I have no idea what to make next, and it's honestly quite saddening to see a project I worked on just die because I have no idea what to do with it. (But yeah people also didn't ask me to make a bot, so I shouldn't expect much honestly.) I hope to be able to attract more people to the bot, but right now I am basically in an infinite loop of trying to get feedback and such and not having enough people to ask for feedback.

I should probably just make a development ramblings channel on Discord for this stuff, but oh well. Thanks for reading and have a great day! (^-^)

~Robert

---
## [GrinGich/PaintCube](https://github.com/GrinGich/PaintCube)@[3226aa1c6f...](https://github.com/GrinGich/PaintCube/commit/3226aa1c6f51f332918c6f50e6b05b12fc2fed15)
#### Sunday 2022-05-22 15:38:11 by TexasElite

Code stuff for the outlines

This shit makes my brain hurt
Its just stuff for the outline code and such.

I can't feel my cock anymore

---
## [wassimk/dotfiles](https://github.com/wassimk/dotfiles)@[51f803051f...](https://github.com/wassimk/dotfiles/commit/51f803051fc3e91a116f0e56e69252a6b4792794)
#### Sunday 2022-05-22 16:06:17 by Wassim Metallaoui

feat: add automatic ctag management in vim

Recently I had someone (@molawson) watching me code in vim, and he said
to use <C-]> to jump to where you need! And it didn't work. It turns out
my ctags setup was completely broken. With this new setup, I'm pretty
much defaults, and it seems to work well.

This change also replaces exuberant-ctags with universal-ctags, which is
a maintained project.

Also, remove the tag generation with git hooks. I don't remember the
last time I coded outside of vim, and these hooks add complexity I never
understood.

On another note I just got the vim lsp tools which should provide a lot
of the same benefits of using ctags. But, after doing some research I
concluded lsp and ctags are both tools worth having loaded. They solve
similar problems (lsp references) but both have different results based
on how they scan and provide capabilities.

Edit: I tried this out and already had a bad experience. One which made
me add these new exclude directories. In a Rails app I work on, these
were generated Javascript files the ctags program took a long time to
process. I think these files should not even be in the project repo, so
I'll exclude them for now and do clean-up after. After ignoring all was
fast again.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d1a0a6b328...](https://github.com/mrakgr/The-Spiral-Language/commit/d1a0a6b328ca0797eb3d53dbc5a1a8d1b78cf776)
#### Sunday 2022-05-22 16:10:44 by Marko Grdinić

"8:20am. Let me chill a bit and then I will start.

https://mangadex.org/chapter/e7be5ba2-728e-4d52-ac69-f84178899817/2

Why did the backgrounds in Saki get such an increase in quality? This is quite nice.

8:50am. Great painted backgrounds one page, does not have time to clean up the line art in the next.

It is also interesting that Saki going in the direction of full out sci-fi.

9:10am. https://mangadex.org/chapter/6a509b98-e12f-4468-b861-2025c5b83b26/15

Even I though I know that this is just traced, I am still in awe at what sense of depth good line art can give. I want to comprehend how I can bring out this effect at will, so I don't fail at something like painting the creases again.

9:15am. Let me start. I want to get through modeling the stuff on the shelves. I have only today left to go, tomorrow I'll be able to start focusing on rendering. 3d modeling takes me too long. I might gone down the wrong path with it. Instead if I want good result in the fastest possible way I need to start leveling up my drawing.

9:20am. the first order of business will be to model the chasis of a router.

9:30am. Let me import the model in Blender so I can get a sense of proportions for when I do the router subdiv chassis.

i intend to model the chassing using subdiv and import it into Moi. It has the kind of round shape that would be a pain to get right using lofting.

9:45am. Change of plans. Now that I am studying the router more closely, I see  that it would be easier to do using a series of cuts. No problem.

What a dusty thing.

10:45am. What a mess. I wanted to do it quickly, but the way I approached it ended up leading me down the long way. Let me take a short break here.

11:10am. Let me resume. Modeling this was interesting. I know where I got wrong. I was taken by surprise by extrude not being able to cap non-planar curves.

11:25am. Damn it, how did this happen. I am having some boolean troubles with modeling the router so I decided to rebuild it, but I seem to be getting lost. I wanted to do this quickly, not like this!

1:10pm. Let me stop here. It is time for breakfast. This was a horrible morning session. And I am still not done with the router. I am not sure if it will even be visible in the final scene, so I am really wasting my time with it. I need to rething the way I've approached this.

3:05pm. Let me get back into Moi. Yeah, I am definitely not going to finish the shelves today. I've been in a daze for the past two hours. I want to figure something out.

4:30pm. Done with the router and its adapter.

4:45pm. By all rights I should go to the top shelf, but I am so tired I do not feel like it.

4:45pm. Let me post the work in /wip/.

One thing I've realized is that those mosquito tablet heater deviced that are on the top shelf have quite nice designs. It is really a pity that I want to rush things on the top shelf so I can get to the more fun stuff.

4:50pm. Actually I do not feel like rushing it. I kind of want to get some real practice done.

The room will get done when it is done. If I want to get things done faster, instead of cutting corners with 3d, I should practice drawing. Fast and 3d do not go well together.

Well, let me post the thing.

///

I made various errors while modeling the router which caused it to take much longer than I thought it would. The problem was that the sides had a slight angle to it, so I could not construct the router using straightforward techniques like I'd anticipated. I should have just separated out the surfaces and scaled them a bit before lofting them back, instead I did all sorts of crazy things to achieve something that should have been quite simple. It took me the entire day to do these two, but they might not even be visible in the scene. Instead of being faithful to my own room layout maybe I should put them on the top shelf where they could be seen.

I am happy with how the model came out, but I really am going to have to learn how to draw as 3d is too slow if you are doing everything from scratch. Maybe I should be kitbashing, but when I was doing a different scene a few months ago I checked out online asset sites and they did not have that much of what I would've wanted.

///

5:20pm. Let me rest a bit more and then I will get started on the next segment. Long or short, fast or slow, the most important thing is to keep going forward.

5:45pm. Let me have lunch here. Then I'll resume. I've been preparing my mind mentally for the next round. Though maybe I should just leave it for tomorrow. I've put in something like 6h being in the zone for this. This is about how much I can endure the programming session for the day. It is all good that I want to catch up and do more, and it is too bad that the router exhausted me, but rest is important.

I really should be iterating between 3d modeling and drawing, that might be the optimal path to actually get good at drawing. Just drawing images would not give you the same kind of feel for the form like 3d modeling does. But just having a feel for the 3d form is not enough to draw by itself, so I have to practice drawing as well.

Right now things are special, as I want to get more stuff into the scene. Honestly, forget rendering.

It is not like I am getting paid to render my room. I'll do the stuff on the top shelf and then start drawing the stuff I've modeled.

This was my original plan last year. Remembered when I was immitating Flycat. I've made good progress in my sculpting at that time, but then starting in January got tied up trying to do bigger scenes. Houdini really took a bit out of my time. I have no idea what I've even been doing for the past 5.5 months.

I've just been essentially playing around. I gained familiarity with a lot of things, but I haven't integrated it into my workflow. There might be a chance that I won't. It is ridiculous when you think just how much skill in 2d I could have acquired in this time. It is just in my nature to explore.

I didn't have a concrete plan of how exactly I am going to take advantage of 3d to make Heaven's Key. I just trusted that improving my skill would open my vistas and hopefully make it fast enough, but it not that easy. Watching Inio Asano work convinced me that the traditional methods are still dominant.

6pm. I could have gotten a programming job in the last 9 months and have made a ton of money, but I hate the thought of working on random things for random people. I do not want to spend the precious time of my life as a human on things of no importance, money or not. Not unless there is some crises that forces my hand.

Mom's cancer is one thing, but she seems to be well now, and it not like rich people have a cure for it. Cryofreeze is pretty extreme, it is the kind of cure that you need the right mindset for.

6:05pm. Let me get lunch, I am obviously done for the day since I've gone into rant mode. Maybe I'll get the desire to do just a bit more later, maybe those two boxes and the stuff I can do easily."

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[594fa3597e...](https://github.com/OxygenCobalt/Auxio/commit/594fa3597ec8af6749eda4a369eb27bd7acc35b4)
#### Sunday 2022-05-22 18:02:31 by OxygenCobalt

playback: add delayed action system

Replace the hodge-podge framework of state restoration and URI playing
with a single "delayed action" system.

Auxio's initialization routine is a total cluster----. This is mostly
because it involves multiple asynchronous operations such as music
loading, state restore, and service starting which tend to make it
highly prone to race conditions and other insanity.

In particular, the way Auxio would attempt to restore playback and
handle file opening was a spaghetti pile of bad API boundaries and
dubious UI code. This has not changed. I want to move this routine
to the service, but it's lifecycle is also sh------ed to such an
extent where that would be nearly impossible. Instead, this commit
introduces a new "delayed action" system that bites the bullet and
allowes PlaybackViewModel to accept a context and an action in
return for initializing playback...eventually.

I tried my best to eliminate as much memory leaks as I physically
could here, but could only go so far. Still though, even this insane
system is better than the UI-level LiveData shenanigans I did
previously, and actually works compared to the broken android
components that google keeps wanting you to use.

---
## [ULTRA-HOI/HOI4-ULTRA-Project](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project)@[22736e8d7d...](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project/commit/22736e8d7db4d9e34d9c17bd381a5b51fbb7103f)
#### Sunday 2022-05-22 18:18:40 by GrafKacper

Updated tank localisation

Fuck you github fuck you fuck you fuck you.

---
## [ThatGuyFromThatPlace/sojourn-station](https://github.com/ThatGuyFromThatPlace/sojourn-station)@[2747557916...](https://github.com/ThatGuyFromThatPlace/sojourn-station/commit/2747557916f2db8c94c80995c12a8516d7dbd351)
#### Sunday 2022-05-22 18:28:14 by DimmaDunk

Drip megapack 100% real not fake 1 commit church buff speedmerge (#3188)

* Drip megapack 100% real not fake 1 commit church buff speedmerge

- Adds Justice, Pandemonica, Malina, Zdrada and Modeus alt styles for charming outfit
- Adds a black suit jacket with adjustable styles for the charming outfit
- Adds charming waistcoat for Malina/Cerberus drip
- Ports the Tojo Pants and Tojo Jacket from the mad dog of Shimano himself
- Ports black and red overcoat styles (Joker, Morningstar)
- New sprites for Prospector/Foreman lockers, Salvager lockers changed in appearance to rusty old ones for fluff
- Adds New Testament Knight Hardsuit RIG module for the church's New Testament Armaments Disk, a Divisor/Numerical joint effort in producing a combat-ready hardsuit. A pre-loaded version with flash, shield, jetpack and storage modules spawns on the Prime's office's altar. Same stats as the Combat Hardsuit.

* Adds Knight RIG module sprite

Solving merge conflicts.

* Catifies your SCAFs

SCAF helmet and Blackshield SCAF helmet given alternate styles with cat ears for that Halo drip.

---
## [JacobLey/mocha](https://github.com/JacobLey/mocha)@[2078c3203f...](https://github.com/JacobLey/mocha/commit/2078c3203f55ee0e1783dc2fc9e20ac51dcb6896)
#### Sunday 2022-05-22 18:43:07 by Christopher Hiller

add support for running tests in parallel mode

* add support for running tests in parallel mode

> (this PR depends on most other PRs linked to #4198, so they should be merged first; documentation will be in another PR)

This PR adds support for running test files in parallel via `--parallel`.  For many cases, this should "just work."

When the `--parallel` flag is supplied, Mocha will swap out the default `Runner` (`lib/nodejs/runner.js`) for `ParallelBufferedRunner` (`lib/nodejs/parallel-buffered-runner.js`).

`ParallelBufferedRunner` _extends_ `Runner`.  `ParallelBufferedRunner#run()` is the main point of extension.  Instead of executing the tests in serial, it will create a pool of worker processes (not worker _threads_) based on the maximum job count (`--jobs`; defaults to `<number of CPU cores> - 1`).  Both `ParallelBufferedRunner` and the `worker` module consume the abstraction layer, [workerpool](https://npm.im/workerpool).

`ParallelBufferedRunner#run()` does _not_ load the test files, unlike `Runner#run()`.  Instead, it has a list of test files, and puts these into an async queue.  The `EVENT_RUN_BEGIN` event is then emitted.  As files enter the queue, `ParallelBufferedRunner#run()` tells `workerpool` to execute the `run()` function of the pool.  `workerpool` then launches as many worker processes are needed--up to the maximum--and executes the `run()` function with a single filepath and any options for a `Mocha` instance.

The first time `lib/nodejs/worker.js` is invoked, it will "bootstrap" itself, by handling `--require`'d modules and validating the UI.  Note that _reporter validation_ does not occur.  Once bootstrapped, it instantiate `Mocha`, add the single file, swap any reporter out for the `ParallelBuffered` reporter (`lib/nodejs/reporters/parallel-buffered.js`) then execute `Mocha#run()`, which invokes `Runner#run()`.

The `ParallelBuffered` reporter listens for events emitting from the `Runner` instance, like a reporter usually does.  But instead of outputting to the console, it buffers the events in a queue.  Once the file has completed running, the queue is drained: the events collected are (trivially) serialized for transmission back to the main process.  `ParallelBufferedRunner#run()` receives the list of events, trivially _deserializes_ them, and re-emits the events to whatever the chosen reporter is (e.g., the `spec` reporter).  In this way, the reporters don't know that the tests were run in parallel.  Practically, the user will see reporter output in "chunks" instead of the "stream" of results they usually expect.  This method ensures that while the test files run in a nondeterministic order, the reporter output will be deterministic for any given test file.

Once the result (the queue of events) has been returned to the main process, the worker process stays open, but waits for further instruction.  If there are more files in `ParallelBufferedRunner#run()`'s queue, `workerpool` will instruct the worker to take the next file from the list, and so on, and so forth.  When all files have executed, the pool terminates, the `EVENT_RUN_END` event is emitted, and the reporter handles it.

Note that exclusive tests ("only") cannot work in parallel mode, because we do not load all files up-front.

> (this section is pasted from the documentation with minimal edits)

### Caveats: Reporters

Due to the nature of the following reporters, they cannot work when running tests in parallel:

- `markdown`
- `progress`
- `json-stream`

These reporters expect Mocha to know _how many tests it plans to run_ before execution. This information is unavailable in parallel mode, as test files are loaded only when they are about to be run.

### Caveats: Buffered Output

In serial mode, tests results will "stream" as they occur. In parallel mode, reporter output is _buffered_; reporting will occur after each file is completed. In practice, the reporter output will appear in "chunks" (but will otherwise be identical).

### Caveats: Nondeterminism

In parallel mode, we have no guarantees about the order in which test files will be run--or what process runs them--as it depends on the execution times of the test files.

Because of this, the following options _cannot be used_ in parallel mode:

- `--file`
- `--sort`
- `--delay`

Because running tests in parallel mode uses more system resources at once, the OS may take extra time to schedule and complete some operations. For this reason, test timeouts may need to be increased either globally or otherwise.

### Caveats: Other Impacted Options

When used with `--bail` (or `this.bail()`) to exit after the first failure, it's likely other tests will be running at the same time. Mocha must shut down its worker processes before exiting.

Likewise, subprocesses may throw uncaught exceptions. When used with `--allow-uncaught`, Mocha will "bubble" this exception to the main process, but still must shut down its processes.

`--forbid-only` does not work in parallel mode, for a similar reason to the unsupported reporters.

> _NOTE: This only applies to test files run parallel mode_.

### Caveats: Root Hooks

A _root hook_ is a hook in a test file which is _not defined_ within a suite. An example using the `bdd` interface:

```js
// test/setup.js
beforeEach(function() {
  doMySetup();
});

afterEach(function() {
  doMyTeardown();
});
```

When run (in the default "serial" mode) via `mocha --file "./test/setup.js" "./test/**/*.spec.js"`, `setup.js` will be executed _first_, and install the two hooks shown above for every test found in `./test/**/*.spec.js`.

**When Mocha runs in parallel mode, test files do not share the same process.** Consequently, a root hook defined in test file _A_ won't be present in test file _B_.

There are a (minimum of) two workarounds for this:

1. `require('./setup.js')` or `import './setup.js'` at the top of every test file. Best avoided for those averse to boilerplate.
1. _Recommended_: Define root-level hooks in a required file, using the new (also as of VERSION) Root Hook Plugin system.

### Caveats: Node.js Only, For Now

Parallel mode is only available in Node.js.

### Migration Checklist

If you find your tests don't work properly when run with `--parallel`, either shrug and move on, or use this handy-dandy checklist to get things working:

- :white_check_mark: Ensure you are using a supported reporter.
- :white_check_mark: Ensure you are not using other unsupported flags.
- :white_check_mark: Double-check your config file; options set in config files will be merged with any command-line option.
- :white_check_mark: Look for root-level hooks in your tests. Move them into a root hook plugin.
- :white_check_mark: Do any assertion, mock, or other test libraries you're consuming use root hooks? They may need to be migrated for compatibility with parallel mode.
- :white_check_mark: If tests are unexpectedly timing out, you may need to increase the default test timeout (via `--timeout`)
- :white_check_mark: Ensure your tests do not depend on being run in a specific order.
- :white_check_mark: Ensure your tests clean up after themselves; remove temp files, handles, sockets, etc. Don't try to share state or resources between test files.

### About Parallelism

Some types of tests are _not_ so well-suited to run in parallel. For example, extremely timing-sensitive tests, or tests which make I/O requests to a limited pool of resources (such as opening ports, or automating browser windows, hitting a test DB, or remote server, etc.).

Free-tier cloud CI services may not provide a suitable multi-core container or VM for their build agents. Regarding expected performance gains in CI: your mileage may vary. It may help to use a conditional in a `.mocharc.js` to check for `process.env.CI`, and adjust the job count as appropriate.

It's unlikely (but not impossible) to see a performance gain from a job count _greater than_ the number of available CPU cores. That said, _play around with the job count_--there's no one-size-fits all, and the unique characteristics of your tests will determine the optimal number of jobs; it may even be that fewer is faster!

### Change Details

- updated signal handling in `bin/mocha` to a) better work with Windows, and b) work properly with `--parallel` to avoid leaving zombie workers
- docstrings in `lib/nodejs/cli/collect-files.js`
- refactors in `lib/nodejs/cli/run-helpers.js` and `lib/nodejs/cli/watch-run.js`.  We now have four methods:
    - `watchRun()` - serial + watch
    - `singleRun()` - serial
    - `parallelWatchRun()` - parallel + watch
    - `parallelRun()` - parallel
- `lib/nodejs/cli/run.js` and `lib/nodejs/cli/run-option-metadata.js`: additions for new options and checks for incompatibility
- add `lib/nodejs/reporters/buffered.js` (`ParallelBuffered`); this reporter is _not_ re-exported in `Mocha.reporters`, since it should only be invoked internally.
- tweak `landing` reporter to avoid referencing `Runner#total`, which is incompatible with parallel mode.  It didn't need to do so in the first place!
- the `tap` reporter now outputs the plan at the _end_ instead of at the beginning (avoiding a call to `Runner#grepTotal()`, which is incompatible with parallel mode).  This is within spec, so should not be a breaking change.
- add `lib/nodejs/parallel-buffered-runner.js` (`ParallelBufferedRunner`); subclass of `Runner` which overrides the `run()` method.
    - There's a little custom finite state machine in here.  didn't want to pull in a third-party module, but we should consider doing so if we use FSM's elsewhere.
    - when `DEBUG=mocha:parallel*` is in the env, this module will output statistics about the worker pool every 5s
    - the `run()` method looks a little weird because I wanted to use `async/await`, but the method it is overriding (`Runner#run`) is _not_ `async`
    - traps `SIGINT` to gracefully terminate the pool
    - pulls in [promise.allsettled](https://npm.im/promise.allsettled) polyfill to handle workers that may have rejected with uncaught exceptions
    - "bail" support is best-effort.
    - the `ABORTING` state is only for interruption via `SIGINT` or if `allowUncaught` is true and we get an uncaught exception
- `Hook`, `Suite`, `Test`: add a `serialize()` method.  This pulls out the most relevant information about the object for transmission over IPC.  It's called by worker processes for each event received by its `Runner`; event arguments (e.g., `test` or `suite`) are serialized in this manner.  Note that this _limits what reporters have access to_, which may break compatibility with third-party reporters that may use information that is missing from the serialized object.  As those cases arise, we can add more information to the serialized objects (in some cases).  The `$$` convention tells the _deserializer_ to turn the property into a function which returns the passed value, e.g., `test.fullTitle()`.
- `lib/nodejs/mocha.js`:
    - refactor `Mocha#reporter` for nicer parameter & variable names
    - rename `loadAsync` to `lazyLoadFiles`, which is more descriptive, IMO.  It's a private property, so should not be a breaking change.
    - Constructor will dynamically choose the appropriate `Runner`
- `lib/nodejs/runner.js`: `ParallelBufferedRunner` needs the options from `Mocha#options`, so I updated the parent method to define the parameter.  It is unused here.
- add `lib/nodejs/serializer.js`: on the worker process side, manages event queue serialization; manages deserialization of the event queue in the main process.
    - I spent a long time trying to get this working.  We need to account for things like `Error` instances, with their stack traces, since those can be event arguments (e.g., `EVENT_TEST_FAIL` sends both a `Test` and the `Error`).  It's impossible to serialize circular (self-referential) objects, so we need to account for those as well.
    - Not super happy with the deserialization algorithm, since it's recursive, but it shouldn't be too much of an issue because the serializer won't output circular structures.
    - Attempted to avoid prototype pollution issues
    - Much of this works by mutating objects, mostly because it can be more performant.  The code can be changed to be "more immutable", as that's likely to be easier to understand, if it doesn't impact performance too much.  We're serializing potentially very large arrays of stuff.
    - The `__type` prop is a hint for the deserializer.  This convention allows us to re-expand plain objects back into `Error` instances, for example.  You can't send an `Error` instance over IPC!
- add `lib/nodejs/worker.js`:
    - registers its `run()` function with `workerpool` to be called by main process
    - if `DEBUG=mocha:parallel*` is set, will output information (on an interval) about long-running test files
    - afaik the only way `run()` can reject is if `allowUncaught` is true or serialization fails
    - any user-supplied `reporter` value is replaced with the `ParallelBuffered` reporter.  thus, reporters are not validated.
    - the worker uses `Runner`, like usual.
- tests:
    - see `test/integration/options/parallel.spec.js` for the interesting stuff
    - upgrade `unexpected` for "to have readonly property" assertion
    - upgrade `unexpected-eventemitter` for support async function support
    - integration test helpers allow Mocha's developers to use `--bail` and `--parallel`, but will default to `--no-bail` and `--no-parallel`.
    - split some node-specific tests out of `test/unit/mocha.spec.js` into `test/node-unit/mocha.spec.js`
    - add some missing coverage in `test/node-unit/worker.spec.js`
- etc:
    - update `.eslintrc.yml` for new Node-only files
    - increase default timeout to `1000` (also seen in another PR) and use `parallel` mode by default in `.mocharc.yml`
    - run node unit tests _in serial_ as sort of a smoke test, as otherwise all our tests would be run in parallel
    - karma, browserify: ignore files for parallel support
    - force color output in CI. this is nice on travis, but ugly on appveyor.  either way, it's easier to read than having no color
    - move non-CLI-related node-specific files into `lib/nodejs/nodejs/`
    - correct some issues with APIs not marked `@private`
    - add some istanbul directives to ignore some debug statements
    - add `utils.isBrowser()` for easier mocking of a `process.browser === true` situation
    - add `createForbiddenExclusivityError()`

Ref: #4198

Signed-off-by: Christopher Hiller <boneskull@boneskull.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8a7606e7b5...](https://github.com/mrakgr/The-Spiral-Language/commit/8a7606e7b5082c201b31460d5a5673a3061051eb)
#### Sunday 2022-05-22 19:03:59 by Marko Grdinić

"7pm. Let me do some more modeling. I am feeling up for it now.

7:25pm. I am running into trouble with the basic boxes. I could leave this for the later stages, but let me just ask.

7:35pm. https://moi3d.com/forum/discussion.php?webtag=MOI&msg=10705.1

Here is the Moi issue. Let me make the other box. This is not that important to me, so I might as well leave it for later.

8:40pm. Modeled the USB stick. Not bad.

Got some experience with using arcs. I've been unfairly neglecting them, I should have been using it instead of freeform in places. The point as well.

8:45pm. https://danbooru.donmai.us/posts/5367063?q=fuzichoco

Fuzichoco (Kenja No Deshi's novel illustrator) is very good. When I say that old masters have nothing on the new ones, people like him are exactly what I mean. People wonder where the von Neuman have gone off to, but there is need to ask the same thing about the artists.

This is what rank 5 in 2d would be for me.

I imagined if I got better in 3d I would be able to make these kinds of scenes quickly, but I am going to have to gain some skill in 2d if at least to comparmentalize my 3d work.

8:50pm. This kind of modeling I am doing here is really great for internalizing various shapes. Sure I know what an USB is, but this kind of exercise really forces me to study the form in ways that aren't superficial. I am starting to think that there is a beauty to hard surface models. Had I made the choice not to go down this path, I never would have realized this."

---
## [fizteh95/Athena](https://github.com/fizteh95/Athena)@[29264fc45e...](https://github.com/fizteh95/Athena/commit/29264fc45eab7a53b607ce99adf36ca5a25dffe9)
#### Sunday 2022-05-22 19:07:00 by kutish

hoooly shit, fucking linter, i fucking hate you sooo much; linter fixes

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[8b77243ce9...](https://github.com/yogstation13/Yogstation/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Sunday 2022-05-22 20:12:47 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [Luramoth/graphics-moment](https://github.com/Luramoth/graphics-moment)@[09c39f0ab3...](https://github.com/Luramoth/graphics-moment/commit/09c39f0ab385e939d1c2b73581a18835e59c0a9e)
#### Sunday 2022-05-22 20:26:40 by Kayla

reformat project to be propor
thank you tuna
(fuck you tuna)

---
## [P3tray/Adonis](https://github.com/P3tray/Adonis)@[4928cc16a3...](https://github.com/P3tray/Adonis/commit/4928cc16a3846384dc873ed8c33186f87ff2a856)
#### Sunday 2022-05-22 20:44:30 by P3tray

Added settings.Messages, also did a lot more. (#757)

* Update Settings.lua

* We Had To Use Dark Magic To Make This Work

* these guys are flipped

* this is how we generate our shit.

* arrgghh... damn this thing for not working.

* Now we tell you your browser sucks in your native tongue.

* All hail the mighty ccuser44

* Update Loader.server.lua

Co-authored-by: Sceleratis <sceleratis@gmail.com>

---
## [gltile-two-electric-boogaloo/uwurandom-in-userspace](https://github.com/gltile-two-electric-boogaloo/uwurandom-in-userspace)@[4b4e0f4702...](https://github.com/gltile-two-electric-boogaloo/uwurandom-in-userspace/commit/4b4e0f4702f59823d90482ef07939a5561b96468)
#### Sunday 2022-05-22 21:41:16 by gltile-two-electric-boogaloo

god i hate windows. like seriously look at this bullshit. i have to "BCryptOpenAlgorithmProvider" before i can "BCryptGenRandom" into a buffer and then i have to "BCryptCloseAlgorithmProvider". like what the fuck is wrong with you. i will personally punch whoever the fuck decided this was a good design choice

---
## [slushpile/slushpile.github.io](https://github.com/slushpile/slushpile.github.io)@[0fe21d4b7b...](https://github.com/slushpile/slushpile.github.io/commit/0fe21d4b7b0125e605643b33794d20faec3eecb2)
#### Sunday 2022-05-22 21:44:52 by Nicholas Lawson

FAT ASS HELL YEAH

I can do shit with the comment tags like i can blow up parts of my site that i want to focus on with comment tags here it's possible for me to throw my disqus up to the top of my screen and that's a good 2nd edition

---
## [DevilishSpirits/arcollect](https://github.com/DevilishSpirits/arcollect)@[7d53feadf9...](https://github.com/DevilishSpirits/arcollect/commit/7d53feadf98ea318ab355dc0380acfb36b272e19)
#### Sunday 2022-05-22 21:53:17 by Devilish Spirits

Added support for KnowYourMeme

	I am a bit overloaded of work right now and destroying my sleep schedule with stupid even less useful things and AAAAAAHHHH!!!! I listened to too much MADs remixes... :sob:

	Also sorry JP if I'm sleepy this morning.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[c3e823d052...](https://github.com/yogstation13/Yogstation/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Sunday 2022-05-22 21:56:12 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---

