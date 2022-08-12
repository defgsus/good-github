## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-11](docs/good-messages/2022/2022-08-11.md)


2,042,389 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,042,389 were push events containing 3,138,473 commit messages that amount to 226,836,759 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [TorannD/RWoM](https://github.com/TorannD/RWoM)@[bc6c0ffd17...](https://github.com/TorannD/RWoM/commit/bc6c0ffd17f558adff1415ef80408b309c434157)
#### Thursday 2022-08-11 00:16:00 by TorannD

v2.5.8.0 update

New:
 o Advanced Classes
  - Unique type of custom class that can be added (or removed) onto existing classes
  - Share the same pawn level and displays on the same might/magic tabs with base class, and other advanced classes
  - Advanced classes share the same xml definition as normal classes, but are identified using the <isAdvancedClass> tag
  - See the Possessed class for an example
  - Other options for advanced classes include:
	* Restrict the advanced class to require a base class first using <requiresBaseClass> (true/false)
	* Allow the advanced class to be added as a trait during pawn generation with <canSpawnWithClass> (true/false)
	* Create advanced class "chains" by removing a pre-requisite trait with <removeRequiredTrait> (true/false)
	* Specify one or more valid pre-requisite traits using <requiredTraits> (TraitDef list)
	* Prevent pawns with certain traits from becoming the advanced class using <disallowedTraits> (TraitDef list)

 o Chained abilities
  - TMAbilityDef options that allow temporary abilities to be added and removed to create ability chains
  - See Possessed Control Spirit Storm for an example
  - Options include:
	* Specify a chained ability <chainedAbility> (TMAbilityDef)
	* Manually set a duration for the temporary ability <chainedAbilityExpiresAfterTicks> (integer > 0, -1 for "do not use")
	* Link the chained ability to be removed when the main ability cooldown expires <chainedAbilityExpiresAfterCooldown> (true/false)
	* Remove the ability after use; can be applied to any ability <removeAbilityAfterUse> (true/false)
	* Remove a list of abilities after use to clear or reset an ability chain <abilitiesRemovedWhenUsed> (TMAbilityDef list)

 o New Class: Possessor - an invisible, wandering spirit able to possess the bodies of the dead or living using spirit energy
  - Perishes when spirit energy fully depletes
  - Uses spirit energy to fuel their abilities
  - Able to possess other bodies and augments the abilities of the occupied body
  - Able to possess a corpse with all skills, talents, and memories of the dead pawn, but spirit energy will gradually deplete and must be replenished
  - Able to possess animals and assert control over their actions; the spirit has limited influence while in the body of an animal and spirit energy gradually depletes
  - Able to possess living pawns; much lower spirit energy loss than other options, but the host pawn will have conflicting thoughts - this can be offset if the spirit and the host pawn share the same outlook on life (backstory preferences, traits, gender, ideo, etc)
  - Shard of spirit extraction is used to remove a spirit from a pawn; the spirit may exit the body of an animal at any time
  - The possessor may naturally gain spirit energy while doing common, meditative tasks and can forcefully gain spirit energy using an ability or inflicting melee damage
  - A pawn occupied by a possessor will no longer be able to heal naturally; wounds can only be healed by external items, abilities, or spells, or when the possessed pawn gains spirit energy (by any means)

 o New Autocast options:
  - <onlyAppliesToCaster> (true/false) - forces the condition check against the caster instead of the target, when different
  - <targetNoFaction> (true/false) - target pawn is only selected if the faction is null (wild pawns)

Tweaks:
 o Summoned creatures will respond more aggressively when summoned near enemies
 o Magic Wardrobe automatically sets swapped equipment as forced/locked
 o Changed Brand graphics to be less error prone

Bug fixes:
 o Polymorphed or shapeshifted animals will take drafted orders again
 o Taunted targets will no longer attempt to attack a deceased taunter
 o Fixed a bug where AI would not use abilities if autocasting was disabled
 o Winter's Reign and Snap Freeze correctly assign damage attribution
 o Cure Disease can be cast while wearing a shield belt
 o Defense pylon will only spam invalid location message once instead of infinitely

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[8a549b0a60...](https://github.com/Mu-L/NetHack/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Thursday 2022-08-11 00:37:06 by Michael Meyer

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

---
## [sjp38/linux](https://github.com/sjp38/linux)@[0d1bc35339...](https://github.com/sjp38/linux/commit/0d1bc3533977d2b47d59aab4eb02f36b98b5eb75)
#### Thursday 2022-08-11 01:19:49 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e9eb094fc0...](https://github.com/treckstar/yolo-octo-hipster/commit/e9eb094fc0ea2d36e4fa079dde5c8c5bcde661da)
#### Thursday 2022-08-11 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [HyukjinKwon/spark](https://github.com/HyukjinKwon/spark)@[c4c623a3a8...](https://github.com/HyukjinKwon/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Thursday 2022-08-11 01:37:23 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [StarbloomSS13/StarbloomSS13](https://github.com/StarbloomSS13/StarbloomSS13)@[dcd6ff7eed...](https://github.com/StarbloomSS13/StarbloomSS13/commit/dcd6ff7eede6f473b20eb41af32c03e8fe27b055)
#### Thursday 2022-08-11 01:49:45 by Cheshify

Merge pull request #192 from unit0016/purple-crowbar-patch

[FUCK] Fixes purple crowbars / inducers because of the shitty ass modular aesthetics bullshit

---
## [Irinek0/iri-sojourn-station](https://github.com/Irinek0/iri-sojourn-station)@[931b7187bd...](https://github.com/Irinek0/iri-sojourn-station/commit/931b7187bd31e71d2a16792b7b2dd042cb049d97)
#### Thursday 2022-08-11 01:50:18 by nikothedude

"Optimizes" superior mobcode with somewhat of a nuclear option in terms of optimization. Fixes stealth bird targetting, fixes mobs being permastunned as well as not getting up from knockdowns.  (#3812)

* fuck

* fucwkc

* holy fuck

* i hate this

* FUCK YOUBALTIMORE

* superi

---
## [vijaydasmp/dash](https://github.com/vijaydasmp/dash)@[67ceda1b5a...](https://github.com/vijaydasmp/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Thursday 2022-08-11 02:32:12 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [Moltovz/StarbloomSS13](https://github.com/Moltovz/StarbloomSS13)@[635f518d04...](https://github.com/Moltovz/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Thursday 2022-08-11 04:27:14 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [sudharshanreddy333/Heart-Disease-Prediction](https://github.com/sudharshanreddy333/Heart-Disease-Prediction)@[b8af511052...](https://github.com/sudharshanreddy333/Heart-Disease-Prediction/commit/b8af51105266239dd25229c7ca8d925a609bdee7)
#### Thursday 2022-08-11 05:18:17 by sudharshanreddy333

Delete README.md

Heart-Disease-Prediction

Python Libraries Python libraries are a collection of functions and methods that allows us to perform many actions without writing the code.

NumPy: NumPy is a very popular python library for large multi-dimensional array and matrix processing, with the help of a large collection of high-level mathematical functions. It is very useful for fundamental scientific computations in Machine Learning.

Pandas: Pandas is a popular Python library for data analysis. Pandas is developed specifically for data extraction and preparation.

Matplotlib: Matpoltlib is a very popular Python library for data visualization. It provides various kinds of graphs and plots for data visualization, viz., histogram, error charts, bar chats, etc.

Scikit-learn: Scikit-learn is one of the most popular ML libraries for classical ML algorithms.

Scikit-learn supports most of the supervised and unsupervised learning algorithms. Scikit-learncan also be used for data-mining and data-analysis, which makes it a great tool who is starting out with ML.

Seaborn: Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

train_test_split: It splits the dataset into a training set and a test set.

Dataset The Heart Disease dataset has been taken from Kaggle. This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. It has a total number of 303 rows and 14 columns among which 165 have a heart disease. Data Source: Heart Disease Dataset

age: age in years sex: (1 = male; 0 = female) cp: chest pain type trestbps: resting blood pressure (in mm Hg on admission to the hospital) chol: serum cholestoral in mg/dl fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) restecg: resting electrocardiographic results thalach: maximum heart rate achieved exang: exercise induced angina (1 = yes; 0 = no) oldpeak: ST depression induced by exercise relative to rest slope: the slope of the peak exercise ST segment ca: number of major vessels (0-3) colored by flourosopy thal: thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect) target: (1= heart disease or 0= no heart disease)

The project involved analysis of the heart disease patient dataset with proper data processing. Then, 4 models were trained and tested with maximum scores as follows:

K Neighbors Classifier: 87%

Support Vector Classifier: 83%

Decision Tree Classifier: 79%

Random Forest Classifier: 84%

K Neighbors Classifier scored the best score of 87% with 8 neighbors.

---
## [begonia-crdroid/android_kernel_xiaomi_begonia](https://github.com/begonia-crdroid/android_kernel_xiaomi_begonia)@[7b69c730ea...](https://github.com/begonia-crdroid/android_kernel_xiaomi_begonia/commit/7b69c730eae9eeff00e97a615e0b239d9823e799)
#### Thursday 2022-08-11 06:13:39 by Peter Zijlstra

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
Signed-off-by: 7Soldier <reg.fm4@gmail.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[e3f78f64ae...](https://github.com/cockroachdb/cockroach/commit/e3f78f64aebdf8bd2c9bc43d7ca6c33ba4f46c73)
#### Thursday 2022-08-11 07:14:28 by craig[bot]

Merge #81995 #84358 #85081 #85440 #85940 #85941

81995: colexec: derive a tracing span in materializer when collecting stats r=yuzefovich a=yuzefovich

If we don't do this, then the stats would be attached to the span of
the materializer's user, and if that user itself has a lot of
payloads to attach (e.g. a joinReader attaching the KV keys it looked
up), then the stats might be dropped based on the maximum size of
structured payload per tracing span of 10KiB (see
`tracing.maxStructuredBytesPerSpan`). Deriving a separate span
guarantees that the stats won't be dropped.

This required some changes to make a test - that makes too many
assumptions about tracing infra - work.

Release note: None

84358: sql/tests: TestRandomSyntaxSchemaChangeColumn use a resettable timeout r=fqazi a=fqazi

fixes https://github.com/cockroachdb/cockroach/issues/65736

Previously, TestRandomSyntaxSchemaChangeColumn had a fixed
timeout, which meant that if schema change got stuck behind
each other, this timeout may not have been sufficient. Previously,
we tried bumping up this timeout, but this is not the most reliable
for this test. To address this, this patch introduces the concept of
resettable timeouts, which states that the timeout expires only if
no other statements are complete within the given timeout (otherwise,
its recalculated since the completion of the last statement. To avoid
potential starvation there is a limit on the number of resets,
which guarantees eventual expiry if a query is always bypassed.

Release note: None

85081: ui/cluster-ui: add wait time insights to active executions r=xinhaoz a=xinhaoz

Closes: https://github.com/cockroachdb/cockroach/issues/79127
Closes: https://github.com/cockroachdb/cockroach/issues/79131

This commit introduces a new section, 'Wait Time Insights' to the
active stmts/txns details pages. The section is included if the txn
being viewed is experiencing contention and includes info on the
blocked schema, table, index name, time spent blocking, and the
executions blocking or waiting for the viewed execution.

The section is powered by querying the `crdb_internal.cluster_locks`
table via the SQL api in `/api/v2/`. The table informatioin is
refreshed at an interval of 10s while on active execution pages,
and is requested along with session information (to give info on
active txns/stmts).

Only users having VIEWACTIVITY or higher permissions can view this
feature.

Refactor note: to remove  duplication across shared selector logic
in the active txn components, `activeExecutionsCommon.selectors.ts`
has been created. This file exports  combiner functions for active
txn selectors. The combiner func step contains the bulk of the logic
to transform data from the redux state to component props, thus future
changes to this logic will not need to be duplicated across packages.

Release note (ui change): A new section, 'Wait Time Insights' has
been added to the active statement and transaction details page.
The section is included if the txn being viewed is experiencing
contention and includes info on the blocked schema, table, index
name, time spent blocking, and the txns blocking or waiting for the
viewed txn.  Only users having `VIEWACTIVITY` or higher can view
this feature. The column 'Time Spent Waiting' has been added to
the active executions tables that shows the total amount of time
an execution has been waiting for a lock.

--------------
### Note to reviewers: only the 2nd commit is relevant, see first commit here: https://github.com/cockroachdb/cockroach/pull/85080

https://www.loom.com/share/53d8a74f9c9041a9b967e32dc370a153

85440: colmem: improve memory-limiting behavior of the accounting helpers r=yuzefovich a=yuzefovich

**colmem: introduce a helper method when no memory limit should be applied**

This commit is a pure mechanical change.

Release note: None

**colmem: move some logic of capacity-limiting into the accounting helper**

This commit moves the logic that was duplicated across each user of the
SetAccountingHelper into the helper itself. Clearly, this allows us to
de-duplicate some code, but it'll make it easier to refactor the code
which is done in the following commit.

Additionally, this commit makes a tiny change to make the resetting
behavior in the hash aggregator more precise.

Release note: None

**colmem: improve memory-limiting behavior of the accounting helpers**

This commit fixes an oversight in how we are allocating batches of the
"dynamic" capacity. We have two related ways for reallocating batches,
and both of them work by growing the capacity of the batch until the
memory limit is exceeded, and then the batch would be reused until the
end of the query execution. This is a reasonable heuristic under the
assumption that all tuples in the data stream are roughly equal in size,
but this might not be the case.

In particular, consider an example when 10k small rows of 1KiB are
followed by 10k large rows of 1MiB. According to our heuristic, we
happily grow the batch until 1024 in capacity, and then we do not shrink
the capacity of that batch, so once the large rows start appearing, we
put 1GiB worth of data into a single batch, significantly exceeding our
memory limit (usually 64MiB with the default `workmem` setting).

This commit introduces a new heuristic as follows:
- the first time a batch exceeds the memory limit, its capacity is memorized,
  and from now on that capacity will determine the upper bound on the
  capacities of the batches allocated through the helper;
- if at any point in time a batch exceeds the memory limit by at least a
  factor of two, then that batch is discarded, and the capacity will never
  exceed half of the capacity of the discarded batch;
- if the memory limit is not reached, then the behavior of the dynamic growth
  of the capacity provided by `Allocator.ResetMaybeReallocate` is still
  applicable (i.e. the capacities will grow exponentially until
  coldata.BatchSize()).

Note that this heuristic does not have an ability to grow the maximum
capacity once it's been set although it might make sense to do so (say,
if after shrinking the capacity, the next five times we see that the
batch is using less than half of the memory limit). This is an conscious
omission since I want this change to be backported, and never growing
seems like a safer choice. Thus, this improvement is left as a TODO.

Also, we still might create batches that are too large in memory
footprint in those places that don't use the SetAccountingHelper (e.g.
in the columnarizer) since we perform the memory limit check at the
batch granularity. However, this commit improves things there so that we
don't reuse that batch on the next iteration and will use half of the
capacity on the next iteration.

Fixes: #76464.

Release note (bug fix): CockroachDB now more precisely respects the
`distsql_workmem` setting which improves the stability of each node and
makes OOMs less likely.

**colmem: unexport Allocator.ResetMaybeReallocate**

This commit is a mechanical change to unexport
`Allocator.ResetMaybeReallocate` so that the users would be forced to use
the method with the same name from the helpers. This required splitting
off the tests into two files.

Release note: None

85940: sql/catalog/typedesc: fix bug which partially hydrated a type r=fqazi a=ajwerner

In rare cases where we hit an error hydrating the contained type of an
array alias type, we'd populate the name, but not the contents.

Fixes #85376

Release note (bug fix): Fixed a rare bug where errors could occur related
to the use of arrays of enums.

85941: sql/types: do not panic formatting unhydrated UDTs r=ajwerner a=ajwerner

Before this patch, if a bug resulted in a UDT's types.T getting to a point
where it was being formatted to a string without being hydrated, a panic would
occur. Now the type is formatted into an OIDTypeReference which is slightly
less pretty, but is valid.

Relates to #85447

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>
Co-authored-by: Faizan Qazi <faizan@cockroachlabs.com>
Co-authored-by: Xin Hao Zhang <xzhang@cockroachlabs.com>
Co-authored-by: Andrew Werner <awerner32@gmail.com>

---
## [SDArtsCode/blindsighted2](https://github.com/SDArtsCode/blindsighted2)@[3d7285bcdd...](https://github.com/SDArtsCode/blindsighted2/commit/3d7285bcdd5ccf4d98dc98531778621763ec42a5)
#### Thursday 2022-08-11 07:27:24 by xrbeaky

Entry #14: My limbs feel like they are frozen solid. I am using my last remaining energy in order to write these messages, and log my final hours. If anyone associated with the project finds this journal, know that you must destroy everything we have worked for. The research must NOT be released to the public. Public knowledge of what we have seen may cause us to tear ourselves apart.  I know you have left me to die, with full intention to publish the research and claim glory. However, your petty prestige will be well overshadowed by the doom that will soon fall upon humanity. If my life's work and research means anything, HEED MY WARNING. If you are not associated with the project, you must leave the artic immediately. Retreat to high-ground, preferably inland. You may have to stay there forever. Do not go back for anybody. If you're reading this, they are probably already dead. Enjoy the sunlight while you still can.

---
## [Historical-Expansion-Mod/Greater-Flavor-Mod](https://github.com/Historical-Expansion-Mod/Greater-Flavor-Mod)@[a137a0720e...](https://github.com/Historical-Expansion-Mod/Greater-Flavor-Mod/commit/a137a0720e565859903a3292ab0d33abf25402fb)
#### Thursday 2022-08-11 09:30:00 by Dukeçza Victor

Shut up Validator

Actually Mineral Oil is a lifesaver holy shit

---
## [desarrollo-ti/laminas-soap](https://github.com/desarrollo-ti/laminas-soap)@[82374c253b...](https://github.com/desarrollo-ti/laminas-soap/commit/82374c253bc52916a1d732b194740ddae32c6115)
#### Thursday 2022-08-11 09:41:59 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [groves/helix](https://github.com/groves/helix)@[973c51c3e9...](https://github.com/groves/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Thursday 2022-08-11 10:00:58 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [sfan5/mpv](https://github.com/sfan5/mpv)@[649556b2b6...](https://github.com/sfan5/mpv/commit/649556b2b65207c0d40751fae941223978b04932)
#### Thursday 2022-08-11 10:02:37 by Dudemanguy

github/workflows: use lua 5.1 on macos

LuaJIT is still actively developed, but upstream is allergic to making
new releases for whatever reason. The last tagged release was in May of
2017, so we probably shouldn't expect a new release anytime soon. Now
for mpv, this doesn't really matter except in the case of macOS where
2.0.5 is actually a bit broken (and of course the CI uses luajit). More
specifically, the 2.0.5 pc is broken and has a "-pagezero_size 10000"
flag which causes libmpv to fail (only executables are allowed to use
this). This magically works on waf. It's possible that it just happens
to ignore the link arguments. However on the meson build, this is broken
and led to a really ugly hack using a partial dependency so both mpv and
libmpv succeed. Fortunately, the 2.1 luajit branch fixes this.
Unfortunately, there's no actual release.

Instead, just use Lua 5.1. Note that lua 5.1 is technically deprecated
in homebrew, but the chances of this going away is pretty slim since
everyone knows that new lua versions are not backwards compatible.
Anyways, using 5.1 works fine and lets us get rid of a terrible hack in
the meson build. People really shouldn't be using 2.0 LuaJIT anyway.

---
## [sfan5/mpv](https://github.com/sfan5/mpv)@[f9bf6a601c...](https://github.com/sfan5/mpv/commit/f9bf6a601c563015706bed7bdb2b4984119db360)
#### Thursday 2022-08-11 10:02:37 by Dudemanguy

meson: remove horrifying macos luajit hack

See the previous commit for the full explanation. Basically, luajit 2.0
has a bad pc file on macos that causes libmpv to fail during build. The
workaround was, if the os was darwin and luajit was found, to save a
full luajit dep and a partial luajit dep with the link args removed. The
partial dep was used for compiling libmpv, and the full dep was used for
the actual mpv executable. This worked and was needed for the CI to pass
but it sucked. Since the previous commit now makes the CI grab lua 5.1,
we don't need all this crap anymore. Just delete it and treat the
dependency normally.

This does effectively mean that building libmpv with luajit 2.0 on macOS
will no longer work with the meson build. However libraries not being
built correctly is not a mpv-specific issue. The waf build will succeed
for some reason, but it has known issues and it would be better if it
just failed honestly. An upstream developer said years ago that that
macOS users should use the 2.1 branch (and there's no release of
course). In any case, no macOS user should be building mpv with luajit
2.0, so we shouldn't be going out of our way to support this.

https://github.com/mpv-player/mpv/issues/7512
https://github.com/LuaJIT/LuaJIT/issues/521#issuecomment-562999247

---
## [sfan5/mpv](https://github.com/sfan5/mpv)@[34e0a212cd...](https://github.com/sfan5/mpv/commit/34e0a212cd2e0a073a3580952549a62ede38c2d6)
#### Thursday 2022-08-11 10:02:37 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[e4613632cc...](https://github.com/Foundation-19/Foundation-19/commit/e4613632cc5b9ab4363d8c768752d74623e9112b)
#### Thursday 2022-08-11 10:36:59 by Grey

Remove ERT Code that makes it so you can't call the shuttle for 30 minutes (#639)

* gets rid of old dumb code

* Revert "gets rid of old dumb code"

This reverts commit a816ca0c26964781b8a0bdf2d1af4858bc76964d.

* simpler implementation (i was strongarmed)

* removes the datum

* fuck your predicates they're not used anywhere

* Revert "fuck your predicates they're not used anywhere"

This reverts commit eefa96c718892a74936efff85b96edbef4382c0a.

* Revert "Revert "fuck your predicates they're not used anywhere""

This reverts commit 6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8.

* THIS TIME WE ACTUALLY REMOVE THE DME RIGHT

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[08b21a9400...](https://github.com/mrakgr/The-Spiral-Language/commit/08b21a94001cb1984045431601ec3743e88fdc05)
#### Thursday 2022-08-11 10:53:09 by Marko Grdinić

"8:35am. I slept like a rock. Considering I went to bed at something close to 2am, it is really surprising how early I got up. I am decently rested right now too. Let me check the mail? Literally nothing.

8:40am. Ok, let me have my fun here and I will do some writing. Girls Frontline manga is out.

9:25am. How dod I spent so much time chilling? At any rate, let me start. I am far too addicted to Kingmaker.

Let's aim for publication to Royal Road.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

$$$

> The symbolism of the poem is strong, and reflects well what I am trying to become, and what I am trying to challenge. I give it high marks, I forgive the lack of rhyme. It would just get lost in translation anyway.

Let me get rid of this sentence.

9:35am. Focus me, stop thinking about ML.

This sucks. I'd rather play Kingmaker than write.

But I have to do this. The best time to do writing is now. There are no AI chips demanding my attention and I am not forced to get a job. My parents are still here in the world, though the decay as time goes on is making me nervous. Years down the road, it might very well be possible that even if I wanted to take a year to just write, I wouldn't have the leeway to do it. I should not take this ability that I have now for granted.

9:40am. It is easy to dream myself being popular and having a ton of people give me dosh on Patreon to support my projects. I need to explore that possibility. Having sponsors for the projects you like doing will always be better than being some mercenary or wage slave.

Right now I am really dissatisfied with myself. I feel like I should be getting my hands on AI chips, but really, they quite rare. I am not wrong about that. It would be another thing if they were easy to get. If they were far enough in their development that I could access them in a major cloud provider, or get them in a store much like GPUs and CPUs, then that is when I'd really have to punch myself in the face for sitting on my ass. But right now, just what am I going to do? My personal ideas for ML have all failed, if I got the chip, I could have some fun implementing the game on them. But then I'd still be stuck bashing my head against the wall trying to find an ML algorithm capable of training the agents. Yes, I could try the evolving the algo idea, but it is likely I would run into difficulties with that as well.

Just trying out random things in hopes of making it work will not make me better as a programmer. If it were a viable approach to developing myself, the best programmers would have been academics working on ML.

I really need something to give me a leg up. If I could have gotten to the point of minor profitability, I could have used that to support my research endeavors. But right now I can't basically do something like selling experimental leftovers to fund the project.

The experimental leftover is Spiral.

9:50am. I could go back to the old Simulacrum arcs, do the covers for them and proofread them. Then I could publish them, but I do not want to touch those old stories as they make me cringe.

9:55am. If I am being arrogant and stuck up, then it is only because I am not appreciating the opportunity bestowed upon me here.

I need to do it, Heaven's Key and Hatred need to be made. I need to write them and see people's reaction to them. I am not the same as in 2014.

10am. This life, and this time, only comes once.

Let me see if I can do even a single page today. You never know when you are going to get tired and give up. If I can't do it, I'll spend some time in bed.

10:05am. Ugh, why didn't I describe the buildings when he first logged in. I should highlight that he is in fact on one of the floating golden cities..

11:20am. Let me take a short break. Now I have to describe the drop. I like the idea for the scene from last year, but not so much the actual content. I need to make it a bit less crazy.

11:35am. The crazyiness of an act really depends on the thought going into it rather than the act itself.

12:40pm. Ok, it has been done. I didn't overplay the craziness this time. Let me paste into the docs. How long is the chapter now?

12:45pm. A bit over 4 pages. Did some fixing.

I am always surprised by how much I write. I thought it would be less.

12:50pm. Let me have breakfast here."

---
## [jelly/bots](https://github.com/jelly/bots)@[146d33c4f6...](https://github.com/jelly/bots/commit/146d33c4f6a12f5140353c23176637fe8d0379a2)
#### Thursday 2022-08-11 11:08:23 by Allison Karlitskaya

machine_virtual: bind multicast to localhost

When using socket-based network devices, with the `mcast` option (but
without an explicitly specified local address), qemu attempts to find a
suitable interface to use by scanning the available "up" interfaces for
ones that have the MULTICAST flag enabled (as per `ip link`).

The loopback interface doesn't normally have this flag enabled, so if
it's the only one that's up, the search will fail, causing the following
message:

    libvirt: QEMU Driver error : internal error: qemu unexpectedly closed the monitor: 2022-08-09T15:52:35.668412Z qemu-system-x86_64: -netdev socket,mcast=230.0.0.1:5600,id=mcast0: can't add socket to multicast group 230.0.0.1: No such device

If we force qemu to use the loopback interface, however, it will
succeed — even without the multicast flag being set.  Since we're not
actually interested in communicating between machines, force
127.0.0.1 as the local address.

This allows `image-customize`, `vm-run`, and testing in general to work
without the presence of any network connection, and without hacks such
as adding a dummy bridge or veth device.

Fixes cockpit-project/cockpit#12782

---
## [khanzjob/crime-prediction](https://github.com/khanzjob/crime-prediction)@[70cdd70e67...](https://github.com/khanzjob/crime-prediction/commit/70cdd70e67cdf354c62ac91de156265f1092bfe6)
#### Thursday 2022-08-11 12:12:00 by khanzjob

HACKLAB HACKTHON PWNSTARS PROJECT FOR CRIME PREDICTION

HACKLAB HACKTHON PWNSTARS PROJECT FOR CRIME PREDICTION
Introduction
San Francisco was infamous for housing some of the world's most notorious criminals on the inescapable island of Alcatraz. Today, the city is known more for its tech scene than its criminal past. From Sunset to SOMA, and Marina to Excelsior, this project analyzes 12 years of crime reports from across all of San Francisco's neighborhoods to create a model that predicts the category of crime that occurred, given time and location.

Definition
Project Overview
Crime is a social phenomenon as old as societies themselves, and although there will never be a free from crime society - just because it would need everyone in that society to think and act in the same way - societies always look for a way to minimize it and prevent it. In the modern United States history, crime rates increased after World War II, peaking from the 1970s to the early 1990s. Violent crime nearly quadrupled between 1960 and its peak in 1991. Property crime more than doubled over the same period. Since the 1990s, however, crime in the United States has declined steadily. Until recently crime prevention was studied based on strict behavioral and social methods, but the recent developments in Data Analysis have allowed a more quantitative approach in the subject. We will explore a dataset of nearly 12 years of crime reports from across all of San Francisco's neighborhoods, and we will create a model that predicts the category of crime that occurred, given the time and location.

Problem Statement
To examine the specific problem, we will apply a full Data Science life cycle composed of the following steps:

Data Wrangling to audit the quality of the data and perform all the necessary actions to clean the dataset.
Data Exploration for understanding the variables and create intuition on the data.
Feature Engineering to create additional variables from the existing.
Data Normalization and Data Transformation for preparing the dataset for the learning algorithms (if needed).
Training / Testing data creation to evaluate the performance of our models and fine-tune their hyperparameters.
Model selection and evaluation. This will be the final goal; creating a model that predicts the probability of each type of crime based on the location and the date.

---
## [myzael/HOI4-ULTRA-Project](https://github.com/myzael/HOI4-ULTRA-Project)@[31b5b6cb9b...](https://github.com/myzael/HOI4-ULTRA-Project/commit/31b5b6cb9bb628e42f0b9e88665228d5b6b5c0c0)
#### Thursday 2022-08-11 12:46:22 by T3rm1dor

Big changes to soviet NF tree

- Removed Cg modifiers in five year plans but made PE gives +5 cg more so initially there is no change. The other cg changes is remove the extra 5 on third year plan but to compensate we will achieve a higher yield is 2% cg reduction and no cg bonus from the collectivization effort. This is probably a sligth buff, but considering the propaganda campaing run for 2 years and that the current +5cg debuff from 3rd year plan can be consider a noob trap as you are only making mils so I'll say it is an improvement.
- On the air tree, I have make most focus that improve red airforce 5 weeks instead of three. Also, I've added an extra -10% efficiency to red airforce but made intensify air pilot training give 10% efficiency while giving less bonuses and not beibg exclusive of intensify aircraft production, with both this focus and the modern air war taking 49 days and can't be taken beforre barb . So now while at war it takes 3 months to fix air mission efficiency, which isn't that much of an issue but should compete a bit with army buffs. It isn't that big of a nerf, but it should make getting those green airs a bit harder to get early on.
- Army changes is making penal battalions improve MP recovery rate like an extra tech and make for the motherland spirit require order 227, which is now moved to desperate measures.
- Red fleet initial focuses are cheaper do getting the initial dockyard decision is more viable.
- Focuses under collectivist science now take 35 days again
- Molotov and Stalin line no longer mutually exclusive but each take 35 days. Molotov line isn't that great to begin with but if a player considers that the opportunity cost is worth it they should go for it.
- On ideas: Soviet land shock recovered the attack debuff
- Propaganda military buffs have overall be nerfed. Metal campaing now gives 4 extra steel and 4 extra aluminium bc the campaing was useless before. The partisan campaing no longer stop enemy strategic redeployment but instead give better combat bonuses.

---
## [SomeGuyEatingPie/GS13](https://github.com/SomeGuyEatingPie/GS13)@[5b7f7a52e4...](https://github.com/SomeGuyEatingPie/GS13/commit/5b7f7a52e462ac381aa5e8bd762ccb2fbfc9476b)
#### Thursday 2022-08-11 13:06:19 by MrSky12

Removed the fat ray

Fuck you fat ray for being bad.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[448da74eb0...](https://github.com/mrakgr/The-Spiral-Language/commit/448da74eb0a43535b88e3bc30f60f9c621f3be4a)
#### Thursday 2022-08-11 15:55:36 by Marko Grdinić

"2:05pm. Done with breakfast. Let me chill and then I will resume writing.

2:25pm. Right now the temperatures are fine at 30C, but my mom mentioned yesterday she heard they are going to rise to 39C. I am not sure how much to believe that. If that happens it is going to be hell in this room. Anyway, I do not feel like writing. I'll turn off the computer and step away from the screen for a while. Right now I've caught up to where I was last year.

I want to think about the next scene carefully and in depth. Maybe I should finally do some outlining now that I am almost done with the intro parts.

I got the momentum going and established my own motivation. I can afford to slow things down somewhat so as to think about it.

2:35pm. Let me rest. If feels like I only have a few hours in a day to work in. It is ridiculous. I am always so strapped for time.

5:35pm. I meant to resume, but I see that it is almost 6pm, so I'll skip. I've had some time to think about it.

5:50pm. For the first time, I thought in depth about the general backstory of the city. I guess that will take place of the outlining.

I want to write, but I do not feel like doing it right now.

In times like these I have to remind myself that this also double as a vacation. I already did a bit for the day so it is not like I am slacking. Let me mind off. I think maybe Playing Pathfinder until so late did damage me. I need to go to bed earlier. If necessary, to make time for sleep, I'll compress my work into a shorter session rather than aiming for 6pm like before.

It will be a tug of war between different desires.

I think if that by the end of the week I do not receive a reply to my Tenstorrent proposal I'll try emailing support and asking them about it. I really wish I could get in touch with somebody doing work at the company. Right now, let me play games and watch anime. That is the way it should go.

5:55pm. I am actually quite stressed due to not writing anything in the afternoon session. I already feel like I am falling behind. I need to learn to just let some things go. I can't be writing every day like a robot if I want to do good work."

---
## [openshift/cluster-version-operator](https://github.com/openshift/cluster-version-operator)@[9222fa9a66...](https://github.com/openshift/cluster-version-operator/commit/9222fa9a6616b58a8056c780b9a6252e82a26e37)
#### Thursday 2022-08-11 15:57:58 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [chanzuckerberg/redis-memo](https://github.com/chanzuckerberg/redis-memo)@[2ea8249b2b...](https://github.com/chanzuckerberg/redis-memo/commit/2ea8249b2be1ea189ca350d1d5563d5ced392fe2)
#### Thursday 2022-08-11 16:40:22 by Matt Wang

migrate to GitHub Actions from Travis CI, upgrade codecov (#101)

### Summary

This is a PR that does a couple of things:

- migrates the existing `.travis.yml` Travis CI to a pair of GitHub Actions (`ci.yml` and `publish-gem.yml`)
    - i replicate the `allow_failures` option using the same hack I implemented when moving to sorbet-coerce
    - in addition, I also now allow failures for rails 7. Let me know if we'd like me to revert that (it currently fails for ruby 2.7+). I believe when Donald last set this up, Rails 7 was not out yet.
- swap out the deprecated/inactive `codecov` gem for the new Action + required formatter 
- resolve new rubocop issues (since the repo doesn't pin rubocop, and has been out of date)
    - resolves autofixable spacing issues
    - changes the target ruby version in the gemspec to the "correct" format, explicitly sets it in rubocop config
    - temporarily disables `Performance/RedundantBlockCall` since its autofixes cause a coverage drop. If we like this PR, I'll open up a follow-up issue/PR to resolve.

I think technically this PR is ready to merge. However, I have a few questions:

- are we okay with introducing the new allowed failures? 
- are we okay with disabling the `Performance/RedundantBlockCall` cop?

In addition, we'll have to set the GitHub Actions secret before publishing the next release.

Shoutout to @katyho for figuring out how to properly connect to the db with `psql` (I later converted this to only use env vars, so the end-user experience is the same).

Closes #100.

---
## [lorleod/crypto-dashboard](https://github.com/lorleod/crypto-dashboard)@[c7044a1c80...](https://github.com/lorleod/crypto-dashboard/commit/c7044a1c807fdc1f5796ea1ccfb741a1e67e80c9)
#### Thursday 2022-08-11 17:24:36 by Taylor McLeod

was struggling last night with an issue related to async nature of setState. Price and date data wasn't passing into table properly. Came back this morning and realized it was working and I just thought it wasn't because of another bug and my incomplete understanding. Also fixed 'objects are not valid as a react child' error!

---
## [danielBingham/peerreview](https://github.com/danielBingham/peerreview)@[cb0b40c941...](https://github.com/danielBingham/peerreview/commit/cb0b40c941c62dfff9f423b10d7b5a0ccee3f9c9)
#### Thursday 2022-08-11 17:41:11 by Daniel Bingham

Issue #48 - Review UX with no overlapping comments.

After three days of fighting with redux and react I finally have a
review UX that works and isn't awful.  I'm bummed I couldn't get Google
Docs style comments working - though... I might be able to now
actually... but what I have now is honestly probably better in the long
run.  It'll be much easier to make this responsive and to make it work
on small screens.  So yeah, we're going with it.

---
## [WillNilges/pubsite](https://github.com/WillNilges/pubsite)@[a9d3afdf2b...](https://github.com/WillNilges/pubsite/commit/a9d3afdf2b41102d645ccc4d4f197861c99a92e0)
#### Thursday 2022-08-11 21:01:05 by Will Nilges

God fucking fuck shit cock fuck

Co-authored-by: Ethan Ferguson <ethanf108@gmail.com>

---
## [keksbg/rustcore](https://github.com/keksbg/rustcore)@[e991493cc5...](https://github.com/keksbg/rustcore/commit/e991493cc53579c370cb4d98661e03147326dae8)
#### Thursday 2022-08-11 22:03:59 by Stella

refractor instructions; changes to derive macro
honestly i have no fucking idea how i got this working. this is a fucking miracle.
jesus christ is real or something idk

---
## [JarlPenguin/platform_bionic](https://github.com/JarlPenguin/platform_bionic)@[1f462dec34...](https://github.com/JarlPenguin/platform_bionic/commit/1f462dec34a5358c3e63d6a8e986a82248338aed)
#### Thursday 2022-08-11 22:17:33 by Elliott Hughes

Add %b and %B support to the scanf/wscanf and strto*/wcsto* families.

Coming to C23 via WG14 N2630.

This one is a little interesting, because it actually changes existing
behavior. Previously "0b101" would be parsed as "0", "b", "101" by these
functions. I'm led to believe that glibc plans to actually have separate
versions of these functions for C23 and pre-C23, so callers can have the
behavior they (implicitly) specify by virtue of which -std= they compile
with. Android has never really done anything like that, and I'm pretty
sure app developers have more than enough to worry about with API levels
without having to deal with the cartesian product of API level and C
standard.

Therefore, my plan A is "if you're running on Android >= U, you get C23
behavior". My plan B in the (I think unlikely) event that that actually
causes trouble for anyone is "if you're _targeting_ Android >= U, you
get C23 behavior". I don't think we'd actually want to have two versions
of each of these functions under any circumstances --- that seems by far
the most confusing option.

Test: treehugger
Change-Id: I0bbb30315d3fabd306905ad1484361f5d8745935

---
## [0x4E0x410x450x530x51/Kanban](https://github.com/0x4E0x410x450x530x51/Kanban)@[33d825353c...](https://github.com/0x4E0x410x450x530x51/Kanban/commit/33d825353c0413a40d990703f4a8f75fc286215f)
#### Thursday 2022-08-11 22:41:26 by AndyI0I

getting tired

i just found out that this bullshit thing for the sized settings doesn't even save the stupid effort value into the json, in fact, it actually removes it and the only thing left is f'n "NaN".
anyways, i now get why my team member Tyris was loosing his mind over javascript, poor dude

---
## [donut25-1/sojourn-station](https://github.com/donut25-1/sojourn-station)@[f5da3823ac...](https://github.com/donut25-1/sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Thursday 2022-08-11 23:41:41 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [donut25-1/sojourn-station](https://github.com/donut25-1/sojourn-station)@[c3c08d0946...](https://github.com/donut25-1/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Thursday 2022-08-11 23:41:41 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---

