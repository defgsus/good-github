## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-04](docs/good-messages/2022/2022-03-04.md)


1,755,244 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,755,244 were push events containing 2,780,359 commit messages that amount to 193,791,358 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [skyhoshi/bitcoin](https://github.com/skyhoshi/bitcoin)@[619f8a27ad...](https://github.com/skyhoshi/bitcoin/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Friday 2022-03-04 00:01:12 by MarcoFalke

Merge bitcoin/bitcoin#24304: [kernel 0/n] Introduce `bitcoin-chainstate`

2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 ci: Build bitcoin-chainstate (Carl Dong)
095aa6ca37bf0bd5c5e221bab779978a99b2a34c build: Add example bitcoin-chainstate executable (Carl Dong)

Pull request description:

  Part of: #24303

  This PR introduces an example/demo `bitcoin-chainstate` executable using said library which can print out information about a datadir and take in new blocks on stdin.

  Please read the commit messages for more details.

  -----

  #### You may ask: WTF?! Why is `index/*.cpp`, etc. being linked in?

  This PR is meant only to capture the state of dependencies in our consensus engine as of right now. There are many things to decouple from consensus, which will be done in subsequent PRs. Listing the files out right now in `bitcoin_chainstate_SOURCES` is purely to give us a clear picture of the task at hand, it is **not** to say that these dependencies _belongs_ there in any way.

  ### TODO

  1. Clean up `bitcoin-chainstate.cpp`
     It is quite ugly, with a lot of comments I've left for myself, I should clean it up to the best of my abilities (the ugliness of our init/shutdown might be the upper bound on cleanliness here...)

ACKs for top commit:
  ajtowns:
    ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0
  ryanofsky:
    Code review ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0. Just rebase, comments, formatting change since last review
  MarcoFalke:
    re-ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 🏔

Tree-SHA512: 86e7fb5718caa577df8abc8288c754f4a590650d974df9d2f6476c87ed25c70f923c4db651c6963f33498fc7a3a31f6692b9a75cbc996bf4888c5dac2f34a13b

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eeb5465931...](https://github.com/tgstation/tgstation/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Friday 2022-03-04 00:02:21 by vincentiusvin

Ordnance Content Update: Scientific Papers (#62284)

How do I play/test/operate this?

Download NT Frontier on any modular computers. It should debrief you on what experiments are available and how to publish.
If you want to do a bomb experiment, make sure it's captured by the doppler array (as usual) and then print the experiments into a disk and publish it.
If you want to do a gas experiment, make the gas and either pump it into a tank and 1) overpressurize it with a "clear" gas like N2 or 2) overpressurize tanks with the gas itself. Make sure you do the overpressurizing in the compressor machine. When tanks are destroyed/ejected leaked gas will get recorded. Print it into a disk and publish it.
For publication, the file needs to be directly present inside the computer's HDD. This means you need to copy it first with the file manager.
Fill the data (if desired, it will autofill with boiler plate if you dont) and send away!
Doing experiments unlock nodes, while doing them well unlocks boosts (which are discounts but slightly more restrictive) which are purchaseable with NT Frontier.
If you are testing this and have access to admin tools, there are various premade bombs under obj/effect/spawner/newbomb

A doc I wrote detailing the why and what part of this PR.
https://hackmd.io/JOakSYVMSh2zU2YL5ju_-Q

---

# Intro

## The Problem(s)

Ordnance, (previously toxins) seems to lack a lot of content and things to do. The gameplay loop consists of making a bomb and then sending it off for credits or using it to refine cores. Ordnance at it's inception originally relies on players experimenting and finding the perfect mix over multiple rounds, but once the recipe for a "do-everything" mix got out, the original charm of individual discoveries becomes meaningless.

Another issue with ordnance is the odd difficulty curve. As a new player, ordnance is almost impossible to decipher, but once you watch a tutorial or read a wiki and can mail a 50k into space, there pretty much isn't anything else to do. Most players will be satisfied at this point without the gameplay loop encouraging them to understand or play more. The only thing you can do afterwards is to sink your teeth in and understand why that particular mix explodes the way it does. This again has a significant difficulty curve, but if you do that, the department doesn't acknowledge or reward that in any way. There are pretty much two huge spikes, with the latter one not really existing inside the department.

TLDR:
* The content being same-y over rounds.
* Odd difficulty curve: 
    1. A new player is oblivious to everything. 
    2. Those in the middle can repeat the final goal consistently without needing to understanding why
    3. There is nothing to justify spending more time in the department after reaching the midgame.

## Abstract

Scientific Papers aim to add a framework to run multiple experiments in ordnance. Adding more experiments scattered across various atmospheric aspects might allow players of various knowledge levels to still have something engaging to do. A new player should have an easier challange than to mail a 50K. While those that already can make bombs should have an easier time understanding why their bombs explode the way it does. Once they fully understand why, they can set their sights on taking advantage of another reaction to set their bomb off or hone one particular reaction down.

## Goals

* Have some intro-level challanges for new players.
* Have some semblance of late-game challanges for more experienced players.
* Explain the mechanics better for those in the middle of the road.
* Incentivize trying new things out in the department.
* Better integrate Ordnance with Experisci

## Boundaries / Dont's

* Do not incentivize people to learn ordnance by using PvP loots.
* Do not shake or change the reaction system by a huge amount.
* Disincentivize having a single god-mix that does everything.
****

# Main design pillars

## A. Framework surrounding the experiments

### A.1. New experiments

Add new experiments to the ExperiSci module. These will come in two flavours: New explosions to do, and various gas synthesis experiments. Both of these are actually supported by the map layout of ordnance right now, but there is no reason to do anything outside of making a 50k as fast as possible.

### A.2. Rewards for experiments: Cash and Techweb Boosts.

Scientific papers will add a separate experiment handling system. A single experiment will be graded into various tiers, each tier corresponding to the explosion size or amount of gas made.  Doing any tier of a specific experiment will unlock the discount for that specific reactions. A single explosion **WILL NOT** do multiple experiments (or even tiers) at once.

On publication, a partner can be selected. A single partner only has a specific criteria of experiments they want. The experiments will then be graded on "how good they are done", with the criteria being more punishing as tier increases. Publication will then reward scientific cooperation with the partnered partner. Players can spend this cooperation on techweb boosts. Techweb boosts are meant to be subservient to discount from experiments and will not shave a node's price to be lower than 500 points.

**Experiments will only unlock nodes, discounts are handled through this boost system.**
This is more for maintainability than anything.

### A.3. On Tedium

*This is a note on implementation more than anything, but I think this helps explains why several things are done.*

