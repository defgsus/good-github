## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-18](docs/good-messages/2022/2022-02-18.md)


1,406,385 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,406,385 were push events containing 2,284,204 commit messages that amount to 170,481,593 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[37184d33a2...](https://github.com/ammarfaizi2/linux-block/commit/37184d33a201ddcc4c09578dc1aabcb193e44653)
#### Friday 2022-02-18 00:00:27 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `s = ror32(s, 5) ^ x`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear function fits this
bill quite well, easily extending to the larger state size and to the
fact that we're mixing in more than just the cycle counter. By picking a
linear function with no non-trivial invariant subspace, unlike NT's
rotate-xor, we benefit from the analysis of <https://eprint.iacr.org/2021/1002>.
This proves that linear functions with only the trivial invariant
subspaces make very good entropy extractors for the type of complex
distributions that we have. It suggests that we extract entropy via
`s = (a * s) ^ x`, where a is the transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [gnprice/zulip-mobile](https://github.com/gnprice/zulip-mobile)@[e117df5f73...](https://github.com/gnprice/zulip-mobile/commit/e117df5f7375eecf6d50156038e6f699e3a6c04c)
#### Friday 2022-02-18 01:43:53 by Greg Price

Fix major startup lag, by using Animated.loop instead of giant duration

This was always a silly-looking hack: what we really want is for
this animation to loop indefinitely, and we do that by saying it
runs for 1000 seconds.

It turns out that doing that makes it extremely slow to start up!
Specifically, in my desktop Android emulator (which is typically
1x-2x the speed of my physical Pixel 4), it takes about 500ms.

Worse: it blocks the entire JS thread while it does that.  So
the app's whole UI is stalled.

Because we use this at startup (in LoadingIndicator), it's been
adding that 500ms of lag (likely more like 1000ms on many devices)
to our startup time since forever.  Moreover, we use
LoadingIndicator in the "Connecting..." banner... which there's
*four* of, one on each of the app's main-screen tabs.  So when we
start loading -- which is promptly after each startup, if you're
already logged in -- the UI hangs for another 2000ms, or more
depending on device.

There are a number of things we could do here.  It seems like a
performance bug in RN's `Animated`.  Also we could shorten the
1000 seconds to like 100 seconds, or 50 seconds -- better that
you occasionally see a stopped spinner, if you've already waited
a long time, than that you find the app completely stuck for a
full second or more every time you start it.

But in fact a very simple solution is available: if you take a look
at the upstream docs for Animated:
  https://reactnative.dev/docs/animated
there is built-in support for just explicitly having a loop.
There's no need for this hack at all.  Even in RN v0.47.2, the
version we were using when this hack was introduced in 2017 in
6594f8ebc, there was an `Animated.loop` and there was no need
for this hack.

So use that.

---
## [rems-project/cerberus](https://github.com/rems-project/cerberus)@[2a8f7721b3...](https://github.com/rems-project/cerberus/commit/2a8f7721b34cc13fd6db9fd6a6e775520d2f45de)
#### Friday 2022-02-18 01:49:29 by Thomas Sewell

Tweak nested time log to ~JSON

Maybe it would make sense if the log parsed as a native
JSON object and/or python value? Some progress in that
direction, but it isn't exactly working out great.

(It's annoying that JSON doesn't seem to permit a trailing
comma, e.g. [ 1, 2, 3, ], so that the printer needs either
state or silly hacks to avoid printing too many commas.)

---
## [WaffleLapkin/mbkb](https://github.com/WaffleLapkin/mbkb)@[b0d3ee5b57...](https://github.com/WaffleLapkin/mbkb/commit/b0d3ee5b5789fc2a7b291201f8bad0cbf0d3d435)
#### Friday 2022-02-18 02:54:16 by Maybe Waffle

Sketch: Add physical layout interface

This commit feels comparatively very big...It is not *that* big -
`git diff --stat --staged` says 6 files changed, 179 insertions and
97 deletions. But still...

My current design idea for this library is to have +- 3 layers:
- Physical — represents where keys are physically located, how they are
  connected to the micro-controller, etc. It is sketched in this commit.
- Logical  — represents mapping of keys to their meaning. For example
  key#2 [on the default layer] is an English A,
  key#13 is a sticky shift,
  key#42 is a conditional layout switch,
  ...
  It is not yet implemented.
- Protocol — represents keyboard<->PC communications, in 99% of the
  cases it's USB. This is partially implemented, though I think I'll
  refine both interface and implementation in the future.

There is also a visual/topological representation that can allow
configuration interfaces to show roughly how keyboard looks. I don't
know how the interface should look and where it should be (I sketched it
as a submodule of physical layer), but I guess I'll figure this out with
time.

------------------------------------------------------------------------

I've also changed the example/testing binary. It previously continuously
printed the "Lorem ipsum [...]" text. It was ok as an example that shows
that I've made protocol layer work (at least a little bit). But it is
of course far from a real keyboard and I wanted an example that is
closer to the reality (which I hate, but still).

With this commit the example/testing binary (see `f103/` directory) is
now a 4 button keyboard! It is not much, but I'm still proud a bit :')

The setup is as follows:
- stm32f103c8 micro-controller aka bluepill
- 4 buttons
  - "Right" sides connected to the ground
  - "Left" sides connected to pins B12, B13, B14 and B15
- st-link (v2?) to upload binary to the micro-controller (& maybe debug
  but I haven't tried this in a long time)

Everything is very sketchy because I still don't have a soldering iron
and all the contacts are very bad (sometimes I need to hold wires in a
particular way just so everything works).

I have a picture of my sketchy setup, to get it run the following:
```shell
git notes --ref=files show commit > sketchy.jpg
```
Where `commit` is replaced with this commits hash.

The picture is made on my pxl4a, then scaled down to 256x256 via Krita,
then drawn on top of via Krita and my mouse with #88ff82 color, and then
stored via git notes.

I've tried to compress it further, but it started loosing too much
details and wasn't vibing with me, so I stopped here.

And yes, I know that this is abuses git notes. 1) I don't care 2) I live
in another city, what can you do to me? 3) This has a great cursed vibe.

