## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-10](docs/good-messages/2022/2022-11-10.md)


2,169,220 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,169,220 were push events containing 3,295,790 commit messages that amount to 263,587,118 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 26 messages:


## [SurovijZashistnik/tgstation](https://github.com/SurovijZashistnik/tgstation)@[32c2e4ccd3...](https://github.com/SurovijZashistnik/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Thursday 2022-11-10 00:47:09 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [Lindonrow/StorytimeOfficialMod](https://github.com/Lindonrow/StorytimeOfficialMod)@[d73b7d648a...](https://github.com/Lindonrow/StorytimeOfficialMod/commit/d73b7d648a11836ae1a7b50cfb706cfcfa5a8d6a)
#### Thursday 2022-11-10 03:10:30 by Isengriff

Chapter 4: Putting the Egg in Egg Nog

-made egg nog a viable food source for ovivores
-added donald duck tip
-remember how I said the last update would be the last one before 1.4? Well I fucking LIED and there's approximately NOTHING any of you dumb sons of bitches can do about it, because I am more powerful than GOD himself
-like comment subscribe

---
## [GODdudesoyeah/cmss13](https://github.com/GODdudesoyeah/cmss13)@[7cb69c2a8b...](https://github.com/GODdudesoyeah/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Thursday 2022-11-10 03:48:12 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [Stalkeros2/STALKER-13](https://github.com/Stalkeros2/STALKER-13)@[1ad74ef093...](https://github.com/Stalkeros2/STALKER-13/commit/1ad74ef0939fc81f96ea3e4485a0b82406a6d22e)
#### Thursday 2022-11-10 04:29:31 by ProtivogaSpriter

FUCK YOU FUCK YOU

FUCK YOU!!!!

this literally comments out the entire renegades job file

---
## [Stalkeros2/STALKER-13](https://github.com/Stalkeros2/STALKER-13)@[fa6e6ee157...](https://github.com/Stalkeros2/STALKER-13/commit/fa6e6ee1574cec2561d35f89969beaa595f11094)
#### Thursday 2022-11-10 04:29:31 by emoats18

Merge pull request #214 from ProtivogaSpriter/srptotr

