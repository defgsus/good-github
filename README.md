## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-16](docs/good-messages/2022/2022-04-16.md)


1,482,445 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,482,445 were push events containing 2,159,427 commit messages that amount to 118,009,852 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [JuliaPackaging/Yggdrasil](https://github.com/JuliaPackaging/Yggdrasil)@[b1469b44df...](https://github.com/JuliaPackaging/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Saturday 2022-04-16 00:27:50 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [JerodGibbs/tgstation](https://github.com/JerodGibbs/tgstation)@[745426eff2...](https://github.com/JerodGibbs/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Saturday 2022-04-16 02:02:22 by LemonInTheDark

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
## [DEMOLITIONDON96/Demolition-Engine](https://github.com/DEMOLITIONDON96/Demolition-Engine)@[d92e11e16b...](https://github.com/DEMOLITIONDON96/Demolition-Engine/commit/d92e11e16b2aff4bfd7c2e169949e19ed9b1be98)
#### Saturday 2022-04-16 03:24:29 by Matt 3

Dumbass example for the stupid shitty ass thing auefhirwyjneklMOQp;waki

oh also i got a new keyboard

Huo JI BT-885 Blue Switches RGB :D

---
## [nevimer/bugstation13](https://github.com/nevimer/bugstation13)@[b1a793f840...](https://github.com/nevimer/bugstation13/commit/b1a793f840d90131f88eabc0450e2b2b2157123e)
#### Saturday 2022-04-16 03:54:41 by Tim

Refactor and improve antimagic to be more robust (#64124)

This refactors the antimagic component to use and have bitflags, documentation, defines, code comments, named arguments, and renames variable names for clarity. 

- /obj/effect/proc_holder/spell/aoe_turf/conjure/creature/cult is not used anywhere and has been removed
- /obj/effect/proc_holder/spell/targeted/turf_teleport/blink/cult is not used anywhere and has been removed

- New sound effects are played when magic is blocked. Depending on the type of magic being used it will be either:

- Equipping antimagic now properly updates the magic buttons
- Any magic being blocked or restricting casting now displays a message
- MAGIC_RESISTANCE_MIND now properly blocks telepathy effects
- Removes blood splatter when fireball is blocked
- Magic projectiles for staff of locker no longer spawn lockers when blocked by antimagic
- Fire breath is no longer blocked by antimagic
- Spellcards are now blocked by antimagic

Any antimagic on a mob blocks that magic type from being casted. (certain spells such as mime abilities completely ignore antimagic)

- Foilhats prevent someone from casting mind magic (telepathy, mindswap, etc.)
- Bibles, ritual Totems, nullrods, holymelons, and TRAIT_HOLY prevent someone from casting unholy magic (cult spells, etc.)
- Nullrods, ritual totem, and holymelons prevent someone from casting wizard magic (fireball, magic missile, etc.)
- Immorality talismans, berserker suits, and TRAIT_ANTIMAGIC prevents all types of magic (except stuff like mime abilities)
- Touch of Madness and Mindswap is now blocked with MAGIC_RESISTANCE and MAGIC_RESISTANCE_MIND
- Voice of god is now blocked with MAGIC_RESISTANCE_HOLY and MAGIC_RESISTANCE_MIND

---
## [stitchfix/hamilton](https://github.com/stitchfix/hamilton)@[834edac907...](https://github.com/stitchfix/hamilton/commit/834edac90764bb34a6c997a0b88575ade8bfa88e)
#### Saturday 2022-04-16 05:09:21 by skrawczyk

Adds parameterized_inputs decorator

This is a squashed commit of all the commits to create the parameterized_inputs
decorator. See the commits below that are in reverse chronological order.

Basically, this replaces `parameterized_input`, and provides a more succinct
API by using the function doc as a template, removing the need for a tuple.

We believe this is a simpler API to read/maintain — the kwargs assumption will
make it harder to extend the API, but we don’t think we need to.

——— Consolidated commits below ——

Adds format doc function to parameterized_inputs

To consolidate formatting in a single place. Want to keep
the code DRY. (+7 squashed commits)
Squashed commits:
[338c02a] Touches up documentation typos

And adds reraising original exception for formatting errors.
[f2725ec] Adds validate test for parameterized_inputs for the doc string

Doc string templates errors should be checked during validate.
That way we can throw a better error.
[4689177] Changes parameterized_inputs to use kwargs

1. So that we don't scope creep this API. Key words arguments are
assumed to be outputs. This removes a level of nesting on the API.
2. We're inline with other decorators in having the kwargs behavior, e.g. config.when.
[df571f3] Changes parameterized_inputs to take dict and format doc string

With the prior design, the issue was documentation. But after noodling on it
and prodding from Eljiah, I realized that the documentation string should just
be a template. Since you're going to be using the same function, the doc string
should be fairly generic, with only the parameters being passed changing the
meaning -- which with templatization, allows for that to come through.

Note - stylistically I think we prefer:

```python
@parametrized_inputs(
    parameterization={
        'output_123': dict(input_value_tbd1='input_1',
                           input_value_tbd2='input_2',
                           input_value_tbd3='input_3')
    }
)
```
because syntax highlighting will make it clearer what is being replaced in the
function with what input value.

to

```python
@parametrized_inputs(
    parameterization={
        'output_123': {
                 'input_value_tbd1'='input_1',
                 'input_value_tbd2='input_2',
                 'input_value_tbd3'='input_3'
        }
    }
)
```
or

```python
@parametrized_inputs(
    parameterization=dict(
        output_123={
                 'input_value_tbd1'='input_1',
                 'input_value_tbd2='input_2',
                 'input_value_tbd3'='input_3'
        }
    )
)
```
I think the last two ones are less clear/readable.

Otherwise I did have the thought of using actual functions in the mapping. It would
then be clearer to trace what is going on with an IDE.
However that brings up the possibility of people importing functions and running
into import messes... So punting on that for now. We can always add that in later
if we think that's required.
[0e21e9d] Changes parameterized_input to parameterized_inputs in decorator docs

Since parameterized_input is deprecated, we should just remove it from the
docs and instead just push parameterized_inputs.
[4379a38] Adds ParameterMapping named tuple object to adjust parameterized_inputs

People creating a dictionary of tuple to tuples is probably unwieldy. This is a power
use case, and thus it should afford a little more friction to use, and the net result of that
is that the code should become more readable.

We should preference keyword arguments everywhere here -- as that will make the code
much more readable than without it. E.g. :
```python
@parametrized_inputs(
    parameters=['input_value_tbd1', 'input_value_tbd2', 'input_value_tbd3'],
    parameter_mappings=[
        ParameterMapping(
            inputs=['input_1', 'input_2', 'input_3'],
            output_name='output_123',
            output_docs='function_with_multiple_inputs called using input_1'),
    ]
)
def func(...)

@parametrized_inputs(
    ['input_value_tbd1', 'input_value_tbd2', 'input_value_tbd3'],
    [ParameterMapping(['input_1', 'input_2', 'input_3'], 'output_123', 'function_with_multiple_inputs called using input_1')]
)
```

Adjusts tests and documentation accordingly.
[c1d5fa8] Adds parameterized_inputs

This change adds `paramterized_inputs` decorator, which
is almost a carbon copy of `paramterized_input` but that it allows
any number of parameters to be mapped.

Why is it a separate class? Well for backwards compatibility
we don't want to break parameterized_input. Should we try to
consolidate them? I think so -- so we should then mark `parameterized_input`
as deprecated and will be removed in a 2.0 release?

I should then probably update all documentation to reflect `parameterized_inputs`
and thus the documentation on `paramterized_input` to either be hidden or
non-existant? Hmm.

---
## [Phenrei/RWoM](https://github.com/Phenrei/RWoM)@[ccc7d0567d...](https://github.com/Phenrei/RWoM/commit/ccc7d0567d3cd0039c481a673a8e6e2c24a4869e)
#### Saturday 2022-04-16 05:50:44 by TorannD

v2.6.3.0 update

New:
 Note: both new classes demonstrate methods of using any hediff or need as a resource for abilities
 o Empath Class - an unique magic class that manipulates emotional (mood/joy) energy to fuel their abilities; there is no 'book' to learn to become an empath - it can only be acquired naturally
 Abilities:
	- Empathy: controls the innate empathic skill to raise spirits
	- Mind Killer: floods all nearby pawns with stored emotions that opens a variety of reactions due to the emotional stress
	- Suppressive Aura: blocks or filters the emotions (good and bad) of nearby pawns at the cost of emotional stress on the empath; prevents mental breaks of suppressed pawns
	- Harvest Passion: attempts to overcome the will of a target and steal their work passions; requires an inspiration
	- Incite Passion: transfers a work passions from the empath to a selected target

 o Apothecary Class - dedicated to the creation of tonics, tinctures, potions and remedies; the apothecary class creates several useful solutions using natural ingredients found in every-day harvesting work.
 Abilities:
	- Herbalist: governs the skill of the apothecary; improves ingredient discovery, preservation and efficiency
	- Elixir: creates a fast acting tonic that speeds wound recovery, fights diseases and infections, and even reduces signs of scars and aging. Side effects may include...
	- Soothing Balm: a mixture of ingredients that can be applied to open wounds to immediately treat them; the salve also reduces overall pain and prevents infections. In large doses, soothing balm may be used as an anesthetic
	- Poison Flask: throw a vial of noxious ingredients that expands into a cloud when it shatters, causing damage to the lungs and throat of anyone that breaths the fumes

 The Apothecary is considered a 'fighter' class and the Empath a 'mage' class, but they are only weakly attuned to their respective fields; training can improve these skills somewhat

Tweaks:
 o Custom class marker will now use the colonist bar mark if classTexturePath is left blank
 o Magical Aura's and undead will trigger the "witnessed magic" ideology requirement

Bug fixes:
 o Living wall skill levels correctly save
 o Shard of extraction correctly removes the Death Knight class
 o Enchanted Body skills correctly apply to Enchanted Aura

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[8b1ec33143...](https://github.com/nevimer/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Saturday 2022-04-16 06:52:28 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[20d3361f6b...](https://github.com/nevimer/Skyrat-tg/commit/20d3361f6b9e81e83b1fe2b69a57713f5a81cc2e)
#### Saturday 2022-04-16 06:52:28 by SkyratBot

[MIRROR] makes podpeople spec_life call parent [MDB IGNORE] (#12106)

* makes podpeople call parent (#65362)

About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

* makes podpeople spec_life call parent

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [JudsenHembree/Escape](https://github.com/JudsenHembree/Escape)@[e152b0865c...](https://github.com/JudsenHembree/Escape/commit/e152b0865c38998c84900f5f9cbfe3e8061e37be)
#### Saturday 2022-04-16 07:08:42 by Judsen S Hembree

need to finish task 3 and audio cue system

I hate my life

---
## [EasyMeshVR/EasyMeshVR-Prototype](https://github.com/EasyMeshVR/EasyMeshVR-Prototype)@[61e024578b...](https://github.com/EasyMeshVR/EasyMeshVR-Prototype/commit/61e024578bd2e8d53cc631bea1162c397b8e5b9a)
#### Saturday 2022-04-16 07:09:10 by cptclouddrake

AAAAAAAAAAAAAAAAAAAAAAAAAAAA

WE'RE ALMOST DONE BOYS
JUST NEED TO ADD FULL EXTRUSION SUPPORT AND WE'RE GOLDEN

- Merges properly re-ID edges and faces when deleted and move them around their respective meshRebuilder arrays for correct references from other scripts
- Well what the fuck does that mean?
- It means when you merge and you grab a face or an edge, the mesh isn't gonna shit itself anymore
- Like it actually works like it's supposed to
- Go figure

---
## [SSpidey/android_kernel_zuk_msm8996](https://github.com/SSpidey/android_kernel_zuk_msm8996)@[329428eecd...](https://github.com/SSpidey/android_kernel_zuk_msm8996/commit/329428eecd3e538f529b1f054eea554183cdaead)
#### Saturday 2022-04-16 07:28:38 by Maciej Żenczykowski

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
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[2c66467b1a...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/2c66467b1a9b4bbfa818f79b3d69b4f761c2e072)
#### Saturday 2022-04-16 09:38:12 by alk3pInjection

drm: Handle dim for udfps

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
## [LenitaTV/NOMOKO-](https://github.com/LenitaTV/NOMOKO-)@[38825fa39d...](https://github.com/LenitaTV/NOMOKO-/commit/38825fa39d1a7ad03dcedabd091af350d0d7d979)
#### Saturday 2022-04-16 10:26:41 by Talent Acquisition Manager - NOMOKO AG

Update README.md

Would you like to support us to develop 3D functionalities in Praedia? Praedia is a free-to-use web platform built by Nomoko. It brings digital transformation to businesses of every size operating at any scale.

Are you thinking of the Al, data visualization, visual detection? This is as high-tech as it can get! Would you like to be part of it with a flexible schedule?

Interesting Challenges Ahead Of You:
Working closely to our 3D Experts, knowledgeable designers and other experienced software developers
Collaborating with our experts on our geo-based application - Ex: Mapbox, Cesium and Esri
Improving the future of Proptech (Property Technology) based on a rapidly changing digital landscape and ever-shifting consumption trends and patterns
Requirements

This will be a great fit if you have some experience as a Frontend React Web Developer, working with NPM, Web GL, Canvas and demonstrated technical ability for writing visualizations in Three.js or other visualization libraries to finally build THE BEST FRONTEND you could ever build by using the most advanced technologies.


We have been investing heavily in cloud services (serverless functions, API Gateways, streams, CQRS). You can set it up the way you like it, and implement all the best practices you were dreaming about.

You’re interested? We’d love to get to know you! Please send me an email with your CV (lenita@nomoko.world).

---
## [Zajicek-Adam/sus-game](https://github.com/Zajicek-Adam/sus-game)@[fc4c3d85db...](https://github.com/Zajicek-Adam/sus-game/commit/fc4c3d85dbb7d4836f1b789ac432db1be0f2cd7e)
#### Saturday 2022-04-16 11:52:56 by Zajicek-Adam

Fuck my life nothing ever works

So
Syncing bullets doesnt work
Syncing gun rotation doesnt work
Bullets are laggy as fuck no matter the settings (havent tested everything yet tho)
Gun rotation is somehow shared between the players which is very fucking stupid fuck this shit I am done

---
## [sidmohanty11/RC4Community](https://github.com/sidmohanty11/RC4Community)@[ddc933b9cc...](https://github.com/sidmohanty11/RC4Community/commit/ddc933b9cc0e4d53f4041682d01789ee8477ee0a)
#### Saturday 2022-04-16 12:16:27 by Sidharth Mohanty

Official Project License Christening Commit (#147)

@sidmohanty11  was nominated by @Dnouv  and seconded unanimously by all in attendance for creating this milestone commit:

@sidmohanty11 @samad-yar-khan @demonicirfan @Sing-Li @RonLek @Dnouv 

On this "Good Friday 2022"  team members meeting,  @Sing-Li was moved to tears by the open source team spirit and camaraderie displayed (seldom seen in "day job" meetings nowadays)  Thanks for sharing  ! :pray: all !

License choice was voted on by team members (between Apache 2, MIT and GPL):

@sidmohanty11 @samad-yar-khan  @demonicirfan @Sing-Li  @RonLek  @Dnouv @debdutdeb @dudanogueira @abhinavkrin @engelgabriel 

All team members - please post a daytime bitmap of an environment near you  (on this comment)  to "remember this time".    Thanks.

---
## [voiceflow/general-runtime](https://github.com/voiceflow/general-runtime)@[5722ab44e2...](https://github.com/voiceflow/general-runtime/commit/5722ab44e2ab100cd8c68840083861c47afa1567)
#### Saturday 2022-04-16 13:48:27 by Tyler Han

fix: api debug messages (VF-3263) (#309)

<!-- You can erase any parts of this template not applicable to your Pull Request. -->

**Fixes or implements VF-3263**

### Brief description. What is this change?
So it turns out when you `stringify` a `VError` you actually don't get the error message, but everything else, which is kinda stupid. 

BEFORE:
![Screen Shot 2022-04-16 at 12 35 07 AM](https://user-images.githubusercontent.com/5643574/163676644-717b2998-7dd4-49b8-a0d8-bffd04151e47.png)


AFTER:
![Screen Shot 2022-04-16 at 12 31 32 AM](https://user-images.githubusercontent.com/5643574/163661454-767cd019-57c7-4630-9e59-4d48e1adaf64.png)

I also updated the debug message so if you get a >400 response on the API call, we show the body too.

---
## [mar3an/alphaproject](https://github.com/mar3an/alphaproject)@[7b91582b90...](https://github.com/mar3an/alphaproject/commit/7b91582b90463e49205da7b82ba1ecb6f5e00751)
#### Saturday 2022-04-16 14:39:02 by mar3an

# - GameServer: Dimensional Merchant Life Energy fix
  - Dimensional Merchant is found in all cities, including starting villages

With it, you can get various pets. To be the lucky owner, you must have a Hunting Helper Exchange Coupon or  High-Grade Hunting Helper Exchange Coupon , which can only be obtained through the Item Mall.
After receiving a coupon, you can exchange it for one of the pets.

Pets that can be obtained for coupons
 - Hunting Helper Exchange Coupon :
 - White Weasel (White Weasel)
 - Fairy Princess (Fairy Princess)
 - Wild Beast Fighter (Wild Beast Fighter)
 - Fox Shaman (Fox Shaman)

High Grade Hunting Helper Exchange Coupon :
 - Toy Knight
 - Spirit Shaman (Magic Spirit)
 - Owl (Owl)
 - Turtle Ascetic

---
## [anjrv/HBV501](https://github.com/anjrv/HBV501)@[7eac94ba88...](https://github.com/anjrv/HBV501/commit/7eac94ba882690cf98bcae118230c8f128721cbd)
#### Saturday 2022-04-16 14:42:06 by Anna Jaerving

make recipe title stop being wonky holy shit what is this

---
## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[759d24ab14...](https://github.com/DragonTrance/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Saturday 2022-04-16 14:49:04 by san7890

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
## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[884c1eeb62...](https://github.com/DragonTrance/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Saturday 2022-04-16 14:49:04 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [ASpoonPlaysGames/NorthstarLauncher](https://github.com/ASpoonPlaysGames/NorthstarLauncher)@[db0af63704...](https://github.com/ASpoonPlaysGames/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Saturday 2022-04-16 14:57:47 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [SciathGH/IonCore](https://github.com/SciathGH/IonCore)@[abc3af59ee...](https://github.com/SciathGH/IonCore/commit/abc3af59ee70dd891fd5ca8a3abd9a4b9c38f056)
#### Saturday 2022-04-16 15:17:00 by Sciath

Fuck you Microshielding, Peter accept this or ill keep exploiting it.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c8ef62c1fb...](https://github.com/timothymtorres/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Saturday 2022-04-16 15:17:50 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

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

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e58fb506ef...](https://github.com/timothymtorres/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Saturday 2022-04-16 15:17:50 by LemonInTheDark

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
## [mar3an/alphaproject](https://github.com/mar3an/alphaproject)@[ce11cf18cb...](https://github.com/mar3an/alphaproject/commit/ce11cf18cb4c22a9a512ea0e9111a9147da6fd96)
#### Saturday 2022-04-16 15:24:44 by mar3an

# - GameServer: Lucky Pig event added, part of Dimensional Merchant

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
(Dimensional Merchants are now functional.) To change a weapon into a rare weapon, you need to supply the Dimensional Merchant with the weapon and 1 Neolithic Crystal of the same grade.

---
## [Thrumbar/julia](https://github.com/Thrumbar/julia)@[62e0729dbc...](https://github.com/Thrumbar/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Saturday 2022-04-16 15:25:43 by Mirek Kratochvil

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
## [jsjohn1951/so_long](https://github.com/jsjohn1951/so_long)@[82f6eecab8...](https://github.com/jsjohn1951/so_long/commit/82f6eecab8fd4914315b5cbcbfbc6476195105cc)
#### Saturday 2022-04-16 17:13:02 by Willem Smith

Version 14 :: found out my split was shit, must build new one, I need to rethink my life because of split fuckery

---
## [PikachuPenial/EscapeFromGarrysMod](https://github.com/PikachuPenial/EscapeFromGarrysMod)@[ca06a39797...](https://github.com/PikachuPenial/EscapeFromGarrysMod/commit/ca06a39797d0c48539497e7b2fd17e000fe94532)
#### Saturday 2022-04-16 17:57:22 by PortableTerraria

made it so you dont have to reset stash to get it to work

fucking smart spawn bullshit just dissapeared thanks github fuck you

---
## [krux02/nimskull](https://github.com/krux02/nimskull)@[f35b5bf2d4...](https://github.com/krux02/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Saturday 2022-04-16 18:05:54 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [uasi/nykk-btn](https://github.com/uasi/nykk-btn)@[b1183813d0...](https://github.com/uasi/nykk-btn/commit/b1183813d0ba2ac02d95e300e05b5bbfadc89d1c)
#### Saturday 2022-04-16 18:34:17 by Tomoki Aonuma

Fix unexpectedly decomposed filenames

Fuck you UTF-8-MAC

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[993d027120...](https://github.com/mrakgr/The-Spiral-Language/commit/993d0271209b15b986e6f9409ab8810836dc7e64)
#### Saturday 2022-04-16 19:20:36 by Marko Grdinić

"10:20am. I am up. No reply again. I am not sure what to think about this. Is this going to be like with Z where I sent him a mail and he replied almost a week later? It is important not to overthink this. Back with that last serious attempt the other party had fairly wild expectations of what the salary range would be and was very lazy when it came to replying to email. It was way more than I ever would have expected.

Tech hiring is all sorts of messed up. Given that people are so desperate for ML engineers that they would resort to emailing anyone who looks good, if this does not pan out, I am probably going to get business in the future.

There is a very small number of people in the world with my skills. Most ML aspirants run a few ML models and call themselves experts. They don't go on years long journeys that involve making programming languages and ML libraries from scratch.

I'll give it a week until I mentally write this off. Last time I wrote Z off after a few days and was surprised when he got back to me, so it makes sense to lengthen the waiting period.

10:25am. Let me read Baki and then I am going to get started.

Yesterday I picked up Estab Life and Birdie Wing on a whim and they are both good. Last season I was mostly following gender bender shows, but they weren't that great. Maybe Hero King will be more to my liking when it comes out.

I also completely forgot about SnK, I should start catching up to that. But I've been spending so much time doing 3d art, that I do not have much time for doing anything else after that.

Hopefully now that I've got essential techniques under wrap, the pace should be more streamlined.

10:50am. Ah, let me chill a bit more. Who feels like starting right away once they get up.

11:45am. I've been working on that piece a bit more. I removed the washout and smoothed out one of the corners using sculpting's smooth brush. I had to do that last one because two of the corners were a bit too harsh. With that I should be done with the piece.

I've UV packed it into tiles and now I am ready to take it into substance. Let me do that. Let me finish this desk. I've been playing with it for way too long. If I go on for any longer, I'll end up writing a thesis on it.

I did a really good job this time around.

I am not saying my art is great, but I haven't made any methodological mistakes this time around. What I have now should be enough to establish a proper hard surface workflow.

Now focus me. Get the desk done. A prop a day keeps the poverty at bay.

12pm. This is troublesome. How do I isolate a particular geometry mask instead of just the texture set?

https://youtu.be/jxHi-oevk8o?t=91

Oh, there is a button to hide exluded geometry on the top panel. Great. Too bad Alt + Q does not work. Is there another shortcut for this?

Alt + H. Alt + Q is for isolating a texture set.

Great. This is great.

Ok, now what I need to do next is the pattern for the top of the desk again. Let me do it in Designer.

What I do not know how to do is make sure it does not wrap around. For this material I do not want a tileable texture.

https://forum.substance3d.com/index.php?topic=2329.0

> Ah it's ok. I found the Tiling Mode attribute. I didn't notice it to start with as it's greyed out as relative to parent, even at the top level. Making it absolute and setting it to not tile sorted my problem.

I couldn't figure out why this one is gray out everywhere, but this answers it.

12:55pm. Problem number one is that the pattern is a pain in the ass to create.

1:30pm. Yeah, it is a pain in the ass. I want to get it done quickly, but my experience is not helping and I just find myself moving stuff around. But at least I am done with it. Never again.

I'll do the distortion by hand in later in Painter as doing it in Designer leads to bad results since the texture is not tileable.

Let me have breakfast here.

I really should have just copy pasted the layers from the old project if possible somehow.

1:40pm. Previously my mentality was to do it again, but now that I've sunk 1.5 hours into it, I am quickly changing my mind. I really should check out whether I could copy paste some of my previous work to the new one. If not then so be it, but if I can I should save myself effort, I should do so. Working on that desk piece's geometry was important so I can save time, but this here is not like that.

2:35pm. Given the amount of fiddling around it took me in Designer, I really should have just drawn the pattern line by line Clip Studio after all. I had to use a fancy approach to save time, but just where did it get me? Well, it did teach my quite a bit. But I can believe Photoshop would be competitive for making textures at this rate.

Let me chill for a bit longer.

3:15pm. Ok, let me work on that pattern for a bit more. I had some inspiration. I've been acting so dumb ever since Covid wrecked me. I fall into the mode of just trying things out instead of stopping to think and reason out my process.

I've been thinking how I would do the pattern in Houdini using height fields.

And the answer is not too hard.

3:35pm. No I give up. It is not working for me. I made a mistake not doing it in CSP and just importing it as a texture. As emarassing as it would be to draw 50 lines and tile them 4 times by hand, it would have taken far less time than this.

Forget it. Ok, as the first thing on the list, let me see if I can copy layers across projects.

3:40pm. No, unfortunately, I can't use that old textured desk.

https://forum.substance3d.com/index.php?topic=8262.0
> you could create a Smart Material from the layers you want to copy over, this is the only way I know to transfer a layer stack.

Trying to do everything from scratch it too tedious so why don't I try this?

I really don't feel like redoing the work. I am playing with mask generators, and they work like shit.

4:10pm. No, let me just go into robot mode. I'll do one piece at a time.

4:25pm. No, I do not feel like it. Instead of going down this route, how about I instead just go back and use regular texture sets? The amount of work I've put into texturing the old thing is not to be underestimated. Right now it feels like I am clumbing a mountain.

Back then I was really in the zone when placing things line by line. Now on the other hand, things are completely different. I just want to get things over with so I can move on to the next thing. But this exactly the wrong mindset to have when doing art, programming or anything important for that matter.

I got UV packmaster and SP, so I got it into my head that I need to do things in the new way. I don't.

I've already made the stupid mistake of spending half the day on this. Instead of digging the hole deeper, let me just go back to Blender and reset the UVs so they are one per object. Let me clean house.

5:05pm. Some weird things are happening. The transfer to the new object works, but after I save and reload things get messed up.

5:10pm. What is this weird bug. It does not save correctly on reprojections. Everything ends up being messed up when I load.

5:20pm. I tried making a change like adding a layer and it saves properly.

Sigh, ok, good.

It looks so great. Let me export the textures and then I'll import them in Clarisse. After I do that, I'll be able to put the desk behind me. It has been over two weeks now. I've gotten way too sidetracked with the desk. It should have taken a few days at most.

5:35pm. Did the export. I wonder what clear channel means?

https://substance3d.adobe.com/documentation/spdoc/creating-export-presets-98959398.html

Ah, I see.

I am supposed to drag the channels to the right into those on the left. At first glance, I assumed that names had something to do with it, but they don't.

5:40pm. The exported textures are all there. Now I just need to bring them in Clarisse. Let me get on with it. I'll do that and maybe I can stop on time for once for the day.

5:50pm. Focus me, focus. How do I navigate in Clarisse. I've forgotten how to focus on objects.

Using F. Now focus. Import the desk. Put the textures on it. It should be a piece of cake.

6:50pm. Connected all the materials. Let me have lunch.

7:05pm. Let me watch some anime while I eat. I connected the shaders before I left, and the desk is showing up in object mode, but not when I put into scene view. I'll figure out why that is happening later.

7:20pm. I finished lunch just as the episode was starting. I'll resume it later. Let me place the desk where it is in the room and I will clear that task.

7:25pm. It does not seem like the height map is working properly.

7:35pm. This is problematic. The height values everywhere are too low. I'll have to adjust them and re-export the textures. 8 bit grayscale is not enough to capture thme. Instead I need to have them in the exact range. This is complicated. Is there some option to normalize the height maps in Substance Painter? Or do I just want to mend it by going over each layer in turn?

https://forum.substance3d.com/index.php?topic=17134.0
> I don't have any solid guidelines I use, except that all nodes that go towards driving height maps I keep as 16, because the difference when turned into normals is very noticeable... Usually results in noise or banding, which looks terrible on anything glossy, and often on non-glossy things, too.

Also, anything that will have its levels adjusted might need to be 16, too, since level adjustments can introduce banding effects.

I guess I'll go with 16 bit for the height maps.

8:40pm. I ended up pushing the height maps 10x by hand in addition to using 16-bit exports.

Tomorrow i am going to do some research on how to use global variables so I can bind the bump map distance for each shading group to it. That will allow me to scale them up and down uniformly. It is really annoying to have to go through each of the 18 shading groups by hand. I am thinking of doing research on how to setup textures as well, but in the future I'll be using UDIMs so I won't have to deal with so many texture sets for any particular object.

8:45pm. Today was pretty annoying, but I got the desk done. If I had decided to stick on the foolhardy path of retexturing everything it could have takem me half a week or more to get it done.

8:50pm. Let me remark, I tried playing with DIMs. With 4k textures the computer really starts grinding down. For those I'd need the 64 core Threadripper and a top of the line GPU. What I have here would not cut it. If it were 8k, I outright would not be able to do it. The computer would run out of memory and crash.

8:55pm. Obviously I am not going to start work on the monitor or the rig right now, so let me close here. It is time to unwind.

9pm. At this point I really have quite a lot. The foundation is hard surface modeling is almost established, I just need some practice to nail it down. I think that by the time I am done with my/Euclid's room I will have fully grown into it. After I do that, I'll start Heaven's Key for real.

I guess I'll do that by doing the particular scenes and sculpting the characters. I'll need a classrom, a city in the sky for the cover, an amusement part, a city on the ground.

Pretty complex scenes actually, but in 3d much like in 2d, things can be as complex as you need them to be. A city is hard, but if I start off with just a bunch of boxes, that will be a lot easier. You add details here and there, and soon you have a city.The same goes for anything else.

The reaon that the room is going so slowly is because I've just started learning texturing or hard surface modeling. I haven't touched that at all since that CG Fast Track course at the very start of the journey. I did do some toy props by following the tutorials, but that is a far cry from the kind of in depth thinking I had to do to deal with the desk in the past 2-3 weeks. In the first few months of the journey it was only enough to get me familiarized with Blender, it is right now that I am really mastering the subject matter.

In the next few months I'll really master environmental creation. I'll also get back to sculpting. Since I managed to do that base mesh, I am not bad at it anymore, but I still have ways to go there.

Master all these aspects and I can consider myself a pretty good generalist in 3d.

That is the plan for the next few months. If that programming offer does turn out to be something though, the plans will be put on hold while I go make money. If not, I'll stay the present course. Either way is fine. It is important in life to have development targets."

---
## [iradukud/Codewars](https://github.com/iradukud/Codewars)@[fa7fb17bbd...](https://github.com/iradukud/Codewars/commit/fa7fb17bbd853b107c33b35ae0d260dcc119ae9b)
#### Saturday 2022-04-16 20:15:03 by David Iradukunda

A_Strange_Trip_to_the_Market

You're on your way to the market when you hear beautiful music coming from a nearby street performer. The notes come together like you wouln't believe as the musician puts together patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or something silly like that, it dawns on you that you have been watching the musician for some 10 odd minutes. You ask, "how much do people normally tip for something like this?" The artist looks up. "It's always gonna be about tree fiddy."

It was then that you realize the musician was a 400 foot tall beast from the paleolithic era! The Loch Ness Monster almost tricked you!

There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A) it is a 400 foot tall beast from the paleolithic era; B) it will ask you for tree fiddy.

Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired of being grifted by this monster, the time has come to code a solution for finding The Loch Ness Monster. Note that the phrase can also be written as "3.50" or "three fifty".

---
## [kuroringo90/android_kernel_xiaomi_sm8150](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150)@[5546f4d819...](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150/commit/5546f4d819494725297183489ffcc4f61a1fa514)
#### Saturday 2022-04-16 20:54:00 by George Spelvin

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
## [locutus2/Stockfish](https://github.com/locutus2/Stockfish)@[cb9c2594fc...](https://github.com/locutus2/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-04-16 21:47:51 by Tomasz Sobczyk

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
## [lioniac/pokefirered](https://github.com/lioniac/pokefirered)@[c28e73a377...](https://github.com/lioniac/pokefirered/commit/c28e73a377904859dc49872d2f15a4550efcfa11)
#### Saturday 2022-04-16 21:54:13 by lioniac

[Base] Multiple BugFixes & Basic QOL
- Bugfix: Tall and Short Grass (Credit: Deokishisu)
- BugFix: Snow Weather (Credit: ghoulslash)
- BugFix: Multiple bugfixes already available in the code
- DEBUG: Debug Startup Script (Credit: Lunos)
- QOL: Extra Save Space (Credit: hjk321)
- QOL: Increased Max Money
- QOL: Removed redundant move grammar tables (Credit: Kurausukun)
- QOL: Fixed Default Names: Red(M), Green(F), Blue(Rival)
- QOL: Faster Joy (Credit: TheXaman and ghoulslash)
- QOL: Autorun
- QOL: Skip Controls+Battle Tutorial, Viridian Old Man, Flashbacks
- QOL: RenderText faster w/o pressing A or B buttons
- QOL: Game Start Options = Fast|Stereo|Set|True|LR
- QOL: Lower case after first input in Naming Screen (Credit: Jaizu)
- QOL: Emerald Bag Sort Ported (Credit: ghoulslash)
- QOL: Register LR (Freed SELECT button)
- QOL: Unhidden Power (Summary and Battle Screen)
- QOL: Pokemon Summary Screen: Nature Colored Stats
- QOL: Removed all FRLG item animation screens
- QOL: BW Repel/Reuse Field Medicine (Credit: ghoulslash/AsparagusEduardo)
- QOL: Enable NationalDex from Start
- QOL: Trainer class-based Pokéballs
- QOL: Better Givemon (Credit: Lunos/ghoulslash)
- QOL: Pokémon editor specials: EV,Moveset,Replenish PP (Credit: Lunos)
- QOL: Reusable TMs; Can purchase only one
- QOL: Expanded TMs up to 92; Only GenIII moves available
- QOL: HackMew's Shinyzer
- QOL: Removed badge boosts.
- QOL: Disable Bag Use In Battle (Credit: ghoulslash)
- QOL: Let a Pokémon forget any move they know (Credit: Lunos)
- QOL: Change Pokémon Nickname from Party Menu (Adapted from Shinny456)
- QOL: Nop Quest Log
- QOL: Increased boxes from 14 to 16
- QOL: Disable Pokémon Center Union Room check
- QOL: Surf Dismount Ground Effects
- QOL: Seed on startup
- QOL: Improved freecam
- QOL: Optimized WaitForVBlank
- QOL: Removed unecessary encryption of Pkmn struct data
- QOL: Allow Pichu Breeding with Volt Tackle
- QOL: Ported Pickup Mechanics (Credit: Lunos)
- QOL: Egg hatches at Lvl 1
- QOL: Physical/Special/Status split
- QOL: Fairy Type, Type Effectiveness Chart Updated
- QOL: Moves, Items and Learnsets Updated
--- Immunity, Limber, Insomnia, Vital Spirit and Magma Armor heal up on Switch
--- Damage Boost held items updated from 10% to 20% increase.
--- Wild Pokemon Held Items updated
--- Learnsets w/ early Leech Life moved to later lvls; Early = Absorb
- QOL: Shop Items By Badge Count (Credit: ghoulslash)
- QOL: TrainerMons EV,Nature,Gender,Friendship,Nicknames (Adapted from: surskitty)
- QOL: All FRLG Mons +Starters +GameCorner Update - Starters like in GenVII: Viridian Forest, Route 3, Route 4, Route 24
- Feature/Untested: Added Dive. Received at Viridian Gym (Credit: ghoulslash)
- Feature/Untested: Follow Me (Credit: ghoulslash)
- Feature/Untested: Quest Menu (Credit: ghoulslash)
- QOL: RTC code (Credit: Anthony La)
- QOL: Dynamic Overworld Palettes (Thanks hjk321)

---
## [Optimism333/vgstation13](https://github.com/Optimism333/vgstation13)@[622f3fac2b...](https://github.com/Optimism333/vgstation13/commit/622f3fac2b24476f23d8c9ebfae2dba5e371a3cc)
#### Saturday 2022-04-16 22:24:50 by ShiftyRail

The Thing Before Christmas (#31715)

I thought this was a good way to spice up the winter season.
While I know Ling was removed for a reason, I want you to consider that it got removed years ago. It is fair to say that the playerbase and the game changed so much since then than a "tabula rasa" might be justified.

Besides, ling had deathsting removed and its obnoxious chemical stings axxed too. (#23014)
From a QoL standpoint, the stings have been converted to spells and should be as easy to use as the vampire ones.

As a final note, it's painstaingly true that ling is the least worked over of all our antags and is in dire need of some love and new content. However, this content can only come if people experience ling first-hand and get motivated to fix it.

Worse come to worse, we remove it again lole

Merry Christmas everyone.

:cl:
- rscadd: Santa Claus is coming to town. More specifically, he's coming to Antartica. Wait, he was already here all this time? And why does he look so familiar... OH GOD HELP

---