------------------------------------------------------------------------

As a side-note: I've noticed weird behavior with the example keyboard.
When holding multiple keys at the same time, only the last one is
repeated and when releasing the key that was last pressed, no keys are
repeated.

Example:
1. I press `A` (prints `AAAAA`...)
2. I press `B` (stops printing `A`s, prints `BBBBB`...)
3. I release `B` (prints nothing, even though `A` is still pressed)

I have no idea what causes this issue or how to fix it, so I just record
the fact that it happens here. That's all I can do at the moment.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[2351c46bd7...](https://github.com/san7890/bruhstation/commit/2351c46bd7d66196ec1dea4946378b53d8e35163)
#### Friday 2022-02-18 03:54:46 by san7890

The Science Lobby; Or, How I Learned To Embrace Congruence

This is a multi-factorial PR in a broader series meant to address the fact that areas are too massive. Today's episode includes the following:

This section of the halls are just incredulously fucking massive. I think the reasoning behind this (I may be wrong) is that no one bothered to make an area/sprite for the very distinct Science Lobby on Delta (as well as Meta and Tram). This PR is someone bothering.

To achieve good symmetry, I also made the area colloquially known as the Medbay Lobby it's own area as well with the already-existing area. Had to shuffle some stuff around, but I think it's not incredibly ugly. Peep a look:

---
## [NEXUS-003/kernel_xiaomi_sdm845](https://github.com/NEXUS-003/kernel_xiaomi_sdm845)@[4914a75846...](https://github.com/NEXUS-003/kernel_xiaomi_sdm845/commit/4914a75846c6834801d11a30352e7edf60e3d22e)
#### Friday 2022-02-18 04:07:10 by tanish2k09

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
## [team8/drive-practice-2022](https://github.com/team8/drive-practice-2022)@[7a5bf59ab0...](https://github.com/team8/drive-practice-2022/commit/7a5bf59ab06afa3bffa5d9b3cfe270cf6f0771f4)
#### Friday 2022-02-18 05:21:11 by Charger1256A

I am bored in english class and have nothing to do I made some improvements to dis thingy. Does anyone wanna huddle cuz I am bored. Plza save me :pray:. Idk what I am even doing that this moment. I am just going on a tanger or ranting, idk the diffrerence. I should be writing my synthsis essay, but that is so boring, so I am not going to. Please show up to room 404, it would be much appreciated. What the heck am I even doing rn? also zach, do you still have my code from csa? If so can you take a picture and send it to me? also everyone should follow Luca on insta and not follow him on git because I am bored. Currently it is 1500 and there is nothing for me to do. I complete my first lewdle today, so that was fun. Ohhh I should make this my blog or something idk. Who is coming to lab today? I love this channel because nobody ready commit messages. Or at least no one I am afraid of of. Except shalen ig, idk if he even is in this channel. i hope no mentors join later and read this message because I will get roasted. If mentors are reading this, I love you guys lol thanks for supervisising and helping us finish our bot. If Zach readin this then he probably thinking to himself what is this man doing. If Luca is reading this he is def gonna try and 1 up this commit message. If rkim is reading this he is like does Adity have have a life? and tbh idk if I do lol. If Ryan Lee is reading this message he will be scared of coding forever, but let me tell you now you should code this is not what coding is like. If Alexis is reading this, she probably didn’t get this far because she is too lazy to read my commit messages. the guy sitting next me is watching a documentary about Kanye and he says it is interesting. WHat do you guys think? I am literally just writing whatever pops into my heada and that just popped into my head. There are not lights in this room so I feel super sleepy. TBH i just want to go to a comp rn cuz i am bored. Luca, Alexis did you guys sign for FF? you guys should. How long are you guys staying at lab today? How do I see how many words this commit message is? it is now 1506 a. When I push I hope I dont get any error messages when I push cuz that would be annoying. What is buildkite, shoudl I integreate it into this channel. For young people. dont take ap lang otherwise you will end up doing this. This concluded my long rant bye. I might be back for more soon

---
## [terilondon/myflextest](https://github.com/terilondon/myflextest)@[42d5a7de40...](https://github.com/terilondon/myflextest/commit/42d5a7de407ce2db51e2317e0dbb950fba6282fd)
#### Friday 2022-02-18 06:01:33 by terilondon

