## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-05](docs/good-messages/2022/2022-02-05.md)


1,450,638 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,450,638 were push events containing 2,054,416 commit messages that amount to 136,035,615 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [MacBlaze1/tgstation](https://github.com/MacBlaze1/tgstation)@[079f8ac515...](https://github.com/MacBlaze1/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Saturday 2022-02-05 00:23:10 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [sya-ri/PackSquash](https://github.com/sya-ri/PackSquash)@[99df59972e...](https://github.com/sya-ri/PackSquash/commit/99df59972efc9741475539f478dd67dd88771877)
#### Saturday 2022-02-05 00:36:17 by AlexTMjugador

bench: add automated benchmark suite based on Criterion.rs

Some PackSquash users contacted me about some tricky details of its
performance characteristics. I try to write code that is as efficient as
possible, and Rust helps with that, but performance is a complicated
topic. Up until now, performance was informally measured by my own
educated guesses and some manual test runs here and there, where I payed
attention to the total run time and resource consumption. However, we've
reached a point where any performance improvement is likely to be not
trivial, and my own careful testing may just not cut it. Moreover, not
having hard baselines to base decisions on is, in general, a bad thing.

To properly tackle those problems, let's introduce automated
benchmarking to PackSquash, leveraging the Criterion.rs framework, which
does a bunch of clever statistics that make it easy to assess how some
changes impact the performance. The benchmarks can also be profiled, and
because they are designed to have a relatively short duration we can do
that with a high sampling frequency, which is desirable to catch small
inefficiencies here and there.

The benchmarks use a curated dataset of resource packs that were
contributed by myself and some PackSquash users, with their written
permission. The packs were chosen due to their diverse asset
distribution and perceived representativeness of PackSquash usage. To
keep the repository lightweight, they are stored externally in a Google
Drive folder. Helper scripts are committed to handle the download and
setup of the pack dataset with ease. Some packs of the dataset are
encrypted with GPG using a cryptographically-secure, random password, as
they are the intellectual property of several people, and in some cases
I was explicitly told not to make them public.

The benchmarks mainly measure the wall-time PackSquash takes to optimize
packs, but on Linux platforms the performance counters kernel subsystem
is used to gather insights on additional metrics that are correlated
with it, such as CPU instruction and context switch counts. The
performance counters can pinpoint the cause of a performance regression
or improvement and are less sensible to noise from, for example, other
running processes, but wall-time is actually what we want to optimize
(in addition to a sane usage of other resources, like I/O and memory).

Future commits may make the GitHub Actions CI run these benchmarks, to
help ensuring that PackSquash stays performant with each commit.

Special thanks to the PackSquash users that discussed performance,
including the Discord users Michael and jilchu. I'd also like to thank
my friend and classmate Víctor for writing the useful sample-pack.py
script and sharing his smart ideas and understanding of mathematical
principles to aid performance optimization.

Co-authored-by: victorlf4 <victorlevosofernandez@gmail.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[7625d5bae2...](https://github.com/cockroachdb/cockroach/commit/7625d5bae2d9d229c8df2574d09dddacde7c1bb2)
#### Saturday 2022-02-05 01:20:13 by craig[bot]

Merge #75820 #75906 #75957 #75961 #76003

75820: sql: block swapping primary keys if dependent fk references exist r=fqazi a=fqazi

Fixes: #71709

Previously, when swapping primary keys it was possible
to cause foreign key references to break by removing
the primary indexes enforcing uniqueness. To address
this, this patch will detect if any foreign key references
will lose their uniqueness with the removal of the
primary index.

Release note (bug fix): Swapping primary keys could
lead to scenarios where foreign key references could
lose their uniqueness.

75906: sql: remove type width enforcement during execution r=mgartner a=mgartner

Assignment casts are now responsible for ensuring that a value written
to a column has a type and width that match the column type. This commit
removes the logic that performed this validation before assignment casts
existed.

Release note: None

75957: sql: update SHOW GRANTS ON TYPE to include grant options r=RichardJCai a=ecwall

refs https://github.com/cockroachdb/cockroach/issues/73394

Release note (sql change): SHOW GRANTS ON TYPE includes is_grantable column

75961: dev: integrate `bazel-remote` with `dev` r=rail a=rickystewart

* Add a new command `dev cache` which prepares the local cache.
  `dev cache --down` tears down the local cache, and `dev cache --reset`
  reboots it. My thinking is that we can extend the `dev cache` command
  with more stuff when we have it (e.g. remote caching).
* To this end we take the PID of the cache process and write it to a
  file in the cache directory. There's also a config file that users can
  manually update if they want.
* I request that people put this in their `~/.bazelrc`. It shouldn't be
  a problem if this applies to every Bazel workspace on the user's
  machine, it's just a cache.
* `dev doctor` now sets up the cache. It will now also fail unless your
  `~/.bazelrc` contains the string `--remote_cache=`. You can disable
  this with `--no-cache` or `DEV_NO_REMOTE_CACHE`.

Release note: None

76003: sql/catalog/bootstrap,*: allow system table IDs to be dynamic r=ajwerner a=ajwerner

This change is relatively small in terms of logic changes but it has large
implications for tests. The crux of the change is that we want to allow system
tables to not specify their IDs explicitly in their definition. The reason for
this is that we only reserved IDs 10-49 before handing out IDs to users. This
has the implication that new system tables in excess of 49 could overlap with
existing user descriptors. To cope with that, we'll need to use the descriptor
ID generator we normally use for user descriptors also for new system
descriptors in migrations.

Now, that could be the end of the story. The problem is that we really like
using data driven tests and we rather like printing out our keys, which
include descriptor IDs. If we were to carry on without changing the point
at which we started generating user descriptors, we'd run into real pain
every time we try to add another system table. All those datadriven tests
would have to change (and some other non-datadriven tests too).

This commit goes through that pain so hopefully for many years nobody else
has to. It does so by moving the first user descriptor we'll generate in a
newly bootstrapped cluster (or tenant) up to 100. This constant is not exported
and we can add mechanisms to override it later. This constant is chosen because
it still falls into the magical realm where the keys remain the same size.
It's also rather aesthetic. We could go bigger, but we'd pay a price for the
key for the first table you introduce. This probably doesn't matter, but I
don't want to be the one to do it.

Release note: None

Co-authored-by: Faizan Qazi <faizan@cockroachlabs.com>
Co-authored-by: Marcus Gartner <marcus@cockroachlabs.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Andrew Werner <awerner32@gmail.com>

---
## [JamieAdamsFanAccount/JamieAdamsFanAccount.github.io](https://github.com/JamieAdamsFanAccount/JamieAdamsFanAccount.github.io)@[fd273e74eb...](https://github.com/JamieAdamsFanAccount/JamieAdamsFanAccount.github.io/commit/fd273e74eb86584af15a0a3bef89de75c0115df5)
#### Saturday 2022-02-05 01:39:08 by Jamie Adams

I swear there's a twitter account that tweets sweary commits. shit shit shit fuck damn suck

---
## [j4james/terminal](https://github.com/j4james/terminal)@[b1ace967a2...](https://github.com/j4james/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Saturday 2022-02-05 02:29:53 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [absent-cc/backend](https://github.com/absent-cc/backend)@[aa8032af78...](https://github.com/absent-cc/backend/commit/aa8032af780821183796c743eca3b1953a07d5b1)
#### Saturday 2022-02-05 03:29:52 by Kevin Yang

fixed the fucking pathing holy shit. Now everything is relative and testing and main scripts work

---
## [ciderapp/Cider](https://github.com/ciderapp/Cider)@[d6981492a0...](https://github.com/ciderapp/Cider/commit/d6981492a0913fec6f4ad96bf42f0ac017da4b30)
#### Saturday 2022-02-05 03:46:25 by cryptofyre

fix quacksires fucky fuck fuck stupid ass code that somehow made it in.

---
## [esciafardini/twilio-hotline](https://github.com/esciafardini/twilio-hotline)@[b188f53b8c...](https://github.com/esciafardini/twilio-hotline/commit/b188f53b8c0ee906dbae0886ba93eea86c7bb5a9)
#### Saturday 2022-02-05 04:36:21 by Ted Ciafardini - work

Update formatting and fn calls

Dont give a fuck

The message has been received and God has arrived.

IF I CUT MY ARM BLEEDING

CUT MY LIFE INTO PIECE

AND M CONTEMPLATI SUICEIDE

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[2521d98504...](https://github.com/repinger/exynos9611_m21_kernel/commit/2521d985045a9a11fd1fb26e6761edb6e0ce5551)
#### Saturday 2022-02-05 05:42:29 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [TheFinalFrontierBruno/Naruto_Ninpou](https://github.com/TheFinalFrontierBruno/Naruto_Ninpou)@[32f854d563...](https://github.com/TheFinalFrontierBruno/Naruto_Ninpou/commit/32f854d563dd24bb8044f996059e59e49cc5e2c3)
#### Saturday 2022-02-05 06:17:29 by MetalfOxXer

changes

nerf shisuis E bonus dmg to 2% per lvl instead of 3%
reduce the time the hero disappears by using bunshins by half, so it atleast takes some skill to dodge
increase the damage of Madara's tengai shinsei in his Perfect Susano form to 15xgen magic damage instead of 10xgen magic damage.
reduce explosive tag dmg to 1000 instead of 1500
increase Anko's D cooldown
reduce Flash bomb silence to 2secs
reduce Zabuza's Q range by 100
remove the category from itens like uchiha sword, uchiha shield, akatsuki ring. Just makes combining itens a bit less annoying
reduce Gaaras pause duration on his Q by atleast 0.5 secs
decrease Hinata's Hakkesho Kuuten T area of effect from 800 to 600, 800 is a bit too much for such a strong ability that also gives her invulnerability
slow down the fire ball from Yugito's T a bit instead of decreasing the range
Ichigos stat gain seems to be incorrect. At lvl 50 he should have more nin and gen but all his stats have the same amount (137)
add a 0.1x tai scaling to the shark in mugensame, they currently deal 146 normal dmg, at 500 tai they would deal 196.
add aoe indicators to Borutos spells
add a audio clue to mifunes d for his allies to hear
temari's Evasion from W is sometimes permanent, making temari or her allies immune to Auto attacks
Make Neji immune to crowd control spells like roots and stuns and wire string during his R so he doesnt get bugged.

---
## [Visual1mpact/Paradox_AntiCheat](https://github.com/Visual1mpact/Paradox_AntiCheat)@[ae63420240...](https://github.com/Visual1mpact/Paradox_AntiCheat/commit/ae63420240c844dceb1e60a619ebc1208c23b1c6)
#### Saturday 2022-02-05 14:21:24 by Visual1mpact

Fix error for killaura

[Actor][error]-My World | actor_definitions |
/storage/emulated/0/Android/data/com.mojang.minecraftpe/
files/games/com.mojang/minecraftWorlds/Iev5YWu0AAA=/
behavior_packs/Paradox_AntiCheat | paradox:killaura |
minecraft:entity | components | minecraft:damage_sensor |
triggers | on_damage | Filter member value of test has_damage
must be a preset string.

[Actor][error]-My World | actor_definitions |
/storage/emulated/0/Android/data/com.mojang.minecraftpe/
files/games/com.mojang/minecraftWorlds/Iev5YWu0AAA=/
behavior_packs/Paradox_AntiCheat | paradox:killaura |
minecraft:entity | components | minecraft:damage_sensor |
triggers | on_damage | Filter test failed to parse inputs -> has_damage

The value was set to "entity_attack" but this value does not exist.
The current values at the time of this commit are as followed:

1. anvil
2. attack
3. block_explosion
4. contact
5. drowning
6. entity_explosion
7. fall
8. falling_block
9. fatal
10. fire
11. fire_tick
12. fly_into_wall
13. lava
14. magic
15. none
16. override
17. piston
18. projectile
19. stalactite
20. stalagmite
21. starve
22. suffocation
23. suicide
24. thorns
25. void
26. wither

For more information you can visit https://docs.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/filters/has_damage

Here we are changing "entity_attack" to "attack". Changes made have been verified using toolbox.

---
## [fajar3109/kernel_xiaomi_ginkgo](https://github.com/fajar3109/kernel_xiaomi_ginkgo)@[2c17383768...](https://github.com/fajar3109/kernel_xiaomi_ginkgo/commit/2c17383768dd590889598f7f5cc1aefbb3e551d3)
#### Saturday 2022-02-05 14:44:27 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: kyvangka1610 <kyvangka2002@gmail.com>
Signed-off-by: fajar <santuyz321@gmail.com>

---
## [IsGabriellaCurious/hockley-watch](https://github.com/IsGabriellaCurious/hockley-watch)@[e50e459a8a...](https://github.com/IsGabriellaCurious/hockley-watch/commit/e50e459a8a39456ed8af2abe086eb9021e18272e)
#### Saturday 2022-02-05 14:44:50 by IsGabriellaCurious

bit of refactoring

yes this is now a real estate not a watch site but well fuck you

---
## [apljungquist/wordlebotrs](https://github.com/apljungquist/wordlebotrs)@[b0a78e4b0d...](https://github.com/apljungquist/wordlebotrs/commit/b0a78e4b0d39cf482a80fac7b42bbb12dfba6e57)
#### Saturday 2022-02-05 14:58:50 by AP Ljungquist

Fix cargo publish thinking repo is dirty

I have previously experienced a similar problem where touching a file
without updating its content caused `git diff` to exit with an error.
In that case doing `git update-index --refresh` solved the issue. At
this point I cannot remember how this worked but it is not helping.
However, when troubleshooting I found that `git status` made the
problem go away so I will stick with that for now.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[17e19ef79d...](https://github.com/ammarfaizi2/linux-block/commit/17e19ef79dd0e0ad4b7ec2831088282ddd7674cd)
#### Saturday 2022-02-05 16:00:59 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [NjalNilum/ytf-bot](https://github.com/NjalNilum/ytf-bot)@[547f4ea374...](https://github.com/NjalNilum/ytf-bot/commit/547f4ea3746026659e0ba1081448a889c3e50fbc)
#### Saturday 2022-02-05 16:49:25 by Njal Nilum

Wie kann ein solch einfaches Problem so scheiße viel Arbeit machen. Fuck off. Fuck you all.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[760c1b431e...](https://github.com/mrakgr/The-Spiral-Language/commit/760c1b431e8b5b1b522d415aed844c7d20f491db)
#### Saturday 2022-02-05 17:47:35 by Marko Grdinić

"10:25am. Let me chill, I'll get started after that.

10:45am. Let me start. I asked some questions and got some replies. I need to see it through.

10:50am. First I am trying out my own idea, but it did not work. The trouble is that subtracting a sphere from the corners results in extra points.

///

>>880137 (You)
>1) How do I rip the edges of a mesh into individual ones?
Convert Line SOP will turn each segment of a curve into its own primitive. Follow this with a Unique Points SOP to break them apart.
>2) Should I then use a foreach edge loop to scale them then?
Not necessary. You can use a Primitive Properties SOP to scale each primitive from its centroid.
>3) How do I erase just a part of the side? Blasting an edge ends up connecting the removed ends which I do not want.
Won't be an issue now. If you want to make this more procedural you could use a Delete SOP with a bounding box area to determine what gets deleted. That way if you futz with your resample values you won't have to go back and re-select your gate geometry.
4) In Blender I also deleted the top face leaving only the edges, how do that in Houdini?
Not sure if this is what you mean, but you can group and delete by normal direction. In a Delete SOP disable the Number tab and go to the Normal tab. Set the direction to 0,1,0 and use a low spread angle. That will delete all the upward facing polys. The Group SOP has the same functionality.

///

I thought what I would do if this failed, and I thought of converting the mesh to splines.

11:05am. Ok, it works fine. Let me try the delete SOP.

I wonder why resample separates the lines.

11:20am. Let me do some more interacting.

///

>>880193
>Won't be an issue now. If you want to make this more procedural you could use a Delete SOP with a bounding box area to determine what gets deleted. That way if you futz with your resample values you won't have to go back and re-select your gate geometry.
I'd like to use the boolean subtract to get rid of the corners. If this worked, this would have the advantage of cutting off only up to a specified length. The Primitive SOP works, and this is a similar solution to what I used in Blender, but that would result in the scaling magnitudes being proportional to the size of the box. I'd instead want them to be ~0.5m from each corner.

Right now the boolean subtract does not work on the output of Convert Line SOP.

The Delete SOP just outright removes the points which is not good for two reasons: I have to put in the bounding sphere by hand, I can't just copy them to the 4 corner points and pass them into the SOP like in Boolean Subtract. The other reason is that I'd need to resample it twice since it just removes the points, and I'd need to use a large resolution the first time otherwise it might remove too much from the corner.

I thought that maybe using the Group SOP and passing in the bounding object to it would work, but I get an error.

At any rate, is there are more powerful node for deleting points from poly lines?

///

11:35am. No, just grouping the corners does not work. What a handful.

11:40am. Let me post the above.

11:45m. Done. The more effort I put into Houdini, the harder it will be to quit and use Blender instead.

Let me watch the mug modeling video.

https://youtu.be/zkfHavLfpuY
Procedurally Modeling a Mug in Houdini

Let me watch this.

12:05pm. It turns out there is a boolean curve SOP. Ok great. That takes care of the fences.

Let me watch the mug modeling video.

https://youtu.be/zkfHavLfpuY?t=735

This is so hacky. Isn't there a tool that just gets the edge?

12:35pm. https://youtu.be/Tvm_wJUrymM
Procedural Modeling Fundamentals in Houdini

Let me watch this at least halfway and then I'll have a break.

12:40pm. https://youtu.be/Tvm_wJUrymM?t=346

This is so annoying, just use polyfil.

No, the polyfill is not that great. Its ability to cut is limited.

12:50pm. Ok, enough. Now that I have the fence out of the way I should just go forward. Houdini is going to kill me at this rate. Let me just finish the pool scene so I can move forward with my life.

What am I going to do next? Let me just put in that pool, and the fence segments. I'll find the chair assets in Orbolt, or model them myself. There is no need to freet too much about this.

Compared to Blender, I feel so restricted in what I can do in Houdini. I hate it.

I need to remember that my plan was to just use Houdini for laying things out. I need to remember that determination. Let me get breakfast here.

2:05pm. Done with breakfast and chores.

Let me work towards bringing in the fence fragment. Focus me. Let me do something real today. I've just been messing around for the past two weeks and it feels like my heart is being gouged due to all the time wasting.

2:30pm. I added the fence segment. Let me do the sign at the entrance.

Doing this should not be hard. Let me use a cuve.

2:50pm. I want to hurt Houdini. It is making me suffer so much.

2:55pm. I am taking a short breather here.

I have a simple thing in mind - draw the curve for those posts so I can sweep a cross section through it. The piece of shit program keep putting it in such weird places.

Forget the fucking curve. Let me just use a cube. I'll do the same as in Blender.

3:20pm. Ok, I did it somehow.

The pool. The next is the f'kin pool. At this point I am 95% sure that I am going to ditch Houdini in favor of Blender, because I really hate working in it. A part of it is definitely attributed to the Covid disease that I've been enduring for the past two weeks, but a part of it is definitely program itself. I hate bloated tool like it the most of all.

I'd much rather use 20-30 good tools like in Blender, elegantly glued to the right hotkeys, than be forced to constantly jump around like this in Houdini.

3:30pm. Ok, focus me. Let me just go through today. Put the pool down. One cube, then another.

3:50pm. Let me take a short break here.

I've done the pool, but not the pool water. I need to figure that out.

4:10pm. Done with the break. Let me ask about the right way of getting the pool water. After that I'll move on to the main course. I'll do those vines and distribute the flowers on them. After I do that I'll know exactly where I stand Houdini vs Blender. After the flowers bloom, I'll know what true justice is.

First let me ask. Let me take a screen shot.

4:15pm. Focus me, focus.

///

In Blender, after I did the pool frame, I took the convex hull of it, and bool subtracted the original to get the water. I see that Houdini has a convex hull SOP, so I could go down that route again, but I was wondering if I could do something smarter than that in Houdini. I can imagine non-convex pool shapes that would get broken using such a method.

///

4:25pm. I need to get moving. Let me do that wireframe.

4:30pm. Hmmm, I note that PolySplit (which I am using for edge loops) actually outputs it in a group. This is great. Let me watch that video again where he had to do that ridiculous bounding box.

4:35pm. Focus me, let me do what I said I would do in the above entry.

4:40pm. Ah, he used the knife tool instead of the polysplit tool. That is why he did not have access to the edge. It is a case of blind leading the blind.

Ok, now that I have a basic frame how do I add a bunch of smaller frames ontop of that? No wait, that is my mouth being faster than my brain. What I really want to do is add a bunch of beam between the larger ones. I have something like a metalic construction frame here, and I need to split it up. Triangulating it would be easy in Blender, but here I am not sure what to do.

Let also ask about that in the Houdini thread.

I think I am finally starting to get into it.

...And it crashed. Hopefully I did not loose too much.

...The crash recovery was useless. It got me yesterday's version. I guess Houdini has that much in common in Blender.

4:50pm. Let me compose the post.

///

I have a metallic construction frame here above the pool, and I want to add a bunch of crisscrossing beams for stability. After that I'll sneak some giant vines through this and distribute the flowers on it. If this was Blender, I could select all the faces and triangulate them. That would turn the quads into tris. This would get me a part of the result, but I'd like a cross shape. So an idea that I'll try here is to loop over each of the primitives and subdivide it. Maybe that will give me what I want.

I'd like it if the main beams in the screenshot stayed as they are, but the newly added edges have a smaller radius.

This is not a huge deal, as I could do a polyframe for the main beams and then the subdivided mesh with a smaller radius which would cover them up, but I'd like to know what the most elegant solution to my problem would be here.

///

5:20pm. I use a foreach to go over all the primitives and then use an add node to make the connections. But how would I incorporate the notion of edge radius. Could I do this same thing using VEX?

No I am not really happy with the add node, because it adds too many poligons. For some reason the straightforward thing did not work, so I have to overcommit to get the result that I want. I fused some of that away just now...

///

(edited)
For separating curves into individual edge segments I think there's a SOP that already does it but I don't remember what it is. The logic in VEX is simple:

```
//in a point wrangle
int neighbours[] = neighbours(0, @ptnum);
foreach(int point; neighbours){
    if(point > @ptnum){
        vector neighbourpos = point(0, "P", point);
        int newpointA = addpoint(0, @P);
        int newpointB = addpoint(0, neighbourpos);
        addprim(0, "polyline", newpointA, newpointB);
        }
    }
```

You'll want to group the original primitives beforehand and blast them after the operation is done.

You could also do it in a vertex wrangle and loop over halfedges connected to the vertex, if the halfedge is primary create the segment.

///

5:35pm. Once again I am running into inspiration problems. I have no idea how to use VEX here to get what I want. Maybe I should watch that Vex tutorial properly. Right now I am drawing such a blank. Nevermind that.

...Ah, right. For the smaller beams, I could just get rid of the existing vertices!

Right...

5:40pm. I still woulnd't know how to do that. I'd need to do some serious studying.

It goes not matter. Right now, how about I do that wine.

I utterly failed at doing that beam using a curve and got really angry at Houdini, but let me try try the wine curve. That one I should manage by squaking left and right. If I run into serius problems doing this thing, then I will ditch the program.

6:10pm. Time for lunch.

6:30pm. Done. Let me close here for the day. It is an ideal time for it. I've almost exceeded my old high in Blender. I still do not have all the elements from the Blender file yet, but I'll get there.

Tomorrow what I will do is finally play around with the scatter and distribute those flowers where they belong. In addition to the two big main vines, I'll have to distribute some auxiliary wines by hand.

My reasoning is telling me to drop Houdini, but something inside me is telling me to persevere. I still don't even know 1% of the total nodes. I need to study it more. At the very least, let me do a single scene start to finish in Houdini.

6:40pm. As slow as it is, I think I am starting to recover just a bit of my sense of taste and smell. Maybe in a week I'll be able to get back to speed.

6:45pm. If Heaven's Key ends up being delayed due to me taking wrong turns in the art maze, I'll have no choice but apoologize. But until then I should persevere. Let me relax here.

Days like this where I put in a couple of hours are the best."

---
## [bmourad01/bap](https://github.com/bmourad01/bap)@[368286012d...](https://github.com/bmourad01/bap/commit/368286012d31312cfc785d940dd89e1f882c7bff)
#### Saturday 2022-02-05 19:35:42 by Ivan Gotovchits

relaxes the Apply.binop function to allow not well-typed operations (#1422)

We are not changing the typing rules of BIL or Core Theory, but
providing a well-defined behavior for application of binary operations
on bitvectors with unequal lengths. Before that, the behavior was
undefined and the precondition of the function was clearly specifying
that the inputs should be of equal lengths.

The new behavior is to promote words to the equal length, (much like
in C, which implicitly coerces the narrow type to the wider type).

The motivation is simple. It is hard to ensure this precondition in
general. Yes, our lifters produce well-typed code, so there are no
issues when we interpret code from the lifters. But we also have a lot
of different interpreters, extensible via primitives. And those
interpreters sometimes don't have any means (or at least efficient
means) to ensure that all binary operations have matching widths. A
concrete example of such interpreter is Veri that is used for
bi-interpretation of traces and BIL programs for
verification. Sometimes, the tracers organically produce ill-typed
code, as they rely on their own typing rules. For example, qemu-based
tracer just represent every register (including flags) and every
number (including bools) with a word-sized bitvector. We still want to
be able to perform calculations on such inputs and, to be honest, the
results are quite well-defined, no hacks required. In other words,
this change tries to follow the robustness principle, i.e., "be
conservative in what you do, be liberal in what you accept from
others". Our lifters, i.e., the code that we produce, are still much
conservative, but our interpreters tend to be more liberal and
understand even the ill-typed code, especially if this code has clear
semantics.

---
## [gorhom/react-native](https://github.com/gorhom/react-native)@[6c080167e6...](https://github.com/gorhom/react-native/commit/6c080167e6e342574298f43bb37becf139f6ac24)
#### Saturday 2022-02-05 19:41:38 by edenb-moveo

Update ImageBackground.js (#32055)

Summary:
Currently ImageBackGround component has optional style props, but if you don't pass it as prop, it still "thinks" you pass style and crushes.
In this pr, I made width and height inside component to be optional so it won't crush.

## Changelog

[General] [Fix] - Changed ImageBackground's style so it won't crush.

[Screen Shot 2021-08-20 at 15 05 45](https://user-images.githubusercontent.com/62840630/130230568-be02b1a2-52ec-4f9d-b3d3-212552d3882b.png)

As you can see in this component, I tried to use ImageBackground without any style props, and my app crushes. Then I added style with empty object and the app didn't crush anymore, as you can see here:
![Screen Shot 2021-08-20 at 15 09 23](https://user-images.githubusercontent.com/62840630/130230932-a576c397-a910-4e40-a202-56482d83dd9c.png).

In conclusion, if we make width and height styles optionals inside ImageBackground component, it won't crush anymore.

Thoughts:
Maybe consider to make style props for this component none-optional because it isn't make any sense that image won't have any style at all.

Thanks ahead, that was my first pr, Eden Binyamin.

Pull Request resolved: https://github.com/facebook/react-native/pull/32055

Reviewed By: charlesbdudley

Differential Revision: D30452297

Pulled By: sshic

fbshipit-source-id: b7071aa457dba443ed2f627c2458ea84fd24b36d

---
## [oantolin/emacs-config](https://github.com/oantolin/emacs-config)@[f09fcd9e81...](https://github.com/oantolin/emacs-config/commit/f09fcd9e8115daa220a319c4dc859ef36875c200)
#### Saturday 2022-02-05 19:49:47 by Omar Antolín

Go back to consult-completion-in-region

Corfu is very pretty and I do like that it pops up right at point, but
in the end I missed acting on completions more than I enjoyed the UI.

Corfu itself does cover the actions I want maybe 80% of the time: it
has corfu-show-location and corfu-show-documentation, which are great.
But I also occasionally want to use embark-collect-snapshot, or to put
several completion candidates on the kill-ring, or to mass insert
them (embark-act-all, embark-insert), or to look them up in the info
manual instead of describe-{function,variable}, or, as a special case
for email addresses, I want to use my remove-email-from-ecomplete
function to delete the email from my addressbook.

Maybe I should try the corfu-move-to-minibuffer command from the corfu
wiki, but honestly it just feels like an unnecessary extra step that
would be only justified if I disliked the consult-completion-in-region
UI and wanted to avoid it, but I was already perfectly used to it
before and I think I don't mind going back (we'll see). The key thing
is the consult preview: thanks to that, I often don't need to glance
down at the minibuffer!

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[95aa5be928...](https://github.com/Zeodexic/tsorcRevamp/commit/95aa5be928dae01ce3716ae6fa7fa317c34e2339)
#### Saturday 2022-02-05 21:28:22 by RecursiveCollapse

SHM Scaling and big balance pass on SHM enemies in general

Most SHM enemies now begin SHM with reduced health, defense, and damage. It increases with each boss killed, eventually growing past their previous health. Damage and other more sensitive stats scale up less than health does, only to 1.2x max vs 2x. Some enemies with *super* low health got theirs boosted. If it isn't enough, health may be reduced further. Additionally most enemies need more interesting and deadly attacks and more evasive movement, and their health will probably be reduced a bit when they get them.

Many SHM enemies now simply have their base projectile damage set to 1/4th its true value, instead of having it set to half and then getting halved in ScaleExpertStats. This has no effect on their final damage, but is a more simple way to do things.

Several SHM enemies with weirdly high or low stats got them brought back within normal ranges, such as:

Basilisk Hunter's Cursed Breath and Cursed Flames now do slightly more damage (54 > 80)
Barrow Wight Phantoms Dragons Breath now does much more damage
Barrow Wight Nemesis's Dragons Breath now *does* damage in the first place (this is likely why it used to curse so absurdly fast, no hit cooldown!)
Dark, Crystal, and Blood Knight's projectiles do slightly less damage
Corrupted Hornet's cursed fire does much more damage
Ice Skeletons are now different in certain ways. Be afraid.
Dramatically reduced Hydris Necromancer Death Strike damage (was almost 400 a hit lmfao)
Dramatically increased Slogra II's trident damage
Left Taurus Knight's crystal fire was not getting its damage cut in half like its other attacks. I'm leaving it as-is because I think it's fine, but feel it should be noted anyway.
Buffed Oolacile Knight's trident damage
Dramatically buffed Oolacile Demon's damage
Doubled damage of all of Artorias and Knight of Gwyn's attacks. They were all... *really* really low for SHM, to the point even mages barely took damage from them.
Guardian Corruptors now fire *much* faster and hitting them no longer interrupts their attack (resulting in easy stun locks)
Guardian Corruptors projectiles now move faster

---
## [ThomasDaheim/GPXEditor](https://github.com/ThomasDaheim/GPXEditor)@[281b3c1653...](https://github.com/ThomasDaheim/GPXEditor/commit/281b3c1653740891685a607971a0bfb312e56e39)
#### Saturday 2022-02-05 21:31:04 by Thomas Feuster

FUCK junit5

- made all the code changes
- "No test executed"
- FUCK YOU

---
## [NBtheMC/The-Adventurers-Guild](https://github.com/NBtheMC/The-Adventurers-Guild)@[7ba7db6ed9...](https://github.com/NBtheMC/The-Adventurers-Guild/commit/7ba7db6ed9393cb1e84a8e38d8d865b5c60ff2fa)
#### Saturday 2022-02-05 21:46:21 by Eric Long

Storylet System works. Fuck yeah.

fuck yeah. Shit's mostly done.

---
## [RSc0d3s/RSc0d3s](https://github.com/RSc0d3s/RSc0d3s)@[8a51c2a0b7...](https://github.com/RSc0d3s/RSc0d3s/commit/8a51c2a0b788d4204831a6aacffc97fdcd4fb897)
#### Saturday 2022-02-05 23:34:02 by Recca

RSc0d3s-patch-2.py

from future.moves import tkinter
from tkinter import *
from datetime import *

root = Tk()
root.title("Welcome to the Potter Dictionary.")

e = Entry(root, width=35, borderwidth=20)
e.pack()

def myClick():
    hello = "Hello, " + e.get()
    myLabel = Label(root, text =hello)
    myLabel.pack()S

#separate welcome window
myButton = Button(root, text= "Enter your name.", command = myClick)
myButton.pack()

print ("\n\n\tWelcome to the Wizarding World's Database of Spells, Charms, Enchantments and Curses.")

root.mainloop()

today = date.today()

year_of_birth = int(input("\n\nWhen were you born?\n\t Type in the year of your birth: "))

userAge = today.year - year_of_birth

#users must be >18 to access this program

Age_Restriction = 18

if userAge >= Age_Restriction:
    print("\n\nYou now have access to the Wizarding World's Database.")
    PotterDict = {"aberto":"opens locked doors.",
                "accio":"summon objects.",
                "aguamenti":"summons water.",
                "alohomora":"unlocks objects.",
                "anapneo":"clears someone's airway.",
                "aparecium":"reveals secret, written messages.",
                "apparate":"transportation spell that allows a witch or wizard to instantly travel on the spot.",
                "avis":"conjures a small flock of birds.",
                "avada kedavra":"is the killing curse.",
                "bat bogey bex":"turns the target's boogers into bats.",
                "bombardo":"creates an explosion.",
                "brackium emendo":"heals broken bones.",
                "capacious extremis":"is known as the Extension Charm.",
                "confundo":"is the confundus charm. Causes confusion to target.",
                "conjunctivitis curse":"affects the eyes and sight of a target.",
                "crinus muto":"changes hair color and style.",
                "crucio":"is one of three Unforgivable Curses, it causes unbearable pain in the target.",
                "diffindo":"is used to precisely cut an object.",
                "disillusionment charm":"causes the target to take on the appearance of its surroundings.",
                "disapparate":"a non-verbal transportation spell (apparate is the opposite).",
                "engorgio":"causes rapid growth in the targeted object.",
                "episkey":"heals minor injuries.",
                "expecto patronum":"a powerful projection of hope and happiness that drives away Dementors.",
                "erecto":"allows a witch or wizard to build a structure, like a tent.",
                "evanesco":"vanishes objects.",
                "expelliarmus":"forces an opponent to drop whatever's in their possession.",
                "ferula":"is a healing charm that conjures wraps and bandages for wounds.",
                "fidelius charm":"is a complex charm that conceals a secret into the soul of a chosen 'Secret Keeper'.",
                "fiendfyre curse":"conjures destructive, enormous enchanted flames.",
                "finite incantatem":"is a general counter-spell that's used to reverse or counter already cast charms.",
                "furnunculus curse":"is a jinx that causes a breakout of boils or pimples.",
                "geminio":"duplicates objects.",
                "glisseo":"transforms a staircase into a slide.",
                "iomenum revelio":"reveals the presence of another person.",
                "iomonculus charm":"detects anyone's true identity and location on a piece of parchment.",
                "immobulus":"immobilises living targets.",
                "impedimenta":"is a temporary jinx that slows the movement of the target.",
                "incarcerous":"conjures ropes.",
                "imperio":"places the target under the complete control of the caster.",
                "impervius":"makes an object waterproof.",
                "incendio":"conjures flames.",
                "langlock":"causes the target's tongue to stick to the roof of their mouth.",
                "legilimens":"invades or navigates another person's mind.",
                "levicorpus":"levitates the target by their ankle.",
                "locomotor mortis":"the Leg-Locker curse bounds the target's legs.",
                "lumos":"illuminates the caster's wand.",
                "morsmordre":"conjures and projects Lord Voldemort's Dark Mark.",
                "mucus ad nauseam":"inflicts an extreme runny nose or cold.",
                "muffliato":"creates a buzzing sound in the target's ears to prevent eavesdropping.",
                "nox":"reverses the lumos charm, extinguishing a wand's light.",
                "obliviate":"erases the target's memory.",
                "obscuro":"conjures a blindfold.",
                "oculus reparo":"repairs eyeglasses.",
                "oppugno":"directs an object or person to attack a victim.",
                "petrificus totalus":"Temporarily freezes or petrifies the body of the target.",
                "periculum":"conjures flares/red sparks.",
                "piertotum locomotor":"is used to bring to life inanimate objects and artifacts.",
                "protean charm":"link objects together for better communication.",
                "protego":"casts an invisible shield around the caster, protecting against spells and objects.",
                "reducto":"reduces the target to pieces.",
                "reducio":"shrinks an enlarged object to its regular size.",
                "renneverate":"awakens or revives the target.",
                "reparifors":"heals magical ailments like poisoning or paralysis.",
                "reparo":"fixes broken objects.",
                "rictusempra":"is a charm that disarms an opponent by tickling them.",
                "riddikulus":"is used to defeat a Boggart,the charm allows the scary creature to assume a comedic form.",
                "scourgify":"cleans objects.",
                "sectumsempra":"inflicts severe lacerations and hemorrhaging on the target.",
                "serpensortia":"conjures a live snake.",
                "silencio":"silences the target.",
                "sonorus":"amplifies the witch or wizard's voice.",
                "spongify":"aoftens the target.",
                "stupefy":"is the Stunning spell freezes objects and renders living targets unconscious.",
                "tarantallegra":"is aimed at the legs, causes uncontrollable dancing movement.",
                "unbreakable vow":"is a magically binding contract that results in the death of whoever breaks it.",
                "wingardium_leviosa":"causes an object to levitate.",}

    key = input("\n\n\tType in the spell or charm to see what it does: ").lower().strip()

    # key = spell

    if key in PotterDict:
        print ("\n\nThis spell or charm", PotterDict[key])

    while True:
        key = input("\n\n\tType in the spell or charm to see what it does: ").lower().strip()

        if key in PotterDict:
            print("\n\nThis spell or charm", PotterDict[key])

        else:
            print("Spell not found. A report has been sent to the Ministry of Magic.\n\t\tPlease EXIT the program.")
            endProgram()


else:
    print("\n\tMinors are not allowed access to this database. \n\t\tPlease EXIT the program.")

---
## [lfnandoc/RimWorldMod_ColonyLeadership](https://github.com/lfnandoc/RimWorldMod_ColonyLeadership)@[e600768fb4...](https://github.com/lfnandoc/RimWorldMod_ColonyLeadership/commit/e600768fb4d74de49e45051229615e81c5aee890)
#### Saturday 2022-02-05 23:56:10 by lfnandoc

Create README.md

Modificação para o jogo RimWorld. O mod foi descontinuado.


This mod add leaders and teaching to RimWorld. Works on current saves.

DOWNLOAD
Steam Workshop
A17: Dropbox
A16 (old): Dropbox

LEADERSHIP TYPES
-> Democracy: the normal type of leadership, where leaders are elected by vote.
-> NEW: Dictatorship: you make the rules and you select which colonist will be the leader. No elections and no "rebellions".

ELECTIONS
-> From the new "Leadership" main tab on the game window, you can manage leaders.
-> Build a ballot box so colonists can "use" them to gather the colony for an election.
-> Elections can be held on day 1, 7 or 15 of each season. Elections can be cancelled if something bad happens during it. Also, remember to build it on a nice spot safe from rain. (If you don't like this feature, you can use dev mode to trigger it)
-> When the election finished, the leaders will be elected.
-> 1 leader limit if the colony has less than 5 colonist. Otherwise, the limit is 2.
-> Be sure that the colonists have good needs before starting an election.
-> The colonists will decide who will be their leader and which type the leader will be.
-> Colonists unable to do social jobs will never be leaders.

LEADERS
-> Leaders will have a always-on buff that will increase some of its stats.
-> Leaders have improved trading prices, gift impact and chance to recruit prisoners.
-> Leadership level can be checked on the "Needs" tab and will influence the buffs.
-> Leaders emit an aura of stat-buffs to nearby colonists in the same room and is also influenced by the leadership level.
-> Leaders can inspire other colonists and give them a small mood buff.
-> The leadership level is calculated by what the colonists think about the leader and the skill levels have a little of influence on it.
-> Unpopular leaders can be asked to step out of power and, on worst cases, the colony can rebel against them and proceed to arrest them.
-> You cannot change leader types.
-> Leader mandate is 1 year.

LEADER TYPES
-> BOTANIST: specialized in Growing, Medicine and Animals. Stat buffs include plant work speed, immunity gain speed, taming chance and more.
-> WARRIOR: specialized in Shooting and Melee. Stat buffs include move speed, accuracy, hit chance and more.
-> CARPENTER: specialized in Crafting, Mining and Artistic. Stat buffs include construction speed, work speed, mining speed and more.
-> SCIENTIST: specialized in Research. Stat buffs include research speed, surgery success chance, learning speed and more.

TEACHING AND LESSONS
-> New buildable objects: teaching table, chalkboard and globe. Found on Architect/Misc.
-> Right now, only leaders can teach.
-> Teaching table is where leaders can hold lessons and teach the skills they are specialized in.
-> Build it, click on it and open its "Schedule" tab. There you can schedule lessons for the whole season, meaning each day you can choose if you want a lesson and which teacher will teach. You can also set which time of day the lesson will start.
-> You can also select which colonists will not join the lectures.
-> Leaders will only teach skills that are level 8 and above.
-> Assign leaders to colors, and use yellow if you want a random teacher that day.
-> You can only hold one lesson each 24 hours, to avoid exploitation.
-> Build the chalkboard and the globe to improve learning. The chalkboard is dynamic!

THANKS TO: The RimWorld mod community for being cool, FlatIcon for some textures I used and Jecrell who helped me getting lessons to work by allowing me to use his code as a reference.
Mods featured on screenshots: FashionRIMSta, Vegetable Garden, Facial Stuff.

Want to support me and my mods? Check out https://www.patreon.com/nandonalt

CHANGELOG
Code: [Select]

VERSON 1.3:
-> Updated for RimWorld Alpha 17
-> (Dev Mode) Added a button to change government type
-> Added keys for translation
Bugfixes:
-> Fixed a few typos.
-> Government types won't reset after changing home bases.

VERSON 1.2:
-> TYPES OF LEADERSHIP:
-> DEMOCRACY is the default leadership, and the leaders are elected by vote.
-> (WIP) A new type of leadership: DICTATORSHIP. On this type of government, you choose the leader and it'll last until it dies, and public opinion doesn't matter for dictators.
(Dictatorship is just a variation requested by users that prefer to choose who will lead the colony, it doesn't necessarily mean that it's an evil thing with propaganda and such).
-> Classrooms are now classified as such by the game.
-> Fixed a bug where the game would not consider leaders in caravan

VERSION 1.1:
->BALLOT BOX. You no longer can trigger elections on your own. You'll have to build the ballot box (found on Misc) on a safe spot and wait for the colonists start a election by themselves. Elections can happen on days 1, 7 and 15.
(If you didn't like this change, the button to start election is enabled on dev mode but will be removed on a later version)
-> You can now select which colonists will not attend lessons by using the new 'Ignore List' button on the schedule window.
-> Leaders now have a star on their colonist icon.
-> Fixed error showing up when there's no able leaders to select on the dev option.
-> Fixed caravan related bugs.
-> Fixed a bug where you could build multiple teaching table blueprints.

SCREENSHOTS





--------------------
** If you want to cheat leaders in, enable dev mode and use the add leader button. However going past the limit is a choice of yours and the effects can be different.
*** If you want to uninstall the mod, purge the leaders using dev mode and clicking the purge leaders button. This will remove traces of leadership on your colonists.

---

