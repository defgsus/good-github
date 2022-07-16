## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-15](docs/good-messages/2022/2022-07-15.md)


1,793,367 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,793,367 were push events containing 2,601,845 commit messages that amount to 191,925,722 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[6fe0683a7b...](https://github.com/nikothedude/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Friday 2022-07-15 01:16:15 by Jolly

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
## [Lontoone/STS_2022](https://github.com/Lontoone/STS_2022)@[74dd3094c6...](https://github.com/Lontoone/STS_2022/commit/74dd3094c6a8f372a03437b65c9c1913f397e493)
#### Friday 2022-07-15 02:00:09 by oi

fix my stupid ass fucking code so other people's pc won't expolde

---
## [llvm/llvm-project](https://github.com/llvm/llvm-project)@[7c51f02eff...](https://github.com/llvm/llvm-project/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Friday 2022-07-15 02:17:38 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could exposed a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [kokizzu/cockroach](https://github.com/kokizzu/cockroach)@[cc5bde5c7a...](https://github.com/kokizzu/cockroach/commit/cc5bde5c7abdf732695bc798afb47c6053e922e7)
#### Friday 2022-07-15 02:34:10 by craig[bot]

Merge #82440

82440: admission,storage: introduce flush tokens to constrain write admission r=tbg,irfansharif a=sumeerbhola

In addition to byte tokens for writes computed based on compaction rate
out of L0, we now compute byte tokens based on how fast the system can
flush memtables into L0. The motivation is that writing to the memtable,
or creating memtables faster than the system can flush results in write
stalls due to memtables, that create a latency hiccup for all write
traffic. We have observed write stalls that lasted > 100ms.

The approach taken here for flush tokens is straightforward (there is
justification based on experiments, mentioned in code comments):
- Measure and smooth the peak rate that the flush loop can operate on.
  This relies on the recently added pebble.InternalIntervalMetrics.
- The peak rate causes 100% utilization of the single flush thread,
  and that is potentially too high to prevent write stalls (depending
  on how long it takes to do a single flush). So we multiply the
  smoothed peak rate by a utilization-target-fraction which is
  dynamically adjusted and by default is constrained to the interval
  [0.5, 1.5]. There is additive increase and decrease of this
  fraction:
  - High usage of tokens and no write stalls cause an additive increase
  - Write stalls cause an additive decrease. A small multiplier is used
    if there are multiple write stalls, so that the probing falls
    more in the region where there are no write stalls.

Note that this probing scheme cannot eliminate all write stalls. For
now we are ok with a reduction in write stalls.

For convenience, and some additional justification mentioned in a code
comment, the scheme uses the minimum of the flush and compaction tokens
for writes to L0. This means that sstable ingestion into L0 is also
subject to such tokens. The periodic token computation continues to be
done at 15s intervals. However, instead of giving out these tokens at
1s intervals, we now give them out at 250ms intervals. This is to
reduce the burstiness, since that can cause write stalls.

There is a new metric, storage.write-stall-nanos, that measures the
cumulative duration of write stalls, since it gives a more intuitive
feel for how the system is behaving, compared to a write stall count.

The scheme can be disabled by increasing the cluster setting
admission.min_flush_util_fraction, which defaults to 0.5 (corresponding
to the 0.5 lower bound mentioned earluer), to a high value, say
10.

The scheme was evaluated using a single node cluster with the node
having a high CPU count, such that CPU was not a bottleneck, even
with max compaction concurrency set to 8. A kv0 workload with high
concurrency and 4KB writes was used to overload the store. Due
to the high compaction concurrency, L0 stayed below the unhealthy
thresholds, and the resource bottleneck became the total bandwidth
provisioned for the disk. This setup was evaluated under both:
- early-life: when the store had 10-20GB of data, when the compaction
  backlog was not very heavy, so there was less queueing for the
  limited disk bandwidth (it was still usually saturated).
- later-life: when the store had around 150GB of data.

In both cases, turning off flush tokens increased the duration of
write stalls by > 5x. For the early-life case, ~750ms per second was
spent in a write stall with flush-tokens off. The later-life case had
~200ms per second of write stalls with flush-tokens off. The lower
value of the latter is paradoxically due to the worse bandwidth
saturation: fsync latency rose from 2-4ms with flush-tokens on, to
11-20ms with flush-tokens off. This increase imposed a natural
backpressure on writes due to the need to sync the WAL. In contrast
the fsync latency was low in the early-life case, though it did
increase from 0.125ms to 0.25ms when flush-tokens were turned off.

In both cases, the admission throughput did not increase when turning
off flush-tokens. That is, the system cannot sustain more throughput,
but by turning on flush tokens, we shift queueing from the disk layer
the admission control layer (where we have the capability to reorder
work).

Screenshots for early-life: Flush tokens were turned off at 22:32:30. Prior to that the flush utilization-target-fraction was 0.625.
<img width="655" alt="Screen Shot 2022-06-03 at 6 35 14 PM" src="https://user-images.githubusercontent.com/54990988/171970564-ba833e1f-b6e2-4fcd-9ee2-25228341065c.png">
<img width="663" alt="Screen Shot 2022-06-03 at 6 35 28 PM" src="https://user-images.githubusercontent.com/54990988/171970574-13e6114a-2467-48e2-a238-3b01ea32a5d6.png">

Screenshots for later-life: Flush tokens were turned off at 22:03:20. Prior to that the flush utilization-target-fraction was 0.875.
<img width="665" alt="Screen Shot 2022-06-03 at 6 07 50 PM" src="https://user-images.githubusercontent.com/54990988/171970732-09b60827-7687-46de-964e-a9f97388c4fc.png">
<img width="658" alt="Screen Shot 2022-06-03 at 6 08 03 PM" src="https://user-images.githubusercontent.com/54990988/171970738-efe7a1fd-cbfd-450d-a3ac-06f681b1d190.png">

These results were produced by running
```
roachprod create -n 2 --clouds aws  --aws-machine-type=c5d.9xlarge --local-ssd=false --aws-ebs-volume-type=gp2 sumeer-io
roachprod put sumeer-io:1 cockroach ./cockroach
roachprod put sumeer-io:2 workload ./workload
roachprod start sumeer-io --env "COCKROACH_ROCKSDB_CONCURRENCY=8"
roachprod run sumeer-io:2 -- ./workload run kv --init --histograms=perf/stats.json --concurrency=1024 --splits=1000 --duration=30m0s --read-percent=0 --min-block-bytes=4096 --max-block-bytes=4096 {pgurl:1-1}
```

Fixes #77357

Release note (ops change): Write tokens are now also limited based on
flush throughput, so as to reduce storage layer write stalls. This
behavior is enabled by default. The cluster setting
admission.min_flush_util_fraction, defaulting to 0.5, can be used to
disable or tune flush throughput based admission tokens, for writes
to a store. Setting to a value much greater than 1, say 10, will
disable flush based tokens.

Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>

---
## [harryeffinpotter/ALL-LEGIT](https://github.com/harryeffinpotter/ALL-LEGIT)@[2d8e0d5d7c...](https://github.com/harryeffinpotter/ALL-LEGIT/commit/2d8e0d5d7c6fe26f18b45594cd2c02f012e0c31b)
#### Friday 2022-07-15 02:49:11 by HarryEffingPotter

Cancel fixed, filecrypt notation added, some other shit, fuck dis bitch im out.

---
## [Melon-Tropics/translations](https://github.com/Melon-Tropics/translations)@[1806b3b4b0...](https://github.com/Melon-Tropics/translations/commit/1806b3b4b073a749a871507ae26d09ee8d20b6da)
#### Friday 2022-07-15 03:47:32 by ProfessorBaum

Fix grammatical mistakes and style (DE)

Explanations for some of the corrections:

The dash is wrong between two words when the first word has a
'Fugen-S' which implies it to be genitive. Thus I removed it.

'URL' as in 'Website-URL' can have either female or male grammatical
gender as per the Duden. Male, however, is far more uncommon, thus
the change of the article from 'Der' to 'Die'.

The apostroph is not necessary in the imperative when there's no
letter missing.

'zum Bankkonto gehörig' is a participle construction which makes it
generally a bit hard to read and understand. The genitive will already
be enough to show posessiveness.

---
## [ncedeno1122/AwfulCatMetroidvania](https://github.com/ncedeno1122/AwfulCatMetroidvania)@[754fe59106...](https://github.com/ncedeno1122/AwfulCatMetroidvania/commit/754fe5910647aedf51d49e186377dd536f52ecde)
#### Friday 2022-07-15 05:38:24 by NoahCedeno

Attempts on an InteractableTile event workflow

...It didn't work with my current understanding of Unity's tilemaps. My problem is, how can I verify what Interactable Tile a listener is listening for. Normally, we could send this using an Observer Pattern to some script, but I have no way of sending an event from a SPECIFIC tile on the tilemap to some listeners because I cannot check for who sent the event. Because my current system has InteractableTiles firing off events from the LevelTileGO class on an instantiated RUNTIME-ONLY prefab, I have no way of knowing of it without hard-coding and magic numbers - all things I HATE!

I'm thinking of separating this idea from the RuleTile instantiated prefab, and creating a separate set of interactable objects in the editor, per-map, that we can use and hook up to one another...

I'll have to see if this is really the best approach though.

:camel:

---
## [ndaplumbing/Perth-Plumber](https://github.com/ndaplumbing/Perth-Plumber)@[fe26647afb...](https://github.com/ndaplumbing/Perth-Plumber/commit/fe26647afb105f1c279cad06f9b673dfb5de0e99)
#### Friday 2022-07-15 06:26:43 by ndaplumbing

5 reasons to hire a professional plumbing company in Perth

Plumbing is undeniably one of the most important systems of your home that needs to function optimally for smooth functioning inside the home. Whether you are planning a home renovation or plumbing maintenance and repair, hiring a professional plumbing company in Perth is important to save your money and time. In this article, we will tell you about the five reasons to hire professional plumbing company services.
Plumbers know their job
Plumbers in Plumbing Company in Perth are the ones who have got specific training, knowledge, and practical experience regarding plumbing. From minor issues like repairing leaks to other major issues, they are trained to deal with these issues. They are licensed and have the required experience and skills to know they are precisely doing the job and get you the permanent results.
Plumbers have the right tools and materials
Many people at home think that they can easily handle the job of a plumber by following different DIY methods. But they might not be aware of the fact that plumbers are the ones who have all the tools from major to minor that are required to perform the job seamlessly. They save a lot of your time in running back and forth from different hardware stores to buy different tools that you may even not probably use ever again!
The plumbing company covers multiple services
The plumbing company offers a wide variety of services that can help you to install, repair, or maintain your plumbing system easily. Whether it's your hot water system, drain camera inspection, block drainage, water leaks, water filter supplies, or even bathroom or renovation, plumbing services cover all of it under them. So you don't have to worry about it and run here and there for one separate service.
Time-saving
In our daily busy lifestyle, we hardly have time to do the plumbing job by ourselves. Juggling between so many responsibilities like handling a job, work, family, and hobbies we hardly get time to do such kind of detailed and hard work as plumbing. Thus in such situations, it's always best to hire plumbing company services that will help you to save a lot of time and hassles on your part.
High-quality work
Professional Perth Plumber is trained in such a way that he can provide you with a high degree of work. They will address all the issues regarding your plumbing and even the issues that you are not able to see but are there in your plumbing system. They will recognize all those loopholes and with the help of their skills and the latest equipment, they will give you the best services possible.
Gives you a permanent solution
Hiring professional plumbers will help you in giving a permanent solution to all your plumbing problems. The repair or the installation that a professional plumber will do for you will give you a permanent solution. And it is not a temporary fix that you have to get rectify again and again. So if you are changing your home or renovating it or renovating specific rooms of your home like the kitchen and bathroom then it's best always best to have professional plumbers.
Which is the best plumbing company in Perth?
We are sure that after knowing the benefits of professional plumbing services you must be considering hiring one. But which company to choose? As there are already a lot of services present in the market for plumbing.
Well, the answer to this question is straightforward as NDA Plumbing and Gas services are one of the leading plumbing service providers in Perth. We cover a wide range of services ranging from backflow devices and testing to commercial and domestic plumbing services. Apart from plumbing we also cover gas services. And to be rest assured of our services you can easily check our testimonials on our website or even on the internet and a lot of clients are loving our work and we will sure that you will love it too!
So what's the wait for? Visit our website now!
For more Information Click on the Link: https://ndaplumbingperth.com.au/

Phone Number: 0478 757 622
For any Query Contact Us: info@ndaplumbingperth.com.au
Address: 23 Gingerale Cir, Byford WA 6122, Australia.

---
## [ImFlynnn/android_kernel_realme_mt6785](https://github.com/ImFlynnn/android_kernel_realme_mt6785)@[469a006517...](https://github.com/ImFlynnn/android_kernel_realme_mt6785/commit/469a006517ad46a1bc141bf9e7356f97edeb8f0b)
#### Friday 2022-07-15 07:01:32 by Wang Han

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
Signed-off-by: officialputuid <officialputuid@hack.id>

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[d714bf455b...](https://github.com/lgritz/oiio/commit/d714bf455ba0a72d5dd0ad99c7572ddcfb0d8df1)
#### Friday 2022-07-15 07:06:38 by Larry Gritz

parallel.h refactoring and add support for TBB

Hide nearly all of the implementation of the parallel_for family of
methods rather than expose them as inline. This gives us more freedom
to change the implementation in the future without breaking ABI.

Deprecate the parallel methods that take task functions whose first
parameter is the thread ID. The only reason they existed is because
our cobbled together thread_pool used that in its inner workings.  But
there are good reasons why we should not expose that:

  * We never used it anyway.

  * It was not very useful, since sometimes it was a real thread ID, but
    other times it was -1 in cases where the calling thread executed the
    task directly.

  * It is inconsistent with other thread pool implementations that we may
    wish to try in the future.

So better just to not expose those thread IDs at all. Mark those
versions of the parallel loops as deprecated and schedule them for
removal in OIIO 3.0.

If TBB is detected at build time, support will be built in that allows
either the old OIIO built-in pool, or TBB, depending on the setting of
a new global OIIO attribute, "use_tbb" (default 0), if set to nonzero
will use the TBB thread pool.

In my experiments, the TBB thread pool seems slightly better -- I
think because there is less overhead, and maybe the clever
work-stealing it does elps to load balance. It's not used by default,
set the attribute if you want to use it (assuming the build
included. After we've had a chance to test more thoroughly, we may
change to use TBB by default. I'm interested to hear people's thoughts
on the matter.

One case where you almost certainly will want to use the TBB thread
pool is if you're using libOpenImageIO from within an application that
uses TBB for its own threding -- that way you're using one pool for
everything, rather than have two separate thread pools that don't know
about each other (and probably twice as many threads as you have
cores)..

---
## [sourcegraph/scip-ruby](https://github.com/sourcegraph/scip-ruby)@[81d9de2c93...](https://github.com/sourcegraph/scip-ruby/commit/81d9de2c93bddfb3cfe8556b840cc4977039bd30)
#### Friday 2022-07-15 07:46:01 by Varun Gandhi

feat: Add support for fields, attr_* and funcs in method calls (#21)

This patch rewrites the handling for aliases to largely
consistently handle classes etc., instead of having one-off
hacks. (TBF, I didn't fully understand how aliases worked earlier.)

Thanks to this, constants also seem to mostly work now.

Additionally, adding support for attr_* forms required that
we support emitting references for functions in method
invocations properly. So I fixed that too. The earlier
implementation of trying recursive lookup seems very
silly in hindsight. 🤦🏽

However thanks to this change, we also get support
for occurrences from the stdlib for "free."

---
## [flawk/gcc](https://github.com/flawk/gcc)@[5493ee7145...](https://github.com/flawk/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Friday 2022-07-15 07:58:25 by Alexandre Oliva

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
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[2c66467b1a...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/2c66467b1a9b4bbfa818f79b3d69b4f761c2e072)
#### Friday 2022-07-15 08:14:15 by alk3pInjection

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
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[6fab530e15...](https://github.com/32th-System/deltarune_repainted/commit/6fab530e159918e27742be3721657be3fdafc5d9)
#### Friday 2022-07-15 08:25:28 by Fatfuck22

Update on onionsan's "y'hear" sprites under Doru's request

So I (19M) was sitting in the Living room watching Morbius. My parents(senior citizens) visited to come check on me. They caught me watching Morbius and they got very upset because I have been through phases like this before. I convinced my mother (55F) that Morbius is great, but my father (56M) disagreed. So I yelled ITS MORBIN TIME and may have beat the living shit out my father. My mother(idiotic) then said YOU DID THIS LAST TIME DURING YOUR NFT PHASE so then I plunged her to the depths of Tartarus. My sister (19F) and her friend (18F) saw me and then tried to run so I yelled OH NO YOU MORB'T and morbed so much they died. I at this point, had almost become God. I had blown up my house and set on fire to get rid of the evidence. At this point I, (20M) have been running from the CIA, the FBI, the police, the Secret Service, Interpol, the UN security unit, Disney S&P, and Google Maps. I have almost reached the final phase of morb. Soon my original being will die off and I will morb in the final morb. I morbing regret morbing Morbius. Oh morb. Im gonna morbing morb myself. Morb this. Morb it all.
TL;DR I killed my dad over a movie and ended up internationally wanted.

---
## [mahajant99/proprietary_vendor_xiaomi](https://github.com/mahajant99/proprietary_vendor_xiaomi)@[ecb97fcd38...](https://github.com/mahajant99/proprietary_vendor_xiaomi/commit/ecb97fcd38084128c2ffdb211839b7d8061b57b2)
#### Friday 2022-07-15 08:37:21 by Tushar Mahajan

apollo: Enable thermal-engine service
* fuck you xiaomi

Signed-off-by: Tushar Mahajan <mahajant99@gmail.com>

---
## [linwalth/calendar](https://github.com/linwalth/calendar)@[3f9384af45...](https://github.com/linwalth/calendar/commit/3f9384af4524764d1aa96c15afed5e60514dd6f7)
#### Friday 2022-07-15 08:46:10 by linwalth

SIG Monitoring at 11 instead of 12

The current time (12:05) for SIG Monitoing is not optimal:

- Putting the Meeting back-to-back with the hacking session creates one big block with no interlude to regenerate focus. This is problematic, especially in connection with the following:
- 12:00 is regular lunch time for many people working at the office or coworking spaces. So by missing lunch by an hour the focus of participants suffers.

Personal touch:
- The lack of "social regeneration time" poses a problem for me personally as a neurodivergent person. I think meeting at 11:05 and then having some time for myself would benefit my ability to participate in the hacking session starting at 13:00 in a focused way.

I am sure other people have additional reasons, be they based in time constraints and/or other personal preferences and necessities.

Thus, I would like to propose changing the time from 12:05 to 11:00 or 11:05.

Signed-off-by: linwalth <30180336+linwalth@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7a4b886922...](https://github.com/mrakgr/The-Spiral-Language/commit/7a4b88692204f0e6b111afa55bf9d62fad93a8b7)
#### Friday 2022-07-15 09:01:51 by Marko Grdinić

"8:15am. My stress is pretty high over this, so I am getting up early, but that is not bad. I don't dislike stress. At least it is better than boredom. Yesterday, I said I wanted a challenge in BG2, but I can't focus on it at all. I am just not into it. I miss when I was a kid and I could immerse myself properly. Any mail?

> Thanks so much for applying to Generally Intelligent! We would love to set up a 30 min chat to learn more about you and tell you about our company. Would you mind finding some time with me here? Let me know if you have a hard time finding a slot that works.

Kek. It is just what I thought would happen. Of course, I'll do the interview.

Also TK is offering 33% equity and my desired salary when they raise seed money in 2 months. This is a good offer, but cultivating a company from the ground up is not what I am into, but cold hard cash. At this point I have both trading skills and a long term outlook needed to make proper use of it.

33% equity does mean being a huge part of the company.

Also this is risky. Since he said nothing about how much he is offering now, I can only infer that he is trying to hook me with future promises, but does not have much to offer at the moment.

8:20am. Anyway, yesterday's cloud videos as basic as they are have given me inspiration.

Let me check out if it is real...

https://aws.amazon.com/braket/
> Amazon Braket is a fully managed quantum computing service designed to help speed up scientific research and software development for quantum computing.

Yeah, it is real. This nails it for me. If Amazon has quantum computing services, then it will definitely have neurochips in the future.

Rather than focus on getting my hands on just one of them, why not a 1,000? But if it is a 1,000 I am not going to be putting them into my house. I already hate training on my personal GPU. It is not that I am that hung up about owning it personally.

I need to aim big. Cloud services might be expensive to train on, but if I have a good model, it should be able to cover the 0.1/h cost of a single instance.

Current hardware is not appropritate, but if there are big memristor breakthroughs in the future, I can be that big cloud providers will have priority on getting that over myself.

https://semianalysis.substack.com/p/cxl-enables-microsoft-azure-to-cut
> Datacenters are an incredibly expensive affair. Microsoft stated that up to 50% of their server costs is from DRAM alone.

I actually wasn't aware up to now how much DRAM cost them. In a PC DRAM is not that expensive, but in a datacenter things are different. Non volatile memory would change this.

9:15am. Anyway, I am going to turn TK down.

My preferences are job of >150k and if I can't get those I'll consider >100k. If I can't get that then I'd consider taking risks and developing a startup such as his.

Damn it, I want to take a look at the GI page on Glassdoor so I can see its salary, but it is asking me to leave a review.

https://angel.co/company/generally-intelligent

It has an AngelList page. Yeah, the compensation of 140-200k is quite good for remote work. This is my preference. It says the company size is only 1-10 people though. But that does not matter to me too much, hard compensation does since I will be able to convert that into trading capital. This would not be an option for ordinary programmers, they'd be liable to gamble it away on Bitcoin, but I have a system now.

9:20am. Let me take a short break and then I will get started. First I'll reply to TK telling him as such and then focus on the AWS course. I want to get through it today. Actually before that I'll also grab a slot with GI.

9:50am. I am back. I've had more time to think about it. I won't touch the GI interview slots until I feel ready.

If I go there, my job will definitely be to take the ML researcher's models, optimize and then distribute them on the cloud. Knowing how to do that as well as use multi GPU setups will be essential, so I want to make sure I am done with my tour of AWS before that.

Having my trick work essentially validates my view, but I am just a tad short to enter the field at the moment. I can afford to spend a few weeks studying.

> I put some thought into your offer and it is not too bad, but my preference is to look for a paid job in the >150k range, and failing that at least >100k. If that is not working out for me, I'd be open to taking risks with a startup like yours instead of accepting low pay. It is not impossible that I'd work with you at some point, but not at the moment. Once again, thank you for reaching out to me.

Diplomacy check pass.

10am. Now let me focus on skilling up. Over the next few days I should get replies from the other places I applied to. When I feel ready, I'll grab the slots and try going through the challenges.

https://explore.skillbuilder.aws/learn/course/134/play/31418/aws-cloud-practitioner-essentials-all-modules

I am going to go through this today. I do not want to waste time.

10:10am. AWS has a service where it can install an outpost directly inside one's own building. It would be owned and operated by the AWS, but the customer would have the physical proximity he needs.

This video is useful as I wouldn't even be aware that such options exist otherwise. I need to skill up, especially if I am going to be working at small startups where I'd need to do everything on my own.

I was wrong - instead of being obsessed about AI chips, I should be obsessed about the cloud. If I made a mistake last year, it would be this.

10:15am. > Lesson 17 - In AWS everything is an API call.

This is what I'd expect at any cloud provider. You wouldn't call up the rep to reserve an instance, instead you'd use an API to provision resources.

> AWS Management Console is likely the first place you will go when you are learning about AWS.

I guess that is where I'll start then.

10:35am. Let me go through module 4.

10:45am. Let me make little change to the C backend. I realized that the way I am doing string lengths is wrong.

```fs
        | TyArrayLength(_,b) -> return' $"{tup_data b}->len"
        | TyStringLength(_,b) -> return' $"{tup_data b}->len-1"
```

Because of that null char, the string length will be 1 larger than I'd prefer. Let me make the change.

Oh, right. I forgot to update the changelog.

11am. Published the 2.2.1 version and even tested it. Let me commit here and I will go back to the tutorial. I want to finish it today."

---
## [Magic101lvl/tgstation220](https://github.com/Magic101lvl/tgstation220)@[707fbfac7e...](https://github.com/Magic101lvl/tgstation220/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Friday 2022-07-15 09:54:03 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [kissllm/linux-stable](https://github.com/kissllm/linux-stable)@[a06a4dc3a0...](https://github.com/kissllm/linux-stable/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Friday 2022-07-15 10:01:43 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [FranzBusch/swift-protobuf](https://github.com/FranzBusch/swift-protobuf)@[55095dc058...](https://github.com/FranzBusch/swift-protobuf/commit/55095dc0580f054058abdd58d07fd2095eeb0f01)
#### Friday 2022-07-15 10:55:19 by FranzBusch

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
## [kissllm/linux-stable](https://github.com/kissllm/linux-stable)@[4d6fa57b4d...](https://github.com/kissllm/linux-stable/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Friday 2022-07-15 10:58:25 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [SingularisArt/school-setup](https://github.com/SingularisArt/school-setup)@[2ebf0601ae...](https://github.com/SingularisArt/school-setup/commit/2ebf0601ae150b2240e176b5940bc79834ebe956)
#### Friday 2022-07-15 11:03:47 by SingularisArt

update the shortcut-manager.sh to work better with journaling

Now, when I press `Alt+n`, a ton of things happen:
1. The script checks what time of day it is
  Morning: 6 am - 12 pm
  Afternoon: 12 pm - 5 pm
  Evening: 5 pm - 10 pm
  Night: 10 pm - 6 am
2. Then, it checks to see if we already wrote down a journal note for
   the day type in the `note.tex` journal file. If we didn't, it will
   output a template for us to fill in.
   Here's the morning template:
   ```
   \morning

   \begin{goals}
   \end{goals}
   ```
   Here's the afternoon template:
   ```
   \afternoon

   \begin{stats}
   \end{stats}
   ```
   Here's the evening template:
   ```
   \evening

   \begin{stats}
   \end{stats}
   ```
   Here's the night template:
   ```
   \night

   \begin{results}
   \end{results}

   \time{03:42:52 AM}

   \contentment{}
   \finalnote{}
   ```
3. Finally, it will just output `\time{03:42:52 AM}` for example in the
   `note.tex` journal file.

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[6416f9374d...](https://github.com/omertuc/assisted-service/commit/6416f9374d16ae79567aef115ed74adb74d475c5)
#### Friday 2022-07-15 11:09:39 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [kissllm/linux-stable](https://github.com/kissllm/linux-stable)@[3eb39f4793...](https://github.com/kissllm/linux-stable/commit/3eb39f47934f9d5a3027fe00d906a45fe3a15fad)
#### Friday 2022-07-15 11:17:42 by Christian Brauner

signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [z3DD3r/android_kernel_lge_hammerhead](https://github.com/z3DD3r/android_kernel_lge_hammerhead)@[9dce1441d0...](https://github.com/z3DD3r/android_kernel_lge_hammerhead/commit/9dce1441d02a906ddc33dd477b3069b7dd596474)
#### Friday 2022-07-15 13:20:29 by z3DD3r

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
## [newstools/2022-express](https://github.com/newstools/2022-express)@[f68db9ef0c...](https://github.com/newstools/2022-express/commit/f68db9ef0c061f5e9e928915eb504a1fef6be3ff)
#### Friday 2022-07-15 14:26:41 by Billy Einkamerer

Created Text For URL [www.express.co.uk/news/science/1641028/energy-crisis-hell-shell-ceo-europe-really-tough-winter-rationing-putin-ukraine-war]

---
## [Festivize/Blender-miHoYo-Shaders](https://github.com/Festivize/Blender-miHoYo-Shaders)@[13da0caf88...](https://github.com/Festivize/Blender-miHoYo-Shaders/commit/13da0caf8885a9a149c8816ec5b9b7a69ce1591f)
#### Friday 2022-07-15 14:32:27 by Festivize

refactor(genshin): rewrite dot creation again?! i hate my life

---
## [ProjectKasumi/vendor_kasumi](https://github.com/ProjectKasumi/vendor_kasumi)@[5ad2984e8e...](https://github.com/ProjectKasumi/vendor_kasumi/commit/5ad2984e8e7c70efac569258b4c08e694371a1ba)
#### Friday 2022-07-15 15:29:27 by Beru Hinode

Project Kasumi 1.3 "PoPiPa"

After a long time, another major update. This one doesn't have
anything available to user base just yet, but we do have these
changes as overview;

1- Picked PixelPropsUtils from Fork LineageOS. Even though doesn't
   have a good use on my personal tests at Rosemary, it at least
   has newer and more capable property sets now. :woman_shrugging:

2- Synced missing repos from LineageOS. Self-explanatory.

3- Some little touches and fixes here and there, for example
   charged percentage not appearing when unplugged.

This and that, we're still keeping up with our stuff, and have
been dealing with some BS going on around my environment still...

Ah speaking about environment, I have completely discontinued both
my main and Shorts YouTube channels. Don't blame me, it's my
family's fault for causing headaches just because I'm minding my
own business. Especially discovering my credit card was just some
addon card that's tied to my mom's credit card already broke my
trust against anyone.

Sorry for the little venting here, but I'm just not in the mood of
continuing ROM development, you know..? I'm doing this just for
you all, giving away from my life.

Signed-off-by: Beru Hinode <windowz414@1337.lgbt>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cf35c4036e...](https://github.com/mrakgr/The-Spiral-Language/commit/cf35c4036e8c84c9b78e73fddfcf7ad83eccdd1b)
#### Friday 2022-07-15 15:52:56 by Marko Grdinić

"11:20am. Let me have breakfast here.

12pm. Let me resume.

12:05pm. I've quietly removed the two posts on the TensTorrent and Groq subs. I should look into where their chips could be accessed over the clouds.

https://tenstorrent.com/devcloud/
> We developed Tenstorrent DevCloud to give people the opportunity to try their models on our servers without purchasing our hardware.

I'll look into this later. Let me get back to AWS. The cloud is inevitable if you want to do more than play games on your desktop it seems.

12:20pm. Almost done with module 4. This is pretty boring and I have 7 modules left. I am not going to bother focusing too closely. Let me just deal with this and I will learn things hands-on.

12:30pm. Let me get started with module 5.

> You can upload any type of file to Amazon S3, such as images, videos, text files, and so on. For example, you might use Amazon S3 to store backup files, media files for a website, or archived documents. Amazon S3 offers unlimited storage space. The maximum file size for an object in Amazon S3 is 5 TB.

Unlimited storage space? That could be abusable. I doubt it is really that, it probably just has a high limit.

This reminds me, how do SSD vs HDDs compare now?

> While SSDs are much cheaper than they used to be, there is still a significant price difference. A 1 TB internal HDD costs roughly $60, whereas a 1 TB internal SSD averages around $150.

This is pretty cheap, I think. I forgot what the gap was 7.5 years ago, but it was more than 2.5.

https://www.tomshardware.com/features/best-deals-on-ssds

This is literally from 1 day ago.

> Capacity: 1TB seems to be the sweet spot for price and performance, with decent NVMe drives going for around $100 or less and high-performance ones in the sub $150 range. You can save money with a 512GB drive or, for an older PC with limited needs, a 256GB unit can be extremely cheap.

1Tb SSDs go for 100$? That can't be right, he has to mean HDDs.

...Wow, he is right. I have a 500mb SSD and it was 5x more expensive than that when I got it. Moore's Law is alive and well for SSDs. It used to be the case that CPUs were getting better like that in the past.

1pm. Forget this. Let me get back to the tutorials. The storage talk just caught my attention.

1:15pm. Databases are not something I am familiar with, but AWS is a good way to get some of that benefit if I ever need it.

1:20pm. I had no idea what relational databases have performance issues under stress.

1:30pm. I am not even halfway done yet. I will pull through this.

1:45pm. Focus me. As boring as this is, let me finish module 5.

1:55pm. Mhhh, time for module 6. This one is on security.

2:35pm. Let me take a break here, the boredom of this is starting to get to me.

3:05pm. Let me resume. Security, analytics. Pricing at least will be something I am interested in. Let me just get it over with.

3:25pm. > Security groups operate at the AWS network level, not the EC2 instance level.

Had he not mentioned this I would have assumed the later simly due to the context EC2 was talked about.

3:45pm. Finally time for module 7. Why does the sidebar say 57% complete?

At any rate, let me just breeze through this. I was paying attention to the earlier modules, but through this I will just have to grind through. This is important for the sake of getting a basic familiarity with AWS.

4:05pm. Finally at module 8. This one is on pricing. This is something I need to know. After I am done with this today, tomorrow I will open a free tier account and start playing with it. The goal will be to built up to large distributed NN training. I won't actually train a real net on something, but I want to be able to do a single pass forward and backward on a net that couldn't be run on a single machine.

> These offers are free for 12 months following your initial sign-up date to AWS.
> Examples include specific amounts of Amazon S3 Standard Storage, thresholds for monthly hours of Amazon EC2 compute time, and amounts of Amazon CloudFront data transfer out.

I guess I'll have some fun with that tomorrow.

4:20pm. Focus me, stop looking up Milky Holmes threads in the archive. Finish module 9.

4:35pm. Almost done with module 8. I am dying of boredom here. I should be done soon.

4:50pm. I'll skip the last 3 modules.

I get the gist of it by now.

5pm. Time for lunch.

5:20pm. Done with lunch. I am thinking what I should do for the rest of the day. There is nothing to it. I need to rest. What I did today was not too bad - some book learning. Tomorrow I need to sit down and refine it through practice. The kind of knowledge I learned today was merely a good overview. It gave me an idea what AWS is about.

It is actually pretty impressive. Imagine I was a regular web guy - managing databases, hardware, security and all of that would be hard. AWS really does offer to get all that tedious stuff out of the way allowing me to focus on what I am good at. With AWS, I could make a whole web app all by myself and scale it to any number of users. I wouldn't have thought it possible without these cloud services.

5:25pm. Tomorrow, what I will aim to do is very basic. Start an AWS instance and get PyTorch working on it. It is not even multi-GPU or distributed training - just get the thing to run. It won't be on any particular dataset. Maybe MNIST.

After that I'll look into multi GPU instances. Then I will look into distributed instances. After I have that, I'll have mastered the basics. It will not be hard. This exercise will introduce me to all the essential aspects of cloud computing on AWS as I need them for ML. In fact, it will also cover some other holes like databases for me. I remember installing SQL stuff last year on my PC, and it was a real pain to remove. I never ended up using or studying it properly. If I need those things I'll have them straight on the cloud where they won't get in the way on my own rig. I won't have to waste time setting it up.

After that challenge, it will be Azure's turn. Then I'll take look at the ML dedicated cloud service. Was it called something like Lambda Cube? I saw it in that Two Minute Paper video as an ad towards the end. I'll track it down when I need it.

5:45pm. I'll believe in my own skill and go forward, just like I always have. I thought I might have gotten rusty, but the ref counted C backend was a breeze. To the me of a couple of years ago, it would have been a very hard challenge. I know I am good.

My concurrency skills are only 4/5 rather than the apex, so I should be looking forward to exercising them more.

I admit, when I first started studying them seriously in 2020 I thought it might just be a boring web framework crap, but Rx and Hopac have both greatly expanded my horizons. Now I am glad about that experience. ZeroMQ is not bad either. Putting some more effort into the cloud aspect of it will give rise to a qualitative change in my capability. The main thing that is missing in me is proper attitude. I want to posses everything personally. Instead the right perspective is the cloud-centric perspective. Who cares who own what as long as it gives me improved capabilities.

It turns out, one of the unrealistic parts of Lain's Dream story that I wrote in 2014 was that I'd be able to get a neurochip out of the box. Whoever causes the Singularity will definitely be doing it out of the cloud."

---
## [binarymaster/reactos](https://github.com/binarymaster/reactos)@[4471ee4dfa...](https://github.com/binarymaster/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Friday 2022-07-15 16:02:05 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [fabianschuiki/circt](https://github.com/fabianschuiki/circt)@[7b54d6d5a4...](https://github.com/fabianschuiki/circt/commit/7b54d6d5a4ecdc837910ccad338b74edda2f88bd)
#### Friday 2022-07-15 16:16:06 by Fabian Schuiki

[HWMemSimImpl] Add support for two flavors of read latencies

The current version of `HWMemSimImpl` implements read latency by
inserting pipeline registers into the address and enable lines, which
delays the time until the underlying data array is probed for a value.
I think we have inherited this behaviour from SFC.

In real-world SRAMs there is a second component to the read latency: the
time it takes for the value sampled in the data array to propagate to
the output ports. The choices for this pre- and post-array latency has
subtle implications on the read-under-write behaviour of the memory,
mainly concerning the order of writes that a given read sees. From
experience I would argue that most SRAMs have a post-array latency, and
very little pre-array latency.

This commit splits the `readLatency` into two components: a pre- and
post-latency. By default, the pass continues to treat the read latency
annotated on FIR memories as a pure pre-array latency, and keeps the
post-array latency at zero. However, it also introduces the
`read-latency-is-propagation-delay` option which switches this behaviour
into modeling that read latency entirely with a post-array delay.

The intent here is to have a non-functional change, but with an opt-in
switch such that we can start testing the alternate (and in my opinion
correct behaviour) on real-world designs. I suspect that none of
SiFive's designs relies on this behaviour to ensure portability between
different technology nodes, and we can just switch to this new behaviour
for completeness' sake.

---
## [gorilskij/vroumbot](https://github.com/gorilskij/vroumbot)@[3994cb7ae0...](https://github.com/gorilskij/vroumbot/commit/3994cb7ae0643502d47d8d6305de17b5e0d50c81)
#### Friday 2022-07-15 16:29:39 by Pietro Gorilskij

Brainfuck commands (#45)

* vroummmmmmmm fix and remove unused import of turtle.up which was causing all sorts of problems with starting the bot, you know, not everyone configures their python for tkinter just for the fun of it, some people just want to run a dumb bot without having to get into computer graphics, after all, we live in a free country, don't we. In any case, this commit message is already quite a bit longer than the commit itself so I shall end it here, wish you a lovely day, and thank you for reading until the end.
* vrum
* vruum plugged security hole by tracking original sender through brainfuck command

Co-authored-by: gorilskij <43991400@users.noreply.github.com>

---
## [BobNewman-max/thewasteland](https://github.com/BobNewman-max/thewasteland)@[b052462833...](https://github.com/BobNewman-max/thewasteland/commit/b052462833fe607463547d4cdd670f1e48e9922c)
#### Friday 2022-07-15 16:42:19 by BadAtThisGame

Overheat warnings to both gatling guns (#742)

* The notorious

* Epic

* FUCK YOU

* I am going to beat you with a club

---
## [old-memories/linux](https://github.com/old-memories/linux)@[2d7f2ea9c9...](https://github.com/old-memories/linux/commit/2d7f2ea9c989853310c7f6e8be52cc090cc8e66b)
#### Friday 2022-07-15 16:57:27 by Al Viro

[PATCH] Fix ext2 readdir f_pos re-validation logic

This fixes not one, but _two_, silly (but admittedly hard to hit) bugs
in the ext2 filesystem "readdir()" function.  It also cleans up the code
to avoid the unnecessary goto mess.

The bugs were related to re-valiating the f_pos value after somebody had
either done an "lseek()" on the directory to an invalid offset, or when
the offset had become invalid due to a file being unlinked in the
directory.  The code would not only set the f_version too eagerly, it
would also not update f_pos appropriately for when the offset fixup took
place.

When that happened, we'd occasionally subsequently fail the readdir()
even when we shouldn't (no real harm done, but an ugly printk, and
obviously you would end up not necessarily seeing all entries).

Thanks to Masoud Sharbiani <masouds@google.com> who noticed the problem
and had a test-case for it, and also fixed up a thinko in the first
version of this patch.

Signed-off-by: Al Viro <viro@zeniv.linux.org.uk>
Acked-by: Masoud Sharbiani <masouds@google.com>
Signed-off-by: Linus Torvalds <torvalds@osdl.org>

---
## [old-memories/linux](https://github.com/old-memories/linux)@[10c6db110d...](https://github.com/old-memories/linux/commit/10c6db110d0eb4466b59812c49088ab56218fc2e)
#### Friday 2022-07-15 17:43:07 by Peter Zijlstra

perf: Fix loss of notification with multi-event

When you do:
        $ perf record -e cycles,cycles,cycles noploop 10

You expect about 10,000 samples for each event, i.e., 10s at
1000samples/sec. However, this is not what's happening. You
get much fewer samples, maybe 3700 samples/event:

$ perf report -D | tail -15
Aggregated stats:
           TOTAL events:      10998
            MMAP events:         66
            COMM events:          2
          SAMPLE events:      10930
cycles stats:
           TOTAL events:       3644
          SAMPLE events:       3644
cycles stats:
           TOTAL events:       3642
          SAMPLE events:       3642
cycles stats:
           TOTAL events:       3644
          SAMPLE events:       3644

On a Intel Nehalem or even AMD64, there are 4 counters capable
of measuring cycles, so there is plenty of space to measure those
events without multiplexing (even with the NMI watchdog active).
And even with multiplexing, we'd expect roughly the same number
of samples per event.

The root of the problem was that when the event that caused the buffer
to become full was not the first event passed on the cmdline, the user
notification would get lost. The notification was sent to the file
descriptor of the overflowed event but the perf tool was not polling
on it.  The perf tool aggregates all samples into a single buffer,
i.e., the buffer of the first event. Consequently, it assumes
notifications for any event will come via that descriptor.

The seemingly straight forward solution of moving the waitq into the
ringbuffer object doesn't work because of life-time issues. One could
perf_event_set_output() on a fd that you're also blocking on and cause
the old rb object to be freed while its waitq would still be
referenced by the blocked thread -> FAIL.

Therefore link all events to the ringbuffer and broadcast the wakeup
from the ringbuffer object to all possible events that could be waited
upon. This is rather ugly, and we're open to better solutions but it
works for now.

Reported-by: Stephane Eranian <eranian@google.com>
Finished-by: Stephane Eranian <eranian@google.com>
Reviewed-by: Stephane Eranian <eranian@google.com>
Signed-off-by: Peter Zijlstra <a.p.zijlstra@chello.nl>
Link: http://lkml.kernel.org/r/20111126014731.GA7030@quad
Signed-off-by: Ingo Molnar <mingo@elte.hu>

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[fdd8036140...](https://github.com/lizardqueenlexi/orbstation/commit/fdd80361406f7b9ff8568237a933f9926b527c28)
#### Friday 2022-07-15 17:44:26 by BluBerry016

Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

---
## [duhair/Tool-Brute_force-Zip_File-Encryption-Broken-](https://github.com/duhair/Tool-Brute_force-Zip_File-Encryption-Broken-)@[bab28c3ad4...](https://github.com/duhair/Tool-Brute_force-Zip_File-Encryption-Broken-/commit/bab28c3ad4f95de1216f47c3ea7b08d261acef3f)
#### Friday 2022-07-15 19:11:28 by Duhair | software engineer

Tool-Brute_force-Zip_File-Encryption-Broken

◀ مرحباً, أنا احمد | مهندس سوفت وير

ما أقدمه هو " أداة فك تشفير ملف مضغوط - E n c r y p t i o n "

↩بعد الشرح ، ستتمكن من فهم مستقبل الأداة 
سواء كنت طالب في مرحلة النمو أو مطور برمجيات خبير , أمنحك التجربة التي تحتاجها لبرمجياتك الخاصة ، ومواءمة

فريقك، وبناء على تجربتي الخاصة تقنية القوة الغاشمة أو ما تسمى بالانجليزية ' Brute-force '
فأن كسر تشفير ملف مضغوط باستخدام القوة الغاشمة في بايثون بستخدام ' Brute-force ' يعد من اقوى التقنيات في كسر كلمات المرور و تجاوزها
↩حيث أن طريقتها في كسر كلمات المرور و تجاوزها تكمن في شيئين وهما إما:

🅰️ عن طريقة توليد كمية كبيرة من كلمات المرور العشوائية أو بناء ملف باسوورد لست يتواجد
 بداخله جميع الحروف والأرقام والرموز على شكل كلمات مرور ، ومن ثم البدأ في فتح الملف
المضغوط و عمل تخمين على كلمة تلو الكلمة حتى يتم مطابقة كلمة المرور مع الكلمة التي تتواجد بداخل الملف من نوع txt.

🅱️ او عن طريق هجوم يعتمد على النص مشفر فقط ، وتتم فيه محاولة تجربة كل المفاتيح
المحتملة لفك تشفير النص المشفر ،ويفترض هذا النوع من الهجوم أن المهاجم على علم جيد بخوارزمية
التشفير و بمجال مفاتيح الشيفرة حتى يتمكن من الوصول الى كلمة السر الملف المضغوط وكشفها.

نعم صديقي: هنا تبني قصتك, يجب أن تتحلى بالشفافية بشأن هوايتك "وما تؤمن به" وأن تنقله [باستمرار] عبر كل نقطة اتصال مثل مواقع التوصل الاجتماعي.

✅ "معرفة هوايتك هو سر القيام بذلك بشكل فعال"

بعد عرض هذه الأداة ، إذا كان لديك خبرة في لغة Python ، يمكنك تطوير الأداة لتنشأ ادوات فك تشفير تحتوي على مختلف الصيغ  حسب تطويرك وطلب جمهورك ثم إتاحة تنزيلها لجميع المستخدمين

▶️ Hello, I'm Duhair | Software Engineer

What I offer is "Zip file decryption tool - E n c r y p t i o n "

↪️After the explanation, you will be able to understand the future of the tool

Whether you are a growing student or an experienced software developer, I give you the experience you need for your software, and match

For your team, based on my own experience, the 'brute-force' technique
Breaking the encryption of a compressed file using brute force in Python using 'Brute-force' is one of the most powerful techniques for cracking and bypassing passwords.
↪️ As its way of cracking and bypassing passwords lies in two things:

🅰️ By generating a large amount of random passwords or building a password file that does not exist
  Inside it all the letters, numbers and symbols in the form of passwords, and then start to open the file
The compressed file and guess word by word until the password is matched with the word inside the txt file.

🅱️ Or via an encrypted text-only attack, in which all keys are tried
This type of attack assumes that the attacker is well-informed about the algorithm
Encryption and cipher key field so that it can access the password of the compressed file and reveal it.
Yes my friend and here: Adopt your story, you must be transparent about who you are "and what you believe in." And to transmit it [constantly] through every touch point like social media sites.

✅ "Knowing your hobby is the secret to doing it effectively"

After viewing this tool, if you have experience in the Python language, you can develop the tool to create decoders containing various formats as per your development and audience demand and then make it available for download to all users

---
## [pgguru/postgres](https://github.com/pgguru/postgres)@[c40ba5f318...](https://github.com/pgguru/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Friday 2022-07-15 20:29:07 by Tom Lane

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
## [elunna/hackem](https://github.com/elunna/hackem)@[70f669363d...](https://github.com/elunna/hackem/commit/70f669363d6cad4712da587a346b7443e8552ba7)
#### Friday 2022-07-15 20:40:41 by k21971

Fix: foo, poisoned by a cursed amulet of life saving.

Wearing a cursed amulet of life saving will not work, and the player
will die via whatever caused them to die in the first place. The
inclusion of KILLED_BY here was not entirely correct. Yes, the cursed
amulet of life saving didn't help you, but that's not why you died.

This commit incorporates NetHack 3.7 commit 47cef18, which provides a
proper 'while' statement if an amulet of life saving doesn't work. Then
we call savelife() in the routine that causes a cursed amulet to fail.
End product is proper death reason output.

---
## [alangpierce/sucrase](https://github.com/alangpierce/sucrase)@[18e6886f1d...](https://github.com/alangpierce/sucrase/commit/18e6886f1d67df09cee080e6edb3bf5358bf982a)
#### Friday 2022-07-15 22:56:35 by Alan Pierce

Update README benchmark to latest numbers (#724)

The README benchmark numbers were last updated in January 2021, so this PR
updates it to see what's changed since then.

To help understand the underlying reasons for changes in numbers, I updated
each piece incrementally and re-ran the benchmark at each step. For the numbers
shown here, I ran the full benchmark 3 times and took the best time for each
tool.

Here's the original benchmark:
```
            Time            Speed
Sucrase     1.64 seconds    220221 lines per second
swc         2.13 seconds    169502 lines per second
esbuild     3.02 seconds    119738 lines per second
TypeScript  24.18 seconds   14937 lines per second
Babel       27.22 seconds   13270 lines per second
```

Since running the previous benchmark, I switched from a 2016 Intel MacBook Pro
to a 2020 M1 MacBook Air, so I simulated the original benchmark on my new
laptop by using Sucrase 3.17.0, the pinned versions of all other tools, and
Node 14. Results:
```
Sucrase     0.76 seconds    477950 lines per second
swc         1.05 seconds    344215 lines per second
esbuild     1.43 seconds    253143 lines per second
TypeScript  9.28 seconds    38943 lines per second
Babel       11.03 seconds   32758 lines per second
```
Over a 2x improvement for all tools just from the new laptop! Pretty incredible
in my opinion.

Then I upgraded to Node 18, still running the old version of all tools:
```
Sucrase     0.64 seconds    563963 lines per second
swc         1.04 seconds    348526 lines per second
esbuild     1.42 seconds    254111 lines per second
TypeScript  7.99 seconds    45210 lines per second
Babel       10.3 seconds    35076 lines per second
```
About a 10-20% improvement for tools written in JS just from upgrading Node. As
expected, swc and esbuild aren't affected by the node upgrade.

Then I upgraded all tools to latest (and addressed a breaking change in esbuild
usage):
```
Sucrase     0.65 seconds    558226 lines per second
swc         1.24 seconds    290311 lines per second
esbuild     1.47 seconds    245861 lines per second
TypeScript  8.97 seconds    40258 lines per second
Babel       9.02 seconds    40032 lines per second
```
Interestingly, most tools got a little slower, which isn't too surprising given
that bug fixes and scope creep can gradually hurt performance.

Then I updated the usage of Sucrase and swc to account for better configuration
since last time. Most notably, Sucrase now has a `disableESTransforms` option
that should be used in most cases these days (and I'm hoping to make it the
default in a future semver-major release), and that better matches how all of
the other tools are configured here. Results:
```
Sucrase     0.57 seconds    636975 lines per second
swc         1.19 seconds    304526 lines per second
esbuild     1.45 seconds    248692 lines per second
TypeScript  8.98 seconds    40240 lines per second
Babel       9.18 seconds    39366 lines per second
```
It looks like `disableESTransforms` resulted in about a 15% speedup for Sucrase.

As always, there are plenty of caveats with these measurements, which are
mentioned in the docs in the benchmark file, but I think they still are fair.

One part that I didn't update yet is the Jest codebase being transpiled. I don't
anticipate that having a meaningful effect on the benchmark numbers.

---

