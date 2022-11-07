## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-06](docs/good-messages/2022/2022-11-06.md)


1,867,970 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,867,970 were push events containing 2,571,744 commit messages that amount to 147,454,884 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[3582aa77bb...](https://github.com/skylord-a52/orbstation-andrea/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Sunday 2022-11-06 00:47:07 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[5b4ba051a0...](https://github.com/GoblinBackwards/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Sunday 2022-11-06 01:21:12 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [aagit/android_kernel_oneplus_sm8150](https://github.com/aagit/android_kernel_oneplus_sm8150)@[c6342577e3...](https://github.com/aagit/android_kernel_oneplus_sm8150/commit/c6342577e3c9cd30a4434f50e7cdfe24bd75571f)
#### Sunday 2022-11-06 02:35:39 by Andrea Arcangeli

git range-diff of e9246ac7cff3881461b3b5d7d8c6f5bba65850ce

Missing commits from https://android.googlesource.com/kernel/common
android-4.14-stable branch (some, as the ext4 bits, was already in
lineage-19.1, others as the random bits skipped because of too many
rejects):

   1:  7529068a775e7 <    -:  ------------- f2fs: refactor resize_fs to avoid meta updates in progress
   2:  9015e363e6fa8 <    -:  ------------- f2fs: fix missing check for f2fs_unlock_op
   3:  86556e67a9fde <    -:  ------------- ANDROID: mmc: MMC crypto API
   4:  7a3e0cb384d3b <    -:  ------------- ANDROID: Add padding for crypto related structs in UFS and MMC
   7:  b8cdb45351d93 <    -:  ------------- ANDROID: dm-default-key: Update key size for wrapped keys
   9:  72091967bfbbc <    -:  ------------- ANDROID: block: backport the ability to specify max_dun_bytes
  10:  8711e464f7dfc <    -:  ------------- ANDROID: dm-default-key: set dun_bytes more precisely
  11:  6be68d89b4d52 <    -:  ------------- ANDROID: fscrypt: set dun_bytes more precisely
  13:  9bbb91899906f <    -:  ------------- Revert "f2fs: refactor resize_fs to avoid meta updates in progress"
  14:  c62296ef40570 <    -:  ------------- ANDROID: Incremental fs: Avoid continually recalculating hashes
  15:  6e1790888863e <    -:  ------------- ANDROID: Incremental fs: Fix scheduling while atomic error
  16:  1c8f02e0a7d8e <    -:  ------------- ANDROID: Incremental fs: wake up log pollers less often
  18:  dabf068133d59 <    -:  ------------- FROMLIST: x86_64: fix jiffies ODR violation
  21:  89b228375922d <    -:  ------------- f2fs: split f2fs_d_compare() from f2fs_match_name()
  22:  77b2eab3542d2 <    -:  ------------- f2fs: rework filename handling
  23:  f8a8368ae70a8 <    -:  ------------- f2fs: fix checkpoint=disable:%u%%
  35:  30796f18dc525 <    -:  ------------- f2fs: remove blk_plugging in block_operations
  38:  cd74e150aea89 <    -:  ------------- f2fs: report delalloc reserve as non-free in statfs for project quota
  42:  963d404e8894c <    -:  ------------- f2fs: refactor resize_fs to avoid meta updates in progress
  90:  a289f82f6a7e7 <    -:  ------------- f2fs: introduce read_inline_xattr
  91:  88266a5413a89 <    -:  ------------- f2fs: introduce read_xattr_block
  92:  ec236cd6a254d <    -:  ------------- f2fs: sanity check of xattr entry size
  93:  1d295b32df866 <    -:  ------------- f2fs: fix to avoid accessing xattr across the boundary
  94:  ae811cecbbb23 <    -:  ------------- f2fs: fix to avoid memory leakage in f2fs_listxattr
  95:  d673c1e5e6fea <    -:  ------------- net: stmmac: Use mutex instead of spinlock
 100:  30f4ac2c49caf <    -:  ------------- virtio-blk: handle block_device_operations callbacks after hot unplug
 114:  7addf56d9a45e <    -:  ------------- netfilter: conntrack: avoid gcc-10 zero-length-bounds warning
 119:  859ea9726dc27 <    -:  ------------- kbuild: compute false-positive -Wmaybe-uninitialized cases in Kconfig
 120:  4cdd5c0c6b134 <    -:  ------------- Stop the ad-hoc games with -Wno-maybe-initialized
 121:  1a99bcaa094d8 <    -:  ------------- gcc-10: disable 'zero-length-bounds' warning for now
 122:  7c29131adf939 <    -:  ------------- gcc-10: disable 'array-bounds' warning for now
 123:  d0e84b91f1557 <    -:  ------------- gcc-10: disable 'stringop-overflow' warning for now
 124:  eaeb85d649fb7 <    -:  ------------- gcc-10: disable 'restrict' warning for now
 138:  e8e3fcbc66f60 <    -:  ------------- ALSA: rawmidi: Initialize allocated buffers
 139:  8645ac3684a70 <    -:  ------------- ALSA: rawmidi: Fix racy buffer resize under concurrent accesses
 163:  08870bd1a24fc <    -:  ------------- ANDROID: namespace'ify tcp_default_init_rwnd implementation
 165:  a52238353e671 <    -:  ------------- BACKPORT: FROMLIST: fscrypt: add support for IV_INO_LBLK_32 policies
 166:  09075917fb5d0 <    -:  ------------- ANDROID: fscrypt: handle direct I/O with IV_INO_LBLK_32
 228:  3d8caf062c689 <    -:  ------------- Revert "ANDROID: Incremental fs: Avoid continually recalculating hashes"
 229:  69eb478ff9324 <    -:  ------------- ANDROID: net: bpf: permit redirect from ingress L3 to egress L2 devices at near max mtu
 230:  25078e97c11ce <    -:  ------------- writeback: Avoid skipping inode writeback
 257:  c151fa995ff78 <    -:  ------------- net: qrtr: Fix passing invalid reference to qrtr_local_enqueue()
 287:  41269451abcfc <    -:  ------------- mmc: block: Fix use-after-free issue for rpmb
 306:  05462bcc7d21b <    -:  ------------- xfrm: fix error in comment
 317:  be22b6df6d804 <    -:  ------------- mm/vmalloc.c: don't dereference possible NULL pointer in __vunmap()
 331:  a556403adbcd5 <    -:  ------------- ANDROID: Incremental fs: Fix four error-path bugs
 332:  3c5daa412cf5b <    -:  ------------- ANDROID: Incremental fs: Cache successful hash calculations
 333:  8330799340d88 <    -:  ------------- ANDROID: dm-bow: Add block_size option
 335:  49d7e80073600 <    -:  ------------- f2fs: avoid utf8_strncasecmp() with unstable name
 339:  a3a7060dbf1cb <    -:  ------------- f2fs: attach IO flags to the missing cases
 340:  9fe854df0eac2 <    -:  ------------- ANDROID: Incremental fs: Remove dependency on PKCS7_MESSAGE_PARSER
 391:  de635b5d05e15 <    -:  ------------- fscrypt: remove unnecessary extern keywords
 393:  6dc3cb5f238a6 <    -:  ------------- fscrypt: add fscrypt_add_test_dummy_key()
 394:  11807f32791ac <    -:  ------------- fscrypt: support test_dummy_encryption=v2
 395:  7c2fcbe7ae974 <    -:  ------------- fscrypt: make test_dummy_encryption use v2 by default
 396:  84aad2655054e <    -:  ------------- fscrypt: add support for IV_INO_LBLK_32 policies
 399:  3cec603f33ae9 <    -:  ------------- fscrypt: remove stale definition
 401:  137526cb94e7d <    -:  ------------- Revert "writeback: Avoid skipping inode writeback"
 402:  e11ead2b8658a <    -:  ------------- writeback: Protect inode->i_io_list with inode->i_lock
 403:  37343fde13a6e <    -:  ------------- writeback: Avoid skipping inode writeback
 404:  418c9b9130438 <    -:  ------------- writeback: Fix sync livelock due to b_dirty_time processing
 405:  59e9f7918960b <    -:  ------------- writeback: Drop I_DIRTY_TIME_EXPIRE
 425:  d808ea8d0b4de <    -:  ------------- x86/speculation: Prevent rogue cross-process SSBD shutdown
 444:  908a17a55104d <    -:  ------------- x86/speculation: Change misspelled STIPB to STIBP
 445:  c9e56c9874105 <    -:  ------------- x86/speculation: Add support for STIBP always-on preferred mode
 446:  b4eba1edf71e3 <    -:  ------------- x86/speculation: Avoid force-disabling IBPB based on STIBP and enhanced IBRS.
 476:  125363839cf38 <    -:  ------------- mmc: sdhci-msm: Clear tuning done flag while hs400 tuning
 477:  ed92d7f71847e <    -:  ------------- mmc: sdio: Fix potential NULL pointer error in mmc_sdio_init_card()
 536:  ab28fb26346cf <    -:  ------------- mmc: sdhci-msm: Set SDHCI_QUIRK_MULTIBLOCK_READ_ACMD12 quirk
 546:  3b6c93db0a02b <    -:  ------------- mm: thp: make the THP mapcount atomic against __split_huge_pmd_locked()
 675:  0c8c366c54f07 <    -:  ------------- usb: gadget: Fix issue with config_ep_by_speed function
 678:  291ae253fb695 <    -:  ------------- scsi: ufs-qcom: Fix scheduling while atomic issue
 704:  9f33eff495888 <    -:  ------------- usb/xhci-plat: Set PM runtime as active on resume
 708:  a43abf15844c9 <    -:  ------------- block: Fix use-after-free in blkdev_get()
 822:  9cf08b8575034 <    -:  ------------- UPSTREAM: binder: fix null deref of proc->context
 873:  0a117d00e86fe <    -:  ------------- ALSA: compress: fix partial_drain completion state
 894:  936d94fabbe70 <    -:  ------------- genetlink: remove genl_bind
 909:  7db1425326b66 <    -:  ------------- arm64/alternatives: use subsections for replacement sequences
 928:  bedfa0049d097 <    -:  ------------- Revert "usb/xhci-plat: Set PM runtime as active on resume"
 929:  e0f07c3c2a1ff <    -:  ------------- doc: dt: bindings: usb: dwc3: Update entries for disabling SS instances in park mode
 953:  c0689058968d4 <    -:  ------------- usb: gadget: function: fix missing spinlock in f_uac1_legacy
 980:  5cb2bc3c21ac9 <    -:  ------------- Revert "arm64/alternatives: use subsections for replacement sequences"
1019:  d8b49f70fffa0 <    -:  ------------- Input: add `SW_MACHINE_COVER`
1059:  bbacb34b84407 <    -:  ------------- mm/page_owner.c: remove drain_all_pages from init_early_allocated_pages
1076:  bc08d46f010cc <    -:  ------------- f2fs: check memory boundary by insane namelen
1077:  6a27f426266ac <    -:  ------------- f2fs: check if file namelen exceeds max value
1080:  53993bba307db <    -:  ------------- x86/build/lto: Fix truncated .bss with -fdata-sections
1097:  a15a67e3eb42a <    -:  ------------- arm64/alternatives: move length validation inside the subsection
1234:  93934e5d463b3 <    -:  ------------- coresight: tmc: Fix TMC mode read in tmc_read_unprepare_etb()
1264:  6de6d1ca5f3e8 <    -:  ------------- net: refactor bind_bucket fastreuse into helper
1364:  0063bb829eba8 <    -:  ------------- mm, page_alloc: fix core hung in free_pcppages_bulk()
1365:  f9d723d0b788c <    -:  ------------- ext4: fix checking of directory entry validity for inline directories
1472:  0fa1f08619ccc <    -:  ------------- writeback: Protect inode->i_io_list with inode->i_lock
1473:  856fa4ebf57c0 <    -:  ------------- writeback: Avoid skipping inode writeback
1474:  77322edb99f01 <    -:  ------------- writeback: Fix sync livelock due to b_dirty_time processing
1499:  3d516e369e3a5 <    -:  ------------- drm/msm: add shutdown support for display platform_driver
1553:  fcc0896148c82 <    -:  ------------- KVM: arm64: Defer guest entry when an asynchronous exception is pending
1563:  e0dc293b49c41 <    -:  ------------- vfio/type1: Support faulting PFNMAP vmas
1580:  c63027f79c173 <    -:  ------------- mmc: sdhci-msm: Add retries when all tuning phases are found valid
1646:  856de6bc25ead <    -:  ------------- f2fs: fix indefinite loop scanning for free nid
1670:  cc34fcefe9768 <    -:  ------------- ANDROID: Delete goldfish build configs and defconfigs
1711:  5656db5e0561b <    -:  ------------- debugfs: Fix !DEBUG_FS debugfs_create_automount
1796:  5a174aebcf540 <    -:  ------------- usb: dwc3: Increase timeout for CmdAct cleared by device controller
1864:  23fb662b13e4f <    -:  ------------- epoll: do not insert into poll queues until all sanity checks are done
1867:  a3915080e95da <    -:  ------------- ep_create_wakeup_source(): dentry name can change under you...
1906:  387026b76afb6 <    -:  ------------- mmc: core: don't set limits.discard_granularity as 0
1940:  d4c49b6733c31 <    -:  ------------- binder: fix UAF when releasing todo list
2115:  73eae769d588d <    -:  ------------- scsi: ufs: ufs-qcom: Fix race conditions caused by ufs_qcom_testbus_config()
2122:  6d6d017a6d704 <    -:  ------------- usb: gadget: f_ncm: allow using NCM in SuperSpeed Plus gadgets.
2144:  4d6d4ed1758f3 <    -:  ------------- fscrypt: return -EXDEV for incompatible rename or link into encrypted dir
2209:  00275153aa523 <    -:  ------------- usb: dwc3: core: add phy cleanup for probe error handling
2210:  d92f1821ad6de <    -:  ------------- usb: dwc3: core: don't trigger runtime pm when remove driver
2377:  3cd62032ff7d9 <    -:  ------------- perf/core: Fix bad use of igrab()
2378:  006f711673971 <    -:  ------------- perf/core: Fix crash when using HW tracing kernel filters
2419:  d124911d0832c <    -:  ------------- ANDROID: Incremental fs: Fix minor bugs
2420:  9540a2c0de66f <    -:  ------------- ANDROID: Incremental fs: dentry_revalidate should not return -EBADF.
2427:  d78af37eedd05 <    -:  ------------- ANDROID: Incremental fs: Fix incfs to work on virtio-9p
2430:  ea3a54ef5d4ef <    -:  ------------- ANDROID: Incremental fs: Add UID to pending_read
2431:  664b74271565a <    -:  ------------- ANDROID: Incremental fs: Separate pseudo-file code
2432:  0f577422348f6 <    -:  ------------- ANDROID: Incremental fs: Add .blocks_written file
2433:  891e6dcc7fec3 <    -:  ------------- ANDROID: Incremental fs: Remove attributes from file
2436:  334f721e51aca <    -:  ------------- ANDROID: Incremental fs: Make compatible with existing files
2437:  362007bd63e35 <    -:  ------------- ANDROID: Incremental fs: Add INCFS_IOC_GET_BLOCK_COUNT
2438:  94eb31aaa51e2 <    -:  ------------- ANDROID: Incremental fs: Add hash block counts to IOC_IOCTL_GET_BLOCK_COUNT
2439:  51c82e61db0e4 <    -:  ------------- ANDROID: Incremental fs: Fix filled block count from get filled blocks
2440:  a527a98b1763b <    -:  ------------- ANDROID: Incremental fs: Fix uninitialized variable
2441:  65652f5a199b7 <    -:  ------------- ANDROID: Incremental fs: Fix dangling else
2442:  17efe505a4c3d <    -:  ------------- ANDROID: Incremental fs: Add .incomplete folder
2443:  ebdb37cbb1711 <    -:  ------------- ANDROID: Incremental fs: Add per UID read timeouts
2444:  1d85ac54f5911 <    -:  ------------- ANDROID: Incremental fs: Fix misuse of cpu_to_leXX and poll return
2445:  2f3ab171fb2c7 <    -:  ------------- ANDROID: Incremental fs: Fix read_log_test which failed sporadically
2447:  c47f87811d216 <    -:  ------------- ANDROID: Incremental fs: Small improvements
2448:  9523a669ca4a5 <    -:  ------------- ANDROID: Incremental fs: Add zstd compression support
2537:  8541087975223 <    -:  ------------- scsi: ufs: Fix race between shutdown and runtime resume flow
2562:  0b456c623afe5 <    -:  ------------- UPSTREAM: arm64: sysreg: Clean up instructions for modifying PSTATE fields
2563:  f5e74ee2c4652 <    -:  ------------- ANDROID: Incremental fs: Fix 32-bit build
2585:  b08e0c0b32f76 <    -:  ------------- ANDROID: Incremental fs: Add zstd feature flag
2586:  b38636bf5933c <    -:  ------------- ANDROID: Incremental fs: Add v2 feature flag
2587:  f527acab63fd1 <    -:  ------------- ANDROID: Incremental fs: Change per UID timeouts to microseconds
2588:  af56fc80708fb <    -:  ------------- ANDROID: Incremental fs: Fix incfs_test use of atol, open
2589:  8278cda5d9767 <    -:  ------------- ANDROID: Incremental fs: Set credentials before reading/writing
2593:  84f747ade2fbb <    -:  ------------- usb: gadget: f_fs: Use local copy of descriptors for userspace copy
2600:  882e038d2cd27 <    -:  ------------- tty: Fix ->pgrp locking in tiocspgrp()
2672:  27e1b18af55f8 <    -:  ------------- usb: gadget: f_fs: Re-use SS descriptors for SuperSpeedPlus
2689:  ce7acf72db8c4 <    -:  ------------- selinux: fix error initialization in inode_doinit_with_dentry()
2698:  44f5d9fecd803 <    -:  ------------- selinux: fix inode_doinit_with_dentry() LABEL_INVALID error handling
2862:  53443687729b0 <    -:  ------------- ANDROID: usb: gadget: f_accessory: fix CTS test stuck
2863:  d5e62e55287d9 <    -:  ------------- ANDROID: USB: f_accessory: Check dev pointer before decoding ctrl request
2864:  74ee3eed8bcfc <    -:  ------------- ANDROID: usb: f_accessory: Remove stale comments
2868:  d1f0db7be7fc9 <    -:  ------------- ANDROID: usb: f_accessory: Add refcounting to global 'acc_dev'
2870:  ff547623ce6c0 <    -:  ------------- ANDROID: usb: f_accessory: Don't corrupt global state on double registration
2871:  3af44e7d523fd <    -:  ------------- ANDROID: usb: f_accessory: Cancel any pending work before teardown
2948:  dee735834d1ea <    -:  ------------- usb: gadget: Fix spinlock lockup on usb_function_deactivate
2949:  4cea32e3d104a <    -:  ------------- usb: gadget: configfs: Preserve function ordering after bind failure
3040:  b3d3fcefbdd05 <    -:  ------------- Revert "ANDROID: Incremental fs: Set credentials before reading/writing"
3041:  abc9dbd4526a7 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix incfs_test use of atol, open"
3042:  0afc7abd4a0ef <    -:  ------------- Revert "ANDROID: Incremental fs: Change per UID timeouts to microseconds"
3043:  554a9ae309ecc <    -:  ------------- Revert "ANDROID: Incremental fs: Add v2 feature flag"
3044:  e28158b16afe9 <    -:  ------------- Revert "ANDROID: Incremental fs: Add zstd feature flag"
3045:  8e12ff818c8d5 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix 32-bit build"
3046:  6c6b05e83a7b3 <    -:  ------------- Revert "ANDROID: Incremental fs: Add zstd compression support"
3047:  eb182876fde1c <    -:  ------------- Revert "ANDROID: Incremental fs: Small improvements"
3049:  51cf7a0f5d9d7 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix read_log_test which failed sporadically"
3050:  d7c055aa83560 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix misuse of cpu_to_leXX and poll return"
3051:  f017e3544bc5b <    -:  ------------- Revert "ANDROID: Incremental fs: Add per UID read timeouts"
3052:  225552d81d223 <    -:  ------------- Revert "ANDROID: Incremental fs: Add .incomplete folder"
3053:  f26f8de0d9642 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix dangling else"
3054:  b517d1c9f8e2e <    -:  ------------- Revert "ANDROID: Incremental fs: Fix uninitialized variable"
3055:  cb39ed9136c9d <    -:  ------------- Revert "ANDROID: Incremental fs: Fix filled block count from get filled blocks"
3056:  436086d7be530 <    -:  ------------- Revert "ANDROID: Incremental fs: Add hash block counts to IOC_IOCTL_GET_BLOCK_COUNT"
3057:  6a10ea0c7321d <    -:  ------------- Revert "ANDROID: Incremental fs: Add INCFS_IOC_GET_BLOCK_COUNT"
3058:  5f1840027f46a <    -:  ------------- Revert "ANDROID: Incremental fs: Make compatible with existing files"
3061:  28b56592edc1c <    -:  ------------- Revert "ANDROID: Incremental fs: Remove attributes from file"
3062:  50acfd185154b <    -:  ------------- Revert "ANDROID: Incremental fs: Add .blocks_written file"
3063:  fcda7b4e57833 <    -:  ------------- Revert "ANDROID: Incremental fs: Separate pseudo-file code"
3064:  15bd987412ebe <    -:  ------------- Revert "ANDROID: Incremental fs: Add UID to pending_read"
3067:  a16a6c43a94c7 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix incfs to work on virtio-9p"
3075:  e17a9ed44c861 <    -:  ------------- Revert "ANDROID: Incremental fs: Fix minor bugs"
3086:  30f2a89f9481f <    -:  ------------- scsi: ufs: Correct the LUN used in eh_device_reset_handler() callback
3121:  52b71186bdc06 <    -:  ------------- futex: Simplify fixup_pi_state_owner()
3122:  50cfcc42dd1be <    -:  ------------- futex: Handle faults correctly for PI futexes
3125:  2f15ad510ebb4 <    -:  ------------- fs: move I_DIRTY_INODE to fs.h
3126:  5c846eee8b209 <    -:  ------------- writeback: Drop I_DIRTY_TIME_EXPIRE
3127:  964d9ec041e2c <    -:  ------------- fs: fix lazytime expiration handling in __writeback_single_inode()
3177:  0b5d24082d8b2 <    -:  ------------- UPSTREAM: dma-buf: free dmabuf->name in dma_buf_release()
3203:  93ea2434bd9dc <    -:  ------------- mm: thp: fix MADV_REMOVE deadlock on shmem THP
3210:  cbb4c73f9eab8 <    -:  ------------- UPSTREAM: net: bpf: Make bpf_ktime_get_ns() available to non GPL programs
3212:  2581e5be65552 <    -:  ------------- BACKPORT: dma-buf: Move dma_buf_release() from fops to dentry_ops
3253:  0d38200da5d9c <    -:  ------------- x86/build: Disable CET instrumentation in the kernel for 32-bit too
3255:  cfc6eb148982c <    -:  ------------- tracing: Fix SKIP_STACK_VALIDATION=1 build due to bad merge with -mrecord-mcount
3256:  4480921923080 <    -:  ------------- tracing: Avoid calling cc-option -mrecord-mcount for every Makefile
3271:  00022873fdc1a <    -:  ------------- HID: make arrays usage and value to be the same
3452:  676c8e5a1bf44 <    -:  ------------- drm/virtio: use kvmalloc for large allocations
3454:  49970f4658632 <    -:  ------------- arm64 module: set plt* section addresses to 0x0
3479:  390881843b4f1 <    -:  ------------- sysfs: Add sysfs_emit and sysfs_emit_at to format sysfs output
3484:  09beeb4694414 <    -:  ------------- zsmalloc: account the number of compacted pages correctly
3509:  63d4b2332739b <    -:  ------------- FROMGIT: configfs: fix a use-after-free in __configfs_open_file
3513:  5aac598c4e897 <    -:  ------------- net: Fix gro aggregation for udp encaps with zero csum
3557:  90c58a548d3a9 <    -:  ------------- mmc: core: Fix partition switch time for eMMC
3625:  84cee271cfdbe <    -:  ------------- net/qrtr: fix __netdev_alloc_skb call
3629:  e93575764f70a <    -:  ------------- USB: replace hardcode maximum usb string length by definition
3630:  27b028b9c3738 <    -:  ------------- usb: gadget: configfs: Fix KASAN use-after-free
3632:  cfdaec38d6045 <    -:  ------------- iio:adc:qcom-spmi-vadc: add default scale to LR_MUX2_BAT_ID channel
3694:  2ed1838a51089 <    -:  ------------- drm/msm: fix shutdown hook in case GPU components failed to bind
3736:  64cf6c3156a5c <    -:  ------------- bpf: Remove MTU check in __bpf_skb_max_len
3755:  99b948bd84de1 <    -:  ------------- USB: quirks: ignore remote wake-up on Fibocom L850-GL LTE modem
3783:  793953356b83a <    -:  ------------- ANDROID: Incremental fs: Set credentials before reading/writing
3877:  b8ae95b946f34 <    -:  ------------- arm64: alternatives: Move length validation in alternative_{insn, endif}
3889:  407faed92b4a4 <    -:  ------------- gup: document and work around "COW can break either way" issue
3891:  457ac0ff3ef2d <    -:  ------------- ext4: correct error label in ext4_rename()
3930:  d2032103bcebe <    -:  ------------- mmc: core: Do a power cycle when the CMD11 fails
3939:  fd9ad3cda28f6 <    -:  ------------- usb: gadget: f_uac1: validate input parameters
4002:  5677f028f1502 <    -:  ------------- usb: gadget: Fix double free of device descriptor pointers
4004:  b40eb2559e02a <    -:  ------------- usb: dwc3: gadget: Fix START_TRANSFER link state check
4195:  d34cab87d2fb6 <    -:  ------------- usb: core: hub: fix race condition about TRSMRCY of resume
4354:  a27e61c6a131c <    -:  ------------- net: usb: cdc_ncm: don't spew notifications
4399:  7308b7bd678d4 <    -:  ------------- sched/fair: Optimize select_idle_cpu
4409:  455c38eb8b351 <    -:  ------------- cgroup: disable controllers at parse time
4515:  58b5e02c6ca0e <    -:  ------------- usb: dwc3: core: fix kernel panic when do reboot
4522:  8e64fac312b25 <    -:  ------------- Makefile: Move -Wno-unused-but-set-variable out of GCC only block
4633:  ee692b6db0303 <    -:  ------------- block_dump: remove block_dump feature in mark_inode_dirty()
4750:  3531c1c2ae7d8 <    -:  ------------- selinux: use __GFP_NOWARN with GFP_NOWAIT in the AVC
4768:  f01bfaea62d14 <    -:  ------------- sctp: validate from_addr_param return
4769:  d890768c1ed66 <    -:  ------------- sctp: add size validation when walking chunks
4770:  1b921f9f4bfcb <    -:  ------------- fscrypt: don't ignore minor_hash when hash is 0
4775:  646cdf842cc52 <    -:  ------------- usb: gadget: f_fs: Fix setting of device and driver data cross-references
4782:  9f6e4f48e9e00 <    -:  ------------- cpu/hotplug: Cure the cpusets trainwreck
4941:  7a78b17fc8282 <    -:  ------------- Revert "USB: quirks: ignore remote wake-up on Fibocom L850-GL LTE modem"
5019:  6c5bc69f722cb <    -:  ------------- ANDROID: staging: ion: move buffer kmap from begin/end_cpu_access()
5134:  24749050f167e <    -:  ------------- usb: dwc3: gadget: Fix dwc3_calc_trbs_left()
5135:  a58d290e7cd85 <    -:  ------------- usb: dwc3: gadget: Stop EP0 transfers during pullup disable
5138:  99279223a37b4 <    -:  ------------- ip_gre: add validation for csum_start
5164:  bd0970398a7a5 <    -:  ------------- clk: fix build warning for orphan_list
5166:  78967749984cf <    -:  ------------- igmp: Add ip_mc_list lock in ip_check_mc_rcu
5168:  2a18f941bccbb <    -:  ------------- f2fs: fix potential overflow
5354:  a2d09569f1e3c <    -:  ------------- events: Reuse value read using READ_ONCE instead of re-reading it
5376:  e58e3511b3c20 <    -:  ------------- sctp: validate chunk size in __rcv_asconf_lookup
5441:  463c46705f321 <    -:  ------------- cpufreq: schedutil: Use kobject release() method to free sugov_tunables
5465:  c13d897b09515 <    -:  ------------- arm64: Extend workaround for erratum 1024718 to all versions of Cortex-A55
5520:  d6e8ea926933d <    -:  ------------- BACKPORT: cgroup: make per-cgroup pressure stall tracking configurable
5521:  6e6c15288df8c <    -:  ------------- BACKPORT: dmabuf: fix use-after-free of dmabuf's file->f_inode
5590:  8b9d000e83eec <    -:  ------------- ARM: 9122/1: select HAVE_FUTEX_CMPXCHG
5597:  1f66b391c76e4 <    -:  ------------- ARM: 8819/1: Remove '-p' from LDFLAGS
5644:  9693ca7b5262a <    -:  ------------- BACKPORT: binder: use cred instead of task for selinux checks
5647:  c0a1a632dca5f <    -:  ------------- ANDROID: usb: gadget: f_accessory: Mitgate handling of non-existent USB request
5649:  8989da231b3b9 <    -:  ------------- binder: use euid from cred instead of using task
5944:  c8e76f849aed3 <    -:  ------------- PCI: Add PCI_EXP_LNKCTL2_TLS* macros
6004:  3bd55e5ed8f56 <    -:  ------------- UPSTREAM: USB: gadget: detect too-big endpoint 0 requests
6005:  6be75351b0acb <    -:  ------------- UPSTREAM: USB: gadget: zero allocate endpoint 0 buffers
6006:  43cc4686b15d7 <    -:  ------------- HID: add hid_is_usb() function to make it simpler for USB detection
6007:  10b7609ebd5bf <    -:  ------------- HID: add USB_HID dependancy to hid-prodikeys
6008:  ef5ba3c8103c8 <    -:  ------------- HID: add USB_HID dependancy to hid-chicony
6009:  ab34124f68f7e <    -:  ------------- HID: add USB_HID dependancy on some USB HID drivers
6010:  cad5c7582322e <    -:  ------------- HID: wacom: fix problems when device is not a valid USB device
6011:  37a6a8d76b01e <    -:  ------------- HID: check for valid USB device for many HID drivers
6038:  e7c8afee14913 <    -:  ------------- USB: gadget: detect too-big endpoint 0 requests
6039:  d8cd524ae4ec7 <    -:  ------------- USB: gadget: zero allocate endpoint 0 buffers
6059:  d3c17d5e271ab <    -:  ------------- FROMGIT: USB: gadget: bRequestType is a bitfield, not a enum
6074:  1fe4d9ba5c921 <    -:  ------------- x86: Make ARCH_USE_MEMREMAP_PROT a generic Kconfig symbol
6081:  a829ff7c8ec49 <    -:  ------------- net/packet: rx_owner_map depends on pg_vec
6094:  2a899eeca5e84 <    -:  ------------- net: lan78xx: Avoid unnecessary self assignment
6217:  cde0f1a0a486f <    -:  ------------- media: dmxdev: fix UAF when dvb_register_device() fails
6357:  2cd45139c0f28 <    -:  ------------- fuse: fix bad inode
6358:  f78d626801194 <    -:  ------------- fuse: fix live lock in fuse_iget()
6467:  32048f4be071f <    -:  ------------- usb: f_fs: Fix use-after-free for epfile
6480:  c7ad83d561df1 <    -:  ------------- USB: gadget: validate interface OS descriptor requests
6481:  4c22fbcef778b <    -:  ------------- usb: gadget: rndis: check size of RNDIS_MSG_SET command
6527:  a162b11c975ef <    -:  ------------- lib/iov_iter: initialize "flags" in new pipe_buffer
6556:  669c2b1789567 <    -:  ------------- usb: gadget: rndis: add spinlock for rndis response list
6561:  3594650c3ec1d <    -:  ------------- usb: dwc3: gadget: Let the interrupt handler disable bottom halves.
6579:  6936d1097e9cb <    -:  ------------- usb: gadget: don't release an existing dev->buf
6580:  70959fa1a003c <    -:  ------------- usb: gadget: clear related members when goto fail
6584:  d4d5190b942ac <    -:  ------------- xfrm: fix MTU regression
6694:  5149b895206f8 <    -:  ------------- net: ipv6: fix skb_over_panic in __ip6_append_data
6695:  2c8abafd6c72e <    -:  ------------- esp: Fix possible buffer overflow in ESP transformation
6712:  9aeb4a5a73d39 <    -:  ------------- arm64: arch_timer: Add workaround for ARM erratum 1188873
6714:  786ec17678a48 <    -:  ------------- arm64: Add silicon-errata.txt entry for ARM erratum 1188873
6716:  52d19a0f65310 <    -:  ------------- arm64: Add part number for Neoverse N1
6717:  60cf0854f6408 <    -:  ------------- arm64: Add part number for Arm Cortex-A77
6718:  80c55ca10f3d4 <    -:  ------------- arm64: Add Neoverse-N2, Cortex-A710 CPU part definition
6719:  63271842d1b02 <    -:  ------------- arm64: Add Cortex-X2 CPU part definition
6734:  0b1c660d8516e <    -:  ------------- KVM: arm64: Add templates for BHB mitigation sequences
6735:  3e3904125fccd <    -:  ------------- arm64: Mitigate spectre style branch history side channels
6738:  2e53c83ea673b <    -:  ------------- arm64: Use the clearbhb instruction in mitigations
6876:  775be2311ae44 <    -:  ------------- clk: qcom: clk-rcg2: Update the frac table for pixel clock
6996:  324d3d6663310 <    -:  ------------- arm64: module: remove (NOLOAD) from linker script
7001:  94c291577f507 <    -:  ------------- xfrm: policy: match with both mark and mask on user interfaces
7079:  bf9c3fa38cc0e <    -:  ------------- USB: quirks: add STRING quirk for VCOM device
7090:  25af94384a872 <    -:  ------------- usb: gadget: configfs: clear deactivation flag in configfs_composite_unbind()
7243:  388bc1e696639 <    -:  ------------- dm verity: set DM_TARGET_IMMUTABLE feature flag
7254:  ff4f627eb1694 <    -:  ------------- USB: new quirk for Dell Gen 2 devices
7289:  4b5541035b59d <    -:  ------------- fat: add ratelimit to fat*_ent_bread()
7449:  a7afaf7916d08 <    -:  ------------- Revert "net: af_key: add check for pfkey_broadcast in function pfkey_process"
7460:  03878a8674726 <    -:  ------------- nfc: st21nfca: fix incorrect validating logic in EVT_TRANSACTION
7504:  f83ff022179e7 <    -:  ------------- crypto: chacha20 - Fix keystream alignment for chacha20_block()
7509:  005e7ac06d2b5 <    -:  ------------- random: Return nbytes filled from hw RNG
7510:  923eb78099e02 <    -:  ------------- random: add a config option to trust the CPU's hwrng
7511:  6169849980907 <    -:  ------------- random: remove preempt disabled region
7512:  4395f2316066c <    -:  ------------- random: Make crng state queryable
7513:  08d453eca365a <    -:  ------------- random: make CPU trust a boot parameter
7514:  c5d75e6df54a7 <    -:  ------------- drivers/char/random.c: constify poolinfo_table
7515:  14c55b81d99a6 <    -:  ------------- drivers/char/random.c: remove unused stuct poolinfo::poolbits
7516:  72ed3248d0d66 <    -:  ------------- drivers/char/random.c: make primary_crng static
7517:  fd5e41d61e379 <    -:  ------------- random: only read from /dev/random after its pool has received 128 bits
7518:  50622066f5d13 <    -:  ------------- random: move rand_initialize() earlier
7519:  b30c2834aa404 <    -:  ------------- random: document get_random_int() family
7520:  138b6da69f991 <    -:  ------------- latent_entropy: avoid build error when plugin cflags are not set
7521:  eaabe771c1aa5 <    -:  ------------- random: fix soft lockup when trying to read from an uninitialized blocking pool
7522:  0b33f93df8793 <    -:  ------------- random: Support freezable kthreads in add_hwgenerator_randomness()
7523:  eb1e322c70cec <    -:  ------------- fdt: add support for rng-seed
7524:  c1f7c9876ef10 <    -:  ------------- random: Use wait_event_freezable() in add_hwgenerator_randomness()
7525:  9ea167431f404 <    -:  ------------- char/random: Add a newline at the end of the file
7526:  b7c853adcdfa2 <    -:  ------------- Revert "hwrng: core - Freeze khwrng thread during suspend"
7527:  a83bdc0830f6b <    -:  ------------- crypto: Deduplicate le32_to_cpu_array() and cpu_to_le32_array()
7528:  6adb419f06ffd <    -:  ------------- crypto: blake2s - generic C library implementation and selftest
7529:  66680715fd7b0 <    -:  ------------- lib/crypto: blake2s: move hmac construction into wireguard
7530:  42b10f6770ed1 <    -:  ------------- lib/crypto: sha1: re-roll loops to reduce code size
7531:  3a8e277bf9ccf <    -:  ------------- random: Don't wake crng_init_wait when crng_init == 1
7532:  32d4b398c078b <    -:  ------------- random: Add a urandom_read_nowait() for random APIs that don't warn
7533:  a7b5560f065e7 <    -:  ------------- random: add GRND_INSECURE to return best-effort non-cryptographic bytes
7534:  aa38e379f95e5 <    -:  ------------- random: ignore GRND_RANDOM in getentropy(2)
7535:  9aefae44f37ef <    -:  ------------- random: make /dev/random be almost like /dev/urandom
7536:  64bfe2ee56743 <    -:  ------------- char/random: silence a lockdep splat with printk()
7537:  5eadd290e1706 <    -:  ------------- random: fix crash on multiple early calls to add_bootloader_randomness()
7538:  ba17344096ae6 <    -:  ------------- random: remove the blocking pool
7539:  3ae32ecd83154 <    -:  ------------- random: delete code to pull data into pools
7540:  051278bf89979 <    -:  ------------- random: remove kernel.random.read_wakeup_threshold
7541:  ea13b4ac6a312 <    -:  ------------- random: remove unnecessary unlikely()
7542:  5088389a9158c <    -:  ------------- random: convert to ENTROPY_BITS for better code readability
7543:  8edfa1c6c05b1 <    -:  ------------- random: Add and use pr_fmt()
7544:  a15f8c15ed979 <    -:  ------------- random: fix typo in add_timer_randomness()
7545:  03fafcef471a8 <    -:  ------------- random: remove some dead code of poolinfo
7546:  b0a6d6a76a2fe <    -:  ------------- random: split primary/secondary crng init paths
7547:  c5948834b0c42 <    -:  ------------- random: avoid warnings for !CONFIG_NUMA builds
7548:  3ebd5da615c02 <    -:  ------------- x86: Remove arch_has_random, arch_has_random_seed
7549:  1cb0d7df9bdbe <    -:  ------------- powerpc: Remove arch_has_random, arch_has_random_seed
7550:  596bcf5911e61 <    -:  ------------- s390: Remove arch_has_random, arch_has_random_seed
7551:  cacc99ee5a9c1 <    -:  ------------- linux/random.h: Remove arch_has_random, arch_has_random_seed
7552:  b7d3392a0ded4 <    -:  ------------- linux/random.h: Use false with bool
7553:  4682b96e868b6 <    -:  ------------- linux/random.h: Mark CONFIG_ARCH_RANDOM functions __must_check
7554:  3d80af75c13cb <    -:  ------------- powerpc: Use bool in archrandom.h
7555:  6aa1f386ebcf6 <    -:  ------------- random: add arch_get_random_*long_early()
7556:  1fb7c4dac63d1 <    -:  ------------- random: avoid arch_get_random_seed_long() when collecting IRQ randomness
7557:  5ab8e04f6da26 <    -:  ------------- random: remove dead code left over from blocking pool
7558:  9404e8c983db0 <    -:  ------------- MAINTAINERS: co-maintain random.c
7559:  34dc98ce21995 <    -:  ------------- crypto: blake2s - include <linux/bug.h> instead of <asm/bug.h>
7560:  b44b759b625d4 <    -:  ------------- crypto: blake2s - adjust include guard naming
7561:  5cdbdd83c7932 <    -:  ------------- random: document add_hwgenerator_randomness() with other input functions
7562:  5a0fda8f1b6a6 <    -:  ------------- random: remove unused irq_flags argument from add_interrupt_randomness()
7563:  1f89b3175be82 <    -:  ------------- random: use BLAKE2s instead of SHA1 in extraction
7564:  eaa94d939f2f5 <    -:  ------------- random: do not sign extend bytes for rotation when mixing
7565:  e59fd7eb5ca08 <    -:  ------------- random: do not re-init if crng_reseed completes before primary init
7566:  66794cda8a8f7 <    -:  ------------- random: mix bootloader randomness into pool
7567:  5d3c00a79b3e7 <    -:  ------------- random: harmonize "crng init done" messages
7568:  048cc34c4cdf8 <    -:  ------------- random: use IS_ENABLED(CONFIG_NUMA) instead of ifdefs
7569:  84647efd92bfb <    -:  ------------- random: initialize ChaCha20 constants with correct endianness
7570:  4d4b3fc01e0fe <    -:  ------------- random: early initialization of ChaCha constants
7571:  d15b7abb41918 <    -:  ------------- random: avoid superfluous call to RDRAND in CRNG extraction
7572:  28601bec7c3f5 <    -:  ------------- random: don't reset crng_init_cnt on urandom_read()
7573:  da31a02410eff <    -:  ------------- random: fix typo in comments
7574:  45b1bfbd54bc1 <    -:  ------------- random: cleanup poolinfo abstraction
7575:  91393740d75fd <    -:  ------------- crypto: chacha20 - Fix chacha20_block() keystream alignment (again)
7576:  f450937d22e63 <    -:  ------------- random: cleanup integer types
7577:  0c8cc8dbe8eaa <    -:  ------------- random: remove incomplete last_data logic
7578:  ac800f0b08577 <    -:  ------------- random: remove unused extract_entropy() reserved argument
7579:  482583b75f5f0 <    -:  ------------- random: try to actively add entropy rather than passively wait for it
7580:  55349296ba9b0 <    -:  ------------- random: rather than entropy_store abstraction, use global
7581:  3653dd775a924 <    -:  ------------- random: remove unused OUTPUT_POOL constants
7582:  9199cebaf68be <    -:  ------------- random: de-duplicate INPUT_POOL constants
7583:  a88fa6c02cb18 <    -:  ------------- random: prepend remaining pool constants with POOL_
7584:  563845199476a <    -:  ------------- random: cleanup fractional entropy shift constants
7585:  166f9970b82af <    -:  ------------- random: access input_pool_data directly rather than through pointer
7586:  5c539eee39b2d <    -:  ------------- random: simplify arithmetic function flow in account()
7587:  35e312919dd97 <    -:  ------------- random: continually use hwgenerator randomness
7588:  7beef135045b3 <    -:  ------------- random: access primary_pool directly rather than through pointer
7589:  7ad714b9dced9 <    -:  ------------- random: only call crng_finalize_init() for primary_crng
7590:  ccf535b5077a2 <    -:  ------------- random: use computational hash for entropy extraction
7591:  62a2b4bd3ec9e <    -:  ------------- random: simplify entropy debiting
7592:  bb375abdbf116 <    -:  ------------- random: use linear min-entropy accumulation crediting
7593:  f82262f273f1b <    -:  ------------- random: always wake up entropy writers after extraction
7594:  6605171cd8cb9 <    -:  ------------- random: make credit_entropy_bits() always safe
7595:  8c39bfd9db3c6 <    -:  ------------- random: remove use_input_pool parameter from crng_reseed()
7596:  839a45e6864da <    -:  ------------- random: remove batched entropy locking
7597:  909f3974c58c2 <    -:  ------------- random: fix locking in crng_fast_load()
7598:  d0841f7e4ae67 <    -:  ------------- random: use RDSEED instead of RDRAND in entropy extraction
7599:  13c423b6b1d3a <    -:  ------------- random: inline leaves of rand_initialize()
7600:  4ceb0d570cf9c <    -:  ------------- random: ensure early RDSEED goes through mixer on init
7601:  2d9c1b42a51c0 <    -:  ------------- random: do not xor RDRAND when writing into /dev/random
7602:  5a595c18329ee <    -:  ------------- random: absorb fast pool into input pool after fast load
7603:  acbf6f4851e3d <    -:  ------------- random: use hash function for crng_slow_load()
7604:  21682884c699e <    -:  ------------- random: remove outdated INT_MAX >> 6 check in urandom_read()
7605:  93ce4028c4e2b <    -:  ------------- random: zero buffer after reading entropy from userspace
7606:  15c96d9cb50df <    -:  ------------- random: tie batched entropy generation to base_crng generation
7607:  f8a196cf47517 <    -:  ------------- random: remove ifdef'd out interrupt bench
7608:  707c01fe19eb2 <    -:  ------------- random: remove unused tracepoints
7609:  fabaab48f24c7 <    -:  ------------- random: add proper SPDX header
7610:  e0a5363f51f50 <    -:  ------------- random: deobfuscate irq u32/u64 contributions
7611:  65419e900306c <    -:  ------------- random: introduce drain_entropy() helper to declutter crng_reseed()
7612:  388e4979d6e16 <    -:  ------------- random: remove useless header comment
7613:  ee5705cffcc84 <    -:  ------------- random: remove whitespace and reorder includes
7614:  25061d366b706 <    -:  ------------- random: group initialization wait functions
7615:  2ee36c835e91e <    -:  ------------- random: group entropy extraction functions
7616:  496b91b6dc443 <    -:  ------------- random: group entropy collection functions
7617:  c3502a795f6ac <    -:  ------------- random: group userspace read/write functions
7618:  57332ead20e16 <    -:  ------------- random: group sysctl functions
7619:  b3fa3d153ad2d <    -:  ------------- random: rewrite header introductory comment
7620:  80adfc1fa6910 <    -:  ------------- random: defer fast pool mixing to worker
7621:  58e0c4ff5342e <    -:  ------------- random: do not take pool spinlock at boot
7622:  535d280612b5a <    -:  ------------- random: unify early init crng load accounting
7623:  5357d828bc6ab <    -:  ------------- random: check for crng_init == 0 in add_device_randomness()
7624:  57a23e728b087 <    -:  ------------- random: pull add_hwgenerator_randomness() declaration into random.h
7625:  40b5b4b62203c <    -:  ------------- random: clear fast pool, crng, and batches in cpuhp bring up
7626:  23fc6dcd2935d <    -:  ------------- random: round-robin registers as ulong, not u32
7627:  430374f42c217 <    -:  ------------- random: only wake up writers after zap if threshold was passed
7628:  55add4d8bc322 <    -:  ------------- random: cleanup UUID handling
7629:  ddb672cf1d04d <    -:  ------------- random: unify cycles_t and jiffies usage and types
7630:  3e3d705c7e9ec <    -:  ------------- random: do crng pre-init loading in worker rather than irq
7631:  dd9970a9e068a <    -:  ------------- random: give sysctl_random_min_urandom_seed a more sensible value
7632:  d2c884e41bc5d <    -:  ------------- random: don't let 644 read-only sysctls be written to
7633:  c8e06a4dc297e <    -:  ------------- random: replace custom notifier chain with standard one
7634:  d9a694a92c210 <    -:  ------------- random: use SipHash as interrupt entropy accumulator
7635:  f629607339682 <    -:  ------------- random: make consistent usage of crng_ready()
7636:  052377053c319 <    -:  ------------- random: reseed more often immediately after booting
7637:  2e7ef351ea331 <    -:  ------------- random: check for signal and try earlier when generating entropy
7638:  df5104c1d0b6a <    -:  ------------- random: skip fast_init if hwrng provides large chunk of entropy
7639:  eed01a6b3e563 <    -:  ------------- random: treat bootloader trust toggle the same way as cpu trust toggle
7640:  cd852448d59e9 <    -:  ------------- random: re-add removed comment about get_random_{u32,u64} reseeding
7641:  bba3aac2241f5 <    -:  ------------- random: mix build-time latent entropy into pool at init
7642:  8a4646c15d4fb <    -:  ------------- random: do not split fast init input in add_hwgenerator_randomness()
7643:  04d681d81b7df <    -:  ------------- random: do not allow user to keep crng key around on stack
7644:  cf8136b351692 <    -:  ------------- random: check for signal_pending() outside of need_resched() check
7645:  50339a2aab7e0 <    -:  ------------- random: check for signals every PAGE_SIZE chunk of /dev/[u]random
7646:  4fab8d784338f <    -:  ------------- random: make random_get_entropy() return an unsigned long
7647:  8005202686bd8 <    -:  ------------- random: document crng_fast_key_erasure() destination possibility
7648:  70e65f65f2489 <    -:  ------------- random: fix sysctl documentation nits
7649:  4798c86f1b70e <    -:  ------------- init: call time_init() before rand_initialize()
7650:  e154c03c323e2 <    -:  ------------- ia64: define get_cycles macro for arch-override
7651:  0da28452ba041 <    -:  ------------- s390: define get_cycles macro for arch-override
7652:  faf62b743975f <    -:  ------------- parisc: define get_cycles macro for arch-override
7653:  d969c9880bafd <    -:  ------------- alpha: define get_cycles macro for arch-override
7654:  0a182df6e951b <    -:  ------------- powerpc: define get_cycles macro for arch-override
7655:  2142a4d898519 <    -:  ------------- timekeeping: Add raw clock fallback for random_get_entropy()
7656:  63959c5833eca <    -:  ------------- m68k: use fallback for random_get_entropy() instead of zero
7657:  abb6b7e172e91 <    -:  ------------- mips: use fallback for random_get_entropy() instead of just c0 random
7658:  7605b26520095 <    -:  ------------- arm: use fallback for random_get_entropy() instead of zero
7659:  f869f2e72e81e <    -:  ------------- nios2: use fallback for random_get_entropy() instead of zero
7660:  4373bcb96fcc5 <    -:  ------------- x86/tsc: Use fallback for random_get_entropy() instead of zero
7661:  d78483f5fe85c <    -:  ------------- um: use fallback for random_get_entropy() instead of zero
7662:  ac7fbc3df2ed9 <    -:  ------------- sparc: use fallback for random_get_entropy() instead of zero
7663:  cf8717e15a9e2 <    -:  ------------- xtensa: use fallback for random_get_entropy() instead of zero
7664:  70cf7fb6d379e <    -:  ------------- random: insist on random_get_entropy() existing in order to simplify
7665:  fed6de0e0bac9 <    -:  ------------- random: do not use batches when !crng_ready()
7666:  71db23726a773 <    -:  ------------- random: do not pretend to handle premature next security model
7667:  e4728fd103ded <    -:  ------------- random: order timer entropy functions below interrupt functions
7668:  18aa432eb1e04 <    -:  ------------- random: do not use input pool from hard IRQs
7669:  eb2fb9672be83 <    -:  ------------- random: help compiler out with fast_mix() by using simpler arguments
7670:  66b2dde034bdc <    -:  ------------- siphash: use one source of truth for siphash permutations
7671:  4ddc38d39e7f9 <    -:  ------------- random: use symbolic constants for crng_init states
7672:  0251a5fd3c69a <    -:  ------------- random: avoid initializing twice in credit race
7673:  319b965f9f19a <    -:  ------------- random: remove ratelimiting for in-kernel unseeded randomness
7674:  1bed234f23cdc <    -:  ------------- random: use proper jiffies comparison macro
7675:  b16b1b66b7d47 <    -:  ------------- random: handle latent entropy and command line from random_init()
7676:  37fe03f2708ed <    -:  ------------- random: credit architectural init the exact amount
7677:  b0eabe217548a <    -:  ------------- random: use static branch for crng_ready()
7678:  c24fb5a30cd03 <    -:  ------------- random: remove extern from functions in header
7679:  25f97736b67d6 <    -:  ------------- random: use proper return types on get_random_{int,long}_wait()
7680:  d77e58eef686f <    -:  ------------- random: move initialization functions out of hot pages
7681:  225c0df138c2d <    -:  ------------- random: move randomize_page() into mm where it belongs
7682:  17685dd543f9c <    -:  ------------- random: convert to using fops->write_iter()
7683:  72389322c99c2 <    -:  ------------- random: wire up fops->splice_{read,write}_iter()
7684:  09b3d3579fd3f <    -:  ------------- random: check for signals after page of pool writes
7685:  fcff2416844d9 <    -:  ------------- Revert "random: use static branch for crng_ready()"
7686:  0c03d07329480 <    -:  ------------- crypto: drbg - add FIPS 140-2 CTRNG for noise source
7687:  80bc8308b5fff <    -:  ------------- crypto: drbg - always seeded with SP800-90B compliant noise source
7688:  b1fb007ad8dbd <    -:  ------------- crypto: drbg - prepare for more fine-grained tracking of seeding state
7689:  b05392dc67af9 <    -:  ------------- crypto: drbg - track whether DRBG was seeded with !rng_is_initialized()
7690:  31a5afe0696ca <    -:  ------------- crypto: drbg - move dynamic ->reseed_threshold adjustments to __drbg_seed()
7691:  eb86176aea774 <    -:  ------------- crypto: drbg - always try to free Jitter RNG instance
7692:  9ed7b5bf2c4ce <    -:  ------------- crypto: drbg - make reseeding from get_random_bytes() synchronous
7693:  aafc845f74e40 <    -:  ------------- random: avoid checking crng_ready() twice in random_init()
7694:  5e70c1a8eea10 <    -:  ------------- random: mark bootloader randomness code as __init
7695:  d4bfd4858d28f <    -:  ------------- random: account for arch randomness in bits
7710:  7112098b69d59 <    -:  ------------- random: credit cpu and bootloader seeds by default
7741:  1085f8d943457 <    -:  ------------- BACKPORT: l2tp: don't use inet_shutdown on ppp session destroy
7742:  035eef00b66d5 <    -:  ------------- BACKPORT: l2tp: fix race in pppol2tp_release with session object destroy
7750:  f2944c94eb2b0 <    -:  ------------- random: schedule mix_interrupt_randomness() less often
7753:  97e6ead027e6f <    -:  ------------- random: quiet urandom warning ratelimit suppression message
7781:  2d83b6548a43b <    -:  ------------- fdt: Update CRC check for rng-seed
7786:  c46a7693636bf <    -:  ------------- UPSTREAM: mm/ksm: Remove reuse_ksm_page()
7787:  bbf3469321c5e <    -:  ------------- BACKPORT: mm: do_wp_page() simplification
7788:  437e22dcba3b7 <    -:  ------------- UPSTREAM: mm: fix misplaced unlock_page in do_wp_page()
7792:  836a2cea5b226 <    -:  ------------- s390/archrandom: simplify back to earlier design and initialize earlier
7818:  2c66b0c95bb0a <    -:  ------------- esp: limit skb_page_frag_refill use to a single page
7847:  f4a5311dfd1cb <    -:  ------------- xhci: make xhci_handshake timeout for xhci_reset() adjustable
7896:  df4cb7f30e831 <    -:  ------------- Revert "Revert "char/random: silence a lockdep splat with printk()""
7924:  fd174ecef9350 <    -:  ------------- s390/archrandom: prevent CPACF trng invocations in interrupt context
7961:  9d5fec6ba2e41 <    -:  ------------- arm64: fix oops in concurrently setting insn_emulation sysctls
8178:  3c2ae48eceaa4 <    -:  ------------- arm64: map FDT as RW for early_init_dt_scan()
8207:  229f47603dd30 <    -:  ------------- binder: fix UAF of ref->proc caused by race condition
8244:  6ce66e3442a59 <    -:  ------------- netfilter: nf_conntrack_irc: Fix forged IP logic
8250:  967d57368d9a4 <    -:  ------------- usb: dwc3: fix PHY disable sequence
8286:  dbd64cf46c8a1 <    -:  ------------- netfilter: nf_conntrack_irc: Tighten matching on DCC message
8338:  12faed72cf1a7 <    -:  ------------- rpmsg: qcom: glink: replace strncpy() with strscpy_pad()
8344:  ec0541c659e00 <    -:  ------------- random: clamp credited irq bits to maximum mixed
8348:  1d6db2ce2ebc1 <    -:  ------------- random: restore O_NONBLOCK support
8349:  ed780fa488de9 <    -:  ------------- random: avoid reading two cache lines on irq randomness
8353:  1426ff001bb2f <    -:  ------------- random: use expired timer rather than wq for mixing fast pool
8370:  6c3da8c0a35bb <    -:  ------------- nilfs2: fix lockdep warnings in page operations for btree nodes
8371:  4799a8c35e768 <    -:  ------------- nilfs2: fix lockdep warnings during disk space reclamation
8452:  fc0ce27192c9b <    -:  ------------- spmi: pmic-arb: correct duplicate APID to PPID mapping logic

Commits not in https://android.googlesource.com/kernel/common
android-4.14-stable (some as the new loop ioctl, are from android-4.14-q):

   -:  ------------- >    1:  225e67d5a456a BACKPORT: Documentation/llvm: add documentation on building w/ Clang/LLVM
   -:  ------------- >    2:  a58a5aa168f7e BACKPORT: Documentation/llvm: fix the name of llvm-size
   -:  ------------- >    3:  4705a90c05519 BACKPORT: kbuild: replace AS=clang with LLVM_IAS=1
   -:  ------------- >    4:  bf321b4c00f12 BACKPORT: kbuild: support LLVM=1 to switch the default tools to Clang/LLVM
   -:  ------------- >    5:  4de5acbd84e87 BACKPORT: crypto: arm64/aes-modes - get rid of literal load of addend vector
   -:  ------------- >    6:  16fcad7c685b9 BACKPORT: arm64: Change .weak to SYM_FUNC_START_WEAK_PI for arch/arm64/lib/mem*.S
   -:  ------------- >    7:  9f57d25399131 arm64: vdso: remove commas between macro name and arguments
   -:  ------------- >    8:  18b5f71e2bd64 kbuild: clear LDFLAGS in the top Makefile
   -:  ------------- >    9:  561635be90fbd kbuild: use HOSTLDFLAGS for single .c executables
   -:  ------------- >   10:  8e7e48e4e699d platform: msm: gsi: Export symbols only if compiled as module
   -:  ------------- >   11:  ff948bd25c007 Revert "selinux: Relocate selinux_enforcing to a separate 4k page"
   -:  ------------- >   12:  2e1bfa1797d9a erofs: lz4armv8: Make it compile with IAS
   -:  ------------- >   13:  72fabe24ff307 ext4: readpages() should submit IO as read-ahead
   -:  ------------- > 1188:  3098e65c0c7a9 net: refactor bind_bucket fastreuse into helper
   -:  ------------- > 1287:  43dddbf0ad9a1 ext4: fix checking of directory entry validity for inline directories
   -:  ------------- > 1413:  8c99a25f964ad ANDROID: overflow.h: fix merge issue with 4.14.196
   -:  ------------- > 1561:  3b6fc8a143c09 f2fs: fix indefinite loop scanning for free nid
   -:  ------------- > 3259:  09c0874d21d53 net: icmp: pass zeroed opts from icmp{,v6}_ndo_send before sending fixup
   -:  ------------- > 3324:  e2c009cd9295c net: Fix gro aggregation for udp encaps with zero csum
   -:  ------------- > 5253:  2f44badae0665 lib/timerqueue: Rely on rbtree semantics for next timer fixup
   -:  ------------- > 5413:  b7e12a215c960 binder: use euid from cred instead of using task
   -:  ------------- > 6299:  926bfeba37173 usb: dwc3: gadget: Let the interrupt handler disable bottom halves.
   -:  ------------- > 7686:  b9aea65979272 mm/rmap: Fix anon_vma->degree ambiguity leading to double-reuse fixup
   -:  ------------- > 8001:  207bfa8031d2a BACKPORT: loop: change queue block size to match when using DIO
   -:  ------------- > 8003:  bfcc6d8d3e882 BACKPORT: loop: Call loop_config_discard() only after new config is applied
   -:  ------------- > 8004:  03a94f795e90b BACKPORT: loop: Remove sector_t truncation checks
   -:  ------------- > 8005:  c8d522e856ff0 BACKPORT: loop: Factor out setting loop device size
   -:  ------------- > 8006:  4436beb401d50 BACKPORT: loop: Refactor loop_set_status() size calculation
   -:  ------------- > 8007:  dd4123735f37b BACKPORT: loop: Remove figure_loop_size()
   -:  ------------- > 8008:  45e93cc525214 BACKPORT: loop: Factor out configuring loop from status
   -:  ------------- > 8009:  1b1b59fa2e1b2 BACKPORT: loop: Move loop_set_status_from_info() and friends up
   -:  ------------- > 8010:  6f14a4abdb397 BACKPORT: loop: Rework lo_ioctl() __user argument casting
   -:  ------------- > 8011:  d54438a2eb181 BACKPORT: loop: Clean up LOOP_SET_STATUS lo_flags handling
   -:  ------------- > 8012:  451ef0ecafd9a BACKPORT: loop: Add LOOP_CONFIGURE ioctl
   -:  ------------- > 8013:  1198c4fb6948f BACKPORT: loop: Fix wrong masking of status flags
   -:  ------------- > 8014:  295ee79dc608c BACKPORT: loop: Set correct device size when using LOOP_CONFIGURE
   -:  ------------- > 8026:  69188cbac8494 fs: fix lazytime expiration handling in __writeback_single_inode()
   -:  ------------- > 8027:  f3bea0c658e36 fscrypt: don't ignore minor_hash when hash is 0
   -:  ------------- > 8028:  3f137c2ff19d8 events: Reuse value read using READ_ONCE instead of re-reading it
   -:  ------------- > 8040:  d446080332178 dm verity: set DM_TARGET_IMMUTABLE feature flag
   -:  ------------- > 8045:  274ceee6727c0 mm: gup: COR: copy-on-read fault
   -:  ------------- > 8046:  b44a012937926 mm: gup: gup_must_unshare()
   -:  ------------- > 8047:  53fff647e7956 mm: gup: gup_must_unshare() use can_read_pin_swap_page()
   -:  ------------- > 8048:  f0e9ae6cc3e6c mm: gup: FOLL_UNSHARE
   -:  ------------- > 8049:  8cd178e7e8a0f mm: gup: FOLL_NOUNSHARE: optimize follow_page
   -:  ------------- > 8050:  493b8590ccf8e mm: COW: skip the page lock in the COW copy path
   -:  ------------- > 8051:  ddd39e51bfd84 Revert "gup: document and work around "COW can break either way" issue"
   -:  ------------- > 8052:  4bd1b27b2dddc mm: mprotect: avoid spurious COW faults for exclusive anon pages in cow mapping
   -:  ------------- > 8053:  d3bc6ace9e5d0 mm: use_mm: fix for arches checking mm_users to optimize TLB flushes
   -:  ------------- > 8054:  4d633ce99fd7e arm64: tlb: skip tlbi broadcast
   -:  ------------- > 8055:  1f389368b335f mm: cacheline alignment for page_table_lock and mmap_lock
   -:  ------------- > 8056:  3b32897283fe4 mm: THP: preserved young bit in the THP split
   -:  ------------- > 8057:  b4315be1bb5ba tweak config for lineageos 20
   -:  ------------- > 8058:  e9246ac7cff38 enable pid namespaces

git range-diff --no-patch 816f245a4e2afc92ac6119852e33524858410c41..c8ea89af5fe4bbde4c39f73c64245b6d0c455bbd b2aa890109a77a55757cca50a7509bd81899f5af..e9246ac7cff3881461b3b5d7d8c6f5bba65850ce

   1:  7529068a775e7 <    -:  ------------- f2fs: refactor resize_fs to avoid meta updates in progress
   2:  9015e363e6fa8 <    -:  ------------- f2fs: fix missing check for f2fs_unlock_op
   3:  86556e67a9fde <    -:  ------------- ANDROID: mmc: MMC crypto API
   4:  7a3e0cb384d3b <    -:  ------------- ANDROID: Add padding for crypto related structs in UFS and MMC
   -:  ------------- >    1:  225e67d5a456a BACKPORT: Documentation/llvm: add documentation on building w/ Clang/LLVM
   -:  ------------- >    2:  a58a5aa168f7e BACKPORT: Documentation/llvm: fix the name of llvm-size
   -:  ------------- >    3:  4705a90c05519 BACKPORT: kbuild: replace AS=clang with LLVM_IAS=1
   -:  ------------- >    4:  bf321b4c00f12 BACKPORT: kbuild: support LLVM=1 to switch the default tools to Clang/LLVM
   -:  ------------- >    5:  4de5acbd84e87 BACKPORT: crypto: arm64/aes-modes - get rid of literal load of addend vector
   -:  ------------- >    6:  16fcad7c685b9 BACKPORT: arm64: Change .weak to SYM_FUNC_START_WEAK_PI for arch/arm64/lib/mem*.S
   -:  ------------- >    7:  9f57d25399131 arm64: vdso: remove commas between macro name and arguments
   -:  ------------- >    8:  18b5f71e2bd64 kbuild: clear LDFLAGS in the top Makefile
   -:  ------------- >    9:  561635be90fbd kbuild: use HOSTLDFLAGS for single .c executables
   -:  ------------- >   10:  8e7e48e4e699d platform: msm: gsi: Export symbols only if compiled as module
   -:  ------------- >   11:  ff948bd25c007 Revert "selinux: Relocate selinux_enforcing to a separate 4k page"
   -:  ------------- >   12:  2e1bfa1797d9a erofs: lz4armv8: Make it compile with IAS
   -:  ------------- >   13:  72fabe24ff307 ext4: readpages() should submit IO as read-ahead
   5:  d6d152b9ff268 !   14:  7b696e5d7a537 ANDROID: cuttlefish_defconfig: enable CONFIG_MMC_CRYPTO
   6:  f79525dda67e7 !   15:  956a6785d3596 ANDROID: cuttlefish_defconfig: Enable CONFIG_STATIC_USERMODEHELPER
   7:  b8cdb45351d93 <    -:  ------------- ANDROID: dm-default-key: Update key size for wrapped keys
   8:  25849e1066e86 !   16:  7760f0fa5398e ANDROID: hid: steam: remove BT controller matching
   9:  72091967bfbbc <    -:  ------------- ANDROID: block: backport the ability to specify max_dun_bytes
  10:  8711e464f7dfc <    -:  ------------- ANDROID: dm-default-key: set dun_bytes more precisely
  11:  6be68d89b4d52 <    -:  ------------- ANDROID: fscrypt: set dun_bytes more precisely
  12:  75acb7a59dc4d !   17:  3f8c955b31166 UPSTREAM: HID: steam: Fix input device disappearing
  13:  9bbb91899906f <    -:  ------------- Revert "f2fs: refactor resize_fs to avoid meta updates in progress"
  14:  c62296ef40570 <    -:  ------------- ANDROID: Incremental fs: Avoid continually recalculating hashes
  15:  6e1790888863e <    -:  ------------- ANDROID: Incremental fs: Fix scheduling while atomic error
  16:  1c8f02e0a7d8e <    -:  ------------- ANDROID: Incremental fs: wake up log pollers less often
  17:  da5a022e8080a !   18:  dcf55b841d416 ANDROID: cuttlefish_defconfig: Enable net testing options
  18:  dabf068133d59 <    -:  ------------- FROMLIST: x86_64: fix jiffies ODR violation
 423:  4d9cdf7243a2b !   19:  765792082aceb x86_64: Fix jiffies ODR violation
  19:  565a986f11a94 !   20:  cdd37fbe247b3 ANDROID: clang: update to 11.0.1
  20:  9abaaca262dce !   21:  4a9ac921d7486 f2fs: don't leak filename in f2fs_try_convert_inline_dir()
  21:  89b228375922d <    -:  ------------- f2fs: split f2fs_d_compare() from f2fs_match_name()
  22:  77b2eab3542d2 <    -:  ------------- f2fs: rework filename handling
  23:  f8a8368ae70a8 <    -:  ------------- f2fs: fix checkpoint=disable:%u%%
  25:  3289192145a01 !   22:  eaf5d3976cc4a f2fs: Use the correct style for SPDX License Identifier
  26:  a73baecd77952 !   23:  5d5f7022cb2e7 f2fs: use strcmp() in parse_options()
  24:  2116cb420405f !   24:  ef1b58c946b02 f2fs: flush dirty meta pages when flushing them
  27:  73bfe5dfd09dc !   25:  0849ca0e0e62b f2fs: remove redundant compress inode check
  28:  b390210e01269 !   26:  6934ede641dff f2fs: support partial truncation on compressed inode
  29:  066c14e56683e !   27:  3275675d8704c f2fs: support fiemap on compressed inode
  30:  1856ffe96fccf !   28:  87c16cf9db385 f2fs: introduce f2fs_bmap_compress()
  31:  32328eaa3f46e !   29:  aefd87c1755eb f2fs: introduce mempool for {,de}compress intermediate page allocation
  32:  3f1146caa34db !   30:  472df569fed8c f2fs: correctly fix the parent inode number during fsync()
  33:  c768e67501d58 !   31:  a81b53c178551 f2fs: shrink spinlock coverage
  34:  25544ed1f9dd2 !   32:  aaff901146810 f2fs: introduce F2FS_IOC_RELEASE_COMPRESS_BLOCKS
  35:  30796f18dc525 <    -:  ------------- f2fs: remove blk_plugging in block_operations
  36:  61163cba00356 !   33:  db914aa724752 f2fs: compress: let lz4 compressor handle output buffer budget properly
  37:  9f25700da34b8 !   34:  e9c35802ea908 f2fs: Fix wrong stub helper update_sit_info
  38:  cd74e150aea89 <    -:  ------------- f2fs: report delalloc reserve as non-free in statfs for project quota
 617:  6053683077c6d !   35:  5169c30466f7e f2fs: report delalloc reserve as non-free in statfs for project quota
  39:  82cc5e607b56a !   36:  a1790d73f56db f2fs: Avoid double lock for cp_rwsem during checkpoint
  40:  2cf3a3e7bffd6 !   37:  aca1848d2712e f2fs: introduce F2FS_IOC_RESERVE_COMPRESS_BLOCKS
  41:  eb7dd3a62bc0b !   38:  852f048714804 f2fs: use round_up to enhance calculation
  42:  963d404e8894c <    -:  ------------- f2fs: refactor resize_fs to avoid meta updates in progress
  43:  a884feeebdbb9 !   39:  88851e0fb86e0 f2fs: remove redundant assignment to variable err
  44:  8d8b720ea93db !   40:  b35e101a5556c f2fs: compress: don't handle non-compressed data in workqueue
  45:  96d6e3f043738 !   41:  3be1a15a23669 f2fs: fix potential use-after-free issue
  46:  bdd18b05940fb !   42:  a920bc8ff9e59 f2fs: add compressed/gc data read IO stat
  47:  e00cdb19a870e !   43:  afad49063b861 f2fs: compress: fix zstd data corruption
  48:  ceaceed21f75a !   44:  b3100efe42754 USB: serial: qcserial: Add DW5816e support
  49:  21c3b07f6bc86 !   45:  aeac8d8dd28d6 dp83640: reverse arguments to list_add_tail
  50:  9f72c9a9da12d !   46:  8d2199a12efa0 fq_codel: fix TCA_FQ_CODEL_DROP_BATCH_SIZE sanity checks
  51:  93f18b82d5e4a !   47:  c31f780886c21 net: macsec: preserve ingress frame ordering
  52:  8d50559b5c8af !   48:  6c6c5d18d9b57 net/mlx4_core: Fix use of ENOSPC around mlx4_counter_alloc()
  53:  d6c0e9ea1c807 !   49:  ab13d5ae51cc0 net: usb: qmi_wwan: add support for DW5816e
  54:  4836eb6b59657 !   50:  c12a8fab5ce58 sch_choke: avoid potential panic in choke_reset()
  55:  9945949908fe1 !   51:  2e22aa7090929 sch_sfq: validate silly quantum values
  56:  20d19a13f8c84 !   52:  49ef8923fcbc8 bnxt_en: Fix VLAN acceleration handling in bnxt_fix_features().
  57:  50387588085e0 !   53:  0bffd222a006e net/mlx5: Fix forced completion access non initialized command entry
  58:  c53246b7a0432 !   54:  646fc35c5a494 net/mlx5: Fix command entry leak in Internal Error State
  59:  7766a0a884ce4 !   55:  2be0605cc3598 bnxt_en: Improve AER slot reset.
  60:  51e8517b44aff !   56:  9d5625b8c406d bnxt_en: Fix VF anti-spoof filter setup.
  61:  a0c23ec2171f9 !   57:  fa0a18b05e37a net: stricter validation of untrusted gso packets
  62:  ff16096314546 !   58:  ff9df03f5f48d ipv6: fix cleanup ordering for ip6_mr failure
  63:  7c5aafc7bfb99 !   59:  c0a5a8643899a HID: wacom: Read HID_DG_CONTACTMAX directly for non-generic devices
  64:  556bf5ffb401a !   60:  c01c296bc4f12 geneve: only configure or fill UDP_ZERO_CSUM6_RX/TX info when CONFIG_IPV6
  65:  2079ed06852f3 !   61:  9349e64f79a0d HID: usbhid: Fix race between usbhid_close() and usbhid_stop()
  66:  9cdab0743f843 !   62:  81faaf8af755a USB: uas: add quirk for LaCie 2Big Quadra
  67:  a7d5a1deb95a1 !   63:  f442a05b55365 USB: serial: garmin_gps: add sanity checking for data length
  68:  4d9c4f41d8bf5 !   64:  fae5e76dc0993 tracing: Add a vmalloc_sync_mappings() for safe measure
  69:  91017f1ac3b63 !   65:  18af1250a7f0a KVM: arm: vgic: Fix limit condition when writing to GICD_I[CS]ACTIVER
  70:  8eb8d55de8114 !   66:  86dcf3019f06b mm/page_alloc: fix watchdog soft lockups during set_zone_contiguous()
  71:  ff6c4721758a3 !   67:  a7bfd768b018f coredump: fix crash when umh is disabled
  72:  8eacda58b60ca !   68:  3f5e510f4bca9 batman-adv: fix batadv_nc_random_weight_tq
  73:  62c373550b168 !   69:  27cf08daf348f batman-adv: Fix refcnt leak in batadv_show_throughput_override
  74:  4bc6aa317fa8a !   70:  a5d5effccb83a batman-adv: Fix refcnt leak in batadv_store_throughput_override
  75:  81f4be8be78d5 !   71:  c819d81ce4daf batman-adv: Fix refcnt leak in batadv_v_ogm_process
  76:  e62991b7aaddc !   72:  01caffc2f4361 x86/entry/64: Fix unwind hints in kernel exit path
  77:  5c458931308a4 !   73:  3f12d8e18f370 x86/entry/64: Fix unwind hints in rewind_stack_do_exit()
  78:  73d90e8cd2420 !   74:  22a642c555fd0 x86/unwind/orc: Don't skip the first frame for inactive tasks
  79:  f5970988a8282 !   75:  c76f5b7bea35e x86/unwind/orc: Prevent unwinding before ORC initialization
  80:  2645ac77ba053 !   76:  ab3aa5b446887 x86/unwind/orc: Fix error path …

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[23b7daee59...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/23b7daee59100e34f488893b57cd3787a0c08b99)
#### Sunday 2022-11-06 02:53:13 by SkyratBot

[MIRROR] Simplifies SM damage calculation, tweaks the numbers. [MDB IGNORE] (#16733)

* Simplifies SM damage calculation, tweaks the numbers. (#70347)

About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

* Simplifies SM damage calculation, tweaks the numbers.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [overlord-bot/Overlord](https://github.com/overlord-bot/Overlord)@[f583fa74ae...](https://github.com/overlord-bot/Overlord/commit/f583fa74ae476b79e7e2f6890536f47146ec31b1)
#### Sunday 2022-11-06 05:36:34 by EggyRepublic

working recursive command parser

inputted scheduler commands are recursively parsed by popping off the top of each command list and executing any remaining commands

this allows one to write strings such as degree, computer science, print, fulfillment, add, 1, dat str
and the program will execute each command one by one as if they were typed separately.

currently uses a lock to prevent simultaneous command execution but you need to remember to unlock it prior to every return statement which is probably a pain in the ass so I'll have to figure something out.

---
## [PixlernBlitz03/android_frameworks_base](https://github.com/PixlernBlitz03/android_frameworks_base)@[b83b4c8d9c...](https://github.com/PixlernBlitz03/android_frameworks_base/commit/b83b4c8d9c1c4551ff64551fe2e9ec4389440e8b)
#### Sunday 2022-11-06 06:47:49 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2
Co-authored-by: kondors1995 <normandija1945@gmail.com>
Co-authored-by: naveenjohnsonv <14140949+naveenjohnsonv@users.noreply.github.com>
Co-authored-by: markakash <akashniki@gmail.com>
Co-authored-by: ReallySnow <kawaii.loli@reallysnow.moe>

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[9a7953e875...](https://github.com/thecsw/thecsw.github.io/commit/9a7953e875dd2532dfc8420face6f8cfca8dfb37)
#### Sunday 2022-11-06 06:48:56 by Ubuntu

[ASTRIE] Added a new fortune: ** 310; 12022 H.E.

“at the end of the day, rascal may not dream of bunny girl senpai, but dear lord I fucking do”

-- Jame, bestie

---
## [Ring-0-Productions/reactos](https://github.com/Ring-0-Productions/reactos)@[f30d79e4c8...](https://github.com/Ring-0-Productions/reactos/commit/f30d79e4c88497de4ddbf71badeba9e94ae50710)
#### Sunday 2022-11-06 06:59:13 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [Stalkeros2/tgstation](https://github.com/Stalkeros2/tgstation)@[91f02f2a6b...](https://github.com/Stalkeros2/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Sunday 2022-11-06 07:03:29 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[a00425f4fd...](https://github.com/re621/dnpcache/commit/a00425f4fdfcffd96914db845f5a0f99e881695f)
#### Sunday 2022-11-06 08:38:26 by bitWolfy

Remove 982 artists from the DNP list.

Removed: kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, cudacore, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, vahldem_sol, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, devildjmachine, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [morning-night-dream/platform](https://github.com/morning-night-dream/platform)@[3b9a0d30f8...](https://github.com/morning-night-dream/platform/commit/3b9a0d30f86e3a062d8dd77ca24f5f7ace7d6318)
#### Sunday 2022-11-06 09:35:52 by takokun

Merge pull request #96 from morning-night-dream/feature/issue#90

#90 cockroachの環境構築を修正

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[7cb69c2a8b...](https://github.com/ThePiachu/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Sunday 2022-11-06 10:57:03 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [frostg-012/kernel_xiaomi_chime-paranoid](https://github.com/frostg-012/kernel_xiaomi_chime-paranoid)@[38b0bd0f25...](https://github.com/frostg-012/kernel_xiaomi_chime-paranoid/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Sunday 2022-11-06 11:00:23 by Linus Torvalds

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
## [molototschek/oxen-core](https://github.com/molototschek/oxen-core)@[9c9552380d...](https://github.com/molototschek/oxen-core/commit/9c9552380ddecc57965e2e393454ef9d880cb803)
#### Sunday 2022-11-06 12:39:45 by Jason Rhinelander

Make hooks use exceptions on error rather than bool returns

bool returns suck in general, but in most cases here they are also a
pain in the ass because *each* place that returns false is also issuing
a log statement.  If only there were a way to return error information
to the common caller to have the common caller handle it... oh wait,
there is!

---
## [OverRaddit/WebServ](https://github.com/OverRaddit/WebServ)@[e289412d65...](https://github.com/OverRaddit/WebServ/commit/e289412d65b7e88995dff10a2204f70f0ac8e35c)
#### Sunday 2022-11-06 12:55:09 by Jinyoung Yoo

Merge pull request #36 from Rob-Yoo/master

FUCK YOU

---
## [antropod/tgstation](https://github.com/antropod/tgstation)@[83c75cac2c...](https://github.com/antropod/tgstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Sunday 2022-11-06 15:17:09 by Jacquerel

Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)



Goliaths, Legions, Watchers, and (as of recently) Bileworms all drop
something vaguely useful when they die.
Brimdemons and Lobstrosities do not. This PR aims to fix that, so that
there's at least some vague benefit to hunting them.

In this case it takes the form of organs you get when you butcher them,
similar to the regenerative core from Legions.
As they're similar to the regenerative core, I modified the regenerative
core to extend from a new common "monster core" typepath which these two
new organs also extend.
Like the regenerative core, both of these items do something when used
and something slightly different if you go to the effort of having
someone implant them into your body. They also decay over time, and you
can use stabilising serum to prevent this from happening.


https://user-images.githubusercontent.com/7483112/195967746-55a7d04d-224e-412d-aedc-3a0ec754db3d.mp4

The Rush Gland from the Lobstrosity lets you do a little impression of
their charging attack, making you run very fast for a handful of seconds
and ignoring slowdown effects. Unlike a lobstrosity you aren't actually
built to do this so if you run into a mob you will fall over, and if you
are doing this on the space station running into any dense object will
also make you fall over (it shouldn't make you _too_ much of a pain for
security to catch).
The idea here is that you use this to save time running back and forth
from the mining base.

The Brimdust Sac from the Brimdemon covers you in exploding dust. The
next three times you take Brute damage some of the dust will explode,
dealing damage equal to an unupgraded PKA shot to anything near you (but
not you).
If you do this in a space station not only is the damage proportionally
lower (still matching the PKA), but it _does_ effect you and also it
sets you on fire. You can remove the buff by showering it off.
The idea here is that you use this for minor revenge damage on enemies
whose attacks you don't manage to dodge.


https://user-images.githubusercontent.com/7483112/195967811-0b362ba9-2da0-42ac-bd55-3809473cbc74.mp4

If you implant the Rush Gland then you can use it once every 3 minutes
without consuming it, and the buff lasts very slightly longer. It will
automatically trigger itself if your health gets low, which might be
good (helps you escape a rough situation) or bad (didn't want to use it
yet).


https://user-images.githubusercontent.com/7483112/195967888-f63f7cbd-60cd-4309-8004-203afc5b2153.mp4

If you implant the Brimdust Sac then you can use it once every 3 minutes
to shake off cloud of dust which gives the buff to everyone nearby, if
you want to kit out your miner squad. The dust cloud also makes you
cough if you stand in it, and it's opaque. If you catch fire with this
organ inside you and aren't in mining atmosphere then it will explode
inside of your abdomen, which should probably be avoided, resultingly it
is very risky to use this on the space station.

---
## [dlandahl/theos](https://github.com/dlandahl/theos)@[d7949b8b04...](https://github.com/dlandahl/theos/commit/d7949b8b04b1c2a45c99338511f02008263446de)
#### Sunday 2022-11-06 16:01:21 by dlandahl

being able to view and compare all libraries from a centralized place is one of the main benefits of package managers. just being able to search "websocket" for example. I imagine jai could work without a real package manager but I think something to solve the problem of information centralization would still be necessary psdrndm — Today at 00:56 A searchable list of modules can be just that without all the negatives of a package manager MisterSkeltal — Today at 00:59 As soon as you have a searchable list of modules, you can run a script to download them, and then that list becomes a package manager, so I don't understand this comment. Maybe it doesn't do semantic versioning or whatever but that's an ancillary detail farzher — Today at 01:00 atm, sharing / using jai libraries is a huge mess that needs some solution. most installation instructions are: "download this code, rename the folder to JSON, and paste it into jai/modules directory" "oh and btw this code depends on the unicode_utils module, so do the same for that too" most people don't even store local copies because it's a bit too much effort to copy them everywhere manually, also then you're forced to use -import_dir or a metaprogram MisterSkeltal — Today at 01:02 JaIDE solves this farzher — Today at 01:02 if jai included -import_dir ./modules by default that'd be very useful, but still not enough psdrndm — Today at 01:20 I think there are more things than a list and a script to download items for it that are implicit in a thing called “package manager,” but maybe that’s just me Kuju — Today at 01:22 if youre arguing for no centralized management of repos at all itll just turn into the cpp free for all hellscape I thought at least it would be pretty agreed upon that the current method of download this repo and the dependencies and put them in the modules folder, isnt ideal MisterSkeltal — Today at 01:24 I am not arguing for that, I'm saying that the suggestion of "you don't need a package manager if you can look up code in a centralized location" is practically a package manager I agree that a package manager could be useful Kuju — Today at 01:27 ah thats not my preference. it feels like an awkward middle ground to me. I was adding onto what @psdrndm said that in the scenario described a searchable repo list is still a bonus (at the very least) almost feels like this whole discussion should be in syntax-suggestions or something :cool_think: MisterSkeltal — Today at 01:31 No, like, if you have a "searchable repo list" or whatever, and that searchable repo list has a canonical location of the source code of that repo, then someone can make a metaprogram which searches the repo list and downloads the source, recursing as necessary, and boom you have a package manager. It would probably be a good idea to have a package manager that is a bit better than this, because this is what will become the "package manager" once you have a repo list. I'm not a package manager expert, but I feel like this isn't going to be a good approach. It's likely just going to be like the current situation, but slightly more automated. ("but that's just all package managers!" har har) Andrew the hacker — Today at 04:07 Maybe it would be better to have the package manager integrated with version control rather than with the language. Something like a better version of git sub modules. So the language can stay agnostic to where any modules came from, and you don’t have two systems doing two layers of fetching and versioning.

---
## [NW360-DDR/MobileGameDesignTeamGame](https://github.com/NW360-DDR/MobileGameDesignTeamGame)@[9484289068...](https://github.com/NW360-DDR/MobileGameDesignTeamGame/commit/94842890686ad36a22e4dceb5574b3eee600afa6)
#### Sunday 2022-11-06 16:17:32 by Nathaniel Owens

Fixed HeadpatScript, Merged art to Main Branch

Changes:
 - Kiria's graphics merged to main branch, not sure how it wasn't, but I'll figure it out later.
 - Edited properties of the status bars due to my own incompetence in setting them correctly.
 - Headpat Script now works properly, and updates the friendship values accordingly.
 - Back Button now added so you can leave the Headpat Minigame.

Known Bugs:
 - Stats do not yet decay over time to emulate neglect of friend.
 - Cleanup Minigame logic needs to be redone to actually fully randomize the pellet spot placement.
 - Oh dear god I tried making an animation object and it blew up my Unity project I think I did something wrong.
 - Food Minigame logic still nonexistent.
 - Food Minigame still nonexistent.
 - Programming deities angered at my cockiness, sacrificial goat required to appease them.

---
## [NW360-DDR/MobileGameDesignTeamGame](https://github.com/NW360-DDR/MobileGameDesignTeamGame)@[1f2e99d259...](https://github.com/NW360-DDR/MobileGameDesignTeamGame/commit/1f2e99d259316b8a0a87c1630ee0587e586107c7)
#### Sunday 2022-11-06 16:19:20 by Nathaniel Owens

Fixed HeadpatScript, Merged art to Main Branch

Changes:
 - Kiria's graphics merged to main branch, not sure how it wasn't, but I'll figure it out later.
 - Edited properties of the status bars due to my own incompetence in setting them correctly.
 - Headpat Script now works properly, and updates the friendship values accordingly.
 - Back Button now added so you can leave the Headpat Minigame.

Known Bugs:
 - Stats do not yet decay over time to emulate neglect of friend.
 - Cleanup Minigame logic needs to be redone to actually fully randomize the pellet spot placement.
 - Audio is not implemented.
 - Oh dear god I tried making an animation object and it blew up my Unity project I think I did something wrong.
 - Food Minigame logic still nonexistent.
 - Food Minigame still nonexistent.
 - Programming deities angered at my cockiness, sacrificial goat required to appease them.

---
## [ProbablyCarl/sunset-wasteland](https://github.com/ProbablyCarl/sunset-wasteland)@[1ebbf79f9d...](https://github.com/ProbablyCarl/sunset-wasteland/commit/1ebbf79f9d9f11e2002df52e8cbdd2073921fae4)
#### Sunday 2022-11-06 17:10:42 by ProbablyCarl

Rocket Shrapnel & Other
- - -
New:
 - Rockets are now their own subclass of projectile, encompassing not just rockets, even though it's weird to say that and kinda wacky, but also grenade launcher projectiles.
 - Rocket classed projectiles can now have shrapnel magnitude and type attributed to them, permitting explosions identical to frag grenades on impact with their selected shrapnel and magnitude.
- - -
Balance:
 - A singular incendiary rocket replaces the high-yield HE round that the NCR Combat Engineer previously got in the rocket kit.
 - Chemical rockets are now absurdly powerful, to compensate for their otherwise useless nature. We'll probably adjust this as needed, if not outright nerf it again.
 - Chemical rockets can be made, but they're a PITA to craft and are likely to be more trouble than they're worth.
 - A singular unit of FEV is enough to OD someone. It's FEV. Stop drinking it.
- - -

---
## [beagleboard/linux](https://github.com/beagleboard/linux)@[adee8f3082...](https://github.com/beagleboard/linux/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Sunday 2022-11-06 17:15:40 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [chief-aberash/Bring-Back-Ex-Lover](https://github.com/chief-aberash/Bring-Back-Ex-Lover)@[d844b452af...](https://github.com/chief-aberash/Bring-Back-Ex-Lover/commit/d844b452af00ca88cb18c20e88bd99ccb6f26c3e)
#### Sunday 2022-11-06 17:22:34 by chief-aberash

Update README.md

Love spells, Marriage spells - Bring lost lover back Stop lover from cheating, be in control of the love in the house. Fix your troubled marriage. Tried many try me last, 35 years of experience. Stop or make a Divorce. Stop cheating. Fall in Love & Commitment. Fix a Broken Marriage.

Contact Me

www.chiefaberash.com

Get in Touch Get instant help for your love life now, with instant and guaranteed results.

Contact +27 63 5340727 Email info@chiefaberash.com

---
## [yyyy-yyyy-yyyy/Erudio](https://github.com/yyyy-yyyy-yyyy/Erudio)@[ad87c4b147...](https://github.com/yyyy-yyyy-yyyy/Erudio/commit/ad87c4b147784470e6f9bdb75609238ebdbbaf54)
#### Sunday 2022-11-06 17:44:30 by JK2Kgit

That was... a long battle,
BUT a successful one at last
However there were sacrifices leading to victory
I lost my sanity, mental fortitude, belief in God, and don't know what else
And patryk ... I don;t know what he lost but something for sure
I don't want to do this ever again
So if docker breaks you know who not to call
Or better yet... I don't know I just wanted to white Or better yet
A think I am losing scraps that where left of my sanity
For your information this entire poem was written and spellchecked during build process in docker compose
I don't even remember why I stared writing it, but I have no plan to end for now
I am now starting to consider if it got stuck or time got dilated for me to write my maybe final maybe not masterpiece that will show my suffering which you can't imagine.
As I continue my OH my god it unstuck, So what I was at, ah I remember, I was tunneling my suffering and if you are still reading it then you to need to visit a doctor because it is not normal for people to be able to read this.
The build process is going and going, and I am still wandering if it will finish or crash , if it crashes I am not sure if I have a strength to suffer throughout repairing it That That That is jus too much for mortal or even immortal or God himself that is just too much
Why the hell am I even continuing to write this beautiful yet pointless poem, that brings pain and no there is no and it is just pain.
That build process is still running and i think it is close to an end. ......... it........ is ....... an ...................... (.*1000) freaking.......... er....r....o......r, but wait is just a copy. I fixed it? or did I?
WHY THE HELL IT IS GOING FROM THE DAEM BEGINIGN. FGEDGSDGDSG. OK lest freaking chill out that is just another few paintful INCRWDABLE PAITEFUL MUTNITED THAT YOU NEDD TO ENDURE. ... .... Let's wait just wait it shouldn't take that long. Right? I am loosing faith in the fact that we live in a simulation, This can't be desired experience for human race.. Wait if finished?
IT WORKS I am amazing, my silks are unparalleled, I feel a will to live

---
## [ZeWaka/tgstation](https://github.com/ZeWaka/tgstation)@[99b8d6b494...](https://github.com/ZeWaka/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Sunday 2022-11-06 18:59:39 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[a424562676...](https://github.com/odoo-dev/odoo/commit/a42456267619522e2f3d36de933a0a7301fd77b4)
#### Sunday 2022-11-06 20:48:43 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104329

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [abu965/Pneumonia-Classification](https://github.com/abu965/Pneumonia-Classification)@[d743216318...](https://github.com/abu965/Pneumonia-Classification/commit/d743216318b0944a91d721e7973e9af2f5dcaee7)
#### Sunday 2022-11-06 21:05:55 by Abdulla Muradov

Add files via upload

Pneumonia, or lung infection, is a viral disease that affects lung tissue and interferes with the
normal oxygen exchange between air and blood. Inflammatory secretions that enter the air sacs of
the lungs do not allow the body to properly supply oxygen. And when the disease grabs most of the
lungs, acute respiratory failure develops. Pneumonia affects people with weak immunity, children
and the elderly. In Germany alone, 1.5 million people get the disease each year, 30% of whom are
infants and people over the age of 70. But pneumonia can be treated and needs to be treated! And
it’s a good idea to do this with an integrated approach. Treatment of the disease begins with a
correct diagnosis. Therefore, seek expert advice at the first signs of pathological development.Learn
what the first symptoms of pneumonia are, how to properly and comprehensively treat them, and
what you need to do to diagnose the disease. ## What is the aim of this notebook? I was hired
by a ”Medtronic” as a Data Scientist. Medtronic is a company that produces medical equipment
that ease the life of doctors by digital solutions. In July we start to develop a x-ray machine that
will be able to detect pneumonia. Now we are trying to develop a machine that makes the x-ray
and gives a diagnosis at the same time. By doing so we are planning to eliminate a human factor.

---
## [woofcore/woofcore.github.io](https://github.com/woofcore/woofcore.github.io)@[9115eb71f1...](https://github.com/woofcore/woofcore.github.io/commit/9115eb71f176e08f6d33ef203cfcbe0595e086bb)
#### Sunday 2022-11-06 21:13:23 by tom dodd

delete everything and start again

im depressed and exerting this small amount of power is the only control i have left in my life.
im joking but i do just want to have a completely plain, link-tree styled site with a short About section. it is harder than you would think to find something like this, especially with severely limited web design/dev knowledge - that I even got jekyll working in the first place is a miracle.

I think i'll still do blogs again in the future but they'll be on a specific platform like Medium where there's some hope of them being seen.

---
## [deavon-and-tiffany/krust-deployments](https://github.com/deavon-and-tiffany/krust-deployments)@[32dc46be16...](https://github.com/deavon-and-tiffany/krust-deployments/commit/32dc46be162c913bb218b7eed1a8d7abf7960f08)
#### Sunday 2022-11-06 21:27:53 by Deavon M. McCaffery

i hate my life

Signed-off-by: Deavon M. McCaffery <dmccaffery@users.noreply.github.com>

---
## [TonybynMp4/qb-printer-1](https://github.com/TonybynMp4/qb-printer-1)@[94945546f3...](https://github.com/TonybynMp4/qb-printer-1/commit/94945546f384e6e25d3c701affb390e878a34d80)
#### Sunday 2022-11-06 21:34:26 by Tony

Facking hell i hate myself

Co-authored-by: Yvan Cywan <c1yvan@outlook.com>

---
## [DEFRA/water-abstraction-system](https://github.com/DEFRA/water-abstraction-system)@[cb5cf8f12e...](https://github.com/DEFRA/water-abstraction-system/commit/cb5cf8f12ec3130e8a4444ebeb6dc52ccf982a44)
#### Sunday 2022-11-06 23:08:18 by Jason Claxton

Refactoring summary list for each service (#8)

https://github.com/DEFRA/water-abstraction-team/issues/54

We wanted to make the layout for each repo consistent and relate things like jobs to the service they belong to. We then decided we'd report on 'apps' rather than just 'repos', as that is what is running on a server and which 'the service' is dependent on.

We tidied up the external services section, including adding the Charge Module API which we'd, though not in the existing /service-status page, should be. We also got them to return meaningful information.

All the calls for info are now robust. Even if all the other apps and external services were down the page would still display.

All this work meant some major refactoring of the `ServiceStatusService()`, for example, a single method for making HTTP requests to the other apps and services.

All of this is tested. To do this we needed to bring in [Nock](https://github.com/nock/nock) to mock our HTTP requests to the other services and [proxyquire](https://github.com/thlorenz/proxyquire) to allow us to stub our calls to `child_process.exec()`.

** Thoughts on the current state

Looking at the tests we see a copious amount of work needed to mock web requests and system calls. We also have a range of scenarios. In our opinion, they are telling us that our service is doing _too_ much. It is collecting data from different sources in different ways, which means it definitely doesn't just have a single responsibility.

It needs breaking up, which in turn means we can break up the tests and hopefully make them a damn sight less scary.

We didn't do those changes in this PR though, because we'd already clocked up more than 1000 changes, well beyond our working target of 100. So, we've agreed to merge and tackle the refactoring as a separate exercise.

** Rebuilding the package-lock.json

Because of how long this PR had been around and the fact it adds new dependencies, we ended up having major merge issues in the `package-lock.json`. We went for a 'delete-and-rebuild' approach but we know we shouldn't have 😳 .

Next time we'll endeavour to use `npm install --package-lock-only` which we [recently learned](https://tkdodo.eu/blog/solving-conflicts-in-package-lock-json) is a command added to npm to help rectify the package-lock.json in these 'merge-hell' situations. 

Co-authored-by: Stuart Adair <43574728+StuAA78@users.noreply.github.com>
Co-authored-by: Rebecca Ransome <beckyrose200@aol.com>
Co-authored-by: Alan Cruikshanks <alan.cruikshanks@gmail.com>

---

