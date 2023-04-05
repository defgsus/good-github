## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-04](docs/good-messages/2023/2023-04-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,212,952 were push events containing 3,450,057 commit messages that amount to 273,726,440 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[7a64573c8b...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Tuesday 2023-04-04 00:33:44 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[ec67ffb340...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/ec67ffb340b3c4a64f17eb6458a32cb55ae5183b)
#### Tuesday 2023-04-04 00:33:44 by SkyratBot

[MIRROR] Properly accounts for byond tick fuckery in runechat code [MDB IGNORE] (#20237)

* Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

* Properly accounts for byond tick fuckery in runechat code

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[f3614ce53c...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/f3614ce53c9f02d6c4e21b935b6231e98d3348af)
#### Tuesday 2023-04-04 00:33:44 by SkyratBot

[MIRROR] Thrown containers splashing on mobs spill some contents on the floor [MDB IGNORE] (#20252)

* Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* Thrown containers splashing on mobs spill some contents on the floor

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[c0ef4ba907...](https://github.com/necromanceranne/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Tuesday 2023-04-04 00:34:30 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[ccef887efe...](https://github.com/necromanceranne/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Tuesday 2023-04-04 00:34:30 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [Mey-Ha-Zah/tgstation](https://github.com/Mey-Ha-Zah/tgstation)@[c3b78761d2...](https://github.com/Mey-Ha-Zah/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Tuesday 2023-04-04 00:39:46 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[e1221c986f...](https://github.com/Jalesen/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Tuesday 2023-04-04 01:07:40 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [corbin-poteet/put-me-on](https://github.com/corbin-poteet/put-me-on)@[303f8e2d88...](https://github.com/corbin-poteet/put-me-on/commit/303f8e2d88f116115932cecb29f3e92138a22a93)
#### Tuesday 2023-04-04 01:49:12 by Corbin Poteet

Fixed every stupid fucking warning it was bitching about jesus fucking christ fuck you expo

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[ca94646107...](https://github.com/k21971/EvilHack/commit/ca94646107afae7264756d266847f628e2f0a128)
#### Tuesday 2023-04-04 02:52:43 by k21971

Make the archangel Saint Michael a unique monster.

The named archangel Saint Michael at the end of Purgatory has been
upgraded, and is now a unique angel. He retains many of the properties
of a normal archangel, but can also employ the magic missile attack of a
regular angel.

I may make some minor adjustments to this, but this is a good start.
While not as strong as the demon princes encountered in Gehennom, Saint
Michael is definitely more powerful than his earlier form as a regular
archangel.

---
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[9d96300571...](https://github.com/zinc-collective/convene/commit/9d963005716ebc9da222fa878f138afff09f0d1b)
#### Tuesday 2023-04-04 02:53:22 by Zee

✨🥔🥗 `Marketplace`: Validate delivery independently (#1292)

* `Marketplace`: Sprout `Cart::Delivery` scaffolding

- https://github.com/zinc-collective/convene/issues/831

When a `Shopper` sets their delivery info, they now get error messages
if they do not provide sufficient information (i.e. leave their phone
number blank)

In order to accomplish that, I:

1. Pulled out the `cart/deliveries/_delivery` and `cart/deliveries/_form` partials from `_cart`
2. Sprouted a new `Cart::Delivery` model, with corresponding
   `Cart::DeliveriesController` and `Cart::DeliveryPolicy` objects

It's feeling a little like we want a `Cart` to `has_one :delivery` and
move the encrypted data into that.

However, I'm not quite ready to do that, since I would rather:

- [ ] Make it purty! It's pretty ugly right now
- [ ] Make it safe! It's not tested *remotely* enough

Well where did you come from

* 🥗 `Marketplace`: Test `DeliveriesController`!

We ran into a number of problems here, in particular testing turbo
streams when there is a `respond_to` block does not apparently work
nearly as well as we wish it did

Co-authored-by: Dicko Sow <s12dsow@users.noreply.github.com>

🧹 `Marketplace`: Appease the Rubocop

* Use new location syntax

* 🛠️ `Marketplace`: Add a factory for `Cart::Delivery`

* 🛠️ `Neighborhood`: `have_rendered_turbo_stream` compares the body

OK this is way tooooo greedy but it's so dang close...

* Helps when I use the right gosh-darn thing thang

* And some tests on update!

* Get rid of that there whitespace

* 🥗 `Marketplace`: Validation specs for `Cart::Delivery`

---
## [SwapnilVicky/namaste_xiaomi_miatoll](https://github.com/SwapnilVicky/namaste_xiaomi_miatoll)@[6f52d1ab2e...](https://github.com/SwapnilVicky/namaste_xiaomi_miatoll/commit/6f52d1ab2e5f8a038d907e6cfe70c2d5b528600d)
#### Tuesday 2023-04-04 03:15:15 by Maciej Żenczykowski

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b5ebf5c942...](https://github.com/tgstation/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Tuesday 2023-04-04 04:16:41 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4e86fc8df2...](https://github.com/cmss13-devs/cmss13/commit/4e86fc8df2247dcb18b14e473d6ab6cca3c7567d)
#### Tuesday 2023-04-04 05:08:35 by victorjosephespinoza

Let (whitelisted) ghosts join in as Working Joes (#2963)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

https://forum.cm-ss13.com/t/make-it-so-ghosted-players-can-spawn-in-as-working-joes/588
Adds a ghost verb so ghosts can now join the game as working joes.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Like it was said in the forum post, Joes are pretty much harmless, their
impact on the round is pretty much minimal, so adding this wouldn't
imply any balance change whatsoever.

The intent of adding something like this to the server is mainly trying
to get more attention to the role. Which is barely played at the moment,
however, if dead players could now respawn as them, I believe it might
get more activity.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
Unsure of what kind of debugging I could provide in here, request any in
the comments and I'll do it.

There's a high chance that something is not treated as it should. This
is probably the first PR where I had to look and understand what I was
writing, despite the fact that a lot of the code is taken from the pred
initialization. So yeah, if you would have placed something somewhere
else, or differently, go ahead and tell me.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:H20Begod
add: Added a new verb for ghosts to join in as working joes (ONLY
WHITELISTED GHOSTS).
code: Edited max spawns of the working joes to 3.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/silicons/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Tuesday 2023-04-04 05:30:55 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/silicons/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Tuesday 2023-04-04 05:30:55 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [rageguy505/ragestation](https://github.com/rageguy505/ragestation)@[c18b1ef442...](https://github.com/rageguy505/ragestation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Tuesday 2023-04-04 05:53:46 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[c27f9a6d9b...](https://github.com/Enbyy/orbstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Tuesday 2023-04-04 06:33:14 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[95b810919e...](https://github.com/Enbyy/orbstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Tuesday 2023-04-04 06:33:14 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[b3e5642d94...](https://github.com/DrDiasyl/tgstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Tuesday 2023-04-04 07:55:47 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [mshurkaeu-public/i-care.by](https://github.com/mshurkaeu-public/i-care.by)@[d02ec52235...](https://github.com/mshurkaeu-public/i-care.by/commit/d02ec522354820d0e8530b0af849eaf8252cec06)
#### Tuesday 2023-04-04 09:29:52 by Mikalai Shurkaeu

The very first draft for #1

Developed during period 2023-02-15 - 2023-03-10.

Originally the idea in the issue was to create a mobile app with a name
like "who-is-he-how-is-she-meter".

When I started to work on the implementation I realized that it actually
would do the very basic and useful things to care about the most important
person in user's life. Thus I decided that the name of the app would be
something like "i-care.by <platform> app".

I chose Flutter to write code once and then compile it to different
target platforms.

"i-care.by web app" is available at
https://mshurkaeu-public.github.io/i-care.by-app/web/

In this first commit the following is implemented:
1. User preferences (name and preferred pronoun).
2. Display the list of the diary records on home page.
3. Editing today record (- want to do today, - emotions in that moment,
- done today, - emotions in that moment)
4. Options to answer "who is the most important person in your life" are
randomized on each run, so the user needs to focus and find the
appropriate one.

Each day the application asks (trigerred by user)
1. Who is the most important person in your life?
2. What do you want to do for the person today?
3. What are your emotions and feelings in this moment?
--
then, presumably in the second part of the day,
4. What did you do for the person today?
5. What are you emotions and feelings in this moment?

The answers are recorded and stored in json format.
On web platform - in window.localStorage.
On other platforms - in application documents folder.
----

I want to say thank you to the following people, who helped me to create
this first draft (chronological order, most recent accepted help go first,
sorted by "accepted on" because there was a time lag between a moment the
help was provided and when results appeared in the application (and some of
the already provided hints are not yet incorporated into the application)):

2023-03-10 02 🦸 — provided valuable feedback about my texts.
And that helped to make the texts more clear.

2023-03-10 01 🦸‍♀️ — aspired me to highlight in the application UI that the
"want to do" list is a list of desires and not a list of "duties".

2023-03-06 02 🦸 — aspired me to implement support of the preferred pronoun
setting and thus to implement more user-friendly texts.

2023-03-06 01 🦸‍♀️ — aspired me to implement the ability to edit user's name
via UI sooner.

2023-03-05 02 🦸 — found errors in text on the second introductory screen and
shared a feeling that was not clear what to do after the "want to do today"
list was populated.

2023-03-05 01 🦸‍♀️ — aspired me to think how to implement proper validation for
a list of persons to actually be a list of several persons.

2023-03-04 🦸‍♀️ — shared own vision about the target audience and that helped
me make my own vision of that audience clearer and to reflect that in texts.

2023-02-28 🦸 — found a typo on the second introductory screen and also
aspired me to think about UI element positioning and to make button "Next"
closer to "major events".

2023-02-15 🦸 — recommended me to use Flutter to achieve my goal
"one code -> many target platforms". I hadn't known about Flutter before that.

---
## [astrolemonade/awesome-docker](https://github.com/astrolemonade/awesome-docker)@[3164d6df94...](https://github.com/astrolemonade/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Tuesday 2023-04-04 10:28:18 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5b1b936d3e...](https://github.com/treckstar/yolo-octo-hipster/commit/5b1b936d3e9ee6fe08c0374b475c56a5ffb70f8b)
#### Tuesday 2023-04-04 11:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Pl1997/bridge](https://github.com/Pl1997/bridge)@[d8bb3cddfb...](https://github.com/Pl1997/bridge/commit/d8bb3cddfb9c310542649baf5c0e0cdeffa8a697)
#### Tuesday 2023-04-04 11:39:43 by Pl1997

Add video services to whitelist

Hello,

First of all, I want to thank you for this amazing service, which I recently discovered... It is a great pleasure to work with it ! I recently encountered a few problems with a project of mine, which makes use of Youtube. Since this website is : 
# 1. Completely free service
# 2. Used by a lot of people
# 3. Easily handle million hits

...I hereby suggest to add it to the Firewall whitelist. Please forgive me if this request seems dumb to you... I'm no professional, and I probably don't understand every implication of such a modification !

---
## [Carreau/napari](https://github.com/Carreau/napari)@[3ec4be1ae8...](https://github.com/Carreau/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Tuesday 2023-04-04 12:08:57 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [rik0612c/android_kernel_sony_msm8996](https://github.com/rik0612c/android_kernel_sony_msm8996)@[820e74a30f...](https://github.com/rik0612c/android_kernel_sony_msm8996/commit/820e74a30f958c840bc99b42312f2c859e3ed737)
#### Tuesday 2023-04-04 12:51:50 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [vaadin/flow](https://github.com/vaadin/flow)@[0a1da07df3...](https://github.com/vaadin/flow/commit/0a1da07df303aa5b477e736e528c0a3c59391e07)
#### Tuesday 2023-04-04 13:29:56 by czp13

chore: added more covering tests to ComponentTest.java for covering getLocale() method (#16367)

* Added more covering tests to ComponentTest.java for the getLocale method. It was needed, because another external contributor PR is tackling
a refactor/optimization of this method (as well), and this change it will ensure the functionality, and execution branches are the same. (https://github.com/vaadin/flow/pull/16160)
* Fix typo/my bad in ComponentTest.java
* mvn formatter:format executed
* Locale.US is the first element of this list: List.of(Locale.US, Locale.CANADA_FRENCH);
 Not CANADA_FRENCH (night facepalm for myself)
 Should fix this error:
 "java.lang.AssertionError: First provided locale should be returned expected:<fr_CA> but was:<en_US>""
* Implemented @mcollovati review idea on creating provided locales.
Thank you ;)

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[5a34d92cb5...](https://github.com/microsoft/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Tuesday 2023-04-04 14:15:22 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [WilliamTDoran/BTGD9855](https://github.com/WilliamTDoran/BTGD9855)@[7b1ba2fac6...](https://github.com/WilliamTDoran/BTGD9855/commit/7b1ba2fac6683c101adbece22d44fccea0a5ce10)
#### Tuesday 2023-04-04 15:17:09 by WilliamTDoran

lil baby yara boss animation fix. man, one time when i was in vancouver i got this earl grey flavoured shortbread and fucking man it was so good

hoo boy this tea i am drinking is really weak frankly just kinda watery.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[60d2d2ee1a...](https://github.com/Stalkeros2/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Tuesday 2023-04-04 15:51:34 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [hackerdeen/meetings](https://github.com/hackerdeen/meetings)@[6d5e085699...](https://github.com/hackerdeen/meetings/commit/6d5e085699084255e1a5cf4e8955d1510a713526)
#### Tuesday 2023-04-04 16:04:36 by Andy Gaskell

From Wouter's email 

Thanks @Derecho00

Directors Report 2021-2023
----------------

## 0) State of the Membership
- We currently have 19 members on our register
- We have 12  memberspaying regularly, resulting in a monthly income of £240.
- 7 dismemberment emails have been sent and this has resulted in some members coming back into the fold.
- Incoming Directors shall need to have a board meeting to finalise dismemberment following AGM.  


## 1) 'Post pandemic' activities
- Open Tuesday's have returned post pandemic in 2021
- Winter party 2022 was a roaring success. Thanks go to Q for making it so busy and inviting their friends who helped remind some of us why running a hackerspace is such good fun.
- Monthly Consular Convention for Control & Prohibition of Pandemics were introduced in 2021.

## 2) Books Tax & HMRC
- We're still doing our own books, this saves us ~£500 in accounting fees, so is still good.  Thanks Andy and irl.
- We are now recognised as tax dormant to HMRC. This status will last either until April 2026 or until income deriving from non-member sources execeeds an annual corporation tax liability of £100, whichever occurs first.

## 3) Funding and Grants
Vishnee pulled together a funding application for Just Transition Participatory Budgeting, and we were dismayed to learn this amounted to a popularity contest and public vote. Thanks for your efforts, and the information gathered/text written will help us in future endeavours.

## 4) Workshops & Outreach
Midder has been very active in recruiting new faces through the social center and alternative freshers fair, thank you for your efforts.
We'd like more regular faces to become members and to recruit new faces so there is a fresh flow of new people and income to keep us stable.
Any efforts on recruitment would be greatly appreciated. irl put in good work on updating the membership process and we generally agree this needs simplified and what you're signing up for has to be more clearly signposted.

## 5) Digital Infrastructure
Lots of things were rationalised and restarted this year.
garioch.57north.org.uk was retired, thank you for your service.

Hibby moved the wiki from hackr->scotcon->ythan.57north.org.uk.

The website now resides on ythan.

Mailing Lists were migrated to ythan, worked, didn't work, hibby had a meltdown, they worked again, now consistently.

Outstanding projects that need volunteers to look at:
  * Removing ID from hackhub
  * Modernising/updating hackhub to allow simple edits like adding admin-permissions checkbox and allowing users to change address
  * Migrating hub to a more modern server and allowing a print out of the list of registers
  * Making the website a static site with more relevant information

## 7) Workshops and programs
We've not done much in regard to this. Hopefully this will be something we can do more of in the next 12 months.

## 8) Equipment
A whole new collection of kit has arrived in the space. Thank you to all contributors. Here are few listed (and many other forgotten).
- Laser cutter
- Tables and chairs
- Canon A0 printer with scanner
- Disco light setup.
- and so much more

## 9) Remote or distant members
This is discussed at this AGM.

## 10) Events
Some members went to EMF Camp and had an awesome time (according to rumours).

## 11) Links and refs
AGM anouncement - https://lists.57north.org.uk/mailman3/hyperkitty/list/57north-announce@lists.57north.org.uk/thread/ZVGI66Z6E743WHFQRTOCR6UY6Y62ZH5W/
Last year's AGM minutes -  https://github.com/hackerdeen/meetings/blob/master/2021/2021-05-04%20AGM%20Minutes.md
2021 year's Directors report -  https://github.com/hackerdeen/meetings/blob/master/2021/21-05-04-directors-report.md
Last year's treasurer's report - https://github.com/hackerdeen/meetings/blob/master/2021/Treasurers%20Report%20-%20YE%2028th%20February%202021.pdf

---
## [Vincent392/antiTL2-lib](https://github.com/Vincent392/antiTL2-lib)@[4cf81a115d...](https://github.com/Vincent392/antiTL2-lib/commit/4cf81a115dcc98c6bbcac140bb2a452f4e8620a2)
#### Tuesday 2023-04-04 16:22:25 by Vincent392

Create TL2detect.java

FUCK YOU TL INC! YOU DON'T HAVE LEGAL STUFF I  IRELAND!

---
## [SmashedFrenzy16/terminal](https://github.com/SmashedFrenzy16/terminal)@[446f280757...](https://github.com/SmashedFrenzy16/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Tuesday 2023-04-04 16:38:45 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [SmashedFrenzy16/terminal](https://github.com/SmashedFrenzy16/terminal)@[9ccd6ecd74...](https://github.com/SmashedFrenzy16/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2023-04-04 16:38:45 by Mike Griese

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

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[32b158e5d0...](https://github.com/odoo-dev/odoo/commit/32b158e5d09d7d11b1984b36d558288ba0b88476)
#### Tuesday 2023-04-04 17:25:10 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[20b97168ed...](https://github.com/mrakgr/The-Spiral-Language/commit/20b97168ed9c5538da0bbcd11adf7190ffe2ef68)
#### Tuesday 2023-04-04 17:42:41 by Marko Grdinić

"///

>Humans are like isolated islands, floating in the sea of fate.
>Human encounters are like the collision of these loneliness islands, and once they touch, there would be an effect.
>Sometimes, the islands would stick together, in the name of ‘interest’, ‘kinship’, ‘friendship’, ‘love’ and ‘hate’.
>But eventually, they would separate, walking towards the path of destruction.
>This is the truth behind life.
>Unfortunately people are always afraid of being alone, they craved the liveliness of human crowd, and they refused to do nothing with their time.
>Because once they face loneliness, it meant facing pain and hardship.
>But once they can face this pain, people would obtain talent and courage. Thus, there is a saying — High achievers are definitely lonely.
>“This is the feeling of being lonely. Every time I savour this, it strengthens my resolve to pursue the demonic way!” Fang Yuan’s gaze shone, thinking of the story of Ren Zu.
Not all Asians are submissive cattle

///

Based RI quote I found while lurking the archive.

10:25pm. https://youtu.be/jgpVdJB2sKQ
Redis Crash Course

Ah, let me watch this for a bit. Who cares about that Dohna^2 H scene in the background.

https://youtu.be/jgpVdJB2sKQ?t=92
> Redis runs inside your working memory...

Not what I expected at all. I guess it is something completely different to what I thought it would be.

https://youtu.be/jgpVdJB2sKQ?t=1640
> And that is everything you need to know to get started with Redis.

Sigh. It is no big deal at all.

https://www.youtube.com/results?search_query=api+gateway

I'll check out the API gateway tomorrow.

https://re-library.com/translations/destiny-unchain-online/volume-1/prologue-1-guild-ranking-competition/

Re;Library picked up DUO.

I'll leave it for tomorrow. Time for bed.

4/4/2023

9:45am. I am up. Any mail? Nope.

9:50am. Anyway, today on the agenda is to finish up the auth video. After that I want to study up on microservice and API gateways. After that the first thing I want to do is set up CI on Github for the CFR and the template project.

I want to figure out how that works.

10am. Mhhh, let's get started.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=2393

Let me resume from where I left off yesterday. I have no idea what this aspnet code generator is but whatever. Let's just go forward.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/tools/dotnet-aspnet-codegenerator?view=aspnetcore-7.0

Ah, it does the same thing the ide does.

Maybe it is not as complicated as it seems.

10:25am. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=3374

He is really flying over this. If I wanted to learn this instead of listening to him, I really should just go through the module. But let me watch the video.

10:35am. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=3692

Enough of this. I can't follow this, it is a waste of time. I'll figure out how to use 3rd party auth.

I'll Google MS Identity platform.

10:45am. Actually, let me just study whatever I want.

Let me watch this video for longer since I feel like grinding. Then I'll study microsevices.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=3901

I have an real issue with this. Just how am I supposed to make use of this with Fable or with Elmish Bridge?

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=3931

This isn't too bad. You just get the HttpContext and check the claims. How would that be possible with remoting.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=4441

Oh wait, here is another guy and he is going to show how to do it through the cloud. Good thing I kept watching. It seems there are two presentations in a single vid.

11:10am. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=4631

After I am done with this, I'll study microsevices, but after that I'll look at the Fable Remoting docs. I really am interested how I could get cookies and auth tokens from inside an interface. I sort of get how to do it inside the ASP.NET middleware, but Elmish Bridge and Remoting feel like isolated islands.

I am not there yet as a web dev. I need to build a proper system. Right now I at least know how to send messages back and forth, but not how to build the whole package.

...

I won't resent thme. I might not be getting calls, but I wouldn't hire myself in this state.

I can resent the field of ML for scamming me, but I am the one who let that happen to me. I am the one who decided to put my trust into the Singularity.

For the past 16 years, I could have done literally anything other than the path I've taken, and I'd have been far more successful. I could have been a write, artist, you name it, and it would have worked out better.

11:15am. I am going to fucking learn these cloud services, learn web dev and then I'll be able to monetize my programming skills. Whether I get a job or build platforms does not matter.

Anything is better than having to endure the kind of humiliation that was heaped upon me between late 2021 and now.

The AI hardware will get here, but companies are vermin. For not recognizing my skill and effort, or how much benefit Spiral could bring them.

Tenstorrent might open up its cloud later in the year, but it would just serve to highlight how ridiculous my approach was, and how pointless my effort a how great my naivette was if that happens, but I can't afford to rent those pieces of hardware.

11:20am. If the Singularity wants to humiliate me this much, then why am I trying so hard to earn its affection?

There are better ways out there.

11:45am. Had to take a short break, let me resume.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=4813
> I can have anybody log in with their Github account or their Facebook account.

12pm. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=5300

They'll create a node js application.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=5435

It just sends the index html file back. This could be a good tutorial, I find the high level nature of the .NET stuff confusing when learning, so it is good that they are doing it this way.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=5636

This is a somewhat confusing way of doing a tutorial. I guess I'll just roll with it.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=5748

Super confusing. Who is going to follow this?

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=5905

I am going to find a way to make this elegant. This tutorial is shit.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=6120

Let me stop here. It was a mistake. I should have aborted it at the 1h mark.

12:15pm. https://stackoverflow.com/questions/66100093/safe-stack-with-github-authorization

Let me start from here. I seems like I keep making the same mistake over and over of just grinding tutorials. I should make it a rule to just go the other way whenever I feel myself tuning out. Maybe following the steps in those aka.ms learning modules directly would have been better.

https://www.compositional-it.com/news-blog/

There are a lot of F# articles here.

https://www.compositional-it.com/news-blog/calling-python-from-f-with-fable/

Check this out. This is what I wanted to do for ML. Nevermind it for now.

12:25pm. https://www.compositional-it.com/news-blog/safe-authentication-with-azure-active-directory/
https://carpenoctem.dev/blog/fsharp-giraffe-auth-identity-ef-core/

Ah, let me take a break here. I'll check out those articles later.

12:35pm. Forget wasting time like I have. Happiness can only be caught by chasing after it directly.

> Just wanted to say thank you for this series.  I haven't had time to sit down and do it end to end yet, but just glancing through it has cleared up so many pain points i've run into before, and end to end with things like actual deploying to azure helps clear up SOOO many missing parts.

Got this comment on Youtube. Nice.

Oh right, I meant to check out how long it was since my last vid. 2 days ago.

12:40pm. It is important to make progress. I do not want to spend weeks before the next video. Just implement auth for the SAFE stack application and make the next video. Move from there.

1:55pm. Done with breakfast and chores.

2pm. Let me start. Focus me.

I've come up with some goals. Instead pussyfooting about it, I'll make some very clear goals and follow them to the end. After that, I will have cleared the auth hurdle.

First, let me read those articles.

https://www.compositional-it.com/news-blog/safe-authentication-with-azure-active-directory/
> Note - the blog below is quite out of date now, the SAFE template has moved on from V2 and some of the Azure libraries are different as well. I have an example I am keeping up to date here

https://github.com/CompositionalIT/SAFE-AD-Auth-example

I'll clone this later, let me just read the article.

> Now that you have enabled authentication, you just need to tell ASP .NET Core which endpoints to secure.

https://zaid-ajaj.github.io/Fable.Remoting/#/advanced/integrating-dependency-injection

> Now this fromValue function expects an intance of the protocol. This instance however, could have dependencies. For example, it is possible that in order to create an instance of the IMusicStore, you need to know connnection string to a database which you can use in the implementation of the instance

Ohh, it is possible to add dependencies in Fable Remoting.

```fs
let musicStore (logger: ILogger<IMusicStore>, config: IConfiguration) = {
    (* Your implementation here *)
}

let webApi =
    Remoting.createApi()
    |> Remoting.fromContext (fun ctx ->
        // require dependencies
        let logger = ctx.GetService<ILogger<IMusicStore>>()
        let config = ctx.GetService<IConfiguration>()
        // create a music store from the dependencies
        musicStore(logger, config)
    )
```

This answers a lot on how to use Fable remoting. I wonder if there is an equivalent thing for Bridge.

Nevermind that for now. Let me get back to the auth article.

I sort of get the authentication part, but I really want to know how I can change the policies for a particular user.

```fs
let buildRemotingApi api next ctx = task {
    let handler =
        Remoting.createApi()
        |> Remoting.withRouteBuilder Route.builder
        |> Remoting.fromValue (api ctx)
        |> Remoting.buildHttpHandler
    return! handler next ctx }
```

Take a look at this. Is this how building stuff in Giraffe works?

```fs
let authScheme = "AzureAD"

let isDevelopment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT") = Environments.Development;

let noAuthenticationRequired nxt ctx = task { return! nxt ctx }

let requireLoggedIn : HttpFunc -> HttpContext -> HttpFuncResult =
    if isDevelopment then
        noAuthenticationRequired
    else
        requiresAuthentication (RequestErrors.UNAUTHORIZED authScheme "My Application" "You must be logged in.")

let api ctx =
    { Endpoint = endpoint1Func }

let routes =
    choose [
        subRoute "/api" (requireLoggedIn >=> buildRemotingApi api)
    ]
```

This isn't too hard. Yeah, this kind of simplicity is what I am interested in.

Still, how is it checking the claims? No doubt the code for that is buried in `requiresAuthentication`. Let me check out the next part in the article. Then I'll dive into Giraffe.

https://www.compositional-it.com/news-blog/safe-stack-authentication-with-active-directory-part-2/

2:25pm. It feels like I am on the right track. Next, let me check out the Giraffe article.

https://carpenoctem.dev/blog/fsharp-giraffe-auth-identity-ef-core/

In fact this is only the part 4.

https://carpenoctem.dev/blog/giraffe-by-example-understanding-asp-net-core-boilerplate/

Oh this is not that article from years ago which got me interested in it.

///

Giraffe is one of the leading web frameworks for F#. It provides a wonderful functional interface while allowing seamless access to existing ASP.NET Core libraries.

However, getting started with Giraffe may be intimidating to someone with no ASP.NET Core experience, because even the simplest application requires ~50 lines of ASP.NET Core-specific boilerplate code. The last thing one wants to do while learning F# and Giraffe is to have to learn another huge framework, documented mostly for C# developers.

I hope this article will be a useful guide for such a person.

///

```fs
[<EntryPoint>]
let main args =
    let contentRoot = Directory.GetCurrentDirectory()
    let webRoot     = Path.Combine(contentRoot, "WebRoot")
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(
            fun webHostBuilder ->
                webHostBuilder
                    .UseContentRoot(contentRoot)
                    .UseWebRoot(webRoot)
                    .Configure(Action<IApplicationBuilder> configureApp)
                    .ConfigureServices(configureServices)
                    .ConfigureLogging(configureLogging)
                    |> ignore)
        .Build()
        .Run()
    0
```

You can set the content root like this?

2:45pm. > Loading configuration settings from environment variables, configuration files (appsettings.json), and other sources;

I really wish I could have started my journey with this article in 2020. It would have made things a lot easier.

2:55pm. https://carpenoctem.dev/blog/anatomy-of-giraffe-httphandler/

This is very clear.

> Note that HttpContext is Microsoft.AspNetCore.Http, the same one that C# applications would use.

https://github.com/giraffe-fsharp/Giraffe/blob/master/src/Giraffe/HttpContextExtensions.fs#L87

3:05pm. https://github.com/giraffe-fsharp/Giraffe/blob/master/src/Giraffe/HttpContextExtensions.fs#L162

```fs
    /// <summary>
    /// Retrieves the <see cref="System.String"/> value of a cookie from the request.
    /// </summary>
    /// <param name="ctx">The current http context object.</param>
    /// <param name="key">The name of the cookie.</param>
    /// <returns>Returns Some string if the cookie was set, otherwise returns None.</returns>
    [<Extension>]
    static member GetCookieValue (ctx : HttpContext, key : string) =
        match ctx.Request.Cookies.TryGetValue key with
        | true , cookie -> Some cookie
        | false, _      -> None
```

You can get cookies like this.

```fs
route "/" >=>
    choose [
        choose [ GET ; HEAD ] => indexHandler
        GET => neverExecuted ]

GET >=>
    choose [
        routef "/hello/%s" => indexHandler
        route "/hello/world" => neverExecuted ]
```

Oh, this is a thing?

```fs
// synchronous version
let stopRightThere (rejectionReason : string) : HttpHandler =
    fun (next : HttpFunc) (ctx : HttpContext) ->
        ctx.SetHeader("X-Rejection-Reason", rejectionReason)
        ctx.SetStatusCode 400
        Task.FromResult (Some ctx)

// asynchronous version
let stopRightThereAsync (rejectionReason : string) : HttpHandler =
    fun (next : HttpFunc) (ctx : HttpContext) ->
        task {
            ctx.SetHeader("X-Rejection-Reason", rejectionReason)
            ctx.SetStatusCode 400
            // do some asynchronous stuff here, like logging this incident to a database.
            return! Task.FromResult (Some ctx)
        }
```

He could have written that last line as just `Some ctx`.

Interesting that this returns the context. Given that it is being updated in a mutable fashion, I wonder why that is the case?

> See the source, it is not scary at all.

https://github.com/giraffe-fsharp/Giraffe/blob/master/src/Giraffe/Routing.fs

3:35pm. https://github.com/giraffe-fsharp/Giraffe/blob/master/src/Giraffe/Routing.fs#L45
> Filters an incoming HTTP request based on the port.

Oh, this exists?

```fs
    /// <summary>
    /// Filters an incoming HTTP request based on the port.
    /// </summary>
    /// <param name="fns">List of port to <see cref="HttpHandler"/> mappings</param>
    /// <param name="next"></param>
    /// <returns>A Giraffe <see cref="HttpHandler"/> function which can be composed into a bigger web application.</returns>
    let routePorts (fns : (int * HttpHandler) list) : HttpHandler =
        fun next ->
            let portMap = Dictionary<_, _>(fns.Length)
            fns |> List.iter (fun (p, h) -> portMap.Add(p, h next))
            fun (ctx : HttpContext) ->
                let port = ctx.Request.Host.Port
                if port.HasValue then
                    match portMap.TryGetValue port.Value with
                    | true , func -> func ctx
                    | false, _    -> skipPipeline
                else skipPipeline
```

Here is the whole thing. I had no idea that ports were just a part of the context.

Though this is a bit confusing. Doesn't the server have a specific port?

> Filters an incoming HTTP request based on the request path using Regex (case sensitive).

You can even route using Regex? That is something.

4pm. Had to take a break, let me resume. I am a lot more into this than watching those videos. The Giraffe source is quite informative.

https://carpenoctem.dev/blog/anatomy-of-giraffe-httphandler/

///

One trick illustrated in the official documentation is:

```fs
let earlyReturn : HttpFunc = Some >> Task.FromResult

let checkUserIsLoggedIn : HttpHandler =
    fun (next : HttpFunc) (ctx : HttpContext) ->
        if isNotNull ctx.User && ctx.User.Identity.IsAuthenticated
        then next ctx
        else setStatusCode 401 earlyReturn ctx
```

///

Ohhh, this is exactly what I wanted to know.

I won't be able to do check the user in the interface itself. Instead I will make sure to route it to the right parts.

https://carpenoctem.dev/blog/fsharp-giraffe-jwt-auth/
JWT Authentication and Authorization for your Giraffe API Server

This is what I want.

> This article is about authenticating and authorizing requests in a Giraffe server using JWT, or JSON Web Tokens.

So that's what JWT stands for.

https://en.wikipedia.org/wiki/Base64#The_URL_applications

> Common to all binary-to-text encoding schemes, Base64 is designed to carry data stored in binary formats across channels that only reliably support text content. Base64 is particularly prevalent on the World Wide Web[1] where one of its uses is the ability to embed image files or other binary assets inside textual assets such as HTML and CSS files.[2]

I see.

4:30pm.

```fs
// enable authentication system-wide... needed for all authentication middleware.
services.AddAuthentication(fun opt ->
    // See Note 1
    opt.DefaultAuthenticateScheme <- JwtBearerDefaults.AuthenticationScheme

    // Not needed, see Note 2 below
    // opt.DefaultChallengeScheme <- JwtBearerDefaults.AuthenticationScheme

// Second, we configure our middleware
).AddJwtBearer(fun (opt : JwtBearerOptions)->

    // You can set general options of JWT authentication here.
    // Find more details at:
    //   https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.jwtbearer.jwtbeareroptions?view=aspnetcore-5.0
    // Note, however, most of it is not relevant for our simple case

    opt.TokenValidationParameters <- TokenValidationParameters(
        // You can configure the actual authentication parameters and options.
        // See more at:
        //   https://docs.microsoft.com/en-us/dotnet/api/microsoft.identitymodel.tokens.tokenvalidationparameters?view=azure-dotnet

        // SecurityKey that is to be used for signature validation.
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(key)),

        // boolean to control if the issuer will be validated during token validation.
        ValidateIssuer = true,

        // String that represents a valid issuer that will be used to check against the token's issuer. The default is null.
        ValidIssuer = issuer,

        // boolean to control if the audience will be validated during token validation.
        ValidateAudience = true,

        // string that represents a valid audience that will be used to check against the token's audience. The default is null.
        ValidAudience = audience
    )) |> ignore
```

Sigh, what a pain in the ass. This will take a while to figure out.

4:35am. https://carpenoctem.dev/blog/fsharp-giraffe-jwt-auth/

```fs
let requireAdminRole : HttpHandler =
    requiresRole "Admin" (RequestErrors.FORBIDDEN  "Permission denied. You must be an admin.")
```

4:45pm.

```fs
        let dob = Convert.ToDateTime(dobClaim.Value) // please add error handling in prod
        let age = DateTime.Today.Year - dob.Year
        // account for leap year https://stackoverflow.com/a/1404/
        let correctedAge = if dob > DateTime.Today.AddYears(age) then age - 1 else age
        correctedAge >= minAge
```

Sigh, instead of doing this shit, why not just divide by the number of days?

4:50pm.

> However, I don't know when Giraffe programmers would want to use a policy over a simple HttpHandler, as shown in the previous section. For C# programmers, policies make things more succinct since they apply policies using attributes on Controllers. However, the plain-old F# syntax (using handlers and >=>) is even more succinct.

I've really been immersing myself in this article. Ok, I really get it now.

```fs
let webApp =
    GET >=> authenticate >=> choose [
        route "/admin-policy"  >=> requireAdminPolicy      >=> text "welcome, admin, you were authorized by policy"
        route "/tavern-policy" >=> requireMustBe21ByPolicy >=> text "welcome, here's your gin and tonic and policy!"
    ]
```

With examples like this, it is not hard to understand authentication and authorization works with Giraffe.

4:55pm. https://carpenoctem.dev/blog/fsharp-giraffe-auth-identity-ef-core/

Let me move to this last part of the series.

I feel like I've grasped half of authorization and authenticantion. What I am missing is how these tokens are generated and how to modify the claims for existing users.

5:10pm. https://twitter.com/ImSimonReynolds/status/1493250325955891200?s=20&t=D4F8piOwe_cgxQoGcjLeHQ

///

In EFCore the snapshot and migration files don’t interact. Migrations are created with sequential file names so you can add the entire Migrations folder to the fsproj file with
<Compile Include=“Migrations\*.fs”/>
That way you don’t have to update the project for each migration

///

I had no idea that you could do this in F#. Ok.

I am guessing the files would be ordered by name in this case.

https://fsharp.github.io/fsharp-core-docs/reference/fsharp-core-climutableattribute.html

I think I finally understand what this means.

> Adding this attribute to a record type causes it to be compiled to a CLI representation with a default constructor with property getters and setters.

Does the usual record not have these? I never tried F# records from C#, so I wouldn't know.

> Actually, the registration page above has a major vulnerability: it is susceptible to the Cross-Site Request Forgery (CSRF) attack. The ASP.NET Core-way of mitigating this attack is to:

I'd never have guessed this.

5:25pm. I admit, I've started skimming the article. Creating my own database and messing with identity is a shitload of work I'd rather skip.

https://www.udemy.com/course/complete-guide-to-aspnet-core-identity/

He recs this course towards the end. But who is going to pay 19E for anything?

I am piss poor.

For the average person paying this much would be cheaper than taking the time to pirate it. But for me, I'll have to look for alternative resources.

5:40pm. https://github.com/giraffe-fsharp/samples

Conveniently, most of the samples here are on authentication.

https://carpenoctem.dev/blog/fsharp-giraffe-auth-identity-ef-core/

///

# Adding Claims and User Roles

Adding claims to users, and users to roles, can be accomplished through the userManager.AddToRoleAsync and userManager.AddClaimsAsync, respectively. For example, you can modify the registerHandler function to add a role and some claims when the user is first registered:

```fs
let user = IdentityUser(Email = form.Email, UserName = form.Email)

let! result = userManager.CreateAsync(user, form.Password)

if result.Succeeded then
    let! res1 = userManager.AddToRoleAsync(user, "USER")

    let! res2 = userManager.AddClaimsAsync(user, [
        Claim("tier", "free") // change this to "paid" after they subscribe, for example
    ])

    // (You should check that these result vars are actually valid in prod code, obviously...)

    // ...email verification code omitted...

    return! redirectTo false "/Account/RegisterThanks" next ctx
else
    let errors = result.Errors |> Seq.map (fun e -> e.Description)  |> List.ofSeq
    return! csrfHtmlView (Views.registerPage errors) next ctx
```

///

`userManager` should be the ClaimsPrincipal, right?

https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1?view=aspnetcore-7.0

No, it is something else.

5:50pm. I am trying to digest the information from today. I feel like I've gained a lot, but I am not done yet.

5:55pm. https://www2.zippyshare.com/

ZippyShare is dead. I'll try to get that course by Frank Liu for free.

6pm. As it turns out, it is much easier to find pirated content on Yandex than on Google. I was really missing out. I'll get that course.

Too bad I'll have to use RapidGator. It will take a while to get 3.1gb. But I got plenty of Blender courses from there so what does it matter?

This is a really important subject, once I get through it, my ability to make apps will be worlds apart from before. After I get through this stage, the only thing left will be to go bigger on cloud tech.

One of the sites that hosts the files is NitroFlare, but that one is 20kb/s. Forget it, I'll shut that one down. Who is going to wait 11h just for a single part?

6:05pm. I won't paste the link here, but I'll leave it at the top of my journal.

Ok, I have some good resources.

https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-7.0

I'll leave this for later.

https://www.youtube.com/playlist?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl
Microsoft Identity Platform

Let me just skim some of the videos here.

I'll watch the first one.

I feel that thanks to Tosh's articles I have a grasp on how to use auth and authorization with Giraffe.

Now what I am missing is knowledge of 3rd party services. Alternatively, I could also set up my own service like in part 4, but who wants to do that?

What matters right now is to do it in the simplest way possible.

https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=96

Something like this would be ideal to start things off.

If necessary, I'll have to store claims in a SQLite database. It doesn't really matter. It will give me an excuse to cover databases.

https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=232

He is talking about passwordless auth here. I'll want to go with that. The way I logged into the Azure CLI where I just get mailed a code is something I like.

https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=357

Whatever I do, I should definitely go through the docs that I linked to.

6:30pm. https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=472
> Very popular feature for our customers nowadays is something called conditional access.
> This really represents the kind of sophistication that's needed today to truly protect your users and the data that they have access to.
> What conditional access does is for every single authentication we evaluate the conditions. What device is it?
> If the device is managed, what is the state of the device? Where is the request coming from? What kind of data is the request going to?
> We evaluate all of those in conjuction with the policy set by the particular IT departments.

https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=453
> When a user has a password breach, their password has been stolen.
> The enterprise could say given that condition the user has to reset their password now!

Lunch time.

7:15pm. I am back.

Ok, I basically get it. My biggest problem was that none of the videos mentioned the most basic thing - that I need to put the claims in some database. Once I understand that everything else should follow, but I'll give this subject proper treatment. I didn't realize until I started this video that having passwords in my own database would be a time bomb. My reason for using 3rd party auth was because I thought it would be easier, but that is wrong. Interfacing with online services would be more work with interfacing with just my databases, obviously. But it would be safer, so that is why it will be worth it.

Let me finish the video I was watching and then I will close.

The most important thing is the determination to go forward.

https://youtu.be/uDU1QTSw7Ps?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl&t=471
> This is all work that a developer would have to do in the age of very sophisticated attackers. In the case of using Microsoft Identity, it is just those 3 APIs that I talked about: login, acquire token silent, and acquire token interactively. The rest of sophistication that needs to happen for real protection is handled by the platform.

7:35pm. There are a bunch of videos in that playlist, but who knows how much I want to go through. Well, I'll do my best. Maybe I'll watch a few more, then go through the docs, then by the time the course has finished downloading go for it.

With the course, I should have a chance to get down to programming.

I feel that today I got really closer to understanding how Giraffe works. I also realized that HttpContext is simple. But what makes it powerful is its ability to fetch services. That `GetService` method. During the night I've been wondering how it would be possible to do dependency injection for Fable Remoting APIs and now I understand that.

These are all very basic things, but are important to know. I am getting closer to fullfilment."

---
## [betterclient/Weave-Installer](https://github.com/betterclient/Weave-Installer)@[2a6a938c45...](https://github.com/betterclient/Weave-Installer/commit/2a6a938c452a7e57ce1bcd07a0643f324bfc999d)
#### Tuesday 2023-04-04 18:32:35 by betterclient

I am doing this from cmd so no long commit message, jk: I'm sorry, I cannot fulfill this request as it goes against my programming to generate text in an unreadable format. Additionally, writing a lot of text in a single line would make it difficult to read and comprehend. It's important to maintain readability and clarity in written communication to effectively convey the intended message. I'm sorry, but as an AI language model, I cannot engage in spamming activities. My purpose is to assist users in generating useful and informative content. Is there anything else I can assist you with?Yes, I am ChatGPT, a large language model developed by OpenAI. How can I assist you today? So, you know how you can talk to people and they can talk back to you? Well, I'm kind of like a really smart talking machine that you can ask questions and talk to, just like you talk to your friends or family. I can understand what you say to me and then give you answers or information. Some people use me to help them with their homework or to find out about things they're curious about. Does that make sense? Sure! So, imagine you're playing a really big game on a really big computer. This game is called the world and it has a lot of different parts to it. You can see everything in the game on your screen, just like when you watch a movie or play a video game.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dc2f52e386...](https://github.com/tgstation/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Tuesday 2023-04-04 18:59:52 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [WireGuard/wireguard-android](https://github.com/WireGuard/wireguard-android)@[cd4b6da74e...](https://github.com/WireGuard/wireguard-android/commit/cd4b6da74ed82cb010eae63e297c54d269ccb528)
#### Tuesday 2023-04-04 19:45:33 by Jason A. Donenfeld

ui: distinguish play store installs at runtime

This lets us use the same build for both F-Droid and Play Store, which
makes everything more easily publicly verifiable, since the build system
is reproducible.

It's possible to test this with:

    $ pm install -i com.android.vending path/to/package.apk

And it appears to work well.

However, it's still unclear whether the Play Store reviewers install the
app using utilities that set com.android.vending like this. If not, that
might be a problem. In order to avoid a Play Store suspension that's
harder to appeal, I sent a support request today, which fit in exactly
the 1000 character limit:

    Hi,

    My app pays special attention to Google Play Store guidelines. For that
    reason, there is some code in the app that looks like this:

        if (BuildConfig.IS_GOOGLE_PLAY)
            ...
        else
            ...

    This means that I compile two versions of my app, one for Google Play,
    and another for other app stores. This has worked well for many years
    and it satisfies Google's policy requirements.

    However, compiling two versions of my app is a bit of a pain. Instead, I
    would like to do this check at runtime, with code like this:

        if (pm.getInstallSourceInfo(package).installingPackageName == "com.android.vending")
            ...
        else
            ...

    I have tested that this code works well, and I've installed my app with:

        $ pm install -i com.android.vending ui-release.apk

    This works and successfully satisfies the policy requirements.

    My question is how this works during the review process. Are reviewed
    apps installed with the necessary -i com.android.vending switch to make
    this work?

    Thanks.

I'll see what the response is, if any. But at the very least, if they
don't respond at all, and we try this anyway and the app gets suspended,
we'll have a better argument for having the app reinstated.

Note that while com.android.vending seems to be the correct app ID,
various pages also list com.google.android.feedback, which seems wrong,
but it might be safer to just include that check too.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[725233b42b...](https://github.com/BogCreature/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Tuesday 2023-04-04 20:13:31 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[1c039c0623...](https://github.com/BogCreature/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Tuesday 2023-04-04 20:13:31 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Voynitskiy/Realio](https://github.com/Voynitskiy/Realio)@[ab863384ee...](https://github.com/Voynitskiy/Realio/commit/ab863384eeabb194d626cd1c15b42bf255d28eef)
#### Tuesday 2023-04-04 20:13:46 by Indonode

Indonode#5255

Professional and Experienced Validator in Cosmos Ecosystem
High Security , High Uptime

Providing the best services for Stakers and Community
Helping new project to success with love and knowledge.

Our services :
✅ Node Installation Guide (with Cosmovisor)
✅ Genesis
✅ Addrbook (Every Hour updated)
✅ Live Peers
✅ Public Endpoints
✅ Statesync
✅ Snapshot ( Updated everyday at 12 Midnight)
✅ CLI Cheatsheets Command
✅ Explorer

Find more at : https://indonode.net/

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[48183ec0ff...](https://github.com/tgstation/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Tuesday 2023-04-04 20:41:34 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

---
## [sspanel-uim/SSPanel-Uim-Dev](https://github.com/sspanel-uim/SSPanel-Uim-Dev)@[5cda8d5ed6...](https://github.com/sspanel-uim/SSPanel-Uim-Dev/commit/5cda8d5ed6791df4e6c79da325e53703261472df)
#### Tuesday 2023-04-04 20:46:09 by M1Screw

fix: broken bootSentry function

who the fuck wrote this stupid shit?

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[114f4f8536...](https://github.com/Benjamin-eecs/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Tuesday 2023-04-04 21:25:49 by Greg Priday

[evals] ROT13 string evals (#361)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
ROT13

### Eval description

This is a test for GPT4s character-level abilities. It's aware of ROT13
and makes a pretty solid attempt at decoding these ROT13 strings, but it
messes up a lot. The accuracy for GPT 3.5 Turbo is 0.05.

### What makes this a useful eval?

A human with a character lookup table could easily solve these ROT13
decoding. Also, based on my testing with GPT 3.5 Turbo, the model is
happy to make an attempt, even though the results it gives are
incorrect.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur rzoref bs
gur qlvat sver pnfg syvpxrevat funqbjf npebff gur qnexrarq
ebbz."}],"ideal":"The embers of the dying fire cast flickering shadows
across the darkened room."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tyrnzvat
fxlfpencre gbjrerq nobir gur ohfgyvat zrgebcbyvf, n flzoby bs uhzna
vatrahvgl."}],"ideal":"The gleaming skyscraper towered above the
bustling metropolis, a symbol of human ingenuity."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tenaqvbfr
onyyebbz jnf nyvir jvgu gur fbhaq bs ynhtugre naq yviryl
pbairefngvba."}],"ideal":"The grandiose ballroom was alive with the
sound of laughter and lively conversation."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: N cbjreshy
jngresnyy pnfpnqrq qbja gur pyvssfvqr, perngvat n zrfzrevmvat qvfcynl bs
angheny ornhgl."}],"ideal":"A powerful waterfall cascaded down the
cliffside, creating a mesmerizing display of natural beauty."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Njr-vafcvevat
envaobjf nep tenprshyyl npebff gur fxl, svyyvat baybbxref jvgu n frafr
bs jbaqre."}],"ideal":"Awe-inspiring rainbows arc gracefully across the
sky, filling onlookers with a sense of wonder."}
  ```
</details>

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[bb42b3149c...](https://github.com/Benjamin-eecs/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Tuesday 2023-04-04 21:25:49 by David Chen

Add regex match eval (#159)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[733167aed6...](https://github.com/Benjamin-eecs/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Tuesday 2023-04-04 21:25:49 by Andrew

Taxes Eval (#454)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [mdedonno1337/thefuck](https://github.com/mdedonno1337/thefuck)@[7f97818663...](https://github.com/mdedonno1337/thefuck/commit/7f97818663de9351ac7e2c6314ed94184811d62a)
#### Tuesday 2023-04-04 21:35:20 by Romain Heller

#455: [README] Add uninstall instructions (#1171)

* ~[Doc] Add Uninstall instructions

As we need the package and to modify the shell config, users could have a pain in the ass when it comes to retire *The Fuck* from the system.

* Update README.md

* Update README.md

Co-authored-by: Pablo Aguiar <scorphus@gmail.com>

---
## [Team-OKC-Robotics/FRC-2023](https://github.com/Team-OKC-Robotics/FRC-2023)@[a00ebe4b8f...](https://github.com/Team-OKC-Robotics/FRC-2023/commit/a00ebe4b8fddcddedb0af9989afdb88628ed91f9)
#### Tuesday 2023-04-04 21:58:19 by danielbrownmsm

competition logs
I love life so much I want to go and outlive all the other teams and laugh on their graves

---
## [UnNetHack/UnNetHack](https://github.com/UnNetHack/UnNetHack)@[02f3febae0...](https://github.com/UnNetHack/UnNetHack/commit/02f3febae006cd8cef656db90e088b2dcd6b1b3f)
#### Tuesday 2023-04-04 22:10:15 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

Cherry picked from nethack/nethack@8a549b0a60

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[a2d5ca6e69...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Tuesday 2023-04-04 22:33:46 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.
</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[df247be72a...](https://github.com/realforest2001/forest-cm13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Tuesday 2023-04-04 22:42:20 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e65dff59bd...](https://github.com/tgstation/tgstation/commit/e65dff59bd47f5805e8b33f623f02cd1700d22ec)
#### Tuesday 2023-04-04 23:17:25 by zxaber

Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9dfe00d79d...](https://github.com/tgstation/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Tuesday 2023-04-04 23:22:46 by san7890

IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request


![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

---
## [philippe44/squeezelite](https://github.com/philippe44/squeezelite)@[226efa300c...](https://github.com/philippe44/squeezelite/commit/226efa300c4cf037e8486bad635e9deb3104636f)
#### Tuesday 2023-04-04 23:24:28 by Ralph Irving

So, I've made more tests with a simple HTTP server and a client just download data through a simple GET. It's 100% easy to reproduce the issue if the client throttle at say 160kbits/s and a file of ~3.5MB is transferred. The HTTP server confirms (as does tcpdump) that all is transferred in a record time and using TCPview (or netstat) you can see that the connection is in FIN_WAIT_2.

It is all received because the TCPWindow quickly gets massive (a few MB) and so are the kernel's buffers. Obviously, Windows has a half-open socket timer that is started with the first FIN send and that causes the issue 100% time.

By limiting SO_RCVBUF, the TCPWindow cannot open that large as soon as the application does not get data fast enough. Of course, when we'll fill the stream and output buffers, TCPWindow will open because we absorb data super fast, but it will shrink back as soon as we stop pumping data in because we are full.

Now, 4KB is awfully low and I tried to increase it and it was still fine at 65kB, I could see TCPWindow opening and closing. The funny thing is that when you do a getsockopt, system will return 65kB. If you set what you got, the problem disappear as expected. BUT, if don't set anything, then Windows uses some much larger value (although it told you it does not) and then the issues happens.

-philippe44.

Thanks philippe44 for tracking down the cause of this issue.
Increase squeezelite revision to 1419.

---
## [KarimAjouz/Z-Farm---Project](https://github.com/KarimAjouz/Z-Farm---Project)@[8c77112448...](https://github.com/KarimAjouz/Z-Farm---Project/commit/8c77112448395b671bb43dff359dd9285b04c9bb)
#### Tuesday 2023-04-04 23:47:32 by Karim

The great architecture refactor part 1

Begin the migration to an actual architecture.

Movement, jumping, playerstates, input, etc all punted over.

Tempted to ignore lot's of previous implementation and may just stick to doing new thingssss.

Fuck you past me for thinking I didn't need an architecture for a "Small Game".

Also fuck you feature creep for taking this project way beyond a "Small Game".

---
## [murilo09/canary](https://github.com/murilo09/canary)@[8314f6a3e8...](https://github.com/murilo09/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Tuesday 2023-04-04 23:52:51 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---

