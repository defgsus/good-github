## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-16](docs/good-messages/2023/2023-08-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,308,148 were push events containing 3,479,194 commit messages that amount to 255,738,157 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [geeman152/Traincraft-5](https://github.com/geeman152/Traincraft-5)@[013605055d...](https://github.com/geeman152/Traincraft-5/commit/013605055d1d02e8c70c8be8483811be24f4333c)
#### Wednesday 2023-08-16 00:22:45 by broscolotos

omg he did

-Fixed dupe when breaking trains sometimes. Happened because an entity can die twice in a single tick??? dumb game
-Added page memory to the paint bucket GUI; when you open the UI it will default to the entities current skin instead of the default. Maybe add to config later
-Added "Random" button to paint bucket GUI. Will select and apply a random skin out of the available skins.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[8abddee0b0...](https://github.com/sjp38/linux/commit/8abddee0b0231406fb41edc2a1ea8ce40185ad75)
#### Wednesday 2023-08-16 01:16:45 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [CrackerCat/UACME](https://github.com/CrackerCat/UACME)@[c65f9215c1...](https://github.com/CrackerCat/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Wednesday 2023-08-16 01:55:30 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[b4642dc835...](https://github.com/cheesePizza2/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Wednesday 2023-08-16 02:20:41 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [1582130940/android_kernel_xiaomi_sdm660](https://github.com/1582130940/android_kernel_xiaomi_sdm660)@[7488db25f0...](https://github.com/1582130940/android_kernel_xiaomi_sdm660/commit/7488db25f00b0eed5be826e549eae7729f953219)
#### Wednesday 2023-08-16 02:35:44 by Angelo G. Del Regno

scripts/Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[7f1d53e719...](https://github.com/Derpguy3/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Wednesday 2023-08-16 02:55:02 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [baemyung/openpower-vpd-parser](https://github.com/baemyung/openpower-vpd-parser)@[45d54976fd...](https://github.com/baemyung/openpower-vpd-parser/commit/45d54976fdb8d27a539d78dc1cd7e2db0998b43a)
#### Wednesday 2023-08-16 02:56:42 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Change-Id: I621a7f0ba68d2c298e4fea0a9d3e21d1939cd090
Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [cashapp/AccessibilitySnapshot](https://github.com/cashapp/AccessibilitySnapshot)@[f37f7cc74d...](https://github.com/cashapp/AccessibilitySnapshot/commit/f37f7cc74d0890cea9e775ce6b378a25affc502d)
#### Wednesday 2023-08-16 03:31:10 by Nicholas Entin

Add imprecise comparison variants to iOSSnapshotTestCase extension

This adds variants of the `SnapshotVerify*(...)` methods that allow for imprecise comparisons, i.e. using the `perPixelTolerance` and `overallTolerance` parameters.

 ## Why is this necessary?

Adding tolerances has been a highly requested feature (see #63) to work around some simulator changes introduced in iOS 13. Historically the simulator has supported CPU-based rendering, giving us very stable image representations of views that we can compare pixel-by-pixel. Unfortunately, with iOS 13, Apple changed the simulator to use exclusively GPU-based rendering, which means that the resulting snapshots may differ slightly across machines (see uber/ios-snapshot-test-case#109).

The negative effects of this were mitigated in iOSSnapshotTestCase by adding two tolerances to snapshot comparisons: a **per-pixel tolerance** that controls how close in color two pixels need to be to count as unchanged and an **overall tolerance** that controls what portion of pixels between two images need to be the same (based on the per-pixel calculation) for the images to be considered unchanged. Setting these tolerances to non-zero values enables engineers to record tests on one machine and run them on another (e.g. record new reference images on their laptop and then run tests on CI) without worrying about the tests failing due to differences in GPU rendering. This is great in theory, but from our testing we've found even the lowest tolerance values to consistently handle GPU differences between machine types let through a significant number of visual regressions. In other words, there is no magic tolerance threshold that avoids false negatives based on GPU rendering and also avoids false positives based on minor visual regressions.

This is especially true for accessibility snapshots. To start, tolerances seem to be more reliable when applied to relatively small snapshot images, but accessibility snapshots tend to be fairly large since they include both the view and the legend. Additionally, the text in the legend can change meaningfully and reflect only a small number of pixel changes. For example, I ran a test of full screen snapshot on an iPhone 12 Pro with two columns of legend. Even an overall tolerance of only `0.0001` (0.01%) was enough to let through a regression where one of the elements lost its `.link` trait (represented by the text "Link." appended to the element's description in the snapshot). But this low a tolerance _wasn't_ enough to handle the GPU rendering differences between a MacBook Pro and a Mac Mini. This is a simplified example since it only uses `overallTolerance`, not `perPixelTolerance`, but we've found many similar situations arise even with the combination.

Some teams have developed infrastructure to allow snapshots to run on the same hardware consistently and have built a developer process around that infrastructure, but many others have accepted tolerances as a necessity today.

 ## Why create separate "imprecise" variants?

The simplest approach to adding tolerances would be adding the `perPixelTolerance` and `overallTolerance` parameters to the existing snapshot methods, however I feel adding separate methods with an "imprecise" prefix is better in the long run. The naming is motivated by the idea that **it needs to be very obvious when what you're doing might result in unexpected/undesirable behavior**. In other words, when using one of the core snapshot methods, you should have extremely high confidence that a test passing means there's no regressions. When you use an "imprecise" variant, it's up to you to set your confidence levels according to your chosen tolerances. This is similar to the "unsafe" terminology around memory in the Swift API. You should generally feel very confident in the memory safety of your code, but any time you see "unsafe" it's a sign to be extra careful and not gather unwarranted confidence from the compiler.

Longer term, I'm hopeful we can find alternative comparison algorithms that allow for GPU rendering differences without opening the door to regressions. We can integrate these into the core snapshot methods as long as they do not introduce opportunities for regressions, or add additional comparison variants to iterate on different approaches.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[820c22a5f5...](https://github.com/tgstation/tgstation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Wednesday 2023-08-16 04:34:47 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [Sofamakersbangalore/ReclinerRenovationinbangalore](https://github.com/Sofamakersbangalore/ReclinerRenovationinbangalore)@[c8ccb0012e...](https://github.com/Sofamakersbangalore/ReclinerRenovationinbangalore/commit/c8ccb0012ebb858ba8c79fc22f225c317d441700)
#### Wednesday 2023-08-16 05:51:05 by Sofamakersbangalore

Update README.md

In the world of furniture, recliners hold a special place for their comfort, style, and relaxation they offer. Over time, however, even the most beloved recliners can start showing signs of wear and tear. This is where the concept of recliner renovation comes into play, offering a range of benefits that can breathe new life into your favourite piece of furniture. Whether you’re in bustling Bangalore or any other location, recliner renovation can be a game-changer. In this article, we’ll delve into the numerous advantages of recliner renovation and why it’s a wise choice for those seeking to enhance both the aesthetics and functionality of their recliners.

For More Visit : https://thesofamakers.com/ 

Enhanced Comfort and Relaxation:

As recliners age, their cushioning and padding may start to deteriorate, leading to a decline in overall comfort. Recliner renovation involves replacing worn-out cushioning with high-quality materials, ensuring that you continue to enjoy the plush comfort you’ve come to love. Imagine sinking into your recliner after a long day and experiencing the same luxurious sensation as when it was brand new. Whether you’re in Marathahalli, Koramangala, JP Nagar, or any other part of Bangalore, the benefits of this enhanced comfort are universal.

Revitalized Appearance:

The visual appeal of a recliner can significantly affect the aesthetics of your living space. Through professional renovation, your recliner can be transformed from a tired-looking piece to a stunning centerpiece. From Indiranagar to HSR, and every neighborhood in Bangalore, the process involves repairing or replacing upholstery, fixing any visible damage, and restoring its original charm. If you’re someone who values a well-designed living space, recliner renovation can make your recliner blend seamlessly into your décor.

Cost-Effective Solution:

When faced with a worn-out recliner, some might consider outright replacement. However, purchasing a new recliner can be a substantial investment. Recliner renovation offers a cost-effective alternative that allows you to keep your beloved furniture while giving it a new lease on life. This is particularly beneficial for those seeking high-quality sofa recliner repair in Bangalore without breaking the bank. By choosing renovation, you contribute to sustainability by reducing waste and extending the lifespan of your furniture.

Tailored to Your Tastes:

Perhaps one of the most exciting advantages of recliner renovation is the opportunity to customize your furniture according to your preferences. If you’re in Jayanagar or anywhere else in Bangalore, finding a professional service like The Sofa Makers that specializes in custom sofa making can be a game-changer. From choosing the fabric to selecting the color scheme, you have the freedom to create a recliner that aligns perfectly with your unique style and vision.

Eco-Friendly Choice:

In a world where sustainability is becoming increasingly important, opting for recliner renovation is a responsible choice. Repairing and renovating your existing furniture reduces the demand for new materials and minimizes the environmental impact associated with manufacturing and disposing of old furniture. By extending the lifespan of your recliner, you contribute to reducing your carbon footprint. This eco-friendly approach resonates not only in Bangalore, from JP Nagar to HSR, but also worldwide.

Time-Saving Solution:

Searching for a new recliner that perfectly fits your preferences can be time-consuming. From visiting multiple stores to comparing designs and prices, it can be a lengthy process. Recliner renovation eliminates this hassle. A quick search for “sofa recliner repair near me” or “sofa recliner repair in Bangalore” can lead you to local services that specialize in giving your old recliner a fresh look and feel. This time-saving advantage is particularly valuable for those with busy schedules in areas like Koramangala or Indiranagar.

Preserving Sentimental Value:

Furniture often holds sentimental value, especially if it has been a part of your life for years. Whether it’s the recliner where you read bedtime stories to your children or the place where you unwind after a long day, there’s a connection that goes beyond aesthetics. Renovating your recliner allows you to preserve that sentimental value while ensuring that the piece remains functional and visually appealing.

In Bangalore, a city known for its innovation and dynamism, the concept of recliner renovation fits seamlessly. From Marathahalli to Jayanagar, residents have the opportunity to breathe new life into their cherished recliners. Whether you’re looking for sofa recliner repair in Bangalore or seeking custom sofa makers to create a unique piece, the benefits are undeniable. From enhanced comfort and revitalized appearance to environmental consciousness and time-saving convenience, recliner renovation offers a holistic solution that aligns with both your needs and values.

Before you consider parting ways with your favorite recliner, think about the benefits that renovation can bring. Visit The Sofa Makers to explore their expert services that cater to the diverse needs of Bangalore residents, including sofa recliner repair in Marathahalli, Koramangala, and many other neighborhoods. Embrace the possibilities of recliner renovation and experience the transformation firsthand – it’s a decision you won’t regret.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[63f7eb1a6a...](https://github.com/tgstation/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Wednesday 2023-08-16 06:51:28 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [PrettyPsychoForAWolf/sojourn-station](https://github.com/PrettyPsychoForAWolf/sojourn-station)@[1895bd5c51...](https://github.com/PrettyPsychoForAWolf/sojourn-station/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Wednesday 2023-08-16 07:05:25 by CDB

Im so sick of bugs. (#4739)

* Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

* Update psi_Larmor.dm

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[2d34c7433a...](https://github.com/FernandoJ8/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Wednesday 2023-08-16 07:24:12 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [KingOfThePing/Shiptest](https://github.com/KingOfThePing/Shiptest)@[7468161f7e...](https://github.com/KingOfThePing/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Wednesday 2023-08-16 08:05:12 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [KingOfThePing/Shiptest](https://github.com/KingOfThePing/Shiptest)@[0e6f7fa646...](https://github.com/KingOfThePing/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Wednesday 2023-08-16 08:05:12 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
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
## [BreathLGD/android_kernel_xiaomi_sm7325](https://github.com/BreathLGD/android_kernel_xiaomi_sm7325)@[870e7d7108...](https://github.com/BreathLGD/android_kernel_xiaomi_sm7325/commit/870e7d7108432f0c6fad2dec6ef6060d4ee49169)
#### Wednesday 2023-08-16 08:40:45 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

commit 27dada070d59c28a441f1907d2cec891b17dcb26 upstream.

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>
Acked-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [sec-js/koreader](https://github.com/sec-js/koreader)@[4acf131071...](https://github.com/sec-js/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Wednesday 2023-08-16 09:13:57 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [jalenng/Draw](https://github.com/jalenng/Draw)@[f286df5ff3...](https://github.com/jalenng/Draw/commit/f286df5ff3f2ffd3501f5e716df7acf7c0de8665)
#### Wednesday 2023-08-16 09:19:16 by spicywheatbread

Add files for SFX (#39)

* Basic SFX Added

Added placeholder sound effects to things like jumping and dying.

(cherry picked from commit e721f5ff4a91ac3e89c323e4e900a352f9b02ebf)

* More SFX

Added new page flip sound, added sounds to return buttons in menus, more work to be done on this but just uploading so I can work on this from my laptop at school

(cherry picked from commit 17ef3bacf1a95b3778570ce80ec9582177c4649c)

* SFX files and settings menu

Added some sound files for sfx and light changes for the settings menu to continue to work on later.

(cherry picked from commit 571e9bcd4503ab057ca9b09099a4f41f4f9d562f)

* Sorry this is a bunch of random changes lmao. Added ambiences to NathanP2, the Prefab to play Ambience. Also, added new respawnManager to respawn necesasry objects like OrangeObjects and ScribbleWall. Moved some scripts into folders. Random level fixes for Mike, Claire, etc from playtesting.

(cherry picked from commit b1b9afbf29567d345e08e4a96ca4f4da3b63e885)

* sfx added + slider func

Added some more sound effects, sliders in settings menu now play a sound to reflect their real volumes, added looping sound to drawing canvases.

(cherry picked from commit 8007a22b04b5dde97c5cbfba0ebc9ccc8ab904c2)

* I'm not gonna lie. I don't remember what I changed
about the levels, but I'm PRETTY sure it's something.
Mostly, Stickman now stops walking animation when walking into a wall
and stops playing footstepSFX as well. PageflipSFX when finishing level.
Quick logic fix for levelendtrigger b/c it would call loadnextscene
multiple times. Made audiosystem global so it's easier to code.

(cherry picked from commit 65a49121750f5d3fb48a452b08b4d0063a770bdd)

* Forgot to commit the change for the animation
controller update.

(cherry picked from commit b6cd4de1442639ee872adb574f27acf95450c4dd)

* Delete it.

I hate it. new page flip wav meta

---
## [anoma/namada-testnets](https://github.com/anoma/namada-testnets)@[b4c14e6c11...](https://github.com/anoma/namada-testnets/commit/b4c14e6c11dab3a6e5025bb3325b8f646cf1868d)
#### Wednesday 2023-08-16 09:43:15 by popek1990.eth

Add a popek1990.toml

Hello, 

I'm popek1990.eth. 

I've been working in the web2 & web3 industry for over half of my life. My beginnings involve creating web2 websites and php forums using html/css/php. Later on, I delved into SEO & marketing. Throughout my life, I've been in love with Linux, especially the Debian distribution which I still use to this day. For the past 4 years, I've been developing my skills in the areas of blockchain and smart contracts. I'm deeply interested in privacy, which led me to discover NAMADA. Previously, I ran my own node in Monero & [Railgun](https://railgun.org/).

 I want to be an active member of the community. I'm also an influencer in the Polish crypto market, and my goal is to spread the good word about crypto technology through articles on my [mirror.xyz](https://mirror.xyz/popek1990.eth) . I would be very pleased if I could join as a genesis validator. I'm aware that I'm joining late, but I've been systematically observing the NOMADA project for many months. I've read the entire whitepaper and .docs, and I'm very impressed with your vision. 

Here are my links: https://linktr.ee/popek1990

Of course, NOMADA and all repositories installed on a strong server and ready to go. I'd like join to testnet 12 ale pre-gnosis validator.

---
## [Digitekomya/Ventes](https://github.com/Digitekomya/Ventes)@[2238b9dc2a...](https://github.com/Digitekomya/Ventes/commit/2238b9dc2a66e6ac7012788aa56525a9f160d2b7)
#### Wednesday 2023-08-16 09:48:44 by Digitekomya

Update README.md

In the world of B2B (business-to-business) marketing, generating high-quality leads is the lifeblood of success. A robust lead generation strategy is essential for driving growth, expanding the customer base, and ultimately boosting revenue. This comprehensive guide dives into the top B2B lead generation strategies that can help your business thrive in today's competitive landscape.

Content Marketing: Producing relevant and valuable content positions your brand as an industry authority. Consistently publishing blog posts, whitepapers, ebooks, and webinars that address your target audience's pain points can attract prospects and establish trust.
Email Marketing: An effective email marketing campaign can nurture leads and guide them through the sales funnel. Personalize your messages, segment your email list, and provide valuable content to keep your leads engaged.
Webinars and Events: Hosting webinars, workshops, and attending industry events can connect you with potential leads directly. These platforms provide opportunities to showcase your expertise and establish meaningful connections.
Content Upgrades and Lead Magnets: Offer valuable resources such as ebooks, templates, or toolkits in exchange for contact information. This strategy not only provides leads with immediate value but also nurtures them for future engagement.
Landing Pages and Forms: Design dedicated landing pages that focus on a single offer, increasing conversions. Implement forms strategically to collect necessary lead information without overwhelming prospects.
Account-Based Marketing (ABM): Tailor your marketing efforts to specific high-value accounts. ABM focuses on creating personalized experiences for each target account, increasing the chances of successful lead conversion.
Chatbots and AI: Incorporate AI-driven chatbots on your website to engage with visitors in real-time. Chatbots can qualify leads, answer basic questions, and provide a seamless experience even outside of business hours.
Referral Programs: Encourage satisfied customers to refer potential leads to your business. Reward referrals with incentives like discounts, exclusive content, or access to premium features.
Search Engine Optimization (SEO): Optimizing your website for search engines increases its visibility to potential leads. Focus on keywords relevant to your industry, create high-quality backlinks, and ensure your website is mobile-responsive for better search rankings.
Influencer Partnerships: Collaborating with industry influencers can expand your reach and credibility. Influencers can help promote your brand and introduce it to their followers, boosting your lead generation efforts.

Social Media Marketing: Utilize platforms like LinkedIn, Twitter, and Facebook to engage with your target audience. Share insightful content, participate in discussions, and use targeted advertising to reach decision-makers in your industry.

Data Analysis and Optimization: Regularly analyze your lead generation efforts to identify what's working and what needs improvement. Use analytics to fine-tune your strategies for better results.

For More Details : https://ventesb2b.com/ 

Conclusion
Successful B2B lead generation requires a strategic approach that encompasses various tactics tailored to your target audience and industry. By combining content marketing, SEO, social media engagement, email outreach, and more, you can create a well-rounded lead generation strategy that drives consistent growth for your business. Keep in mind that no single strategy fits all; experimentation, continuous learning, and adaptation are crucial to staying ahead in the ever-evolving B2B landscape.

Regards,
Digitek Omya
https://ventesb2b.com/
New York, US

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[ebbc45b161...](https://github.com/Thunder12345/tgstation/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Wednesday 2023-08-16 10:51:59 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[27d46f1717...](https://github.com/Thunder12345/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Wednesday 2023-08-16 10:51:59 by OrionTheFox

Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)


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
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[a288abcaf2...](https://github.com/Thunder12345/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Wednesday 2023-08-16 10:51:59 by san7890

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

---
## [imrehg/langchain](https://github.com/imrehg/langchain)@[16af5f8690...](https://github.com/imrehg/langchain/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Wednesday 2023-08-16 10:55:41 by niklub

Add LabelStudio integration (#8880)

This PR introduces [Label Studio](https://labelstud.io/) integration
with LangChain via `LabelStudioCallbackHandler`:

- sending data to the Label Studio instance
- labeling dataset for supervised LLM finetuning
- rating model responses
- tracking and displaying chat history
- support for custom data labeling workflow

### Example

```
chat_llm = ChatOpenAI(callbacks=[LabelStudioCallbackHandler(mode="chat")])
chat_llm([
    SystemMessage(content="Always use emojis in your responses."),
        HumanMessage(content="Hey AI, how's your day going?"),
    AIMessage(content="🤖 I don't have feelings, but I'm running smoothly! How can I help you today?"),
        HumanMessage(content="I'm feeling a bit down. Any advice?"),
    AIMessage(content="🤗 I'm sorry to hear that. Remember, it's okay to seek help or talk to someone if you need to. 💬"),
        HumanMessage(content="Can you tell me a joke to lighten the mood?"),
    AIMessage(content="Of course! 🎭 Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"),
        HumanMessage(content="Haha, that was a good one! Thanks for cheering me up."),
    AIMessage(content="Always here to help! 😊 If you need anything else, just let me know."),
        HumanMessage(content="Will do! By the way, can you recommend a good movie?"),
])
```

<img width="906" alt="image"
src="https://github.com/langchain-ai/langchain/assets/6087484/0a1cf559-0bd3-4250-ad96-6e71dbb1d2f3">


### Dependencies
- [label-studio](https://pypi.org/project/label-studio/)
- [label-studio-sdk](https://pypi.org/project/label-studio-sdk/)

https://twitter.com/labelstudiohq

---------

Co-authored-by: nik <nik@heartex.net>

---
## [archy-bold/not-enough-musk-spambot](https://github.com/archy-bold/not-enough-musk-spambot)@[66162009c3...](https://github.com/archy-bold/not-enough-musk-spambot/commit/66162009c3d389c53a16226680554be4d6d04f3e)
#### Wednesday 2023-08-16 11:41:49 by Simon Archer

Wow
Unless there are a few issues where you at least slightly disagree with your political party, then you are not in a political party, you are in a cult
A few times a year, I take Sunday afternoons off
We are hell bent on making this platform the best place on Earth for great content creators!
Am lifting weights throughout the day, preparing for the fight. Don’t have time to work out, so I just bring them to work.
Product testing & working out kills two birds with one stone!
I build muscle fast. Physical endurance is my weak spot, so I’m aiming to make this quick.
Obviously
CEO is fake title
Exact date is still in flux. I’m getting an MRI of my neck & upper back tomorrow. May require surgery before the fight can happen. Will know this week.
Maximizing unregretted user-seconds
Our user-seconds have reached all time highs in recent months, so something is wrong. Will investigate.
Testosterone rocks, ngl.
If Zuck my 👅 really wants a lesson in why there are weight categories in fighting so badly, I could just head over to his house next week and teach him a lesson he won’t soon forget
👅😂
Honey is neither animal, plant or fungus *nor
I’m gonna bang on his door tomorrow and demand to fight
Zuck is a chicken
He can’t eat at chic fil a because that would be cannibalism
Knock knock, Who’s there?, Knutsēk, Nutsack who?, Knutsēk Tæbag
I’m not cis, you are

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Wednesday 2023-08-16 12:43:51 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [dayomoro/Omega_loan_prediction_app](https://github.com/dayomoro/Omega_loan_prediction_app)@[5b636d79fc...](https://github.com/dayomoro/Omega_loan_prediction_app/commit/5b636d79fcb801de3bf176f80022160d27c9eea4)
#### Wednesday 2023-08-16 12:53:24 by EHINMORO DAYO

Update README.md

#Project Overview: Loan Default Prediction System#
The Loan Default Prediction System merges data science and user experience to revolutionize lending. Using predictive analytics, it accurately forecasts loan default probabilities, enhancing profitability and decision-making. Data Scientists craft transparent models from historical data, empowering informed lending choices. A user-friendly interface streamlines operations for loan officers, while transparency ensures confident risk assessment. This innovative system redefines risk mitigation, making lending both prudent and efficient.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[837d09bddb...](https://github.com/TaleStation/TaleStation/commit/837d09bddb73c051ecb7705b3a1e6f55569ef457)
#### Wednesday 2023-08-16 13:22:36 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a unique medibot to the Syndicate Infiltrator (#7326)

Original PR: https://github.com/tgstation/tgstation/pull/77582
-----

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[05e1cac249...](https://github.com/ahjragaas/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Wednesday 2023-08-16 14:10:08 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [t0nysama/tonystation](https://github.com/t0nysama/tonystation)@[31f1924324...](https://github.com/t0nysama/tonystation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Wednesday 2023-08-16 14:43:40 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[028416a56e...](https://github.com/argilla-io/argilla/commit/028416a56e1eb05defe9dffcd03de5d1744bdcf2)
#### Wednesday 2023-08-16 15:31:05 by Natalia Elvira

Docs/feedback setfit tutorial (#3530)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

Adds a new tutorial on how to use SetFit to get zero-shot suggestions
for `Label` and `MultiLabel` questions in Feedback datasets.

Closes #3528 

**Type of change**

(Remember to title the PR according to the type of change)

- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [x] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [ ] I added relevant documentation
- [x] I followed the style guidelines of this project
- [x] I did a self-review of my code
- [x] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [naim/naim.github.io](https://github.com/naim/naim.github.io)@[97408ab0e0...](https://github.com/naim/naim.github.io/commit/97408ab0e0fc12cb46aacef1aed81915064985a4)
#### Wednesday 2023-08-16 15:38:43 by Naim Falandino

Update index.html

Remove Twitter widget (fuck you, Elon); update links

---
## [iangrunert/hubris](https://github.com/iangrunert/hubris)@[8e0b13b865...](https://github.com/iangrunert/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Wednesday 2023-08-16 16:23:28 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [meedan/check-api](https://github.com/meedan/check-api)@[dc890de6e2...](https://github.com/meedan/check-api/commit/dc890de6e23208a4db9e99f8e28e665b8ffc8a7e)
#### Wednesday 2023-08-16 16:44:13 by Christa Hartsock

Update GraphQL to use class-based SDK 🫠

This commit upgrades us to GraphQL 1.11.10, from 1.9.21, and begins using the new class-based SDK from the previous .define syntax.Though this change isn't supposed to be required until GraphQL 2.0, I found in practice that we couldn't upgrade to the minimum version needed for Ruby 3.0 (1.11.7) without doing it. 

**What I did**

With the new GraphQL DSL, we are able to use Ruby class composition, which includes inheritance from base classes and including modules to get specific functionality.

I tried to create some useful abstract base classes that borrowed heavily from our previous GraphQL CRUD generator. We had a lot of carveouts in the generator for specific classes (specifically in .define_parent_returns or the generator functions for what wanted to be classes), and I tried to eliminate these and move them to explicit declarations in classes now that we have the ability to do that (yay library enabling composition!)

As much as possible, I tried to move us toward declaring things explicitly to reduce my and hopefully future us's confusion rather than using metaprogramming or extracting abstract functions. Going forward, I think we should only extract methods or classes where there is shared functionality for a type or mutation, and rely on explicit declaration or modules for attributes that differ based on the underlying class we're modifying.

There is some kind of tricky metaprogramming and code in the mutation base classes, because of problems I ran into with inheritance and other things. I also hope that now that the pattern is set up we won't have to touch them too much, and can instead rely on configuring their child classes.

**Some gotchas I ran into / things of note**

Our API uses a mix of camel-case and snake-case. The new GraphQL library wants to convert everything to camelcase, which will break our API. I've tried where possible to default attributes to snakecase (changing this in the base Type), but it's not possible for everything - specifically when we set fields and arguments on mutation classes. To override the default behavior of camelcaseing, we have to manually set camelize: false on any field or argument that has an underscore in mutation classes.

* GraphQL Ruby now has a new base mutation class that we could opt into if we want, but it changes the way the API would look - of note is removing the input: key from request bodies, not allowing direct setting of inputs and fields on the input type in the mutation class (I think), and not automatically injecting the global ID in the response. To maintain our old behavior, we have to descend from GraphQL::Schema::RelayClassicMutation rather than GraphQL::Schema::Mutation, which I've done in Mutations::BaseMutation (and all descendent classes we expect to use for our mutations: Mutations::CreateMutation, Mutations::UpdateMutation, Mutations::DestroyMutation, Mutations::BulkUpdateMutation, Mutations::BulkDestroyMutation)
* GraphQL schema now gets generated at runtime. When our tests run they only start the application a maximum of once per file. This means that the previous approach we used to create and delete annotation types, which the GraphQL schema relies on to be generated correctly, and reloading the schema as necessary does not work - as a result we're now calling  TestDynamicAnnotationTables.load! before GraphQL controller tests, which loads the existing annotation tables generated in development into test fresh each time.
* Our QueryType returns an always null ID field. This is because the frontend was requesting it even though we don't use it. I don't know why, but this fixed it. So, I added it and moved on.

Resources:

Here's the migration guide I leaned on heavily: https://imaharu.github.io/graphql-ruby-doc-ja/schema/class_based_api.html#compatibility--migration-overview. It's still missing a lot, but may help if you want to understand changes in the API.

Also, the new API is described in the GraphQL ruby docs: https://graphql-ruby.org/guides

**Some additional things that appear in this commit, that may be of note in future**

* Manually specify resolve functions for missing methods

We sometimes automatically generate getters for attributes stored
as a hash (eg get_slack_webhook, get_languages) but since we rely
on method_missing to do so, GraphQL doesn't detect those methods as
being valid because it checks for their validity using
Model.respond_to(:method_name), which returns false even though
Model.method_name returns a legitimate value. To get around this,
we can manually create resolve methods with the attribute name
that just call into the model.

* Allow batch nesting

This is now allowed in GraphQL batch, and the error we were previously
catching no longer exists.

https://github.com/Shopify/graphql-batch/issues/70

* Properly implement nodes and interfaces, and support OpenStructs

OpenStructs break the class hierarchy, so we need more explicit
handling to support our current use case. Our id_from_object now
calls down into the OpenStruct :type method, like we were doing before

* Fix edge setting in most mutation classes

I think there was a naming conflict (name -> obj_name) causing things
to go totally wonky.

* Fix tests that depend on a specific schema

Certain tests require annotation types to be in the database before loading
the schema. We can't reload the schema easily in test environment. Given that this
data is actually static in practice (and hardcoded into the GraphQL schema we
generate), we might want to consider preloading it into the database rather than
creating it in individual tests. For now, we just create the dynamic annotations in
the test setup for the controller test file the test is run within.

Try to avoid altering the other tests for now, even though we'll need
to eventually. Begins loading in DynamicAnnotation stuff from a dump
of our local (and QA) database after a fresh build so that we can have
a consistent GraphQL schema. The new GraphQL interpreter only creates the
schema at runtime, which means we build it once per test run. As a result,
we need to have all of our DynamicAnnotation annotation types and fields
in place before we start the app to run tests.

This sidesteps fixing the dynamic annotation stuff for the rest of the
app, since that's a big one.

* Change flaking tests to use createDynamic instead of db-gen mutation

Also adds :action to Dynamic mutations to support using createDynamic
for createDynamicReportDesign, which requires the action attribute
in certain circumstances. Kind of a hack for tests to pass, since we're
having problems loading the schema from database consistently

CV2-3094

---
## [trflynn89/ladybird-appkit](https://github.com/trflynn89/ladybird-appkit)@[f54887629d...](https://github.com/trflynn89/ladybird-appkit/commit/f54887629d7f08f0491b639ffb5771d03a32ff4d)
#### Wednesday 2023-08-16 16:44:16 by Timothy Flynn

Place the web view inside a scrolling container

The NSScrollView has two components, a document view and a content view.
The document view is effectively the "real" view, which applications are
meant to paint / add subviews into. The content view is the cropped view
of the document view that is actually visible.

So normally, we'd paint the entire web page onto the document view, and
the content view would scroll around that view. However, we don't paint
the entire web page - we specifically only paint the visible portion.

To accommodate this, we trick the NSScrollView by creating an entirely
empty document view, sized to the layout size provided to us by LibWeb.
This allows the scroll bars to appear with an appropriate size. We then
make the web view the content view, and paint the portion of the web
page that we have accordingly.

FIXME: Scrolling speed is pretty bad. The larger the scroll area, the
slower we scroll. If the scroll area is very small, we scroll incredibly
fast. Not a very good experience, so we should improve on this.

---
## [ormenachem/metroidjam2023](https://github.com/ormenachem/metroidjam2023)@[b3125b1511...](https://github.com/ormenachem/metroidjam2023/commit/b3125b1511bac58bf11764c746cba6c605f4ae6d)
#### Wednesday 2023-08-16 17:06:22 by NimiHiLol

I smoothed out the acceleration and made it so you won't glide on the ground when landing on the ground

fuck you

---
## [hickford/oauth2](https://github.com/hickford/oauth2)@[a835fc4358...](https://github.com/hickford/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Wednesday 2023-08-16 18:58:45 by Brad Fitzpatrick

oauth2: move global auth style cache to be per-Config

In 80673b4a4 (https://go.dev/cl/157820) I added a never-shrinking
package-global cache to remember which auto-detected auth style (HTTP
headers vs POST) was supported by a certain OAuth2 server, keyed by
its URL.

Unfortunately, some multi-tenant SaaS OIDC servers behave poorly and
have one global OpenID configuration document for all of their
customers which says ("we support all auth styles! you pick!") but
then give each customer control of which style they specifically
accept. This is bogus behavior on their part, but the oauth2 package's
global caching per URL isn't helping. (It's also bad to have a
package-global cache that can never be GC'ed)

So, this change moves the cache to hang off the oauth *Configs
instead. Unfortunately, it does so with some backwards compatiblity
compromises (an atomic.Value hack), lest people are using old versions
of Go still or copying a Config by value, both of which this package
previously accidentally supported, even though they weren't tested.

This change also means that anybody that's repeatedly making ephemeral
oauth.Configs without an explicit auth style will be losing &
reinitializing their cache on any auth style failures + fallbacks to
the other style. I think that should be pretty rare. People seem to
make an oauth2.Config once earlier and stash it away somewhere (often
deep in a token fetcher or HTTP client/transport).

Change-Id: I91f107368ab3c3d77bc425eeef65372a589feb7b
Signed-off-by: Brad Fitzpatrick <bradfitz@golang.org>
Reviewed-on: https://go-review.googlesource.com/c/oauth2/+/515675
TryBot-Result: Gopher Robot <gobot@golang.org>
Reviewed-by: Roland Shoemaker <roland@golang.org>
Reviewed-by: Adrian Dewhurst <adrian@tailscale.com>
Reviewed-by: Michael Knyszek <mknyszek@google.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[72174845f5...](https://github.com/tgstation/tgstation/commit/72174845f5b417bf0cbd3f4a8fc66835b052acf8)
#### Wednesday 2023-08-16 19:04:43 by Jacquerel

Basic Watchers & Basilisks (#77630)

## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [budmaster13/Nanna.github.io](https://github.com/budmaster13/Nanna.github.io)@[d6d9b0df92...](https://github.com/budmaster13/Nanna.github.io/commit/d6d9b0df92490f05622352aa8dbaf5248da3f493)
#### Wednesday 2023-08-16 19:19:33 by budmaster13

Update README.md

This project is a tribute and memorial website dedicated to the loving memory of my dear mother, [Mother's Name]. Through this website, I wanted to honor her life, share her story, and create a digital space where friends and family could gather to remember her.
Technology and Journey

When I embarked on this project, I had little to no coding experience. I built this memorial website entirely in HTML, using the limited knowledge I had at the time. I didn't know about platforms like WordPress, so I learned the basics of HTML step by step.

I pieced together each section of the website, from the main page that tells her story to the photo gallery that captures beautiful moments. The process was a learning journey for me, as I gradually discovered how to structure a webpage, add images, and even include simple styling using CSS.
A Labor of Love

Creating this website was a deeply personal experience. It allowed me to express my love and gratitude for my mother while learning valuable skills along the way. Each line of code represents not only my dedication to the project but also my enduring love for her.
How to Contribute

This project is a tribute from the heart, and its purpose is to celebrate my mother's life. While I don't anticipate many contributions, if you have any ideas or suggestions to improve the website, please feel free to reach out.
Contact Information

If you'd like to connect or share your memories, you can reach me at budmaster13@protonmail.com

Feel free to personalize and expand upon this example to share your journey and the significance of your memorial website. It's a wonderful way to convey your emotions and the effort you've put into creating this heartfelt tribute.

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[16cecf864d...](https://github.com/RigglePrime/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Wednesday 2023-08-16 19:27:33 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[d12cab7a49...](https://github.com/RigglePrime/tgstation/commit/d12cab7a498f64df366eba748175405f8fd0ffef)
#### Wednesday 2023-08-16 19:27:33 by Sealed101

Collapsible lobby buttons (#76443)

## About The Pull Request
Adds a button to the new player HUD that allows collapsing and expanding
the menu buttons.
Also gives the buttons names so they can show up in the BYOND's prompt
on the bottom left.
Readiness is now also displayed in the status tab.
The menu HUD can be reset with a verb Reset Lobby Menu HUD in the OOC
tab.

### I SAW FOOTAGE


https://github.com/tgstation/tgstation/assets/75863639/2054c09d-48d7-4736-b862-4406667dde67

#### Here be dragons (dev progress footage)

#### GACHI BGM WARNING
<details><summary>Mk. I </summary>


https://github.com/tgstation/tgstation/assets/75863639/3e886254-bebd-4aa3-b7f7-5fdd8b7c9040

</details> 

___

<details><summary>Mk. II</summary>


https://github.com/tgstation/tgstation/assets/75863639/14d84a2d-1732-4700-aad0-df85c9befa86

</details> 

___

<details><summary>Mk. III (featuring: the shutter!) ((NOT featuring:
gachi BGM))</summary>


https://github.com/tgstation/tgstation/assets/75863639/98576c1f-6877-41b9-bec6-e11207501965


</details> 

___

<details><summary>Mk. IV (new collapse button sprite )</summary>

~~& shutter graffiti~~ (in a followup PR)

this video has a bug with the poll button lighting up without an active
poll, this was fixed before it was pushed


https://github.com/tgstation/tgstation/assets/75863639/6c0489e2-c80a-4682-b543-5d7c74071a39

</details> 

___

<details><summary>Mk. IV with updated shutter sprite and animation
speed</summary>

<sub>TIL github sanitizes ♂ and probably other ascii from file
names</sub>


https://github.com/tgstation/tgstation/assets/75863639/61ed85fe-8df6-4f38-91aa-1f70258289e7

</details> 

## TO-DO
- [x] A shutter that comes down and hides the buttons away. 
  - [ ] The shutter will have a chance to have silly graffiti on it.
- [x] Redesign and move the collapse/expand button to be a part of the
menu.

## Why It's Good For The Game
Banishes the curse cast upon lobby art. Ties in with the on-going lobby
art contest.


## Changelog
:cl:
qol: Lobby Menu buttons can now be collapsed. Rejoice!
qol: Lobby Menu buttons have names, which can be seen in the prompt on
the bottom left of the viewport.
qol: you may see your readiness status during pre-game in the Status
Bar.
qol: Reset Lobby Menu HUD verb added in case you manage to break the
damn thing.
/:cl:

---
## [chapmanjacobd/journal](https://github.com/chapmanjacobd/journal)@[db93f1d607...](https://github.com/chapmanjacobd/journal/commit/db93f1d60753d5af92abf7a216f1c55116e06ec0)
#### Wednesday 2023-08-16 20:00:50 by Jacob Chapman

gitignore beliefs memories advice robot-apple-n-banana annoying art as collected comm computer concepts contemporary_intangible_cultural_property curating death drinks_to_try edu effects evil favorite food funeral games goals hello howto ideas interests learn list misc music patterns people places playlist Classical20Music program programming software survival teach thoughts todo_tools tools unsolicited video videos weird wh writing writingtheory wt

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[34940906e0...](https://github.com/git-for-windows/git/commit/34940906e0b662d07ade74a631445df3f6694aa0)
#### Wednesday 2023-08-16 20:13:03 by Johannes Schindelin

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
## [ValidebagMUN/ValidebagMUN-Site](https://github.com/ValidebagMUN/ValidebagMUN-Site)@[c80535aeeb...](https://github.com/ValidebagMUN/ValidebagMUN-Site/commit/c80535aeeb977228250c79f420be08bd10925afa)
#### Wednesday 2023-08-16 20:45:40 by Ege Ender Anaklı

Merge pull request #15 from ValidebagMUN/develop

FOR THE LOVE OF GOD JESUS AND THE HOLY SPIRIT ALLAAAAH

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[dc6ddd821b...](https://github.com/lessthnthree/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Wednesday 2023-08-16 20:52:04 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [gr33nb3rry/MovieMatch](https://github.com/gr33nb3rry/MovieMatch)@[cf6277ec95...](https://github.com/gr33nb3rry/MovieMatch/commit/cf6277ec95fe9a061abcc0f2fa6f24693ebe1442)
#### Wednesday 2023-08-16 21:00:45 by Ruslan Bulak

OMG It was so painful!! I was suffering for 3 hours just because of wrong line, but now it works

I implemented adding new collection that is related to match_movie_user.user_id and simple GetMapping of all collections

---
## [dabhunt/GenesisZero](https://github.com/dabhunt/GenesisZero)@[6323738d8d...](https://github.com/dabhunt/GenesisZero/commit/6323738d8d9f3c83809f7b6ed07e7ba95b81131b)
#### Wednesday 2023-08-16 21:05:49 by dabhunt

AP balancing for endless mode

After watching a friend play endless mode and attempt Ability power builds with little success, I have decided after 3 years GZ is due for an update to make AP builds scale better.
- Introduce a legendary modifier that gains +10 AP per kill stacking infinitely
- Culling blast can go through shield Boyz shield. (This ability was previously pretty much useless due to shields)
- shield Boyz shield's are now disabled while stunned
- legendary modifier added: Supercharger: After killing an enemy, your next bullet deals 100% of your AP as bonus damage.

---
## [gcoleman19/undevelopers](https://github.com/gcoleman19/undevelopers)@[884410a94c...](https://github.com/gcoleman19/undevelopers/commit/884410a94c251604c91fa1e209663b921bae2557)
#### Wednesday 2023-08-16 21:07:56 by Vivvns

Added 04-citations.rmd for Case Studies

RMD text below:

#**Case Studies

In our modern world where artificial intelligence (AI) is entwined with daily life, the discovery of biases within algorithms has unveiled a troubling reflection of societal prejudices. These biases, both unintentional and intentional, reverberate through sectors like hiring, lending, and criminal justice, influencing lives in profound ways. However, alongside these unintentional biases, there exists a complex landscape of intentional biases applied with the goal of promoting fairness, addressing historical injustices, or achieving specific societal objectives.

Two groundbreaking studies cast a humanizing light on this technological dilemma. [Gender Shades by Joy Buolamwini and Timnit Gebru](https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) explored the troubling racial and gender disparities in facial recognition, revealing how these technologies can unintentionally mirror and magnify existing inequalities. Meanwhile, [Man is to Computer Programmer as Woman is to Homemaker?](https://proceedings.neurips.cc/paper_files/paper/2016/file/a486cd07e4ac3d270571622f4f316ec5-Paper.pdf) Debiasing Word Embeddings by Bolukbasi et al. delved into gender biases within language algorithms, unearthing the subtle ways in which technology can perpetuate stereotypes. Both studies serve as poignant reminders that behind every algorithm, there are human lives and societal norms that deserve careful consideration and compassion.

## **Biases in hiring, lending, criminal justice:**


**[Gender Shades" by Joy Buolamwini and Timnit Gebru:](https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) **

Buolamwini and Gebru evaluated commercial facial recognition systems by testing them on a more diverse dataset that included a wider representation of gender, skin color, and ethnic backgrounds. They discovered significant disparities in accuracy across different demographic groups, with the algorithms performing poorly on darker-skinned and female faces.

![](https://ars.electronica.art/outofthebox/files/2019/08/GenderShades_gs04.jpg)

***Key Takeaway:***

**Exposing Disparities:** Their method has shed light on real-world implications of bias within facial recognition technologies, bringing attention to an issue that has substantial societal impact.

**Discrimination:** These biases can lead to systematic discrimination, where certain groups may be unfairly targeted or misclassified by automated systems used in law enforcement, hiring, or other critical domains.

**Loss of Trust:** Awareness of these biases can erode trust in AI systems and technology more broadly, especially among those most affected by the inaccuracies.

![](https://globalnews.ca/wp-content/uploads/2018/02/gs03.png)
The work by Buolamwini and Gebru is pioneering and has had a profound impact on how the industry approaches bias in AI. Their methods are robust and have led to broader conversations about ethical AI. While technological solutions are necessary, a systemic approach involving diverse stakeholders is essential to truly eliminate biases.

**[Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings" by Bolukbasi et al.:](https://proceedings.neurips.cc/paper_files/paper/2016/file/a486cd07e4ac3d270571622f4f316ec5-Paper.pdf)**

![](https://2.bp.blogspot.com/-RUpKuflR6qQ/XLwEXB16ozI/AAAAAAAAr4Q/Jo3_0oqOZfYE6rygFvl8CA0MOo5lkS43QCLcBGAs/s1600/Debias1.png)

The article by Tolga Bolukbasi and others describes a process to reduce gender bias by identifying and modifying the geometric relationships within word embeddings. The authors first identify a gender subspace by looking at pairs of words that reflect gender, such as ("he", "she"), ("man", "woman"), etc. They then project word vectors onto this subspace to measure their gender bias and adjust them to reduce this bias, while preserving other semantic relationships.

***Key Takeaway:***

**Effectiveness:** The methods present a clever way to reduce gender bias in word embeddings, and they have been influential in guiding further research in the field.

**Limitations:** While the method addresses gender bias for certain word pairs, it may not completely remove all forms of gender bias, especially more subtle or complex biases.

**Ethical Considerations:**Deciding what constitutes a bias and how to address it can be controversial. This method mainly addresses one specific type of bias, and the decision-making process might need to involve broader social input.

The methodology in this paper is an essential step in addressing biases in AI, but it also highlights the complexity of the problem. A multidisciplinary approach, involving technological innovation, human expertise, and societal input, might be the best path forward to build AI systems that are both powerful and aligned with human values.

## **Inherent Biases - the complex trade-offs in designing fair machine learning models.**


*Intentional biases in machine learning models are indeed sometimes applied with the goal of promoting fairness, addressing historical biases, or achieving specific societal objectives. This is often referred to as "fairness through awareness" or "algorithmic affirmative action." Below are some examples of intentional biases and related case studies:*


**Equalized Odds in Hiring Practices:** Some hiring algorithms might intentionally favor candidates from underrepresented groups to ensure that the selection process provides equal opportunity to all applicants [(Fazelpour & Lipton, 2020)](https://www.researchgate.net/publication/339105052_Algorithmic_Fairness_from_a_Non -ideal_Perspective).


**Bias Correction in Credit Scoring:**  Intentional adjustment in removing sensitive attributes, such as gender identifiers may aim to provide fair access to credit opportunities by counterbalancing biases against specific demographic groups [(Liang et al., 2023)](https://www.frontiersin.org/articles/10.3389/fdata.2022.1049565/full)

![](https://www.frontiersin.org/files/MyHome%20Article%20Library/1049565/1049565_Thumb_400.jpg)


**Intentional Gender Bias in Gender Classification Models:** Many researchers make intentional effort to compile a dataset of facial images representing different genders, ethnicities, and other demographic factors, ensuring a diverse sample that includes non-binary and transgender individuals. Thus, they further encourage the industry to evolve in a direction that recognizes the complexity and diversity of human gender identity [(Scheuerman et al., 2019)](https://doi.org/10.1145/3359246)


![](https://media.cnn.com/api/v1/images/stellar/prod/191118130655-ai-gender-identification-morgan.jpg?q=w_3000,h_1688,x_0,y_0,c_fill)

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[ee4021c507...](https://github.com/TypeVar/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Wednesday 2023-08-16 21:09:38 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [warriorstar-orion/Paradise](https://github.com/warriorstar-orion/Paradise)@[a3dc32cf34...](https://github.com/warriorstar-orion/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Wednesday 2023-08-16 22:12:14 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[817d59923d...](https://github.com/treckstar/yolo-octo-hipster/commit/817d59923d44b748d651d88be798d60ee43610d0)
#### Wednesday 2023-08-16 22:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [SingingSpock/tgstation](https://github.com/SingingSpock/tgstation)@[cfd40aeef5...](https://github.com/SingingSpock/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Wednesday 2023-08-16 22:41:35 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [DevinLeamy/bevy](https://github.com/DevinLeamy/bevy)@[fb4c21e3e6...](https://github.com/DevinLeamy/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Wednesday 2023-08-16 22:46:34 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[092d0db574...](https://github.com/vampirebat74/lobotomy-corp13/commit/092d0db57485cf85d88536cd25e3701845bd61b6)
#### Wednesday 2023-08-16 23:10:32 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

---

