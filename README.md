## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-07](docs/good-messages/2023/2023-03-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,351,151 were push events containing 3,562,353 commit messages that amount to 287,734,219 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 55 messages:


## [Cockatrice/Cockatrice](https://github.com/Cockatrice/Cockatrice)@[55a2f75d16...](https://github.com/Cockatrice/Cockatrice/commit/55a2f75d16511bad70e4689c9ac85af86ec797b2)
#### Tuesday 2023-03-07 00:41:11 by Basile Clement

Make cards rounded (#4765)

* Make cards rounded

Magic cards have rounded corners, and playing cards tend to have rounded
corners as well, but Cockatrice currently displays rectangular cards.

This can cause visual glitches when using image scans where the border
does not extend in the corner, and for this reason Cockatrice always
draws a (rectangular) border around the card to try and make it look a
bit better.

In this patch I take a different approach: rather than try to make
rounded pegs, er, cards, go into a square hole, the hole is now rounded.
More precisely, the AbstractCardItem now has a rounded rectangular shape
(with a corner of 5% of the width of the card, identical to that of
modern M:TG physical cards).

As a side effect, the card drawing gets a bit simplified by getting rid
of transformPainter() when drawing the card outline and using the
QPainter::drawPixmap overloads that takes a target QRectF instead.  This
means we no longer have to bother about card rotation when painting
since that's taken care of by the Graphics View framework (which
transformPainter() undoes).

* format

* Also give PileZone rounded corners

* Forgot untap status + bits of CardDragItem

* fix deckviewcard calculations

