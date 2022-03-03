## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-02](docs/good-messages/2022/2022-03-02.md)


1,570,246 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,570,246 were push events containing 2,520,001 commit messages that amount to 192,668,598 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 24 messages:


## [shelteredfreak/tgstation](https://github.com/shelteredfreak/tgstation)@[4051ad647e...](https://github.com/shelteredfreak/tgstation/commit/4051ad647e3e94ea5c722cee18cecf350270ab6f)
#### Wednesday 2022-03-02 00:18:19 by LemonInTheDark

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
## [shelteredfreak/tgstation](https://github.com/shelteredfreak/tgstation)@[3bd5a2d8df...](https://github.com/shelteredfreak/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Wednesday 2022-03-02 00:18:19 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [PixelExperience-Devices/kernel_motorola_msm8998](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998)@[480931c8b0...](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998/commit/480931c8b0febd01942851b8cf8eeb0e3551c536)
#### Wednesday 2022-03-02 01:28:48 by Maciej Żenczykowski

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
## [BerkeleyTrue/dotfiles](https://github.com/BerkeleyTrue/dotfiles)@[c34b54ba7e...](https://github.com/BerkeleyTrue/dotfiles/commit/c34b54ba7ebd18174691634d4c7d19206b9adef4)
#### Wednesday 2022-03-02 02:35:52 by Berkeley True

fix(conf/xmonad): remove dep fullscreeneventhook

Don't even bother. I'll fullscreen if I want to. Fuck you Zoom

---
## [ishitatsuyuki/LatencyFleX](https://github.com/ishitatsuyuki/LatencyFleX)@[0d9f3f7276...](https://github.com/ishitatsuyuki/LatencyFleX/commit/0d9f3f7276199930b8ceceec8f344b98d94523a0)
#### Wednesday 2022-03-02 05:17:25 by Tatsuyuki Ishi

readme: Add Apex Legends as a supported game

A huge thanks to Valve for bringing this amazing reality, EA & Respawn for their cooperation, and EAC for developing a developer friendly anti-cheat solution.

[ci skip]

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Wednesday 2022-03-02 07:09:23 by Julien Castiaux

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
## [alphagov/govuk_publishing_components](https://github.com/alphagov/govuk_publishing_components)@[6e0eb5b830...](https://github.com/alphagov/govuk_publishing_components/commit/6e0eb5b830a4d8209ffb4ecb6049c6eba7b6acdd)
#### Wednesday 2022-03-02 10:37:11 by Kevin Dew

Clobber assets before running jasmine tests

I'm adding this in because we use globbing to match what files to test.
I'm concerned that without this we're at risk of the same files being
included multiple times (say you have application-1234.js, then edit it
and end up with application-2345.js)

It's a bit of a pain to do a clobber first as it means you'll always
have to experience the cost of compiling assets each test run, however
this is preferable to tests liable to fail.

---
## [TadavomnisT/candle_search_engine](https://github.com/TadavomnisT/candle_search_engine)@[df9994f6df...](https://github.com/TadavomnisT/candle_search_engine/commit/df9994f6df6e4be70ed85f1fad1f70be2415557d)
#### Wednesday 2022-03-02 10:51:34 by behrad.b

 Updating readme, explaining crawler logic 

 Updating readme, explaining crawler logic (bloody hell:/ that "s" is a pain in the arse mates)

---
## [SuffolkLITLab/ALKiln](https://github.com/SuffolkLITLab/ALKiln)@[fe728649d3...](https://github.com/SuffolkLITLab/ALKiln/commit/fe728649d3b5a7be2d6cbf4eff90857d63a2986b)
#### Wednesday 2022-03-02 12:28:05 by plocket

Update our package's dependencies for v4 (#503)

I'm thinking this is just going to be for v4. Not bothering with this for v3 unless we absolutely have to since none of the vulnerabilities are severe. My current rationale is that the more work we do to maintain 3, the less work we can do getting v4 ready for release. Ready to hear opinions.

