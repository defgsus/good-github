## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-22](docs/good-messages/2022/2022-10-22.md)


1,815,735 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,815,735 were push events containing 2,538,867 commit messages that amount to 154,187,905 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 26 messages:


## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[8272749e8c...](https://github.com/justinpryzby/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Saturday 2022-10-22 00:16:19 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [tydavis/git](https://github.com/tydavis/git)@[d3775de074...](https://github.com/tydavis/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Saturday 2022-10-22 00:49:39 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [entrez/EvilHack](https://github.com/entrez/EvilHack)@[844574b621...](https://github.com/entrez/EvilHack/commit/844574b62157db544c1b9af1683b8cba4b0cc12f)
#### Saturday 2022-10-22 01:00:29 by k21971

Sanctum/ascension run revamp: part 1 (sanctum).

This is the first part of the sanctum/ascension run revamp for EvilHack.
The plan is this: instead of the player having to trek all the way back
out through Gehennom and the dungeon to escape and enter the elemental
Planes, they will instead make their way from the bottom of Gehennom
(the Sanctum) up through Purgatory, and then be deposited in the dungeon
on the same level as their quest home entrance (this is in case the
player needs to chat with their quest leader again). They then traverse
the few remaining dungeon levels to the Planes. Purgatory will only be
2-3 levels at most, but will be just as difficult as the Sanctum, if not
more so. It won't be an easy trek back out to the Planes, but it will be
a much shorter and less tedious one.

Part one focuses on the Sanctum, and the west side of the map has been
redesigned to accommodate the changes. Once the player acquires the
Anulet of Yendor (for Infidels, imbue the Idol of Moloch), a gate is
formed in the west wall of the inner sanctum, leading to a previously
unreachable part of the map. At the same time that this gate magically
appears, the stairs leading back up out of the sanctum are removed, and
all other forms of leaving the sanctum (branchporting, levelporting, or
quaffing a cursed potion of gain level) are suppressed. The only way to
leave the sanctum and continue is through the newly formed gates, and to
face the monsters within.

In this new section resides Lucifer, the most powerful demon prince of
them all. He guards the magic portal that leads to Purgatory. His
entourage are four named balrogs waiting outside his inner chamber.
Lucifer will not engage until the player attacks or moves next to him.
His attacks, while not as severe as Demogorgon's illness attack or
Graz'zt's stealing ability, are stong enough to be taken seriously.
Lucifer also spawns with 666 hit points, so he won't be an easy or quick
kill, even with silver weapons.

There's room for improvement here, such as the com_pager() dialogue, or
what gear Lucifer could spawn with, and so on. I added the branch port
location to Purgatory in the .des file, but as of this commit, it isn't
active yet since the Purgatory branch hasn't been created. Once
Purgatory is created - if the player needs to go back there for any
reason once they've exited and are back in the regular dungeon, they
will have the ability to travel back down to the bottom of Gehennom and
enter the Sanctum via the stairs formed during the invocation, and then
through the portal to Purgatory again.

In this commit, there's also a bugfix concerning u.uachieve.amulet and
when an Infidel actually imbues the Idol of Moloch.

---
## [jiangbo0216/react](https://github.com/jiangbo0216/react)@[b6978bc38f...](https://github.com/jiangbo0216/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-10-22 02:25:03 by Andrew Clark

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
## [shintaro-iwasaki/FBGEMM](https://github.com/shintaro-iwasaki/FBGEMM)@[466e1ea92c...](https://github.com/shintaro-iwasaki/FBGEMM/commit/466e1ea92c9044d18f5ab25943de6704b5c37779)
#### Saturday 2022-10-22 03:29:11 by siwasaki