* Rounded CardInfoPicture

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/silicons/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Tuesday 2023-03-07 00:50:01 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[3978cfe70f...](https://github.com/carlarctg/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Tuesday 2023-03-07 01:12:02 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

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

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [memfault/memfault-docs](https://github.com/memfault/memfault-docs)@[57fd44b7f2...](https://github.com/memfault/memfault-docs/commit/57fd44b7f2bd7f018f26109102e66db2bcfd22f5)
#### Tuesday 2023-03-07 01:19:39 by Noah Pendleton

Add PAT to prettier action (#415)

Use a Personal Access Token instead of the built-in
`secrets.GITHUB_TOKEN`. This is very annoying, but pushes from the
`secrets.GITHUB_TOKEN` _do not_ trigger a workflow run:

https://github.com/orgs/community/discussions/25702#discussioncomment-3248819

I assume some weird way to avoid eternally-looping workflows?

Which results in PR's never getting the updated status if the prettier
action pushes a commit, and the PR never satifies the merge requirement.

Anyway, using a PAT works around the problem 🤷 . Update the action
version too since I'm in here.

You can see it in "action" (😅) here:

https://github.com/memfault/memfault-docs/pull/414

NB: I never noticed this because I am obsessive about squash-rebase if
prettier detects any changes.

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[6f1b1717a7...](https://github.com/insertnamehere123/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Tuesday 2023-03-07 01:21:33 by TotalEpicness

Boiler rework Part 1: Globber base boiler (#965)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request


A total redesign of the base boiler reminiscent of the old premoba
boiler that would shoot projectile "Globs" with a modern CM take.

Base boiler as it is right now, is completely unfun, to play against and
to even play as. You'd be hard-pressed to find someone who enjoys
playing it past the first 10 minutes of doing so. It is this way not
because it's weak, but because it's unchallenging and 100% "safe"
gameplay. There are no combos, cool moves you can do, or even satisfying
effects, you just hit a button to spawn a telegraph which becomes a gas
cloud.

This PR, turns that right ontop of its head. Instead of "safe" gameplay,
globber's design philosophy is centered around being challenging, fun
and even adding new gameplay dynamics.

Globber will have higher HP, faster walkspeed, and faster firing bombard
compared to premoba.

However, globber will have their fellow xenos making plays to cover for
boiler, either directly through bodyblocking shots or making plays to
distract marines due to a minimal zoom range.

These both, in theory, will create a new gameplay dynamic where boilers
will still be able to block marine spearheads, but Globber needs to help
make a small counter push with their fellow brethren in order for
Globber to directly strike at marines and giving the Xenos the choice to
either capitalize on their advantage or heal up upon a successful glob.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

### Details:
Globber will feature [TENTATIVE] higher HP and [TENTATIVE] faster walk
speed. It however will be slightly more vulnerable to fire as fire deals
[TENTATIVE]% more damage to it!


https://cdn.discordapp.com/attachments/458150341742166017/1013647188313776148/2022-08-28_17-10-53.mov

Globber Active 1 - Bombard: Spit a large acid glob that will, upon
impact, immediately spread a gas glob of your choice

- Cooldown: 30 seconds
- cost: 200 plasma
- Windup: 5 seconds

Globber Active 2 - Acid spray, instantly sprays a line of acid, May make
it a cone spray if it is too weak

- 8 second c/d
- No windup
- 40 plasma
- 6 tile range

Globber Active 3 - Shift spits: Switch between acid and neuro gas globs.
Acid deals more raw damage while neuro slows,blinds and eventually
knocks down marines. Neuro has a larger radius than acid

Globber Active 4 - Acid shroud: A quick windup action that dumps an acid
cloud over the boiler. Cooldowns other abilities similar to dump acid.

Globber Active 5 - Zoom: Short ranged zoom with short windup. Trades
awareness for zoom

Globber Passive: Brute armor, Globber features brute armor, however, it
does not protect against flames! Globber takes 1.5x damage to fire!

Acid glob: Pretty much the same as before. May adjust numbers.

Neuro smoke rework:
- Instead of insta blindness and deafness, these will now have a chance
of applying for every tick you are in the smoke. You still have
blurry/weldervision though
- Oxyloss toned down, it was 9 per tick, now two
- Knockdown chance lowered to 5% per tick. Stamina damage replaces RNG
knockdowns
+ Now deals stamina damage, and am making it stack fast, targeted
knockdown time is 2-3 seconds
+ Minor immediate slowdown applied. May remove as it stacks with stamina
damage slow
+ chance of dealing minor tox damage

### Boiler rework as a whole

The boiler rework is a total rework of the boiler strain and it's
strains.

I'm not gonna write the entire design doc here, but in short:

-Base boiler will be reworked (as shown here), named Globber
- trapper will be totally scrapped for 'Grenadier', a heavy siege strain
that lobs devastating nades that's counterable and challenging.
Grenadier will have the same zoom as Globber
- A long-range, general-purpose strain will be added, named "Striker
Boiler", which combines both the Railgun boiler and the mostly forgotten
"Acid Splatter" strains in the past, with a modern CM twist.

design docs( old as fuck and needs updating) _**REPLACE ME WITH NEW
ONE**_
https://github.com/cmss13-devs/cmss13-design-docs/pull/7
Striker design doc
https://github.com/cmss13-devs/cmss13-design-docs/pull/8


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
TL;DR base boiler is a literal NPC strain that no one likes to play as
or against. Attempt to make it more fun or die trying

if the design philosophy fails, then we can simply just tweak a few
values and have premoba boiler again.

Design doc is already made but its ancient as shit and I'm just gonna
make a new one so its WIP for now.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Totalepicness
add: Added "Globber Boiler", which is a total replacement of base
boiler, designed to kill the "safe" gameplay loops of current base
boiler in an attempt for a more challenging and fun caste to both play
as and against.
balance: Globber Active 1 - Bombard: Spit a large acid glob that will,
upon impact, immediately spread a gas glob of your choice
balance: Globber Active 2 - Spray acid: Instantly sprays a line of acid
balance: Globber Active 3 - Shift spits: Switch between acid and neuro
gas globs. Acid deals damage while neuro slows, blinds and eventually
knocks down marines. Neuro has a larger radius than acid
balance: Globber Active 4 - Acid shroud: A quick windup action that
dumps an acid cloud over the boiler. Cooldowns other abilities similar
to dump acid.
balance: Globber Active 5 - Zoom: Short-ranged zoom with no windup.
balance: Globber Passive: Globber features armor, but it is weaker
against flames! Stay away from fire!
refactor: Refractored some minor spit code and icons
balance: Neuro has been completely reworked to deal mainly stamina
damage, causes dizzyness and has a small chance to make you 'stumble' in
a random direction along with minor tox damage. Stay out of it!
add: Completly reworked neuro gas, it now uses a proper effect with
escalating effects the larger the dosage rather than RNG.
fix: Acid now deals damage to cades and now has a good chance of going
over instead of being airtight
fix:  Boiler globs no longer can target mobs and track them.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: Geeves <ggrobler447@gmail.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [KennethMetz/anime_finder](https://github.com/KennethMetz/anime_finder)@[0d942c2413...](https://github.com/KennethMetz/anime_finder/commit/0d942c2413f8782edfc745764881510eb0d71688)
#### Tuesday 2023-03-07 02:45:13 by Steve Metz

Normalize avatar images, update some for quality

I've updated the portrait images to all be 160x160 jpgs.  I tried to select similar pictures to the ones originally added, but in some cases I had to choose a slightly different picture to either get the color temperatures to line up right (the character was from a still in a show where their skin was tined weird colors by the lighting of the scene or something), or to get the quality high enough that all the images look matching.  I couldn't for the life of me find a good portrait shot of rebecca to work with, so I replaced her with another character from the mocks, but we can add her back if we can find a good portrait that plays well with the others.  Not totally set on these as the final images of these characters (Naruto's has some compression artifacts from the source image that I don't love).  In the end, it will probably be ok to have some variance in the image color temps and qualities, as long as "sets" of images from each show all look consistent (i.e. Naruto's characters may never look as HD as those from a new show, but if the row of Naruto avatars all match well, and the row of each other show's avatars match, then it should work)

---
## [saint-lascivious/saint-lascivious.github.io](https://github.com/saint-lascivious/saint-lascivious.github.io)@[6585d105cd...](https://github.com/saint-lascivious/saint-lascivious.github.io/commit/6585d105cd1b1f8c64c13136d81650a408989179)
#### Tuesday 2023-03-07 02:49:54 by Hayden Pearce

saint-lascivious.github.io: idiotic serviceworker qoute snafu

 - i didn't use backticks with the baseDomain template literals
   (fuck javascript)

Changes to be committed:
 - modified:   .formatted/serviceworker.min.js
 - modified:   serviceworker.min.js

---
## [balabit-deps/balabit-os-7-linux](https://github.com/balabit-deps/balabit-os-7-linux)@[213445bcb5...](https://github.com/balabit-deps/balabit-os-7-linux/commit/213445bcb5451a6a5b9d35c6f97d1f470b54c728)
#### Tuesday 2023-03-07 03:24:27 by Luke Nowakowski-Krijger

Import Debian changes 4.15.0-206.217

linux (4.15.0-206.217) bionic; urgency=medium

  * bionic/linux: 4.15.0-206.217 -proposed tracker (LP: #2004655)

  * CVE-2023-0461
    - SAUCE: Fix inet_csk_listen_start after CVE-2023-0461

linux (4.15.0-205.216) bionic; urgency=medium

  * bionic/linux: 4.15.0-205.216 -proposed tracker (LP: #2004414)

  * Bionic update: upstream stable patchset 2023-01-20 (LP: #2003596)
    - NFSv4.1: Handle RECLAIM_COMPLETE trunking errors
    - NFSv4.1: We must always send RECLAIM_COMPLETE after a reboot
    - nfs4: Fix kmemleak when allocate slot failed
    - net: dsa: Fix possible memory leaks in dsa_loop_init()
    - nfc: s3fwrn5: Fix potential memory leak in s3fwrn5_nci_send()
    - nfc: nfcmrvl: Fix potential memory leak in nfcmrvl_i2c_nci_send()
    - net: fec: fix improper use of NETDEV_TX_BUSY
    - ata: pata_legacy: fix pdc20230_set_piomode()
    - net: sched: Fix use after free in red_enqueue()
    - ipvs: use explicitly signed chars
    - rose: Fix NULL pointer dereference in rose_send_frame()
    - mISDN: fix possible memory leak in mISDN_register_device()
    - isdn: mISDN: netjet: fix wrong check of device registration
    - btrfs: fix inode list leak during backref walking at resolve_indirect_refs()
    - btrfs: fix ulist leaks in error paths of qgroup self tests
    - Bluetooth: L2CAP: fix use-after-free in l2cap_conn_del()
    - net: mdio: fix undefined behavior in bit shift for __mdiobus_register
    - net, neigh: Fix null-ptr-deref in neigh_table_clear()
    - media: s5p_cec: limit msg.len to CEC_MAX_MSG_SIZE
    - media: dvb-frontends/drxk: initialize err to 0
    - i2c: xiic: Add platform module alias
    - Bluetooth: L2CAP: Fix attempting to access uninitialized memory
    - block, bfq: protect 'bfqd->queued' by 'bfqd->lock'
    - btrfs: fix type of parameter generation in btrfs_get_dentry
    - tcp/udp: Make early_demux back namespacified.
    - capabilities: fix potential memleak on error path from vfs_getxattr_alloc()
    - ALSA: usb-audio: Add quirks for MacroSilicon MS2100/MS2106 devices
    - efi: random: reduce seed size to 32 bytes
    - parisc: Make 8250_gsc driver dependend on CONFIG_PARISC
    - parisc: Export iosapic_serial_irq() symbol for serial port driver
    - ext4: fix warning in 'ext4_da_release_space'
    - KVM: x86: Mask off reserved bits in CPUID.80000008H
    - KVM: x86: emulator: em_sysexit should update ctxt->mode
    - KVM: x86: emulator: introduce emulator_recalc_and_set_mode
    - KVM: x86: emulator: update the emulation mode after CR0 write
    - linux/const.h: prefix include guard of uapi/linux/const.h with _UAPI
    - linux/const.h: move UL() macro to include/linux/const.h
    - linux/bits.h: make BIT(), GENMASK(), and friends available in assembly
    - RDMA/qedr: clean up work queue on failure in qedr_alloc_resources()
    - net: tun: fix bugs for oversize packet when napi frags enabled
    - ipvs: fix WARNING in __ip_vs_cleanup_batch()
    - ipvs: fix WARNING in ip_vs_app_net_cleanup()
    - ipv6: fix WARNING in ip6_route_net_exit_late()
    - parisc: Avoid printing the hardware path twice
    - HID: hyperv: fix possible memory leak in mousevsc_probe()
    - net: gso: fix panic on frag_list with mixed head alloc types
    - bnxt_en: fix potentially incorrect return value for ndo_rx_flow_steer
    - net: fman: Unregister ethernet device on removal
    - capabilities: fix undefined behavior in bit shift for CAP_TO_MASK
    - net: lapbether: fix issue of dev reference count leakage in
      lapbeth_device_event()
    - hamradio: fix issue of dev reference count leakage in bpq_device_event()
    - drm/vc4: Fix missing platform_unregister_drivers() call in
      vc4_drm_register()
    - ipv6: addrlabel: fix infoleak when sending struct ifaddrlblmsg to network
    - tipc: fix the msg->req tlv len check in
      tipc_nl_compat_name_table_dump_header
    - dmaengine: mv_xor_v2: Fix a resource leak in mv_xor_v2_remove()
    - drivers: net: xgene: disable napi when register irq failed in
      xgene_enet_open()
    - net: cxgb3_main: disable napi when bind qsets failed in cxgb_up()
    - ethernet: s2io: disable napi when start nic failed in s2io_card_up()
    - net: mv643xx_eth: disable napi when init rxq or txq failed in
      mv643xx_eth_open()
    - net: macvlan: fix memory leaks of macvlan_common_newlink
    - arm64: efi: Fix handling of misaligned runtime regions and drop warning
    - ALSA: hda: fix potential memleak in 'add_widget_node'
    - ALSA: usb-audio: Add quirk entry for M-Audio Micro
    - nilfs2: fix deadlock in nilfs_count_free_blocks()
    - drm/i915/dmabuf: fix sg_table handling in map_dma_buf
    - platform/x86: hp_wmi: Fix rfkill causing soft blocked wifi
    - btrfs: selftests: fix wrong error check in btrfs_free_dummy_root()
    - udf: Fix a slab-out-of-bounds write bug in udf_find_entry()
    - cert host tools: Stop complaining about deprecated OpenSSL functions
    - dmaengine: at_hdmac: Fix at_lli struct definition
    - dmaengine: at_hdmac: Don't start transactions at tx_submit level
    - dmaengine: at_hdmac: Fix completion of unissued descriptor in case of errors
    - dmaengine: at_hdmac: Don't allow CPU to reorder channel enable
    - dmaengine: at_hdmac: Fix impossible condition
    - dmaengine: at_hdmac: Check return code of dma_async_device_register
    - x86/cpu: Restore AMD's DE_CFG MSR after resume
    - selftests/futex: fix build for clang
    - drm/imx: imx-tve: Fix return type of imx_tve_connector_mode_valid
    - ASoC: core: Fix use-after-free in snd_soc_exit()
    - serial: 8250_omap: remove wait loop from Errata i202 workaround
    - serial: 8250: omap: Flush PM QOS work on remove
    - tty: n_gsm: fix sleep-in-atomic-context bug in gsm_control_send
    - ASoC: soc-utils: Remove __exit for snd_soc_util_exit()
    - block: sed-opal: kmalloc the cmd/resp buffers
    - parport_pc: Avoid FIFO port location truncation
    - pinctrl: devicetree: fix null pointer dereferencing in pinctrl_dt_to_map
    - net: bgmac: Drop free_netdev() from bgmac_enet_remove()
    - mISDN: fix possible memory leak in mISDN_dsp_element_register()
    - mISDN: fix misuse of put_device() in mISDN_register_device()
    - net: caif: fix double disconnect client in chnl_net_open()
    - xen/pcpu: fix possible memory leak in register_pcpu()
    - drbd: use after free in drbd_create_device()
    - net/x25: Fix skb leak in x25_lapb_receive_frame()
    - cifs: Fix wrong return value checking when GETFLAGS
    - ftrace: Fix the possible incorrect kernel message
    - ftrace: Optimize the allocation for mcount entries
    - ftrace: Fix null pointer dereference in ftrace_add_mod()
    - ring_buffer: Do not deactivate non-existant pages
    - ALSA: usb-audio: Drop snd_BUG_ON() from snd_usbmidi_output_open()
    - USB: serial: option: add Sierra Wireless EM9191
    - USB: serial: option: remove old LARA-R6 PID
    - USB: serial: option: add u-blox LARA-R6 00B modem
    - USB: serial: option: add u-blox LARA-L6 modem
    - USB: serial: option: add Fibocom FM160 0x0111 composition
    - usb: add NO_LPM quirk for Realforce 87U Keyboard
    - usb: chipidea: fix deadlock in ci_otg_del_timer
    - iio: adc: at91_adc: fix possible memory leak in at91_adc_allocate_trigger()
    - iio: trigger: sysfs: fix possible memory leak in iio_sysfs_trig_init()
    - iio: pressure: ms5611: changed hardcoded SPI speed to value limited
    - dm ioctl: fix misbehavior if list_versions races with module loading
    - serial: 8250: Fall back to non-DMA Rx if IIR_RDI occurs
    - serial: 8250_lpss: Configure DMA also w/o DMA filter
    - mmc: core: properly select voltage range without power cycle
    - mmc: sdhci-pci: Fix possible memory leak caused by missing pci_dev_put()
    - misc/vmw_vmci: fix an infoleak in vmci_host_do_receive_datagram()
    - nilfs2: fix use-after-free bug of ns_writer on remount
    - serial: 8250: Flush DMA Rx on RLSI
    - macvlan: enforce a consistent minimal mtu
    - tcp: cdg: allow tcp_cdg_release() to be called multiple times
    - kcm: avoid potential race in kcm_tx_work
    - bpf, test_run: Fix alignment problem in bpf_prog_test_run_skb()
    - kcm: close race conditions on sk_receive_queue
    - 9p: trans_fd/p9_conn_cancel: drop client lock earlier
    - gfs2: Check sb_bsize_shift after reading superblock
    - gfs2: Switch from strlcpy to strscpy
    - 9p/trans_fd: always use O_NONBLOCK read/write
    - mm: fs: initialize fsdata passed to write_begin/write_end interface
    - ntfs: fix use-after-free in ntfs_attr_find()
    - ntfs: fix out-of-bounds read in ntfs_attr_find()
    - ntfs: check overflow when iterating ATTR_RECORDs
    - wifi: cfg80211: fix memory leak in query_regdb_file()
    - net: tun: Fix memory leaks of napi_get_frags
    - riscv: process: fix kernel info leakage
    - vmlinux.lds.h: Fix placement of '.data..decrypted' section
    - net: thunderbolt: Fix error handling in tbnet_init()
    - scsi: target: tcm_loop: Fix possible name leak in tcm_loop_setup_hba_bus()
    - Input: i8042 - fix leaking of platform device on module removal
    - wifi: mac80211_hwsim: fix debugfs attribute ps with rc table support
    - audit: fix undefined behavior in bit shift for AUDIT_BIT
    - wifi: mac80211: Fix ack frame idr leak when mesh has no route
    - spi: stm32: fix stm32_spi_prepare_mbr() that halves spi clk for every run
    - MIPS: pic32: treat port as signed integer
    - af_key: Fix send_acquire race with pfkey_register
    - ARM: dts: am335x-pcm-953: Define fixed regulators in root node
    - bus: sunxi-rsb: Support atomic transfers
    - ARM: dts: at91: sam9g20ek: enable udc vbus gpio pinctrl
    - nfc/nci: fix race with opening and closing
    - net: pch_gbe: fix potential memleak in pch_gbe_tx_queue()
    - 9p/fd: fix issue of list_del corruption in p9_fd_cancel()
    - ARM: mxs: fix memory leak in mxs_machine_init()
    - net/mlx4: Check retval of mlx4_bitmap_init
    - net/qla3xxx: fix potential memleak in ql3xxx_send()
    - xfrm: Fix ignored return value in xfrm6_init()
    - NFC: nci: fix memory leak in nci_rx_data_packet()
    - dccp/tcp: Reset saddr on failure after inet6?_hash_connect().
    - s390/dasd: fix no record found for raw_track_access
    - nfc: st-nci: fix incorrect validating logic in EVT_TRANSACTION
    - nfc: st-nci: fix memory leaks in EVT_TRANSACTION
    - net: thunderx: Fix the ACPI memory leak
    - s390/crashdump: fix TOD programmable field size
    - nios2: add FORCE for vmlinuz.gz
    - arm64: dts: rockchip: lower rk3399-puma-haikou SD controller clock frequency
    - iio: light: apds9960: fix wrong register for gesture gain
    - iio: core: Fix entry not deleted when iio_register_sw_trigger_type() fails
    - kconfig: display recursive dependency resolution hint just once
    - nilfs2: fix nilfs_sufile_mark_dirty() not set segment usage as dirty
    - Input: synaptics - switch touchpad on HP Laptop 15-da3001TU to RMI mode
    - serial: 8250: 8250_omap: Avoid RS485 RTS glitch on ->set_termios()
    - xen/platform-pci: add missing free_irq() in error path
    - platform/x86: asus-wmi: add missing pci_dev_put() in asus_wmi_set_xusb2pr()
    - platform/x86: acer-wmi: Enable SW_TABLET_MODE on Switch V 10 (SW5-017)
    - platform/x86: hp-wmi: Ignore Smart Experience App event
    - [Config] updateconfigs for INET_TABLE_PERTURB_ORDER
    - tcp: configurable source port perturb table size
    - net: usb: qmi_wwan: add Telit 0x103a composition
    - drm/amdgpu: always register an MMU notifier for userptr
    - iio: health: afe4403: Fix oob read in afe4403_read_raw
    - iio: health: afe4404: Fix oob read in afe4404_[read|write]_raw
    - iio: light: rpr0521: add missing Kconfig dependencies
    - hwmon: (i5500_temp) fix missing pci_disable_device()
    - hwmon: (ibmpex) Fix possible UAF when ibmpex_register_bmc() fails
    - of: property: decrement node refcount in of_fwnode_get_reference_args()
    - net/mlx5: Fix uninitialized variable bug in outlen_write()
    - can: sja1000_isa: sja1000_isa_probe(): add missing free_sja1000dev()
    - can: cc770: cc770_isa_probe(): add missing free_cc770dev()
    - qlcnic: fix sleep-in-atomic-context bugs caused by msleep
    - net: phy: fix null-ptr-deref while probe() failed
    - net: net_netdev: Fix error handling in ntb_netdev_init_module()
    - net/9p: Fix a potential socket leak in p9_socket_open
    - dsa: lan9303: Correct stat name
    - net: hsr: Fix potential use-after-free
    - packet: do not set TP_STATUS_CSUM_VALID on CHECKSUM_COMPLETE
    - net: ethernet: renesas: ravb: Fix promiscuous mode after system resumed
    - hwmon: (coretemp) Check for null before removing sysfs attrs
    - hwmon: (coretemp) fix pci device refcount leak in nv1a_ram_new()
    - perf: Add sample_flags to indicate the PMU-filled sample data
    - btrfs: qgroup: fix sleep from invalid context bug in btrfs_qgroup_inherit()
    - tools/vm/slabinfo-gnuplot: use "grep -E" instead of "egrep"
    - nilfs2: fix NULL pointer dereference in nilfs_palloc_commit_free_entry()
    - x86/bugs: Make sure MSR_SPEC_CTRL is updated properly upon resume from S3
    - arm64: Fix panic() when Spectre-v2 causes Spectre-BHB to re-allocate KVM
      vectors
    - arm64: errata: Fix KVM Spectre-v2 mitigation selection for Cortex-A57/A72
    - efi: random: Properly limit the size of the random seed
    - ASoC: ops: Fix bounds check for _sx controls
    - pinctrl: single: Fix potential division by zero
    - iommu/vt-d: Fix PCI device refcount leak in dmar_dev_scope_init()
    - nvme: restrict management ioctls to admin
    - x86/tsx: Add a feature bit for TSX control MSR support
    - x86/pm: Add enumeration check before spec MSRs save/restore setup
    - x86/ioremap: Fix page aligned size calculation in __ioremap_caller()
    - mmc: sdhci: use FIELD_GET for preset value bit masks
    - mmc: sdhci: Fix voltage switch delay
    - proc: avoid integer type confusion in get_proc_long
    - proc: proc_skip_spaces() shouldn't think it is working on C strings
    - v4l2: don't fall back to follow_pfn() if pin_user_pages_fast() fails
    - ipc/sem: Fix dangling sem_array access in semtimedop race
    - x86/nospec: Fix i386 RSB stuffing
    - Revert "x86/speculation: Change FILL_RETURN_BUFFER to work with objtool"
    - ASoC: sgtl5000: Reset the CHIP_CLK_CTRL reg on remove
    - net: pch_gbe: fix pci device refcount leak while module exiting
    - Drivers: hv: vmbus: fix double free in the error path of
      vmbus_add_channel_work()
    - Drivers: hv: vmbus: fix possible memory leak in vmbus_device_register()
    - bnx2x: fix pci device refcount leak in bnx2x_vf_is_pcie_pending()
    - iio: pressure: ms5611: fixed value compensation bug
    - arm: dts: rockchip: fix node name for hym8563 rtc
    - ARM: dts: rockchip: fix ir-receiver node names
    - ARM: 9251/1: perf: Fix stacktraces for tracepoint events in THUMB2 kernels
    - ARM: 9266/1: mm: fix no-MMU ZERO_PAGE() implementation
    - ARM: dts: rockchip: disable arm_global_timer on rk3066 and rk3188
    - ALSA: seq: Fix function prototype mismatch in snd_seq_expand_var_event
    - ASoC: soc-pcm: Add NULL check in BE reparenting
    - regulator: twl6030: fix get status of twl6032 regulators
    - net: usb: qmi_wwan: add u-blox 0x1342 composition
    - xen/netback: do some code cleanup
    - xen/netback: don't call kfree_skb() with interrupts disabled
    - rcutorture: Automatically create initrd directory
    - media: v4l2-dv-timings.c: fix too strict blanking sanity checks
    - memcg: fix possible use-after-free in memcg_write_event_control()
    - KVM: s390: vsie: Fix the initialization of the epoch extension (epdx) field
    - HID: hid-lg4ff: Add check for empty lbuf
    - HID: core: fix shift-out-of-bounds in hid_report_raw_event
    - ieee802154: cc2520: Fix error return code in cc2520_hw_init()
    - ca8210: Fix crash by zero initializing data
    - gpio: amd8111: Fix PCI device reference count leak
    - e1000e: Fix TX dispatch condition
    - igb: Allocate MSI-X vector when testing
    - Bluetooth: 6LoWPAN: add missing hci_dev_put() in get_l2cap_conn()
    - mac802154: fix missing INIT_LIST_HEAD in ieee802154_if_add()
    - net: encx24j600: Add parentheses to fix precedence
    - net: encx24j600: Fix invalid logic in reading of MISTAT register
    - net: mvneta: Prevent out of bounds read in mvneta_config_rss()
    - NFC: nci: Bounds check struct nfc_target arrays
    - net: stmmac: fix "snps,axi-config" node property parsing
    - net: hisilicon: Fix potential use-after-free in hisi_femac_rx()
    - net: hisilicon: Fix potential use-after-free in hix5hd2_rx()
    - tipc: Fix potential OOB in tipc_link_proto_rcv()
    - ethernet: aeroflex: fix potential skb leak in greth_init_rings()
    - net: plip: don't call kfree_skb/dev_kfree_skb() under spin_lock_irq()
    - ipv6: avoid use-after-free in ip6_fragment()
    - net: mvneta: Fix an out of bounds check
    - net: mvneta: Prevent out of bounds read in mvneta_config_rss()
    - i40e: Fix not setting default xps_cpus after reset
    - i40e: Fix for VF MAC address 0
    - i40e: Disallow ip4 and ip6 l4_4_bytes
    - nvme initialize core quirks before calling nvme_init_subsystem
    - can: esd_usb: Allow REC and TEC to return to zero

  * CVE-2022-3628
    - wifi: brcmfmac: Fix potential buffer overflow in brcmf_fweh_event_worker()

  * rdpru in ubuntu_kvm_unit_tests failed on B-4.15 node riccioli with FAIL:
    RDPRU raises #UD (LP: #1968681)
    - x86/cpufeatures: Add feature bit RDPRU on AMD
    - kvm: svm: Intercept RDPRU

  * NFS: client permission error after adding user to permissible group
    (LP: #2003053)
    - cred: add cred_fscmp() for comparing creds.
    - NFS: Clear the file access cache upon login
    - NFS: Judge the file access cache's timestamp in rcu path
    - NFS: Fix up a sparse warning

  * 5.15.0-58.64 breaks xen bridge networking (pvh domU) (LP: #2002889)
    - xen/netback: fix build warning

  * CVE-2023-0461
    - net/ulp: prevent ULP without clone op from entering the LISTEN status

  * CVE-2022-3545
    - nfp: fix use-after-free in area_cache_get()

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[645054b489...](https://github.com/ArcaneDefence/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Tuesday 2023-03-07 03:29:39 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[db7534d6da...](https://github.com/tgstation/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Tuesday 2023-03-07 03:49:07 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [larryv/dotfiles](https://github.com/larryv/dotfiles)@[4b3eb37d3f...](https://github.com/larryv/dotfiles/commit/4b3eb37d3fabf743df369507b09453fb0ca22329)
#### Tuesday 2023-03-07 03:51:28 by Lawrence Velázquez

Drop some temporary shell variables

I've changed my mind since 01afd9e (Use temporary shell variables for
in-progress data, 2021-06-21) and 29c57cc (gnupg, sh: Don't error-handle
`export` or `shift`, 2021-06-24).  Now I'm trying to make things simpler
and clearer, with fewer moving parts.  These temporary variables aren't
necessary and don't serve an obvious purpose, so they should go.

    YOU: "simpler and clearer"?  this whole project is messy and obtuse
    ME:  shut up

Furthermore, I've been a little obsessed lately with handling unlikely
failure modes, one of which is variable assignment error.  I've been
testing how different shells respond to that and thinking about how to
manage that failure.  One approach is to have fewer variables to worry
about in the first place, so here we are.

    YOU: hell yeah, overthinking nonexistent problems is your jam
    ME:  shut up

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[34daca112c...](https://github.com/PhantomEpicness/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Tuesday 2023-03-07 04:03:52 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

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

:cl:
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[fc1e2e5e26...](https://github.com/PhantomEpicness/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Tuesday 2023-03-07 04:03:52 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
 
:cl:
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[bc48a6eafc...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/bc48a6eafcf9afedfc419afaa982dd15339a94aa)
#### Tuesday 2023-03-07 05:23:23 by Darius

Add vampire ability permission check

Adds a new mob proc that allows checking if vampiric abilities should function. Allows easily checking anti-magic, trait holy, garlic necklace, garlic blood, and staked status.

Bloodfledge actions and coffin healing will now use this check. Flight potions will warn bloodfledge quirk users before allowing consumption.

---
## [rstrojan/AutoBattlerPrototype](https://github.com/rstrojan/AutoBattlerPrototype)@[d7eaaa7a30...](https://github.com/rstrojan/AutoBattlerPrototype/commit/d7eaaa7a303e713faeaea6e928ce7208ce8aa4ae)
#### Tuesday 2023-03-07 05:51:44 by Ryan Suter

Inventory and PrntScrn upgrades

-MAN OH MAN that was a real challange. I set up the assignSlotValueOnly functionality and that was far more difficult than I had imagined. However, from the user standpoint, it should be incredibly easy to use. If you want it to be printed as "key: value" you pass it normally to assignSlot(1, myMap). However, if you don't want it formatted like that, you can print out just the value using an optional bool argument, assignSlot(1, myMap, true), that sets a isValueOnly flag, which gets used when formatting the map to print.
- To accomplish this, I created a new struct called slot { map, isValueOnly }. The isValueOnly flag is then used to determine how the information is going to be printed to the screen. After some trial and error (mostly error) I decided not to use function pointers (you're welcome future you). Instead, I decided I would just add some if logic to handle the two cases of key:value or valueOnly. Those few sentences make it sound like it was a pretty straightforward afair, but it felt like a gigantic mess. And I think I did make a mistake at this point (well later it will be revealed I had made two), which was that I should have scrapped all of my changes to this file completely and taken a break of maybe 30 minutes. That would have given some time to reflect on what I had done and come back to a completely clean slate. However, I did not do that, I barely took a break and only reverted a portion of what I had changed. By doing that, I felt a bit like I was standing on bad foundation and that maybe some of the errors I was getting were because I hadn't completely reverted the file and I had left something that should have been deleted. That nagging question sat on my mind for quite a while. Then I had gotten so far that I started succumbing to the sunk-cost fallacy. The issue I was facing was having to do with pointers, references, and types. It's a common issue to run into, but this one has taken the longest to fix out of any of them. Indeed, I was not actually able to fix it, so I deleted it. Made it simpler. I went with storing only the isValueOnly flag and using that to branch logic. HOWEVER, remember when I had mentioned that there was a second bug? Well, there was and it was pretty rooky. At one point, I was passing an obj as a copy and not as a reference, so I wasn't getting the changes I had expected to see. So after trying to do one of the most complex pointer/reference configuration I've done so far, I made the very error that they use to teach how references work.
- Well, overall it was a good weekend though. I made two pretty significant changes to core functionality relating to inventory and printing. The only coding thing that I did not get to yet was moving the obj data over into GameState.
-There is one outstanding issue that we are going to have to face sooner or later: Print Order. You can't have inventories seemingly change order.

---
## [larryv/dotfiles](https://github.com/larryv/dotfiles)@[c7a94a3472...](https://github.com/larryv/dotfiles/commit/c7a94a34729ac33e269a2fc50866c50cb100a807)
#### Tuesday 2023-03-07 06:04:08 by Lawrence Velázquez

Drop some temporary shell variables

I've changed my mind since 01afd9e (Use temporary shell variables for
in-progress data, 2021-06-21) and 29c57cc (gnupg, sh: Don't error-handle
`export` or `shift`, 2021-06-24).  Now I'm trying to make things simpler
and clearer, with fewer moving parts.  These temporary variables aren't
necessary or obviously beneficial, so they should go.

    YOU: "simpler and clearer"?  this whole project is messy and obtuse
     ME: shut up

Furthermore, I've been a little obsessed lately with handling unlikely
failure modes, one of which is variable assignment error.  I've been
testing how different shells respond to that and thinking about how to
manage that failure.  One approach is to have fewer variables to worry
about in the first place, so here we are.

    YOU: hell yeah, overthinking nonexistent problems is your jam
     ME: shut up

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[c9a7611c75...](https://github.com/Kapu1178/daedalusdock/commit/c9a7611c75ca8d6fbbe413cc52607ab495017cb8)
#### Tuesday 2023-03-07 06:07:40 by Kapu1178

Fixes asset caching (#69852) (#193)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Veritius/space-station-14](https://github.com/Veritius/space-station-14)@[581e8a0d12...](https://github.com/Veritius/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Tuesday 2023-03-07 07:10:49 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [fineks/rustest](https://github.com/fineks/rustest)@[d21740b475...](https://github.com/fineks/rustest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Tuesday 2023-03-07 07:17:09 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [DutKulang/LEAD](https://github.com/DutKulang/LEAD)@[cde04bc0a0...](https://github.com/DutKulang/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Tuesday 2023-03-07 07:18:54 by Dawa Edina Hillary

Proposed changed for Sida's profile

---
layout: profile
title:  "Sida Lillian"
image: "assets/images/profiles/Sida-Lillian/Sida-Lillian.jpg"
country: Uganda
region: West Nile
hub: CC4D
languages: "English (Fluent spoken and written), Bari/Kakwa (Fluent spoken and spoken), Arabic (good spoken only), Lugbara (fair spoken only)"
mail: sidalilian@proton.me
phone: "+256782739162"
whatsapp: 
website: 
telegram: "+256782739162"
github: github.com/sidalillian
linkedin: 
twitter: 
facebook: https://www.facebook.com/profile.php?id=100074066215635
instagram: 
mastodon: 
wikifab:
skills:
  - {name: Web & Software, number: 1, qualification: "using platforms, basic social media experiences, software download and installation \n \n
     * [Sida Lilian was trained on social media skills during the #ASKnet training in 2018](https://m.facebook.com/story.php?story_fbid=303135693607634&id=100017336164583) "}
  - {name: Community & Moderation, number: 2, qualification: "connecting people, trauma healing, event facilitation and meditation \n \n 
     * Certificate of participation in trauma healing& meditation training \n
     * She was trained and facilitated a post training on how to use Condoms under the #ASKnet project 2018"}
  - {name: Data Security & Research, number: 3, qualification: "data collection and protection of personal data \n \n 
     * Certificate in data collection"}

---

Sida Lilian is a female South Sudanese refugee in Uganda.

Expert in data collection, trauma healing, mediation, event facilitation of different types.

She was trained on how to collect both qualitative and quantitative data by REACH Uganda, Danish Refugee Council, Norwegian Refugee Council Uganda and GROUND TRUTH SOLUTIONS, she was also trained and worked as frontline worker on the *BOOST FOR THE YOUNGEST by Save The Children under Dubai Cara not only that she was also trained on Social Enterprise online by Makerere University - Canada in 2018, she was trained and worked as hygiene Promoter by CEFORD Uganda and was also trained and worked as Community Development Worker (CDW) by Danish Refugee Council.

She is confident, talented and determined to transform her community.

---
## [Keenonthedaywalker/Simple-CK2-AGOT-Mod-File-Parser](https://github.com/Keenonthedaywalker/Simple-CK2-AGOT-Mod-File-Parser)@[2738821270...](https://github.com/Keenonthedaywalker/Simple-CK2-AGOT-Mod-File-Parser/commit/27388212704522868b1e888eff506523c3c02283)
#### Tuesday 2023-03-07 07:30:45 by Keenon

Uploaded all the files.

Brother, I can not, for the life of me, remember what is supposed to be the main file, I THINK that it is just main one and the rest are test files, so that's why I will be keeping them, maybe they lead me to some future insight... Also whatever you do, make sure THAT THERE IS A FULLY BLANK LINE AT THE BOTTOM OF TEXT FILE YOU WANT TO PARSE.

---
## [migzone/dsvpn](https://github.com/migzone/dsvpn)@[230a486914...](https://github.com/migzone/dsvpn/commit/230a486914bd0751e80cc64ac04ff3127022ced5)
#### Tuesday 2023-03-07 07:32:31 by Naveen Nathan

Idiotproof usage: show a basic example (#61)

Rationale:

1. Some don't remember dd incanatation and how many bytes are needed
   exactly for a key.

2. base64 is bloody complicated.

3. Even when confronted with the usage screen - it isn't immediately
   clear what is the quickest way to start the vpn; even now I still
   refer to the project README anyway.

base64 usage is hard to remember because it's inconsistent across
platforms -- but can be used consistently. It's partly the
luck of the draw depending on which platforms you interact with.

First it is hard to specify input for base64 if you try too hard.
Most implementations thankfully use stdin by default for encode
and decode.

Remember the encode flag is hard. There's -e and --encode. Except
as far as I can tell it's only for FreeBSD. Linux and Mac both
default to encode without even providing an option.

Ditto for decoding. It's hard to remember if it is:
base64 -d or -D or --decode. It is -d on Linux/FreeBSD, -D on mac,
but fortunately --decode across all.

This usage screen puts an end to the madness and gives the most common
ways to do it across platforms, which may not work 99% of the time.
Otherwise, I'm unnecessarily spending a few minutes to
github.com/jedisct1/dsvpn and ctrl-f for dd/base64.

And frankly the usage screen is probably biggest selling point of the
program. Even despite how trivial it is to deploy OpenVPN with a
single config file + a few certificates :).

---
## [Offroaders123/Flatlands](https://github.com/Offroaders123/Flatlands)@[532dfbb57b...](https://github.com/Offroaders123/Flatlands/commit/532dfbb57b16c715942c6122affedbb6ea7a15c3)
#### Tuesday 2023-03-07 08:57:25 by Offroaders123

Component Streamlining

That title made me think of Rush Dreamline, now I want to play that while I write this :D

This further moves the app over to working in a more component-based manner, using less element IDs in this case.

First time using ChatGPT myself, tonight! My parents and I all tried it out. I think I do actually like the potential that it has. It's yet another thing to either dive right into and to try and embed into your life since it probably will eventually anyways, vs trying to stay away from it. I asked it some questions about the Legacy Console Edition world save format, and it was actually nearly accurate about everything! The only thing it didn't know correctly is that the Region files are named `.mcr` still, instead of `.mca` like modern versions of Java Edition. It also let me know that the Leveldown npm module actually does support zlib compression, and that's great news to me! Earlier before working on Flatlands today, I was looking into using `node-leveldb-zlib` as WASM in the browser, but that looked like it was gonna be a very heavy task to try and get done and working. If Leveldown does in fact have zlib support like GPT says it does, that will help a very big amount to getting Bedrock world save opening working in the browser! Browser-first is my biggest thing now that the web is so powerful nowadays.

Also just found out about a ton of news for WebKit/iOS! PWAs (Home Screen Web Apps :P ) are getting *muuuch* more powerful coming up here soon! I'm absolutely astounded with how much work the WebKit team appears to be putting into their browser for Web Apps now. Whether it's because of the possible lawsuits against Apple for the anti-competition things or not, they really are doing a great job at playing catch-up right now. Either way, I'm very happy that they are moving forward in that regard. As a dev, it makes me very happy to be able to prospect Apple's platforms to be great places for Web Apps in the future. Such a stark difference!

https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes

The lyrics to Dreamline actually collide very similar to some of my conversations today out and about, yesterday and today have felt like some of those days where things just start to click again, and you kind of feel like you know what your doing in life, and where you're going. While it's probably not too much different, you kind of have a glimpse that you know what you're doing might be the right thing for you.

Roll The Bones is a great album, gotta listen to this more often! It's also clicking for me tonight :)

Note to me: I should use the paragraph above for my own lyrics, that's a neat idea :D

Been working on my music production and sharing the last few days too, the Flatlands album being up is very happy-ing (?) to me, it's great to be moving forward with that (my music catalog stack overflow, haha).

---
## [xeronull/awesome-console-services](https://github.com/xeronull/awesome-console-services)@[4b8f298fb2...](https://github.com/xeronull/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Tuesday 2023-03-07 09:19:18 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [OneAsianTortoise/fulpstation](https://github.com/OneAsianTortoise/fulpstation)@[fc5620aa13...](https://github.com/OneAsianTortoise/fulpstation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Tuesday 2023-03-07 09:21:41 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [Offroaders123/Flatlands](https://github.com/Offroaders123/Flatlands)@[1e0ed2fa03...](https://github.com/Offroaders123/Flatlands/commit/1e0ed2fa03753bad3acc52f1b621350e4af0262e)
#### Tuesday 2023-03-07 09:32:32 by Offroaders123

Service Re-Worker

Upgraded the Service Worker! Now it's fancy just like STE's Service Worker setup.

Listening to Neurotica now, I love this song just as much as I remember back in freshman year while walking to school. Good times :D

I also just realized that I think this is where I started liking that flange/chorus-sound that I realized I liked on Metropolis Pt. 2, I think I was having light flashbacks to Rush when I heard that album about a year or two later in 2019. I've more recently been wondering where Petrucci got that taste for it too, as now I've been picking up on it more when listening to Rush and bands from that time. I have always really liked Lifeson's tone too, especially the chord strikes. You Bet Your Life is reminding me of Presto, Chain Lightning. Rush albums from that era remind me of my early high school years now; looking back on it, I guess that's when I ended up looking into them the most! High school really was great, even with the pandemic and all. Learned so much just those few years :)

---
## [smogon/pokemon-showdown-loginserver](https://github.com/smogon/pokemon-showdown-loginserver)@[317c0623db...](https://github.com/smogon/pokemon-showdown-loginserver/commit/317c0623db2cf5742f725a19f5fb4abc342616bd)
#### Tuesday 2023-03-07 09:36:37 by Guangcong Luo

Remove sql-template-strings dependency

Frivolous dependencies are bad for perf and bad for security.

The usual justification for frivolous dependencies is something like
"a community-maintained package is more likely to be bug-free and
maintained than something you wrote yourself", but:

1. frivolous dependencies are usually maintained by Just Some Random
   Guy, not by some community
2. you are probably more likely to introduce a bug using some guy's API
   incorrectly, than by writing a few lines of raw JavaScript that you
   understand inside and out
3. if that guy deprecates his package, or decides to ragequit, or
   whatever, you do not want to be depending on it
4. debugging becomes a lot more annoying
5. the dependency is full of unnecessary complexity to support use
   cases we're not even using

Anyway, yeah, there's no need for this dependency.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Tuesday 2023-03-07 09:46:28 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [newstools/2023-metro](https://github.com/newstools/2023-metro)@[db3e1db975...](https://github.com/newstools/2023-metro/commit/db3e1db9756d913a7426ce0b8f7952cae736da5d)
#### Tuesday 2023-03-07 09:46:31 by Billy Einkamerer

Created Text For URL [metro.co.uk/2023/03/06/lancashire-teen-sends-i-love-you-text-to-girlfriend-before-taking-his-life-18395978/]

---
## [madhanonline/Java-Programming](https://github.com/madhanonline/Java-Programming)@[68e3cbcf7e...](https://github.com/madhanonline/Java-Programming/commit/68e3cbcf7e14ffc2c3884ecc796c95adb7d3f924)
#### Tuesday 2023-03-07 09:47:55 by madhanonline

Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line. 

Input Format: 

Input consists of 4 integers. 

The first integer corresponds to x1 . 

The second integer corresponds to y1. 

The third and fourth integers correspond to x2 and y2 respectively. 

Output Format: 

Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]

Sample Input:

 2

 4

 10

 15

Sample Output:

Binoy's house is located at (6.0,9.5)

---
## [madhanonline/Java-Programming](https://github.com/madhanonline/Java-Programming)@[b471ee2dda...](https://github.com/madhanonline/Java-Programming/commit/b471ee2dda4ac12f0f0baa0a4ba8db523db143da)
#### Tuesday 2023-03-07 09:56:49 by madhanonline

Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output

6.0
9.5

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a3451b7fe4...](https://github.com/tgstation/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Tuesday 2023-03-07 11:24:47 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [wanwan7777/Assignment_1](https://github.com/wanwan7777/Assignment_1)@[e5c397f634...](https://github.com/wanwan7777/Assignment_1/commit/e5c397f63405ec95dda4f838c083f51b39689de1)
#### Tuesday 2023-03-07 11:31:55 by Rachel

![IMG_7718](https://user-images.githubusercontent.com/125838993/222997163-b9ec3433-bc29-40a1-9169-0d4d42ffc5c9.png)

*My Name is Rachel, I'm a recent GMBA student in Tunghai University after completing my Finance degree in UTAR Malaysia.*

*I am an extrovent person and always be passionate to explore new things, so I'm activite in attending events and actvities during my uni life. Maybe is sound impossible but I am good at Volleyball which have been represented my state for the volleyball competitions. Other than that, as an extrovent, I also enjoy reading, listening to Jazz, and some art things like Baking, Acrylic Panting, Pottery Making, etc.*

*Besides, I quite feminist and willing to being the leader if needed, but there a quote, "Being alone, you can go faster, but as a team you can go far as you wish". So, I am a person have ability to work alone also willing to work as a team.*

- 2022 in Global Master of Business Administration 國企企業管理碩士 at Tunghai University 東海大學, Taiwan
- 2018 in Bachelor of Finance at Universiti Tunkul Abdul Rahman (UTAR)拉曼大學, Malaysia

- 2022 Chinese Online Tutor, Star Edu, Mongolian (PART-TIME)
- 2022 Sales Executive, Bisou Bisou Stores, Taiwan
- 2021 Customer Relationship Manager Assistant, EasyParcel, Malaysia
- 2019 Internship of Finance Assistant, Malaysia

- Chinese Cultural Night June 2019, Public Relation Assistant Manager
- Seken Art Festival Nov 2018, Public Relation Assistant Manager.
- Golden Tongue Debate Competition July 2018, Programme Helper
- Safety Campaign May 2018, Programme Manager
-  Photography Exploration May 2018, Decoration Assistant Manager
- Safety and Non-Smoking Campaign Jan 2018, Decoration Assistant Manager
- Song Composing Competition Feb 2018, Public Relation Assistant Manager
- Talent time Jan 2018, Public Relation Assistant Manager

- English - Professional proficiency in listening, speaking, reading, and writing
- Bahasa Melayu
- Chinese, Native

---
## [VastKilleroOm/Skyrat-tg](https://github.com/VastKilleroOm/Skyrat-tg)@[1fe9efd00a...](https://github.com/VastKilleroOm/Skyrat-tg/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Tuesday 2023-03-07 11:32:22 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[307bcafdef...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/307bcafdef765c3c0072b70127294d4fd07a5069)
#### Tuesday 2023-03-07 11:56:37 by JoeBidenWhatAreYouHiding

Greetings, Canadian citizen.  We are here to report an incident in which you participated in wrongspeak against the rightful monarch.  "I just think that maybe we should have a bit more freedom of press, is all."  Your Social Credit score has been reduced by -50. You are in warning of dropping to a C-Class Civilian & at risk of reduced Ration Tickets.  God save the King.

---
## [kiVts/cmss13](https://github.com/kiVts/cmss13)@[7731fa738f...](https://github.com/kiVts/cmss13/commit/7731fa738f01b0c83dce6183a3e58387984926bf)
#### Tuesday 2023-03-07 14:11:34 by naut

A small assortment of more fortunes (#2643)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

> _"When you look through rose-colored glasses, all the red flags just
look like flags."_

Adding to the fortune cookie poll once again with some nice
inspirational quotes and bits to help someone's mood. Contains an
assortment of movie/TV quotes, inspirational words, and quotes from real
people. Yes, real people.

Also alphabetizes the fortunes.txt file to make everything more tidy.
Unfortunately this also demolishes the diff file, so the new fortunes
are provided below instead.

# Explain why it's good for the game

A little more motivation never hurt anyone, eh?
Change comes from embracing the future, not fighting your past.

# New Fortunes

<details>
<summary>Click to expand</summary>

```
A broken vase is more interesting than a perfect one.
A bruise is a lesson, and each lesson makes us better.
After all, tomorrow is another day.
All we have to decide is what to do with the time that is given to us.
Be the reason someone thinks life is worth living.
Be the reason someone wants to wake up in the morning.
Change comes from embracing the future, not fighting your past.
Do the thing that scares you the most.
Don't let anyone ever make you feel like you don't deserve what you want.
Embrace a new narrative.
Enter unknown territory.
Every day, in every way, you are getting better and better.
Every new beginning comes from some other beginning's end.
Everything always goes wrong. You just have to deal with it.
Everything you do is your life's work.
Evolve as a human.
Expect great things of yourself before you do them.
Follow your heart and see what turns up.
Fortune and glory.
Generosity is its own form of power.
Get busy living or get busy dying.
Get lost in the right direction.
Get out of your comfort zone. It's not even that comfortable.
Good instincts are worthless if you don't follow them.
Good news: the light at the end of the tunnel is not a train.
Great men are not born great, they grow great.
Happiness is not something ready made. It comes from your own actions.
I never dreamed about success. I worked for it.
If we wait until we're ready, we'll be waiting for the rest of our lives.
Imperfections are beautiful.
It's not our abilities that show what we truly are. It's our choices.
It's what you do right now that makes a difference.
Live in the constant unexpected.
Look how far you've come.
Love doesn't have to be a person. It can be a passion.
Love yourself, conquer your fears!
Loving yourself isn't vanity; it's sanity.
Make someone laugh today.
Make someone smile today.
Mind over matter.
Never be cruel, never be cowardly. And never ever eat pears.
Never forget who you are. The rest of the world will not. Wear it like armor and it can never be used to hurt you.
Never let anyone tell you what you can't do.
No man is good enough to govern another man without that other’s consent.
Normal is nothing more than a cycle on a washing machine.
Nothing can dim the light that shines from within.
Oh yes, the past can hurt. But you can either run from it, or learn from it.
One day you’ll look back at right now and say, 'If I got through that, I can get through anything.' And that will truly be a gift.
Recognize yourself in others.
Some people can't believe in themselves until someone else believes in them first.
Surviving is the least we can do.
The present is just one chapter of your own novel.
The weirdest people happen to be the most successful.
Turn wounds into wisdom.
We all make choices, but in the end, choices make us.
What people call you weird for is in fact your greatest strength.
While there's life, there's hope.
Why are you trying so hard to fit in when you were born to stand out?
Worrying means you suffer twice.
You are your best thing.
You attract what you are ready for.
You can discover a whole new world by just adjusting how you see everything.
You cannot live your life to please others. The choice must be yours.
You don’t lead by pointing and telling people some place to go. You lead by going to that place and making a case.
You make your own luck.
You'll never meet someone who isn't important.
You're never alone in your struggles.
```

</details>

Some of my favorites:

> Why are you trying so hard to fit in when you were born to stand out?
> Never let anyone tell you what you can't do.
> You don’t lead by pointing and telling people some place to go. You
lead by going to that place and making a case.
> Good instincts are worthless if you don't follow them.

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

:cl:
add: Added several new fortunes to fortune cookies.
code: Alphabetized the fortunes.txt file for fortune cookie blurbs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2eb146a25e...](https://github.com/treckstar/yolo-octo-hipster/commit/2eb146a25ea14d3db96c627f9081bcd65a364fff)
#### Tuesday 2023-03-07 17:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Stalkeros2/tgstation](https://github.com/Stalkeros2/tgstation)@[ae08395328...](https://github.com/Stalkeros2/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Tuesday 2023-03-07 17:54:52 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[97054a0e76...](https://github.com/cockroachdb/cockroach/commit/97054a0e76049cd8f78d8b534ab1e2107be9f2ed)
#### Tuesday 2023-03-07 18:05:55 by Tobias Grieger

kvnemesis: uniquely identify all versions

This is essentially a v2 of kvnemesis. While a lot of code has changed, it's not a rewrite, rather we are actually bringing kvnemesis closer to the idea which ultimately led to it being built. That idea is that if values can uniquely identify the operation which wrote them, serializability checking becomes easier as any observation of a value totally orders the reader and the writer with respect to each other. "Easier" meant both simpler code, as well as actually being able to computationally do the verification on complex histories.

Prior to this PR, kvnemesis was writing unique values where it could, but it couldn't do it for deletions - after all, a deletion is like writing a "nothing" to MVCC, and there wasn't any way to make two "nothings" distinguishable. Having broken with the basic premise of unique values, there was a lot of bending over backwards going on to avoid, for the most part, devolving into a "normal" serializability checker. However, for contrived edge cases this would not be avoidable, and so there would be histories that kvnemesis just couldn't handle.

"v2" (this PR) gets this right. The main contribution is that we now thread kvnemesis' sequence numbers all the way down into MVCC and back up with the RangeFeed. Values are now truly unique: a deletion tombstone is identifiable via its `MVCCValueHeader`, which carries the `kvnemesisutil.Seq` of the `Operation` that originally wrote it. On top of this, everything "just works" as you expect.

Plumbing testing-only fields through the KV API protobufs isn't something that was taken lightly and that required a good amount of deliberation. However, we figured out a clever (maybe too clever?) way to have these fields be zero-sized in production, meaning they cannot possibly affect production logic and they also do not influence struct sizes or the wire encoding. As a drawback, kvnemesis requires the `crdb_test` build tag (it will `t.Skip()` otherwise).

The remainder of this PR is mostly improvements in code quality. `echodriven` testing was introduced for many of the tests that could benefit from it. The core components of kvnemesis were reworked for clarity (the author spent the first week very confused and wishes for that experience to remain unrepeated by anyone). kvnemesis also tracks the execution timestamps as reported by the KV layer, which a future change could [use](https://github.com/cockroachdb/cockroach/issues/92898) for additional validation.

Of note is the updated doc comment, which is reproduced below in entirety.

Fixes #90955.
Fixes #88988.
Fixes #76435.
Fixes #69642.

----

Package kvnemesis exercises the KV API with random concurrent traffic (as
well as splits, merges, etc) and then validates that the observed behaviors
are serializable.

It does so in polynomial time based on the techniques used by [Elle] (see in
particular section 4.2.3), using the after-the-fact MVCC history as a record
of truth. It ensures that all write operations embed a unique identifier that
is stored in MVCC history, and can thus identify which of its operations'
mutations are reflected in the database ("recoverability" in Elle parlance).

A run of kvnemesis proceeds as follows.

First, a Generator is instantiated. It can create, upon request, a sequence
in which each element is a random Operation. Operations that are mutations
(i.e. not pure reads) are assigned a unique kvnemesisutil.Seq which will be
stored alongside the MVCC data written by the Operation.

A pool of worker threads concurrently generates Operations and executes them
against a CockroachDB cluster. Some of these Operations may
succeed, some may fail, and for some of them an ambiguous result may be
encountered.
Alongside this random traffic, kvnemesis maintains a RangeFeed that ingests
the MVCC history. This creates a "carbon copy" of the MVCC history.

All of these workers wind down once they have in aggregate completed a
configured number of steps.

Next, kvnemesis validates that the Operations that were executed and the
results they saw match the MVCC history, i.e. checks for Serializability. In
general, this is an NP-hard problem[^1], but the use of unique sequence
numbers (kvnemesisutil.Seq) makes it tractable, as each mutation in the MVCC
keyspace uniquely identifies the Operation that must have written the value.

We make use of this property as follows. First, the Validate method iterates
through all Operations performed and, for each, inspects

- the type of the Operation (i.e. Put, Delete, Get, ...),
- the (point or range) key of the operation, and
- its results (i.e. whether there was an error or which key-value pairs were returned).

Each atomic unit (i.e. individual non-transactional operation, or batch of
non-transactional operations, or transaction) results in a slice (in order
in which the Operations within executed[^2]) of observations, where each
element is either an observed read or an observed write.

For example, a Batch that first writes `v1` to `k1`, then scans `[k1-k3)`
(reading its own write as well as some other key k2 with value v2) and then
deletes `k3` would generate the following slice:

       [
         observedWrite(k1->v1),
         observedScan(k1->v1, k2->v2),
         observedWrite(k3->v3),
       ]

Each such slice (i.e. atomic unit) will then be compared to the MVCC history.
For all units that succeeded, their writes must match up with versions in
the MVCC history, and this matching is trivial thanks to unique values
(including for deletions, since we embed the kvnemesisutil.Seq in the value),
and in particular a single write will entirely fix the MVCC timestamp at
which the atomic unit must have executed.

For each read (i.e. get or scan), we compute at which time intervals each
read would have been valid. For example, if the MVCC history for a key `k1`
is as follows:

                  k1

       	 -----------------
       	 t5      v2
       	 t4
       	 t3
       	 t2     <del>
       	 t1      v1

then

  - observedGet(k1->v1)  is valid for [t1,t2),
  - observedGet(k1->nil) is valid for [0,t1) and [t2,t5), and
  - observedGet(k1->v2)  is valid for [t5,inf).

By intersecting the time intervals for each Operation in an atomic unit, we
then get the MVCC timestamps at which this Operation would have observed what
it ended up observing. If this intersection is empty, serializability must have
been violated.

In the error case, kvnemesis verifies that no part of the Operation became visible.
For ambiguous results, kvnemesis requires that either no Operation become visible,
or otherwise treats the atomic unit as committed.

The KV API also has the capability to return the actual execution timestamp directly
with responses. At the time of writing, kvnemesis does verify that it does do this
reliably, but it does not verify that the execution timestamp is contained in the
intersection of time intervals obtained from inspecting MVCC history[^3].

[Elle]: https://arxiv.org/pdf/2003.10554.pdf
[^1]: https://dl.acm.org/doi/10.1145/322154.322158
[^2]: there is currently concurrency within the atomic unit in kvnemesis. It
could in theory carry out multiple reads concurrently while not also writing,
such as DistSQL does, but this is not implemented today. See:
https://github.com/cockroachdb/cockroach/issues/64825
[^3]: tracked in https://github.com/cockroachdb/cockroach/issues/92898.

Epic: none
Release note: None

---
## [Firecharge123/cmss13](https://github.com/Firecharge123/cmss13)@[d7c05a7165...](https://github.com/Firecharge123/cmss13/commit/d7c05a71658b5b7f5312c6a0ec9947f59b307b60)
#### Tuesday 2023-03-07 18:45:52 by carlarctg

Aimed shot and spotting now have laser beams. (#1905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Aiming a shot on a sniper rifle now adds a red laser beam that connects
the target and the aimer. Spotting designators will emanate a faint
yellow one. Both will slowly increase in alpha from 0 to max as the
tracking progresses.

The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Stepping through laser beams will check for eye protection, if it isn't
sufficient, and the small probability chance passes, the target will
scream in pain! Completely flavor. If they have enough eye protection,
it will bounce off their headgear, and if said protection is BiMex
patented personal shades it will create a cool visual effect.

Refactored eye_protection to have three levels, flavor, flashes, and
welding. Sunglasses have flavor protection, sechuds have flash
protection, welding gear has welding protection.

The spotter's designator now has a white band on it to distinguish it
from the rest.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.

The primary reason for this addition is because it looks sick as FUCK.
The secondary one is to help xenos see where they're being shot from.

> The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Makes sense, cloaked sniper/spotters shouldn't be made completely
useless due to the beam. It makes sense for the laser to reduce aim time
and it isn't a pain for xenomorphs to deal with as they know exactly
where it is coming from and where they can run for cover (And other
xenos can protect them better)

> Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

It made no sense for sniper reticles to be blue. Red is danger, yellow
is warning, blue is.... good? Additionally, since both reticles for
spotting and aiming were nigh-identical, it caused quite the amount of
confusion. I've tested it myself, you can spook away xenos with only
spotting because they think it's the aimed shot reticle.

> The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Look, I know what I just said makes this sound stupid. But I think it
makes a lot of sense for the dangerous high-tech sniper rifles to have
stronger blue lasers, it just feels like a 'strong sci fi laser' color.
Like the pulse rifle in base ss13, it looks similar to the disabler but
you don't see anyone complaining. The base sniper reticle being red is
enough for people to realize this is a more dangerous version anyways.

> Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.

Cool flavor. Also lore-accurate!

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>


Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>

https://streamable.com/kyprhl

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

:cl:
add: Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.
bal: The sniper's laser beam can be disabled with a button, but keeping
it enabled reduces aiming shot time. Cloaked spotters will not cause a
beam to appear.
imageadd: Completely resprited the indicators for spotting (it's now
yellow) and aiming (it's now red, usually)
imageadd: The XM42B and PMC sniper rifles have more intense blue lasers
and reticles.
add: Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.
refactor: Refactored eye_protection to have three levels, flavor,
flashes, and welding. Sunglasses have flavor protection, sechuds have
flash protection, welding gear has welding protection.
imageadd: The spotter's designator now has a white band on it to
distinguish it from the rest.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: harryob <me@harryob.live>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[199d239375...](https://github.com/git-for-windows/git/commit/199d239375ce8123c62923cbb983da834a170697)
#### Tuesday 2023-03-07 19:04:40 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b7b5c3075e...](https://github.com/mrakgr/The-Spiral-Language/commit/b7b5c3075ebc8b72b1a8643643da04abd3c61ca4)
#### Tuesday 2023-03-07 19:11:59 by Marko Grdinić

":35am. I am up. I slept well tonight, I think. Any mail? Not really.

I see that the mic still hasn't been handed over to the delivery service, but it is still early in the morning today.

7:40am. Today I want to take a break. Let me do some reading, then I will take a bath.

Rosen Garten and Kakeru are out, and I have to catch up with the Eiyu thread and watch the anime.

8am. Let me watch Inglis' anime. I need to take it easy. After going at it full tilt, I do not feel like going at it strong today. I really should reserve a day or two just for fun. Though I will do some programming later today.

9:05am. I've chilled. Next is to start getting ready for that bath. Only after that will I do some programming.

https://boards.4channel.org/g/thread/91932922/twg-tech-workers-general

> Read the sticky and make your resume just like it says. Each work experience job should be summed up into a single informative line, and use https://resumake.io/ to make your resume spiffy and scrapable to recruiters. Then put that resume onto indeed (you don't need to convert it to indeed's format just add the pdf) and LinkedIn, and in a few days or weeks at most you'll be getting Indians calling you and e-mailing you for contract work in your local area.

I'll try it later.

https://www.careercup.com/resume
> This is what a good resume looks like.

https://resumake.io/

///

>>91933616
Lots and lots of people lie on their resume, it's very common for newgrads. Fluff, "C++/C", "I ran my own startup" (Made $0, never attempted to make money anyway), worked at McDonald's? Don't list the title, imply it's IT at McDonalds, etc.
Newgrads are between a rock and a hard place. On one side, you have to get past those resume filters and HR retards, made worse by the fact that ALL your competition is lying 10x the amount you probably are, making you look bad in comparison, but on the other, once you get past them, then you have to get through the actual tech guy that's interviewing you, and he will pick through that bullshit so easily and embarrass you. So it's a balancing act. Don't sell yourself too short as to not get through HR, but don't put C++ on your resume because you had to write a Hello World for it in college one time.

///

This is from a recent thread.

9:20am. Let me take a bath here. It is time for that. Then I'll start moving to programming. Or I can watch that Reaper course. Whatever I feel like. I really want the mic to get here.

10:10am. Let me start work for the day. Here is what I am going to do. I am going to move the setup videos to a separate playlist. Then I am going to unlist some of the vids. Actually, delete them entirely. I am going to be redoing the intro and the minimal UI anyway once the mic gets here. After that, let me make a new resume.

10:25am. I moved the 3 important setup videos to their own playlist and unlinked them.

The Leduc intro on the other hand I will redo, but I'll leave them there for now.

Now, what I want to do is make a resume.

https://resumake.io/

I've done this a lot but...

You know what, let me not do it. As much as I want Indian recruiters to treat me like some hot piece of ass, it would just waste my time. What I should it face the torment. Do the damn projects. Then go into it properly. 4 years of work at at research focused startup called Rajnet, and 2 years at my father's company called Stag. After that I'll aim for mid and senior positions.

Now...let me get started. Just for a bit. Let me start Rider.

Ok, I have the project from yesterday there. What else should I do, but put in the game?

Yeah, it is time for that.

Those projects that I did in 2021? It is finally time to revisit them.

PS C:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests> dotnet "c:\Users\Marko\.vscode\extensions\mrakgr.spiral-lang-vscode-2.3.10\compiler\Spiral.dll" port=13805
Server bound to: tcp://*:13805 & tcp://*:13806

Sigh, just sigh. Note how I am using two ports for essentially no reason. Now that I have some skills, I'll really want to update my methods, but nevermind that for now.

```spiral
// Since the past attempts failed, I am going to try something else here. Inspired by the
// signSGN papers, for the optimizer I am going to make an update that interpolates
// signSGD + infinity norm gradient normalization. For the value network, since I absolutely
// need the values to act as weighted moving averages, I am going to semi-tabular CFR in the
// value head.

// Instead of one hot vectors like in full tabular, the semi tabular will have probabilistic
// vectors. I'll take a log softmax over the body, exp it and use that as the prob vector input
// to the head which be optimized using the tabular algorithm.

// For getting the gradients for the value body, I'll use the absolute value differential
// between the given and the predicted error, center it with regards to the probabilistic mean
// and use that as the backwards input for the log softmax.
// (Edit: As it turns out, the regular softmax works a lot better. I was worrying that saturation
// would be an issue, but that property actually makes convergence possible.)

// Alternatively updating the value head and body will make this an EM procedure similar to k-means.
// The main reason why I am going for this besides being able to weight the values is because
// right now I can't tell at all whether the value update works. If I had a tabular agent, this
// kind of debugging would be a lot easier.

// The issue with the value net is that it needs to learn the reward magnitudes in the weights,
// so I cannot use something like signSGD (which is Adam with full batch learning) to stabilize it.
// This is a source of many of my headaches. NNs are good for probability distributions, but bad
// for learning large ranges of values.

// With this method I'll be able to optimize the value head and get something useful even without
// necessarily optimizing the body if I want to pick that route. (Edit: Much like for the actor,
// optimizing the critic body using the targets generated by the tabular algorithm works fine.)

// The actor on the other hand will be will be possible to deal with as I will be able to use policy
// gradients with the aforementioned optimizer together.

// ---

// Update (6/9/2021): My worked and I am capable of training a NN agent competitive with the tabular
// one with roughly the same amount of compute. The NN algo itself is implemented in `control.py`.

// Some details:
// * Even though the optimizer supports interpolation, I've ditched infinity norm in favor of pure signSGD.
//   I might add a momentum component to signSGD in the future, but otherwise I won't bother with adaptive
//   optimizers like Adam. They all converge to signSGD when doing full batch learning anyway.
//   In future work, I think I'll just tune the batch size until signSGD is happy.
// * Averaging in the weight space is sufficient for dampening self play oscilations and getting good policies.
//   Thanks to it I did not have to gradually lower the learning rate or anneal the exploration epsilon.
//   I did observe a benefit when I lowered the actor LR by 2x, so it should be possible to get better
//   performance by doing LR annealing even with averaging.

// I am quite pleased with how things went here. I'll archive this project and move on to making
// the Holdem game next. The algorithm here is novel and deserves a blog post at some point, though I
// won't bother writing a paper as I am not into theorems.

// I am looking forward to trying it out on games that could give me real world advantages.

// Update (6/18/2021): Did some updating and cleaning up. As it turns out, I was looking the
// regular players instead of the averaged ones and drawing the right conclussions from the
// wrong data. I am lucky that what I wrote in the relevant bullet about weight averaging point
// is all true.

// The commit at this date has data on what my runs look like. I've been training agents over and
// over for the whole day. The only activations worth using with LN are Relu and Leaky Relu.
// I tried a few others, but probably because of poor weight init they saturate too easily and
// work very poorly. Relu composes with LN particularly well, and it will be my main choice. Relu,
// Leaky Relu (and `abs` which I haven't tried) when paired with LN and signSGD have the property
// of making gradient steps invariant to the weight scale.

// The algorithm in `control.py` preserves that property when the goal is to learn value functions.

// Update (6/22/2021): As it turns out updating the critic, actor and the critic head all at once
// improves computation time by 4x without degrading the final performance. I am impressed.
// Compared to the `Actor-Critic Policy Optimization in Partially Observable Multiagent Environments`
// paper, my method here gives better final performance while being over a 100 times faster to train.
// In that paper they update the critic 128 times before updating the actor once.

// I haven't bothered testing this until now, but since I am preping for Holdem, I realized that
// I really should since if it worked, it could reduce the time it takes to train an agent from a
// month to a week. One hyperparam I still haven't bothered tuning at all is the head decay.

// A batch of 1024 is enough to cover all of the Leduc's states so I haven't bothered, but for Holdem
// and bigger games 2 ** -2 might be too strong of a decay.

// Update (6/27/2021): Testing the architecture here on Holdem made me realize it is absolute garbage
// at optimizing the value function. On flop poker vs callbot, it cannot learn a thing. The only reason
// it works on Leduc at all because the game is so small. Not just the NN architecture, I changed the
// the `belief_tabulate` and `model_evaluate` functions significantly as well. Adding momentum to
// signSGD helps significantly as well. (Edit: I tried it on Leduc and it works far worse than vanilla.
// What a disappointment, it seems it only helps vs static players.)

// Due to all the changes I would not recommend using this project as a reference, I have a lot better
// stuff in ui_holdem2. There is an updated Leduc test there. That having said, it takes a very large
// number of iterations to become competent at hand reading. There might be even better architectures
// out there; I get the sense that vanilla nets are not the right thing for the job.

packages: |core2-
modules:
    serialization/
        dense/
            array
        sparse/
            int
    utils-
    sampling
    nodes-
    leduc
    train
    agent/
        uniform
        neural
        tabular_old
        tabular
    create_args
```

Look at the comments in the final ui-leduc spiproj file. It is broken as I no longer even have core2. But this stuff is a blast from the past. I put in so much passion into it.

```spiral
// I could not finish it by adding the hindsight information. That having said, the challenge of making the value function
// trainable has been dealt with. Now I just need to find a way to train the policy. I have the same issue as last time
// where the agent converges to an aggrodonk. Given the small batch sizes, the optimization process is simply too unstable.

// The way I will defeat this challenge is by having the net train against static copies of itself. Not just a single static
// copy, but multiple past iterations. I tried this before while trying the Flop agent, and it did not work better than regular
// self play, but that was a special case. Holdem is large enough that the stability benefits of making the enviroment
// stable are needed.

// The minimax optimization that is going on here needs stable and careful steps. Leduc works because it is small, and Flop
// worked because it had short sequences and MC. Hodlem is beyond the threeshold where such tricks would be applicable.

packages: |core-
modules:
    types-
    conv-
    serialization/
        dense/
            array
        sparse/
            int
    utils-
    sampling
    nodes-
    train
    train_cat
    hand_scorer
    hu_holdem
    leduc
    agent/
        uniform
        holdem_callbot
        tabular
        neural_leduc
        neural_holdem
    create_args_leduc
    create_args_holdem
```

This is from the final `ui_holdem` project. Since it uses the regular core, it at least typechecks properly.

11am.

```spl
union rec node state obs (actions : * -> *) act =
    | Terminal : pl2 obs act * state * r2
    | Action : pl2 obs act * state * pid * actions act * (log_prob * act -> node state obs actions act)
```

Hmmm, I was returning nodes instead of CPSing it like I thought I was.

Eh, the thing is really abstract.

```spl
inl belief_tabulate slots (action_indices : a u64 st) (at_action_value : a u64 f32) (at_action_weight : a u64 f32) =
    inl update_head () =
        am.iter4 (fun {policy head={weighted_value weight}} i_action at_action_value at_action_weight =>
            inl add_to l v = inl x = index l i_action in set l i_action (x + v)
            add_to weighted_value (at_action_value * at_action_weight) . add_to weight at_action_weight
            ) slots action_indices at_action_value at_action_weight
    inl action_fun (action_probs : a u64 (a st f32)) (sample_probs : a u64 (a st f32)) =
        inl batch_qs =
            am.map4 (fun {policy head={weighted_value weight}} i_action sample_prob r =>
                am.mapi2 (fun i_action' weighted_value weight =>
                    inl q = if weight <> 0 then weighted_value / weight else 0
                    if i_action = i_action' then (r - q) / (index sample_prob i_action) + q else q
                    ) weighted_value weight
                ) slots action_indices sample_probs at_action_value
        inl rewards = am.map2 (am.fold2 (fun s a b => s + a * b) 0) batch_qs action_probs
        inl update_policy () =
            am.iter4 (fun {policy={current grad} head} qs mean regret_prob =>
                am.mapInplace (fun i grad => grad + regret_prob * (index qs i - mean)) grad
                ) slots batch_qs rewards at_action_weight
        rewards, update_policy
    update_head, action_fun
```

Back then I understood this quite well, but now...

11:15am. I am looking at the past code and thinking.

It really has been a while since I've done real programming.

12:15pm. Breakfast time.

12:50pm. I had time to think about how I am going to do this. After glancing at the old code, I realized all the game implementations are intervowen with the sampling stuff. I am definitely going to put some effort into decoupling them.

I'll redo both games in F#. That will be my next goal. I'll use the MVU pattern for it instead of a recursive function block like I am doing now.

https://headcanontl.wordpress.com/2023/02/27/savage-fang-vol-2-c6/

Let me catch up with Savage Fang, then I will do the chores. Then I will do some actual programming. Today is pretty chill.

12:55pm. Every day should be chill like this. What is the point in exerting myself? I've more or less reached the apex of my programming at this point. What I will do next is bring it all together under the umbrella of web development.

A project like this will in some way be culmination of all my experience. Many different languages and backends, all seamlessly integrated into a single system. What is not to like?

1:10pm. Though it is not correct to say that I've reached the apex. Aren't I still learning?

And isn't what I am going to do here a step up from what I had before?

1:25pm. Ok, let's go do the chores. Then I will redo the Leduc game the way it should be done.

1:55pm. Done with chores.

Ok, let me just do it. Let me implement Leduc in F#. I am just going to change the architecture of the old game a little and port it from Spiral to F#. That will ensure it is decoupled.

```spl
union action = Fold | Call | Raise
union card = King | Queen | Jack

type player = {card : card; id : u8; pot : i32}
type players = player * player
nominal leduc_state = player * player * bool * card
nominal leduc_actions act = { is_fold : bool; is_raise : bool }
type actions = leduc_actions action

inl compare_hands (community_card : card) (p1,p2 : players) =
    let tag = function King => 2i32 | Queen => 1 | Jack => 0
    inl community_card = tag community_card
    inl a = tag p1.card, community_card
    inl b = tag p2.card, community_card
    inl is_pair (a,b) = a = b
    if is_pair a && is_pair b then comp (fst a) (fst b)
    elif is_pair a then gt()
    elif is_pair b then lt()
    else
        inl order (a,b) = if a > b then a,b else b,a
        inl a,b = order a, order b
        inl x = comp (fst a) (fst b)
        if eq_is x then comp (snd a) (snd b) else x

inl raiseBy amount (p1,p2 : players) = p2.pot + amount

inl game() =
    inl deck = a ;[King; Queen; Jack; King; Queen; Jack]
    $"numpy.random.shuffle(!deck)"

    inl pot = 1i32
    inl id = 0u8
    draw deck fun (card, deck : card * a u64 card) =>
    notify (Some id) card fun _ =>
    inl p1 = {card id pot}

    inl id = 1u8
    draw deck fun card, deck =>
    notify (Some id) card fun _ =>
    inl p2 = {card id pot}

    sample deck fun community_card =>

    inl action (p1,p2,is_show_community_card) = action (leduc_state (p1,p2,is_show_community_card,community_card))
    inl terminal ((p1 : player),(p2 : player),is_show_community_card) (i,r) =
        inl r = if i = 0 then r else -r
        inl p1,p2 =
            inl p (x : player) = {x with pot#=(+) (if x.id = 0 then r else -r)}
            inl p1, p2 = p p1, p p2
            if p1.id = 0 then p1,p2 else p2,p1
        terminal (leduc_state (p1,p2,is_show_community_card,community_card)) (r2 (f32 r))

    let actions_from_state (p1,p2 : players) (raises_left : i32) : actions =
        leduc_actions {is_fold = p1.pot <> p2.pot; is_raise = 0 < raises_left}

    inl rec round_two ~(raises_left : i32) ~(p1,p2 : players) =
        inl s = p1,p2,true
        action s p1.id (actions_from_state (p1,p2) raises_left) function
        | Fold => terminal s (p2.id, p1.pot)
        | Call =>
            inl p1 = {p1 with pot=p2.pot}
            inl s = p1,p2,true
            let x = compare_hands community_card (p1,p2)
            terminal s if gt_is x then p1.id, p2.pot elif lt_is x then p2.id, p1.pot else p1.id, 0i32
        | Raise => round_two (raises_left-1) (p2,{p1 with pot=raiseBy 4 (p1,p2)})
    inl round_two_init ~(p1,p2 : players) =
        notify None community_card fun _ =>
        action (p1,p2,true) p1.id (actions_from_state (p1,p2) 2) function
        | Fold => failwith "impossible 2"
        | Call => round_two 2 (p2,p1)
        | Raise => round_two 1 (p2,{p1 with pot=raiseBy 4 (p1,p2)})
    inl rec round_one ~(raises_left : i32) ~(p1,p2 : players) =
        inl s = p1,p2,false
        action s p1.id (actions_from_state (p1,p2) raises_left) function
        | Fold => terminal s (p2.id, p1.pot)
        | Call =>
            inl p1 = {p1 with pot=p2.pot}
            round_two_init (if p1.id = 0 then p1,p2 else p2,p1)
        | Raise => round_one (raises_left-1) (p2,{p1 with pot=raiseBy 2 (p1,p2)})

    action (p1,p2,false) p1.id (actions_from_state (p1,p2) 2) function
    | Fold => failwith "impossible 1"
    | Call => round_one 2 (p2,p1)
    | Raise => round_one 1 (p2,{p1 with pot=raiseBy 2 (p1,p2)})

let game x = game () x
```

this is the entire game in Spiral. But it is coupled to what exists elsewhere. I have no idea why I let something like this pass last time.

```
union action = Fold | Call | Raise
union card = King | Queen | Jack

type player = {card : card; id : u8; pot : i32}
type players = player * player
nominal leduc_state = player * player * bool * card
nominal leduc_actions act = { is_fold : bool; is_raise : bool }
type actions = leduc_actions action
```

Sigh, what the hell is all this shit. I was crazy to do it like this. MVU. Model - View - Update. That is the pattern that I should be using in the face of concurrency.

```
action (p1,p2,false) p1.id (actions_from_state (p1,p2) 2) function
```

Passing in p1,p2 twice. This is cringe.

2:15pm. This whole thing isn't bad, but the fact that it is not isolated is making me cringe.

Web dev is looked down on, but maybe it is just the right punishment for me for writing such tightly coupled code.

```fs
type Action = Fold | Call | Raise
type Card = King | Queen | Jack
type Player = { card : Card; id : uint8; pot : int32 }
type Model = { p1 : Player; p2 :Player;  table_card : Card ValueOption }
type SelectableActionsDescriptor = { is_fold : bool; is_raise : bool }
```

This should be the game state.

https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bitoperations.popcount?view=net-7.0

I need to make the sampling functions. Let me break out the intrinsics.

```
let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(uint64 target, mask)
```

Damn, now I have to figure out how the parallel bit deposit works. I am not sure if this will even work on the cloud CPU or the Tenstorrent card in the future.

Let me skip this. I'll just make the regular loop. At least popcnt I can expect to be present on future devices. Who knows about

...

Actually, the thought of how to make this work occured to me.

3:10pm.

```fs
open System

let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< target, ~~~mask)

let mask_bit i = 1UL <<< i

[|
for i=0 to 99 do
    yield (int (sample [|1;2;3;4;5|] (mask_bit 0 ||| mask_bit 1)))
|]
|> Array.groupBy id
|> Array.map (fun (a,b) -> a, b.Length)
|> Array.sortBy fst
```

I am playing with this in Rider. It works very nicely. Now if only I could turn that pow2 index back into the regular thing.

3:20pm.

```fs
open System

let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< target, ~~~mask)
    |> Numerics.BitOperations.TrailingZeroCount

let mask_bit i = 1UL <<< i

[|
for i=0 to 99 do
    yield (int (sample [|1;2;3;4;5|] (mask_bit 1 ||| mask_bit 2)))
|]
|> Array.groupBy id
|> Array.map (fun (a,b) -> a, b.Length)
|> Array.sortBy fst
```

Let me just go with this for now. It is not supported on the cloud, I'll implement a hand written method.

```fs
let parallel_bit_deposit_u64 value mask =
    let rec loop s i c =
        if i < 64 then
            let i' = 1UL <<< i
            if i' &&& mask <> 0UL then loop (s ||| ((i' &&& value) >>> c)) (i+1) c
            else loop s (i+1) (c+1)
        else s

    loop 0UL 0 0
```

I just had to do it now. Is this correct? Let me give it a try.

3:35pm.

```fs
let parallel_bit_deposit_u64 (value, mask) =
    let rec loop s i c =
        if i < 64 then
            let i' = 1UL <<< i
            if i' &&& mask <> 0UL then loop (s ||| ((i' &&& value) >>> c)) (i+1) c
            else loop s (i+1) (c+1)
        else s

    loop 0UL 0 0

let t =(15UL, ~~~1UL)
let q = parallel_bit_deposit_u64 t
let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
```

Now comes the debugging. I did everything wrong.

3:50pm.

```fs
open System

let parallel_bit_deposit_u64 (value, mask) =
    let rec loop s i c =
        if i+c < 64 then
            if (1UL <<< (i+c)) &&& mask <> 0UL then loop (s ||| (((1UL <<< i) &&& value) <<< c)) (i+1) c
            else loop s i (c+1)
        else s

    loop 0UL 0 0

for i = 1 to 10000000 do
    let f n = Random.Shared.NextInt64(0L,n) |> uint64
    let t = f Int64.MaxValue, f Int64.MaxValue
    let q = parallel_bit_deposit_u64 t
    let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
    if q <> w then failwith "q <> w"
```

This test passes, so I am decently sure I got it right.

```fs
let parallel_bit_deposit_u64' (value, mask) =
    let rec loop s i c =
        if i+c < 64 then
            if (1UL <<< (i+c)) &&& mask <> 0UL then loop (s ||| (((1UL <<< i) &&& value) <<< c)) (i+1) c
            else loop s i (c+1)
        else s

    loop 0UL 0 0

let parallel_bit_deposit_u64 (value, mask) =
    let mutable s = 0UL
    let mutable i = 0
    let mutable c = 0
    while i+c < 64 do
        if (1UL <<< (i+c)) &&& mask <> 0UL then
            s <- s ||| (((1UL <<< i) &&& value) <<< c)
            i <- i + 1
        else
            c <- c + 1
    s

let f n = Random.Shared.NextInt64(0L,n) |> uint64
#time "on"
for i = 1 to 10_000_000 do
    let q = parallel_bit_deposit_u64 (0UL, 0UL)
    // let t = f Int64.MaxValue, f Int64.MaxValue
    // let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
    // if q <> w then failwith "q <> w"
    ()
#time "off"
```

By far, generating the two random numbers takes the most time. Weirdly enough, the functional tail call function is twice as fast as the imperative version for some reason.

4:15pm.

```fs
/// Samples an action from an array.
let sample (actions : 'action []) (mask : uint64) =
    let i =
        let popcnt = Numerics.BitOperations.PopCount mask
        let i = Random.Shared.Next(0, actions.Length - popcnt)
        if Runtime.Intrinsics.X86.Bmi2.IsSupported then
            Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< i, ~~~mask)
        else
            parallel_bit_deposit_u64 (1UL <<< i, ~~~mask)
        |> Numerics.BitOperations.TrailingZeroCount
    actions[i], mask ||| (1UL <<< i)

let mask_bit i = 1UL <<< i
let ar = [|1;2;3;4;5|]

let result =
    [|
        for i=0 to 999 do
            yield [|
                let mutable mask = 0UL
                for _ in ar do
                    let action, mask' = sample ar mask
                    mask <- mask'
                    yield action
            |]
    |]

result |> Array.forall (fun x -> Array.distinct x = x)
```

This works perfectly. I've tested the sampling function to death.

4:45pm.

```fs
module Game

type Action = Fold | Call | Raise
type Card = King | Queen | Jack
type Player = { card : Card; id : uint8; pot : int32 }
type Model = { p1 : Player; p2 :Player; raises_left : int; table_card : Card ValueOption; mask_desk : uint64 }
type ActionPicker = { is_fold : bool; is_raise : bool }
type RewardForPlayerOne = float32

let compare_hands (community_card : Card) (p1 : Player, p2 : Player) =
    let tag = function King -> 2 | Queen -> 1 | Jack -> 0
    let community_card = tag community_card
    let a = tag p1.card, community_card
    let b = tag p2.card, community_card
    let is_pair (a,b) = a = b
    if is_pair a && is_pair b then compare (fst a) (fst b)
    elif is_pair a then 1
    elif is_pair b then -1
    else
        let order (a,b) = if a > b then a,b else b,a
        compare (order a) (order b)

let raiseBy amount (p1 : Player, p2 : Player) = p2.pot + amount

let deck = [|King; King; Queen; Queen; Jack; Jack|]
let sample_card mask = Sampler.sample deck mask

let init () : Model * (ActionPicker * RewardForPlayerOne) =
    let mask = 0UL
    let c,mask = sample_card mask
    let p1 : Player = {id=0uy; card=c; pot=1}
    let c,mask = sample_card mask
    let p2 : Player = {id=1uy; card=c; pot=1}
    {p1=p1; p2=p2; raises_left=2; table_card=ValueNone; mask_desk=mask}, ({is_fold=false; is_raise=true}, 0.0f)
```

Here is the initial part so far.

Let me do the update next.

```fs
let init () : Model * (ActionPicker * RewardForPlayerOne) =
    let mask = 0UL
    let c,mask = sample_card mask
    let p1 : Player = {id=0uy; card=c; pot=1}
    let c,mask = sample_card mask
    let p2 : Player = {id=1uy; card=c; pot=1}
    {p1=p1; p2=p2; raises_left=2; table_card=ValueNone; mask_desk=mask}, ({is_fold=false; is_raise=true}, 0.0f)

let update (model : Model) (msg : Action) =
    match msg with
    | Fold ->
        failwith "TODO"
    | Call ->
        failwith "TODO"
    | Raise ->
        failwith "TODO"
```

This is so lame. Instead of that action picker, I can just derive the list from state.

5pm.

```fs
type ActionPicker = { is_fold : bool; is_call : bool; is_raise : bool }
let actions_allowed (model : Model option) =
    match model with
    | Some model -> {is_fold=model.p1.pot <> model.p2.pot; is_call=true; is_raise=model.raises_left > 0}
    | None -> {is_fold=false; is_call=false; is_raise=false}

let actions_array (x : ActionPicker) = [|
    if x.is_fold then Fold
    if x.is_call then Call
    if x.is_raise then Raise
|]
```

I'll move it to a different file later.

Actually instead of this, I really should be using masks.

https://stackoverflow.com/questions/38938911/portable-efficient-alternative-to-pdep-without-using-bmi2

Agh, I should have just transcribed this.

6:25pm. This is ridiculous. I am deep in thought, thinking about the design of Leduc.

6:35pm. Both the way I did it last time, and the way I wanted to push into this time is bonkers.

There is no way the MVU pattern is the right choice. There is no way that what I had is the right choice.

Instead, what I need to do is take in the `game` and pass it an interface with the `choice`, `action`, and `terminal` members. I need to CPS it. That would be an efficient design I could use on AI chips in the future.

But what I've realized is, that this interface would be native to this particular game.

In order to make it usable in learning algorithms, what I would do is compose that game native interface in something else that I could pass to generic learning algorithms.

I can see a hierarchy.

What I've done in `ui_holdem` is squish it all together.

Agh, what was I thinking?

7:05pm. Ok, I think I get everything. I am going to deal with Leduc tomorrow.

I see how I am going to do the learning algorithms as well.

game -> lrn -> game -> lrn

There is a mutually recursive relationship where the game interface calls the learning interface and so on.

7:10pm. Let me go get lunch.

I have a feeling in the abstract for how it should work, but the feeling eludes me. I get the feeling that I knew all of this, but it faded from my memory. I'll figure it out as I go into it.

Remember how long and hard I thought about CPS and recursion? Remember the Y combinators and how hard I found them?

I have that power and understanding. I am sure that the knowledge will come back to me when the time is right to make use of it.

8:10pm. Let me close. I didn't exactly do too much today. Tomorrow, I am going to deal with the game, unless the mic arrives.

...The parcel is still not in the system. I guess it won't get here anytime soon then.

Let me chill. I'll give Succubus & Hitman a try."

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[89ac5ea431...](https://github.com/shiptest-ss13/Shiptest/commit/89ac5ea431cec77f5c7243204eefadfca4c74a18)
#### Tuesday 2023-03-07 19:37:41 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Mjoonlight/MythosOfMoonlight](https://github.com/Mjoonlight/MythosOfMoonlight)@[bc25497baa...](https://github.com/Mjoonlight/MythosOfMoonlight/commit/bc25497baa4dcad276ce075f03ce6f91a32b34d3)
#### Tuesday 2023-03-07 19:45:26 by Ebon1

1In the beginning God created the heaven and the earth.
2And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
3And God said, Let there be light: and there was light.
4And God saw the light, and it was good; and God divided the light from the darkness.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[946a305a6d...](https://github.com/treckstar/yolo-octo-hipster/commit/946a305a6da5157875204d7024d97bc5244cd1c2)
#### Tuesday 2023-03-07 20:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [YarataDarkness/Abdanor-Daniel-airflight](https://github.com/YarataDarkness/Abdanor-Daniel-airflight)@[e6f163bd5c...](https://github.com/YarataDarkness/Abdanor-Daniel-airflight/commit/e6f163bd5cc44f8164c2a877beffaab7f6a07999)
#### Tuesday 2023-03-07 20:44:11 by Yarata

this time im really going to do it

If i dont get the delusional praise and glory I want like a petty child im really going to do it. it pretty easy. an easy liquid. an easy pill. Im going to do it. A rope? Garage. You think it funny? huh? it a pretty funny copypasta huh? unitl it happens then youll pretend to have empathy dipshit. aaaaaaaaaah

---
## [YarataDarkness/Abdanor-Daniel-airflight](https://github.com/YarataDarkness/Abdanor-Daniel-airflight)@[47dc6a2fc7...](https://github.com/YarataDarkness/Abdanor-Daniel-airflight/commit/47dc6a2fc7847c90ad4c627b6ad11e8466f6cffb)
#### Tuesday 2023-03-07 21:09:28 by Yarata

favourite things i like

a lot of poke games(3DS ERA >>>>>>>>> ANY OTHER ERA SHUT UP DS FANS SHIT NEEDED 3RD VERSION IN ORDER TO BE DECENT WITH HORRID PACING STILL GOOD BUT FUCK MAN GET A GRIP YOU BLIND BITCH

Digimon dusk n dawn>>>>>>digimon would be better if they hummm put the hummm made the thing with the digimans I WANTED tehher

Twst LILIA VANROUGE AAAAA

Yu-gi-oh; Yami Bakura is so cool I hope he jumps off a building lolololo I wanna look like him teherr

bakugan battle brawlers for the ds
shut the fuck up heartgold simpsuckers you buncha lynches with no bitches to suck by

watchmen(I love the colors and the paneling)

beyblade metal kills poeple that sooo cool

Dragon super manga (actually my favourite is the dragon ball manga(i love the master roshi fight) dbz was weird to me i dunno why. I like the fight in dbs(manga)

the forsaken in WoW

batman vs dracula(both the comic and the random kino aniamted movie)

plushiesssss

vocaloidssssss

touhou (yuuka and flandre are my favvvv)

my cat erina

viziepop character designs

angel dust(the spider)

the dark god(but he doesnt like me back i think :(

cats

bakingbacons(youtube channel that does food stuff)

Girl A

Ruruchan suicide show

bunny sona

when poeple I dont like DIE in a really PATHETIC and STUPID way lolll >_<

sailor mmon kid(chibiusa? i think? She such a sad character! just like mefrfrfr)

Neferpitou from hxh

dragons

snakes

spiders

there nprobably more but hummmmmm that it i think? ((ε(*⌒▽⌒)†*ﾟ¨ﾟﾟ･*
Arent i so interesting? huhh???
✧♡
   /ᐢ⑅ᐢ\   ♡   ₊˚
꒰ ˶• ༝ •˶꒱       ♡‧₊˚    ♡
./づ~ :¨·.·¨:     ₊˚
           `·..·‘    ₊˚   ♡

---
## [hyperlane-xyz/hyperlane-monorepo](https://github.com/hyperlane-xyz/hyperlane-monorepo)@[59a90b1bb6...](https://github.com/hyperlane-xyz/hyperlane-monorepo/commit/59a90b1bb63106d9dd7fa640b17772096073dfb8)
#### Tuesday 2023-03-07 21:42:41 by Trevor Porter

Default to not allowing LocalStorage checkpoint syncers in relayer (#1900)

### Description

Open to better names

Adds a setting to the relayer, `allow_local_checkpoint_syncers`, which
determines whether local storage based checkpoint syncers will be
allowed by the metadata builder.

Originally, I wanted something a bit more clever, like being able to
specify `HYP_RELAYER_VALIDCHECKPOINTSYNCERS=LocalStorage,S3` or
something, where I'd like those variants to be matched to the variants
found in
https://github.com/hyperlane-xyz/hyperlane-monorepo/blob/main/rust/hyperlane-base/src/types/checkpoint_syncer.rs#L14.
But that enum requires values, so things get ugly. One option would be
to create a new enum like:
```
enum CheckpointSyncerTypes {
  LocalStorage,
  S3,
}
```
And another option is to use something like strum's
[EnumString](https://docs.rs/strum/latest/strum/derive.EnumString.html)
(shoutout to @mattiecnvr). But this still is a bit clunky, so for now
just making this a bool and we can figure out something more elegant
later if we ever get to a point where we're supporting multiple types of
checkpoint syncers

### Drive-by changes

none

### Related issues

- Fixes https://github.com/hyperlane-xyz/issues/issues/402

### Backward compatibility

_Are these changes backward compatible?_

Yes - although if you ever want to run a relayer that uses local storage
now, you'll need to set `HYP_RELAYER_ALLOWLOCALCHECKPOINTSYNCERS=true`

_Are there any infrastructure implications, e.g. changes that would
prohibit deploying older commits using this infra tooling?_

None - we always expect to not be reading from the local fs in deployed
relayers


### Testing

_What kind of testing have these changes undergone?_

Ran e2e tests

---
## [k6l2/korl](https://github.com/k6l2/korl)@[e512f8b775...](https://github.com/k6l2/korl/commit/e512f8b775829ebd461f9e523d4ad7f6d934dfae)
#### Tuesday 2023-03-07 22:47:16 by Kyle

remove `sort` submodule, add korl-algorithm

as it turns out, this sort library's generic C macro API was causing
build times to explode; locally, this reduces my korl-build times by
like 0.5 seconds on average, which is huge considering my rebuild times
are 1.7ish seconds now

for now, we'll just use the CRT sort function, and honestly it doesn't
bother me too much; the API actually looks cleaner now anyway, in my
opinion at least, and I am not noticing any huge changes to run-time
performance #s

---
## [mdegans/tegrity](https://github.com/mdegans/tegrity)@[d639341449...](https://github.com/mdegans/tegrity/commit/d6393414492fecbb9f7c2f370902563766931811)
#### Tuesday 2023-03-07 22:59:09 by TrellixVulnTeam

Adding tarfile member sanitization to extractall() (#4)

This commit fixes the case where the codebase is changed such that the [hashes used to validate the input archives](https://github.com/mdegans/tegrity/blob/69e85ceeb6ea18414fda82c4c376ba89a41fce93/tegrity/settings.py#L20) somehow aren't checked, and I don't honestly remember if there's a `--option` somewhere to do that (I don't think so), so it's a good idea to fix this.

This isn't believed to be an *immediate* security issue for `tegrity` because other than the rootfs, which the developer would create themselves, all archives are checked against a SHA_512, and if the developer created a compromised rootfs, that developer would already be compromised. It's possible that somebody could be tricked into downloading, say, an emulator image or something, and paste in a bad SHA_512, then sure, the host could be compromised, but I can't think of everything and it's better to patch this anyway.

That, being said, looking at that code, the **kernel is probably ancient** and loaded with vulnerabilities and I should probably flag this project as abandoned. I might resume development on `dev` at some point if there was some money in it, but otherwise, I'll put a `do not use for now`. I made the project mostly because Nvidia didn't support a particular camera at the time officially, and now they do, so I don't need it anymore personally.

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[32c31b8fc0...](https://github.com/CandleJaxx/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Tuesday 2023-03-07 23:10:16 by SkyratBot

[MIRROR] Lighting source refactor (Tiny) [MDB IGNORE] (#19370)

* Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode.
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible.
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

* Lighting source refactor (Tiny)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[9e981753ca...](https://github.com/CandleJaxx/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Tuesday 2023-03-07 23:10:16 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[26688597e3...](https://github.com/CandleJaxx/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Tuesday 2023-03-07 23:10:16 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[55c39d4573...](https://github.com/wrye-bash/wrye-bash/commit/55c39d45734a59dc3fb734adbbe36f7995648af2)
#### Tuesday 2023-03-07 23:35:22 by Infernio

Fix the whole 'auto-wrapping text' mess

I've finally figured it out. Took literally hours of fiddling around
with AutoWrapStaticText to work around a really weird bug, then more
hours to figure out how to get the settings dialog to wrap nicely when
it's opened, but it's done. It's wonderful. I never want to touch it
again.

Utumno:
We must link to the commit here - just a fixup (kept separate in case
there is a shorter url - certainly needs to wrap better :P)

I am really curious to learn what the 'really weird bug" was - I
remember wrapping being a pain so I'd like to know what made the
difference finally - is it just the `dc = wx.ClientDC(self)` (?)

You mean wx.AutoWrapStaticText and it _is_ wonderful

Edit: added a wx (Pep8) suffix to wx functions/overrides - makes it
much easier to figure out on first read (plus if we ever want to swap
gui libs this would be done by a metaclass reading off the correctly
suffixed method)

---
## [newstools/2023-express](https://github.com/newstools/2023-express)@[63cc812482...](https://github.com/newstools/2023-express/commit/63cc8124821b3f3f6e521f535b8d23e5a3824de1)
#### Tuesday 2023-03-07 23:46:23 by Billy Einkamerer

Created Text For URL [www.express.co.uk/entertainment/music/1743574/Freddie-Mercury-girlfriend-Mary-Austin-birthday-gay-boyfriend-Jim-leave-the-house-in-will]

---

