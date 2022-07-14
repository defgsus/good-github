## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-13](docs/good-messages/2022/2022-07-13.md)


1,731,723 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,731,723 were push events containing 2,568,175 commit messages that amount to 187,372,142 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[321f65bb34...](https://github.com/mbs-octoml/mbs-tvm/commit/321f65bb34a29b749fbeab7bc9860097048ebb79)
#### Wednesday 2022-07-13 00:13:43 by Mark Shields

** Collage v2 sketch ***

- Test ByKind CombinerRule
- Move the TOpPattern attributes from Python to C++ so visible to C++ unit tests.
- wibble
- wibble
- starting to add CombinerRule unit tests
- sync with mbs-collage-subgraph changes
- rebase
- sync
- Clarify dataflow_graph.expr() vs expr constraints
- Beef up test_sub_graph
- Polish
- False alarm, reverting unnecessary const fiddles
- Bad merge, still have bug with missing const.
- Fix rebase
- Prepare for rebase
- Move CaptureIndexInSpans to generic tvm.relay.transform
- Fix test_sub_graph.py unit tests
- Make PartitionSpecs 1:1 with Targets
- Fix tests
- Finish merging Matthew's changes
- First pass merging Matthew's changes
- finish fixing lints
- test_tensorrt.py runs
- some lint fixes while waiting
- test annotation fiddles, disable pytorch test
- fix constant handling
- update tests for new API
- Switch TensorRT BYOC integration to IRModule-at-a-time
- [bug] index out of range
- don't need InferTypeExpr
- revert unnecessary changes
- revert unnecessary changes
- fix accumulate bug
- sync with 11481
- Eta-expand tuple ars in candidate partitions
  (so measurements does not need to worry about
  constructing tuple arguments)
- Polish compiler_function_utils for splitting out
- Mark functions as extern.
- Get rid of relay.ext.cutlass
- kExternalSymbol:String ----> kExtern:Bool
- Host glitch if PlanDevices run before CollagePartition
- Fix unit test
- Make load_static_library first class python func
- Get CUTLASS going on graph executor as well as vm
- Include export_library in estimate_seconds
- Rollback DSOLibrary changes.
- Add StaticLibraryNode and switch CUTLASS to use it
  This avoids the crazy serialize/deserialize/load hackery, which I'll now remove.
- Get running again
- CUTLASS picks up all options from 'cutlass' external codegen target.
- Revert false starts with cutlass handling
- Get CUTLASS going with program-at-a-time tuning and compilation instead of
  function at a time.
- Save DSOLibraries by contents rather than by reference.
- futzing with libraries
- revert unnecessary cutlass changes
- starting unit test for dsolibrary save
- Prepare scalar changes for PR.
- Eager candidate cost measurement.
- More conv2d_cudnn.cuda training records.
- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [D-Programming-GDC/gcc](https://github.com/D-Programming-GDC/gcc)@[5493ee7145...](https://github.com/D-Programming-GDC/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Wednesday 2022-07-13 00:23:30 by Alexandre Oliva

i386 testsuite: cope with --enable-default-pie

Running the testsuite on a toolchain build with --enable-default-pie
had some unexpected fails.  Adjust the tests to tolerate the effects
of this configuration option on x86_64-linux-gnu and i686-linux-gnu.

The cet-sjlj* tests get offsets before the base symbol name with PIC
or PIE.  A single pattern covering both alternatives somehow triggered
two matches rather than the single expected match, thus my narrowing
the '.*' to not skip line breaks, but that was not enough.  Still
puzzled, I separated the patterns into nonpic and !nonpic, and we get
the expected matchcounts this way.

Tests for -mfentry require an mfentry effective target, which excludes
32-bit x86 with PIC or PIE enabled, that's why the patterns that
accept the PIC sym@RELOC annotations only cover x86_64.  mvc7 is
getting regexps extended to cover PIC reloc annotatios and all of the
named variants, and tightened to avoid unexpected '.' matches.

The pr24414 test stores in an unadorned named variable in an old-style
asm statement, to check that such asm statements get an implicit
memory clobber.  Rewriting the asm into a GCC extended asm with the
variable as an output would remove the regression it checks against.
Problem is, the literal reference to the variable is not PIC, so it's
rejected by the elf64 linker with an error, and flagged with a warning
by the elf32 one.  We could presumably make the variable references
PIC-friendly with #ifdefs, but I doubt that's worth the trouble.  I'm
just arranging for the test to be skipped if PIC or PIE are enabled by
default.


for  gcc/testsuite/ChangeLog

	* gcc.target/i386/cet-sjlj-6a.c: Cope with --enable-default-pie.
	* gcc.target/i386/cet-sjlj-6b.c: Likewise.
	* gcc.target/i386/fentryname3.c: Likewise.
	* gcc.target/i386/mvc7.c: Likewise.
	* gcc.target/i386/pr24414.c: Likewise.
	* gcc.target/i386/pr93492-3.c: Likewise.
	* gcc.target/i386/pr93492-5.c: Likewise.
	* gcc.target/i386/pr98482-1.c: Likewise.

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[707fbfac7e...](https://github.com/OliOliOnsiPree/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Wednesday 2022-07-13 00:29:44 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[6fe0683a7b...](https://github.com/GForceTF/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Wednesday 2022-07-13 01:06:15 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [Ben10083/Foundation-19](https://github.com/Ben10083/Foundation-19)@[353aa23a95...](https://github.com/Ben10083/Foundation-19/commit/353aa23a9557e3c61325f5ed53874d69cd484445)
#### Wednesday 2022-07-13 01:17:50 by CerberusHellHound

Mapping Update : LCZ Medbay, CDC and Reeducation Center (#225)

* Update baystation12.dme

* 9mm/.45ACP Buff

Changes are as follow:
- Buffed 9mm dam from 8 to 25 (now it doesn't take a whole mag to take down an unarmoured man)
- Buffed .45 dam from 10 to 30
- Nerfed 9mm AP from 34 to 30
- Buffed 7,62 dam from 40 to 50 (It's supposed to be beefier than 5,56mm)

* Organ changes

Lower organ health value to make combat much deadlier.
Headshots are truly lethal now.

* Slight rebalance and renamings

List of changes :
- decreased brain health to 150 (instead of 200), it's high enough that medical assistance can be given if fast but low enough that you don't want to get shot
- increased damage values of weapons to baystation/nebula level (40 for a pistol for eg)
- increased adrenalin generation when hurt (less fading in and out, you can still use your gun when hit and pain won't be such a pain in the ass, but you're less likely to get back up once the final shot hits you)
- decreased relative size of lungs from 60% to 30% so that now, getting hit in the chest won't have as much chance of damaging your poor fucking lungs (yes 60% is the original baystation number.. it makes sense, it's a large organ, but it's a pain in the ass)
- changed some names and descriptions of certain weapons and firearms to better fit established naming convention
-made revolvers cycle the barrel instead of eject each shot (it's a revolver, not a damn rifle)
- slightly decreased firing delay for the mk9 revolver (slightly weaker than the mateba so slightly faster firing)
- decreased firing delay for the mk9 pistol (lower caliber, less recoil, easier to magdump)

* Mateba fix

Fixed a misstype for the mateba that incorrectly qualified its caliber.

* Mateba fix

Fixing typo

* The big Security Zone update

Main changes:
- Each zone have unique uniform and gears now (MTF is dressed tactically and well armoured to act as the toughest defense force for the critical area in HCZ and to pass as a rapid response team, EZ gets slightly formal but still utilitarian gears to accomplish their internal security and bodyguarding tasks, and LCZ largely remains the same)
- All security guards spawns with most of their gears on themselves and in their satchel (with the exception of webbings, thigh holster and rifle/p90)
- Nerfed Beanbag damage from 10 to 3 so that it will stop causing bleeding injuries to CDs, making it more usable as a non lethal ammunition
- Slightly nerfed rubber P90 agony damage

* Map change LCZ

* LCZ mapping update

Co-authored-by: tichys <tichman27@gmail.com>

---
## [wkxboot/libmodbus](https://github.com/wkxboot/libmodbus)@[6f915d4215...](https://github.com/wkxboot/libmodbus/commit/6f915d4215c06be3c719761423d9b5e8aa3cb820)
#### Wednesday 2022-07-13 01:37:56 by Stéphane Raimbault

Fix my so stupid fix for VD-1301 vulnerability

I can't believe I committed that copy/paste mistake.
Sorry Maor Vermucht and Or Peles, excepted naming your original
patch was OK.

Thank you Karl Palsson for your review.

---
## [enjoy-binbin/redis](https://github.com/enjoy-binbin/redis)@[0e5b813ef9...](https://github.com/enjoy-binbin/redis/commit/0e5b813ef94b373f82bc75efcf3405f2c81af3dc)
#### Wednesday 2022-07-13 02:05:47 by yoav-steinberg

Multiparam config set (#9748)

We can now do: `config set maxmemory 10m repl-backlog-size 5m`

## Basic algorithm to support "transaction like" config sets:

1. Backup all relevant current values (via get).
2. Run "verify" and "set" on everything, if we fail run "restore".
3. Run "apply" on everything (optional optimization: skip functions already run). If we fail run "restore".
4. Return success.

### restore
1. Run set on everything in backup. If we fail log it and continue (this puts us in an undefined
   state but we decided it's better than the alternative of panicking). This indicates either a bug
   or some unsupported external state.
2. Run apply on everything in backup (optimization: skip functions already run). If we fail log
   it (see comment above).
3. Return error.

## Implementation/design changes:
* Apply function are idempotent (have no effect if they are run more than once for the same config).
* No indication in set functions if we're reading the config or running from the `CONFIG SET` command
   (removed `update` argument).
* Set function should set some config variable and assume an (optional) apply function will use that
   later to apply. If we know this setting can be safely applied immediately and can always be reverted
   and doesn't depend on any other configuration we can apply immediately from within the set function
   (and not store the setting anywhere). This is the case of this `dir` config, for example, which has no
   apply function. No apply function is need also in the case that setting the variable in the `server` struct
   is all that needs to be done to make the configuration take effect. Note that the original concept of `update_fn`,
   which received the old and new values was removed and replaced by the optional apply function.
* Apply functions use settings written to the `server` struct and don't receive any inputs.
* I take care that for the generic (non-special) configs if there's no change I avoid calling the setter (possible
   optimization: avoid calling the apply function as well).
* Passing the same config parameter more than once to `config set` will fail. You can't do `config set my-setting
   value1 my-setting value2`.

Note that getting `save` in the context of the conf file parsing to work here as before was a pain.
The conf file supports an aggregate `save` definition, where each `save` line is added to the server's
save params. This is unlike any other line in the config file where each line overwrites any previous
configuration. Since we now support passing multiple save params in a single line (see top comments
about `save` in https://github.com/redis/redis/pull/9644) we should deprecate the aggregate nature of
this config line and perhaps reduce this ugly code in the future.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ca0610f124...](https://github.com/treckstar/yolo-octo-hipster/commit/ca0610f124f6745aedce7eb4e9a0fceb536f2815)
#### Wednesday 2022-07-13 03:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Jul-Lii/android_kernel_xiaomi_sdm845](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845)@[7d36e4b87c...](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845/commit/7d36e4b87cd1390c309ab1f1af3370adce50eed4)
#### Wednesday 2022-07-13 04:17:19 by Peter Zijlstra

sched/core: Implement new approach to scale select_idle_cpu()

Hackbench recently suffered a bunch of pain, first by commit:

  4c77b18cf8b7 ("sched/fair: Make select_idle_cpu() more aggressive")

and then by commit:

  c743f0a5c50f ("sched/fair, cpumask: Export for_each_cpu_wrap()")

which fixed a bug in the initial for_each_cpu_wrap() implementation
that made select_idle_cpu() even more expensive. The bug was that it
would skip over CPUs when bits were consequtive in the bitmask.

This however gave me an idea to fix select_idle_cpu(); where the old
scheme was a cliff-edge throttle on idle scanning, this introduces a
more gradual approach. Instead of stopping to scan entirely, we limit
how many CPUs we scan.

Initial benchmarks show that it mostly recovers hackbench while not
hurting anything else, except Mason's schbench, but not as bad as the
old thing.

It also appears to recover the tbench high-end, which also suffered like
hackbench.

Tested-by: Matt Fleming <matt@codeblueprint.co.uk>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Cc: Chris Mason <clm@fb.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: Mike Galbraith <efault@gmx.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: hpa@zytor.com
Cc: kitsunyan <kitsunyan@inbox.ru>
Cc: linux-kernel@vger.kernel.org
Cc: lvenanci@redhat.com
Cc: riel@redhat.com
Cc: xiaolong.ye@intel.com
Link: http://lkml.kernel.org/r/20170517105350.hk5m4h4jb6dfr65a@hirez.programming.kicks-ass.net
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>

---
## [Layla-Veridian/XRF-Third-Contact-production](https://github.com/Layla-Veridian/XRF-Third-Contact-production)@[05ff5cdfce...](https://github.com/Layla-Veridian/XRF-Third-Contact-production/commit/05ff5cdfce37fc95d79f9f92a260eabf1fb467ee)
#### Wednesday 2022-07-13 04:42:11 by Aphast

Sneed - Feed and Seed. CHUCK - F**K AND SUCK WE GET IT HAHAHA HA SO FUNNY BECAUSE F**K AND SUCK F**K WHOOOOOA BRO LIKE HAVING INTERCOURSE AND FELLATIO HOLY WOW HOW DID THE SIMPSONS GET AWAY WITH THIS ONE? GOLLY GEE WILLIKERS WHAT THE F**K IT'S ABSOLUTELY HILARIOUS AHAHAHAHAHA BECAUSE SNEED SELLS FEED AND SEED WHICH IS TOTALLY NORMAL BUT CHUCK, CHUCKY, CHUCK SELLS F**K AND SUCK CHUCK SELLS F**K AND SUCK! F**K AND SUCK! (#3)

---
## [Catrol-s-Forks/terminal](https://github.com/Catrol-s-Forks/terminal)@[9ccd6ecd74...](https://github.com/Catrol-s-Forks/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Wednesday 2022-07-13 05:31:28 by Mike Griese

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
## [KhaoticPluto/Prototype](https://github.com/KhaoticPluto/Prototype)@[88215214c5...](https://github.com/KhaoticPluto/Prototype/commit/88215214c59d85cc9782a8eea54ffec6f0c33203)
#### Wednesday 2022-07-13 06:09:11 by xyndall

fixing the models

oh god it was an annoying as thing, luckily i got a new process that is much better and less finiky and yeah

---
## [SgtHunk/tgstation-1](https://github.com/SgtHunk/tgstation-1)@[98f32035d8...](https://github.com/SgtHunk/tgstation-1/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Wednesday 2022-07-13 06:37:43 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

---
## [vdavalon01/nomad](https://github.com/vdavalon01/nomad)@[f998a2b77b...](https://github.com/vdavalon01/nomad/commit/f998a2b77b84a542d73f11a0a254576f9031d1f3)
#### Wednesday 2022-07-13 07:34:03 by Michael Schurter

core: merge reserved_ports into host_networks (#13651)

Fixes #13505

This fixes #13505 by treating reserved_ports like we treat a lot of jobspec settings: merging settings from more global stanzas (client.reserved.reserved_ports) "down" into more specific stanzas (client.host_networks[].reserved_ports).

As discussed in #13505 there are other options, and since it's totally broken right now we have some flexibility:

Treat overlapping reserved_ports on addresses as invalid and refuse to start agents. However, I'm not sure there's a cohesive model we want to publish right now since so much 0.9-0.12 compat code still exists! We would have to explain to folks that if their -network-interface and host_network addresses overlapped, they could only specify reserved_ports in one place or the other?! It gets ugly.
Use the global client.reserved.reserved_ports value as the default and treat host_network[].reserverd_ports as overrides. My first suggestion in the issue, but @groggemans made me realize the addresses on the agent's interface (as configured by -network-interface) may overlap with host_networks, so you'd need to remove the global reserved_ports from addresses shared with a shared network?! This seemed really confusing and subtle for users to me.
So I think "merging down" creates the most expressive yet understandable approach. I've played around with it a bit, and it doesn't seem too surprising. The only frustrating part is how difficult it is to observe the available addresses and ports on a node! However that's a job for another PR.

---
## [hestiacp/hestiacp](https://github.com/hestiacp/hestiacp)@[365dab5670...](https://github.com/hestiacp/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Wednesday 2022-07-13 08:11:09 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [decompiler-explorer/decompiler-explorer](https://github.com/decompiler-explorer/decompiler-explorer)@[2fd7c468f1...](https://github.com/decompiler-explorer/decompiler-explorer/commit/2fd7c468f14898a4f75964f6bdc6e5c1bdcbadc6)
#### Wednesday 2022-07-13 08:35:01 by Glenn Smith

Mega sketchy multi-worker config by timeout locking until HN calms down

Oh god our WIP site is #2 on HN at 4 in the morning I'm so sorry everyone I swear we were going to scale it soon

---
## [loafoflead/secs](https://github.com/loafoflead/secs)@[0a03b0538b...](https://github.com/loafoflead/secs/commit/0a03b0538b99555826004f223ba5bae46c111b86)
#### Wednesday 2022-07-13 08:35:57 by loafoflead

renamed to 'sceller' because someone already had secs :( waa waa also now its a cool french name which means SCLICING so FUCK YEAH. I'm not mad haha.

---
## [SparshaSaha/react-native](https://github.com/SparshaSaha/react-native)@[47280de85e...](https://github.com/SparshaSaha/react-native/commit/47280de85e62f33f0b97bc1ed7c83bc6ca0dc7d4)
#### Wednesday 2022-07-13 08:46:43 by Joshua Gross

New Props parsing infrastructure for perf improvements: visitor pattern vs random-map-access pattern (ViewProps, minus YogaLayoutableShadowNode)

Summary:
Perf numbers for this stack are given in terms of before-stack and after-stack, but the changes are split up for ease of review, and also to show that this migration CAN happen per-component and is 100% opt-in. Most existing C++ components do not /need/ to change at all.

# Problem Statement

During certain renders (select critical scenarios in specific products), UIManagerBinding::createNode time takes over 50% of JS thread CPU time. This could be higher or lower depending on the specific product and interaction, but overall createNode takes a lot of CPU time. The question is: can we improve this? What is the minimal overhead needed?

The vast, vast majority of time is taken up by prop parsing (specifically, converting JS values across the JSI into concrete values on the C++ props structs). Other methods like appendChild, etc, do not take up a significant amount of time; so we conclude that createNode is special, and the JSI itself, or calling into C++, is not the problem. Props parsing is the perf problem.

Can we improve it? (Spoiler: yes)

# How does props parsing work today?

Today, props parsing works as follows:

1. The ConcreteComponentDescriptor will construct a RawPropsParser (one per component /type/, per application: so one for View, one for Image, one for Text... etc)
2. Once per component type per application, ConcreteComponentDescriptor will call "prepare" on the RawPropsParser with an empty, default-constructed ConcreteProps struct. This ConcreteProps struct will cause RawProps.at(field) for every single field.
3. Based on the RawProps::at calls in part 2, RawPropsParser constructs a Map from props string names (width, height, position, etc) to a position within a "value index" array.
4. The above is what happens before any actual props are parsed; and the RawPropsParser is now ready to parse actual Props.
5. When props are actually being parsed from a JSI dictionary, we now have two phases:
  1. The RawPropsParser `preparse`s the RawProps, by iterating over the JSI map and filling in two additional data structures: a linear list of RawValues, and a mapping from the ValueIndex array (`keyIndexToValueIndex_`; see step 3) to a value's position in the values list (`value_` in RawPropsParser/RawProps);
  2. The ConcretePropT constructor is called, which is the same as in step 2/3, which calls `fieldValue = rawProps.at("fieldName")` repeatedly.
  3. For each `at` call, the RawProps will look up a prop name in the Map constructed in step 3, and either return an empty value, or map the key name to the `keyIndexToValueIndex_` array, which maps to a value in `values_`, which is then returned and further parsed.

So, a few things that become clear with the current architecture:

1. Complexity is a property of the number of /possible/ props that /can/ be parsed, not what is actually used in product code. This violates the "only pay for what you use" principal. If you have `<View opacity={0.5} />`, the ViewProps constructor will request ~170 properties, not 1!
2. There's a lot of pre-parsing which isn't free
3. The levels of indirection aren't free, and make cache misses more likely and pipelining is more challenging
4. The levels of indirection also require more memory - minor, but not free

# How can we improve it?

The goal is to improve props parsing with minimal or zero impact on backwards-compability. We should be able to migrate over components when it's clear there's a performance issue, without requiring everything gets migrated over at once. This both (1) helps us prove out the new architecture, (2) derisks the project, (3) gives us time, internally and externally, to perfect the APIs and gradually migrate everything over before deleting the old infrastructure code entirely.

Thus, the goal is to do something that introduces a zero-cost abstraction. This isn't entirely possible in practice, and in fact this method slightly regresses components that do not use the new architecture /at all/, while dramatically improving migrated components and causing the impact of the /old/ architecture to be minimal.

# Solution

1. We still keep the existing system in place entirely.
2. After Props are constructed (see ConcreteComponentDescriptor changes) we iterate over all the /values/ set from JS, and call PropsT::setProp. Incidentally, this allows us to easily reuse the same prop for multiple values for "free", which was expensive in the old system.
3. It's worth noting that this makes a Props struct "less immutable" than it was before, and essentially now we have a "builder pattern" for Props. (If we really wanted to, we could still require a single constructor for Props, and then actually use an intermediate PropsBuilder to accumulate values - but I don't think this overhead would be worth for the conceptual "immutability" win, and instead a "Construct/Set/Seal" model works fine, and we still have all the same guarantees of immutability after the parsing phase)

# Implementation Details
# How to properly construct a single Prop value

Minor detail: parsing a single prop is a 3-step process. We imagine two scenarios: (1) Creating a new ShadowNode/Props A from nothing/void, so the previous Props value is just the default constructor. (2) Cloning a ShadowNode A->B and therefore Props A must be copied to Props B before parsing.

We will denote this as a clone from A->B, where A may or may not be a previous node or a default-constructed Props node; and imagine in particular that we're setting the "opacity" value for PropsB.

We must first (1) copy a value over from the previous version of the Props struct, so B.opacity = A.opacity; (2) Determine if opacity has been set from JS. If so, and there is a value, B.opacity = parse(JSValue). (3) If JS has passed in a value for the prop, BUT the value is `null`, it means that JS is resetting or deleting the prop, so we must set it BACK to the default. In this case we set PropsB.opacity = DefaultConstructedProps.opacity.

We must take care in general to ensure that the correct behavior is achieved here, which should help to explain some of the code below.

## String comparisons vs hash comparisons

In the previous system, a RawPropsKey is three `const char*` strings, concatenated together repeatedly /at runtime/. In practice, the ONLY reason we have the prefix, name, suffix Key structure is for the templated prop parsing in ViewProps and YogaStyableProps - that's it. It's not used anywhere else. Further, the key {"margin", "Left", "Width"} is identical to the key {"marginLeftWidth", null, null} and we don't do anything fancy with matching prefixes before comparing the whole string, or similar. Before comparison, keys are concatenated into a single string and then we use `strcmp`. The performance of this isn't terrible, but it's nonzero overhead.

I think we can do better and it's sufficient to compare hashed string values; even better, we can construct most of these /at compile time/ using constexpr, and using `switch` statements guarantee no hash collisions within a single Props struct (it's possible there's a collision between Props.cpp and ViewProps.cpp, for example, since they're different switch statements). We may eventually want to be more robust against has collisions; I personally don't find the risk to be too great, hash collisions with these keys are exceedingly unlikely (or maybe I just like to live dangerously). Thus, at runtime, each setProp requires computing a single hash for the value coming from JS, and then int comparisons with a bunch of pre-compiled values.

If we want to be really paranoid, we could be robust to hash collisions by doing `switch COMPILED_HASH("opacity"): if (strcmp(strFromJs, "opacity") == 0)`. I'm happy to do this if there's enough concern.

## Macros

Yuck! I'm using lots of C preprocessor macros. In general I found this way, way easier in reducing code and (essentially) doing codegen for me vs templated code for the switch cases and hashing prop names at compile-time. Maybe there's a better way.

Changelog: [Added][Fabric] New API for efficient props construction

Reviewed By: javache

Differential Revision: D37050215

fbshipit-source-id: d2dcd351a93b9715cfeb5197eb0d6f9194ec6eb9

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[5e051f5244...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/5e051f52443dce3178a94a28db60314b652a5e49)
#### Wednesday 2022-07-13 12:03:17 by Raja Kunal Pandit

Create 579A - Raising Bacteria.cpp

Output Status:

By Rajakunalpandit, contest: Codeforces Round #320 (Div. 2) [Bayan Thanks-Round], problem: (A) Raising Bacteria, Accepted

You are a lover of bacteria. You want to raise some bacteria in a box.

Initially, the box is empty. Each morning, you can put any number of bacteria into the box. And each night, every bacterium in the box will split into two bacteria. You hope to see exactly x bacteria in the box at some moment.

What is the minimum number of bacteria you need to put into the box across those days?

Input
The only line containing one integer x (1 ≤ x ≤ 109).

Output
The only line containing one integer: the answer.

Examples
inputCopy
5
outputCopy
2
inputCopy
8
outputCopy
1
Note
For the first sample, we can add one bacterium in the box in the first day morning and at the third morning there will be 4 bacteria in the box. Now we put one more resulting 5 in the box. We added 2 bacteria in the process so the answer is 2.

For the second sample, we can put one in the first morning and in the 4-th morning there will be 8 in the box. So the answer is 1.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5477158475...](https://github.com/mrakgr/The-Spiral-Language/commit/5477158475a988798b7369cb8cd9a575e0f132da)
#### Wednesday 2022-07-13 12:40:42 by Marko Grdinić

"1:30pm. Done with breakfast. I'll leave ep 2 of Lycoris for later. I've still yet to finish Virgin Road.

I've just been chilling during the break, but let me resume now. Usually I'd go on for longer, but since I am close to finishing the codegen I am eager to get through all the tests. I only have just a little bit left.

After I am done I'll take a break for the rest of the day.

```spiral
// Do array literals and their patterns work correctly?
inl main() : i32 =
    inl a = ;[1;2;3]
    match a with
    | ;[a;b;c] => a+b+c
    | ;[a;b] => a+b
    | ;[a] => a
    | _ => 0
```

This test gives me an out of bounds read.

```c
v0 = ArrayLit0(10, (int32_t []){1l,2l,3l});
```

This is a bit weird. What is with the array size here?

```fs
            let b = List.map tup_data b |> String.concat "," |> sprintf "{%s}"
            $"ArrayLit{(carray a).tag}({b.Length}, ({tup_ty a} []){b})" |> return'
```

Damn, I am taking the length of the string.

```fs
        | TyArrayLiteral(a,b') ->
            let b = List.map tup_data b' |> String.concat "," |> sprintf "{%s}"
            $"ArrayLit{(carray a).tag}({b'.Length}, ({tup_ty a} []){b})" |> return'
```

Let me do this.

Yeah, it works now. I like these nice and easy error to fix. As it turns out, I've been losing out on quite a bit by not using a memory safe version of C.

1:45pm. Gone through the main round of testing. Only serialization 1-4 are left. They should go swiftly. Let me do it and then I am done. I'll release the next minor version of Spiral.

1:50pm. I forgot that I can't run these on the C backend since it uses some .NET stuff.

I am done here. I guess I'll try updating the minor version. Let me try releasing it on the VS Code marketplace.

```
(node:17480) ExperimentalWarning: Conditional exports is an experimental feature. This feature could change at any time
v2.2.0
Publishing mrakgr.spiral-lang-vscode@2.2.0...
 ERROR  {"$id":"1","customProperties":{"Descriptor":null,"IdentityDisplayName":null,"Token":null,"RequestedPermissions":0,"NamespaceId":"00000000-0000-0000-0000-000000000000"},"innerException":null,"message":"A
ccess Denied: The Personal Access Token used has expired.","typeName":"Microsoft.VisualStudio.Services.Security.AccessCheckException, Microsoft.VisualStudio.Services.WebApi","typeKey":"AccessCheckException","errorCode":0,"eventId":3000}
```

It is saying that the token has expired.

https://code.visualstudio.com/api/working-with-extensions/publishing-extension

Damn it, now I have to go through this shit again. It worked for me right away for that other marketplace.

The azure page has change and I am not sure where I have to create the access token. Where was my marketplace? I want to try uploading it manually.

https://marketplace.visualstudio.com/manage/publishers/mrakgr

Finally found it on the marketplace.

```
C:\Users\Marko\AppData\Roaming\npm\node_modules\vsce\out\package.js:136
    return (translations ?? [])
                          ^
```

I guess I need to update node. How do I do that?

https://www.freecodecamp.org/news/how-to-update-node-and-npm-to-the-latest-version/

Let me try `nvm install node`.

Nope. Let me just get the binaries. Right now I can't even use `vsce package` properly. I need it to turn the extension into a msix file that I could upload.

2:10pm. Is something happening in the terminal? I'll wait a few minus before doing anything like force aborting it.

2:15pm. 3 chapter of rebuild world are out. Sweet. Right now I do not know whether the terminal has encountered an error or if it is downloading something in the background. I might as well take a break that I could before.

...Oh, it finished. Ok, let me try packaging it again. Once it is uploaded I'll take a real break.

2:20pm. I need to wait for it to finish verifying. The last time I did this, it told me it was detecting a virus.

Oh, nice. It went through. Now let me update the readme.

///

Created the C backend for Spiral and updated the language to v2.2.0. I regret not doing this last year, so I decided to finally do it. Compared to the F#, or the Cython backend, the C one is not too useful because C does not have any worthwhile libraries to take advantage of. But it is going to serve a prototype for AI chip C backends, and I needed to do it in order to get a grasp on reference counting. I did pretty well at that. I have gone through the testing suite, but it isn't too thorough or designed to catch memory errors, so for the time being it might be worth putting the programs produced by it through [Cee Studio](https://www.cee.studio/). Consider it in beta right now. From here on out, the best kind of test would be to use it in the real world.

When I get some novel hardware it is going to be easy to adapt it to them. Until then, I won't bother using it for anything in particular.

///

Let me just go with this.

Let me commit here. It is time for that break. I did really well in the past week. Tomorrow, I will start taking job applications seriously. I'll make finding a job my job."

---
## [santoshmalyala/Devops](https://github.com/santoshmalyala/Devops)@[1b4f1508d3...](https://github.com/santoshmalyala/Devops/commit/1b4f1508d38f35a175d85411ba692872d5e20144)
#### Wednesday 2022-07-13 12:43:19 by santoshmalyala

Merge pull request #3 from santoshmalyala/Testing

Adding fuck you to line

---
## [deitch/linuxkit](https://github.com/deitch/linuxkit)@[860934d5d9...](https://github.com/deitch/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Wednesday 2022-07-13 14:01:13 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [ElectronicsArchiver/firmware](https://github.com/ElectronicsArchiver/firmware)@[d0a66b113c...](https://github.com/ElectronicsArchiver/firmware/commit/d0a66b113cdcf3d9e8ef3d0dc9d9a80cdc3e9625)
#### Wednesday 2022-07-13 14:05:11 by jascoproducts

Thursday mini-update

Due to the holiday weekend, we will not be issuing our usual Friday major update this week.

What was originally hoped to be tomorrow's major update should come to be our final batch of firmware uploaded by end-of-week next week. In the meantime, we are discussing what the future of this repository will look like since we have continued to enjoy this community-facing experience.

Enjoy this mini-update, however, if you are a user of:
	- Enbrighten-GE
		- ZW3004\14296 - In-Wall Smart Toggle Dimmer (Lt. Alm)

Other fixes:

2. Documented the existence of pre-6.51.06 SDK-developed firmware releases for some of our Jasco-branded products

3. Updated several readmes and repackaged into new .zip archives

---
## [JoshAdamPowell/tgstation](https://github.com/JoshAdamPowell/tgstation)@[92fda5014d...](https://github.com/JoshAdamPowell/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Wednesday 2022-07-13 14:35:46 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [harudagondi/bevy](https://github.com/harudagondi/bevy)@[4847f7e3ad...](https://github.com/harudagondi/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Wednesday 2022-07-13 15:16:45 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [FranzBusch/swift-protobuf](https://github.com/FranzBusch/swift-protobuf)@[af8b464a10...](https://github.com/FranzBusch/swift-protobuf/commit/af8b464a1073bb34111e6c1a4697fa479238fe78)
#### Wednesday 2022-07-13 16:06:24 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [newstools/2022-sunday-world](https://github.com/newstools/2022-sunday-world)@[f8c172159d...](https://github.com/newstools/2022-sunday-world/commit/f8c172159df3387bea7d99ff3155208992bdc6e3)
#### Wednesday 2022-07-13 17:28:34 by Billy Einkamerer

Created Text For URL [sundayworld.co.za/news/man-sent-to-jail-for-life-for-raping-his-girlfriends-grandchild/]

---
## [ranihorev/gate](https://github.com/ranihorev/gate)@[e2a108db75...](https://github.com/ranihorev/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Wednesday 2022-07-13 18:59:38 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [z3DD3r/android_kernel_lge_hammerhead](https://github.com/z3DD3r/android_kernel_lge_hammerhead)@[cfefee544d...](https://github.com/z3DD3r/android_kernel_lge_hammerhead/commit/cfefee544ddcfe9eb98fa54ecc4301578f5898f2)
#### Wednesday 2022-07-13 22:42:16 by z3DD3r

msm_thermal: simplified thermal driver

Thermal driver by franco.
This is a combination of 9 commits:

msm: thermal: add my simplified thermal driver.
Stock thermal-engine-hh goes crazy too soon and too often and offers no way for userland to tweak its parameters

Signed-off-by: franciscofranco <franciscofranco.1990@gmail.com>

msm: thermal: moar magic

Added a sample time between heat levels. The hotter it is, the longer
it should stay throttled in that same freq level therefore cooling this
down effectively.
Also due to this change freqs have been slightly adjusted.
Now the driver will start a bit earlier on boot.
Few cosmetic changes too because why the fuck not.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: reduce throttle point to 60C

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: rework previous patches

The changes on previous patches didn't really work out. Either the device
just reboots for infinity during boot because if it reaches high temperatures
and fails to throttle down fast enough to mitigate it, or it usually just
crashes the device while benchmarking on Geekbench or Antutu again because
when there's a big ass temp spike this doesn't mitigate fast enough.

These changes are confirmed working after testing in all scenarios previously
described.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: work faster with more thrust

Last commit was not enough, it mitigated most of the issues, but some users
were still having weird shits because temperature wasn't going down as fast
as it should. So now queue it every fucking 100ms in a dedicated high prio
workqueue. It's my last stance!

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: offline cpu2 and cpu3 if things get REALLY rough

Just for safe measure put cpu2 and cpu3 to sleep if the heat gets way bad.
Also the polling time gets back to default stock 250ms since the earlier 100ms
change was just a band-aid for a nastier bug that got fixed in the mean time.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm_thermal: send OFF/ONLINE uevent in hotplug cases

Send the correct uevent after setting a CPU core online or offline.
This allows ueventd to set correct SELinux labels for newly created
sysfs CPU device nodes.

Bug: 28887345
Change-Id: If31b8529b31de9544914e27514aca571039abb60
Signed-off-by: Siqi Lin <siqilin@google.com>
Signed-off-by: Thierry Strudel <tstrudel@google.com>
[Francisco: slightly adapted from Qcom's original patch to apply]
Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

Revert "msm_thermal: send OFF/ONLINE uevent in hotplug cases"

Crashes everything if during early early boot the device is hot
and starts to throttle. It's madness!

This reverts commit 80e38963f8080c3c9d26374693dd0f0a88f8060b.

msm: thermal: return to original simplified driver

Some users still had a weird issue that I was unable to reproduce which
either consisted in cpu2 and cpu3 getting stuck in offline mode or after
a gaming session while charging the device would crash with "hw_reset"
and then the device would loop in bootloader -> boot animation forever
until the device cooled down.

My test was leaving the device charging during the night, brightness close
to max and running Stability Test app with the CPU+GPU suite. I woke up
and the device was still running it flawlessly. Rebooted while hot and it
booted just fine.

Since I was unable to reproduce the issue and @osm0sis flashed back to <r92
and was unable to reproduce it anymore here we go back to that stage.

Only change I made compared to that original driver was simply queue things
into a dedicated high prio wq for faster thermal mitigation. Rest is unchanged.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[4704df506b...](https://github.com/CHOMPStation2/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Wednesday 2022-07-13 23:02:38 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [mnh48/guild.mnh48.moe](https://github.com/mnh48/guild.mnh48.moe)@[c279d47005...](https://github.com/mnh48/guild.mnh48.moe/commit/c279d470057ffd3d1c727ea58e1046061dae6e0b)
#### Wednesday 2022-07-13 23:17:08 by Yaya MNH48

updates all servers to current conditions, add translations
- Rumi Malay translations `ms` added for all server summary and section names
- Jawi Malay translations `ms-Arab` added for all server summary and section names
- renamed server `Global Transit and Infrastructure Central` to `Global Transit & Infrastructure Central`
- removed server `Disy's Hideout` as I'm no longer in the server
- change link for `HammerTime` in summary of server `HammerTime` from `https://hammertime.djdavid98.art/` to `https://hammertime.cyou/`
- renamed server `Blender` to `Blender Community`
- renamed server `Animekos | Ayako` to `Animekos | Anime ❀ Social ❀ Ayako`
- readded invite link for server `R. Danny` as the server is now available to public again (written in the bot help menu)
- change summary for server `R. Danny` to reflect recent changes
- renamed server `🔞Hentai Desu` to `🔞Hentai Desu🔞`
- removed server `ilysm` as the server itself had been deleted by Discord
- change summary for server `Akek Hunters` to reflect recent changes
- renamed server `LinusTechTips` to `Linus Tech Tips`
- renamed server `VTube Studio Headquarter` to `VTube Studio Headquarters`
- add missing exclamation marks in several proper names:
  - Project SEKAI: Colorful Stage! feat. Hatsune Miku
  - LoveLive! Sunshine!!
  - BanG Dream! Girls Band Party!
- renamed server `Project Sekai Colorful Stage! feat. Hatsune Miku` to `Project Sekai Colorful Stage!`
- added server `Project SEKAI Wiki (Miraheze)` as I joined it
- renamed server `/r/Otonokizaka unofficial server` to `/r/Otonokizaka`
- renamed server `BanG Dream! Girls Band Party` to `BanG Dream! Girls Band Party!`
- renamed server `BandoYay` to `BandoGumi!`
- all server icons updated to latest version (except those using daily commerational icons, as they're updated to the base non-commerational icon)
- changed server icon for `MyVTubers Community Server` from static to animated version
- multiple formatting edits:
  - added nogit parameter to `_data/html/footer.yml` for all languages
  - change in-file CSS in en/index.md from `ul[data-title]::before` to `.toc ul[data-title]::before`
- added paragraph disclosing that server-specific profile introduction will not be translated
- changed last update date to today (14 July 2022)
- translated `en/index.md` into Rumi Malay at `ms/index.md`
- transliterated `ms/index.md` into Jawi Malay at `ms-Arab/index.md`

---