fuckin hooks can suck it rn nicole dont u dare solve all of this without me ima die mad about it ok smooches night night

---
## [dfrank2781/week-06-murray.md](https://github.com/dfrank2781/week-06-murray.md)@[0fc8395006...](https://github.com/dfrank2781/week-06-murray.md/commit/0fc8395006093ac489c2e0baf41db2bd9276ae04)
#### Friday 2022-02-18 06:08:35 by dfrank2781

Create week-06-murray.md

In my opinion, I believe Murray's predictions are somewhat accurate. I don't think that they will be 100% true though, as I feel as if some of his predictions are far fetched. I don't believe it will be the new form of "serial drama", which I'm not completely sure what was meant by this. I do, however believe, that it's true when he says that virtual environments are an extensional of the fictional world. This is present now in ways such as simulations, as well as social interactions in my opinion due to them all being associated with real life encounters. 

The Mandalorian uses multiple forms of digital technology in order to achieve the effect it achieves. According to further research, this is all thanks to pre production  work. Lots of time has been spent on VFX workflows well before the principal photography deadline, according to the ibc.org article "Behind The Scenes: The Mandalorian's Groundbreaking Virtual Production. It relates very much so to what Murray was referring to in the way that their stages are nearly all very technical, leaning more into a virtual reality than anything else. VFX, Parallax, and enhanced LED lighting also are present on this set. Parallax, which according to the aforementioned article, as a camera effect where the camera is moving rapidly alongside a set as a character moves, in order to make it seem as if you're following right along with them. This adds a more intense, dramatic affect to the film. Lastly, LED lights, which also include the reflection, refraction, and enhancing of specific color lights, also add a virtual affect to the set of the Mandalorian. As stated in the article, this creates special affects such as sun glares, light, and even darkness as if it were actually happening right there and then in the moment, in real life.

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[2bf47f773c...](https://github.com/osamuaoki/qmk_firmware/commit/2bf47f773c389d99c45712e6353484225057eb59)
#### Friday 2022-02-18 08:57:01 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [markbirss/inxi](https://github.com/markbirss/inxi)@[2feaf0b853...](https://github.com/markbirss/inxi/commit/2feaf0b853d38635badf5375a354c17dd221df93)
#### Friday 2022-02-18 09:10:27 by Harald Hope

Thanks manjaro user alven for finding a bunch of corner and not so corner case
errors, glitches, documentation oversights, etc.

This is a point release between the coming full CPU refactor and the current
set of bug fixes and issue handlings.

This release also contains the debuggers for the new CPU data logic, which are
important to get this CPU refactor stable and reliable across old/new systems,
different operating systems and platforms.

Wanted to do this intermediate releaase to get the current fixes out, which
make inxi overall better for CPU issues, but do not handle the core requirement
to do a full refactor.

--------------------------------------------------------------------------------

CORRECTION:

1. On release notes for 3.3.08: due to a long delay to get real debugger data
from the person who had the issue, but finally getting it after the release of
3.3.08, there was NO bug in ps wwaux output. Something else was creating the
linewraps, maybe the subshell, it's basically impossible to know since we never
got a real debugger data set, which is the only real way to get the actual same
data inxi will see.

Was it a subshell wrapping the output? We just can't know, nor are we likely to
ever find out.

This highlights very well however why some issues are essentially impossible to
ever fully resolve without the --debug 22 dataset. This bug/fix is definitely in
that class of issues.

It's never good to accuse another program of having a bug when it doesn't, so
sorry to ps authors, no bug or issue exists for ps in this area.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. wiryonolau issue #259 points out that if --tty is used, default IRC filter
rule is still active and on. Because his case appears to be from an autostart
using Bash, which then gives up to find the parent at dash, which then makes
inxi believe it's in an IRC shell client, that issue doesn't appear to be
resolvable.

--------------------------------------------------------------------------------
BUGS:

1. Documentation, help menu and man page showed wmctl instead of wmctrl,
which for someone who reads the help man, leads to command --fake wmctl failing.
Thanks manjaro user alven for finding this typo.

2. For dmidecode cpu data, had global total values for cache that could result
in wrong output values, 2x or more wrong for L1 / L3 cache on linux. Difficulty
is preserving that data for bsd, which in general do not show phys cpu counts,
and thus make showing totals off. Created new '-total' item for each L cache
type, which will handle > 1 cpus, and also can be used to determine if > 1 cpus
present!.

3. Manjaro user pointed out that hub types were wrong, this is because inxi was
using the INTERFACE ID values for hubs instead of the TYPE values. For all other
device types, INTERFACE is correct, but for hubs, we needed TYPE, so fix is to
detect INTERFACE 9/0/0 and if TYPE present for that, swap.

--------------------------------------------------------------------------------
FIXES:

1. For > 1 cpu systems, with dmidecode sourced cpu cache data, can now determine
physical cpu count based on comparing L2 and L2-total values. This means that
when dmidecode is used on BSD for CPU data, inxi may now be able to deduce that
it is a > 1 cpu system.

2. Forgot to set $run{'filter'} to 0 for whitelist start client detection.

3. Going along with bug 3, changed 'Full speed (or root) hub' to:
Full speed or root hub, to make more clear that it's one or the other, or both.

4. For apply_filter(), added test if <superuser required> just return the
string.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. Going with bug 1, and fix 1, for > 1 cpu systems, will now show for all
cache: items L1: 2x 1.5 MiB (3 MiB), same for L2 and L3. This is far less
confusing than showing the totals without explaining what they are.

2. Going along with 1, now root is not required to show L1 and L3 -Cxx on Linux
as long as the system is reasonably new, about after 2008, and has getconf -a
supported. That support is came in somewhere around 2.10, not sure exactly when.
Debian Etch had it, Sarge did not, Ubuntu 9.10 had it. Tinycore does not have
getconf at all. This will probably be replaced by a more robust full cpu /sys
data tool.

3. Added ht to default short -Cx flag list, that should show, and it's short.

4. Added --no-filter to activate -Z, --filter-override isn't consistent with
other --no-xxx options, even I forgot it. No changes, just another way to use
-Z.

5. For issue #260 added pch as a new sensor output type, it's kind of a builtin
southbridge / northbridge in the CPU die, but it's not a core, and has a
different temp. Will anyone even know what pch is? probably not, but who cares.

--------------------------------------------------------------------------------
CHANGES:

1. No longer showing for > 1 physical cpu systems the sum total of L1/2/3 cache
data. Now shows per cpu L1/L2/L3, and if > 1 cpu, shows for example:

cache: L1: 2x 512 KiB (1024 KiB) L2: 2x 2 MiB (4 MiB)  L3: 2x 20 MiB (40 MiB)

For single physical cpu output remains the same:

cache: L1: 576 KiB L2: 3 MiB L3: 16 MiB

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updated help/man for L1/L3 cache -Cxx changes.

2. Updated man and help to suggest -Z for --tty.

3. Forgot to note -v 7 adds -f, added to man/help.

--------------------------------------------------------------------------------
CODE:

* Added 'getconf -a' to debugger, that may be usable for cpu cache data, need to
gather data on that to confirm. that's regading issue #257 cache glitches.

2. Removed all * $physical_count for cache data in cpu_properties, that is now
handled by creating string with cpu count, per cpu caches, and total in parens.

3. Added in fallback failure case for the ZFS file system issue exposed by
accident in issue #258 - will now log in debugger the error, so we can try to
find what is going on there, impossible to reproduce until we find what zfs or
more likely, freebsd, changed there. Could be hyper specific, some weird thing
like a person making a zfs device name with space, impossible to guess. Note
that since the freebsd user declined to supply any data to help resolve this
issue, then closed it, we're back where we usually end up with FreeBSD issues,
either a Linux user (or worse, me) willing and able to find the issue and supply
the debugger data required shows up, OR the issue is ignored as valid but
impossible to resolve.

RANT: Note that this also confirmed to me that in order to preserve my own
sanity and not waste endless hours trying to get data, from now on, unless
utterly trivial, if a FreeBSD user refuses to promptly supply the required data,
the issue will be closed with a freebsd-closed-no-data-supplied label, which
means, valid but not possible to solve due to user refusing to help me help
them.

Come on FreeBSD users!! If you want help, and inxi to support your distro, help
me help you!! If not, then why are you even filing an issue in the first place?
Do you expect faeries to spread magic bug / issue fixing faerie dust over inxi
and then activate it with their little wands? This is growing tiresome to be
honest because it's so utterly predictable.

4. Shuffled order of sensor type detections, there was a slim chance that a non
gpu sensor type could have string intel in it, so put the gpu sensors second
to last, before 'main'.

5. Started refactor of cpu core/cache logic. Added feature to cpu_arch, and
changed it to cpu_info since now it gives by vendor/family/model/stepping both
micorarch and cache/core math array returns. Also started refactor to make more
predictable, with increased comments, about what is going on in cpu_properties
to avoid breaking existing correct results.

6. Added to --debug /sys cpu data globber tool, that will help debugging the new
/sys cpu data feature, will let me insert the file data directly into the logic.

7. Added CpuItem::cpu_data_sys() with debuggers, that will now start collecting
user cpu data whenever the debugger is run, though it's not active yet.

8. Set $Data::Dumper::SortKeys = 1; dugh, could have saved big headaches if had
found this before. Makes all keys sorted cleanly, gets rid of random hash sorts.

---
## [poettering/systemd](https://github.com/poettering/systemd)@[de90700f36...](https://github.com/poettering/systemd/commit/de90700f36f2126528f7ce92df0b5b5d5e277558)
#### Friday 2022-02-18 09:50:22 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>

---
## [chandu078/kernel_oneplus_sm8350](https://github.com/chandu078/kernel_oneplus_sm8350)@[71af2706ad...](https://github.com/chandu078/kernel_oneplus_sm8350/commit/71af2706adb333f7577dec9e8fcab8a9e5a82977)
#### Friday 2022-02-18 10:18:10 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: chandu078 <chandudyavanapelli03@gmail.com>

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[e5ac022a56...](https://github.com/zx2c4/linux-rng/commit/e5ac022a5606d7a2056834b0750919a0b536fe97)
#### Friday 2022-02-18 10:22:43 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `s = ror32(s, 5) ^ x`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear function fits this
bill quite well, easily extending to the larger state size and to the
fact that we're mixing in more than just the cycle counter. By picking a
linear function with no non-trivial invariant subspace, unlike NT's
rotate-xor, we benefit from the analysis of <https://eprint.iacr.org/2021/1002>.
This paper proves that those types of linear functions, used in the form
`s = f(s) ^ x`, make very good entropy extractors for the type of
complex distributions that we have.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[49bb20bbcd...](https://github.com/Gullwing-door/restoration-mod/commit/49bb20bbcdd563dc83518a19482985676a270cf2)
#### Friday 2022-02-18 10:42:58 by SonicSoapyBoi

HOLY SHIT WHY YOU HAVE SWEDISH COLORS?!

Fixed Zombie Zeal Cloakers having swedish textures
-Added Summers and his Co. back to Boiling Point
-Added Winters to First World Bank (i did some tests here and he works good here)

---
## [TenSeventy7/android_kernel_samsung_exynos9610_mint](https://github.com/TenSeventy7/android_kernel_samsung_exynos9610_mint)@[006123e284...](https://github.com/TenSeventy7/android_kernel_samsung_exynos9610_mint/commit/006123e2842b5400ce88f6fdbe59535d87989967)
#### Friday 2022-02-18 12:17:05 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Signed-off-by: John Vincent <git@tenseventyseven.cf>

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[889758ccf6...](https://github.com/ammarfaizi2/linux-block/commit/889758ccf6ccf0e80e84d3cdaa06939bb3e43c23)
#### Friday 2022-02-18 12:19:08 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `s = ror32(s, 5) ^ x`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear feedback shift
register fits this bill quite well, easily extending to the larger state
size and to the fact that we're mixing in more than just the cycle
counter. By picking a linear function with no non-trivial invariant
subspace, unlike NT's rotate-xor, we benefit from the analysis of
<https://eprint.iacr.org/2021/1002>.  This paper proves that those types
of linear functions, used in the form `s = f(s) ^ x`, make very good
entropy extractors for the type of complex distributions that we have.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. And the
performance is better, which perhaps matters in interrupt context. I
would like to emphasize, again, that the purpose of this commit is to
improve the existing design, by making it analyzable, without changing
anything fundamental to the existing design. There may well be value
down the road in changing up the existing design, using something
cryptographic, or simply using a ring buffer of samples rather than
having a fast_mix() at all , or changing which and how much data we
collect each interrupt, or a variety of other ideas. This commit does
not invalidate the potential for those in the future.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [gnosis/gp-v2-services](https://github.com/gnosis/gp-v2-services)@[107f76cf12...](https://github.com/gnosis/gp-v2-services/commit/107f76cf122a9fdaf3dcea81bd1abe7c8b6b2444)
#### Friday 2022-02-18 13:55:08 by Nicholas Rodrigues Lordello

Introduce external prices type (#1669)

Fixes #1666 

This PR introduces a new `ExternalPrices` type for external prices from the `/auction` endpoint. Internally, it tracks this as exchange rates from tokens to Ether (although this detail shouldn't "leak" out of the type). It also internalizes the logic of how to convert a token amount into a native asset amount (so you don't have to remember if you should divide or multiply by the price 😵‍💫).

Additionally it verifies that the prices returned by the `/auction` endpoint satisfy our external price invariant (i.e. Ether prices are 1).

One notable small change in behaviour (which should have no practical bearing) is that the `SellVolumeFilteringSolver` now panics for orders without an external price. Since all orders should have external prices anyway, and we don't actually use this solver anymore, the behaviour of the driver should not have changed.

Overall, I don't think this is a huge improvement (when I opened the issue #1666 it seemed a lot more of a cut and dry improvement, however, as I implemented it, I'm not so sure any more...). Eager to hear your thoughts and feedback on the change!

### Test Plan

Adjusted unit tests to use new type. They continue to pass. It is worth noting, however, that now, external prices need to have a concept of a "native token", this means that unit tests that used external prices were modified to have one of the tokens be the native token.

---
## [Ironnhawk/Skyrat-tg](https://github.com/Ironnhawk/Skyrat-tg)@[d504fe76f4...](https://github.com/Ironnhawk/Skyrat-tg/commit/d504fe76f4935518b45f3ba1ec6d935af5f16b55)
#### Friday 2022-02-18 13:59:20 by SkyratBot

[MIRROR] Fixes harddels in pinned module code, cleans up a musty pattern that I want to die [MDB IGNORE] (#11319)

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

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

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [lesthack/dailyupdate_github](https://github.com/lesthack/dailyupdate_github)@[ad9cfd8ccd...](https://github.com/lesthack/dailyupdate_github/commit/ad9cfd8ccd8def28c2f5699ce0228bdc9fa24df3)
#### Friday 2022-02-18 14:37:52 by Jorge Hernández

Joy Again - unknown - Sorry You Didn't Get to Kiss That Boy You Wanted to Kiss

---
## [SuffolkLITLab/ALKiln](https://github.com/SuffolkLITLab/ALKiln)@[fe728649d3...](https://github.com/SuffolkLITLab/ALKiln/commit/fe728649d3b5a7be2d6cbf4eff90857d63a2986b)
#### Friday 2022-02-18 15:04:17 by plocket

Update our package's dependencies for v4 (#503)

I'm thinking this is just going to be for v4. Not bothering with this for v3 unless we absolutely have to since none of the vulnerabilities are severe. My current rationale is that the more work we do to maintain 3, the less work we can do getting v4 ready for release. Ready to hear opinions.

- Close #164, update cucumber to v7
- Prepare for v8 of cucumber because I won't remember it later
- Close #394, update puppeteer
- Update our version of node (and that of our action that we'll run for other people's libs). [Addresses #393 so we can use the suffolk npm org package.]
- Use `npm audit` to fix the remaining vulnerabilities (now 0)
- [Remove package.json as discussed in #489 to align our tests' behaviors with those of our users.]

* Update action.yml node to v17

* Update from cucumber v6 to v7. See details.

See https://github.com/cucumber/cucumber-js/blob/main/docs/migration.md#migrating-to-cucumber-js-7xx

Only use cucumber setDefaultTimeout globally and use a shim that replicates the fix in v8 that lets you do custom timeouts more easily so we can still give enough time for steps that may need more time.

Use all caps for statuses.

Test screenshot step.

Btw, the cucumber test output visually looks a bit different now - when a scenario passes, all the steps pass too.

Sorry about the little comment changes, etc. Tried to remove a lot of those incidental unrelated changes.

* Update puppeteer to latest (13). See details below.

- page.waitFor -> page.waitForTimeout and page.waitForSelector (Got deprication notice. See https://github.com/puppeteer/puppeteer/issues/6214.)
- remove removeEventListener (we'd need to change it to removeListener anyway - v4.0.0 and see https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#eventemitterremovelistenerevent-handler). For now we'll count on page close taking care of it, just in case removing it would prevent multiple-file-downloads.

* Update GitHub worflow node version, tweak changelog item order

* Fix npm audit vulnerabilities and update action.yml cucumber

* Pin the colors lib in action.yml

* Remove package-lock.json #489, use kiln v4 for users, CHANGELOG

* Fix custom timeout, remove duplicate report entry, as per review

---
## [ExactExampl/Kirisakura_bonito](https://github.com/ExactExampl/Kirisakura_bonito)@[83cacca694...](https://github.com/ExactExampl/Kirisakura_bonito/commit/83cacca694d1a144b85d8d305093ade5c34b3045)
#### Friday 2022-02-18 16:41:04 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [BixConcept/tutoring-backend-express](https://github.com/BixConcept/tutoring-backend-express)@[7e935b90ad...](https://github.com/BixConcept/tutoring-backend-express/commit/7e935b90ad5b2fa4ad321bd096bb7bc5088b46ca)
#### Friday 2022-02-18 17:01:41 by 3nt3

fix fucking syntax error fuck you prettier

Signed-off-by: 3nt3 <gott@3nt3.de>

---
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[78f998dddc...](https://github.com/bellomia/MOTTlab/commit/78f998dddc859f3b578d80323757821abbe4ec45)
#### Friday 2022-02-18 17:20:48 by Gabriele Bellomia

First try at square lattice

A lot of problems:

- Despite carefully following gftool implementation we apparently get a wrong DOS, from imag(gloc_0).

- The Symbolic Math Toolbox function ellipticK() is so much sloooooooooooooooow, unusable, it's computing time dominates everything. I'd guess I should have forseen this. A symbolic implementation to process very dense numerical samples of complex numbers. Such a bad idea. Overall a bethe lattice loop takes ~300ms, while a square lattice loop around 24s, that is a x80 slowdown. Damn it.

- Anyway I don't want to force a symbolic math dependency.

HENCE

We'd try the good old fft-powered numerical way.

1. Generate the DOS by whatever, numerical, method (even elliptic integrals, but numerical, probably the standard ellipke() MATLAB function). If things go really bad fuck it, let's generate it one time and save in binary.

2. Go by definition of self-consistency: Gloc(z) = H[DOS](z-Sloc(z)), an Hilbert transform to which we feed the DOS (generated or tabulated, whatever)

NB1) Frustration apart, let's try to avoid tabulating the DOSes, we want flexibility with the energy sampling and interpolating / downsampling could be cumbersome.

NB2) If we succeed generating the DOS we should consider avoiding regenerating at each loop. Instead of passing around a string identifying the lattice we should then consider passing directly the generated DOS.

NB3) This has to perform better than the symbolic method in gftools, BUT, it could still be significantly slower / less accurate than the current implementation, for the Bethe lattice. Maybe let's make the DOS argument optional and fall back to the bethe lattice by default. This way the blazing fast, reliable, bethe implementation would be preserved.

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[1bd3a1ee78...](https://github.com/tannerhelland/PhotoDemon/commit/1bd3a1ee7848e4ac89590e9ae45281955db96880)
#### Friday 2022-02-18 18:11:38 by Tanner

MULTIPLE SELECTIONS ARE ACTUALLY GONNA WORK!

This commit is just a placeholder, and only "add" combine mode is implemented, but for the first time in PhotoDemon history, the program is capable of functional multiple selection support.

This is a placeholder commit because there are a billion details still to work out, including a lot of critical feature work, but the core fundamentals are all in place and they work without crashing the app.  I honestly had my doubts that I would ever make it this far... but hey, hope springs eternal!

This commit may not look like it contains much code, but there are approximately two thousand rounds of work that were written then deleted as I tried to to graft multiple selection behavior onto PD's ancient selection engine.  A lot of attempts didn't go well so I had to back up and start over, but I finally think I've arrived at a solution that won't require a total rewrite of the app.  (In a perfect world, that would be lovely and probably produce a much tidier selection engine core, but I don't have infinite time so I have to be practical about how I implement new features.)

A lot of debug messaging is strewn throughout this commit, but don't worry - I'll deal with these as I work through the known bugs associated with those program areas.

Next up is getting border rendering working correctly when multiple selections are active (only masks are calculated right now), then I need to get "subtract" and "intersect" modes working.  Then there are a ton of UI issues left to solve.... but the worst of this project is finally in the past, I think.

---
## [khonsulabs/bonsaidb](https://github.com/khonsulabs/bonsaidb)@[b2086b60e1...](https://github.com/khonsulabs/bonsaidb/commit/b2086b60e1b795b5734f3dcd4d9dae2e78ffb0e5)
#### Friday 2022-02-18 18:34:38 by Jonathan Johnson

Add lz4 compression support

Closes #185

This is a first pass at compression support. I believe that ultimately
we'll want to support both zstd and lz4, but right now feature flags are
really annoying to implement. When we can implement namespaced features
(#178), we should revisit adding multiple compression backends and
options. lz4-flex has a faster unsafe option that can be enabled
optionally, but I've kept disabled in the spirit of BonsaiDb's "safe"
defaults.

From my research, zstd will be preferred when storage is at a premium,
but lz4 *should* be faster in general. I want to write a good benchmark
suite, because I believe the relative performance will potentially be
hardware dependent, and users should be able to gauge what works best
for them.

---
## [VOREStation/VOREStation](https://github.com/VOREStation/VOREStation)@[46b6bbaf74...](https://github.com/VOREStation/VOREStation/commit/46b6bbaf74996c9d7ffc25125491e2293e136a1c)
#### Friday 2022-02-18 19:07:28 by VerySoft

Misc Tweaks

Fixes a space vine runtime

Makes it so space vines can't climb stairs (because that leads to practically unkillable stacks of vines that lag the server)

Makes it so space vines can't grow on open space (because you usually can't kill vines if they're way out in open space and that doesn't make much sense anyway.)

Attempts to limit the maximum range of plant bioluminescence (having hundreds or thousands of dynamic light sources with maximum possible light range seems to lag the server)

Adds a funny dog that no one should ever actually spawn but I will one day as a joke and everyone will cry. (its base form is actually not hostile so if you kill that one the hell you earn will all be on you)

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[bc0ea7cd46...](https://github.com/facebook/pyre-check/commit/bc0ea7cd46402fe4c5ee5405a048a8ab676ad081)
#### Friday 2022-02-18 19:24:11 by Shannon Zhu

Preserve existing type information in local inference

Summary:
At the risk of opening a bigger can of worms, my investigation into why we inference codemod diffs needed to be abandond bc weren't accounting for the types of parameter default values (see context: D34161066 (https://github.com/facebook/pyre-check/commit/787e576f124f2992e0e848b0a0f167e05338aed0)) has uncovered some broader questions about how we structure the inference fixpoint.

General structure of pyre inference type propagation, for context:
1. We run TypeCheck's initialize state to get a starting set of local annotations from the define signature
2. We run Infer's `initial_forward` modifier to reset some `Any` annotations back to `Bottom` so we don't lose type information we gather in the subsequent pass
3. We run Infer's `forward`, which special cases some unassigned call expressions, etc., but primarily just shells out to Typecheck's `forward` to propagate type information.
4. We pass the resulting state into Infer's `initial_backward` to add type information for a dummy `$return$` local variable from the return annotation if it exists, something normal type check can ignore
5. We run Infer's `backward` which special cases some assign statements and return statements to propagate type info
6. We continue the forward/backward cycle until a fixpoint is reached.

The issue at hand here is that we aren't actually gathering all possible types that a local variable might have over the course of the function to suggest an annotation.
There are some forward-specific and backward-specific assumptions we're making that may make sense in a forward-only or backward-only world where we want correctness at each point of the control flow, but don't really make sense in the combined inference setting here where we recommend one annotation for the local variable overall.

**Forward loses info (not addressed in this diff):**

```
def foo(x = 1) -> None:
   x = "string"
```

Will annotate the parameter `x` as having type `str`.

This is because for the purposes of forward type propagation, if there isn't an immutable type given to a value, all we care about is the most recent mutable value assigned to a local. It makes perfect sense to throw away the previous type information as we learn new type information.

However, for type inference purposes, as long as we are allowing local variables to change their type over the course of a function scope, shouldn't we want to suggest the type annotation that can accommodate all of the types that local takes on at any point in the function? ie., stop throwing away the previous annotation info and join it in instead?

**Backward loses info (addressed in this diff):**

```
def foo(y = 1) -> str:
   y = unknown()
   x = y
   return x
```

Will annotate the parameter `y` as having type `str` despite it clearly possibly sometimes being an `int`.

Side note: If we really wanted to be precise about propagating types backward, seeing an assignment like `x = y` should actually completely wipe everything we know about `x` since we are going bottom-up. `x` could be literally anything before such an assignment, and our post-assignment state would not be affected.

However, we don't wipe this info, precisely because we are OK making some theoretical correctness tradeoffs for retaining information that will be relevant to a suggested annotation the vast majority of the time in the wild.

This doesn't need to be extrapolated much further to say that we probably should be OK with collecting type information across the local scope of the variable to make our type inference suggestion the most useful and landable, rather than wiping/dropping information that is specific to forward-only or backward-only per-statement correctness.

 ---

Thoughts/concerns welcome - so far this stack doesn't touch forward logic yet, so it won't fix the original common issue during the codemod pass where `None` is often used as a default param value and we don't make the suggested annotation optional:

```
def foo(x: int = None) -> None:
   ...
   x = 1
   ...
```
I might not prioritize fixing all of this logic right away, but since this can of worms was opened figured this is a high level choice we should iron out.

Reviewed By: dkgi

Differential Revision: D34161077

fbshipit-source-id: 7ad64c103f5fd2cf55620262e535ce118d609279

---
## [raupy/AYTO](https://github.com/raupy/AYTO)@[0858965d9e...](https://github.com/raupy/AYTO/commit/0858965d9e7dee59d824c72776f72726b99fab10)
#### Friday 2022-02-18 20:37:18 by raupy

fix: resolve trouble with special person

in function get_permutations_from_comb:
vanessa's match doesnt necessarily belong to the single boys. only if length(single_boys) != length(single_girls)

___________________
additional feature: add a functionality in the is.possible function so that we cant look in the "future" and have to work with the insights we have until the current matching night
TODO: there should be two options: progressively or retrospectively

---
## [matthewgismondi76/kodachi-maybe](https://github.com/matthewgismondi76/kodachi-maybe)@[3c09fab74d...](https://github.com/matthewgismondi76/kodachi-maybe/commit/3c09fab74d697452e60e2f3c9dc29d99fcd07bbe)
#### Friday 2022-02-18 22:37:47 by Matthew Gismondi

Add files via upload

After the Ls it stopped letting me upload anything, and I got so frustrated anyway because of the impossibility of just uploading a file tree. When I tell you that I am fighting against more than just what you see as being there, I am not just saying that I am fighting against some hacker kids who are trying to be better than God. I am saying that I am also having to maintain favor among every spiritual influence involved as well since I am stuck with their politics instead of the ones from God that I should be able to claim through Jesus Christ as having freedom through Him. Because I am not doing anything wrong, but I suspect these files are full of malicious intent, and if the angels are under the impression that I am working against God then they might not protect me as much. And if there are demons who think I am working against them they might make my arm itch or something at just the wrong times to mess up whatever they want to. And if people perceive me as a threat for any reason they might just .... This is not just a simple game of cowboys and indians anymore. This is a game of guerilla warfare where even humanity is not a safe assumption.

---
## [ylorant/Hedgebot-admin](https://github.com/ylorant/Hedgebot-admin)@[58ee0e6f7f...](https://github.com/ylorant/Hedgebot-admin/commit/58ee0e6f7fd2525cf305df5f58be328ba0e0e399)
#### Friday 2022-02-18 22:40:13 by RomainOdeval

Fix somme stupid shitty useless DI ... shame on me !

---
## [matthewgismondi76/kodachi-maybe](https://github.com/matthewgismondi76/kodachi-maybe)@[3ea136b16c...](https://github.com/matthewgismondi76/kodachi-maybe/commit/3ea136b16c3915e767257ecca5b1707ab2ac58e1)
#### Friday 2022-02-18 22:50:18 by Matthew Gismondi

Add files via upload

And by the way I am not singling out grub at all. I just started there. Toby used to eat grubs and could dig them out of the dirt like a truffle hunting creature (even though that was more like a description of Blue -- or Blur, as Autocorrect preferred to call him. And sometimes there is great wisdom in Autocorrect. Sometimes Autocorrect is a cruel and evil meany-pants.) But that is why I have focused on Grub/Grasshopper and also why I know that a SOCKS5 proxy is helpful. Because of all the times Toby would stand in the doorway with a sock in his mouth that he had stolen from my roommate's room as if to say, "Your belongings may be in my house but you are still less than me. He still loves me more. And you will not take that away from me. This is the proof. I own you." There was great wisdom in that ridiculous and oversized horse of a dog.

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[af609afe70...](https://github.com/BakaKaito/Mergebot.NET/commit/af609afe708ff9fe88646a16b5991d40bd9cd0b3)
#### Friday 2022-02-18 23:30:14 by Koi

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

