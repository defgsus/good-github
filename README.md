## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-16](docs/good-messages/2022/2022-05-16.md)


1,759,346 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,759,346 were push events containing 2,828,525 commit messages that amount to 217,632,140 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[a064b35b25...](https://github.com/Paxilmaniac/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Monday 2022-05-16 00:16:04 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[a3c8013b45...](https://github.com/dragomagol/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Monday 2022-05-16 00:28:52 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [hrs/dotfiles](https://github.com/hrs/dotfiles)@[64e1f64189...](https://github.com/hrs/dotfiles/commit/64e1f6418997e18ea85d4ea97dbccae00b4123ad)
#### Monday 2022-05-16 01:15:25 by Harry R. Schwartz

Only use evil-org for evil-org-agenda

Honestly, all I want is `j` and `k` in my agenda, plus `TAB` to cycle.

The real issue here was that always running `evil-org-mode` with `org-mode`
overrode my binding for `M-l`, `downcase-word`, which I use often enough that it
kinda frustrated me.

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[4b8be9df69...](https://github.com/Rhials/tgstation/commit/4b8be9df6982c1394e190fe9485d46e0943d6392)
#### Monday 2022-05-16 01:57:08 by Rhials

i fucking ahte you dm i hate you so much i hate you i hate you i hate you i hate you

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [SuperNovaa41/tgstation](https://github.com/SuperNovaa41/tgstation)@[3f18dadd1a...](https://github.com/SuperNovaa41/tgstation/commit/3f18dadd1a5d654aafc2c37539ff917580bfe0b2)
#### Monday 2022-05-16 02:48:11 by san7890

Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

---
## [veggiemike/linux-mdl](https://github.com/veggiemike/linux-mdl)@[9709c8b5cd...](https://github.com/veggiemike/linux-mdl/commit/9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5)
#### Monday 2022-05-16 04:20:35 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Pascoato/android_device_xiaomi_sm8350-common](https://github.com/Pascoato/android_device_xiaomi_sm8350-common)@[a3fa79874c...](https://github.com/Pascoato/android_device_xiaomi_sm8350-common/commit/a3fa79874cd9529da9d7fd897b8b1abfba30a4b3)
#### Monday 2022-05-16 04:52:47 by Pascoato

sm8350-common: Set BUILD_BROKEN_DUP_RULES := true

* Fuck you mlipay

---
## [a3-Prjkt/kernel_xiaomi_ginkgo_consistenX](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX)@[77d3719edc...](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX/commit/77d3719edcb174b74b0b3ad85ae0eea065c8cfe7)
#### Monday 2022-05-16 06:15:47 by Yaroslav Furman

power: supply: force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>

This is possibly breaking the DS28E16 verification driver
Signed-off-by: Forenche <prahul2003@gmail.com>
better safe than sorry
Signed-off-by: HafizZiq <hafizuddinismail552@gmail.com>
Signed-off-by: Forest <forestd.github@gmail.com>

---
## [vware/android_kernel_oneplus_msm8998](https://github.com/vware/android_kernel_oneplus_msm8998)@[a495e9226c...](https://github.com/vware/android_kernel_oneplus_msm8998/commit/a495e9226c681e1a6c1075f365e446176697aa88)
#### Monday 2022-05-16 09:34:41 by Maciej Żenczykowski

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[15072f0938...](https://github.com/mrakgr/The-Spiral-Language/commit/15072f09382cc0a7df16ce4e1f876aedac24b365)
#### Monday 2022-05-16 11:26:06 by Marko Grdinić

"7:50am. I do not know whether I slept well, but I am rested right now. Let me chill for a while and then I will start.

7:55am. Dong Bai, Kaiji, something else and then I will start. Today's morning is good. I am just going to focus on painting today. I have a small desire to do more modeling, but it is not too important. I need test my painting chops. It should work.

8:15am. So it turns out the prequel to Rondo Duo is translated. I found it on the F95Zone I'll get it and leave it for later.

8:55am. Let me start. Yesterday I spent the whole day reading Fable. It is the kind of manga like the ones that got me into the hobby as a kid.

I just realized a strategic mistake I might have made two days ago. That is when I opened CSP for the first time and tried making a sketch.

The mistake was trying to encompass my whole view. Instead I should have just sketched out the area near the center of my vision. That would only have been a smaller part of my view, but it would be easily to keep it stedy through the head tilts.

Instead I tried taking in everything and it just confused me.

Well, now that I have a 3d model of the room as reference it is no problem, but I could have made better progress if it weren't for it.

9:05am. The time I did the couch I mostly just traced over a cycles rendered image. In comparison here I have a fairly rough model without any rendering. In fact, rather than just be rough it goes both ways, some of the detail on the grills and the rig is too small to be easily noticeable and there are many of of them. It is going to be a challenge to paint those in.

There are also many objects in the room that I haven't bothered modeling directly and will want to paint in.

There is also the fact that as the day goes on, the lighting in the room will shift. Given how slow I am, the image will no doubt be a blend of different lighting conditions. But that could be cool stylstically.

9:15am. Let me go for it. I am not going to rush this particular illustration at all and will spread it out over several days, even going back to remodel it if need be. Oh, right before that, did I get a reply to the Substance issue? No.

Nevermind it then.

9:20am. Being able to do good illustrations is a real power. Sure it is an illusion, and I can only go so far with doing thing by hand like now, but it is not like I can do particularly more with programming. Without the algorithms and the AI chips, I am just a peasant here as well. Now that I have the ability to 3d model, I have something to base my artistic endeavors on. Even if it is just sketching things out, that is enough. Sketching is not to be underestimated.

9:25am. I am not there yet of course. I need to do this challenging indoors scene. I need to be able to paint characters as well. After that I need to do challenging outdoors scenes like cities and forests.

I also need to finish the Zbrush course and complete my modeling journey.

I do not see much appeal in box modeling. Right now I see my workflow as Moi for blockouts plus importing subdiv models made in Blender if I need more power. If I need to go all out with modeling I'd take a sculpting approach. For texturing I'll use flats and face material assignments. If I need to go full out, there is Substance. For layouting there is Blender, but I need high poly crunching, there is Clarisse.

I just need a tiny bit more proficiency in hard surface sculpting on the 3d side and that should be good enough to get to the level in 3d that I've sought.

9:30am. But I had enough of develping 3d for now.

I need to check myself in 2d. It is time to do it. I think most beginners find it tought because they can't get past through fundamental hurdles.

Take note of the mistake I did two days ago. Trying to capute all of my perspective as if my eyes were cameras was lame.

9:35am. Yeah, it is worth it. Being good at art is worth it. It is really lame to want to do a game or a novel and have to shell out to other people for such an important aspect. I do not want to feel the shame being required to get a job to pay other people for this like in 2014. It is time for revenge.

I am going to get through this hurdle and leave the old weak self behind.

There is no need to life with the shame and humiliation of being bad at art.

Afterwards I think I should do sketches of select pieces in the room. Since I know not to try to capture the whole FOV all at once, even if I decide to do a minor chunk, I can just stitch those chunks together. If such a thing works, it might allow me to loosen my dependency on 3d.

I might have put in 7.5 months into it, but it is not like I have to do it if I do not need to. If I had a high level of skill in 2d, I would not bother with it.

Let me give it a try. Let me just start with the bed in the lower left side. It might be better to start with flats everywhere, but I need to refresh my memory of how CSP works. I am also not sure how to do a color layer properly.

9:40am. Let me take a short break first.

9:55am. Let me finally start. I'll break out the pen and focus on just one bed. This is not too great of an idea. If I had the right workflow in mind, I'd do a pass over the whole room first to set the overall lighting first. Having it like this will affect the image negatively. But I'll make an exception. I am doing the bed so I can find that workflow. Adjusting the overall shading for it later won't be hard.

10am. I confused. I knew this six months ago, but I completely forgot how layer masks work in CSP. Let me watch a tutorial or two.

https://youtu.be/F04bMk-_DTI
Layer Masking - Clip Studio Paint Quick Tips - CSP Tutorial

Let me watch this. I'll also want to refresh my memory of how selection layers work. After that I'll want to play with the various blending modes such as color and brightness.

https://youtu.be/F04bMk-_DTI?t=33

Yeah, I actually don't know what the resolution here is supposed to be doing. I should investigate that.

https://youtu.be/aS7TltA9MMw
The Power of Masking and Blending Modes in Clip Studio Paint!

That last vid did not quite tell me how to paint the masks directly.

Ah, I remember now. While in Substance Painter the masks are grayscale, in CSP they are affected by the alpha. They start off pure white and to make things out I have to go in with the eraser. Or I can just switch the current brush to erase using C.

Mhhh, not bad at all. Let me just take a peek at the video above. After that I'll refresh my memory of selection layers. I know it is possible to turn masks into selection layers and back. How did that work?

https://youtu.be/aS7TltA9MMw?t=138

The blending mode explanations in 2d software is dogshit as usual. His explanation of multiply is that adding colors pushes it closer twoards black. I am really grateful that I took the time to learn Substance Painter and had these explained to me properly.

10:20am. What is clip to layer below again? Ah, I see. It just uses the transparency of the layer below as a mask.

Lock transparent pixels on the other hand uses the transparency of the current layer as a temporary mask.

It is a bit like doing a select on what is current. You can do that using Ctrl Shift.

10:30am. There is no helping it. I haven't used CSP seriously in 2022. I need some downtime to get reacquainted with it. Let me finish the tutorial and then I'll take a look at selection layers.

https://youtu.be/aS7TltA9MMw?t=399

This has some really useful shortcuts. I hadn't know about Ctrl + T for moving the layer or Alt + Del for filling it.

https://youtu.be/aS7TltA9MMw?t=510

Is this how SSS it works? I had no idea.

https://youtu.be/aS7TltA9MMw?t=527

Had no idea about the Alt + Drag thing for duplicating masks. This is a pain in the ass in Substance, but maybe I simply did not know the right trick there. I should try this if I ever use it again.

10:40am. It was good that I watched the above tutorial. I really did need a refresher.

https://youtu.be/tpg733_tgT0
Clip Studio Paint (Manga Studio): Quick Mask and Selection Layers

Let me just get up to speed with selection layers. I used those a lot.

Ah, right I see. I had the shortcut set to @ and Shift + @. Huh?

To get @ on my keyboard I need to press Shift + 2. Just how would I press Shift + @ then?

10:55am. I have no idea how I managed to set such a shortcut. I've remapped to A and Shift+A. Now things are good. I've also been having real trouble clicking deselect. The shortcut for that is just Ctrl + D.

11am. Let me finish the tutorial. Another 3m are left. After that I'll play with blending modes. I want to come to an understanding how I can separate the flats from the shading.

11:15am. I get it perfectly. For shading I just need a grayscale layer and set it to Saturation. Alternatively, I can have it be at the bottom as a Normal layer and put flats above it as a Color layer.

https://youtu.be/ua9MMABBA4A
How to Color FASTER for Digital Artists in Clip Studio Paint

Let me watch this just for a bit.

11:20am. Nevermind, let me just get on with it.

I can't recall how to do auto actions. I know there was a record button somewhere, but I forgot where it was. It does not matter. I can easily pick this back up should I need to.

11:25am. This was a pretty good refresher. I certainly could not pick CSP up from scratch in this timeframe. Actually, I still don't know what a lot of the stuff in this program do. Hell, I definitely know 3d programs better than it, but it will do.

CSP is like Moi. Moi is all basics, and in CSP the basics are what is important. The same goes for Zbrush. Modeling and 2d should be fine for now.

11:30am. I should have spent more time in the modeling stage, but that does not matter. Even thought I can see various perspective errors on the bed model, why don't I take it as a challenge to adjust it.

11:35am. Instead of drawing masks by hand, maybe I should have extracted freestyle edges, but nevermind that for now. That would just be a timesaver. That is not what I should be worried about.

11:40am. No, it won't be that easy to correct the perspective. But it does not matter. I can just pretend this is fine. Let me put the flats down.

12:20pm. Down with the flats. I had to take a short break again. I forgot about the Moi issue.

12:25pm. Got a reply yesterday. Let me see what he did.

1:10pm. https://moi3d.com/forum/discussion.php?webtag=MOI&msg=10695.2

I had to play around with this for a bit. Now, I am really interested in what his answer will be. I guess in the end I did not really loft it correctly. I should have taken care to avoid having some of those edges.

1:15pm. Nevermind. Forget playing with this for now. I did take the chance to set up the shortcut for the area zoom while I was at it.

Moi would really be perfect if it wasn't for situations like these where it inexplicably fails during overlaps.

Yeah, I could have thought to separate the door into 4 solids and cut it that way.

1:20pm. Now it is time for breakfast.

1:25pm. Focus me."

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[cd1b891d79...](https://github.com/OliOliOnsiPree/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Monday 2022-05-16 11:59:13 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [hedyhli/site](https://github.com/hedyhli/site)@[06198fdc7d...](https://github.com/hedyhli/site/commit/06198fdc7d70975e164157ae418958aabf140f44)
#### Monday 2022-05-16 12:36:37 by hedy

Nav, CSS, Content(index): Add favicon, better homepage and nav title

Basically all the changes involving my profile pics

- Favicon: 32x32 2-colors version
  - Both SVG and PNG provided

- Nav home link: Now having the icon next to the name
  - Configurable in config.toml (see its comment)
  - For homepage: the home link is Site.title
  - For other pages: icon next to name

- Index page h1: No more big ugly pfp, now inline
  - Using shortcodes with corresponding partials ln'ed to them

- CSS for the nav thing
  - Right now when user hovers on the home link, the portion has a
    background color. I tried to not select it but apparently failed.

    Desired behaviour: it should only have the hover effect if the home
    link does not have the image (which is the case for all pages other
    than index page, as described in second list item above).

    Current behaviour: A useless CSS selector change that did not alter
    the site's behaviour in any way whatsoever. Don't mind me, I'm
    horrible at comitting things for this repo - I tend to like to make
    a lot of changes in one go and commit using `git apply -p`. I also
    litter a lot of comments in the CSS, which apparently increases the
    size of the inline <style> in every. single. HTML file generated.
    Literally.

    Most likely switching back to external stylesheet in the future to
    save some bytes in my overall website size.

- (Most likely the worst CSS addition I've every made): A blinking
  lower-block for the h1 on index page. Seriously? CSS Animations on a
  supposedly "simple" site like this??? Hopefully I would know better
  and remove it soon.
  - It's only animated for like 5 seconds. After that it is hidden
  - For text-based browsers it willbe static and forever there. This may
    be a problem because it looks like my name has a trailing
    underscore :facepalm:
  - It just looks wrong. I didn't have the typewriter animation for the
    h1 text though, so ugh.

---
## [Tavelar/OddJobs-Backend](https://github.com/Tavelar/OddJobs-Backend)@[becdfc69da...](https://github.com/Tavelar/OddJobs-Backend/commit/becdfc69da419887f03b357935e07abddc33ba7e)
#### Monday 2022-05-16 12:48:22 by Tavelar

tims beautiful work, god hes so amazing i hate him so much

---
## [hedyhli/site](https://github.com/hedyhli/site)@[5fb340aa03...](https://github.com/hedyhli/site/commit/5fb340aa03a0fee91e93d7e7b77d3694b4220392)
#### Monday 2022-05-16 13:02:30 by hedy

Add a perfectly appropriate alt text to icon image

Yes 100% suitable :P

It describes what the image is to those who can't see the image
perfectly well.

It magically makes the image show up in terminal browsers, as if your
terminal browser can render small images to the very pixel.

Bonus, for terminal/text-based browsers the "image" can even adapt to
your custom font! How cool is that?

Look, people, unique per-user images without cookies, without
javascript, without sessions, without CSS.

It was a very pleasant commit-message-writing experience...

Until realization hit. Why TF did you have the stupid image in the first
image when it can just be a block of text (<code>)? Oops! Let's not
celebrate my site's accessibility features too early, *cough* *cough*.

---
PS: Anyways after like almost two(?) years my site finally has a
favicon, lol, see previous commits.

---
## [xaur/decred-news](https://github.com/xaur/decred-news)@[2a0bdc88e0...](https://github.com/xaur/decred-news/commit/2a0bdc88e0e4845d66428b92c7e99414bac67d7f)
#### Monday 2022-05-16 13:22:10 by xaur

Media formatting tweaks, read inside

- Reformatted coverage of the full node guide. First, format quote as a
  quote block. Second, move out the Raspberry Pi sentence since it's not
  part of the quote. Mind that I do not add indentation to "nest" all 3
  paragraphs under the bullet. GitHub Markdown renderer will handle it,
  but Medium will not.

- Make decredsociety.com domain visible. I type important domains
  explicitly to help people remember them for security and a bit of
  promotion.

- Convert content titles to `Sentence case` for consistency with past
  issues. Open to discuss this if it looks worse than `Title Case`.

- Add authors names to articles, in addition to outlet names.

- Use `@phoenixgreen` over `@DecredSociety`. I thought a lot about how
  to refer to people (https://github.com/xaur/decred-news/issues/20) and
  the latest is to use "the most widely known" handle, preferring Matrix
  ones.

  `@phoenixgreen` was used in his Medium originally, then in Matrix, and
  I used it in many past DJ issues. One undocumented "feature" of
  consistent usernames in DJ is I can do a fast and simple text search
  over DJ files and find person's contributions over 3+ years of Decred
  history. Open to discuss/change this ofc.

- Changed "Element" back to "Matrix" because Element is just one client.
  However, it made me wonder if we should make a step back on naming
  things properly to better connect with people who call the chat network
  "Element", which may be a lot of people.

---
## [iknek/DAT257-Agile-Project](https://github.com/iknek/DAT257-Agile-Project)@[074ef9cef9...](https://github.com/iknek/DAT257-Agile-Project/commit/074ef9cef902fc9ca0fd47ef4db80fa6e83cfcd1)
#### Monday 2022-05-16 13:42:19 by iknek

Committed cardinal sins against whatever god there is for programmers. See you in hell suckasssss.

---
## [raresica1234/Kumo](https://github.com/raresica1234/Kumo)@[5184e348e4...](https://github.com/raresica1234/Kumo/commit/5184e348e4922c8cddd8f474aae1cd549abc6f3b)
#### Monday 2022-05-16 13:52:05 by BuildTools

No I'm not finishing shocket fuck you <@214980279964663808>

---
## [tliam1/UnnamedProject](https://github.com/tliam1/UnnamedProject)@[ebb16e5be0...](https://github.com/tliam1/UnnamedProject/commit/ebb16e5be0ad2130a4ea76dc77655b88ba7529d2)
#### Monday 2022-05-16 14:16:12 by CosmicShiny

omg I love dream hes m y favorite ytber <3333

The Hog Rider card is unlocked from the Spell Valley (Arena 5). He is a very fast building-targeting, melee troop with moderately high hitpoints and damage. He appears just like his Clash of Clans counterpart; a man with brown eyebrows, a beard, a mohawk, and a golden body piercing in his left ear who is riding a hog. A Hog Rider card costs 4 Elixir to deploy.

Strategy

His fast move speed can boost forward mini tanks like an Ice Golem in a push. At the same time, he can also function as a tank for lower hitpoint troops such as Goblins as he still has a fair amount of health. Most cheap swarms complement the Hog Rider well, as they are nearly as fast as him and usually force more than one card out of the opponent's hand.

The Hog Rider struggles with swarms, as they can damage him down and defeat him quickly while obstructing his path. Barbarians in particular can fully counter him without very strict timing on the defender's part, though be wary of spells.

A Hunter can kill the Hog Rider in 2 hits if placed right on top of it. However, if you place something in front of the Hog Rider, the Hunter's splash will damage the Hog Rider and hit the card in front of it more.

The Hog Rider in conjunction with the Freeze can surprise the opponent and allow the Hog Rider to deal much more damage than anticipated, especially if the opponent's go-to counter is a swarm, or swarms are their only effective counter to him. Skeletons and Bats will immediately be defeated by the spell, while Spear Goblins, Goblins, and Minions will be at low enough health to be defeated by a follow up Zap or Giant Snowball.

However, this strategy isn't very effective against buildings as the Hog Rider will take a while to destroy the building, giving the opponent ample time to articulate another counter.

Against non-swarm troops, it can deal a lot of damage during the freeze time, but this can allow the opponent to set up a massive counterpush. For this reason, players should either only go for a Hog Rider + Freeze when they have other units backing it up from a counterattack, or if the match is about to end and they need to deal as much damage as possible.

It is not a good idea to send in a Hog Rider simply to destroy a building, especially if it is the only building targeting unit available, as defeating Crown Towers becomes substantially more difficult. Spells or simply waiting out the lifetime of the building are more effective. The exception to this is an Elixir Collector placed in front of the King's Tower. If a Hog Rider placed at the bridge, he can destroy the Collector for a positive Elixir trade, though the damage from both Princess Towers will usually mean he does not survive to deal any damage to them. However, if the opponent sends in defending troops, it can be an opportunity to gain spell damage value.

In a deck with several low-cost cards, it might be worth it to simply send the Hog Rider against one building. These decks shuffle their card rotation quick enough, that they will arrive to their next Hog Rider before the next building arrives in the opponent's card rotation.

Long-ranged troops like Musketeer and Flying Machine can snipe those buildings, preserving some of the Hog Rider's health, possibly allowing it to get some Tower damage.

When there are buildings placed in the middle to counter the Hog Rider, understanding the placement of the Hog Rider and the type of building placed can help the Hog Rider to bypass certain buildings.

Passive buildings such as spawners and Elixir Collector have a larger hitbox than defensive buildings; which means that if a passive building was placed 3 tiles away from the river in the middle of the opponent's side, then it is impossible for the Hog Rider to bypass that placement as the Hog Rider will get pulled to that building.

Defensive buildings have a smaller hitbox than a passive building, which means if that if a defensive building was placed three tiles away from the river in the middle of the opponent's side, a Hog Rider placed at the very left or right side of the Arena may be able to bypass it due to its smaller hitbox.

If the player has a building already placed down in the center of the arena, and the opponent tries to bypass it with a Hog Rider at the edge of the arena, they can use certain air troops to push the Hog Rider towards the building as it jumps over the river, effectively denying the bypass attempt. They must be already hovering over the correct placement, as very quick reflexes are required to correctly perform this technique.

For Bats, Skeleton Dragons, and Minion Horde, they should be placed right in front of the Hog Rider as soon as it is deployed.

For Minions, Skeleton Barrel, Mega Minion, Flying Machine, Electro Dragon, Baby Dragon, Inferno Dragon, Balloon, and Lava Hound, stagger the above placement one tile to the right if the Hog Rider is placed on the left side of the arena, and vice versa.

They can also use ground troops to achieve the same result. Something like an Ice Golem deployed at the Hog Rider’s landing spot will obstruct his path and force him to go around the unit, which causes him to be closer to the building instead of the Crown Tower.

The Hog Rider can kite Very Fast non-building targeting troops due to his own Very Fast speed and building only targeting if he is placed on the fourth tile from the bridge, slightly into the opposite lane. He can also stall grounded units when placed right at the bridge. He will pull them towards him while deploying, and then be untargetable by them when he jumps over the bridge. After landing, he will pull them back. This can be useful when the player needs to deal damage in the same lane they are defending. It will also help separate troops behind a tank in a large push.

A Tornado placed on the second tile front of the player's King's Tower and staggered two tiles towards the Princess Tower will activate it without any damage dealt to the Princess Tower, helping them in defending future pushes. This can also be a method of mitigating all damage dealt to a Princess Tower, but doing this more than three times may result in the King's Tower's health being low enough to be targeted directly, opening up the possible threat of a back door three crown. A better alternative is to pull the Hog away from the Princess Tower into the attacking range of all three Crown Towers, which will negate all damage as long as none of them are already distracted

A very powerful combo is the Hog Rider, the Musketeer, and the Valkyrie, typically referred to as the Trifecta. The Musketeer will defend against most troops, while the Valkyrie can protect her and the Hog Rider from swarms or high damage units. The Hog Rider is used to deal damage to the tower.

This can be effectively countered by Lightning, one-shotting the Musketeer and severely damaging both the Valkyrie and Hog Rider. The Minion Horde is also effective, but the enemy can Zap them and the Musketeer will one-shot them all. Even if the Musketeer is defeated, the Hog Rider and Valkyrie will have enough time to severely damage the Tower.

The Hog Rider should be placed behind the Valkyrie to give it a boost so that it stays in front of the Hog Rider, protecting it.

A Hog Rider combined with a Goblin Barrel can be awkward for the opponent to defend against. Timing it so that the Hog Rider is tanking the tower shots for the Goblins is the most effective way to deal damage. However, a Barbarian Barrel can shut this down with minimal Tower damage for a positive Elixir trade, as long as the Goblin Barrel was placed directly on the Tower.

Pairing the Hog Rider with the Balloon can deal devastating damage. If executed properly, the Hog Rider will act as a tank while the Balloon threatens to deal massive damage. The Hog Rider can also destroy any buildings attempting to slow down the combo. However, this combo is very vulnerable to swarms and anti-air cards as neither of the troops target anything but buildings. Additionally, they are easy to separate, due to the disparity in move speeds. Alternatively, the Hog Rider and the Balloon can be played in different lanes to spread the opponent's defenses thin. However, a building or Tornado can bring them back together for an easier defense.

The Hog Rider can be paired with the Lumberjack as both a swarm bait and damage combo. It is a very fast combo with an extremely high damage output potential, so the enemy will likely try to counter it with a swarm. If this happens, use a spell like Arrows to render the opponent defenseless. If they manage to defeat the Lumberjack, the dropped Rage will make the Hog Rider even more dangerous than it normally is.

A fast and deadly combination is the Hog Rider and Mini P.E.K.K.A. combo. Both units are fast but the Mini P.E.K.K.A. does much more damage and does not attack only buildings so the Mini P.E.K.K.A. can deal with troops like the Executioner and Musketeer. However, this combo can be defeated with swarms like Skeleton Army, which will defeat both of them since neither of them can deal area damage. They are also unable to target air troops, so the Minion Horde can stop this easily.

A risky play is to deploy the Hog Rider at the bridge as soon as the match starts. If the opponent does not react fast enough, the Hog Rider will deal a significant amount of damage to the Princess Tower. This can also allow the player to quickly scout the opponent's deck if they happen to react to him fast enough

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[0504c0a2b4...](https://github.com/Wallemations/heavenstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Monday 2022-05-16 16:33:17 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [rimadeodhar/cockroach](https://github.com/rimadeodhar/cockroach)@[13a65d3682...](https://github.com/rimadeodhar/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Monday 2022-05-16 17:08:04 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [Pokye/rathena](https://github.com/Pokye/rathena)@[d617d9f083...](https://github.com/Pokye/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Monday 2022-05-16 17:55:16 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [H0tP0cket/sidsrifolio](https://github.com/H0tP0cket/sidsrifolio)@[ee44663cbb...](https://github.com/H0tP0cket/sidsrifolio/commit/ee44663cbbf848e6e919bc06dbe7e2dcce74df36)
#### Monday 2022-05-16 18:08:45 by Siddharth Srinivasan

did some random shit need to make it not ugly as fuck

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[7c61bf65f2...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Monday 2022-05-16 18:21:55 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[e88f63cd33...](https://github.com/silicons/Citadel-Station-13-RP/commit/e88f63cd33d7e9bd0322ddb33de4cd6a5fb15fa7)
#### Monday 2022-05-16 19:21:19 by silicons

refactors some gun things (#4036)

* wow

* wack

* fix

* fix

* fuck you

* i am declaring war on gun devs

* fix

* fix

Co-authored-by: fake_vm_user <fake_vm_user>

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[fbd33d0b85...](https://github.com/facebook/pyre-check/commit/fbd33d0b8570c69957213b943255bba2c3c74285)
#### Monday 2022-05-16 19:23:29 by Shannon Zhu

Split find references for local and global names

Summary:
We probably can't support find all references with a table lookup, because we need to be able to handle requests on any name - not just function calls, and not just at the point of definition.

For example,

```
1: def foo() -> None:
2:    x = 1
3:    y = x
4:
5: def bar() -> None:
6:    foo()
7:
8: def baz() -> None:
9:    foo()
```

In this case, we'd need to be able to ask for "find all references" on `foo` on line 9, and return the `foo`s on lines 1 and 6. We need to be able to ask for "find all references" on `x` in line 2 and return the `x` on line 3.

Essentially, if we represented this as a mapping from reference -> list of references, every single reference in the list would also need its own entry to refer back to the rest of the group; so this isn't just a reverse callgraph lookup.

Given that we also need to support this for essentially every valid name: functions, attributes, globals, local values, class names, module names, etc., I think the only way to implement this is to take Hack's approach of tweaking the name of the reference in question, and then re-asking the type checker to calculate undefined name errors and converting those errors into reference locations.

In cases where we're asking for references of a name that is in the global scope, this starts to look a lot like unsaved changes overlays with a few exceptions (cc stroxler):

- Unsaved changes can be filtered down to only a module in question to prevent fan-out and keep things performant, also limit the memory footprint of writing overlay keys to all of the dependency tables. For find-all-references, we /need/ the fan-out and don't mind the perf hit, but this means we will need to make adjustments to make sure we aren't blowing up memory if we do many find-all-references checks in a row on the same server.
- To clean up the memory footprint, we'll either need to pay a heavy performance cost of remembering the last overlaid change and reverting it when applying the new overlaid change (I don't think this makes sense, since perf costs are highly variable depending on the name we pass in), or implementing a clean-up/sweep functionality that goes through shared memory tables and uses the dependency graph to delete keys written by the overlay check when we are done.
- We'll want to block writes to the dependency graph and just rely on the "logical" key to propagate our changes and propagate the cleanup.
- We'll need a transform visitor to figure out the right place to make the AST renaming change to kick off the incremental check.

In cases where we're asking for references of a name that is only in a local scope, we don't have to care about the environment at all - just take the relevant define body, make an adjustment to make sure the line defining the reference doesn't register or is modified, and then run an uninitialized local analysis on that one define and convert the errors to reference locations.

I'll tackle the local portion first before diving into the overlay/environment dependency changes needed to support this globally.

Note that: performance is likely not a concern here at all. find-all-references in Hack will load for minutes if you invoke it on some standard library function or basic class that is used all over the repository, as it should. Find all references should behave, performance wise, identically to a type check when the thing is changed. Also fun fact that pylance's find all references is also very slow and anecdotally seems quite flaky/often incorrect. I could not get a find all references request working at all in the current jedi setup.

Reviewed By: stroxler

Differential Revision: D35629810

fbshipit-source-id: 4761013b68a1389287731f9b9ac36fc749defcf3

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b340ae4806...](https://github.com/mrakgr/The-Spiral-Language/commit/b340ae4806a499bcd03419327dc28cee69d1f40f)
#### Monday 2022-05-16 19:35:45 by Marko Grdinić

"2:15pm. Done wtih breakfast. Let me read the hikivamp novel for a bit and I will resume.

I wanted to say, it really might not have been a bad idea to do more work in the modeling state. Separate rendering, freestyle edges, going over the bed with the clothes brush - things like that would have saved me time. I could also have filled the scene with flat colors in Blender. Also better modeling would make things better.

But it does not matter. I purposely made the models rough I intend to push myself a little in the painting arena. For the next work, I'll try getting things to come out exactly right.

2:55pm. That was fun. Let me resume. This is more the usual pace for me.

3:15pm. I am having to fight back my fear here. Let me finally do some shading.

3:40pm. Doing cloth creases like I am doing now is an enormous pain in the ass.

https://youtu.be/4AyD9GZJf0E
[ CLIP STUDIO PAINT ] Clothing Tutorial: Folds, Rouches and Frills

I get the sense I am trying to capture too much detail. Should I go for a cell shaded style like this?

https://youtu.be/4AyD9GZJf0E?t=36

When I say pain in the ass, I do not mean it like this.

I am sort of trying to emulate the lighting around the creases, meaning I had to draw a black line and the white line right next to it. Isn't there a brush that can do this automatically? Something like a dual brush?

3:50pm. Nevermind the fancy stuff. If need be I'll just stick to grinding out the bed one stoke at a time for now. It is not like I have to do the whole image like this. I'll just do the bed so I can get a measure of things. If need be I'll take a step back into the modeling stage and use sculpting to iron out the creases as well as model more objects. Or I'll take a step back from this super labor intensive style and try cell shading.

4:10pm. Let me take a break. I am thinking right now. This isn't doable. If I try to take the same approach as with the couch, I will be painting the individual bed creases for day here!

4:10pm. The couch had very good composition and not too much detail, and despite that it still took me 15h.

Forget painting. How about I just draw it for starters? Clean lines and blocked in shading. Some blur afterwards. Let me take a break just for a bit.

5:20pm. Shit. It feel like I am bashing my head against the wall using my existing methods. I put in the flats for the bed and literally the only part of it I like is the shaded part to the side. It really catpures the flat plane well.

But when it comes to do these creases I'd rather just run away.

Let me try again. This time I'll start with a vector layer.

https://artradarjournal.com/2022/02/19/how-to-change-color-of-vector-in-clip-studio-paint/

Let me make them black.

6pm. https://youtu.be/gwaUmkzNidU
How to Change Line Colour in Clip Studio Paint Tutorial

I can't figure out where the options are. Let me just watch this.

Oh, nice. I thought it might have been an accident, but once you have the lines and then use the magic wand tool, it draws a border straight through the middle. This would make managing them way easier than having a ton of different masks like when I was doing the couch.

6:10pm. https://www.clip-studio.com/site/gd_en/csp/userguide/csp_userguide/500_menu/500_menu_edit_linecolor.htm

Where the hell is this option?

Convert to drawing color! So that was it. Holy shit. Can't I use modifier keys in tool shortcuts? It seems I can't.

6:35pm. My inspiration has been quite low today, but now that I've done some lines and actually seen how auto select workson them, I am starting to feel it. Once I turn off the vector layer and and see that flat shading I really get a good feeling.

6:45pm. Time for lunch.

7:35pm. https://www.youtube.com/results?search_query=paint+sheet+folds

Let me just watch some of this. I can't figure out how to do the bed sheet folds.

7:40pm. https://youtu.be/gKiSb9aFJsA?t=136

Well, this is how I did the pillows for the couch roughly. I don't know. I am being a retard. I am trying to find an easy way to do the creases and failing. I got hung up on the stupidest of things. I am completely flumoxed as how how I should even approach them.

Let me try the lasso.

8:10pm. The lasso is much better, but the end result looks too taut to be bedsheets. Maybe I am just overdoing it. Maybe a rougher touch would be better.

https://4uview.com/373/83070/

This is Satanopany chapter 203. I am looking for inspiration how to draw cloth folds. They aren't much diffent in essence from what I am trying to on the bed. Interesting note that the folds are all two tone. I am trying to fit 3 tones on the bed and it is making the whole task a lot harder.

https://4uview.com/373/82536/

202. The author of Satanopany is such a mster. The cover pages for each chapter of this manga are always very well made.

https://4uview.com/373/81513/

201. He isn't using bluring like I am trying to do and the whole composition flows naturally. The cloth folds could be made using the lasso tool.

If you look at the rim of the skirt I am amazed that he got the highlights done correctly there.

Looking at the architecture in the background, and for example the carpet in ch 202, it is done so well, that I am betting 3d plays a role. But all the 3d that I've seen wasn't particularly good. I mean the cell shaded type.

8:35pm. I am really tempted to go through the series, collecting the cover pages as references.

9pm. I am still thinking about it.

9:05pm. I need to close. I am leaning towards doing more in 3d. I am not good enough to do it using the current reference. Instead what I should do is redo the beds in Moi tomorrow, put the blankets on them as well, do the extra objects on top of the shelves. I might also want to redo the door so it gets cut through properly.

I've been taking this too lightly. This is not just an illustration for me. The way I do this first scene is what is going to determine my whole style going forward. So I can afford to put in just a bit more effort.

Also forget doing the edge work by hand. I should make it a priority to investigate freestyle edges and toon shading.

9:15pm. Let me make a list of things to do.

* Fix the doors based on what the Moi author told me. As well as shorten one of the boards. Maybe even make it a bit thinner. I'll have to redo them to make this happen, but that is fine.
* Open the right grills a bit so the light can shine through properly.
* Remodel the beds, this time in Moi.
* Optionally the shelves as well.
* Put the blankes on the bed.
* Use the clothes brush to create the creases.
* Model some extra objects on top of the shelves as well as in the shelves.
* Do a sweep of the room edges with that stylized beveld wood specifically intended for corners.

Optionally, I can also model the lights on top of the ceiling, but they aren't present in the scene. Still the ceiling is a bit empty. I'll leave these two from the light of points. The above is enough to busy me.

9:20pm. But I do not feel like doing the above immediatelly. Supposing the Satanophany author is in fact using 3d, I can imagine him going over all the edges by hand, or that carpet for example.

Can I do anything in Blender to extra more information out of the model to me with what I am trying to do.

I gave it a serious try doing it by hand, but as expected my skills aren't up to the challenge. I can break solving the problem into a sequence of steps in 3d, but in 2d my skills are as lackluster as they could be. I am not 1/5, but I am on the lower end of 2/5 which is nothing.

The scene even as it is now is enough for me to experiment with toon shading and freestyle edges. Last year as I was getting into it, I watched those Blender for comics vids. I think tomorrow I should revisit that again.

9:30pm. I do not really care too much about whether I use 3d or 2d for the backgrounds. But it will take some effort to integrate 3d into a 2d style. I need to find a way. I'll embark on it tomorrow.

Of course it wouldn't be so easy. If anybody could just put up a scene in 3d and have it automatically translate into 2d, the world would have a lot more good looking manga. The level I am seeking is not achivable by somebody with mediocre talent in just 7.5 months. I am going to have to go all out to bring out the power of technology.

I should be upper 2/5 in 3d right now. I need to go a bit further to break through to 3/5."

---
## [jocrl/cockroach](https://github.com/jocrl/cockroach)@[0f1328cfb1...](https://github.com/jocrl/cockroach/commit/0f1328cfb16c88f1a891283fd028debfaf02beaf)
#### Monday 2022-05-16 20:19:56 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03 p`, or
- `1:03 P`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Typing `1:03pm`, `1:03PM`, or other versions without the space before `PM` still do not
work.

Additionally, typing the keys in `1:03 pm` will lead to the input being `1:03 PMm`, as the
`M` autofill after `p` is typed. The `1:03 PMm` input in the text box is still
accepted, but it does look weird and will likely be annoying to users who will
delete the trailing `m`.

Alternate approaches not pursued

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [cdcline/meta-puzzles](https://github.com/cdcline/meta-puzzles)@[223bab7210...](https://github.com/cdcline/meta-puzzles/commit/223bab7210de74395599eb213f5263bfcca0607b)
#### Monday 2022-05-16 22:01:39 by Chris Cline

Just calculate expected uniform values

I was talking to a friend about the problem and he mentioned
just "calculating all the expected values and checking if it's in
the range."

At first I thought it was a crazy idea b/c we don't acutally look
at any particular values in A or B but when thinking about it, for
any given power of 10, there's only 9 max uniform values.

So you could just "calulate" expected things if you figured out
the powers of 10 with a "max uniform value" within the range. Then
you only have to compare the inital pow of 10 and final pow of 10,
which is actually a pretty small amount.

This saves a TON on calculating (altho I think it's kinda cheating).

I broke the meta puzzle page tho somehow and it won't let me submit.

Seems to work for my test cases tho!

Thanks for the idea Sterling!

Co-authored-by: Sterling Hirsh <sterlinghirsh@users.noreply.github.com>

---
## [netflixfurimmer/Multi_Panel](https://github.com/netflixfurimmer/Multi_Panel)@[58efc0a4bf...](https://github.com/netflixfurimmer/Multi_Panel/commit/58efc0a4bf8ae51eea00f7fb959b1640df90c5cd)
#### Monday 2022-05-16 22:38:50 by ZFX_HACRYPT Exploit

Loud DDOS Panel Slamming 20 gig dstat      Tags  ddos attack, ddos attack explained, ddos panel, ddos attack roblox, ddosing, ddos tool, ddos apex legends, ddos roblox, ddos attack live, ddos attack tutorial, ddos attack kali linux, ddos attack website free, a ddos attack, ddosing a scammer, ddos a website, ddosing a ddoser, ddosing a minecraft server, doxing school, ddos a ip, ddos a router, ddos botnet, ddos booter, ddos bots tf2, ddos by daylight, ddos bot, ddos blizzard, ddos bot discord, ddos bluetooth, ddos crypto, ddos cloudflare, ddos coin, ddos csgo, ddos call of duty, ddos cod, ddos computerphile, ddos clash royale, c ddos script, reaper.c ddos, white c ddos, ddos c'est quoi, ddos discord, ddos dbd, ddos dead by daylight, ddos discord server, ddos download, ddos detection, ddos discord bot, ddos destiny 2, ddos explained, ddos em biet anh dang nghi gi, ddos error, ddos event, ddos exploit, ddos er, ddos eli5, ddos ethereum, attacco dos e ddos, o'que e ddos, ddos free, ddos fivem server, ddos fortnite, ddos from iphone, ddos facebook, ddos fortnite server, ddos fivem, ddos free tool, ddos ghost data, ddos gta 5, ddos gta, ddos gaming, ddos game servers, ddos glaive, ddos gta online, ddos github, ddos hack, ddos how to, ddos hacking song, ddos hacker, ddos hypixel, ddos hping3, ddos home router, ddos hammer, ddos in effect, ddos i_o, ddos internet attack, ddos ip address, ddos in kali linux, ddos is back, ddos in python, ddos in valorant, i does, i doesn't matter, i does what i wish to, i doesn't matter the rock, i does try to make you happy, i doesn't, i does do it like a boss machel montano, i doesn't matter how old i am, ddos jail, ddos jedag jedug, ddos jokes, ddos juniper, ddos jak zrobić, jensen ddos, jinn ddos, javascript ddos attack, ddos kali linux, ddos king, ddos kali, ddos karma, ddos kali linux 2021, ddos kali linux github, ddos kahoot, ddos kellogg's, ddos live, ddos league of legends, ddos ltg, ddos linux, ddos loic, ddos lucid, ddos link, ddos live attack, ddos mitigation, ddos meaning, ddos minecraft server, ddos mitigation techniques, ddos meme, ddos music, ddos multi tool, ddos methods, fivem ddos, ddos nasıl atılır, ddos net, ddos nedir, ddos news, ddos neighbors wifi, ddos network attack, ddos nfl mateja, ddos nasıl atılır discord, ddos overwatch, ddos on xbox, ddos on phone, ddos osrs, ddos overwatch ps4, ddos on kali, ddos on ps4, ddos on android, i_o ddos, o que é ddos ataque, o que e ddos, ddos protection, ddos panel free, ddos panel source, ddos python, ddos panel source code, ddos ps4, ddos protection by cloudflare, ddos questions, ddos quick guide, ddos que es, mac quayle ddos hacking song, comment ddos quelqu'un, ddos quelqu'un sur discord, ddos roblox server, ddos rainbow six siege, ddos roblox attack 2021, ddos ripper, ddos roblox script, ddos rocket league, ddos rust, ddos script, ddos school, ddos song, ddos script python, ddos software, ddos scammer, ddos school wifi, ddos someone, ddos tutorial, ddos titanfall 2, ddos tf2, ddos tool python, ddos tool free, ddos termux, ddos tool download, ddos using kali, ddos using python, ddos using ip, ddos using termux, ddos using cmd, ddos urban, ddos udp flood, ddos using a ldap reflection attack, how do u ddos someone, ddos vs dos, ddos valorant, ddos voip, ddos vs vpn, ddos vs dox, ddos vps, ddos vpn, ddos virus, gta v dos, ddos websites free, ddos website, ddos with kali, ddos with python, ddos warzone, ddos wifi, ddos with cmd, ddos wifi router, ddos w notatniku, jak ddosowac w minecraft, jak ddosowac w cmd, ddos w cmd, ddos xbox, ddos xbox 2021, ddos xbox one, ddos xbox live, ddos xbox gamertag, ddos xbox booter, ddos xbox party, xqc ddos, project x ddos, ddos x jedag jedug, ddos yiyen yayıncı, ddos yourself, ddos youtube, ddos yesterday, ddos yourself test, ddos your own network, ddos you, ddos your friends, dos y dos, ataque dos y ddos, ddos zoom meeting, ddos zoom, ddos zombie, ddos zombie nets, ddos zombie attack, ddos vent, ddos in effect xenoblade, ddos attack on zoom meeting, jak z ddosować kogos, ddos 127.0.0.1, ddos 101, ddos windows 10, ddos cs 1.6 server, titanfall 1 ddos, ddos tool windows 10, cách ddos 1 trang web, ddos cs 1.6, ddos 2021, ddos 2016, ddos 2019, 2b2t ddos, tf2 ddos 2021, dbd ddos 2021, ddos attack 2021, titanfall 2 ddos, titanfall 2 ddos update, titanfall 2 ddos attack, destiny 2 ddos, titanfall 2 ddos is back, slavehack 2 ddos, titanfall 2 ddos dlc, titanfall 2 ddos lore, ddos 33, teamspeak 3 ddos attack, teamspeak 3 ddos, ddos 403, ddos layer 4, ddos playstation 4, ddos gtps 4, ddos left 4 dead 2, layer 4 ddos script,

Loud DDOS Panel Slamming 20 gig dstat      Tags  ddos attack, ddos attack explained, ddos panel, ddos attack roblox, ddosing, ddos tool, ddos apex legends, ddos roblox, ddos attack live, ddos attack tutorial, ddos attack kali linux, ddos attack website free, a ddos attack, ddosing a scammer, ddos a website, ddosing a ddoser, ddosing a minecraft server, doxing school, ddos a ip, ddos a router, ddos botnet, ddos booter, ddos bots tf2, ddos by daylight, ddos bot, ddos blizzard, ddos bot discord, ddos bluetooth, ddos crypto, ddos cloudflare, ddos coin, ddos csgo, ddos call of duty, ddos cod, ddos computerphile, ddos clash royale, c ddos script, reaper.c ddos, white c ddos, ddos c'est quoi, ddos discord, ddos dbd, ddos dead by daylight, ddos discord server, ddos download, ddos detection, ddos discord bot, ddos destiny 2, ddos explained, ddos em biet anh dang nghi gi, ddos error, ddos event, ddos exploit, ddos er, ddos eli5, ddos ethereum, attacco dos e ddos, o'que e ddos, ddos free, ddos fivem server, ddos fortnite, ddos from iphone, ddos facebook, ddos fortnite server, ddos fivem, ddos free tool, ddos ghost data, ddos gta 5, ddos gta, ddos gaming, ddos game servers, ddos glaive, ddos gta online, ddos github, ddos hack, ddos how to, ddos hacking song, ddos hacker, ddos hypixel, ddos hping3, ddos home router, ddos hammer, ddos in effect, ddos i_o, ddos internet attack, ddos ip address, ddos in kali linux, ddos is back, ddos in python, ddos in valorant, i does, i doesn't matter, i does what i wish to, i doesn't matter the rock, i does try to make you happy, i doesn't, i does do it like a boss machel montano, i doesn't matter how old i am, ddos jail, ddos jedag jedug, ddos jokes, ddos juniper, ddos jak zrobić, jensen ddos, jinn ddos, javascript ddos attack, ddos kali linux, ddos king, ddos kali, ddos karma, ddos kali linux 2021, ddos kali linux github, ddos kahoot, ddos kellogg's, ddos live, ddos league of legends, ddos ltg, ddos linux, ddos loic, ddos lucid, ddos link, ddos live attack, ddos mitigation, ddos meaning, ddos minecraft server, ddos mitigation techniques, ddos meme, ddos music, ddos multi tool, ddos methods, fivem ddos, ddos nasıl atılır, ddos net, ddos nedir, ddos news, ddos neighbors wifi, ddos network attack, ddos nfl mateja, ddos nasıl atılır discord, ddos overwatch, ddos on xbox, ddos on phone, ddos osrs, ddos overwatch ps4, ddos on kali, ddos on ps4, ddos on android, i_o ddos, o que é ddos ataque, o que e ddos, ddos protection, ddos panel free, ddos panel source, ddos python, ddos panel source code, ddos ps4, ddos protection by cloudflare, ddos questions, ddos quick guide, ddos que es, mac quayle ddos hacking song, comment ddos quelqu'un, ddos quelqu'un sur discord, ddos roblox server, ddos rainbow six siege, ddos roblox attack 2021, ddos ripper, ddos roblox script, ddos rocket league, ddos rust, ddos script, ddos school, ddos song, ddos script python, ddos software, ddos scammer, ddos school wifi, ddos someone, ddos tutorial, ddos titanfall 2, ddos tf2, ddos tool python, ddos tool free, ddos termux, ddos tool download, ddos using kali, ddos using python, ddos using ip, ddos using termux, ddos using cmd, ddos urban, ddos udp flood, ddos using a ldap reflection attack, how do u ddos someone, ddos vs dos, ddos valorant, ddos voip, ddos vs vpn, ddos vs dox, ddos vps, ddos vpn, ddos virus, gta v dos, ddos websites free, ddos website, ddos with kali, ddos with python, ddos warzone, ddos wifi, ddos with cmd, ddos wifi router, ddos w notatniku, jak ddosowac w minecraft, jak ddosowac w cmd, ddos w cmd, ddos xbox, ddos xbox 2021, ddos xbox one, ddos xbox live, ddos xbox gamertag, ddos xbox booter, ddos xbox party, xqc ddos, project x ddos, ddos x jedag jedug, ddos yiyen yayıncı, ddos yourself, ddos youtube, ddos yesterday, ddos yourself test, ddos your own network, ddos you, ddos your friends, dos y dos, ataque dos y ddos, ddos zoom meeting, ddos zoom, ddos zombie, ddos zombie nets, ddos zombie attack, ddos vent, ddos in effect xenoblade, ddos attack on zoom meeting, jak z ddosować kogos, ddos 127.0.0.1, ddos 101, ddos windows 10, ddos cs 1.6 server, titanfall 1 ddos, ddos tool windows 10, cách ddos 1 trang web, ddos cs 1.6, ddos 2021, ddos 2016, ddos 2019, 2b2t ddos, tf2 ddos 2021, dbd ddos 2021, ddos attack 2021, titanfall 2 ddos, titanfall 2 ddos update, titanfall 2 ddos attack, destiny 2 ddos, titanfall 2 ddos is back, slavehack 2 ddos, titanfall 2 ddos dlc, titanfall 2 ddos lore, ddos 33, teamspeak 3 ddos attack, teamspeak 3 ddos, ddos 403, ddos layer 4, ddos playstation 4, ddos gtps 4, ddos left 4 dead 2, layer 4 ddos script,

---
## [LensPlaysGames/LensorOS](https://github.com/LensPlaysGames/LensorOS)@[9b91ffa65b...](https://github.com/LensPlaysGames/LensorOS/commit/9b91ffa65bc454ae088903bf738aa1e5c2a7eb1b)
#### Monday 2022-05-16 23:01:20 by Lens

Syscalls use System V ABI, like ELF

As ELF is our executable format of choice, at least for now,
why not also follow the same calling convention?

I don't see any reason why this won't work.
*cut to a week later when I hate myself for thinking this*

The `syscall()` function in libc will be able to
load it's arguments into the proper registers,
as well as the return value(s), if any are even present.

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[796aeaa98f...](https://github.com/sojourn-13/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Monday 2022-05-16 23:32:22 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---