FUCK YOU FUCK YOU

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[c76ee8e438...](https://github.com/ammarfaizi2/linux-fork/commit/c76ee8e438657393c14ed956bb917f4efb89bd80)
#### Thursday 2022-11-10 04:36:12 by Dan Williams

fsdax: wait on @page not @page->_refcount

Patch series "Fix the DAX-gup mistake", v3.

ZONE_DEVICE was created to allow for get_user_pages() on DAX mappings.  It
has since grown other users, but the main motivation was gup and
synchronizing device shutdown events with pinned pages.  Memory device
shutdown triggers driver ->remove(), and ->remove() always succeeds, so
ZONE_DEVICE needed a mechanism to stop new page references from being
taken, and await existing references to drain before allowing device
removal to proceed.  This is the origin of 'struct dev_pagemap' and its
percpu_ref.

The original ZONE_DEVICE implementation started by noticing that 'struct
page' initialization, for typical page allocator pages, started pages at a
refcount of 1.  Later those pages are 'onlined' by freeing them to the
page allocator via put_page() to drop that initial reference and populate
the free page lists.  ZONE_DEVICE abused that "initialized but never
freed" state to both avoid leaking ZONE_DEVICE pages into places that were
not ready for them, and add some metadata to the unused (because refcount
was never 0) page->lru space.

As more users of ZONE_DEVICE arrived that special casing became more and
more unnecessary, and more and more expensive.  The 'struct page'
modernization eliminated the need for the ->lru hack.  The folio work had
to remember to sprinkle special case ZONE_DEVICE accounting in the right
places.  The MEMORY_DEVICE_PRIVATE use case spearheaded much of the work
to support typical reference counting for ZONE_DEVICE pages and allow them
to be used in more kernel code paths.  All the while the DAX case kept its
tech debt in place, until now.

However, while fixing the DAX page refcount semantics and arranging for
free_zone_device_page() to be the common end of life of all ZONE_DEVICE
pages, the mitigation for truncate() vs pinned DAX pages was found to be
incomplete.  Unlike typical pages that surprisingly can remain pinned for
DMA after they have been truncated from a file, the DAX core must enforce
that nobody has access to a page after truncate() has disconnected it from
inode->i_pages.  I.e.  the file block that is identical to the page still
remains an extent of the file.  The existing mitigation handled explicit
truncate while the inode was alive, but not the implicit truncate right
before the inode is freed.

So, in addition to moving DAX pages to be refcount-0 at idle, and add
'break_layouts' wakeups to free_zone_device_page(), this series also
introduces another occurrence of 'break_layouts' to the inode freeing
path.  Recall that 'break_layouts' for DAX is the mechanism to await code
paths that previously arbitrated page access to drop their interest /
page-pins.  This new synchronization point is implemented by special
casing dax_delete_mapping_entry(), called by truncate_inode_pages_final(),
to await page pins when mapping_exiting() is true.

Thanks to Jason for the nudge to get this fixed up properly and the review
on v1, Dave, Jan, and Jason for the discussion on what to do about the
inode end-of-life-truncate problem, and Alistair for cleaning up the last
of the refcount-1 assumptions in the MEMORY_DEVICE_PRIVATE users.


This patch (of 25):

The __wait_var_event facility calculates a wait queue from a hash of the
address of the variable being passed.  Use the @page argument directly as
it is less to type and is the object that is being waited upon.

Link: https://lkml.kernel.org/r/166579181584.2236710.17813547487183983273.stgit@dwillia2-xfh.jf.intel.com
Link: https://lkml.kernel.org/r/166579182271.2236710.15120970389485390592.stgit@dwillia2-xfh.jf.intel.com
Signed-off-by: Dan Williams <dan.j.williams@intel.com>
Reviewed-by: Jason Gunthorpe <jgg@nvidia.com>
Cc: Matthew Wilcox <willy@infradead.org>
Cc: Jan Kara <jack@suse.cz>
Cc: "Darrick J. Wong" <djwong@kernel.org>
Cc: Christoph Hellwig <hch@lst.de>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Daniel Vetter <daniel@ffwll.ch>
Cc: Dave Chinner <david@fromorbit.com>
Cc: David Airlie <airlied@linux.ie>
Cc: Felix Kuehling <Felix.Kuehling@amd.com>
Cc: Jerome Glisse <jglisse@redhat.com>
Cc: Karol Herbst <kherbst@redhat.com>
Cc: Lyude Paul <lyude@redhat.com>
Cc: "Pan, Xinhui" <Xinhui.Pan@amd.com>
Cc: kernel test robot <lkp@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [neoGeneva/omnisharp-roslyn](https://github.com/neoGeneva/omnisharp-roslyn)@[efeafeca33...](https://github.com/neoGeneva/omnisharp-roslyn/commit/efeafeca33abe1d19659ed8c7ebab1d7c3481188)
#### Thursday 2022-11-10 07:18:17 by Fredric Silberberg

Host dependency cleanup

Today, we delete a a few dlls in the cake packaging scripts, to remove DLLs that should come from the runtime we're loaded with, rather than the dlls we built with. This is fine for packaging, but is annoying when doing local tests by just rebuilding the relevant driver, because you have to remember to go into the output directly and delete them every time. I addressed this by removing the dlls in msbuild itself:

* System.Configuration.ConfigurationManager: this was a transitive dependency through Microsoft.CodeAnalysis.Features -> Microsoft.CodeAnalysis.Elfie. We don't need Elfie or its dependencies, so I made all references to these layers explicit and turned off flowing of transitive dependencies. This does cause a slight issue: one of those transitive dependencies is System.Text.Json 6.0, while OmniSharp.MSBuild transitively references 5.0. To ensure the appropriate binding redirects are still generated, I added an explicit reference to System.Text.Json, but we are not using that reference for anything else.
* Nuget.*.dll: these are real dependencies that we should not ship in .NET 6+. I added a target to remove that version from the list of files to be copied.

---
## [stackotter/delta-client](https://github.com/stackotter/delta-client)@[6418ed402f...](https://github.com/stackotter/delta-client/commit/6418ed402fea3152885c00892d32b15c0b948dfd)
#### Thursday 2022-11-10 09:37:06 by stackotter

I hate OpenSSL, it took 6 hours of my life (I think it hates me too)

I got online-mode server support working again by fixing a typo in SHA hash generation
and implementing RSA myself cause OpenSSL wouldn't work whatsoever

---
## [Perkedel/perkedel-astro](https://github.com/Perkedel/perkedel-astro)@[5c72c29d3e...](https://github.com/Perkedel/perkedel-astro/commit/5c72c29d3eede51649c994b8b347e9355959f784)
#### Thursday 2022-11-10 10:23:01 by Joel Robert Justiawan

miss spell

K is not cultured! he expect you to ask DM even after you pirated his content, claiming to avoid copyright.

People how do you feel if somebody photographed your paiting, shared it on internet, edited it horrible into say Beautiful lady, while nobody knows if it is say Mona Lisa. All this to avoid reference. How does it fell to be misrepresented? how does it feel that your painting shared without correct name in the description but instead Hollow Knight 💀💀💀💀💀💀💀💀💀💀💀?

https://kemono.party/patreon/user/55351025

how does it feel that nobody can't share the information because I think every PM has personalized copy, compromising our heroes?

---
## [satr9/landing](https://github.com/satr9/landing)@[d23d109a14...](https://github.com/satr9/landing/commit/d23d109a1418794e143fd01f4c4aef6a7e8c592c)
#### Thursday 2022-11-10 13:07:51 by satr9

Style action section and footer...awfully again

Finish the page. Finish. Haha. As one can see, it is beyond terrible.
Just awful garbage page. Looks fucking shit. "Styled" the call to
action section and the footer. It's so bad there's visible garbage
on the page. But at this point, who gives a fuck?...

---
## [Bartimeus973/goonstation](https://github.com/Bartimeus973/goonstation)@[693f38836f...](https://github.com/Bartimeus973/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Thursday 2022-11-10 13:20:43 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [ElRealMitch/42git_ctf](https://github.com/ElRealMitch/42git_ctf)@[f6bf03369e...](https://github.com/ElRealMitch/42git_ctf/commit/f6bf03369e95d41db062bdfecd42890319816953)
#### Thursday 2022-11-10 13:31:34 by jcervoni

UPDATE THIRD_CONV :

Still playin around with deprecated magic number. The result could
be interesting huhu...
remember git commands push/pull are used for updating respectively
distant and local repo. Pull is, in reality, a call to several git
commands, find them to understand what really does git pull.
By the way, this version of third function is ok. Really. You have
to keep it. The main function looks awfull, don´t keep this one;

 Changes to be committed:
	modified:   golden_rules.c

---
## [AishuKeeriSahi/Recommender_Project](https://github.com/AishuKeeriSahi/Recommender_Project)@[12eb8f73d0...](https://github.com/AishuKeeriSahi/Recommender_Project/commit/12eb8f73d00acd8a8e1651f29a7c0354c49097d2)
#### Thursday 2022-11-10 14:13:04 by AishuKeeriSahi

Add files via upload

We are going to obtain users emotion at the moment. It uses tkinter as a sketchy
demonstration of user interface.Users are able to select multiple emotions.
There are 10 categories of emotion the system presented to users to choose from. These are 5 postive emotions ("Happy", "Satisfied", "Peaceful", "Excited", "Content") and 5 negative emotions ("Sad", "Angry", "Fearful", "Depressed", "Sorrowful"). These emotions taken as inputs from the GUI interface we built through tkinter.
The correspondence of every emotion with genre of movies are set up as below:
• Happy - Horror
• Sad - Drama
• Satisfied - Animation
• Angry - Romance
• Peaceful - Fantasy
• Fearful - Adventure
• Excited - Crime
• Depressed - Comedy
• Content - Mystery
• Sorrowful - Action
Based on the inputted emotion, the system is going to be selected from the corresponding genre based on their ratings given by two websites: IMDB and Rotten Tomatoes. The reason why we are collecting movie information from both websites is that we believe the system is able to capture a more full-scaled opinions from movie lovers.

---
## [Moribun/sunset-wasteland](https://github.com/Moribun/sunset-wasteland)@[fcd5d9077e...](https://github.com/Moribun/sunset-wasteland/commit/fcd5d9077eda7e5b14cd90f761d4f8b52adab669)
#### Thursday 2022-11-10 15:13:39 by Moribun

Bug fix

this was busted before I even touched it and im fucking glad I did. this is what has been breaking defibs. when you toxin removed someone it removes the toxin but doesnt count to the overall heal. its why you had to melee damage them after removing it for the game to register there new health state when dead. I gave a very shitty fix to it but it works. set it to give light light light .01 brute damage on each step. so the game will register the over all health change

---
## [dawsonkeyes/master-skyrat](https://github.com/dawsonkeyes/master-skyrat)@[bbaefcefeb...](https://github.com/dawsonkeyes/master-skyrat/commit/bbaefcefebf4200cf30456cfdb3cbfdb30af6c49)
#### Thursday 2022-11-10 16:21:44 by SkyratBot

[MIRROR] UpdatePaths Readme - Reforged [MDB IGNORE] (#17204)

* UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

* UpdatePaths Readme - Reforged

Co-authored-by: san7890 <the@san7890.com>

---
## [jgunthorpe/linux](https://github.com/jgunthorpe/linux)@[dd22e60e55...](https://github.com/jgunthorpe/linux/commit/dd22e60e556599dd5c634c5e4039a301ec19413d)
#### Thursday 2022-11-10 18:04:30 by Jason Gunthorpe

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
Cc: Anthony Krowiak <akrowiak@linux.ibm.com>
Cc: Halil Pasic <pasic@linux.ibm.com>
Cc: Jason Herne <jjherne@linux.ibm.com>
Signed-off-by: Jason Gunthorpe <jgg@nvidia.com>

---
## [Sarthak-Sidhant/week](https://github.com/Sarthak-Sidhant/week)@[41545c6055...](https://github.com/Sarthak-Sidhant/week/commit/41545c6055d8157c812f181f734a1b3560b1bcfd)
#### Thursday 2022-11-10 18:19:25 by Sarthak Sidhant

Unit Converter

A Converter that Converts the Converted Value Of The Converted Units.
FUCK YOU IMPERIAL

---
## [BSData/horus-heresy](https://github.com/BSData/horus-heresy)@[ab6d842785...](https://github.com/BSData/horus-heresy/commit/ab6d8427859a41e472f3b74db50dcfb7fd337fa4)
#### Thursday 2022-11-10 18:22:33 by Mayegelt

Power Daggers on RoT units

Crimson Paladins,
Dawnbreakers
Angels Tears
Interemptor Squad
Inner Circle Cenobuim (and broken claws) all models
Grave Wardens
Mortus Poisoner
Kakophoni
Palatine Blade & Aquilae
Phoenix Termy
Sun Killer
Huscarl
Phalanx Warder
Templar Brethren
Gorgon Termy
Medusan Immortals
Iron Havocs
Tyrant Siege Termy
Atramentar
Contekar
Night Raptor
Terror Squad
Dark Furies
Deliverers
Mor Deythan
Firedrakes
Pyroclast
Reaver Aggressor and Reaver Attack squads
Gray Stalkers
Gray Slayers
Jorlund Hunter
Varagyr Wolf Guard
Ammitara Occult
Khenetai
Numerologist
Sekhmet
Fulmentarus
Invictarus Suzerain (looks a bit messy due to currently all collectives, and every model is a character, but will only affect AL players. Might be able to be tidied up later)
Locutarus
Nemesis Destroyer
Praetorian Breacher
Dark Sons of Death
Falcon's Claws
Golden Keshig
Ashen Circle
Rampager
Red Butchers
Red Hand Destroyers

---
## [vijithassar/bisonica](https://github.com/vijithassar/bisonica)@[5151b4a2f2...](https://github.com/vijithassar/bisonica/commit/5151b4a2f265a2b081f04aec5f5d6b89cc7db1bf)
#### Thursday 2022-11-10 18:54:25 by Vijith Assar

chore(core): don't use typeof in undefined checks

Removes typeof checks everywhere a conditional checks for an undefined value. This was once a historical best practice because it used to be possible to change the value of undefined, but that's no longer the case in modern browsers. This change also means that an undefined check with a variable that has not been declared will throw a ReferenceError. That used to be sort of scary, but it's more disciplined to allow them – those errors should be early and catastrophic so as to encourage code styles where they are still impossible because they are appropriately guarded against.

In theory, this does make it a bit harder to get inside the conditionals where errors are thrown, which is a bit of a shame – instead of the helpful error message text, you'd get a cryptic ReferenceError, because the ReferenceError blocks the code path into the better error message!

But none of this matters, because the linter should prevent this kind of mistake anyway.

---
## [soynain/microservice-practice](https://github.com/soynain/microservice-practice)@[c6d4d86b82...](https://github.com/soynain/microservice-practice/commit/c6d4d86b823ba82eaa2497ddb76a7d24ac0a8097)
#### Thursday 2022-11-10 19:18:49 by Moises

API GATEWAY FINALLY FUCKING WORKKING, problem was the cors overlapping, I had to set the default cors headers in the gateway api microservice application properties file to get it to work. I have to configure the rest of the cors in the rest of the microservices and, yeah, we are going for less shit to code

---
## [Lombra/Critline](https://github.com/Lombra/Critline)@[40ce6ffb66...](https://github.com/Lombra/Critline/commit/40ce6ffb667edf7cabc43198e1d50e67bfbc892b)
#### Thursday 2022-11-10 19:46:48 by lombra

- Register UNIT_AURA to let aura tracker pick up auras that does not trigger a combat log event.
- Add Fel Rage (Gurtogg Bloodboil), Primsatic auras (Mother Shahraz), Shadow Walk (Well of Eternity, additional spell ID), Ysera's and Kalecgos's Presences and Expose Weakness to aura filters.
- Add Ancestral Awakening, Cleansing Waters, Echo of Light, Holy Words: Serenity and Sanctuary to player spells.
- Use more aggressive aura filtering; as soon as you gain a filtered aura, no more records will be registered for the remainder of the encounter, and no more records will be registered on a target once it's gained a filtered aura. (even after it fades, in both cases)

---
## [alemidev/dashboard](https://github.com/alemidev/dashboard)@[88e07a502a...](https://github.com/alemidev/dashboard/commit/88e07a502a32a298316344bc78b685e85600a4f1)
#### Thursday 2022-11-10 21:04:33 by alemidev

fix: maybe no more weird freezes?

this is a weird one: sometimes, after sending some changes to the state
worker, the GUI will completely freeze. No error or panic reported, just
completely frozen, must be terminated and restarted. This is super
annoying! I tried to debug it, and it seems that the main GUI thread
gets blocked inside an unsafe block of crate `parking_lot` invoking a
FUTEX syscall (Fast Userspace muTEX). Climbing up the stack trace, it
seems to be originating from accessing a watch channel, specifically
when rendering panels. I noticed that there were unnecessary borrow
calls, and slimmed them down, and still haven't experienced it again.
Which is weird! Seems like a very "magic" fix, but it is to be expected
with race conditions, and this looks to be the case. I could quite
reliably reproduce it with ~20 metrics on ~4 sources set up.

idk, I just want this fixed, but I'm still super bummed I didn't catch
the culprit...

---
## [sunset-wasteland/sunset-wasteland](https://github.com/sunset-wasteland/sunset-wasteland)@[0da80ad53e...](https://github.com/sunset-wasteland/sunset-wasteland/commit/0da80ad53e5db8126fb8adeff3fa3a4b80e843b5)
#### Thursday 2022-11-10 21:31:04 by Carl?

Khan Pass | Part Two (#701)

- - -
Balance:
 - Khan Senior Enforcer given a Khan scrap sabre.
 - Khan scrap sabre now able to be crafted by anyone in the faction.
 - Legion Forgemaster lost their standard welding tool, given they have a basic one in their belt.
 - Neostead lootdrop updated to exclusively contain trainshot, rather than a mix of buckshot and slugs.
- - -
Map:
 - Water in Rock Springs once again made safe. Somehow this was left scuffed and no one caught it until I took a look myself.
 - Khans given a second level to their camp, which is just a double-stacked tent for chemistry and an overlook of the gate.
 - Khans given control of Heaven's Knight, with a ladder leading to and from it accessible via their mining area.
 - Bighorn given a magical disposal bin. Enjoy.
 - Pool closed.
- - -
New | Khan:
 - Khan Smith added. They're near identical in function to the Legion Forgemaster.
 - Khan Courtesan added. They're an RP exclusive role and are fairly self-explanatory.
- -

---
## [AquillaF/Shiptest](https://github.com/AquillaF/Shiptest)@[3efa9b5382...](https://github.com/AquillaF/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Thursday 2022-11-10 22:47:03 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [TheRealJake12/Kade-Engine-Community](https://github.com/TheRealJake12/Kade-Engine-Community)@[e69c4ebf99...](https://github.com/TheRealJake12/Kade-Engine-Community/commit/e69c4ebf99deb6c36cecdce12e4e25bc1f932bf7)
#### Thursday 2022-11-10 23:38:24 by TheRealJake_12

I am so sorry it took so long

and everything is broken fuck 1.6 I hate everything

---
## [DanielBainbridge/Hareborne_HDRP](https://github.com/DanielBainbridge/Hareborne_HDRP)@[86392ffe36...](https://github.com/DanielBainbridge/Hareborne_HDRP/commit/86392ffe362855e558448be1094dbe1fd9033924)
#### Thursday 2022-11-10 23:50:47 by FynnCat

Merge pull request #41 from DanielBainbridge/FynnBranch

A bunch of things, very import, just pull it right now... Why haven't you done it yet? I said now. Bloody hell. This is getting ridiculous, just do it & get back to work.

---

