## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-22](docs/good-messages/2022/2022-04-22.md)


1,765,756 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,765,756 were push events containing 2,813,092 commit messages that amount to 207,346,080 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [VanyaBaou/v5](https://github.com/VanyaBaou/v5)@[5de9d663cc...](https://github.com/VanyaBaou/v5/commit/5de9d663cc324674ffb644fc9a7af97e542117ab)
#### Friday 2022-04-22 00:11:24 by VanyaBaou

Update pickletweaks-common.toml

Disabled:
Watering Can (Thermal adds one)
Magnet (already disabled)
Night Vision Goggles (a bauble version exists already)
Tool Breaker (kinda personal preference, saw someone else complain, personally its hella annoying)

---
## [atteria/Paradise](https://github.com/atteria/Paradise)@[6082c95eb3...](https://github.com/atteria/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Friday 2022-04-22 00:33:42 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [leoxia007/kernel_xiaomi_odin](https://github.com/leoxia007/kernel_xiaomi_odin)@[8cefae8c40...](https://github.com/leoxia007/kernel_xiaomi_odin/commit/8cefae8c40df9edbc103b13a43e49b41d2090a05)
#### Friday 2022-04-22 00:43:54 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [SabreML/Skyrat-tg](https://github.com/SabreML/Skyrat-tg)@[c2a88900c6...](https://github.com/SabreML/Skyrat-tg/commit/c2a88900c67fe6db78c3e17631270c05be14d9af)
#### Friday 2022-04-22 01:01:38 by SkyratBot

[MIRROR] Updates The Derelict to some modern standards, also some turf edits [MDB IGNORE] (#12859)

* Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

* Updates The Derelict to some modern standards, also some turf edits

Co-authored-by: Jolly <70232195+Jolly-66@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[cd1b891d79...](https://github.com/timothymtorres/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Friday 2022-04-22 01:07:02 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [xSkyyy/pep.py](https://github.com/xSkyyy/pep.py)@[5a0c7d975e...](https://github.com/xSkyyy/pep.py/commit/5a0c7d975eba5ea02a852cdb470b10cbd74b4e38)
#### Friday 2022-04-22 01:36:07 by Skylar

changed the db thing because ive been suffering with nginx for 2 fucking hours trying to find a config that actually fucking works and saw it was outdated

i want to kill myself

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[d411393e72...](https://github.com/FernandoJ8/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Friday 2022-04-22 02:05:39 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[b86cf89125...](https://github.com/FernandoJ8/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Friday 2022-04-22 02:05:39 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [swf541/ColdWarIronCurtain](https://github.com/swf541/ColdWarIronCurtain)@[7d8b2e5b13...](https://github.com/swf541/ColdWarIronCurtain/commit/7d8b2e5b132a5e26262099252d3180a597be0731)
#### Friday 2022-04-22 02:40:02 by baldamundo

Six Day War + UAR focus tree fixes

This is a very complex and consequently very buggy event chain, so I've annotated it to make future troubleshooting & editing easier and I've also made a few fixes. The phrasing of some of the annotations is slightly inconsistent, but that's phrasing copied and pasted from the comments in the localisation file.

The main changes are:
- the war will start a week after Egypt closes the Straits of Tiran via its focus tree - as it did historically - instead of always occurring on the same date.
- Egypt/UAR's focuses are now unlocked by the war (The Six-Day War when the war begins, Partial Liberation of Palestine when the UAR wins, an Naksah when it ends either in stalemate or Israeli victory) - previously there seemed to be no way of unlocking them at all
- the Golan Heights and West Bank sections of the conflict should now still occur if Egypt/UAR has annexed the territory of Syria and/or Jordan
- switched Syria's victory national focus to be attached with event .35 and edited event .5 so that it doesn't fire for Syria - the event was kind of redundant for Syria anyway, and having the two border conflicts share the event caused issues if one country owned both territories
- SIX_DAYS_WAR.3 is fixed to use the correctprovinces, so that border conflict can actually occur
-  SIX_DAYS_WAR.14 uses the description from SIX_DAYS_WAR.8.d, but it says you are being given a choice, even though SIX_DAYS_WAR.14 doesn't offer a choice, so the text of desc = SIX_DAYS_WAR.3.d fits better.

Known unresolved issues:
- SIX_DAYS_WAR.192 - Israeli Perspective Counter-Attack into Sinai - appears to have no trigger
- the news events are still a bit of a mess and i've not tried to fix them - some countries don't get properly notified when the war has ended (the original event chain is primarily written for Israel) or get notifications that are clearly written from the perspective of a different country
- if Jordan owns Syria's territory, or vice versa, it won't fire both border conflicts
- if an Arab power other than UAE (e.g. Iraq as the Arab Federation or a unified Arab League) owns Jordan's or Syria's territory, their border conflicts won't fire
- if Israel declines to attack, Egypt/UAE attacks alone only on the Sinai front - when historically the other Arab powers likely would have joined in
- UAR's focus description for UAR_an_Naksah describes the war as a crushing defeat, but the focus still applies even if the war is a stalemate
- UAR's focus UAR_The_Six_Days_War describes the war as an Israeli surprise attack, but it's possible for the war to play out as an Egyptian/UAE surprise attack instead.

And tbh there's probably still a lot of unresolved bugs I've missed still. I've tested it a lot of times, with different combinations of countries involved, and different paths, but it's a very complex chain and there are a lot of different possible combinations, so I've not tested exhaustively. And I'm not an experienced modder, so I'm sure things have slipped through the cracks, but it seems significantly less buggy now than before. There is probably an argument for rewriting the entire war, getting rid of all the complex chains of Border Conflicts, and just having it as a regular war with scripted peace deals, but that's above my pay grade - I was just trying to make what already exists functional.

---
## [LSD-RP/qb-core](https://github.com/LSD-RP/qb-core)@[9d83a952c2...](https://github.com/LSD-RP/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Friday 2022-04-22 04:01:32 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[95d7f599e7...](https://github.com/treckstar/yolo-octo-hipster/commit/95d7f599e7d0fcf53bda06595e66889da341e587)
#### Friday 2022-04-22 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [inferno964/platform_android_kernel_xiaomi_sdm660](https://github.com/inferno964/platform_android_kernel_xiaomi_sdm660)@[a938b43afa...](https://github.com/inferno964/platform_android_kernel_xiaomi_sdm660/commit/a938b43afab7eca662afd122b4677a76e246ba75)
#### Friday 2022-04-22 04:23:31 by Maciej Żenczykowski

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
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[dca0edc30e...](https://github.com/StarStation13/StarStation13/commit/dca0edc30e9db1424dffb582c5e8d075e0581ac0)
#### Friday 2022-04-22 05:19:22 by B4CKU

Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

---
## [sthagen/OpenImageIO-oiio](https://github.com/sthagen/OpenImageIO-oiio)@[7956ca328f...](https://github.com/sthagen/OpenImageIO-oiio/commit/7956ca328fb6ea61fe1af904ff251ddadb62231f)
#### Friday 2022-04-22 05:29:19 by Larry Gritz

Speed up case insensitive string comparisons (#3388)

Oh boy, never leave anything unbenchmarked.

Turns out the boost::algorithm functions we were relying on underneath
many Strutil "case-insensitive" comparisons were ridiculously slow.
We thought they were good enough because they allowed specification of
locale, so we could just pass the static classic locale, and so they
would be inexpensive because they didn't have to query the current
locale.  But this is wrong, they were still ghastly.

So here I rewrite Strutil::iequals, iless, starts_with, istarts_with,
ends_with, iends_with in terms of a new (internal) Strutil::strcasecmp
and strncasecmp (which underneath handle differences in platform, and
use the locale-independent versions). The net result is that most of
those case-independent comparisons speed up by a factor of
50-100x. Wow.

I still need to tackle the family of 'ifind' related functions. They
are a bit trickier. But I'll leave them for another time, because I
need to roll this present fix out right away to fix a real production
bottleneck.

(Worth noting: iequals is instrumental when you're searching a
ParamValueList for a particular name, which is what happens when you
look up attributes from an ImageSpec, which is what happens when you
call get_texture_info(), which is what underlies OSL gettextureinfo()
calls in the cases that they cannot be constant-folded during runtime
optimization. So this came to my attention when analyzing a slow scene
whose shaders had a pathological explosion of gettextureinfo calls that
couldn't be optimized away.)

---
## [LabyMod/og-names](https://github.com/LabyMod/og-names)@[05d1c1c1d2...](https://github.com/LabyMod/og-names/commit/05d1c1c1d23e8eeb417e99c5c65be2784032793e)
#### Friday 2022-04-22 05:49:10 by fez

Create abbreviations.txt (#58)

* Create abbreviations.txt

> 4AO - For adults only
> AFK - Away from keyboard
> AKA - Also known as
> ASAP - As soon as possible
> BAE - Before anyone else
> BFF - Best friend forever
> BRB - Be right back
> BTW - By the way
> BUMP - Bring up my post
> CTR - Click-through rate
> DIY - Do it yourself
> ETC - Et cetera
> FAQ - Frequently asked questions
> FYI - For your information
> G2G - Got to go
> HMU - Hit me up
> IDC - I don't care
> IDK - I don't know
> ILY - I love you
> IMO - In my opinion
> J4F - Just for fun
> KISS - Keep it simple stupid
> LMAO - Laughing my ass off
> LMFAO - Laughing my f***ing ass off
> LMK - Let me know
> MSG - Message
> NSFW - Not safe for work
> NVM - Nevermind
> OMW - On my way
> PPL - People
> POV - Point of view
> QNA - Questions and answeres
> ROFL - Rolling on floor laughing
> RUOK - Are you okay
> SOS - Save our ship
> SMS - Short message service
> STFU - Shut the f**k up
> TBH - To be honest
> TTYL - Talk to you later
> UUID - Universally unique identifier
> VIP - Very important person
> WTF - What the f**k
> XMAS - Christmas
> Y2K - The year 2000
> ZZZ - Sleeping noise

* Added "idfc"

Added:
› IDFC - I don't f\*\*\*ing care

* Fix: GTG

Fixed:
› GTG - Got to go | Changed from "G2G".

---
## [Kafva/spicetify-cli](https://github.com/Kafva/spicetify-cli)@[0a89573c1c...](https://github.com/Kafva/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Friday 2022-04-22 06:17:07 by Łukasz Ordon

fix: `New Releases` custom app for Spotify 1.1.81+ (#1563)

* Fix `New Releases` custom app for Spotify 1.1.81+

- Based on proposed fix for `Shuffle+` (#1559)
- Fixes #1539 #1530 

Notes:
- Can probably be written nicer - this is my scuffed attempt to fix it
- May or may not actually show all new releases for all followed artists - have over 665 of them but I don't think I'm getting all of them (see below)
- May or may not return `error 500` (added `.catch()` block keeps it from breaking whole custom app)

* Minimize `internal server error: 500`...

...for big libraries of followed artists.

Changes:
- Change `URL` to query only discographies
- Limit amount of queried albums to 5

Notes:
- This does **NOT** fixes erroring fully - it only maxes out amount of data you can query before getting rate limited
- The more options you select (ex. albums + EPs + podcasts), the less data you may receive
- To max number of albums received, I recommend to select only `Albums` (since `Singles and EPs` will probably get displayed anyway...)

* Add notifications when error occurred

Notifications added:
- Error code (`500`, `429` etc.)
- Amount of followed artists to fetch releases from
- Amount of followed artists failed to fetch releases from

I guess we have to get along with getting `500-ed` - one time it fetches everything instantly, second time it drops 60 artists...

* "Prettify" file to pass `Prettier` test

* Fix filtering, counter...

- Fixing filtering as no matter was what set in config, it always displayed everything as "Album"
- Fixing "Missing releases from..." counter - should properly reset now

What broke again:
- "Appears on" releases cannot be retrieved with that API endpoint - this filter is just there and doesn't do anything - this prevents from showing everything as "Appears on" etc.

Notes:
- There seem to be an API endpoint for retrieving "Related content" stuff - problem is that would query everything TWICE... which breaks everything even more (and we don't wanna do that)
- If someone knows how to query everything using separate endpoint without doing it 4 times, let me know...

* Forgor `( )`... Oops... :skull:

I forgor 💀

* Include requested changes

Changes:
- Properly encode URI including variables
- Make `limit` variable customizable via settings (set default to 5)
- Make error messages as "dev console only"

Notes:
- Errors displayed in console may be a little spammy - if we get error early, there may be lots of lines displaying it + counter...
   * I'm not too sure how to tackle this - just remove them altogether? Or is there a function that could "suppress" them?
   * Switching from normal `log` to `debug` may help a little as they will be only visible if user has set their console log level to include `Verbose`
- Making `limit` customizable may lead to even more errors but fuck it I guess - it's better to have a choice than not, right?
   * It can be manually input via custom app settings (same place where other options are) - there is no list etc. - it's just normal input field
- Set `offset` value as const `0` and not making it customizable (cause why would you want to start searching from ex. 3rd album instead of beginning, right?)
- Leaving `Fetching releases from...` notification cause it looks cool - it's fun to know how many followed artists you have 😆

---
## [ian-mcconnell/Studio-I---Office-Chair-Studios](https://github.com/ian-mcconnell/Studio-I---Office-Chair-Studios)@[a15847c448...](https://github.com/ian-mcconnell/Studio-I---Office-Chair-Studios/commit/a15847c448a20ac7fbe0daca5c75341b2e1db8b6)
#### Friday 2022-04-22 08:00:05 by Bubblyssa

read description

-New settings menu pieces (if i need to scale stuff tell me)
-New NPC's- trans pride girl, pride flag girl, chubby asian kid who loves food, nerdy chubby kid
-Updated Basement wall pieces (extra messed up walls, green blobs and red blood claw marks for extra customization)
-Extra main floor pieces (called them rotunda pieces for some reason but o well)...pillars may look tacky and we can remove...library is an easter egg if you understand the reference

---
## [y2kbadbug/freebsd-ports-y2kbadbug](https://github.com/y2kbadbug/freebsd-ports-y2kbadbug)@[e250aeb4a1...](https://github.com/y2kbadbug/freebsd-ports-y2kbadbug/commit/e250aeb4a1399664907d0df0605a3577ba671609)
#### Friday 2022-04-22 08:03:32 by Tobias C. Berner

KDE: Update KDE Gear to 22.04

Thursday, 21 April 2022

Welcome to KDE Gear ⚙️ 22.04!

Skip to What’s New

KDE Gear ⚙️ 22.04 brings you all the updates added to a long list of KDE
apps over the last four months. KDE programs allow you to work, create
and play without having to submit yourself to extortionate licenses and
intrusive advertising, or surrender your privacy to unscrupulous
corporations.

Below you will discover a selection of the changes added in the last
four months to software designed to make your life better. But remember,
there is much, much more: games, social media apps, utilities for
communicating, developing and creating stuff… All these things have been
worked on to give you more stability and boost your productivity.

If you want to see a full list of everything we have done, check out the
complete changelog.

WARNING: There’s a lot!

All the details can be found here:
	https://kde.org/announcements/gear/22.04.0/

---
## [ItsProf-org/my_whatever_kernel](https://github.com/ItsProf-org/my_whatever_kernel)@[b05303d76e...](https://github.com/ItsProf-org/my_whatever_kernel/commit/b05303d76eff0b49589c1a57bce47941dd4a12f0)
#### Friday 2022-04-22 08:36:11 by Peter Zijlstra

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
Signed-off-by: Vaisakh Murali <mvaisakh@statixos.com>
Signed-off-by: ImLonely13 <gabutuhaku@gmail.com>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[4d54e290db...](https://github.com/silicons/Citadel-Station-13-RP/commit/4d54e290db51697d12fc54a6bbb0a376f43b7280)
#### Friday 2022-04-22 10:04:01 by Zandario

Security TGUI (#3886)

* e

* Fuck it, I'm pushing it.

* Fuck you

* Refactored Brigdoors, updated their UI, does annoucements

Also updated logging a little bit and documented some things.

* Multitool sync

---
## [yeshria/Website_Submission_2178751](https://github.com/yeshria/Website_Submission_2178751)@[7ae0806ddb...](https://github.com/yeshria/Website_Submission_2178751/commit/7ae0806ddb7b74f781e02ced3c2db02525dbdfc9)
#### Friday 2022-04-22 10:49:41 by Yeshria

another another push

fuck you andre i want to kill myself

---
## [ArtificialRangerRex/IS12-Warfare](https://github.com/ArtificialRangerRex/IS12-Warfare)@[1867654758...](https://github.com/ArtificialRangerRex/IS12-Warfare/commit/186765475881bf58bbee319880653287d578820b)
#### Friday 2022-04-22 12:01:57 by Matt

Should fix the issue of loading the wrong CSS by making them all the same fuck you

---
## [jukibom/FlyDangerous](https://github.com/jukibom/FlyDangerous)@[ce7a1246c3...](https://github.com/jukibom/FlyDangerous/commit/ce7a1246c3145e0dc16a49c02058cc66e335d144)
#### Friday 2022-04-22 13:10:27 by Jay Faulkner

fix: remove shit fades based on animation system and implement properly

honestly unity's animation system is fucking horrible, my god

---
## [Giraffey27/Friendly-bot](https://github.com/Giraffey27/Friendly-bot)@[3ade46456b...](https://github.com/Giraffey27/Friendly-bot/commit/3ade46456bb1ec116a63f2531f435af6613c8d28)
#### Friday 2022-04-22 13:50:14 by Giraffey_27

Friendly bot V2 (update 1.0)

Just making it easier to see the answer to your jokes, I'm still trying to find a way to make it so that whatever joke you get, you get that exact answer, but for now (and probably forever) there will not be the exact answer to your joke. Please recommend any things that I should add to it in the comments.

---
## [nicerapp/nicerapp](https://github.com/nicerapp/nicerapp)@[63009ab0ba...](https://github.com/nicerapp/nicerapp/commit/63009ab0bae438d29605f869e08f54271d40f319)
#### Friday 2022-04-22 13:57:36 by Rene AJM Veerman

added some vital, and therefore for the foreseeable future, only, political-country-alliance-set origin marketing material image pictures to my github repository as sign of thanks to the performances that WERE useful by the armies of NATO, of which i am STILL a soldier at General 5-star and General 4-star level (see my https://facebook.com/gavanHoverswell account). the pictures give you clear hints why i support my home country and NATO's right to remain a superpower, even after that whole and very awful war on terror 2 decades worth of regular Muslim deaths happening far before the old age, which i suspect to be among the most primary life goals of all humans world-wide.

---
## [SuperHarmony910/SuperHarmony910](https://github.com/SuperHarmony910/SuperHarmony910)@[cee88db09f...](https://github.com/SuperHarmony910/SuperHarmony910/commit/cee88db09f924ab05e1097330d7c1c20a5b57759)
#### Friday 2022-04-22 14:33:47 by SuperHarmony910

yk what fuck the random babel website shit this is what we're going with now

---
## [nightshadetvn/Qwarzu-botto](https://github.com/nightshadetvn/Qwarzu-botto)@[2072f305b9...](https://github.com/nightshadetvn/Qwarzu-botto/commit/2072f305b9b3a9fc87f77d8c035d3ffccbf1eaf2)
#### Friday 2022-04-22 14:45:15 by DeltaWither

Added a fucking mess. Oh god, I'll just go to sleep and magically sort it out tomorrow

---
## [ettoreleandrotognoli/rathena](https://github.com/ettoreleandrotognoli/rathena)@[d617d9f083...](https://github.com/ettoreleandrotognoli/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Friday 2022-04-22 15:50:19 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [dsas/gutenberg](https://github.com/dsas/gutenberg)@[3ea2d42b0a...](https://github.com/dsas/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Friday 2022-04-22 15:54:45 by Dennis Snell

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
## [knowler/knowlerkno.ws](https://github.com/knowler/knowlerkno.ws)@[5e8fd6174f...](https://github.com/knowler/knowlerkno.ws/commit/5e8fd6174fd9acc1f49ee9abf851fdd5fa7c79a8)
#### Friday 2022-04-22 17:38:48 by Nathan Knowler

Improve invalid form submission response + UI

We populate the form with the invalid data so that the user doesn’t need
to fill it out again. If the honeypot was triggered, we leave the form
empty as a “fuck you.”

---
## [sailfishos-mirror/openconnect](https://github.com/sailfishos-mirror/openconnect)@[b982b2e41e...](https://github.com/sailfishos-mirror/openconnect/commit/b982b2e41ec9e711f086b62951dabfb6509057ae)
#### Friday 2022-04-22 18:14:35 by David Woodhouse

Silence static-analyser warning about redundant assignment to 'sep'

I did this for a reason. The *compiler* is clever enough not to bother
actually doing the assignment (not that it would matter anyway, since it
is hardly a fast path). But *developers*, including myself, are much less
likely to spot that it needs to be added in the 'deflate' case if we add
a new case at the end. So now in order to shut the tools up, I have to
turn a non-bug into a latent *actual* bug.

I suppose I could leave it there with a comment, or refactor it into a
loop over tuples of the form { COMPR_LZ4, "oc-lz4" }…  but it probably
doesn't matter as we're unlikely to be adding more. Just suck it up.

Signed-off-by: David Woodhouse <dwmw2@infradead.org>

---
## [DespairFactor/raviole](https://github.com/DespairFactor/raviole)@[8d8429f40a...](https://github.com/DespairFactor/raviole/commit/8d8429f40a0321d6c02d0151dd693bd505e55ca5)
#### Friday 2022-04-22 18:31:35 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [MetaMask/controllers](https://github.com/MetaMask/controllers)@[1d56fd5312...](https://github.com/MetaMask/controllers/commit/1d56fd53128ce0a1509f38cc0252931db7fbf5b9)
#### Friday 2022-04-22 18:34:36 by Elliot Winkler

WIP: Use Polly to mock HTTP requests in tests

**tl;dr:** I've introduced [Polly][1] as a replacement for Nock as I
believe it will lead to more readable and authentic tests. A few things:

* This is a proof of concept – I've only added it to
  CollectiblesController to start out with.
* All I've done is replace Nock requests with Polly requests. Ideally,
  we wouldn't need to mock anything manually at all and let Polly do its
  thing. Unfortunately, some HTTP requests that we are mocking no longer
  work, so we have to keep mocking for now. That can be refactored in a
  future commit.
* In the future, we should investigate using Ganache instead of hitting
  mainnet and exposing our Infura project ID in tests.

---

Currently there are a couple of problems with our tests as it relates to
network requests:

1. We do not prevent network requests from being made. There are
   some tests which use Nock to mock requests, but not all requests are
   being mocked, and we are unaware which ones are actually going
   through.
2. Nock, although a popular package, is rather cumbersome to use, and
   makes tests difficult to understand and follow.

To address these problems, this commit replaces Nock with Polly. Polly
is a package developed by Netflix that intercepts all HTTP requests and
automatically captures snapshots (recordings) of these requests as they
are being made. These recordings are then used in successive test runs.
You can also manually mock requests if you want more manual control.

There are a few problems with Nock that make it difficult to work with:

1. Mocks take up space in your test, so you will probably find yourself
   extending a collection of mocks you've assembled at the top of the
   file. Once you have enough, who knows which mocks serve which tests?
2. Once you've added a mock to your test, that mock stays forever. If
   the API changes in the future, or stops working altogether, you will
   never know until you remove that mock.
3. If you turn `nock.disableNetConnect()` on, and you haven't mocked a
   request, [it will throw a NetConnectNotAllowedError][2]. This works
   in most cases, but what happens if you have a `try`/`catch` block
   around the request you're making and you are swallowing the error?
   Then your test may fail for no apparent reason. And how do you know
   which request you need to mock? Nock has a way to peek behind the
   curtain and log the requests that are being made by running
   `DEBUG=nock.* yarn jest ...`, but this output is seriously difficult
   to read:

   ```
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io query matching skipped
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io matching https://api.opensea.io:443/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193 to GET
   https://api.opensea.io:443/api/v1/asset_contract/0x2aEa4Add166EBf38b63d09a75dE1a7b94Aa24163: false
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io attempting match {"protocol":"https:","slashes":true,"auth":null,"host":"api.opensea.io:443","port":443,"hostname":"api.opensea.io","hash":null,"search":null,"query":null,"pathname":"/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","path":"/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","href":"https://api.opensea.io/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","method":"GET","headers":{"accept":["*/*"],"user-agent":["node-fetch/1.0 (+https://github.com/bitinn/node-fetch)"],"accept-encoding":["gzip,deflate"],"connection":["close"]},"proto":"https"}, body = ""
   ```

Polly removes all of these problems:

1. Because Polly records request snapshots, you don't usually have to
   worry about mocking requests manually. These recordings are kept in
   files which are categorized by the tests which made the requests.
2. Because Polly actually hits the API you're mocking, you can work with
   real data. You can instruct Polly to expire these recordings after a
   designated timeframe to guarantee that your code doesn't break if
   the API ceases to work in the way you expect.
3. Polly will also print a message when a request is made that it
   doesn't recognize without needing to run an extra command:

    ```
    Errored ➞ POST https://mainnet.infura.io/v3/ad3a368836ff4596becc3be8e2f137ac PollyError: [Polly] [adapter:node-http] Recording for the following request is not found and `recordIfMissing` is `false`.
        {
          "url": "https://mainnet.infura.io/v3/ad3a368836ff4596becc3be8e2f137ac",
          "method": "POST",
          "headers": {
            "content-type": "application/json",
            "connection": "keep-alive",
            "host": "mainnet.infura.io",
            "user-agent": "Mozilla/5.0 (Darwin x64) node.js/12.22.6 v8/7.8.279.23-node.56",
            "content-length": "201"
          },
          "body": "{\"jsonrpc\":\"2.0\",\"id\":30,\"method\":\"eth_call\",\"params\":[{\"to\":\"0x18E8E76aeB9E2d9FA2A2b88DD9CF3C8ED45c3660\",\"data\":\"0x0e89341c0000000000000000000000000000000000000000000000000000000000000024\"},\"latest\"]}",
          "recordingName": "CollectiblesController/updateCollectibleFavoriteStatus/should keep the favorite status as false after updating metadata",
          "id": "53192eab94ddedfb300b625b1cb79843",
    ...
    ```

It's true that Nock contains a feature to capture requests called [Nock
Back][3]. However, this is cumbersome, too:

1. You have to wrap your test in a `nockBack` call.
2. You have to name your recording files.
3. You have to call `nockDone()` in your test.

There is a package called `jest-nock-back` that fixes these issues and
makes using Nock Back very easy. However, it isn't maintained (last
release was 3 years ago) and is likely incompatible with the newest
version of Jest.

Some requests make irreversible changes to resources, such as
transferring a token from one account to another.

To handle these types of requests, Polly still lets you manually mock
requests just like Nock. We've configured Polly to not record a request
it doesn't recognize by default, so in this case you'll get a message
when running the test that makes such a request. From there you can make
a decision about how you'd like to mock this request — whether you want
Polly to record the request or whether you'd like to manually mock it.

That said, if the request in question involves a blockchain network,
instead of mocking the request, we might investigate whether it's
possible to use Ganache to perform the irreversible action rather than
actually hitting mainnet or some other network.

* Because Polly automatically creates request mocks and these mocks are
  no longer contained in tests, developers will need to be educated
  about Polly (Polly is not as popular as Nock) and remember that it
  exists whenever updating tests.
* If a recording is no longer needed or needs to be updated, the
  associated file holding the recorded information about the request
  needs to be deleted. Finding this file is not a great experience.
* Nock has virtually zero initialization code. Polly's initialization
  code is surprisingly complicated (although that is largely hidden, so
  no one should have to mess with it).

[1]: https://netflix.github.io/pollyjs/#/README
[2]: https://github.com/nock/nock#enabledisable-real-http-requests
[3]: https://github.com/nock/nock#nock-back

---
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[bdd08a1eeb...](https://github.com/Den-Xero/Journeyman_Game/commit/bdd08a1eebc3353d9879a6aa2f0bfed345dd0e45)
#### Friday 2022-04-22 19:32:50 by McConnell2111

Working Item spin and shows item just not remove yet and ai still triggers it

I want to die, this entire time i was missing 1 line 1 FKING LINE and that caused me so much pain. anyway ive watched taskmaster today series 8 pretty good, played some fortnite, league and a little r6 fun day over all. before i explode from this shitty game im going to do something else otherwise i might give myself a heart attack :)

---
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[0077421526...](https://github.com/Den-Xero/Journeyman_Game/commit/0077421526be1a70564f4dfd2a5b4d7d27f525bc)
#### Friday 2022-04-22 19:32:50 by McConnell2111

Added Extras, Mainmenu options portal spin (its cool)

So today as i told you watched moon knight since then watched some esports done some work (ofc) TSM look like they are back after the last major which they did win tbf but they were dog in NA league for a while. mmmhm what else...... might watch a film.... dunno what yet tho. oooooooo actually might watch that other ep of halo and play some games. anyway thats me done ranting about random crap enjoy the rest of your day :)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f54fa83190...](https://github.com/mrakgr/The-Spiral-Language/commit/f54fa83190e36ca4134aadd6420f592a63e8fb65)
#### Friday 2022-04-22 19:38:01 by Marko Grdinić

"
9:25am. I am up. I went to bed at 1am as is usual yesterday and today my plan is to do art. I wasn't so fatigue from stress that I had to go to sleep at 9pm. If I get any follow ups from Strong Compute, the way to handle it is to just send it into archive and not reply anything. That would get me an A. Short replies would get me C. Long replies and emotional involvement are a fail.

Scam or not, I can't let other people use my obligation towards Spiral as a way of manipulating me. If they just wanted to hire me, they could have gone with open-the-wallet approach. Sure, I would have ignored such offers, but it is not like them throwing enough money at me would not move me. These manipulative plays are really something else.

9:40am. No emails, good. Let me chill just for a bit and then I will start. The current goal is to watch Arrimus' playlist from start to finish and then go through the docs. Before I can do anything on my own, I'll want to find out how subdiv works in this program.

10:35am. Let me start. I've wasted enough time to satisfy me.

This is the way to go. I should take the recent experience to heart and appreciate how good it is to just be able to focus on cultivating one particular skill at a a time.

If something happens that forces me to pursue money then fine, I'll focus on clearing the interviews and get a job. No more of this nonsense.

If I get a sponsorship offer in the future, I'll start things off by querying the other party's intent directly instead of letting them control the flow. I'll be more properly skeptical rather than nursing doubts and lightly probing.

10:40am. My heart is just so weak.

https://youtu.be/BiaRcr8b_Hk?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Safety Step #2 | MoI3D

Let me resume from here.

10:50am. I really like Moi 3d. It feels like a much more suitable modeling tool than Blender for me. Blender forces me to think about topology in places I shouldn't need to.

Focus me. Let me get through a bunch of these vids. I want to master Moi before the month is over.

https://youtu.be/9IjKxEI6TY8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=231

Cutting into curved surfaces like this would be very hard in Blender. For that reason you will see the Blender Bros mostly cutting into flat ngons.

https://youtu.be/9IjKxEI6TY8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=602

It is a bit too close to the heole. I keep watching this and am thinking that my ability to tell proportions is better than this guy's.

Though he might simply be in a hurry due to making a video.

https://youtu.be/0b3ihcF8K8Y?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=9
> For an object like this, details like this are easier to deal with NURBS. THat is the recommended solution for an object such as this.

https://youtu.be/0b3ihcF8K8Y?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=118

I expected him to extrude and start cutting things out instead of putting a circle here.

https://youtu.be/0b3ihcF8K8Y?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=341

So far apart from the initial shape, he has not been approaching this like I thought he would at all.

11:35am. I got an idea. For the kind of bevel that I wanted to do yesterday it should be possible with loft. Let me give it a try.

Yeah, I got it! Loft in loose mode is exactly the tool for the job.

This is great. Let me go into Houdini and I will try out spline fillet. I do not think it will work, but it just might.

Wow, it sure takes long to load.

https://vimeo.com/179247730
Tutorial: Point Beveling

No it does not have spline fillet anymore. And I think the purpose of that node is different anyway. Rather let me watch the above Houdini tutorial. I think it does what I want. I do not need to do this, but I want to generalize my understanding as much as possible.

It works only if you make it a polygon. Nevermind.

Well, I might as well watch it all the way to the end.

12pm. That was fun for a bit. Let me go back to Arrimus.

https://youtu.be/0b3ihcF8K8Y?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=1093

Note: There is a loop selection script here.

I should put it in when I am doing the shortcuts.

12:20pm. I really like loft quite a lot. it has a lot of possibility. The modeling in Moi is very straightforward. It is quite a treasure.

Let me just put one hotkey in. I'll remap redo from Ctrl + Y to Ctrl + Shift + Z.

12:30pm. https://youtu.be/gM_jriAZ3ro?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=4
Blade #1 | MoI 3D

Put in the redo and loop shortcuts. Let me watch this.

https://youtu.be/gM_jriAZ3ro?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=262

He kept clicking the make corner instead of using Ctrl. And now he is fixing the sharp corners by hand instead of using fillet.

https://youtu.be/gM_jriAZ3ro?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=352

Oh, wow. This capability of Moi is great. I was wondering what tan/tan meant and it turns out it is a way to putting down lines tangeont to two objects.

https://youtu.be/gM_jriAZ3ro?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=718

It seems there are a bunch of commands that really should be in, but aren't.

https://youtu.be/gM_jriAZ3ro?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=806

Ah, I get it. He is having this trouble because he is using sweep. Had he done this using loft, there would be have been less issue getting the middle line to align to the surface.

Hmmm, no I don't think aligning this should be a problem even with sweep...I am on the wrong track with this.

1:05pm. https://youtu.be/jZ8fQpDow60?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=350

This is a nice way of filleting. I am starting to get eager to give it a try myself. I want get started on going through the docs today.

2:05pm. Done with breakfast and chores. Let me catch up with Tog and then I will get back into the fray.

2:20pm. Siu is really great at keeping up the tension despite the series being so long. There is never a dull moment in Tog. I really like Traumerei for calling Bam a human, and saying it is wrong to treat him as an animal. When I start writing Simulacrum again, the Inspired will in general have that kind of view assuming they don't go Fang Yuan level rational.

Let me move on. Downloads really are fast these days. To think that it would get 500mb in 1:15m. I'll leave the the ep of Estab Life for after I am done for the day. I'll have it and the last 4 eps of Magia Record waiting for me. There are all sorts of shows I'll be interested in the upcoming season as well.

2:25pm. Let me start.

https://youtu.be/jZ8fQpDow60?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=528

Why does he not use freeform all the way?

https://youtu.be/8OJC3ZOllDY?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe

He had some good advice to set the hotkeys to be the same between different programs. I really did not want to bother with that when moving from Blender to Houdini though.

https://youtu.be/8OJC3ZOllDY?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Pro Tip : Read the Manual

Yep, I'll do that after I finish the playlist.

https://youtu.be/8OJC3ZOllDY?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=200

Alt disables snapping. Interesting.

https://youtu.be/8OJC3ZOllDY?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=232

Use Ctrl Shift to force selection. Another bit of advice to keep in mind.

https://youtu.be/OYszsvAP5D8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
[Important Technique] Avoiding Fillet Problems Using Rebuild

Let me watch this. So far I am 1/3rd through the playlist already.

https://youtu.be/OYszsvAP5D8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=356

Ahhh, so that is why he was rebuilding the corners manually.

https://youtu.be/OYszsvAP5D8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=374
> List of commands without UI button.

I guess the merge I saw them typing is not the same as boolean merge. And while join might join lines, it still leaves vertices intact. I had to find that out the hard way yesterday.

But merge did not work for me though.

https://youtu.be/VOLWep6z2uY?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
CAD For Artists! - Plasticity is On the Rise (Invest Now!)

This video has interesting comments.

3:40pm. https://youtu.be/fLE7QlULuLo?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
CS:GO Skins #3 - NURBS

Focus me. Let me watch a few more and then I will start going through the manual. I don't really have the patience to just sit here for days watching stuff. I want to try out some of my own projects. I've had a lot of inspiration so far.

https://youtu.be/fLE7QlULuLo?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=598

What is he doing to get that middle line after the fillet?

Ah, I see. He is getting shearing.

4:25pm. There were some good replies in the question I posted.

///

Hopscutter stuff is easier to unwrap, better control of normals, manifold so it can bake to itself better in painter etc.

I gave CAD a go and fusion 360 was a joy to use but yeah you'll never get directly usable data out of it for anything other than a keyshot render, you certainly can't author a mid poly asset

---

CAD is definitely usable for creating game assets/other stuff once you get to know the workflow
https://www.artstation.com/artwork/mqv1QE

///

The stuff in the link looks really great looks really great. I'll check out RizomUV at some point.

4:40pm. https://youtu.be/yF2h7M26FQ4?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=38
Create Decals in MoI

Let me go for this one and a few more that look interesting and then I'll transition to reading the manual. I want to know what all the tools do and here I just see him using the basic ones.

https://youtu.be/TABhL4b07kM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Types of CG Artists

Let me watch this.

https://youtu.be/TABhL4b07kM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=20
> For example, you might have noticed that some artists care a lot about topology and having good topology and quads, other artists do not really care that much.

I am in the later camp. Blender is really forcing me to care about topology so for that reason I am looking beyond it. Being serious with your own projects really has a way of crystalizing what is really important.

https://youtu.be/TABhL4b07kM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=104
> However more and more, concept artists have also started to use 3d applications and incorporate them into their workflow. So for example if you want to create an environment you can create some basic 3d shapes. You don't even have to be a good or an experienced 3d modeler, you can simply start by putting in some blocks and cylinders, and basic shapes and they can help you setup your perspective and things like that. They can use various programs to generate large environments, mountains to make it easier to paint over that. They can use CAD programs or polygonal programs to sketch some mechanical objects and paint over that as well. So more and more concept artists are incorporating 3d into their 2d, but you can still work a lot faster with 2d than you can with 3d.

> To craete a 3d character in an environment can take days or weeks, but you can draw it in an hour if you are really good.

I'll have to take this as caution. Maybe I'll ultimately converge to such a style, but before that I'll master 3d.

5:15pm. https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Freeform Cuts in MoI

Let me watch this next.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=36

It is possible to just select a single thing in object snap and go back to all again. This is really useful.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=105

Booleans with curves do not work unless it is flat. This is also something I've been wondering about.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=332

What I tried earlier that worked with loft is to instead of just lofting two, to loft 3 edges. That is a good way of making washouts.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=423

These are good tips. I need to keep that I can just flatten the curve in mind to make it applicable in booleans.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=523

I hand't realized you can hold control while scaling.

https://youtu.be/lmiCOGKZ7q0?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=626

I hadn't known that booleaning a curve directly on the surface results in a single object.

https://youtu.be/jYRV_YxiCG8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
NURBS Retopology Tips #1

https://youtu.be/cPwOe8Das6s?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Non-Destructive Workflow Using Merge in MoI

Let me go for these two and then I will take a break.

https://youtu.be/cPwOe8Das6s?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=155

Ah, so this is how you name an object.

https://youtu.be/g9e216qyCEg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Weapon Grip in MoI

I can't find any vids on subdiv modeling in Moi. Let me watch this as I am interested in how he does those handle grips.

After that I'll focus on the manual. I'll want to check out the art station walkthrough after that.

https://youtu.be/jYRV_YxiCG8?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
NURBS Retopology Tips #1

Ah, right I also haven't finished this one. I've just been playing with inset.

https://youtu.be/g9e216qyCEg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=555

I think I get what he will do. He will make the path along the silhouette and array a bunch of circles which he will boolean in the next step.

https://youtu.be/g9e216qyCEg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=636

By hand? Lame.

https://youtu.be/g9e216qyCEg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=731

The way he moved with gradual deselection was not bad. Yeah, there is nothing wrong with what he did. I thought he might have gone for something fancier.

7pm. Lunch time.

7:20pm. Let me resume. I had 3m left in that last video.

https://youtu.be/IW08b0vgcdg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Fast and Fun Product Design with NURBS and Polygons

Ah, let me watch this as well.

https://youtu.be/IW08b0vgcdg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=144

So you can't actually do subd in Moi?

https://youtu.be/IW08b0vgcdg?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=468

This is a pretty interesting result.

Now I am interested in how he did that brush.

7:40pm. https://www.blenderbros.com/products/hard-surface-modeling-jumpstart

Let me watch the brush vid and then I'll go for some of the free course by Ponte.

Ponte Ryuurui has a chad face and even has a masculine voide, but check out his bio.

> Ponte Ryuurui (Ryuu) is a Tokyo based multi-genre artist, author and educator. His current focus is on 3D hard surface concept art and creating 3D courses for Blender. Ryuu is also a professional portrait photographer and a certified Master of Japanese calligraphy with All Japan Calligraphy and Literature Association, as well as an author of several books on the subject of Japanese writing systems.

Is a popular hard surface modeling Youtuber. I can't tell if he's a weeb or not.

https://youtu.be/QCZ2CNMnRT8
Request - Brush

Ok, let me just watch it and then I'll watch the Blender thing.

...No it is a 3ds Max tutorial. I could easily replicate something like this in Blender though.

8:05pm. Watched some of the free Blender Bros course. I get it basically.

https://www.youtube.com/watch?v=RL_mgs_jwHM
Car Modeling SEAMLESS (principle) in MoI 3D (Moment of Inspiration) and Subdiv Tools

He seems to be using some kind of special plugin called Subdiv Tools.

8:15pm. https://youtu.be/u75skb32GTo?t=2148
ZBrush Masters: Hard Surface Modeling - Marco Plouffe - ZBrush 2020

If I start watching this I'll never get anywhere. It is time to close for the day.

I didn't get what was happening in the subdiv vid. It seems he had the shapes already in place and just put a bunch of loop cuts across.

8:20pm. https://youtu.be/RL_mgs_jwHM?t=159

Is the curvature all in place here? I can't really tell.

https://youtu.be/lcM7wBlvA4c
The Game Has Changed - The New Polygon Paradigm

Let me watch this. I think that I was wrong in my initial assumption. He did a car using the regular tools and then just did something to convert it to a subd model. He did not actually use the subd workflow in Moi.

8:30pm. https://youtu.be/lcM7wBlvA4c?t=232

This video is going to be a plug for the quad remesher, but I am still curious what he intends to do with it. Just remesh after a boolean? If so, that would be an interesting workflow. I want to see how it would work.

While I was doing sculpting last year, I tried pirating the quad remesher, but was not successful. Right now I bet I could just get it off Persia.

https://youtu.be/lcM7wBlvA4c?t=384
> This is what I'd like to call the new polygon paradigm. This should be the new standard of doing things with polygons here. In fact I think this is so good that Autodesk should just get the license to this quad remesher and include it with 3ds Max by default with every single copy here. Because this really allows you design and model so much faster and it pretty much frees up your imagination. Instead of having to spend an hour retopologizing this, it's just a few seconds and we get this really amazing result here.

I admit, I've never thought of adopting a workflow like this.

8:55pm. https://youtu.be/fS8e0x03p_s?t=725
[Blender] Modeling Realistic Sci-Fi Helmet w/ Rachel Frick | Part 1: Beginning Modeling

I am just skimming this.

https://boards.4channel.org/3/thread/892783/id-like-to-study-more-hard-surface-modeling-my

There is a ton of good resources here.

https://www.artstation.com/blogs/timbergholz/0dz7/revolver-tutorial-whats-in-it-and-why-blenders-remesher-workflow-is-amazing

Remesher workflow in Blender directly, not using the quad, but the regular remesher?

9:25pm. I am doing a bit of a read through the docs. All this is not that big of deal. I should be done with the tutorials and the docs tomorrow. I'll also watch the revolver tutorial as it caught my attention.

I am going to get hack to the monitor and this time do it to perfection. Though admittedly it is already pretty good, but it is not enough to be good, I also want it to be easy.

I am going to attain that and get to 3/5 of in regular modeling. I've already been doing this for close to 7 months, so another couple of months should be enough to get me to a decent level.

It really has been to long. I need to go from training to producing. When I reach that level it will be quite a day. I won't ask for a programmer's salary. I'll just want enough to support myself and create better art. I want to work towards that.

If I got a real offer, not the fake bait like in the past week, then I'd switch to my old path. But AI chips are not quite here yet. So I must not lose sight of myself.

This madness of learning will one day pass.

To be able to endure all of this learning for so long, my will is not bad at all. One day may I get rewarded.

9:35pm. Let me close here, that ep of Estab Life is waiting for me."

---
## [jknight42/poker-trainer](https://github.com/jknight42/poker-trainer)@[0aee175306...](https://github.com/jknight42/poker-trainer/commit/0aee1753065d922023bd802dc7f81b49c9ac04f9)
#### Friday 2022-04-22 20:42:16 by Jeremy Knight

Big old messy commit after re-re-jiggering a bunch of stuff. This is a mostly working commit though.
- game can be played all the way to the end.
- most of the state has been moved up to App.js which I think is the best way to do this stuff although it does put a lot of shit in App.js. Anyway, it's what we're doing so fuck it.
- some of the best hand ranking code is working now

---
## [uchuhikoshi/dmb-shodan](https://github.com/uchuhikoshi/dmb-shodan)@[89db84b237...](https://github.com/uchuhikoshi/dmb-shodan/commit/89db84b2371059630e15202e3399cfad20d307a6)
#### Friday 2022-04-22 20:53:33 by Artem uchuhikoshi L

Fixed another dumbest fucking shit god i hate myself

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[62e0729dbc...](https://github.com/JuliaLang/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Friday 2022-04-22 22:01:45 by Mirek Kratochvil

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
## [gitster/git](https://github.com/gitster/git)@[a6c0fc5339...](https://github.com/gitster/git/commit/a6c0fc533977c8d20fbc52e7be187a0efd24b23d)
#### Friday 2022-04-22 22:56:33 by Tao Klerks

merge: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local feature branch from an existing
upstream branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the remote tracking branch.

When the user pushes with "git push", they get an error, and (amongst
other things) a suggestion to run "git push origin HEAD". Eventually
they figure out to add "-u" to change the tracking branch, or they set
push.default to "current", or some tooling does one or the other of
these things for them.

When one of their coworkers works on the same branch, they don't get
any of that weirdness. They just "git checkout feature1" and
everything works exactly as they expect, with the shared remote branch
set up as remote tracking branch, and push and pull working out of the
box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

Any experienced git user will presumably say "well yeah, that's what
it means to have the remote tracking branch set to origin/master!" -
but that user didn't *ask* to have the remote master branch added as
remote tracking branch - that just happened automatically when they
branched their feature branch. They didn't necessarily even notice or
understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the feature branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make these flows painless by introducing a new branch.autosetupmerge
option called "simple", to match the same-name "push.default" option
that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [pa1nki113r/Project_Brutality](https://github.com/pa1nki113r/Project_Brutality)@[39b09db16b...](https://github.com/pa1nki113r/Project_Brutality/commit/39b09db16bbe225ec575ab2a118358732b755288)
#### Friday 2022-04-22 23:50:26 by Jason Martinez

Fixed alive baron/hell knight corpse when attack by burning attack, fixed incorrect imp corpse on baron, changed some Hell Nobles smoke effects to be more performance friendly (thanks Kamil). Fixed Demon Tech Trooper pinned bug

---

