## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-17](docs/good-messages/2022/2022-02-17.md)


1,712,302 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,712,302 were push events containing 2,767,303 commit messages that amount to 206,629,043 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [rain2wood/amaoto](https://github.com/rain2wood/amaoto)@[19984342b8...](https://github.com/rain2wood/amaoto/commit/19984342b823a3a0e140b682610bc8393dfa9ad7)
#### Thursday 2022-02-17 00:04:01 by Wang Han

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
Signed-off-by: Wiley Lau <henloboii@protonmail.ch>

---
## [Horatio22/fulpstation](https://github.com/Horatio22/fulpstation)@[c449fbb56c...](https://github.com/Horatio22/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Thursday 2022-02-17 00:38:41 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [RogerThiede/Stockfish](https://github.com/RogerThiede/Stockfish)@[cb9c2594fc...](https://github.com/RogerThiede/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-02-17 00:45:53 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[a045e87e07...](https://github.com/CleverRaven/Cataclysm-DDA/commit/a045e87e07b9208bc9c46e3f3f1e2281e39b4ed4)
#### Thursday 2022-02-17 00:46:04 by Mylie

Artifact improvements and artifact debug QOL (#54837)

* Artifacts can now have enchantment::has specified

- Artifacts can now have enchantment::has (aka where they apply from, be it while worn, while wielded, or even while carried in a bag) specified for each individual enchantment entry- except for the activated effect, which logically remains wield-only as you can only activate it while wielding the artifact.
- This does work for hit_me and hit_you effects, for any amazing things that can be done with an object that casts magic from your backpack when you punch something.
- In addition, one misleading error message was reworded, and artifacts no longer have a niche case that causes num_attribute to increase without actually adding an attribute.

* Expand artifact spawning functions, add example monolith artifacts

- map::spawn_artifact now supports specification of max_attributes, power_level, and max_negative_power.
- Added example (but hopefully actually usable) artifact procgen data for artifacts that are still effective while held in a bag or pocket or thermos or whatever
- Debug spawning of artifacts vastly expanded, now supports selection of group, max attributes, power level, and max negative power for a fully customizable artifact testing experience!
- Added new material for artifacts, Monolith, which exists to provide easier support for artifacts being quite sturdy, and added two artifacts made from it that tie to the new example artifact category

Co-authored-by: Binrui Dong <brett.browning.dong@gmail.com>

---
## [Harrand/Topaz](https://github.com/Harrand/Topaz)@[a2aed74da0...](https://github.com/Harrand/Topaz/commit/a2aed74da0a8d04c1c1f032f9f082a24a4df166d)
#### Thursday 2022-02-17 00:47:38 by Harrand

- Removed ResourceAccess::StaticVariable. If you want your resources to be variable-size, you're gonna have to pay the perf cost of having it dynamic too, fuck you

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[35dfe36042...](https://github.com/zx2c4/linux-rng/commit/35dfe360421e060830af62a0fbf868b4186974c9)
#### Thursday 2022-02-17 01:56:44 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a *max-period* linear function fits
this bill quite well, easily extending to the larger state size and to
the fact that we're mixing in more than just the cycle counter. By
picking one that is max-period, there are no non-trivial invariant
subspaces, unlike NT's rotate-xor, which means we benefit from the
analysis of <https://eprint.iacr.org/2021/1002>. This paper gives proofs
that linear functions with only trivial invariant subspaces make very
good entropy extractors for the type of complex distributions that we
have, and suggests that we extract entropy via S←AS⊕X, where S is our
pool vector, X is the new interrupt data vector, and A is the
transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period with
no non-trivial invariant subspaces, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [git/git](https://github.com/git/git)@[07564773c2...](https://github.com/git/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Thursday 2022-02-17 01:59:40 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[e67a6c8c6a...](https://github.com/zx2c4/linux-rng/commit/e67a6c8c6ad26f13e7e49792455b0117a047414a)
#### Thursday 2022-02-17 02:10:39 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear function fits this
bill quite well, easily extending to the larger state size and to the
fact that we're mixing in more than just the cycle counter. By picking a
linear function with no non-trivial invariant subspaces, unlike NT's
rotate-xor, we benefit from the analysis of <https://eprint.iacr.org/2021/1002>.
This proves that linear functions with only trivial invariant subspaces
make very good entropy extractors for the type of complex distributions
that we have. It suggests that we extract entropy via S←AS⊕X, where S is
our pool vector, X is the new interrupt data vector, and A is the
transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period with
no non-trivial invariant subspaces, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [OceanFish1/Skyrat-tg](https://github.com/OceanFish1/Skyrat-tg)@[1f70226654...](https://github.com/OceanFish1/Skyrat-tg/commit/1f70226654438f75811a2d59ad9c52bf88c048fc)
#### Thursday 2022-02-17 02:19:29 by SkyratBot

[MIRROR] Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit [MDB IGNORE] (#11027)

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [wvanrensselaer/next.js](https://github.com/wvanrensselaer/next.js)@[91146b23a2...](https://github.com/wvanrensselaer/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Thursday 2022-02-17 03:46:00 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [lsw3961/SonOfHermes](https://github.com/lsw3961/SonOfHermes)@[57876d5f23...](https://github.com/lsw3961/SonOfHermes/commit/57876d5f23b34f0dfc91d40e04a75ee7f8784b19)
#### Thursday 2022-02-17 04:00:51 by Logan White

WOOOO I spent 2 nights on it but finally got the dash working at a set distance

Pretty cool but finally cracked the bug for dash distance. Vector math kills me sometimes but wooo boy did figuring it out feel good. Bless the French! anyway, now that thats done were moving on to making it feel good. So the next step is to add all the cool stuff that goes along with the dash. ie animation, particle effects, screenshake. also make sure that you can only dash in the air once. after that we should have all the pieces for a killer player controller.

---
## [TopDogCORS/assets](https://github.com/TopDogCORS/assets)@[f983562c4b...](https://github.com/TopDogCORS/assets/commit/f983562c4b8e887ad701a2291c49020dd3be787e)
#### Thursday 2022-02-17 04:11:02 by TopDog

Uploading my first token

CorsoCoin looks to establish a dominant position in the market. There is nothing special about this token except for the hope of the developer in his peers.
    Since the division of jobs in the tribal society many have been the faces of a token. People have been swapping fish for eggs, jewellery for freedom in times of war and jewellery for love in all times. We live a new era.
     Inspired by the Cane Corso breed out of Italy I am bringing to you one more deflationary coin with a very determined master.

---
## [SaintPatricksGitcoinGang/LibAFL](https://github.com/SaintPatricksGitcoinGang/LibAFL)@[a0ce4cfd68...](https://github.com/SaintPatricksGitcoinGang/LibAFL/commit/a0ce4cfd68ef3ab428d2e8398030c83e6992cc45)
#### Thursday 2022-02-17 04:42:22 by Dominik Maier

Ignored qemu fuzzer for non-linux (#397)

* ignored qemu fuzzer for non-linux

* fixed cfg

* ignore rm -rf errors in make short_test (fuck you macos)

Co-authored-by: Andrea Fioraldi <andreafioraldi@gmail.com>

---
## [Jcelestra03/SparkProject](https://github.com/Jcelestra03/SparkProject)@[031bfc8d21...](https://github.com/Jcelestra03/SparkProject/commit/031bfc8d21fb67b2831c433da4acc2ea2182e094)
#### Thursday 2022-02-17 05:49:04 by Jeremiah Celestra

Update jem testing.unity

Blockchange completed, while making it work i hated my life. Earlier this night i went to a choir Recital of my friends. I felt alone watching it because i didn't know anyone at the recital plus i sat alone
by the time the recital ended i saw my friend he was talking with his fellow choir people and i just left in a hurry , on the 20 min car ride back i kept thinking how useless i was, the stench of my existence is a means to get out of the way of other people , a source where i hate myself for it and love myself

---
## [TheNeoGamer42/Shiptest](https://github.com/TheNeoGamer42/Shiptest)@[5e29827ceb...](https://github.com/TheNeoGamer42/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Thursday 2022-02-17 06:15:21 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [noah-nuebling/mac-mouse-fix](https://github.com/noah-nuebling/mac-mouse-fix)@[db3a695fa9...](https://github.com/noah-nuebling/mac-mouse-fix/commit/db3a695fa9bee1d3c373ebf26fbdec6bd5a2a6fd)
#### Thursday 2022-02-17 06:37:36 by Noah Nuebling

Tried to implement mechanism for scrolling the drag subcurve of a HybridCurve by sending momentum scroll events if the 'inertialScroll' setting is enabled.

But I want to try a different approach.

Our approach was to still let the GestureScrollSimulator do the work of sending the momentumScroll events but to interact with it from Scroll.m to see how far it still wants to scroll and stuff.

This way of implementing things is really bad. When I started struggling with race conditions I gave up, because I was fighting the current structure too much.

Instead we need to
- Make a method for sending momentumScrolls available to Scroll.m and then use that directly.
- Make it so that the animator callbacks in Scroll.m know which subcurve of the HybridCurve they are on (Bezier or Drag)
	- Maybe pass the callback a little flag 'Bool hybridSubCurveChanged' - that should be enough
	- This would more 'tightly couple' the HybridCurve and the Animator I guess but I don't think it matters
- Use this to figure out whether to send normal gesture scroll events of momentumScroll events in the Animator callback.
- To make things interact properly with click and drag: We'll probably have to eventually build some function that can interrupt the animation and then will have to send a momentumScrollEnd event if appropriate and stuff.
→ This is all quite complicated and convoluted and requires some refactoring, but at the end it should be a cleaner solution that I can work with and that doesn't have lots of weird race conditions that are super hard to understand.

Should undo these changes from this commit:

- Pretty much all changes to Scroll.m
	- _momentumPrediction
	- All the if statemtents where '_scrollConfig.inertialScroll' is the condition.
- Some of the class properties that I made public don't need to be. E.g. momentumAnimator, dragValueRange, baseCurve, maybe more. This doesn't really matter though.

- Some of the other restructuring like creating animationTimeLeft_Internal and making the animationTimeLeft thread safe are good clean up, and I don't want to undo it.
- I don't think there's anything else important that I should undo

---
## [edvacco/undetected-chromedriver](https://github.com/edvacco/undetected-chromedriver)@[ebafbe1db6...](https://github.com/edvacco/undetected-chromedriver/commit/ebafbe1db6fe34dff142bfa74da49b011fa62418)
#### Thursday 2022-02-17 07:07:45 by Leon

3.0.0 (#180)

*3.0.0
added lots of features and bugfixes

- You can now subscribe to Chrome Devtools Protocol Events like networking.
- splitted the project up in seperate modules now
- fixed locale (accept-language)
- you can enter your user-data-folder as property of
    ChromeOptions() now.
- The ChromeOptions had a makeover, and i took the one from alpha 4,
    people having troubles with mobile emulation and other bullshit,
    can try again now.
- fixed the logic where sometimes options did not
    respect the given values
- for headless (though still not supperted for undetectability),
    added some real cool features which need to be set in
    the options object):

    defaults:
    emulate_touch = True
    mock_permissions = True  # headless had notificationpermissions
                                setup in a distinguisable way.
    mock_chrome_global = False
    mock_canvas_fp = True  # patch fingerprint

EXTENSIONS ARE NOT SUPPORTED BY CHROME IN HEADLESS MODE
YET. IF YOU WANT TO USE THEM, CREATE A PROFILE AND INSTALL
EXTENSIONS BY USING A REGULAR CHROME SESSION FIRST.
ALSO LOGIN TO GMAIL WHILE YOU'RE ON A GENUINE SESSION.

WHEN FINISHED, COPY THE USERDATA FOLDER OF CHROME TO SOME KNOWN
LOCATION (and make maye 2 copies?). BY HAVING GMAIL LOGGED IN
FIXES ALSO THE UNSAFE BROWSER MESSAGE FROM GOOGLE (AT LEAST FOR
ME IT WORKS)


* 2.2.2

* fixed a number of bugs
- specifying custom profile
- specifying custom binary path
- downloading, patching and storing now (if not explicity specified)
    happens in a writable folder, instead of the current working dir.

Committer: UltrafunkAmsterdam <UltrafunkAmsterdam@github>

* tidy up

* uncomment block

* - support for specifying and reusing the user profile folder.
    if a user-data-dir is specified, that folder will NOT be
    deleted on exit.
    example:
        options.add_argument('--user-data-dir=c:\\temp')

- uses a platform specific app data folder to store driver instead
    of the current workdir.

- impoved headless mode. fixed detection by notification perms.

- eliminates the "restore tabs" notification at startup

- added methods find_elements_by_text and find_element_by_text

- updated docs (partly)

-known issues:
    - extensions not running. this is due to the inner workings
        of chromedriver. still working on this.
    - driver window is not always closing along with a program exit.
    - MacOS: startup nag notifications. might be solved by
        re(using) a profile directory.

- known stuff:
    - some specific use cases, network conditions or behaviour
      can cause being detected.

* Squashed commit of the following:

commit 7ce8e7a236cbee770cb117145d4bf6dc245b936a
Author: ultrafunkamsterdam <info@blackhat-security.nl>
Date:   Fri Apr 30 18:22:39 2021 +0200

    readme change

commit f214dcf33f26f8b35616d7b61cf6dee656596c3f
Author: ultrafunkamsterdam <info@blackhat-security.nl>
Date:   Fri Apr 30 18:18:09 2021 +0200

    - make sure options cannot be reused as it will
        cause double and conflicting arguments to chrome



    - support for specifying and reusing the user profile folder.
        if a user-data-dir is specified, that folder will NOT be
        deleted on exit.
        example:
            options.add_argument('--user-data-dir=c:\\temp')

    - uses a platform specific app data folder to store driver instead
        of the current workdir.

    - impoved headless mode. fixed detection by notification perms.

    - eliminates the "restore tabs" notification at startup

    - added methods find_elements_by_text and find_element_by_text

    - updated docs (partly)

    -known issues:
        - extensions not running. this is due to the inner workings
            of chromedriver. still working on this.
        - driver window is not always closing along with a program exit.
        - MacOS: startup nag notifications. might be solved by
            re(using) a profile directory.

    - known stuff:
        - some specific use cases, network conditions or behaviour
          can cause being detected.

---
## [prati0100/linux-next](https://github.com/prati0100/linux-next)@[ac7f6befc3...](https://github.com/prati0100/linux-next/commit/ac7f6befc3d1a58728ce3b93546aa24967ad90e7)
#### Thursday 2022-02-17 08:20:00 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [prati0100/linux-next](https://github.com/prati0100/linux-next)@[74293225f5...](https://github.com/prati0100/linux-next/commit/74293225f50391620aaef3507ebd6fd17e0003e1)
#### Thursday 2022-02-17 08:20:00 by Vasily Averin

memcg: prohibit unconditional exceeding the limit of dying tasks

commit a4ebf1b6ca1e011289677239a2a361fde4a88076 upstream.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It is assumed that the amount of the memory charged by those
tasks is bound and most of the memory will get released while the task
is exiting.  This is resembling a heuristic for the global OOM situation
when tasks get access to memory reserves.  There is no global memory
shortage at the memcg level so the memcg heuristic is more relieved.

The above assumption is overly optimistic though.  E.g.  vmalloc can
scale to really large requests and the heuristic would allow that.  We
used to have an early break in the vmalloc allocator for killed tasks
but this has been reverted by commit b8c8a338f75e ("Revert "vmalloc:
back off when the current task is killed"").  There are likely other
similar code paths which do not check for fatal signals in an
allocation&charge loop.  Also there are some kernel objects charged to a
memcg which are not bound to a process life time.

It has been observed that it is not really hard to trigger these
bypasses and cause global OOM situation.

One potential way to address these runaways would be to limit the amount
of excess (similar to the global OOM with limited oom reserves).  This
is certainly possible but it is not really clear how much of an excess
is desirable and still protects from global OOMs as that would have to
consider the overall memcg configuration.

This patch is addressing the problem by removing the heuristic
altogether.  Bypass is only allowed for requests which either cannot
fail or where the failure is not desirable while excess should be still
limited (e.g.  atomic requests).  Implementation wise a killed or dying
task fails to charge if it has passed the OOM killer stage.  That should
give all forms of reclaim chance to restore the limit before the failure
(ENOMEM) and tell the caller to back off.

In addition, this patch renames should_force_charge() helper to
task_is_dying() because now its use is not associated witch forced
charging.

This patch depends on pagefault_out_of_memory() to not trigger
out_of_memory(), because then a memcg failure can unwind to VM_FAULT_OOM
and cause a global OOM killer.

Link: https://lkml.kernel.org/r/8f5cebbb-06da-4902-91f0-6566fc4b4203@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Roman Gushchin <guro@fb.com>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [JK0JK/Minigame-Investigator](https://github.com/JK0JK/Minigame-Investigator)@[e476129bda...](https://github.com/JK0JK/Minigame-Investigator/commit/e476129bdaa0eee1a6767be6b9dfec8ccf9bbd64)
#### Thursday 2022-02-17 10:23:38 by root

The  Identity Update

FUCK YOU
FUCK YOU
FUCK YOU
FUCK YOU
I WIN
I WIN
I WIN
I WIN
GET FUCKED
GET FUCKED
GET FUCKED
GET FUCKED

I AM BETTER AT PROGRAMMING THAN YOU ARE AT BREAKING ON ME, STUPID PIECE OF SOFTWARE
FUCK YOU

I GOT MY REVENGE, BITCH

TL;DR - Fixed the error that wouldn't display the "This diary belongs to..." text

---
## [PsalmEquipt/PsalmEquipt](https://github.com/PsalmEquipt/PsalmEquipt)@[cc4e15fa90...](https://github.com/PsalmEquipt/PsalmEquipt/commit/cc4e15fa90099e3e87ba9d0220e30af8829f1fab)
#### Thursday 2022-02-17 10:38:30 by PsalmEquipt

Hi, I'm PsalmEquipt

For several years, I've trusted God in matters big and small, and He has never let me down. He's in the miracle business every day and will not do less than His Word. Perhaps like Moses, you'd like to find out more.

And the angel of the LORD appeared unto him in a flame of fire out of the midst of a bush: and he looked, and, behold, the bush burned with fire, and the bush was not consumed. And Moses said, I will now turn aside, and see this great sight, why the bush is not burnt. Exodus 3:2,3

Just as Moses did, we can take the time and effort to seek the things of God in our daily lives. Ephesians reveals a glimpse of what's ahead for us as we are faithful in this:

That in the ages to come he might shew the exceeding riches of his grace in his kindness toward us through Christ Jesus. Ephesians 2:7

For a wealth of enlightenment and answers to life's questions visit:

THE WAY INTERNATIONAL Biblical Research, Teaching, and Fellowship Ministry

Founded 1942

Website www.theway.org

More Info psalmequipt.nichesite.org

---
## [UniverseLambda/42-inception](https://github.com/UniverseLambda/42-inception)@[ae18cfbc3f...](https://github.com/UniverseLambda/42-inception/commit/ae18cfbc3fb2164580260ab3113b6a1a9c9c05fb)
#### Thursday 2022-02-17 11:38:17 by SAAD Clement

WELL WELL WELL. Fuck you correction

add a user account to Wordpress (Mamaaaaaaaa)

fix mariadb not asking password when connecting to root as sudo
fix root has no password
fix every alpine linux version (penultimate)

remove suprem_commander mariadb user

---
## [exampreparation51/pdfdumps](https://github.com/exampreparation51/pdfdumps)@[8ed949d55a...](https://github.com/exampreparation51/pdfdumps/commit/8ed949d55add2d990c8500fac47caf9cfd8c3f66)
#### Thursday 2022-02-17 11:46:26 by exampreparation51

Update PSP Exam - Questions

<h1><strong>ASIS PSP Pdf Dumps - A Profession Advancement Tool</strong></h1>
<p><span style="font-weight: 400;">ASIS PSP certification exam is obtaining all the recognized interest as  PSP certification exam not merely helps the Physical Security Professional pros but Physical Security Professional exam also the persons who desires to upgrade their Physical Security Professional career on best. ASIS PSP exam assists you in maximizing your skills, efficiency, and productivity.&nbsp;</span></p>
<p><span style="font-weight: 400;">By using <span style="color: #0000ff;"><a href="https://www.dumpsgeek.com/PSP-pdf-dumps.html">PSP pdf dumps which you will acquire by acing the PSP exam</a></span> you will be in a position to resolve the complex issues inside the organizations. By solving these troubles, you are able to get the required fame in the domain of certificaton.</span></p>
<p><span style="font-weight: 400;"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://i.ibb.co/cvT8nkQ/69160853-2351723308245096-1422782013575790592-n.jpg" alt="PSP dumps pdf" width="554" height="270" /></span></p>
<h2><strong>Settle Your Thoughts With  PSP Pdf Questions Even Though Preparing For The PSP Exam</strong></h2>
<p><span style="font-weight: 400;">1 factor that you need to take into account although attempting the ASIS PSP exam is that acing the Physical Security Professional PSP certification exam just isn't a piece of cake and also you should settle this thing within your thoughts from the day one of the preparations from the PSP certifications. Should you be opting for the ASIS PSP certification exam and can not locate a suitable PSP dumps pdf, then you definitely need to get the Physical Security Professional PSP questions pdf in the DumpsGeek. Why you must go for the  PSP braindumps from the DumpsGeek? let&rsquo;s dig up a bit.</span></p>
<h3><strong>ASIS PSP Braindumps - Finest Strategy to Prepare</strong></h3>
<p><span style="font-weight: 400;">ASIS  PSP pdf questions provided by the DumpsGeek has been verified by the Physical Security Professional professionals creating these Physical Security Professional PSP braindump the finest way for the preparation on the PSP pdf dumps. PSP questions pdf is equipped using the <span style="color: #0000ff;"><a href="https://www.dumpsgeek.com/PSP-pdf-dumps.html">latest  PSP dumps pdf</a></span> which will surely are available in the final exam on the Physical Security Professional. Besides this DumpsGeek also supply you the ASIS PSP exam simulator for the practicing from the Physical Security Professional certification exam. These PSP pdf questions are finely prepared by maintaining in thoughts the scenario of the Physical Security Professional actual exam.</span></p>
<p><a href="https://www.dumpsgeek.com/PSP-pdf-dumps.html"><span style="font-weight: 400;"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://i.ibb.co/k2VCXGQ/68998124-2519157348106036-5952036962369011712-n.jpg" alt="PSP dumps" width="578" height="282" /></span></a></p>
<h3><strong>100% Passing Assure With Physical Security Professional Questions Pdf</strong></h3>
<p><span style="font-weight: 400;">At times it occurs with some students that they got scammed by some PSP preparation material sources, but DumpsGeek is amongst the risk-free and assured source for the  PSP braindumps as they supply 100% passing guarantee together with the  PSP exam dumps. You'll be able to get the concept of their PSP dumps pdf by downloading the pdf demo on the PSP questions pdf. Furthermore to this DumpsGeek has a loved ones of greater than 50,000 happy clients producing them the special tool for the preparation and achievement of the Physical Security Professional test.</span></p>

---
## [hanziKR/Evolve](https://github.com/hanziKR/Evolve)@[2cd5860161...](https://github.com/hanziKR/Evolve/commit/2cd5860161e23a0a160cd9c4be4876fbf98dbd6b)
#### Thursday 2022-02-17 11:58:29 by Beorseder

Calculator Updates, Minor Bug Fixes, and Info

Perks:
Added Doomed achievement to the perks lists because there's no way to know that it unlocks Hellscape/Eden planets otherwise.
Added Governor CRISPR tree to perks list.
Fixed Evolve Journeyman not showing the full list of values in the wiki perks page if the perk was not yet obtained.

Calculators:
Updated Plasmid/Anti-Plasmid gain calculators with the new caps on gains, the High Population trait, being Synthetic genus for MADs, and being in Truepath, and AI Apocalypse reset.
Updated Phage gain calculator with Truepath and AI Apocalypse reset.
Updated Dark Energy bonus calculator with Lemon Cleaner perk.
Added AI Core gain and bonus calculators.
Added gain calculators to AI Apocalypse reset entry.
Updated Job Stress calculator to be fixed and accommodate for trait rankings and, the Emotionless trait and to fix Titan Colonist string.

Wiki Info:
Added information about Sludge's modification costing 10x more and their inability to remove Ooze to the Failed Experiment entry. Also fixed the data link to MAD reset.
Similarly added to CRISPR Mutation entry that Sludge also have 10x costs.
Added to Raid, Siege, and Terrorist Attack events how they don't happen in Truepath.
Added Pillage event(s) entry to Major Events page.
Updated Llama Minor Event with trait restrictions.
Updated Ascension reset entry with information on the geology buff and Ascended planets.
Added wiki effect to Alien Biotech tech.

Textual:
Fixed Entertainer tooltip showing twice the effect of Musical.
Fixed Gauss Rifles showing the effect for Disruptor Rifles.
Fixed some wiki fuel cost displays.
Fixed Water Freighter tooltip showing half the Helium-3 cost. Fixes #713
Fixed some typos.
Changed instances of "space cost creep" to "non-homeworld cost creep" to indicate that they apply to Hell Dimension as well.
Updated Pig-Latin.

Misc:
Exporting the save now updates accelerated time bank to account for if someone is paused and exports, updating their save's current time and thus losing all that accelerated time.
Fixed CRISPR and Blood Infusions being affected by adjustCosts when checking their affordability, which caused some issues with traits shifting their costs around making the coloring inaccurate sometimes near the cost.
Fixed Ritual Casting not showing up in Industry in Cataclysm.
Fixed bug where, if not Preloading Tab Content, shifting to another tab when in the custom lab and then shifting back to Civilization tab would not show the custom lab anymore. Fixes #671
Detritivores no longer see the Farming ritual as it doesn't do anything for them.
Fixed bug with building the Forward Base not reloading space to show the Troop Lander and Crashed Ship structures.

---
## [VOREStation/VOREStation](https://github.com/VOREStation/VOREStation)@[46b6bbaf74...](https://github.com/VOREStation/VOREStation/commit/46b6bbaf74996c9d7ffc25125491e2293e136a1c)
#### Thursday 2022-02-17 13:01:38 by VerySoft

Misc Tweaks

Fixes a space vine runtime

Makes it so space vines can't climb stairs (because that leads to practically unkillable stacks of vines that lag the server)

Makes it so space vines can't grow on open space (because you usually can't kill vines if they're way out in open space and that doesn't make much sense anyway.)

Attempts to limit the maximum range of plant bioluminescence (having hundreds or thousands of dynamic light sources with maximum possible light range seems to lag the server)

Adds a funny dog that no one should ever actually spawn but I will one day as a joke and everyone will cry. (its base form is actually not hostile so if you kill that one the hell you earn will all be on you)

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[b306af392c...](https://github.com/zx2c4/linux-rng/commit/b306af392c75a5e0045f2c46c2a87cb8444efe50)
#### Thursday 2022-02-17 15:20:37 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear function fits this
bill quite well, easily extending to the larger state size and to the
fact that we're mixing in more than just the cycle counter. By picking a
linear function with no non-trivial invariant subspace, unlike NT's
rotate-xor, we benefit from the analysis of <https://eprint.iacr.org/2021/1002>.
This proves that linear functions with only the trivial invariant
subspaces make very good entropy extractors for the type of complex
distributions that we have. It suggests that we extract entropy via
S←AS⊕X, where S is our pool vector, X is the new interrupt data vector,
and A is the transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [Avarice12/platform_frameworks_base](https://github.com/Avarice12/platform_frameworks_base)@[07889b7c02...](https://github.com/Avarice12/platform_frameworks_base/commit/07889b7c02bcccdf130eaf2d5b55aa2b773bc54f)
#### Thursday 2022-02-17 15:46:42 by Joey Huab

core: Rework the Photos features blacklist again

* Apparently, Magic Eraser currently requires a
  specific Photos version for it to show up and
  actually work. (https://apkmirror.com/apk/google-inc/photos/photos-5-65-0-405472367-release/google-photos-5-65-0-405472367-10-android-apk-download)

* Basically, Magic Eraser feature will crash if
  Photos is spoofed as Pixel XL. We want to
  make Magic Eraser work by default as long as
  the Unlimited Photos spoof is turned off.

* However, when PIXEL_2021_EXPERIENCE feature
  is detected by the Photos app, it will use
  the TPU tflite delegate. So we need to
  blacklist it by default from the Photos app.

* TL;DR Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

---
## [McGluckerson/ScuffOS](https://github.com/McGluckerson/ScuffOS)@[9e55e70fd4...](https://github.com/McGluckerson/ScuffOS/commit/9e55e70fd480d063258dafeb85f3ef3868b43a51)
#### Thursday 2022-02-17 16:29:25 by McGluckerson

Maze
possibly the large content update

- added app "maze". maze has 4 levels and does not connect to database

- for some reason git says I deleted casino and battleship (I didn't)

this is one of the last updates. I don't really want to work on this any more because its horribly programed. its honestly a piece of shit.

---
## [balmeetkaur/PythonPrograms](https://github.com/balmeetkaur/PythonPrograms)@[8084ed92a3...](https://github.com/balmeetkaur/PythonPrograms/commit/8084ed92a36e37bb54b409747126828470aa2a39)
#### Thursday 2022-02-17 17:24:28 by Balmeet Kaur

conditional programs 

program 1: WAP based on following scenario
    : Big sales :
    
    product categories = electronics  , apparels,baby products , personal care 
    
    electronics = phone 10% discount  , laptops 5% , ac and refrig 20% - price 
    apparels =  gender wise females proffesional 30%  , personal  20%
    baby = 40%
    personal care , if the actual price above 600 then  50% off

program 2: Consider you have your own restaurant : three item choices  is there :
1: pizza
2:  burger
3:  hotdog
toppings available for pizza: paneer, mushrooms, and capsicum
fillings available for burger and hot dog is  single layer cheeze and double layer cheese
and side order menu is softdrinks
WAP TO CALCULATE THE COST OF ITEM which user ordered BASED ON THE MENU OF RESTAURANT

program 3: CONSIDER A COMPANY : SINCE 2016 (5 YEARS OLD) 
Need to give bonus to the employee at the end of the year 
ELIGIBILTY :
if person has overall greater than or equal to 10 years of work experience then 5k
if person has overall greater than or equal to 10 years of work experience then 5k:
if a person is having 3 years in current company but overall experience is 8 then 3k
if overall experience is 3 years in current company then 3k

program 4 : WAP to check whether the entered number is odd or even if it is odd
then also check it is divisible by 7 if it is divisible by 7 then compute its cube

program 5 : Write a prog to take input from the user regarding the weight and height of
a person and calculate the BMI of the person and print it and also display weather the person
is under weight, normal, overweight and obese

program 6 : WAP regarding this condition 
For PM election , whether is person is eligible for PM or not :
  eligibility criteria as :
   1: No of criminal cases = 0
   2. Age>45
   3. past experince as CM

---
## [htc-msm8960-dev/android_kernel_htc_msm8960](https://github.com/htc-msm8960-dev/android_kernel_htc_msm8960)@[8dff5ab9c5...](https://github.com/htc-msm8960-dev/android_kernel_htc_msm8960/commit/8dff5ab9c58907b141b7a2e99dbebbb04533727b)
#### Thursday 2022-02-17 18:18:05 by KOSAKI Motohiro

mqueue: don't use kmalloc with KMALLOC_MAX_SIZE

KMALLOC_MAX_SIZE is not a good threshold.  It is extremely high and
problematic.  Unfortunately, some silly drivers depend on this and we
can't change it.  But any new code needn't use such extreme ugly high
order allocations.  It brings us awful fragmentation issues and system
slowdown.

Signed-off-by: KOSAKI Motohiro <mkosaki@jp.fujitsu.com>
Acked-by: Doug Ledford <dledford@redhat.com>
Acked-by: Joe Korty <joe.korty@ccur.com>
Cc: Amerigo Wang <amwang@redhat.com>
Cc: Serge E. Hallyn <serue@us.ibm.com>
Cc: Jiri Slaby <jslaby@suse.cz>
Cc: Joe Korty <joe.korty@ccur.com>
Cc: Manfred Spraul <manfred@colorfullife.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Change-Id: Ia01e50b8366d6196ca382aa7b16789679749b4e4

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[427b7205de...](https://github.com/mrakgr/The-Spiral-Language/commit/427b7205decc12c061e2476daa807a8de917848c)
#### Thursday 2022-02-17 18:27:30 by Marko Grdinić

"10:45am. Let me read Kumo and I will get started on the Cloth tutorial.

11am. Enough, it is time to start.

This season, I only seem to be watching badly done anime like Kenja and Girls Frontline. I am thinking about that shot where Mira is overlooking the city and I am sure that whoever was responsible just scattered the buildings without putting in roads.

I am glad that Kenja seems to be doing well though.

Hmmm, right. Let me break the ice by doing the walkway with PolyExpand2d.

Also I'll have to figure out how to renew the apprentice license. I tried doing it a few days ago, but I could not figure out how. Oh, it offers to do it automatically. Ok good.

...First time looking at example content. There are some things of slight interest there, but nevermind it for now.

Yeah, one thing I need to figure out how to do is do a fold and scan over the attributes. Just having maps is too restrictive.

Forget this for now. Let me do the walkway again.

11:45am. I did it. I have some grasp of how this works now. It turns out that crave is not as reliable as I thought it was. There is not much advantage to using it instead of group by range. The way PolyExpand2d works is by stretching the edges. This made the end edges 10x larger than the rest. When I tried carving that, I got strange results.

11:50am. I am satisfied. This method is an improvement on what I had before even if the results are the same. I dislike calculating the perimeter and then doing a loop with carve. I have to do that weird hexp to divide by the perim, and the attribute ends up lingering around.

As a rule, I do not want to do much, or any for that matter, Vex programming Houdini. The value of the program is in the nodes it has on the top and I should make use of that.

11:55am. Now let me focus on Cloth. Focus me, focus.

https://youtu.be/2sbBe9Q3PSY?t=326

Let me resume from where I was yesterday.

12:05pm. https://youtu.be/2sbBe9Q3PSY?t=592

Houdini has a lot of good stuff in it. I would not have thought to rename it like this.

12:30pm. https://youtu.be/2sbBe9Q3PSY?t=1787

This tutorial has been quite light so far. Learning how to do physics sims in Blender was honestly harder than this.

https://youtu.be/2sbBe9Q3PSY?t=2266

I should use this extrude by thickness to give the towels some volume.

https://youtu.be/2sbBe9Q3PSY?t=2439

Did he freeze it? Where was the option for that? Vellum Drape had that option. He set it at frame 150. Let me resume.

https://youtu.be/2sbBe9Q3PSY?t=2550

Here he is talking about the cloth stretching too much.

https://youtu.be/2sbBe9Q3PSY?t=2589

I see. Increasing the substeps would fix my problem as well. Great. It was worth watching this.

Let me finish the video. Only 5m more left.

https://youtu.be/2sbBe9Q3PSY?t=2604

Seeing him wire it one by one makes me think he is not aware of the population trick. If he just dragged the node on top it would be done automatically.

https://youtu.be/2sbBe9Q3PSY?t=2643

There is a detangle option here. ...No I doubt that would be good at resolving the hook issue. I'd get some ugly geometry on a hard surface that I would not blink an eye on for a cloth.

1pm. Let have breakfast here. That tutorial gave me some ideas. To fix my stretching issues all I need to do is increase the number of solver substeps, but after that I should put it through post process.

1:05pm. I gave it a try. Right now the simulation is pretty much perfect.

1:10pm. Forget it, let me go have breakfast. I'll figure out how to put the other two towels later.

1:50pm. Let me do the chores. After that I'll deal with the towels. After that I'll finally look into texturing for the first time.

2:20pm. Done with chores. Let me start.

2:25pm. I've decreased the patch edge length by 2x to get more detail. I've also made the pins soft as I've been getting weird sticking out. Right now it it takes it 3s per frame so I am waiting for it to finish baking.

2:30pm. Hmmm, the place where is hooked is too stiff. Rather than than falling down on the back, it is acting as if it was some stiff synthetic polymer. I am going to have lower the stiffness.

2:40pm. Lowering stiffness from 1e10 to 1e3 was the way to go.

3:40pm. I am still playing around with it. Right now I've set it to cache 120 frames at high detail. It takes it about 5-10s per frame.

3:45pm. Let me think what to do while this is going on.

Now that I have this done, I think it is time that I seriously start thinking about texturing.

4:10pm. Did some cleaning up. That bench had too much noise. The boards were too deformed. I suppose I should do the menu for it, but let me forget about that for now.

Texturing is the next step. I won't be adding any more geometry to the scene.

4:15pm. Right now I am taking a short breather. I've been building up to this for a long time.

4:20pm. How should I start this?

Let me start with the big things. Forget the small objects. Instead let me grab some textures I can put on that big block of island. Let me start by selecting something.

https://polyhaven.com/

> Previously we ran HDRI Haven, Texture Haven and 3D Model Haven as separate independent projects, but ultimately decided we could serve the community better by joining forces and creating a single new platform: Poly Haven.

There is free stuff here. I got some textures off textures.com previously, but the amount they allowed in the free account is pitiful.

https://polyhaven.com/a/square_floor

Ok, I'll go with this. Not exactly what I had in mind, and I'll have to change the color scheme, but it should do.

https://polyhaven.com/a/marble_01

No, let me go with this. Let's not get fancy.

4:35pm. Now that I've decided on a texture, let me watch a texturing tutorial. I know how to do this in Blender, but I've never tried it in Houdini.

https://www.youtube.com/results?search_query=houdini+texture

Well, let me explore a bit.

https://www.youtube.com/watch?v=Fspeu7Q9c1Y
Mantra Tutorial — Layer (Material) Mixing — Getting Started Course ep. 07

I need to get into the mindset of working with shaders. No doubt I am in for some pain since I never bothered propagating uv values for any of my models. I'll probably have to resimulate the towels for them to stick.

Well, let me take this slowly. I'll watch some tuts, try it myself and see where that takes me.

https://youtu.be/Fspeu7Q9c1Y?t=223

Oh, Houdini has displace along normals. I've been wondering how I would shape the towel so they are thinner in places and this is it.

https://youtu.be/Fspeu7Q9c1Y?t=565

Instead of renaming outright, he should just use the postfix.

https://www.youtube.com/watch?v=4qndzJljTfQ&list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Mantra Shading and Rendering Course

I should go through this.

Let me start a new file, the towels when saved take up 4gb.

I'll clean that up at some point. Nevermind it for now.

https://youtu.be/4qndzJljTfQ?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=381

Ah, right. I completely forgot that you can make materials in the geometry node itself.

5:10pm. Let me continue watching. Once he shows me how to import textures, I'll give it a try myself.

5:25pm. He mentions that intensity and exposure are the same. I really want an explanation of what they are supposed to represent.

5:35pm. Let me just tough out this series. It will serve as a reference for later.

https://youtu.be/9lIIGhUM4hE?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=416

I'll admit, until I watched the bull video yesterday I had no idea that render view is for previews.

https://youtu.be/9lIIGhUM4hE?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=1458

Here he mentions textures for the first time.

...Let me have lunch here.

6:30pm. Let me watch a few more vids. Actually, let me just finish the one I was watching and then...the next one is 40m long.

I'd rather just leave that one for tomorrow. Watching lectures is the most boring part of the art journey so I do not know if I'll have the focus for it at this time in the day.

6:40pm.

> This series is great. I just downloaded Houdini for the first time. Coming from being a basic blender user. Is Mantra GPU or CPU? I wonder if it can use octane.
> Mantra is soon to be officially EOLed. Karma is the next thing from sidefx/Houdini. Also unless you want to do various sims, I’d suggest actually learning blender deeper.

Interesting the a Houdini guy is recommending Blender to people.

Let me watch the next video for a while.

6:55pm. https://youtu.be/LhWQKQdiR8I?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=267

Let me stop here.

https://www.sidefx.com/forum/topic/46048/
> It is simply exponential light intensity control and should be named appropriately. Furthermore the total light intensity from this control should be displayed.

Huh, so that is what exposure is?

> I teach lighting. At my school, where we also teach photography/cinematography, we have to teach that there is a light control in Houdini called “exposure” which is nothing like the exposure controls we teach in photography class. We have to teach that it really just changes individual light intensity more radically than the regular light intensity control and that it does not affect exposure in any way. This is the only way students with photography training can make any sense of the control.

Oh lol.

> The reasoning behind this apparent redundancy is that, for some people, f-stops are a much more intuitive way of describing light brightness than raw intensity values, especially when you're directly matching values to a plate. You may be asked by the director of photography (who is used to working with camera f-stop values) to increase or decrease a certain light by ‘one stop’. Other than that, this light parameter has nothing to do with a real camera's f-stop control. Also, working with exposure means you won't have to type in huge values like 10,000 in the intensity input if your lights have quadratic falloff (which they should).
> If you are not used to working with exposure in the lights, you can simply leave the exposure parameter at its default value of 0 (since 2^0 = 1, the formula then simplifies to: color * intensity * 1).

Huh so exposure just multiplies it by 2^n.

I found Houdini not having power like Blender and instead intensity and exposure really confusing last time.

https://www.sidefx.com/docs/houdini/nodes/obj/hlight.html
> Light intensity as a power of 2. Increasing the value by 1 will double the energy emitted by the light source. A value of 0 produces an intensity of 1 at the source, -1 produces 0.5. The result of this is multiplied with the Intensity parameter.

The docs confirm it. Ok. This actually isn't a bad idea at all. I'd actually want to manipulate exposure. In fact, they could have just gotten rid of intensity entirely.

7pm. Let close here for the day. I am going to go through the rest of the course tomorrow and start texturing.

Today I had the realization that even though the principle shader in the node tree is scary, the stuff in the parameter window is actually fairly straightforward. It should not take me long to grasp all of this. Every time I figure out something like the above, I get closer to my goal.

7:10pm. I need to get familiar with shading and texturing. I probably won't need too much in this area. But I am going to have to get started. If I can manage to get through this, I will almost be at the point where I could be a fully fledged artist. I just need to put in more work into it to get really good at it.

If I can get to that level, getting minor amounts of money will be a resolved issue. I'll do the next part of Simulacrum while having fun. The last 4 arcs were not real stories. They were a test to see if I can convince myself of the truth of the self improvement loop.

7:15pm. Sigh what a pain in the ass. I could have done this from the start and left Spiral for another time. That is a lie, no I could not. If I hadn't done Spiral, there is no way I would be able to program AI chips at my leasure once they arrived. If I want to cause the Singularity, having a complete mastery of a programming language is one of the prerequisites.

But now, I have the problem that even if the chips are here, I wouldn't be able to buy them. How ridiculous that I do not have money at my age.

Right now if my PC broke down, I'd have to abort my current quest and actually get a job to pay off the loan for the replacement hardware. I am always at the edge of a chasm.

A few months more. Just a few months more and I will be able to make my debut as an artist. If I can get my art skills to a sufficient level, I'll have a much easier time after that. It will be a lot more fun to create stuff than to go through endless reams of tutorials and documents."

---
## [AllyssonComin/Nadc-awards](https://github.com/AllyssonComin/Nadc-awards)@[1eca2fa47e...](https://github.com/AllyssonComin/Nadc-awards/commit/1eca2fa47e3b9d1cb4f39611a3bc22b2d4807c1d)
#### Thursday 2022-02-17 20:22:33 by Tasso Henrique Rodrigues de Oliveira

Merge pull request #22 from AllyssonComin/votes

fuck you igor, votes work.. but with no ajax

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[78c05ef34c...](https://github.com/san7890/bruhstation/commit/78c05ef34c11edc51c6b4e074e6539b32567e86a)
#### Thursday 2022-02-17 22:42:36 by san7890

The Science Lobby; Or, How I Learned To Embrace Congruence

This is a multi-factorial PR in a broader series meant to address the fact that areas are too massive. Today's episode includes the following:

This section of the halls are just incredulously fucking massive. I think the reasoning behind this (I may be wrong) is that no one bothered to make an area/sprite for the very distinct Science Lobby on Delta (as well as Meta and Tram). This PR is someone bothering.

To achieve good symmetry, I also made the area colloquially known as the Medbay Lobby it's own area as well with the already-existing area. Had to shuffle some stuff around, but I think it's not incredibly ugly. Peep a look:

---
## [OrionTheFox/Shiptest](https://github.com/OrionTheFox/Shiptest)@[031c0866ed...](https://github.com/OrionTheFox/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Thursday 2022-02-17 22:43:04 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[e26e3764e9...](https://github.com/zx2c4/linux-rng/commit/e26e3764e98f7ff54b76971fee96b06a0dd09305)
#### Thursday 2022-02-17 22:47:51 by Jason A. Donenfeld

random: use max-period linear interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However, with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a max-period linear function fits this
bill quite well, easily extending to the larger state size and to the
fact that we're mixing in more than just the cycle counter. By picking a
linear function with no non-trivial invariant subspace, unlike NT's
rotate-xor, we benefit from the analysis of <https://eprint.iacr.org/2021/1002>.
This proves that linear functions with only the trivial invariant
subspaces make very good entropy extractors for the type of complex
distributions that we have. It suggests that we extract entropy via
𝑺←𝐴𝑺⊕𝑿, where 𝑺 is our pool vector, 𝑿 is the new interrupt data vector,
and 𝐴 is the transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/TiMyEpmr>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [team8/drive-practice-2022](https://github.com/team8/drive-practice-2022)@[7a5bf59ab0...](https://github.com/team8/drive-practice-2022/commit/7a5bf59ab06afa3bffa5d9b3cfe270cf6f0771f4)
#### Thursday 2022-02-17 23:10:52 by Charger1256A

I am bored in english class and have nothing to do I made some improvements to dis thingy. Does anyone wanna huddle cuz I am bored. Plza save me :pray:. Idk what I am even doing that this moment. I am just going on a tanger or ranting, idk the diffrerence. I should be writing my synthsis essay, but that is so boring, so I am not going to. Please show up to room 404, it would be much appreciated. What the heck am I even doing rn? also zach, do you still have my code from csa? If so can you take a picture and send it to me? also everyone should follow Luca on insta and not follow him on git because I am bored. Currently it is 1500 and there is nothing for me to do. I complete my first lewdle today, so that was fun. Ohhh I should make this my blog or something idk. Who is coming to lab today? I love this channel because nobody ready commit messages. Or at least no one I am afraid of of. Except shalen ig, idk if he even is in this channel. i hope no mentors join later and read this message because I will get roasted. If mentors are reading this, I love you guys lol thanks for supervisising and helping us finish our bot. If Zach readin this then he probably thinking to himself what is this man doing. If Luca is reading this he is def gonna try and 1 up this commit message. If rkim is reading this he is like does Adity have have a life? and tbh idk if I do lol. If Ryan Lee is reading this message he will be scared of coding forever, but let me tell you now you should code this is not what coding is like. If Alexis is reading this, she probably didn’t get this far because she is too lazy to read my commit messages. the guy sitting next me is watching a documentary about Kanye and he says it is interesting. WHat do you guys think? I am literally just writing whatever pops into my heada and that just popped into my head. There are not lights in this room so I feel super sleepy. TBH i just want to go to a comp rn cuz i am bored. Luca, Alexis did you guys sign for FF? you guys should. How long are you guys staying at lab today? How do I see how many words this commit message is? it is now 1506 a. When I push I hope I dont get any error messages when I push cuz that would be annoying. What is buildkite, shoudl I integreate it into this channel. For young people. dont take ap lang otherwise you will end up doing this. This concluded my long rant bye. I might be back for more soon

---
## [Jetof20/Astroids](https://github.com/Jetof20/Astroids)@[0e3f7aa137...](https://github.com/Jetof20/Astroids/commit/0e3f7aa137efee692b2669c499ece75a2c091a1f)
#### Thursday 2022-02-17 23:52:18 by Jetof20

Completly Scrapped Everything. Starting fucking over

Who ever at oracle spent their fucking life developing a tool so horrible, need a restraining order. So they dont harm anyone anymore.

---

