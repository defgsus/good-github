## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-03](docs/good-messages/2022/2022-03-03.md)


1,736,388 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,736,388 were push events containing 2,757,359 commit messages that amount to 200,712,140 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[a7be3919bf...](https://github.com/newstools/2022-daily-post-nigeria/commit/a7be3919bf91f5891ed86f5ecba7654fbb7794fa)
#### Thursday 2022-03-03 00:01:20 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/03/02/man-commits-suicide-inside-his-car-after-killing-girlfriend-in-ogun/]

---
## [UltraFormula1/Python-2022](https://github.com/UltraFormula1/Python-2022)@[497c674f35...](https://github.com/UltraFormula1/Python-2022/commit/497c674f350ace7f9431cd6dff22fbd85ecd29b9)
#### Thursday 2022-03-03 00:21:46 by UltraFormula1

Update 5_input.py

It was 20 years ago today
Sergeant Pepper taught the band to play
They've been going in and out of style
But they're guaranteed to raise a smile
So may I introduce to you
The act you've know for all these years
Sergeant Pepper's Lonely Hearts Club Band
We're Sergeant Pepper's Lonely Hearts Club Band
We hope you will enjoy the show
Sergeant Pepper's Lonely Hearts Club Band
Sit back and let the evening go
Sergeant Pepper's Lonely, Sergeant Pepper's Lonely
Sergeant Pepper's Lonely Hearts Club Band
It's wonderful to be here
It's certainly a thrill
You're such a lovely audience
We'd like to take you home with us
We'd love to take you home
I don't really want to stop the show
But I thought that you might like to know
That the singer's gonna sing a song
And he wants you all to sing along
So let me introduce to you
The one and only Billy Shears
And Sergeant Pepper's Lonely Hearts Club Band, yeah

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[3bd5a2d8df...](https://github.com/Shadow-Quill/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Thursday 2022-03-03 00:31:12 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [thevandie/Bungalow-13](https://github.com/thevandie/Bungalow-13)@[ecb4422e56...](https://github.com/thevandie/Bungalow-13/commit/ecb4422e566a8bb38d5d249496a6012173756ffb)
#### Thursday 2022-03-03 00:50:39 by BlackCat-055

Attempting to put Frost Demonic Miner to Ice Moon Z-Level (#403)

* First attempt at trying to add clockwork defender and demonic frost miner to icemoon z level

* changed miner cave map type to TGM

* my attempts at fixing the whole gosh darn place

changed the snow tiles of clockwork to icemoon tiles, and made it gen turf for icemoon, hopefully that works

* Update tgstation.dme

* Update icemoon_underground_miner_cave.dmm

* Fixes the damn cave

* Update icemoon.dm

Co-authored-by: Kirie Saito <77302679+Kitsunemitsu@users.noreply.github.com>

---
## [monu70152/android_kernel_asus_sdm660](https://github.com/monu70152/android_kernel_asus_sdm660)@[9222d34c8b...](https://github.com/monu70152/android_kernel_asus_sdm660/commit/9222d34c8b5f53c7970d1b5181b1c7a0cda73619)
#### Thursday 2022-03-03 00:52:14 by Maciej Żenczykowski

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
## [dfrank2781/week-08-response.md](https://github.com/dfrank2781/week-08-response.md)@[130bc0f401...](https://github.com/dfrank2781/week-08-response.md/commit/130bc0f4017de382d0de2bec0a32924cc4a31008)
#### Thursday 2022-03-03 05:46:07 by dfrank2781

Create week-08-response.md

   In my opinion, both O'neil, and Chalabi brought up good points in each of their respective mediums.  I have definitely noticed a lot of what they were talking about, or can at least say that the overall concepts they discussed are not completely foreign to me. I would say that I have especially fallen victim to the internet marketing scheme different companies play. I find it annoying to simply be googling, or browsing the internet for a new outfit idea, or something that I wanted to further research, only to find it on the left of my screen a day or two later; as I'm doing homework. This can definitely be distracting, as I am someone who desires to stay focused with what I'm doing. I find myself x-ing out of these ads as I'm trying to read my online articles for whatever assignment I have to do. I have even experienced seeing them just hours, or even the very next day after looking up that coveted Jordan shoe, or that new shirt I saw and thought about purchasing online. While continuously putting these items in your face on the side of the screen is a good way to convince one to buy it, I do feel as if it's going a bit far to unwillingly track our internet activity in ways such as this. 

   Another tactic that was discussed came from Chalabi during her TED talk. I found it to be very eye opening, yet true to see and hear how not all data presented is accurate or true 100% of the time. I especially realized this after seeing the pool feces diagram she showed during the presentation. I looked at it thinking, "well that's not so bad it's still mostly clean, but then it seems as if it's nearly all of the diagram that contains feces". It made me see how though figures can often times sounds bigger or smaller than they actually are, not everything is what it seems. It especially resonated with me at the end of her talk when she said that we cannot only go by the numbers we see when it comes to making decisions for ourselves. However, we must also not only go off of our own thinking or understanding as well. As we can see, based off of her evidence, and the aforementioned article, there is power in numbers. How many times we visit a site, or click on things of a certain nature will certainly affect what we see on our computer screens. In many ways, I feel as if this also applies to life, as far as pursuing good and bad habits go. I believe the internet would be more useful, and egalitarian if we all had a choice, similar to smart phone data usage, whether or not we want our browsing history to be tracked. Other times, when you are maybe the one behind some of the content that's being shared this way, as in you created it, it can be more useful. In this case, the internet's algorithm can actually help you push your content out further to bigger audiences. Nowadays, nothing seems to hold more power, or spread quicker than the internet.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eeb5465931...](https://github.com/tgstation/tgstation/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Thursday 2022-03-03 11:05:48 by vincentiusvin

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
## [Prashant1873/PersephoneForNord](https://github.com/Prashant1873/PersephoneForNord)@[ab297b66f1...](https://github.com/Prashant1873/PersephoneForNord/commit/ab297b66f10ba71dc685d5b4116a6f99b4bbdfb2)
#### Thursday 2022-03-03 12:38:06 by alk3pInjection

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
## [cw-sf/Stockfish](https://github.com/cw-sf/Stockfish)@[cb9c2594fc...](https://github.com/cw-sf/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-03-03 12:53:11 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [log1cs/alice_lge_sdm845](https://github.com/log1cs/alice_lge_sdm845)@[128db1c1a1...](https://github.com/log1cs/alice_lge_sdm845/commit/128db1c1a1b12c3131f428ca21fdd30316326289)
#### Thursday 2022-03-03 13:16:53 by George Spelvin

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
## [bboygg/nwitter](https://github.com/bboygg/nwitter)@[7d4d4357f1...](https://github.com/bboygg/nwitter/commit/7d4d4357f140cf15c5ba0f540be048c83fe1f10e)
#### Thursday 2022-03-03 13:46:12 by bboygg

 Honestly, I didn't do anything  but I just commit just because I want to make my github looks green.... I know, it sounds silly, however, this is the only way prove my passion for developemen to everyone .....
Yes... now I'
m drunken.. I coudnd't coding what I planned in this morning
but I'm sitting in desk and do commit just for decorate my github
If you guys think I'm lying, and cheating ... then I accept your words...
but I would like to say I want to be smarter like you guys even if I lying
so.... kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllllllllllllllllllllllllllllll
alright
I'll go to bed now.
I hope everybody will be happy in these cut-throgght worlds.

---
## [lowRISC/ibex](https://github.com/lowRISC/ibex)@[c15f3b8888...](https://github.com/lowRISC/ibex/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Thursday 2022-03-03 13:48:13 by Rupert Swarbrick

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
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[f343288dcc...](https://github.com/canalplus/rx-player/commit/f343288dcc68870233652312d5adc9370e54818d)
#### Thursday 2022-03-03 14:35:25 by Paul Berberian

Switch from a `Manifest` class to a `IManifest` interface

The `Manifest` object was a class describing a content regardless of the
streaming protocol (e.g. DASH, Smooth etc.) used:
  - Its URL (at which it can be refreshed)
  - Its minimum and maximum seekable position
  - The description of the available audio/video/text tracks and
    qualities
  - How to request initialization and media segments
  - decryption initialization data
  - and many other things

It is thus a central part of the RxPlayer.

However, the fact that it is defined as a class made us encounter
several issues over time:
  1. No asynchronous operation can happen at object construction. This
     mainly have been problematic recently, as I wanted to use an
     asynchronous Web API (MediaCapabilities's decodingInfo object) to
     detect support to define a property of a `Representation` (which is
     another class inside the `Manifest`'s instance).

     At the end, I may not decide to go in this road (defining the
     property as instanciation) for various other reasons, but the
     possible need to define asynchronous properties still could stand in
     the future.

  2. At instanciation, no other value (excepted the constructed
     `Manifest` object) can be returned.
     This was already problematic as various minor issues can occur
     while instanciating a `Manifest` (e.g. a track has no supported
     codec).

     Due to this, the idea was previously to define a new property of
     the `Manifest`, called `contentWarnings`, which contained all those
     issues. This was kind of a hack.

  3. I remember wanting in the past to have multiple potential
     constructors, with different arguments given, to unlock advanced
     features while staying readable.

     This is not really possible with `classes`, at least not easily
     and readably.

Those are the reason why this commit is a proposal to define an
`IManifest` interface instead and having regular functions constructing
it.
However doing this has also several disadvantages:

  - Property names and method signatures are duplicated: once at type
    definition and the other time in the function that creates it.

    As they are in two separate places, we might also more easily forget
    to update e.g. the documentation when doing changes.

  - tsserver's "go to definition" feature presents in most editors is
    going to favour the interface over the code. This can be good as
    that's where the documentation is, but also bad as that's not where
    the real logic is.

  - it's not possible to call `instanceof` anymore on it, and the most
    probable replacement is doing good ol' and ugly duck typing.

    However this was done at only one place in the code (checking if the
    `initialManifest` `loadVideo` option is a `Manifest` instance).

---
## [corvinux/hubris](https://github.com/corvinux/hubris)@[8e0b13b865...](https://github.com/corvinux/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Thursday 2022-03-03 14:49:30 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [oleg-jukovec/my_dwm](https://github.com/oleg-jukovec/my_dwm)@[67d76bdc68...](https://github.com/oleg-jukovec/my_dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-03-03 14:58:55 by Chris Down

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Thursday 2022-03-03 16:15:23 by Julien Castiaux

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
## [Fazeria8/Isleep](https://github.com/Fazeria8/Isleep)@[78defb6732...](https://github.com/Fazeria8/Isleep/commit/78defb67323e03e48d61d37fe88777d8b25b4dbc)
#### Thursday 2022-03-03 16:22:42 by Fazeria8

ISleep

Market Potential
The global sleep tech devices market generated almost $13 billion revenue in 2020, and it is expected to grow at a CAGR of 14.5% in the next 10 years. 
The key factors are increasing prevalence of sleep disorders, growing awareness about ill effects of untreated sleep apnea, and surging usage of oral appliances.
During the COVID-19 pandemic, a large number of affected people suffered with sleep deprivation, as a result of health problems caused by the coronavirus, which in turn, affected the sales of these devices. 
Sales started to increase at a good pace after the lifting of lockdowns, in 2021, due to the emerging demand for telemedicine and teleconsultation, which leads to the increased growth of the market.

Prevalence of Sleep Disorders and Growing Awareness About Its Ill Effects Are Major Drivers
The prevalence of sleep disorders, such as insomnia, has increased significantly across the globe, which in turn drives the sleep tech devices market. 
This can be affecting every aspect of life, including safety, relationships, school and work performance, thinking, mental health, and body weight, and also leading to the development of diabetes and heart diseases. 
According to the Philips Global Sleep Survey, in 2019, 62% of adults do not sleep properly, and 67% of adults report sleep disturbances at least once every night. Thus, this factor drives the demand for sleep tech devices.

---
## [kdave/btrfs-devel](https://github.com/kdave/btrfs-devel)@[a50e1fcbc9...](https://github.com/kdave/btrfs-devel/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Thursday 2022-03-03 17:51:52 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [oddtiming/push_swap](https://github.com/oddtiming/push_swap)@[a2e206d13e...](https://github.com/oddtiming/push_swap/commit/a2e206d13e666d27e69005b25454f8778fcede10)
#### Thursday 2022-03-03 18:11:42 by Ismael Yahyaoui Racine

Backup commit, bout to fuck shit up

Trying to remove the temp_moves_list in try_pb, as I don't think it needs it.

Good news, got rid of the weird segfault where my cont's values kept getting written over when going into undo_moves();
		it seems to be because of an unitialized value in undo_moves, but unsure of why it manifested itsef only now.

Bad news, it now loops forever
		:)

---
## [Almogbb/App-sus](https://github.com/Almogbb/App-sus)@[902481d6d9...](https://github.com/Almogbb/App-sus/commit/902481d6d903dcff26ddca5bf2dc24fd0821d116)
#### Thursday 2022-03-03 18:36:49 by sowhat1234

after a little bit css breaking my fucking head against the fucking wall for motherfucking hours  over a little small piece of shitty little thing like puting a property in a object. fucking stupid commit

---
## [DimabroStins/Angel-Arena-Reborn](https://github.com/DimabroStins/Angel-Arena-Reborn)@[94662ab559...](https://github.com/DimabroStins/Angel-Arena-Reborn/commit/94662ab559e4e3256f0a865db8af92904cc1c31b)
#### Thursday 2022-03-03 19:27:59 by Akke

Nerf the Soul Collector

I think that the soul collector has a very good place in the current meta of the game, and it has honestly always been great. The problem (in my opinion) is that it is capable of decreasing the value of someones networth based on the fact that it stops all current regeneration, and on top of this it also slows for a huge amount.

This nerf would target the healing reduction primarily, but also slightly touch the slow amount to make it feel a bit more balanced without impacting the game too much.
 
Specifically for the healing reduction, I've decided to decrease it to 75%, because if you're playing as a tank hero it's capable of turning your high networth spent on tanky regen items into basically nothing. On top of this, it's also a very powerful nuke item, and when cast on enemies in their fountain you prevent the fountain from actually protecting them, and I still feel like that should never be the case. 

Decreasing it from 100% to 75% is justified, in my opinion, because the 25% will still let you keep some of that regen, while also making it possible to kill you — it would just take a second or two longer.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[e3d0ced875...](https://github.com/kleinesfilmroellchen/serenity/commit/e3d0ced8756eb2b99ce5de516ed8682eeb8cf32b)
#### Thursday 2022-03-03 19:28:25 by kleines Filmröllchen

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
## [bitcoin-core/gui](https://github.com/bitcoin-core/gui)@[619f8a27ad...](https://github.com/bitcoin-core/gui/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Thursday 2022-03-03 19:33:20 by MarcoFalke

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
## [miloshIra/webStuff](https://github.com/miloshIra/webStuff)@[abddd0aed1...](https://github.com/miloshIra/webStuff/commit/abddd0aed1364615a2cab22eea6b161b87c1f367)
#### Thursday 2022-03-03 20:09:46 by miloshIra

Started the LunchIdea app,
# TODO 2: Work on weekly list of ideas and how to generate a shopping list from their ingredients.
# TODO 3: Make flask-mail work!
# TODO 4. Protect endpoints from not logged users.
# TODO 5. Enjoy life more.

Count works, get idea is a class method now, randomizing works, but I get a None value sometimes, because there is no num=0 in the database, spent hours picking a template picked nothing ..

---
## [crawl/crawl](https://github.com/crawl/crawl)@[e8bc28a0cf...](https://github.com/crawl/crawl/commit/e8bc28a0cf5eb223156f893c8f47b1284931e78a)
#### Thursday 2022-03-03 21:15:41 by DreamDust

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f62ca9f41e...](https://github.com/mrakgr/The-Spiral-Language/commit/f62ca9f41ea18f86cd4f0f4add0c7c7d3d671151)
#### Thursday 2022-03-03 21:29:23 by Marko Grdinić

"10:25am. I am up. I am not sure if I slept well, but it is definitely better than yesterday. Let me chill and I will get in on the action.

10:55am. It is time to start. First let put up the video by Rohan. I want to see how to start the IPR for V-Ray.

https://youtu.be/NoJEsRU-uq0
render engines in houdini - Vray intro

11:15am. Let me just follow the video. I am having trouble getting it to work on my own.

https://youtu.be/NoJEsRU-uq0?t=396

Hmmm, it just works for him. Let me try changing to CPU rendering.

11:25am. I guess what is really necessary is to add a camera. But the reason why I am persisting is because I saw Rohan do without. Let me watch the video.

https://youtu.be/NoJEsRU-uq0?t=402

Oh, he had a cam there. I should have been more attentive. But I do not think he used it to move around.

11:35am. I do not get it. Shouldn't there be settings to change cameras in the IPR?

https://youtu.be/NoJEsRU-uq0?t=728

I think he just had the camera locked on the whole time. This isn't really a problem.

But the way this is setup really requires two monitors to be ergonomic. I just do not have the screen space to keep looking at the result.

What about in the render view?

That just opens the regular IPR. I tried render region just now at it crashed.

11:50am. I do not know why it crashed last time when I tried the render preview, but it works well now. The way to get the render preview in the viewport is to draw a box and then maximize it. That will make it unndeeded to keep looking at the IPR window.

Nice. Everything is set up. V-Ray is decently snappy too.

Now I can proceed with my plans. I am glad the last few days are over. It was like standing on quicksand, but now I am on solid ground once again.

12pm. What I will do next is get back to the pool scene and start rebuilding.

Ah, right. Let me just test whether rendering work on .hipnc files.

...Damn, no. I does not.

12:10pm. I am in great luck. It seems that upgrading from 383 to 455 got rid of all my loading issues in the original scene. Nice!

12:15pm. Now, what I need to do is rebuild the network in a hip file.

///

I shold have started off with a pirate version. I think I am going to have to convert it all by hand at this rate.

https://forums.odforce.net/topic/32925-upgrade-houdini-file-from-non-commercial-file-to-commercial-version-no-more-orbolt-asset-available-why/

> I was Apprentice, then Indie. I think, that I was able to copypaste from my .HIPNC into my .HIPLC ... (maybe there was some signature in those .hipnc, that indicated I created them on the same machine/id?)

https://kiko3d.wordpress.com/2015/03/19/converting-houdini-not-commercial-files/

What a pain in the ass. I'll do it all by hand. I have nodes broken so I might as well anyway.

Now with that out of the way...

///

I found these links a few days ago. Let me focus on them.

> Note that this approach wont export digital assets content. All of the asset need to be unlocked for this approach to work.

Hmmm, how do I deal with this?

https://www.orbolt.com/upgrade-houdini-files

I can just use this web service instead.

It converts to limited commercial rather than full, but nevermind that.

No, I'll have to convert the assets as well.

1pm. I had a weird shading issue, but it turned out to be just the env texture missing. I need to keep that in mind in the future. At any rate, I've mostly converted the file, except for that bench. Will I have to get it again? I am afraid so.

1:10pm. Wait, what the hell. I entered nc mode by accident.

1:20pm. That was a tedious. But now the scene if fully rebuilt. In the Indie version mind you, but that still gives me everything that I'd want.

Good work me. Time for breakfast. When it is time to resume, what will I do? Rendering. I've put in a bunch of shader nodes on those vines, but I need to expore the deeper secrets. I need to replace those principal shaders with the V-Ray ones and move from there. Maybe I should follow that Mantra shading tutorial as an exercise and see whether I can do it in V-Ray instead.

Now that I've come this far, I can actually get serious about this.

This is wonderful. If I can beat this mastery challenge, I will surely be able to reach much greater heights.

Right now I am not much as an artist, but I am only a couple of such challenges away from becoming really good at the craft.

3:05pm. Let me finish the chapter I am reading and I will resume. I am slacking too much.

I have some chores waiting for me later, but I'll try to push them to after I am done for today.

3:15pm. I have to rechache the towels.

Maybe I should have compressed them first. Agh...

Let me figure out how to do that. I did that in the very first tutorial.

3:20pm. Let me do it again. Now where was I?

I read in the docs that the bgeo.sc already uses compression. So I have nothing to do there.

3:25pm. No, I have to save these to disk before applying the subdivision.

While this is going on, let me think.

3:30pm. I fucked up the save. Actually this thing where I am evaling the towels separately I can do much beter now. I know how to feed separate pieces to a loop. Nevermind it for now.

3:35pm. I exited Houdini and am trying to start it again, and now I am getting an error. Let me reset.

3:40pm. The cache works great. It saved me 90%. The subdivision takes huge amount of memory, so it is good to save the results before post processing.

3:45pm. Right now I am too scatter brained.

Let me forget about the towels.

Right. Shading. I need to concern myself with shading.

Ok, first let me control the number of particles. I want to drastically lower the number of instances so that it does not grind down my system so much. Later I'll pump them up.

3:55pm. Damn it the stupid thing crashed. I did not think that would happen here.

4:05pm. I hate Houdini. I had to flip back and forth in order to get the shaders to stick. Maybe this problems are related to upgrading the license of the file.

Now that is out of the way.

4:20pm. I have another problem. Let me take a look at the release log for Houdini.

https://www.sidefx.com/changelog/?page=4&show_compatibility=True&show_versions=True

Wow, there are tons of fixes. At any rate, I just now noticed that offset and element scale do nothing. That was not a problem that I had in the latest version.

https://www.sidefx.com/changelog/?journal=&categories=&body=adjust+color&version=&build_0=&build_1=&show_versions=on&show_compatibility=on&items_per_page=
> The anistropic elementsize and offset options of Attribute Adjust Color for noise is now properly linked up so should work.

This got fixed in 498. Should I try updating the Labs? Let me try it.

I hope this does not break Houdini. It should not. I am guessing that they are separate for a reason.

Updated...no, Color Adjust is not a labs node now even it was in the past so this did not fix it. Can I upgrade Houdini to the latest prod build? I need to check out whether V-Ray is upgradeable first.

4:30pm. I do not even know what version of V-Ray do I have. Where is that information. Also how do I upgrade?

///

# Changelog

## Build 5.20.02 (V-Ray 5) (10 Nov 2021)

### Solaris:
* V-Ray: Added support for the Referenced Shader VOP
* V-Ray: Added support for live (in-memory) volumes

///

Ah, it is from a few months ago.

Looking at the free trial, that is what they are selling. Actually, the free trial is from Dec 9th so it is a bit more up to date, but, I need them to upgrade to the more up to date Houdini version.

I remember Rohan telling me to email them once I have an license to get the most up to date version.

4:40pm. The above changelog is directly from the install on my HDD, and I see that the one on the Chaos Group website for the Dec 9th version is the same.

There is no reason to download the trial.

>  I'm pretty sure the installers are available to download directly from chaosgroup and you can probably continue to use the cgauth.dll for newer builds.

What installers?

4:45pm. No there aren't any other downloads other than on the main site. There is a site for nightly builds, but I'd need a real license for those. I'd need to email the company to ask them about that.

Forget it. While this bug is annoying, it is hardly a deal breaker. If I need noise offsets and per points scales I can just use VOPs. Let's not worry about it.

4:50pm. That seems to be the last bug. I just noticed that floor tiles were not the right color.

Now can I refocus on shading?

4:55pm. Yes, I can. I have 6 shaders that I need to replace. I'll need more shaders for the rest of the scene, but for now let me just focus on the vines.

5pm. Right. There is nothing to it. The plan is simple. I need to replace the shaders with V-Ray specific ones. I also need more knowledge of how to do shading in Houdini.

That Mantra tutorial I got bored of? It is time to bring it up now.

I should watch that shading tutorial from yesterday as well.

What should I do first?

Let me close this scene.

5:05pm. I opened a new scene.

Now let me think. No I do not feel like messing with the test geometries.

Let me just watch V-Ray tutorials. For the next few days that is all what I will concern myself with.

https://youtu.be/z9DTGy6Xrfk
BEST HOUDINI RENDERING ENGINE - Shading Workflow Equivalence

Let me resume this from yesterday. Not really V-Ray specific, but it will do. I'll dive deeper after that.

https://youtu.be/z9DTGy6Xrfk?t=552

I am going to try immitating this.

https://youtu.be/z9DTGy6Xrfk?t=656

Let me pause here. I'll try putting in the displacement as an exercise. I played a lot with this in Blender.

5:25pm. No it is not working for me. Let me just dive into Rohan's tutorial. Right now, I can't even set the color properly.

https://youtu.be/NoJEsRU-uq0
render engines in houdini - Vray intro

5:40pm. I grasped how to change the color, but why doesn't the dome light work? The renderer does not recognize the light from it.

Also, the way I changed the color of the shader is the regular way. The problem is that the GL renderer does not recognize it. While working on the vines I'll have to make heavy use of the preview.

Let me watch the video by Rohan. I think he showed how to set up the dome light/env texture.

One thing I also do not understand is why the sun light was yellow. Was it set that way somewhere?

https://youtu.be/NoJEsRU-uq0?t=716

What the hell, it worked for him right away.

5:45pm. It crashed. This is going to be painful isn't it?

5:50pm. It crashed again as soon as I changed the light intensity.

I need to do the chores here.

6:30pm. Let me resume.

6:35pm. I thought that the .hdr might have too low of an intensity or have the wrong color space, but that is not the case.

I tried my own starry sky HDRI and it works just fine.

Why do Houdini's own textures not work for me.

Wait, those are .rat. What is that? I tried googling it and I am just getting rat images.

They show up in the viewport, but not in the IPR.

6:45pm. It is a mystery. I have no idea why those .rat files are not working.

I am trying a Blender's HDRI and they work.

Let me continue watching the tutorial. I'll push this issue to the back of my mind and be on a lookout for a solution. I do not even know what rat files are.

So far, V-Ray is stable unless you use render preview.

https://youtu.be/NoJEsRU-uq0?t=884

Is self illumation here suposed to be emission?

7pm. Yes.

Time for lunch.

7:20pm. I am back. I had this hunch - emission or global illumination is not that great. For some reason the renderer has a lot of trouble with it. And it makes up the object loose all texture. I meant to use it for the orbs, but now I think that I am better off making the orb translucent and putting the light inside it.

7:35pm. Let me watch the tutorial while I munch on this fruit. Where are those options for smoothing the shadows? I have no idea.

8:20pm. I changed the camera resolution and it crashed. Just what are these guys doing? Are they coding it all in C and getting buffer overruns?

This is beta quality software at best.

Too bad they aren't doing it all in Spiral, that would make things fast and efficient.

9:20pm. The user color attribute does not show up in the shader for some reason. Why is this happening? Let me watch more of the tutorial.

https://youtu.be/NoJEsRU-uq0?t=1698

Is that Rayserver Instancer responsible for propagating user attributes?

No, it is assigning the material to the instance object. That is not good.

Ah, damn I did not assign the material to the original toy, just its object. No wonder it failed.

9:45pm. Instancing works, even on the GPU, and it is not necessary to turn on that special option for it. I did run into a bug though that the turning off the object with the instances and turning on another does not make it show up. It really perplexed me at first before I figured out that I had to abort and restart the render.

V-Ray is very beta quality so far. It stability is abysmal and there are these UI bugs as well. The .rat textures fail to load in the dome light for some reason. The IES light does nothing. The V-Ray shaders do not show up in the viewport.

In its current form it is not worth shelling out the big bucks for.

I am not all that impressed in the quality of craftmanship going into the programs, Blender was on a way higher level for me.

But I suppose it should be better than Karma XPU.

The way the IPR vwindow keeps interfering with my view really tells me that it is designed to be put on a second monitor. It gets poor marks for integration.

I am wondering how things were in 18.5. Did V-Ray suddenly lose all stability in the move to 19 or was it always this clunky?

It also occurs to me though, that all the problems V-Ray and Houdini have are in some way related to the UI. The guys working on this should really study Rx and Hopac to brush up on their concurrency skills.

10:05pm. Let me close here. Right now what I did for the last several hours was merely fiddle with the basic settings. I've scratched the surface and tomorrow it will be time to dive deeper.

The V-Ray surface material node is not that complicated. It is well designed.

Now I just need to explore the rest of the nodes and I will get somewhere.

tomorrow, I'll start with the volume shading tutorial. I'll try to get the noise displacement going and from there I am going to push forward until I get back to my old Blender level as far as shading is concerned. Once I am able to apply all that I've learned, I should be able to do pretty interesting things.

10:20pm. It feels like I am always at the beginner level since I am always trying to learn and master new things. But there is a finite amount of 3d art knowledge. A few more months should definitely be enough to get me to a very capable level. Right now, I know how to deal with geometry. I just need the part that makes it look good in the final product.

If I can meet my goals regarding the arts, Heaven's Key is going to be an impressive work, something that would be fitting of my ambition.

It is a pity I can't tackle AI directly, but I am going to get my rematch in the future. I've mastered programming, and if I can master art, I will have mastered the full range of creative skills.

The clock is ticking. I do not have forever to do this, but on the other hand, it cannot be rushed either.

For long trips, it is not running, but walking that will get you through them."

---
## [HermitDreams/FFR-Spellcrafting](https://github.com/HermitDreams/FFR-Spellcrafting)@[6d50b696a6...](https://github.com/HermitDreams/FFR-Spellcrafting/commit/6d50b696a69214438aa6fb09c9b18784775d7139)
#### Thursday 2022-03-03 23:39:07 by Linkshot

Added March 3rd's spell list (click for full summary)

CURE: Power: 16- Shape: Merging Stars, Colour: 10 (Bright Green), Message: 1 (HP up!) {WmRmWwRwKn}
BRAC- Shape: Bar of Light, Colour: 6 (Magenta), Message: Defend hindrance {WmRmWwRwKn}
JUDG: Power: 20, Acc Bonus: 32- Shape: Energy Bolt, Colour: 12 (Pale Cyan), Message: 0; None {WmWw}
HARM: Power: 20, Acc Bonus: 24- Shape: Flaring Bolt, Colour: 12 (Pale Cyan), Message: 0; None {WmWw}
-
HAZE: Acc Bonus: 32- Shape: Palm Blast, Colour: 1 (White), Message: 0; None {BmBwRwNi}
FIRE: Power: 10, Acc Bonus: 16- Shape: Energy Flare, Colour: 7 (Red), Message: 0; None {BmRmBwRwNi}
PIN : Acc Bonus: 8- Shape: Palm Blast, Colour: 9 (Yellow), Message: 13 (Attack halted) {BmRmBwRwNi}
RUB : Acc Bonus: 5- Shape: Glowing Ball, Colour: 14 (Grey), Message: 21 (Erased) {BmBw}
=
AICE- Shape: Twinkling Bar, Colour: 13 (Bright Cyan), Message: Defend cold {WmRmWwRwKn}
LMPa- Shape: Magic Burst, Colour: 7 (Red), Message: 0; None {WmWwRwKn}
LULL: Acc Bonus: 32- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {WmRmWwRwKn}
BOG: Acc Bonus: 64- Shape: Twinkles, Colour: 10 (Bright Green), Message: 11 (Lost intelligence) {WmWwRwKn}
-
CURS: Acc Bonus: 40 (Element: Earth)- Shape: Palm Blast, Colour: 8 (Orange), Message: 0; None {BmBwRwNi}
HIDE: Power: 30- Shape: Bar of Light, Colour: 4 (Purple), Message: 3 (Easy to dodge) {BmRmBwRwNi}
BRAK: Acc Bonus: 40- Shape: Energy Bolt, Colour: 1 (White), Message: 0; None {BmBw}
RALY: Power: 7- Shape: Twinkling Bar, Colour: 7 (Red), Message: 10 (Weapons stronger) {BmRmBwRwNi}
=
CUR2: Power: 33- Shape: Merging Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!) {WmRmWwRwKn}
AWEK- Shape: Twinkling Bar, Colour: 6 (Magenta), Message: Defend hindrance[White Shirt] {WmRmWwRwKn}
RUS2: Power: 80- Shape: Bar of Light, Colour: 3 (Dark Blue), Message: 3 (Easy to dodge)[Defense] {WmWwRwKn}
HEAL: Power: 12- Shape: Stars, Colour: 10 (Bright Green), Message: 1 (HP up!)[Heal Helm/Staff] {WmWw}
-
LIT2: Power: 30, Acc Bonus: 24- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None[Thor/Zeus] {BmRmBwRwNi}
BZZT: Acc Bonus: 8- Shape: Bursting Ball, Colour: 3 (Dark Blue), Message: 31 (Exile to 4th dimension) {BmBw}
SLEP: Acc Bonus: 48- Shape: Palm Blast, Colour: 9 (Yellow), Message: 0; None {BmRmBwRwNi}
WEL2: Power: 60, Acc Bonus: 64- Shape: Twinkles, Colour: 11 (Dark Green), Message: 5 (Easy to hit) {BmRmBwRwNi}
=
PURE- Shape: Directed Burst, Colour: 10 (Bright Green), Message: 0; None {WmRmWwRw}
TIM2: Power: 32, Acc Bonus: 16- Shape: Flaring Bolt, Colour: 11 (Dark Green), Message: 0; None[Light Axe] {WmRmWwRw}
VIG2: Power: 5, Acc Bonus: 8- Shape: Twinkling Bar, Colour: 12 (Pale Cyan), Message: 27 (Weapon became enchanted) {WmWwRw}
FOC2: Power: 10, Acc Bonus: 24- Shape: Bar of Light, Colour: 1 (White), Message: 27 (Weapon became enchanted) {WmWwRw}
-
PSH2: Power: 25, Acc Bonus: 16- Shape: Twinkles, Colour: 9 (Yellow), Message: 15 (Became terrified) {BmBw}
FIR2: Power: 40, Acc Bonus: 24- Shape: Energy Flare, Colour: 7 (Red), Message: 0; None[Mage Staff] {BmRmBwRwNi}
ICE2: Power: 40, Acc Bonus: 24- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None[Black Shirt] {BmRmBwRwNi}
ZAP!: Acc Bonus: 5- Shape: Bursting Ball, Colour: 11 (Dark Green), Message: 31 (Exile to 4th dimension) {BmBw}
=
CUR3: Power: 66- Shape: Merging Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!) {WmRmWwRw}
LIFE- Shape: Directed Burst, Colour: 12 (Pale Cyan), Message: 74 (Ineffective now) {WmWwRw}
GRO3: Power: 30, Acc Bonus: 32- Shape: Twinkles, Colour: 11 (Dark Green), Message: 15 (Became terrified) {WmWw}
HEL2: Power: 24- Shape: Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!) {WmWw}
-
WAV3: Power: 62, Acc Bonus: 40- Shape: Flaring Bolt, Colour: 6 (Magenta), Message: 0; None {BmBwRw}
ARM3: Power: 16- Shape: Bar of Light, Colour: 13 (Bright Cyan), Message: 2 (Armor up) {BmBwRw}
WARP {BwRw}
SAND: Acc Bonus: 107- Shape: Palm Blast, Colour: 8 (Orange), Message: 0; None {BmBwRw}
=
SOFT- Shape: Directed Burst, Colour: 1 (White), Message: 74 (Ineffective now) {WmWw}
EXIT {WwRw}
HRM3: Power: 70, Acc Bonus: 48- Shape: Flaring Bolt, Colour: 7 (Red), Message: 0; None {WmWw}
SKIP: Acc Bonus: 48- Shape: Palm Blast, Colour: 11 (Dark Green), Message: 30 (Time stopped) {WmRmWwRw}
-
FUM3: Power: 60, Acc Bonus: 64- Shape: Energy Flare, Colour: 4 (Purple), Message: 0; None[Bane Sword] {BmBwRw}
BRN3: Power: 60, Acc Bonus: 48- Shape: Fizzling Flare, Colour: 7 (Red), Message: 0; None {BmRmBwRw}
SAB3: Power: 28- Shape: Bar of Light, Colour: 2 (Light Blue), Message: 10 (Weapons stronger)[Power Glove] {Bw}
OUB3: Power: 120, Acc Bonus: 175- Shape: Twinkles, Colour: 8 (Orange), Message: 5 (Easy to hit)[Wizard Staff] {BmBwRw}
=
CUR4- Shape: Merging Stars, Colour: 3 (Dark Blue), Message: 24 (HP max!) {Ww}
HRM4: Power: 80, Acc Bonus: 48- Shape: Flaring Bolt, Colour: 12 (Pale Cyan), Message: 0; None {Ww}
BLS3: Power: 10, Acc Bonus: 32- Shape: Bar of Light, Colour: 12 (Pale Cyan), Message: 27 (Weapon became enchanted) {WmWwRw}
HEL3: Power: 48- Shape: Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!) {WmWw}
-
VNM3: Power: 70, Acc Bonus: 107- Shape: Fizzling Flare, Colour: 4 (Purple), Message: 0; None {BmBwRw}
PSH4: Power: 47, Acc Bonus: 32- Shape: Twinkles, Colour: 9 (Yellow), Message: 15 (Became terrified) {Bw}
TMP3: Power: 25- Shape: Bar of Light, Colour: 7 (Red), Message: 10 (Weapons stronger) {BmBwRw}
BOM3: Power: 70, Acc Bonus: 48- Shape: Energy Flare, Colour: 9 (Yellow), Message: 0; None {BmBwRw}
=
LIF2- Shape: Merging Stars, Colour: 5 (Pink), Message: 74 (Ineffective now) {Ww}
WALL- Shape: Bar of Light, Colour: 5 (Pink), Message: Defend all {WwRw}
MUFF: Acc Bonus: 210- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {WwRw}
WEL4: Power: 200, Acc Bonus: 128- Shape: Twinkles, Colour: 11 (Dark Green), Message: 5 (Easy to hit) {WwRw}
-
RIP : Acc Bonus: 107- Shape: Twinkles, Colour: 3 (Dark Blue), Message: 29 (Defenseless) {BwRw}
HAIL: Power: 100, Acc Bonus: 64- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None {Bw}
CONF: Acc Bonus: 175- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {BwRw}
SOOT: Acc Bonus: 152- Shape: Palm Blast, Colour: 7 (Red), Message: 0; None {BwRw}
=
Battle Messages
#01: HP up! [Assigned]
#02: Armor up [Assigned]
#03: Easy to dodge [Assigned]
#05: Easy to hit [Assigned]
#08: Defend hindrance [Spaces to add: 0]
#10: Weapons stronger [Assigned]
#11: Lost intelligence [Assigned]
#12: Defend fire [Unassigned]
#13: Attack halted [Assigned]
#15: Became terrified [Assigned]
#16: Defend cold [Assigned]
#18: Quick shot [Unassigned]
#21: Erased [Assigned]
#22: Fell into crack [Unassigned]
#24: HP max! [Assigned]
#25: Defend magic [Unassigned]
#27: Weapon became enchanted [Assigned]
#28: Defend all [Assigned]
#29: Defenseless [Assigned]
#30: Time stopped [Assigned]
#31: Exile to 4th dimension [Assigned]
#43: Critical hit!! [Unassigned]
#47: Stopped [Unassigned]
#74: Ineffective now [Assigned]
#76: Go mad [Unused]
#77: Poison smoke [Unassigned]

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[4051ad647e...](https://github.com/DesmontTiney/tgstation/commit/4051ad647e3e94ea5c722cee18cecf350270ab6f)
#### Thursday 2022-03-03 23:41:13 by LemonInTheDark

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
## [beavertronics/2022code5970](https://github.com/beavertronics/2022code5970)@[ca8014ebff...](https://github.com/beavertronics/2022code5970/commit/ca8014ebffa812093791edef49aaa41c57fa4648)
#### Thursday 2022-03-03 23:59:25 by duke1733

i dont even remember what the fuck i did last night but it works

---

