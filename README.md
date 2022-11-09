## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-08](docs/good-messages/2022/2022-11-08.md)


2,168,573 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,168,573 were push events containing 3,346,667 commit messages that amount to 281,039,765 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [jgunthorpe/linux](https://github.com/jgunthorpe/linux)@[b749f7a25a...](https://github.com/jgunthorpe/linux/commit/b749f7a25a42862b3f8a3600d90a475510a5f110)
#### Tuesday 2022-11-08 00:48:56 by Jason Gunthorpe

cover-letter: IOMMUFD Generic interface

[
This has been in linux-next for a little while now, and we've completed
the syzkaller run. 1300 hours of CPU time have been invested since the
last report with no improvement in coverage or new detections. syzkaller
coverage reached 69%(75%), and review of the misses show substantial
amounts are WARN_ON's and other debugging which are not expected to be
covered.
]

iommufd is the user API to control the IOMMU subsystem as it relates to
managing IO page tables that point at user space memory.

It takes over from drivers/vfio/vfio_iommu_type1.c (aka the VFIO
container) which is the VFIO specific interface for a similar idea.

We see a broad need for extended features, some being highly IOMMU device
specific:
 - Binding iommu_domain's to PASID/SSID
 - Userspace IO page tables, for ARM, x86 and S390
 - Kernel bypassed invalidation of user page tables
 - Re-use of the KVM page table in the IOMMU
 - Dirty page tracking in the IOMMU
 - Runtime Increase/Decrease of IOPTE size
 - PRI support with faults resolved in userspace

Many of these HW features exist to support VM use cases - for instance the
combination of PASID, PRI and Userspace IO Page Tables allows an
implementation of DMA Shared Virtual Addressing (vSVA) within a
guest. Dirty tracking enables VM live migration with SRIOV devices and
PASID support allow creating "scalable IOV" devices, among other things.

As these features are fundamental to a VM platform they need to be
uniformly exposed to all the driver families that do DMA into VMs, which
is currently VFIO and VDPA.

The pre-v1 series proposed re-using the VFIO type 1 data structure,
however it was suggested that if we are doing this big update then we
should also come with an improved data structure that solves the
limitations that VFIO type1 has. Notably this addresses:

 - Multiple IOAS/'containers' and multiple domains inside a single FD

 - Single-pin operation no matter how many domains and containers use
   a page

 - A fine grained locking scheme supporting user managed concurrency for
   multi-threaded map/unmap

 - A pre-registration mechanism to optimize vIOMMU use cases by
   pre-pinning pages

 - Extended ioctl API that can manage these new objects and exposes
   domains directly to user space

 - domains are sharable between subsystems, eg VFIO and VDPA

The bulk of this code is a new data structure design to track how the
IOVAs are mapped to PFNs.

iommufd intends to be general and consumable by any driver that wants to
DMA to userspace. From a driver perspective it can largely be dropped in
in-place of iommu_attach_device() and provides a uniform full feature set
to all consumers.

As this is a larger project this series is the first step. This series
provides the iommfd "generic interface" which is designed to be suitable
for applications like DPDK and VMM flows that are not optimized to
specific HW scenarios. It is close to being a drop in replacement for the
existing VFIO type 1 and supports existing qemu based VM flows.

Several follow-on series are being prepared:

- Patches integrating with qemu in native mode:
  https://github.com/yiliu1765/qemu/commits/qemu-iommufd-6.0-rc2

- A completed integration with VFIO now exists that covers "emulated" mdev
  use cases now, and can pass testing with qemu/etc in compatability mode:
  https://github.com/jgunthorpe/linux/commits/vfio_iommufd

- A draft providing system iommu dirty tracking on top of iommufd,
  including iommu driver implementations:
  https://github.com/jpemartins/linux/commits/x86-iommufd

  This pairs with patches for providing a similar API to support VFIO-device
  tracking to give a complete vfio solution:
  https://lore.kernel.org/kvm/20220901093853.60194-1-yishaih@nvidia.com/

- Userspace page tables aka 'nested translation' for ARM and Intel iommu
  drivers:
  https://github.com/nicolinc/iommufd/commits/iommufd_nesting

- "device centric" vfio series to expose the vfio_device FD directly as a
  normal cdev, and provide an extended API allowing dynamically changing
  the IOAS binding:
  https://github.com/yiliu1765/iommufd/commits/iommufd-v6.0-rc2-nesting-0901

- Drafts for PASID and PRI interfaces are included above as well

Overall enough work is done now to show the merit of the new API design
and at least draft solutions to many of the main problems.

Several people have contributed directly to this work: Eric Auger, Joao
Martins, Kevin Tian, Lu Baolu, Nicolin Chen, Yi L Liu. Many more have
participated in the discussions that lead here, and provided ideas. Thanks
to all!

The v1/v2 iommufd series has been used to guide a large amount of preparatory
work that has now been merged. The general theme is to organize things in
a way that makes injecting iommufd natural:

 - VFIO live migration support with mlx5 and hisi_acc drivers.
   These series need a dirty tracking solution to be really usable.
   https://lore.kernel.org/kvm/20220224142024.147653-1-yishaih@nvidia.com/
   https://lore.kernel.org/kvm/20220308184902.2242-1-shameerali.kolothum.thodi@huawei.com/

 - Significantly rework the VFIO gvt mdev and remove struct
   mdev_parent_ops
   https://lore.kernel.org/lkml/20220411141403.86980-1-hch@lst.de/

 - Rework how PCIe no-snoop blocking works
   https://lore.kernel.org/kvm/0-v3-2cf356649677+a32-intel_no_snoop_jgg@nvidia.com/

 - Consolidate dma ownership into the iommu core code
   https://lore.kernel.org/linux-iommu/20220418005000.897664-1-baolu.lu@linux.intel.com/

 - Make all vfio driver interfaces use struct vfio_device consistently
   https://lore.kernel.org/kvm/0-v4-8045e76bf00b+13d-vfio_mdev_no_group_jgg@nvidia.com/

 - Remove the vfio_group from the kvm/vfio interface
   https://lore.kernel.org/kvm/0-v3-f7729924a7ea+25e33-vfio_kvm_no_group_jgg@nvidia.com/

 - Simplify locking in vfio
   https://lore.kernel.org/kvm/0-v2-d035a1842d81+1bf-vfio_group_locking_jgg@nvidia.com/

 - Remove the vfio notifiter scheme that faces drivers
   https://lore.kernel.org/kvm/0-v4-681e038e30fd+78-vfio_unmap_notif_jgg@nvidia.com/

 - Improve the driver facing API for vfio pin/unpin pages to make the
   presence of struct page clear
   https://lore.kernel.org/kvm/20220723020256.30081-1-nicolinc@nvidia.com/

 - Clean up in the Intel IOMMU driver
   https://lore.kernel.org/linux-iommu/20220301020159.633356-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220510023407.2759143-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220514014322.2927339-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220706025524.2904370-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220702015610.2849494-1-baolu.lu@linux.intel.com/

 - Rework s390 vfio drivers
   https://lore.kernel.org/kvm/20220707135737.720765-1-farman@linux.ibm.com/

 - Normalize vfio ioctl handling
   https://lore.kernel.org/kvm/0-v2-0f9e632d54fb+d6-vfio_ioctl_split_jgg@nvidia.com/

 - VFIO API for dirty tracking (aka dma logging) managed inside a PCI
   device, with mlx5 implementation
   https://lore.kernel.org/kvm/20220901093853.60194-1-yishaih@nvidia.com

 - Introduce a struct device sysfs presence for struct vfio_device
   https://lore.kernel.org/kvm/20220901143747.32858-1-kevin.tian@intel.com/

 - Complete restructuring the vfio mdev model
   https://lore.kernel.org/kvm/20220822062208.152745-1-hch@lst.de/

 - Isolate VFIO container code in preperation for iommufd to provide an
   alternative implementation of it all
   https://lore.kernel.org/kvm/0-v1-a805b607f1fb+17b-vfio_container_split_jgg@nvidia.com

 - Simplify and consolidate iommu_domain/device compatability checking
   https://lore.kernel.org/linux-iommu/cover.1666042872.git.nicolinc@nvidia.com/

 - Align iommu SVA support with the domain-centric model
   https://lore.kernel.org/all/20221031005917.45690-1-baolu.lu@linux.intel.com/

This is about 233 patches applied since March, thank you to everyone
involved in all this work!

Currently there are a number of supporting series still in progress:

 - DMABUF exporter support for VFIO to allow PCI P2P with VFIO
   https://lore.kernel.org/r/0-v2-472615b3877e+28f7-vfio_dma_buf_jgg@nvidia.com

 - Start to provide iommu_domain ops for POWER
   https://lore.kernel.org/all/20220714081822.3717693-1-aik@ozlabs.ru/

However, these are not necessary for this series to advance.

This is on github: https://github.com/jgunthorpe/linux/commits/iommufd

v4:
 - Rebase to v6.1-rc3, include the iommu branch with the needed EINVAL
   patch series and also the SVA rework
 - All bug fixes and comments with no API or behavioral changes
 - gvt tests are passing again
 - Syzkaller is no longer finding issues and achieved high coverage of
   69%(75%)
 - Coverity has been run by two people
 - new "nth failure" test that systematically sweeps all error unwind paths
   looking for splats
 - All fixes noted in the mailing list
   If you sent an email and I didn't reply please ping it, I have lost it.
 - The selftest patch has been broken into three to make the additional
   modification to the main code clearer
 - The interdiff is 1.8k lines for the main code, with another 3k of
   test suite changes
v3: https://lore.kernel.org/r/0-v3-402a7d6459de+24b-iommufd_jgg@nvidia.com
 - Rebase to v6.1-rc1
 - Improve documentation
 - Use EXPORT_SYMBOL_NS
 - Fix W1, checkpatch stuff
 - Revise pages.c to resolve the FIXMEs. Create a
   interval_tree_double_span_iter which allows a simple expression of the
   previously problematic algorithms
 - Consistently use the word 'access' instead of user to refer to an
   access from an in-kernel user (eg vfio mdev)
 - Support two forms of rlimit accounting and make the vfio compatible one
   the default in compatability mode (following series)
 - Support old VFIO type1 by disabling huge pages and implementing a
   simple algorithm to split a struct iopt_area
 - Full implementation of access support, test coverage and optimizations
 - Complete COPY to be able to copy across contiguous areas. Improve
   all the algorithms around contiguous areas with a dedicated iterator
 - Functional ENFORCED_COHERENT support
 - Support multi-device groups
 - Lots of smaller changes (the interdiff is 5k lines)
v2: https://lore.kernel.org/r/0-v2-f9436d0bde78+4bb-iommufd_jgg@nvidia.com
 - Rebase to v6.0-rc3
 - Improve comments
 - Change to an iterative destruction approach to avoid cycles
 - Near rewrite of the vfio facing implementation, supported by a complete
   implementation on the vfio side
 - New IOMMU_IOAS_ALLOW_IOVAS API as discussed. Allows userspace to
   assert that ranges of IOVA must always be mappable. To be used by a VMM
   that has promised a guest a certain availability of IOVA. May help
   guide PPC's multi-window implementation.
 - Rework how unmap_iova works, user can unmap the whole ioas now
 - The no-snoop / wbinvd support is implemented
 - Bug fixes
 - Test suite improvements
 - Lots of smaller changes (the interdiff is 3k lines)
v1: https://lore.kernel.org/r/0-v1-e79cd8d168e8+6-iommufd_jgg@nvidia.com

# S390 in-kernel page table walker
Cc: Niklas Schnelle <schnelle@linux.ibm.com>
Cc: Matthew Rosato <mjrosato@linux.ibm.com>
# AMD Dirty page tracking
Cc: Joao Martins <joao.m.martins@oracle.com>
# ARM SMMU Dirty page tracking
Cc: Keqian Zhu <zhukeqian1@huawei.com>
Cc: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>
# ARM SMMU nesting
Cc: Eric Auger <eric.auger@redhat.com>
Cc: Jean-Philippe Brucker <jean-philippe@linaro.org>
# Map/unmap performance
Cc: Daniel Jordan <daniel.m.jordan@oracle.com>
# VDPA
Cc: "Michael S. Tsirkin" <mst@redhat.com>
Cc: Jason Wang <jasowang@redhat.com>
# Power
Cc: David Gibson <david@gibson.dropbear.id.au>
# vfio
Cc: Alex Williamson <alex.williamson@redhat.com>
Cc: Cornelia Huck <cohuck@redhat.com>
Cc: kvm@vger.kernel.org
# iommu
Cc: iommu@lists.linux.dev
# Collaborators
Cc: "Chaitanya Kulkarni" <chaitanyak@nvidia.com>
Cc: Nicolin Chen <nicolinc@nvidia.com>
Cc: Lu Baolu <baolu.lu@linux.intel.com>
Cc: Kevin Tian <kevin.tian@intel.com>
Cc: Yi Liu <yi.l.liu@intel.com>
# s390
Cc: Eric Farman <farman@linux.ibm.com>
Signed-off-by: Jason Gunthorpe <jgg@nvidia.com>

---
## [Metastruct/node-metaconcord](https://github.com/Metastruct/node-metaconcord)@[07889a57e7...](https://github.com/Metastruct/node-metaconcord/commit/07889a57e7193be909ad9a4eaf4a85f976132ad6)
#### Tuesday 2022-11-08 00:52:06 by Meta Construct

for some god forsaken reason there is an
empty server item in the gamebridge
that fucks up this particular call which makes me mad as hell.
I just want to sleep

---
## [Rob-Yoo/WebServ](https://github.com/Rob-Yoo/WebServ)@[e289412d65...](https://github.com/Rob-Yoo/WebServ/commit/e289412d65b7e88995dff10a2204f70f0ac8e35c)
#### Tuesday 2022-11-08 00:53:45 by Jinyoung Yoo

Merge pull request #36 from Rob-Yoo/master

FUCK YOU

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[32c2e4ccd3...](https://github.com/Ryll-Ryll/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Tuesday 2022-11-08 01:29:32 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[ccc2020f7a...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/ccc2020f7a6d83542860a66a8f124bd9ff38528b)
#### Tuesday 2022-11-08 01:40:52 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Jeremiah-Griffin/SagaGUI](https://github.com/Jeremiah-Griffin/SagaGUI)@[08f7bd4c5b...](https://github.com/Jeremiah-Griffin/SagaGUI/commit/08f7bd4c5b8de64b038ba85a1b4bbadf8884f316)
#### Tuesday 2022-11-08 01:44:25 by Jeremiah Griffin

FUCKING STUPID SHIT WILL ITERMITTENTLY COMPILE WITH NO FUCKING CHANGES FOR NO FUCKING REASON BECAUSE APPARENTLY THE ANGULAR DEVS ARE FUCKING MORONS

---
## [dibarbet/omnisharp-roslyn](https://github.com/dibarbet/omnisharp-roslyn)@[efeafeca33...](https://github.com/dibarbet/omnisharp-roslyn/commit/efeafeca33abe1d19659ed8c7ebab1d7c3481188)
#### Tuesday 2022-11-08 02:31:47 by Fredric Silberberg

Host dependency cleanup

Today, we delete a a few dlls in the cake packaging scripts, to remove DLLs that should come from the runtime we're loaded with, rather than the dlls we built with. This is fine for packaging, but is annoying when doing local tests by just rebuilding the relevant driver, because you have to remember to go into the output directly and delete them every time. I addressed this by removing the dlls in msbuild itself:

* System.Configuration.ConfigurationManager: this was a transitive dependency through Microsoft.CodeAnalysis.Features -> Microsoft.CodeAnalysis.Elfie. We don't need Elfie or its dependencies, so I made all references to these layers explicit and turned off flowing of transitive dependencies. This does cause a slight issue: one of those transitive dependencies is System.Text.Json 6.0, while OmniSharp.MSBuild transitively references 5.0. To ensure the appropriate binding redirects are still generated, I added an explicit reference to System.Text.Json, but we are not using that reference for anything else.
* Nuget.*.dll: these are real dependencies that we should not ship in .NET 6+. I added a target to remove that version from the list of files to be copied.

---
## [dizzyjaguar/zulip-mobile](https://github.com/dizzyjaguar/zulip-mobile)@[0af1d1133c...](https://github.com/dizzyjaguar/zulip-mobile/commit/0af1d1133c50f38057877eba063f837f82b961bd)
#### Tuesday 2022-11-08 03:36:26 by Chris Bobbe

UnicodeEmoji [nfc]: Reduce to just what we use; cut out r-n-vector-icons

Emojis aren't icons, so even from its name, it's not clear that
react-native-vector-icons is best suited to render them, even if it
has turned out to be convenient for a subset of emoji (Unicode
emoji).

Like avatars, emojis are a mode of freeform user expression (think
of the "thank you" emoji). Icons, on the other hand, are a palette
of UI elements that UI designers use to convey UI meaning and make
the UI more approachable. ("Ah, a star icon, I bet that'll take me
to starred messages if I press it.")

The createIconSet function from r-n-vector-icons is designed to give
us such a palette of UI elements: we're to call it once, at module
top-level, and and it'll give us a React component that can render
any one of a static menu of icons. We've co-opted that into "a
static menu of Unicode emoji," but that's worked fine so far.

But, with #2956, we don't want a static menu, we want a menu that's
defined by the server. That's a breaking point for continuing to use
createIconSet here. We'd have to handle these constraints:
  - We can't call createIconSet at module top-level anymore, since
    we don't have the server data at that time.
  - We'd have to call it before it's time to render a Unicode emoji.
…And that seems like too much trouble to keep around something that
isn't designed for this use case anyway.

So, as a first step, in this commit, take part of createIconSet's
returned component [1] -- just enough to preserve current behavior
-- and define it in a separate file. It's pretty small, so, go ahead
and convert to a function component while we're at it. After this,
it'll be an easy switch to consume data from Redux, with
useSelector.

[1] node_modules/react-native-vector-icons/lib/create-icon-set.js

---
## [AEFeinstein/Super-2023-Swadge-FW](https://github.com/AEFeinstein/Super-2023-Swadge-FW)@[96fc3fdfbd...](https://github.com/AEFeinstein/Super-2023-Swadge-FW/commit/96fc3fdfbdcc9103ac8aaf179d9d84592a2367bf)
#### Tuesday 2022-11-08 04:33:05 by gelakinetic

Merge pull request #231 from AEFeinstein/paint

"that's weird, why is the placeholder music still in main" AKA oh my god i never made an actual PR for paint yesterday???

---
## [ahamlinman/xt](https://github.com/ahamlinman/xt)@[8b138aa647...](https://github.com/ahamlinman/xt/commit/8b138aa64757f1355a286fbc0711317927a4e23d)
#### Tuesday 2022-11-08 05:22:31 by Alex Hamlin

Introduce initial support for streaming YAML input

Thanks to the new streaming text encoder and YAML chunker, we've finally
achieved the first working implementation of streaming YAML input!

Besides the awful hackishness of the implementation that I've written
about at length in the comments, the main limitation of this first pass
is that YAML streaming only works when format detection is bypassed.

My current thinking is that instead of returning a String, the chunker
can return a richer "Chunk" that includes both the string content and a
marker indicating whether the root of the document is a scalar,
sequence, or mapping. It should be pretty easy for the format detector
to take advantage of that, I just hope it doesn't complicate the chunker
too much more. The other possibility would be to parse the first chunk
with serde_yaml and somehow have it tell us the root type, but that
would probably require a custom Deserialize impl that I don't feel like
writing.

---
## [Dabger1/tgstation](https://github.com/Dabger1/tgstation)@[5b4ba051a0...](https://github.com/Dabger1/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Tuesday 2022-11-08 06:41:52 by LemonInTheDark

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
## [m5l14i11/probability](https://github.com/m5l14i11/probability)@[9b67e5abdd...](https://github.com/m5l14i11/probability/commit/9b67e5abdd31840b33d17f106a275fca017827ef)
#### Tuesday 2022-11-08 06:59:01 by Dave Moore

Port `make_trainable` to use new state utilities, and add a stateless version w/ JAX support.

The change to make_trainable itself is minimal. A couple of issues that came up:

1. Stateful trainable distributions are now DeferredModules, which 'quack like' distributions, but break a few `isinstance` checks that I had to update. (thus illustrating the perils of `isinstance` checks).

2. How should we distinguish stateful/stateless functions in the API? Some options:
a) Keep both functions in the same module, with a `_stateless` suffix for the stateless version. (what I've done here, and what we did with tfp.math.minimize_stateless)
b) Put stateless versions in their own submodule, e.g., `tfp.experimental.vi.stateless.make_trainable`.
c) Put both stateful and stateless versions in their own submodules, with a top-level wrapper that points to the stateless versions under JAX and the stateful versions under TF. (this is too magicky IMHO).

Various other things are possible too. I don't think the choice now is *too* critical since it's still experimental, but lmk if you have strong feelings.

3. It's a pain to specify docstrings for both the stateful and stateless versions. I ended up writing a 'base' docstring for the generator, and then using replacement magic (some substitutions here, plus the stuff in trainable utils that converts 'Yields' to 'Returns' and adds the 'seed' kwarg to the stateful builder docstring) to generate the stateful and stateless versions. I don't love this, but at least it kind of works.

PiperOrigin-RevId: 418707747

---
## [acsone/odoo](https://github.com/acsone/odoo)@[1636ba5ed2...](https://github.com/acsone/odoo/commit/1636ba5ed2f8a284bef0930313a85cc3dc7cf072)
#### Tuesday 2022-11-08 07:08:43 by qsm-odoo

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

closes odoo/odoo#104335

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Tuesday 2022-11-08 07:33:17 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

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

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [serokell/nixpkgs](https://github.com/serokell/nixpkgs)@[8e6538f3de...](https://github.com/serokell/nixpkgs/commit/8e6538f3de1508a18d4ccdb367c0296a6718434f)
#### Tuesday 2022-11-08 08:55:09 by adisbladis

Python: introduce NIX_PYTHONPREFIX in order to set site.PREFIXES

This is needed in case of `python.buildEnv` to make sure site.PREFIXES
does not only point to the unwrapped executable prefix.

--------------------------------------------------------------------------------

This PR is a story where your valiant hero sets out on a very simple adventure but ends up having to slay dragons, starts questioning his own sanity and finally manages to gain enough knowledge to slay the evil dragon and finally win the proverbial price.

It all started out on sunny spring day with trying to tackle the Nixops plugin infrastructure and make that nice enough to work with.

Our story begins in the shanty town of [NixOps-AWS](https://github.com/nixos/nixops-aws) where [mypy](http://mypy-lang.org/) type checking has not yet been seen.

As our deuteragonist (@grahamc) has made great strides in the capital city of [NixOps](https://github.com/nixos/nixops) our hero wanted to bring this out into the land and let the people rejoice in reliability and a wonderful development experience.

The plugin work itself was straight forward and our hero quickly slayed the first small dragon, at this point things felt good and our hero thought he was going to reach the town of NixOps-AWS very quickly.

But alas! Mypy did not want to go, it said:
`Cannot find implementation or library stub for module named 'nixops'`

Our hero felt a small sliver of life escape from his body. Things were not going to be so easy.

After some frustration our hero discovered there was a [rule of the land of Python](https://www.python.org/dev/peps/pep-0561/) that governed the import of types into the kingdom, more specificaly a very special document (file) called `py.typed`.
Things were looking good.

But no, what the law said did not seem to match reality. How could things be so?

After some frustrating debugging our valiant hero thought to himself "Hmm, I wonder if this is simply a Nix idiosyncrasy", and it turns out indeed it was.
Things that were working in the blessed way of the land of Python (inside a `virtualenv`) were not working the way they were from his home town of Nix (`nix-shell` + `python.withPackages`).

After even more frustrating attempts at reading the mypy documentation and trying to understand how things were supposed to work our hero started questioning his sanity.
This is where things started to get truly interesting.

Our hero started to use a number of powerful weapons, both forged in the land of Python (pdb) & by the mages of UNIX (printf-style-debugging & strace).

After first trying to slay the dragon simply by `strace` and a keen eye our hero did not spot any weak points.
Time to break out a more powerful sword (`pdb`) which also did not divulge any secrets about what was wrong.

Our hero went back to the `strace` output and after a fair bit of thought and analysis a pattern started to emerge. Mypy was looking in the wrong place (i.e. not in in the environment created by `python.withPackages` but in the interpreter store path) and our princess was in another castle!

Our hero went to the pub full of old grumpy men giving out the inner workings of the open source universe (Github) and acquired a copy of Mypy.
He littered the code with print statements & break points.
After a fierce battle full of blood, sweat & tears he ended up in https://github.com/python/mypy/blob/20f7f2dd71c21bde4d3d99f9ab69bf6670c7fa03/mypy/sitepkgs.py and realised that everything came down to the Python `site` module and more specifically https://docs.python.org/3.7/library/site.html#site.getsitepackages which in turn relies on https://docs.python.org/3.7/library/site.html#site.PREFIXES .

Our hero created a copy of the environment created by `python.withPackages` and manually modified it to confirm his findings, and it turned out it was indeed the case.
Our hero had damaged the dragon and it was time for a celebration.

He went out and acquired some mead which he ingested while he typed up his story and waited for the dragon to finally die (the commit caused a mass-rebuild, I had to wait for my repro).

In the end all was good in [NixOps-AWS](https://github.com/nixos/nixops-aws)-town and type checks could run. (PR for that incoming tomorrow).

---
## [oriyaf1/he.reactjs.org](https://github.com/oriyaf1/he.reactjs.org)@[72906a541c...](https://github.com/oriyaf1/he.reactjs.org/commit/72906a541c81b6c2af69c490431bcd1f687d7f55)
#### Tuesday 2022-11-08 09:01:56 by oriyaf1

Removing duplicate original and translation

Apparently, both the translation and the original text were mixed into the paragraph by mistake,
If it's on purpose, it's really annoying and interferes with reading in my opinion,
If it is indeed by mistake, then I deleted the unnecessary,
The translation is accurate!
תודה רבה

---
## [hickford/git](https://github.com/hickford/git)@[762521e8a5...](https://github.com/hickford/git/commit/762521e8a5a6948501d56d51da3f70df4f3dfdbe)
#### Tuesday 2022-11-08 12:04:55 by Jeff King

t5516: move plaintext-password tests from t5601 and t5516

Commit 6dcbdc0d66 (remote: create fetch.credentialsInUrl config,
2022-06-06) added tests for our handling of passwords in URLs. Since the
obvious URL to be affected is git-over-http, the tests use http. However
they don't set up a test server; they just try to access
https://localhost, assuming it will fail (because the nothing is
listening there).

This causes some possible problems:

  - There might be a web server running on localhost, and we do not
    actually want to connect to that.

  - The DNS resolver, or the local firewall, might take a substantial
    amount of time (or forever, whichever comes first) to fail to
    connect, slowing down the tests cases unnecessarily.

  - Since there's no server, our tests for "allow" and "warn" still
    expect the clone/fetch/push operations to fail, even though in the
    real world we'd expect these to succeed. We scrape stderr to see
    what happened, but it's not as robust as a more realistic test.

Let's instead move these to t5551, which is all about testing http and
where we have a real server. That eliminates any issues with contacting
a strange URL, and lets the "allow" and "warn" tests confirm that the
operation actually succeeds.

It's not quite a verbatim move for a few reasons:

  - we can drop the LIBCURL dependency; it's already part of
    lib-httpd.sh

  - we'll use HTTPD_URL_USER_PASS, etc, instead of our fake URL. To
    avoid repetition, we'll add a few extra variables.

  - the "https://username:@localhost" test uses a funny URL that
    lib-httpd.sh doesn't provide. We'll similarly construct it in a
    variable. Note that we're hard-coding the lib-httpd username here,
    but t5551 already does that everywhere.

  - for the "domain:port" test, the URL provided by lib-httpd is fine,
    since our test server will always be on an exotic port. But we'll
    confirm in the test that this is so.

  - since our message-matching is done via grep, I simplified it to use
    a regex, rather than trying to massage lib-httpd's variables.
    Arguably this makes it more readable, too, while retaining the bits
    we care about: the fatal/warning distinction, the "uses plaintext"
    message, and the fact that the password was redacted.

  - we'll use the /auth/ path for the repo, which shows that we are
    indeed making use of the auth information when needed.

  - we'll also use /smart/; most of these tests could be done via /dumb/
    in t5550, but setting up pushes there requires extra effort and
    dependencies. The smart protocol is what most everyone is using
    these days anyway.

This patch is my own, but I stole the analysis and a few bits of the
commit message from a patch by Johannes Schindelin.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [Chainsawicus/cmss13](https://github.com/Chainsawicus/cmss13)@[ca2114f0f5...](https://github.com/Chainsawicus/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Tuesday 2022-11-08 14:40:15 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [ProtonAOSP-NS/frameworks_base](https://github.com/ProtonAOSP-NS/frameworks_base)@[935dc4c5b4...](https://github.com/ProtonAOSP-NS/frameworks_base/commit/935dc4c5b49c3cc5fe990b62bb282e1b32e42abb)
#### Tuesday 2022-11-08 15:21:35 by Kuba Wojciechowski

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

---
## [avar/git](https://github.com/avar/git)@[d22fddf78a...](https://github.com/avar/git/commit/d22fddf78ad961aa4e2e523d99376006872efe05)
#### Tuesday 2022-11-08 15:23:58 by Ævar Arnfjörð Bjarmason

[TODO t0450] submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior related to "--" handling, even when that
behavior is stupid. We'll fix in subsequent commits, but let's first
faithfully reproduce it.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

It would be better to use run_command() here directly to avoid copying
"args" and "env" copying, but let's use run_command_v_opt_cd_env()
instead to optimize for subsequent diff size. By using our own "struct
strvec args" we can push to "&args", not a "&cp.args". Eventually
we'll stop invoking "submodule--helper" as a sub-process, and avoid
the churn of converting all of "&cp.args" to "&args".

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [Faustas156/NeonLite](https://github.com/Faustas156/NeonLite)@[31039b8464...](https://github.com/Faustas156/NeonLite/commit/31039b8464959a6bc81826506f7abc8cba007846)
#### Tuesday 2022-11-08 15:59:18 by faustas

apparently github did a funny and released my readme god damnit

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[3dfeccbf27...](https://github.com/Zergspower/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Tuesday 2022-11-08 16:47:52 by SkyratBot

[MIRROR] Clowns will now always like bananas. [MDB IGNORE] (#17300)

* Clowns will now always like bananas. (#70919)

## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog

:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

* Clowns will now always like bananas.

Co-authored-by: Striders13 <53361823+Striders13@users.noreply.github.com>

---
## [Quick4Tech/ARIES](https://github.com/Quick4Tech/ARIES)@[12c89d0b0e...](https://github.com/Quick4Tech/ARIES/commit/12c89d0b0e3ef45d2c863b28e5edb2bc5833cee5)
#### Tuesday 2022-11-08 16:56:22 by Liam

does anyone read these?

born to code the wode and the smode for the dodes who implode when coded into the matrix which is in itself an illusion even once realized that it doesn't exist but still despite  that people still call it a miracle when they can escape it when really the solution was infront of them the whole time but in reality when you think about the sybolism of the film you start to see that it's not about a robotic dystopia with humanity all used to power the mechines even with the true end saying that the martriix has layers and they were in it the whole time even when they thought they were in the real world. now this is a revelation that shocked the audidence and nobody expected for it to be like this as the established theme was them going from the fake world to the real world. and that's my opinion on hotdogs thanks for reading!

---
## [Stanagley/Overlord-Bot](https://github.com/Stanagley/Overlord-Bot)@[f583fa74ae...](https://github.com/Stanagley/Overlord-Bot/commit/f583fa74ae476b79e7e2f6890536f47146ec31b1)
#### Tuesday 2022-11-08 18:10:09 by EggyRepublic

working recursive command parser

inputted scheduler commands are recursively parsed by popping off the top of each command list and executing any remaining commands

this allows one to write strings such as degree, computer science, print, fulfillment, add, 1, dat str
and the program will execute each command one by one as if they were typed separately.

currently uses a lock to prevent simultaneous command execution but you need to remember to unlock it prior to every return statement which is probably a pain in the ass so I'll have to figure something out.

---
## [zBinFinn/MiningGame](https://github.com/zBinFinn/MiningGame)@[d4e6e3431c...](https://github.com/zBinFinn/MiningGame/commit/d4e6e3431c4deba1f32a4c5c6b687ab978e9402c)
#### Tuesday 2022-11-08 19:06:33 by zBinFinn

Too lazy to write a formatted commit message fuck you

---
## [GremlingSS/funset-pastryland](https://github.com/GremlingSS/funset-pastryland)@[2062e298a0...](https://github.com/GremlingSS/funset-pastryland/commit/2062e298a06759209a0f3832362b4d750c10a9be)
#### Tuesday 2022-11-08 19:57:01 by Tk420634

Slows Knife Raiders, and their buddies attacks a bit.

Haha, fucked that up didn't I?  We do a little shitting.  Also lowered some damages on rapid_meleeing mobs

---
## [fmeum/bazel](https://github.com/fmeum/bazel)@[2232c5b445...](https://github.com/fmeum/bazel/commit/2232c5b445f5264b31b53a698f5f0e726d9be249)
#### Tuesday 2022-11-08 20:19:27 by Christopher Peterson Sauer

Move Boost into C++ Docs; Add Libraries Section

Hi wonderful Bazelers,

This is just a docs change.

Backstory: I'd been looking to make HTTPS requests across platforms from C++. A classic problem if there ever were one, networking being perhaps the most glaring omission in the C++ standard library. Thankfully, this is a problem Bazel can solve well, since most of the problem is the friction of using 3rd party libraries from C++. So, I spun up some build rules to make network requests easy, inspired by collaborating on the boost ones, and set off to add them to the docs.

Along the way, I noticed that the boost rules were in an odd spot: Listed at the language level alongside C++, rather than nested within C++. So I fixed that by nesting Boost inside, added Abseil, and then (hoping you'll forgive my hubris), I'd love to add the rules I just released, since I think they're a solution to a very real need. Perhaps rules for more famous, critical libraries can accumulate there over time, helping Bazel users get set up with the essential tools they need.

Thanks for your consideration!
Chris
(ex-Googler and author of [bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor), also in the docs.)

Closes #16621.

PiperOrigin-RevId: 486106928
Change-Id: I119ccff4f70e66415f8c6ac4930c975e48086bc2

---
## [pharbst/libft](https://github.com/pharbst/libft)@[41b068dc27...](https://github.com/pharbst/libft/commit/41b068dc27fa18b74ccca8bddaa31f890c888b6c)
#### Tuesday 2022-11-08 20:56:51 by pharbst

added the strcmp function because passing a fucking lenght to compare is stupid i just want to compare the two strings the whole two strings fuck you libft

---
## [Ubunfu/craftonomy-authz](https://github.com/Ubunfu/craftonomy-authz)@[4015628aea...](https://github.com/Ubunfu/craftonomy-authz/commit/4015628aea40fccbf4c9b19ffc9a71412e402814)
#### Tuesday 2022-11-08 21:26:07 by Ryan Allen

Reading keystore file as binary string instead of a stupid  buffer. Fuck. That. Shit.

---
## [theElandor/MyProjects](https://github.com/theElandor/MyProjects)@[a938714446...](https://github.com/theElandor/MyProjects/commit/a93871444615fe0eb54abb9140dd7ab1ac04625b)
#### Tuesday 2022-11-08 22:04:37 by theElandor

Create FindPeakElement.cpp

Kinda easy binary search problem.
I never consider  edgecases when thinking about solution, so my code sometimes
ends up being clunky. Don't really care as long as it works....cmon it's 11 a.m.
Good night.

---
## [MASQ-Project/Node](https://github.com/MASQ-Project/Node)@[b0e9bb484e...](https://github.com/MASQ-Project/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Tuesday 2022-11-08 22:15:23 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [Mikary31/mesa](https://github.com/Mikary31/mesa)@[3a9cdd780d...](https://github.com/Mikary31/mesa/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Tuesday 2022-11-08 22:17:50 by Alyssa Rosenzweig

panfrost/ci: Disable trace-based testing

Trace-based testing has not worked for Panfrost. It was a neat
experiment, and I'm glad we tried it, but the results have been mostly
negative for the driver. Disable the trace-based tests.

For testing that specific API features work correctly, we run the
conformance tests (dEQP), which are thorough for OpenGL ES. For big GL
features, we run Piglit, and if there are big GL features that we are
not testing adequately, we should extend Piglit for these. For
fine-grained driver correctness, we are already covered.

Where trace-based testing can fit in is as a smoke test, ensuring that
the overall rendering of complex scenes does not regress. In principle,
that's a lovely idea, but the current implementation has not worked out
for Panfrost thus far. The crux of the issue is that the trace based
tests are based on checksums, not fuzzy-compared reference images. That
requires updating checksums any time rendering changes. However, a
rendering change to a trace is NOT a regression. The behaviour of OpenGL
is specified very loosely. For a given trace, there are many different
valid checksums. That means that correct changes to core code frequently
fail CI after running through the rest of CI, only because a checksum
changed in a still correct way. That's a pain to deal with, exacerbated
by rebase pains, and provides negative value to the project. Some recent
examples of this I've hit in the past two weeks alone:

   panfrost: Enable rendering to 16-bit and 32-bit
   4b49241f7d7 ("panfrost: Use proper formats for pntc varying")
   ac2964dfbd1 ("nir: Be smarter fusing ffma")

The last example were virgl traces, but were especially bad: due to a
rebase fail, I had to update traces /twice/, wasting two full runs of
pre-merge CI across *all* hardware. This was extremely wasteful.

The value of trace-based testing is as a smoke test to check that traces
still render correctly. That is useful, but it turns out that checksums
are the wrong way to go about it. A better implementation would be
storing only a single reference image from a software rasterizer per
trace. No driver-specific references would be stored. That reference
image must never change, provided the trace never changes. CI would then
check rendered results against that image with tolerant fuzzy
comparisons. That tolerance matches with the fuzzy comparison that the
human eye would do when investigating a checksum change anyway. Yes, the
image comparison JavaScript will now report that
0 pixels changed within the tolerance, but there's nothing a human eye
can do with that information other than an error prone copypaste of new
checksums back in the yaml file and kicking it back to CI, itself a
waste of time.

Finally, in the time we've had trace-based testing alongside the
conformance tests, I cannot remember a single actual regression in one
of my commits the trace jobs have identified that the conformance tests
have not also identified. By contrast, the conformance test coverage has
prevented the merge of a number of actual regressions, with very few
flakes or xfail changes, and I am grateful we have that coverage. That
means the value added from the trace jobs is close to zero, while the
above checksum issues means that the cost is tremendous, even ignoring
the physical cost of the extra CI jobs.

If you work on trace-based testing and would like to understand how it
could adapted to be useful for Panfrost, see my recommendations above.
If you work on CI in general and would like to improve Panfrost's CI
coverage, what we need right now is not trace-based testing, it's
GLES3.1 conformance runs on MediaTek MT8192 or MT8195. That hardware is
already in the Collabora LAVA lab, but it's not being used for Mesa CI
as the required kernel patches haven't made their way to mainline yet
and nobody has cherry-picked them to the gfx-ci kernel. If you are a
Collaboran and interested in improving Panfrost CI, please ping
AngeloGioacchino for information on which specific patches need to be
backported or cherry-picked to our gfx-ci kernel. Thank you.

Signed-off-by: Alyssa Rosenzweig <alyssa@collabora.com>
Acked-by: Jason Ekstrand <jason.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/19358>

---
## [HavensurgeSW/-ServerDefense-](https://github.com/HavensurgeSW/-ServerDefense-)@[1a47b013ea...](https://github.com/HavensurgeSW/-ServerDefense-/commit/1a47b013eac375524868021822d802bee9547c46)
#### Tuesday 2022-11-08 22:21:45 by Ignacio Fernandez Lemos

Actual fucking attempt at killing that shit .meta file for the love of god

---
## [Dailynewsy/Solidmighty](https://github.com/Dailynewsy/Solidmighty)@[b32beddf08...](https://github.com/Dailynewsy/Solidmighty/commit/b32beddf084e55e63b332fc2c742c6bfc8412cdd)
#### Tuesday 2022-11-08 22:50:54 by Dailynewsy

https://hyperfollow.com/solidmighty

Solidmighty fast rising star 

Search for Solidmighty on google search and see his latest songs that is currently making waves on the internet 
Obidike Joseph (Solid: born in Abatete Anambra state Nigeria ), Date of birth 1996/3/25, known professionally as Solidmighty(Mr Conquer), is a Trinidadian-born[a] rapper, singer, and songwriter based in the Ghana. he is known for his musical versatility, animated flow in his rapping, alter egos and accents. Solidmighty first gained recognition after releasing three mixtapes between 2019 and 2022. His  debut album, My forever dreams (2022), very determined to obtain the Billboard chart. his viral  single,that girl is mine) reached number One on the google podcast Billboard Hot 100 chart and, in 2022, was certified Verified Artist by Google .

Solidmighty Self-employed record label 
registered date on 2010
Solidmighty
December 8,2019 )
release his first Music Video(that girl is mine)
Musical University of High School
Occupation
Rapper singer songwriter acting as radio personality
Years active
2010–present
Works
discography songs recorded videography performances
His single and he is not the type that is fond of ladies. He really doesn't ​interest going after girls and he has been focused since he start to hustle on the streets (he was 7 years old when his father died in a car accident and He won  3
Awards
Full list
Musical career
Origin:Anambra , Nigeria 
Genres
Hip hop[1][2] pop[3]
Instrument(s)
Vocals
Labels
Mega Gangstar Republic
Website
Solidmightystar.Business.site
So follow-up album, New born king the best rap song Reloaded (2020), explored dance-pop and his singing, reaching number one in several countries worldwide. Its lead single, "Starships", peaked inside the top five in fifteen countries. His third album, Akanaku song (2021) explored more personal topics and marked a return to his hip-hop roots. the Total songs dropped reached number 10 on the Hot 100 and, in 2022, its music video became the first by a solo male rapper to reach one million views on Google podcast . He released his songs and sold worldwide. Several media outlets have described him as one of the most influential rappers of all time, and Billboard ranked him as the top selling Male rapper of the 2022, and His various accolades include 9 on Music Awards, five MTV Video Music Awards (including the 2022 Video Vanguard Award), twelve BET Awards, four Billboard Music Awards, a Brit Award and three Guinness World Records. In 2022, Time included his 100 most influential people in the world. Outside of music, his street Hustle career has been so tough and hardship and there was no one who could helped him after the death of his father and he remained Continental Determined since (he was ten years old )

Life and career
Artistry
Public image
Philanthropy
Legacy
Achievements
Other activities
Discography
Filmography
References
Further reading
External links
on google search TheHipHopRapping

Content is available under CC BY-SA 3.0 unless otherwise noted.
Privacy policy Terms of UseDeskto

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[41c3bd44cd...](https://github.com/Buildstarted/linksfordevs/commit/41c3bd44cd014f17f873a44a57e769cd8703ffa8)
#### Tuesday 2022-11-08 23:07:36 by Ben Dornis

Updating: 11/8/2022 11:00:00 PM

 1. Added: What’s that magic computation in stb__RefineBlock?
    (https://fgiesen.wordpress.com/2022/11/08/whats-that-magic-computation-in-stb__refineblock/)
 2. Added: Containers are chroot with a Marketing Budget
    (https://earthly.dev/blog/chroot/)
 3. Added: Twenty Questions
    (https://aaronson.org/blog/twenty-questions)
 4. Added: Announcing NuGet 6.4 - Signed, Central, Delivered
    (https://devblogs.microsoft.com/nuget/announcing-nuget-6-4-signed-central-delivered/)
 5. Added: From WampServer, to Vagrant, to QEMU
    (https://andrewpillar.com/programming/2022/11/08/from-wampserver-to-vagrant-to-qemu/)
 6. Added: 50 Tabs means 50 Mental contexts and needless cognitive load
    (https://dsebastien.net/blog/2022-11-07-50-tabs-means-50-mental-contexts)
 7. Added: My favorite 12 side projects in 2022
    (https://trycombine.com/posts/12-of-my-favorite-side-projects-in-2022/)
 8. Added: Rails Quick Tip - Use Private Debugging Aliases
    (https://pawelurbanek.com/rails-debug-aliases)
 9. Added: Vanilla Rails is plenty
    (https://dev.37signals.com/vanilla-rails-is-plenty)
10. Added: "Trust, but verify" is bullshit
    (https://tmp.bearblog.dev/trust-but-verify-is-bullshit/)
11. Added: Vim Is Just English
    (https://mark.mcnally.je/blog/post/Vim%20Is%20Just%20English)
12. Added: Zoom! Enhance! — Monday Morning Haskell
    (https://mmhaskell.com/blog/2022/11/7/zoom-enhance)
13. Added: Sometimes... Constraints Are Good
    (https://tiberriver256.github.io/software%20architecture/Constraints-Are-Good/)
14. Added: Traits in Rust
    (https://serokell.io/blog/rust-traits)

Generation took: 00:07:25.3663840
 Maintenance update - cleaning up homepage and feed

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[f1c903debd...](https://github.com/ttaylorr/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Tuesday 2022-11-08 23:10:49 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [ati-ozgur/pydot](https://github.com/ati-ozgur/pydot)@[682edb7be6...](https://github.com/ati-ozgur/pydot/commit/682edb7be6d7d82bc1addbab901cce98c97ef7aa)
#### Tuesday 2022-11-08 23:42:55 by Peter Nowee

Add ppc64le and bump Python versions in Travis CI

Considering that:

- IBM, through its supplier Datamatics, requested many Python projects
  to [add the `ppc64le` (Power) architecture][1] to their Travis CI
  test matrices. Related links:
  - ibm.com: [Build your open source projects on IBM Power Systems with
    Travis CI][2].
  - youtube.com: [OpenPOWER Summit NA 2019: Developing Applications
    using Acceleration Hardware on Power][3].
  - Gerrit Huizenga of IBM (@gerrith3 on GitHub) provided more details
    on the [motives and open source contributions of IBM][4] in answer
    to questions from Ludovic Fernandez (@ldez) of nrdcg/goinwx.
- The request to add `ppc64` testing was also made to pydot in PR
  [pydot/pydot#243][5] by @asellappen of Datamatics. The proposed
  implementation extended the test job configuration by [matrix
  expansion][6].
- [Matrix expansion][7] means adding a new dimension to the build
  configuration (e.g. `arch`, `os`, `env`), after which the number of
  test jobs is automatically multiplied by the number of choices given
  in the newly added dimension. In this case, it would add a dimension
  of two architectures, expanding the matrix of test jobs by a factor
  of 2: 5 Python versions (at that time) * 2 architectures = 10 test
  runs of 2 to 3 minutes each.
- Gerrit Huizenga of IBM said he thinks the adding of `ppc64le` test
  jobs to Travis will not lead to additional billing from Travis CI to
  the OSS community, because [he provides Travis CI with the Power
  hardware][8].
- The [Travis CI documentation on CPU architectures][9] currently says
  IBM architecture support is in beta stage and only available for Open
  Source repositories.
- There are many abstraction layers between pydot and the hardware
  architecture, including other libraries, Python and the operating
  system. Pydot itself does not need to be compiled for a specific
  architecture. In a perfect world, pydot is architecture-independent
  and testing pydot on a single architecture should be sufficient.
- However, the world is not perfect and [abstraction layers can be
  leaky][10]. According to Gerrit Huizenga of IBM, [corner cases do
  come up][11], which is why they do so much testing up front and
  provide free access to testing.
- Still, even if an automated testing service is provided for free, it
  has an [environmental footprint][12], so there are limits to how much
  we should make use of that as well.
- Travis CI also requests open-source users to remember that Travis CI
  provides its service free of charge to the community and only specify
  the matrix we [actually need][13].
- Even if we ever find an architecture-specific bug in pydot, it seems
  highly likely that it will come out on several Python versions for
  that architecture.
- All of this was further discussed between pydot maintainers Sebastian
  Kalinowski (@prmtl) and Peter Nowee (@peternowee) and Gerrit Huizenga
  of IBM in PR [pydot/pydot#245][14].

The following was decided:

- Baseline testing is kept at `amd64`, with testing of the lowest and
  the highest Python versions supported by the Python community, as
  well as the lowest end-of-life (EOL) Python version that we still
  choose to support pydot on. Currently, that means Python 3.6, 3.9 and
  2.7 respectively.
- For other architectures, such as `ppc64le`, we do limited testing to
  catch reasonably expectable corner cases and validate architecture
  independence in a resource conserving way. For now, we start with
  Python 2.7 and 3.9.

We can always reconsider this policy depending on actual findings.

[1]: https://github.com/pulls?q=author%3Aasellappen+ppc64le+travis
[2]: https://developer.ibm.com/tutorials/travis-ci-on-power/
[3]: https://www.youtube.com/watch?v=qPZtf3hoMSs
[4]: https://github.com/nrdcg/goinwx/pull/5
[5]: https://github.com/pydot/pydot/pull/243
[6]: https://docs.travis-ci.com/user/build-matrix/#matrix-expansion
[7]: https://config.travis-ci.com/matrix_expansion
[8]: https://github.com/nrdcg/goinwx/pull/5#issuecomment-721422838
[9]: https://docs.travis-ci.com/user/multi-cpu-architectures/
[10]: https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
[11]: https://github.com/nrdcg/goinwx/pull/5#issuecomment-719084047
[12]: https://en.wikipedia.org/wiki/Data_center#Energy_use
[13]: https://docs.travis-ci.com/user/build-matrix/#listing-individual-jobs
[14]: https://github.com/pydot/pydot/pull/245

---

