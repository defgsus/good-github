## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-18](docs/good-messages/2022/2022-05-18.md)


1,769,472 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,769,472 were push events containing 2,817,623 commit messages that amount to 199,832,348 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [SmiteWindows/rust-analyzer](https://github.com/SmiteWindows/rust-analyzer)@[1a5925dc84...](https://github.com/SmiteWindows/rust-analyzer/commit/1a5925dc84d0ef966023d6612147f93a0464174c)
#### Wednesday 2022-05-18 00:00:13 by bors

Auto merge of #12294 - listochkin:prettier, r=Veykril

Switch to Prettier for TypeScript Code formatting

## Summary of changes:

 1. Added [`.editorconfig` file](https://editorconfig.org) to dictate general hygienic stuff like character encoding, no trailing whitespace, new line symbols etc. for all files (e.g. Markdown). Install an editor plugin to get this rudimentary formatting assistance automatically. Prettier can read this file and, for example, use it for indentation style and size.
 2. Added a minimal prettier config file. All options are default except line width, which per [Veykril](https://github.com/Veykril) suggestion is set to 100 instead of 80, because [that's what `Rustfmt` uses](https://rust-lang.github.io/rustfmt/?version=v1.4.38&search=#max_width).
 3. Change `package.json` to use Prettier instead of `tsfmt` for code formatting.
 4. Performed initial formatting in a separate commit, per [bjorn3](https://github.com/bjorn3) suggestion added its hash to a `.git-blame-ignore-revs` file. For it to work you need to add a configuration to your git installation:
    ```Shell
    git config --global blame.ignoreRevsFile .git-blame-ignore-revs
    ```
 5. Finally, removed `typescript-formatter` from the list of dependencies.

----
What follows below is summary of the discussion we had on Zulip about the formatter switch:

## Background

For the context, there are three reasons why we went with `tsfmt` originally:
* stick to vscode default/built-in
* don't add extra deps to package.json.lock
* follow upstream (language server node I think still uses `tsfmt`)

And the meta reason here was that we didn't have anyone familiar with frontend, so went for the simplest option, at the expense of features and convenience.

Meanwhile, [**Prettier**](https://prettier.io) became a formatter project that JS community consolidated on a few years ago. It's similar to `go fmt` / `cargo fmt` in spirit: minimal to no configuration to promote general uniformity in the ecosystem. There are some options, that were needed early on to make sure the project gained momentum, but by no means it's a customizable formatter that is easy to adjust to reduce the number of changes for adoption.

## Overview of changes performed by Prettier

Some of the changes are acceptable. Prettier dictates a unified string quoting style, and as a result half of our imports at the top are changed. No one would mind that. Some one-line changes are due to string quotes, too, and although these a re numerous, the surrounding lines aren't changed, and git blame / GitLens will still show relevant context.

Some are toss ups. `trailingComma` option - set it to `none`, and get a bunch of meaningless changes in half of the code. set it to `all` and get a bunch of changes in the other half of the code. Same with using parentheses around single parameters in arrow functions: `x => x + 1` vs `(x) => x + 1`. Perrier forces one style or the other, but we use both in our code.

Like I said, the changes above are Ok - they take a single line, don't disrupt GitLens / git blame much. **The big one is line width**. Prettier wants you to choose one and stick to it. The default is 80 and it forces some reformatting to squish deeply nested code or long function type declarations. If I set it to 100-120, then Prettier finds other parts of code where a multi-line expression can be smashed into a single long line. The problem is that in both cases some of the lines that get changed are interesting, they contain somewhat non-trivial logic, and if I were to work on them in future I would love to see the commit annotations that tell me something relevant. Alas, we use some of that.

## Project impact

Though Prettier is a mainstream JS project it has no dependencies. We add another package so that it and ESLint work together nicely, and that's it.

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[b42b4bcbc6...](https://github.com/mbs-octoml/mbs-tvm/commit/b42b4bcbc6ad111902b34973365d9bb301caa06d)
#### Wednesday 2022-05-18 00:04:20 by Mark Shields

** Collage v2 sketch ***

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
## [francinum/Pariah-Station](https://github.com/francinum/Pariah-Station)@[95db2c6bfc...](https://github.com/francinum/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Wednesday 2022-05-18 00:08:22 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [ViceRabbit/MCModpack-Isha-Reforged](https://github.com/ViceRabbit/MCModpack-Isha-Reforged)@[6132a17b67...](https://github.com/ViceRabbit/MCModpack-Isha-Reforged/commit/6132a17b67bc94e89e397d68077521a8fe2c141a)
#### Wednesday 2022-05-18 00:38:51 by ViceRabbit

first announcement

 17/5/2022,
- **New Github Repo!** Vice is responsible for this repo which you should redirect questions to him regarding this.
- Every update a date will be included; this is to easily track each **update**.
- Only **minor updates** would be frequenctly updated here - major updates will be announced in discord so dw you lazy bitches
- yes i fucking know i wrote the date as x\x\x instead of x/x/x, thats due to github being ass with dates.

# I will be looking forward to the potential of this modpack! Further minor updates will be having new repos in the /main/Update-Tracker page and an interrogration will be announcing everything in discord! ^_^

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[d411393e72...](https://github.com/jlsnow301/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Wednesday 2022-05-18 00:52:20 by Zytolg

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[4652d4bb63...](https://github.com/jlsnow301/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Wednesday 2022-05-18 00:52:20 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [sourceruckus/linux-mdl](https://github.com/sourceruckus/linux-mdl)@[9709c8b5cd...](https://github.com/sourceruckus/linux-mdl/commit/9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5)
#### Wednesday 2022-05-18 01:26:34 by Linus Torvalds

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
## [DrtSinX98/android_kernel_realme_mt6781](https://github.com/DrtSinX98/android_kernel_realme_mt6781)@[90d6314705...](https://github.com/DrtSinX98/android_kernel_realme_mt6781/commit/90d631470525c740dcd95f24e6714071ac2437f8)
#### Wednesday 2022-05-18 02:45:01 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: DrtSinX98 <pritish@stag-os.org>

---
## [atkins126/guava](https://github.com/atkins126/guava)@[e015172847...](https://github.com/atkins126/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Wednesday 2022-05-18 03:53:13 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[b86cf89125...](https://github.com/necromanceranne/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Wednesday 2022-05-18 04:33:55 by Aleksej Komarov

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
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[46200d89ae...](https://github.com/cyberitsolutions/bootstrap2020/commit/46200d89aee3f4cdd5e761ca80e9bb2b50f9a3ba)
#### Wednesday 2022-05-18 06:27:32 by Trent W. Buck

dvdrip: remove needless timestamp

16:13 <twb> self.dvd_title = f'{self.dvd_title or "Unknown"} {datetime.datetime.today()}'
16:13 <twb> That should be date.today(), but I want to remove it completely
16:13 <twb> the tvserver adds another timestamp, so I don't think it's needed
16:14 <twb> REDACTED: any opinion?
16:14 <REDACTED> Hmmm, I think the timestamp should be added as soon as possible to avoid 2 rip jobs trampling on each other
16:14 <twb> REDACTED: it's already using temp dirs.
16:15 <twb> It just means that if two staff have the *same* disc, and try to rip *both* discs on the same day, the second one will go "oh, it already exists in the .ripped queue" and (now) cleanup after itself
16:16 <REDACTED> If we're reliably handling errors, then yeah fine, it can go, I think. Because realistically they'll be the same regardless of date ripped. But make sure you're not overwriting things without checking
16:16 <twb> Whereas what happens at AMC is they end up re-rippign the same dvd 11 fuckign times
16:16 <REDACTED> Ok, cleanup itself is the important part
16:16 <twb> Yeah
16:16 <twb> Anyway the desktop side of this I'll check today incidentally as part of this

---
## [QueIvan/library-manager](https://github.com/QueIvan/library-manager)@[2d63379131...](https://github.com/QueIvan/library-manager/commit/2d63379131bea06f13d90d40aa133cde850969f5)
#### Wednesday 2022-05-18 06:47:41 by Jan Szewczyk

Merge pull request #11 from QueIvan/dev

Full blown refactor (FUCK YOU CEZIK)

---
## [BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER)@[4233041c30...](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/commit/4233041c30ecbd335e5c03d8f529d260e396b4a3)
#### Wednesday 2022-05-18 07:27:39 by 1212-5858

[Read MOV distribution continues beyond earlier requests of non-consent](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/9)

Read MOV distribution continues beyond earlier requests of non-consent

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/9
-- i lost his number on my other phone... i think my GF stole it to be honest...

these TORTS and Violations of Privacy also are a BREACH OF CONTRACT.'
/// so please get this to WInans & CO.
---https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1
## peeped me THROUGH the door?
---# https://user-images.githubusercontent.com/70865813/153544431-27d6b33b-d34a-4e37-9532-aad92b15264c.png


STATE FARM INVESTMENT MANAGEMENT
SECURITY SYMBOL 3487
04-12-2022
TERRENCE MICHAEL LUDWIG
2004555
STATE FARM VP MANAGEMENT CORP 43036
FAILURE TO DISCLOSE.
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/%5BSTATE%20FARM%20VP%2043036%5D%20$3231040-2004555.pdf

\
COLUMBIA.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png

CRC.
https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png
\
ZUCKER.
- WILSON & DICKER
https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/7
\
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==

RE: STATE FARM ASSOCIATES’ FUNDS TRUST
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==


STATE FARM ASSOCIATES’ FUNDS TRUST 1
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf


### EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION
*** A VIOLATION OF PRIVACY AND A BREACH OF THE LAW AND CONTRACT.
![image](https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png)

--- 
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00) Monrovia, Reykjavik.
To: PS Investigation
Subject: see also : camera NOT POINTED AT A WINDOW docket 49 + SHANKING THE PORTER you missed.
Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

![168761279-17e64f23-4613-49b2-8704-123e68425e5c](https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png)


![168761716-5f9b1aed-fef9-4ec2-9d90-3fa22bc69bc3](https://user-images.githubusercontent.com/70865813/168770555-25ef68a8-5bb3-42e6-a28a-c35b60cd9b0b.png)


#### READ TIMESTAMPS

[ https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2 ](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2)

[MSG BOX 1: VIOLATION OF PRIVACY - DISTRIBUTION WITHOUT CONSENT](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68)

[MSG BOX 2: § 11 440 Tampering with or fabricating physical evidence](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/0d69023191f5a8a25006caf258a50b649da83aa0)

[MSG BOX 3: The Zuckers are protected by these individuals](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/4/files)


## ECONOMIC BENEFITS
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==)

#### HIRED A sub-par ON-DEMAN VIDEO SPECIALIST.
**** ps what the heck is Pod-Cast?
**** did NOT know I had one of those either.
@rosaliachann
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==]
(https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)


p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or any of these people who documented me every day.[nov13 and Dec18 2021 - multiple dwelling laws.pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706680/nov13.and.Dec18.2021.-.multiple.dwelling.laws.pdf)
[(PS-Investigation@facil.columbia.edu)(crcmessages@ftc.gov).pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706682/PS-Investigation%40facil.columbia.edu.crcmessages%40ftc.gov.pdf)



https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/upload/CRC-REYYKJAVIK-MONROVIA

[Not read MOV distribution continues beyond earlier requests of non-consent](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/7)

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5


--
THESE PERVERT UPLOADED THE VIDEOS THEMSELVES.... AND EMAILED THEM AMONGS EACH OTHER...
https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2





A very expensive decision... by a professional team of 900 + 1 Laskowitz?

    **** non-joinder... no wonder....

    **** https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5

  **** 

https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003

>> https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Xjn0/e1NcBADqRc_PLUS_g11P4g==

https://www.sec.gov/Archives/edgar/data/1516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml



[ALL VIDEOS  - UNRETURNED AS OF CURRENT    SEE ALSO DOCKET 008](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

008 - ROSALIA CHANN AND ALEXIS BRANDON
2020 07 26 - WINDOW NOT REPAIRED   CAMERA IS WORKING  ON 2020 08 07 DOCKET 300
2022 02 04 --- FRIDAY  --- CONFIRMATIONS
2022 02 06 --- SUNDAY --- CONFIRMATIONS
CAMERA HAS NOT BEEN REMOVED - ENTERED IN THE DESCRIPTION OF THESE EXHIBITS - REYNOSO - TECHMANN  VENTILATOR  FOUND A  MOV FILE

CHECK LINKS

510-682 -9510  -- THIS ONE... 
NOTARIZED AN AFFIDAVIT IN ALAMEDA, CALIFORNIA AFTER MOVING OUT OF 111 SULLIVAN STREET, ALLEGEDLY...
 AND HER MOTHER ANNEXED A COMPLAINT THAT  I WAS BOTHERING HER DAUGHTER... 
I NEVER MET THESE B****S 
- I DON'T EVEN KNOW IF SHES A REAL PERSON, BUT THEY ANNEXED THAT SHE HAD TO MOVE OUT...


[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==)




https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==

[Read  FW  ATTACHED    NOT IN DISNEYLAND -- AND NOT ON MY WATCH  -- -- -- SORRY  (155)](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/7)

https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf

510  682   9510

Andrew Reynoso <AREYNOSO@MSKYLINE.COM>
Tom Eschmann <TESCHMAN@MSKYLINE.COM>
Joseph Giamboi <JGiamboi@mskyline.com>;
MONDAY APRIL 13TH
Laurie Zucker <LZucker@mskyline.com>
Edward Devine <EDevine@mskyline.com>
Laurie Zucker <LZucker@mskyline.com>


MG Messer <mgMESSER@GMAIL.COM>
"Miwa Messer
111 Sullivan #3AR"

Paul Regan <Legal@mskyline.com>


MG Messer <rngrnessei Pgnrail.corn>
Miwa Messer


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/8de5f89e10d3ec11a7b5002248286421/CE48526B-6A0E-4B2A-89B9-93BD202498A9.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/a463845010d3ec11a7b5000d3a1326fe/0F6C27D5-69BD-4971-91F6-A5A40317CC63.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/5380dd8997d3ec11a7b5000d3a132789/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/3bb9011795d3ec11a7b5000d3a132789/153974-2020.Docket399.FTC.StateFarmRealtyInsuranceLLC.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/ff91792a95d3ec11a7b50022482864f0/[sfVP43036]%20$2876793%20-%20david.moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/[STATE%20FARM%20VP%2043036]%20$3231040-2004555.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/[sfVP%2043036]%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/%5BsfVP%2043036%5D%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==





https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==


https://portal.311.nyc.gov/sr-details/?id=4296b0c3-c4a2-ec11-826d-0003ff86900c


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


            PROPERTY 1:     111 SULLIVAN STREET REAR, NEW YORK, NY, 10012     
							IS WHERE I RESIDED.
            PROPERTY 2:     117 SULLIVAN STREET, NEW YORK, NY, 10012	
							WAS ALSO TRANSFERRED TO STATE FARM.


\
STATE FARM INVESTMENT MANAGEMENT
SECURITY SYMBOL 3487
04-12-2022
TERRENCE MICHAEL LUDWIG
2004555
STATE FARM VP MANAGEMENT CORP 43036
FAILURE TO DISCLOSE.
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/%5BSTATE%20FARM%20VP%2043036%5D%20$3231040-2004555.pdf

\
COLUMBIA.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png
\
CRC.
https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png
\
ZUCKER.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==
\
RE: STATE FARM ASSOCIATES’ FUNDS TRUST
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

\
STATE FARM ASSOCIATES’ FUNDS TRUST 1
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf
\
### EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION
*** A VIOLATION OF PRIVACY AND A BREACH OF THE LAW AND CONTRACT.
![image](https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png)

--- 
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00) Monrovia, Reykjavik.
To: PS Investigation
Subject: see also : camera NOT POINTED AT A WINDOW docket 49 + SHANKING THE PORTER you missed.
Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

![168761279-17e64f23-4613-49b2-8704-123e68425e5c](https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png)


![168761716-5f9b1aed-fef9-4ec2-9d90-3fa22bc69bc3](https://user-images.githubusercontent.com/70865813/168770555-25ef68a8-5bb3-42e6-a28a-c35b60cd9b0b.png)


#### READ TIMESTAMPS

[ https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2 ](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2)

[MSG BOX 1: VIOLATION OF PRIVACY - DISTRIBUTION WITHOUT CONSENT](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68)

[MSG BOX 2: § 11 440 Tampering with or fabricating physical evidence](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/0d69023191f5a8a25006caf258a50b649da83aa0)

[MSG BOX 3: The Zuckers are protected by these individuals](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/4/files)


## ECONOMIC BENEFITS
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==)

#### HIRED A sub-par ON-DEMAN VIDEO SPECIALIST.
**** ps what the heck is Pod-Cast?
**** did NOT know I had one of those either.
@rosaliachann
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==]
(https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)


p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or any of these people who documented me every day.[nov13 and Dec18 2021 - multiple dwelling laws.pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706680/nov13.and.Dec18.2021.-.multiple.dwelling.laws.pdf)
[(PS-Investigation@facil.columbia.edu)(crcmessages@ftc.gov).pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706682/PS-Investigation%40facil.columbia.edu.crcmessages%40ftc.gov.pdf)

---
## [LineageOS/android_kernel_oneplus_msm8998](https://github.com/LineageOS/android_kernel_oneplus_msm8998)@[91a9e91029...](https://github.com/LineageOS/android_kernel_oneplus_msm8998/commit/91a9e91029ffc61fce24204c43e5d27e7e382b07)
#### Wednesday 2022-05-18 07:52:52 by Maciej Żenczykowski

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
## [6moon-fcc/new-repo](https://github.com/6moon-fcc/new-repo)@[13d64cfc57...](https://github.com/6moon-fcc/new-repo/commit/13d64cfc575fe7ddcb048f85f749c335ce8ef715)
#### Wednesday 2022-05-18 08:22:28 by Konstantin Shevchenko

added style.css and changed some code idk fuck you

---
## [BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER)@[f1e1a8ee7f...](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/commit/f1e1a8ee7fbaa061866a713cf8045d08e2c44152)
#### Wednesday 2022-05-18 08:47:19 by 1212-5858

https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png

columbia-wilson-zucker-and-dicker A FUNNY FARM - where they belong.
these TORTS and Violations of Privacy also are a BREACH OF CONTRACT.'

---# #11

---# https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/upload/BBOY-EPIC-SONY
/// so please get this to WInans & CO.
/ i lost the thing he made me sign earlier, AND MY PHONE... i did tell him NOT to move to Jersey though.. 
they have plenty of studios in Manhattan, even cheaper in Brooklyn - PLus. the food is better.



---https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1
## peeped me THROUGH the door?
---# https://user-images.githubusercontent.com/70865813/153544431-27d6b33b-d34a-4e37-9532-aad92b15264c.png

##
they distributed them without CONSENT - written or oral.
- and you know.
[BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#6

# there is no price tag for me. especially when they are positioned like THAT,
[https://user-images.githubusercontent.com/70865813/154165664-8ee2ea3f-b933-4d20-9224-c70e54b0b882.png](https://user-images.githubusercontent.com/70865813/154165664-8ee2ea3f-b933-4d20-9224-c70e54b0b882.png)


[video on-demand](BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#8 (comment))
///


STATE FARM INVESTMENT MANAGEMENT
SECURITY SYMBOL 3487
04-12-2022
TERRENCE MICHAEL LUDWIG
2004555
STATE FARM VP MANAGEMENT CORP 43036
FAILURE TO DISCLOSE.
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/%5BSTATE%20FARM%20VP%2043036%5D%20$3231040-2004555.pdf

\
COLUMBIA.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png

CRC.
https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png
\
ZUCKER.
- WILSON & DICKER
BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#7
\
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==

RE: STATE FARM ASSOCIATES’ FUNDS TRUST
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==


STATE FARM ASSOCIATES’ FUNDS TRUST 1
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf


### EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION
*** A VIOLATION OF PRIVACY AND A BREACH OF THE LAW AND CONTRACT.
![image](https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png)

--- 
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00) Monrovia, Reykjavik.
To: PS Investigation
Subject: see also : camera NOT POINTED AT A WINDOW docket 49 + SHANKING THE PORTER you missed.
Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

![168761279-17e64f23-4613-49b2-8704-123e68425e5c](https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png)


![168761716-5f9b1aed-fef9-4ec2-9d90-3fa22bc69bc3](https://user-images.githubusercontent.com/70865813/168770555-25ef68a8-5bb3-42e6-a28a-c35b60cd9b0b.png)


#### READ TIMESTAMPS

[ #2 ](#2)

[MSG BOX 1: VIOLATION OF PRIVACY - DISTRIBUTION WITHOUT CONSENT](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68)

[MSG BOX 2: § 11 440 Tampering with or fabricating physical evidence](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/0d69023191f5a8a25006caf258a50b649da83aa0)

[MSG BOX 3: The Zuckers are protected by these individuals](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/4/files)


## ECONOMIC BENEFITS
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==)

#### HIRED A sub-par ON-DEMAN VIDEO SPECIALIST.
**** ps what the heck is Pod-Cast?
**** did NOT know I had one of those either.
@rosaliachann
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==]
(https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)


p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or any of these people who documented me every day.[nov13 and Dec18 2021 - multiple dwelling laws.pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706680/nov13.and.Dec18.2021.-.multiple.dwelling.laws.pdf)
[(PS-Investigation@facil.columbia.edu)(crcmessages@ftc.gov).pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706682/PS-Investigation%40facil.columbia.edu.crcmessages%40ftc.gov.pdf)



https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/upload/CRC-REYYKJAVIK-MONROVIA

[Not read MOV distribution continues beyond earlier requests of non-consent](BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#7)

BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#5


--
THESE PERVERT UPLOADED THE VIDEOS THEMSELVES.... AND EMAILED THEM AMONGS EACH OTHER...
#2





A very expensive decision... by a professional team of 900 + 1 Laskowitz?

    **** non-joinder... no wonder....

    **** BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#5

  **** 

https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003

>> https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Xjn0/e1NcBADqRc_PLUS_g11P4g==

https://www.sec.gov/Archives/edgar/data/1516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml



[ALL VIDEOS  - UNRETURNED AS OF CURRENT    SEE ALSO DOCKET 008](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

008 - ROSALIA CHANN AND ALEXIS BRANDON
2020 07 26 - WINDOW NOT REPAIRED   CAMERA IS WORKING  ON 2020 08 07 DOCKET 300
2022 02 04 --- FRIDAY  --- CONFIRMATIONS
2022 02 06 --- SUNDAY --- CONFIRMATIONS
CAMERA HAS NOT BEEN REMOVED - ENTERED IN THE DESCRIPTION OF THESE EXHIBITS - REYNOSO - TECHMANN  VENTILATOR  FOUND A  MOV FILE

CHECK LINKS

510-682 -9510  -- THIS ONE... 
NOTARIZED AN AFFIDAVIT IN ALAMEDA, CALIFORNIA AFTER MOVING OUT OF 111 SULLIVAN STREET, ALLEGEDLY...
 AND HER MOTHER ANNEXED A COMPLAINT THAT  I WAS BOTHERING HER DAUGHTER... 
I NEVER MET THESE B****S 
- I DON'T EVEN KNOW IF SHES A REAL PERSON, BUT THEY ANNEXED THAT SHE HAD TO MOVE OUT...


[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==)




https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==

[Read  FW  ATTACHED    NOT IN DISNEYLAND -- AND NOT ON MY WATCH  -- -- -- SORRY  (155)](BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER#7)

https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf

510  682   9510

Andrew Reynoso <AREYNOSO@MSKYLINE.COM>
Tom Eschmann <TESCHMAN@MSKYLINE.COM>
Joseph Giamboi <JGiamboi@mskyline.com>;
MONDAY APRIL 13TH
Laurie Zucker <LZucker@mskyline.com>
Edward Devine <EDevine@mskyline.com>
Laurie Zucker <LZucker@mskyline.com>


MG Messer <mgMESSER@GMAIL.COM>
"Miwa Messer
111 Sullivan #3AR"

Paul Regan <Legal@mskyline.com>


MG Messer <rngrnessei Pgnrail.corn>
Miwa Messer


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/8de5f89e10d3ec11a7b5002248286421/CE48526B-6A0E-4B2A-89B9-93BD202498A9.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/a463845010d3ec11a7b5000d3a1326fe/0F6C27D5-69BD-4971-91F6-A5A40317CC63.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/5380dd8997d3ec11a7b5000d3a132789/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/3bb9011795d3ec11a7b5000d3a132789/153974-2020.Docket399.FTC.StateFarmRealtyInsuranceLLC.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/ff91792a95d3ec11a7b50022482864f0/[sfVP43036]%20$2876793%20-%20david.moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/[STATE%20FARM%20VP%2043036]%20$3231040-2004555.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/[sfVP%2043036]%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/%5BsfVP%2043036%5D%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==





https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==


https://portal.311.nyc.gov/sr-details/?id=4296b0c3-c4a2-ec11-826d-0003ff86900c


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


            PROPERTY 1:     111 SULLIVAN STREET REAR, NEW YORK, NY, 10012     
							IS WHERE I RESIDED.
            PROPERTY 2:     117 SULLIVAN STREET, NEW YORK, NY, 10012	
							WAS ALSO TRANSFERRED TO STATE FARM.


\
STATE FARM INVESTMENT MANAGEMENT
SECURITY SYMBOL 3487
04-12-2022
TERRENCE MICHAEL LUDWIG
2004555
STATE FARM VP MANAGEMENT CORP 43036
FAILURE TO DISCLOSE.
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/%5BSTATE%20FARM%20VP%2043036%5D%20$3231040-2004555.pdf

\
COLUMBIA.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png
\
CRC.
https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png
\
ZUCKER.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==
\
RE: STATE FARM ASSOCIATES’ FUNDS TRUST
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

\
STATE FARM ASSOCIATES’ FUNDS TRUST 1
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf
\
### EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION
*** A VIOLATION OF PRIVACY AND A BREACH OF THE LAW AND CONTRACT.
![image](https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png)

--- 
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00) Monrovia, Reykjavik.
To: PS Investigation
Subject: see also : camera NOT POINTED AT A WINDOW docket 49 + SHANKING THE PORTER you missed.
Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

![168761279-17e64f23-4613-49b2-8704-123e68425e5c](https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png)


![168761716-5f9b1aed-fef9-4ec2-9d90-3fa22bc69bc3](https://user-images.githubusercontent.com/70865813/168770555-25ef68a8-5bb3-42e6-a28a-c35b60cd9b0b.png)


#### READ TIMESTAMPS

[ #2 ](#2)

[MSG BOX 1: VIOLATION OF PRIVACY - DISTRIBUTION WITHOUT CONSENT](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68)

[MSG BOX 2: § 11 440 Tampering with or fabricating physical evidence](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/0d69023191f5a8a25006caf258a50b649da83aa0)

[MSG BOX 3: The Zuckers are protected by these individuals](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/4/files)


## ECONOMIC BENEFITS
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==)

#### HIRED A sub-par ON-DEMAN VIDEO SPECIALIST.
**** ps what the heck is Pod-Cast?
**** did NOT know I had one of those either.
@rosaliachann
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==]
(https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)


p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or any of these people who documented me every day.[nov13 and Dec18 2021 - multiple dwelling laws.pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706680/nov13.and.Dec18.2021.-.multiple.dwelling.laws.pdf)
[(PS-Investigation@facil.columbia.edu)(crcmessages@ftc.gov).pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706682/PS-Investigation%40facil.columbia.edu.crcmessages%40ftc.gov.pdf)
 BSCPGROUPHOLDINGSLLC-patch-1 (#7)

---
## [LeartS/odoo](https://github.com/LeartS/odoo)@[cbc9279eaa...](https://github.com/LeartS/odoo/commit/cbc9279eaa169e65aeb2dab6dd36e3ffab4e481e)
#### Wednesday 2022-05-18 09:01:25 by Odoo's Mergebot

[MERGE] im_livechat: introduce chatbot scripts

PURPOSE

This commit introduces a chatbot operator that works based on a user-defined
script with various steps.

SPECS

A im_livechat.chatbot.script can be defined on a livechat rule.
When a end-user reaches a website page that matches the rule, the chat window
opens and the script of the bot starts iterating through its steps.

The chatbot code is currently directly integrated with the existing livechat
Javascript code.
It defines extra conditions and layout elements to be able to automate the
conversation and register user answers.

AVAILABLE STEPS

A script is defined with several steps that can currently be one of the
following types:

"text"

A simple text step where the bot posts a message without expecting an answer
e.g: "Hello! I'm a friendly robot!"

"question_selection"

The bot will ask a question and suggest answers, the end-user will have to
click on the answer he chooses
e.g: "How can I help you?
  -> Create a Ticket
  -> Create a Lead
  -> Speak with a human"

"question_email"

That step will ask the end user's email address (and validate it)
The result is saved on the linked im_livechat.im_livechatchatbot.mail.message

"question_phone"

Same logic as the 'question_email' for a phone number
We don't validate the input this time as it's a complicated process
(requires country, ...)

"forward_operator"

Special type of step that will add a human operator to the conversation when
reached, which stops the script and allow the visitor to discuss with a
real person.

The operator will be chosen among the available operators on the
livechat.channel.

If there is no operator available, the script continues normally which allows
to automate an "answering machine" that will redirect the user in case no
operator is available.

e.g: "I'm sorry, no operator is available right now, please contact us by email
at 'info@company.com', we will try to respond as soon as possible!".
(Or even something more complex with multiple questions / paths).

"free_input_single"

Will ask the visitor for a single line of text.
This text is not saved anywhere else than in the conversation, but it's still
useful when combined with steps that create leads / tickets since those print
the whole conversation into the description.

"free_input_multi"

Same as "free_input_single" but lets the user input multiple lines of text.
The frontend implementation is made by waiting a few seconds (currently 10) for
either the next submitted message or the next character typed into the input.

This lets visitors explain their issue / question with multiple messages.
Which is very useful since new messages are sent every time you press "Enter".

"create_lead"

Special step_type that allows creating a crm.lead when reaching it.
Usually used in addition to 'question_email' and 'question_phone' to create
interesting leads.

LINKS

Task-2030386

closes odoo/odoo#84000

Related: odoo/enterprise#24894
Signed-off-by: Thibault Delavallee (tde) <tde@openerp.com>
Co-authored-by: Patrick Hoste <pko@odoo.com>
Co-authored-by: Aurélien Warnon <awa@odoo.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2a94a63428...](https://github.com/treckstar/yolo-octo-hipster/commit/2a94a63428db73c766fcc68c71fac7992d82a59e)
#### Wednesday 2022-05-18 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [anditto/bitcoin](https://github.com/anditto/bitcoin)@[619f8a27ad...](https://github.com/anditto/bitcoin/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Wednesday 2022-05-18 09:35:51 by MarcoFalke

Merge bitcoin/bitcoin#24304: [kernel 0/n] Introduce `bitcoin-chainstate`

2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 ci: Build bitcoin-chainstate (Carl Dong)
095aa6ca37bf0bd5c5e221bab779978a99b2a34c build: Add example bitcoin-chainstate executable (Carl Dong)

Pull request description:

  Part of: #24303

  This PR introduces an example/demo `bitcoin-chainstate` executable using said library which can print out information about a datadir and take in new blocks on stdin.

  Please read the commit messages for more details.

  -----

  #### You may ask: WTF?! Why is `index/*.cpp`, etc. being linked in?

  This PR is meant only to capture the state of dependencies in our consensus engine as of right now. There are many things to decouple from consensus, which will be done in subsequent PRs. Listing the files out right now in `bitcoin_chainstate_SOURCES` is purely to give us a clear picture of the task at hand, it is **not** to say that these dependencies _belongs_ there in any way.

  ### TODO

  1. Clean up `bitcoin-chainstate.cpp`
     It is quite ugly, with a lot of comments I've left for myself, I should clean it up to the best of my abilities (the ugliness of our init/shutdown might be the upper bound on cleanliness here...)

ACKs for top commit:
  ajtowns:
    ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0
  ryanofsky:
    Code review ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0. Just rebase, comments, formatting change since last review
  MarcoFalke:
    re-ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 🏔

Tree-SHA512: 86e7fb5718caa577df8abc8288c754f4a590650d974df9d2f6476c87ed25c70f923c4db651c6963f33498fc7a3a31f6692b9a75cbc996bf4888c5dac2f34a13b

---
## [brando-soen/CodeWars](https://github.com/brando-soen/CodeWars)@[60b4bd53b1...](https://github.com/brando-soen/CodeWars/commit/60b4bd53b182b8f93280ef71a36c263b05bc2a8a)
#### Wednesday 2022-05-18 10:08:37 by brando-soen

I love you, a little , a lot, 

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

---
## [rohittembhurne2194/Desaiganj_ICTSBM_CMS](https://github.com/rohittembhurne2194/Desaiganj_ICTSBM_CMS)@[97a575f772...](https://github.com/rohittembhurne2194/Desaiganj_ICTSBM_CMS/commit/97a575f7721732b7b43dafbb554d57d56eefb268)
#### Wednesday 2022-05-18 10:33:30 by umeshl@appynitty.com

Chnages done From my side its umesh aka peaceMinded the future Millionaire persone and i will be definietly successful in this yeat in trading god is with me alwayas thanku god ji the higer energy sorry for any mistake god blessed me har har mahadev jai shree ram

---
## [LoveSkye/free-programming-books](https://github.com/LoveSkye/free-programming-books)@[97016edd67...](https://github.com/LoveSkye/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Wednesday 2022-05-18 10:34:48 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [fizteh95/Athena](https://github.com/fizteh95/Athena)@[29264fc45e...](https://github.com/fizteh95/Athena/commit/29264fc45eab7a53b607ce99adf36ca5a25dffe9)
#### Wednesday 2022-05-18 10:37:05 by kutish

hoooly shit, fucking linter, i fucking hate you sooo much; linter fixes

---
## [robn/mujmap](https://github.com/robn/mujmap)@[b961b9032e...](https://github.com/robn/mujmap/commit/b961b9032e024c84044d8667ff8dbf47a45d70e6)
#### Wednesday 2022-05-18 11:35:42 by Eliza Velasquez

Add troubleshooting section with auth guide

Also adds more warnings to the "migration" section, as I am becoming
increasingly paranoid that someone might behave like me and recklessly
try to migrate without doing the proper precautions, destroying their
notmuch database they spent hours working on (which in my case was not
because of mujmap, but because I tried to switch protonmail IMAP
clients, which was a horrible idea to do without backing up that I
immediately regretted)

---
## [ipluxteamx/FNF-GhostedEngine](https://github.com/ipluxteamx/FNF-GhostedEngine)@[cb4339bb43...](https://github.com/ipluxteamx/FNF-GhostedEngine/commit/cb4339bb43f2d6701d77a885836d391a4237a996)
#### Wednesday 2022-05-18 12:17:04 by iplux

fix memory leak + fuck you haxeflixel splash is staying on we ly haxeflixel

---
## [GarimaJai/Heartdisease_DecisionTree](https://github.com/GarimaJai/Heartdisease_DecisionTree)@[e1033cad5f...](https://github.com/GarimaJai/Heartdisease_DecisionTree/commit/e1033cad5fde3346c4019ea5dffa8c8bebb8448d)
#### Wednesday 2022-05-18 14:27:07 by GarimaJai

Update README.md

Heart Disease Case Study
Objective : Predict the presence of heart disease in a pateint.

Data contain a binary outcome HD for 454 patients who presented with chest pain. An outcome value of Yes indicates the presence of heart disease based on an angiographic test, while No means no heart disease

There are 13 predictors including Age, Sex, Chol (a cholesterol measurement), and other heart and lung function measurements

In the data, some of the predictors, such as Sex, Thal (Thallium stress test), and ChestPain, are qualitative

Data Source-UCI Machine Learning Repository

Data Description

(age)-> age in years
(sex)-sex (1 = male; 0 = female)
(chestPain)
-- Value 1: typical angina
-- Value 2: atypical angina
-- Value 3: non-anginal pain
-- Value 4: asymptomatic

(RestBP)->resting blood pressure (in mm Hg on admission to the hospital)
(chol)->serum cholestoral in mg/dl
(fbs)->(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
(restecg)->resting electrocardiographic results
-- Value 0: normal
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

(MaxHR)->maximum heart rate achieved
(exang)->exercise induced angina (1 = yes; 0 = no)
(oldpeak)->ST depression induced by exercise relative to rest
(slope)->the slope of the peak exercise ST segment
-- Value 1: upsloping
-- Value 2: flat
-- Value 3: downsloping

(ca)->number of major vessels (0-3) colored by flourosopy
(thal)->3 = normal; 6 = fixed defect; 7 = reversable defect
(AHD) (the predicted attribute) ->diagnosis of heart disease (angiographic disease status) Yes/No

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2f9f3fc19b...](https://github.com/mrakgr/The-Spiral-Language/commit/2f9f3fc19b8014e9e5a964e22f8ebc86694a6768)
#### Wednesday 2022-05-18 14:59:20 by Marko Grdinić

"9:25am. I am up, but I am hesitating a bit. I've been very focused on the subject of how to draw folds. I am not going to go with the plan from yesterday. Rather I am going to lower the size of the pen to the minimum and see where that gets me. I do want to go with the painterly approach, just not all the way with it. The style is very beatiful when it works well. I just need to upgrade my skills with it.

Right now let me read Frieren.

10:05am. Let me start. Let me check out the Moi thread.

10:10am. Oh it seems the boolean difference leaves some planes that I've missed. Let me try it out. After that I'll get back to CSP.

10:15am. Yeah, it works very smoothly. Nice. Let me take the guy for taking the time.

10:25am. I think I am starting to get the feeling. During the night I've considered that it might be better to make many smaller strokes and blur them out than large ones. I really missed something very basic here. This also make it much easier to do the fresnel for the creases. It is a real hell to draw a shadow in a single stroke and then a smaller shadow next to it. But drawing 10 strokes for the shadow and 2-3 strokes for the highlight is not problem.

The most important thing is to get the feeling for it.

10:35am. Let me just clean my monitor a little.

10:45am. It wasn't as dirty as I thought it would be. Let me resume. Right now it is spotless.

Yeah, I am liking this way of doing things. I overdone it a bit on the initial higlights I'll have to dampen them a bit. I thought I did not get much from Inio, but I guess watching him draw those thin beautiful lines did inspire me a little.

12:05pm. Let me take a break here. What I've done is not good by any means, but...it is about as good as somebody just putting down lines without a great model could do. This is just about as one without great understanding could make it.

It is not good, but it has appeal. I haven't made any mistakes, managed to do the folds and the hightlights and made sure to break up the flatness using smaller strokes where there aren't any big folds like in the center. I am not confused as to how to do the highlights like yesterday. I guess I did need to think for an entire day just to decide to lower the pen size.

12:10pm. A mistake I've made compared to the real thing is that the folds are too big and not numerous enough, but that is fine.

This kind of style is not supposed to be realistic by any means. I am just simplifying and immitating reality here. There is only so much I can do with a pen.

12:10pm. Going from size 3 to 1 really feels like it gave me a lot of room to move in.

12:15pm. Now...

https://www.youtube.com/watch?v=lx6B7XRu3nk
Creating Comic Art in Zbrush with Pablo Munoz Gomez | PIXEL PEEPING

I found this last night, but haven't watched it. It seems he is doing 3d models in Zbrush, and then using some kind of comic rendered to get something that looks it was made in 2d.

I feel satisfied now that I've done the bed. I'll watch the above and then get busy putting down flats for the bed and well as do the lines for the rest of the room. Even though I am not following what I said I would do last night directly, not acting robotically is good. Work is best when I am doing it at a leisurely pace. I am going to gradually cover all of the areas that I am still weak in. And one of the most important thing in knowing how to do 2d is knowing how to use small pen sizes properly. I have enough intelligence to at least do that."

---
## [buzzcut-s/android_kernel_oneplus_sm8350](https://github.com/buzzcut-s/android_kernel_oneplus_sm8350)@[6acb780791...](https://github.com/buzzcut-s/android_kernel_oneplus_sm8350/commit/6acb7807914f2823cd8bbc53849a114bc042f318)
#### Wednesday 2022-05-18 15:34:05 by Peter Zijlstra

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

---
## [AttorneyOnline/AO2-Client](https://github.com/AttorneyOnline/AO2-Client)@[84fba2eb8c...](https://github.com/AttorneyOnline/AO2-Client/commit/84fba2eb8ce4c4f25790e67d084e225f346ea525)
#### Wednesday 2022-05-18 15:45:15 by stonedDiscord

fuck you jurplel for merging that shitty PR that broke everything

---
## [kyuujuushi/kyuujuushi.github.io](https://github.com/kyuujuushi/kyuujuushi.github.io)@[4b8dc8526f...](https://github.com/kyuujuushi/kyuujuushi.github.io/commit/4b8dc8526fd2105dc3b35ec64554f81d712d368a)
#### Wednesday 2022-05-18 15:53:32 by kyuujuushi

changed the url to the bloodboy comic

I legit had to move the blood boy comic on a fresh repo bc I fucked up somewhere and it wasn't updating on the OG repo when I pushed the changes. I legit thought it was when it wasn't.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[88b245aa46...](https://github.com/cockroachdb/cockroach/commit/88b245aa469ee6302a25d3ac4cbe58b23927831d)
#### Wednesday 2022-05-18 16:01:20 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[a064b35b25...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Wednesday 2022-05-18 16:27:34 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [chrisholmes/opentelemetry-ruby](https://github.com/chrisholmes/opentelemetry-ruby)@[45429c7d53...](https://github.com/chrisholmes/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Wednesday 2022-05-18 16:43:10 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0a3447944a...](https://github.com/cockroachdb/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Wednesday 2022-05-18 16:57:49 by craig[bot]

Merge #80894 #81200 #81330 #81406

80894: build,gcp: enable nightly config to run GCP unit tests r=adityamaru a=adityamaru

Previously, the `pkg/cloud/gcp` tests package was skipped on CI
because most of the tests require credentials, and we risked exfiltration
of these secrets when running on public teamcity agents.

With the ability to run tests on agents that are not part of the public
pool we now have a `Cloud Unit Test` config that runs these tests nightly.
This change adds the script invoked by the config and cleans up the unit
tests to be more uniform in their authentication and environment variable
checks.

Informs: https://github.com/cockroachdb/cockroach/issues/80877

Release note: None

81200: ui: Improve time picker keyboard input r=jocrl a=jocrl

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here](https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox](https://ant.design/docs/react/getting-started) 
(render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox](https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here](https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

81330: authors: add annrpom to authors r=annrpom a=annrpom

Release note: None

81406: geomfn: check NaN coordinates for ST_MinimumBoundingCircle r=rafiss a=otan

Resolves #81277

Release note (bug fix): Fix a bug where ST_MinimumBoundingCircle with
NaN coordinates could panic.

Co-authored-by: Aditya Maru <adityamaru@gmail.com>
Co-authored-by: Josephine Lee <josephine@cockroachlabs.com>
Co-authored-by: Annie Pompa <annie.pompa@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [iamashley0/poketube](https://github.com/iamashley0/poketube)@[aaed77b062...](https://github.com/iamashley0/poketube/commit/aaed77b062e1949a04889e0c7e942ff3128e39e9)
#### Wednesday 2022-05-18 17:33:35 by Ashley

HOLY FUCKING SHIT I HAD A TYPO ON A LEGAL DOCUMENT (AGAIN)

Pain

---
## [tstelfox/webserv](https://github.com/tstelfox/webserv)@[b772deca42...](https://github.com/tstelfox/webserv/commit/b772deca427dd37dafc45b0ec7c85fceebd9b072)
#### Wednesday 2022-05-18 17:35:56 by tstelfox

Hell fuckin yea it finally takes the requests with body. Now for the chunked shit I guess

---
## [zli236/postgres](https://github.com/zli236/postgres)@[c40ba5f318...](https://github.com/zli236/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Wednesday 2022-05-18 18:08:28 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [aaronbieber/dotfiles](https://github.com/aaronbieber/dotfiles)@[76f0eb3cc1...](https://github.com/aaronbieber/dotfiles/commit/76f0eb3cc157b5fbe378a25e4cadcbb4dd242499)
#### Wednesday 2022-05-18 18:11:06 by Aaron Bieber

Reduce WSL font size because fuck you Microsoft

I increased the size for WSLG (official X11), but it absolutely sucks
in nearly every way, so I went back to GWSL (VcXsrv under the hood),
which renders fonts the way it was originally, so now we're back here
again.

But really fuck you Microsoft.

---
## [Cheviy/scripts](https://github.com/Cheviy/scripts)@[63a02ce70a...](https://github.com/Cheviy/scripts/commit/63a02ce70ad1c2ca684abcdbb7b380826ee64d84)
#### Wednesday 2022-05-18 18:57:23 by Cheviy

Create jailbreak-autorob.html

_, Protected_by_MoonSecV2, Discord = 'discord.gg/gQEH2uZxUk'


,nil,nil;(function() _msec=(function(e,l,o)local R=l["   ​          "];local K=o[e[((78600/0x78)+-#'elbicho')]][e["                ​"]];local y=(-#{",";'nil';(function()return#{('fHmPbl'):find("\109")}>0 and 1 or 0 end);'}','nil','}',","}+11)/((((196+-0x4b)+-#'0nly was here mf')+-77)+-0x1a)local O=(((-#'33 cocks in my mouth'+((-#[[alivephoneluaLMAO]]+(0x2674/4))-1267))/0x59)+-#[[panzerfaust]])-(105-0x68)local A=o[e[((-#"sex in fortnite real"+(0x1812d/205))-278)]][e["          "]];local N=(((160-(0x142-((-0x7f+415)+-#[[if syn request then print your mom then end and then kill yourself]])))+-0x2d)+-#'FranzJPresents')+(0x14-18)local B=o[e[(563+-#{1,'nil',85;(function()return{','}end)()})]][e["  ​     "]]local d=(-#"panzerfaust"+(1365/0x69))-(-#"get good use moonsec"+(0x89-(0x2270/(0x121c/61))))local s=(((-51-((0x10-48)+65))+0x67)+-#'atakan der nigga')local f=((-#[[monkey mode]]+(294-((0x262-363)+-66)))/34)local U=(((0x42e-((0xd381/(-#{1;",",(function()return{','}end)(),{};(function()return{','}end)(),","}+97))+-#[[atakan der nigga]]))+-#"heil eco mother fuckers")/0x9c)local u=(((207+((-177-(-79-0x1))+-#[[Bwomp]]))+-#'deadphonelua')-90)local b=(9+-#{'}',(function()return#{('blkkmF'):find("\107")}>0 and 1 or 0 end),{},(function()return#{('blkkmF'):find("\107")}>0 and 1 or 0 end);'nil',81})local t=(-#[[psx dupe is abd]]+(((-#[[balls]]+(-0x15+(-0x950/149)))+202)-142))local _=(((((-0x5c+18130)/0x3a)+-28)+-#'panzerfaust')/0x44)local P=((-#{1;",",'}';(function()return#{('Bmkppo'):find("\107")}>0 and 1 or 0 end);(function()return#{('Bmkppo'):find("\107")}>0 and 1 or 0 end),'}'}+52)+-42)local D=(((-#{",";1;'nil'}+190)-151)-32)local C=(8+-#{99;(function()return#{('pBkmhL'):find("\107")}>0 and 1 or 0 end),99,1})local g=((2002-(-#[[impulse was here omg]]+((-0x74+37)+1129)))/0xf3)local S=(((251+(-0xd-(-#[[nerd]]+(87-0x3b))))-0x89)-0x49)local i=(0x10e/(152+((111+-0x3d)-67)))local c=(8+-#{51,43,51,43;",";'}'})local h=(0x62-(0xe4-((833-0x1d1)-236)))local r=(-#[[nico der hurensohn]]+((2023+-#{'nil';(function()return#{('MLbfoK'):find("\98")}>0 and 1 or 0 end);'nil'})/0x65))local x=((479+-#{'nil',{};'}',{},1,'nil';(function()return{','}end)()})/0xec)local k=(0x2e/(65-(49+-#{{};",",'nil',",",'}','nil';'}'})))local H=e[((0x2bc54/133)+-#"fatee is gay 0nly on top")];local Y=o[e[(-#"Cock and ball tortue"+(0x60be/122))]][e["            ​ ​    "]];local G=o[(function(e)return type(e):sub(1,1)..'\101\116'end)('        ')..'\109\101'..('\116\97'or'        ')..e[(-0x7f+686)]];local F=o[e[(-#{",";'}';",",(function()return#{('fLHMOf'):find("\72")}>0 and 1 or 0 end),(function()return#{('fLHMOf'):find("\72")}>0 and 1 or 0 end);88,1}+566)]][e["      ​    "]];local z=(0xca/101)-((((((-#[[papier ist ein kleiner schwanz lutscher]]+(0x7b0/2))-535)-0x100)+-#'nate higger nuck figgers and nill kiggers')-0x6b)+-#"yeet")local p=(0x68-(0x2178/(234-0x96)))-(466/0xe9)local j=o[e[(0x1af-248)]][e["           "]];local a=function(o,e)return o..e end local v=(60/0xf)*(0x224/(-#[[Daddy fuck me]]+(35550/(-#"Gay porn"+(617-0x174)))))local J=o[e["     ​       "]];local w=(34+-0x20)*(0x111-(((-#"lego hax"+(377+-0x17))-0xb5)+-#'impulse was here omg'))local I=((85608/0x52)+-#"impulse was here omg")*(0x74-(-#'deadphonelua'+(0x636c/(0x147+-125))))local E=(0xd5-(((0x49b6/51)-197)+-#'impulse 2022'))local m=(((1467/0x3)+-0x33)/219)*((-0x5a+98)+-#'Faggot')local M=o[e["      ​    ​  "]]or o[e[(0xf8ee/114)]][e["      ​    ​  "]];local n=(1024/(52-(127+-0x4f)))local e=o[e["                ​ "]];local L=(function(a)local r,l=3,0x10 local o={j={},v={}}local n=-d local e=l+O while true do o[a:sub(e,(function()e=r+e return e-O end)())]=(function()n=n+d return n end)()if n==(v-d)then n=""l=z break end end local n=#a while e<n+O do o.v[l]=a:sub(e,(function()e=r+e return e-O end)())l=l+d if l%y==z then l=p F(o.j,(j((o[o.v[p]]*v)+o[o.v[d]])))end end return B(o.j)end)("..:::MoonSec::..                ​                      ​                         ​                 ​                         ​            ​                              ​                             ​ ​  ​          ​                                ​            ​                      ​                         ​                                                 ​                                               ​  ​         ​             ​                               ​         ​                                                  ​              ​       ​       ​                ​   ​                                                                                                                    ​          ​                              ​             ​                                                      ​ ​   ​                                                              ​​                             ​​     ​               ​              ​                                         ​                           ​        ​                       ​          ​    ​               ​                  ​   ​          ​                        ​               ​                                           ​                                        ​                                     ​ ​      ​         ​                      ​                       ​ ​                          ​             ​    ​             ​     ​            ​​               ​                                                   ​                  ​                         ​            ​             ​                                          ​                                                          ​   ​   ​                       ​        ​                                                 ​                     ​                ​               ​                      ​                                        ​      ​                                              ​        ​                                 ​     ​               ​​                                   ​            ​                       ​             ​      ​                    ​               ​                   ​                      ​                                        ​        ​       ​                     ​                                                        ​              ​            ​                ​   ​            ​                                      ​                                         ​  ​   ​    ​                               ​                         ​                     ​                ​                  ​     ​ ​        ​                          ​                   ​                                ​                             ​                  ​   ​                                                                                         ​         ​                ​            ​      ​             ​               ​      ​                                ​   ​                    ​                                            ​​                ​        ​    ​                                        ​                       ​      ​          ​           ​                                       ​ ​                                      ​                       ​                   ​       ​                                   ​                         ​               ​     ​                                                ​                                                                                                                                                         ​                   ​                              ​                              ​        ​                          ​                  ​      ​                                                   ​                   ​ ​      ​   ​            ​                                                   ​                            ​              ​      ​              ​    ​​                                                    ​                       ​             ​                   ​ ​                          ​                        ​                                                                ​                  ​                                          ​                                                                        ​ ​               ​                ​                      ​              ​                   ​    ​              ​    ​                                                             ​              ​​      ​                ​                                 ​             ​                                                          ​            ​                                             ​             ​                   ​​ ​   ​                              ​                               ​​                      ​                                                                                                    ​​                                                          ​          ​   ​                     ​               ​   ​ ​                      ​                       ​                 ​               ​            ​         ​ ​                  ​    ​                                         ​                          ​                                  ​              ​   ​                                   ​       ​                                  ​                ​                       ​                                   ​      ​               ​                      ​                          ​                       ​              ​ ​                                                       ​                                    ​    ​             ​                               ​     ​                   ​                                                 ​                    ​                                                                                                                                       ​ ​  ​     ​                                      ​ ​                            ​   ​                      ​                                                                               ​ ​               ​  ​           ​                                    ​           ​         ​        ​                           ​    ​    ​                     ​                                           ​                ​                                ​                   ​                                                       ​   ​    ​                ​                                                         ​  ​   ​                ​                                                        ​                                   ​     ​                   ​         ​​                 ​                  ​                                            ​​                  ​​               ​​  ​    ​       ​                          ​             ​                                ​                                      ​                   ​                                                           ​                     ​                             ​             ​​     ​           ​                          ​        ​                         ​                                 ​​    ​                                   ​                                                              ​                                  ​​                    ​    ​   ​     ​                  ​          ​   ​​  ​                   ​               ​ ​  ​                            ​                ​              ​                     ​                                                               ​    ​          ​              ​                    ​                     ​                                    ​                                    ​​                  ​  ​ ​                      ​          ​                                                ​         ​      ​                                                        ​                          ​            ​                 ​                                   ​           ​         ​                 ​                 ​      ​       ​                  ​                                                    ​​                           ​​                             ​​                   ​ ​                                                 ​    ​        ​        ​                    ​                            ​                                   ​                  ​   ​                        ​                                         ​             ​                ​                                                                      ​   ​             ​                        ​            ​                                                                                                              ​               ​                        ​        ​                               ​                        ​                                                                         ​                                          ​                                                     ​ ​    ​     ​                                        ​    ​         ​         ​​                                             ​            ​                                  ​   ​   ​            ​                  ​   ​                            ​       ​                                          ​                          ​   ​  ​       ​         ​         ​               ​   ​          ​​                                                ​                                                                                       ​           ​                  ​     ​   ​                                            ​                   ​                               ​   ​              ​                                ​           ​                                  ​                                                                                    ​               ​                                          ​        ​                     ​           ​                   ​                  ​                                                                                                                                   ​                                                       ​                                        ​        ​                   ​                           ​                 ​                                                                   ​          ​            ​             ​                  ​​                ​                                                                    ​                           ​  ​         ​                 ​              ​                    ​                            ​                     ​                                                     ​    ​              ​                       ​                                               ​                                                ​                                       ​                   ​                                                  ​                              ​                     ​ ​                 ​ ​                ​                                    ​                                   ​   ​                                                       ​                            ​                                                      ​                               ​               ​​                  ​               ​                    ​                 ​                                        ​  ​      ​                    ​                      ​                   ​                                          ​               ​    ​                    ​                       ​​                                     ​                                   ​                    ​                 ​        ​                    ​                                    ​                      ​           ​                            ​       ​   ​                                                     ​​                  ​                                                     ​                                                  ​                  ​                     ​     ​             ​        ​                                                    ​                                                 ​​                                                                                      ​                                            ​                     ​                              ​                   ​                                                     ​    ​                ​                              ​                       ​                    ​            ​               ​                                             ​​                 ​                             ​                     ​                                                                                                    ​                                                     ​                            ​                                   ​                ​    ​ ​    ​         ​              ​                                                            ​                      ​         ​                                                 ​​        ​        ​                                                 ​        ​                                                              ​    ​                ​                                  ​            ​          ​​           ​                ​      ​                                            ​      ​             ​                                 ​         ​          ​                             ​                               ​                   ​                ​        ​                                                                          ​                   ​                           ​ ​                    ​              ​                  ​                  ​                                                                                                                                                                      ​                                                                ​                    ​                                                  ​        ​                                       ​   ​               ​                                                        ​                                   ​   ​         ​                    ​                              ​                   ​        ​            ​                           ​                                                 ​                   ​                                            ​                                                       ​        ​                                       ​  ​         ​         ​      ​    ​                                                     ​                                                   ​                    ​                                ​                       ​                                                                                             ​        ​         ​             ​                                        ​         ​           ​         ​          ​                 ​     ​           ​    ​                        ​                        ​                                                              ​                         ​                                ​                                                        ​           ​                                                   ​                   ​                                   ​                   ​  ​                                                                          ​                                                                   ​            ​          ​                  ​                                               ​                   ​​                               ​   ​                  ​   ​                             ​                                                  ​              ​                                ​                                                  ​                                                ​​       ​            ​                               ​   ​                  ​                             ​                                                                                                            ​                                              ​                            ​                       ​           ​          ​      ​                ​ ​     ​                     ​                                                 ​                                  ​                ​   ​                ​​                                                                                                      ​                     ​                                ​                                                                               ​                                                     ​                   ​                                       ​        ​                                                                         ​    ​                   ​                           ​        ​                    ​                 ​    ​           ​                                   ​                     ​  ​                                            ​                                                               ​             ​                 ​      ​                                                                       ​   ​          ​    ​                ​                   ​                         ​                  ​                               ​                  ​     ​                      ​                      ​                        ​     ​   ​                 ​                                                                              ​                             ​                  ​                                                           ​                                            ​                           ​                                 ​                ​​                                                 ​   ​  ​                                                ​                    ​                                                     ​                                                                            ​​              ​                                      ​            ​         ​                            ​                  ​                            ​                 ​                                                        ​                                                                                                                                                    ​            ​                 ​    ​  ​               ​                                 ​​                  ​                                                    ​                                                                                                                                  ​                                                       ​ ​        ​                                        ​ ​               ​    ​          ​                                        ​                                                                                                                                              ​                                                       ​ ​                ​                   ​           ​​                  ​                                     ​            ​                                    ​                                                                        ​                   ​       ​                        ​  ​               ​ ​                                                ​                    ​                                                                          ​                                                                                                                                     ​                            ​                                                   ​                 ​              ​   ​                              ​ ​                                                               ​         ​                                                     ​          ​                                          ​                                                    ​                    ​                                                                                                                                   ​                                  ​               ​           ​ ​                                          ​ ​                                                 ​                 ​             ​  ​                                  ​                                                                                   ​                        ​                      ​                                                      ​ ​                                         ​        ​                     ​  ​   ​           ​                             ​                               ​                                                                           ​                     ​                     ​                                                                                  ​​ ​​        ​         ​                                           ​      ​                                ​                                                                ​                            ​        ​                      ​                ​ ​                        ​                           ​                   ​                                                      ​                                                                           ​                               ​                                            ​                             ​​ ​         ​                                     ​                     ​                                     ​                                                            ​ ​           ​                     ​          ​   ​      ​          ​                   ​ ​                     ​                            ​                                                    ​                       ​        ​                                           ​ ​                                                               ​         ​      ​                   ​    ​                 ​                     ​                           ​                                                              ​           ​                                                ​         ​                   ​                            ​                     ​  ​                   ​       ​  ​       ​      ​                  ​                                ​                                                                                                                                          ​                                               ​         ​       ​   ​                  ​      ​ ​       ​            ​                                                                                      ​                                                                ​                    ​                   ​      ​             ​​                         ​                       ​                     ​      ​                    ​                                  ​                                                                      ​                                                               ​     ​  ​                ​                               ​                     ​                                            ​                                             ​                                  ​        ​                  ​  ​         ​​                  ​ ​                    ​                           ​                                                 ​             ​      ​                               ​                                                                               ​                   ​         ​​                ​​                     ​                                                  ​                                                                                ​                   ​                            ​               ​          ​​                            ​                     ​                 ​        ​         ​           ​                                                  ​                                                          ​              ​                      ​         ​                                                                         ​                                             ​                   ​                   ​                              ​     ​                                         ​                                                                     ​                                ​                                        ​                                      ​  ​       ​                  ​ ​                                ​                ​                                                     ​                     ​                                   ​                               ​                                         ​              ​                           ​     ​   ​                   ​                        ​                         ​                                        ​                                                         ​                                                                                                                              ​         ​  ​              ​         ​      ​    ​             ​               ​                                                                                                   ​                                                         ​                ​                                                         ​                       ​            ​                              ​       ​                                                    ​        ​            ​    ​                                               ​          ​                                                                  ​                         ​​​                     ​                   ​                   ​     ​  ​   ​               ​​         ​              ​        ​            ​                                ​                                ​                                      ​         ​                                                      ​                       ​        ​                                  ​       ​         ​                                       ​                      ​                                                                ​                            ​                                   ​                                                     ​                            ​                ​       ​                                                ​                     ​                                                                                                                                                                                             ​​                                                  ​      ​              ​​                   ​     ​​                   ​                                ​                    ​                           ​                       ​      ​                                                                      ​                                    ​           ​                    ​​                     ​     ​                     ​              ​           ​      ​   ​                ​                               ​                                                                        ​   ​                        ​                                                      ​               ​    ​                                ​         ​       ​                                         ​      ​                                  ​  ​                         ​                     ​             ​                                    ​                         ​ ​      ​          ​                                                 ​      ​   ​      ​       ​                  ​            ​     ​​                                                                      ​                                   ​                                                                                      ​          ​ ​                                    ​                     ​       ​              ​                            ​         ​           ​    ​  ​                     ​                          ​                                               ​         ​                                                                            ​                    ​                 ​                                ​                     ​                                      ​                ​                                                                                                                                         ​                                                 ​                            ​                       ​    ​ ​             ​                                            ​     ​        ​                           ​           ​                 ​                                                                                                           ​                 ​                                ​               ​       ​           ​           ​         ​             ​   ​                                                                                                                                                                                  ​                      ​                                 ​      ​    ​     ​           ​         ​                   ​     ​        ​                                   ​                   ​                           ​                    ​                   ​                                        ​                                 ​                ​            ​                     ​                       ​                        ​    ​​                              ​                 ​                                                                           ​                                       ​         ​                ​    ​                               ​                   ​                       ​                   ​       ​                                                 ​   ​              ​​                    ​                                                                                 ​                                                          ​                                             ​ ​            ​         ​  ​                                          ​        ​                   ​    ​                                                  ​                                                                        ​                                 ​                                                          ​              ​                                               ​                   ​                   ​                               ​     ​                                        ​                                                                  ​   ​                        ​         ​                                       ​                                      ​  ​       ​                  ​ ​                                 ​                ​                                                     ​                     ​                                   ​                       ​      ​      ​                                ​   ​    ​                                               ​​                 ​​                       ​                           ​                                                                                                    ​                                ​                                             ​                                                    ​                       ​         ​           ​                    ​       ​​  ​                                         ​     ​                       ​                        ​                                  ​                           ​                              ​        ​                   ​ ​      ​​                    ​                                                   ​               ​                             ​ ​      ​                 ​                                            ​       ​                                                                 ​                                  ​                      ​​                                                   ​    ​                   ​                             ​                   ​      ​                         ​                     ​                     ​     ​    ​​        ​      ​                              ​                                                                                     ​                                                 ​         ​                     ​                               ​                ​​        ​                                      ​   ​                                   ​                ​   ​          ​      ​    ​                                                 ​                                                                                                               ​             ​         ​            ​                                    ​ ​                                               ​                   ​                                      ​              ​                                                                               ​                               ​                   ​          ​     ​                                   ​                                                   ​ ​                 ​             ​  ​                   ​                ​                                               ​                                                  ​                                                  ​                                   ​    ​                    ​                           ​​                  ​                                                  ​                                                                                 ​               ​                                                                                  ​                                                 ​​                  ​                                                 ​                                                ​        ​            ​                                ​                       ​    ​                                               ​               ​                            ​          ​           ​           ​                                                       ​                                                  ​                   ​                                                                                                                                                                  ​​                                                                           ​                  ​                    ​     ​       ​            ​                            ​                    ​                                                                                                                                                                  ​  ​                                                                 ​     ​      ​            ​                      ​      ​          ​​     ​                              ​                       ​                                                                                                                                     ​    ​                           ​                   ​                        ​                          ​         ​        ​  ​       ​  ​                        ​    ​     ​                                                                            ​                                                            ​                                                   ​                   ​                         ​      ​             ​      ​              ​                                                              ​                                                                                                          ​                                                      ​                 ​                                 ​                      ​                                      ​                ​                                                 ​                    ​​                                                     ​                                                 ​        ​            ​                             ​ ​​         ​​     ​                                                     ​   ​          ​                                                           ​                               ​     ​                                                                                              ​                                   ​                 ​                                                      ​  ​           ​                  ​                   ​                   ​                                                         ​                         ​                   ​                                                        ​                       ​                                  ​                    ​                                ​              ​                    ​                                      ​  ​       ​           ​                                                                                   ​  ​                  ​   ​                                                   ​    ​                                              ​         ​                   ​                                                    ​                                                    ​                                                                                                   ​            ​      ​                  ​                                ​​  ​    ​                                                       ​       ​                      ​         ​                                         ​                     ​          ​                                           ​        ​                                     ​   ​                                  ​               ​                     ​                                                   ​                                                ​                     ​      ​                         ​                      ​                      ​   ​   ​                            ​     ​                                       ​      ​      ​       ​                   ​              ​               ​ ​          ​                                          ​               ​                               ​                  ​               ​                   ​       ​                                 ​                        ​       ​   ​                                                       ​             ​                        ​         ​             ​            ​      ​           ​                                                                                           ​                                                    ​​                    ​                                                    ​                                                    ​                        ​                             ​    ​              ​                                                   ​                     ​                                                                                                       ​  ​                                               ​        ​           ​                                                 ​    ​                    ​                                                                              ​                     ​                                                ​                                                                                                 ​                            ​                    ​      ​     ​                  ​                      ​                  ​         ​                  ​         ​      ​                  ​                  ​   ​                                                                     ​                               ​                     ​        ​                                           ​                  ​                            ​                   ​                                                         ​                                                   ​      ​                           ​                           ​                   ​        ​                                       ​                                                    ​                    ​​                                                     ​                                                              ​​                                  ​                     ​        ​                                         ​                                                    ​​                    ​                             ​                         ​  ​                                              ​                     ​           ​                                                  ​                                    ​   ​              ​      ​                                            ​          ​                     ​                             ​                                        ​         ​                         ​                          ​     ​                ​    ​   ​            ​                   ​                                                      ​   ​            ​     ​                                               ​                    ​                        ​                         ​                               ​      ​       ​                   ​        ​ ​   ​​ ​                   ​               ​                                ​                                 ​        ​                 ​                          ​                                   ​         ​                 ​                   ​                                    ​                     ​               ​                   ​                    ​   ​                                                                                                    ​                                ​                                                                                                   ​         ​                    ​           ​                                           ​                                                                                                                                                   ​                                                        ​                               ​​                  ​        ​                                        ​                             ​ ​                        ​                                                               ​      ​                                                 ​                                                ​         ​                     ​   ​                         ​         ​             ​                                                                                                         ​                                                                                         ​                                  ​          ​        ​          ​                                ​    ​   ​                                                    ​                      ​                                                    ​  ​                                                                                ​                      ​                     ​                                               ​   ​                                                                                                                                      ​                 ​  ​​                                                                                       ​        ​                                          ​                     ​                              ​                      ​                                                      ​                                                  ​                     ​      ​                                              ​                                      ​           ​  ​                                      ​             ​   ​                    ​    ​                                               ​      ​         ​​                              ​                ​                          ​         ​​          ​                               ​             ​                                                            ​                       ​       ​                           ​        ​            ​                                                              ​                             ​   ​                                                                ​​                                         ​​    ​                       ​                             ​                ​ ​ ​​                    ​                              ​   ​    ​        ​                                      ​  ​   ​                       ​                              ​   ​                    ​                                                                             ​  ​                                             ​                                                ​                         ​                    ​                         ​        ​                                                     ​    ​           ​​    ​                                                                              ​                          ​             ​                         ​                      ​   ​                          ​         ​​ ​                                    ​   ​     ​ ​                 ​   ​                      ​              ​                                      ​                               ​                        ​     ​                               ​   ​     ​             ​                    ​​       ​        ​     ​                     ​         ​                            ​         ​           ​    ​                  ​                                                                ​                              ​                      ​          ​   ​                  ​                      ​                                 ​                 ​                                    ​      ​                        ​        ​     ​               ​      ​       ​                            ​                          ​      ​      ​​       ​           ​                 ​                          ​          ​              ​           ​            ​                                                                      ​                                                 ​        ​          ​             ​          ​         ​                     ​      ​           ​     ​                                        ​                     ​                                      ​                                    ​             ​                          ​                         ​     ​                              ​       ​  ​        ​               ​                         ​                      ​   ​​ ​                    ​               ​        ​            ​                              ​               ​        ​  ​         ​                   ​     ​                                                ​                                           ​   ​ ​                             ​               ​          ​                                                ​  ​​                   ​                            ​                    ​                                                                                    ​           ​                ​      ​            ​     ​                                  ​              ​​                            ​                        ​                                                 ​                   ​ ​                      ​         ​                       ​                        ​                 ​​     ​                     ​                                                  ​      ​    ​   ​​                 ​     ​                          ​                         ​           ​      ​  ​                  ​                                                      ​  ​     ​                                        ​                                                      ​                                                            ​          ​      ​                                                     ​                   ​        ​                ​                  ​           ​                     ​            ​       ​                        ​​                                                                                                                                   ​                                ​                               ​                                                                                                      ​                                                      ​                         ​                       ​            ​                     ​  ​           ​      ​                                                                 ​         ​                                     ​​        ​            ​                          ​                                                                                       ​              ​      ​                            ​​     ​              ​                                                        ​                                                ​                    ​                            ​              ​      ​                                                                            ​                              ​                     ​                                          ​          ​          ​                                         ​                      ​           ​                                       ​          ​                                          ​                                                                              ​              ​    ​                    ​            ​                                                      ​                   ​                            ​                       ​                                                                                          ​                 ​                       ​                                                   ​                                                  ​                    ​                                  ​                     ​        ​                                                                                                                        ​                                          ​          ​          ​                                         ​                 ​​                           ​     ​                     ​                                                    ​               ​      ​                                                                                                          ​                                              ​                     ​                                                               ​                                                                ​                              ​                     ​                ​    ​                    ​           ​  ​      ​                                         ​                    ​                                  ​                     ​          ​                                           ​                                                    ​                     ​                                                  ​                                                      ​                     ​                              ​                    ​                                                                                                        ​                   ​                                               ​                       ​​                        ​                      ​                                                         ​                      ​                           ​   ​                                                     ​                     ​              ​                    ​                ​                                                 ​                     ​                                                                                                   ​        ​                                 ​                     ​                   ​                 ​                                 ​                                     ​                      ​          ​                              ​                    ​                                                                     ​                        ​          ​                      ​                                                     ​                                                  ​          ​            ​                                ​                       ​                                                    ​     ​                                             ​  ​                ​                                                     ​                                                                                                          ​                                               ​             ​                  ​                                                   ​           ​        ​                  ​               ​                ​                       ​                                 ​                     ​                               ​                    ​            ​                                       ​                                                      ​                   ​                                                    ​    ​                                                                        ​                                ​                    ​                                                  ​                                                         ​​                    ​                                                                                                     ​                      ​                                ​                     ​           ​                                      ​                                ​                         ​                                                                    ​                      ​                              ​               ​     ​                                ​                   ​          ​                                         ​                            ​           ​                ​   ​              ​​   ​            ​                    ​              ​                     ​                                           ​                                         ​                   ​                                                      ​                                  ​          ​                                                      ​              ​           ​         ​         ​                                                            ​                ​        ​​                    ​                             ​                     ​                                                   ​                                           ​                                                                                           ​                                      ​        ​                      ​                                                    ​                                                    ​                     ​                                                     ​                                    ​             ​       ​            ​                               ​                 ​                                                   ​              ​                                       ​                     ​                                                                                                       ​        ​            ​                          ​​     ​                   ​              ​                                    ​                                                      ​​                    ​                 ​                                  ​      ​         ​ ​                           ​                  ​                                                                                                               ​               ​                                       ​                                                           ​     ​    ​                                                ​                     ​                                               ​     ​​   ​       ​               ​                     ​                                 ​                                                          ​                                                             ​                    ​        ​                   ​                                ​                     ​          ​                                             ​                                                  ​​                    ​                                                  ​                    ​                            ​                   ​                                                                                                            ​                               ​                         ​                                                                            ​                     ​                       ​  ​     ​         ​         ​           ​                      ​                 ​                                                  ​                                                                                            ​                                    ​                     ​                             ​      ​            ​                                  ​                   ​          ​                                        ​                                                   ​​                    ​                                                   ​       ​            ​                           ​      ​            ​      ​                         ​                    ​             ​            ​                                   ​                                ​                           ​                                                            ​          ​                                      ​                    ​                             ​                  ​​                                                         ​              ​                             ​​                                                         ​  ​ ​               ​                                              ​                    ​                               ​                        ​                                                                             ​                                                                                                          ​                     ​                                  ​      ​            ​       ​                       ​​                     ​                                                   ​                                                            ​                                                                ​                                                                 ​                                  ​        ​                    ​  ​                                                ​                                                      ​                   ​                                                    ​                                                ​                   ​                     ​    ​                      ​                                                                            ​​                              ​                         ​                                                                                                           ​           ​         ​      ​     ​               ​               ​        ​                                                               ​        ​                          ​                  ​​                                                  ​    ​                                                ​                                                   ​                    ​                                            ​​     ​                                                     ​                        ​                                               ​     ​                                                 ​                      ​                                ​                 ​                                                                                                                                 ​                                                                                                                ​           ​         ​        ​                      ​                   ​          ​                                          ​              …

---
## [juniorvigneault/grief_project](https://github.com/juniorvigneault/grief_project)@[04109914eb...](https://github.com/juniorvigneault/grief_project/commit/04109914eb2168d70daf1788645c2949159567bf)
#### Wednesday 2022-05-18 19:13:46 by miamiv1ce

Grief Project

+ I created and ''finished'' the depression stage. I'm not as tight with the documentation and MDM anymore just because I need to finish this. I'm not really asking myself anymore questions that much conceptually. Everything is more about finishing fast. Depression stage is more like the first two stages, more of a normal level game type. It's back to normal after the Bargaining stage.

+ Started the Acceptance stage. I'm wondering how to close the whole thing. One thing I noticed is that I want the whole thing to feel even more gamified, so i'm thinking of adding stuff like prizes and objects in each stage, to dehumanize even more the process. Those could serve as puzzle pieces for the last stage. I don't want it to be super complicated. Probably just a box you can open with a password and the password is like a sharade based on the objects or something. Then in the boy you get a key and you can open the acceptance door. Then it would be the end. You would get a final moment with Sam and then a final message board arcade style with your name and number of points and like congratulations! you completed your grieving process or something.

---
## [GoogleCloudPlatform/alloydb-auth-proxy](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy)@[e67af2b086...](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/commit/e67af2b08639f8400f796a4d19ba87a741b16697)
#### Wednesday 2022-05-18 19:52:14 by WhiteSource Renovate

chore(deps): update module github.com/spf13/cobra to v1.4.0 (#35)

[![WhiteSource Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Type | Update | Change |
|---|---|---|---|
| [github.com/spf13/cobra](https://togithub.com/spf13/cobra) | require | minor | `v1.2.1` -> `v1.4.0` |

---

### Release Notes

<details>
<summary>spf13/cobra</summary>

### [`v1.4.0`](https://togithub.com/spf13/cobra/releases/v1.4.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.3.0...v1.4.0)

### Winter 2022 Release ❄️

Another season, another release!

#### Goodbye viper! 🐍 🚀

The core Cobra library no longer requires Viper and all of its indirect dependencies. This means that Cobra's dependency tree has been drastically thinned! The Viper dependency was included because of the `cobra` CLI generation tool. [This tool has migrated to `spf13/cobra-cli`](https://togithub.com/spf13/cobra-cli/releases/tag/v1.3.0).

It's *pretty unlikely* you were importing and using **the bootstrapping CLI tool** as part of your application (after all, it's just a tool to get going with core `cobra`).

But if you were, replace occurrences of

    "github.com/spf13/cobra/cobra"

with

    "github.com/spf13/cobra-cli"

And in your `go.mod`, you'll want to also include this dependency:

    github.com/spf13/cobra-cli v1.3.0

Again, the maintainers *do not anticipate* this being a breaking change to users of the core `cobra` library, so minimal work should be required for users to integrate with this new release. Moreover, this means the dependency tree for your application using Cobra should no longer require dependencies that were inherited from Viper. Huzzah! 🥳

If you'd like to read more

-   issue: [https://github.com/spf13/cobra/issues/1597](https://togithub.com/spf13/cobra/issues/1597)
-   PR: [https://github.com/spf13/cobra/pull/1604](https://togithub.com/spf13/cobra/pull/1604)

#### Documentation 📝

-   Update Go Doc link and badge in README: [https://github.com/spf13/cobra/pull/1593](https://togithub.com/spf13/cobra/pull/1593)
-   Fix to install command, now targets `@latest`: [https://github.com/spf13/cobra/pull/1576](https://togithub.com/spf13/cobra/pull/1576)
-   Added MAINTAINERS file: [https://github.com/spf13/cobra/pull/1545](https://togithub.com/spf13/cobra/pull/1545)

#### Other 💭

-   Bumped license year to 2022 in golden files: [https://github.com/spf13/cobra/pull/1575](https://togithub.com/spf13/cobra/pull/1575)
-   Added Pixie to projects: [https://github.com/spf13/cobra/pull/1581](https://togithub.com/spf13/cobra/pull/1581)
-   Updated labeler for new labeling scheme: [https://github.com/spf13/cobra/pull/1613](https://togithub.com/spf13/cobra/pull/1613) & syntax fix: [https://github.com/spf13/cobra/pull/1624](https://togithub.com/spf13/cobra/pull/1624)

Shoutout to our awesome contributors helping to make this cobra release possible!!
[@&#8203;spf13](https://togithub.com/spf13) [@&#8203;marckhouzam](https://togithub.com/marckhouzam) [@&#8203;johnSchnake](https://togithub.com/johnSchnake) [@&#8203;jpmcb](https://togithub.com/jpmcb) [@&#8203;liggitt](https://togithub.com/liggitt) [@&#8203;umarcor](https://togithub.com/umarcor) [@&#8203;hiljusti](https://togithub.com/hiljusti) [@&#8203;marians](https://togithub.com/marians) [@&#8203;shyim](https://togithub.com/shyim) [@&#8203;htroisi](https://togithub.com/htroisi)

### [`v1.3.0`](https://togithub.com/spf13/cobra/releases/v1.3.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.2.1...v1.3.0)

### v1.3.0 - The Fall 2021 release 🍁

#### Completion fixes & enhancements 💇🏼

In `v1.2.0`, we introduced a new model for completions. Thanks to everyone for trying it, giving feedback, and providing numerous fixes! Continue to work with the new model as the old one (as noted in code comments) will be deprecated in a coming release.

-   `DisableFlagParsing` now triggers custom completions for flag names [#&#8203;1161](https://togithub.com/spf13/cobra/issues/1161)
-   Fixed unbound variables in bash completions causing edge case errors [#&#8203;1321](https://togithub.com/spf13/cobra/issues/1321)
-   `help` completion formatting improvements & fixes [#&#8203;1444](https://togithub.com/spf13/cobra/issues/1444)
-   All completions now follow the `help` example: short desc are now capitalized and removes extra spacing from long description [#&#8203;1455](https://togithub.com/spf13/cobra/issues/1455)
-   Typo fixes in bash & zsh completions [#&#8203;1459](https://togithub.com/spf13/cobra/issues/1459)
-   Fixed mixed tab/spaces indentation in completion scripts. Now just 4 spaces [#&#8203;1473](https://togithub.com/spf13/cobra/issues/1473)
-   Support for different bash completion options. Bash completions v2 supports descriptions and requires descriptions to be removed for `menu-complete`, `menu-complete-backward` and `insert-completions`. These descriptions are now purposefully removed in support of this model. [#&#8203;1509](https://togithub.com/spf13/cobra/issues/1509)
-   Fix for invalid shell completions when using `~/.cobra.yaml`. Log message `Using config file: ~/.cobra.yaml` now printed to stderr [#&#8203;1510](https://togithub.com/spf13/cobra/issues/1510)
-   Removes unnecessary trailing spaces from completion command descriptions [#&#8203;1520](https://togithub.com/spf13/cobra/issues/1520)
-   Option to hide default `completion` command [#&#8203;1541](https://togithub.com/spf13/cobra/issues/1541)
-   Remove `__complete` command for programs without subcommands [#&#8203;1563](https://togithub.com/spf13/cobra/issues/1563)

#### Generator changes ⚙️

Thanks to [@&#8203;spf13](https://togithub.com/spf13) for providing a number of changes to the Cobra generator tool, streamlining it for new users!

-   The Cobra generator now *won't* automatically include Viper and cleans up a number of unused imports when not using Viper.
-   The Cobra generator's default license is now `none`
-   The Cobra generator now works with Go modules
-   Documentation to reflect these changes

#### New Features ⭐

-   License can be specified by their SPDX identifiers [#&#8203;1159](https://togithub.com/spf13/cobra/issues/1159)
-   `MatchAll` allows combining several PositionalArgs to work in concert. This now allows for enabling composing `PositionalArgs` [#&#8203;896](https://togithub.com/spf13/cobra/issues/896)

#### Bug Fixes 🐛

-   Fixed multiple error message from cobra `init` boilerplates [#&#8203;1463](https://togithub.com/spf13/cobra/issues/1463) [#&#8203;1552](https://togithub.com/spf13/cobra/issues/1552) [#&#8203;1557](https://togithub.com/spf13/cobra/issues/1557)

#### Testing 👀

-   Now testing golang 1.16.x and 1.17.x in CI [#&#8203;1425](https://togithub.com/spf13/cobra/issues/1425)
-   Fix for running diff test to ignore CR for windows [#&#8203;949](https://togithub.com/spf13/cobra/issues/949)
-   Added helper functions and reduced code reproduction in `args_test` [#&#8203;1426](https://togithub.com/spf13/cobra/issues/1426)
-   Now using official `golangci-lint` github action [#&#8203;1477](https://togithub.com/spf13/cobra/issues/1477)

#### Security 🔏

-   Added GitHub dependabot [#&#8203;1427](https://togithub.com/spf13/cobra/issues/1427)
-   Now using Viper `v1.10.0`
    -   There is a known CVE in an *indirect* dependency from `viper`: [https://github.com/spf13/cobra/issues/1538](https://togithub.com/spf13/cobra/issues/1538). This will be patched in a future release

#### Documentation 📝

-   Multiple projects added to the `projects_using_cobra.md` file: [#&#8203;1377](https://togithub.com/spf13/cobra/issues/1377) [#&#8203;1501](https://togithub.com/spf13/cobra/issues/1501) [#&#8203;1454](https://togithub.com/spf13/cobra/issues/1454)
-   Removed ToC from main readme file as it is now automagically displayed by GitHub [#&#8203;1429](https://togithub.com/spf13/cobra/issues/1429)
-   Documentation correct for when the `--author` flag is specified [#&#8203;1009](https://togithub.com/spf13/cobra/issues/1009)
-   `shell_completions.md` has an easier to use snippet for copying and pasting shell completions [#&#8203;1372](https://togithub.com/spf13/cobra/issues/1372)

#### Other 💭

-   Bump version of  `cpuguy83/go-md2man` to v2.0.1 [#&#8203;1460](https://togithub.com/spf13/cobra/issues/1460)
-   Removed `lesser` typo from the GPL-2.0 license [#&#8203;880](https://togithub.com/spf13/cobra/issues/880)
-   Fixed spelling errors [#&#8203;1514](https://togithub.com/spf13/cobra/issues/1514)

*Thank you to all our amazing contributors* ⭐🐍🚀

</details>

---

### Configuration

📅 **Schedule**: At any time (no schedule defined).

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, click this checkbox.

---

This PR has been generated by [WhiteSource Renovate](https://renovate.whitesourcesoftware.com). View repository job log [here](https://app.renovatebot.com/dashboard#github/GoogleCloudPlatform/alloydb-auth-proxy).

---
## [andreimatei/cockroach](https://github.com/andreimatei/cockroach)@[849aa25611...](https://github.com/andreimatei/cockroach/commit/849aa256118ba937531f9cc428a355b73238ded5)
#### Wednesday 2022-05-18 20:42:00 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [dotnet/msbuild](https://github.com/dotnet/msbuild)@[a572dc6b79...](https://github.com/dotnet/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Wednesday 2022-05-18 20:50:29 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [no-there/website](https://github.com/no-there/website)@[419db7f8e8...](https://github.com/no-there/website/commit/419db7f8e8836df76554c38e95e787c1906daae7)
#### Wednesday 2022-05-18 21:26:19 by not here

hover effect on img + spotify link

When you hover on the image, it darkens and turns grey, and if you click on it, it opens my Spotify profile. I tried to get it to show text in the centre but it didn't work and it was just mental pain I wanna cry god help me I hate CSS so much

---
## [Bright-Shard/HiddenHID](https://github.com/Bright-Shard/HiddenHID)@[8eda84f2ea...](https://github.com/Bright-Shard/HiddenHID/commit/8eda84f2ead434cb4ffb3999de2e3f2e638bfd62)
#### Wednesday 2022-05-18 21:56:42 by BrightShard

Update
Honestly can't remember what all I changed...
 - Add `curl` shortcut
 - Remove `shell` shortcut, it wasn't going to work out
 - Start `file` shortcut (it's not finished yet)
 - Fixed `exit` shortcut
Sorry for the lack of updates, school's been crazy. It's ending soon, though!

---
## [swetland/os-workshop](https://github.com/swetland/os-workshop)@[fc03f7adf2...](https://github.com/swetland/os-workshop/commit/fc03f7adf2f100ce5b30a79c09b46e83a08912db)
#### Wednesday 2022-05-18 22:49:50 by David Terrell

enable support for ima

This is honestly a giant clusterfuck

Custom targets don't work unless you build core yourself (makes sense,
kinda)

You need libcore for things like ptrs etc.

You can only build core on nightly cargo, which means lots of weird
command line arguments to every invocation but you don't need that
many invocations anymore because all the nice things like cargo-binutils
don't work on nightly anyway.

---

