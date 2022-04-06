## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-05](docs/good-messages/2022/2022-04-05.md)


1,908,223 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,908,223 were push events containing 3,067,116 commit messages that amount to 220,499,926 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 21 messages:


## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[b995fbe31b...](https://github.com/Zonespace27/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Tuesday 2022-04-05 00:23:07 by Zonespace

Contractor Expansion 2 (#12311)

* weh!

* fuck you linter

* very important

* Update modular_skyrat/modules/contractor/code/datums/midround/event.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Update modular_skyrat/modules/contractor/code/datums/midround/outfit.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* requested changes

* also this

* requested + cleanup

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [mqt635/terminal](https://github.com/mqt635/terminal)@[446f280757...](https://github.com/mqt635/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Tuesday 2022-04-05 00:26:55 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [LunarWatcher/Acacia](https://github.com/LunarWatcher/Acacia)@[61d5af99f5...](https://github.com/LunarWatcher/Acacia/commit/61d5af99f57ec7521090a2ea2c32ab7e16764ea2)
#### Tuesday 2022-04-05 00:34:16 by Olivia

Basic compiling

God fucking damn that was complicated

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[55336d1e53...](https://github.com/JohnFulpWillard/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Tuesday 2022-04-05 01:45:11 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cef4383bc0...](https://github.com/treckstar/yolo-octo-hipster/commit/cef4383bc092e4c664e4909a3fe822c3c28d3210)
#### Tuesday 2022-04-05 02:45:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Cutiekittypet/Tannhauser-Gate](https://github.com/Cutiekittypet/Tannhauser-Gate)@[242ef904f0...](https://github.com/Cutiekittypet/Tannhauser-Gate/commit/242ef904f0a2ea2cc5de87863e93def5131ea0be)
#### Tuesday 2022-04-05 05:11:15 by SkyratBot

[MIRROR] Fixes bartender drink throwing, makes smashing always spill [MDB IGNORE] (#12326)

* Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

* Fixes bartender drink throwing, makes smashing always spill

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [jurgengjoncari/calculator](https://github.com/jurgengjoncari/calculator)@[6f6dccd185...](https://github.com/jurgengjoncari/calculator/commit/6f6dccd18589e96931182800d63d20ed2e521c23)
#### Tuesday 2022-04-05 06:12:02 by Jurgen Gjonçari

Apparently it's too damn difficult to revert to the past in git so I have to manually delete everything. GIT FUCKING SUCKS!

---
## [UQ-PAC/bap](https://github.com/UQ-PAC/bap)@[368286012d...](https://github.com/UQ-PAC/bap/commit/368286012d31312cfc785d940dd89e1f882c7bff)
#### Tuesday 2022-04-05 06:34:44 by Ivan Gotovchits

relaxes the Apply.binop function to allow not well-typed operations (#1422)

We are not changing the typing rules of BIL or Core Theory, but
providing a well-defined behavior for application of binary operations
on bitvectors with unequal lengths. Before that, the behavior was
undefined and the precondition of the function was clearly specifying
that the inputs should be of equal lengths.

The new behavior is to promote words to the equal length, (much like
in C, which implicitly coerces the narrow type to the wider type).

The motivation is simple. It is hard to ensure this precondition in
general. Yes, our lifters produce well-typed code, so there are no
issues when we interpret code from the lifters. But we also have a lot
of different interpreters, extensible via primitives. And those
interpreters sometimes don't have any means (or at least efficient
means) to ensure that all binary operations have matching widths. A
concrete example of such interpreter is Veri that is used for
bi-interpretation of traces and BIL programs for
verification. Sometimes, the tracers organically produce ill-typed
code, as they rely on their own typing rules. For example, qemu-based
tracer just represent every register (including flags) and every
number (including bools) with a word-sized bitvector. We still want to
be able to perform calculations on such inputs and, to be honest, the
results are quite well-defined, no hacks required. In other words,
this change tries to follow the robustness principle, i.e., "be
conservative in what you do, be liberal in what you accept from
others". Our lifters, i.e., the code that we produce, are still much
conservative, but our interpreters tend to be more liberal and
understand even the ill-typed code, especially if this code has clear
semantics.

---
## [garett09/Hulo](https://github.com/garett09/Hulo)@[11c3e1b1a2...](https://github.com/garett09/Hulo/commit/11c3e1b1a2e8734198fea9171f97420df2e4aa95)
#### Tuesday 2022-04-05 08:44:06 by Adrian Sian

backend: fuck you im done

Change-Id: Icf5da5cac3c3220500c0502ef5b870bce908eb6a

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e58fb506ef...](https://github.com/timothymtorres/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Tuesday 2022-04-05 09:14:16 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[3a417c1b21...](https://github.com/kleinesfilmroellchen/serenity/commit/3a417c1b210926fb47070695866d691e20176b2a)
#### Tuesday 2022-04-05 12:33:40 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [oscardssmith/julia](https://github.com/oscardssmith/julia)@[62e0729dbc...](https://github.com/oscardssmith/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Tuesday 2022-04-05 18:40:12 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [thekayperson/Solaroid](https://github.com/thekayperson/Solaroid)@[b37f0ec3e8...](https://github.com/thekayperson/Solaroid/commit/b37f0ec3e8fc1d07c87df9acc060f5c922804fe5)
#### Tuesday 2022-04-05 18:52:11 by thecrisperson1

got a bunch of stuff done i cannot be asked to write it all so fuck you

---
## [zeta96/L_soul_santoni_msm4.9](https://github.com/zeta96/L_soul_santoni_msm4.9)@[7e969f0ca1...](https://github.com/zeta96/L_soul_santoni_msm4.9/commit/7e969f0ca128c539dec50755904d6f47b5349423)
#### Tuesday 2022-04-05 18:57:25 by Maciej Żenczykowski

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
## [vignetteapp/vignette-web](https://github.com/vignetteapp/vignette-web)@[0085366487...](https://github.com/vignetteapp/vignette-web/commit/0085366487d49b80730489b2e59f9b7691174235)
#### Tuesday 2022-04-05 19:06:21 by Ayane

Engineering blog, nya! (#88)

* Engineering blog, nya!

* why isn't it showing up D:

* ヽ(*。>Д<)o゜

* thank you timezones (┬┬﹏┬┬)

* Fuck you YAML ヽ(*。>Д<)o゜

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0dce3fbc6d...](https://github.com/mrakgr/The-Spiral-Language/commit/0dce3fbc6d795cc10f970cfe20284c6f4c5810fa)
#### Tuesday 2022-04-05 19:26:30 by Marko Grdinić

"10:15am. I said I would do the pattern in CSP, but I ended up obsessing all night over it and figured out how to do it in Designer. So let me try it out in Designer then. I want to get started right away.

There is no hope for me. At this rate, I'll end up studying how to do that tree bark.

11:05am. Sigh, though the ideas worked, I cannot get close enough to the pattern on my desk. I have no idea how to do it. Let me just draw it.

11:45am. No, doing it by hand is not doing it for me either.

I am on the wrong track. I keep thinking that the wood pattern is special, but it is not. It is standard wood pattern. The (radial) knots are just close to each other.

I could probably immitate what I see here by using the regular wood pattern.

To make sure the lesson sticks, I am going to study the Designer file for that wood bark pattern. Let me take a break here first.

12:35pm. Done with chores. Breakfast time.

1:15pm. Done with the last ep of Kuroitsu. Now I only have Fabiniku until I am done with the last season.

Let me say what I wanted to say earlier.

If I want the wood pattern, I should just use the existing ones. If none of the starter ones are good, no doubt I'll be able to find something on the community site.

But deep down, it annoys me to just be a brainless consumer. I should not use something unless I can replicate it myself.

1:25pm. I guess I'll do what I want today and study that wood texture in Designer. Let me chill a bit more first.

1:50pm. Let me resume. First let me get that file.

...It is 121kb while the rest are 100s of megatives large.

Procedural texturing is powerful in its ability to squeeze down the size. Programming is the ultimate way to compress.

2pm. Updating the file to the latest version seems to have gone smoothly. Let me study it.

It is really interesting that it starts with linear gradient 3 and then blurs it. I'd never have thought of doing something like that.

2:40pm. Back in high school, when I looked at the solution to some of the olympiad level progrmaming probems, I could not understand them. In the end I never managed to surmount that challenge. Looking at the designer file gives me those kinds of unpleasant feelings.

I thought I got a handle on procedural materials thanks to the Houdini experience, but this is on a whole another level.

2:50pm. But it is not like I gained nothing for the effort. A lot of the nodes in Painter are based on the Designer ones.

Gradient dynamic for example. If I was trying to figure out what it did solely in painter it would be hard, but it is not problem to do once I saw it use in Designer.

3:10pm. I am going over the existing wood textures checking out whether there is something I could use.

https://forum.substance3d.com/index.php?topic=22952.0
> At one point, the author says "I also reinjected the height data into the albedo to give the inside of the pores a reddish color." How did they do this and can the same thing be done with normal maps?

> You can project a layer's channel onto a different layer using so-called Anchor Points. I would use Height as the output instead of Normal because it's only B/W, which is easier to work with when adjusting the anchor input.

I guess now I have cause to study anchor points.

3:15pm. Ok...let me get on with it.

The fact that I can't do shader magic right now does not matter. It is not something that I need to know. Past the Singularity I'll push all the scores past 6, but for now, I might as well be happy with 3 in the essentials.

I have 5 in what is really important, so it should be fine if I am 3 at the rest. It is not quite being a jack of all, master of none, since I do have masteries in functional programming and language dev.

3:20pm. What I've done so far is the ideal resolution to the problem - neither do it by hand in Clip Studio Paint or in Substance Designer. Rather rip the height from existing wood textures. I'll stick to this kind of workflow in the future and make rapid progress.

Now if I can only overcome this depression.

Let me watch some anchor point vids.

https://substance3d.adobe.com/tutorials/courses/Substance-3D-Painter-Anchor-Points-Generators-and-Brush-Maker/youtube-LCud1p6lnCI
Substance 3d Painter: Anchor Points, Generators And Brush Maker

Let me start with this. Though this is more of a showcase than anything else.

https://youtu.be/LCud1p6lnCI?t=385

Ah, I see. Can I do something similar to this for a color map?

3:45pm. Not bad at all.

It works. Though now that I am looking at it more carefully I do not like the pattern. Isn't there something straighforward that I could use. Let me check out the community site.

https://substance3d.adobe.com/assets

A lot of stuff here.

https://substance3d.adobe.com/assets/allassets/f29a05cfa921399e066521161731c2dfeeeeef60?q=wood&u=wood

This one is good, if not quite there.

4:05pm. I do not know whether I should have picked something other than basematerial when importing that tutorial texture, but it has no parameters exposed.

4:10pm. At any rate, there are a lot of wood materials on the community site. But for that I really would require a Substance Painter subscription. I can't afford 20$ a month right now, not just for this.

4:30pm. Had to take a break.

4:40pm. Damn it, in the starting pack not a single one of these patterns is good!

Let me back to designer. Though I do not get most of it, I did pick up a few ideas from studying that file. Let me start with a wave pattern and try distorting it.

I can't actually do this in Clip Studio because i need the texture to be tileable. I can't do it in Houdini because those objects going across the texture go all the way around. The tiler most likely won't know how to deal with it. It can only be a procedural texture.

4:50pm. Interesting. Gradient radial, unlike the shapes gives perfect circles when passed through gradient dynamic. This is what I want. Now let me see if I can do some size variation in the circles.

5:10pm. Sigh, I am so stupid for not understanding how to set the circle widhs properly. I tried warping the gradient, but instead I could have just used the levels node on the irignal radial gradient.

It is a bit thick on the top though.

5:15pm. Just now I had a happy accident. I am using gradient radial and gradient linear 2, multiplied them, and when I messed with the opacity I got the perfect knotted pattern.

Also I just realized that for gradient radial, you can dynamically move the circle in the 2d view.

I see what is going on. When the foreground is opaque, the background gets passed through as is.

5:25pm. It seems Warp is one of those nodes that is a lot less useful at first glance than it seems.

5:30pm. I guess since things are like this, I might as well obsess about it. Let me watch some warp tutorials.

But first let me try some things out.

5:50pm. I am enraptured by experimentation. I need to get back on track.

https://youtu.be/frLyo__8hIk
KNOW YOUR NODES Directional Warp

Let me watch this.

https://youtu.be/DDQHKT7uAho
Multi-Directional Warp

Let me watch this.

https://youtu.be/DDQHKT7uAho?t=393

I was wondering how to use the pixel processor. So this is how it works!

https://youtu.be/DDQHKT7uAho?t=435

Ok, now I know how to use the pixel processor. But it is rather weak its functionality. I tried using power, and it only has 2^a. It wasn't even a^b. What the hell? I really wanted to use power to move pixels around, but it did nto work.

6:25pm. Oh, there is a substance function that gives me prop Pow. Phew.

6:50pm. https://www.youtube.com/watch?v=PBkFaeKzhGE
Easy cliffs in Substance Designer! (non-uniform directional warp)

Let me watch this as well.

https://youtu.be/PBkFaeKzhGE?t=164

Hmmm, I could use this to get the kind of directional warping that would be desirable.

https://youtu.be/PBkFaeKzhGE?t=195

Oh, it has trail lengths? That is exactly something I'd need to smudge the knot a bit.

8:05pm. Let me close here. I am still engrossed in it, but the fun has to stop at some point.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-y8q6-tgQjZc
Getting Started With Substance 3d Designer

I've gotten some desire to study this further. I'll leave this 4h course for tomorrow. Right now I only have a single knot pattern, but I should be able to generalize it to a whole texture.

https://substance3d.adobe.com/tutorials/courses/Creating-Old-Wood-Planks-in-Substance-3D-Designer/youtube-vLz8ZyduQi0
Creating Old Wood Planks In Substance 3d Designer

Actually let me play a bit more. I want to see if I can get the same pattern, just adding or add subbing.

9:10pm. https://substance3d.adobe.com/documentation/sddoc/blur-172825121.html

The docs answer what the difference is between HQ blur and the regular one.

Ok.

It turns out there is a large number of ways of getting the knot patterns. Pretty much overthing will work: add, multiply, screen, overlay, addsub. Height blend is also a good option.

9:20pm. Rather than being hard, the base pattern should be easy.

I'll study the 4:30h course on making muddy ground tomorrow. There is no way around it. Whatever is driving me won't be satisfied with just using existing textures. It wants me to do my own.

There is a first time for everything. I might as well go for it.

I'll master these aspects of Designer and move to bigger and better things."

---
## [kernel-patches/bpf-rc](https://github.com/kernel-patches/bpf-rc)@[9a7ef9f86b...](https://github.com/kernel-patches/bpf-rc/commit/9a7ef9f86b96be22d009422e4c0ba52e1292492f)
#### Tuesday 2022-04-05 20:24:50 by Alexei Starovoitov

Merge branch 'Add libbpf support for USDTs'

Andrii Nakryiko says:

====================

Add libbpf support for USDT (User Statically-Defined Tracing) probes.
USDTs is important part of tracing, and BPF, ecosystem, widely used in
mission-critical production applications for observability, performance
analysis, and debugging.

And while USDTs themselves are pretty complicated abstraction built on top of
uprobes, for end-users USDT is as natural a primitive as uprobes themselves.
And thus it's important for libbpf to provide best possible user experience
when it comes to build tracing applications relying on USDTs.

USDTs historically presented a lot of challenges for libbpf's no
compilation-on-the-fly general approach to BPF tracing. BCC utilizes power of
on-the-fly source code generation and compilation using its embedded Clang
toolchain, which was impractical for more lightweight and thus more rigid
libbpf-based approach. But still, with enough diligence and BPF cookies it's
possible to implement USDT support that feels as natural as tracing any
uprobe.

This patch set is the culmination of such effort to add libbpf USDT support
following the spirit and philosophy of BPF CO-RE (even though it's not
inherently relying on BPF CO-RE much, see patch #1 for some notes regarding
this). Each respective patch has enough details and explanations, so I won't
go into details here.

In the end, I think the overall usability of libbpf's USDT support *exceeds*
the status quo set by BCC due to the elimination of awkward runtime USDT
supporting code generation. It also exceeds BCC's capabilities due to the use
of BPF cookie. This eliminates the need to determine a USDT call site (and
thus specifics about how exactly to fetch arguments) based on its *absolute IP
address*, which is impossible with shared libraries if no PID is specified (as
we then just *can't* know absolute IP at which shared library is loaded,
because it might be different for each process). With BPF cookie this is not
a problem as we record "call site ID" directly in a BPF cookie value. This
makes it possible to do a system-wide tracing of a USDT defined in a shared
library. Think about tracing some USDT in libc across any process in the
system, both running at the time of attachment and all the new processes
started *afterwards*. This is a very powerful capability that allows more
efficient observability and tracing tooling.

Once this functionality lands, the plan is to extend libbpf-bootstrap ([0])
with an USDT example. It will also become possible to start converting BCC
tools that rely on USDTs to their libbpf-based counterparts ([1]).

It's worth noting that preliminary version of this code was currently used and
tested in production code running fleet-wide observability toolkit.

Libbpf functionality is broken down into 5 mostly logically independent parts,
for ease of reviewing:
  - patch #1 adds BPF-side implementation;
  - patch #2 adds user-space APIs and wires bpf_link for USDTs;
  - patch #3 adds the most mundate pieces: handling ELF, parsing USDT notes,
    dealing with memory segments, relative vs absolute addresses, etc;
  - patch #4 adds internal ID allocation and setting up/tearing down of
    BPF-side state (spec and IP-to-ID mapping);
  - patch #5 implements x86/x86-64-specific logic of parsing USDT argument
    specifications;
  - patch #6 adds testing of various basic aspects of handling of USDT;
  - patch #7 extends the set of tests with more combinations of semaphore,
    executable vs shared library, and PID filter options.

  [0] https://github.com/libbpf/libbpf-bootstrap
  [1] https://github.com/iovisor/bcc/tree/master/libbpf-tools

v2->v3:
  - fix typos, leave link to systemtap doc, acks, etc (Dave);
  - include sys/sdt.h to avoid extra system-wide package dependencies;
v1->v2:
  - huge high-level comment describing how all the moving parts fit together
    (Alan, Alexei);
  - switched from `__hidden __weak` to `static inline __noinline` for now, as
    there is a bug in BPF linker breaking final BPF object file due to invalid
    .BTF.ext data; I want to fix it separately at which point I'll switch back
    to __hidden __weak again. The fix isn't trivial, so I don't want to block
    on that. Same for __weak variable lookup bug that Henqi reported.
  - various fixes and improvements, addressing other feedback (Alan, Hengqi);

Cc: Alan Maguire <alan.maguire@oracle.com>
Cc: Dave Marchevsky <davemarchevsky@fb.com>
Cc: Hengqi Chen <hengqi.chen@gmail.com>
====================

Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[5522769378...](https://github.com/cockroachdb/cockroach/commit/5522769378eea814c85e4d22b839c6ff81f6f744)
#### Tuesday 2022-04-05 21:09:56 by craig[bot]

Merge #76776 #76793 #76835 #76901

76776: scpb,scdecomp,scbuild: remodel elements, use decomposition r=postamar a=postamar

This change adresses some shortcomings of the declarative schema
changer that would have compromised its ability to evolve gracefully in
its current form. Basically these are:
  1. the builder generating targets based off a hybrid descriptor-and-
     element scheme, and
  2. an awkward handling of back-references which precludes doing much
     more than DROP statements correctly.

This change therefore consists of, respectively:
  1. rewriting the builder to hide descriptors from the `scbuildstmt`
     package, instead exposing sets of elements, and
  2. reworking the element model definition by getting rid of
     back-reference elements entirely.

In support of (1) this commit introduces a new `scdecomp` package which,
given a descriptor, will walk a visitor function over all its
constituent elements. This itself is made quite simple by (2) which
largely removes the need to look up referenced descriptors outside of
some mild edge-cases.

This `scdecomp` package is used by the backing structs of the
`scbuildstmt` dependency interfaces to collect a "state-of-the-world"
snapshot of elements upon which the schema change target elements are
layered. This approach lends itself well to caching as the descriptors
remain immutable in the builder.

The rewrite of most of `elements.proto` in support of (2) implies a slew
of cascading changes:
 - the attributes in `screl` need to be adjusted,
 - the lifecyles of the elements in `opgen` have to be adjusted,
 - the dependency rules and no-op rules need to be adjusted,
 - in turn, new operations need to be defined in `scop`, and,
 - in turn, these operations need to be implemented in `scmutationexec`.

Elements are now responsible for updating any back-references that
correspond to their forward references, which effectively pushed that
complexity into these reference update ops in `scmutationexec`. These
have to operate on a best-effort basis, because there are no longer
back-reference elements with dependency rules to enforce convenient
assumptions about the context of their adding or removal. This is
arguably not a bad thing per-se: this new paradigm is "fail hard, fail
fast" which surfaces bugs a lot more quickly than a badly-written
dependency rule would.

The rules themselves fall into cleaner patterns. This commit provides some
tools to express the most common of these. This commit also unifies the
`deprules` and `scopt` packages into a commit `rules` package with full
data-driven test coverage.

Other changes in this commit are peripheral in nature:
  - Working on this change surfaced some deficiencies in the
    cross-referenced descriptor validation logic: we checked that the
    referenced descriptor exists but not that it's not dropped. This
    commit fixes this.
  - The expression validation logic in `schemaexpr` quite reasonably
    used to assume that columns can be found in descriptors;
    unfortunately the builder needs to be able to use this for columns
    which only exist as elements. This commit refactors the entry points
    into this validation logic as a result.
  - Quality-of-life improvements like adding a testing knob used to
    panic TestRollback with an error with a full stack trace when the
    rollback fails.
  - Because back-references don't exist as elements anymore, they also
    don't exist as targets, so we now have schema changer jobs linked to
    descriptors for which there are zero targets. This commit addresses this
    by simply allowing it. This is necessary to lock descriptors to
    prevent any concurrent schema changes which would affect them.

Release note: None


76793: storage: introduce guaranteed durability functionality r=jbowens a=sumeerbhola

This is the CockroachDB plumbing for Pebble's
IterOptions.OnlyReadGuaranteedDurable. It is for use in
the raftLogTruncator https://github.com/cockroachdb/cockroach/pull/76215.

Since most of the exported interfaces in the storage
package use a Reader, we support this via a
DurabilityRequirement parameter on Engine.NewReadOnly,
and not via an iterator option.

There is also a RegisterFlushCompletedCallback method
on Engine which will be used to poll certain durable
state in the raftLogTruncator.

Other than the trivial plumbing, this required some
refactoring of the Reader.MVCCGet* code for Pebble
and pebbleReadOnly. Even though it is deprecated and
primarily/only used in tests, we don't want to have
the durability semantics diverge.

Release note: None

76835: ttljob: add controls to pause TTL jobs r=rafiss a=otan

See individual commits for details.

76901: colexecspan: de-templatize span assembler and use span.Splitter r=RaduBerinde a=RaduBerinde

#### colexecspan: de-templatize span assembler

The span assembler code is generated only to inline a piece of code
that has two variants. This change converts it to non-generated code
and simply forks the code paths above the batch loop.

Release note: None

#### colexecspan: use span.Splitter

The span assembler duplicates some of the logic in `span.Splitter`.
Now that the latter is a separate type, we can use it instead.

Release note: None


Co-authored-by: Marius Posta <marius@cockroachlabs.com>
Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>

---
## [C0rva1r/Skyrat-tg](https://github.com/C0rva1r/Skyrat-tg)@[8607ba8b7d...](https://github.com/C0rva1r/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Tuesday 2022-04-05 21:15:30 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [post-rex/wassup](https://github.com/post-rex/wassup)@[efd472a33c...](https://github.com/post-rex/wassup/commit/efd472a33ccccff96c036b84d0ed0183bd4d84eb)
#### Tuesday 2022-04-05 21:49:14 by PostRex

I fucking hate git

I wanted to undo a commit because it's wrong and it was all local still
So I tried to do it the git way instead of fixing it the "wrong" way
yeah anyways I just lost all of my progress today.
Fuck you git

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[262364189c...](https://github.com/mbs-octoml/mbs-tvm/commit/262364189c15173c8cd20b10683c4daea6e8155e)
#### Tuesday 2022-04-05 23:07:15 by Mark Shields

** Collage v2 sketch ***

- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
  *** CAUTION: Almost certainly broken ***
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---

