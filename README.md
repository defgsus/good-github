## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-30](docs/good-messages/2021/2021-12-30.md)


1,530,669 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,530,669 were push events containing 2,110,072 commit messages that amount to 141,378,056 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 24 messages:


## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[fab444ffe2...](https://github.com/Tastyfish/Skyrat-tg/commit/fab444ffe2887cb2838f974a41c392ed48d2ae6e)
#### Thursday 2021-12-30 00:32:00 by Seris02

[modular] big borg code improvements and fixes (#9701)

* big borg code improvements and fixes

* I missed a modular comment

* fuck you linters

* yis

* converts skyrat versions to better

* annnnnd that should fix it

---
## [lkkuma/Project-Luna](https://github.com/lkkuma/Project-Luna)@[0866aa468a...](https://github.com/lkkuma/Project-Luna/commit/0866aa468a33a9fd1168e9d098920972b4fe5941)
#### Thursday 2021-12-30 00:37:32 by 0Tateki0

EverDawn_Tateki_1

\<Beginning of development under name: "EverDawn">

This changelog will largely be dealing with fixing issues that occurred due to the branch merge.

[Start of Changes]

Moved `Menu Camera` up to Y = 200 just to get it out of the way of the gameplay scene. (and out of the river).

Created a new Scene: `Title_Scene`

The title screen functions as a typical title screen but will likely also have other features that may be needed in case of a damaged download or something of the like. (Creating some sort of method to clear cache for example if there happens to be an issue that prevents the game from booting into the main menu for whatever reason. I've seen it happen in some of the mobile games I play and I'd rather play it safe than sorry to get features like this implemented in case of an issue.) The scene is then intended to be unloaded after the main menu is loaded and other functionality is confirmed to have loaded correctly.

Added an end game/surrender button into `InGameScene` this just unloads `InGameScene` by directly loading `Main_Menu_Scene`

Created `End_Game_Canvas` in `InGameScene` to eventually display game results and etc. It should be activated after the game ends. It also has a button to load back into the main menu.

Created `EndGame()` in `GameManager.cs` which runs when a player's score reaches 3. It destroys all GameObjects and TowerObjects that the game manager has in its respective lists and removes them from said lists. This is not yet implemented with the timer or if the player's keep dies.

It should then hide the gameplay HUD and display the end of game screen. but man am I having some trouble with object references so this part of the code is currently commented out

Added text to the game queue/loading overlay

Added Pot's meme logo into the project as the title screen as `Title_Screen_Background_Moon` which has an attached script `Moon_Background_Temp_Animator` which basically just makes it act like a panorama.

Preemptively changed the `Scene_Loader_Unloader` script to make it a singleton. This is commented out as other objects that need it don't have the functionality to use it as a singleton yet though. Eventually, this object should be used as a singleton that's instantiated at boot or something, opposed to existing in all scenes independently. It's also a prefab now that is added in all scenes under the "loading" type of empty.

Created a basic singleton type script called `Data_Storage` that is capable of serializing a file through C#'s built in means. This was more meant as a test to see how C# goes about serializing files and uses a super basic like cookie cutter type method of going about it. All it currently does is create a binary file which stores a list which could theoretically be used to store what cards are selected. There is not currently anything implemented that uses this script.

The bottom menu selection buttons are no longer setup as a toggle group, but are now managed by the `UI_Tab_Group` and `UI_Tab_Button` scripts. These scripts should allow for flexible Tab System implementation. I'm to expand the functionality of these scripts in the future (ex: probably also going to add color options eventually).

Added a couple sprites - some jokes, some for the tab system, etc. One is a slightly edited version of one of Noden's concept arts. (Changed to be 16x9 resolution and gave it a transparent background.) I just needed something a little closer to what we'd actually be working with so I can work on adjusting the positioning and stuff of character backgrounds in the future.

---
## [wingedrhino/DistroSetup](https://github.com/wingedrhino/DistroSetup)@[1810975a55...](https://github.com/wingedrhino/DistroSetup/commit/1810975a55e992a7030d55dc3ff76eb91e963bdf)
#### Thursday 2021-12-30 04:35:31 by wingedrhino

Changed byobu-ctrl-a to screen

* Chromebooks don't ship with function keys
* A recent ChromeOS update means that you need to use search+mediakeys
  for function keys
* This means you need to COUNT the fucking keys to get to a goddamned
  function key
* Also, there is no F11 or F12 anymore on ChromeOS.
* Fuck you Google!

---
## [ksh93/ksh](https://github.com/ksh93/ksh)@[4491bc6a99...](https://github.com/ksh93/ksh/commit/4491bc6a991759b61c5f7d49dd0477a2f2bfb1a1)
#### Thursday 2021-12-30 05:16:41 by Martijn Dekker

[shp cleanup 00] Reunify the original sh state struct

As observed previously (see 3654ee73, 7e6bbf85, 79d19458), the ksh
93u+ codebase on which we rebased development was in a transition:
AT&T evidently wanted to make it possible to have several shell
interpreter states in the same process, which in theory would have
made it possible to start a complete new shell (not just a
subshell) without forking a new process.

This required transitioning from accessing the 'sh' state struct
directly to accessing it via pointers (usually but not always
called 'shp'), introducing a lot of bug-prone passing around of
those pointers via function arguments and other state structs.

Some of the original 'sh' struct was separated into a 'struct
shared' called 'shgd' a.k.a. 'sh.gd' (global data) instead; these
were global state variables that were going to be shared between
the different main shell environments sharing a process. Yet, for
some reason, that struct was allocated dynamically once at init
time, requiring yet another pointer to access it. <shrug>

None of this ever worked, because that transition was incomplete.
It was much further along in the ksh 93v- beta, but I don't think
it actually worked there either (not very much really did). So,
starting a new shell has always required starting a new process.

So, now that it's clear what they were trying to do, should we try
to make it work? I'm going to go with a firm "no" on that question.

Even non-forking (virtual) subshells, something quite a bit less
ambitious, were already an unmitigated nightmare of bugs. In 93u+m
we fixed a load of bugs related to those, but I'm sure there are
still many left. At the very least there are multiple memory leaks.

I think the ambition to go even further and have complete shells
running separate programs share a process, particularly given the
brittle and buggy state of the existing codebase, is evidence that
the AT&T team, in the final years, had well and truly lost the
ability to think "wait a minute, aren't we in over our heads here,
and why are we doing this again? Is this *actually* a feasible and
useful idea?"

In my view, having entirely separate programs share a process is a
*terrible*, horrible, no-good idea that takes us back to the bad
old days before Unix, when kernels and CPUs were unable to enforce
any memory access restrictions. Programmers are imperfect. If
you're going to run a new program, you need the kernel to enforce
the separation between programs, or you're just asking for memory
corruption and security holes. And that separation is enforced by
starting a new program in a new process. That's what processes are
*for*. And if you need *that* to be radically performance-optimised
then you're probably doing it wrong anyway.

(By the way, I would still argue the same for subshells, even after
we fixed many bugs in virtual subshells. But forking all subshells
would in fact cause many scripts to slow down, and the community
would surely revolt. <sigh>  Maybe I should make it a shell option
instead, so scripts can 'set -o subfork' for reliability.)

It is also unclear how they were going to make something like
'ulimit' work, which can only work in a separate process. There
was no sign of a mechanism to fork a separate program's shell
mid-execution like there is for subshells (sh_subfork()).

Anyway... I had already changed some code here and there to access
the sh state struct directly, but as of this commit I'm beginning
to properly undo this exercise in pointlessness. From now on, we're
exercising pointerlessness instead.

I'll do this in stages to make any problems introduced more
traceable. Stage 0 restores the full 'sh' state struct to its
former static glory and reverts 'shgd' as a separate entity.

src/cmd/ksh93/sh/defs.c,
src/cmd/ksh93/include/defs.h,
src/cmd/ksh93/include/shell.h
src/cmd/ksh93/Mamfile::
- Move 'struct sh_scoped' and 'struct limits' from defs.h to
  shell.h as the sh struct will need their complete definitions.
- Get rid of 'struct shared' (shgd) in defs.h; its members are
  folded back into their original place, the main Shell_t struct
  (sh) in shell.h. There are no name conflicts.
- Get rid of the _SH_PRIVATE macro in defs.h. The members it
  defines are now defined normally in the main Shell_t struct (sh)
  in shell.h.
- To make this possible, move <history.h> and "fault.h" includes
  from defs.h to shell.h and update the Mamfile accordingly.
- Turn sh_getinterp() and shgd into macros that resolve to (&sh).
  This will allow the compiler to optimise out many pointer
  dereferences already.
- Keep extern sh_getinterp() for libshell ABI compatibility.

src/cmd/ksh93/sh/init.c:
- sh_init(): Do not calloc (sh_newof) the sh or shgd structs.
- sh_getinterp(): Keep function for libshell ABI compat.

---
## [Jprimero15/lolz_kernel_redmi8](https://github.com/Jprimero15/lolz_kernel_redmi8)@[1ab5536ea8...](https://github.com/Jprimero15/lolz_kernel_redmi8/commit/1ab5536ea8ad8eaaea6813887ce0d9962fe3b9d0)
#### Thursday 2021-12-30 08:14:14 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>

Conflicts:
	mm/swapfile.c

---
## [wobbier/MitchEngine](https://github.com/wobbier/MitchEngine)@[fbd94b9b47...](https://github.com/wobbier/MitchEngine/commit/fbd94b9b4763453b2f347920216a81de76e60d3a)
#### Thursday 2021-12-30 09:32:38 by Mitch Andrews

🍓 Everything works (on windows lmao), minus DLL copying, and UWP

oh yeah and some stupid ImGui shit

---
## [cokia/aws-cdk](https://github.com/cokia/aws-cdk)@[c071367def...](https://github.com/cokia/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Thursday 2021-12-30 11:12:34 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [Favouriteless/Enchanted](https://github.com/Favouriteless/Enchanted)@[af55f010b5...](https://github.com/Favouriteless/Enchanted/commit/af55f010b54d30b3ffabfdca4bccc1d491f1e53d)
#### Thursday 2021-12-30 11:22:08 by Favouriteless

Rite of sanctity

cool as fuck particles omg i love it so much

---
## [Roy-043/FreeCAD](https://github.com/Roy-043/FreeCAD)@[92e6094449...](https://github.com/Roy-043/FreeCAD/commit/92e6094449275e89e6ffd7a74c32e3ce3c62c1e6)
#### Thursday 2021-12-30 11:46:36 by Abdullah Tahiri

Sketcher: EditModeCoinManager/DrawSkechHandler refactoring

======================================================

Creation of EditModeCoinManager class and helpers.

In a nutshell:
- EditModeCoinManager gets most of the content of struct EditData
- Drawing is partly outsourced to EditModeCoinManager
- EditModeCoinManager gets a nested Observer class to deal with parameters
- A struct DrawingParameters is created to store all parameters used for drawing
- EditModeCoinManager assume responsibility for determining the drawing size of the Axes
- Preselection detection responsibility is moved to EditModeCoinManager.
- Generation of constraint nodes and constraint drawing is moved to EditModeCoinManager.
- Constraint generation parameters are refactored into ConstraintParameters.
- Text rendering functions are moved to EditModeCoinManager.
- Move HDPI resolution responsibility from VPSketch to EditModeCoinManager
- Move responsibility to create the scenograph for edit mode to EditModeCoinManager
- Move full updateColor responsibility to EditModeCoinManager
- Allows for mapping N logical layers (LayerId of GeometryFacade) to M coin Layers (M<N). This
is convenient as, unless the representation must be different, there is no point in creating coin
layers (overhead).

Refactoring of geometry drawing:
- Determination of the curve values to draw are outsourced to OCC (SRP and remove code duplications).
- Refactor specific drawing of each geometry type into a single template method, based on classes of geometry.
- Drawing of geometry and constraints made agnostic of scale factors of BSpline weights so that a uniform treatment can be provided.

Refactoring of Overlay Layer:
- A new class EditModeInformationOverlayConverter is a full rewrite of the previous overlay routines.

ViewProviderSketch:
- Major cleanup due to migration of functionalities to EditModeCoinManager
- Reduce public api of ViewProviderSketch due to refactor of DrawSketchHandler
- Major addition of documentation
- ShortcutListener implementation using new ViewProvider Attorney
- Gets a parameter handling nested class to handle all parameters (observer)
- Move rubberband to smart pointer
- Refactor selection and preselection into nested classes
- Removal of SEL_PARAMS macro. This macro was making the code unreadable as it "captured" a local stringstream that appeared unused. Substituted by local private member functions.
- Remove EditData
- Improve documentation
- Refactor Preselection struct to remove magical numbers
- Refactor Selection mechanism to remove hacks

ViewProviderSketchDrawSketchHandlerAttorney:
- new Attorney to limit access to ViewProviderSketch and reduce its public interface
- In order to enforce a certain degree of encapsulation and promote a not too tight coupling, while still allowing well
defined collaboration, DrawSketchHandler accesses ViewProviderSketch via this Attorney class.
-DrawSketchHandler has the responsibility of drawing edit temporal curves and markers necessary to enable visual feedback
to the user, as well as the UI interaction during such edits. This is its exclusive responsibility under the Single
Responsibility Principle.
- A plethora of speciliased handlers derive from DrawSketchHandler for each specialised editing (see for example all the
handlers for creation of new geometry). These derived classes do * not * have direct access to the
ViewProviderSketchDrawSketchHandlerAttorney. This is intentional to keep coupling under control. However, generic
functionality requiring access to the Attorney can be implemented in DrawSketchHandler and used from its derived classes
by virtue of the inheritance. This promotes a concentrating the coupling in a single point (and code reuse).

EditModeCoinManager:
- Refactor of updateConstraintColor
- Multifield - new struct to identify a single element in a multifield field per layer
- Move geometry management to delegate class EditModeCoinGeometryManager
- Remove refactored code that was never used in the original ViewProviderSketch.

CommandSketcherBSpline:
- EditModeCoinManager automatically tracks parameter change and triggers the necessary redraw, rendering an explicit redraw obsolete and unnecessary.

Rebase on top of master:
- Commits added to master to ViewProviderSketch applied to EditModeCoinManager.
- Memory leaks - wmayer
- Constraint Diameter Symbol - OpenBrain
- Minor bugfix to display angle constraints - syres

Architecture Description
=======================

* Encapsulation and collaboration - restricting friendship - reducing public interface

Summary:
- DrawSketchHandler to ViewProviderSketch friendship regulated via attorney.
- ShortcutListener to ViewProviderSketch friendship regulated via attorney.
- EditModeCoinManager (new class) to ViewProviderSketch friendship regulated via attorney.
- ViewProviderSketch public interface is heavily reduced.

In further detail:
While access from ViewProviderSketch to other classes is regulated via their public interface, DrawSketchHandler, ShortcutListener and EditCoinManager (new class) access
to ViewProviderSketch non-public interface via attorneys. Previously, it was an unrestricted access (friend classes). Now this interface is restricted and regulated via attorneys.
This increases the encapsulation of ViewProviderSketch, reduces the coupling between classes and promotes an ordered growth. This I call the "collaboration interface".

At the same time, ViewProviderSketch substantially reduces its public interface. Access from Command draw handlers (deriving from DrawSketchHandler) is intended to be restricted to
the functionality exposed by DrawSketchHandler to its derived classes. However, this is still only partly enforced to keep the refactoring within limits. A further refactoring of
DrawSketchHandler and derivatives is for future discussion.

* Complexity and delegation

Summary:
- Complexity of coin node management is dealt with by delegation to helper classes and specialised objects.

In further detail:

ViewProviderSketch is halved in terms of code size. Higher level ViewProviderSketch functions remain

* Automatic update of parameters - Parameter observer nested classes

Summary:
- ViewProviderSketch and CoinManager get their own observer nested classes to monitor the parameters relevant to them and automatically update on change.

The split enables that each class deals only with parameters within their own responsibilities, effectively isolating the specifics and decoupling the implementations. It is
more convenient as there is no need to leave edit mode to update parameters. It is more compact as it leverages core code.

More information:
https://forum.freecadweb.org/viewtopic.php?p=553257#p553257

---
## [PixelExperience-Devices/kernel_oneplus_sm7250](https://github.com/PixelExperience-Devices/kernel_oneplus_sm7250)@[4c776067fc...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm7250/commit/4c776067fc746e330cfb3d561bee7925b7071759)
#### Thursday 2021-12-30 12:04:15 by Art_Chen

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
## [MiezeMC/PocketMine-MP](https://github.com/MiezeMC/PocketMine-MP)@[d9c70cb176...](https://github.com/MiezeMC/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Thursday 2021-12-30 12:39:00 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [rk134/kernel_threadripper_vince](https://github.com/rk134/kernel_threadripper_vince)@[83cacca694...](https://github.com/rk134/kernel_threadripper_vince/commit/83cacca694d1a144b85d8d305093ade5c34b3045)
#### Thursday 2021-12-30 13:37:27 by Maciej Żenczykowski

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
## [FlamingCheese/tgstation](https://github.com/FlamingCheese/tgstation)@[d005d76f0b...](https://github.com/FlamingCheese/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Thursday 2021-12-30 13:57:16 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [LongSleeves/sojourn-station](https://github.com/LongSleeves/sojourn-station)@[66a6e3d75b...](https://github.com/LongSleeves/sojourn-station/commit/66a6e3d75b1fd8cd72b3b22441443186c71832da)
#### Thursday 2021-12-30 14:41:50 by Bones

More Genes then JC Pennies!

bottomless belly given to doggos. Increases max capacity for nutrition to 4 times the amount. good for long journeys if you can fill up. -10%
cat eyes on panthers and cats. Gives increased dark vision. Flashes will wreck your ass. -20%
cold resistance renamed into Thick Fur. Thick fur given to bears and corgis of all kind (protect Ian)  Now gives 10% brute resist along with cold resistance. Gives 10% burn weakness and takes up skin mutation slot - 20% instability.
honk given to geese. Literally just makes you honk like a dork
Echolocation given to bats.  allows you to see without eyes. -40% (If people abuse this with organ insertions I will make it turn your vision fucking black)
screaming given to possoms. Like moo and honk but for those who must scream!
toxin resistance given to snakes and bats. Gives a 10% reduction in toxin damage taken. 20% instability
Balances cowhide to cause 20% instability (Agreed amount with Hex)
Creates MUT_TYPE_EYES to keep from gaining all the eye genes.
Barotrauma gene added to space sharks/great whites. costs 20% instability. Gives pressure resistance.

---
## [caitlynahall/caitlynahall.github.io](https://github.com/caitlynahall/caitlynahall.github.io)@[35444b7b82...](https://github.com/caitlynahall/caitlynahall.github.io/commit/35444b7b82dfc74f7fc3d5aeb2868734a80a425b)
#### Thursday 2021-12-30 15:57:35 by caitlynahall

Update about.md

Original text: 

---
layout: page
title: About
---

<p class="message">
  Hey there! This page is included as an example. Feel free to customize it for your own use upon downloading. Carry on!
</p>

In the novel, *The Strange Case of Dr. Jeykll and Mr. Hyde*, Mr. Poole is Dr. Jekyll's virtuous and loyal butler. Similarly, Poole is an upstanding and effective butler that helps you build Jekyll themes. It's made by [@mdo](https://twitter.com/mdo).

There are currently two themes built on Poole:

* [Hyde](http://hyde.getpoole.com)
* [Lanyon](http://lanyon.getpoole.com)

Learn more and contribute on [GitHub](https://github.com/poole).

## Setup

Some fun facts about the setup of this project include:

* Built for [Jekyll](http://jekyllrb.com)
* Developed on GitHub and hosted for free on [GitHub Pages](https://pages.github.com)
* Coded with [Sublime Text 2](http://sublimetext.com), an amazing code editor
* Designed and developed while listening to music like [Blood Bros Trilogy](https://soundcloud.com/maddecent/sets/blood-bros-series)

Have questions or suggestions? Feel free to [open an issue on GitHub](https://github.com/poole/issues/new) or [ask me on Twitter](https://twitter.com/mdo).

Thanks for reading!

---
## [RonsenbergVI/probability](https://github.com/RonsenbergVI/probability)@[9b67e5abdd...](https://github.com/RonsenbergVI/probability/commit/9b67e5abdd31840b33d17f106a275fca017827ef)
#### Thursday 2021-12-30 17:25:36 by Dave Moore

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
## [CrashedLife/Simple-YouTube-Age-Restriction-Bypass](https://github.com/CrashedLife/Simple-YouTube-Age-Restriction-Bypass)@[0b9ce74230...](https://github.com/CrashedLife/Simple-YouTube-Age-Restriction-Bypass/commit/0b9ce7423094b9905337fc9cc9991dc506c1008d)
#### Thursday 2021-12-30 17:58:45 by Demirci K

[chore] remove eslint & husky (#96)

* [chore] remove eslint & husky

Currently both are a pain in the ass and hard to work with in terms of developer experience, they are more like a nuisance than a helper.

ESlint is hard to work with when unconfigured. We might add this back in later when we have enough time to write the config rules.

Husky is reasonable, but with Prettier it tends to change files which are not in the commit. Although this is solvable with `lint-staged`, the fact that your code looks different on the commit vs what you just wrote is annoying. Also the error/warning messages are a lap of text, with bunch of useless information and it also does not play nicely with a GUI based Git.

My proposal (#97) as an alternative is having CI testing on GitHub on each pull request, when it fails, the dev must manually run `npm run format`. At that point it is clear to the dev that transformation has happened to the original code and is able to review it.

* upgrade packages

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d7a9819fe1...](https://github.com/mrakgr/The-Spiral-Language/commit/d7a9819fe152efdf4516f79bd2be591c8c86aa47)
#### Thursday 2021-12-30 18:35:52 by Marko Grdinić

"10:50am. Done with chores. I had trouble falling asleep due to change in temperature, and I ended up inadvertently being waken up early by my parents. Let me chill a bit and then I will start.

11:25am. Let me start. Time to get those stars done.

11:25am. Instead of doing it like I have before, let me try the magic wand, though I doubt that will work.

11:40am. It did not work all at once, but using the auto select was a lot easier than using the g-pen. Now I have my stars. Let me give them the golden outlines.

12:25pm. Did the golden outlines for the stars. It makes them look quite nice. I could take what I have now and use it as a wallpaper.

12:30pm. This is a great spot to stop for breakfast. I'll work on reflections after breakfast.

1:25pm. Just a bit more and I will resume.

1:55pm. Let me resume. It is time to deal with the painting.

3:15pm. Right now I am on very last part. Just a bit more and I am done.

3:50pm. I am done. I did it!

Hell yeah.

4pm. I guess I'll post it in the /beg/ thread. Since I have my first real artwork, I should look into opening an artist's account somewhere. I have no idea where.

5pm. Where did the last hour go? I feel high right now. I've even sent this to my dad's email to impress him. At least one person in the /beg/ thread likes it. I am proud.

Ok, I'll set it as my wallpaper even though it would waste memory.

5:10pm. The taskbar cuts off the lower part, what a pity. But it is fine.

5:15pm. Ok, focus me. I'll want to do some research on where to post my art online. But otherwise it is yearly review time.

5:20pm. Focus me, focus.

https://share.clip-studio.com/en-us

Something like this? I don't know.

Tumblr? I have no idea. Though I won't make porn, I do not want the platform getting in the way of me posting naked girls.

Ahh, what I need is something like Pixiv.

5:35pm. Enough of this, I'll just ask in the /beg/ thread. I'll look up advice on Youtube on where to post art if that fails. Youtube hasn't failed me so far when it comes to education.

5:40pm. I need to focus on the review. Right now my brain is euphoric from finishing the piece and getting praised a bit. I want to just call it a day here, but let me at least start the review.

///

In the last review, I was in a middle of a heated battle. I though with just a push I'd be able to make the other side crumble. Bullets were blazing, but expected I would be able to push through because surely something like training a poker should be doable given how near the Singularity is. What happened that in the frenzy of battle I lost track of ammo and when I went to reload, I found my satchel empty. And the enemy which was on the verge of defeat got a fresh batch of reinforcements, ready to open fire.

I suffered a lot of mental damage when I threw in the towel back in September, and just about now my sanity points have recevered to a reasonable level. To think that in the last post I thought I was only a few weeks away from getting the agent to work.

There is no getting the poker agent plan to work with my current level of hardware. None.

The methods I had worked just fine on toy games like Leduc and even Flop poker, but pretty much everything I've tried just dies on Holdem. The only thing that worked for me was increasing the batch size by 10x to 5k, but that slows down the already very slow training to an unbearable degree. The realization that I do not have the computational power to fulfil my goal made me extremely obsessed about AI chips, to the point I actually considered getting a job for the first time, just to get the chip. During my bouts of normality, I did spent time making a resume and applying. One time I even got an offer, but it was so poor that I gave up in disgust. Maybe I shouldn't as it would have been enough to get the chip, but I honestly felt the other party was mocking me with how the negotiation went. I do not regret aborting it. Plenty of places list salary ranges and I should have stuck to those when applying.

The tech job market is such a shitshow, the reject rates make it impossible to pick something you'd like to work on, instead if you are really serious, you have to pick whatever you get. You can either focus on maximizing your salary or picking work that is meaningful.

To continue on the path of developing my external cortex I need the bare minimum of money to buy one of the Grayskull chips from TensTorrent. They cost 1-2k might not be much depending on where you live, but I have no way of getting that amount without doing paid labor. This pisses me off because I was supposed to make money of poker to make those chips in the first place. For the first time, I've felt that the path I am on is particularly weak. It is just sending me hurdles, but it is not sustaining me wit resources to keep pursuing it. It was one thing when my goal was just to make a language and a ML library, but now I need the world to cooperate.

This situation made me reflect upon my approach, and got me thinking. It is one thing try to get to human or even animal level, but I was so sure that CPU+GPU should be enough for toy games, which I'd say poker falls into. I did not expect it to get to superhuman level even there, but I wasn't prepared for the amount of struggle the crappy current day algorithms would have to endure. At this point I can only ask: if CPU+GPU aren't enough, just how sure am I that getting an AI chip would help? I mean, by porting the game directly to chip and parallelizing the training, I could get 100x performance improvements most likely. That would be enough to cover the increases in batch size necessary to do training. That is obviously right.

But what then? Past poker I'd need to scale again and run into the same again. A single chip is not going to cut it on Dota or Starcraft. Unlike Deepmind even if I had the money, I can't just open my wallet every time I run into problem. I actually want to make money off RL, not go deeply into the red for sake of research.

At the start of the year, I forcefully quashed my skepticism towards deep learning and backprop, but I think my initial impression was right after all.

If I am going to succeed, I need better algorithms. Backprop was the only choice I had, so I had to go for it, but that was a mistake.

///

7pm. Done with lunch. I'll leave the above as it is. I'll finish it tomorrow. It is energy intensive to draw these words out. It seems finishing the picture drained the energy out of me. The guys in the /beg/ thread are recommending Twitter. Twitter it shall be then. I have an old handle there from a decade ago that I never used. I'll dust it off and give it a try after I finish the review.

Tomorrow, I think I'll take a break from doing art. After finishing the review and post it on Twitter, I'll have to think what my next move is. Probably doing more of the limbo and maybe doing some cell shaded art of it. After that I'll have to get back to sculpting. I need to further improve that base mesh, and turn it into actual model with hair and colored eyes. I'll have to retopo and rig it as well. All this will take me a while, but if I can accomplish these goals, I should be just about good enough to do the art parts of Heaven's Key. It will take some work to do just the cover. A floating city covered in a golden radiance will be a decent challenge for me."

---
## [MiltosKoutsokeras/higan-1](https://github.com/MiltosKoutsokeras/higan-1)@[e6e19a7c89...](https://github.com/MiltosKoutsokeras/higan-1/commit/e6e19a7c897574491e19a17edd33664ff4d49942)
#### Thursday 2021-12-30 18:58:26 by byuu

Update to bsnes v053 release.

This release greatly polishes the user interface, adds a new cheat code search utility, adds the snesfilter library, and adds Qt-based GUI support to both snesfilter and snesreader. snesfilter gains 2xSaI, Super 2xSaI and Super Eagle support, plus full configuration for both the NTSC and scanline filters; and snesreader gains support support for multi-file ROM archives (eg GoodMerge sets.)
Statically linking Qt to bsnes, snesfilter and snesreader would be too prohibitive size-wise (~10MB or so.) I have to link dynamically so that all three can share the same Qt runtime, which gets all of bsnes and its modules to ~1MB (including the debugger build); and Qt itself to about ~2.5MB.
However, there is some bad news. There's a serious bug in MinGW 4.4+, where it is not generating profile-guided input files (*.gcno files.) There is also a serious bug in Qt 4.5.2/Windows when using dynamic linking: the library is hanging indefinitely, forcing me to manually terminate the process upon exit. This prevents the creation of profile-guided output files (*.gcda files.) It would be tough enough to work around one, but facing both of these issues at once is too much.
I'm afraid I have no choice but to disable profile-guided optimizations until these issues can be addressed. I did not know about these bugs until trying to build the official v053 release, so it's too late to revert to an all-in-one binary now. And I'm simply not willing to stop releasing new builds because of bugs in third-party software. As soon as I can work around this, I'll post a new optimized binary. In the mean time, despite the fact that this release is actually more optimized, please understand that the Windows binary will run approximately ~10% slower than previous releases. I recommend keeping v052 for now if you need the performance. Linux and OS X users are unaffected.
Changelog:
    - save RAM is initialized to 0xff again to work around Ken Griffey Jr Baseball issue
    - libco adds assembly-optimized targets for Win64 and PPC-ELF [the latter courtesy of Kernigh]
    - libco/x86 and libco/amd64 use pre-assembled blocks now, obviates need for custom compilation flags
    - added a new cheat code search utility to the tools menu
    - separated filters from main bsnes binary to libsnesfilter / snesfilter.dll
    - added 2xSaI, Super 2xSaI and Super Eagle filters [kode54]
    - added full configuration settings for NTSC and scanline filters (12+ new options)
    - further optimized HQ2x filter [blargg]
    - added Vsync support to the Mac OS X OpenGL driver
    - added folder creation button to custom file load dialog
    - fixed a few oddities with loading of "game folders" (see older news for an explanation on what this is)
    - updated to blargg's file_extractor v1.0.0
    - added full support for multi-file archives (eg GoodMerge sets)
    - split multi-cart loading again (BS-X, Sufami Turbo, etc) as required for multi-file support
    - cleaned up handling of file placement detection for save files (.srm, .cht, etc)
    - file load dialog now remembers your previous folder path across runs even without a custom games folder assigned
    - windows now save their exact positioning and size across runs, they no longer forcibly center
    - menus now have radio button and check box icons where appropriate
    - debugger's hex editor now has a working scrollbar widget
    - added resize splitter to settings and tools windows
    - worked around Qt style sheet bug where subclassed widgets were not properly applying style properties

---
## [KingdomsCrusade/kc-mod-bot](https://github.com/KingdomsCrusade/kc-mod-bot)@[c09b1d65d7...](https://github.com/KingdomsCrusade/kc-mod-bot/commit/c09b1d65d704a6d55397416fd400c7932ca38578)
#### Thursday 2021-12-30 19:34:41 by Zac

LMAO FUCK YOU SEMICOLONS

removed every single fucking semicolon HAHAHA

---
## [KingdomsCrusade/kc-mod-bot](https://github.com/KingdomsCrusade/kc-mod-bot)@[39f98aa695...](https://github.com/KingdomsCrusade/kc-mod-bot/commit/39f98aa6959a4bf1e37002bfd43a94e28f7ad166)
#### Thursday 2021-12-30 19:40:21 by Zac

Revert "LMAO FUCK YOU SEMICOLONS"

This reverts commit c09b1d65d704a6d55397416fd400c7932ca38578.

---
## [alinsavix/kaitai-wow](https://github.com/alinsavix/kaitai-wow)@[132263c036...](https://github.com/alinsavix/kaitai-wow/commit/132263c036895b0f846a6af22330f13c31f81987)
#### Thursday 2021-12-30 19:52:14 by TDV Alinsa

wowdump: implement offboard metadata & use for simplifiers

A mostly complete (if really ugly) implementation of separate
metadata that can be used for (at the moment) choosing what
simplifier is used for a data type, so that we don't have to
do a billion regex matches just to display data. Probably shaves
~15% off of dumper runtime, at least on things that have a ton
of data.

Kinda sloppy at the moment (lots of not-DRY), but seems mostly
functional and doesn't do anything *too* insane, I don't think.

---
## [rtts/fftok](https://github.com/rtts/fftok)@[adf594321d...](https://github.com/rtts/fftok/commit/adf594321df451bca59db47126933c477a7ce48d)
#### Thursday 2021-12-30 20:33:00 by Jaap Joris Vens

Seek output to same value as input

The FFmpeg wiki says:

> As of FFmpeg 2.1, combined seeking is still possible but I have yet to
> find a valid use case for it

Here is a valid use case for ya: when combining input seeking with -copyts,
the resulting output is almost unplayable with both mpv and TikTok (and
probably lots of other players, too). These players don't discard the time
between 00:00:00 and the -ss timestamp, so you have to stare at a black
screen feeling like an idiot until playback finally begins.

mpv is at least smart enough to do the initial seeking for you (TikTok
isn't) but the timeline, seek bar, track slider or whatever the damn thing
is called is still broken. Letting FFmpeg do the output seeking solves this
problem, but without ALSO specifying the input seeking the entire video will
be transcoded and discarded except for the selected cut, which is a waste of
time and resources.

So, if anyone from FFmpeg reads this, please tell me that I'm wrong or
update your Wiki. I still love you.

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[f699dac00f...](https://github.com/tdauth/wowr/commit/f699dac00f281d1358e04f1a8dd30be4394adc9b)
#### Thursday 2021-12-30 23:29:23 by barade

1.9.4

- Add and fixed caused damage in tooltip of Finger of Death.
- Reduce effect of Holy Light.
- Increase food cost of Couatl from 2 to 3.
- Remove Forgotten creeps from Paladin bosses.
- Remove 2 Paladins from boss creep group and reduce the level of two from 40 to 35.
- Reduce the level of Nether Dragon boss from 90 to 65.
- Research Evolution for Boss player as well.
- Show player name of player who caused Evolution upgrade for all creeps.
- Reduce bonuses from Evolution a bit,
- Reduce time of research Improved Mount.
- Add two Fountain of Powers to Archimonde's area.
- Move some creeps in Kalimdor away from the start base.
- Translate Storm, Earth, And Fire back into English, add the number of forms to the tooltip and mention that the number of warriors is increased.
- Fix number of workers in the stats multiboard by considering summoned workers as well.
- Simplify creep hero revival system to avoid future bugs.
- Add Wizard to Bonus Heroes.
- Add new boss Sea Turtle.
- Skull of Gul'dan does not summon Demons permanently anymore.
- Add chat command "-professionrepick".
- Reset stats of Spellbreakers back to default.
- Allow Hideouts receiving gold and lumber and Neutral Citizens collecting gold and lumber.
- Make Paladin on Theramore invulnerable.
- Fix value in tooltip of Improved Lumber Harvesting for Furbolg.
- Let all AIs except Night Elf buy 1 Shredder.
- Add Black Market, Fountain of Power, Goblin Laboratory, Mercenary Camp and trees to each Freelancer AI start island.
- Add more Doodads to Archimonde's area.
- Fix tooltips of Furbolg researches.
- Do not respawn creeps from spots next to AI buildings.
- Freelancer AI buys Shredder and hires Neutral Citizen.
- Freelancer AI collects gold and lumber.
- Support more heroes in Freelancer AI.
- Let AI use random paths and defend players.
- Add building AI laboratory to train Shredders, Sappers etc. for AI only.
- Handle player leaving while voting for the game type.
- Add game type Easy.
- Add column handicap to stats multiboard.
- Prevent starting constructing or harvesting on Freelancer AI islands for user players.
- Remove many black border areas between the east Ocean and land area.
- Change some unit soundsets of citizens fitting their models.
- Increase interval of stats multiboard updates to improve the performance.
- Update stats workers from the beginning and after AI has started.
- Do not apply Evolution to heroes which change the owner which reset some hero levels to 1.
- Make sure Illidan control release changes Illidan and not the triggering hero preventing the entering hero from becoming invulnerable.
- Only show user players in stats when you are an ally of them not when you ally them.
- Reduce summoned Nether Dragons of Nether Dragon boss.
- Replace Evasion from Nether Dragon boss with Devotion Aura.
- Do not increase the area of Earthquake with every level to avoid massive lags.
- Add basic save/load system which stores XP only and is restricted to your game settings.
- Mention in the tooltip of Demon Slayer Axe that it stacks.
- Show elapsed time in the stats multiboard title.
- Add chat command "-clear".
- Remove annoying sound from Archimonde when a hero entered his realm.
- Add number of successful save code loads as column to the stats.

---