Enhance FBGEMM nightly CI with cuDNN fix (#1407)

Summary:
This PR updates FBGEMM nightly CI to make it more usable and maintainable by using GitHub Actions more effectively, with a cuDNN installation fix. I want to make them happen together so that the "fix" really fixes an issue.

## 1. Fix the cuDNN installation issue in FBGEMM nightly CI

We used `conda-forge` to install cuDNN, but this unintentionally added CUDA 10 dependency to the FBGEMM nightly package, breaking installation steps that rely on FBGEMM nightly.

To address this issue, we install cuDNN separately in the CI script so that it can coexist with CUDA 11.7, which is used by PyTorch-CUDA nightly.

## 2. Implement label-triggered wheel tests during a PR review

Previously, we needed to apply a hack to trigger wheel-related tests before merging the PR, which is neither comprehensive nor efficient.

To address this issue, this PR adds optional wheel-related tests.  Now a PR with a label such as `"test_wheel_nightly"`, `"test_wheel_prerelease"`, and `"test_wheel_release"` enables the corresponding wheel-related tests.  We don't need to modify YML files again, so we can easily run these tests.  Please trigger these tests for suspicious PRs that touch the installation logic.  Note that binaries won't be pushed to PYPI if this method is used.

## 3. Remove duplicated logic across YML files

Nightly/release/cpu/gpu wheel scripts shared most in common, but the logic were scattered across different files, which significantly lowered maintainability.

To address this issue, this PR collects all the wheel-related test logic into a single file (`build_wheel.yml`) and makes the callers (e.g., scheduled nightly trigger or per-PR tests using labels) pass flags to control the flow (e.g., per-PR tests do not push the wheel binary to PYPI).  No duplication improves maintainability.

<img width="1269" alt="Screen Shot 2022-10-21 at 9 58 56 AM" src="https://user-images.githubusercontent.com/15073003/197249555-bb00f3b1-9bc9-46f1-8fea-7874460723f6.png">

## 4. Support handy wheel-related tests on a local machine

Previously, the core wheel-related build/test logics were embedded into GitHub workflow files (`*.yml`) mixed with AWS-specific commands, so it was very tedious to test the nightly logic on a local machine, lowering the developer efficiency.

To address this issue, this PR extracts core scripts from GitHub workflow files and makes them standalone so that the developer can try wheel-build locally (i.e., without access to AWS machine). It uses conda to create a virtual software environment, so it should be handy enough in many cases though this is not as robust as a container-based solution.

```sh
# For example, check prerelease PyTorch (pytorch-test package) locally.
git clone https://github.com/pytorch/FBGEMM.git
cd FBGEMM
git submodule update --init --recursive
bash .github/scripts/build_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -o fbgemm_gpu_test
bash .github/scripts/test_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -w fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
git clone https://github.com/pytorch/torchrec.git
cd torchrec
git submodule update --init --recursive
bash ../.github/scripts/test_torchrec.bash -o torchrec_nightly -p 3.10 -c 11.7 -v -P pytorch-test -w ../fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
```

## 5. [Temporary] Add TorchRec integration test

TorchRec is one of our most important users, but we didn't test TorchRec integration in the nightly CI, so the changes in FBGEMM sometimes surprised the TorchRec developers.

To address this issue, though it is temporary, but this PR adds a TorchRec integration test before pushing a binary to PYPI so that we can make sure that FBGEMM works with TorchRec.  However, now broken TorchRec can break FBGEMM-nightly; we will investigate a more sustainable solution that makes everyone happy.

## 6. Better interface to manually trigger the CI

It looks nice. I love to operate the release management in an automated way as much as possible to reduce human errors at the very last minute. In the future, we can add more options if needed.

<img width="844" alt="Screen Shot 2022-10-21 at 5 53 03 AM" src="https://user-images.githubusercontent.com/15073003/197240190-e808df23-795a-451d-a7d9-ec1c43c68e92.png">

Pull Request resolved: https://github.com/pytorch/FBGEMM/pull/1407

Differential Revision: D40597700

Pulled By: shintaro-iwasaki

fbshipit-source-id: 425ef0be6c652bc7294f6940adb0a27fc96b353d

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[ef03b21acc...](https://github.com/Conga0/Mo_Creeps/commit/ef03b21acc84b738913b86fe3ba11a6c6c8e5025)
#### Saturday 2022-10-22 06:49:08 by Conga Lyne

New Creeps, New Spells, semi-final update

Fixed illusion firebugs setting you and the environment on fire
Fixed esoteric being's divine light attack being pushed around by repulsion
Optimised Polymorph Crystal Tags
Slightly reduced Magic Poring damage
Changed Magic Poring's projectile to look visually distinct from polymorph orbs
Fixed Cats being homing targets, especially problematic if they're immortal
Added Boss Health Multiplier option in settings
Added mod compatibility with Worse Enemies
Improved Cursed Orb Barrage Sprite
Fixed Typo in personal thrower spells, "tun" to "turn"
New (currently final) trophy room statue added
Fixed Pixel scenes overriding NG+ pixelscenes
Message of the Day is now displayed as a sign rather than a tablet
Updated Tablet of Apotheosis description
Fixed Delusions being polymorphable

New Creep: Overzealous Poly Master
New Creep: Big Blob
New Creep: Creepy Blob
New Boss Creep: Colossal Blob
New Spell: Split Spell
New Spell: Mass Drunk
New Spell: Mass Wet
New Spell: Mass Fire
New Spell: Mass Jarate
New Spell: Mass Polymorph

---
## [RalfJung/rust](https://github.com/RalfJung/rust)@[9e8f53d09a...](https://github.com/RalfJung/rust/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Saturday 2022-10-22 06:58:25 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [racingmars/dwm](https://github.com/racingmars/dwm)@[67d76bdc68...](https://github.com/racingmars/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Saturday 2022-10-22 06:59:28 by Chris Down

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
## [viethung204/PAINDEALER](https://github.com/viethung204/PAINDEALER)@[b3cdce3aab...](https://github.com/viethung204/PAINDEALER/commit/b3cdce3aabd73e52c51f83122d8c29d0aa3a4703)
#### Saturday 2022-10-22 08:28:52 by viethung204

misc

fuck convex colliders, all my homies hate convex colliders, ughhhhhhhhhhh, thank god i was able to fix this piss-drinking, shit-eating of a bug today

---
## [Empire-Strikes-Back/Solo](https://github.com/Empire-Strikes-Back/Solo)@[05a9e308c0...](https://github.com/Empire-Strikes-Back/Solo/commit/05a9e308c0b5dc1a5df60c7949c464899fe70ec9)
#### Saturday 2022-10-22 10:47:02 by Solo

it's not much but it will help you get to salt-process Zurich

unlike TheViper we don't turn temple into marketpace - we are money free

like Rich Hickey understands importance of hosted - so do we don't cook

I am a branch of Jesus - I know about store, posessions, least, two masters, denarius, woman who touched his cloak

let source of our B12 be not a library but food
let it come from biggest food store - github
like Jason Bourne has changed but still have to deal with Treadstone - so do we despise word project
let project.clj - not our libraries - be how we are repled and compiled
let project.cj be like fish - daily, not a drug supplement B12
I look up to Jesus and I know about today and tomorrow and worry
let nori be B12 that is enough for body - but not for caesar
project.clj says project - but we are vegan programs inside who eat fish because we should, not need but should
like Marie does not need to stay with Bourne - but she should and chooses to

:Matt-Damon you must be really bombed out?
:Jimmy-Kimmel yeah - I'm a little disappointed
:Matt-Damon hey, let's cheer Jimmy up - he's a big loser

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[7ae7f4e466...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/7ae7f4e46680ec2a501346d4b7a8bcbc4ca8e38d)
#### Saturday 2022-10-22 10:59:38 by tanish2k09

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
## [kittenbox-isa/scratchpost](https://github.com/kittenbox-isa/scratchpost)@[87a3e22f65...](https://github.com/kittenbox-isa/scratchpost/commit/87a3e22f65bf95117cfc1921105b1f38b985aacc)
#### Saturday 2022-10-22 11:43:38 by kaylatheegg

finally fixes the "-fno-common" bug
starting in gcc 10, -fno-common was the default
fuck gnu god DAMNIT

---
## [Tiktodz/kernel_msm-4.4](https://github.com/Tiktodz/kernel_msm-4.4)@[d3ff68b921...](https://github.com/Tiktodz/kernel_msm-4.4/commit/d3ff68b921ff75ec88c4d4b43744bf0df75422ff)
#### Saturday 2022-10-22 11:52:28 by Maciej Żenczykowski

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
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [AnandSuresh02/kernel_asus_sdm660](https://github.com/AnandSuresh02/kernel_asus_sdm660)@[fcde8efe52...](https://github.com/AnandSuresh02/kernel_asus_sdm660/commit/fcde8efe52b815ab488a83420a2d66080a7f71d2)
#### Saturday 2022-10-22 14:17:30 by Christian Brauner

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
## [NonProjects/tgbox](https://github.com/NonProjects/tgbox)@[c6a01ccba3...](https://github.com/NonProjects/tgbox/commit/c6a01ccba352ff1e63d4a1baafed91536c8b1418)
#### Saturday 2022-10-22 14:38:03 by NotStatilko

TGBOX update 22/22

Title doesn't make big sense, ye?

This update includes:
 1. Fingerprints: now you can't upload two files on
    the same file path with the same name. Otherwise
    is strange as far i see;

 2. Flexible LocalBox: starting from now database
    structure will auto update on a first commit
    according to the version requirements;

 3. Custom defaults: now TGBOX will fetch default
    values from the new DEFAULTS table of the
    LocalBox sqlite database, so starting from
    now you can easily change i.e METADATA_MAX
    to the more than 1MB of size. To sync your
    personal defaults with the RemoteBox you're
    advised to decrypt an EncryptedRemoteBox
    object with the DecryptedLocalBox object,
    and not with keys (BaseKey/MainKey), cuz
    otherwise RemoteBox will use the default
    defaults from the defaults module (yeah!);

 4. Proxy: we added cute and easy way to use
    proxy for any TelegramClient connections;

 5. exported -> imported: prior this update
    files that was imported from the other
    RemoteBox was called... exported? IDK
    what this is all about was, so now you
    can access this info via imported flag;

 6. Some other little improvements & bugfixes.

This update took really long because of my
life circumstances and the new feature i
tried to implement called "Mirroring". The
Mirroring was about making links to already
uploaded files. I.e if you uploaded before
a file A on a path X and try to upload the
same file A but on a path Y then we don't
upload a file again, but make a link to
it (mirror) and push to RemoteBox. Sounds
pretty good? Well, i think so. But there
is really a big amount problems behind
this: i.e how to clone it, how to remove
it, how to share it, etc, so i abandoned
this idea. Telegram isn't really designed
for such things in my humble opinion.

---
## [GTD-Carthage/Obsidian-Content](https://github.com/GTD-Carthage/Obsidian-Content)@[9863d33d15...](https://github.com/GTD-Carthage/Obsidian-Content/commit/9863d33d15eb399c20c6d086c45be24a7d4ad6bf)
#### Saturday 2022-10-22 17:57:17 by Demiosis

Modified slightly the organ T hall

To help impatient kids, peoples who can't read a map and zoomers understand it better! Holy shit I laughed quite hard on this one..

---
## [CheezusChrust/ACE-Dev](https://github.com/CheezusChrust/ACE-Dev)@[93be1b21bb...](https://github.com/CheezusChrust/ACE-Dev/commit/93be1b21bbdbf656b4de5abb25a3fbd6fb01ec69)
#### Saturday 2022-10-22 18:04:29 by Mr Marty

optional nadmod, missile adjustments & more

- added acf3's traceline workaround. useless tracehull calls should be removed as time passes.
- Fixed closest distance output. Now it will give a distance properly.
- Fixed some bugs with some missile crazy trayectory. Remember: dont shoot at 90°, you will not want friendly causalities...
- Added Plunging fuze. Aka tow2b top attack capacity
- Done fuze core less shitty. Ability to override the detonation perform.
- Nadmod becomes optional. Without it, damage can be done. Damage permissions becomes no available.
- Added primitive class ent into contraption look for filter.
- Updated armor analyzer. ERA armor calculation considers angle now.
- Minor changes to AT-3 and AT-2 missiles

---
## [avar/git](https://github.com/avar/git)@[56b10c5383...](https://github.com/avar/git/commit/56b10c5383d5359d0cec112f7b40f77ff57ec029)
#### Saturday 2022-10-22 18:19:26 by Ævar Arnfjörð Bjarmason

submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior related to "--" handling, even when that
behavior is stupid. We'll fix in subsequent commits, but let's first
faithfully reproduce it.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

It would be better to use run_command() here directly to avoid copying
"args" and "env" copying, but let's use run_command_v_opt_cd_env()
instead to optimize for subsequent diff size. By using our own "struct
strvec args" we can push to "&args", not a "&cp.args". Eventually
we'll stop invoking "submodule--helper" as a sub-process, and avoid
the churn of converting all of "&cp.args" to "&args".

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[7c9e26bb85...](https://github.com/YakumoChen/Skyrat-tg/commit/7c9e26bb85a40ee3f5a570fe4f51df3c4f350ea5)
#### Saturday 2022-10-22 19:19:27 by SkyratBot

[MIRROR] Fixes Some Incredulously Fucked Up Recycler Behavior [MDB IGNORE] (#17018)

* Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Fixes Some Incredulously Fucked Up Recycler Behavior

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[3e5c10f876...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/3e5c10f8761cbba75815db23af91175d8f5b745a)
#### Saturday 2022-10-22 19:33:47 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Change-Id: Iac0a8b6392036e35509a609ee0800301915a885e
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3582aa77bb...](https://github.com/tgstation/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Saturday 2022-10-22 20:10:24 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [water-sucks/nixed](https://github.com/water-sucks/nixed)@[41bab887d4...](https://github.com/water-sucks/nixed/commit/41bab887d46b214e535d56f1dbc4fcfa2fbefd3d)
#### Saturday 2022-10-22 20:53:47 by Varun Narravula

Remove digga entirely and replace with flake-parts

This is a rather large commit, because of all of the refactoring;
while I hate large commits, because you can't really bisect them,
this one was a sad necessity to keep things atomic, in a sense that
my commits are ideally supposed to be working revisions I can switch
to at any time if I wish to.

- Remove flake-utils and all digga flake inputs
- Add flake-parts input
- Update nix-darwin input so it would stop complaining about runCommand
- Create custom lib with functions to generate modules for
  profiles/users
- Replace all invocations of specialArgs with profiles/suites to use
  generated modules with genModules
- Fix boot issues by moving out Plymouth configuration into a profile
  and manually allowing redistributable firmware
- Replace systemd-boot with grub (sadly, I found this to be a much
  easier path to troubleshooting stuff if booting goes haywire)
- Change hm-system-defaults to user-defaults and set home-manager
  options there
- Replace weird override mechanism for mixing different nixpkgs
  inputs with a simple overlay
- Override nvim configuration to be use stable versions of broken
  plugins (in line with previous)
- Move weird polybar stuff into a single module to remove usage of
  imports
- Move nix settings into a single common profile
- Add single argument to all profiles so that they can be
  imported and called as functions by genProfileOption
- Rekey secrets (agenix gave me hell about this and wouldn't let
  me log in, presumably because the hashing changed?)
- Move rofi-power-menu into separate profile to prevent callback hell
- Remove touch-id module that got merged into nix-darwin

---
## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[a2577296e6...](https://github.com/skylord-a52/orbstation-andrea/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Saturday 2022-10-22 21:44:41 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[422accbe4e...](https://github.com/skylord-a52/orbstation-andrea/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Saturday 2022-10-22 21:44:41 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [punesemu/glsl-shaders](https://github.com/punesemu/glsl-shaders)@[0c3d862e0d...](https://github.com/punesemu/glsl-shaders/commit/0c3d862e0d361b043d11f7b1e42be24134fe362b)
#### Saturday 2022-10-22 22:17:58 by mudlord

Deobfuscated shit TV shader. Feel free to cannibalize. (#179)

* It's been a long time.
We shouldn't of left you.
Without a dope beat to step to.
Time's up.

* fuck.

---
## [CluckeyMcCormick/ncg2](https://github.com/CluckeyMcCormick/ncg2)@[a373324901...](https://github.com/CluckeyMcCormick/ncg2/commit/a373324901e4441230fcc17798dffe14817a9ede)
#### Saturday 2022-10-22 22:39:30 by frick-nedrickson

Set up the AutoTower's UV values

Now that we're generating using the CubeMesh, we need to modify the UV
values - and possibly other values besides.

To do that, we needed to know which vertex was which. Some
experimentation showed that the vertices have this odd interleaved
scheme. So the vertices go FACE-A FACE-B FACE-A FACE-B and so on until
the eight total vertices for FACE-A and FACE-B are finished. Then we
do FACE-C FACE-D FACE-C FACE-D and so on and so on until we've got a
complete shape.

Unfortunately since we have face-specific processing, and this
alternating structure was so odd, I had no choice but to just list out
all the indicies and handle them appropriately. Maybe there's a
mathematical way of grouping it but I certainly couldn't think of it.

Anyway, the structure of the UV values in the CubeMesh was odd as
well - I think they were deliberately structured to sort of wrap
around the Cube. This meant we had to handle each face differently to
get the exact UV values we needed. Kinda ugly code, but it works.

Now I need to start working with the UV2 values to pack in the light
data... or light reference data. Or whatever.

---