- Close #164, update cucumber to v7
- Prepare for v8 of cucumber because I won't remember it later
- Close #394, update puppeteer
- Update our version of node (and that of our action that we'll run for other people's libs). [Addresses #393 so we can use the suffolk npm org package.]
- Use `npm audit` to fix the remaining vulnerabilities (now 0)
- [Remove package.json as discussed in #489 to align our tests' behaviors with those of our users.]

* Update action.yml node to v17

* Update from cucumber v6 to v7. See details.

See https://github.com/cucumber/cucumber-js/blob/main/docs/migration.md#migrating-to-cucumber-js-7xx

Only use cucumber setDefaultTimeout globally and use a shim that replicates the fix in v8 that lets you do custom timeouts more easily so we can still give enough time for steps that may need more time.

Use all caps for statuses.

Test screenshot step.

Btw, the cucumber test output visually looks a bit different now - when a scenario passes, all the steps pass too.

Sorry about the little comment changes, etc. Tried to remove a lot of those incidental unrelated changes.

* Update puppeteer to latest (13). See details below.

- page.waitFor -> page.waitForTimeout and page.waitForSelector (Got deprication notice. See https://github.com/puppeteer/puppeteer/issues/6214.)
- remove removeEventListener (we'd need to change it to removeListener anyway - v4.0.0 and see https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#eventemitterremovelistenerevent-handler). For now we'll count on page close taking care of it, just in case removing it would prevent multiple-file-downloads.

* Update GitHub worflow node version, tweak changelog item order

* Fix npm audit vulnerabilities and update action.yml cucumber

* Pin the colors lib in action.yml

* Remove package-lock.json #489, use kiln v4 for users, CHANGELOG

* Fix custom timeout, remove duplicate report entry, as per review

---
## [blink1073/nbformat](https://github.com/blink1073/nbformat)@[68e399a8c0...](https://github.com/blink1073/nbformat/commit/68e399a8c0efa91dfd0e45ef38449cacf712df3c)
#### Wednesday 2022-03-02 13:48:24 by Jason Grout

Allow notebook format version 4.1 mimebundle keys ending in `+json` to have arbitrary JSON

There are a number of people posting issues with nbformat 5 being stricter about validating notebook format 4.1, including:

https://github.com/jupyter/nbformat/issues/160
https://github.com/jupyter/nbformat/issues/161
https://github.com/jupyter-widgets/ipywidgets/issues/2553
https://github.com/jupyter-widgets/ipywidgets/issues/2788


Essentially, nbformat package version 4.x allowed noncompliant format 4.1 notebooks to be verified as valid, leading to many notebooks in the wild having major/minor format version 4.1, but with widgets and other json outputs that were technically invalid.

Upgrading to nbformat package 5.x correctly flagged these notebook as noncompliant. This is correct technically. However, practically it means that all these notebooks files tagged as format 4.1 that were working fine suddenly won't even open after upgrading to nbformat version 5. This is a pain.

This retroactively upgrades the format 4.1 schema to allow json in these cases, since in practice there are lots of notebooks labeled as format 4.1, I think by official Jupyter software, that have json in the mimebundle output. Essentially, this acknowledges that in the official implementations from Jupyter, notebook format 4.1 has indeed had arbitrary JSON values in mimebundles, and we cannot in good conscience decree it invalid.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[1b9c50e2ae...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/1b9c50e2ae1e5fca135e24e11a8bdf0012f89563)
#### Wednesday 2022-03-02 14:07:12 by AmCath

My love for the whole "Spooky" portrait thing stems, I think, from a love of the old stuff KR used to do. Not to get all "SOVL KINO OLD GOOD NEW BAD," but the stuff like the old Halloween stuff, or the Christmas updates or hell even the ancient April fools thing that KR got rid of a while back was and still is super cool. It represented a different time, the old wild west days I guess. One of my fav things about working on KX is the fact that that attitude and style lives on.

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[2c66467b1a...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/2c66467b1a9b4bbfa818f79b3d69b4f761c2e072)
#### Wednesday 2022-03-02 14:45:47 by alk3pInjection

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
## [Welf06/news-in-a-minute](https://github.com/Welf06/news-in-a-minute)@[89144c954f...](https://github.com/Welf06/news-in-a-minute/commit/89144c954f13ba73b57cf3285be5e662b15be14f)
#### Wednesday 2022-03-02 15:06:21 by thennal

Move scraper to subdirectory

Fuck you python imports

---
## [AquillaF/Shiptest](https://github.com/AquillaF/Shiptest)@[031c0866ed...](https://github.com/AquillaF/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Wednesday 2022-03-02 15:23:36 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [freevpnbest/miracastwindows7](https://github.com/freevpnbest/miracastwindows7)@[e3d438f5b7...](https://github.com/freevpnbest/miracastwindows7/commit/e3d438f5b706e5b37faa3c16e8456d460f9d1bc6)
#### Wednesday 2022-03-02 15:58:13 by freevpnbest

Delete README.md

Watch anything together
Connecting your device to Miracast is easy; there are no clunky menus as Miracast dongles and devices are simply receivers for content.
Sharing your phone between friends so that they can see a short YouTube video is often not worth the hassle. Fortunately, Miracast is here to let you quickly display your mobile device’s screen on any Miracast supported system, including televisions and projectors.

Miracast is excellent if you’re a teacher as it lets you seamlessly connect your devices to a projector, giving you the ability to quickly display study tips, historical documentaries, dissection diagrams or the answers to last week’s English test. Miracast will also serve as a useful tool for you if you’re preparing to give a big presentation at your work.

To link a device look for an option in setting called screen mirroring, connect your Miracast receiver to your television or other devices (if the device doesn’t have a receiver built in), select the device you wish to stream to and enjoy the show.

Android devices with Android 4.2 and later are capable of supporting Miracast as well as most Windows devices. Many manufacturers such as Sony, LG and Panasonic have begun to implement Miracast receivers in their televisions removing the need for a dongle. Otherwise, you’ll need to buy a Miracast supported dongle to connect to any device.

Where can you run this program?
Android devices with Android 4.2 and newer as well as most Windows devices support Miracast. To mirror on screens, you may need to purchase a dongle.

Is there a better alternative?
No, while Chromecast is a viable alternative, it isn’t able to let you wirelessly stream content from your Android device or enable the sharing of material such as games, files, and other apps.

Our take
Miracast is an excellent option for anyone looking to mirror their device’s screen onto another system. Most mobile devices already have Miracast, and the need for dongles is disappearing.

Should you download it?
Yes, purchasing a Miracast dongle will give you a whole new avenue for entertainment and provide opportunities to improve your presentations.

Highs

Seamless display
Share on Wi-Fi devices
No need for HDMI ports
Lows

Requires enabled devices or a dongle
Inconsistent performance
Display capture only

---
## [Bungalow-13/Bungalow-13](https://github.com/Bungalow-13/Bungalow-13)@[ecb4422e56...](https://github.com/Bungalow-13/Bungalow-13/commit/ecb4422e566a8bb38d5d249496a6012173756ffb)
#### Wednesday 2022-03-02 16:05:51 by BlackCat-055

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
## [kdave/btrfs-devel](https://github.com/kdave/btrfs-devel)@[a50e1fcbc9...](https://github.com/kdave/btrfs-devel/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Wednesday 2022-03-02 16:54:06 by Josef Bacik

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
## [wanted2/wanted2.github.io](https://github.com/wanted2/wanted2.github.io)@[e8216e9bd3...](https://github.com/wanted2/wanted2.github.io/commit/e8216e9bd329eeb669bb2ab9eca9e97ca00a8b1f)
#### Wednesday 2022-03-02 17:04:50 by wanted2

[1;36m"Success is a terrible thing and a wonderful thing. If you can enjoy it, it's wonderful. If it starts eating away at you, and they're waiting for more from me, or what can I do to top this, then you're in trouble. Just do what you love. That's all I want to do."[1;m
		[1;35m--Gene Wilder[1;m[0m

---
## [iqraameer/Code-Mixed-Multi-label-Emotion-Classification](https://github.com/iqraameer/Code-Mixed-Multi-label-Emotion-Classification)@[140e860aee...](https://github.com/iqraameer/Code-Mixed-Multi-label-Emotion-Classification/commit/140e860aee3387a5a251aefce5f5421ee2c471f0)
#### Wednesday 2022-03-02 19:02:08 by Iqra Ameer

Add files via upload

 The corpus consists of 11,914 code-mixed (Roman Urdu and English) multi-label SMS messages manually annotated for the presence/absence of the following 12 emotions: anger, anticipation, disgust, fear, joy, love, optimism, pessimism, sadness, surprise, trust, and neutral (no emotion).

Paper to cite:

@ARTICLE{ameer2022emotion,
  author={Ameer, Iqra and Sidorov, Grigori and Gómez-Adorno, Helena and Nawab, Rao Muhammad Adeel},
  journal={IEEE Access}, 
  title={Multi-Label Emotion Classification on Code-Mixed Text: Data and Methods}, 
  year={2022},
  volume={10},
  number={},
  pages={8779-8789},
  doi={10.1109/ACCESS.2022.3143819}}

---
## [nickclason/Senior-Design](https://github.com/nickclason/Senior-Design)@[a32368f7cc...](https://github.com/nickclason/Senior-Design/commit/a32368f7cc62e3e40861457060002e4102af146d)
#### Wednesday 2022-03-02 19:18:10 by Nick Clason

Remove all previous css to start from scratch

Ben i'm sorry for deleting all your css again, but it had to be done everything was a disaster. CSS sucks and the project works but looks awful.

I probably also did some other stuff but I forgot to commit last night sooo...

---
## [thomjonson4/newby_learning](https://github.com/thomjonson4/newby_learning)@[b739eb7636...](https://github.com/thomjonson4/newby_learning/commit/b739eb7636c2bc9ad4f90ed8ad54b3607fbbb125)
#### Wednesday 2022-03-02 20:34:19 by John Lima-Thompson

Validating whether the input is a valid email... if emails dont have periods in the username FUCK YOU VASIA

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[987505219f...](https://github.com/mrakgr/The-Spiral-Language/commit/987505219fbba7c5e641675f245315a912c760ff)
#### Wednesday 2022-03-02 22:03:48 by Marko Grdinić

"8:35am. I go up this early due to a nightmare. In fact, I must have woken up an hour or two earlier and just lounged in bed. I feel very stressed right now.

It gives me such a sour feeling to drop what I've been doing because Houdini is just the tool that I want for dealing with geometry. It has so much good stuff that Blender does not. I got this reply yesterday in the Houdini thread.

///

Arnold/htoa works. If you're on python 3:

> Arnold 6.2.1.1 HtoA 5.6.3.0 - Houdini 18.5.596 Python 3 /

you can use the crack from there, but grab the installer straight from solidangle

There's a crack for v-ray as well but I haven't tested it.

Octane is a no-go. Redshift is crack is from a few years ago.

///

Should I just get Houdini 18.5 and try to make it work with Arnold?

I dropped Houdini just as I got some real skill with it. That really hurts.

> you can use the crack from there

From where exactly?

> There's a crack for v-ray as well but I haven't tested it.

8:50am. Let me bite at this.

https://www.vfxmed.com/tag/arnold/

I found this site. I never considered Arnold as a 3rd party renderer option.

https://www.vfxmed.com/2021/07/v-ray-5-houdini-18-5-596-python-3-crack-download/

I should try V-Ray 5. My intuition is telling me that this has a chance of working for 19 as well.

https://www.downloadpirate.com/sidefx-houdini-fx-18-5-696-win-x64-full-version-free-download/

If that fails, I could always download the previous version of Houdini and make it work wit that.

9:05am. V-Ray wants 19.0.455 while I have 19.0.383. Well, let me try it anyway.

And the versions for 18.5 are either behind or forward.

9:15am. Let me take a break for today. I won't push myself to start work. Today I just have to make up my mind what I want to do. I am halfway into going back to Blender, but it is really hard for me to drop Houdini.

> C:\Program Files\Side Effects Software\Houdini 19.0.455\packages

No this is a no go. It wants this Houd version specifically based on the directory. This will have to be another trial wasted. I am not going to bother trying to redirect it into 383.

9:20am. The weather is so cold today. These last few days have been full winter.

9:40am. Enough. Let me start Blender. I've had time to think, and the problem here is not getting started. The problem is not finishing the scene. The problem is just making up the resolve to just do a single thing.

I could sit here the whole day wasting time and stressing myself out. Instead why don't I load the old scene and just find a single thing to do? That is the only thing I need to think about, not the immense labor of the future.

9:40am. Let me get the 3.1 Beta actually. The 3.2 Alpha won't load the latest file.

9:55am. Wonderful. That first big sphere with the are now has proper refractions in Eevee.

This has been the first thing I did.

...And so does the pool. This has been the second thing. Do I keep the bistro table, or do I go with the same thing I did in Houdini?

It is kind of ironic that something like importing the towel post with the hooks is something I could easily do since it is just raw geometry, but the vines? Forget it.

10:20am. https://cgpersia.theproxy.ws/?s=houdini

I see there is a crack here, but this site is pure cancer and I can't get to it.

Let me try making a demonoid accound again. I made one 15 years ago, but who knows what happened to it. I haven't used it in a long time.

10:20am. Done. I see that Demonoid has a bunch of old version of Houdini.

https://www.reddit.com/r/trackers/comments/s3e3vy/cgpersia_forums_worth_it/

It seems there is a lot of stuff on CGPersia, but the registration is closed.

https://torrent-invites.org/showthread.php?tid=5200

Should I make an effort to go on IRC and get an invite. I wish I could do a search ahead of time to see if this would be worth my while.

10:35am. No forget it.

Let me do it like this. I'll redo the scene in Blender from scratch. Forget the outside assets. I'll even redo the bench.

https://rutracker.net/forum/tracker.php?nm=houdini

Now I am looking for stuff here. I see that there is a V-Ray for Houdini 18.0.499 and also a torrent for that particular Houdini version.

https://rutracker.net/forum/viewtopic.php?t=5939827

///

Houdini 17.5.173 / 17.5.229 + Redshift 2.6.41
Houdini 17.5.460 + Arnold 5.5 + V-Ray 5.0 Next
Houdini 18.0.416 + Arnold 5.2.1
Houdini 18.0.460 + V-Ray 4.3 + V-Ray 5.5 Next
Houdini 18.0.499 + V-Ray 4.3
Houdini 18.0.532 + Arnold 5.4 + V-Ray 5.0 Next
Houdini 18.0.566 + V-Ray 5.0 Next
Houdini 18.0.597 + Arnold 5.5
Houdini 18.5.351 + Arnold 5.5

///

Amazing. You really do need to look around to see what you can find.

This torrent has 7 seeds and it has Houdini bundled with the renderers. This is what I am going to get...if...

https://cgpersia.com/

I also found this site which is a non-cancerous version of what is on Google top hit. Even if I can't download from here, I should be able to do a search for Houdini renderers.

...This is more than I expected. This place actually does have links.

11:10am. Ok, it is official. Google has gone to shit. None of the links on the top can be trusted to be a decent representative of anything.

https://cgpersia.com/2021/12/v-ray-5-houdini-19-0-455-python-3-win-181818.html

If I could get this and then upgrade Houdini to 19.0.455 without the licenses breaking, that would be absolutely ideal!

If it is something like 20$ for a monthly subscription, maybe I could even afford it. I have 100$ in my wallet, and the 150E that was donated to the Spiral Open Collective.

11:10am. Ok, let me see if I can push forward here. I'll try upgrading Houdini to 19.0.455. I am not sure how though.

...Let me download the launcher. What I've done is only really add some fake licenses.

https://www.sidefx.com/download/daily-builds/?production=true&python3=true&show_launcher=true

There are a bunch of old prod builds here. They are uncompressed so that means An extra 1.3gb I need to download. But it is worth it.

https://cgpersia.com/2021/12/v-ray-5-houdini-19-0-455-python-3-win-181818.html
> Now Houdini 19.0.455 would be nice. The keygen from the 19.0.383 won´t work with the new version

Ah crap. Let me cancel the download after all.

11:25am. I am going to take a risk and verify that the old keygen does not work. Maybe the licenses will stick. I am looking at the comments for the 19.0.383 Houdini download and I see people complaining that the keys do not work. I had this same problem 1.5 months ago and it got fixed. Maybe the guy telling me it does not work with 383 is simply wrong.

Also, V-Ray is 4Gb long. It is damn enormous. But it would definitely be worth it to get it.

If I fail to get it to work, I'll have wasted some time, but so be it. I'll just go with the Russian bundle in that case. I'd have to work in 18.5 instead of 19, but I'd get everything that I need myself.

11:40am. I just love Houdini too much despite its flaws. It is very hard for me to go back to Blender. It is like going to Python after experiencing F#. I could not do it even for the sake of ML.

https://www.downloadpirate.com/sidefx-houdini-fx-18-5-499-win-x64-full-version-free-download/

Here is Houd 18.5.499.

https://cgpersia.com/2021/03/v-ray-5-00-50-for-houdini-18-5-499-win-175925.html

Here is V-Ray for it. All matching versions.

11:45am. If it was just a raw overwrite, I would not bother, but there is a chance of things working like this.

> Students currently enrolled at an educational institution qualify for academic pricing.
> Proof of status will be required in order to access the special pricing for education.

I am checking the price for V-Ray and it is 80$/month.

There is really a large difference between won't buy and can't buy. 80$ just enters the later.

11:55am. Let me have breakfast here. I did zero art this morning despite getting up at 8:30am, but whether I do it in Houdini or Blender for me holds the same significance whether I get a job or not. It is a huge fork in the road! it is hugely meaningful for Heaven's Key as well. It absoultely matters whether I spend the next few years working in Houdini or Blender.

I can't focus at all in this state. I am absolutely unsure about wanting to do it in blender.

I should focus on just resting today while this stuff downloads in the background. In fact, I forgot to switch to the fast connections so I am getting 800kb/s download speeds instead of 5mb.

12:30pm. Done with chores. Let me install 19.0.455. I'll know right away whether it passes. If it passes, the fake licenses should remain. If not, I'll try the keygen, but it is unlikely to work.

This is strange. It just installed the launcher and not Houd itself.

12:35pm. I do not get it. Is it downloading 19.0.455 now despite me having downloaded it in the ISO? What a waste of time.

Let me eat here.

1:10pm. Oh wow. I installed 19.0.455 and it passes! Houdini FX itself runs cleanly. Spectacular!

Just as a precation I dissallowed the app from accessing the net.

One thing I find shocking is how long it takes the docs to load despite it being offline. It is actually faster to just type it in the browser.

Ok, now I won't touch the license server lest it jinxes me. For now, no more updates or anything of that sort. Let me just remove 383.

1:15pm. That went smoothly. I'll leave the Labs at 383 instead of risking an upgrade. I can't neatly upgrade that to 455, just the latest build.

My gamble paid off. Now let me get V-Ray.

1:25pm. I moved to the fast connection. let me set the downloads.

Download restriction for Rapid Gator is 1 file per 120m. But there are 3 different sites. I can get them in parallel to speed things up.

1:30pm. 2m waiting times? Wow these sites are cancer. Hopefully the downloads do not start breaking. That would be tough.

Rapid gator has 100kb/s donwload restriction, Nitro is 20kb/s and Alfalife is 70kb/s. Imagine downloading a 1gb file at 20kb/s. I am glad the file is split. There is actually a risk of the file connection breaking.

1:35pm. At any rate, if things go well, I should be able to finish downloading V-Ray by the end of the day. I can't do anything else, but keep my fingers crossed the the connection does not break mid download. That happens sometimes, and it would suck if that happened after hours of downloading.

Now...let me check that the labs nodes work.

Labs Auto UV works.

I guess that is good enough.

Now what I need to do is rebuild the scene.

2pm. Let me read Demon Sword Maiden for a while. I only have a couple of chapters to catch up. If V-Ray fails for me, I'll have to rebuild the scene in 18.5 so I am not really motivated to work right now, not until I set everything up. I am going to have to investigate what is wrong with the non-commercial version. Rather than rebuild the node tree by hand, it might be worth using that script.

2:05pm. If I can't manage to download V-Ray by tomorrow, I'll spend a few dollars to get a Rapid Gator accound and get these files.

If I can get my tools set up, I'll have everything I need to last me for the next year or so. Right now my art progress has flatlined due to lack of good renderer, but there are ways of getting around that.

500$ per year would mean having to spend two weeks on salary on just software, but if I had to spend something like 250$ for just the renderer that would not be too bad. V-Ray is stupidly expensive, but Octane and Redshift are not too bad.

2:15pm. Let me go back to chilling. It is actually quite draining to have to scheme my way forward like this. If I can set up Houdini properly, I'll be a lot more reassured about my future.

Come to think of it, which versions does Redshift support? 383 was no go, but what about 455?

///

19.0.455
19.0.498
19.0.531

I am looking at the supported Houdini vers and I see that 0.36 which I downloaded from the pirate site is not on the list.

///

This is from my journal. Good thing I noted down the directories. It is too bad I wiped Redshift, but it might be worth trying out the trial in case I want to buy it in the future.

Since I upgraded Houd to 455, I should be able to do it for the latest prod build as well.

2:45pm. https://youtu.be/NoJEsRU-uq0
render engines in houdini - Vray intro

Let me finish reading Shadow and then I am watch this. AFter that I'll go over the file.

2:55pm. Let me watch Rohan's renderer intro vids. He will cover a bunch of them.

Right now the Rapid Gator is 50% done, Nitro is 10% and Alfafile is 35% done. After RapidGator finishes I'll set the last file to start. And since it will be faster to ...

Let me see if I can start a download in parallel on Rapid Gator.

...No, it says max 1 parallel download. I won't even try.

Forget it. Let me just study up on these renderers.

3:20pm. https://www.youtube.com/watch?v=JrMiSQAGOS4
Why is Ukraine the West's Fault? Featuring John Mearsheimer

I noticed this on the sidebar and it is from 6 years ago. To be honest, I have no idea why Russia is attacking Ukraine anymore why there was a war in my own country 3 decades ago, so it might be interesting to hear what it was about.

https://youtu.be/NoJEsRU-uq0?t=1290

This is a pretty good demo of how to actually use the renderer. It will definitely be something I will be referencing when setting up V-Ray. From what I can see it is decently fast. If this was Mantra I'd need to wait at least a minute for it get the same result.

Here he is giving me a good demo of what Measure Curvature SOP does.

https://youtu.be/NoJEsRU-uq0?t=1574

Couldn't they have just used a selection list instead like in Blender?

https://youtu.be/NoJEsRU-uq0?t=1666

How to put materials on instances is actually relevant to my interests. I have a bunch of BW tiles and I want to use the CD attribute to lightly control the intensity.

It is not the same thing to me which renderer I am trying to learn. If I learn the V-Ray nodes, I'd have some trouble adjusting to a different engine.

https://youtu.be/NoJEsRU-uq0?t=1762

Being able to color attributes like this is one of the reasons why I want Houdini's power.

3:50pm. Let me cancel Nitro, it is just wasting my time. By the looks of things, this might really get downloaded at this rate.

https://youtu.be/NoJEsRU-uq0?t=1794

Oh, what he was demonstrating was all CPU rendering. I'd never have guessed.

https://youtu.be/UeRiA7SIFm8
render engines in houdini - vray volume shader

Let me watch this as well. i do not feel like doing anything to specific until I have the setup done.

https://youtu.be/UeRiA7SIFm8?t=64

I'll keep the Axiom solver in mind. Rohan says it is a lot better than Pyro.

4:25pm. Wonderful. Part 1 has finished DLing.

Let me set part 3.

https://cgpersia.com/2021/12/v-ray-5-houdini-19-0-455-python-3-win-181818.html

Let me paste the URL here again. I have a bunch of them and it is getting hard to find.

4:30pm. https://youtu.be/eFXTmcbgsBc
render engines in houdini - arnold intro

If the V-Ray download fails me for whatever reason Arnold will be my second choice, so let me watch this. He said he would do fire with V-Ray, but it does not seem like he got around to it.

https://youtu.be/eFXTmcbgsBc?t=128

Arnold does not support packed primitives. What trash.

Instead it does some quirky thing with instance objects.

> Can you tell, what is the difference between CPU and GPU rendering in Arnold, is there any limitations for  GPU-mode? because for example V-ray GPU can'd render tesselation. I just wonder why so many people are using CPU Arnold instead of GPU?

> Arnold GPU supports about 80 or 90 percent features of the CPU version. There are still stability issues with Arnold gpu. If you make changes too fast the ipr gets stuck sometimes. I haven’t done a speed comparison as yet, so I can’t say which one is faster. I will make a video on the gpu version so I’ll be able to give a better answer.
The bottom line is, it’s still in development.

It also has GPU problems apparently.

What is tesselation? Ok, I know what is is now, but I do not understand why it cannot render it. Forget that.

5:15pm. Done with lunch. Let me resume the video.

7:10pm. So far the downloading has been very smooth, no breaks whatsoever. The 3rd file is at 90%. 2-3 hours more and V-Ray will finish.

8:10pm. I am starting to feel hopeful. I had to spend an entire day doing nothing, but my heart is settled now. I should be able to sleep better tonight. I am going to go with Houdini.

Houdini + Mantra < Blender, but with V-Ray that equation will change.

You can't chose many things in life, but at the very least I am glad to be able to chose what I work on. I got demoralized yesterday, but it turns out I just had to put in more effort.

For the past few hours, I've just been listening to John Mearsheimer instead of reading novels or manga or games. I been working, but I haven't been in leasure. It feels like I am some beast waiting to pounce. That is my mindset.

Until the final file finishes downloading I won't be able to rest.

I'll leave actually installing V-Ray for tomorrow. I am think it is very likely that it is going to work and that I am going to get my pro renderer.

After that I'll spend some time rebuilding the scene.

In fact, I should rebuild it in Apprentice...

Can I even run Apprentice or did...

Maybe I should not have removed 19.0.383. Right now I only have the FX version and I should test whether I can open .hipnc files.

...Ah, it is fine. It is no trouble.

The pirate version for some reason installed Core/Apprentice/FX side by side for some reason.

The upgraded one is just FX.

8:15pm. Yeah, I'll first rebuild the scene in the .hipnc file. I need to figure out what those errors are, but I am expecting that the assets will be missing. After I patch that up, I'll use that script and rebuild the file as a .hip file. Actually, the only reason I am doing that is because I am suspecting that the 3rd party renders won't work.

But maybe they will. The restrictions might only apply to the app version, not to the file I am using. I can easily check that out.

Why did I assume the worst? If I can render properly with .hipnc, who cares if it is commercial or not. I won't touch it again after I am done.

Well, that is what I initially assumed, and then I saw people using scripts to convert .hipnc to .hip files so I assumed that the assumption was right.

If I can't render then I should fix the asset errors in the .hipnc file, and then convert to .hip programatically after that. It makes zero sense to do it by hand. It would take a lot of effort I do not want to put in.

After that I'll be ready to resume from I left before. I'll check out the V-Ray docs and move from there. Since I know about CGPersia and Rutracker I'll get some V-Ray tuts from there. No problem.

8:25pm. I'll get my shit into shape and push the scene towards completion. That is the mastery challenge I need to pass to get to the next level.

It might not be pure art, but having the capability to put the tools together despite being on a shoestring is one of the obstacles to being an artist.

My relationship with Houdini right now is very similar to my relationship with F# and functional programming in late 2015. I came from an imperative background, and functional programming was new and interesting at that time. 6 months later I could not bear to go back.

I won't blast Blender since it is really good at what it does, but Blender is like Python while I want real programming. And actually comparing Blender to Python is unfair because Python is bloated and cumbersome, and Blender is anything but that. But it is still not functional programming. Even if Python was fixed to be performant, it would still be an imperative mess.

Functional first is the way to go.

I compared Houdini to Haskell, but Houdini is much like F# in its philosophy. It is eminently practical, despite garnering academic interest.

8:30pm. Let me watch Kenja no Deshi and I'll take a bath. I meant to take it tomrrow, but today is the ideal time since I am just wasting it.

9:35pm. It hasn't finished yet, only 100mb left to go. Let me watch some shading tuts.

https://youtu.be/z9DTGy6Xrfk
BEST HOUDINI RENDERING ENGINE - Shading Workflow Equivalence

https://youtu.be/z9DTGy6Xrfk?t=24

Damn, this looks good.

https://youtu.be/z9DTGy6Xrfk?t=101

Oh, it is possible to use Renderman for free for non-commercial projects.

https://youtu.be/BPk0hKzzR8Y
This is the BEST Render Engine in 2022! Arnold vs V-Ray vs Redshift

https://youtu.be/BPk0hKzzR8Y?t=97

He says that Redshift wins in speed by a mile.

> V-Ray is not that far behind Redshift, but Arnold is much slower.

Speed is really important to me, so I'd probably go with Redshift if I had to buy a license. Too bad I wasted my trial.

https://youtu.be/BPk0hKzzR8Y?t=368

> With V-Ray you get Chaos Cosmos which is a V-Ray specific asset library with 100s of high quality models, materials, HDRI skies ready to be added to your V-Ray scenes.

He mentions that Redshift devs are slacking due to it being the fastest.

https://youtu.be/gXDRMpsjuIs
How to improve your Cinema4D Workflow in 2022 - Octane vs. Redshift vs. Cycles4D

10pm. Only 7mb left.

10:15pm. It finished. Let me unpack it.

Oh, 3.45gb in the file are just the material library!

I want to say I could have done without it, but no, this is actually quite beneficial for me in the stage I am at!

I really have no assets I can use.

I am in the mood. Let me install it in full.

As with any properly pirated software, it comes with instruction what to do. For example here I need to do the advanced install and say no to the local license server.

10:25pm. I was smart and selected not to download the material library. Given my experience with the Houdini ISO, I am starting to anticipate the installers being retarded and trying to download from the net despite the data being right there on the hard drive. Instead I just unpacked it by hand.

I cracked the thing, now the only thing that remains is to try running it.

10:30pm. It works. I succeeded!

There is an exe installer of 400mb, right next to a zip file of 360mb.

Let's see, V-Ray is 4,239mb in total when unpacked. The asset library is 3,459mb and the useless zip file is 368mb. Trim the fat and you get 412mb. I guess just the program parts of V-Ray are not too extreme.

Ok, good.

Right now, I got everything installed. I am not going to try rendering right now because I still have to figure that out, but I have zero reason to think I will fail.

The program is not going to suddenly start acting up. Things are straightforward from here.

Great!

I have my tooling set up. I can resume cultivating my 3d skills. I still have a day left to go before I can catch up to where I was a few days ago, but I'll be able go through that quickly enough. After that I will be able to finish the scene.

https://youtu.be/z9DTGy6Xrfk?t=375
BEST HOUDINI RENDERING ENGINE - Shading Workflow Equivalence

I really don't feel like watching this, so I've been putting it off. I'll leave it at this for later. I'll close the day here.

This is a good way to end the day. I might not have produced anything, but I've started the day off depressed, and now I am back in action. I really want to see how far I can go with Houdini. 1.5 months of functional programming was not enough to become an expert at it. But months and years brough about changes.

My next hurdle is leveling up these skills and making money. After that it is back to AI and chasing the Singularity. I'll am going to get those AI chips and find a way to fuse my art skills into a single whole with my programming ones. The way Houdini works makes makes them greatly related so I am in a good spot.

But I can't really say that art is programming. The need to plan is the same, but dealing with geometry and rendering is not something I've ever had to do in programming. Also, art does not stress my functional programming chops much. Maybe with AI that will change. The future should be belong to programmers."

---
## [snaker938/dijkstras-game](https://github.com/snaker938/dijkstras-game)@[876860ef5c...](https://github.com/snaker938/dijkstras-game/commit/876860ef5ca03e8ef0c883092ec505d0c2cc2740)
#### Wednesday 2022-03-02 23:06:47 by snaker938

Biggest update yet - the UI update

This has been the biggest update so far.

I have implemented a working home screen.

I removed most of the previous code in the home screen. Things I have added:

- I have added the background image, which moves back and forth gradually. There were a few issues getting this to work. The first issue was actually making the image move left and right in the first place. The first thing I did was use margin-left AND margin-right for my two from and to values- this did not work. I had to use margin-left AND margin-left for my two from and to values. I also made the margin-left 'to' value larger than the "from" value. This is because there was more room on the left hand side to move away from, because the end node was in the top right corner, and I did not want it to come out of view.

-  I added a way for the user to input a username by typing, the goal is to eventually have a slight story to the campaign, and the username the player enters will both be saved to local storage, so the user can resume progress, and also appear in the cutscenes.

- I added a semi-3d title text which displays the name of the game. It uses one of the custom fonts I added a while back and has a big shadow, which gives the 3d effect.

I had to remember to add the "user-select" = none tag to the css, to stop the mouse curser acting like it was actual text. I had to do this for all <p> tags.

- I added a bottom divider that houses the 4 current buttons in the home screen: campaign, sandbox, credits and settings. The divider is made out of pure css, because it  meant it was much easier for me to modify it according to the size and margins of the buttons it would contain.

I also added a semi working campaign menu, which is currently work in progress. Some of the things I hope to add and have been added are listed below:

- The same main menu background is used once again, moving from right to left.

- All of the 15 level buttons get rendered in the level container- made out of pure css, such as the bottom divider mentioned above. The level container is made out of two parts, a rectangle, and a trapezium, which sits on top. The rectangle has a blur affect, which blurs the background behind it. I would do the same to the trapezium, but the blur affect blurs the background of the whole element, not just the trapezium- which can be noticed (see picture for what I mean). To make up for this, the opacity has been lowered a bit more. I was contemplating whether I should render these containers as images, or using css. I chose css because it was easier to get the dimensions the way I want them- and easier to modify their attributes, such as adding that blur affect.

- Added the text "Select Stage" above the level buttons, so the user knows what to do.

- The first level button is also selected first, the user can then click another level button and it's level info is displayed on the right (more on that later). There are separate affects if the user hovers over a level button, clicks a level button, and the level button that has been clicked is different to the other level buttons.

- The user can then click the "Start Game" button, which enters the level the user has clicked

Next to the level buttons, is the level info. Info about the level that is currently clicked is displayed. It is currently work in progress, and it does not yet display all the info about the levels:

- The container is made the same way as the level button containers- facing the same problem with the blur affect for the trapezium. It is wider, but has the same height.

- The level name is rendered. This text will eventually be placed at the top of the screenshot of the level thumbnail, which has not been implemented yet. There was a slight complication of this text appearing behind of the level info container. This was because of the layering in the html, which could not be changed easily, due to it having a unique position in the container. As a result, I had to change z index of the text, which alters the stacking of the elements. This pushed the text to the top of the layers, so it could be displayed on top of the container. Surprisingly, this was the only element that I had to do this for.

- The description of the level is displayed in a nice background. The background is a bit lighter than the backgrounds of the other level info text

- The number of random wall presses (powerups) is also displayed, but this is work in progress, as although it works, I also need to render a tag with it, to show that this number actually is. I also have the decision of whether to render "none" if there are no powerups for this level, or not to render anything at all.

Other things that will be added here:

- A thumbnail of the starting board. This will mainly help fill up the space, and the level name will be placed at the top of this thumbnail. It will have a trapezium top border, which will allow it to slot nicely in the level info container itself, having a small margin between the two.

- The difficulty (easy, medium hard). This is already implemented in the level data manager.

- Lives + addition of lives in the actual game

- Levels that have not yet been unlocked, because the user has not beaten the previous levels, will say "locked" and cannot be accessed. This will need the addition of a winning/losing feature of the game, which isnt really there yet.

After the campaign info for each level is rendered correctly, I am going to finally design the layout of the actual game board itself. I am currently thinking the top buttons (play, unanimate, random walls) will be placed inside a divider at the top, sort of like where the buttons are placed in the home screen.

---
## [rswarbrick/ibex](https://github.com/rswarbrick/ibex)@[aa014d38c9...](https://github.com/rswarbrick/ibex/commit/aa014d38c9556decb2c43985e958444bbb2d5df9)
#### Wednesday 2022-03-02 23:59:11 by Rupert Swarbrick

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