Due to the nature of atmospheric reactions in the game (they're all linear), tedium is a very important thing to consider. An experiment should have a sweet spot to aim for, but there should not be a point where further mastery is stopped dead on it's track with a reward cap.

Scientific Papers attempts to discourage this behaviour by having the "maximum score" scale off to infinity but with the rewards being smaller and smaller. The sweet spot is always there to aim for and should be well communicated with players, but on their last submission of an experiment topic players should be encouraged to do their best. There should always be a reward for pushing the system to it's limit as long as it doesn't completely nullify the other subdepartments. This is the reason why there is a hard limit on the number of publications and why the score calculation is a bit more complex than it needed to be.

## B. Gas Synthesis (Early-Mid Game)

Scientific papers will add one new machine that requests a tank to release x amounts of y gas. This will be accomplished by adding a tank pumping machine which will either burst or explode a tank, releasing the gas inside. The gas currently requested are BZ, Nitryl, Halon and Nob.

The overarching goal of this compressor machine is to present a gas synthesis challange for the players and to get them more accustomed to how a tank explodes. The gas synthesis part can always be changed in order to reflect the current state of atmospheric reactions.

## C. Explosion Changes (Mid-Late Game)

### C.1 Cause and effect.

The main theme of the explosion changes is establishing cause and effect of explosions. Reactions that happens inside a tank that's going to explode will be recorded and forwarded to a doppler array. Some experiments will require only a single cause to be present (think of it as isolating a variable). This is currently implemented for nobliumformation and pressure based bombs. Having other reactions occuring besides noblium formation will fail the first one, while having any reactions at all will fail the second one. 

Adding more explosions here will be a slight challange because as of now the game has only two reactions that can reliably make an explosion.

### C.2 Tools upgrade.

Doppler array has now been retrofitted to state the probable cause of an explosion, be it reactions or just overpressurization on gas merging. These should help intermediate players figure out what is causing an explosion.

Added a new functionality to the implosion compressor:
Basically performs the gas merging and reaction that TTV does in a machine and reports the results back as if someone uses an analyzer on them. Here to give players feedback so they can try and understand what is actually going on in a bomb.

## D. Player Interaction

There should be more room for more than 1 player to play ordnance simultaneously. Previously players are also able to split tasks, but this rarely happens because tritium synthesis needs only the gas chamber to be reconfigured. Now, different players can pick different experiments and work on them. Players can also do joint tasks on one single experiment. Gases like noblium will need tritium production and also a cooling module online.

Ordnance can also coordinate with their parent department on what they really need, be it money or research bonuses.

# Potential Changes

The best-case changes that can be implemented if the current roster of content isn't enough is more reactions that can be used in bombs. Eliminating bombs entirely goes against the spirit of the subdepartment, while adding new ones will need a lot of care and consideration.

Another possible change is to implement a "gas payload" bomb. Bombs that has a set number of unreacting gas inside that will increase the heat capacity, reduce the payload, and neccesitates more bespoke mixes.

Adding more gas synthesis experiments is discouraged. The main focus of ordnance should be bombs, with gas synthesis being a side project for ordnance. These are present to ease the introduction to bombs and provide some side content. 
There should be a somewhat well-justified goal in adding new synthesis experiments: e.g. BZ is there as a "tutorial" gas, Nitryl to introduce players to cooling/heating mixes, Halon to a more efficient tritium production, and Nob as a nudge to nobformation bombs and mastery over other aspects.

# Conclusion / Summary

Add more experiments to ordnance that players can take, accomplish this by:
1. Making the players perform gas synthesis or make bombs.
2. Have them collect the data, see if it fits the criteria. Explain why if it fits and why if it doesn't.
3. Have the player publish a paper.

Reward them based on how well did they do, give players agency both on the experiment phase and also publication phase.


---
TLDR: Added new experiment to toxins, added the framework for those experiments existing. Experiments comes in gas synthesis and also bombs but with more parameters. Experiments needs to be published through papers, various choices to be made there.

Implementation notes:

Because of how paper works, ordnance experiments are handled outside of experiment_handler components. My reasoning for this is twofold:

The experiments will be completed manually on publication and if the experiment isn't unlocked yet it will still be completed.
Experiment handler datums have several procs which require an atom-level parent, and I figured this is the most sensible and cleanest way to implement this without changing the experiment handler datum too much.

Small change to /obj/machinery/proc/power_change() signal ordering to adjust the state first and then send the signal. Didn't found any other usage of this signal except mine but barge down my door if it broke something.

Rewrote the ttv merge_gases() code to be slightly more readable.
A small code improvement for thermomachine to use tofixed (my fault).

Ordnance have been updated to enable the publication of papers
Several new explosive and gas synthesis experiments have been added to ordnance
Anomaly compressor has been TGUIzed and now supports simulating the reaction of the gases inside the ttv.
New tank compressor machine for toxins. You can overpressurize tanks with exotic gases and complete experiments.
Several techweb nodes are locked and require toxin experiments to complete.
Toxins can purchase boosts for various techweb nodes.
You no longer need to anchor doppler arrays for it to work.
Doppler array and implosion compressor now supports deconstruction, implosion compressor construction added.
Doppler now emits a red light to denote it's direction and it being on. Doppler not malf.
Implosion compressor renamed to anomaly refinery.
Created a new program tab "Science" for the downloader app. Removed Robotics.
Reworked the code for bombspawner (used in the cuban pete arcade game)

---
## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[11d3ea66af...](https://github.com/rorydale/pointbreakradio/commit/11d3ea66afb3e37c781bb742dc0143693a78b4bd)
#### Friday 2022-03-04 00:15:31 by Rory Dale

2022-03-03

Thursday, March 3rd, 2022 - the early 00s alt rock, pop, and a little emo show! I was in a Jack Johnson mood this morning, but it's not always possible to stretch a vibe across a two hour show so I had to widen the criteria a little. Given as I played new music from Dashboard Confessional yesterday, if I went back to their early albums, that aligned perfectly with Jack, and placed me in the early 00s. There was a lot of great music for me at that time, and it was a great time in my life too, so as I continue to use music as an escape, it felt like the right year to travel back to tonight.

---
## [dmitryvinn/pyre-check](https://github.com/dmitryvinn/pyre-check)@[bc0ea7cd46...](https://github.com/dmitryvinn/pyre-check/commit/bc0ea7cd46402fe4c5ee5405a048a8ab676ad081)
#### Friday 2022-03-04 00:16:30 by Shannon Zhu

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
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[4051ad647e...](https://github.com/DesmontTiney/tgstation/commit/4051ad647e3e94ea5c722cee18cecf350270ab6f)
#### Friday 2022-03-04 00:54:03 by LemonInTheDark

Space drifting fixes and cleanup (#64915)

* Fixes infi pushing off something in space

Right now you can just push "into" a dense object forever, and depending
on your move rate, just kinda glide

We can fix that by checking if we're trying to push "off" something
we're moving towards

* Makes pushing off something shift it instantly

Currently if you kick off something in space it waits the delay of the
move to start drifting. Looks dumb, let's not

* Updates backup movement to properly account for directional windows. GOD I HATE DIRECTIONAL DENSITY SHOOOOOT MEEEEEEEEEEEEEEEEEEE

* Uses range instead of orange so standing on the same tile as a directional counts properly, rather then suddenly entering a drift state. I hate it here

* Ensures all args are named, updates implementations of the proc with the new arg

---
## [Kurgis/tgstation](https://github.com/Kurgis/tgstation)@[6ed2fafd4e...](https://github.com/Kurgis/tgstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Friday 2022-03-04 01:33:32 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to)@[5293b63553...](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to/commit/5293b63553020b051ef7d2b55429402caa8cea17)
#### Friday 2022-03-04 01:45:52 by Maciej Żenczykowski

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
## [oddtiming/push_swap](https://github.com/oddtiming/push_swap)@[8659551ce7...](https://github.com/oddtiming/push_swap/commit/8659551ce73ba715ede2f214eea5bce86032082a)
#### Friday 2022-03-04 01:48:45 by Ismael Yahyaoui Racine

I believe I know what the fuckup was

I had my optimization flag set to -O3, which I believe can cause some wonky behaviour when some code is misaligned. Don't quote me on that.
I'll set it to -O2 for now, and see what gives, and at the end if I still have time and energy for it, I'll do some optimization of my own to make -O3 work

Forgot to mention that one of the fixes that I did for my previous bug of misadressed function pointers
was to malloc my main container, which fixed some of the issues.

The logic now works, just need to properly update the biggest/smallest position iterators on push in a subfunction, and we're good to actually start the sorting process, lol

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[e8bc28a0cf...](https://github.com/Mu-L/crawl/commit/e8bc28a0cf5eb223156f893c8f47b1284931e78a)
#### Friday 2022-03-04 01:59:26 by DreamDust

vaults: float vaults by DreamDust

dreamdust_dug_too_deep

The dwarves dug a little too deep and unearthed... a Balrug! Even a
mighty dwarf hero (with a potentially good weapon to loot!) fell in
battle to the demon. RIP. Maybe this is why we don't see deep dwarves
much anymore. Hmmmm...

The idea behind this vault is to place a single Balrug early enough that
it's a serious (but not unmanageable) threat. I added a downhatch close
by if players need to escape in a hurry. There are also warning signs in
advance (all the dwarf corpses and the suspicious volcanic floor tiles
outside the Balrug room).

[ Committer's note: Added a runed door for the balrug, adjusted
  transparency, traded volcanic floor for blood. ]

dreamdust_wu_jian_sword_trials

A Wu Jian-themed vault. Challenge three increasingly powerful
sword-wielders for their increasingly good swords.

[ Committer's note: Adjusted depth range, added monsters to the earlier
  trial, trimmed arenas, added transperency. ]

dreamdust_merry_men

Inspired by Robin Hood and his band of merry men. Features a forest with
a bunch of archers and a good bow and aides to banditry to loot in the center.

[ Committer's note: Adjusted layout to prevent teleport closets, monster
  counts, loot. ]

dreamdust_tengu_aerie

A large nest of tengus. They keep their shiny loot in the center...
along with their fledglings (wait, are we the baddies??).

[ Committer's note: moved the crystal walls to the middle, put the
  rock wall on the outside (so the reavers can bolt bounce their
  omnibolts), and thinned the monster density. ]

dreamdust_hydra_shepherd

A shepherd is raising a flock (?) of hydras down in the Depths! Some
players might regret abandoning their flaming weapons after finishing
Lair/Swamp, haha.

[ Committer's note: upgraded the cyclops to a stone giant, added a small
  chance for a really high head count. ]

dreamdust_elfheim

The home of Duvessa and Dowan.
The more-practical Duvessa has training dummies in her room, while the
vain Dowan has a large mirror to admire himself with.

[ Committer's note: cut down on custom tiling/colouring a bit. ]

---
## [Neternels/android_kernel_samsung_universal7580](https://github.com/Neternels/android_kernel_samsung_universal7580)@[54d9ac0b07...](https://github.com/Neternels/android_kernel_samsung_universal7580/commit/54d9ac0b07976153e8616947de88dc91241139d0)
#### Friday 2022-03-04 02:19:38 by Masahiro Yamada

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
## [MacBlaze1/tgstation](https://github.com/MacBlaze1/tgstation)@[3bd5a2d8df...](https://github.com/MacBlaze1/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Friday 2022-03-04 02:33:08 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [ne3lob/GEOLOGY](https://github.com/ne3lob/GEOLOGY)@[790f20f1e7...](https://github.com/ne3lob/GEOLOGY/commit/790f20f1e781c259977664da38c241476b7f74fc)
#### Friday 2022-03-04 02:57:05 by bapek

Some Fixes and Cave Walls,Button

Warja,

I changed the buttons' places to the bottom, because otherwise they are too close and create desire to push just for curiousity, but I might accidentally fucked up the first level's length, can you check it?

Also I changed the platform's place in 3rd level, because it was creating some vulgar scenes like buildings are beating you after some time. I tried to stay longer in the other one and looks unproblematic for now.

Caves' walls are closer to each other now, but maybe can be smaller as length since it might me klostrophobic for some people now. Also added the button for cave.

Hope you see this in the morning, good night! And then we can build,

---
## [trrapp12/React-Jokes](https://github.com/trrapp12/React-Jokes)@[f119018f4b...](https://github.com/trrapp12/React-Jokes/commit/f119018f4b56b616647ed862df728ea9f3fd52e7)
#### Friday 2022-03-04 04:02:16 by Trevor Rapp

adds more jokes, puts them in the form of an array that is then imported in, uses map() to iterate through each JSON object and print it as JSX, then also adds logic that when you 'hover' over the container the joke and the meta data reveal themselves.  Yeah, and this is only one commit for a whole day of work.

---
## [asuka-mio/android_kernel_xiaomi_cas](https://github.com/asuka-mio/android_kernel_xiaomi_cas)@[f24f51f0db...](https://github.com/asuka-mio/android_kernel_xiaomi_cas/commit/f24f51f0db15fd48a0ca2c23faa59ab6a6817409)
#### Friday 2022-03-04 04:24:04 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Forenche <prahul2003@gmail.com>

---
## [lsw3961/PixelArtPipeline](https://github.com/lsw3961/PixelArtPipeline)@[7b5127390b...](https://github.com/lsw3961/PixelArtPipeline/commit/7b5127390b6e61891c054204cb87b864a59a18c8)
#### Friday 2022-03-04 04:59:37 by Logan White

3 new animations

god bless this render pipeline, it honestly has been the biggest lifesaver in terms of time and animations. Now if I want an animation I just render the model here and badabing I now have a sprite sheet.

---
## [Evolution-X-Devices/kernel_oneplus_sm8250](https://github.com/Evolution-X-Devices/kernel_oneplus_sm8250)@[c748ae1d8a...](https://github.com/Evolution-X-Devices/kernel_oneplus_sm8250/commit/c748ae1d8a9d722e252d2f63b7b6cf3e6ed5b430)
#### Friday 2022-03-04 05:56:32 by alk3pInjection

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
## [Kaz205/renoir](https://github.com/Kaz205/renoir)@[f5cbad3840...](https://github.com/Kaz205/renoir/commit/f5cbad38403eb99fb6d30e99077e25dce1577ea8)
#### Friday 2022-03-04 06:37:29 by Peter Zijlstra

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

---
## [Mezque/Trolly](https://github.com/Mezque/Trolly)@[a163d4c53f...](https://github.com/Mezque/Trolly/commit/a163d4c53f517ce3ac51f683aace586df3c8243b)
#### Friday 2022-03-04 07:11:39 by Royal

PEOPLE ARE WEIRD I HATE PEOPLE STUPID SHIT POST HHAHAHAHAHAHAHAHAHAHAHAHAHA

---
## [log1cs/alice_lge_sdm845](https://github.com/log1cs/alice_lge_sdm845)@[635a61c63f...](https://github.com/log1cs/alice_lge_sdm845/commit/635a61c63fc0bdf989a03025050b333e1c0ea662)
#### Friday 2022-03-04 08:38:06 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Friday 2022-03-04 09:12:44 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [Jay1Koding/react-for-beginners](https://github.com/Jay1Koding/react-for-beginners)@[4792738369...](https://github.com/Jay1Koding/react-for-beginners/commit/4792738369e5a8a5957a536e45b3faf4e610eeac)
#### Friday 2022-03-04 09:13:53 by jay1coding

fuck this package fuck you all fuck this shit im so stupid as fuck

---
## [egor-tensin/wireguard-config](https://github.com/egor-tensin/wireguard-config)@[4013056d5b...](https://github.com/egor-tensin/wireguard-config/commit/4013056d5b6cf8ab83cdda9391acc5e4d4ba90e9)
#### Friday 2022-03-04 09:18:04 by Egor Tensin

bundle ip-address (to be used instead of ipaddr.js)

This fucking sucks ass, but ipaddr.js is buggy:

    https://github.com/whitequark/ipaddr.js/issues/160

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[b1ace967a2...](https://github.com/microsoft/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Friday 2022-03-04 11:56:15 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[1b9c50e2ae...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/1b9c50e2ae1e5fca135e24e11a8bdf0012f89563)
#### Friday 2022-03-04 12:05:36 by AmCath

My love for the whole "Spooky" portrait thing stems, I think, from a love of the old stuff KR used to do. Not to get all "SOVL KINO OLD GOOD NEW BAD," but the stuff like the old Halloween stuff, or the Christmas updates or hell even the ancient April fools thing that KR got rid of a while back was and still is super cool. It represented a different time, the old wild west days I guess. One of my fav things about working on KX is the fact that that attitude and style lives on.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1a00db1f6b...](https://github.com/mrakgr/The-Spiral-Language/commit/1a00db1f6b10d4ea243b8c2ae5dd1c64cb4a742a)
#### Friday 2022-03-04 12:20:55 by Marko Grdinić

"10:35am. Let me chill just a bit more and I will start. I got up 10m ago.

11:10am. Done chilling, it is time to start. It is Houdini time for me. Did I get a reply to that .rat question?

Nope. Nwm.

Now I can go for the V-Ray volume shading tutorial and try messing with displacement, but let me go through the official V-Ray tutorials first.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+for+Houdini+Help

https://forums.chaos.com/

Let me start going through these. They even have a forum.

https://www.youtube.com/watch?v=XvTQeP3Lm2s
V-Ray 5 for Houdini, update 2 — How to create and render white hair.

Let me start with this.

https://youtu.be/XvTQeP3Lm2s?t=105

This is a pretty nice looking bear.

https://youtu.be/myg-VbapLno
Render engine speed comparison

Let me watch this.

https://youtu.be/myg-VbapLno?t=111

This guy has such great video composition. He told me it took him 2 years to make this benchmark.

https://youtu.be/myg-VbapLno?t=329

I am probably using the V-Ray in its default setting. I'll have to check out how to use that secondary solver.

https://youtu.be/myg-VbapLno?t=352

Wow the GPU sure makes a difference. Note that they were using RTX 3090 so the results for me would be quite worse.

https://youtu.be/myg-VbapLno?t=469

Redshift is really fast.

https://youtu.be/myg-VbapLno?t=500
> Cycles is unreasonably slow at volumetrics.

https://youtu.be/myg-VbapLno?t=539

This scene has IES lamps. I guess that tells me what those lights are. Given that it does not work for me, I wonder if there is something wrong with my V-Ray install. I absolutely need to get them working.

https://youtu.be/myg-VbapLno?t=246

I'll have to take a look at how to turn on the light cache.

Ah, the option is in Renderer -> Global Illumination -> Light Cache. It is on by default. Ok, good.

Redshift is really good at volumetrics, but V-Ray itself took the win at the all rounder test.

12:05pm. That was pretty interesting. I actually like and subscribed. Andrew Price really knows his stuff.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+for+Houdini+Help

Now let me focus on the stuff here.

https://docs.chaos.com/display/VRAYHOUDINI/Lights

Let me start with lights. I am surprised it has a sphere light. I do not see that one in the shelf. Let me try it out. After that I'll read up on the IES light to see why it is giving me so much trouble.

Wow, if you press shift, you can actually move in the IPR.

Though the functionality is limited. It is also difficult to control the focus.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+IES+Light

> Photometric lights utilize an .ies file which contains the distribution profile for the light. An .ies file contains complete specifications of a real world light bulb or tube including the shape of the light's cone and the steepness of the light's falloff. Such files are usually provided by the manufacturer of the real-world bulb, and the information in those files, gathered through lab experiments, is extremely accurate in its representation of the light source. By loading an .ies file, the light's properties are recreated within Houdini and used by V-Ray during rendering.

Maybe I need that IES file from somewhere.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Mesh+Light

> The V-Ray Light Mesh can create light sources that have volume and shape without the need to use self-illuminated objects and global illumination.

> If the V-Ray Light Mesh is close to other surfaces in the scene, it is best to use it with GI enabled so V-Ray can use combined direct and GI sampling of the mesh light. Without GI, the light might produce noisy results for surfaces that are very close to it.

Let me give this one a try. I do not like how slow and noisy self illumination is on objects. This might work better.

12:30pm. Mesh light works way better.

Now let me try instancing these lights.

12:35pm. Nope, the light is attached to the object itself rather than geometry.

Another option I should look into is light materials.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Sun+Light
> The V-Ray Sun and V-Ray Sky are special features which are provided by the V-Ray renderer. Developed to work together, they reproduce the real-life sun and sky environment of the Earth. Both are coded so that they change their appearance depending on the direction of the V-Ray Sun.

Oh, the sun light really is the sun.

What is V-Ray Sky? I have no idea, I can't find the V-Ray Sky node.

> Sky Model – Determines the procedural model used to generate the V-Ray Sky texture:

12:40pm. It is in the Sun light.

Ok.

12:45pm. https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Sun+Light

These docs are very well made. They have interesting examples.

> By default, the VRaySun and VRaySky are very bright. In the real world, the average solar irradiance is about 1000 W/m^2 (see the references below). Since the image output in V-Ray is in W/m^2/sr, you will typically find that the average RGB values produced by the sun and the sky are about 200.0-300.0 units. This is quite correct from a physical point of view, but is not enough for a nice image. You can either use Color Mapping to bring these values to a smaller range (which is the preferred way), or you can use the Sun's Intensity multiplier to make the sun and sky less bright. Using the V-Ray Physical Camera with suitable values also produces a correct result without changing the sun and sky parameters.

What is that `/sr`?

Well, no matter, I'll just use the physical camera like they suggest.

12:55pm. https://docs.chaos.com/display/VRAYHOUDINI/What%27s+New+in+V-Ray+5

///

V-Ray Material Library
Efficiently browse from a library of over 500 render-ready materials including metals, glass, wood and more.

Coat layer
Add reflective coatings directly in V-Ray Material so you can render faster and more efficiently.

Sheen layer
Render soft microfiber fabrics like velvet, satin and silk with new V-Ray Material sheen options.

Randomized textures and colors
For more realistic textures and materials, add variety and subtle imperfections with the new VRayUVWRandomizer map and improved VRayMultiSubTex controls.

Stochastic texture tiling
Automatically remove texture tiling artifacts with the new Stochastic tiling option on the VRayUVWRandomizer.

Dirt and weathering
Give surfaces a weathered look. With the improved V-Ray Dirt texture, you can add dirt to cracks and crevices, create procedural streaks, or cover an entire surface.

New Sun and Sky model
A new Sun & Sky analytical model is more accurate and improves lighting at sunrise and sunset.

///

These weathered textures are of interest to me! I had no idea something like this was possible. Getting that effect was in fact one of my goals.

1pm. https://docs.chaos.com/display/VRAYHOUDINI/What%27s+New+in+V-Ray+5%2C+update+2

Curvature textures?

1:05pm. I have my goal. I need to master V-Ray. If it takes a month or two that is fine. I need to dive deep into it and get familiar with each of its nodes. Once I have that I'll have a powerful ability at my disposal.

Right now the scene looks amateurish, but if I could put in proper lighting and texturing it could really come to life.

1:05pm. The amout of nodes is not too big. I can justify taking the time to go through the entirety of the documentation at some point. But for now I think I'll just go through the video tutorials on Youtube. There aren't many V-Ray specific ones, but triangulating the Mantra one in V-Ray seems like an ideal exercise. I need to go through it and build up my familiarity step by step.

1:15pm. I might have started the art journey in Oct 2021, but Houdini in effect restarted my learning curve so I am 1.5 months in. It might have been better to start learning Houdini from the beginning. At any rate I do not care.

There was never really a hope to master art quickly. If it takes me a year that is fine. Eventually I'll cover all the ground that I need and will be able to stand on my own two feet by the end of it.

Potentially, I could ignore music if art turns out to be too time consuming. The visuals take clear priority. But that won't come to pass. I'll master art, and then move on to music.

The Houdini path is just so involved and full of details. it is very hard to internalize due to the sheer quantity of information that I need to process. But is not something that will take forever. I will adapt and prosper.

Now let me have breakfast here."

---
## [gregalmundo/Emeralds](https://github.com/gregalmundo/Emeralds)@[3c6dcdba88...](https://github.com/gregalmundo/Emeralds/commit/3c6dcdba880b5b711563fa92b4e894913378743d)
#### Friday 2022-03-04 12:48:31 by gregalmundo

Update and rename README.md to READMEhasSmallInfo.md

At school
Lucas goes to school every day of the week. He has many subjects to go to each school day: English, art, science, mathematics, gym, and history. His mother packs a big backpack full of books and lunch for Lucas.

His first class is English, and he likes that teacher very much. His English teacher says that he is a good pupil, which Lucas knows means that she thinks he is a good student.

His next class is art. He draws on paper with crayons and pencils and sometimes uses a ruler. Lucas likes art. It is his favorite class.

His third class is science. This class is very hard for Lucas to figure out, but he gets to work with his classmates a lot, which he likes to do. His friend, Kyle, works with Lucas in science class, and they have fun.

Then Lucas gets his break for lunch. He sits with Kyle while he eats. The principal, or the headmaster as some call him, likes to walk around and talk to students during lunch to check that they are all behaving.

The next class is mathematics, which most of the students just call math. Kyle has trouble getting a good grade in mathematics, but the teacher is very nice and helpful.

His fourth class is gym. It is just exercising.

History is his last class of the day. Lucas has a hard time staying awake. Many lessons are boring, and he is very tired after doing gym.

---
## [Eism/MuseScore](https://github.com/Eism/MuseScore)@[cd92ec6f01...](https://github.com/Eism/MuseScore/commit/cd92ec6f01c3f7510f5a645703fa1abceea320df)
#### Friday 2022-03-04 12:54:28 by Marc Sabatella

fix #276141: no space for lyrics in continuous view + collect_artifacts

Resolves: https://musescore.org/en/node/276141

A common complaint since the release of MuseScore 3 is
that we no longer allocate additional space between staves
for lyrics and other elements above/below the staff,
when in continuous view.
That's because these calculations in page view can be optimized
so they only need to be done for affected systems on each layout.
In continuous view, there is only one system,
so it would mean a full layout, which is very slow.
But MuseScore 2 did this, and people writing vocal music especially
were accustomed to this automatic staff spacing.
Since lyrics were about the only thing that did this spacing,
it wasn't as expensive as it would be using MuseScore 3 autoplace.
And yet, MuseScore 2 was extremely slow with large scores,
because it lacked any range optimizations, even in page view.

This change finds a compromise that should work well.
On the initial layout in continuous view, we do build a full skyline,
so it is easy enough to add space for each staff then,
and any performance penalty is paid only at that time.
Any extra space needed for this is remembered for subsequent layouts.
On future layouts, we do use a range, so we only have a partial skyline.
The code here calculates the space needed just within the current range,
but it also compares this with the remembered value,
so uses whichever is larger (and remembers this new value if different).

The result is that the spacing is correct when first opening the score,
or when first switching to continuous view.
After that, any edits that *increase* the required space
(such as adding a new verse of lyrics)
will do so as expected.
If you later make a change that reduces the amount of space requires,
we cannot reclaim that space, since a full layout would be required
in order to detect that we truly don't need the space anywhere.
But you can always reclaim it by switching to page view and back.

The code to do the partial skyline comparison is not free,
but it happens only once per staff per layout,
so in theory it should have a negigible effect on performance.
If this assumption turns out to be wrong,
we can switch to the code that skips the partial skyline comparison
except on the initial layout.
This is included but ifdef'ed out.

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[c62bef2e15...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/c62bef2e15ee82b7f676d8475cc60006c9d84ae7)
#### Friday 2022-03-04 13:40:09 by Abhishek Shrivastava

AWS Community Builders 2022-23

I am super thrilled and honored to be officially declared as an Amazon Web Services (AWS) Community Builder. 



The Amazon Web Services (AWS) Community Builders program offers technical resources, mentorship, and networking opportunities to AWS technical enthusiasts and emerging thought leaders who are passionate about sharing knowledge and connecting with the technical community.

 

In this program, my primary category will be Containers.



Atos is a "Great Place to Work" where you get inspired and supported to achieve goals!



I also want to thank AWS Community Builders Team Shafraz Rahim , Jason Dunn , #awscommunitybuilders who selected me for this!



Please follow me on below channels ::



GitHub :: https://lnkd.in/dHAMiTcH

Hashnode :: https://lnkd.in/dh3SYw4t

Twitter :: https://lnkd.in/d-_g9UrF



Address my mentor Mahesh Bhosale, who always treat me like his small brother and being a leader who is not only Bossy nature even he treat all juniors his good friends at every level ..



CC- Adding my leaders and colleagues to share achievement::

Pritish Kumar Swapneel Doshi Girish Chhabra Luis Méndez Osvaldo C. Jason Chance Anji Reddy Venumula Naman Kher Gary Bowers Susan Cutinha Murli Reddy Rakesh Khanna Sohil Shah Kaviarasu Subramaniam PMP CSM SAFe 4 Certified Agilist Anujj Jain PgMP®,PMP®, Prince2 Agile, CSA, ITIL EUR ING Ioannis Kolaxis MSc Vijay Bijjargi Chris Broccoli Dinesh Damodaran Janarthanan Selvaraj Atos Atos Digital Security Rajeev Choudhary



Thanks to my motivators who always encouraged me with their achievements --

Yongkang ⎈ ☁️ HE Yujun Liang ⎈ ☁️🇺🇸  Konrad Cłapa, Google Cloud Certified Fellow  Denise Reed Lamoreaux Sathya Prasad Nanjundaiah Satyen Kumar Sophie Proust Dan Rey, MVP Deepak Rajendran



#aws #security #amazon #team #community #networking #awscommunity #awscommunitybuilders #opportunities2022 #mentoring #learning #atos Atos Digital Security Atos

---
## [GregAC/ibex](https://github.com/GregAC/ibex)@[c15f3b8888...](https://github.com/GregAC/ibex/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Friday 2022-03-04 13:58:17 by Rupert Swarbrick

[icache] Define some fake DPI functions to simplify linking

This is triggered by the fact that if the ICache parameter is false
then we don't instantiate the ibex_icache module. For verilator
simulations, the module is then discarded entirely, which means that
its two DPI functions are not defined. That's unfortunate because
we're also compiling the code in scrambled_ecc32_mem_area.cc, which
expects the functions to be defined.

The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
don't have an icache) isn't easy to do, because FuseSoc doesn't
currently allow us to use parameters to configure its dependency
tree (see fusesoc issue 438 for a discussion).

The super-clever solution that I came up with before(!) was to declare
these symbols as weak in the C++ code. That way, we can do a runtime
check to make sure that no-one is silly enough to call them without an
icache, but everything will still build properly either way.

Unfortunately, that doesn't work well with xcelium simulations.
Xcelium turns out to compile all the C++ code into one .so library and
generate functions for exported DPI functions in another. These two
solibs then get loaded at runtime with dlopen(). But this doesn't work
with weak symbols: in fact, it seems you end up with the C++ version
every time. Boo!

So let's be stupider about it and define (bogus) versions of the DPI
functions in this case. Fortunately, both of them are designed to
return zero on failure so we can just return zero and needn't worry
too much.

The idea is that when this lands, we can revert the OpenTitan change
that switched the C++ code to using weak symbols and Xcelium
simulations will start working.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[42b5882be5...](https://github.com/kleinesfilmroellchen/serenity/commit/42b5882be55f4e4b0e0b96af3ddd5a2926090a8c)
#### Friday 2022-03-04 14:03:53 by kleines Filmröllchen

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

Known issues/exposed bugs:
- Two processes running audio enqueues at the same time will pin the CPU
  at 100% due to both of them yield()ing all the time. See #12679.
- AudioServer hangs in driver after changing sample rate. (Probably
  already an issue before these changes.)
- SoundPlayer's BarsVisualization doesn't draw anything until you switch
  to another visualization and back again.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[41ba81e876...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/41ba81e876ca25ec23b98bb8ee7c110fa0800970)
#### Friday 2022-03-04 16:40:05 by Cyber Knight

kramel: Switch to LLVM Binutils for {AR, OBJDUMP, STRIP}

- GNU Binutils seem to break compilation hence let's switch to LLVM Binutils.
- Fuck you GNU.

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1d0fcfe792...](https://github.com/mrakgr/The-Spiral-Language/commit/1d0fcfe7922fa17132a098b33bf79d38b02a433c)
#### Friday 2022-03-04 18:51:06 by Marko Grdinić

"2:05pm. Right now I am having breakfast.

https://docs.chaos.com/display/VRAYHOUDINI/What%27s+New+in+V-Ray+5%2C+update+2

* Enhanced ACEScg support

I am looking at the stuff here. Just what is this ACES thing? I'll have to look into it.

* VDB to AUR converter

> Chaos Phoenix’s Aura files are rendered faster with V-Ray. A new node makes it easy to perform a quick conversion from VDB to Aura right in the Houdini GUI. See V-Ray Aur Convert

V-RAy was slower than Redshift for volumetrics by a significant margin. Maybe if they converted it to Aura things would have been different.

2:35pm. https://docs.chaos.com/display/VRAYHOUDINI/Interactive+Rendering

> V-Ray for Houdini supports interactive rendering in Houdini's Render View. To benefit from this feature, go to Render View > Render button.
> Note that the Use V-Ray Frame Buffer option must be disabled.

Oh, this is something that I want. Maybe it opens the IPR because I did not disable the Frame Buffer. Where can that be done?

2:40pm. This is great. Maybe I should find a way to set up a hotkey to switch between the two views. Either way is fine.

Let me resume for real. I chilled for a bit and now I will resume my studies.

2:50pm. https://docs.chaos.com/display/VRAYHOUDINI/Materials

I really appreciate the docs being like this. Let me try the light material.

3pm. It works much like self illumination in the regular material. It is not worth concerning myself with it.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Toon+Material
> 2D cel and cartoon effects can easily be achieved with the V-Ray Toon Material. Use this material to make your scene get that hand-drawn look. Controlling the shadows and lights received by the material in combination with material transparency, gotten from Object or Material IDs, allows for fine-tuning the result. You can take advantage from the other standard V-Ray material options such as reflection, refraction, anisotropy, subsurface scattering and bump/normal mapping to set up the render to your liking.

No examples here. But I will be looking into this.

3:05pm. I feel like a kid in a candy store. But I can't eat it all. It will take me a long time to digest the gains. Let me open a new file. What I will do is make a sphere and try out displacement on it.

No, actually, let me just put the stuff here in a subnet and make it invisible.

3:15pm. Oh, the shaders actually work in GL mode when they are put directly on the objects. Interesting.

...Hmmm, I actually do not know where to put displacement. Let me backtrack to yesterday. I'll immitate what he was doing.

https://youtu.be/z9DTGy6Xrfk?t=472

So I just need to plug it into the second node? Let me give it a try.

3:30pm. For textures to stick, the objects really need UVs. Oh, it has options even for UV noise.

3:40pm. I am messing with texture noise and the gradient ramp. The gradient ramp has a ton of options. To actually apply it to the texture, you need to select mapped, which is not the default, but the fourth option instead. Just can actually apply noise directly in the gradient ramp itself.

My second impression of V-Ray is actually quite positive. Yesterday it was crashing on me all the time, but now that I've set it up properly and know how to avoid those situations, I feel I am benefiting. let me try the displacement.

3:45pm. I don't know. The displacement is not working for me for some reason.

https://youtu.be/z9DTGy6Xrfk?t=550

Here is V-Ray.

...I have no idea. Let me try switching to CPU rendering. Maybe there is an option in Render settings I need to click in order to have displacement work.

3:55pm. No that is not it. Let me check out the docs. Maybe there are some tips there.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Displacement

4:05pm. No, there are no tips there. Why isn't this working for me?

https://docs.chaos.com/display/VRAYHOUDINI/Adding+Displacement+to+Object

Oh, wow, this is how to do a map of the Earth. I was wondering how I would do the globe, but it could be quite simple in the end.

> In order to get a correct render, the geometry has to be "packed" before assigning the materials. That's why we set a pack SOP before the material SOP. The geometry has to be packed when using this workflow because V-Ray deals with Displacement at the object level. V-Ray for Houdini exports each packed primitive as a separate object, providing you with the ability to partition the SOP-level geometry into individual shapes to assign different displacement maps to.

> This way V-Ray can apply the correct displacement for each object.

Unwittingly, I did the very right thing when dealing with that toy.

Ah, crap, I just realized I assigned the shader node directly instead of the builder. As a result it is not taking in the displacement.

...That was in fact the problem. It had nothing to do with V-Ray itself.

4:15pm. What if I lowered the geometry of the sphere?

4:20pm. It still works, and it works on the GPU just fine.

I love V-Ray right now. So far it hadn't crashed even once. And since I have access to the render view I do not have to struggle with that floating IPR. Let me finish reading the docs.

4:25pm. Yeah, I have the displacement down. One thing I am going to have to figure out is how to reassign materials in Houdini without having to hunt things down by hand.

But maybe I can clean things up. It would not be bad to be able to assign mats separately outside the pack. I think I made a mistake by assigning those strings to point attributes.

4:35pm. https://docs.chaos.com/display/VRAYHOUDINI/ACEScg+Workflow+Setup

This explains what ACES is. Let me take a look.

4:50pm. https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Fog+Effect

> V-Ray EnvironmentFog is an atmospheric effect that allows the simulation of participating media like fog, atmospheric dust, and so forth. Volumetric properties can be determined by 3D texture maps. The atmospheric effect can also be confined with geometry objects.

3d texture maps exist?

4:55pm. Hmmm, distance...is that the distance between each step?

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Fur

Procedural fur is not bad idea. It is certainly better than putting a million points like in Blender and having that crush the computer.

5:25pm. https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Bump+Normals

Amazing that even these have examples. I won't focus on this right now.

And with this, I've gone over the docs. I know how deal with the basics of V-Ray. I am at the top of 1/5 range in my estimate.

I know how to put in textures, the gradient map, the displacement. At this point I should be able to follow that shading tutorial.

5:30pm. I am very satisfied right now.

Forget the docs and I will watch the tutorial.

https://youtu.be/z9DTGy6Xrfk?t=642

Huh, is it not projecting to UVs by default?

5:35pm. Yep it was not. Once I added the UV object the texture became a lot less stretched.

https://docs.chaos.com/display/VRAYHOUDINI/Texture+Mapping

Let me study this just for a bit after all.

No, I might be wrong. This does not bring in UVs. Rather it turns the object coordinate into UVs. In the UV space, the way I projected it should result in stretching.

Let me try cutting it up. That will tell me right away where I stand.

5:40pm. I use the Auto UV node, and without the Object UV shader node that results in very obvious seams which are present in actual UV coordinates.

This is very nice. I wasn't sure what these mapping nodes are, but they are quite important.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+UV+Bercon

I can guess what Object XYZ, World XYZ and Screen are, but what these explicit map channels?

5:50pm. The bounding box is not what I thought it would be. It behaver like the regular thing instead. Maybe it just pretends the UVs are from a bounding box?

6:35pm. I was wrong, object is not based off the pivot point. The centroid then?

That can only be it.

6:45pm. Ok, I get Object and World, but not much else. Sigh. I can't find it well explained what the rest of the nodes do either.

Let me continue watching the tutorial.

https://youtu.be/z9DTGy6Xrfk?t=1049

Let me stop here. I am done for the day. I want to go on for longer, but I have a chore of installing Windows on a 10+ year old computer for a family friend.

https://youtu.be/7FSS6S1ZcV0
Using Windows 10 on a Computer from 2005

I wish I did not have to do this, but this is one of the disadvantages of not having money. I have to do random favors with my skills. Well, so be it.

Let me save a another link.

https://youtu.be/bWzwCn3sNEI
Lecture 207 - Texture Mapping in V-Ray (Fall 2019)

Maybe this will answer my questions on what those UV mapping nodes do.

Let me watch it just for a bit and then I'll close.

7:40pm. Enough, this is not important. all I have to know is object, world, and the regular thing. I do not need to do UV projections in the shader.

7:45pm. Let me finally close here. Tomorrow I will finish the shading tutorial and then take a look at the Mantra one. I want to see what kinds of things are possible. After that I simply have to go for it. Slap some dirt on those leaves, make the leaves translucent in the middle, put emission on the orbs. Things like that. I'll also want to figure out how to do the facing trick from Blender.

Maybe I should just get the V-Ray rendering for C4D course. Since the resources are so sparse compared to Blender, I should also read the docs top to bottom.

Now, let me take care of that old PC so I do not have to deal with it tomorrow."

---
## [bradmwilliams/api](https://github.com/bradmwilliams/api)@[5b82635ef1...](https://github.com/bradmwilliams/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Friday 2022-03-04 18:53:49 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [shanisebarona/accessibility-insights-web](https://github.com/shanisebarona/accessibility-insights-web)@[60a93ded2b...](https://github.com/shanisebarona/accessibility-insights-web/commit/60a93ded2b227455a1fc794a2fa0ef1735a2c200)
#### Friday 2022-03-04 19:33:30 by Dan Bjorge

fix(tabstops-report): enable hover/focus highlighting on tab stops requirement rows (#5111)

#### Details

This PR enables the Details View > Fast Pass > Tab Stops' new Requirements table to use Office Fabric's default on-hover/on-focus styling that darkens the row backgrounds, to be consistent with the similar behavior in the similar looking Assisted Instance tables in Assessment.

The implementation for this is a little more complicated than expected. The on-hover/on-focus behavior is actually the default fabric behavior; Assessment doesn't do anything special to enable it. The reason we weren't seeing it in FastPass was that we were previously using a very hacky bit of CSS to override the background of the Fabric `DetailsView` to match the slightly-darker-than-usual-gray background we use in FastPass pages (it's different from Assessment to support Cards-based views that want to use our "normal" white background color for Card backgrounds):

```scss
.requirement-table {
    // ...
    * {
        background-color: $neutral-2;
    }
}
```

This was used because the fabric `DetailsView` contains many implementation-detail subcomponents (for rows, cells, headers, etc) that each individually apply overlapping background-color styles; if you just apply background-color to our containing `requirement-table` class, it doesn't have any effect on its own. However, this also has the effect of overriding all of the `:hover` and `:focus` styling under the table.

I originally tried using various combinations of `:not(:focus):not(:hover)` styles, but it rapidly devolved into a big mess of very hacky CSS. Instead, this PR implements a solution based on Office Fabric Themes, which are Fabric's intended way to solve this problem but not the way we normally use in our codebase (we usually use hacky overrides of CSS styles that are Fabric implementation details instead).

The typical Fabric-recommended solution for this is to use their `<Customizer>` to temporarily override the globally-loaded theme; however, this has the disadvantage that it isn't cognizant of the way we swap between "default" and "high-contrast" theme palettes at runtime in our top-level `<Theme>` component. This PR implements a new `<ThemeFamilyCustomizer>` which wraps the fabric `<Customizer>` in a way which respects our app's high contrast mode setting.

##### Animated screenshots

Before:

![animation showing no background color changes on hover/focus](https://user-images.githubusercontent.com/376284/151073621-adfcdd04-33de-4a77-8eed-ecb79cd42936.gif)

After (default theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151073627-a7fe0460-af59-40de-94bb-7c690f959d2a.gif)

After (app high contrast setting):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151074562-16c08b67-c134-42d2-92dd-04a66af30373.gif)

After (Windows "Night Sky" HC theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151076651-43484480-bb32-4958-aacf-3bdc9e6b2516.gif)

##### Motivation

* Make table hover/focus behavior consistent between Assessment and FastPass
* Set up infrastructure that can be used in other components to avoid some types of CSS hacks

##### Context

n/a

#### Pull request checklist
<!-- If a checklist item is not applicable to this change, write "n/a" in the checkbox -->
- [x] Addresses an existing issue: Part of #5099
- [x]  Ran `yarn fastpass`
- [x] Added/updated relevant unit test(s) (and ran `yarn test`)
- [x] Verified code coverage for the changes made. Check coverage report at: `<rootDir>/test-results/unit/coverage`
- [x] PR title *AND* final merge commit title both start with a semantic tag (`fix:`, `chore:`, `feat(feature-name):`, `refactor:`). See `CONTRIBUTING.md`.
- [x] (UI changes only) Added screenshots/GIFs to description above
- [x] (UI changes only) Verified usability with NVDA/JAWS

---
## [bytewax/bytewax](https://github.com/bytewax/bytewax)@[b2937e2525...](https://github.com/bytewax/bytewax/commit/b2937e25257c141111d6ec1f213facf3b71bbb1b)
#### Friday 2022-03-04 19:43:22 by David Selassie

Async execution

_AKA in which I rewrite the execution model again._

Since this was exploratory and coordinates changes to lots of pieces,
I couldn't really break it up into smaller PRs or commits. But it
barely changes the user-facing API! So that's something.

Background
==========

Previously, `run()` and `run_cluster()` would fully turn their inputs
into lists before running the dataflow upon them. This was easy to
code, but also means we didn't support infinite streams or things that
wouldn't all fit in memory. It would be super cool if you could run a
dataflow on an un-ending metrics stream in a notebook, e.g.

This change table-flips the execution of workflows to allow that to
happen. It seems to work, but ups the complexity of our execution code
quite a bit: you now have to know nitty gritty details about
generators, coroutines, thread pools, process pools, why nobody uses
`dill`, IPC queues, unwind logic safety.

I put forth the question: do you think it's worth it?

Implementation
==============

Coroutine Main
--------------

The heart of the whole operation is `WorkerCoro` which is a PyO3 class
which implements Python's `Coroutine` interface. `WorkerCoro.send()`
is the new "main loop" for each worker doing all the same things as
before: pump pumps, step Timely, check probes for output. But it's not
a loop, just one iteration. It will be "looped" by whatever is running
the coroutine allowing other code to run in-between calls.

Because this requires persisting the Timely worker in a PyO3 class,
there are some gotchas surrounding panics and `allow_threads` that are
commented upon in the code.

`WorkerCoro::compile` what builds a `WorkerCoro` from the `Dataflow`
and IO builders, and, crucially, a Timely Worker.

There are also a few other shim methods to match the `Coroutine`
interface with minimal implementations.

Worker Builder
--------------

Timely is very clever. It takes advantage of closures, threads,
ownership, the send trait to ensure that `execute` and
`execute_directly` both magically start up the right number of worker
and background communication threads without race conditions and the
ability to accidentally perform operations in the wrong order.

Because we're wrestling control of the execution of the worker back
from Timely, we have to learn and re-implement some of that internal
magic. But also, because we're playing in Python-land, we don't have
the nice guarantees that Rust gives us to ensure that it's done right.

A `WorkerBuilder` contains the coordination information to start up a
single worker thread. We piggy back on
`timely::CommunicationConfig::try_build()` to generate all the
builders we need to setup a cluster (or just one for single-threaded
mode). Once we have those builders, we can make a worker thread for
each of them, send them to those threads, then actually construct the
worker coroutine with the dataflow we care about.

`run` Generator
---------------

The `WorkerCoro` is all we need to implement running a dataflow in the
current thread. We use the generator as the "run loop" for that
coroutine, stepping it manually and yielding output.

For cluster mode, we need a few more concepts:

Communication Threads
---------------------

A sort of secret thing that Timely did for us when it managed
execution, was start up background threads to communicate with other
processes over the network in cluster mode. We still delegate the
creation of those threads to Timely (they are made at the same time as
the builders above), but we need to wrap them in our own Python object
so we can join them when work is complete.

The `CommsThreads` class encapsulates that.

Graceful Shutdown
-----------------

If you remember in our previous "main" functions, we had some
`AtomicBool` flags to say "shut 'er down" when something went wrong in
another worker. Since the execution is now being managed from Python,
we have to move it there. There's now some `threading.Event` or
`multiprocessing.Event` flags that take on that role.

Then as a way to provide a generic interface to that in the
`WorkerCoro`, we thread around a new callback `should_stop` (or
`proc_should_stop`) which will return `True` whenever the level above
in the cluster found a problem and all workers should shutdown.

Exceptions
----------

Within a cluster process, exceptions are bubbled up from individual
worker threads through using `Future.exception()` created from a
`ThreadPoolExeuctor` in `cluster_main()`. When we see that one thread
excepted, use the event flags described above to shutdown all other
workers, then bubble the exception up to the main thread in that
process.

Then when the main thread throws an exception, the same sort of action
happens on the cluster level via the `AsyncResult` of
`multiprocess.Pool` in `spawn_cluster()`: set a flag that all cluster
processes watch and shutdown.

These two work together to allow a whole cluster to stop on error or
ctrl-c.

A Pile of Queues
----------------

To get the magic of `run_cluster()` continuously yielding output to
work there's three queues which allow us to send out input from the
input iterator and combine output from the workers back to this
process. Then calling all of those, using the output generator as the
"run loop" for the coroutine.

Ugly Bits
=========

I couldn't find much prior art on using a generator as the run loop
for a coroutine, hence all the magic surrounding `send()` and
`StopIteration`. I don't think there's a general way to do this since
most coroutines are waiting on _something_ not just a generic
"yielding of control" like we're doing.

Unfortunately, `asyncio` doesn't EAFP and instead checks if coroutine
objects are subclasses of `abc.Coroutine` and PyO3 doesn't support
subclassing Python types, so there's this `WorkerCoroWrapper` thing.

For some reason `multiprocess.Manager.Queue` doesn't support
`.close()` so I have to enqueue "finished" sentinel values.

It also feels strange to use `multiprocess.Pool` which has a
non-`asyncio` compatible API and so you don't have access to the nice
waiting functions it gives you. But we have to use it to support
`dill` pickling of lambdas in dataflows.

On that note, if we want to drop lambda support, there are some async
libraries that might streamline a lot of this code. One that looks
promising to me is
[`aiomultiprocess`](https://aiomultiprocess.omnilib.dev/en/stable/index.html);
if we discover that having multiple threads per process isn't really
worth it because of the GIL, we could drop a lot of the complexity of
coordinating threads and instead have only one pool to deal with.

---
## [subsurface/subsurface.github.io](https://github.com/subsurface/subsurface.github.io)@[ad4b82193b...](https://github.com/subsurface/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Friday 2022-03-04 20:49:46 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [gimmerain4days/monkeytype](https://github.com/gimmerain4days/monkeytype)@[d23462c38e...](https://github.com/gimmerain4days/monkeytype/commit/d23462c38ea60c6a6e85ae1fed5e9e8c2171ea36)
#### Friday 2022-03-04 21:55:35 by gimmerain4days

Remove comments

I used a list of banned words to clean up the list a bit. 

Removed words (mostly complete): 
    //"Poole",Proper Noun; Placename; City in England
    //"nime", Abbreviation, obscure.
    //"Teresina",Proper Noun, Placename; City in Brazil
    //"feck",//Potentially Offensive
    //"Michelle",//Proper Noun; Name
    //"Winnipeg",//Proper Noun; Placename; City, River
    //"jackass",Potentially Offensive
    //"invagination",//Potentially Offensive
    //"whorehouse",//Potentially Offensive
    //"poop",//Potentially Offensive
    //"anus", 
    //"damnable",//Potentially Offensive
    //"damnation",//Potentially Offensive
    //"wank",//Potentially Offensive
    //"helluva",//Potentially Offensive
    //"dumbass",Potentially Offensive
    //"boner",Potentially Offensive
    //"massimo",Proper Noun; Name
    //"teledildonics",//Potentially Offensive
    //"whoremonger",//Potentially Offensive
    //"slut",//Potentially Offensive
    //"asswage",//Obsolete
    //"shitting",//Potentially Offensive
    //"bullshit",//Potentially Offensive
    //"arse",Potentially Offensive
    //"turd",//Potentially Offensive
    //"asshole",Potentially Offensive
    //"Meuse",Proper Name; Placename; River in Europe
    //"clitoris",//Potentially Offensive
    //"fagot",//Potentially Offensive
    //"fellatio",Potentially Offensive
    //"Tallahassee",//Proper Noun; Placename; City in Florida
    //"pube",//Potentially Offensive
    //"penises",//Potentially Offensive
    //"dyke",//Potentially Offensive
    //"vagina",//Potentially Offensive
    //"hellas",//Potentially Offensive
    //"Geraldine",//Proper Noun; Name 
    //"pussy",//Potentially Offensive
    //"coon",//Potentially Offensive; Racial slur
    //"whore",//Potentially Offensive
    //"vaginal",//Potentially Offensive
    //"analyse", British
    //"shite",//Potentially Offensive
    //"boob",//Potentially Offensive
    //"bastard",//Potentially Offensive
    //"labial",//Potentially Offensive
    //"whoreson",//Potentially Offensive
    //"hellen",//Proper Noun; Name
    //"Abdullah",//Proper Noun; Biographical Name;
    //"penis",//Potentially Offensive
    //"smegma",//Potentially Offensive
    //"hella",//potentially offensive
    //"cocks",//Potentially Offensive
    //"whoremaster",//Potentially Offensive
    //"goddamn",//Potentially Offensive
    //"piss",//Potentially Offensive
    //"shit",//Potentially Offensive
    //"muff",//Potentially Offensive
    //"spunk",//Potentially Offensive
    //"whores",//Potentially Offensive
    //"labia",//Potentially Offensive
    //"anal",//Potentially Offensive
    //"crap",//Potentially Offensive
    //"Hitler",//Proper Noun; Name; Biographical

Other notes made: 
    "WWII",//Abbreviation
    "Uranus",//Capitalize Proper Noun; Planet, Deity
    "Swazi",//Demonym    
    "Ares",//Proper Noun; Name, Deity
    "SATA",//Abbreviation
    "Quetzalcoatl",//Proper Noun; Name; Deity
    "Oceanus",//Proper Noun; Name; Deity
    "Janus",//Capitalize Proper Noun; Name; Deity
    "Leicestershire",//Proper Noun; Placename
    "passover",//Religious
    "Kobe",//Proper Noun; Placename; City
    "Ghanaian",//Demonym
    "Santorini",//Proper Noun; Placename; Island near Italy
    "Zebadiah",//Proper Noun; Name; Biblical
    "mori",//latin
    "Abkhazia",//Proper Noun; Placename; State in Georgia; Disputed
    "Burmese",//Demonym
    "Abbasid",//Proper Noun, Demonym; Religious; Caliphate
    "Nassau",//Proper Noun; Placename; City and Island
    "Passamaquoddy",//Demonym
    "Angola",//Proper Noun 
    "Cassiopeia",//Proper Noun; Name; Deity, Constellation
    "Ugandan",//Demonym
    "Zoroastrianism",//Proper Noun; Religion
    "Guadalcanal",//Capitalize Proper Noun; placename

---
## [YoshiCrafter29/YoshiEngine](https://github.com/YoshiCrafter29/YoshiEngine)@[b74d1a597c...](https://github.com/YoshiCrafter29/YoshiEngine/commit/b74d1a597c454c1771ce5da8fb8b6bd27c99f2e0)
#### Friday 2022-03-04 22:26:48 by YoshiCrafter29

I've come to make an announcement; Shadow The Hedgehog's a bitch ass motherfucker, he pissed on my fucking wife. Thats right, he took his hedgehog quilly dick out and he pissed on my fucking wife, and he said his dick was "This big" and I said that's disgusting, so I'm making a callout post on my twitter dot com, Shadow the Hedgehog, you've got a small dick, it's the size of this walnut except WAY smaller, and guess what? Here's what my dong looks like: PFFFT, THAT'S RIGHT, BABY. ALL POINTS, NO QUILLS, NO PILLOWS. Look at that, it looks like two balls and a bong. He fucked my wife so guess what? I'm gonna fuck the Earth. THAT'S RIGHT THIS IS WHAT YOU GET, MY SUPER LASER PISS! Except I'm not gonna piss on the earth. I'm gonna go higher. I'M PISSING ON THE MOON! HOW DO YOU LIKE THAT, OBAMA? I PISSED ON THE MOON YOU IDIOT! YOU HAVE 23 HOURS BEFORE THE PISS DROPLETS HIT THE FUCKING EARTH NOW GET OUT OF MY SIGHT BEFORE I PISS ON YOU TOO.

---
## [mrk-its/rust-mos](https://github.com/mrk-its/rust-mos)@[734368a200...](https://github.com/mrk-its/rust-mos/commit/734368a200904ef9c21db86c595dc04263c87be0)
#### Friday 2022-03-04 22:29:10 by bors

Auto merge of #87869 - thomcc:skinny-io-error, r=yaahc

Make io::Error use 64 bits on targets with 64 bit pointers.

I've wanted this for a long time, but didn't see a good way to do it without having extra allocation. When looking at it yesterday, it was more clear what to do for some reason.

This approach avoids any additional allocations, and reduces the size by half (8 bytes, down from 16). AFAICT it doesn't come additional runtime cost, and the compiler seems to do a better job with code using it.

Additionally, this `io::Error` has a niche (still), so `io::Result<()>` is *also* 64 bits (8 bytes, down from 16), and `io::Result<usize>` (used for lots of io trait functions) is 2x64 bits (16 bytes, down from 24 — this means on x86_64 it can use the nice rax/rdx 2-reg struct return). More generally, it shaves a whole 64 bit integer register off of the size of basically any `io::Result<()>`.

(For clarity: Improving `io::Result` (rather than io::Error) was most of the motivation for this)

On 32 bit (or other non-64bit) targets we still use something equivalent the old repr — I don't think think there's improving it, since one of the fields it stores is a `i32`, so we can't get below that, and it's already about as close as we can get to it.

---

### Isn't Pointer Tagging Dodgy?

The details of the layout, and why its implemented the way it is, are explained in the header comment of library/std/src/io/error/repr_bitpacked.rs. There's probably more details than there need to be, but I didn't trim it down that much, since there's a lot of stuff I did deliberately, that might have not seemed that way.

There's actually only one variant holding a pointer which gets tagged. This one is the (holder for the) user-provided error.

I believe the scheme used to tag it is not UB, and that it preserves pointer provenance (even though often pointer tagging does not) because the tagging operation is just `core::ptr::add`, and untagging is `core::ptr::sub`. The result of both operations lands inside the original allocation, so it would follow the safety contract of `core::ptr::{add,sub}`.

The other pointer this had to encode is not tagged — or rather, the tagged repr is equivalent to untagged (it's tagged with 0b00, and has >=4b alignment, so we can reuse the bottom bits). And the other variants we encode are just integers, which (which can be untagged using bitwise operations without worry — they're integers).

CC `@RalfJung` for the stuff in repr_bitpacked.rs, as my comments are informed by a lot of the UCG work, but it's possible I missed something or got it wrong (even if the implementation is okay, there are parts of the header comment that says things like "We can't do $x" which could be false).

---

### Why So Many Changes?

The repr change was mostly internal, but changed one widely used API: I had to switch how `io::Error::new_const` works.

This required switching `io::Error::new_const` to take the full message data (including the kind) as a `&'static`, rather than just the string. This would have been really tedious, but I made a macro that made it much simpler, but it was a wide change since `io::Error::new_const` is used everywhere.

This included changing files for a lot of targets I don't have easy access to (SGX? Haiku? Windows? Who has heard of these things), so I expect there to be spottiness in CI initially, unless luck is on my side.

Anyway this large only tangentially-related change is all in the first commit (although that commit also pulls the previous repr out into its own file), whereas the packing stuff is all in commit 2.

---

P.S. I haven't looked at all of this since writing it, and will do a pass over it again later, sorry for any obvious typos or w/e. I also definitely repeat myself in comments and such.

(It probably could use more tests too. I did some basic testing, and made it so we `debug_assert!` in cases the decode isn't what we encoded, but I don't know the degree which I can assume libstd's testing of IO would exercise this. That is: it wouldn't be surprising to me if libstds IO testing were minimal, especially around error cases, although I have no idea).

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[132e05ef22...](https://github.com/tdauth/wowr/commit/132e05ef22d2ff3f2abc49c42d96a484a5a820f7)
#### Friday 2022-03-04 22:34:19 by barade

2.0

- Show the percentage in the tooltip of Brilliance Aura.
- Increase hero level of Archimonde to 500 which is the maximum hero level skill points can be spent.
- Remove irritating boss marker at mages creep spot in Lordaeron.
- Add new boss Mathog.
- Allow deactivating Divine Shield.
- Reduce cooldown and duration of Divine Shield.
- Add new boss Gul'dan.
- Simplify triggers to drop legendary artifacts on hero deaths.
- Add JASS function AssignAllUnitsToCurrentGroup to assign all units at once to a creep respawn group.
- Add global unit group variable udg_CurrentRespawnGroup to add all respawning creeps to it.
- Replace useless Embassy of Theramore with an Arcane Academy of Theramore selling mana-related items.
- Remove useless Tavern of Theramore.
- Add new island next to Maelstrom with new boss Sea Witch.
- Play Naga or Blood Elf Theme if you choose the corresponding races.
- Reduce the number of air units and increase the number of ground units for Demon/TBL AIs.
- Add new boss Avatar of Sargeras with legendary item which can convert units to different races.
- Fix worker counter in stats when using Charm.
- Add more unit and building types for savecodes.
- New race Goblins.
- Add save code for researches and chat command "-loadr XXX" to load it.
- Allow voting for Only Freelancers for AI in the beginning.
- Generate dragon units and good items savecodes with cheats.
- Replace Tier 1 - 3 equivalent texts with "Tier 1", "Tier 2" and "Tier 3" instead of listing all town halls.
- New island Kezan with boss Rumblefitz.
- Allow disabling AI The Burning Legion and The Alliance via votes in the beginning.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[83e2c9bb76...](https://github.com/mrakgr/The-Spiral-Language/commit/83e2c9bb7690f85d1c425e5869ee32959482b80c)
#### Friday 2022-03-04 23:04:09 by Marko Grdinić

"9:15pm. My first attempt failed. It turns out Win 7 Aero Lite does not have the net drivers that I need. I installed Windows, but I can't connect to the Internet. Useless.

9:35pm. https://www.youtube.com/watch?v=zsxg3eWkNYM
Introduction to Vray for Houdini Tutorial

I'll leave this for tomorrow. Right now I am too stressed.

10:45pm. https://docs.blender.org/manual/en/latest/render/shader_nodes/input/layer_weight.html

I wonder how I can get the layer weight equivalent in V-Ray.

https://docs.chaos.com/display/VMAYA/VRayFalloff

> VRayFalloff produces a gradient texture based on the angular falloff of the surface of the geometry to which the texture is applied. The resulting map can simulate the falloff of opacity, reflection, and refraction for surfaces where these properties vary depending on the surface's angle to the camera, such as curved glass or water.

This is eactly the node I need to emulate Blender's Layer Weight node's facing output.

Let me test it.

11:40pm. The VRay Falloff texture is awesome. I am going to make heavy use of it for the scene.

https://docs.chaos.com/display/VMAYA/VRayFalloff

> Towards/Away – Based on face normal directions. Faces with normals that point in the Falloff Direction generate the Front Color while those facing in the opposite direction (180 degrees off the falloff direction) generate the Side Color.

> Perpendicular/Parallel –Based on face normal directions. Faces with normals that point in the Falloff Direction generate the Front Color while those facing in a perpendicular direction (90 degrees off the falloff direction) generate the Side Color.

The explanation for what these modes do is good.

Yeah, remember that Blender vid where he could not get the bakc to work. If he had this node it would have been a piece of cake. He just needed the Perpendicular/Parallel mode. The back would naturally be parallel.

I had no luck getting near/far to work, but...

> Distance – Sets the falloff range based on distance from the camera, as specified by Near Distance and Far Distance. This option is useful for generating a Z-depth type of map when rendering a very large object such as terrain, where the Falloff Map can be used as a mask to dim distant details.

The tip here is really poignant.

The docs also show some neat tricks how to use the ramp. I appreciate they took the time to show it animated.

Yesterday, my impression of V-Ray was quite negative, but today it was the opposite of that. It didn't crash even once, mostly because I know how not to stress it, and I am able to see its good parts. In that intro video, Rohan said it was massive, but I do not agree. The nodes themselves feel well designed. I'll only get more powerful from here as I learn.

12am. At first I hated how Houdini nodes had so much extra parameters compared to Blender ones, but now I am starting to appreciate the extra capability this gives me.

Let me this overtime session. I am quite satisfied by the new insights. I haven't even talked about the Edge material node. I should be able to use this for procedural bevels."

---
## [CitiesSkylinesMods/TMPE](https://github.com/CitiesSkylinesMods/TMPE)@[8ad7a2983d...](https://github.com/CitiesSkylinesMods/TMPE/commit/8ad7a2983d9e313858480015773933ca4c60a309)
#### Friday 2022-03-04 23:22:33 by aubergine10

gah, my brain while my friends are being bombed = mush

Note: FUCK ALL STATE FUNDED TERORIST GROUPS

---

