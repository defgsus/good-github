## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-13](docs/good-messages/2022/2022-03-13.md)


1,521,064 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,521,064 were push events containing 2,208,746 commit messages that amount to 113,814,495 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[745426eff2...](https://github.com/GoblinBackwards/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Sunday 2022-03-13 00:22:44 by LemonInTheDark

Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Derpius/DevApps](https://github.com/Derpius/DevApps)@[fcfda6f13c...](https://github.com/Derpius/DevApps/commit/fcfda6f13c1a867c1fba227a8facd59345e732e6)
#### Sunday 2022-03-13 00:24:02 by Vurv

rust

To be fair, you have to have a very high IQ to understand Rust. The pointer semantics are extremely subtle, and without a solid grasp of PL theory most of the concepts will go over a typical programmer's head. There's also Rust's zero-cost abstractions, which are deftly woven into the standard library - its architectural philosophy draws heavily from Haskell literature, for instance. The Rust evangelists understand this stuff; they have the intellectual capacity to truly appreciate the depths of this language, to realize that it's not just the future- it says something deep about LIFE. As a consequence people who dislike Rust truly ARE idiots- of course they wouldn't appreciate, for instance, the truth in Rust's existencial catchphrase "guaranteed memory safety, fearless concurrency, zero-cost abstractions" which itself is a cryptic reference to Edward Kmett's Haskell package Lens I'm smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Philip Wadler's genius unfolds itself on their computer screens. What fools... how I pity them. 😂 And yes by the way, I DO have a Rust tattoo. And no, you cannot see it. It's for the ladies' eyes only- And even they have to demonstrate that they're within 5 IQ points of my own (preferably lower) beforehand.

---
## [0b5vr/tweakpane-plugin-profiler](https://github.com/0b5vr/tweakpane-plugin-profiler)@[3a1bc9f2c9...](https://github.com/0b5vr/tweakpane-plugin-profiler/commit/3a1bc9f2c95ace0b1c3614ce8d1bb75dabbab31e)
#### Sunday 2022-03-13 03:00:52 by 0b5vr

BREAKING performance: fuck you GC

ProfilerBladeMeasureHandler no longer have path on its first
argument

---
## [Kscope-Devices/android_kernel_xiaomi_sdm660](https://github.com/Kscope-Devices/android_kernel_xiaomi_sdm660)@[a938b43afa...](https://github.com/Kscope-Devices/android_kernel_xiaomi_sdm660/commit/a938b43afab7eca662afd122b4677a76e246ba75)
#### Sunday 2022-03-13 03:04:28 by Maciej Żenczykowski

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
## [newstools/2022-new-telegraph-nigeria](https://github.com/newstools/2022-new-telegraph-nigeria)@[9084312505...](https://github.com/newstools/2022-new-telegraph-nigeria/commit/90843125054a8b734db361f4d6c33fb7f26ed482)
#### Sunday 2022-03-13 03:40:00 by Billy Einkamerer

Created Text For URL [www.newtelegraphng.com/bbnaijas-uriel-recounts-how-her-ex-boyfriend-body-shamed-her/]

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[759d24ab14...](https://github.com/tgstation/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Sunday 2022-03-13 03:44:37 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [DystopiaDump/kernel_xiaomi_vayu](https://github.com/DystopiaDump/kernel_xiaomi_vayu)@[201a806455...](https://github.com/DystopiaDump/kernel_xiaomi_vayu/commit/201a806455d086d735a96053a546562f9282296e)
#### Sunday 2022-03-13 04:44:54 by Wang Han

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: Jagaddhita Jalu <jaguarexodus@gmail.com>

---
## [double-a-stories/life-of-the-party](https://github.com/double-a-stories/life-of-the-party)@[1f929bcfbf...](https://github.com/double-a-stories/life-of-the-party/commit/1f929bcfbf3e0eff70079410b5c55c3c7d173e6e)
#### Sunday 2022-03-13 05:36:45 by double-a-stories

Changed religious references (e.g. "God")...

-Most characters reflexively use "oh my gosh" instead.
-Nikki/Nox are polytheists, and say "gods"
-Ana says "woof" and "oh my fuck" instead.
-Hollis's commands still use "oh god oh fuck"
-The "pantheon of animal gods" are no longer forgotten.

---
## [schqiushui/android_kernel_oneplus_sm8250](https://github.com/schqiushui/android_kernel_oneplus_sm8250)@[0fc91fe945...](https://github.com/schqiushui/android_kernel_oneplus_sm8250/commit/0fc91fe9452de8d7b547193adc4be2e37ad38816)
#### Sunday 2022-03-13 05:59:22 by alk3pInjection

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

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[884c1eeb62...](https://github.com/tgstation/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Sunday 2022-03-13 07:43:06 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [Fartlicker777/KTaNEShittyBeatsHoldable](https://github.com/Fartlicker777/KTaNEShittyBeatsHoldable)@[37c219308f...](https://github.com/Fartlicker777/KTaNEShittyBeatsHoldable/commit/37c219308fb116a5b39dbe7514bb8634ed821963)
#### Sunday 2022-03-13 09:22:43 by Fartlicker777

Updated to the current version

+ Zero's Song
+ Old Town Road
+ Mountain King (again)
+ Death by Krab Borg
+ Crack Miser
+ Roosevelt vs Churchill
+ BIG SHOT
+ Ghost Fight
+ Viral Song
+ Whatever the Fuck
+ Midnight Ride
+ FNAF Beatbox
+ BIG SPICE SHOT

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[51032656e6...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/51032656e67d198bf223fc2f7393c15a93043184)
#### Sunday 2022-03-13 10:04:43 by Hayden Pearce

munin-pihole-plugins: shit

My fellow Americans. As a young boy, I dreamed of being a baseball. But tonight I say, we must move forward, not backward; upward, not forward; and always twirling, twirling, twirling towards freedom!

Changes to be committed:
 - modified:   script/munin-pihole-plugins
   bump version to 2.9.3
   try to unfuck stuff i pushed to master
   fuck, seriously
   do. not. drink. and. merge.
   and sure as shit don't push, to master
   should probably just revert and redeploy - but, nope

---
## [Omicron166/LNS](https://github.com/Omicron166/LNS)@[9bed171a9d...](https://github.com/Omicron166/LNS/commit/9bed171a9d7085bb5a25a4c8d9c206a98bec67ad)
#### Sunday 2022-03-13 10:39:13 by Omicron166

new url parser

go fuck yourself urllib, no more problems with url ports

---
## [greenforce-project/kernel_xiaomi_citrus_sm6115](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115)@[0ce4d9f480...](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115/commit/0ce4d9f480f31f7297922af3dc3d56ff8b16fa0f)
#### Sunday 2022-03-13 11:44:29 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Reinazhard <reinazhard@gmail.com>

---
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[a718cb70a4...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/a718cb70a4e0dbcc74b99992cc93d9257c082d69)
#### Sunday 2022-03-13 12:43:06 by exordium-vic3

fuck you mito and artur bring back communist armenia REEEEEEEEEEEE

---
## [ImagineGamingPlay/Cheeku-Development](https://github.com/ImagineGamingPlay/Cheeku-Development)@[1af5ae6373...](https://github.com/ImagineGamingPlay/Cheeku-Development/commit/1af5ae6373e644b1d90a65d9eb5c0736ca533a82)
#### Sunday 2022-03-13 13:04:04 by WithoutIdeas

Update index.js v2

second time doing this, I hate my life

---
## [team-eoanb/EoaNB](https://github.com/team-eoanb/EoaNB)@[3bb7bedc87...](https://github.com/team-eoanb/EoaNB/commit/3bb7bedc876b1b062883bd6b8b5a48717d5b9d31)
#### Sunday 2022-03-13 14:16:53 by Kenhel

Major Serbian Updated - Eco n Political tree

The Eco tree now have effects and ideas, no events and decisions since those have yet to be drafted, same goes with the politics before the regency, as for the regency itself, we are working on a transition between the 2 trees so ima a add a skeleton of it maybe later because this was so fucking painful, fixing all the errors and shit, there are still some left but mighty kuba told me not to touch them, so im not gonna touch them, its kuba so i def aint taking my chances with touching those stuff anyways this was pain oh god help the economic tree is unbelievably large, watch serbia show up as one of the major interesting nations along side prussia lmao

---
## [openlab-aux/vuizvui](https://github.com/openlab-aux/vuizvui)@[10c9c75cd3...](https://github.com/openlab-aux/vuizvui/commit/10c9c75cd335802ee698c790a4ac739e6cece5f7)
#### Sunday 2022-03-13 14:35:54 by devhell

profiles/packages: Add packages

I'm particularly interested in `gurk-rs` as it's a Signal client that
runs in the terminal. It's in early development but it looks already
amazing and it doesn't rely on the Java library.

`termusic` is also a nice music player written in Rust that I've come to
enjoy when MPD doesn't make sense.

Lastly, `writedisk` is just mad awesome. It can write ISOs of all sorts
to USB stick, and it even knows how to deal with Windows ISOs. It writes
those ISOs really fast as well, so I'm guessing it somehow measures the
ideal block size. Either way, this is much more convenient than having
to invoke `dd` every time I have to write an ISO. Funny enough, this too
is a Rust application.

---
## [ryangjchandler/natalie](https://github.com/ryangjchandler/natalie)@[c2a7d2c4ae...](https://github.com/ryangjchandler/natalie/commit/c2a7d2c4ae628380d7e8c7c321a800ea6848fd6b)
#### Sunday 2022-03-13 15:13:49 by Tim Morgan

Don't require Tempfile when running in interpreted mode

This is kinda an ugly hack, but I don't know how I want to handle this
sort of thing when interpreting Ruby. We should load the Tempfile
provided by MRI instead? Thought required...

---
## [ecatmur/gcc](https://github.com/ecatmur/gcc)@[aeac414923...](https://github.com/ecatmur/gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Sunday 2022-03-13 15:18:24 by Thomas Schwinge

Revert "Fix PR 67102: Add libstdc++ dependancy to libffi" [PR67102]

This reverts commit db1a65d9364fe72c2fff65fb2dec051728b6f3fa.

On 2021-09-17T01:01:39-0700, Andrew Pinski via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
> On Fri, Sep 17, 2021 at 12:46 AM Thomas Schwinge <thomas@codesourcery.com> wrote:
>> On 2021-09-15T13:56:37-0700, apinski--- via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
>> > The error message is obvious -funconfigured-libstdc++-v3 is used
>> > on the g++ command line.  So we just add the dependancy.
>>
>> > --- a/Makefile.def
>> > +++ b/Makefile.def
>> > @@ -592,6 +592,7 @@ dependencies = { module=configure-target-fastjar; on=configure-target-zlib; };
>> >  dependencies = { module=all-target-fastjar; on=all-target-zlib; };
>> >  dependencies = { module=configure-target-libgo; on=configure-target-libffi; };
>> >  dependencies = { module=configure-target-libgo; on=all-target-libstdc++-v3; };
>> > +dependencies = { module=configure-target-libffi; on=all-target-libstdc++-v3; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libbacktrace; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libffi; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libatomic; };
>>
>> I'm confused, because given that this 'Makefile.def' change only has the
>> following effect:
>>
>> > --- a/Makefile.in
>> > +++ b/Makefile.in
>> > @@ -61261,6 +61261,7 @@ all-bison: maybe-all-intl
>> >  all-flex: maybe-all-intl
>> >  all-m4: maybe-all-intl
>> >  configure-target-libgo: maybe-all-target-libstdc++-v3
>> > +configure-target-libffi: maybe-all-target-libstdc++-v3
>> >  configure-target-liboffloadmic: maybe-configure-target-libgomp
>> >  all-target-liboffloadmic: maybe-all-target-libgomp
>> >  configure-target-newlib: maybe-all-binutils
>>
>> ... isn't that actually a no-op, because we already had such a dependency
>> listed?  Now twice:
>>
>>     $ grep -n -F 'configure-target-libffi: maybe-all-target-libstdc++-v3' -- Makefile.in
>>     61264:configure-target-libffi: maybe-all-target-libstdc++-v3
>>     61372:configure-target-libffi: maybe-all-target-libstdc++-v3
>>
>> Compared to the existing one, the one you've added is additionally
>> restricted by '@unless gcc-bootstrap'.
>>
>> I noticed this as I remembered that on our og[...] development branches
>> we have a patch in the opposite direction: get rid of this dependency via
>> removing 'lang_env_dependencies = { module=libffi; cxx=true; };' from
>> 'Makefile.def'.  See
>> <http://mid.mail-archive.com/alpine.DEB.2.21.9999.1812201344250.99920@build7-trusty-cs.sje.mentorg.com>
>> "Disable libstdc++ dependency for libffi".  (Maciej CCed in case you have
>> any further thoughts on that.)
>
> Oh, I see what happened now, the old bug was actually fixed by r6-5415
> which added cxx=true.
> So yes my patch is actually not needed and can be reverted.
> I tried to look to see if there was a dependency was there but for
> some reason I did not see it.

---
## [wyw5445/kx](https://github.com/wyw5445/kx)@[08617de495...](https://github.com/wyw5445/kx/commit/08617de495cfb0c93361ae3380637e3c6a26cac2)
#### Sunday 2022-03-13 15:25:59 by AmCath

alt Tammany portrait should they say fuck you democracy

---
## [G3-Studio/Grief-Day](https://github.com/G3-Studio/Grief-Day)@[bfe839ebec...](https://github.com/G3-Studio/Grief-Day/commit/bfe839ebecca217d4b0f045b44526cad2073eaaa)
#### Sunday 2022-03-13 15:37:38 by Vincent Gonnet

I commited a horrible and unbelievable sin, sorry Teddy, shall you forgive me master

---
## [team-eoanb/EoaNB](https://github.com/team-eoanb/EoaNB)@[b0d9e4defc...](https://github.com/team-eoanb/EoaNB/commit/b0d9e4defcdb7d2f5e8d45e0518d38796dab9bcb)
#### Sunday 2022-03-13 15:42:05 by Kenhel

Last serbian skeleton

today was a painful day anyways heres the last fucking skeleton its 11:41 pm and i wnated to get it done today so i got it done today damn it ima go do the effects and ideas tommorrow if i feel like it

---
## [bandithijo/dwm](https://github.com/bandithijo/dwm)@[67d76bdc68...](https://github.com/bandithijo/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-03-13 16:00:32 by Chris Down

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[e90c879880...](https://github.com/san7890/bruhstation/commit/e90c87988036bc2e93363be517fc63b25b40963b)
#### Sunday 2022-03-13 17:22:18 by san7890

Mapper's Delight: Directional Poster Spawners [MDB IGNORE]

A lot of my PRs have been focused on having a fire lit under the seat of my pants. However, this PR is based off one conversation I had with someone.

"Haha, mapper. All you do is var_edits."

It was a bit more verbose than that, but it really did get me thinking about how fucking massive our files our thanks to these var_edits. This PR adds directional helpers to both A) Help mappers map the correct things with as little var edits as possible and B) Lessen the amount of space each fucking map file is thanks to however many extra bytes are taken up with pixel_x = 32. we have a lot of posters.

Bluntly put, this PR adds directional helpers to all generic /random poster spawners. i would add them to every single poster in the game, but that's a lot of work for unique posters, and someone can probably come up with a better idea. Good luck with that, this is just a good first step.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1234e88d33...](https://github.com/mrakgr/The-Spiral-Language/commit/1234e88d33fc6349531a6140f12df7d26a70d329)
#### Sunday 2022-03-13 21:03:02 by Marko Grdinić

"https://www.reddit.com/r/vfx/comments/miqzm7/what_does_clarisse_do_and_who_uses_it/

Some interesting comments here.

///

Clarisse's main benefit (in my experience) is that it can handle a lot more geometry than other renderers.

I worked on a project making a massive 3D city... in Maya the city had to be rendered in clusters and then comped together in 2D. It was somewhat frustrating to work with because renders that had too many unique buildings would often crash.

Some of the buildings were quite detailed and even a lone asset or two made Maya, c4d etc start to chug.

I was able to bring in the entire city in Clarisse and render it fairly easily. It's very good at handling a lot of unique geometry... not just scattering the same model (although it can do that as well)

It would be useful to a dmp artist that was responsible for cobbling together a lot of their own geo and didn't really have time to go through and decimate/remesh 3D assets all the time.

///

///

I use c4d and it doesnt take much complexity and polygon count before you really have to start using solutions like proxy geo and instances or rely on Redshift proxies or vray proxies etc.. or rendering out parts background in one pass, foreground in one pass etc VDBs in one pass and so forth. and really managing how everything is going to layer up in the comp. Clarisse expands the headroom of polygon limit so you can really load up your scene with everything and you have a robust renderer IPR that is always giving you feedback. So you can build your environment with a cityscape populate it with all the details add the some alembic files of destruction and particles sims then add vdbs of clouds scatter them and you can still fly around the scene like a god and the viewport doesn't choke from all of the elements that would choke C4d or Maya or whatever... this is what I have seen from the demo videos... this makes is a kind of central hub to take everything you build in other apps and bring it to Clarisse. Its pretty amazing when you start fiddling around with it...you are like "are you sure I can add this and this and this and multiply this and that?...wtf!!!"

///

It is worth trying out. I am thinking - if Houdini can barely handle 5k flowers, how will I do an entire city in it? I am going to have problems doing what I want to do in Houdini or Blender either way.

10:50pm. https://www.reddit.com/r/vfx/comments/k7p0c0/houdini_clarisse_nuke_drone_explosion_chase/

A very short clip here.

> Basically its for building your scene, lighting and rendering. Its been used on a TON of movies. And used by studios like ILM and DNEG for there environments. Clarisse can handle MASSIVE polycounts. Like TRILLIONS of polygons! Its awesome. So I use Houdini or any other 3d software to build the basic layout, animation, models and assets. Then bring it into Clarisse where I can use super high poly assets and scatter millions of objects to make my scenes feel more realistic. Then I do all the lighting and rendering in Clarisse.

Exactly what I want.

3/13/2022

9am. I seem to be really looking forward to the day these past few weeks. I'll have remember to include the above comments in the commit.

9:05am. Ok...let me start downloading the course. After that I'll start going through the Clarisse tutorials. I was on the wrong track with Houdini. If it is just one off assets, maybe I'll have no need for it all. Well, this wouldn't be the first time I've wasted two months down the drain due to getting on the wrong path. My whole life I've been the wrong path.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
Beginner's Journey with Clarisse - Part1 - Fundamentals

I'll start this from scratch. I haven't been able to follow it properly yesterday due to fatigue, but now I am ready to get going. I'll thoroughly get familiar with Clarisse and master my style thanks to it. I won't be using V-Ray and Houdini for lookdev. One good thing I'll get out of it is the V-Ray asset library though.

https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=230

Now that I am learning how to do layouting, it makes me realize what a mess my Blender stuff was. It actually never occured to me to just copy an instance for the layouting work. I did do better separation in Houdini, but it was still messy compared to this since I did not have a separate folder for assets. The problem is that having a separate object network would make them disappear from the scene. The way Clarisse does it is really very clean. As expected of a dedicated tool for this.

I am definitely going to downgrade Houdini and Blender to asset creation tools rather than my mainstays.

10:45am. How do I change multiple properties all at once?

I thought that all I had to do was drag over the fields like in Blender, but that is not it. No, nwm. It seems there isn't a way. But I can switch easily between fields by tabbing and shift tabbing.

10:55am. https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=272

5km on both sides? Now that's scale!

My thought to make it big was to size it up by 40x.

https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=351

I am starting to sense what combiners are going to be. Remember how in Blender it was a massive pain in the ass to move that couch around? I'd click on it and then move a pillow or just its frame by accident. For that reason I had started merging objects, but that had the disadvantage of applying its modifiers. This was one of the motivations for switching to Houdini. I could easily do things like bevels and subdivs and merge the object pieces together and move it around.

It is absolutely amazing how appropriate Clarisse is for me at my current stage of development. It might be exactly what I need. I am starting to get my hopes up.

11:35am. Huh, I managed to crash Clarisse simply by messing around. It seems none of these programs follow proper reactive principles in their design.

11:40am. I am liking the Clarisse UI so far though. I think this was the first time I actually moved the camera properly. What I did was simply move it using the move tool. It turns out that when you are looking through it, you only rotate the camera. Which makes sense. Remember how painful it was to put it into the right position in Houdini? It makes sense to have a split view and move it separately.

12:20pm. https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=663

Let me stop here for the morning. It seems a displacement map on the crater is going to come in here.

1:35pm. Done with breakfast and chores. Let me chill a bit more and I will resume.

https://www.asianhobbyist.com/high-school-girl-warrior-how-to-save-an-apocalyptic-world/high-school-girl-warrior-31/

I liked this story when it was a manga, and I meant to catch up for a while. It has the same feel as early Kumo.

1:55pm. Maybe my natural state is to just enjoy fiction rather than make it...but I need to master the style I am going for.

I once read the quote: "Even if Michaelangelo only had a bucket and a mop, the Sixtinth Chapel would still have been made."

I am sure that Michaelangelo would have agreed with me that whoever made that quote is a moron. The best way to get better at anything is to master a better tool. It is inevitable that I'd go down wrong directions. I got some experience that will make future work easier. And I might end up using Houdini for various things.

Let me resume.

2:25pm. https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=787

I am really confused what those bounds are supposed to be. I'll deviate from the tutorial and just adjust the offset instead. That will allow me to have smaller bounds.

Actually, I see it does work. The bounds work strangely. Displacement does not work as a straight division, but some kind of projection. It is not visible from the sides, but only if the view is set to the entire render context. Did I really need to split the grid?

2:35pm. I might be getting fooled by bump maps. It does some weird thing to make the terrain appear lively.

Clarisse does not do displacement as any other programs. Instead of me putting in the bounds myself, I wonder why it does not calculate them automatically?

https://youtu.be/A83Jhj1fyjM?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=907

Ah, the combiners are in fact exactly what I thought they were. This is something I'd see as an absolute necessity for layouting.

3:10pm. Actually, it is fairly hard to move the camera. I wish I had something like the first person view. The way I am trying to do it now is ridiculous.

3:20pm. https://youtu.be/CK0UYRwDb2c
Clarisse 5: Camera Overlays

Let me watch this since I am having trouble directing the camera.

3:30pm. Nope, the above was on something else.

https://www.awn.com/news/isotropix-clarisse-55-now-available

I guess I'll get access to Angie a few months from now. But I see that the version I have already has GPU support. I haven't tried it though.

4pm. I am really missing the snapping options that Blender has. As well as the axis hotkeys.

4:15pm. Instead of messing with manual movement I should have used copy stamp to make more instances.

4:20pm. Lunch seems to be early today. Let me have it.

4:30pm. Done with lunch. I went crazy with placing barrels, though not too crazy. Much like in Blender copy pasting objects is a chore. But copy stamping them is pretty great.

4:35pm. https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
Beginner's Journey with Clarisse - Part3 - Lighting Basics

Yeah, this is the kind of material that I should have moved on to immediatelly after Blender. Like in programming if you pick the wrong design, you will have no end of trouble.

5:05pm. Let me stop messing around with rotating the light and move on.

The way it is currently set up, it is difficult to point the light where you want it. Blender has the better interface. Even Houdini allows you to go into the light and point is as a camera. Let me watch the videom. Maybe it will give me some hints how to set it up.

5:10pm. Goddamit, it is hard to set up the light properly like this.

5:25pm. Doesn't this stupid thing have hotkeys like Blender?

5:30pm. Ah, as long as it is selected it is possible to snap it to wherever. I do not have to use the manipulator.

5:45pm. Shit, moving around is so difficult in this. Where did the light disappear. There are some UI bugs present.

...No wait. Somehow I managed to dive into the light itself. How did that happen?

5:50pm. Ah, I see. I can select the light and then press L to look through it much like a camera. The scroll whell does not work for zooming after that for some reason, but Alt + right clicking does.

5:55pm. Clarisse's rendering engine is pretty nice. It is raytracing, but it does not hug all the rig resources and it is quite fast, way faster that V-Ray.

I think that I am finally getting a grasp on how to move things around.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=173

Why is he copy pasting and rotating it 180? There is a double sided option that can be checked.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=321

It is great to not have to worry about how changing colors and assigning material could crash the program. Also not having to wait 10s before I get something of decent quality.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=344

> This is a very powerful workflow. Please see our shading layer tutorials for more information on this topic.

Noted. I will.

6:30pm. https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=483

This is not working for me. No matter how low I set the density, it is always pure black.

...I must have assigned the material incorrectly.

...It is not the name. What I did wrong was not notice that the rule needs to be active!

6:55pm. It crashed, and to make matters worse, it took out the OS alongside it. I had to hit the reset key. That download that spent hours in the background and was at 90%? Gone. I'll have to restart it from scratch.

I guess I do need worry about assigning colors and changing materials leading to a meltdown.

Let me take a break here. I am going through thse basic tutorials at a snail's pace.

7:15pm. Let me resume. A part of the reasons why I am having these long sessions is because they resemble playing games more than programming. I am really bashing my head against the wall trying to plan through a tough problem. Rather it is more like getting accomodated to an environment. It is not just motivation, but the overall mental intensity of the task is lower.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=581

This ability to instance lights is pretty good. Blender lacks a good browser. And for Houdini, the less I think about its lookdev the better.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=593

I just realized that his distant light must be colored while mine is pure white. Ah well.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=615

Disney Principled? Not Autodesk Surface?

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=700

The way the imports work is elegant. Also, I tried disabling and enabling the barrel folder and confirmed it very well could be possible to switch between multiple lookdev folders based on that. But I bet Clarisse will have smoother mechanisms for swapping shaders than that.

7:50pm. The way the material editor is designed is quite good.

Hmmm, things are a bit weird. Does it have proper UVs assigned?

8pm. No, I just had to pass it through the normal map node. So far, based on the feel of the program, I can tell that Clarisse would be worth paying 500$ a year for it. By artists for artists was right. It is very sleek and fast and well designed, even though I'll have to spend some time getting used to it.

8:10pm. Agh, if you use the shading layer it does not actually work.

8:35pm. I keep forgetting to exit the camera and moving it by accident using F. To make things aven more troublesome that ends up focusing the camera on an object.

https://clarissewiki.com/4.0/move_camera.html

> You can also see through selected lights or cameras by pressing L key. You can also press Look through... (7) and browse for an item. If you wish to switch back to the free view, just press L key again or press (7) and select no item by clicking to an empty space of the browser.

8:40pm. It crashed with an out of bounds access. Messing with the camera was what made it happen.

8:50pm. https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=872

Let me rewatch this last part and I will call it a day. I wonder how he just dragged it into the lake. When I tried doing that it assigned it to the fog. Geh. I wish I knew how to make objects unselectable.

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=939

He has it disabled. When did he do that?

https://youtu.be/ZKP4E2aXpAI?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=773

It just ends up being disabled between frames.

9pm. I tried playblasting, and it kept the HUD information.

9:15pm. I'll figure out how to save images at a later point. I've looked into the shader rules for some of this stuff. I think that the > allows different materials to be assigned to different parts of the image. And I think the rules take priority from most to least specific rather than in the input order. I still don't know what some of the stuff does. I thought that Gathering SL would be a shader layer, but for some reason when I double click it, it opens up the 3d view.

SL rules also override material linkage when the layer is used.

9:25pm. Let me close here. I do not have the energy to mess around with more.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
Beginner's Journey with Clarisse - Part4 - Procedural Layout

I'll play around with scattering tomorrow. Sigh, it will be worth it...eventually. When I shed my humanity through the power of technology, I am going to be doing this for the rest of eternity so I might as well get into the swing of things ahead of time. That was one of the thoughts leading into this.

Maybe I'll get a bite for those AI chip posts, but my emotions are telling to just forget about that crap and buy them via regular way. That way I won't have any obligations to sponsors. The fact that I am not getting bites might be doing me a favor as I won't get exploited this way.

I've been thinking what I am going to do on the third Spiral run, and I've decided. In addition to doing the AI chip backends, I'll make a ref counted F# backend if careful memory management of something like GPU memory becomes necessary. That way I'll close all the gaps.

I'll get the benefits of staged functional programming all across the board.

Cython really made me mad when I tried bechmarking it and found it to be on par with Python due to the object allocation/deallocation costs.

9:30pm. I feel like I've gained a lot today. The ability to properly separate instances, assets and lookdev should not be underestimated. I actually understand what the point of Solaris is now, not that I'll use it.

If I had to go back to Blender, I'd definitely change my habits to match what I've learned today. I didn't really understand what instancing was about it seems.

I'll try to redo the pool scene one last time in Clarisse. The third time will definitely succeed.

9:40pm. Tomorrow, I'll finish the rest of the tutorial and then explore the rest of the material. I think a week or two of indepth studying this should be enough to get me up to speed. It won't be like Houdini when it is like studying an entirely new framework.

I've looked at the material nodes, and they aren't any more complex than Blender's shading nodes. In fact, it does not seem like Clarisse has the equivalent of geo nodes.

Clarisse is a lot closer to being an art program and than a programming language.

The trouble with doing programming, like in Houdini is that programming is really slow. Something I could do easily using direct modeling, in something like 5m, would take longer than an hour with procedural modeling. In the last two months, I had to absorb a completely different way of thinking about art in order to get decent at Houdini. It was hugely energy and time intensive. But with Clarisse I just need to learn its interface and the various knobs that it has. It is more like learning to drive a car than programming.

9:50pm. I've learned my lesson with V-Ray. I won't try to push success again in such a manner. It was just luck that I found out about Clarisse, but I should applaud myself for being decisive when it comes to switching.

I am going to establish my workflow in the next few months and break into the 3/5 range as an artist. Nothing will stop me. I will not give up in my efforts to break through to the level of true skill.

Though saying that is trying to hurry things along. At the rate I am currently going, it feels that it will take a few years for me to become so proficient that everything comes to me with ease in this domain. But still that isn't an extreme amount of time to acquire such a skill. It is certainly worth it.

Rather than flaming out pathetically due to not being able to hack it in ML, I am going to build a solid foundation from which to make further gains."

---
## [emrecancorapci/tcgy_3-bookArchive](https://github.com/emrecancorapci/tcgy_3-bookArchive)@[28708114f7...](https://github.com/emrecancorapci/tcgy_3-bookArchive/commit/28708114f7a86b7d9d0aa78f85727134d5501a16)
#### Sunday 2022-03-13 21:29:11 by emrecancorapci

New publisher form and some changes
- Publisher form created and works really well.
- Author form is renamed and fixed. And it checks if new author is exist in db.
- Now languages can be added to new books.
- Now requied fields are needs to be fill. ( Why wasn't it like that before? :/)
- Now most of the buttons are colored! ( YAY! )
- Now all the exceptions handling elegantly. ( Except if you find another one. Please don't find another one. )

Bugs and lack of usefullness to be fixed :
- You cannot add multiple author or publisher. :((((
- You cannot see all the authors in the database unless you click on the list of authors while adding a new book. ( And it's not that hard you know. )
- You cannot see all the publishers in the database unless you click on the list of publishers while adding a new book. ( Not gonna say it twice )
- You cannot see book details. ( This is kinda sad. )
- You can add the same book twice and more. ( I allow this for a short time. ( Short time means until I'm not lazy enough to fix it) )
- You can add the same publisher twice. ( I hope it doesn't cause copyright wars. )
- You cannot add images of books. ( You may never see this one. )
- You cannot add book dimesions. ( Why do you even need it? )
- You cannot add your comment to books. ( Freedom of speech? I didn't say you can't say it. )
- You cannot see whether the books have been read or not. ( hehe )
- Most of the fields are not requied to offend perfectionsits. ( And I am one of them. ( This shouldn't be on this list. This is a feature. )

---
## [NobilityDeviant/RealmCrakV2](https://github.com/NobilityDeviant/RealmCrakV2)@[74cfd29b48...](https://github.com/NobilityDeviant/RealmCrakV2/commit/74cfd29b489fe59bdf3144a50b47cf26ad8815be)
#### Sunday 2022-03-13 23:02:21 by NobilityDev

Removed tons of useless code and assets.

Renamed & reorganized a couple of classes and code.

Added a toast to show quick popup messages and used it in certain places.

Created an enum to represent the current page.
- Used to increase perfomance

The entire interface is now completely resizable. :) finally!!

Added new design to alert pop
- Also moved all alerts to a single class

Proxy checker now sorts by status at the start.

Proxy checker now checks to see if your ip has been received. If not, it asks you to try again if
you try to start the proxy checker.

Fixed a couple ui issues i dont remember..

Program now centers on screen on launch

Proxy checker now automatically sorts bt status when a working proxy is found.
- Yes it might be annoying if trying to sort with something else, but i find it useful.

Edit item list is now resizable.
- nice little design change too.

Updated items to the latest.

Proxy settings design has been updated.
- Colors are off, but it's too much of a pain to edit.

Checker progress now shows 4 digits instead of one

Removed all old classes and functions related to the database.

Replaced tons of alerts with toasts.
Alerts will now only be used for important messages.

Progress bars now have colors.

Scroll bars all now use the same css values.

Removed the updater.
- Now when a github update is available, it asks if you want to open the github page.
- Might add an updater in the future. I didn't include the jar, so we have to wait.

---
## [nik9000/elasticsearch](https://github.com/nik9000/elasticsearch)@[37ea6a8255...](https://github.com/nik9000/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Sunday 2022-03-13 23:38:36 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---

