## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-02](docs/good-messages/2022/2022-10-02.md)


1,799,832 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,799,832 were push events containing 2,480,828 commit messages that amount to 157,083,568 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [KDr2/rust](https://github.com/KDr2/rust)@[744e397d88...](https://github.com/KDr2/rust/commit/744e397d8855f7da87d70aa8d0bd9e0f5f0b51a1)
#### Sunday 2022-10-02 00:05:17 by bors

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
## [josephfrazier/Reported-Web](https://github.com/josephfrazier/Reported-Web)@[0ec59081cc...](https://github.com/josephfrazier/Reported-Web/commit/0ec59081cc2c28999b878521bb2d943f390b5a75)
#### Sunday 2022-10-02 00:11:57 by Joseph Frazier

Disable zoom on mobile devices to avoid unescapeable map issue (#346)

This fixes https://github.com/josephfrazier/Reported-Web/issues/344 by
preventing zoom entirely, on mobile devices:

> From https://reportedcab.slack.com/archives/C9VNM3DL4/p1657204889174239?thread_ts=1656783831.210109&cid=C9VNM3DL4:
>
> > > UPDATE: you appear to have fixed #2 by disabling pinching, but this also makes map view crash easily (on my first two tries, once it crashed and sent me back to Reported login, then it crashed and sent me to a Chrome "Can't open this page" (edited)
> >
> >
> > I don't think I've made any changes relating to pinching or the map in at least a year (if you're curious, you can see the list of changes here), so I'm not sure how to explain the difference in behavior you're seeing.
> > That said, I can try to discuss the issue:
> > > (2) map view issue #1: The only ways to get out of map view are (1) click one of the buttons on the bottom, or (2) touch the grayed-out part of the underlying page. If neither of those is visible, you can't get out of map view. This means that if you pinch the map out (expand it), even accidentally, so that the margin around the map itself is no longer visible, there is no way to get out of map view, you have to reload the page (and re-upload your photo or maybe start the whole report over, I can't remember). (You can't pinch it back in if the entire window is full of map.)
> >
> >
> > I'm curious how you were previously able to pinch-zoom the map/page such that neither the buttons or the margin were visible. When I try (on Android), I can either pinch the map, which only zooms the map while leaving the rest of the page alone, or I can pinch the margin, which zooms the entire page, but the margin is still visible because I'm pinching it.
> > Perhaps things behave differently on iOS?
>
> > Actually the map zoom issue is: if you are zoomed out at all when you enter map view (which you often are, especially on an iPad, and you may not realize it), you’re screwed, because you can’t zoom in (in order to see the buttons or margins, the things you have to click in order to get out of map view) if the only things your fingers can touch are the map itself
>
> > ohhh, I see now, and I was able to reproduce that issue. I wonder if there's a way to detect the zoom level, and prompt the user to zoom back out all the way before they can open the map
> > (side note, I think we're using "zoom in" and "zoom out" with opposite meanings. To me "zooming in" makes the things on screen bigger, and "zooming out" makes them smaller)

---
## [Foxterosa/Skyrat-tg](https://github.com/Foxterosa/Skyrat-tg)@[00d7e1f375...](https://github.com/Foxterosa/Skyrat-tg/commit/00d7e1f375b7f6f55f71d77be8c7612a6a5d6030)
#### Sunday 2022-10-02 00:45:14 by SkyratBot

[MIRROR] Rocking The Boat, er, Map Vote [MDB IGNORE] (#16083)

* Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

* Rocking The Boat, er, Map Vote

Co-authored-by: san7890 <the@san7890.com>

---
## [a3project/android_kernel_xiaomi_rosy](https://github.com/a3project/android_kernel_xiaomi_rosy)@[c36a32d1d9...](https://github.com/a3project/android_kernel_xiaomi_rosy/commit/c36a32d1d9c98808cdd651e962784e0f8a9c80ea)
#### Sunday 2022-10-02 01:16:17 by tanish2k09

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
## [amstan/Marlin](https://github.com/amstan/Marlin)@[49ee847f65...](https://github.com/amstan/Marlin/commit/49ee847f6502981b16a53492f5514cdc6967cf42)
#### Sunday 2022-10-02 01:29:50 by Alexandru M Stan

Configuration: Added Lulzbot 5 (Archim 2.2)

This inherits from my Rambo config of Lulzbot TAZ 5

Copied most settings from Configuration*.h from Lulzbot's firmware, labeled
1df0e3c64ea04ee57f0d2f8900411a9539f76436 - TAZ_5.0.1_Single_Extruder_v2
It had a bootscreen of "Marlin V1.0.0.1"

A lot of settings had to be adapted, hopefully I didn't miss anything.

Got a lot of brought over:
	* pid settings (and max duty cycle)
	* motor microstepping of 16 (still HIGH, HIGH)
	* motor currents

The max speeds/accelerations were a little wonky originally, setting
them the same with the new firmware resulted in unusably fast speeds.
The new values have been determined experimentally.

Perfect fan pwm settings are still a TODO, the 400Hz is a little
annoying, especially with the original board and part cooling fans. I would
have preferred for 30Hz, but something's wrong with the avr timer drivers.

Also added a few quality of life improvements, like fancy session management,
nicer graphics.

Also enabled LIN_ADVANCE, seems like the printer might benefit. Way better
retraction performance after it got set.

To upload: pio run --target upload -e DUE_archim --upload-port /dev/serial/by-id/usb-marlinfw.org_Lulzbot_TAZ_5_123985739853-if00

---
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[91f02f2a6b...](https://github.com/GesuBackups/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Sunday 2022-10-02 02:30:43 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [satishppawar/free-programming-books](https://github.com/satishppawar/free-programming-books)@[5fd70502a0...](https://github.com/satishppawar/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Sunday 2022-10-02 02:36:00 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [ctwtruscottwatters/Thank-you-so-much-MIT](https://github.com/ctwtruscottwatters/Thank-you-so-much-MIT)@[62cdda1d91...](https://github.com/ctwtruscottwatters/Thank-you-so-much-MIT/commit/62cdda1d913010edb5b260a83616ad2f30330aff)
#### Sunday 2022-10-02 02:46:26 by Charles Truscott Watters

Add files via upload

Giving up computing for 600 days of public entrances, sex, socializing daily and lifetime financial gain to avoid homelessness, afford food, shelter, running water and electricity and own a home and get my first girlfriend in 14 years

---
## [mathisto/tangerine.nvim](https://github.com/mathisto/tangerine.nvim)@[2ae5c5c961...](https://github.com/mathisto/tangerine.nvim/commit/2ae5c5c961c52dc8b903bdcb1a8707fbc68df450)
#### Sunday 2022-10-02 03:46:28 by Matt Kelly

Fix literal table syntax in README

Yo ! First things first. You are awesome and this library is just gorgeous. I can tell home much love you put into it. Thank you so much for sharing it with the world.

This is just a doc fix I found while installing. I'm guessing this is just your lisp heart leaking out into the Lua source. 

Thanks again, friend. You are doing amazing work.

-Very Respectfully,
Matt Kelly

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[6ae62e2c13...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/6ae62e2c133d78bcc97668e42abe0fc56ad49510)
#### Sunday 2022-10-02 03:55:10 by Maciej Żenczykowski

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
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [technicalreju/all-new-programs](https://github.com/technicalreju/all-new-programs)@[030f20c01f...](https://github.com/technicalreju/all-new-programs/commit/030f20c01f8d86303cad9a9a7c46fda7d653bebc)
#### Sunday 2022-10-02 04:43:59 by technicalreju

Guess the word.py

Problem Statement – Kochouseph Chittilappilly went to Dhruv Zplanet , a gaming space, with his friends and played a game called “Guess the Word”.
Rules of games are –

Computer displays some strings on the screen and the player should pick one string / word if this word matches with the random word that the computer picks then the player is declared as Winner.
Kochouseph Chittilappilly’s friends played the game and no one won the game. This is Kochouseph Chittilappilly’s turn to play and he decided to must win the game.
What he observed from his friend’s game is that the computer is picking up the string whose length is odd and also that should be maximum. Due to system failure computers sometimes cannot generate odd length words. In such cases you will lose the game anyways and it displays “better luck next time”. He needs your help. Check below cases for better understand
Sample input :
5 → number of strings
Hello Good morning Welcome you
Sample output :
morning

Explanation:

Hello → 5
Good → 4
Morning → 7
Welcome → 7
You → 3
First word that is picked by computer is morning

Sample input 2 :
3
Go to hell

Sample output 2:
Better luck next time

Explanation:
Here no word with odd length so computer confuses and gives better luck next time

---
## [RealN00B/frameworks_base](https://github.com/RealN00B/frameworks_base)@[9b97fe5eaa...](https://github.com/RealN00B/frameworks_base/commit/9b97fe5eaa9a0299926e6a328853f2582b8bafd7)
#### Sunday 2022-10-02 06:39:24 by Joey Huab

core: Refactor Pixel features

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [Goldenkenneth409/Goldenkenneth409](https://github.com/Goldenkenneth409/Goldenkenneth409)@[661856384e...](https://github.com/Goldenkenneth409/Goldenkenneth409/commit/661856384e67e861eac544f947270801ef5f516c)
#### Sunday 2022-10-02 07:15:07 by Goldenkenneth409

Create +2349166885936 We wish every members of the greatest billoniers brother's , happy new month, another great opportunity,. what is your plan to achieve success, to make a good living, to give your family shelter, to be celebrated on Earth, do not allow your unborn children to die in poverty, join the greater island of riches brotherhood. ByFor more information call ✓+2349166885936 ✓•   

+2349166885936//
Do not die in poverty ", You have a very big opportunity if you are among the lucky people seeing this post. It's time to change your life for good, join  THE GREAT BILLIONAIRE BROTHER'S BROTHERHOOD to eliminate poverty in your life. We are the only occult

Do not die in poverty ", You have a very big opportunity if you are among the lucky people seeing this post. It's time to change your life for good, join the great occult of THE GREAT BILLIONAIRE BROTHER'S BROTHERHOOD to eliminate poverty in your life. We are the only occult that can give you money with no side effect, no human sacrifice, but only with some special animals blood to please our Lord Spiritual, and all your wishes are granted don't miss this !!! CALL  THE GREAT BILLIONAIRE BROTHER'S OCCULT GRAND MASTER on +2349166885936 or Email us at thegreatbilloniersb@gmail.com  JOIN THE GREAT BILLIONAIRE BROTHER'S BROTHERHOOD FOR WEALTH, FAME, POWER, PROTECTION, FORTUNE AND BE FABLOUSELY BLESSED call +2349166885936

---
## [Goldenkenneth409/Goldenkenneth409](https://github.com/Goldenkenneth409/Goldenkenneth409)@[a4edf10996...](https://github.com/Goldenkenneth409/Goldenkenneth409/commit/a4edf10996989f165cdf07623b78534d454d560b)
#### Sunday 2022-10-02 07:19:03 by Goldenkenneth409

Create +2349166885936THE GREAT BILLONIERS BROTHER'S BROTHERHOOD OCCULT . Nostarted this petition

Are you really tried of living in poverty ? if you really want your life to change for the better, here is a full opportunity for you to live a life of your dreams and the most interesting thing about this occult group is that no human sacrifice is needed no blood shad, this occult is base on animal sacrifice and no limits to the wealth we give, join us today and give the testimony latter call +2349166885936

---
## [CuriousGeorgiy/tarantool](https://github.com/CuriousGeorgiy/tarantool)@[66ca6252c4...](https://github.com/CuriousGeorgiy/tarantool/commit/66ca6252c428ca7a369e24faaa833e3520e809d6)
#### Sunday 2022-10-02 07:24:25 by Alexander Turenko

console: don't mix stdout/stderr with readline prompt

The idea is borrowed from [1]: hide and save prompt, user's input and
cursor position before writing to stdout/stderr and return everything
back afterwards.

Not every stdout/stderr write is handled this way: only tarantool's
logger (when it writes to stderr) and tarantool's print() Lua function
performs the prompt hide/show actions. For example,
`io.stdout:write(<...>)` Lua call or `write(STDOUT_FILENO, <...>)` C
call may mix readline's prompt with actual output. However the logger
and print() is likely enough for the vast majority of usages.

The readline's interactive search state (usually invoked by Ctrl+R) is
not covered by this patch. Sadly, I didn't find a way to properly save
and restore readline's output in this case.

Implementation details
----------------------

Several words about the allocation strategy. On the first glance it may
look worthful to pre-allocate a buffer to store prompt and user's input
data and reallocate it on demand. However rl_set_prompt() already
performs free() plus malloc() at each call[^1], so avoid doing malloc()
on our side would not change the picture much. Moreover, this code
interacts with a human, which is on many orders of magnitude slower that
a machine and will not notice a difference. So I decided to keep the
code simpler.

[^1]: Verified on readline 8.1 sources. However it worth to note that
      rl_replace_line() keeps the buffer and performs realloc() on
      demand.

The code is organized to make say and print modules calling some
callbacks without knowledge about its origin and dependency on the
console module (or whatever else module would implement this interaction
with readline). The downside here is that console needs to know all
places to set the callbacks. OTOH, it offers explicit list of such
callbacks in one place and, at whole, keep the relevant code together.

We can redefine the print() function from every place in the code, but I
prefer to make it as explicit as possible, so added the new internal
print.lua module.

We could redefine _G.print on demand instead of setting callbacks for a
function assigned to _G.print once. The downside here is that if a user
save/capture the old _G.print value, it'll use the raw print() directly
instead of our replacement. Current implementation seems to be more
safe.

Alternatives considered
-----------------------

I guess we can clear readline's prompt and user input manually and don't
let readline know that something was changed (and restore the
prompt/user input afterwards). It would save allocations and string
copying, but likely would lean on readline internals too much and repeat
some of its functionality. I considered this option as unstable and
declined.

We can redefine behavior for all writes to stdout and stderr. There are
different ways to do so:

1. Redefine libc's write() with our own implementation, which will call
   the original libc's write()[^2]. It is defined as a weak symbol in
   libc (at least in glibc), so there is no problem to do so.
2. Use pipe(), dup() and dup2() to execute our own code at
   STDOUT_FILENO, STDERR_FILENO writes.

[^2]: There is a good article about pitfalls on this road: [2]. It is
      about LD_PRELOAD, but I guess everything is very similar with
      wrapping libc's function from an executable.

In my opinion, those options are dangerous, because they implicitly
change behavior of a lot of code, which unlikely expects something of
this kind. The second option (use pipe()) adds more user space/kernel
space context switches, more copying and also would add possible
implicit fiber yield at any `write(STD*_FILENO, <...>)` call -- unlikely
all user's code is ready for that.

Fixes #7169

[1]: https://metacpan.org/dist/AnyEvent-ReadLine-Gnu/source/Gnu.pm
[2]: https://tbrindus.ca/correct-ld-preload-hooking-libc/

NO_DOC=this patch prevents mixing of output streams on a terminal and it
       is what a user actually expects; no reason to describe how bad
       would be his/her life without it

---
## [nblockchain/conventions](https://github.com/nblockchain/conventions)@[e4f6a5652c...](https://github.com/nblockchain/conventions/commit/e4f6a5652cf22ead98f6dd16367bf6f32d656fdd)
#### Sunday 2022-10-02 08:51:31 by Andres G. Aragoneses

plugins: add assertions before type conversion

This is a sanity check before we get stupid "null" string
or something similarly idiotic from this shitty javascript
world.

---
## [SomethingFish/tgstation](https://github.com/SomethingFish/tgstation)@[d45e244401...](https://github.com/SomethingFish/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Sunday 2022-10-02 11:00:58 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1eab5a8364...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1eab5a8364114dce9f63c97852461b6e4f27d7b0)
#### Sunday 2022-10-02 13:13:26 by SkyratBot

[MIRROR] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix [MDB IGNORE] (#16486)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tastyfish <crazychris32@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[635aee8e34...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Sunday 2022-10-02 13:14:33 by SkyratBot

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
## [DocFX/symfony](https://github.com/DocFX/symfony)@[338daf25c9...](https://github.com/DocFX/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Sunday 2022-10-02 13:37:20 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[ad01ab5ed0...](https://github.com/GoblinBackwards/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Sunday 2022-10-02 13:43:15 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e1839f0e37...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Sunday 2022-10-02 14:24:45 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [SAnschutz/practice-git](https://github.com/SAnschutz/practice-git)@[3e75622506...](https://github.com/SAnschutz/practice-git/commit/3e756225060d96a2bd49ec3bd342b3624a8d725e)
#### Sunday 2022-10-02 14:47:30 by gacetta

There is unrest in the galaxy. Revolts. Looting. Riots. Revolution. Resistance. Real trouble in THE EMPIRE. STRIKES. BACK in the day, before he was Darth Vader, he was just a boy named Anakin.

---
## [Nitrohedge21/2D-Sonic-Project](https://github.com/Nitrohedge21/2D-Sonic-Project)@[9110d3b952...](https://github.com/Nitrohedge21/2D-Sonic-Project/commit/9110d3b952c1a39de0b01ae8273eb75ba32f5ef2)
#### Sunday 2022-10-02 14:50:45 by Nitrohedge21

Goalpost/finish line test

- This shit is not doing the animation for some fucking reason.
- Will try to make another push tonight which will hopefully be the fixed version.

---
## [exhq/neOwOfetch](https://github.com/exhq/neOwOfetch)@[f206dfc0bf...](https://github.com/exhq/neOwOfetch/commit/f206dfc0bfcfbc3bc1098601b0d0eb32137ed15a)
#### Sunday 2022-10-02 15:25:47 by echo

holy fucking shit fr another neowofetch ubdate????!?!?!?!/! i fucking love neowofetch its the best fucking anime bro frfr bruh fr

---
## [LineageOS/android_kernel_fxtec_msm8998](https://github.com/LineageOS/android_kernel_fxtec_msm8998)@[8d9a4c77b0...](https://github.com/LineageOS/android_kernel_fxtec_msm8998/commit/8d9a4c77b0c04968915d9f173edaf85816950394)
#### Sunday 2022-10-02 15:25:50 by Christian Brauner

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
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[8f52eb9e0f...](https://github.com/Nyanotrasen/Nyanotrasen/commit/8f52eb9e0f7e246ddcadb7f96a948ceec27d7ee4)
#### Sunday 2022-10-02 16:18:33 by ZeroDayDaemon

Psionic Content (#542)

* Psionic Content

* Address Reviews

* rane bitches too much

* Tonight, on unsolved mysteries, find out who gives a shit about bigfoot

UPDATE: apparently nobody gives a shit so fuck him.

UPDATE: Last night somebody broke in and stole $500 worth of shit at my house

That’s right $500 worth of BULLSHIT!!!

* Address reviews

---
## [relaxtakenotes/deadeye](https://github.com/relaxtakenotes/deadeye)@[eda47178fd...](https://github.com/relaxtakenotes/deadeye/commit/eda47178fd46e50c86a1610c7c108401f2739499)
#### Sunday 2022-10-02 16:27:24 by relaxtakenotes

fix tfa's awful decision of enabling soundscale and fucking with my shit

---
## [saba-14/my-first-guessor-game-application](https://github.com/saba-14/my-first-guessor-game-application)@[3939aed350...](https://github.com/saba-14/my-first-guessor-game-application/commit/3939aed3505221c1ccc63f3998c7c062a9f0dbc2)
#### Sunday 2022-10-02 17:10:10 by saba-14

AN EXCITING EXPERIENCE

# my-first-guessor-game-application
Its been an amazing day learning java ,its third day in a row as we were learning .
Seems intresting till now ,it was an exciting activity writing the code for the guesser game.
Though it seemed like a piece of cake for the first time writing it in the book.
Surely was a task to deal while trying to execute and debug it.

---
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[ada955b5b6...](https://github.com/Brawaru/knossos/commit/ada955b5b65001add2ddb468c1c5554c87a900d4)
#### Sunday 2022-10-02 18:19:45 by Sasha Sorokin

Add v-i18n:wrap directive

v-i18n:wrap directive is a directive that only has effect within the
<i18n-formatted> element. It takes an element as a skeleton and allows
to use so-called 'wrappers' in the translations.

Wrappers are extremely useful if translation needs to contain links or
buttons, but it does not make to split text from those to separate
strings.

For example, let's say we have the following HTML:

  Your project was rejected, please check out the <a href="/rules">rules</a>.

Without wrapper elements we would have to resort to the following:

In our translations file,

  {
    "rejection-message": "Your project was rejected, please check out the {rulesLink}.",
    "rejection-message.rules-link": "rules"
  }

In our Vue file,

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:value="'rules-link'">{{ $t('rejection-message.rules-link') }}</a>
  </i18n-formatted>

For translators, this is not very plausable experience because they'd
have to guess what that 'rulesLink' variable actually contains, it's
good that we use good message IDs, but nevertheless, it's confusing
experience.

It also introduces a surface for mistake, translator may not pay close
attention to the message IDs and translate both strings independently.
As English speakers we tend to forget that other languages have more
advanced casing systems, where noun or verb may change depending on what
surrounds it, so in some languages, translating both strings can lead to
mistake.

To demonstrate, let me give you an example from Discord:

Say we have the following strings in original English text:

  {
    "hello-cta": "Say ‘{hello}’ to the {helloTarget}",
    "hello-cta.target": "cat"
  }

Which we can use as such:

  $t('hello-cta', { helloTarget: $t('hello-cta.target') })

But what happens if Ukrainian translator translates `hello-cta.target`
independently of `hello-cta` string. They translate it as such:

  {
    "hello-cta": "Сказати «привіт» {helloTarget}",
    "hello-cta.target": "кіт"
  }

And using code above, the result we will get from these translations:

  'Сказати «привіт» кіт'

Which is incorrect, in this case 'кіт' is supposed be in dative case,
which would change it to 'коту'.

Keeping that in mind, let's look how things would change if we were to
use wrapping syntax:

  {
    "hello-cta": "Сказати «привіт» <target>коту</target>"
  }

This looks like HTML, and if you think about it, it kinda is, but not
quite, it's merely wrapper, like BB-codes, and those do not accept any
arguments, to not complicate things.

In the code we would use `hello-cta` string as such:

  $t('hello-cta', { helloTarget: (parts) => `${parts.map(_ => String(_)).join('')}` }`)

Keep in mind, that in this example we don't do anything fancy yet, you
can see that our wrapper doesn't do anything apart from taking some
parts and later converting them to strings. If we don't use any objects
in our context object, then it will never be not array of strings, but
otherwise it'd contain these objects too in places of variables.

So what do we get when evaluating code above? Well, of corse:

  'Сказати «привіт» коту'

What v-i18n:wrap allows us to do is to create skeleton node, which will
be copied every time the wrapper used, and which children will be
replaced with aforementioned parts.

Let's look at the first example, but using wrappers now:

Here's our changed translation file:

  {
    "rejection-message": "Your project was rejected, please check out the <rules-link>rules</rules-link>."
  }

And here's how we'd change our template:

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:wrap="'rules-link'" />
  </i18n-formatted>

Notice that we self-close our link element, that's because we know that
anything will be replaced anyway, so there is no sense to provide any
children.

And what happens when this string actually gets rendered?

  Your project was rejected, please check out the <a href="/roles">rules</a>.

Exactly what we'd expect.

So there we go, this is the new directive for you, hope this was
insightful and useful to understand the importance and usage of this
feature.

---
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[e2967009ca...](https://github.com/Brawaru/knossos/commit/e2967009cababd184780db28d37d361219a6295e)
#### Sunday 2022-10-02 18:19:45 by Sasha Sorokin

Initial work on the i18n support

Absolutely not ready, just a draft for progress and maybe quick review
whether it's good idea or not.

This commit will be squashed with more meaningful message as the work
goes.

For now things are like this:

- It uses @formatjs/intl which uses ICU Message Format for messages,
  it's the same underlying framework than used in React. However,
  their Vue module is only for Vue 3 and it also not dynamic (means
  you can only initialise it with a single language which is weird),
  so I had to re-do all work by myself.

- Reason not to use vue-i18n: it's weird formatting for translations.
  I agree it's a more mature module, but as translator myself I under
  no circumstance want to translate things like {n} apple | {n} apples.
  ICU Message Format is already an industry standard so there's no good
  reason to re-invent the wooden wheel when people already have alloy
  ones.

- There is no automatic extraction, sadly.

- There is no automatic locale packing. I have no clue how to implement
  Nuxt modules to do this magic, but it's probably very possible, should
  look at https://i18n.nuxtjs.org/ for inspiration, they use some weird
  templates and generate plugins. Oh my oh my.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1d8e1fb83c...](https://github.com/treckstar/yolo-octo-hipster/commit/1d8e1fb83c565fa7204b9312c0ea9a0f5c5ca60f)
#### Sunday 2022-10-02 19:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[23bfdec8f4...](https://github.com/GoldenAlpharex/tgstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Sunday 2022-10-02 20:00:21 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[cee07f804c...](https://github.com/GoldenAlpharex/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Sunday 2022-10-02 20:00:21 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [notzyro/ForkBot.NET](https://github.com/notzyro/ForkBot.NET)@[addf27fd16...](https://github.com/notzyro/ForkBot.NET/commit/addf27fd1688c4785202b53177d7fa84069d9bed)
#### Sunday 2022-10-02 20:58:33 by Koi

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
## [0b10000/vignette-web](https://github.com/0b10000/vignette-web)@[0085366487...](https://github.com/0b10000/vignette-web/commit/0085366487d49b80730489b2e59f9b7691174235)
#### Sunday 2022-10-02 21:51:05 by Ayane

Engineering blog, nya! (#88)

* Engineering blog, nya!

* why isn't it showing up D:

* ヽ(*。>Д<)o゜

* thank you timezones (┬┬﹏┬┬)

* Fuck you YAML ヽ(*。>Д<)o゜

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[bdfccf66a4...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/bdfccf66a44e9d970f772e3946c266595986b839)
#### Sunday 2022-10-02 21:55:28 by silicons

[MDB IGNORE] erases d1/d2 varedits from *most* cables (#4463)

* e

* e

* e

* more

* y'all weird

* fuck you

* FUCK YOU THE INTEGRATION TEST IS GOING ON

* fine that goes off

Co-authored-by: VM_USER <VM_USER>

---
## [philipl/mpv](https://github.com/philipl/mpv)@[3d459832a8...](https://github.com/philipl/mpv/commit/3d459832a88a9bd2835b339cf6ca98f84aad0115)
#### Sunday 2022-10-02 22:02:08 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in a previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [VELD-Dev/SubnauticaBZMultiplayerMod](https://github.com/VELD-Dev/SubnauticaBZMultiplayerMod)@[c91b28b2eb...](https://github.com/VELD-Dev/SubnauticaBZMultiplayerMod/commit/c91b28b2eb67ed568196d09bed58784a909145a0)
#### Sunday 2022-10-02 22:03:23 by V E L Δ

New ID system WORKS HOLY SHIT.
No for real I would have never expected it would
work so fast damn

---
## [ike709/tgstation](https://github.com/ike709/tgstation)@[9b9337de49...](https://github.com/ike709/tgstation/commit/9b9337de493ec62927f15b0ee18f9342cd3c2d04)
#### Sunday 2022-10-02 22:19:59 by Tim

Add speech modifier to zombie tongue (#69899)


About The Pull Request

A zombie rotten tongue has a complex language modifier.
The language modifier works by:

    All occurrences of characters "eiou" (case-insensitive) are replaced with "r".
    All characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
    Multiple spaces are replaced with a single.
    Lower-case "r" at the end of words replaced with "rh".
    An "a" or "A" by itself will be replaced with "hra".
    The first character is capitalised.

Some interesting dialogue examples:

    Bab, am gaa habbah abah zah namrh ah Bh!rh!b?
    Bob, are you happy about the death of Philip?

    Zah bang bang man ganna harm mah zambah?
    Will the Zombie Hunter attack me?

    Mah zambah nah harm brazzarz.
    I do not hurt brothers.

    Mah zambah ganna gangbang harmanz zammarrar.
    I will kill humans tomorrow.

    Mah zambah am nah habbah, an mah zambah gab, -Graaaagh!-
    I am not happy, and I say "Graaaagh!"

The language idea was taken from a zombie game back in 2005 called Urban Dead. It's no longer developed and I made all the code myself while following the given language rule structures.

Zombie Speech Translator
Zombie Language Examples
Zombie Dictionary
Why It's Good For The Game
Abracadabra - The Steve Miller Band

    Ah raab zha brahnz ahn zarh hagh, (I love the brains in your head)
    Ah ganna barg abgrah gangbang, (I'm gonna eat them when you're dead)
    Az rahnah zarh ranz ahn hahg ahahz, (Now as you run and hide away)
    Zarh harh mah zambah az hah zahz: (You hear my zombie as he says:)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)

Changelog

cl
add: Rotten zombie tongue has a new speech modifier that converts spoken language into zombie sentences. If the person speaking is a high-functioning zombie this is bypassed.
/cl

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[f923f61011...](https://github.com/Kubisopplay/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Sunday 2022-10-02 22:46:05 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [ABuffaloHerd/cise-product-1](https://github.com/ABuffaloHerd/cise-product-1)@[83ad7355d6...](https://github.com/ABuffaloHerd/cise-product-1/commit/83ad7355d67be7e7b2f4de08168402fdd001dd27)
#### Sunday 2022-10-02 23:03:14 by ABuffaloHerd

submit form update from alessandra fuck you node modules all you do is ruin everything

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[99b8d6b494...](https://github.com/tgstation/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Sunday 2022-10-02 23:28:57 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---

