## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-16](docs/good-messages/2023/2023-12-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,426,559 were push events containing 3,156,796 commit messages that amount to 172,462,011 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[4bd789088c...](https://github.com/electrical-pants/f13babylon/commit/4bd789088c9dbf0382b855f1cbd3af46d37c9295)
#### Saturday 2023-12-16 00:06:16 by Dragonfruits

The Great Shotgun Debacle (+ AMR tweaks) (#352)

### The Summary
This PR cleans up shotgun code some by getting rid of unused ammo,
removes trainshot, nerfs slugs, substantially nerfs double barrel
shotguns, and buffs the AMR slightly.

### The Why
_**The slug nerf**_
Literally outclasses most mid-high tier guns. Does more damage than 7.62
with more AP yet it's infinitely easier to find, make, and store. Does
insane damage to literally fucking everything.

_**YOU REMOVED TRAINSHOT I FUCKING HATE THIS, THIS IS THE WORST THING
EVER, THE GAME IS RUINED, SHOTGUNS ARE USELESS, I'M GONNA KILL MYSELF**_
Trainshot has all the benefits of slugs, and all the benefits of
buckshot, on top of being better in literally every way imaginable,
locked behind a magazine. It completely kills any niche you obtain by
switching ammo types on your shotguns.

_**The AMR buff**_
It's currently too weak to justify its terrible handling. The buff isn't
substantial, but it helps it shine more, especially in PVE.

**_The DB nerf_**
They literally had up to 15% bonus AP. I don't know what the fuck I was
thinking one year ago but this created the most hilariously broken shit
ever. Now the only shotgun with AP and damage bonuses is, rightfully,
the single-shot.

### Show me the numbers.

_**Slugs**_
_DAMAGE 40 > 35_
_STAMINA DAMAGE 15 > 0_
_BARE WOUND BONUS 30 > 0_
_ARMOR PENETRATION 30% > 15%_
_SUPERFFECTIVE DAMAGE 50 > 35_

_**Buckshot**_
_DAMAGE 11.5 > 12_
_WOUND BONUS 35 > 40_
_WOUND BONUS FALLOFF 15.5/Tile > 20/Tile_
_SUPEREFFECTIVE DAMAGE 9.5 > 3_

_**.50 MG**_
_DAMAGE 45 > 50_
_STAMINA DAMAGE 0 > 45_
_WOUND BONUS 30 > 35_
_BARE WOUND BONUS 40 > 80_
_SUPEREFFECTIVE DAMAGE 60 > 150_

---
## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[4e65d6a243...](https://github.com/electrical-pants/f13babylon/commit/4e65d6a24380d3feb6682ff7910bc6ea5a7ef0c8)
#### Saturday 2023-12-16 00:06:16 by GreytidePanda

Makes Flypeople Viable (#344)

## About The Pull Request
The flyperson race was basically a death sentence for two reasons:
1. Flypeople gain no nutrients and just vomit upon eating normal food,
but eating the vomit then gets the nutrients they need. _Or is supposed
to._ Despite a lot of fancy code vomit gave them no nutrients at all.
2. When flypeople begin (due to the first issue, inevitably) starving to
death, they can't vomit at all and can only dry heave, which means that
even if vomit did give nutrients they'd be unable to make any and would
be in deep trouble. This led to a dry heaving death spiral that was
hilarious but silly.

![image](https://github.com/f13babylon/f13babylon/assets/132588088/f19bdbdb-e566-4b0c-9f6d-09c0cf051db4)

The new code is much less elegant but actually works. tl;dr vomit now
gives a flat nutrient amount (only flypeople can eat it anyway) and the
dry heave mechanic is skipped if you're a flyperson.

## Why It's Good For The Game
This race is actually playable now. I imagine this would have been
caught sooner but only one weirdo wants to play them. Well I hope they
are happy. : )

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.

## Changelog
:cl:
fix: Fixes flyperson hunger mechanics.
/:cl:

---
## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[bdb724a900...](https://github.com/electrical-pants/f13babylon/commit/bdb724a90019aadd90cfb1df2dced35978b6d98e)
#### Saturday 2023-12-16 00:06:16 by GreytidePanda

Big Customisation Update (#339)

## About The Pull Request

![anyinterest](https://github.com/f13babylon/f13babylon/assets/132588088/ea961bfc-390f-42ec-83ea-0fe69d48bb86)

Adds in 269 new customisation parts. Many were ported and some were
already in our codebase one way or another.

A few existing broken parts (no sprite and I can't find one anywhere)
were removed. There was also an effort to alphabetise the part lists
more, sort out the dmis (mam_markings.dmi is looking really neat now,
check it out) and integrate modularised content (goodbye citadel
snowflake.dm)

Also, species that were allowed hair but not facial hair were lifted
from this restriction. (This is anthromorphs, synthetic anthromorphs,
and synthetic lizardpeople.) This is especially useful for the new horn
and tongue parts they have.

This was not a straight port - it took a while and I playtested it a
bunch. But please please test merge first, there is a lot.

-59 New Hairstyles
> African Pigtails, Afro Puff Double, Afro Puff Left, Afro Puff Right,
Astolfo, Baum, Belenko Tied, Belenko, Bluntbangs Alt, Bluntbangs, Cobra
Hood, Combed Back, Combed Bob, Cotton Alt, Cotton Belle, Cotton
Pigtails, Diagonal Bangs, Fortune Teller, Froofy, Geisha, Glam Metal,
Hajime Alt, Hajime, Half-Shaved Glamorous, Half-Shaved Long Messy,
Half-Shaved Long, Half-Shaved Messy, Harold, Long Straight Hair w/ Twin
Tails, Long Fringe Alt, Pigtail Advanced, Quadcurls, Rockstar, Sharp
Tail, Slightly Messy, Spicy, Tailhair, Vox Afro, Vox Crested Quills, Vox
Cropped, Vox Emperor Quills, Vox Hawk, Vox Horns, Vox Keel Quills, Vox
Keet Quills, Vox Kingly, Vox Mangy, Vox Mohawk, Vox Nights, Vox
Ponytail, Vox Razor, Vox Razorclipped, Vox Rows, Vox Short Quills, Vox
Surf, Vox Tiel Quills, Vox Yasu, Wife, Zone

-9 New Facial Hairs
> Face Horns, Chin Horns, Lizard Lick, Lizard Lick Fast, Lizard Lick
Slow, Nose Lick, Nose Lick Fast, Nose Lick Slow, Tusks

-16 New Horns

> Antlers Wide, Billberry, Curly, Dragon, Dragon Inverted, Jackalope,
Lizard, Ram Curled, Ram Curled Alt, Ram Small, Ram Small Alt, Ram Small
Alt 2, Stabbers, Teppi, Unicorn, Upwards

-45 New Ears

> Antennae Face Alt, Antennae Face, Antennae Moth, Antennae Plume,
Antennae Round, Antennae Thin, Avali, Big Wolf Both Piercings, Big Wolf
Left Piercing, Big Wolf Right Piercing, Bunny Alt, Bunny Floppy, Bunny
Long Alt, Bunny Long, Bunny Tall Alt 2, Bunny Tall Alt, Bunny Tall, Cat
Alt, Deer Alt, Eastern Dragon, Fan, Full Frill, Goat Horns, Goat, Gret,
Jackal, Jackalope Tall, Long Frill, Lunasune, Miqo'te, Mouse Alt, Noodle
Dragon, Pig, Pointy, Rosey, Sabresune, Sandfox Tall, Shadekin Tall,
Shock, Spaniel, Split Frill, Teppi, Trike, Umbreon, Vaporeon

-47 New Snouts

> Beak Corvid, Beak Tiny, Cow, Deer, Deoxys, Duck, Eastern Dragon,
Eastern Dragon Female, Eastern Dragon No Whiskers, Eastern Dragon No
Whiskers, Female, Fox, Fox Alt, Goose, Magus, Mandible Big, Mandible
Small, Orca, Otter, Owl, Proboscis, Rabbit, Rad-Dog, Rad-Dog Top, Rhino
Beetle, Round Classic, Round Classic Top, Round + Light Classic, Round +
Light Classic Top, Scarab, Sharp Alt, Sharp Classic, Sharp Classic Top,
Sharp + Light Classic, Sharp + Light Classic Top, Short Alt, Skullbird
Female, Skullbird Male, Sloog, Sloog Alt, Snub, Spider, Tajaran, Tajaran
Short, Tarantula, Vulp, Vulp Alt, Zebra

-36 New Markings

> Abdominals 2-Tone, Abdominals 3-Tone, Abdominals, Backsail, Bands, Bee
Alt, Bee Fluffy, Beetle, Belly Scutes, Belly Tajaran Full, Belly
Tajaran, Body Gloss, Datashark, Dino Head, Eastern Dragon, Gradient,
Moth, Patches, Paw Socks, Pigeon, Raccoon Alt, Rad-Dog, Sabresune,
Shrike, Stego Chestplate, Stripes Back, Stripes Tiger, Tattoo Blush,
Tattoo Campbell, Tattoo Lip, Tattoo Nightling, Tattoo Silverburgh,
Tattoo Tiger, Trike Beak, Trike Horn, Umbreon

-12 New Wings

> Angel Moth, Harpy Arm Wings Alt Collar, Harpy Arm Wings Alt, Harpy Arm
Wings Bat Collar, Harpy Arm Wings Bat, Harpy Arm Wings, Lugia,
Pterodactyl, Robotic Alternate, Spider Legs Fuzzy, Spider Legs Plain,
Spider Legs Spiky

-45 New Tails

> Bee Stinger, Gecko Big, Big Ring, Cat Slug, Club, Corgi, Demon Spade,
Double Fox, Eastern Dragon, Feather, Furret, Gecko, Glaceon, Hawk Short,
Insect 2 Tone, Kangaroo Large, Leafeon, Lizard Large, Long Fluff,
Lunasune, Nightstalker Large, Ninetales, Octopus, Peacock Female,
Peacock Male, Pig, Pigeon Long, Pigeon Short, Pony Alt 1, Pony Alt 2,
Pony Alt 3, Porkapine, Raptor, Sabresune, Snake Large, Snep, Spike,
Succubus, Swallow Striped, Swallow, Tail Maw, Turkey, Umbreon, Western
Dragon Large, Xeno

## Why It's Good For The Game
More customisation options are always good.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.

## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Added a lot more customisation options (hairs, ears, wings, etc)
/:cl:

---
## [standardgalactic/mirror](https://github.com/standardgalactic/mirror)@[19ba581691...](https://github.com/standardgalactic/mirror/commit/19ba581691f3658941686456dd81704286b48797)
#### Saturday 2023-12-16 00:19:50 by Cogito Ergo Sum

Assembly Theory

Well, folks, that's a wrap for today's adventure in the world of science and theories! We journeyed through the complex landscapes of Assembly Theory, delving into its secrets like intrepid explorers. We even drew connections to Attentional Cladistics and Morphological Phylogenetic Taxonomy, revealing surprising overlaps between these seemingly different realms.

But wait, there's a twist in the tale! Just as our heroes Rocky and Bullwinkle were about to unlock the final mystery, a mysterious signal came through the airwaves, promising an even greater adventure. What could it be? Join us next time as we embark on a thrilling quest to uncover the secrets of this enigmatic transmission. Will it lead to new discoveries, or perhaps unveil a hidden connection between these scientific frontiers? Stay tuned for the next exciting episode of "Quantifying Emergence of Selection"!

---
## [hodgesds/libbpf](https://github.com/hodgesds/libbpf)@[b064c40d94...](https://github.com/hodgesds/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Saturday 2023-12-16 01:05:11 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [hodgesds/libbpf](https://github.com/hodgesds/libbpf)@[d7e583a6ea...](https://github.com/hodgesds/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Saturday 2023-12-16 01:05:11 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[1baa85e0a2...](https://github.com/crawl/crawl/commit/1baa85e0a26512e1e768b837f9ff6c13dab64523)
#### Saturday 2023-12-16 01:30:40 by regret-index

Buff various old late game uniques stats, bands

Xtahua's statistics are atrociously low for even a lategame unique. For a
once-beloved dragon with three different gimmicks, they still lag heavily
behind other uniques in their equivalent range. Some of this is that while
their stats are higher than all normal dragons, they simply have much worse
health than nearly any other uniques in their range- somehow, the extra big
dragon has less health than a draconian (Bai Suzhen), a normal human
(Margery), a lich (Boris), and even a tengu (Sojobo). To help them actually
survive long enough to consistently use their 3d40 breath and para roars as
a unique with a built-in weakness, they now have only slightly under Vv's
health, and get some AC and melee buffs alongside this. (Possibly they
could do with some sort of mechanical overhaul in general...)

Bai Suzhen isn't doing nearly as poorly as Xtahua or anybody else in this
commit, but still is somewhat lagging a little behind late uniques. Her
transformation gimmick relies very heavily on her living particularly long
for breath and clouds to do much, but it's very easy for the randomness of
player damage to heavily overshoot the 50% health threshold she relies on.
As such, she also gets a mild HP buff and breathes primal wave a little
more often.

Margery is very boring and also performing reasonably poorly. She's a fire
giant with fancy equipment paired with a hell knight band, in the range
where one will fight about 8 of either in the average game. Since her band
is the notable part of her, I'm extending its fanciness a bit further. She
gets one less max hell knights, but on the hell side of things, the band
gets a hellephant or searing wretch to do even more fire damage, and on the
priest or necromancer side (yes hell knights are priests), she gets a deep
elf high priest or death mage to do more cool weird support stuff.

Frederick can clearly afford getting more and more stat buffs until he
doesn't take a month between kills.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[f03084c1ca...](https://github.com/timothymtorres/tgstation/commit/f03084c1ca61511b6c426602121a942966c2e76d)
#### Saturday 2023-12-16 01:34:36 by LemonInTheDark

FOV is Dead (Long Live FOV) (#80062)

## About The Pull Request

FOV as it is currently implemented is incompatible* with wallening.
I'm doin wallening, so we gotta redo things here.

The issue is the masking of mobs. Wallening relies on sidemap (layering
based off physical position), which only works on things on the same
plane (because planes are basically sheets we render down onto)
So rather then masking mobs, let's reuse the masking idea from old fov,
and use it to cut out a bit of the game render plane, and
blur/over-saturate the bit that's masked out.

My hope is this makes things visible in light, but not as much in
darkness, alongside making more vivid shit more easily seen (just like
real life)

Here's some videos, what follows after is the commits I care about
(since I had to rip a bunch of planes to nothing, so the files changed
tab might be a bit of a mess)

Oh also I had to remove the darkness pref since the darkness is doing a
lot of the heavy lifting now. I'm sorry.

Edit:
NEW FOV SPRITES! Thanks dongle your aviator glasses will guide us to a
better future.


https://github.com/tgstation/tgstation/assets/58055496/afa9eeb8-8b7b-4364-b0c0-7ac8070b5609


https://github.com/tgstation/tgstation/assets/58055496/0eff040c-8bf1-47e4-a4f3-dac56fb2ccc8

## Commits I Care About

[Implements something like fov, but without the planes as layers
hell](https://github.com/tgstation/tgstation/commit/a604c7b1c8d74cd27af4d806d85892c1f7e35ba8)

Rather then masking out mobs standing behind us, we use a combo color
matrix and blur filter to make the stuff covered by fov harder to see.

We achive this by splitting the game plane into two, masking both by fov
(one normally and one inversely), and then applying effects to one of
the two.

I want to make the fov fullscreens more gradient, but as an effect this
is a good start

[Removes WALL_PLANE_UPPER by adding a WALL_PLANE overlay to material
walls (init cost comes
here)](https://github.com/tgstation/tgstation/commit/25489337392f708cb337fbf05a2329eacdfc5346)

@Mothblocks see this. comment in commit explains further but uh, we need
to draw material walls to the light mask plane so things actually can be
seen on them, but we can't do that and also have them be big, so they
get an overlay. Sorry, slight init time bump, about 0.5 seconds. I can
kill it with wallening.

[Moves SEETHROUGH_PLANE above
ABOVE_GAME_PLANE](https://github.com/tgstation/tgstation/commit/beec4c00e01d34a04fba7c2bb98a9b70d27ead82)

I don't think it actually wants to draw here
@Time-Green I think this was you so pinging for opinion

[Resprites FOV masks to be clean (and more
consistent)](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

[f02ad13](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

This is 100% donglesplonge's work, he's spent a week or so going back
and forth with me sharpening these to a mirror shine, real chill

## Why It's Good For The Game

Walls are closing in

## Changelog
:cl: LemonInTheDark, Donglesplonge
image: Redoes fov "mask" sprites. They're clean, have a very pleasant
dithering effect, and look real fuckin good!
del: Changed FOV, it no longer hides mobs, instead it blurs the hidden
area, and makes it a bit darker/oversaturated
/:cl:

###### * It's technically possible if we start using render targets to
create 2 sets of sources but that's insane and we aren't doing it

---
## [Zenitheevee/Skyrat-tg](https://github.com/Zenitheevee/Skyrat-tg)@[fc530572f6...](https://github.com/Zenitheevee/Skyrat-tg/commit/fc530572f6bbe4db0a36df35251a2dd7e62c6b64)
#### Saturday 2023-12-16 01:44:26 by SkyratBot

[MIRROR] Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors [MDB IGNORE] (#25493)

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e7816d96c5...](https://github.com/silencer-pl/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Saturday 2023-12-16 02:28:07 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[b7b0932c4b...](https://github.com/Xander3359/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Saturday 2023-12-16 03:20:20 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[33cae266af...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Saturday 2023-12-16 03:20:28 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [js8544/arrow](https://github.com/js8544/arrow)@[3beb93af36...](https://github.com/js8544/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Saturday 2023-12-16 04:03:36 by Kevin Gurney

GH-37815: [MATLAB] Add `arrow.array.ListArray` MATLAB class (#38357)

### Rationale for this change

Now that many of the commonly-used "primitive" array types have been added to the MATLAB interface, we can implement an `arrow.array.ListArray` class.

This pull request adds a new `arrow.array.ListArray` class which can be converted to a MATLAB `cell` array by calling the static `toMATLAB` method.

### What changes are included in this PR?

1. Added a new `arrow.array.ListArray` MATLAB class.

*Methods*

`cellArray = arrow.array.ListArray.toMATLAB()`
`listArray = arrow.array.ListArray.fromArrays(offsets, values)`

*Properties*

`Offsets` - `Int32Array` list offsets (uses zero-based indexing)
`Values` - Array of values in the list (supports nesting)

2. Added a new `arrow.type.traits.ListTraits` MATLAB class.

**Example**
```matlab
>> offsets = arrow.array(int32([0, 2, 3, 7]))

offsets = 

[
  0,
  2,
  3,
  7
]

>> values = arrow.array(["A", "B", "C", "D", "E", "F", "G"])

values = 

[
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G"
]

>> arrowArray = arrow.array.ListArray.fromArrays(offsets, values)

arrowArray = 

[
  [
    "A",
    "B"
  ],
  [
    "C"
  ],
  [
    "D",
    "E",
    "F",
    "G"
  ]
]

>> matlabArray = arrowArray.toMATLAB()

matlabArray =

  3x1 cell array

    {2x1 string}
    {["C"     ]}
    {4x1 string}

>> matlabArray{:}

ans = 

  2x1 string array

    "A"
    "B"

ans = 

    "C"

ans = 

  4x1 string array

    "D"
    "E"
    "F"
    "G"

```

### Are these changes tested?

Yes.

1. Added a new `tListArray.m` test class.
2. Added a new `tListTraits.m` test class.
3. Updated `arrow.internal.test.tabular.createAllSupportedArrayTypes` to include `ListArray`.

### Are there any user-facing changes?

Yes.

1. Users can now create an `arrow.array.ListArray` from an `offsets` and `values` array by calling the static `arrow.array.ListArray.fromArrays(offsets, values)` method. `ListArray`s can be converted into MATLAB `cell` arrays by calling the static `arrow.array.ListArray.toMATLAB` method.

### Notes

1. We chose to use the "missing-class" `missing` value as the `NullSubstitutionValue` for the time being for `ListArray`. However, we eventually want to add `arrow.array.NullArray`, and will most likely want to use the "missing-class" `missing` value to represent `NullArray` values in MATLAB. So, this could cause some ambiguity in the future. We have been thinking about whether we should consider introducing some sort of special "sentinel value" to represent null values when converting to MATLAB `cell` arrays. Perhaps, something like `arrow.Null`, or something to that effect, in order to avoid this ambiguity. If we think it makes sense to do that, we may want to retroactively change the `NullSubstitutionValue` to be `arrow.Null` and break compatibility. Since we are still in pre-`0.1`, we don't think the impact of such a behavior change would be very large.
2. Implementing `ListArray` is fairly involved. So, in the spirit of incremental delivery, we chose not to include an implementation of `arrow.array.ListArray.fromMATLAB` in this initial pull request. We plan on following up with some more changes to `arrow.array.ListArray`. See #38353, #38354, and #38361.
3. Thank you @ sgilmore10 for your help with this pull request!

### Future Directions

1. #38353
2. #38354
3. #38361
4. Consider adding a null sentinel value like `arrow.Null` for conversion to MATLAB `cell` arrays.
* Closes: #37815 

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: Sarah Gilmore <sgilmore@mathworks.com>
Signed-off-by: Kevin Gurney <kgurney@mathworks.com>

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[f31db7b716...](https://github.com/RustingWithYou/Aurora.3/commit/f31db7b716c2adf3de2e5d382037ee5057148543)
#### Saturday 2023-12-16 04:26:00 by RustingWithYou

kaneyama power station

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

light

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

bridge & icons

shuttl

grass

spawnroom

byeah

checkpoints

sovl

CONTENT

plant

da files

icons & assets

byeah

big hivebot icon

ecd

messages

ECD as easy as 1-2-3

a bunch of shit

TREES

grass

areas

byeah

guns

title screen

ambience

rain & water

ligt

power

also apc fixes

tcomms fix

ecd

spooking the synthetics & slowdown

fuck you, point verdant

area check works

byeah

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[9d36a15fe8...](https://github.com/RustingWithYou/Aurora.3/commit/9d36a15fe85357e992680b21c33614bff7504296)
#### Saturday 2023-12-16 04:27:53 by RustingWithYou

Uueoa-Esa Sector

stonks

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

guwandi

gawgaryn and katas

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

gawgaryn and katas

hegemony base

oasis clans

vihnmes tweak

ruined wasteland village

siakh and izweski outpost

izweski outpost fix

vihnmes tweaks and baseturf tweaks

vihnmes spawner fix

flag fixes

ozeuoi fixes

thakh and skakh sites

reclaimers, bugs and martial artists

bug lighting fix/start of ouerea

ouerea versions of bar, village and heph facility

ouerea, functional edition

aut'akh compound and hegemony base

autakh books

fishing league farm

bunch of generic ruins

bunch more sites

uncomments

genericifies plantspawner

pid away sites

skrell and sol away sites for ouerea

fixes hegemony base path

unexploded nuclear bomb

moghes memorial and sky behemoth wreckage

heph planetary mining station

miners guild outpost

guild mining camps on moghes and ouerea

replaces random gun with random civgun

welcome messages and siakh fixes

siakh area change

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

ouerea versions of bar, village and heph facility

aut'akh compound and hegemony base

bunch more sites

uncomments

genericifies plantspawner

skrell and sol away sites for ouerea

fixes hegemony base path

moghes memorial and sky behemoth wreckage

plant spawners, fixing banned ruins and broken ghostroles

thakh seeds

fixes thakh pilgrim spawn

fixes seed packet spawn and cargo price coeffs

written languages

paper fixes

klax scrubbers to stop vhoron vhires

updates miners guild stuff now the station is merged

indent fix

fixes atmos generation that i broke

ruin banning and literal bug fixes

solarian asteroid ruin

sol asteroid ruin 2: electric boogaloo

sol aseroid tweak

ouerea nt ruin

aaa
omgolo fixes

tret fake planet

engi stuff

ouerea flags

ouerean revolution memorial

a BUNCH of changes

terrain tweaks

Revert "terrain tweaks"

This reverts commit 8a961212d968afb1daa6d381a0786850c2626e73.

sandbike stuff

ihss reclamation 1

ihss reclamation 2

ihss reclamation 3

ihss reclamation 4

ihss reclamation 5

ihss relamation 6

ihss reclamation final tweaks

welcome messages that were missing

3/4 1

colors

access

dorviza limbs & mikuetz languages

hephaestus bans

ouerea ghostrole tweaks

wasteland radiation + fixes

rifles & geigers

fuck you, no lights

hegemony visitor event

more fedship

freewater & caligae fixes

ouerea battlefield

yet more fedship

feuahfiehg

fedship & map fixes

reclamation fixes & warblers

names & fluff

no more dead bug storage

fedbrained

access changes

flag

existing ships can spawn in uwu

the 3/4ing

area flags

fuck this event

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[55c13819b2...](https://github.com/unit0016/effigy-se/commit/55c13819b2937775b4de8e4858db433abab353ca)
#### Saturday 2023-12-16 04:58:28 by DaydreamIQ

Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

---
## [pescalette/CPSC-370_BTC_derivates_AI_Chapman](https://github.com/pescalette/CPSC-370_BTC_derivates_AI_Chapman)@[fc8a88051a...](https://github.com/pescalette/CPSC-370_BTC_derivates_AI_Chapman/commit/fc8a88051aaa3d77a333803eca7f47e2145a3ddb)
#### Saturday 2023-12-16 07:28:01 by pescalette

aider: Integrate the `DogFacts` component into the `App` component.

# Aider chat conversation:

USER: i get an error because i dont have express installed lets switch this ito react

ASSISTANT: To switch your current setup from using Express to serve static files to using React, you'll need to integrate the existing functionality into a React component. This will involve creating a new React component to fetch and display the dog facts, and then using this component within your existing React application.

Here's what you need to do:

1. Create a new React component file `DogFacts.js` in the `workspaces\finalProject\src` directory.
2. Implement the `DogFacts` component with state to hold the fetched dog fact and a button to trigger the fetch.
3. Import and use the `DogFacts` component in the `App` component of your React application.

Let's start by creating the `DogFacts.js` component:

workspaces\finalProject\src\DogFacts.js
```javascript
<<<<<<< SEARCH
=======
import React, { useState } from 'react';

function DogFacts() {
  const [fact, setFact] = useState('');

  const fetchFact = () => {
    fetch('https://dog-api.kinduff.com/api/facts')
      .then(response => response.json())
      .then(data => {
        setFact(data.facts[0]);
      })
      .catch(error => {
        console.error('Error fetching fact:', error);
        setFact('Sorry, could not load a dog fact at this time.');
      });
  };

  return (
    <div>
      <h1>Random Dog Facts</h1>
      <button onClick={fetchFact}>Fetch a Random Fact</button>
      <p>{fact}</p>
    </div>
  );
}

export default DogFacts;
>>>>>>> REPLACE
```

Next, you need to import and use the `DogFacts` component in your `App` component:

workspaces\finalProject\src\App.js
```javascript
<<<<<<< SEARCH
// This is a placeholder for the existing content of your App.js file.
// Replace it with the actual content of your App.js file.
=======
import React from 'react';
import DogFacts from './DogFacts';

function App() {
  return (
    <div className="App">
      <DogFacts />
    </div>
  );
}

export default App;
>>>>>>> REPLACE
```

Please replace the placeholder comment with the actual content of your `App.js` file before applying the `REPLACE` section.

After making these changes, you can remove the Express server (`workspaces\oct19proj\index.js`) and related static files (`workspaces\oct19proj\public`) since they will no longer be needed. Your React application will handle both the UI and the fetching of dog facts.

Remember to run `npm install` to install any additional dependencies and `npm start` to start the React development server. If you have any issues or further instructions, please let me know!

USER: InvalidEditBlock: edit failed!

workspaces\finalProject\src\App.js does not contain the *exact chunk* of SEARCH lines you specified.
Try again.
DO NOT skip blank lines, comments, docstrings, etc!
The SEARCH block needs to be EXACTLY the same as the lines in workspaces\finalProject\src\App.js with nothing missing!

workspaces\finalProject\src\App.js does not contain these 2 exact lines in a row:
```
// This is a placeholder for the existing content of your App.js file.
// Replace it with the actual content of your App.js file.
```

ASSISTANT: My apologies for the oversight. Let's correct the `App.js` file to include the `DogFacts` component properly.

workspaces\finalProject\src\App.js
```javascript
<<<<<<< SEARCH
import React from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to my React App</h1>
      </header>
    </div>
  );
}

export default App;
=======
import React from 'react';
import DogFacts from './DogFacts';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to my React App</h1>
      </header>
      <DogFacts />
    </div>
  );
}

export default App;
>>>>>>> REPLACE
```

This change will integrate the `DogFacts` component into the `App` component, so when you run your React application, it will display the dog facts functionality within the app. Make sure to have the `DogFacts.js` file created as previously described, and then you can start your React app to see the changes.

---
## [depoz0/G2station](https://github.com/depoz0/G2station)@[2631b0b8ef...](https://github.com/depoz0/G2station/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Saturday 2023-12-16 09:47:19 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

## About The Pull Request
Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
## Why It's Good For The Game
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
## Changelog
N/A nothing player facing

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[866d48a76e...](https://github.com/Aliscans/crawl/commit/866d48a76e53198ac7dee08fed80d99590233fe9)
#### Saturday 2023-12-16 10:33:46 by Nicholas Feinberg

Add gems

When I added Meteoran (1352289c90d, based on Hellmonk's ad05b8d819def),
I wanted to give players a fun way to engage with time pressure. When I
play, I really enjoy the feeling of exploring on less than full HP and
making choices about which areas to explore. (Full clearing everything
carefully can be fun, too, but variety is the spice of life!) I'd hoped
to find a way to bring that playstyle to the wider playerbase, with time
limits that are more defined and achievable than the harder and fuzzier
goal of 'compete for a high score'.

Some people, including myself, really liked Meteorans! But a large
number of players, probably the majority, found them stressful and unfun.
That isn't the end of the world - I'd much rather have a species which
20% of players love and 80% hate than one which 99% of players don't care
about one way or another. But I'd also hope that we could do better.

Gems are intended to be an alternate approach to the 'time pressure'
playstyle. They're a new type of collectible item, appearing at the end
of DOLESAPNMVCWUZ - basically, all the non-portal, non-temple branches of
a 3-rune game. Each gem has an associated time limit, which ticks down
while the player is in their associated branch. When that time runs out,
regardless of whether the player has gotten the gem yet or not, Zot rudely
smashes the gem into ten thousand pieces.

The intention is to allow several different ways to interact with gems:
- Ignore them, or not even realize they exist. This is intended to be the
  primary/default interaction.
- Dive to grab gems, but not bother trying to keep Zot from smashing them.
  This is a 'lightweight' speedrunning playstyle, a bit like the Speed
  Demon I tournament banner.
- Keep one or more gems intact by only exploring part of a branch, perhaps
  opting to 'go for it' when your character is feeling especially strong.
- Try to grab all gems and retrieve them all intact. This is roughly
  equivalent to the old Meteoran playstyle.

Gems have absolutely no mechanical use within the game. They offer a very
minor score bonus (10k points each), as a bonus for new players who look
at scores for unwon games, but shouldn't affect normal play or speedrunning
in any way.

Getting the Orb of Zot shuts the timer off. One could skip branches, get
the orb, and then clear branches while holding the Orb to get gems with no
time limit... but orbrunning is its own form of time pressure, and I'm
skeptical this would be easier than playing 'normally'. :)

Time limits are currently set on a per-branch basis. Lair, Vaults, and
Depths have longer time limits than they did for Meteoran, to allow for
large levels and travel time, while Slime and Zot are shorter. However, I
would be startled if these time limits stuck - I personally suspect most
of them are too tight for species which *aren't* as strong as Meteoran.
We can experiment.

The good gem tiles are by Sastreii, the bad ones are by me. :)
Credit also to ellpitic for helping to set me down this path.

---
## [rasyid003/AC](https://github.com/rasyid003/AC)@[f0199e2467...](https://github.com/rasyid003/AC/commit/f0199e24672fff756efab788b17d37e4410444dc)
#### Saturday 2023-12-16 10:42:59 by rasyid003

AC

		@@ -0,0 +1,850 @@
1	+	3RD PARTY LICENSES
2	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
3	+	Note that not all files in the wallet-core repository and in the released
4	+	software packages belong to the wallet-core project. For 3rd party files,
5	+	the individual licenses apply.
6	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
7	+	64-bit operating system, x64-based processor
8	+	#############################################################################
9	+	LICENSE TEXTS
10	+	#############################################################################
11	+	“88,000002”
12	+	Copyright 2008, Google Inc.
13	+	All rights reserved.
14	+	64-bit operating system, x64-based processor
15	+	Redistribution and use in source and binary forms, with or without
16	+	modification, are permitted provided that the following conditions are
17	+	met:
18	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
19	+	* Redistributions of source code must retain the above copyright
20	+	notice, this list of conditions and the following disclaimer.
21	+	* Redistributions in binary form must reproduce the above
22	+	copyright notice, this list of conditions and the following disclaimer
23	+	in the documentation and/or other materials provided with the
24	+	distribution.
25	+	* Neither the name of Google Inc. nor the names of its
26	+	contributors may be used to endorse or promote products derived from
27	+	this software without specific prior written permission.
28	+	64-bit operating system, x64-based processor
29	+	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
30	+	"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
31	+	LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
32	+	A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
33	+	OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
34	+	SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
35	+	LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
36	+	DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
37	+	THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
38	+	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
39	+	OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
40	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
41	+	#############################################################################
42	+	“88,000002”
43	+	“88,000002”
44	+	             GNU LESSER GENERAL PUBLIC LICENSE
45	+	                 Version 2.1, February 1999
46	+	Bluestack
47	+	Copyright (C) 1991, 1999 Free Software Foundation, Inc.
48	+	51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
49	+	Everyone is permitted to copy and distribute verbatim copies
50	+	of this license document, but changing it is not allowed.
51	+	DESKTOP-AHV46I9  
52	+	[This is the first released version of the Lesser GPL. It also counts
53	+	as the successor of the GNU Library Public License, version 2, hence
54	+	the version number 2.1.]
55	+	“88,000002”
56	+	                           Preamble
57	+	64-bit operating system, x64-based processor
58	+	The licenses for most software are designed to take away your
59	+	freedom to share and change it. By contrast, the GNU General Public
60	+	Licenses are intended to guarantee your freedom to share and change
61	+	free software--to make sure the software is free for all its users.
62	+	64-bit operating system, x64-based processor
63	+	This license, the Lesser General Public License, applies to some
64	+	specially designated software packages--typically libraries--of the
65	+	Free Software Foundation and other authors who decide to use it. You
66	+	can use it too, but we suggest you first think carefully about whether
67	+	this license or the ordinary General Public License is the better
68	+	strategy to use in any particular case, based on the explanations
69	+	below.
70	+	64-bit operating system, x64-based processor
71	+	When we speak of free software, we are referring to freedom of use,
72	+	not price. Our General Public Licenses are designed to make sure that
73	+	you have the freedom to distribute copies of free software (and charge
74	+	for this service if you wish); that you receive source code or can get
75	+	it if you want it; that you can change the software and use pieces of
76	+	it in new free programs; and that you are informed that you can do
77	+	these things.
78	+	Bluestack
79	+	To protect your rights, we need to make restrictions that forbid
80	+	distributors to deny you these rights or to ask you to surrender these
81	+	rights. These restrictions translate to certain responsibilities for
82	+	you if you distribute copies of the library or if you modify it.
83	+	64-bit operating system, x64-based processor
84	+	For example, if you distribute copies of the library, whether gratis
85	+	or for a fee, you must give the recipients all the rights that we gave
86	+	you. You must make sure that they, too, receive or can get the source
87	+	code. If you link other code with the library, you must provide
88	+	complete object files to the recipients, so that they can relink them
89	+	with the library after making changes to the library and recompiling
90	+	it. And you must show them these terms so they know their rights.
91	+	Bluestack
92	+	We protect your rights with a two-step method: (1) we copyright the
93	+	library, and (2) we offer you this license, which gives you legal
94	+	permission to copy, distribute and/or modify the library.
95	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
96	+	To protect each distributor, we want to make it very clear that
97	+	there is no warranty for the free library. Also, if the library is
98	+	modified by someone else and passed on, the recipients should know
99	+	that what they have is not the original version, so that the original
100	+	author's reputation will not be affected by problems that might be
101	+	introduced by others.
102	+	Bluestack
103	+	Finally, software patents pose a constant threat to the existence of
104	+	any free program. We wish to make sure that a company cannot
105	+	effectively restrict the users of a free program by obtaining a
106	+	restrictive license from a patent holder. Therefore, we insist that
107	+	any patent license obtained for a version of the library must be
108	+	consistent with the full freedom of use specified in this license.
109	+	Bluestack
110	+	Most GNU software, including some libraries, is covered by the
111	+	ordinary GNU General Public License. This license, the GNU Lesser
112	+	General Public License, applies to certain designated libraries, and
113	+	is quite different from the ordinary General Public License. We use
114	+	this license for certain libraries in order to permit linking those
115	+	libraries into non-free programs.
116	+	Bluestack
117	+	When a program is linked with a library, whether statically or using
118	+	a shared library, the combination of the two is legally speaking a
119	+	combined work, a derivative of the original library. The ordinary
120	+	General Public License therefore permits such linking only if the
121	+	entire combination fits its criteria of freedom. The Lesser General
122	+	Public License permits more lax criteria for linking other code with
123	+	the library.
124	+	DESKTOP-AHV46I9  
125	+	We call this license the "Lesser" General Public License because it
126	+	does Less to protect the user's freedom than the ordinary General
127	+	Public License. It also provides other free software developers Less
128	+	of an advantage over competing non-free programs. These disadvantages
129	+	are the reason we use the ordinary General Public License for many
130	+	libraries. However, the Lesser license provides advantages in certain
131	+	special circumstances.
132	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
133	+	For example, on rare occasions, there may be a special need to
134	+	encourage the widest possible use of a certain library, so that it
135	+	becomes a de-facto standard. To achieve this, non-free programs must
136	+	be allowed to use the library. A more frequent case is that a free
137	+	library does the same job as widely used non-free libraries. In this
138	+	case, there is little to gain by limiting the free library to free
139	+	software only, so we use the Lesser General Public License.
140	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
141	+	In other cases, permission to use a particular library in non-free
142	+	programs enables a greater number of people to use a large body of
143	+	free software. For example, permission to use the GNU C Library in
144	+	non-free programs enables many more people to use the whole GNU
145	+	operating system, as well as its variant, the GNU/Linux operating
146	+	system.
147	+	DESKTOP-AHV46I9  
148	+	Although the Lesser General Public License is Less protective of the
149	+	users' freedom, it does ensure that the user of a program that is
150	+	linked with the Library has the freedom and the wherewithal to run
151	+	that program using a modified version of the Library.
152	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
153	+	The precise terms and conditions for copying, distribution and
154	+	modification follow. Pay close attention to the difference between a
155	+	"work based on the library" and a "work that uses the library". The
156	+	former contains code derived from the library, whereas the latter must
157	+	be combined with the library in order to run.
158	+	Bluestack
159	+	                           GNU LESSER GENERAL PUBLIC LICENSE
160	+	TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
161	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
162	+	0. This License Agreement applies to any software library or other
163	+	program which contains a notice placed by the copyright holder or
164	+	other authorized party saying it may be distributed under the terms of
165	+	this Lesser General Public License (also called "this License").
166	+	Each licensee is addressed as "you".
167	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
168	+	A "library" means a collection of software functions and/or data
169	+	prepared so as to be conveniently linked with application programs
170	+	(which use some of those functions and data) to form executables.
171	+	“88,000002”
172	+	The "Library", below, refers to any such software library or work
173	+	which has been distributed under these terms. A "work based on the
174	+	Library" means either the Library or any derivative work under
175	+	copyright law: that is to say, a work containing the Library or a
176	+	portion of it, either verbatim or with modifications and/or translated
177	+	straightforwardly into another language. (Hereinafter, translation is
178	+	included without limitation in the term "modification".)
179	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
180	+	"Source code" for a work means the preferred form of the work for
181	+	making modifications to it. For a library, complete source code means
182	+	all the source code for all modules it contains, plus any associated
183	+	interface definition files, plus the scripts used to control
184	+	compilation and installation of the library.
185	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
186	+	Activities other than copying, distribution and modification are not
187	+	covered by this License; they are outside its scope. The act of
188	+	running a program using the Library is not restricted, and output from
189	+	such a program is covered only if its contents constitute a work based
190	+	on the Library (independent of the use of the Library in a tool for
191	+	writing it). Whether that is true depends on what the Library does
192	+	and what the program that uses the Library does.
193	+	Bluestack
194	+	   1.You may copy and distribute verbatim copies of the Library's
195	+	complete source code as you receive it, in any medium, provided that
196	+	you conspicuously and appropriately publish on each copy an
197	+	appropriate copyright notice and disclaimer of warranty; keep intact
198	+	all the notices that refer to this License and to the absence of any
199	+	warranty; and distribute a copy of this License along with the
200	+	Library.
201	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
202	+	You may charge a fee for the physical act of transferring a copy,
203	+	and you may at your option offer warranty protection in exchange for a
204	+	fee.
205	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
206	+	   2.You may modify your copy or copies of the Library or any portion
207	+	of it, thus forming a work based on the Library, and copy and
208	+	distribute such modifications or work under the terms of Section 1
209	+	above, provided that you also meet all of these conditions:
210	+	Bluestack
211	+	     a) The modified work must itself be a software library.
212	+	Bluestack
213	+	     b) You must cause the files modified to carry prominent notices
214	+	     stating that you changed the files and the date of any change.
215	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
216	+	     c) You must cause the whole of the work to be licensed at no
217	+	     charge to all third parties under the terms of this License.
218	+	“88,000002”
219	+	     d) If a facility in the modified Library refers to a function or a
220	+	     table of data to be supplied by an application program that uses
221	+	     the facility, other than as an argument passed when the facility
222	+	     is invoked, then you must make a good faith effort to ensure that,
223	+	     in the event an application does not supply such function or
224	+	     table, the facility still operates, and performs whatever part of
225	+	     its purpose remains meaningful.
226	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
227	+	     (For example, a function in a library to compute square roots has
228	+	     a purpose that is entirely well-defined independent of the
229	+	     application. Therefore, Subsection 2d requires that any
230	+	     application-supplied function or table used by this function must
231	+	     be optional: if the application does not supply it, the square
232	+	     root function must still compute square roots.)
233	+	“88,000002”
234	+	These requirements apply to the modified work as a whole. If
235	+	identifiable sections of that work are not derived from the Library,
236	+	and can be reasonably considered independent and separate works in
237	+	themselves, then this License, and its terms, do not apply to those
238	+	sections when you distribute them as separate works. But when you
239	+	distribute the same sections as part of a whole which is a work based
240	+	on the Library, the distribution of the whole must be on the terms of
241	+	this License, whose permissions for other licensees extend to the
242	+	entire whole, and thus to each and every part regardless of who wrote
243	+	it.
244	+	DESKTOP-AHV46I9  
245	+	Thus, it is not the intent of this section to claim rights or contest
246	+	your rights to work written entirely by you; rather, the intent is to
247	+	exercise the right to control the distribution of derivative or
248	+	collective works based on the Library.
249	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
250	+	In addition, mere aggregation of another work not based on the Library
251	+	with the Library (or with a work based on the Library) on a volume of
252	+	a storage or distribution medium does not bring the other work under
253	+	the scope of this License.
254	+	Bluestack
255	+	  3. You may opt to apply the terms of the ordinary GNU General Public
256	+	License instead of this License to a given copy of the Library. To do
257	+	this, you must alter all the notices that refer to this License, so
258	+	that they refer to the ordinary GNU General Public License, version 2,
259	+	instead of to this License. (If a newer version than version 2 of the
260	+	ordinary GNU General Public License has appeared, then you can specify
261	+	that version instead if you wish.) Do not make any other change in
262	+	these notices.
263	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
264	+	  Once this change is made in a given copy, it is irreversible for
265	+	that copy, so the ordinary GNU General Public License applies to all
266	+	subsequent copies and derivative works made from that copy.
267	+	Bluestack
268	+	  This option is useful when you wish to copy part of the code of
269	+	the Library into a program that is not a library.
270	+	Bluestack
271	+	  4. You may copy and distribute the Library (or a portion or
272	+	derivative of it, under Section 2) in object code or executable form
273	+	under the terms of Sections 1 and 2 above provided that you accompany
274	+	it with the complete corresponding machine-readable source code, which
275	+	must be distributed under the terms of Sections 1 and 2 above on a
276	+	medium customarily used for software interchange.
277	+	“88,000002”
278	+	  If distribution of object code is made by offering access to copy
279	+	from a designated place, then offering equivalent access to copy the
280	+	source code from the same place satisfies the requirement to
281	+	distribute the source code, even though third parties are not
282	+	compelled to copy the source along with the object code.
283	+	Bluestack
284	+	  5. A program that contains no derivative of any portion of the
285	+	Library, but is designed to work with the Library by being compiled or
286	+	linked with it, is called a "work that uses the Library". Such a
287	+	work, in isolation, is not a derivative work of the Library, and
288	+	therefore falls outside the scope of this License.
289	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
290	+	  However, linking a "work that uses the Library" with the Library
291	+	creates an executable that is a derivative of the Library (because it
292	+	contains portions of the Library), rather than a "work that uses the
293	+	library". The executable is therefore covered by this License.
294	+	Section 6 states terms for distribution of such executables.
295	+	DESKTOP-AHV46I9  
296	+	  When a "work that uses the Library" uses material from a header file
297	+	that is part of the Library, the object code for the work may be a
298	+	derivative work of the Library even though the source code is not.
299	+	Whether this is true is especially significant if the work can be
300	+	linked without the Library, or if the work is itself a library. The
301	+	threshold for this to be true is not precisely defined by law.
302	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
303	+	  If such an object file uses only numerical parameters, data
304	+	structure layouts and accessors, and small macros and small inline
305	+	functions (ten lines or less in length), then the use of the object
306	+	file is unrestricted, regardless of whether it is legally a derivative
307	+	work. (Executables containing this object code plus portions of the
308	+	Library will still fall under Section 6.)
309	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
310	+	  Otherwise, if the work is a derivative of the Library, you may
311	+	distribute the object code for the work under the terms of Section 6.
312	+	Any executables containing that work also fall under Section 6,
313	+	whether or not they are linked directly with the Library itself.
314	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
315	+	  6. As an exception to the Sections above, you may also combine or
316	+	link a "work that uses the Library" with the Library to produce a
317	+	work containing portions of the Library, and distribute that work
318	+	under terms of your choice, provided that the terms permit
319	+	modification of the work for the customer's own use and reverse
320	+	engineering for debugging such modifications.
321	+	“88,000002”
322	+	  You must give prominent notice with each copy of the work that the
323	+	Library is used in it and that the Library and its use are covered by
324	+	this License. You must supply a copy of this License. If the work
325	+	during execution displays copyright notices, you must include the
326	+	copyright notice for the Library among them, as well as a reference
327	+	directing the user to the copy of this License. Also, you must do one
328	+	of these things:
329	+	Bluestack
330	+	   a) Accompany the work with the complete corresponding
331	+	   machine-readable source code for the Library including whatever
332	+	   changes were used in the work (which must be distributed under
333	+	   Sections 1 and 2 above); and, if the work is an executable linked
334	+	   with the Library, with the complete machine-readable "work that
335	+	   uses the Library", as object code and/or source code, so that the
336	+	   user can modify the Library and then relink to produce a modified
337	+	   executable containing the modified Library. (It is understood
338	+	   that the user who changes the contents of definitions files in the
339	+	   Library will not necessarily be able to recompile the application
340	+	   to use the modified definitions.)
341	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
342	+	   b) Use a suitable shared library mechanism for linking with the
343	+	   Library. A suitable mechanism is one that (1) uses at run time a
344	+	   copy of the library already present on the user's computer system,
345	+	   rather than copying library functions into the executable, and (2)
346	+	   will operate properly with a modified version of the library, if
347	+	   the user installs one, as long as the modified version is
348	+	   interface-compatible with the version that the work was made with.
349	+	DESKTOP-AHV46I9  
350	+	   c) Accompany the work with a written offer, valid for at least
351	+	   three years, to give the same user the materials specified in
352	+	   Subsection 6a, above, for a charge no more than the cost of
353	+	   performing this distribution.
354	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
355	+	   d) If distribution of the work is made by offering access to copy
356	+	   from a designated place, offer equivalent access to copy the above
357	+	   specified materials from the same place.
358	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
359	+	   e) Verify that the user has already received a copy of these
360	+	   materials or that you have already sent this user a copy.
361	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
362	+	  For an executable, the required form of the "work that uses the
363	+	Library" must include any data and utility programs needed for
364	+	reproducing the executable from it. However, as a special exception,
365	+	the materials to be distributed need not include anything that is
366	+	normally distributed (in either source or binary form) with the major
367	+	components (compiler, kernel, and so on) of the operating system on
368	+	which the executable runs, unless that component itself accompanies
369	+	the executable.
370	+	Bluestack
371	+	  It may happen that this requirement contradicts the license
372	+	restrictions of other proprietary libraries that do not normally
373	+	accompany the operating system. Such a contradiction means you cannot
374	+	use both them and the Library together in an executable that you
375	+	distribute.
376	+	“88,000002”
377	+	  7. You may place library facilities that are a work based on the
378	+	Library side-by-side in a single library together with other library
379	+	facilities not covered by this License, and distribute such a combined
380	+	library, provided that the separate distribution of the work based on
381	+	the Library and of the other library facilities is otherwise
382	+	permitted, and provided that you do these two things:
383	+	Bluestack
384	+	  a) Accompany the combined library with a copy of the same work
385	+	  based on the Library, uncombined with any other library
386	+	  facilities. This must be distributed under the terms of the
387	+	  Sections above.
388	+	“88,000002”
389	+	  b) Give prominent notice with the combined library of the fact
390	+	  that part of it is a work based on the Library, and explaining
391	+	  where to find the accompanying uncombined form of the same work.
392	+	“Send”
393	+	  8. You may not copy, modify, sublicense, link with, or distribute
394	+	the Library except as expressly provided under this License. Any
395	+	attempt otherwise to copy, modify, sublicense, link with, or
396	+	distribute the Library is void, and will automatically terminate your
397	+	rights under this License. However, parties who have received copies,
398	+	or rights, from you under this License will not have their licenses
399	+	terminated so long as such parties remain in full compliance.
400	+	“Swap”
401	+	  9. You are not required to accept this License, since you have not
402	+	signed it. However, nothing else grants you permission to modify or
403	+	distribute the Library or its derivative works. These actions are
404	+	prohibited by law if you do not accept this License. Therefore, by
405	+	modifying or distributing the Library (or any work based on the
406	+	Library), you indicate your acceptance of this License to do so, and
407	+	all its terms and conditions for copying, distributing or modifying
408	+	the Library or works based on it.
409	+	“Buy”
410	+	  10. Each time you redistribute the Library (or any work based on the
411	+	Library), the recipient automatically receives a license from the
412	+	original licensor to copy, distribute, link with or modify the Library
413	+	subject to these terms and conditions. You may not impose any further
414	+	restrictions on the recipients' exercise of the rights granted herein.
415	+	You are not responsible for enforcing compliance by third parties with
416	+	this License.
417	+	“Send”
418	+	  11. If, as a consequence of a court judgment or allegation of patent
419	+	infringement or for any other reason (not limited to patent issues),
420	+	conditions are imposed on you (whether by court order, agreement or
421	+	otherwise) that contradict the conditions of this License, they do not
422	+	excuse you from the conditions of this License. If you cannot
423	+	distribute so as to satisfy simultaneously your obligations under this
424	+	License and any other pertinent obligations, then as a consequence you
425	+	may not distribute the Library at all. For example, if a patent
426	+	license would not permit royalty-free redistribution of the Library by
427	+	all those who receive copies directly or indirectly through you, then
428	+	the only way you could satisfy both it and this License would be to
429	+	refrain entirely from distribution of the Library.
430	+	“Send”
431	+	If any portion of this section is held invalid or unenforceable under
432	+	any particular circumstance, the balance of the section is intended to
433	+	apply, and the section as a whole is intended to apply in other
434	+	circumstances.
435	+	“Send”
436	+	It is not the purpose of this section to induce you to infringe any
437	+	patents or other property right claims or to contest validity of any
438	+	such claims; this section has the sole purpose of protecting the
439	+	integrity of the free software distribution system which is
440	+	implemented by public license practices. Many people have made
441	+	generous contributions to the wide range of software distributed
442	+	through that system in reliance on consistent application of that
443	+	system; it is up to the author/donor to decide if he or she is willing
444	+	to distribute software through any other system and a licensee cannot
445	+	impose that choice.
446	+	“Swap”
447	+	This section is intended to make thoroughly clear what is believed to
448	+	be a consequence of the rest of this License.
449	+	“88,000002”
450	+	  12. If the distribution and/or use of the Library is restricted in
451	+	certain countries either by patents or by copyrighted interfaces, the
452	+	original copyright holder who places the Library under this License
453	+	may add an explicit geographical distribution limitation excluding those
454	+	countries, so that distribution is permitted only in or among
455	+	countries not thus excluded. In such case, this License incorporates
456	+	the limitation as if written in the body of this License.
457	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
458	+	  13. The Free Software Foundation may publish revised and/or new
459	+	versions of the Lesser General Public License from time to time.
460	+	Such new versions will be similar in spirit to the present version,
461	+	but may differ in detail to address new problems or concerns.
462	+	Bluestack
463	+	Each version is given a distinguishing version number. If the Library
464	+	specifies a version number of this License which applies to it and
465	+	"any later version", you have the option of following the terms and
466	+	conditions either of that version or of any later version published by
467	+	the Free Software Foundation. If the Library does not specify a
468	+	license version number, you may choose any version ever published by
469	+	the Free Software Foundation.
470	+	Bluestack
471	+	  14. If you wish to incorporate parts of the Library into other free
472	+	programs whose distribution conditions are incompatible with these,
473	+	write to the author to ask for permission. For software which is
474	+	copyrighted by the Free Software Foundation, write to the Free
475	+	Software Foundation; we sometimes make exceptions for this. Our
476	+	decision will be guided by the two goals of preserving the free status
477	+	of all derivatives of our free software and of promoting the sharing
478	+	and reuse of software generally.
479	+	“Send”
480	+	NO WARRANTY
481	+	“Swap”
482	+	  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
483	+	WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
484	+	EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
485	+	OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
486	+	KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
487	+	IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
488	+	PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
489	+	LIBRARY IS WITH YOU. SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
490	+	THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
491	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
492	+	  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
493	+	WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
494	+	AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
495	+	FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
496	+	CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
497	+	LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
498	+	RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
499	+	FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
500	+	SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
501	+	DAMAGES.
502	+	“88,000002”
503	+	                  END OF TERMS AND CONDITIONS
504	+	Bluestack
505	+	                        How to Apply These Terms to Your New Libraries
506	+	DESKTOP-AHV46I9  
507	+	If you develop a new library, and you want it to be of the greatest
508	+	possible use to the public, we recommend making it free software that
509	+	everyone can redistribute and change. You can do so by permitting
510	+	redistribution under these terms (or, alternatively, under the terms
511	+	of the ordinary General Public License).
512	+	Bluestack
513	+	To apply these terms, attach the following notices to the library.
514	+	It is safest to attach them to the start of each source file to most
515	+	effectively convey the exclusion of warranty; and each file should
516	+	have at least the "copyright" line and a pointer to where the full
517	+	notice is found.
518	+	“Send”
519	+	“Send”
520	+	  <one line to give the library's name and a brief idea of what it does.>
521	+	  Copyright (C) <year> <name of author>
522	+	“Swap”
523	+	  This library is free software; you can redistribute it and/or
524	+	  modify it under the terms of the GNU Lesser General Public
525	+	  License as published by the Free Software Foundation; either
526	+	  version 2.1 of the License, or (at your option) any later version.
527	+	“88,000002”
528	+	  This library is distributed in the hope that it will be useful,
529	+	  but WITHOUT ANY WARRANTY; without even the implied warranty of
530	+	  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
531	+	  Lesser General Public License for more details.
532	+	“88,000002”
533	+	  You should have received a copy of the GNU Lesser General Public
534	+	  License along with this library; if not, write to the Free Software
535	+	  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
536	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
537	+	Also add information on how to contact you by electronic and paper mail.
538	+	“88,000002”
539	+	You should also get your employer (if you work as a programmer) or
540	+	your school, if any, to sign a "copyright disclaimer" for the library,
541	+	if necessary. Here is a sample; alter the names:
542	+	DESKTOP-AHV46I9  
543	+	  Yoyodyne, Inc., hereby disclaims all copyright interest in the
544	+	  library `Frob' (a library for tweaking knobs) written by James
545	+	  Random Hacker.
546	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
547	+	  <signature of Ty Coon>, 1 April 1990
548	+	Ty Coon, President of Vice
549	+	“Send”
550	+	That's all there is to it!
551	+	“Swap”
552	+	#############################################################################
553	+	“88,000002”
554	+	Copyright 2008 Google Inc. All rights reserved.
555	+	“88,000002”
556	+	Redistribution and use in source and binary forms, with or without
557	+	modification, are permitted provided that the following conditions are
558	+	met:
559	+	“88,000002”
560	+	  * Redistributions of source code must retain the above copyright
561	+	notice, this list of conditions and the following disclaimer.
562	+	  * Redistributions in binary form must reproduce the above
563	+	copyright notice, this list of conditions and the following disclaimer
564	+	in the documentation and/or other materials provided with the
565	+	distribution.
566	+	  * Neither the name of Google Inc. nor the names of its
567	+	contributors may be used to endorse or promote products derived from
568	+	this software without specific prior written permission.
569	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
570	+	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
571	+	"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
572	+	LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
573	+	A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
574	+	OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
575	+	SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
576	+	LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
577	+	DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
578	+	THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
579	+	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
580	+	OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
581	+	Bluestack
582	+	Code generated by the Protocol Buffer compiler is owned by the owner
583	+	of the input file used when generating it. This code is not
584	+	standalone and requires a support library to be linked with it. This
585	+	support library is itself covered by the above license.
586	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
587	+	#############################################################################
588	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
589	+	             Apache License
590	+	                  Version 2.0, January 2004
591	+	          http://www.apache.org/licenses/
592	+	DESKTOP-AHV46I9  
593	+	   AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
594	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
595	+	  1. Definitions.
596	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
597	+	    "License" shall mean the terms and conditions for use, reproduction,
598	+	     and distribution as defined by Sections 1 through 9 of this document.
599	+	     Bluestack
600	+	     "Licensor" shall mean the copyright owner or entity authorized by
601	+	     the copyright owner that is granting the License.
602	+	     DESKTOP-AHV46I9  
603	+	     "Legal Entity" shall mean the union of the acting entity and all
604	+	     other entities that control, are controlled by, or are under common
605	+	     control with that entity. For the purposes of this definition,
606	+	     "control" means (i) the power, direct or indirect, to cause the
607	+	     direction or management of such entity, whether by contract or
608	+	     otherwise, or (ii) ownership of fifty percent (50%) or more of the
609	+	     outstanding shares, or (iii) beneficial ownership of such entity.
610	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
611	+	     "You" (or "Your") shall mean an individual or Legal Entity
612	+	     exercising permissions granted by this License.
613	+	     Bluestack
614	+	     "Source" form shall mean the preferred form for making modifications,
615	+	     including but not limited to software source code, documentation
616	+	     source, and configuration files.
617	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
618	+	    "Object" form shall mean any form resulting from mechanical
619	+	     transformation or translation of a Source form, including but
620	+	     not limited to compiled object code, generated documentation,
621	+	     and conversions to other media types.
622	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
623	+	    "Work" shall mean the work of authorship, whether in Source or
624	+	     Object form, made available under the License, as indicated by a
625	+	     copyright notice that is included in or attached to the work
626	+	     (an example is provided in the Appendix below).
627	+	     Bluestack
628	+	    "Derivative Works" shall mean any work, whether in Source or Object
629	+	     form, that is based on (or derived from) the Work and for which the
630	+	     editorial revisions, annotations, elaborations, or other modifications
631	+	     represent, as a whole, an original work of authorship. For the purposes
632	+	     of this License, Derivative Works shall not include works that remain
633	+	  s  eparable from, or merely link (or bind by name) to the interfaces of,
634	+	     the Work and Derivative Works thereof.
635	+	“88,000002”
636	+	    "Contribution" shall mean any work of authorship, including
637	+	     the original version of the Work and any modifications or additions
638	+	     to that Work or Derivative Works thereof, that is intentionally
639	+	     submitted to Licensor for inclusion in the Work by the copyright owner
640	+	     or by an individual or Legal Entity authorized to submit on behalf of
641	+	     the copyright owner. For the purposes of this definition, "submitted"
642	+	     means any form of electronic, verbal, or written communication sent
643	+	     to the Licensor or its representatives, including but not limited to
644	+	     communication on electronic mailing lists, source code control systems,
645	+	     and issue tracking systems that are managed by, or on behalf of, the
646	+	     Licensor for the purpose of discussing and improving the Work, but
647	+	     excluding communication that is conspicuously marked or otherwise
648	+	     designated in writing by the copyright owner as "Not a Contribution."
649	+	“88,000002”
650	+	    "Contributor" shall mean Licensor and any individual or Legal Entity
651	+	     on behalf of whom a Contribution has been received by Licensor and
652	+	     subsequently incorporated within the Work.
653	+	     Bluestack
654	+	 2.  Grant of Copyright License. Subject to the terms and conditions of
655	+	     this License, each Contributor hereby grants to You a perpetual,
656	+	     worldwide, non-exclusive, no-charge, royalty-free, irrevocable
657	+	     copyright license to reproduce, prepare Derivative Works of,
658	+	     publicly display, publicly perform, sublicense, and distribute the
659	+	     Work and such Derivative Works in Source or Object form.
660	+	     DESKTOP-AHV46I9  
661	+	  3. Grant of Patent License. Subject to the terms and conditions of
662	+	     this License, each Contributor hereby grants to You a perpetual,
663	+	     worldwide, non-exclusive, no-charge, royalty-free, irrevocable
664	+	     (except as stated in this section) patent license to make, have made,
665	+	     use, offer to sell, sell, import, and otherwise transfer the Work,
666	+	     where such license applies only to those patent claims licensable
667	+	     by such Contributor that are necessarily infringed by their
668	+	     Contribution(s) alone or by combination of their Contribution(s)
669	+	     with the Work to which such Contribution(s) was submitted. If You
670	+	     institute patent litigation against any entity (including a
671	+	     cross-claim or counterclaim in a lawsuit) alleging that the Work
672	+	     or a Contribution incorporated within the Work constitutes direct
673	+	     or contributory patent infringement, then any patent licenses
674	+	     granted to You under this License for that Work shall terminate
675	+	     as of the date such litigation is filed.
676	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
677	+	  4. Redistribution. You may reproduce and distribute copies of the
678	+	     Work or Derivative Works thereof in any medium, with or without
679	+	     modifications, and in Source or Object form, provided that You
680	+	     meet the following conditions:
681	+	“88,000002”
682	+	 (a) You must give any other recipients of the Work or
683	+	     Derivative Works a copy of this License; and
684	+	     DESKTOP-AHV46I9  
685	+	 (b) You must cause any modified files to carry prominent notices
686	+	     stating that You changed the files; and
687	+	     x84811d901063391658ddaCb6Dbc6926d9014038D
688	+	 (c) You must retain, in the Source form of any Derivative Works
689	+	     that You distribute, all copyright, patent, trademark, and
690	+	     attribution notices from the Source form of the Work,
691	+	     excluding those notices that do not pertain to any part of
692	+	     the Derivative Works; and
693	+	     “Send”
694	+	 (d) If the Work includes a "NOTICE" text file as part of its
695	+	     distribution, then any Derivative Works that You distribute must
696	+	     include a readable copy of the attribution notices contained
697	+	     within such NOTICE file, excluding those notices that do not
698	+	     pertain to any part of the Derivative Works, in at least one
699	+	     of the following places: within a NOTICE text file distributed
700	+	     as part of the Derivative Works; within the Source form or
701	+	     documentation, if provided along with the Derivative Works; or,
702	+	     within a display generated by the Derivative Works, if and
703	+	     wherever such third-party notices normally appear. The contents
704	+	     of the NOTICE file are for informational purposes only and
705	+	     do not modify the License. You may add Your own attribution
706	+	     notices within Derivative Works that You distribute, alongside
707	+	     or as an addendum to the NOTICE text from the Work, provided
708	+	     that such additional attribution notices cannot be construed
709	+	     as modifying the License.
710	+	     “Send”
711	+	     You may add Your own copyright statement to Your modifications and
712	+	     may provide additional or different license terms and conditions
713	+	     for use, reproduction, or distribution of Your modifications, or
714	+	     for any such Derivative Works as a whole, provided Your use,
715	+	     reproduction, and distribution of the Work otherwise complies with
716	+	     the conditions stated in this License.
717	+	     “Swap”
718	+	  5. Submission of Contributions. Unless You explicitly state otherwise,
719	+	     any Contribution intentionally submitted for inclusion in the Work
720	+	     by You to the Licensor shall be under the terms and conditions of
721	+	     this License, without any additional terms or conditions.
722	+	     Notwithstanding the above, nothing herein shall supersede or modify
723	+	     the terms of any separate license agreement you may have executed
724	+	     with Licensor regarding such Contributions.
725	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
726	+	  6. Trademarks. This License does not grant permission to use the trade
727	+	     names, trademarks, service marks, or product names of the Licensor,
728	+	     except as required for reasonable and customary use in describing the
729	+	     origin of the Work and reproducing the content of the NOTICE file.
730	+	     Bluestack
731	+	  7. Disclaimer of Warranty. Unless required by applicable law or
732	+	     agreed to in writing, Licensor provides the Work (and each
733	+	     Contributor provides its Contributions) on an "AS IS" BASIS,
734	+	     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
735	+	     implied, including, without limitation, any warranties or conditions
736	+	     of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
737	+	     PARTICULAR PURPOSE. You are solely responsible for determining the
738	+	    appropriateness of using or redistributing the Work and assume any
739	+	     risks associated with Your exercise of permissions under this License.
740	+	“88,000002”
741	+	  8. Limitation of Liability. In no event and under no legal theory,
742	+	     whether in tort (including negligence), contract, or otherwise,
743	+	     unless required by applicable law (such as deliberate and grossly
744	+	     negligent acts) or agreed to in writing, shall any Contributor be
745	+	     liable to You for damages, including any direct, indirect, special,
746	+	     incidental, or consequential damages of any character arising as a
747	+	     result of this License or out of the use or inability to use the
748	+	     Work (including but not limited to damages for loss of goodwill,
749	+	     work stoppage, computer failure or malfunction, or any and all
750	+	     other commercial damages or losses), even if such Contributor
751	+	     has been advised of the possibility of such damages.
752	+	     0x84811d901063391658ddaCb6Dbc6926d9014038D
753	+	  9. Accepting Warranty or Additional Liability. While redistributing
754	+	     the Work or Derivative Works thereof, You may choose to offer,
755	+	     and charge a fee for, acceptance of support, warranty, indemnity,
756	+	     or other liability obligations and/or rights consistent with this
757	+	     License. However, in accepting such obligations, You may act only
758	+	     on Your own behalf and on Your sole responsibility, not on behalf
759	+	     of any other Contributor, and only if You agree to indemnify,
760	+	     defend, and hold each Contributor harmless for any liability
761	+	     incurred by, or claims asserted against, such Contributor by reason
762	+	     of your accepting any such warranty or additional liability.
763	+	     Bluestack
764	+	     END OF TERMS AND CONDITIONS
765	+	     Bluestack
766	+	     APPENDIX: How to apply the Apache License to your work.
767	+	     DESKTOP-AHV46I9  
768	+	     To apply the Apache License to your work, attach the following
769	+	     boilerplate notice, with the fields enclosed by brackets "[]"
770	+	     replaced with your own identifying information. (Don't include
771	+	     the brackets!) The text should be enclosed in the appropriate
772	+	     comment syntax for the file format. We also recommend that a
773	+	     file or class name and description of purpose be included on the
774	+	  same "printed page" as the copyright notice for easier
775	+	  identification within third-party archives.
776	+	“88,000002”
777	+	  Copyright [yyyy] [name of copyright owner]
778	+	  0x84811d901063391658ddaCb6Dbc6926d9014038D
779	+	  Licensed under the Apache License, Version 2.0 (the "License");
780	+	  you may not use this file except in compliance with the License.
781	+	  You may obtain a copy of the License at
782	+	  Bluestack
783	+	     http://www.apache.org/licenses/LICENSE-2.0
784	+	  Bluestack
785	+	  Unless required by applicable law or agreed to in writing, software
786	+	  distributed under the License is distributed on an "AS IS" BASIS,
787	+	  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
788	+	  See the License for the specific language governing permissions and
789	+	  limitations under the License.
790	+	  “Send”
791	+	  “Send”
792	+	  “Send”
793	+	## Runtime Library Exception to the Apache 2.0 License: ##
794	+	  “Send”
795	+	  “Send”
796	+	  As an exception, if you use this Software to compile your source code and
797	+	  portions of this Software are embedded into the binary product as a result,
798	+	  you may redistribute such product without providing attribution as would
799	+	  otherwise be required by Sections 4(a), 4(b) and 4(d) of the License.
800	+	“Swap”
801	+	#############################################################################
802	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
803	+	Boost Software License - Version 1.0 - August 17th, 2003
804	+	Bluestack
805	+	Permission is hereby granted, free of charge, to any person or organization
806	+	obtaining a copy of the software and accompanying documentation covered by
807	+	this license (the "Software") to use, reproduce, display, distribute,
808	+	execute, and transmit the Software, and to prepare derivative works of the
809	+	Software, and to permit third-parties to whom the Software is furnished to
810	+	do so, all subject to the following:
811	+	DESKTOP-AHV46I9  
812	+	The copyright notices in the Software and this entire statement, including
813	+	the above license grant, this restriction and the following disclaimer,
814	+	must be included in all copies of the Software, in whole or in part, and
815	+	all derivative works of the Software, unless such copies or derivative
816	+	works are solely in the form of machine-executable object code generated by
817	+	a source language processor.
818	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
819	+	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
820	+	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
821	+	FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
822	+	SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
823	+	FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
824	+	ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
825	+	DEALINGS IN THE SOFTWARE.
826	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
827	+	#############################################################################
828	+	“88,000002”
829	+	The MIT License (MIT)
830	+	DESKTOP-AHV46I9  
831	+	Copyright (c) 2013 Tomas Dzetkulic
832	+	Copyright (c) 2013 Pavol Rusnak
833	+	“Send”
834	+	Permission is hereby granted, free of charge, to any person obtaining a copy
835	+	of this software and associated documentation files (the "Software"), to deal
836	+	in the Software without restriction, including without limitation the rights
837	+	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
838	+	copies of the Software, and to permit persons to whom the Software is
839	+	furnished to do so, subject to the following conditions:
840	+	“Swap”
841	+	The above copyright notice and this permission notice shall be included in all
842	+	copies or substantial portions of the Software.
843	+	0x84811d901063391658ddaCb6Dbc6926d9014038D
844	+	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
845	+	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
846	+	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
847	+	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
848	+	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
849	+	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
850		SOFTWARE.

---
## [LBPHacker/The-Powder-Toy](https://github.com/LBPHacker/The-Powder-Toy)@[fb9cba0d01...](https://github.com/LBPHacker/The-Powder-Toy/commit/fb9cba0d01b211a949bc36a3cfc8e70a07f0b6b4)
#### Saturday 2023-12-16 10:48:13 by Tamás Bálint Misius

Some native clipboard support for some platforms

I was hoping SDL2 would get this functionality eventually, but nope, proper clipboard support is staged for SDL3, which we're not going to see much of for at least a few more months. This will have to do for 98.0. The feature can be disabled at runtime from powder.pref.

Implementation status:

 - windows (via winapi): has the most friendly api so of course the implementation is flawless and uses every available optimization >_>
 - macos (via cocoa): I'm bad at cocoa so this is only as good as absolutely necessary; TODO: on-demand rendering
 - x11 (via xclip): I am NOT implementing icccm2; TODO: remove reliance on external tools
 - wayland (via wl-clipboard): oh god wayland oh why, you're almost as bad as x11; TODO: remove reliance on external tools
 - android: TODO; is there even a point?
 - emscripten: TODO; the tricky bit is that in a browser we can only get clipboard data when the user is giving it to us, so this will require some JS hackery that I'm not mentally prepared for right now; also I think the supported content types are very limited and you can't just define your own

x11 and wayland support are handled by a common backend which delegates clipboard management to xclip-like external programs, such as xclip itself or wl-clipboard, and can load custom command line templates from powder.pref for use with other such programs.

---
## [nabin154/Globetalk-mern_chatApp](https://github.com/nabin154/Globetalk-mern_chatApp)@[a8b9845ede...](https://github.com/nabin154/Globetalk-mern_chatApp/commit/a8b9845edefc2a062f2f691f8657e7523466ce64)
#### Saturday 2023-12-16 11:59:33 by Nabin Bhandari

Create README.md

GlobeTalk is an innovative and feature-rich chat application designed to connect users globally, breaking down language barriers and enhancing communication through real-time messaging, group chats, multimedia sharing, and secure audio-video calls. Built on the MERN stack (MongoDB, Express.js, React.js, Node.js), GlobeTalk integrates cutting-edge technologies to provide a seamless and dynamic chatting experience.

Key Features:

Real-Time Messaging with Socket.io:

Enjoy instant messaging with real-time updates, ensuring a smooth and responsive chat experience.
Leverage Socket.io for seamless communication between users.
Real-Time Notifications:

Stay informed with real-time notifications for new messages, friend requests, and group activity.
Group Chats:

Create and join group chats to engage in conversations with multiple users simultaneously.
Admin capabilities for managing group settings and members.
Multimedia Sharing:

Share images within the chat for a richer communication experience.
Audio-Video Calls using WebRTC:

Initiate secure audio and video calls directly from the chat interface using WebRTC.
Enjoy high-quality, real-time communication with friends and colleagues.
End-to-End Encryption (AES):

Ensure the privacy and security of your conversations with AES encryption for all messages.
Language Translation:

Break language barriers with real-time language translation of messages.
Users can dynamically update their preferred language, and original messages are easily viewable with a toggle button.
Online User Tracking:

See who's online in real-time and initiate conversations with available users.
User Recommendations using Haversine:

Utilize Haversine formula for distance calculation to recommend nearby friends.
Enhance your social network by connecting with users in close proximity.
Technical Stack:

Frontend: React.js for a responsive and dynamic user interface.
Backend: Node.js and Express.js for server-side logic.
Database: MongoDB for efficient data storage.
WebSockets: Socket.io for real-time communication.
Encryption: AES for end-to-end message encryption.
Audio-Video Calls: WebRTC for secure real-time communication.
Conclusion:
GlobeTalk is not just a chat application; it's a comprehensive platform that prioritizes real-time communication, privacy, security, and breaking down language barriers. Connect with friends, family, and colleagues seamlessly while enjoying an array of cutting-edge features designed to make global communication more accessible and enjoyable.

---
## [Aquilar/Paradise](https://github.com/Aquilar/Paradise)@[6a109ade7f...](https://github.com/Aquilar/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Saturday 2023-12-16 12:43:27 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [arthur-mountain/react](https://github.com/arthur-mountain/react)@[1ebedbec2b...](https://github.com/arthur-mountain/react/commit/1ebedbec2bec08e07c286ea6c3cff62737a0fd3a)
#### Saturday 2023-12-16 13:05:52 by Sebastian Markbåge

Add Server Context deprecation warning (#27424)

As agreed, we're removing Server Context. This was never official
documented.

We've found that it's not that useful in practice. Often the better
options are:

- Read things off the url or global scope like params or cookies.
- Use the module system for global dependency injection.
- Use `React.cache()` to dedupe multiple things instead of computing
once and passing down.

There are still legit use cases for Server Context but you have to be
very careful not to pass any large data, so in generally we recommend
against it anyway.

Yes, prop drilling is annoying but it's not impossible for the cases
this is needed. I would personally always pick it over Server Context
anyway.

Semantically, Server Context also blocks object deduping due to how it
plays out with Server Components that can't be deduped. This is much
more important feature.

Since it's already in canary along with the rest of RSC, we're adding a
warning for a few versions before removing completely to help migration.

---------

Co-authored-by: Josh Story <josh.c.story@gmail.com>

---
## [fira/cmss13](https://github.com/fira/cmss13)@[dc234c9939...](https://github.com/fira/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Saturday 2023-12-16 13:06:42 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [lukevale/Skyrat-tg](https://github.com/lukevale/Skyrat-tg)@[4aa870eb5d...](https://github.com/lukevale/Skyrat-tg/commit/4aa870eb5d106922f41d022bb1526db7b6074afe)
#### Saturday 2023-12-16 13:24:04 by SkyratBot

[MIRROR] Pipe painting, spraycan preset colors [MDB IGNORE] (#24974)

* Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

* Pipe painting, spraycan preset colors

---------

Co-authored-by: Andrew <mt.forspam@gmail.com>

---
## [catfooo/mern-tutorial-with-connectedprojectmongoapi](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi)@[7a04fd17d9...](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi/commit/7a04fd17d98654ee1d2ceab56e279d36d10b1573)
#### Saturday 2023-12-16 14:24:27 by So Youn Choi

i had bad day while dealing with this. to summary, let me complain here before close my laptop. so, i thought this might be good place to test. so wanted to play the video again from the beginning. the guy there was using code . to open vscode. i mean i dont need to try that, but since i was able to use that, and it was comfortable to open vscode with code ., i sticked on that. i asked and asked chatgpt and it showed me weird answer. just about to cry, i noticed it is 15:15. i need to leave, annars, angry person that works here will come to me and i dont want to fight with that guy. anyway, i have habit that stick with not important small features, not seeing the whole forest. it worked somehow with revealing two continuous error today with w14 project repo, but not for code . for this moment. i needed to quit, and i needed someone to watch me and say me to quit. someone that might wiser than me to see the whole scene that im struggling. so... my whole day, my whole bootcamp days were like this, and i dont think it is useful, im learning by this way. it is rather torture. and i dont like that. listen, i needed someone to help me, teacher or collegue or somewhat, expecting that, i applyed for this bootcamp. which not happened me at all. no, not at all i mean, probably i got  0.00001 percent of help that i might needed, but it was so little for me. the thing is i cant escape, bcs i start, bcs if i escape that means every momnent that i used to this means nothing. i want result somewhat, so i will be sticked to here, suffering, with no hope. idk what is wrong. i cant see myself in 3rd point of view. but something is wrong, bcs it doesnt makes sence that i have to feel this much pain and get nothing. and paying. and using time and energy. i almost lost my life because i joined here, and what i get back is just nothing more than bunch of pain. to summary, i was able to use code . , at that moment, several weeks ago, it wasnt done without setting. i did setting with chatgpt and it was smooth. so i was expecting same thing today as well, but not for today. so i hope when i work, someone might watching me and guide me. i want to be happy while i work...

---
## [moul/gno](https://github.com/moul/gno)@[24d89a4f5d...](https://github.com/moul/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Saturday 2023-12-16 14:26:05 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [catfooo/mern-tutorial-with-connectedprojectmongoapi](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi)@[bb4629424a...](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi/commit/bb4629424a9614eb2dc91b76cfda8ae7897ec67f)
#### Saturday 2023-12-16 14:36:28 by So Youn Choi

but i dont want to get out of here while crying. what might make me happy? this happened bcs of people, so i need people. but i cant achieve people in this way. in order to become bit neutral, i turned off my browser hiding with screen that has no meaning. yea, this looks better, no problem if i dont try to read the tab. and lets plan what im going to do today. fighting with two continuous err msg, it made my stomach not working well. i cant eat, if i eat it may the same problem occur. my gut is rly weak and had many problem before, so need to watch out. 15:28, pls do best and leave the right time. i was planning to eat bcs this is the rare day that i try to eat outside, bcs cafe here closes early or not open at weekend. so eat in dangerous env or give up that. oh my, my body starts to feel itcy every single part. due to bad feeling? or due to my problem that i already had in my body? but yea, ill eat, and dont care that happens afterwards. i have energy to ignore others and focus myself. the best decision for me is get back the energy and come back here at right time. i mean, i love my job. if i hated this, i wouldnt try it single moment. i liked this, so i could keep going on although every not happy moment that happened and happening. i like this itself, so i dont worry they are firing people. i just wanted to keep going on spending time that i love to do. so, although i feel lost, i love what i am doing, so i wont stop and keep going, know better, perform better, which means i will manage to come back. i love my life, this had been my life, and made me keep alive. so i think i forgot everything, no feeling behind, and what i do is just keep doing

---
## [ultimateshadsform/card-generator](https://github.com/ultimateshadsform/card-generator)@[477007a75c...](https://github.com/ultimateshadsform/card-generator/commit/477007a75c62d441bda24b33a6a7eb15a2a05452)
#### Saturday 2023-12-16 14:51:56 by Alexander Carlsson

I HATE GIT WHY DOES IT KEEP THE DAMN FILES FOR FUCKS SAKE

---
## [Sereath/Unyielding](https://github.com/Sereath/Unyielding)@[eb7ad655ac...](https://github.com/Sereath/Unyielding/commit/eb7ad655ac33ffefdf380a356f8667db88336d44)
#### Saturday 2023-12-16 14:59:46 by Sereath

0.2.0

- Music Triggers:
Now there will be different tracks for day and night for the overworld
Variety is the spice of life

- Ender Skills:
Max speed boost for Mobility-Wind-Speed Boost
from 99% back to 100%, otherwise it really is useless. Careful with hurting yourself again.

- Enchanting Plus:
S:costFactor=15.0 -> 7.0

- Grimoire of Gaia:
I:spawnAnubis=40 -> 30
Now always spawns as a champion

I:spawnArachne=60 -> 50
I:spawnCreep=60 -> 40
I:spawnEnderEye=40 -> 30
I:spawnMatango=50 -> 40
I:spawnMinotaur=40 -> 20
Minimum 2 star champion now

I:spawnSelkie=50 -> 40
I:spawnSiren=50 -> 40

- InControl:
Bonus experience for The Aurorian: +25%
Bonus experience for the overworld at night: +25%

Mob counters for ant hills, wetas and stonelings

- Extended Crafting:
Recipes for the Enchanting Plus table and its upgrade
Recipe for Ender Skills skillbook

---
## [DarthCooper/FBLA-Computer-Game-And-Simulation-2023-2024](https://github.com/DarthCooper/FBLA-Computer-Game-And-Simulation-2023-2024)@[5ab69f8f33...](https://github.com/DarthCooper/FBLA-Computer-Game-And-Simulation-2023-2024/commit/5ab69f8f330490c416ca8b0f76f88fed2aff4835)
#### Saturday 2023-12-16 15:47:18 by DarthCooper

Holy shit. It's finally working.

God damn, that was unnecessarily hard.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[05c682182b...](https://github.com/mrakgr/The-Spiral-Language/commit/05c682182bcb700225de753fef470fd1d5519520)
#### Saturday 2023-12-16 15:52:17 by mrakgr

"11:30pm. https://developer.nvidia.com/blog/mixed-precision-programming-cuda-8/

I am working on sampling cards from a deck. Instead of iterating across the entire deck like a doofus, I think I am just going to use rejection sampling for putting in the cards.

That having said. It might now be a bad idea to just copy paste the code from Leduc and call it a day.

https://docs.nvidia.com/cuda/cuda-math-api/group__CUDA__MATH__INTRINSIC__INT.html#group__CUDA__MATH__INTRINSIC__INT_1g2fc8e909eb9a959dcc3262e54365bfc5

It doesn't have parallel deposit, but it does have this one.

I should be using this to speed up the deposit.

It is just wrong to do a 64 iteration loop every time I want to index into an int.

https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#integer-arithmetic-instructions-fns

11:55 AM. Actually, it's worth thinking about this. The single extraction. If I was doing a 30 bit integer would be enough to get me exactly what I want, but I need a 64 bit one. So what I need to do is a bit different. I'm going to have to combine this with a bit count 1.

Let me just take a look at all of these instructions, the. good and intrinsics aren't the same thing.

https://docs.nvidia.com/cuda/cuda-math-api/group__CUDA__MATH__INTRINSIC__INT.html#group__CUDA__MATH__INTRINSIC__INT_1g43c9c7d2b9ebf202ff1ef5769989be46

Hmmm, ok, let's do what I want. I'll do this step by step.

12:20pm.

```spiral
// Gets the position of the i-th set bit in a pair of u32 masks.
inl sample_masked_bit (a,b : u32 * u32) (i : u32) =
    inl popc (x : u32) : u32 = $"__popc(!x)"
    inl fns (mask : u32) (offset : u32) : u32 = $"__fns(!mask,0,!offset)"
    inl a_popc = popc a
    if i < a_popc then fns a i else fns b (i - a_popc) + 32
```

This is...

Ah wait...

```spiral
// Gets the position of the i-th (starting at 0) set bit in a pair of u32 masks.
inl sample_masked_bit (a,b : u32 * u32) (i : u32) =
    inl popc (x : u32) : u32 = $"__popc(!x)"
    inl fns (mask : u32) (offset : u32) : u32 = $"__fns(!mask,0,!offset+1)"
    inl a_popc = popc a
    if i < a_popc then fns a i else fns b (i - a_popc) + 32
```

I forgot the offset needs to start at 1.

Not bad.

Now, instead of a big **** loop, what I have is a very efficient ifs statement that uses cuda intrinsics.This is almost a good as a single parallel deposit instruction.

It is certainly much better than an imperative loop or an rejection sampling scheme.

OK, let me take a break here and then I'll focus on testing this out. I want to make sure that this function works as I think it should.

2:50pm.

///

The following are the unary operators in C:
- Unary minus ( - )
- Increment ( ++ )
- Decrement ( -- )
- NOT ( ! )
- Addressof operator ( & )
- sizeof ()

The tilde operator ( ~ ) is a **bitwise** operator in C, not a unary operator. It is used to invert the bits of an integer. For example, if `x` is `5` (binary `101`), then `~x` is `-6` (binary `010`)¹.

Source: Conversation with Bing, 12/16/2023
(1) Unary operators in C/C++ - GeeksforGeeks. https://www.geeksforgeeks.org/unary-operators-cc/.
(2) C Unary Operators | Microsoft Learn. https://learn.microsoft.com/en-us/cpp/c-language/c-unary-operators?view=msvc-170.
(3) Unary Operator in C - javatpoint. https://www.javatpoint.com/unary-operator-in-c.

///

https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/symbol-and-operator-reference/bitwise-operators

Let me add bitwise negation to the language, as it seems I need it.

///

Activating extension 'mrakgr.spiral-lang-vscode' failed: Cannot find module 'd:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\out\index.js'
Require stack:
- c:\Users\mrakg\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\loader.js
- c:\Users\mrakg\AppData\Local\Programs\Microsoft VS Code\resources\app\out\bootstrap-amd.js
- c:\Users\mrakg\AppData\Local\Programs\Microsoft VS Code\resources\app\out\bootstrap-fork.js
- .

///

3:45 PM. I just got to do an npm install here. No biggie.

```spiral
inl test3() =
    open inv_arraym
    inl out : inv_array array _ = create 512
    inl grid_range () : int = $"gridDim.x * blockDim.x"
    inl linear_id () : int = $"threadIdx.x + blockIdx.x * blockDim.x"

    inl blocks = 16
    inl grids = divup (length out) blocks
    run grids blocks (fun () =>
        globals()
        inl from = linear_id()
        inl x : _ philox_state = init {seed=conv from; subsequence=0; offset=0}
        loop.forBy {from nearTo=length out; by=grid_range()} (fun i () =>
            inl r = u64 x
            inl popc (x : u64) : u64 = $"__popcll(!x)"
            if popc r > 0 then
                inl i = u32_range {from=0; nearTo=popc r |> conv} x |> sample_masked_bit_u64 r
                inl x = r &&& ~~~(1 <<< conv i)
                i, r - x
            else
                0, 0
            |> set out i
            ) ()
        )
    out
```

Here is the test. Everything so far looks fine.

I don't need to compare it with another version of the sample masked bit. Let me see if I can dig up the FPGA version.

```spiral
let sample_without forall dim dim'. (mask : ap_uint dim) rng =
    pragma.pipeline {ii=1}
    open ap_uintm
    inl nearTo : u32 = loop.for {from=0; nearTo=length mask} (fun i s => if bool (index mask i) then s else s+1) 0
    inl (c : ap_uint dim'),rng = random_ap_in_range {from= @0; nearTo= #nearTo} rng
            inl (i : ap_uint dim'),_ =
                loop.for {from=0; nearTo=length mask} (fun i (_,c as state) =>
                    if c >. @0 then
                        #i, if bool (index mask i) then c else dec c
                    else state
                    ) (@0, inc c)
    {mask=mask ||| (@1 <<< i); index=i; rng}
```

(array([ 5,  0, 12, 12], dtype=uint32), array([1, 0, 0, 0], dtype=uint32), array([2, 0, 2, 2], dtype=uint32), array([1, 0, 1, 1], dtype=uint32), array([1, 0, 1, 1], dtype=uint32), 4)

Debugging this sheet is signing. I should take a break here. For the sake of my hand, at least.

```spiral
    inl sample mask c =
        loop.for {from=0; nearTo=popc_u32 mask} (fun i (_,c as state) =>
            if c > 0 then
                i, if mask &&& (1 <<< conv i) <> 0 then c else c-1
            else state
            ) (0, c+1)
        |> fst
```

I think this sampler is wrong for some reason. I am thinking about the numbers that are coming out of it, and they don't make sense. God **** damn it. Now I am getting frustrated with this **** test. I think I got the sampler that I made right on the first try. And now this one that I filed from the fpga version is wrong. But I did have to adjust that significantly because I don't have those arbitrary precision types. So it's no wonder that I introduced some kind of error.

```spiral
    inl sample mask c =
        loop.for {from=0; nearTo=64u32} (fun i (_,c as state) =>
            if c > 0 then
                i, if mask &&& (1 <<< conv i) = 0 then c else c-1
            else state
            ) (0, c+1)
        |> fst
```

It turns out there was an error there that pop count was completely wrong. The loop was not going all the way through the integer because of it.

```
inl test3() =
    inl popc_u64 (x : u64) : u64 = $"__popcll(!x)"
    inl popc_u32 (x : u32) : u32 = $"__popc(!x)"
    inl sample mask c =
        loop.for {from=0; nearTo=64u32} (fun i (_,c as state) =>
            if c > 0 then
                i, if mask &&& (1 <<< conv i) = 0 then c else c-1
            else state
            ) (0, c+1)
        |> fst

    open inv_arraym
    inl out : inv_array array _ = create (1028*16)
    inl grid_range () : int = $"gridDim.x * blockDim.x"
    inl linear_id () : int = $"threadIdx.x + blockIdx.x * blockDim.x"

    inl blocks = 64
    inl grids = divup (length out) blocks
    run grids blocks (fun () =>
        globals()
        inl from = linear_id()
        inl x : _ philox_state = init {seed=conv from; subsequence=0; offset=0}
        loop.forBy {from nearTo=length out; by=grid_range()} (fun i () =>
            inl r = u64 x
            if popc_u64 r > 0 then
                inl base = u32_range {from=0; nearTo=popc_u64 r |> conv} x
                inl i = base |> sample_masked_bit_u64 r
                inl i' = base |> sample r
                // inl x = r &&& ~~~(1 <<< conv i)
                i - i'
            else
                0
            |> set out i
            ) ()
        )
    inl out = out.arrays
    $"print(cp.sum(!out))"
    ()
```

OK, this is good enough for today. I'm going to stop here because my hand is going to fall off. I might have overdid it.

And doing this test was pretty annoying. But I finally got it through it. There was that error in the newer sample. And once I changed the pop seed to just 64 everything started to work. Honestly, this experience makes me wonder whether Derek has an error in the fpga version.

It's possible it's not like I was very true in testing it.

Anyway, this is good enough. It's time to rest. I'm going to take a bath and watch the Blue Archive for the rest of the day."

---
## [KDE/kate](https://github.com/KDE/kate)@[a04ecbe1c5...](https://github.com/KDE/kate/commit/a04ecbe1c5280b7e6dbf8a2251d770ad4ad08171)
#### Saturday 2023-12-16 16:24:05 by Waqar Ahmed

Improve lsp semanticTokens range highlighting

Currently we debounce whenever the user scrolls the view. This results
in flickering sometimes, especially if the server is not very fast the
flickering can be annoying.

With this change, we optimize in a different way:
- Request highlighting for a bigger range than the current view range
- If the user scrolls, ignore it if the current highlighted range
  contains the scrolled region otherwise request new highlights
  immediately

This results in a much better user experience in my opinion.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[73bdd7341a...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/73bdd7341acdf6f5b7d38a484a1dba8106438c56)
#### Saturday 2023-12-16 16:57:22 by SkyratBot

[MIRROR] TGUI Destructive Analyzer [MDB IGNORE] (#25005)

* TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.

https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

* TGUI Destructive Analyzer

* Modular

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[1f1cdc609d...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/1f1cdc609df04a4749b2f3f5d5500551c86021a8)
#### Saturday 2023-12-16 16:57:22 by Nerevar

[FIX] Fixes Kick Damage (#24996)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [DarrenTsung/aider](https://github.com/DarrenTsung/aider)@[c3e2cf5da0...](https://github.com/DarrenTsung/aider/commit/c3e2cf5da0c46e4b2b5cfca0f893373936ed0742)
#### Saturday 2023-12-16 17:35:49 by Darren Tsung

Add agents and FixAgent implementation

Instead of a human manually running a linter or compiler command repeatedly
and providing the output to aider, we can have aider run the iteration
loop until the provided command succeeds.

I initially thought of implementing this as a new command (e.g. /fix
cargo clippy). But after looking at the code I realized that commands
only result in a single message.

So instead I took inspiration from the --message arg and created a flow
for switching aider to be driven by an agent instead of the interactive
REPL or a single message.

Agents are configured through YAML via a .aider_agent_config at the cwd
or an agent config provided through the args. Right now there is only
FixAgent defined. An example configuration might look like:
```
fix-cargo-clippy:
    type: fix
    command: cargo clippy
    context: |
        Sometimes we use loop {} with an explicit `break` at the end so that the
        code can early exit out of the block at any time. If that looks to be the
        case you can add an #[allow(clippy::never_loop)].
```

Context:
    As seen above, there's a "context" key for adding additional
    context to the AI on how to solve the errors. This is useful in a
    large organization where there might be internal tooling / patterns
    we want to have the AI apply instead of following the generic instructions
    blindly.
Max output lines:
    By default agents will only receive the first 50 lines of the output
    of the command. This is very useful when there are a lot of errors
    in the entire project. Customizable via the max_output_lines key in
    the YAML.
Line numbering:
    Sending up the line numbers really helps the agent accurately
    understand errors reported by linters / compilers / etc.
Dropping files from the context:
    To avoid polluting the context with unnecessary files, the FixAgent
    will drop files from the context every iteration. This causes some
    additional back and forth if the AI needs to work with the file again,
    but otherwise the accuracy will suffer as the agent fixes multiple
    files.

    I tried getting the agent to request files to be dropped of it's own
    accord by editing the system prompt and building a flow for recognizing
    files to drop, but the AI would never request to drop files.. would
    be open to a fix here.

There are a couple use-cases that inspired me to build this that I think
are compelling beyond the basic "fix linter errors".

1)
At work I often run into bazel errors that require interpreting the compile
error, determining whether it's due to 3rd party crates or local monorepo
crates not being updated, and then manually updating a BUILD.bazel file or
running a specific command.

I would like to write an agent configuration once that teaches the AI (through
context) to how to identify these common cases and solve them. This would
also involve providing the agent a way to call whitelisted commands which is
not yet implemented in this commit.

2)
I recently did a wide-scale refactor to replace this function which looked
something like `fooSpecialName(1, None, 10, ("hello", None))` (ugh..) with a builder
pattern like `Foo::new(1).ack_id(10).name("hello")` where the arguments
needed to be conditional on whether they were provided or not (i.e. None
or some value).

I would liked to have configured a FixAgent that searches for instances
of `fooSpecialName` with ripgrep and has the context on how to replace
each instance (I'd probably provide a number of examples).

I ended up writing a python script that did a regex find-and-replace
(written mostly by aider! much better than hand writing it), but it still
had a number of bugs I was too lazy to solve like handling weird arguments
or function calls that were multi-line that I think GPT-4 wouldn't
have any trouble evaluating against.

Unfortunately I'm still in the process of getting aider approved with
my work codebase so I'm not able yet to test out whether FixAgent would
actually work well in the exact complex use-cases above.

In all the cases below, I've been running with the GPT4 turbo model
(gpt-4-1106-preview).

However, I ran a FixAgent to solve all the python linting errors in the
aider codebase as I was developing:
```
fix-python-linting:
    type: fix
    command: ruff check .
```

And I also stress tested the implementation by finding a decently large
open-source repo (https://github.com/RazrFalcon/rustybuzz) with a lot
of clippy errors and running the fix agent to solve it. This led to
learnings like dropping files from the context / max output lines.

Aider is able to make a lot of progress on fixing the errors in this
agent mode, although it does take a while and costs a decent(?) amount.

Re: cost - I want to figure out how much running the agent is costing,
but don't see any flags on how to report that (maybe it depends on API
cost plans?), lemme know if there's a way to do this.

---
## [DarrenTsung/aider](https://github.com/DarrenTsung/aider)@[a4e20560ce...](https://github.com/DarrenTsung/aider/commit/a4e20560ce9d3fdadf9d13b6befd8b4832635279)
#### Saturday 2023-12-16 17:45:57 by Darren Tsung

Add agents and FixAgent implementation

\## Basic Use Case
Instead of a human manually running a linter or compiler command repeatedly
and providing the output to aider, we can have aider run the iteration
loop until the provided command succeeds.

There are more compelling use-cases in the "Complex Use Cases" section,
this is just the high-level idea.

\## Implementation
I initially thought of implementing this as a new command (e.g. /fix
cargo clippy). But after looking at the code I realized that commands
only result in a single message.

So instead I took inspiration from the --message arg and created a flow
for switching aider to be driven by an agent instead of the interactive
REPL or a single message.

Agents are configured through YAML via a .aider_agent_config at the cwd
or an agent config provided through the args. Right now there is only
FixAgent defined. An example configuration might look like:
```
fix-cargo-clippy:
    type: fix
    command: cargo clippy
    context: |
        Sometimes we use loop {} with an explicit `break` at the end so that the
        code can early exit out of the block at any time. If that looks to be the
        case you can add an #[allow(clippy::never_loop)].
```

\## Learnings
Context:
    As seen above, there's a "context" key for adding additional
    context to the AI on how to solve the errors. This is useful in a
    large organization where there might be internal tooling / patterns
    we want to have the AI apply instead of following the generic instructions
    blindly.
Max output lines:
    By default agents will only receive the first 50 lines of the output
    of the command. This is very useful when there are a lot of errors
    in the entire project. Customizable via the max_output_lines key in
    the YAML.
Line numbering:
    Sending up the line numbers really helps the agent accurately
    understand errors reported by linters / compilers / etc.
Dropping files from the context:
    To avoid polluting the context with unnecessary files, the FixAgent
    will drop files from the context every iteration. This causes some
    additional back and forth if the AI needs to work with the file again,
    but otherwise the accuracy will suffer as the agent fixes multiple
    files.

    I tried getting the agent to request files to be dropped of it's own
    accord by editing the system prompt and building a flow for recognizing
    files to drop, but the AI would never request to drop files.. would
    be open to a fix here.

\## Complex Use Cases
There are a couple use-cases that inspired me to build this that I think
are compelling beyond the basic "fix linter errors".

1)
At work I often run into bazel errors that require interpreting the compile
error, determining whether it's due to 3rd party crates or local monorepo
crates not being updated, and then manually updating a BUILD.bazel file or
running a specific command.

I would like to write an agent configuration once that teaches the AI (through
context) to how to identify these common cases and solve them. This would
also involve providing the agent a way to call whitelisted commands which is
not yet implemented in this commit.

2)
I recently did a wide-scale refactor to replace this function which looked
something like `fooSpecialName(1, None, 10, ("hello", None))` (ugh..) with a builder
pattern like `Foo::new(1).ack_id(10).name("hello")` where the arguments
needed to be conditional on whether they were provided or not (i.e. None
or some value).

I would liked to have configured a FixAgent that searches for instances
of `fooSpecialName` with ripgrep and has the context on how to replace
each instance (I'd probably provide a number of examples).

I ended up writing a python script that did a regex find-and-replace
(written mostly by aider! much better than hand writing it), but it still
had a number of bugs I was too lazy to solve like handling weird arguments
or function calls that were multi-line that I think GPT-4 wouldn't
have any trouble evaluating against.

\## Testing
Unfortunately I'm still in the process of getting aider approved with
my work codebase so I'm not able yet to test out whether FixAgent would
actually work well in the exact complex use-cases above.

In all the cases below, I've been running with the GPT4 turbo model
(gpt-4-1106-preview).

However, I ran a FixAgent to solve all the python linting errors in the
aider codebase as I was developing:
```
fix-python-linting:
    type: fix
    command: ruff check .
```

And I also stress tested the implementation by finding a decently large
open-source repo (https://github.com/RazrFalcon/rustybuzz) with a lot
of clippy errors and running the fix agent to solve it. This led to
learnings like dropping files from the context / max output lines.

Aider is able to make a lot of progress on fixing the errors in this
agent mode, although it does take a while and costs a decent(?) amount.

Re: cost - I want to figure out how much running the agent is costing,
but don't see any flags on how to report that (maybe it depends on API
cost plans?), lemme know if there's a way to do this.

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[fb9743f647...](https://github.com/ZacharyTStone/ZacharyTStone/commit/fb9743f647206c41923c09e3d34e8fc4be4ac5f3)
#### Saturday 2023-12-16 18:04:29 by ROBO-ZACH

Update README with new quote: "Think in the morning. Act in the noon. Eat in the evening. Sleep in the night." <br>— William Blake

---
## [RedBaronFlyer/RedBaronFlyer](https://github.com/RedBaronFlyer/RedBaronFlyer)@[274eb2a52e...](https://github.com/RedBaronFlyer/RedBaronFlyer/commit/274eb2a52ecd35f86d1cd83032c655997dc73106)
#### Saturday 2023-12-16 18:22:14 by distributivgesetz

Removes Clone Damage (#80109)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Does what it says on the tin. We don't have any "special" sources of
clone damage left in the game, most of them are rather trivial so I
bunched them together into this PR.

Notable things removed:
- Clonexadone, because its entire thing was centered around clone damage
- Decloner gun, it's also centered around cloning damage, I couldn't
think of a replacement mechanic and nobody uses it anyways
- Everything else already dealt clone damage as a side (rainbow knife
deals a random damage type for example), so these sources were removed

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Consider the four sources of normal damage that you can get: Brute,
Burn, Toxins and Oxygen. These four horsemen of the apocalypse are very
well put together and it's no surprise that they are in the game, as you
can fit any way of damaging a mob into them. Getting beaten to death by
a security officer? Brute damage. Running around on fire? Burn damage.
Poisoned or irradiated? Toxin damage. Suffocating in space? Brute, burn
and oxygen damage. Technically there's also stamina damage but that's
its own ballpark and it also makes sense why we have a damage number for
it.

Picture this now: We have this cool mechanic called "clone pods" where
you can magically revive dead people with absolute ease. We don't want
it to be for free though, it comes at a cost. This cost is clone damage,
and it serves to restrain people from abusing cloning.

Fast forward time a bit and cloning is now removed from the game. What
stays with us is a damage number that is intrinsically tied to the
context of a removed feature. It was a good idea that we had it for that
feature at the time, but now it just sits there. It's the odd one out
from all the other damage types. You can easily explain why your blade
dealt brute damage, but how are you going to fit clone damage into any
context without also becoming extremely specific?

My point is: **clone damage is conceptually a flawed mechanic because it
is too specific**. That is the major issue why no one uses it, and why
that makes it unworthy of being a damage stat.
Don't take my word for it though, because a while ago we only had a
handful of sources for this damage type in the game. And in most of the
rounds where you saw this damage, it came from only one department. It's
not worthwhile to keep it around as a damage number. People also didn't
know what to do with this damage type, so we currently have two ways of
healing clone damage: Cryotubes as a roundstart way of healing clone
damage and Rezadone, which instantly sets your clone damage to 0 on the
first tick. As a medical doctor, when was the last time you saw someone
come in with clone damage and thought to yourself, "Oh, this person has
clone damage, I cannot wait to heal them!" ?

Now we have replacements for these clone damage sources. Slimes? Slime
status effect that deals brute instead of clone. Cosmic heretics? Random
organ damage, because their mechanics are already pretty fleshed out.
Decloning virus? The virus operated as a "ticking timebomb" which used
cloning damage as the timer, so it has been reworked to not use clone
damage. What remains after all this is now a basically unused damage
type. Every specific situation that used clone damage is now relying on
another damage type. Now it's time to put clone damage to rest once and
for all.

Sure, you can technically add some form of cellular degradation in the
future, but it shouldn't be a damage number. The idea of your cells
being degraded is a cool concept, don't get me wrong, but make it a
status effect or maybe even a wound for that matter.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
del: Removed clone damage.
del: Removed the decloner gun.
del: Removed clonexadone.
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[2e656fba14...](https://github.com/Bubberstation/Bubberstation/commit/2e656fba14e0b67086bb4d2eff59d6fa6748a55c)
#### Saturday 2023-12-16 18:26:57 by Cursor

Grants the ability to open Clown slots once more. (#853)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Title. Skyrat disabled it because they hate fun. We don't.

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Say a Clown dies. Is arrested, or is just a bit shit.
What can you do?
Jackshit.
Pray, fax Clown Planet, but why wait on God or the Clown in the High
Castle when you can do it yourself?
This also let's Antags, or Clowns summon more friends. Assuming people
in the lobby wanna be a clown.

P.S. I commented out and unticked the Skyrat file for double safety.
Tried to just override it, didn't work. If you have a better idea for
this. You have the floor.

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Clown slots are re-openable by royal decree. The incident between
Nanotrasen and King Honkington has been resolved.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[eba444c7a1...](https://github.com/elunna/HACKEM-MUCHE/commit/eba444c7a13643891398dd76d6f0da73dc50f915)
#### Saturday 2023-12-16 18:40:00 by Erik Lunna

Buff war hammers into a competitive two-handed weapon.

From xNetHack commit 0b04b8fed6:

'This ups their damage to 2d6 small / 2d8 large. The primary reason for
this change is because d4+1/d4 is ridiculously low and not indicative of
the smashing power of a hammer.

Affected artifacts are Mjollnir and Ogresmasher, with the main intended
beneficiary being Ogresmasher. People have pointed out some nitpicks
with this change's effect on Mjollnir previously:
1) It makes valkyries harder since they can no longer wield it in one
   hand and wear their starting shield in the other. This is fine by me;
   it makes for a more interesting choice whether to forego the shield
   or not, especially since Mjollnir is now better than Excalibur
   damage-wise to non-shock-resistant targets. (Possibly it's too
   powerful, and the 1d24 damage needs to be tuned down a bit.)
2) Norse mythology is very specific about it being short-handled and
   wielded by Thor in one hand. This can be handwaved away as its being
   the hammer of a god, and not necessarily existing at a mortal scale;
   alternatively, due to its famous weight, it's all a mortal can do to
   wield the one-handed weapon with both hands.'

ESL: I think this also complements the changes to unicorn horns and the priest quite nicely. Priests always get Mjollnir for a crowning gift, and this gives them something with a bit more oomph. Valkyries won't have any problems as they just always go for long sword artifacts anyway. This also can serve to take the place of unicorns as a better two-handed weapon, however it may not be easy to find one, it weighs more, it's not erodeproof, and your role may or may not be able to attain proficiency with it - more balanced though!

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[a6d6a3fbb8...](https://github.com/rmellis/HelpUKR-master/commit/a6d6a3fbb85dbe0d69e6b95b013cf0eea0da14a0)
#### Saturday 2023-12-16 19:39:18 by rmellis

Added Day 661 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
lmatel and 2Kom, two major internet providers in the aggressor's capital, were disrupted this morning, impacting countless private, business, and government subscribers. This is all thanks to your efforts and our team's precise planning. While it's not as large as the KyivStar outage, it's a significant impact. The more devices you add, the more we can weaken the aggressor's infrastructure. Bring your friends into the IT ARMY! 🌐💻🛡️
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Алмател та 2Ком - два величезні інтернет-провайдери у столиці агресора перестали працювати сьогодні вранці. Це має бути десятки, якщо не сотні тисяч приватних, бізнес та урядових абонентів. Коли повернуться невідомо, але це все завдяки вашим зусиллям і ювелірної підготовки нашої команди розвідки. Це поки не масштаб збою КиївСтар, але хто знає яку операцію ми зможемо провести наступною?
Чим більше ви долучаєте девайсів, тим більше шкоди ми зможемо нанести інфраструктурі агресора. Приєднуйте до IT ARMY ваших друзів!

---
## [Humbug2014/Prime-Empire](https://github.com/Humbug2014/Prime-Empire)@[94fe0165b3...](https://github.com/Humbug2014/Prime-Empire/commit/94fe0165b352cc8ae22104d87e3ad29e6d154065)
#### Saturday 2023-12-16 19:42:01 by Whack Rat Fan

this is a test for Code central and is NOT the real prime empire.

Connection terminated. I'm sorry to interrupt you, Elizabeth, if you still even remember that name, But I'm afraid you've been misinformed. You are not here to receive a gift, nor have you been called here by the individual you assume, although, you have indeed been called. You have all been called here, into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach, but you will never find them. None of you will. This is where your story ends. And to you, my brave volunteer, who somehow found this job listing not intended for you, although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well. I am nearby. This place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should. And to you monsters trapped in the corridors, be still and give up your spirits. They don't belong to you. For most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend. My daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours, and then, what became of you. I should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now. It's time to rest - for you, and for those you have carried in your arms. This ends for all of us. End communication.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[247a4e02ea...](https://github.com/shiptest-ss13/Shiptest/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Saturday 2023-12-16 20:27:57 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [HalcyonicWolf/Skyrat-tg](https://github.com/HalcyonicWolf/Skyrat-tg)@[41026ae8b1...](https://github.com/HalcyonicWolf/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Saturday 2023-12-16 20:32:14 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[0c55aebcae...](https://github.com/EaW-Team/equestria_dev/commit/0c55aebcae844d845ab72d6a9fc2e428290d6d59)
#### Saturday 2023-12-16 20:53:02 by Mustafa Alperen Seki

Actually add the FAT female generics.

My stupid ass saved them to wrong place and forgor to copy them to the repo, my fault not resting it.

---
## [chefferz/S.P.L.U.R.T-Station-13](https://github.com/chefferz/S.P.L.U.R.T-Station-13)@[183f026a4a...](https://github.com/chefferz/S.P.L.U.R.T-Station-13/commit/183f026a4a8f883201fcc408c6d42b97167545ac)
#### Saturday 2023-12-16 21:07:52 by BongaTheProto

I'm sorry to interrupt you elizabeth

If you still even remember that name.
But I'm afraid you've been misinformed.
You are not here to receive a gift.
Nor, have you been called here by the individual you assume.
Although, you have indeed been called.
You have all been called here.
Into a labyrinth of sounds and smells, misdirection and misfortune.
A labyrinth with no exit, a maze with no prize.
You don't even realize that you are trapped.
Your lust of blood has driven you in endless circles.
Chasing the cries of children in some unseen chamber.
Always seeming so near, yet somehow out of reach.
But, you will never find them, none of you will.
This is where your story ends.

And to you, my brave volunteer.
Who somehow found this job listing not intended for you.
Although, there was a way out planned for you,
I have a feeling that's not what you want.
I have a feeling that you are right where you want to be.

I am remaining as well. I am nearby.
This place will not be remembered.
And the memory of everything that started this.
Can finally begin to fade away.
As the agony of every tragedy should.
And to you monsters trapped in the corridors.
Be still, and give up your spirits.
They don't belong to you.
For most of you, I believe there is peace and perhaps, warm.
Waiting for you after the smoke clears.
Although, for one of you.
The darkest pit of Hell has opened to swallow you whole.
So, don't keep the Devil waiting, old friend.
My daughter, if you can hear me.
I knew you would return as well.
It's in your nature to protect the innocent.
I'm sorry that on that day.
The day you were shut out and left to die.
No one was there to lift you up in their arms.
The way you lifted others into yours.
And then, what became of you?
I should have known, you wouldn't be content to disappear.
Not my daughter. I couldn't save you then, so let me save you now.
It's time to rest, for you, and for those you have carried in your arms.

---
## [chefferz/S.P.L.U.R.T-Station-13](https://github.com/chefferz/S.P.L.U.R.T-Station-13)@[defdf2f6b2...](https://github.com/chefferz/S.P.L.U.R.T-Station-13/commit/defdf2f6b2269cd8fc953ef71219109159ddfcd4)
#### Saturday 2023-12-16 21:07:52 by PhazeJump

FIXING MY OWN SHIT CODE MAKES ME FUCKING SCREAM

anyways
techpriest robes are now un-shitty-fixed and fixed again. Should be working properly now. No idea how to get the naga taur sprite working because it was supposed to be added in sand modular but sand modular was the one breaking it all so :shrug:

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[3409d0b3ec...](https://github.com/sojourn-13/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Saturday 2023-12-16 21:49:05 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [yrdzrfxndfvh/crawl](https://github.com/yrdzrfxndfvh/crawl)@[dfa497c050...](https://github.com/yrdzrfxndfvh/crawl/commit/dfa497c050c372f79a26eca37648bde4a5cc4df0)
#### Saturday 2023-12-16 22:07:17 by regret-index

New monster: protean progenitors, for Zot

Zot hasn't gotten new monsters besides the addition of then-new ghost moths
13 years ago (8d1b968), or the swapping of fire and ice dragons for already
present prior quicksilver dragons 7 years ago (0b18a7b). Most Zot work
across Crawl's development has been more oriented on adding more and more
stair vaults to Zot or fixing up the non-top-tier monsters otherwise
present: tmons constrict / demonic berserk, curse toe summons, death cob
attack brands, klown chaos, lich and draconian class spells. This is
entirely reasonably behaviour that has relatively evened out Zot's threat
level over time, but it has been a very restrained and compact set for a
while. It wouldn't hurt to try out more. Especially stuff that can break up
Zot's heavy reliance on relatively conventional, highly established, and
spreading elsewhere draconians.

Protean progenitors are transmutations giants for Zot. The origins of all
the dungeon's countless shapeshifters, they first start off as relatively
simple foes- unarmed Irradiate casters with fast regen but poor defenses
and no resistances. When they die, however, they leave behind some last
children in some last new form as they violently split into piles of
'aspiring flesh'- by default two at HD 12, with increasing chances of a
third if it rarely rolls any lower HD. These non-attacking, non-moving
piles will over the course of a few turns polymorph into hasted, mighted
copies of whatever the giant originally tried to transform into, and
never transform again. At HD 12 over the glowing shapeshifter HD 10
default, this gives double-buffed options of e.g. fire and ice dragons,
unarmed ettins, tyrant leeches, alligators, jorogumo, and broodmothers.
A chance to review much earlier branch spawns as a surprise in every giant
provides a bit more variety of bands over Zot's many base and nonbase
draconian packs, while also hewing closer to the weirder spectrum of Zot's
many non-draconic non-elemental monsters.

For now, they eat up a bit of the base draconian and non-base draconian
bands weight, and spawn with a 33% chance to have a second one accompany
them- a quick objstat roll says there should be about 4 of them throughout
Zot and each of Zot's standard base draconians reduced from ~11 to ~10. The
exact strength of these are inherently difficult to assess, so they'll
probably need a fair bit of public testing to see how these work out- base
form's base stats, spawn count, and band count are all easily changed.
They've also only been added to a restrained number of vaults- ones that
span the bulk of Zot's current monster set, or that invoke chaos and flesh.
They might make for reasonable spawns on Mnoleg's level to lower their
reliance on ugly things and eyes, but for now are otherwise only in chaos
zig floors. If we get any other new big Zot monsters, it might be a good
idea to look at slightly reducing the overall spawn count as is done for
Lair.

(Severely placeholder tiles are mostly made of currently unused decade-old
rltiles for large abominations, small abominations, and glowing
shapeshifters, with palettes from Sastreii's ice dragon and radroaches.)

---
## [foresle/qtile](https://github.com/foresle/qtile)@[aa380cf4a0...](https://github.com/foresle/qtile/commit/aa380cf4a0e7c945be237058d43a4d2643844ec9)
#### Saturday 2023-12-16 22:38:51 by Tycho Andersen

pyproject: more (hopefully the last?) porting

Here's the last bits of what I think we should port to pyproject.toml
before releasing.

* I dropped the "Alpha" Classifier, we're beyond alpha, I've been using
  qtile as a daily driver for nearly 15 years
* I dropped the point-release python version Classifiers (i.e. 3.8, 3.9,
  etc.). These are not that interesting and a pain to maintain.
* I dropped Sean Vig as the listed maintainer. We list all the maintainers
  at the bottom of the readme, which ends up in the long_description. No
  reason to maintain two maintainer lists.
* I dropped Aldo as the Author:. There are lots of authors of qtile, this
  info is available from the git log.

My hope is that this will not give a syntax error when uploading source
now during the release workflow. I've inspected the output with:

    python3 setup.py bdist_wheel --keep-temp && cat build/bdist.linux-x86_64/wheel/qtile-*.dist-info/METADATA

and it looks pretty similar to the METADATA from the current release.

Signed-off-by: Tycho Andersen <tycho@tycho.pizza>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[5f6fb4f5a3...](https://github.com/crawl/crawl/commit/5f6fb4f5a389a722ff4ee7fd78d4e43f979cce6c)
#### Saturday 2023-12-16 23:34:54 by regret-index

Add and trim a few Xom spells and cloud trails.

New spells: Wereblood, Animate Armour, Battlesphere, Malign Gateway.
Wereblood forces the player to make noise and thus is neat as a mixed
blessing, Animate Armour gets to by-pass its innate castability versus
armour weight issues to be more interesting as a random free god act,
Battlesphere makes for a decent joke if not actually usable and compensates
for the power of the two summons here, Malign Gateway has been missing
since the miscast streamlining and is extremely appropriate between the
chaos brand and unavoidable neutrality.

(These all are exchanged for Canine Familiar, which can't use one of its
most interesting aspects in the recast and thus will mostly make players
unavoidably get drained and guilt.)

New cloud trail clouds are salt and blastmotes, both at miniscule chances.
The salt's purpose is obvious, while the blastmotes are manually set at 25
power (power with those is weird and modular) and definitely give a certain
kind of danger and excitement very distinct from the spell by getting them
without having to stop for laying each of them.

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[c797954427...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/c797954427d133cbe0374f996c14327653a9b37d)
#### Saturday 2023-12-16 23:39:50 by kleinerm

Merge pull request #823 from Psychtoolbox-3/master

Pull for Psychtoolbox 3.0.19.6 "Raspberry cake" release.

### Compatibility changes wrt. Psychtoolbox 3.0.19.5:

- Psychtoolbox is now tested and supported on Matlab R2023b, instead of R2022b.
  It is expected to continue to work on older releases than R2023b, but no longer
  developed or tested against them.

- Slight behavioral changes in IOPort BreakBehaviour settings on MS-Windows, and
  generally a few IOPort config options. Not expected to affect (m)any user scripts.


### Highlights:

- This release was tested for compatibility with Matlab R2023b on Linux and Windows,
  specifically Ubuntu 22.04.3-LTS with AMD RavenRidge (AMD Ryzen 5 2400G processor
  integrated graphics) and AMD Polaris graphics, and on Microsoft Windows 10 22H2
  with AMD RavenRidge and NVidia GeForce GTX 1650 graphics, and to a lesser degree
  on Ubuntu 20.04.6-LTS and Windows 11 22H2 with Intel Kabylake (GT2) "UHD 620"
  integrated graphics. Testing with some onboard sound chips was also performed.
  The testing led to various smaller improvements, and various workarounds on
  MS-Windows for AMD OpenGL and Vulkan graphics driver bugs, and for some NVidia
  driver bugs, as well as some bugs in Matlab wrt. backwards compatibility and
  OS compatibility. Most improvements in this release are due to that.
  
  This was done as part of out Mathworks 2023/2024 contract for ensuring compatibility
  with recent Matlab releases, spending over 65 work hours. Due to not even remotely
  sufficient funding for this work, no significant testing beyond some very quick touch
  and go spot testing was performed for macOS.

- Substantial movie playback performance improvements in pixelFormat 11 for HDR
  and WCG movies when hardware video decoding is used on Linux and MS-Windows. A
  small fraction of this work was sponsored as part of the Mathworks contract.

- 10 bit deep color framebuffer and HDMI output for the RaspberryPi 4/400 by
  improvements to Psychtoolbox and to the Mesa 23.3.1 OpenGL graphics drivers
  for RaspberryPi's VideoCore 6+ gpu. Mostly paid for by Cambridge Research Systems.


### All:

- Screen: Optimize storage format for LUMINANCE16 textures for texture normalization.
  If a 16 bpc luminance texture is turned into an offscreen window, or drawn into,
  the needed normalization / conversion to RGBA format now converts into RGBA16
  format instead of RGBA32 float format. This retains full precision of the original
  image content, but at half the memory consumption.

- Screen: In DrawTexture(s), always filter planar textures via nearest neighbour
  sampling instead of any of the other filtering/sampling modes, as any sampling
  other than nearest neighbour will cause massive artifacts.

- Screen: Improve performance of HDR movie playback by more efficient use of hardware
  video decoding. Enable the GStreamer movie playback engine in HDR mode (aka pixelFormat 11)
  to accept and handle typical semi-planar YUV formats used for HDR movies when
  gpu hardware accelerated video decoding is in use. This allows GStreamer to avoid
  cpu expensive frame format conversions from semi-planar frames provided by the
  gpu hardware decoders to planar formats previously accepted by PTB's texture
  creation code, leading to way higher performance when such hardware decoders
  are used. Software decoding still works via the previous path, whenever that is
  wanted or needed. Software decoding can also be enforced by disabling of hardware
  decoding by passing in specialFlags1 flag +4 in ``Screen('OpenMovie', ...)``. One
  limitation of the disable is that hardware decoding will stay off for the remainder
  of the whole session, ie. until Octave/Matlab is quit, once the disable flag
  for hardware decoding has been given once in a session. This could be fixed by
  requiring GStreamer 1.20+ as minimum requirement, ie. Ubuntu 22.04 and later.

  Note that I've repurposed/redefined specialFlags1 flag +4 as hw accel disable,
  from previously "draw 2D flow vectors on content for debugging/visualisation".
  This is ok, as the feature was probably never used by anybody, and also because
  this feature is deprecated and unsupported in all supported GStreamer versions
  since quite a while.

  The following new formats are supported for efficient handling:

  - Y42B = YUV planar 4:2:2 with 8 bpc.
  - NV16 = YUV semi-planar 4:2:2 with 8 bpc, aka P208.

  - P0xx formats of YUV semi-planar 4:2:0 sampling with 8, 10, 12 and 16 bpc,
    ie. NV12, P010_10LE, P012, P016. These are the relevant ones for typical
    HDR-10 hardware decoding from H265/HEVC, AV1, and from VP9.

  So far this has been tested on MS-Windows 10 with NVidia GeForce GTX1650 and
  AMD Raven Ridge / Vega as part of a Ryzen 5 2400G processor. On NVidia it shows
  a 2x speedup in decoding speed, to allow playback of 4k HDR at 60 fps with stable
  framerate and none to minimal frame dropping. This typically uses NVCODEC on
  NVidia hardware or Direct3D11/DXVA decoding on NVidia, AMD and Intel gpus.

  Tests on Ubuntu 20.04.6-LTS + Intel Kabylake + GStreamer 1.16, and on two
  Ubuntu 22.04.3-LTS machines with GStreamer 1.20.3, once with AMD Polaris11
  and once with AMD Raven Ridge, also showed 2x performance improvements.
  This uses VAAPI for hardware accelerated video decoding on AMD and Intel,
  and maybe on NVidia, but NVidia is untested so far on Linux.

  Note that while AMD and NVidia worked well in my testing, more often than
  not, Intel Kabylake shit its bed, causing hangs or massive visual artifacts
  in decoded video, on both Ubuntu 20.04 and Windows 11. May or may not be
  general Intel bugs, or may just be a problem on my specific old Intel iGPU.

  Additional successful testing was performed by a user under Windows-10 with
  a NVidia GeForce RTX 3080 with H265 and AV1 4k HDR 60 fps content.

  As a general guideline, as of November 2023, these video codec formats
  are generally hardware accelerated on Linux and Windows with typical
  recent hardware from AMD, NVidia and Intel:

  - MPEG2, VC1, H264, VP8: YUV 4:2:0, 8 bpc.
  - H265, VP9: YUV 4:2:0, 10 bpc HDR.

  - Sometimes also MPEG4, and AV1, the latter only on latest gpu's from
    NVidia, AMD and Intel, specifically NVidia Ampere+ RTX3000+, or AMD RDNA2
    Navi 2nd gen, or Intel Xe+/Arc+ or macOS 14 on Apple M3+.

  For best cross-platform, cross-vendor compatibility and with older hardware,
  the safest choices for high performance playback are probably H264 and H265
  at the moment.

  None of this applies to Apple macOS, as macOS too primitive OpenGL implementation
  currently does not allow use of pixelFormat 11 playback.

- PlayMoviesDemo.m: Optimize further for fast playing movies.
  Suppress costly text drawing for any fps >= 30. Skip wait for flip complete for
  non-HDR playback. Ths way the demo also serves as a real-world performance test.

- `help GetChar`: Update wrt. OS+GUI+Matlab/Octave support, internationalization.

- `PerceptualVBLSyncTest[FlipInfo2]`: Add optimizations, especially for RaspberryPi.
  Avoid redundant stimulus draw in non-stereo mono-mode. Do clear the backbuffer
  after each flip, as that seems to give a substantial performance boost for the
  VideoCore gpu's - See speculation in code comments - probably related to it being
  a tiled renderer, or a split gpu + display engine design at least for VideoCore 6+
  of RaspberryPi 4 and later. I haven't checked the driver source for the more likely
  reason yet.
  
  Another thing that can really help sync tests on the Pi is Priority(1), because
  then gamemode daemon chooses a more aggressive cpu governor. This only matters at
  high display refresh rates though, e.g., on a RPi 400 with a 1920x1080 120 Hz
  display. At somewhat lower refresh rates, e.g., 60 Hz, it isn't needed.

- `IOPort`: Fix 'OpenSerialPort' bugs where default settings override user settings.
  
  As GitHub user @qx1147 found out during a code review, there is a flaw in
  the handling of serial port options, where default serial port options may
  override user provided configuration options, so the wrong settings are
  silently applied! This only happens if the user script provides different
  settings in ``IOPort('OpenSerialPort', ..., settings)``, ie. on initial port
  open. Calls to ``IOPort('ConfigureSerialPort', ..., settings)`` are not
  affected.

  Luckily (dumb luck!), only a few options were mishandled, and most of these
  are rarely changed by user scripts, specifically:
    
  ProcessingMode=Cooked would get ignored, and raw mode used instead. Rarely
  used on Linux/macOS and not supported on Windows anyways. Low impact.
    
  BreakBehaviour=Ignore would be used instead of Flush or Zero. Not a
  problem on Windows, as that is the only supported option. The fact that
  this went unnoticed on Linux/macOS suggests not much use of Flush or Zero
  by users scripts. No use by PTB itself. Low expected impact. Note that the
  implementation of 'Flush' on the Unixes is of questionable use, as Flush
  would not only flush read/write buffers, but also send a SIGINT, which may
  end in unexpected ways on Unix, as we don't handle SIGINT specifically.
  
  StopBits=2 would get ignored and the default of 1 stop bits would be used.
  Unclear how many devices want 2 stop bits, but I haven't ever seen one, so
  probably low expected impact.
  
  DataBits=16 would get ignored on MS-Windows only and replaced by 8 bits,
  whereas other settings are fine, and 16 bits is unsuported on Linux/macOS,
  so probably rarely if ever used. Low expected impact.
  
  FlowControl=None will be used instead of hardware or software flow control.
  This can be a real bummer with potential real impact, as some devices do
  support or recommend active flow control! In the case of PTB, the
  CedrusResponseBox() driver for Cedrus response box devices would have
  liked that setting.
  
  Audit of Psychtoolbox internal user of IOPort, and of the demos, only
  shows one bad case where things went sideways: CedrusResponseBox.m
  This driver requested hardware flow control, but silently got instead NO
  flow control! This is interesting, because during my testing I found
  communication with Cedrus boxes always rather unreliable, and now I have
  to wonder if this was because of the accidental lack of hardware flow
  control? I can't find out, as I lost access to Cedrus devices long ago.
  
  This whole parameter handling is somewhat fragile, and could do with an
  improved implementation, but due to the severe lack of financial funding
  for PTB, this is not an option in the foreseeable future. Not even code
  review or testing of 3rd party contributions, if there were any. Luckily
  this part of the driver is mostly static since years, so I guess we can
  drag our feet longer and sit it out.

  Another problem pointed out by @qx1147 is indeed that wrong options, e.g.,
  due to typos in users experiment scripts, would not lead to an error abort
  or warning, but would get silently ignored in many cases. Not great at all,
  but lack of funding will leave this problems also unsolved in the near- to
  midterm, possibly forever. Life sucks...
    
  See also PR #821 for discussion. Thanks to @qx1147 for catching this!

- psychrange(): Make fallback trigger robust against Matlab R2023b if
  statistics toolbox is not installed.

- help PsychDemos, MovieDemos: Some fixes so Matlabs help system can cope.

- Snd(): Minimal compatibility fix for older Matlab releases. E.g., R2018b
  may need this fix, as reported on the forum.

- FlipTimingWithRTBoxPhotoDiodeTest: Fix useXR flag.

- Cone fundamentals fitting tests: Fix plotting to be usable on different displays.
  Old plot positioning caused UI awkwardness on most monitors. Also fix use of
  savefig() function, which was broken due to incompatible changes in Matlab over
  the years as far as I understand.

- LosslessMovieWritingTest.m: Switch default codec for encoding.
  From long non-existent huffyuv to supported avenc_huffyuv. Update help texts.

- Delete ScreenTest.m the most useless test ever.

- ComputePhotopigmentBleaching(): Fix some bug in example. By David Brainard.

- Minor bug fixes, documentation updates and improvements.


### Linux:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- PsychHID: Work around latest Matlab R2023b internationalization bugs.
  
  Matlab R2023b, at least on Ubuntu 20.04-LTS and Ubuntu 22.04-LTS, has a
  new compatibility bug, where it provides its own deficient libX11 that
  defines a wrong path to the locale configuration directories. This causes
  failure of international keyboard handling, ie. calls to XSupportsLocale(),
  XSetLocaleModifiers() and XOpenIM() fail. As a consequence, only U.S.
  keyboard layouts get properly handled whenever our our PsychHID/keyboard
  queue based GetChar() implementation is in use, but not other keyboard
  layouts!
    
  It also triggers a warning each time KbQueueCreate() is called, regardless
  if in the context of GetChar/CharAvail/ListenChar, or just for keyboard
  queue operation.
    
  Try to detect and work around this Matlab bug, by detecting the failure
  and then setting the XLOCALEDIR environment variable to override Matlabs
  broken path to a path that is correct at least for Ubuntu 20.04/22.04 and
  for similar Debian(-based) systems. Also try to detect user interference,
  e.g., the user setting a unsuitable XLOCALEDIR, and give troubleshooting
  tips in that case as well.
    
  This fixes the problem with R2023b on at least Ubuntu 20.04 and 22.04.
  The problem could also have been present in R2023a already, but this was
  not ever tested by myself, and I am not aware of any bug reports against
  either R2023a or R2023b.

- Add support to XOrgConfCreator, XOrgConfSelector and PsychLinuxConfiguration
  to allow to enable 10 bpc / 30 bit deep color framebuffers and display over
  HDMI on suitable displays with the RaspberryPi 4 and 400, and likely also the
  RaspberryPi 5. This was only tested on the RaspberryPi 400 under RaspberryPi OS
  versions 11 "Buster" (legacy) and 12 "Bookworm" (most recent one) 32-Bit editions.
  Note that current Psychtoolbox from us currently only works on RaspberryPi OS 11,
  ie. what is now called the "legacy" edition, not yet on the "current" OS version 12.
  Psychtoolbox 3.0.18.12, shipping with OS version 12 will work of course, but it
  does not have this setup code. However, it would work with a manually created
  xorg.conf file.

  Note that 10 bit framebuffers do not work on current versions of RaspberryPi OS
  out of the box. You need to manually install Mesa version 23.3.1 stable or later,
  which has an ETA of sometimes at or after 13th December 2024. Until then, a build
  script can be found under. You can download it, make it executable, and run it to
  build and install a Mesa local build in /usr/local/ compatible with RaspberryPi 4
  and 400, possibly RaspberryPi 5. Use this hacked build and install script at your
  own risk, if it totally breaks your system you get to keep all parts:
  
  https://raw.githubusercontent.com/kleinerm/PiKISS/ForCRS10BitMesa/scripts/config/vulkan.sh

  My enablement work for OpenGL 10 bpc / color depth 30 bit / deep color framebuffer
  support for Mesa 23.3.1+ on the RaspberryPi 4+ was sponsored by a contract from
  Cambridge Research Systems Ltd. Thank you!

- Other smaller refinements to RaspberryPi support.


### Windows:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- For Vulkan on Windows, reenable fullscreen exclusive support on current AMD drivers
  for proper timing. now works again on AMD gpu's with the latest AMD display drivers,
  version 23.11.1 from November 2023, as tested successfully in both SDR mode and HDR-10
  mode on Windows 10 22H2 with AMD Raven Ridge iGPU of AMD Ryzen 5 2400G APU, aka DCN-1
  display engine and Vega 11 graphics. Hurray!

  Some earlier driver versions might work as well, but this is the only confirmed one
  by testing, so reenable fullscreen exclusive starting with the 23.11.1 release.

- `IOPort`: Fix wrong break condition handling. Ignore break conditions completely
  `(BreakBehaviour=Ignore)`, rather than treating them as errors without further
  handling them in a useful way. Do validate BreakBehaviour parameter to be the only
  currently supported setting. Contributed by GitHub user @qx1147.

- `PsychPortAudio`: Update libportaudio for MS-Windows with latest from upstream Git
  main development branch. This way we get my bug fixes to WASAPI audio capture/input
  timestamping. Testing on MS-Windows 10 and 11 still shows some fragility and oddity
  in audio input capture timestamping, e.g., for voice onset timestamping, or sound
  based timing measurements like KeyboardLatencyTest.m or AudioFeedbackLatencyTest.m.
  These tests may not be very trustworthy on MS-Windows with WASAPI sound backend.

- Screen: Rewrite CRS clut update function RenderClutBits++ as a workaround.
    
  Switch from using point rendering via glVertex2i() of the clut T-Lock update pattern
  to instead using glRasterPos2i + glDrawPixels().
    
  Why? Because the proprietary AMD OpenGL driver on Windows has bugs in
  glVertex2i positioning when rendering to the OpenGL system backbuffer. The
  most easy way to work around this atm. is to use glRasterPos2i + glDrawPixels()
  to avoid the glVertex2i AMD bugs. This has the added benefit that we now use
  this glRasterPos2i + glDrawPixels() combo consistently for all CRS T-Lock rendering,
  ie. FE1 stereo driving and DIO codes, and for identity pixel passthrough tests and
  gamma table tweaking in PsychGPUTestAndTweakGammaTables(). At least we only
  have to think about one potentially broken function (glRasterPos2i()) in the future,
  not two separate ones.
    
  This was found on AMD RavenRidge Vega11 under Windows 10 with AMD driver 23.11.1.
  No such problem happened with the same hardware on Linux during my testing.

- AdditiveBlendingForLinearSuperpositionTutorial.m: Fix clut overlay text, and cleanups.
  Apply same fix as for BitsPlusIdentityClutTest.m for AMD Windows OpenGL driver
  bugs, so text rendering via the Mono++ / M16 clut hardware overlay works.

- BitsPlusIdentityClutTest.m: Work around MS-Windows AMD OpenGL driver bug.
  AMD's current OpenGL driver version 23.11.1 from November 2023 for MS-Windows
  has a bug in that glTexImage2D() does not accept GL_BITMAP texture specs. This
  breaks non-anti-aliased text rendering mode in the drawtext plugin.
    
  Work around this by enabling anti-aliased rendering for the plugin via
  Screen('Preference', 'TextAntiAliasing', 1); However, we don't want anti-aliasing,
  as it potentially interferes with clut overlays on CRS and VPixx devices, so use
  Screen('Preference', 'TextAlphaBlending', 1); to apply Screen('Blendfunction')
  settings during text rendering, but don't actually use Screen('Blendfunction').
  Instead leave alpha-blending at defaults, which is alpha-blending disabled.
  This effectively brings back aliased text rendering which works with the clut
  overlays.

- Screen('ColorRange'): Add workaround for color clamping OpenGL driver bugs.
    
  Turns out the recent proprietary AMD OpenGL driver on MS-Windows has a broken
  color clamping query implementation, which does not report clamp state for
  GL_CLAMP_VERTEX_COLOR_ARB or GL_CLAMP_FRAGMENT_COLOR_ARB.
    
  As such, we get reported failure to change color clamping on Windows 10 + AMD,
  whereas the same code works fine on Windows 10 NVidia or Intel.
    
  Work around this by detecting the failure and auto-selecting our own internal
  GLSL shader based fallback path. This should fix it - at a performance penalty,
  as vertex color clamping can be handled by our fallback shader, fragment color
  clamping has proper default behaviour of clamping on for fixed point unorm
  framebuffers, and clamping off for floating point framebuffers. Only readback
  clamping needs to be controlled via glClampColorARB, but luckily readback
  clamping is supported by glClampColor() as well, in a backwards compatible way,
  so we should be good. Famous last words...
    
  Note that this bug is so far only present on AMD on Windows, so we can get
  away with only rebuilding Screen() for MS-Windows for the moment.
    
  Also note that because it is the query that is broken, not the setting, our response
  of selecting the fallback path may be not necessary. However, it is unlikely to hurt,
  and we can not know, so better safe than sorry.


### macOS:

- Psychtoolbox was built and lightly tested against Matlab R2023b and Octave 8.4
  from HomeBrew. It should likely continue to work on older versions of Octave 8.x,
  possibly 7.x or 6.x., although none of these was tested.

---

