## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-05](docs/good-messages/2022/2022-06-05.md)


1,575,782 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,575,782 were push events containing 2,230,399 commit messages that amount to 112,089,592 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [KDr2/rust](https://github.com/KDr2/rust)@[07f586fe74...](https://github.com/KDr2/rust/commit/07f586fe746a362fdebfc1cec0016dd024780dce)
#### Sunday 2022-06-05 00:02:30 by Dylan DPC

Rollup merge of #96642 - thomcc:thinbox-zst-ugh, r=yaahc

Avoid zero-sized allocs in ThinBox if T and H are both ZSTs.

This was surprisingly tricky, and took longer to get right than expected. `ThinBox` is a surprisingly subtle piece of code. That said, in the end, a lot of this was due to overthinking[^overthink] -- ultimately the fix ended up fairly clean and simple.

[^overthink]: Honestly, for a while I was convinced this couldn't be done without allocations or runtime branches in these cases, but that's obviously untrue.

Anyway, as a result of spending all that time debugging, I've extended the tests quite a bit, and also added more debug assertions. Many of these helped for subtle bugs I made in the middle (for example, the alloc/drop tracking is because I ended up double-dropping the value in the case where both were ZSTs), they're arguably a bit of overkill at this point, although I imagine they could help in the future too.

Anyway, these tests cover a wide range of size/align cases, nd fully pass under miri[^1]. They also do some smoke-check asserting that the value has the correct alignment, although in practice it's totally within the compiler's rights to delete these assertions since we'd have already done UB if they get hit. They have more boilerplate than they really need, but it's not *too* bad on a per-test basis.

A notable absence from testing is atypical header types, but at the moment it's impossible to manually implement `Pointee`. It would be really nice to have testing here, since it's not 100% obvious to me that the aligned read/write we use for `H` are correct in the face of arbitrary combinations of `size_of::<H>()`, `align_of::<H>()`, and `align_of::<T>()`. (That said, I spent a while thinking through it and am *pretty* sure it's fine -- I'd just feel... better if we could test some cases for non-ZST headers which have unequal and align).

[^1]: Or at least, they pass under miri if I copy the code and tests into a new crate and run miri on it (after making it less stdlibified).

Fixes #96485.

I'd request review ``@yaahc,`` but I believe you're taking some time away from reviews, so I'll request from the previous PR's reviewer (I think that the context helps, even if the actual change didn't end up being bad here).

r? ``@joshtriplett``

---
## [Waklaidan/tgstation](https://github.com/Waklaidan/tgstation)@[20e4add487...](https://github.com/Waklaidan/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Sunday 2022-06-05 01:00:08 by Tim

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
## [greenforce-project/kernel_xiaomi_juice_sm6115](https://github.com/greenforce-project/kernel_xiaomi_juice_sm6115)@[38b0bd0f25...](https://github.com/greenforce-project/kernel_xiaomi_juice_sm6115/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Sunday 2022-06-05 02:29:16 by Linus Torvalds

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[cbf2bd9fbc...](https://github.com/pytorch/pytorch/commit/cbf2bd9fbc376f0b147709fcfe6b119f082658d3)
#### Sunday 2022-06-05 02:53:31 by Edward Z. Yang

Update base for Update on "Replace TensorMeta with FakeTensor"


Alrighty this one is a doozy so listen up.

- FakeTensor by eellison is a better version of TensorMeta, with the primary difference that it makes use of Meta definitions in the dispatcher rather than directly reading out the meta field on the function callable. This is an important improvement because it means that we can use FakeTensor with conventional torch API calls whereas we could only use TensorMeta with refs. A number of previously failing python_ref_consistency tests are now passing, and post this change I recommend using torch API in refs as much as possible (E.g. when you are not making use of new functionality that only occurs in refs). There is no downside and the upside is that it is possible to get fused eager kernels without being forced to decomposed
- To avoid having to wobble all of the Prim metas, I keep a function named TensorMeta that has the old API for constructing fake tensors. TBH all of these should be using methods like new_empty instead
- I need an API for excluding the autograd dispatch key from TLS; the standard `no_grad` doesn't cut it. I exposed the low level TLS functions but on advice by alband we should probably expose the higher level API.
- How prims get registered to dispatcher has changed: previously their implementations were registered as CompositeImplicitAutograd but that prevents prims from getting traced which is no good. So now they are CompositeExplicitAutograd. A consequence of this is that AD on prims stops working but this makes sense since previously we were relying on their aten implementations to implicitly provide AD, which is not long term how it should be implemented. This also means prims are going to show up in traces so backends be ready (I wonder if we need a BC lower back to backends pass). Because backwards no longer works I have to disable it in the OpInfos.
- ProxyTensor is annoyingly recording overload packets to FX IR rather than overloads, which means I can't find the `impl_nvfuser` properties. But since prims are guaranteed to have only one overload I just spray the properties on both the overload and the overload packet
- The PrimContext tracer is now completely subsumed by the ProxyTensor tracer. Well actually I made things worse since ProxyTensor isn't using fake tensors for metadata (but this is the plan)
- Since PrimContext is dead I also had to update execute to take a GraphModule directly instead. But wait there's more: for some reason the old algorithm for constructing nvFuser graphs doesn't work with ProxyTensor's FX graphs, so I rewrote it from scratch to use an FX interpreter rather than mutating the FX graph. Newer implementation is shorter and more correct.
- I simplified TensorLikeType to be literally Tensor (actually we could have done this before but forgot). However this triggered some mypy errors in `atleast_1d` and friends. I fixed it by writing a more verbose implementation which I think is more accurate. In general, however, I feel that it is hard to replicate overload behavior purely in Python
- I relaxed FakeTensor to work with meta tensor inputs cuz this codepath gets triggered in PrimTorch tests
- We are starting to hit some import cycles so there are some shenanigans to keep Python mypy happy

Signed-off-by: Edward Z. Yang <ezyangfb.com>

[ghstack-poisoned]

---
## [Sector-Echo-13-Team/Echo13](https://github.com/Sector-Echo-13-Team/Echo13)@[91795aa57f...](https://github.com/Sector-Echo-13-Team/Echo13/commit/91795aa57f5ecc4aeee81e91a50e08de0d960be5)
#### Sunday 2022-06-05 03:21:38 by TheNeoGamer42

Arrowhead-Class Long Range Scoutship (#111)

* woo

* i kinda fucking forgot i moved an entire room and that there was a wall there now

* god fucking damnet the other wall too

* wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwires

* you know this really throws a wrench in my plans, you know? I hate wrenches in my plans.

* slightly less sane piping to infuriate both myself and others. also a waste hookup for that portable scrubber I threw in.

---
## [VictorZisthus/CHOMPStation2](https://github.com/VictorZisthus/CHOMPStation2)@[4704df506b...](https://github.com/VictorZisthus/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Sunday 2022-06-05 03:52:28 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [Sagit-Kscope/kernel_xiaomi_msm8998](https://github.com/Sagit-Kscope/kernel_xiaomi_msm8998)@[81cb3d10f4...](https://github.com/Sagit-Kscope/kernel_xiaomi_msm8998/commit/81cb3d10f442a0ced767c774abbc46ec06b63608)
#### Sunday 2022-06-05 03:56:08 by Maciej Żenczykowski

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
## [Sinbest/mojave-sun-13](https://github.com/Sinbest/mojave-sun-13)@[2996f41136...](https://github.com/Sinbest/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Sunday 2022-06-05 04:02:55 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [rlawoehd187/android_kernel_pantech_msm8937](https://github.com/rlawoehd187/android_kernel_pantech_msm8937)@[2f76ba6132...](https://github.com/rlawoehd187/android_kernel_pantech_msm8937/commit/2f76ba6132472593e1201a2a6916dd02db3b8d5c)
#### Sunday 2022-06-05 04:53:44 by Masahiro Yamada

BACKPORT: modpost: file2alias: go back to simple devtable lookup

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Change-Id: I3d1201177711fd3e2935336d592970a90923d54f
Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Link: https://git.kernel.org/linus/ec91e78d378cc5d4b43805a1227d8e04e5dfa17d
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>

---
## [ItsSelis/VOREStation](https://github.com/ItsSelis/VOREStation)@[38724d4d4c...](https://github.com/ItsSelis/VOREStation/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Sunday 2022-06-05 09:26:29 by VerySoft

[WIP] pAI tweaks and upgrades

Changes some things around! 

Removes the 'wipe' button from pAI's interface, since I think there being an instant 'kill player' button is pretty lame, especially since most pAIs activate on their own without a master. They're easy enough to kill or contain without this, so I don't see it as necessary. If you want to kill your pAI friend just eat them. :U

Removes the 'pAI Suicide' verb, and renames the 'Wipe Personality' to 'Enter Storage' and moved it from the OOC tab to the pAI Commands tab. Killing a pAI deletes the card and all that, where the 'Enter Storage' verb deletes the card and spawns a new one that can be used, which! I think it more appropriate.

Makes it so that, when damaged, pAIs will slowly regenerate while folded up, at a rate of 0.5 brute and burn per life tick, where previously it had been impossible to recover health outside of admin intervention.

Updated the Universal Translator with many of the newer languages that aren't obviously for events or hivemind type things.

Added the same emotes that humans can use to pAIs

Added an alternative pAI card style, and rearranged the expressions for the cards a little bit, and added one more.

Plan to add more pAI chassis to play with

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2b7819777f...](https://github.com/mrakgr/The-Spiral-Language/commit/2b7819777f89740557d292d1c858fccd4b9b69b7)
#### Sunday 2022-06-05 10:31:03 by Marko Grdinić

"8:10am. I am up really early for some reason. I am groggy right now. Yesterday it occured to me that once I get NNST working, I could turn it into an app or a Blender plugin and sell it.

https://youtu.be/5j8I7V6blqM
NVIDIA’s New AI Grows Objects Out Of Nothing! 🤖

https://youtu.be/yl1jkmF7Xug
NVIDIA's Ray Tracing AI - This is The Next Level! 🤯

Then I watched these two. For the last one, I realized that I could try TensTorrent with an offer to make a ray tracer. I've always thought that NNs could be used to accelerate rendering, but now I see that in action for the first time successfuly. AI chips would be more suited for this than GPUs, though I do not understand rendering well enough to say if global memory is needed or if local memory will suffice. Probably the later.

8:20am. This is an element of the true path. It gives you opportunities to make money on the side. It is not like I have to rely solely on Patreon donations for Heaven's Key. Since I have strong programming and NN skills, I should use that to supplement my 3d journey.

It is far from hopeless for me, I just have to put in the effort. ML will pay off for me in the end. It is not right to expect to do everything by hand for a person like me.

8:25am. Ok, let me chill for a while. First comes Egg of the Elf.

9:10am. Let me finish ch 48 of Legendary Mechanic and I will get started. Forget the nonsense about doing a ray tracer for TensTorrent. I should just do what would benefit me directly. If I make a Blender plugin of NNST and some Youtuber covers it, I could get 100s and 1000s of sales.

9:40am. Let me get started. That was fun, but I should put some work into it. Forget patching. I realized that due to upscaling, the effective patch size would need to be larger. Still, the upscaling happens only 3 times. It is not a big deal. But what about...no, I don't get. Nevermind this. Let me go with checkpointing. I think that even with upscaling the upper levels can draw in data beyond the bounds. Patching is not the solution.

Also, rather that checkpointing, an idea came to me just now. Since I am dealing with a CNN, if I do some smart padding, I can split the image into patches and get a result equivalent to the original. This would have the advantage of allowing me to work on images of any size.

```py
# Free gpu memory in case something else needs it later
if misc.USE_GPU:
    torch.cuda.empty_cache()

```

I had no idea this was possible.

9:50am. Let go over the source for all of this.

10:05am. It sure has a lot of stuff. It is well commented I'll give it that. Regardless, this kind of undertaking is not for the faint of heart.

10:15am.

```py
    def forward(self, x_in, inds=[1, 3, 6, 8, 11, 13, 15, 22, 29], concat=True):

        x = x_in.clone()  # prevent accidentally modifying input in place
        # Preprocess input according to original imagenet training
        mean = [0.485, 0.456, 0.406]
        std = [0.229, 0.224, 0.225]
        for i in range(3):
            x[:, i:(i + 1), :, :] = (x[:, i:(i + 1), :, :] - mean[i]) / std[i]

        # Get hidden state at layers specified by 'inds'
        l2 = []
        if -1 in inds:
            l2.append(x_in)

        # Only need to run network until we get to the max depth we want outputs from
        for i in range(max(inds) + 1):
            x = self.vgg_layers[i].forward(x)
            if i in inds:
                l2.append(x)
```

I see it having 4 slices, but what are these indices?

10:25am. Let me take a break here. This is going to be a pain in the ass to get to work with checkpointing. Most likely I will have to change things, but I'll manage it somehow.

10:55am. Let me get back into it. Reading code is always a boring activity.

https://bottosson.github.io/posts/oklab/

A lot of novel stuff is in the repo.

```py
    x_norm = torch.sqrt((x**2).sum(1).view(-1, 1))
    y_norm = torch.sqrt((y**2).sum(1).view(-1, 1))
```

Using the specialized norm functions would have made things more efficient.

11:05am.

```py
def dec_lap_pyr(x, levs):
    """ constructs batch of 'levs' level laplacian pyramids from x
        Inputs:
            x -- BxCxHxW pytorch tensor
            levs -- integer number of pyramid levels to construct
        Outputs:
            pyr -- a list of pytorch tensors, each representing a pyramid level,
                   pyr[0] contains the finest level, pyr[-1] the coarsest
    """
    pyr = []
    cur = x  # Initialize approx. coefficients with original image
    for i in range(levs):

        # Construct and store detail coefficients from current approx. coefficients
        h = cur.size(2)
        w = cur.size(3)
        x_small = F.interpolate(cur, (h // 2, w // 2), mode='bilinear')
        x_back = F.interpolate(x_small, (h, w), mode='bilinear')
        lap = cur - x_back
        pyr.append(lap)

        # Store new approx. coefficients
        cur = x_small

    pyr.append(cur)

    return pyr
```

What's a laplacian pyramid? I goggled it. I'll have to dive deeper in order to figure out what is it for.

11:10am.

```py
def whiten(x, ui, u, s):
    '''
    Applies whitening as described in:
    https://openaccess.thecvf.com/content_ICCV_2019/papers/Chiu_Understanding_Generalized_Whitening_and_Coloring_Transform_for_Universal_Style_Transfer_ICCV_2019_paper.pdf
    x -- N x D pytorch tensor
    ui -- D x D transposed eigenvectors of whitening covariance
    u  -- D x D eigenvectors of whitening covariance
    s  -- D x 1 eigenvalues of whitening covariance
    '''
    tps = lambda x: x.transpose(1, 0)
    return tps(torch.matmul(u, torch.matmul(ui, tps(x)) / s))
```

Let me check out the paper just for a bit.

11:35am. I've gone over the code. There is not a small amount of it, but it is not large by any means either. It is nicely commented, and this all seems like a decent short job, suitable for my skills. The next try is to try running it. Before I try it on my own, I've noticed that it has a web demo. Let me try passing in my own big image after downscaling it.

11:40am. Damn it, what style did I use for that room image?

Ah, the butterfly. I can check out the results in my account rather than just the folder.

'Copied style images cannot be downloaded.' What a ripoff.

I did it manually. Right now it says it is warming up the server.

```
## Hardware Requirements
Primarily tested in gpu mode with nvidia gpus using cuda, cpu mode implemented but not tested extensively (and is very slow).
Generating 512x512 outputs requires ~6GB of memory, generating 1024x1024 outputs requires ~12GB of memory.
```

Ah, I see where the youtuber got his hardware reqs, from the repo readme.

11:50am. Forget anything too fancy.

```py
python styleTransfer.py --content_path inputs/content/C1.png --style_path inputs/style/S4.jpg --output_path ./output.jpg
```

Let me just run this once.

11:50am. Looks nice. Let me try the high res web version.

11:55am.

```
(base) PS E:\NeuralNeighborStyleTransfer> python styleTransfer.py --content_path inputs/content/C1.png --style_path inputs/style/S4.jpg --output_path ./output.jpg
Downloading: "https://download.pytorch.org/models/vgg16-397923af.pth" to C:\Users\Marko/.cache\torch\hub\checkpoints\vgg16-397923af.pth
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 528M/528M [02:15<00:00, 4.07MB/s]
C:\Users\Marko\anaconda3\lib\site-packages\torch\nn\functional.py:3609: UserWarning: Default upsampling behavior when mode=bilinear is changed to align_corners=False since 0.4.0. Please specify align_corners=True if the old behavior is desired. See the documentation of nn.Upsample for details.
  warnings.warn(
-(0, 64)-
C:\Users\Marko\anaconda3\lib\site-packages\torch\nn\functional.py:718: UserWarning: Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important
until they are released as stable. (Triggered internally at  ..\c10/core/TensorImpl.h:1156.)
  return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
-(1, 128)-
-(2, 256)-
-(3, 512)-
Traceback (most recent call last):
  File "styleTransfer.py", line 65, in <module>
    output = produce_stylization(content_im_orig, style_im_orig, phi,
  File "E:\NeuralNeighborStyleTransfer\utils\stylize.py", line 107, in produce_stylization
    target_feats = replace_features(feats_c, feats_s)
  File "E:\NeuralNeighborStyleTransfer\utils\stylize.py", line 166, in replace_features
    d_mat = pairwise_distances_cos_center(ref_flat, src_flat)
  File "E:\NeuralNeighborStyleTransfer\utils\distance.py", line 66, in pairwise_distances_cos_center
    return pairwise_distances_cos(center(x), center(y))
  File "E:\NeuralNeighborStyleTransfer\utils\distance.py", line 26, in pairwise_distances_cos
    d = 1. - torch.mm(x / x_norm, y_t)
RuntimeError: CUDA out of memory. Tried to allocate 1.06 GiB (GPU 0; 4.00 GiB total capacity; 1.87 GiB already allocated; 822.46 MiB free; 1.94 GiB reserved in total by PyTorch)
```

What trouble. Couldn't it go for another Gb? Can I pre-allocate 3gb manually in PyTorch.

12pm. At any rate, given that it came to this point, I can assume that nothing would have prevented me from running the script if I had enough memory. There is nothing I need to do to adapt it to Windows.

12:10pm. Right now I am passing in Nostalgia from the /wip/ thread. I want to see what NNST gives me back.

12:20pm. I am thinking about it. The result is actually pretty impressive. Way better than DDG.

NNST is worth optimizing so it runs at higher res.

It will give me a huge advantage in the art journey. Even if it took me a month it would still be worth it, let alone a few days. And more than just using it for myself, this is something worth selling. If I can make an addon that does style transfer as well as upscaling, it would be worth putting on Blendermarket and Gumroad.

12:25pm. Let me have breakfast here. After that I will look into finding out my system's GPU memory capacity. PyTorch might have an easier time allocating 3gb all at once rather than in chunks."

---
## [justACatBuryMe/activate-linux](https://github.com/justACatBuryMe/activate-linux)@[6012d283ca...](https://github.com/justACatBuryMe/activate-linux/commit/6012d283caeb096b9667ce759f0eeb92c0e99005)
#### Sunday 2022-06-05 11:55:41 by Reperak

Fix rgba_color_string returning default

Shame on me for not testing before submitting #65, and shame on the people who reviewed #65 for trusting my stupid ass.

Fixes #99

---
## [13spacemen/tgstation](https://github.com/13spacemen/tgstation)@[cd294e9040...](https://github.com/13spacemen/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Sunday 2022-06-05 12:17:22 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [13spacemen/tgstation](https://github.com/13spacemen/tgstation)@[245ec35dae...](https://github.com/13spacemen/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Sunday 2022-06-05 12:17:22 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

---
## [Guidesu/sojourn-station](https://github.com/Guidesu/sojourn-station)@[796aeaa98f...](https://github.com/Guidesu/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Sunday 2022-06-05 12:41:36 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [caido/diesel](https://github.com/caido/diesel)@[448df6b615...](https://github.com/caido/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Sunday 2022-06-05 13:48:34 by Georg Semmler

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
## [Chargnn/gutenberg](https://github.com/Chargnn/gutenberg)@[3ea2d42b0a...](https://github.com/Chargnn/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Sunday 2022-06-05 13:49:15 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [Goratrix/goratrix-crawl](https://github.com/Goratrix/goratrix-crawl)@[1352289c90...](https://github.com/Goratrix/goratrix-crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Sunday 2022-06-05 13:50:22 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [CodeIGuess/CodeIGuess.github.io](https://github.com/CodeIGuess/CodeIGuess.github.io)@[fbd413538b...](https://github.com/CodeIGuess/CodeIGuess.github.io/commit/fbd413538b741e1e27f71fb8ad1d63dbbe4b6279)
#### Sunday 2022-06-05 14:02:26 by CodeIGuess

I need this

It fakes a call. Pretty shitty, yeah, but I need this to get out of an awkward social situation, _specifically today_

---
## [alalek/opencv_contrib](https://github.com/alalek/opencv_contrib)@[78392f786d...](https://github.com/alalek/opencv_contrib/commit/78392f786da6d3871590c62d88e6ba323d834e5b)
#### Sunday 2022-06-05 15:37:01 by fegorsch

Rename `near` to `zNear`

`near` is an illegal variable name on Windows (if `windef.h` is included),
because a macro with the same name is defined.

Someone else already put your rage into words, see
http://lolengine.net/blog/2011/3/4/fuck-you-microsoft-near-far-macros.

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[27946f516d...](https://github.com/Zytolg/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Sunday 2022-06-05 15:52:08 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[5c0764e7e4...](https://github.com/EtraIV/MerchantStation13/commit/5c0764e7e4079abb539e36eba6fdaade4e77ca1e)
#### Sunday 2022-06-05 16:07:09 by EtraIV

Moves the point vendors to the FUCKIGN VENDING DIRECTORY HOLY SHIT TCEO WHY DID YOU PUT THEM IN ECONOMY YOU IDIOT

---
## [Singe-Horizontal/rathena](https://github.com/Singe-Horizontal/rathena)@[d617d9f083...](https://github.com/Singe-Horizontal/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Sunday 2022-06-05 16:14:29 by Aleos

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
## [NonCoderAlias/Merchant-Station-13](https://github.com/NonCoderAlias/Merchant-Station-13)@[663688130e...](https://github.com/NonCoderAlias/Merchant-Station-13/commit/663688130e83b094351f8cdf1b1d20a6b0c80c4b)
#### Sunday 2022-06-05 16:26:29 by karmaisblackandbluepilled

I hate /tg/code so much it's actually unreal (#57)

* Hulk Recoil Removal go fuck yourself 41 damage for one wall

* medical doctors have access to genetics, again, why was this removed FUCK you

* buffs bpowder and methsplosions back up, fuck you edge

* Unnerfs chemicals for speed why why why why why

* adds silver back to synthesizers but removes the solidification reaction, for obvious reasons

* unfucks the dna sequencers because genetics is a shit minigame and making it harder to solve is for [SLUR REMOVED]

* did what the guy above told me to(?)

---
## [planetscale/vitess](https://github.com/planetscale/vitess)@[dbfb9a49f7...](https://github.com/planetscale/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Sunday 2022-06-05 17:27:22 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [The-Merchants-Guild/Merchant-Station-13](https://github.com/The-Merchants-Guild/Merchant-Station-13)@[144b5838c0...](https://github.com/The-Merchants-Guild/Merchant-Station-13/commit/144b5838c01985628a46954e276f5f643596634c)
#### Sunday 2022-06-05 17:44:30 by karmaisblackandbluepilled

Adds surplus crate-only items. (#256)

* Funny stuff right here

* is this piece of shit ACTUALLY complaining about indentation in a fucking comment fuck you

---
## [makingglitches/GooglePhotoDownload](https://github.com/makingglitches/GooglePhotoDownload)@[d9074bdcfb...](https://github.com/makingglitches/GooglePhotoDownload/commit/d9074bdcfbaa038194d3544e30511317ccddde6b)
#### Sunday 2022-06-05 17:52:22 by John Sohn

Added some logic to handle tracking mountpoints
Added some logic for searching for downloaded files and matching them against file items in database
to prevent re-download
Made some notes about needed changes.

Eg.  Need to create a prompt in searchlocal.js to handle unmounted devices
     Also need to resolve multiple copies of the same file
     Also need to implement the storeitemlocation table
     Also need to investigate what is happening at startup in index.js regarding marking files missing and consider prompting user to redownload the files.  The logic in searchlocal as this newest fucking pig evil bitch shows up with her victim has already been considered while in wholefoods a this point in Boston, MA.

---
## [markkiths/android_kernel_asus_msm8916](https://github.com/markkiths/android_kernel_asus_msm8916)@[64a8d273c6...](https://github.com/markkiths/android_kernel_asus_msm8916/commit/64a8d273c6207206e96a6c958f6fdaa564a1af83)
#### Sunday 2022-06-05 19:21:43 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

[ Upstream commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d ]

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: If4290e58a2c34a7f69e2aa8e9ec0b07f15792d21

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[e37591540b...](https://github.com/MidoriWroth/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Sunday 2022-06-05 19:25:06 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [ilya-zhidkov/nis](https://github.com/ilya-zhidkov/nis)@[ceefa3d7da...](https://github.com/ilya-zhidkov/nis/commit/ceefa3d7dab0c5ced659708b514ad8c1429f9190)
#### Sunday 2022-06-05 19:27:21 by Ilya Zhidkov

api: Retrieve Moodle courses

We are beginning our journey of removing hard-coded values.

First step is to acquire the actual courses alongside its assignments.
Unfortunately, I couldn't find a "convenient" way of asking for a course.
Unless a student remembers or knows the identifier of a course there is now way to get the assignments.
Of course, it's a bad user experience. It makes way more sense to get a course by a name, or its short-code.

Other than that, a few quality of life improvements have been made:

- When authorization fails => return 401 (Unauthorized) instead of 400 (Bad request)
- Default course id has been set to 5 which corresponds to our own playground.

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[220cf3628a...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/220cf3628aadc159468cd72591abc5cd5e75c7c2)
#### Sunday 2022-06-05 19:34:59 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Kneba <abenkenary3@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [ishitbyabullet/thewasteland](https://github.com/ishitbyabullet/thewasteland)@[013fb2bd4b...](https://github.com/ishitbyabullet/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Sunday 2022-06-05 20:12:36 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [trydalcoholic/opencart](https://github.com/trydalcoholic/opencart)@[89c304ae61...](https://github.com/trydalcoholic/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Sunday 2022-06-05 21:09:35 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [PhantasarProductions/StarStory2](https://github.com/PhantasarProductions/StarStory2)@[27f13a7e87...](https://github.com/PhantasarProductions/StarStory2/commit/27f13a7e87ddbd71ca349b1a8fc1ea1133b87548)
#### Sunday 2022-06-05 22:17:57 by Jeroen Broks

FUCKING CRAP SHIT AND DAMNATION! NOTHING LEADING TO THIS PUSH IS POSSIBLE AND I HAD TO VOID MY AWAY AROUND A KIND OF MAGIC!

---
## [aRandomN3rd/Idlegame](https://github.com/aRandomN3rd/Idlegame)@[35ab2d12b2...](https://github.com/aRandomN3rd/Idlegame/commit/35ab2d12b21b33abd91477ac471c9ec1cab519f9)
#### Sunday 2022-06-05 23:35:24 by aRandomN3rd

i keep breaking shit

Made the cavaliers and new currency system work, broke the fuck out of pickaxes please help oh my god there are so many pickaxes

---

