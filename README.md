## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-21](docs/good-messages/2022/2022-03-21.md)


1,695,177 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,695,177 were push events containing 2,662,513 commit messages that amount to 203,166,320 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[ec62cb0aac...](https://github.com/postgresql-cfbot/postgresql/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Monday 2022-03-21 00:04:59 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[770ef81a1f...](https://github.com/StarStation13/StarStation13/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Monday 2022-03-21 00:24:19 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [DeveloperLoser/fulpstation](https://github.com/DeveloperLoser/fulpstation)@[c449fbb56c...](https://github.com/DeveloperLoser/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Monday 2022-03-21 01:24:06 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [daheige/log](https://github.com/daheige/log)@[e49f063235...](https://github.com/daheige/log/commit/e49f063235752784b0476e74559d142cd7786ca8)
#### Monday 2022-03-21 02:09:44 by Thomas de Zeeuw

Add key-values to the macros

Attempt number two/three? Too many in any case.

Previously I proposed a design that followed a `struct` like syntax:

```rust
info!("my message: {}", arg, {
    key1: "value1",
    key2: 123,
});
```

However it turns out that this does not work well with named arguments
as reported in issues #369 and #372. The implementation was eventually
reverted in pr #374.

This new design takes inspiration from the `tracing` crate which already
supports key-value pairs in logging events. The basic idea is to put the
key-value pairs before the message and arguments. Applying the same
structure like syntax as above we would get something like the
following.

```rust
info!({
    key1: "value1",
    key2: 123,
}, "my message: {}", arg);
```

But personally I'm not a big fan of this formatting, let's try putting
everything on a single line instead.

```rust
info!({ key1: "value1", key2: 123 }, "my message: {}", arg);
```

A little better, but at this point the structure like syntax is really
more annoying then helpful. So, instead I've done away it, opting
instead use the following syntax.

```rust
info!(key1 = "value1", key2 = 123, "my message: {}", arg);
```

Two major differences:
 * Removed the brackets.
 * Colons (`:`) are replaced with equal/assignment signs (`=`).

This gives us syntax similar to variable assignment.

But then we run in some limitations of the macro syntax, specifically
that `expr` fragments aren't allowed after `expr` fragments. To fix this
I went with the easiest option of changing the last comma (`,`) after
the key-value pairs to a semicolon (`;`). Making the final syntax look
like the following.

```rust
info!(key1 = "value1", key2 = 123; "my message: {}", arg);
info!(target: "my_target", key1 = "value1", key2 = 123; "my message: {}", arg);
log!(target: "my_target", log::Level::Info, key1 = "value1", key2 = 123; "my message: {}", arg);
```

Which, in my opinion and all things considered, it's too bad looking.

---
## [daisy-watt/rails_marketplace](https://github.com/daisy-watt/rails_marketplace)@[b9ff9e2bd2...](https://github.com/daisy-watt/rails_marketplace/commit/b9ff9e2bd215293010296415a73228839bb6ff9c)
#### Monday 2022-03-21 02:20:43 by daisy watt

Merge pull request #10 from daisy-watt/stripe-feature-pls

fuck you map

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[2576a663c9...](https://github.com/morgoth1145/advent-of-code/commit/2576a663c917116ebd9a0dcef56dc9e2e961e208)
#### Monday 2022-03-21 02:47:17 by Patrick Hogg

2019 Rewrite Day 10 Part 2

It turns out that I had a bug in part 2! I was (stupidly) thinking that a dx,dy of 0,1 was pointing up, forgetting that low y is up. That means that 0,-1 is up and I had the intended sorting all mixed up for my angle order.

Additionally, I forgot that dx would be negative for left side angles so left_side_angles was sorted in the opposite order that I intended, correcting for the above mistake.

Thankfully the right asteroid was in the left quadrant so these bugs canceled out. However, that's really icky behavior so I reworked the angle sorting to be based on math.atan2 which is smarter than me. The only issue is that it doesn't put the up angle first in the list so the angle order list needs to be shifted.

One other small improvement here is sorting the asteroids based on their manhattan distance from the station in determine_asteroid_visibility. This makes the destruction order much easier to compute since we just pop the 0th item from the list until it's empty.

---
## [TheDigitalFellow18/DO-YOU-UNDERSTAND-DIGITAL-ROI](https://github.com/TheDigitalFellow18/DO-YOU-UNDERSTAND-DIGITAL-ROI)@[e18dccc80e...](https://github.com/TheDigitalFellow18/DO-YOU-UNDERSTAND-DIGITAL-ROI/commit/e18dccc80e949b97c278f80b49f765e0c890cdce)
#### Monday 2022-03-21 03:26:55 by TheDigitalFellow18

Update README.md

Wonder why you haven’t had much luck with digital marketing for your business?

You believe in getting 𝐑𝐎𝐈 in the short term. But wise digital marketing is for the long run.

You have sales mentality, and you are only interested  in quick returns. You see marketing as an expense and not an investment. Don’t understand brand building or long term value oriented thinking.

Our observations are based on the substantial clientele we have handled from various industries and the digital pain areas we have solved for each business. (Take a look at the two figures to understand the breadth and depth of our work.)

We have thus been able to filter the kind of leaders and CXOs who are serious about their organisation’s digital transformation and are committed to investing in the right digital marketing resources. The others are non-digital CXOs who do not even have the right questions to ask us!

We try our best to avoid onboarding businesses who do not respect the basic requirements for digital transformation. We saw a sales person is heading digital marketing and there is no dedicated marketing head.

Even if we work with you, you wouldn’t have the right human resources with their digital KRAs to understand the value we bring to your digital transformation. A dedicated marketing team (consisting of a marketing qualified team) suggests the marketing mindset of an organisation.

We’ll work with you if you qualify as per the following criteria:- 

   01. Growth or digital  mindset or acceptance of digital transformation 

   02. Shedding of digital denial attitude

   03. Willingness to truly understand business transformation 

   04. Patience to invest in brand discovery

   05.Willingness to invest in the right measures of digital marketing

If you wish to invest in better digital marketing and have the resources and patience for it, talk to us.


𝐆𝐞𝐭 𝐢𝐧 𝐭𝐨𝐮𝐜𝐡:  +𝟗𝟏 𝟗𝟗𝟔𝟕 𝟔𝟑𝟎𝟑 𝟐𝟗

---
## [Socks-code/AttendancePlus](https://github.com/Socks-code/AttendancePlus)@[4190bc25f8...](https://github.com/Socks-code/AttendancePlus/commit/4190bc25f8dcf6f7091e0ae55f87532069c40889)
#### Monday 2022-03-21 04:05:09 by Socks-code

date/time to homepage

im quick as fuck boi

added more shit to homepage so she doesnt bitch

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[b187902786...](https://github.com/RedDevilus/pcsx2/commit/b187902786e572a2def342ad663bbb042ac1fb88)
#### Monday 2022-03-21 04:16:11 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Resident Evil 4
Thrillville

Also commented out where merge sprite fixes blurriness but removes bloom:
God Hand
Naruto Uzumaki Chronicles
Thrillville

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[05b52ab6df...](https://github.com/RedDevilus/pcsx2/commit/05b52ab6df076507b6e34793b8575f9b47ce97b8)
#### Monday 2022-03-21 04:31:33 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Resident Evil 4
Thrillville / Off the Rails

Also commented out where merge sprite fixes blurriness but removes bloom:
God Hand
Naruto Uzumaki Chronicles
Thrillville

---
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[81df0d577e...](https://github.com/Gullwing-door/restoration-mod/commit/81df0d577ea6810aef7aba782067ba46f861135d)
#### Monday 2022-03-21 04:37:50 by Reeeno

_sc zeals (crashes)

i dont fucking care i hate working on them someone else fix this shit

---
## [sabarop/kernel_xiaomi_sdm660_clover](https://github.com/sabarop/kernel_xiaomi_sdm660_clover)@[0d2c52f8b5...](https://github.com/sabarop/kernel_xiaomi_sdm660_clover/commit/0d2c52f8b5723ae9fd2edb816bc26a0c77e46075)
#### Monday 2022-03-21 05:40:00 by Maciej Żenczykowski

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
## [IN2-Moist/2Take1-Moist-Script](https://github.com/IN2-Moist/2Take1-Moist-Script)@[1b182bc8f0...](https://github.com/IN2-Moist/2Take1-Moist-Script/commit/1b182bc8f03f5166c4252a1567103d481eef551c)
#### Monday 2022-03-21 06:07:06 by IN2_Moist

2.0.6.3

Updated - Most of my custom calculation functions

Updated - PlayerBar for 32 players and moved Date & Time + My Speed into the left over space in the playerbar

Added - Spawn Parts of the map to local online players troll

Added - Experimental Functions Extend The World still a work in progress spawns an extra part of the map at the end of lsia over the ocean (more visual than something you can go on at the moment)

Added - Previously Seen Players Info : Previously Kicked: True|False

Added - Option Kick Previously Kicked Players on join

Updated - Audio sounds in Orbital Session and Sound Annoyances so is not overloud for network players

Added - Re-Added Noftify God Audio and Visual Notify Sound only can be heard by yourself and anyone close enough to hold your hand

Added - ModderFlag Shit to Modder Shit

Added - Flags to AutoKick to ModderFlag Shit

Added - Flags to AutoRemove to ModdderFlag Shit

Advise to toggle off notify detected modders in protections to avoid any notify spam the script will now tell you once what it detected and removed

Added - Bypass Kick & Remove Flag from Friends to Flags to AutoKick

Updated - Online Player Features Spawn Options:

Spawn attackers in vehicles now spawns aircraft in the air above and offset to player bit like lester savage hunter
Spawned attackers now retask on death option becomes visible once attacker spawned and deletes the spawns when toggled off

Fixed - Error in weapons array

Updated - God Mode Detection

Updated - Interior Detection and Calculations

Updated - Modder Module now includes protections against Clear Ped Tasks, All Give & Remove Weapons and marks player as a cunt
Modder Module now runs from the config folder

Updated - Interior Locations more locations added to improve god mode detection

---
## [schqiushui/android_kernel_oneplus_sm8250](https://github.com/schqiushui/android_kernel_oneplus_sm8250)@[16ab3e87ae...](https://github.com/schqiushui/android_kernel_oneplus_sm8250/commit/16ab3e87ae59d72c71bbf5e3f564dd18c541807d)
#### Monday 2022-03-21 07:02:28 by alk3pInjection

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
## [QuickMythril/qortal-minting-logger](https://github.com/QuickMythril/qortal-minting-logger)@[7d2ae4b4fd...](https://github.com/QuickMythril/qortal-minting-logger/commit/7d2ae4b4fd9f8bc3f8a8e4906a974207457740f5)
#### Monday 2022-03-21 08:42:04 by sakumatto

Added log file showing boot from genesis

# Building up from Genesis
# Whenever the 3rd and 4th column disappears it means the minter stuck for one reason or another
# I was forced to "reboot" using my other machine's db at one point as I was unable to get the minter to react in any way for several days.
# On May 27th the log entry changes, this is due to the minter catching up to the height where I personally joined Qortal and got sponsored (thanks Qortal Rose :), so it starts showing my status (first M for minting, then L1 / L2 for reaching next levels)

# Findings:
# 1) It took from May 17th 19:49 to June 17th 14:25 (local time) to reach the height (this was my second try, pls read below)
# 2) My log is for every five minutes and it can clearly be seen that as the height developed less and less height could be acquired in that 5 minutes
#    I presume this is due to more and more users in Qortal ie more and more to calculate when trying to catch up. Does this also imply that the further the height grows, the more impossible it becomes for someone to start from Genesis?
# ================ Log entries to visualize above point of decreasing trend
##29.05.2021 24H minted: 10796
##30.05.2021 24H minted: 9812
##31.05.2021 24H minted: 6731
##01.06.2021 24H minted: 5827
##02.06.2021 24H minted: 5457
##03.06.2021 24H minted: 3639
##04.06.2021 24H minted: 3011
##05.06.2021 24H minted: 3087
##14.06.2021 24H minted: 87303 (days long period where I could not get system running and was forced to cheat)
##15.06.2021 24H minted: 1032
##16.06.2021 24H minted: 2849
##17.06.2021 24H minted: 2089
##18.06.2021 24H minted: 1935
##19.06.2021 24H minted: 1074
# ================
# Every midnight my logger logs the version number and it shows clearly that the auto update works.

# Other:
# On May 14th I got Caldescent's help when running into stuck height "there's a bug in 1.5.1 preventing syncing from genesis. It gets stuck on a few specific blocks."
# so after getting the patched jar I was able to pass 46101, the magic number.
# On May 17th Caldescent was able to point out that I'd formatted my disk in the wrong way so I had to start from scratch after proper format "Just wondering if it's FAT32 and you're hitting the 4GB limit for a single file...
I formatted my drive to ext4 to avoid that"
# On May 18th Moose_onthe_Loose (thanks man!) adviced me to keep fan on all the time and temp dropped by 10 ° C and have stayed low.

---
## [xTrayambak/pysyn](https://github.com/xTrayambak/pysyn)@[bdf2871c46...](https://github.com/xTrayambak/pysyn/commit/bdf2871c467944e1275a7baedcde49a3906359fc)
#### Monday 2022-03-21 09:06:29 by xTrayambak

go fuck yourself, whoever created pysyn on PyPi before I did.

---
## [TheChosenEvilOne/Merchant-Station-13](https://github.com/TheChosenEvilOne/Merchant-Station-13)@[663688130e...](https://github.com/TheChosenEvilOne/Merchant-Station-13/commit/663688130e83b094351f8cdf1b1d20a6b0c80c4b)
#### Monday 2022-03-21 09:15:52 by karmaisblackandbluepilled

I hate /tg/code so much it's actually unreal (#57)

* Hulk Recoil Removal go fuck yourself 41 damage for one wall

* medical doctors have access to genetics, again, why was this removed FUCK you

* buffs bpowder and methsplosions back up, fuck you edge

* Unnerfs chemicals for speed why why why why why

* adds silver back to synthesizers but removes the solidification reaction, for obvious reasons

* unfucks the dna sequencers because genetics is a shit minigame and making it harder to solve is for [SLUR REMOVED]

* did what the guy above told me to(?)

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Monday 2022-03-21 09:54:41 by Dennis Snell

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
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[399e9bf0b1...](https://github.com/RedDevilus/pcsx2/commit/399e9bf0b1551c3258817977522436c2002b3750)
#### Monday 2022-03-21 10:47:31 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [safwan6363/my-files](https://github.com/safwan6363/my-files)@[6d8c4dfceb...](https://github.com/safwan6363/my-files/commit/6d8c4dfcebaccd40168993ad102f7956c4a94ba2)
#### Monday 2022-03-21 11:40:05 by safwan6363

i hate myself actually no wait no yes fuck everything

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[52f621f1c4...](https://github.com/mrakgr/The-Spiral-Language/commit/52f621f1c4997aee1b14ae4243b6cbc2f4e0cfc8)
#### Monday 2022-03-21 12:24:38 by Marko Grdinić

"10:40am. I am up. Let me chill for a while and then I will start by watching the procedural texturing tutorial. Did I get a reply to any of the Clarisse questions? No. This is the first time I've experienced something like this. Are they really holding me back from asking pertinent questions on their forum? At this point I can assume that what I want from those questions will be resolved negatively.

11:25am. Let me start. I've listened to the XPirates Geoscape OST a few times, and my conclussion is that it is very difficult to compete with the original Geoscape theme from UFO. It is easily one of the best musical compositions of all time.

A lot what is going on in this era is not appreciated properly in the present. After the Singularity hits, it is very likely that people will look back at this period as a mythical era.

Games themselves are yet to take their proper role.

https://youtu.be/9ngbOV0YKbk
Advanced Procedural Texturing

Let me start by watching this. The first time around I was too unfamiliar with Clarisse to understand it, but now I'll be able to make progress.

https://youtu.be/9ngbOV0YKbk?t=76

Ah, this is a way to get the UVs.

Lately I really feel like I am going senile. So many thoughts are going through my mind...

Ah, yes. A question I wanted to ask was: How did you get Houdini to show a whole city without it shitting itself?

There was a clip in both the keynote and the USD exports tab. I'll leave that for later.

https://youtu.be/9ngbOV0YKbk?t=79

Also, watching this makes me realize how he got those quadrants in blender. The black square is the negative position, and the rest go sharply positive quickly.

https://youtu.be/9ngbOV0YKbk?t=136

What is the difference between randomizing a texture and creating a random one?

https://youtu.be/9ngbOV0YKbk?t=132

Why did he get squares like this. When I tried it yesterday I just got a white noise texture.

https://youtu.be/9ngbOV0YKbk?t=203

Ah, the color picked can show values beyond 1. It did not occur to me that this could be a use of the pixel inspection.

https://youtu.be/9ngbOV0YKbk?t=239

Let me pause here. I want to understand what randomize is doing. How did he get those squares?

https://youtu.be/9ngbOV0YKbk?t=55

I do not get it. Why did changing the projection cause it to tile?

12pm. Hmmm, I see. It seems randomize is a noise function that takes in color as input. That means the same color gets mapped to the same thing.

12:15pm. https://youtu.be/9ngbOV0YKbk?t=360

I can follow this video perfectly now.

https://youtu.be/9ngbOV0YKbk?t=766

Sigh, why don't the remap nodes start with grayscale by default. Why just one point white? Unlike in Houdini there are no presets either.

https://youtu.be/9ngbOV0YKbk?t=1064

It seems there is a specialize point cloud texture.

12:55pm. https://youtu.be/R3usfNNH8wg
Clarisse Workflows: Creating Procedural Dunes

Let me watch this. There is a desert scene as well in the intro peom.

https://youtu.be/R3usfNNH8wg?t=233

Hmmmm, hmmm, what if I started with a voronoi texture, inverted the colors and then squished it. But I am not sure of being able to manage the rotation.

https://youtu.be/R3usfNNH8wg?t=544

Ah, it is possible to use an expression like this.

1:15pm. I learned quite a bit. When it comes to making deserts I'll definitely make use of this knowledge. You can really get a lot of power through procedural texturing.

I really meant to use sculpting for a lot more things, but now that I am learning different techniques, I am leaning more and more towards the programming approach.

1:20pm. It might seem that I haven't moved much from months ago, but previously I definitely was not paying attention to texturing. Right now I feel like I've gotten my modeling concerns out of the way which allwos me on to focus a lot more on the 'painterly' aspects of 3d art. After I internalize this, I will have completely conquered 3d illustration.

Let me have breakfast here. I am overdue."

---
## [smartpie/blogr-landing-page](https://github.com/smartpie/blogr-landing-page)@[f7fa10914a...](https://github.com/smartpie/blogr-landing-page/commit/f7fa10914a589042ff1243de905ff779ff2a3819)
#### Monday 2022-03-21 12:38:24 by smartpie

Some shitty mixins from the shitty "Medium" website, that doesn't fucking allow you you to copy the piece of code. And also, FUCK YOU, U SHOULD NOT READ THIS, U MORON

---
## [ecatmur/gcc](https://github.com/ecatmur/gcc)@[aeac414923...](https://github.com/ecatmur/gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Monday 2022-03-21 13:04:41 by Thomas Schwinge

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
## [tImIbreakdown/android_kernel_leeco_msm8976](https://github.com/tImIbreakdown/android_kernel_leeco_msm8976)@[cec218965c...](https://github.com/tImIbreakdown/android_kernel_leeco_msm8976/commit/cec218965c6f1d3f12dcac46abcfdf08e5a0ddf4)
#### Monday 2022-03-21 14:14:05 by Josh Triplett

clone: support passing tls argument via C rather than pt_regs magic

clone has some of the quirkiest syscall handling in the kernel, with a
pile of special cases, historical curiosities, and architecture-specific
calling conventions.  In particular, clone with CLONE_SETTLS accepts a
parameter "tls" that the C entry point completely ignores and some
assembly entry points overwrite; instead, the low-level arch-specific
code pulls the tls parameter out of the arch-specific register captured
as part of pt_regs on entry to the kernel.  That's a massive hack, and
it makes the arch-specific code only work when called via the specific
existing syscall entry points; because of this hack, any new clone-like
system call would have to accept an identical tls argument in exactly
the same arch-specific position, rather than providing a unified system
call entry point across architectures.

The first patch allows architectures to handle the tls argument via
normal C parameter passing, if they opt in by selecting
HAVE_COPY_THREAD_TLS.  The second patch makes 32-bit and 64-bit x86 opt
into this.

These two patches came out of the clone4 series, which isn't ready for
this merge window, but these first two cleanup patches were entirely
uncontroversial and have acks.  I'd like to go ahead and submit these
two so that other architectures can begin building on top of this and
opting into HAVE_COPY_THREAD_TLS.  However, I'm also happy to wait and
send these through the next merge window (along with v3 of clone4) if
anyone would prefer that.

This patch (of 2):

clone with CLONE_SETTLS accepts an argument to set the thread-local
storage area for the new thread.  sys_clone declares an int argument
tls_val in the appropriate point in the argument list (based on the
various CLONE_BACKWARDS variants), but doesn't actually use or pass along
that argument.  Instead, sys_clone calls do_fork, which calls
copy_process, which calls the arch-specific copy_thread, and copy_thread
pulls the corresponding syscall argument out of the pt_regs captured at
kernel entry (knowing what argument of clone that architecture passes tls
in).

Apart from being awful and inscrutable, that also only works because only
one code path into copy_thread can pass the CLONE_SETTLS flag, and that
code path comes from sys_clone with its architecture-specific
argument-passing order.  This prevents introducing a new version of the
clone system call without propagating the same architecture-specific
position of the tls argument.

However, there's no reason to pull the argument out of pt_regs when
sys_clone could just pass it down via C function call arguments.

Introduce a new CONFIG_HAVE_COPY_THREAD_TLS for architectures to opt into,
and a new copy_thread_tls that accepts the tls parameter as an additional
unsigned long (syscall-argument-sized) argument.  Change sys_clone's tls
argument to an unsigned long (which does not change the ABI), and pass
that down to copy_thread_tls.

Architectures that don't opt into copy_thread_tls will continue to ignore
the C argument to sys_clone in favor of the pt_regs captured at kernel
entry, and thus will be unable to introduce new versions of the clone
syscall.

Patch co-authored by Josh Triplett and Thiago Macieira.

Signed-off-by: Josh Triplett <josh@joshtriplett.org>
Acked-by: Andy Lutomirski <luto@kernel.org>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: "H. Peter Anvin" <hpa@zytor.com>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: Thiago Macieira <thiago.macieira@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Change-Id: Ic6aaa903881ab064c0b95ea636aaad1f8d4ac406

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[18883987b1...](https://github.com/pytorch/pytorch/commit/18883987b1697b79bb672bf5ec4d83140b8b47dd)
#### Monday 2022-03-21 15:45:47 by Edward Z. Yang

Update on "Disable meta device tests."


After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Differential Revision: [D35010278](https://our.internmc.facebook.com/intern/diff/D35010278)

[ghstack-poisoned]

---
## [bobbahbrown/tgstation](https://github.com/bobbahbrown/tgstation)@[759d24ab14...](https://github.com/bobbahbrown/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Monday 2022-03-21 16:22:17 by san7890

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
## [bobbahbrown/tgstation](https://github.com/bobbahbrown/tgstation)@[884c1eeb62...](https://github.com/bobbahbrown/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Monday 2022-03-21 16:22:17 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [Firehawke/mame](https://github.com/Firehawke/mame)@[6978cffeec...](https://github.com/Firehawke/mame/commit/6978cffeec7fb90878e9e6b7109e2839503c7958)
#### Monday 2022-03-21 16:25:46 by Firehawke

New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Science Explorers: Animal Adaptations (800K 3.5") [4am, Firehawke]
Black Belt [4am, Firehawke]
Zoo Master [4am, Firehawke]
Ape Escape [4am, Firehawke]
The Playroom [4am, Firehawke]
The Eating Machine [4am, Firehawke]
Word Spinner (Version 1.0) [4am, Firehawke]
Critical Mass [4am, Firehawke]
Gunslinger [4am, Firehawke]
The Black Cauldron [4am, Firehawke]
Mixed-Up Mother Goose [4am, Firehawke]
Science Explorers: Day, Night, and The Seasons (800K 3.5") [4am, Firehawke]
His Majesty's Ship "Impetuous" [4am, Firehawke]
Micro Mother Goose [4am, Firehawke]
Skybombers II [4am, Firehawke]
Battleship Commander [4am, Firehawke]
Three Mile Island [4am, Firehawke]
Conglomerates Collide [4am, Firehawke]
Cyborg (Version 2) [4am, Firehawke]
Fantasyland 2041 A.D. [4am, Firehawke]
Cross Country Rallye [4am, Firehawke]
Creature Venture [4am, Firehawke]
Science Explorers: Nutrition (800K 3.5") [4am, Firehawke]
Exploring Gas Laws (Version 1.0) (800K 3.5") [4am, Firehawke]
Wonderland Puzzles (Version 1.0) (800K 3.5") [4am, Firehawke]
Cryptoquest (Version 1.0) (800K 3.5") [4am, Firehawke]
Science Giants (Version 1.0) (800K 3.5") [4am, Firehawke]
Freedom! (Version 1.0) (800K 3.5") [4am, Firehawke]
Arizona Mix (Version 1.0) (800K 3.5") [4am, Firehawke]
Rescue in the Outback (Version 1.0) (800K 3.5") [4am, Firehawke]
Woolly's Garden (Version 1.0) (800K 3.5") [4am, Firehawke]
Exploring Chaos (Version 1.0) (800K 3.5") [4am, Firehawke]
Pet Shop (Version 1.0) (800K 3.5") [4am, Firehawke]
Science Explorers: Simple Machines (800K 3.5") [4am, Firehawke]
Dog Sled Ambassadors (Version 1.0) (800K 3.5") [4am, Firehawke]
Moving Museum (Version 1.0) (800K 3.5") [4am, Firehawke]
Take a Chance! (Version 1.0) (800K 3.5") [4am, Firehawke]
Treasures for Sale (Version 1.0) (800K 3.5") [4am, Firehawke]
Caravans to Timbuktu! (Version 1.0) (800K 3.5") [4am, Firehawke]
Amazing Arithmetricks (Version 1.0) (800K 3.5") [4am, Firehawke]
Picture a Story (Version 1.0) (800K 3.5") [4am, Firehawke]
Number Jumpers (Version 1.0) (800K 3.5") [4am, Firehawke]
Windy City (Version 1.0) (800K 3.5") [4am, Firehawke]
Word Builder (Version 1.0) (800K 3.5") [4am, Firehawke]
On Balance (800K 3.5") [4am, Firehawke]
Dueling Digits (Version 1.0) (800K 3.5") [4am, Firehawke]
History Makers (Version 1.0) (800K 3.5") [4am, Firehawke]
Dr. Livingstone, I Presume? (Version 1.0) (800K 3.5") [4am, Firehawke]
Eerieville Library (Version 1.0) (800K 3.5") [4am, Firehawke]
Fish School (Version 1.0) (800K 3.5") [4am, Firehawke]
Grammar Gobble (Version 1.0) (800K 3.5") [4am, Firehawke]
Grammar Madness (Version 1.0) (800K 3.5") [4am, Firehawke]
Nutrition Nabber (Version 1.0) (800K 3.5") [4am, Firehawke]
On Stage (Version 1.0) (800K 3.5") [4am, Firehawke]
Sum Stories (Version 1.0) (800K 3.5") [4am, Firehawke]
Big Book Maker: The Rain Forest (800K 3.5") [4am, Firehawke]
Rocket Factory (Version 1.0) (800K 3.5") [4am, Firehawke]
Probability Lab (Version 1.0) (800K 3.5") [4am, Firehawke]
Space Station Freedom (Version 1.0) (800K 3.5") [4am, Firehawke]
Weeds to Trees (Version 1.0) (800K 3.5") [4am, Firehawke]
Sun and Seasons (Version 1.0) (800K 3.5") [4am, Firehawke]
Paper Plane Pilot (Version 1.0) (800K 3.5") [4am, Firehawke]
Patterns (Version 1.2) (800K 3.5") [4am, Firehawke]
Lewis and Clark Stayed Home (Version 1.0) (800K 3.5") [4am, Firehawke]
Grammar Toy Shop (Version 1.0) (800K 3.5") [4am, Firehawke]
Fossil Hunter (Version 1.0) (800K 3.5") [4am, Firehawke]
Big Book Maker: The Three Princesses (800K 3.5") [4am, Firehawke]
Murphy's Minerals (Version 1.0) (800K 3.5") [4am, Firehawke]
Grammar Monsters (Version 1.0) (800K 3.5") [4am, Firehawke]
Mystery Matter (Version 1.1) (800K 3.5") [4am, Firehawke]
Grammar Gazette (Version 1.0) (800K 3.5") [4am, Firehawke]
Five Star Forecast (Version 1.0) (800K 3.5") [4am, Firehawke]
Lunar Greenhouse (Version 1.1) (800K 3.5") [4am, Firehawke]
Miner's Cave (Version 1.0) (800K 3.5") [4am, Firehawke]
Measure Works (Version 1.0) (800K 3.5") [4am, Firehawke]
Money Works (Version 1.1) (800K 3.5") [4am, Firehawke]
Fraction Concepts, Inc. (Version 1.2) (800K 3.5") [4am, Firehawke]
Story Starters: Science (800K 3.5") [4am, Firehawke]
Estimation Strategies (Version 1.0) (800K 3.5") [4am, Firehawke]
Estimation Activities (Version 1.0) (800K 3.5") [4am, Firehawke]
Estimation: Quick Solve I (Version 1.0) (800K 3.5") [4am, Firehawke]
CommuniKeys (Version 1.1) (800K 3.5") [4am, Firehawke]
Fraction Munchers (Version 1.0) (800K 3.5") [4am, Firehawke]
Conquering Decimals (+, -) (Version 1.1) (800K 3.5") [4am, Firehawke]
Conquering Fractions (+, -) (Version 1.1) (800K 3.5") [4am, Firehawke]
Conquering Decimals (x, /) (Version 1.1) (800K 3.5") [4am, Firehawke]
Conquering Fractions (x, /) (Version 1.1) (800K 3.5") [4am, Firehawke]
Instant Survey (Version 1.0) (800K 3.5") [4am, Firehawke]
Story Starters: Social Studies (800K 3.5") [4am, Firehawke]
Spellevator (Version 1.3) (800K 3.5") [4am, Firehawke]
Spelling Puzzles and Tests (800K 3.5") [4am, Firehawke]
Spelling Series Toolkit (800K 3.5") [4am, Firehawke]
Spelling Workout (Version 1.1) (800K 3.5") [4am, Firehawke]
Teacher Option Organizer (Version 1.1) (800K 3.5") [4am, Firehawke]
Perplexing Puzzles (800K 3.5") [4am, Firehawke]
Science Explorers: Plants (800K 3.5") [4am, Firehawke]
Science Explorers: Shadows (800K 3.5") [4am, Firehawke]
Science Explorers: Skeletons (800K 3.5") [4am, Firehawke]
Science Explorers: Weather (800K 3.5") [4am, Firehawke]
The Final Conflict [4am, Firehawke]
Intrigue! [4am, Firehawke]
Deathmaze 5000 [4am, Firehawke]
Space Pirates 3000 [4am, Firehawke]
Windmere Estate [4am, Firehawke]
Super Galaxy Wars [4am, Firehawke]

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[55643945a1...](https://github.com/influxdata/influxdb_iox/commit/55643945a1a654d0db0bcc5eb0a42d7c3185efa9)
#### Monday 2022-03-21 16:58:03 by Marco Neumann

refactor: `querier` w/o `db` (#4063)

* feat: `TombstoneRepo::list_by_table`

* feat: `ParquetFileRepo::list_by_table_not_to_delete`

* refactor: `querier` w/o `db`

Get the `querier` to work w/o relying on `db`. A few notes:

- Testing is kinda shallow, we really need to get `query_tests` working
  w/ `querier` (see #3934).
- We still run a sync loop for namespaces, tables and schemas. This will
  be a replaced by "update namespace incl. tables and schemas on demand".
  Note however that we cannot fetch single tables and schemas on demand
  at the moment, because DataFusion doesn't implement async schema
  inspection (only `scan` / "give me all the chunks" is async). I think
  that's OK for now and we can address this later.
- There is NO cache for parquet files and tombstones at the moment. For
  correctness, they need to be fetched in a single transaction (or we
  need a kinda tricky sequence number / logical clock tracking) and I am
  not sure yet how this makes sense when we have the ingester data wired
  up and predicates pushed down to the catalog (see next point). So
  let's measure first and then decide on a caching strategy for this.
- Predicates are currently NOT pushed down to the catalog. I'll need to
  figure out how to extract time range from generic DataFusion
  expressions to make that work (it's easier for InfluxRPC queries, but
  they are not tested at the moment, see first point).

Sorry that this commit is kinda huge. I initially planned to only
migrate the chunks away from `db` and leave the tables and schemas for a
follow-up PR, but the DataFusion trait structure (chunks are bound to
their tables) makes this kinda pointless.

Closes #3974.

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

* docs: mention tracking issues

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[c26a554900...](https://github.com/niftynei/lightning/commit/c26a55490032c2bbac85900058b06b8db52cfe12)
#### Monday 2022-03-21 18:59:33 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [Perkedel/HexagonEngine](https://github.com/Perkedel/HexagonEngine)@[a146411ab0...](https://github.com/Perkedel/HexagonEngine/commit/a146411ab0c407da387b32437173287ffaefb4b3)
#### Monday 2022-03-21 19:34:59 by Joel Robert Justiawan

political shock

https://twitter.com/DsaiAndrew/status/1500768197850525697?s=20&t=eHZNug9TTh1olkfsHGk4YQ

https://docs.google.com/presentation/d/10aAo7SUAEabCSXDPMJEbpQ_ngu1kgKJG/mobilepresent?slide=id.g1186945f7cf_6_7

wtf timeline!? I love latex-like shiny skin material!!! Oh man. I wanted to make game about this. make film game about this.

QUick, hide this! don't let anyone see this. Oh sh88! I think Krostenqeni found it already. Okay, just pecking hide it. see what happen next, like is it nothing happened, or happened big idk.

Okay hear me out, We may be a hypocrite for not canceling LoulouVZ. Yes, this is screwed up, undefendable, just like YandereDev. Difference is, she atleast has one thing went real. not huge, just the comic, 3 reboots. but it's there. not like YandereDev who still... forget about it, won't see that coming I guess. idk.

These drawings, in the artstyle is f8888 amazing awesome, I am in love! mmmmmh! Man! Spaicy skin, mmmmmmmm!hhhhh!! Imagine low roughness, specularly iridescent

This makes it even harder for me to go out.

I saw Steam. they are bad person too. DRM!!! Digital Restriction management, ew!!! But that guys... make Linux Gaming, canon! they make.. cool games! last but not the least, they're one of the company that make piracy obsolete! that also make me hard to go out.

any other bad person but makes great product? I know, Google, Microsoft, wai wait. with specific issue like her and him. who is it? Okay idk, I have no idea yet.

God, help me.

Wait, Yeah I uh donated her for "iOS app development kit" and uh... I think that's the Emergency funding. can't see that one come out. Oh shoot. Maybe that's that.

---
## [sandutsar/terminal](https://github.com/sandutsar/terminal)@[855e1360c0...](https://github.com/sandutsar/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Monday 2022-03-21 20:02:31 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row. 

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight. 

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

---
## [ModruKinstealer/CS50ProblemSets](https://github.com/ModruKinstealer/CS50ProblemSets)@[1a885e3fc1...](https://github.com/ModruKinstealer/CS50ProblemSets/commit/1a885e3fc1aee54e8eacc5313fdc4e7758630b29)
#### Monday 2022-03-21 20:43:54 by ModruKinstealer

Problem set3: tideman original upload 3/9/22

Specification
https://cs50.harvard.edu/x/2022/psets/3/tideman/

You should not modify anything else in tideman.c other than the implementations of the vote, record_preferences, add_pairs, sort_pairs, lock_pairs, and print_winner functions (and the inclusion of additional header files, if you’d like). You are permitted to add additional functions to tideman.c, so long as you do not change the declarations of any of the existing functions.

I did fairly well on this pset, up until sort_pairs. I struggled with getting it to work properly but managed to figure it out. lock_pairs I spent over a week on and probably in the 30-40 hours? I'm not sure how much I should have actually spent, I spent a long time working on it before I realized that my recursive call to cycle_created had the arguments reversed and I was sending (loser, winner) instead of (winner, loser) It still took me another few hours to get everything nailed down in that one. In the end I'm not sure that I actually learned anything from trying to implement the recursive function of cycle_created.  If I get time I might come back to tideman after the course and see if I can solve it more easily/faster. I did find numerous posts about how tideman was the hardest problem in the entire course and that a lot of people struggle with it so I'm not totally upset with it taking so long. I'm glad to have completed it with minimal looks at hints beyond something like https://gist.github.com/nicknapoli82/6c5a1706489e70342e9a0a635ae738c9
My biggest frustration came from the feeling that at this point I don't think I could have come close to figuring out this program from scratch if I was tasked to do so in the real world. I would definitely need assistance from a senior dev or something. I feel like I understand the tideman process itself, but translating it to code was very difficult.
There were a couple other functions that I thought would have been good candidates for a recursive function but I decided against it, one because it specifcally stated the function should only be called once and also because we couldn't change the functions and they were void for both arguments and returns. I figured if I created a custom function that did the function recursively and the original one basically just called the custom function it wasn't really following the specifications of the problem set. 

Print_winner I spent way more time on that I should have had to. I had implemented it references pairs[], my thinking was that we did all the work to create and sort pairs and cycling through that would take a lot less cycles than cycling through locked[][]. However the function just would not pass check50 using pairs and I found a mention on the cs50 discord that check50 wouldn't pass it if you used pairs over locked so I re-did the code to use locked[][] and it worked within minutes.

Last note, I'm getting pretty good at the implemented style guide for cs50. I did have a few changes I had to make where I missed a space, if( instead of if (, or variable+1 instead of variable + 1. But less than a dozen missed spaces in 284 lines of codes seems relatively reasonable at this stage so I'm happy with my progress there.

---
## [noahshaw11/couchdb](https://github.com/noahshaw11/couchdb)@[9b6454b81c...](https://github.com/noahshaw11/couchdb/commit/9b6454b81ca1a599da1f538548dc67654b6ce8d7)
#### Monday 2022-03-21 21:13:59 by Adam Kocoloski

Refactor Jenkins build to dynamically generate test stages (#3903)

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 24.2 as the embedded Erlang version in packages.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

---
## [PseudoDistant/ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby](https://github.com/PseudoDistant/ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby)@[a21d7df1b8...](https://github.com/PseudoDistant/ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby-ruby/commit/a21d7df1b8e0e8afc45adf84d551ed696fd1b8bf)
#### Monday 2022-03-21 21:15:13 by Distant

The heckin Ruby file builds this...

In this exact location, even...
Fuck you Gradle.

---
## [kofemann/guava](https://github.com/kofemann/guava)@[e015172847...](https://github.com/kofemann/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Monday 2022-03-21 23:07:31 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---

