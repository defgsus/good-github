## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-11](docs/good-messages/2022/2022-09-11.md)


1,776,977 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,776,977 were push events containing 2,365,227 commit messages that amount to 126,375,223 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [Elazar-Halperin/calculator2](https://github.com/Elazar-Halperin/calculator2)@[4de353159e...](https://github.com/Elazar-Halperin/calculator2/commit/4de353159e90479690de818f3b9937788f4a1284)
#### Sunday 2022-09-11 00:44:06 by Elazar Halperin

Merge branch 'main' of https://github.com/Elazar-Halperin/calculator2
okso first thing first fuck you

---
## [Stardust9681/AerovelenceMod](https://github.com/Stardust9681/AerovelenceMod)@[e1cb667958...](https://github.com/Stardust9681/AerovelenceMod/commit/e1cb667958d1834df82cd724fa0aeca367eff1d9)
#### Sunday 2022-09-11 00:58:33 by Stardust9681

(6) Magic Weapons

Ported & improved Carbon Cadence, Crystal Glade, Crystal Spray, Cthulhu's Wrath, Cursed Flame Staff, and Dark Crystal Staff

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[3b2cf65d59...](https://github.com/pizie11/orbstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Sunday 2022-09-11 01:08:15 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [wfleming/advent-of-code](https://github.com/wfleming/advent-of-code)@[8a904bbc88...](https://github.com/wfleming/advent-of-code/commit/8a904bbc88f6e5fdf3ddca86a060d8108cb34a75)
#### Sunday 2022-09-11 01:22:31 by Will Fleming

2018 d23

This is weird in that it is simulatenously among the hardest, most
frustrating AOC puzzles I've done, and yet once it's all done it all
seems fairly straightforward.

Part 1 was trivial, part 2 was a huge headache.

The basic search-the-space ideas weren't that hard to figure out. I
initially was leaning towards a binary search type approach, but after
reading some Reddit posts I learned about octrees and that seemed
sensible so I tried that since my binary search approach wasn't running
quickly.

My octree approach was also woefully slow, though. I think the real
issue I had that kept me from a completes-in-reasonable-time algorithm
was my original `Cube#intersect?(bot)` implementation wasn't accurate
enough. I started with a sphere-intersects-cube test
(https://stackoverflow.com/questions/4578967/cube-sphere-intersection-test),
which doesn't quite match the problem (because bots use manhattan
distance, their range isn't really a sphere).

Treating them as a sphere gives a bit of extra range, but I figured it
would be good enough as an estimate (and better to slightly overcount
than undercount bots intersecting a cube), and that once I got down to
smaller cubes the error wouldn't matter much. That turned out to not be
true - with this approach *most* octree nodes, at pretty much all sizes,
thought they'd intersect with 975 bots in my input, which was
effectively going to force the search method to search most of the
search space down to pretty small cubes, which was going to be very
small.

I found a better implementation for the interesection test on the reddit
megathread
(https://www.reddit.com/r/adventofcode/comments/a8s17l/2018_day_23_solutions/ecfmpy0/).
I confess I don't quite understand *how* this calculation works, and I'd
like to, but I'm tired right now, and it seems to be accurate so that's
good enough for me right now.

This still isn't very fast, about 17s for me. Good enough, though!

---
## [LetsZiggy/black](https://github.com/LetsZiggy/black)@[0019261abc...](https://github.com/LetsZiggy/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Sunday 2022-09-11 01:25:06 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [packkill/RosettaStone](https://github.com/packkill/RosettaStone)@[a4cc04fff8...](https://github.com/packkill/RosettaStone/commit/a4cc04fff867a53ee3fb9f9c9a5607a14f92358d)
#### Sunday 2022-09-11 01:33:32 by Chris Ohk

feat(patch): Apply card update for Hearthstone Patch 24.0.3

- Celestial Alignment: Old: Set each player to 0 Mana Crystals. Set the cost of all cards in hands and decks to (1). → New:  Set your Mana Crystals to 0. Set the cost of all cards in your hand and deck to (1).
- Stag Spirit Wildseed: Old: Dormant for 3 turns. When this awakens, equip a 4/2 Greatbow. → New: Dormant for 3 turns. When this awakens, equip a 3/2 Greatbow.
- Snowfall Guardian: Old: 3 Attack, 3 Health. Battlecry: Freeze all other minions. Gain +1/+1 for each Frozen minion. → New: 5 Attack, 5 Health. Battlecry: Freeze all other minions.
- Vile Library: Old: Give a friendly minion +1/+1. Repeat for each Imp you control. → New: Give a minion +1/+1 for each Imp you control.
- Kobold Illusionist: Old: [Costs 4] → New: [Costs 5]
- Relic Vault: Old: [Costs 3] → New: [Costs 2]
- Relic of Extinction: Old: [Costs 2] → New: [Costs 1]
- Bibliomite: Old: 4 Attack, 4 Health → New: 5 Attack, 4 Health
- Magnifying Glaive: Old: 2 Attack, 2 Durability → New: 3 Attack, 2 Durability
- Abyssal Depths: Old: [Costs 4] → New: [Costs 3]
- Battleworn Vanguard: Old: 2 Attack, 1 Health → New: 2 Attack, 2 Health
- Irebound Brute: Old: [Costs 8] →  New: [Costs 7]
- Legendary Invitation (generated by The Countess): Old: [Costs 3] → New: [Costs 2]
- Stand Against Darkness: Old: [Costs 5] → New: [Costs 4]
- Warhorse Trainer: Old: Your Silver Hand Recruits Have +1 Attack. → New: Your Silver Hand Recruits have +2 Attack and Taunt.
- Promotion: Old: Give a Silver Hand Recruit +3/+3. → New: Give a Silver Hand Recruit +3/+3 and Taunt.
- Edwin, Defias Kingpin: Old: [Costs 4] 4 Attack, 4 Health → New: [Costs 3] 3 Attack, 3 Health
- Sprint: Old: [Costs 6] →  New: [Costs 5]
- Silverleaf Poison: Old: [Costs 2] → New: [Costs 1]
- Halkias: Old: Deathrattle: If you control a Secret, store Halkias' soul inside of it. It resummons Halkias when triggered. → New: Stealth. Deathrattle: Store Halkias's soul inside of a friendly Secret. It resummons Halkias when triggered.
- Sanguine Depths: Old: Deal 1 damage to a minion and give it +1 Attack. → New: Deal 1 damage to a minion and give it +2 Attack.
- Imbued Axe: Old: After your hero attacks, give your damaged minions +1/+1. Infuse (3): +2/+2 instead. → New: After your hero attacks, give your damaged minions +1/+2. Infuse (2): +2/+2 instead.
- Cruel Taskmaster: Old: 2 Attack, 2 Health →  New: 2 Attack, 3 Health
- Tidal Revenant: Old: Battlecry: Deal 5 damage. Gain 5 Armor. → New: Battlecry: Deal 5 damage. Gain 8 Armor.
- Shield Shatter: Old: Deal 4 damage to all minions. Costs (1) less for each Armor you have. → New: Deal 5 damage to all minions. Costs (1) less for each Armor you have.
- Slam: Old: [Costs 2] → New: [Costs 1]
- Bash: Old: [Costs 3] → New: [Costs 2]

---
## [Optimism333/vgstation13](https://github.com/Optimism333/vgstation13)@[496d3bb777...](https://github.com/Optimism333/vgstation13/commit/496d3bb777d9538dd05b57d9a042acffd6496741)
#### Sunday 2022-09-11 02:09:13 by ValkyrieSkies

Med/Sci mapping changes on Metaclub, also Bridge lightswitch (#33197)

* Metaclub Science Improvements

* Feature creep

* Fixes the god awful bridge wallpipes

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/silicons/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Sunday 2022-09-11 02:10:34 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [moist-mason/Trollface](https://github.com/moist-mason/Trollface)@[642c5db641...](https://github.com/moist-mason/Trollface/commit/642c5db64195c3294937ee8d2b4fb45358f38887)
#### Sunday 2022-09-11 02:52:40 by moist-mason

This took way too long to make, holy shit. I need to actually learn Java.

This commit adds the funny Totem of Trolling. Go ahead and see what it does.

---
## [projects-nexus/android_xtreme_kernel_lavender](https://github.com/projects-nexus/android_xtreme_kernel_lavender)@[d62897e2de...](https://github.com/projects-nexus/android_xtreme_kernel_lavender/commit/d62897e2de6908d4b4cb11a4a7aba066d15e43f8)
#### Sunday 2022-09-11 04:43:38 by Maciej Żenczykowski

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
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [a-flyleaf/ygbtdm](https://github.com/a-flyleaf/ygbtdm)@[40f4ed75e8...](https://github.com/a-flyleaf/ygbtdm/commit/40f4ed75e86ce63ffccf445cc2f00c4b23412026)
#### Sunday 2022-09-11 05:52:47 by a-flyleaf

designnotes: art updates

- What Happened To WR's Teeth. ✔
-+redraw teen!Joce a bit? just fix the hip area a bit, shouldn't look *too* scrawny (she's no Seq) + the left corner's just kinda weird ✔
- Diana's tie is too fucking long again isn't it :V and what the heck, do the endgame version while you're at it; keep the grin (make the DEFAULT expression drier), and i GUESS she can have the tie. as a treat(/touch of blue because blue = past or smthn) ✔
- forgot the lines on her neck too ✔
- did not color sequitur's earrings ✔
- maaaaaaybe change KL's default arm pose? crossed behind the back, I really like that one (and it's more different from Addison) ✔
- check inner ears ✔
+paste this whole thing into the commit desc, why not ✔
- white (50%?) outlines?? just makes the outline look less like ass on a black/dark background, helps hide any stray pixels ✗ (maybe later)

---
## [holgerschlegel/chummer5a](https://github.com/holgerschlegel/chummer5a)@[85dc0f8354...](https://github.com/holgerschlegel/chummer5a/commit/85dc0f8354083947e63cb021d7b20d7a88af6dbc)
#### Sunday 2022-09-11 06:10:25 by Teksura

Toxic and mutant critters (#4899)

* Adding Kokoro Cobra

I mean it mostly works. I feel it's kinda bullshit that the natural weapon doesn't work but that's a later problem

* Update critters.xml

fuck

* Update critters.xml

Adds Pandamonium and Montauk

* Update critters.xml

Added the last of the Critters

* Delete .DS_Store

This file should have been ignored

---
## [zenosa/android_kernel_xiaomi_msm8956](https://github.com/zenosa/android_kernel_xiaomi_msm8956)@[995e42ed19...](https://github.com/zenosa/android_kernel_xiaomi_msm8956/commit/995e42ed1940cd130d4499205a1ab850c1453197)
#### Sunday 2022-09-11 06:25:11 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

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
[nc: Omit rpmsg, sdw, tbsvc, and typec as they don't exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [boot2big/immersive_vehicles_vanity](https://github.com/boot2big/immersive_vehicles_vanity)@[75b5c46547...](https://github.com/boot2big/immersive_vehicles_vanity/commit/75b5c46547c51c49447a7e4650eaa77735b3d754)
#### Sunday 2022-09-11 07:13:27 by boot2big

That oughta fucken do it
Git uses vi now. Even though I need to learn it more
..Oh yeah also there's proper registry for the random old man sounds I don't remember adding.
huuh?

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[7c64d6bc23...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/7c64d6bc23932166425605b0263e750dc0760bde)
#### Sunday 2022-09-11 07:34:18 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Vishal123raj/Heart-desease-dataset-analysis](https://github.com/Vishal123raj/Heart-desease-dataset-analysis)@[09394e91c9...](https://github.com/Vishal123raj/Heart-desease-dataset-analysis/commit/09394e91c917941c3d59e3762b6d3ec3a8da4696)
#### Sunday 2022-09-11 08:45:58 by Vishal Raj

Create README.md

Heart-disease-prediction-analysis
AGE:    Age in years
SEX:    1 = Male; 0 = Female
CP:    Chest Pain type
TRESTBPS:   Resting Blood Pressure (in mm Hg on Admission to the Hospital)
CHOL:    Serum Cholestoral in mg/dl
FPS:    Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)
THALACH:    Maximum Heart Rate Achieved
OLDPEAK:    ST Depression induced by Exercise Relative to Rest
CA:   Number of Major Vessels (0-3) Colored by Flourosopy
THAL:    A blood disorder called Thalassemia (3 = Normal; 6 = Fixed Defect; 7 = Reversable Defect)
TARGET:    1 or 0

Conclusion:
 using visualization and compare different machine learning models based on accuracy and it is found that Decision Tree and Random Forest work efficiently for this data set

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c1e4b63e07...](https://github.com/LemonInTheDark/tgstation/commit/c1e4b63e072e1f9dc16ac8c134a46313eb36c986)
#### Sunday 2022-09-11 09:15:01 by LemonInTheDark

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generate
corners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and
then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do
not need to. This resolves that, since it pissed me off.
It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad
expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is
this still here.

Oh also I deleted the turfs list, because it was totally unused. Come
on.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too

---
## [newstools/2022-los-angeles-times](https://github.com/newstools/2022-los-angeles-times)@[5caa2c8d44...](https://github.com/newstools/2022-los-angeles-times/commit/5caa2c8d44e68b931375b9388dc77f3b2eecd5c7)
#### Sunday 2022-09-11 09:26:59 by Billy Einkamerer

Created Text For URL [www.latimes.com/california/story/2022-09-10/mothers-boyfriend-arrested-in-murder-of-8-year-old-girl-found-dead-in-merced-authorities-say]

---
## [ByaCherX/react-rds](https://github.com/ByaCherX/react-rds)@[b6978bc38f...](https://github.com/ByaCherX/react-rds/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Sunday 2022-09-11 11:05:42 by Andrew Clark

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[57303fe8c9...](https://github.com/mrakgr/The-Spiral-Language/commit/57303fe8c9e42f19c5c38761877be68a16a1e873)
#### Sunday 2022-09-11 11:07:46 by Marko Grdinić

"10:35am. I played till quite late last night and only got up recently. Let me chill just a bit and then I will figure out how to deal with the Paypal link on RR.

10:45am. Let me figure it out.

https://www.paypal.com/buttons/

11:25am. Ended up talking in that RR thread I posted yesterday.

https://www.royalroad.com/forums/thread/122332

Now, Paypal button. Focus me, focus. I need to deal with this.

Paste the email url of your donation button?

Does that mean I just have to put in my own email address? I've checked that first link out, but what that does is produce some HTML I could paste into my own web page. This is obviously not what I need.

No, that wasn't it.

///

How do I find my PayPal donation URL?
You simply log in to PayPal, click on “Merchant Services”, click “Donations” and then follow the site's prompts to get your personalized HTML code.

///

https://www.gmg.cm/blog/creating-a-paypal-donate-link#:~:text=You%20simply%20log%20in%20to,get%20your%20personalized%20HTML%20code.

11:35am. https://youtu.be/o1SznCPE6F4
How To Create A PayPal Button To Accepts Payments Online

Mhhhh, let me watch this. I think that maybe I supposed to put the button code somewhere and link to it.

https://youtu.be/o1SznCPE6F4?t=107

Hmmm, saved buttons. Maybe those will have shareable URLs?

https://youtu.be/o1SznCPE6F4?t=249

Hmmm, what is this Email tab? That is definitely what I need!

https://youtu.be/o1SznCPE6F4?t=271

Yes, this is it. When I tried creating a button I only ever saw the code, where was the email? Let me try it again.

11:50am. I don't know. Paypal is behaving weird.

https://youtu.be/o1SznCPE6F4?t=153

To begin with, the UI I have is different. I have to go into options and seller tools. Once I get there, it directs me outside the site for some reason. If I click on view saved buttons I get an error. There isn't an option to actually save any of the buttons for me, just to extract the code. Do I maybe need a bussiness account for this? I am not sure.

Also, when I go to the buttons page, it tells me that I need to access it from a trusted page which is proof that it can't see I am logged in. There is something weird going on with the site.

https://youtu.be/2YO56yY8z-U
How to Create PayPal #Button Smart Buttons Donate Subscribe Buy it Now, Add to Cart 2022 Payments

Here is an updated video.

I am missing the Buy Now and Add To Card buttons.

https://youtu.be/2YO56yY8z-U?t=30

No, the UI is different for me already. How ridiculous.

> You’ll have to use our trusted partner sites to add our “Buy Now,” “Add to Cart,” “Subscribe,” and “Auto-Billing” payment buttons to your platform.

It is really confusing me as to why clicking on the buttons in seller tools ejects me from the site. Is the Paypal site buggy, or merely badly designed?

https://youtu.be/uGd3-8TvAmI
How To Collect Donations on ANY Website for FREE! | PayPal Donation Button

https://youtu.be/uGd3-8TvAmI?t=78

No the UI is different again. Do I maybe need a bussiness account?

https://wise.com/us/blog/paypal-business-vs-personal#:~:text=PayPal%20calls%20these%20Personal%20and,offers%20additional%20features%20for%20them.

https://youtu.be/N6Tm6y9xZ_A
Paypal Business Account VS Personal - Which One To Pick?

Let me watch this and I am done. If Paypal requires a business account then nevermind setting it up on RR.

12:15pm. It didn't really answer my question about the UI differences. I asked the Youtuber if business is needed.

12:20pm. Anyway, enough of this. I know what I need to put in now into Patreon, but I can't get it right now. Since I already have an avenue, I might as well go with Patreon. The Paypal button does not matter. Getting more followers does.

1:05pm. Done with breakfast. Let me chill just a bit and then I will get started. I think I'll post just a small part of chapter 9 and then I'll move the Spiral blog to Patreon. Let me commit here. I'll miss this place."

---
## [ProjectIgnis/CardScripts](https://github.com/ProjectIgnis/CardScripts)@[cc8f36cb12...](https://github.com/ProjectIgnis/CardScripts/commit/cc8f36cb12c9f1ca1b064c5294a1e09651992bca)
#### Sunday 2022-09-11 11:18:59 by pyrQ

Various script fixes/updates

Official:
- Armed Dragon Blitz: General script polish.
- Blackwing - Chinook the Snowstrike: The Quick version of its effect should be usable in the Damage Step.
- Blackwing - Twin Shadow: Added a hint timing for the opponent's End Phase.
- Chorus in the Sky: Small typo in the code regarding target redirection effects.
- Cipher Spectrum: Shouldn't activate if the Xyz Monster was sent to the GY by an effect but wasn't destroyed.
- Earth Golem @Ignister: Small typo in the code regarding target redirection effects.
- Ebon High Magician: Match the strings used in its script with the ones in its database entry.
- Evil★Twin Ki-sikil: Should check that you control an appropriate monster only when the effect would be activated.
- Evil★Twin Lil-la: Should check that you control an appropriate monster only when the effect would be activated.
- Fire Formation - Yoko: Shouldn't be considered an effect that destroys if the player doesn't target anything when activating it + general script polish.
- Flower Bloom of the Vernusylph: The last effect now uses the correct string.
- Gishki Chain: Adding a card to the hand and re-arranging the order of the rest shouldn't happen at the same time.
- Jurrac Meteor: If the effect doesn't successfully destroy anything then the player shouldn't be able to Special Summon a Tuner.
- Legendary Six Samurai - Enishi: Should also check the condition on resolution + general script polish.
- Live☆Twin Lil-la: Should check that you control no other monsters only when the effect would be activated.
- Live☆Twin Ki-sikil: Should check that you control no other monsters only when the effect would be activated.
- Lovely Labrynth of the Silver Castle: Should only protect Normal Trap Card activations, not Normal Traps' effects' activations.
- Shock Troops of the Ice Barrier: Shouldn't destroy the target if it's not a WATER monster anymore when this card's effect resolves.
- Star-Crossed Meeting: Should be able to negate its GY effect with something like "Solemn Warning".
- Virtual World Hime - Nyannyan: The Special Summoning restriction should be applied even if it's not Special Summoned successfully + general script polish.
- Wrath of Neos: Shuffling and destroying should be simultaneous + general script polish.

Unofficial/Rush:
- Monster Reborn (Rush): Should use the value indicating that it's a summon with "Monster Reborn".
- Speed Spell - Monster Reborn: Should use the value indicating that it's a summon with "Monster Reborn".

---
## [oleg-dubinskiy/reactos](https://github.com/oleg-dubinskiy/reactos)@[4471ee4dfa...](https://github.com/oleg-dubinskiy/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Sunday 2022-09-11 11:47:09 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [Caldony/lobotomy-corp13](https://github.com/Caldony/lobotomy-corp13)@[0611eb6563...](https://github.com/Caldony/lobotomy-corp13/commit/0611eb6563f7feaddae9a78f7ad276bed22b5378)
#### Sunday 2022-09-11 13:49:32 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

---
## [ChainsawGarden/Cataclysm-DDA-DF](https://github.com/ChainsawGarden/Cataclysm-DDA-DF)@[3dd5fbed93...](https://github.com/ChainsawGarden/Cataclysm-DDA-DF/commit/3dd5fbed9357a47db81ffcf0b359019b87ab0e4d)
#### Sunday 2022-09-11 14:03:04 by I2pRandom

another update to the buttplug item.

this joke has gone beyond a joke to an actual item addition, cus fuck it.
Added the "ONLY_ONE" flag, Removed the cover tag so that it's 'socketless' with (ty Kheir), and finally redefined the description for one that feels better.
still no idea how to apply the 'fun' artifact effect to the item as a stand-in for a custom morale bonus.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[acb4c9934e...](https://github.com/mrakgr/The-Spiral-Language/commit/acb4c9934e4605e1b71fd16c33b8b147ab717be8)
#### Sunday 2022-09-11 14:09:50 by Marko Grdinić

"1:45pm. Just a bit more. Let me have some sweets and I'll start writing chapter 9.

2:10pm. Let me start. Now that I've gotten Patreon and Paypal out of the way I have room in my head for writing again.

Focus me. Also, I think that those triple $ brackets I've been using to open the story parts are in fact something in markdown. Inside them, I put in % everything past that gets colored green. I find this awkward.

Let me use triple exclamation marks for the Spiral parts instead...No wait. Those might get used in the story.

Then how about triple @? That should do fine.

Let me open up chapter 9. I am interested in the intro part so that is what I am going to do. But after that I'll have to think about how I want the story to proceed.

@@@

(Heaven's Key, Inn room)

Back at the inn, I spend some time lying on the bed after the strenuous battle. Earning my first kill made me introspective about my path. I need to think about the future too, so if there is anything I can do to reward myself, it is to give myself some leisure time before the next round of battle. I let the thoughts come to me on their own, and in my loneliness, I imagine Lily, my latest adversary, and Dale's party. They are smiling invitingly, welcoming me into their group and encouraging me to move away from the sinister path that I’ve chosen. In the background, the golden city had a festive and sunny atmosphere, just like the day I spent with Lily before I started to see its shadows.

That has to be a false path. Their smiles are bound to kill me even if they were genuine.

There is really no saving me from becoming based. I learned too much forbidden knowledge on the Internet, I can never go back. That I am in this situation, I can only blame it on my curiosity. The novel worldviews succeeded in winning me over and now I am paying the price for it. The reward is something I'll only get in the future.

For now I have to work towards finishing this scenario of Simulacrum.

Simulacrum has a lot of different scenarios and some are downright mythical. For example, one scenario makes a copy of the real world at that point in time, letting you play in it. I've taken a look and found it in the scenario selector. So if I wanted to, I could play with a simulacra of the real world, except on easy mode or with cheats.

Besides games, the one who made Simulacrum penned numerous stories of the Inspired to immortalize their struggle. There was one story which made a particular impact on me and is related to the ‘Branch of Reality’ scenario. The story starts much like my own, of some guy trying out the brain core and selecting that world copying scenario.

Life is much easier when you have the whole universe helping you, and he immersed himself in that game. At the start of the story he is in his third year of college and middle of the pack, but with the system's help, he goes to the top and stays there. He experiences what it is like to be popular and to have great grades. He gets into a romantic relationship, and after college is done, marries the girl. The job he got afterwards is the one he desired as well. On the game side, with the system's help he attained a happy peaceful life with a woman who loved him.

From the real world side, he is just some nerd immersing himself in games. Whereas at the start of the story he was a normie, after the technology stole his soul, he fell to the bottom, just barely passing his classes. Socialization would take time from his ideal world, so he ignored that. Nobody cared about him either, least of all the girl who pursued him inside the game. He was interested in her and made some awkward attempts to strike up a conversation, but without the flow of events being on his side, he could not get anywhere and got the cold shoulder. The girl that was interested in him when he was popular did not want him in the real world. Having his approaches rebuked was a recurring event in the real world and he coped with it by being successful in the game.

After the college finished he applied to the place he worked in the game. The company did not care about him, and he became unemployed. He applied to other places, but it felt like being a ball on a roulette table, his fate outside his control.

One night while he was getting back from grocery shopping he saw a pair kissing on the street. The woman seemed enamored with the man, and when he looked at her face he realized instantly that it was the girl who so repeatedly rebuked him back in college and the woman who was his wife in the real world. The way she looked at the man was the same way she looked at him in the game.

He said to himself it was not a big deal and went back home.

But back in his room his true feelings came to the fore. Clutching the brain core in his fist and squeezing down on it as if he desired to crush it, his face was a mask of agony as if a dagger had been stabbed through his heart. A streak of tears fell down his cheeks.

"Just why, why is this happening to me? Nothing in the real world ever works the way I want it to."
"In the game, I can accomplish anything I set my mind to, but over here nobody cares about me at all."
"I put so much effort into the game."
"But just why doesn't winning inside it give me any benefit outside?"

It was killing him. In the real world he played games, and inside the game he lived his life. For the first time, he felt that it was unjust. That vibrant fake life he had inside the game, why did it have to come at the expense of his real life? That woman should have been his in both the game and real life! Inside the game the system gave him power, but outside he had nothing to assure himself of victory. He just had to gamble that the talents he got would be enough to take him where he wanted to go. But inside the game only effort mattered.

"I used to laugh at loser nerds back when I was a kid, but look at where I am now?"

For the first time, he understood what it meant to be a nerd. It was not that they were losers, it was much worse. A loser is at the bottom and he knows it. But the nerds have to bear the dissonance of being kings in one place, and slaves in another at the same time, not being able to cast the ambition that tortured them away and having to endure the wait for an opportunity.

In the end, he abandoned the game he was playing. The real world didn't matter to him either, but he didn't want to play that game any longer. Being successful, admired and having a wife inside a game had become mockery to him. People's admiration had become an insult reminding him of the world outside.

He vowed to play in such a way that it would give him power in reality. He changed his attitude towards gaming. He absorbed the forbidden knowledge and started to idealize the power of the machines. Machines aren't limited by talent. Give them a game and they will master it to a level no human is capable of reaching. He went on a journey to make the power of the machines his own and became one of the Inspired. Having a job and a wife inside a game had become absolutely meaningless, but he realized that the algorithms which work inside the game also work in reality. The programs he created inside the game to become his power would also be his power in the real world.

The world quaked. Usually as it happens in such stories, the normies got fucked.

Society took computers far too lightly. At any given point in time, the algorithms might not be good and the hardware might not be there. But the idea of creating a game and having the machine master it is the most powerful there is. It was inevitable that the dissonance between the real and the fake would snap and the nerds would lash out at the world. It was inevitable that the Singularity would happen and that computation itself would take on a divine quality.

I, just like that fictional character, have my chance and am going to make use of it. I am not going to make the mistake of getting attached to game characters. Computer programs are the only true path to power, and that power is the only thing that matters. With power, love and friendship will come easily enough to me should I one day want them. So there is nothing to hesitate about.

@@@

3:50pm. Let me put this into Docs. This is going to be last journal commit on the Spiral repo and the first one on the Patreon blog so I might as well clean it up.

4pm. Done. Goodbye Spiral and hello Patreon.

https://www.patreon.com/simulacrum_post_singularity_story
https://github.com/mrakgr/The-Spiral-Language
https://www.royalroad.com/fiction/57747/simulacrum-heavens-key

If anybody of my Github followers are interested in where my journey leads me from here on out, you know where to find me. Well, either way, I hope you read Heaven's Key."

---
## [nishi88/DataScirenceProjects](https://github.com/nishi88/DataScirenceProjects)@[e34995cb32...](https://github.com/nishi88/DataScirenceProjects/commit/e34995cb32cf6b1a8cc5ea90d80bf2b6a1ed55b6)
#### Sunday 2022-09-11 14:42:50 by Nishi Malviya

Update README.md

The BCG Open-Access Data Science & Advanced Analytics Virtual Experience Program

Welcome to the Open-Access Data Science & Advanced Analytics Virtual Experience Program

We recognise that these tasks are challenging and that there are undoubtedly phrases and terminology you may not have heard before – don’t worry! We have tried to make this experience as true to life as possible and therefore our ask is that you attempt to seek out independent sources of information and do your own research, as required, to help guide you through the tasks.

Welcome to the BCG GAMMA virtual experience! BCG GAMMA is transforming the businesses of today through data science and advanced analytics initiatives and our goal is to help companies generate competitive advantage through these initiatives. This module is designed to give you a feel of what it is like to work at BCG GAMMA as we help our clients using data science.

Our client for this project is PowerCo, a major utilities company. PowerCo has had declining profits due to significant customer churn. We have been engaged to drive churn reduction within their Small & Medium Enterprise (SME) customers.

As a BCG GAMMA Data Scientist, you can expect to work in many different industries, and on many different types of business challenges. The skills you will use and develop today are part of the consultant and data scientist toolkits, and will be applicable to many different types of cases.

We hope you will enjoy your virtual experience and get a glimpse into the exciting life of a Data Scientist at BCG GAMMA!

Tasks
1: Business Understanding & Problem Framing
How to quickly understand the business context

Background information on task 1

PowerCo is a major gas and electricity utility that supplies to corporate, SME (Small & Medium Enterprise), and residential customers. The power-liberalization of the energy market in Europe has led to significant customer churn, especially in the SME segment. They have partnered with BCG to help diagnose the source of churning SME customers.

One of the hypotheses under consideration is that churn is driven by the customers’ price sensitivities and that it is possible to predict customers likely to churn using a predictive model. The client also wants to try a discounting strategy, with the head of the SME division suggesting that offering customers at high propensity to churn a 20% discount might be effective.

The Lead Data Scientist (LDS) held an initial team meeting to discuss various hypotheses, including churn due to price sensitivity. After discussion with your team, you have been asked to go deeper on the hypothesis that the churn is driven by the customers’ price sensitivities.

Your LDS wants an email with your thoughts on how the team should go about to test this hypothesis.

Objectives:

Your first task today is to understand what is going on at the client and think about how you would approach a problem like this to test this specific hypothesis.

Formulate the hypothesis as a data science problem and lay out the major steps needed to test this hypothesis. Communicate your thoughts and findings in an email to your LDS, focusing on the potential data that you would need from the client and analytical models you would use to test such a hypothesis.

We would suggest spending no more than one hour on this task.

Please note, there are multiple ways to approach the task and that the sample answer is just one way to do it.

2: Exploratory Data Analysis & Data Cleaning
Understanding business through data

Background information on task 2

The BCG project team thinks that building a churn model to understand whether price sensitivity is the largest driver of churn has potential. The client has sent over some data and the LDS wants you to perform some exploratory data analysis and data cleaning.

The data that was sent over includes:

Historical customer data: Customer data such as usage, sign up date, forecasted usage etc
Historical pricing data: variable and fixed pricing data etc
Churn indicator: whether each customer has churned or not
These datasets are otherwise identical and have historical price data and customer data (including churn status for the customers in the training data).

We recommend spending no more than 1.5 hours on this task.

Please note, there are multiple ways to approach the task and that the sample answer is just one way to do it.

Objectives:

Sub-Task 1: Clean the data – you might have to address missing values, duplicates, data type conversions, transformations, and multicolinearity, as well as outliers.

Sub-Task 2: Perform some exploratory data analysis. Look into the data types, data statistics, and identify any missing data or null values, and how often they appear in the data. Visualize specific parameters as well as variable distributions.

3: Feature Engineering
Uncovering signals with data

The team now has a good understanding of the data and feels confident to use the data to further understand the business problem. The team now needs to brainstorm and build out features to uncover signals in the data that could inform the churn model.

Feature engineering is one of the keys to unlocking predictive insight through mathematical modeling. Based on the data that is available and was cleaned, identify what you think could be drivers of churn for our client and build those features to later use in your model.

Objectives:

We’ve included some pre-written functions to help you focus on your analysis as opposed to programming syntax.

Sub-task 1: Think through what key drivers of churn could be for our client

Sub-task 2: Build the features in order to get ready to model

4: Modeling & Evaluation
Modeling the problem and evaluating the model

Background information on task 4

Recall that one of the hypotheses under consideration is that churn is driven by the customers’ price sensitivities and that it would be possible to predict customers likely to churn using a predictive model.

The client also wants to try a discounting strategy, with the head of the SME division suggesting that offering customers at high propensity to churn a 20% discount might be effective.

Build your models and test them while keeping in mind you would need data to prove/disprove the hypotheses, as well as to test the effect of a 20% discount on customers at high propensity to churn.

Objectives:

Sub-Task 1: Build churn model(s) to try to predict the churn probability of any customer, taking into account all the explanatory variables you have constructed in the feature engineering process.

Sub-Task 2: Evaluate your model, using a holdout set, and with metrics of your choosing. Be sure to pick a metric that would make sense for this business case.

Sub-Task 3: Interpret the results and use them to formulate your answers to the client’s hypotheses and questions. You will be asked to form these answers into coherent thoughts and recommendations in the next module.

Please note, there are multiple ways to approach the task and that the sample answer is just one way to do it.

---
## [Kubisopplay/Skyrat-tg](https://github.com/Kubisopplay/Skyrat-tg)@[f0ceecff46...](https://github.com/Kubisopplay/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Sunday 2022-09-11 15:05:44 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Kubisopplay/Skyrat-tg](https://github.com/Kubisopplay/Skyrat-tg)@[e7230e8b4a...](https://github.com/Kubisopplay/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Sunday 2022-09-11 15:05:44 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ToppleTheNun/WoWAnalyzer](https://github.com/ToppleTheNun/WoWAnalyzer)@[90c1dd8db4...](https://github.com/ToppleTheNun/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Sunday 2022-09-11 15:20:58 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[9354870474...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/9354870474eaff17302039fc07d6248c9ee5bace)
#### Sunday 2022-09-11 15:34:26 by Mario Kleiner

PsychHID/OSX: Improve macOS security troubleshooting instructions.

Sometimes macOS shitty security GUI lies about the permission status
of "Input Monitoring" etc., and displays Matlab/Octave/Terminal as
on the list and checked, and one does need to do more stupid stuff
like unchecking or rechecking the checkbox. Add comments regarding
this.

---
## [killer7luis/lobotomy-corp13](https://github.com/killer7luis/lobotomy-corp13)@[f0e6476eb0...](https://github.com/killer7luis/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Sunday 2022-09-11 16:04:50 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [isaaguilar/terraform-operator](https://github.com/isaaguilar/terraform-operator)@[779030735a...](https://github.com/isaaguilar/terraform-operator/commit/779030735afb66e6763fa218e3fdb0f2e18b9d28)
#### Sunday 2022-09-11 19:25:12 by Isa Aguilar

New v1alpha2 apiVersion

Many changes in a new api version. Most of the changes are backwards compatible.

**Inroducing v1alpha2**

Changes have been introdced into v1alpha2 to give users even more granularity and options to configure
the workflow tasks (formerly known as runners). Each task container can now have defined container
options, such as labels, annotations, envs and envFrom, and more

Along with the changes to task options, each task is now a stand-alone container in a pod. This
simplifies setting up tasks since there is no sharing of pod configuration aside from the common items,
such as envs, volumes, volume mounts and a few others.

And of the biggest change is that tasks do not have their execution scripts built into the containers
anymore. Instead, tasks will pull their tasks from an http source, read them from a configmap, or
have them defined inline in the tfo resource spec. Why this change? Frankly, it was very hard to
modify the execution scripts becuase they had to be baked into containers. Changing a simple fix
in the task execution meant having to build new images to hunderds of different terraform versions.

I hope that the ability to get the execution script from a source would encourage users to make
changes easily and then contribute back if they feel their changes could benifit the community.

**Migration from v1alpha1**

This is not fun to say, but until v1alpha1 is fully deprecated and removed, a conversion webhook has
been introduced to migrate existing v1alpha1 resources to fit the into v1alpha2. The challenge of
api change was how guarantee parity to a greatest extent. Unfortunately, some features have been made. The
features may be added back as a plugin or a separate controller in the future.

**Conersion webhook**

The conversion webhook is both a blessing and a curse. The beauty of it means users can continue to
use v1alpha1 to create new resources. The ugly part is that is has a rather large operational
burden.

If a user's cluster has cert-manager installed, this really isn't that bad. Otherwise, operators will need
to create ssl certs to secure the webhook endpoints so that kubernetes could communicate with it. It's
probably not as bad as it sounds. I'll document some of the ways to do this.

**Removals**

One such feature that has been removed is exportRepo. This feature, though useful when terraform may be needed
to be run outside of tfo, was always run in the background. This meant it wasn't tracked as
a first-class citizen of the tfo project. A new project might be added to reintroduce this back into
the tfo ecosystem.

---
## [AntiqueAtlasTeam/AntiqueAtlas](https://github.com/AntiqueAtlasTeam/AntiqueAtlas)@[c0da6ad297...](https://github.com/AntiqueAtlasTeam/AntiqueAtlas/commit/c0da6ad297410412666d7b02724f7b0dd700a45a)
#### Sunday 2022-09-11 20:05:56 by tyra314

Fuck you gitignore

No. build.gradle is neither build nor .gradle.
Gosh darn it.

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[6f2354e694...](https://github.com/Imaginos16/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Sunday 2022-09-11 20:30:09 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[e63b5e0675...](https://github.com/crawl/crawl/commit/e63b5e06755426de847c50467f48fc9086cc1eea)
#### Sunday 2022-09-11 20:55:33 by Nicholas Feinberg

Remove Abyssal Knight

Dungeon Crawl once had many, many zealot backgrounds. The dev team
has been steadily moving away from this, because picking a god is a
big, interesting, exciting moment in each game. A zealot start has to
do something really valuable to justify taking that away.

Historically, abyssal knights' big thing was starting in the abyss. This
was a fun little minigame, a bit like delver - the bold could wander a
bit to try to pick up an extra scroll or potion, the reasonable could
race for the exit, and then you could start a normal game. It was a little
taste of something different, especially for newer players.

However, a series of changes have steadily eroded that experience. Items
no longer generate in the Abyss, and you now start on the exit. The correct
move is almost always to hit > immediately. It's a nothingburger. Sad!

Removing Abyssal Knight from the starting backgrounds allows us to make
Lugonu much stronger. Altars to Lugonu scattered around the Abyss are meant
as an incentive to worship, but the consequences of your old god's wrath
are harsh enough that it's rarely right to do so, and it also feels bad -
if you wanted to play a Lugonu worshipper, you'd just start AK! We can now
(in subsequent commits) fix both problems.

Last and certainly least, this means that adding another background to the
centre column of the background picker doesn't add a new row to the display.
:)

Closes #2689.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Sunday 2022-09-11 21:19:50 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

closes odoo/odoo#99458

Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>

---
## [Pale-Jack/horus-heresy](https://github.com/Pale-Jack/horus-heresy)@[26d54434f4...](https://github.com/Pale-Jack/horus-heresy/commit/26d54434f495e6a3b77ab1b3ae097381fd1485eb)
#### Sunday 2022-09-11 21:31:25 by Nikola Beo

WLTs and Shrapnel

[Added]
- Generic WLTs
- Legion-specific WLT placeholders
- WLT SEG added to generics (Praetors, Centurion)
- Graviton and Shrapnel weapons to all relevant models (I'm dead inside after needing to handle such needlessly picky formatting from GW)
- To facilitate Shrapnel Pistols, I added a Bolt Pistol Options SEG to several generic units

[Changed]
- Master of the Legion; now a separate SE that checks for 1 instance per 1k pts
- Added MotL to all relevant characters
- Mandatory generic WLTs handled as links to single WLT rather than SEG (Only done for IW characters, but can easily be duplicated for others)
- Mandatory non-generic WLTs only constrained by Min/Max 1 Warlord (didn't think it was relevant to make their specific WLTs also constrained as only one Warlord can be chosen at a time afaik)
- Reformatted Palatine Blades to fit Tactical template (Min X, decrement X, repeat X for models)
- Reformatted Centurion weapon options to cut down on clutter and bring in line with recent discussions/other entries
- Some fairly serious changes to Veterans to force checks on TLC and basic unit choice. I might honestly suggest formatting them more like Termies; as much I hate how clunky it is, there does not seem to be another way to force model integrity. The other option is completely ignoring the book's format and formatting it the way Recon Squads and several others currently are; please advise.

Pretty sure I missed some Shrapnel/Graviton options in some places, but I'm very tired and can deal with them when someone points them out.

---
## [vamegh/cfn-stack-rename](https://github.com/vamegh/cfn-stack-rename)@[05cfc7ebd0...](https://github.com/vamegh/cfn-stack-rename/commit/05cfc7ebd063ec7e46a8911e67e4e33607fba719)
#### Sunday 2022-09-11 23:09:51 by vam

I believe stack_rename should have all current functionality of index.py

The tool has been pretty much refactored.

aws_handler added the following:

create_changeset
exec_changeset
list_imports
list_exports
delete_stack
waiter

Added all original functions - with a twist

it does not bomb out if it encounters resources that dont support
importing instead it lists them - but currently it is not printing out
this information.

the list_imports should list all of the stacks using the exports created
by the original stack (the code still needs to be written still) will
need to go through each stack that imports the resource and change that
specific import to be the actual value of the resource rather than an
"import" statement - theoretically this could be something random - it
may break the service but it will be temporary.

There is a function: resolvePropertyValue which I believe was originally
intended to go through the template and replace all subs and refs into
other values - however this is not used any where. I have not included
it.

No where in the documentation does it state that using a ref for a
resource that doesnt exist cant be done - I think the deployment may
fail for a new resource being built from scratch, but not for an import.
For the time being however I am not tackling this - this should be
addedjust for keeping thing sane.

I believe as we are retaining resources - if they reference
resources that cannot be retained / imported - the resources will exist
but become broken on the next update however those resources will once
again exist so should work again - this is the theory however
cloudformation is insanely dumb. Why would anyone use this ? Terraform
exists and absolutely destroys this mess of a deployment system. All
this code to rename a stack ?? Why is this not available as a function
without all of this mess - also stack drift what a farsical way of
handling this - aws has apis it can query itself to know the state of
the system - why do we have ito manually run this process ? Why is it not
capable of maintaining its own "drift" status ? Just awful, supremely
awful.

	modified:   libs/aws_handler.py
	modified:   stack_rename

---
## [DunniDee/Project-R](https://github.com/DunniDee/Project-R)@[9399dd164b...](https://github.com/DunniDee/Project-R/commit/9399dd164bffaa93b9dcfa60f4faf40eafa4f2eb)
#### Sunday 2022-09-11 23:18:58 by Noobcoodoocoo

1st and 2nd level tweaks for beter fuck you leroy for loking ov

---
## [EvanWright565/first-Repo](https://github.com/EvanWright565/first-Repo)@[578dedcdfa...](https://github.com/EvanWright565/first-Repo/commit/578dedcdfa997c65267b084c50ea9ae6972c4f8c)
#### Sunday 2022-09-11 23:57:43 by EvanWright565

Create homework 2

The last Lecture 



I found the last lecture to contain a lot of material stated by Randy to allow and welcome a great deal of perseverance and inspiration to be flooded into our mindsets. Going through his childhood dreams was a great way to go about this lecture for that is something nearly every individual on earth has or once had and although that could be used as a way to say something like your dreams are to late and may night come to fruition but yet its as if he's showing you ways that you can now apply to your life moving forward to achieve the goals of the oncoming future no matter the age of the listener. I found the idea of how you say something to someone and word choosing to get the same message across but with different reactions and intentions to be very interesting and made me evaluate how in many situations I may tend to react in a negative light when it could be completely avoidable with my word choice and decision to present myself through to those around me. “If you didn’t get what you want, you’ll still have the experience” was one of the many great quotes that I heard in the lecture that has certainly resonated with me and I will not be forgetting any time soon, it made me go back and remember the concerts i've played or the situations i've endured with spite and understand that there's a bright side to it all and that is the growth and experience from the moments that may be deemed as mistakes or unfortunate. Lastly I found his approach to certain dreams that may not exactly be obtainable to be very humbling with the idea of searching for the next best thing and realizing the significance of that rather than losing yourself in the original dream you so desperately wanted even though it may be impossible

---

