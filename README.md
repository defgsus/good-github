## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-25](docs/good-messages/2022/2022-05-25.md)


1,670,443 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,670,443 were push events containing 2,700,822 commit messages that amount to 211,424,046 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [ItzSheilzy/Snake-Game](https://github.com/ItzSheilzy/Snake-Game)@[dfeb01b3ef...](https://github.com/ItzSheilzy/Snake-Game/commit/dfeb01b3ef9fcefbc1fb84175463865c260fa2f2)
#### Wednesday 2022-05-25 00:37:54 by William Sheil

Snake Game Final Final Version

This is the final final finished product of my Snake Game 
What's new
The Border of the map is gone and replaced with a Red floored map and if you go right up to the edge in game mode 1 you will die and in game mode 2 you will come out the other side of the wall
I Put the map to the original size and speed thanks to the bug fix made in the game

Final Bug fixes
Fixed a bug where the fruit would spawn outside the map and ruin the run once you get to 51 fruits 

it looks a lot more cleaner now and I am very happy how it turned out
I Hope you enjoy playing it

---
## [cheeserox/pokTwo](https://github.com/cheeserox/pokTwo)@[0e63ce5dd8...](https://github.com/cheeserox/pokTwo/commit/0e63ce5dd8c6052b43daaba4eb35f6438b377058)
#### Wednesday 2022-05-25 01:17:13 by Chaz "Gamerappa" Péloquin

fuck you, no 2013 html5 player

i've wasted like 3 hours of my life getting nothing to work, fuck this.

---
## [redguy999/tgstation](https://github.com/redguy999/tgstation)@[20e4add487...](https://github.com/redguy999/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Wednesday 2022-05-25 01:18:30 by Tim

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
## [MrDoomBringer/tgstation](https://github.com/MrDoomBringer/tgstation)@[a137c15a79...](https://github.com/MrDoomBringer/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Wednesday 2022-05-25 01:49:46 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[c77fb1e795...](https://github.com/pariahstation/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Wednesday 2022-05-25 01:51:40 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [DarkoniusXNG/ancient_battle](https://github.com/DarkoniusXNG/ancient_battle)@[11de86211c...](https://github.com/DarkoniusXNG/ancient_battle/commit/11de86211ca2f0402fec33960337ea7f49ed0d43)
#### Wednesday 2022-05-25 02:03:11 by Darko V

Some fixes

* Fixed Paladin's Angel Wings not appearing properly and for full duraiton.
* Added Halo to the Paladin's Angel
* Wrath of God Angels will no longer spawn for neutrals. (This is the best way to reduce the lag. I tried to fix it in another way using Async, it crashed the game for some reason.)
* Eternal Devotion Angel min duration increased from 6.5/7/7.5/8 to 10 seconds.
* Void Demon Time Slow cooldown reduced from 45/40/35/30 to 23/22/21/20 seconds.
* Void Demon Time Slow mana cost reduced from 120/130/140/150 to 80/90/100/110.
* Void Demon Time Slow move speed slow improved from 10/18/26/34% to 18/26/34/42%

---
## [cuckooman/Merchant-Station-13](https://github.com/cuckooman/Merchant-Station-13)@[f51ff8cdbd...](https://github.com/cuckooman/Merchant-Station-13/commit/f51ff8cdbd744bf998ea669bab7e523eb023baa9)
#### Wednesday 2022-05-25 02:26:16 by hamurlik

Adds simpson skintone (#138)

* Adds simpson skintone

The sign is a subtle joke. The shop is called "Sneed's Feed & Seed", where feed and seed both end in the sound "-eed", thus rhyming with the name of the owner, Sneed. The sign says that the shop was "Formerly Chuck's", implying that the two words beginning with "F" and "S" would have ended with "-uck", rhyming with "Chuck". So, when Chuck owned the shop, it would have been called "Chuck's Fuck and Suck".

Co-authored-by: EtraIV <34369281+EtraIV@users.noreply.github.com>

---
## [rmboyce/ucla-hangbruin](https://github.com/rmboyce/ucla-hangbruin)@[76bf4d5901...](https://github.com/rmboyce/ucla-hangbruin/commit/76bf4d590120dc8befd864749db3ee958d70f1a3)
#### Wednesday 2022-05-25 02:26:42 by victorli2002

Send reviews to Firebase

Was able to send reviews/comments to firebase, but this shit like doesn't work half of the time because of some localhost bullshit.
"Something was already running on PORT 3000" like bitch gtfo.

Honestly restarting react was like the only fix that I found but it didnt work all the time. Maybe my wifi is bad?

---
## [brandonneth/chapel](https://github.com/brandonneth/chapel)@[bf1082871e...](https://github.com/brandonneth/chapel/commit/bf1082871e365ebaebf0057c1793ebcae9e963e7)
#### Wednesday 2022-05-25 02:50:51 by Andy Stone

Merge pull request #19851 from stonea/llvm_check_for_lclang_cpp

Add check to see if libclang-cpp-dev package is installed and ensure missing package errors get to user

I'm trying to install llvm 13 on my desktop to use it as the "system" LLVM when CHPL_LLVM=system.  Anyway, I must have forgotten to install a package because when I build Chapel I get this error:
`/usr/bin/ld: cannot find -lclang-cpp`

I figured out the missing package was: libclang-cpp-dev (after apt-getting it things work fine).
It's a better user experience if we can get printchplenv to guide the user towards installing the necessary packages. I see in chplenv/chpl_llvm.py (in the check_llvm_config function) we have some checking that looks for things like missing include files (due to missing packages) and produces some nice error messages. Unfortunately, these error messages never reach the user, rather you'll get this more confusing error:

`Exception: CHPL_LLVM=system but could not find an installed LLVM with one of the supported versions: 14, 13, 12, 11`

You can reproduce this by running sudo apt remove libclang-dev and running printchplenv. I think this is due to a bug where we produce the error message (and add it to some error log) but never actually report it to the user.

In this PR I fix this so we separate out the check for the presence of llvm_config from the other checks about include files (and now libs) and ensure that we run these checks when we're using the system LLVM.
I also add in the check for missing -lclang_cpp, you'll now get this message if it can't find it:

`Perhaps you need to install the libclang-cpp-dev package`

[Reviewed by @daviditen]

---
## [LZakida/vgstation13](https://github.com/LZakida/vgstation13)@[da0db7dac8...](https://github.com/LZakida/vgstation13/commit/da0db7dac8d8237115e38429767b243092bf0bd7)
#### Wednesday 2022-05-25 03:08:32 by L Z

wow all this for lolvests

Hazard vests are (mostly*) in again

+added nitro tanks to all vests whitelist
*fixed path issues for all vests
+added pie cannons
+added the Last Miner Standing suit
*fixed bugs that existed in former codebase for both piecannons and LMS suit that I somehow never noticed. Seriously, these were super obvious bugs. How did I not see this shit?!
+added code files for future port jobs. Currently only contain a comment line and do nothing.
*throw guns renamed to yeet guns. added a sound variable to spam firing check, currently the fart noise. This makes the BPC a potential fart machine which is pretty fucking funny to me.

---
## [dedshit/Zee5](https://github.com/dedshit/Zee5)@[2c879e70e4...](https://github.com/dedshit/Zee5/commit/2c879e70e4fe828ee61f2a988e5eaa81ac5f9e2d)
#### Wednesday 2022-05-25 03:10:52 by dedshit

added fucking heroku app

nothing just a bullshit zee5 copying this shit leads to ass cancer lol 😂😂😂

---
## [RecordReplay/devtools](https://github.com/RecordReplay/devtools)@[ddd6d3fd39...](https://github.com/RecordReplay/devtools/commit/ddd6d3fd398f823c757df036f3662f7af894ba24)
#### Wednesday 2022-05-25 04:28:26 by Josh Morrow

Motivation and Changes

Soft focus has been a theoretical goal of the front-end team for close
to a month at this point (although it was really just me tinkering and
thinking for the first couple of weeks). And that has produced some
results, but there's still quite a bit in motion, as well as some
unknowns. Technically, all we need to do to enable V1 of soft focus is
not onload regions upon the focus window changing (we still issue the
load command, because if we are already loaded it is a noop, and if the
backend has unloaded a portion of the recording that the user has asked
for, we need to ensure that we reload it). One thing that jumps out as
soon as you enable soft-focus is that we need more specific points to
pass for ranges to backend functions like getHitCounts. I tried just
using getPointNearTime with the focus window times, but that is no good,
because it always returns the beginning of the region, so sub-region
focus windows end up looking like windows of 0 length in point-terms.
Instead, I do a more sophisticated version of what we were doing
previously with timeline seeks:

Any time we get a timestamped point from the backend, we store it in a
sorted array in redux. Then, when the user sets the focus window, we use
that point array to approximate the point that lies near the user's
selected times. This is sometimes not very fine-grained, but here's the
elegant part: if there is stuff that matters around the area that is
being selected (for instance, analysis hits), then we will have stored
fine-grained point correlations already, and we won't be vastly off.
Conversely, if the points we have are really rough approximations, it is
unlikely that they will affect anything anyways, because the user has
not looked at anything of interest around them.

I was prepared for this to be terrible, but in my relatively limited
experience... it's pretty good? I think at the very least it is good
enough to enable it internally and poke around.

Followups:

- We should actually soft-focus analyses, but I will wait on Mark's
rewrite of the analysisManager before making that change.

---
## [xenkap/IceEngine](https://github.com/xenkap/IceEngine)@[73d7bf77a8...](https://github.com/xenkap/IceEngine/commit/73d7bf77a835d58afb4b0298ab7cccaf8e070fad)
#### Wednesday 2022-05-25 04:50:55 by xenkap

holy shit (mic'd up ui, main menu, icons, ratings, bf versions, THE FUCKING GANG)

what the fuck

---
## [crawl/crawl](https://github.com/crawl/crawl)@[f57aedb6d1...](https://github.com/crawl/crawl/commit/f57aedb6d1f1ab370f734d3b2dce165f5af6366c)
#### Wednesday 2022-05-25 05:02:04 by Nicholas Feinberg

New species: Star

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species! Stars
have an exciting variety of bonuses - good attributes and
aptitudes across the board, passive mapping, damage shaving (ala
Deep Dwarves), and eventually innate MP and HP regen. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Stars are humanoid beings. (In the night sky, they look like
  dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Stars' LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- A future commit will make stars shine.

---
## [TymurShatillo/Yogstation](https://github.com/TymurShatillo/Yogstation)@[c3e823d052...](https://github.com/TymurShatillo/Yogstation/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Wednesday 2022-05-25 05:26:44 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [TymurShatillo/Yogstation](https://github.com/TymurShatillo/Yogstation)@[8b77243ce9...](https://github.com/TymurShatillo/Yogstation/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Wednesday 2022-05-25 05:26:44 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [ImPrashantt/kernel_xiaomi_lavender](https://github.com/ImPrashantt/kernel_xiaomi_lavender)@[ba512c196b...](https://github.com/ImPrashantt/kernel_xiaomi_lavender/commit/ba512c196bbb428bb1e0913bb2081e2f5183a705)
#### Wednesday 2022-05-25 09:28:52 by Maciej Żenczykowski

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
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [UmaCafe/uma-cafe](https://github.com/UmaCafe/uma-cafe)@[260b00fd02...](https://github.com/UmaCafe/uma-cafe/commit/260b00fd02d4682054118efa64cee63003b76c79)
#### Wednesday 2022-05-25 09:45:07 by Snep

Merge pull request #27 from UmaCafe/develop

fix absolutely fucking insanely stupid bug

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[0f2755b42a...](https://github.com/NetBSD/pkgsrc/commit/0f2755b42a47006d5292f1391bf224c8c8b2532f)
#### Wednesday 2022-05-25 10:26:54 by wiz

mame: update to 0.244.

Given how many exciting updates have gone into MAME 0.244, it’s
hard to believe it’s only been a month since the last release! Only
one disk has been added to the Apple II software lists, but it
comes with a very engaging story involving physically damaged media
and manual data repairs. The Zilog Z80 CPU has had a bit of an
overhaul this month, allowing more accurate memory access timings
for the ZX Spectrum family. This fixes a lot of broken visual
effects and other glitches. The HP 9000/300 series computers have
had the necessary floppy disk image formats hooked up, allowing
them to mount floppy disks from their software list.

MAME’s driver for JPM’s first CPU-based fruit machine platform,
dating all the way back to the late 1970s, has been almost completely
rewritten this month. Four games are now playable, albeit with
minimal internal artwork. Colour video output has been implemented
for Zilec’s Vortex. Don’t get too excited, though – while the
approach they used to produce colourful graphics without adding
any video memory is technically interesting, the results are very
ugly and don’t make a bad game any better.

Other improvements in arcade emulation include:

    Score display and diorama control outputs have been hooked up
    for Bubble Trouble (this means you’ll need updated artwork for
    Golly! Ghost! as well).  Layer offsets in Slap Fight and Alcon
    should be fixed, and cocktail mode now works for the original
    sets.  The communication board for Super Street Fighter II:
    The Tournament Battle is now supported, allowing it to actually
    run in eight-player tournament mode.

SDL builds (the default for Linux and macOS) now detect game
controller reconnection. Note that due to limitations of SDL itself,
MAME may confuse similar controllers, potentially causing issues
if multiple controllers are disconnected at the same time. Issues
using MIDI input or output with 64-bit Windows builds should be
fixed.

---
## [sipakhti/WAD](https://github.com/sipakhti/WAD)@[a4ad29f0ca...](https://github.com/sipakhti/WAD/commit/a4ad29f0cae3c23d04b02eb189251ed61f0876fb)
#### Wednesday 2022-05-25 10:39:48 by Umer Mehmood

23 05 2022 (#7)

* class prep done

* no class. stupid as fuck regulatons and more idiotic gaurds

Co-authored-by: L1F20ASCS0028 <L1F20ASCS0028@ucp.com>

---
## [IKnopochka/js_ts_native_and_forStudents](https://github.com/IKnopochka/js_ts_native_and_forStudents)@[ff49ad3a78...](https://github.com/IKnopochka/js_ts_native_and_forStudents/commit/ff49ad3a781e6c6fb297325ad4c7147c709017e0)
#### Wednesday 2022-05-25 11:31:49 by Irina Novakovich

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

---
## [mar3an/L2Private_Server](https://github.com/mar3an/L2Private_Server)@[251c611817...](https://github.com/mar3an/L2Private_Server/commit/251c6118179a43021b9676b7e298ba30b7ea72b4)
#### Wednesday 2022-05-25 12:16:07 by mar3an

# Added Lucky Pig:

- Part I: Dimensional Merchants
(Dimensional Merchants are now functional.)

- Part II: Lucky Pig
(Lucky Pig are implemented and functional.)

  - While hunting in certain zones, you can encounter the Lucky Pig. Lucky Pig is a flying pig with white feathery wings. When it appears, it shouts and approaches a nearby character at random.

  - Lucky Pig eats Adena dropped nearby and disappears if not fed for 10 minutes. You can feed Adena to Lucky Pig a minimum of three times and a maximum of ten times. Talk to it to determine if it's full. When it is full, Lucky Pig loses its wings. At that point, it may give you a reward for feeding it.
You can obtain a reward either by feeding Lucky Pig ten times or talking to it after you have fed it at least three times.


   - Lucky Pig Locations:

  - Level 52 Lucky Pig: Enchanted Valley.
  - Level 70 Lucky Pig: Forest of the Dead, Valley of Saints.
  - Level 80 Lucky Pig: Wild Beast Pastures, Plains of the Lizardmen, Sel Mahum Training Grounds, Fields of Whispers & Silence, Crypts of   -   isgrace, Den of Evil, Primeval Isle, and the solo area in Dragon Valley.

   - Lucky Pig Rewards:

   - Level 52 Lucky Pig: Neolithic Crystal B and Top-Grade Life Stone - Level 52.
   - Level 70 Lucky Pig: Neolithic Crystal A and Soul Crystals - Stage 11.
   - Level 80 Lucky Pig: Neolithic Crystal S and Attribute crystals.

You can exchange Neolithic Crystals with a Dimensional Merchant to change a normal weapon into a rare weapon.
To change a weapon into a rare weapon, you need to supply the Dimensional Merchant with the weapon and 1 Neolithic Crystal of the same grade.

---
## [jecsatta/PhotoDemon](https://github.com/jecsatta/PhotoDemon)@[9dea56340e...](https://github.com/jecsatta/PhotoDemon/commit/9dea56340e82e33d43d27621b6dd9d8498979d98)
#### Wednesday 2022-05-25 12:39:05 by Tanner

First draft of `Edit > Content-Aware Fill` tool

Holy shit, friends - this actually works.  I'm honestly a little (okay a LOT) astonished to see the functional content-aware fill behavior in action, because part of me thought this was never going to work in a reasonably good way.

But it works, and it works *well*.  Like, this will be a tool that people actually use!

There's a ton of clean-up and refinement left to do (and I still need to build a UI) but that's easy-peasy compared to just getting the damn algorithm working in the first place.

---
## [jecsatta/PhotoDemon](https://github.com/jecsatta/PhotoDemon)@[bcc4e689ee...](https://github.com/jecsatta/PhotoDemon/commit/bcc4e689eea716a315f8f88871511c4ef386f05c)
#### Wednesday 2022-05-25 12:39:05 by Tanner

pdInpaint: a new solution for content-aware fill

Photoshop has a borderline-magical feature called "content-aware fill":

https://helpx.adobe.com/photoshop/using/content-aware-fill.html

I want something similar for PhotoDemon, so here we gooooooo!

The best reference I've seen on texture synthesis (which is what content-aware fill does - it attempts to "synthesize" a new "texture" that can be used to seamlessly "fill" over the top of an unwanted object) is Paul Harrison's PhD Thesis, "Image Texture Tools: Texture Synthesis, Texture Transfer, and Plausible Restoration":

https://www.logarithmic.net/pfh-files/thesis/dissertation.pdf

Using the concepts from his thesis, Paul would go on to release the "Resynthesize" plugin that provides content-aware fill in GIMP.  Resynthesize is still available as a GIMP plugin, but unfortunately it is under a new maintainer now and it is very challenging to build for Windows (and the source code is GPL anyway, so I can't use it in PhotoDemon even if I wanted to).

Fortunately, Paul's thesis is very comprehensive.  He lays out pretty much everything you need to consider when writing a texture synthesizer, and he cites many other author's takes on the topic (which are also useful references, with good ideas to be taken from all).

From these various references, I have now completed my first draft of a texture synthesizer for PhotoDemon.  This first draft is not actually a content-aware fill tool - that will come later - but it *is* a seamless tile generator, which provides a simple test ground for the underlying algorithm.  Basically, given an input image, the code tries to construct a novel output image that is capable of seamless tiling, using only pixel data from the original image as its reference.  From this, it's easy to study how the algorithm handles complexity and sampling, and whether it's capable of generating representative textures from a variety of inputs.

As it stands today, this code is slow, but it works well - very well, even - and I'm now at a stage where I comfortable committing it so I have a good backup reference before I start writing a UI for it.  (A UI is needed for further testing, since there are a number of parameters you can toggle to trade-off between quality and performance, and I need to ensure PD's algorithm works well across the entire spectrum.)

I don't have an ETA for final merge into PD, but it shouldn't be long - I'm thinking a measurement in days possibly weeks, not months.

---
## [walter-wa/odin-recipe](https://github.com/walter-wa/odin-recipe)@[76f42428de...](https://github.com/walter-wa/odin-recipe/commit/76f42428de5d18ab82cc2e33ad60e981dc870022)
#### Wednesday 2022-05-25 13:24:49 by walter-wa

Uploading the image files conatining pictures of the means whose recipes were covered in the odin recipe project. I'm sorry guys, i forgot to upload the photos while committing and pushing my earlier projects into git hub. It is amazing to share this experience with the github community

---
## [BeaTConT/BeaTConT](https://github.com/BeaTConT/BeaTConT)@[a02fc6cc06...](https://github.com/BeaTConT/BeaTConT/commit/a02fc6cc0635d019fccd38237c5e2e454defffae)
#### Wednesday 2022-05-25 14:00:08 by ILIA ConT

Update README.md

Persian electronic music composer.
Mohammad Raisi Azizi ,on Psytrance Project called: Ilia Cont
From 1998 in Iran
Over time, I began playing instruments such as the setar , dulcimer(santur), daf and reed(ney) with his family members. His interest in playing music led him to continue his career in music and began to learn and compose music in the Iranian traditional style. he became acquainted with electronic music in 2008 and began learning and Producing it the following year.

Since 2010, My first project style was Trance, along with other styles such as Trance ,G-House & another EDM style Musics .Inner Mine After 3 years in 2013, I tried Composing & Writing Melody With Pure Psytrance Feeling & I started to Create & Build collections & Release Like: INNER MINE , Suicide , ENERGY MIND & Some Single Track .Adaptive to Get a Favorable sense of Music to Listeners. iN tHE From of Biography.
So Now Welcome to My Universe .
A unique Story is On Way.
Hope to Enjoy by My Skill.
Soon ¡!..!¡

---
## [Glepooek/terminal](https://github.com/Glepooek/terminal)@[77215d9d77...](https://github.com/Glepooek/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Wednesday 2022-05-25 14:55:40 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [Sirryan2002/Paradise](https://github.com/Sirryan2002/Paradise)@[ab7a358506...](https://github.com/Sirryan2002/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Wednesday 2022-05-25 15:19:00 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [LunarWatcher/upm](https://github.com/LunarWatcher/upm)@[7843701f4c...](https://github.com/LunarWatcher/upm/commit/7843701f4ccc323b29323690dcb5240ef66c7689)
#### Wednesday 2022-05-25 15:23:53 by None

Stage one pi compatibility

Worked out installation, and I should in theory have that up and
running. Fucked up on which arm version was selected for node, but
that's a quickfix.

Haven't tested activation because I'm dumb, forgot which version I just
installed, and the lack of @latest symlinks/tracking is starting to
annoy me.

Should also start tracking which versions are actually installed. Not
sure if that's better suited for metadata, or if that's something
I'll just compute at runtime. Not particularly performant, especially if
the underlying file system is shit, but that's a problem for me to
figure out when I start diving into this rabbit hole.

---
## [fabian-s/spikeSlabGAM](https://github.com/fabian-s/spikeSlabGAM)@[04df885842...](https://github.com/fabian-s/spikeSlabGAM/commit/04df8858421f8a94a20cb0fb33adb588500786ec)
#### Wednesday 2022-05-25 16:05:37 by fabian-s

stupidity. utter utter stupidity.

also i hate fucking latex

---
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Wednesday 2022-05-25 16:42:53 by Marty Boren

Very rough skeleton of move code search

after many moons of struggle, I've finally got something that
kinda works.
There's an endpoint for searching for moves.
and an office page with a search box that hits that endpoint
and drops the results in a table.

i was really struggling to get the react part of this to work without
setting off an infinite loop, so now that I've finally gotten there
i want to commit even though this is still full of debug cruft.

lots of exciting things left to do, such as:
- the moves that are returned by the endpoint are missing most of the
  stuff they should have.
- We also can't search for DoD ID
- interface for passing search info between things is inconsistent

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[763cbfdf1b...](https://github.com/mrakgr/The-Spiral-Language/commit/763cbfdf1b1f4874e2ad0cef0f66344ae8cd9558)
#### Wednesday 2022-05-25 17:54:46 by Marko Grdinić

"8:45am. I am eager to try out Luxcore so I'll get started on that as soon as possible. Regarding Eevee, yesterday I considered moving lights further away and increasing the power to manipulate the light falloff, but I missed a really obvious problem with that. No, not the UI difficulties Blender would give me with dealing with objects that far apart. With Eevee the further the lights are, the more pixelated the shadows get.

Let me check out that thread, have I gotten any file requests fulfilled.

9:25am. Let me start instead of reading the Mob thread. First off, let me install the addon. Then I will check out what it has.

The installation went well, let me give it a try. Actually before that, let me check out the docs.

I pressed render and it seems to be frozen. Let me start taking things out of the scene. Maybe I should try rendering the default cube.

Possibly because of all the lights in the scene.

9:40am. Why isn't the HDRI working with LuxCore?

https://youtu.be/FE_ppJ6Tovk
Luxcore HDRI tutorial in Blender 2.79b

Let me watch this.

https://youtu.be/FE_ppJ6Tovk?t=115

It does not seem like he is doing anything special here.

I see that some of the Blender HDRIs supposedly have invalid values. The renderer is buggy. I got the studio HDRI to work thought. Nevermind this. I'll just put a single sun. What really matters is how well it performs. In fact, let me disable all lights and I'll just put a Sky there.

9:50am. It seems compiling Cuda kernels takes 15-30m for it.

https://youtu.be/Qr9t8VaV8z4
Luxcore Vs CyclesX Benchmark

https://youtu.be/UVattTf1a5Q
Blender 2.8 Luxcore Engine Setting Tutorial

This later one might be of interest to me.

https://youtu.be/myg-VbapLno?t=725

I remember Luxcore did not do well at all in BG's benchmark so I had not payed attention to it. Oh, right. If I remember, that guy turned off the faux bed creases for some reason. It might be good to try that, but it should not really influence anything.

...Yeah, it is not like it does not support it.

Nevermind. It took like 7m just to compile the kernels. Instead of path tracing which works about as well as one could imagine, let me try the other rendering mode.

10:05am. Bidi tracing with metropolis. It seems to work better. Now I notice that all the caches are turned off. Let me also turn on clamping.

10:10am. Hmmm, no it is noisy. Maybe there are settings that make it work particularly well.

https://youtu.be/UVattTf1a5Q?t=10

Let me watch this for a bit, and then I will move on to Malt.

https://youtu.be/UVattTf1a5Q?t=311

It recommends bidir for scenes with small windows.

https://youtu.be/UVattTf1a5Q?t=336

Here he says it is deprecated because as development went on Path became able to do the work of Bidi. Good thing I am watching this. No way would I have figured that out on my own.

10:40am. Huh, what the hell. I turned on the caches and the light tracing, and let it run. When I took a peek I see that I am getting an excellent result, far better than bidi. The balcony door is not shining like a lightbulb either, instead the light is nicely spread out just like in reality.

10:45am. Ok, this has my attention. Now I am feeling more motivated to study this more.

Ah, it says light tracing is just for caustics. I see. Let me go at it with the same settings, but without light tracing.

Ah, it says that the env light cache is to be used in scenes with small windows. I see now that I need to hover the cursor over the checkbox to get a tooltip.

10:55am. Yeah, light tracing was not responsible for the result. In fact, I get a better result almost immediatelly with this compared to Cycles.

11:05am. Huh, I wonder if portals are doing anything for Luxcore?

Ok, I see in the portal a warning that Luxcore does not use portals and suggest that I use env cache instead. Wonderful. I never liked portals to begin with.

Er, let me just render it again to make sure that those good shadows aren't from the portal like in Eevee. I'll just move it into the excluded collection.

No, there is no problem. Luxcore is great. I'll want to figure out why the sunrise HDRI is not working, but otherwise there is no problem.

Let me make some posts in the thread I opened.

11:40am. https://blenderartists.org/t/how-do-i-render-a-scene-where-most-of-the-lights-comes-from-grills/1381668/25?u=marko_grdinic

Hmmm, how did she get an area light to have this kind of grill pattern. Focus me. Let me think about what she is doing. I'll check out the file as well. After that I'll try out Malt.

11:45am. Right now I am looking at her file. No indirect lighting. That is good.

Ah, it is not a grill pattern in the area light. Instead she just put an area light where the sun beams fall on the wall.

12pm. I like her solution, it looks quite nice.

https://blenderartists.org/t/world-hdr/1239972

https://blog.polyhaven.com/what-is-clipping/

I think I should get some outdoor HDRIs from polyhaven.

12:05pm. Nevermind this for now. Let me just move on to the next step. Let me try out Malt.

12:15pm. I am just playing with the light in Malt. It definitely is not photorealistic. I am not sure how to write this, it seems to calculate the light shinning onto the object and the shadows they project differently. The former does not take into account the occluding objects, but the later does. Unlike Eevee it does not seem to be using shadow caches and as a result the shadows are very crisp and non pixelated.

12:20pm. I think I understand, Malt handles light and shadows differently.

Hmmm, how do I use this? Where are those nodes the dev showed in the preview yesterday. It is quite interesting that Malt sets up an VS Code project in the same folder as the blend file.

https://malt3d.com/documentation/graphs/

Ah, Malt has its own nodes.

12:35pm. https://www.youtube.com/playlist?list=PLiN2BGdwwlLqbks8h5MohvH0Xd0Zql_Sg

Let me check out the first video here.

https://youtu.be/tE99jgCCcNE?list=PLiN2BGdwwlLqbks8h5MohvH0Xd0Zql_Sg&t=55
> No graph type selected.

Yeah, this is a problem that I have right now.

https://youtu.be/tE99jgCCcNE?list=PLiN2BGdwwlLqbks8h5MohvH0Xd0Zql_Sg&t=103

What are these pixel shaders? I can only find vertex ones.

12:55pm. I am not making much progress. Let me take a look at the material examples.

I get a bunch of socket errors in the node tree. Things like this happen in developing software. Things get changed and added, and the examples become out of date.

https://polyhaven.com/a/signal_hill_sunrise

Let me get this exr. I want to see if Luxcore can be made to work with it.

As for Malt, I'll check it out later once some learning materials for it come out. Right now it seems it is just for shader wizards. I am not interested in getting into that right now.

Yeah, this works quite fine. It turns out it is possible to attach the HDRI to a sun light in Luxcore. That makes it easy to rotate the HDRI.

It keeps crashing. At least when I try to do viewport rendering.

I do not get it. Why is the HDRI crashing Luxcore.

1:55pm. Done with breakfast. The render crashed my rig.

2:05pm. It kind of looked good, but I can't get the abiental kind of shadows going around the grills.

Let me take a break here. I've been obsessing over that render for far too long. It is time to put this under wraps.

2:55pm. Done iwth the break. I needed some time to think and sort my thoughts.

I've been wondering why there wasn't a striped pattern going past the grills on the walls. I thought that it might be some kind of issue with the renderer at first, but thinking about the grill rays, I realized that to get those stripes you need a strong directional light. The sun acts as one, and with just the ambient light from the rest of the environment you wouldn't get that sort of thing. I realized that to get that pattern, the HDRI would need to have some kind of extra lights on it.

When I looked outside past the grills what I saw was the balcony railings and suddenly the lightbulb went off. The sun rays bouncing off the railing acts as extra light sources! Ahhhh, right...

Damn. Why didn't I realize this earlier?

Yesterday when I was playing with Eevee I was putting the lights around the balcony door, but I had no clue what they represented.

3:05pm. Let me do another 10m render. I like the golden rays and the background from that HDRI. I won't bother the balcony railing outside. I'll deal with the walls not having shadowy stripes.

Let me just do some work on the bevels. I left some sharp edges on various objects on purpose because I intended to do shader beveling. Let me do that now. Let me just first figure out how Luxcore handles that.

https://forums.luxcorerender.org/viewtopic.php?t=3380

It seems it does not have it. It does not work for me here either.

3:15pm. I'll let it render for 10m. Hopefully it won't crash my rig this time.

Actually, let me instead put a few bevel shaders on stuff first. Let me also bring the new and improved rig.

3:25pm. No, it is a nightmare trying to bevel anything here. I do not want to waste time with it. Forget it. Let me just do a final render and then I am moving on to the drawing stage. I'll close this issue (so to speak) on the Blender Artists forum. I'll also do a post in the /wip/ thread. After that I'll execute my drawing skill improvement plan. I'll just draw and draw from here on out until I get good enough at it.

///

I am satisfied with the results of this so I'll leave this thread be. I wish Luxcore (and Eevee) had a bevel shader, I specifically left some edges sharp in the models with the intention of beveling them at render time, but unfortunately only Cycles has it. Malt has it, but it does not have any learning materials. Since it just hit 1.0 it might be worth checking it out in a couple of months.

I modeled the room mostly in Moi, and what is next on the agenda is using it as reference for drawing practice. Everyone, thank you for the help.

///

Yeah, I am done with this. Let me take care of /wip/ thread.

///

Luxcore is slower than other renderers, but it can handle scenes the others can't once the caches are on. It handles those grills like a pro. Here is my reference, the only light source is from the HDRI. With this I should be able to start drawing practice. I regret not beveling the edges while I was modeling them. Neither Eevee nor Luxcore have a bevel (or round edges) shader, and Cycles which has it cannot handle this scene.

I tried out Malt as well, but right now it is too raw. It hit 1.0 so it should start stabilizing, but right now there are no learning materials for it. I'll wait a couple of months before checking it again. Right now I have no incentive to dive into it.

Phew, I am glad this is over. Not having beveled edges on a model is bad from a 3d modeling perspective, but it won't matter for a drawing reference. I'll try to tackle drawing by immitating a 3d program. Start with the wireframe, then hatch the face normals in the UV direction, after that the shading. I'll try avoiding tackling deformed surfaces like sheets until I am ready for them. I'll also try to avoid tracing the shapes outright as it would defeat the purpose of the training.

///

4:15pm. Let me just do this. Forget 3d for a while and focus on drawing.

4:20pm. Let me take a short break here.

As far as 3d is concenred I am close to breaking into 3/5, but it is not like I'd get some kind of prize for doing it. So if I took off now to practice drawing for a few months, that would be fine.

4:50pm. Let me resume. It is time to just draw, draw, draw. First of all, instead of just trying to do the scene, what if I play around with 3d primitives. I should try immitating standard 3d operations like booleans. I need to get into the drawing mood first. If I just have to force myself to do it, then I might as well get a job.

First of all why does brush density work the same as opacity for me. I thought with density drawing a stroke over an existing one would layer over it.

5:50pm. Ok, I gave it a try. And I am feeling depressed. The paper does not speak to me. I just can't summon any kind of accurate detail to draw over.

Me: *draws a bunch of lines*
Me: How close am I to my target?
Brain: *shrugs* Roughly there somewhere.

I look at the reference, and I am much further away than I aimed at. But the thing is, I am supposed to refine it without looking at the reference so much. Since the reference is perfect, just what am I trying to do here anyway? The reason why the 3d model came out good is because I was constantly observing the objects as I was modeling them.

6:05pm. No, just draw is not a realistic method of improvement for me. There isn't an exercise that will improve my visual memory at my age. It would be easy to do this if I had access to the self improvement loop, but I don't.

Look at it this way, now I have the perfect excuse to do that Zbrush course. As well study Malt.

To close off the day, how about I watch the tutorial on the illustration shader?

I should get the mangaka plugin and play with it tomorrow. I can turn real world scenes into linework easily enough. Even somebody of my mediocre ability can do that sort of thing. And if I have to bring in models, I can sculpt them and use comic rendering trick. Even if I cannot move my 2d skills from this low level, it will by no means stop me from getting the job done. The reason why modeling took me so long here is because I had to go into so much depth. I mean, in total I had 192 objects, and those are just the unmerged ones.

Sculpting a character would take me a day or two once I get good at this.

6:15pm. https://youtu.be/rXdeJ_sigf4
Blender Illustration Shader - Eevee Live Lighting Tutorial

Let me watch this.

https://www.youtube.com/results?search_query=npr+tutorial

I'll really busy myself with these. I'll make it my goal to explore different renderings for the room.

6:55pm. I should just stick to what I know. How about I study Malt for real. I dropped it, but how about I put in a more significant effort into figuring it out.

I am curious as to how far exactly I can push it. I won't know this unless I give it a serious try.

Maybe I'll fail at this and never reach the efficiency level I am seeking to make Heaven's Key work. But this approach is close to my nature of always being an explorer.

7:25pm. Ok, so the plan is this - I'll give Malt a serious try tomorrow. I'll open an issue and ask the dev how to run the examples.

7:30pm. Being unable to draw would be a huge disadvantage to an artist before the age of computers, but in 2022 it is not a big deal. I am going to handle it using sculpting.

7:50pm. Let me close here for the day. It is Birdie Wing time. Forget improving my 2d skills directly. I am going to aim for 3/5 in 3d. Nothing will stop me getting it."

---
## [gsteve3/tiller-challenge-2022](https://github.com/gsteve3/tiller-challenge-2022)@[62b54b4247...](https://github.com/gsteve3/tiller-challenge-2022/commit/62b54b424713b93030629be6bc6147c943c840f2)
#### Wednesday 2022-05-25 18:00:43 by Greg Stevens

feat(excel): 💄 LIZPORTER LIVES - New name, and beautiful print friendly 2-page layout for Worksheet `401 LIZPORTER WIZARD`

- I want this project to have both Import (CSV, JSON, ledger-cli, Quickbooks, etc...) and also Export, largely to those same formats.
- Importer, Exporter, etc... are all pretty specific to that operation.
- I 💗bearded dragons.
- Best Pet Shop and Advice ([School House Pets in Okotoks](http://www.schoolhousepets.org)), has stickers on their tanks that read ""You're a Lizard Harry!", which tickles my Dad Joke Funny Bone.
- `Import Wizard` => `Import Lizard` => `Lizport` => `Lizport Wizard`
- Project Name now `Lizport` :) May change.

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[769ac685b6...](https://github.com/willior/Action_RPG_1/commit/769ac685b6c4c5c4a394e7c06fcad8a39268ac81)
#### Wednesday 2022-05-25 18:23:24 by willior

crash fix & cleanup, MAJOR REFACTOR

attacking the slime (multiplying it) would crash the game is done after re-zoning. this was because when we instantiate the new slime, we'd used a newly created Global variable called "enemies" which was a reference to the World/YSort/Enemies node. the issue was that this variable was being set on launch, and not getting reset whenever we generated a new World, ie. changing zones. so when we attempted to add_child to enemies, we were attempting a function call on a deleted object.
i still want a globally accessible reference to the enemies node, although now it gets set on World._ready(). it can be accessed via Global.enemies_node.
the MAJOR REFACTOR is re-programming how the previously named GUI (now "HUD") was referenced. since i've decided to use global references to commonly accessed objects, i've decided to make the HUD one of them, and in doing so, re-naming it from GUI to HUD.
i'm also re-programming HUD elements, particularly in regards to multiplayer. when the HUD was first put together i was not as comfortable as i am now with the concept of inheritance, so each player's HUD elements were discrete scripts that reference the respective player's stats. the HUD element scenes can be different, because the placement of HUD elements differs for each player.
and an unexpected, and completely fucking nonsensical issue has popped up, out of nowhere, for no fucking reason. the crit text label has shifted up by a few pixels, for no fucking reason. now there is a bigger gap at the bottom of crit damagePopups and no gap at the top. there is no fucking reason why this should be occurring. the last time i touched the damagePopup code, other than changing tween values, was 1 fucking year ago. i have spent hours not only trying to figure out why this has occurred, but also how to fix it, and i cannot. it's a complete fucking waste of time trying to figure out what the fuck is going on here. there is NO FUCKING REASON THIS SHOULD HAVE HAPPENED. THE CODE/SCENE HAVE NOT CHANGED IN OVER A FUCKING YEAR. it is simply displaying in a FUCKING WRONG LOCATION. FOR NO FUCKING REASON. WHEN IT WORKED BEFORE. i am at a complete fucking loss. i have two options: continue trying to fix this and waste more fucking time because there's no reason why it should be occurring in the first place, or ignore it and waste my fucking time later. this is unbelievable.

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[648c963897...](https://github.com/facebook/hhvm/commit/648c963897f25839c9d1697939acaf8762a64978)
#### Wednesday 2022-05-25 21:28:43 by Lucian Wischik

mitigate HackIDE:idle messages

Summary:
There are two separate things going on with this diff. Both are prompted by a user repro where the progress-message "[HackIDE:idle]" keeps popping up.

**Fewer IDE_IDLE**. The behavior of hh_server is, if it receives an RPC from clientLsp, then it must receive a subsequent IDE_IDLE message from clientLsp before it will do any typechecking. It does this because it takes ~1s for hh_server to wind down a typecheck and then start one up again, which made things clunky and slow when you were doing a lot of typing and interrupting a typecheck with every keystroke you made. The design is that IDE_IDLE only gets sent after the LSP queue has been emptied.

We had accidentally gotten this code wrong at times, so that sometimes the IDE_IDLE message didn't get sent and hence hh_server got permanently stuck, but that seems to have been fixed for a year or more. The final robust design was that for every single event (other than "tick" meaning no-event), then clientLsp would believe it needed to send IDE_IDLE.

This became a bit inessential with clientIdeDaemon, where we'd send IDE_IDLE even after clientIdeDaemon had handled a hover request all by itself, but wasn't too bad.

It became downright frustrating with streaming-IDE-errors, where hh_server sends error updates while a typecheck is underway. Every single one of these counted as an event, which prompted the catch-all robust design to think it needed to send an IDE_IDLE, so it did, which caused hh_server to interrupt then restart its typechecking for ~1s to deal with this message. DOH!

This diff changes clientLsp so that we only think we need to send IDE_IDLE after having sent some kind of message to hh_server (apart from sending IDE_IDLE to hh_server).

**Unclear status**. When hh_server received and processed IDE_IDLE, then it would update progress.PID.json accordingly, and the command-line hh_client would display the progress message [HackIDE:idle]. But then it takes ~1s for bulk typechecking to resume, we're not going to display any progress message until it does, so users just see [HackIDE:idle] even when they know there's a lot of typechecking to do and they just wish it would get on with it. This is confusing to us on the hack team, and to users.

This diff makes a minor change. It now displays [HackIDE:idle] while it embarks upon handling this request, and [HackIDE:idle done] after it's finished. In this way, we on the hack team will at least know that the "idle" command-handling is done, and what we're witnessing is the ~1s it takes to resume after the interruption.

(I think it's good that users and we on the hack team will know WHICH interruption is the cause for the ~1s resumption that we're seeing.)

Did all these interruptions cause actual slowness in overall typechecking time? -- not that I could reasonably measure, not within the bounds of noise.

Reviewed By: CatherineGasnier

Differential Revision: D36392047

fbshipit-source-id: 245f22eb33e9aeb034f8a7a193f3c941ed257610

---
## [wrachel/PrimitiveApes](https://github.com/wrachel/PrimitiveApes)@[0021e24fe6...](https://github.com/wrachel/PrimitiveApes/commit/0021e24fe61c9bc9957083da5bf59137e6fd4d78)
#### Wednesday 2022-05-25 21:49:23 by wiz124

fixed thymeleaf, some idiot fucking fiddled with forbidden shit

---
## [cheeserox/pokTwo](https://github.com/cheeserox/pokTwo)@[2687a9f50b...](https://github.com/cheeserox/pokTwo/commit/2687a9f50b1411e7fae8e76e06c63b777384a20e)
#### Wednesday 2022-05-25 22:19:02 by Chaz "Gamerappa" Péloquin

pain in the ass

we're not gonna support 2005, hence why we're dragging backend shit around.

---
## [Feyn-23/Lab-II](https://github.com/Feyn-23/Lab-II)@[e6698e3cc0...](https://github.com/Feyn-23/Lab-II/commit/e6698e3cc02fb67b1f11916bc90e07d5d47caf30)
#### Wednesday 2022-05-25 22:43:18 by Niccolò Zanotti

Hate level of this stupid fuckin experiment: over 9000

---
## [mrnuke/openwrt](https://github.com/mrnuke/openwrt)@[609538e3e2...](https://github.com/mrnuke/openwrt/commit/609538e3e2e4c965502233f13a196f98e3f4e911)
#### Wednesday 2022-05-25 22:55:25 by Alexandru Gagniuc

realtek-poe: De-suckify "poe sendframe" command

Typing "0x" repeatedly in a string of numbers that's obviously
hexadecimal is painful. So don't use sscanf(), which forces the "0x"
prefix. Instead, use strtoul() in base 16. This accepts numbers with
and without the prefix.

Also, if the string we receive is crap for whatever reason, don't try
to send it to the PoE controller. Just throw it the fuck out.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[6ec4ec8237...](https://github.com/Buildstarted/linksfordevs/commit/6ec4ec82372874d6c13921822d77987fd8923613)
#### Wednesday 2022-05-25 23:06:28 by Ben Dornis

Updating: 5/25/2022 11:00:00 PM

 1. Added: Why a PhD was not for me
    (https://dharmaram.bearblog.dev/why-a-phd-was-not-for-me/)
 2. Added: The power of tech debt
    (https://blog.simonwhite.io/startups-and-the-power-of-tech-debt/)
 3. Added: 6 Tips for Starting a Software Engineering Internship
    (https://calebschoepp.com/blog/2022/6-tips-for-starting-a-software-engineering-internship/)
 4. Added: Questions for Developers to ask at interviews
    (https://joshghent.com/interview-questions/)
 5. Added: CurlyTP: Every Web Server is a Dead Drop - MiscDotGeek
    (https://miscdotgeek.com/curlytp-every-web-server-is-a-dead-drop/)
 6. Added: Learnings from 5 years of tech startup code audits - Ken Kantzer's Blog
    (https://kenkantzer.com/learnings-from-5-years-of-tech-startup-code-audits/)
 7. Added: Lessons learned as a software developer turned project manager
    (https://karimjedda.com/lessons-learned-developer-to-project-manager/)
 8. Added: Linux and a Bluetooth Dongle
    (https://www.gaunt.dev/blog/2022/linux-and-bluetooth-dongle/)
 9. Added: A Kernel Hacker Meets Fuchsia OS
    (https://a13xp0p0v.github.io/2022/05/24/pwn-fuchsia.html)
10. Added: Advertising is Obsolete | Jake Poznanski — Software Engineer
    (https://www.jakepoz.com/thoughts/advertising-is-obsolete.html)
11. Added: Ghost in the Shellcode
    (https://www.notcheckmark.com/2022/05/ghost-in-the-shellcode/)
12. Added: The pain of using budget notebooks as a software developer
    (https://blog.l0g4n.me/using-budget-laptops/)
13. Added: How I made the most out of my coding bootcamp ?
    (https://blog.paul-verdure.com/how-i-made-the-most-out-of-my-coding-bootcamp)
14. Added: Message Ordering in Pub/Sub or Queues
    (https://codeopinion.com/message-ordering-in-pub-sub-or-queues/)

Generation took: 00:06:18.5029863
 Maintenance update - cleaning up homepage and feed

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[16b27f8569...](https://github.com/mbs-octoml/mbs-tvm/commit/16b27f8569436306c16b65e4937e5203cf7fb786)
#### Wednesday 2022-05-25 23:57:01 by Mark Shields

** Collage v2 sketch ***

- Host glitch if PlanDevices run before CollagePartition
- Fix unit test
- Make load_static_library first class python func
- Get CUTLASS going on graph executor as well as vm
- Include export_library in estimate_seconds
- Rollback DSOLibrary changes.
- Add StaticLibraryNode and switch CUTLASS to use it
  This avoids the crazy serialize/deserialize/load hackery, which I'll now remove.
- Get running again
- CUTLASS picks up all options from 'cutlass' external codegen target.
- Revert false starts with cutlass handling
- Get CUTLASS going with program-at-a-time tuning and compilation instead of
  function at a time.
- Save DSOLibraries by contents rather than by reference.
- futzing with libraries
- revert unnecessary cutlass changes
- starting unit test for dsolibrary save
- Prepare scalar changes for PR.
- Eager candidate cost measurement.
- More conv2d_cudnn.cuda training records.
- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
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

