## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-21](docs/good-messages/2021/2021-12-21.md)


1,734,571 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,734,571 were push events containing 2,524,670 commit messages that amount to 189,458,595 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [Tiresoup/tgstation](https://github.com/Tiresoup/tgstation)@[b2ba847c22...](https://github.com/Tiresoup/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Tuesday 2021-12-21 00:01:23 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [revenorror/Coveted-Treasures](https://github.com/revenorror/Coveted-Treasures)@[2f0e95b205...](https://github.com/revenorror/Coveted-Treasures/commit/2f0e95b205e0416cdfbd60980e3bfda90b0f5047)
#### Tuesday 2021-12-21 00:28:34 by revenorror

Esp update 4

Implemented magical gyroscope, War Horn of the World, Gilded steel longsword, compass, wolf head bust, painting 4 (The Dunes at Camiers), painting 5 (Water Lilies), paiting 6 (Untitled), wooden cat, anatomical figure 2, decorative plate, enameled vase, magnifying glass, ancient nordic bonesaw, rocking horse, mostrous skull, deer figurine, cup of the dragon god, gold goblet, beauty dominates strength,  hookah, genie's lamp, and stuffed whale
removed the capitoline wolf
Removed golden egg 06 from Niranye's house and moved it to a new location

---
## [sourajitk/device_essential_mata](https://github.com/sourajitk/device_essential_mata)@[23e3525ac5...](https://github.com/sourajitk/device_essential_mata/commit/23e3525ac593d2880648cc007f5e8ce79b1dc6f4)
#### Tuesday 2021-12-21 00:45:51 by Sourajit Karmakar

mata: Add EXPENSIVE_RENDERING hints for GPU

To start off, mata had a pretty shit kernel. This kernel neither used
efficient frequencies, nor had great battery life not to mention the
horrible performance. This was fine because most users never gave a fuck
and I (the only guy dailying mata and tinkering with this stuff) just
never had a pleasant experience with it.

Looking at the new Kawase blur implementation added to Android 11, I
couldn't help but want it ASAP. However, the kernel just wouldn't
cooperate (apparently). Anay wanted me to rebase the kernel because,
"our kernel visibly didn't respond to GPU boost hints triggered by
the surfaceflinger from rendering expensive blur."

Well after two lengthy kernel rebases (albeit useful ones as I was able
to eliminate a LOT OF JUNK), here we fucking go — it was never the kernel
my genius man xD. Power hint changes taken from [1].

* While at it, let's boost the GPU's minimum frequencies to the 515MHz
  (basically the third step from the maximum frequency step available to
  the Adreno 540), to further help this old 10nm chad render that beastly
  but gorgeous looking blur.

[1]: https://android.googlesource.com/device/google/coral/+/refs/tags/android-s-beta-2/powerhint.json#905

Change-Id: I8f72e68873ea46b8b7a562e5d292422d602cf42d

---
## [themilkman420/tgstation](https://github.com/themilkman420/tgstation)@[96b81f6c7f...](https://github.com/themilkman420/tgstation/commit/96b81f6c7f40fb9e103646e642a0e554a3841c18)
#### Tuesday 2021-12-21 00:58:53 by Wallem

Refactors Sign Language & Fixes Inconsistency (#62836)

Refactors Sign Language code so instead of copy-pasting the same giant wall of checks we can just use a proc.
Also now checks to see if your limb is disabled, which fixes people with disabled robotic limbs being able to sign still.
Finally, the tongue only has ORGAN_UNREMOVABLE if you attained it from the trait. I've been told that the tongue could be attained from meateors and I think that's funny as hell so I swapped that over.

---
## [alceo5/dugite](https://github.com/alceo5/dugite)@[7b4d332577...](https://github.com/alceo5/dugite/commit/7b4d332577c8db25d912f41701b829a7c59f02b3)
#### Tuesday 2021-12-21 01:24:01 by alceo5

Add files via upload

cute boy in love sucking dick of boyfriend

---
## [Auralcat/my-dotfiles](https://github.com/Auralcat/my-dotfiles)@[321a47f36c...](https://github.com/Auralcat/my-dotfiles/commit/321a47f36c99c5035165241280f5a3b3df231931)
#### Tuesday 2021-12-21 01:41:24 by Miriam Retka

Use evil-normal-state inside vterm-copy-mode

Inspiration:
https://dev.to/iggredible/the-easy-way-to-copy-text-in-tmux-319g

This article mentions Tmux copying pet peeves, and the scenario is not
that different for vterm-copy-mode. Turns out that using vi keys for
both cases is more comfortable, but I want to return to the emacs-state
when I leave the copy mode.

---
## [Gurky-Kronos/pfQuest-turtle](https://github.com/Gurky-Kronos/pfQuest-turtle)@[6bb36ee048...](https://github.com/Gurky-Kronos/pfQuest-turtle/commit/6bb36ee0489a4daab1b556d958f8cc384686f142)
#### Tuesday 2021-12-21 02:10:34 by Gurky

Quests, Items, Objects, Units

Added:

Quests:
You Reap What You Sow
Fallen Adventurers
Preventive Strike
Trapped in the Nightmare
Serpentbloom
Down With the Sickness
Preventing Poison
Kodo Hunt
Mother of the Hollow
Troubles From Distant Lands
Trader's Misfortune
Mastering the Arcane
Arcane Arms
A Glittering Opportunity
A Bloody Good Deed

Items:
Country Pumpkin Seeds
Mountain Berries Seeds
Striped Melon Seeds
Magic Mushroom Spores
Squealer Thornmantle's Mane
Sickly Gazelle Flesh Sample
Summer Dew
Life's Dawn
Vulpa Bloom
Moontouched Wood
Crystal of the Serpent
Everchanging Essence

Objects:
Ripe Garden Pumpkin
Garden Berry Bush
Ripe Garden Watermelon
Summer Dew
Life's Dawn
Vulpa Bloom
Mysterious Glittering Object

Units:
Kern Mosshoof
Chok'Garok
Ureda
Kheyna Spinpistol
Aneka Konko

I believe some of the quests need races,faction,classes added to them which I will visit later.

---
## [Chia-Network/chia-blockchain](https://github.com/Chia-Network/chia-blockchain)@[7949033929...](https://github.com/Chia-Network/chia-blockchain/commit/7949033929384e16d2537c179b1ee3fda7285959)
#### Tuesday 2021-12-21 02:29:48 by dustinface

tests: Use `temp_dir` as `tmp2_dir`, drop `temp_dir` if canceled (#9601)

If you currently cancel the test during the plot setup phase it just
removes the whole directoy and with it all the test plots for no good
reason. At least in my opinion its just annoying. Sure, you can clone
the `test-cache` repo and copy them over if this happens but i still
think its better to just merge this PR :)

---
## [Kitsunemitsu/KirieStation](https://github.com/Kitsunemitsu/KirieStation)@[0b5947a20f...](https://github.com/Kitsunemitsu/KirieStation/commit/0b5947a20f2f218ad0e3f972add1e6ea5a90a9b5)
#### Tuesday 2021-12-21 02:47:21 by Kirie Saito

6 MONTHS. SIX FUCKING MONTHS OF THIS CRAP I FINALLY FIXED IT (#376)

FUCK YOU

---
## [Henry2SS/incubator-doris](https://github.com/Henry2SS/incubator-doris)@[ef2ea1806e...](https://github.com/Henry2SS/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Tuesday 2021-12-21 02:57:25 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[60237fd855...](https://github.com/morgoth1145/advent-of-code/commit/60237fd8553b4e3a504d1e9483060002d5103a99)
#### Tuesday 2021-12-21 05:21:31 by Patrick Hogg

2021 Day 21 Part 2

Oh now *that* is a twist I didn't see coming! It took me too long to understand what the quantum die was supposed to do.. I was thinking the problem meant it rolled 1, 2, and 3 in separate universes then continued on but I couldn't find where the rules said that. Once I realized it really meant *just* those 3 results it made more sense!

Once I realized that, it became a simple recursive memoization problem. I love functools.cache!

Also RANK 29 WOOOO!!! I wonder how much time I could have saved by being quicker on the uptake, but I'll take it!

---
## [xamarin/xamarin-macios](https://github.com/xamarin/xamarin-macios)@[368cf1fbbb...](https://github.com/xamarin/xamarin-macios/commit/368cf1fbbb221b75b364962dc2d65cadc66e3518)
#### Tuesday 2021-12-21 07:08:43 by Rolf Bjarne Kvinge

[VTCompressionSession] Fix broken Create overloads for .NET. (#13589)

Once upon a time there was a single VTCompressionSession.Create method, which
was [driving users insane][1] - they had to manually call CFRetain to avoid
crashes! What an abomination!!

Insane users are clearly not happy users, and we wanted happy users, so time
and effort went into creating a solution: a new Create overload was devised
and [implemented][1], taking extreme care to not break our brave and insane
existing users who had to manually call CFRetain. Because the fix would break
existing users - the now extraneous CFRetain would mean that their apps would
leak memory. *A lot* of it! That's bad, so we decided to make sure that didn't
happen.

Of course, dear old Murhpy wanted a say, so the new Create overload didn't do
as intended. In fact, it had the same insane behavior the old Create overload
had! Ops.

But Murphy decided to have even more fun: the changes were so buggy, that they
in fact fixed the old Create overload! Which from now on wouldn't require the
horrendous manual CFRetain calls... and effectively introducing the leak the
fix was trying so hard to not introduce.

Oh dear Murphy.

Of course he had another trick up his sleeve: in our extreme efforts to help
our users, we added an Obsolete attribute that would tell people to use the
new Create overload.

Let that sink in for a moment: we had an Obsolete attribute on a function that
was (now) perfectly fine, telling users to use a function that was broken.

To get the correct behavior, users would now have to to remove their manual
CFRetain calls, and ignore the obsolete warning on the old (and correct)
Create overload which told users to use the new (and buggy) Create overload.

In other words: still insanity, just a slightly different flavor.

Murphy had a field day!

Time went by, and eventually a sane enough user [reported the insanity to
us][2]. Even better: the user actually provided a fix! Truly, we have some
amazing users.

Unfortunately, the user didn't have access to our code history, and thus was
obviously not able to see the whole picture, and the fix ended up being
incorrect.

Unrelated lesson learned: don't forget your history, otherwise you'll end up
repeating mistakes from the past.

So now came the problem: how to fix all the APIs? In a way that didn't make
our users' existing apps just suddenly start crashing or leaking?

There really was no way, so nothing really happened for quite a while.

Then, an opportunity presented itself: we'd be able to do [widespread breaking
changes][3].

So, hoping that Murphy stays away this sunny winter day, I'm changing both the
new and the old Create overloads to do the right thing. But only in .NET,
where we can do breaking changes! Or at least that's my intention. I've tried
to stave off our dear old friend by adding his arch enemy: unit tests. Which,
of course, Murphy couldn't stay away from, but it seems adding a few
Thread.Sleep calls makes him bored enough to stay away. Hopefully for good...

[1]: https://github.com/xamarin/maccore/commit/66c50b9a176c6edfa8e633bfd9b54831ebddc9e5
[2]: https://github.com/xamarin/xamarin-macios/pull/2070
[3]: https://github.com/xamarin/xamarin-macios/issues/13087

---
## [Caulaflower/CombatExtended](https://github.com/Caulaflower/CombatExtended)@[e9c4ac2915...](https://github.com/Caulaflower/CombatExtended/commit/e9c4ac29158608d0b4d0349dd2984784d954fba2)
#### Tuesday 2021-12-21 08:27:20 by AL9000

mortar

"You know what, fuck you!"
*replaces mortar def*

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[442912a65c...](https://github.com/mawrick26/SM8250/commit/442912a65cc1a8af09aaf64ce56686e61f58fb07)
#### Tuesday 2021-12-21 09:32:27 by George Spelvin

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
Signed-off-by: Forenche <prahul2003@gmail.com>

---
## [jandurovec/adventofcode-2021-in-kotlin](https://github.com/jandurovec/adventofcode-2021-in-kotlin)@[4ae4537c65...](https://github.com/jandurovec/adventofcode-2021-in-kotlin/commit/4ae4537c658be32ca59f52c27096bacbaaba86d1)
#### Tuesday 2021-12-21 09:33:37 by Jan Durovec

Add Day 21

The first part is quite straightforward but looks like a good
opportinuty to use sequences and windowed function. After I have the
sequence of dice roll sums, I easily learn the first star.

The description of the second part is not long but quite a bit harder to
understand. Some examples of at least the first steps would be helpful.

After some time I think I understand the requirement and write the code.
However, even though I'm pretty sure I got the algoritm correctly it
yields incorrect results. With no detailed information in the
description I have no idea whether I have a bug somewhere in the code or
I have misunderstood the task.

I think it's time for a break (and breakfast).

After aproximately another hour spent debugging the code and then
finally writing the first step on a piee of paper I realize that my
beautiful function to parse the input yields IntArray which is mutable,
so after calling part1(input) the input is no longer what it used to be
an I call my part2 function with incorrect arguments! :man_facepalming:

After I finally call the function with correct arguments I earn also the
second star.

---
## [no23reason/gooddata-ui-sdk](https://github.com/no23reason/gooddata-ui-sdk)@[d5312212c6...](https://github.com/no23reason/gooddata-ui-sdk/commit/d5312212c6dd00fb9f1f290cb65599947293ed91)
#### Tuesday 2021-12-21 09:45:52 by Dan Homola

Implement LRUCache and use it

Since the lru-cache in version 4 (the last compatible with IE11) needs
specific setup when used with Webpack 5 (process polyfills), it makes
GoodData.UI unusable with create-react-app 5 that migrated to Webpack 5
and makes it impossible to alter these settings out of the box.

As a workaround, we wanted to migrate to another LRU implementation,
however none of the reasonably used existing implementations were good
for our particular use cases (IE11 support and maxAge):

* quick-lru: does not support IE11 because it uses generators.
  Older versions do not have maxAge which we need
* tiny-lru: does not work with cache size 1 (I sent a PR to fix that
  but I do not expect that to be merged, the package is quite stale)
* hashlru: does not have maxAge

So I ended up implementing a LRU cache in our code base. The code uses
the hashlru algorithm and is heavily inspired by quick-lru (which we
should migrate to once IE11 is dropped and get rid of the version
added in this commit).

One particular caveat of the hashlru algorithm (that is not that
important in my opinion) is that the maxSize is not precise:
the cache can hold more keys than the maxSize, but not by much (it very
much depends on the particular sequence of inserts and evicts). It will,
however, never be more than twice the maxSize. Since we use the maxSize
as more of a "do not cache millions of items here" kind of mechanism,
I think this caveat is ok for us given the performance gains
and relative code simplicity.

JIRA: RAIL-2928

---
## [ilammy/themis](https://github.com/ilammy/themis)@[1ca96de89b...](https://github.com/ilammy/themis/commit/1ca96de89b66391114f615658fbc4819aa248b9b)
#### Tuesday 2021-12-21 11:27:10 by Alexei Lozovsky

Add missing OpenSSL includes (#684)

* Add missing OpenSSL includes

Add those files use BIGNUM API of OpenSSL but do not include relevant
headers. Due to miraculous coincidence, this seems to somehow work for
the OpenSSL versions we use, but only because either existing headers
include this "bn.h" transitively, or because the compiler generates
code that kinda works without function prototype being available.

However, curiously enough, this breaks when building Themis for macOS
with recent OpenSSL 1.1.1g but not with OpenSSL 1.0.2, or OpenSSL 1.1.1g
on Linux. The issue manifests itself as missing "_BN_num_bytes" symbol.
Indeed, there is no such symbol because this function is implemented as
a macro via BN_num_bits(). However, because of the missing header, the
compiler -- being C compiler -- decides that this must be a function
"int BN_num_bytes()" and compiles it like a function call.

Add the missing includes to define the necessary macros and prototype,
resolving the issue with OpenSSL 1.1.1g. It must have stopped including
<openssl/bn.h> transitively, revealing this issue.

This is why you should always include and import stuff you use directly,
not rely on transitive imports.

P.S. A mystery for dessert: BoringSSL backend *includes* <openssl/bn.h>.

* Treat warnings as errors in Xcode

In order to prevent more silly issues in the future, tell Xcode to tell
the compiler to treat all warnings as errors. That way the build should
fail earlier, and the developers will be less likely to ignore warnings.

* Fix implicit cast warnings

Now that we treat warnings as errors, let's fix them.

themis_auth_sym_kdf_context() accepts message length as "uint32_t" while
it's callers use "size_t" to avoid early casts and temporary values.
However, the message length has been checked earlier and will fit into
"uint32_t", we can safely perform explicit casts here.

* Suppress documentation warnings (temporarily)

Some OpenSSL headers packaged with Marcin's OpenSSL that we use have
borked documentation comments. This has been pointed out several
times [1][2], but Marcin concluded this needs to be fixed upstream.

[1]: https://github.com/krzyzanowskim/OpenSSL/pull/79
[2]: https://github.com/krzyzanowskim/OpenSSL/pull/41

Meanwhile, having those broken headers breaks the build if the warnings
are treated as errors. Since we can't upgrade Marcin's OpenSSL due to
other reasons (bitcode support), we have no hope to resolve this issue.

For the time being, suppress the warnings about documentation comments.

* Fix more implicit cast warnings

There are more warnings actual only for 32-bit platforms. Some iOS
targets are 32-bit, we should avoid warnings there as well.

The themis_scell_auth_token_key_size() and
themis_scell_auth_token_passphrase_size() functions compute the size of
the autentication token from the header. They return uint64_t values to
avoid overflows when working with corrupted input data on the decryption
code path. However, they are also used on the encryption path where
corruption is not possible. Normally, authentication tokens are small,
they most definitely fit into uint32_t, and this is the type used in
Secure Cell data format internally.

It is not safe to assign arbitrary uint64_t to size_t on 32-bit
platforms. However, in this case we are sure that auth tokenn length
fits into uint32_t, which can be safely assigned to size_t.

Note that we cast into uint32_t, not size_t. This is to still cause
a warning on platforms with 16-bit size_t (not likely, but cleaner).

---
## [isaaacme/isaaac.me](https://github.com/isaaacme/isaaac.me)@[688d7170c2...](https://github.com/isaaacme/isaaac.me/commit/688d7170c2c5403f5b2f87d8ed95c622a289c2f0)
#### Tuesday 2021-12-21 12:10:43 by isaac

Create Post “fuck-you-pay-me-is-so-much-more-than”

---
## [r-neal-kelly/nkr](https://github.com/r-neal-kelly/nkr)@[b687458637...](https://github.com/r-neal-kelly/nkr/commit/b6874586376072451aaa5231ca374af2b825dc36)
#### Tuesday 2021-12-21 13:55:46 by r-neal-kelly

okay, the tests are in and I think it's giving me a pretty clear picture, at least on my machine. The Visual C++ compiler cannot optimize away a wrapper. The boolean::cpp_t is on average apparently about twice as slow. And interestingly, I see now appreciable difference between using the boolean::cpp_t and the boolean::fast_t. It's as if the compiler is making the bool the size of the machine word in the binary where it would be faster anyway, which is great. So, I'm going to remove one of the wrappers and just keep one as a so-called safe boolean, which has no unwanted operators on it. Maybe someday I can figure out how to make it as fast as the fundamental. I've already decided that removing the destructors from all library types that don't need them is a pretty good idea. Believe it or not, even having an empty destructor causes the compiler to generate slower code, which I think is silly but I remember there being some reason why it doesn do that, maybe something to do with ABI or something. Anyway, it's a standard practice among standard library developers not to do that for this reason, so we'll be following it. It's true though that zero'ing out data in the destructor has saved me from leaving unseen bug in code before. So the best solution would be to have the destructors in debug mode only, which I may very end up doing. It's crappy though because we have to use the ugly preprocessor code to do it. But it's probably worth it.

---
## [near/nearcore](https://github.com/near/nearcore)@[23c5b07519...](https://github.com/near/nearcore/commit/23c5b07519c021f1af596e1aebb0675f1ab50dc1)
#### Tuesday 2021-12-21 14:34:46 by Aleksey Kladov

make it easier to understand how each cost is computed (#4733)

Ready to review!

This is a huge change which overhauls how parameter estimator works. Previously, we were running a bunch of estimations in order, which created interference between estimations (as they sometimes were re-using the same state), made it hard to run only subset of estimations (existing `--metrics-to-measure` flag partially alleviates the problem), and forced using a specific way to estimate all the costs (ie, if we wanted to use something else than "run a block with transactions" for estimation, that required ad-hoc code).

In the new setup, each cost is estimated by a single rust function. That function can do whatever, but there are helpers for common estimation methods, like the "run a block of transactions"  one. So, the end result looks like this: 

```rust
fn action_stake(ctx: &mut Ctx) -> GasCost {
    let total_cost = {
        let test_bed = ctx.test_bed();

        let mut make_transaction = |tb: &mut TransactionBuilder| -> SignedTransaction {
            let sender = tb.random_unused_account();
            let receiver = sender.clone();

            let actions = vec![Action::Stake(StakeAction {
                stake: 1,
                public_key: "22skMptHjFWNyuEWY22ftn2AbLPSYpmYwGJRGwpNHbTV".parse().unwrap(),
            })];
            tb.transaction_from_actions(sender, receiver, actions)
        };
        transaction_cost(test_bed, &mut make_transaction)
    };

    let base_cost = action_sir_receipt_creation(ctx);

    total_cost - base_cost
}
```

Notable changes in behavior: 

* we now prepare testbed with estimator contracts deployed. Previously, we prepared testbed with some trivial contract, and had a separate logic to populate it with estimator contracts. 
* we no-longer use `mean + 4*stddev` as the estimation. Instead, we just use `mean` but flag the cost as suspicious if we observe deviations of more than 15% during estimation. The two problems with stddev is that:
  *  it gives you *some* number instead of saying "hey, your measures are highly inconsistent and I can't give a sensible estimate"
  * it's not entirely statistically sound, as we are calculating stdev over blocks, and block already aggregates many transactions. 

But overall I've tried to preserve existing behavior as much as possible. I don't have a guarantee that I didn't make some stupid mistake for every specific cost, but I generally cross-referenced new results with old estimator and with current costs, and didn't find anything super weird except for #4836. After this is merged, I want to go through each cost and make sure it actually gives a reasonable, reproducible result which accounts for IO costs and matches our currently reployed cost table.

---
## [sheldonmlee/dwm](https://github.com/sheldonmlee/dwm)@[67d76bdc68...](https://github.com/sheldonmlee/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2021-12-21 14:39:47 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [CharlesDesiderio/portfolio-v4](https://github.com/CharlesDesiderio/portfolio-v4)@[71e52078ed...](https://github.com/CharlesDesiderio/portfolio-v4/commit/71e52078ed40f4814bf90e5277649764f60a5129)
#### Tuesday 2021-12-21 14:56:36 by Charles Desiderio

Removed contact form becuase of 4chan. Seriously fuck you assholes

---
## [Mohdazimq6/Psych-Engine-0.5-Android-Port](https://github.com/Mohdazimq6/Psych-Engine-0.5-Android-Port)@[a4a70f1ec8...](https://github.com/Mohdazimq6/Psych-Engine-0.5-Android-Port/commit/a4a70f1ec8a6bacb7cbc4649c541eb83a0b9d57c)
#### Tuesday 2021-12-21 15:44:50 by Mohdazimq6

package editors;  #if desktop import Discord.DiscordClient; #end import Conductor.BPMChangeEvent; import Section.SwagSection; import Song.SwagSong; import flixel.FlxG; import flixel.FlxSprite; import flixel.FlxObject; import flixel.group.FlxSpriteGroup; import flixel.input.keyboard.FlxKey; import flixel.addons.display.FlxGridOverlay; import flixel.addons.ui.FlxInputText; import flixel.addons.ui.FlxUI9SliceSprite; import flixel.addons.ui.FlxUI; import flixel.addons.ui.FlxUICheckBox; import flixel.addons.ui.FlxUIInputText; import flixel.addons.ui.FlxUINumericStepper; import flixel.addons.ui.FlxUITabMenu; import flixel.addons.ui.FlxUITooltip.FlxUITooltipStyle; import flixel.addons.transition.FlxTransitionableState; import flixel.group.FlxGroup.FlxTypedGroup; import flixel.group.FlxGroup; import flixel.math.FlxMath; import flixel.math.FlxPoint; import flixel.system.FlxSound; import flixel.text.FlxText; import flixel.ui.FlxButton; import flixel.ui.FlxSpriteButton; import flixel.util.FlxColor; import haxe.Json; import haxe.format.JsonParser; import lime.utils.Assets; import openfl.events.Event; import openfl.events.IOErrorEvent; import openfl.media.Sound; import openfl.net.FileReference; import openfl.utils.ByteArray; import openfl.utils.Assets as OpenFlAssets; import lime.media.AudioBuffer; import haxe.io.Bytes; import flash.geom.Rectangle; import flixel.util.FlxSort; #if MODS_ALLOWED import sys.io.File; import sys.FileSystem; import flash.media.Sound; #end  using StringTools;  class ChartingState extends MusicBeatState { 	public static var noteTypeList:Array<String> = //Used for backwards compatibility with 0.1 - 0.3.2 charts, though, you should add your hardcoded custom note types here too. 	[ 		'', 		'Alt Animation', 		'Hey!', 		'Hurt Note', 		'GF Sing', 		'No Animation' 	]; 	private var noteTypeIntMap:Map<Int, String> = new Map<Int, String>(); 	private var noteTypeMap:Map<String, Null<Int>> = new Map<String, Null<Int>>();  	var eventStuff:Array<Dynamic> = 	[ 		['', "Nothing. Yep, that's right."], 		['Hey!', "Plays the \"Hey!\" animation from Bopeebo,\nValue 1: BF = Only Boyfriend, GF = Only Girlfriend,\nSomething else = Both.\nValue 2: Custom animation duration,\nleave it blank for 0.6s"], 		['Set GF Speed', "Sets GF head bopping speed,\nValue 1: 1 = Normal speed,\n2 = 1/2 speed, 4 = 1/4 speed etc.\nUsed on Fresh during the beatbox parts.\n\nWarning: Value must be integer!"], 		['Blammed Lights', "Value 1: 0 = Turn off, 1 = Blue, 2 = Green,\n3 = Pink, 4 = Red, 5 = Orange, Anything else = Random."], 		['Kill Henchmen', "For Mom's songs, don't use this please, i love them :("], 		['Add Camera Zoom', "Used on MILF on that one \"hard\" part\nValue 1: Camera zoom add (Default: 0.015)\nValue 2: UI zoom add (Default: 0.03)\nLeave the values blank if you want to use Default."], 		['BG Freaks Expression', "Should be used only in \"school\" Stage!"], 		['Trigger BG Ghouls', "Should be used only in \"schoolEvil\" Stage!"], 		['Play Animation', "Plays an animation on a Character,\nonce the animation is completed,\nthe animation changes to Idle\n\nValue 1: Animation to play.\nValue 2: Character (Dad, BF, GF)"], 		['Camera Follow Pos', "Value 1: X\nValue 2: Y\n\nThe camera won't change the follow point\nafter using this, for getting it back\nto normal, leave both values blank."], 		['Alt Idle Animation', "Sets a specified suffix after the idle animation name.\nYou can use this to trigger 'idle-alt' if you set\nValue 2 to -alt\n\nValue 1: Character to set (Dad, BF or GF)\nValue 2: New suffix (Leave it blank to disable)"], 		['Screen Shake', "Value 1: Camera shake\nValue 2: HUD shake\n\nEvery value works as the following example: \"1, 0.05\".\nThe first number (1) is the duration.\nThe second number (0.05) is the intensity."], 		['Change Character', "Value 1: Character to change (Dad, BF, GF)\nValue 2: New character's name"], 		['Change Scroll Speed', "Value 1: Target value\nValue 2: Time it takes to change fully"] 	];  	var _file:FileReference;  	var UI_box:FlxUITabMenu;  	/** 	 * Array of notes showing when each section STARTS in STEPS 	 * Usually rounded up?? 	 */ 	public static var curSection:Int = 0; 	public static var lastSection:Int = 0; 	private static var lastSong:String = '';  	var bpmTxt:FlxText;  	var camPos:FlxObject; 	var strumLine:FlxSprite; 	var quant:AttachedSprite; 	var strumLineNotes:FlxTypedGroup<StrumNote>; 	var curSong:String = 'Dadbattle'; 	var amountSteps:Int = 0; 	var bullshitUI:FlxGroup;  	var highlight:FlxSprite;  	public static var GRID_SIZE:Int = 40; 	var CAM_OFFSET:Int = 360;  	var dummyArrow:FlxSprite;  	var curRenderedSustains:FlxTypedGroup<FlxSprite>; 	var curRenderedNotes:FlxTypedGroup<Note>; 	var curRenderedNoteType:FlxTypedGroup<FlxText>;  	var nextRenderedSustains:FlxTypedGroup<FlxSprite>; 	var nextRenderedNotes:FlxTypedGroup<Note>;  	var gridBG:FlxSprite; 	var gridMult:Int = 2;  	var daquantspot = 0; 	var curEventSelected:Int = 0; 	 	var _song:SwagSong; 	/* 	 * WILL BE THE CURRENT / LAST PLACED NOTE 	**/ 	var curSelectedNote:Array<Dynamic> = null;  	var tempBpm:Float = 0;  	var vocals:FlxSound = null;  	var leftIcon:HealthIcon; 	var rightIcon:HealthIcon;  	var value1InputText:FlxUIInputText; 	var value2InputText:FlxUIInputText; 	var currentSongName:String; 	 	var zoomTxt:FlxText; 	var curZoom:Int = 1;  	#if !html5 	var zoomList:Array<Float> = [ 		0.5, 		1, 		2, 		4, 		8, 		12, 		16, 		24 	]; 	#else //The grid gets all black when over 1/12 snap 	var zoomList:Array<Float> = [ 		0.5, 		1, 		2, 		4, 		8, 		12 	]; 	#end  	private var blockPressWhileTypingOn:Array<FlxUIInputText> = []; 	private var blockPressWhileScrolling:Array<FlxUIDropDownMenuCustom> = [];  	var waveformSprite:FlxSprite; 	var gridLayer:FlxTypedGroup<FlxSprite>; 	//public var quants:Array<Float> = [4,2,1]; 	/**/ 	  	public var quants:Array<Float> = [ 	4,// quarter 	2,//half 	4/3, 	1, 	4/8];//eight 	 	 	public static var curQuant = 0; 	var text:String = ""; 	public static var vortex:Bool = false; 	override function create() 	{ 		if (PlayState.SONG != null) 			_song = PlayState.SONG; 		else 		{ 			_song = { 				song: 'Test', 				notes: [], 				events: [], 				bpm: 150.0, 				needsVoices: true, 				arrowSkin: '', 				splashSkin: 'noteSplashes',//idk it would crash if i didn't 				player1: 'bf', 				player2: 'dad', 				player3: null, 				gfVersion: 'gf', 				speed: 1, 				stage: 'stage', 				validScore: false 			}; 			addSection(); 			PlayState.SONG = _song; 		} 		#if MODS_ALLOWED 		Paths.destroyLoadedImages(); 		#end  		#if desktop 		// Updating Discord Rich Presence 		DiscordClient.changePresence("Chart Editor", StringTools.replace(_song.song, '-', ' ')); 		#end  		vortex = FlxG.save.data.chart_vortex; 		var bg:FlxSprite = new FlxSprite().loadGraphic(Paths.image('menuDesat')); 		bg.scrollFactor.set(); 		bg.color = 0xFF222222; 		add(bg);  		gridLayer = new FlxTypedGroup<FlxSprite>(); 		add(gridLayer);  		waveformSprite = new FlxSprite(GRID_SIZE, 0).makeGraphic(FlxG.width, FlxG.height, 0x00FFFFFF); 		add(waveformSprite);  		var eventIcon:FlxSprite = new FlxSprite(-GRID_SIZE - 5, -90).loadGraphic(Paths.image('eventArrow')); 		leftIcon = new HealthIcon('bf'); 		rightIcon = new HealthIcon('dad'); 		eventIcon.scrollFactor.set(1, 1); 		leftIcon.scrollFactor.set(1, 1); 		rightIcon.scrollFactor.set(1, 1);  		eventIcon.setGraphicSize(30, 30); 		leftIcon.setGraphicSize(0, 45); 		rightIcon.setGraphicSize(0, 45);  		add(eventIcon); 		add(leftIcon); 		add(rightIcon);  		leftIcon.setPosition(GRID_SIZE + 10, -100); 		rightIcon.setPosition(GRID_SIZE * 5.2, -100);  		curRenderedSustains = new FlxTypedGroup<FlxSprite>(); 		curRenderedNotes = new FlxTypedGroup<Note>(); 		curRenderedNoteType = new FlxTypedGroup<FlxText>();  		nextRenderedSustains = new FlxTypedGroup<FlxSprite>(); 		nextRenderedNotes = new FlxTypedGroup<Note>();  		if(curSection >= _song.notes.length) curSection = _song.notes.length - 1;  		FlxG.mouse.visible = true; 		//FlxG.save.bind('funkin', 'ninjamuffin99');  		tempBpm = _song.bpm;  		addSection();  		// sections = _song.notes;  		currentSongName = Paths.formatToSongPath(_song.song); 		loadAudioBuffer(); 		reloadGridLayer(); 		loadSong(); 		Conductor.changeBPM(_song.bpm); 		Conductor.mapBPMChanges(_song);  		bpmTxt = new FlxText(1000, 50, 0, "", 16); 		bpmTxt.scrollFactor.set(); 		add(bpmTxt);  		strumLine = new FlxSprite(0, 50).makeGraphic(Std.int(GRID_SIZE * 9), 4); 		add(strumLine);  		quant = new AttachedSprite('chart_quant','chart_quant'); 		quant.animation.addByPrefix('q','chart_quant',0,false); 		quant.animation.play('q', true, false, 0); 		quant.sprTracker = strumLine; 		quant.xAdd = -32; 		quant.yAdd = 8; 		add(quant); 		 		strumLineNotes = new FlxTypedGroup<StrumNote>(); 		for (i in 0...8){ 			var note:StrumNote = new StrumNote(GRID_SIZE * (i+1), strumLine.y, i % 4, 0); 			note.setGraphicSize(GRID_SIZE, GRID_SIZE); 			note.updateHitbox(); 			note.playAnim('static', true); 			strumLineNotes.add(note); 			note.scrollFactor.set(1, 1); 		} 		add(strumLineNotes);  		camPos = new FlxObject(0, 0, 1, 1); 		camPos.setPosition(strumLine.x + CAM_OFFSET, strumLine.y);  		dummyArrow = new FlxSprite().makeGraphic(GRID_SIZE, GRID_SIZE); 		add(dummyArrow);  		var tabs = [ 			{name: "Song", label: 'Song'}, 			{name: "Section", label: 'Section'}, 			{name: "Note", label: 'Note'}, 			{name: "Events", label: 'Events'}, 			{name: "Charting", label: 'Charting'}, 		];  		UI_box = new FlxUITabMenu(null, tabs, true);  		UI_box.resize(300, 400); 		UI_box.x = FlxG.width / 2 + GRID_SIZE / 2; 		UI_box.y = 25; 		UI_box.scrollFactor.set();  		text = 		"W/S or Mouse Wheel - Change Conductor's strum time 		\nA or Left/D or Right - Go to the previous/next section 		\nHold Shift to move 4x faster 		\nHold Control and click on an arrow to select it 		\nZ/X - Zoom in/out 		\n 		\nEsc - Test your chart inside Chart Editor 		\nEnter - Play your chart 		\nQ/E - Decrease/Increase Note Sustain Length 		\nSpace - Stop/Resume song";  		var tipTextArray:Array<String> = text.split('\n'); 		for (i in 0...tipTextArray.length) { 			var tipText:FlxText = new FlxText(UI_box.x, UI_box.y + UI_box.height + 8, 0, tipTextArray[i], 16); 			tipText.y += i * 14; 			tipText.setFormat(Paths.font("vcr.ttf"), 16, FlxColor.WHITE, LEFT/*, FlxTextBorderStyle.OUTLINE, FlxColor.BLACK*/); 			//tipText.borderSize = 2; 			tipText.scrollFactor.set(); 			add(tipText); 		} 		add(UI_box);  		addSongUI(); 		addSectionUI(); 		addNoteUI(); 		addEventsUI(); 		addChartingUI(); 		updateHeads(); 		updateWaveform(); 		//UI_box.selected_tab = 4;  		add(curRenderedSustains); 		add(curRenderedNotes); 		add(curRenderedNoteType); 		add(nextRenderedSustains); 		add(nextRenderedNotes);  		if(lastSong != currentSongName) { 			changeSection(); 		} 		lastSong = currentSongName;  		zoomTxt = new FlxText(10, 10, 0, "Zoom: 1x", 16); 		zoomTxt.scrollFactor.set(); 		add(zoomTxt); 		 		updateGrid();  		#if mobileC 		addVirtualPad(FULL, A_B); 		#end  		super.create(); 	}  	var check_mute_inst:FlxUICheckBox = null; 	var check_vortex:FlxUICheckBox = null; 	var playSoundBf:FlxUICheckBox = null; 	var playSoundDad:FlxUICheckBox = null; 	var UI_songTitle:FlxUIInputText; 	var noteSkinInputText:FlxUIInputText; 	var noteSplashesInputText:FlxUIInputText; 	var stageDropDown:FlxUIDropDownMenuCustom; 	function addSongUI():Void 	{ 		UI_songTitle = new FlxUIInputText(10, 10, 70, _song.song, 8); 		blockPressWhileTypingOn.push(UI_songTitle); 		 		var check_voices = new FlxUICheckBox(10, 25, null, null, "Has voice track", 100); 		check_voices.checked = _song.needsVoices; 		// _song.needsVoices = check_voices.checked; 		check_voices.callback = function() 		{ 			_song.needsVoices = check_voices.checked; 			//trace('CHECKED!'); 		};  		var saveButton:FlxButton = new FlxButton(110, 8, "Save", function() 		{ 			saveLevel(); 		});  		var reloadSong:FlxButton = new FlxButton(saveButton.x + 90, saveButton.y, "Reload Audio", function() 		{ 			currentSongName = Paths.formatToSongPath(UI_songTitle.text); 			loadSong(); 			loadAudioBuffer(); 			updateWaveform(); 		});  		var reloadSongJson:FlxButton = new FlxButton(reloadSong.x, saveButton.y + 30, "Reload JSON", function() 		{ 			loadJson(_song.song.toLowerCase()); 		});  		var loadAutosaveBtn:FlxButton = new FlxButton(reloadSongJson.x, reloadSongJson.y + 30, 'Load Autosave', function() 		{ 			PlayState.SONG = Song.parseJSONshit(FlxG.save.data.autosave); 			MusicBeatState.resetState(); 		});  		var loadEventJson:FlxButton = new FlxButton(loadAutosaveBtn.x, loadAutosaveBtn.y + 30, 'Load Events', function() 		{ 			var songName:String = Paths.formatToSongPath(_song.song); 			var file:String = Paths.json(songName + '/events'); 			#if sys 			if (#if MODS_ALLOWED FileSystem.exists(Paths.modsJson(songName + '/events')) || #end FileSystem.exists(file)) 			#else 			if (OpenFlAssets.exists(file)) 			#end 			{ 				clearEvents(); 				var events:SwagSong = Song.loadFromJson('events', songName); 				_song.events = events.events; 				changeSection(curSection); 			} 		});  		var saveEvents:FlxButton = new FlxButton(110, reloadSongJson.y, 'Save Events', function () 		{ 			saveEvents(); 		});  		var clear_events:FlxButton = new FlxButton(320, 310, 'Clear events', function() 			{ 				clearEvents(); 			}); 		clear_events.color = FlxColor.RED; 		clear_events.label.color = FlxColor.WHITE;  		var clear_notes:FlxButton = new FlxButton(320, clear_events.y + 30, 'Clear notes', function() 			{ 				for (sec in 0..._song.notes.length) { 					_song.notes[sec].sectionNotes = []; 				} 				updateGrid(); 			}); 		clear_notes.color = FlxColor.RED; 		clear_notes.label.color = FlxColor.WHITE;  		var stepperBPM:FlxUINumericStepper = new FlxUINumericStepper(10, 70, 1, 1, 1, 339, 1); 		stepperBPM.value = Conductor.bpm; 		stepperBPM.name = 'song_bpm';  		var stepperSpeed:FlxUINumericStepper = new FlxUINumericStepper(10, stepperBPM.y + 35, 0.1, 1, 0.1, 10, 1); 		stepperSpeed.value = _song.speed; 		stepperSpeed.name = 'song_speed';  		#if MODS_ALLOWED 		var directories:Array<String> = [Paths.mods('characters/'), Paths.mods(Paths.currentModDirectory + '/characters/'), Main.getDataPath() + Paths.getPreloadPath('characters/')]; 		#else 		var directories:Array<String> = [Paths.getPreloadPath('characters/')]; 		#end  		var tempMap:Map<String, Bool> = new Map<String, Bool>(); 		var characters:Array<String> = CoolUtil.coolTextFile(Main.getDataPath() + Paths.txt('characterList')); 		for (i in 0...characters.length) { 			tempMap.set(characters[i], true); 		}  		#if MODS_ALLOWED 		for (i in 0...directories.length) { 			var directory:String = directories[i]; 			if(FileSystem.exists(directory)) { 				for (file in FileSystem.readDirectory(directory)) { 					var path = haxe.io.Path.join([directory, file]); 					if (!FileSystem.isDirectory(path) && file.endsWith('.json')) { 						var charToCheck:String = file.substr(0, file.length - 5); 						if(!charToCheck.endsWith('-dead') && !tempMap.exists(charToCheck)) { 							tempMap.set(charToCheck, true); 							characters.push(charToCheck); 						} 					} 				} 			} 		} 		#end  		var player1DropDown = new FlxUIDropDownMenuCustom(10, stepperSpeed.y + 45, FlxUIDropDownMenuCustom.makeStrIdLabelArray(characters, true), function(character:String) 		{ 			_song.player1 = characters[Std.parseInt(character)]; 			updateHeads(); 		}); 		player1DropDown.selectedLabel = _song.player1; 		blockPressWhileScrolling.push(player1DropDown);  		var player3DropDown = new FlxUIDropDownMenuCustom(player1DropDown.x, player1DropDown.y + 40, FlxUIDropDownMenuCustom.makeStrIdLabelArray(characters, true), function(character:String) 		{ 			_song.gfVersion = characters[Std.parseInt(character)]; 			updateHeads(); 		}); 		player3DropDown.selectedLabel = _song.gfVersion; 		blockPressWhileScrolling.push(player3DropDown);  		var player2DropDown = new FlxUIDropDownMenuCustom(player1DropDown.x, player3DropDown.y + 40, FlxUIDropDownMenuCustom.makeStrIdLabelArray(characters, true), function(character:String) 		{ 			_song.player2 = characters[Std.parseInt(character)]; 			updateHeads(); 		}); 		player2DropDown.selectedLabel = _song.player2; 		blockPressWhileScrolling.push(player2DropDown);  		#if MODS_ALLOWED 		var directories:Array<String> = [Paths.mods('stages/'), Paths.mods(Paths.currentModDirectory + '/stages/'), Main.getDataPath() + Paths.getPreloadPath('stages/')]; 		#else 		var directories:Array<String> = [Paths.getPreloadPath('stages/')]; 		#end  		tempMap.clear(); 		var stageFile:Array<String> = CoolUtil.coolTextFile(Main.getDataPath() + Paths.txt('stageList')); 		var stages:Array<String> = []; 		for (i in 0...stageFile.length) { //Prevent duplicates 			var stageToCheck:String = stageFile[i]; 			if(!tempMap.exists(stageToCheck)) { 				stages.push(stageToCheck); 			} 			tempMap.set(stageToCheck, true); 		} 		#if MODS_ALLOWED 		for (i in 0...directories.length) { 			var directory:String = directories[i]; 			if(FileSystem.exists(directory)) { 				for (file in FileSystem.readDirectory(directory)) { 					var path = haxe.io.Path.join([directory, file]); 					if (!FileSystem.isDirectory(path) && file.endsWith('.json')) { 						var stageToCheck:String = file.substr(0, file.length - 5); 						if(!tempMap.exists(stageToCheck)) { 							tempMap.set(stageToCheck, true); 							stages.push(stageToCheck); 						} 					} 				} 			} 		} 		#end  		if(stages.length < 1) stages.push('stage');  		stageDropDown = new FlxUIDropDownMenuCustom(player1DropDown.x + 140, player1DropDown.y, FlxUIDropDownMenuCustom.makeStrIdLabelArray(stages, true), function(character:String) 		{ 			_song.stage = stages[Std.parseInt(character)]; 		}); 		stageDropDown.selectedLabel = _song.stage; 		blockPressWhileScrolling.push(stageDropDown);  		var skin = PlayState.SONG.arrowSkin; 		if(skin == null) skin = ''; 		noteSkinInputText = new FlxUIInputText(player2DropDown.x, player2DropDown.y + 50, 150, skin, 8); 		noteSkinInputText.focusGained = () -> FlxG.stage.window.textInputEnabled = true;		 		blockPressWhileTypingOn.push(noteSkinInputText); 	 		noteSplashesInputText = new FlxUIInputText(noteSkinInputText.x, noteSkinInputText.y + 35, 150, _song.splashSkin, 8); 		noteSplashesInputText.focusGained = () -> FlxG.stage.window.textInputEnabled = true;		 		blockPressWhileTypingOn.push(noteSplashesInputText);  		var reloadNotesButton:FlxButton = new FlxButton(noteSplashesInputText.x + 5, noteSplashesInputText.y + 20, 'Change Notes', function() { 			_song.arrowSkin = noteSkinInputText.text; 			updateGrid(); 		});  		var tab_group_song = new FlxUI(null, UI_box); 		tab_group_song.name = "Song"; 		tab_group_song.add(UI_songTitle);  		tab_group_song.add(check_voices); 		tab_group_song.add(clear_events); 		tab_group_song.add(clear_notes); 		tab_group_song.add(saveButton); 		tab_group_song.add(saveEvents); 		tab_group_song.add(reloadSong); 		tab_group_song.add(reloadSongJson); 		tab_group_song.add(loadAutosaveBtn); 		tab_group_song.add(loadEventJson); 		tab_group_song.add(stepperBPM); 		tab_group_song.add(stepperSpeed); 		tab_group_song.add(reloadNotesButton); 		tab_group_song.add(noteSkinInputText); 		tab_group_song.add(noteSplashesInputText); 		tab_group_song.add(new FlxText(stepperBPM.x, stepperBPM.y - 15, 0, 'Song BPM:')); 		tab_group_song.add(new FlxText(stepperSpeed.x, stepperSpeed.y - 15, 0, 'Song Speed:')); 		tab_group_song.add(new FlxText(player2DropDown.x, player2DropDown.y - 15, 0, 'Opponent:')); 		tab_group_song.add(new FlxText(player3DropDown.x, player3DropDown.y - 15, 0, 'Girlfriend:')); 		tab_group_song.add(new FlxText(player1DropDown.x, player1DropDown.y - 15, 0, 'Boyfriend:')); 		tab_group_song.add(new FlxText(stageDropDown.x, stageDropDown.y - 15, 0, 'Stage:')); 		tab_group_song.add(new FlxText(noteSkinInputText.x, noteSkinInputText.y - 15, 0, 'Note Texture:')); 		tab_group_song.add(new FlxText(noteSplashesInputText.x, noteSplashesInputText.y - 15, 0, 'Note Splashes Texture:')); 		tab_group_song.add(player2DropDown); 		tab_group_song.add(player3DropDown); 		tab_group_song.add(player1DropDown); 		tab_group_song.add(stageDropDown);  		UI_box.addGroup(tab_group_song);  		FlxG.camera.follow(camPos); 	}  	var stepperLength:FlxUINumericStepper; 	var check_mustHitSection:FlxUICheckBox; 	var check_gfSection:FlxUICheckBox; 	var check_changeBPM:FlxUICheckBox; 	var stepperSectionBPM:FlxUINumericStepper; 	var check_altAnim:FlxUICheckBox;  	var sectionToCopy:Int = 0; 	var notesCopied:Array<Dynamic>;  	function addSectionUI():Void 	{ 		var tab_group_section = new FlxUI(null, UI_box); 		tab_group_section.name = 'Section';  		stepperLength = new FlxUINumericStepper(10, 10, 4, 0, 0, 999, 0); 		stepperLength.value = _song.notes[curSection].lengthInSteps; 		stepperLength.name = 'section_length';  		check_mustHitSection = new FlxUICheckBox(10, 30, null, null, "Must hit section", 100); 		check_mustHitSection.name = 'check_mustHit'; 		check_mustHitSection.checked = _song.notes[curSection].mustHitSection;  		check_gfSection = new FlxUICheckBox(130, 30, null, null, "GF section", 100); 		check_gfSection.name = 'check_gf'; 		check_gfSection.checked = _song.notes[curSection].gfSection; 		// _song.needsVoices = check_mustHit.checked;  		check_altAnim = new FlxUICheckBox(10, 60, null, null, "Alt Animation", 100); 		check_altAnim.checked = _song.notes[curSection].altAnim; 		check_altAnim.name = 'check_altAnim';  		check_changeBPM = new FlxUICheckBox(10, 90, null, null, 'Change BPM', 100); 		check_changeBPM.checked = _song.notes[curSection].changeBPM; 		check_changeBPM.name = 'check_changeBPM';  		stepperSectionBPM = new FlxUINumericStepper(10, 110, 1, Conductor.bpm, 0, 999, 1); 		if(check_changeBPM.checked) { 			stepperSectionBPM.value = _song.notes[curSection].bpm; 		} else { 			stepperSectionBPM.value = Conductor.bpm; 		} 		stepperSectionBPM.name = 'section_bpm';   		var copyButton:FlxButton = new FlxButton(10, 150, "Copy Section", function() 		{ 			notesCopied = []; 			sectionToCopy = curSection; 			for (i in 0..._song.notes[curSection].sectionNotes.length) 			{ 				var note:Array<Dynamic> = _song.notes[curSection].sectionNotes[i]; 				notesCopied.push(note); 			} 			 			var startThing:Float = sectionStartTime(); 			var endThing:Float = sectionStartTime(1); 			for (event in _song.events) 			{ 				var strumTime:Float = event[0]; 				if(endThing > event[0] && event[0] >= startThing) 				{ 					var copiedEventArray:Array<Dynamic> = []; 					for (i in 0...event[1].length) 					{ 						var eventToPush:Array<Dynamic> = event[1][i]; 						copiedEventArray.push([eventToPush[0], eventToPush[1], eventToPush[2]]); 					} 					notesCopied.push([strumTime, -1, copiedEventArray]); 				} 			} 		});  		var pasteButton:FlxButton = new FlxButton(10, 180, "Paste Section", function() 		{ 			if(notesCopied == null || notesCopied.length < 1) 			{ 				return; 			}  			var addToTime:Float = Conductor.stepCrochet * (_song.notes[curSection].lengthInSteps * (curSection - sectionToCopy)); 			//trace('Time to add: ' + addToTime);  			for (note in notesCopied) 			{ 				var copiedNote:Array<Dynamic> = []; 				var newStrumTime:Float = note[0] + addToTime; 				if(note[1] < 0) 				{ 					var copiedEventArray:Array<Dynamic> = []; 					for (i in 0...note[2].length) 					{ 						var eventToPush:Array<Dynamic> = note[2][i]; 						copiedEventArray.push([eventToPush[0], eventToPush[1], eventToPush[2]]); 					} 					_song.events.push([newStrumTime, copiedEventArray]); 				} 				else 				{ 					if(note[4] != null) { 						copiedNote = [newStrumTime, note[1], note[2], note[3], note[4]]; 					} else { 						copiedNote = [newStrumTime, note[1], note[2], note[3]]; 					}	 					_song.notes[curSection].sectionNotes.push(copiedNote); 				} 			} 			updateGrid(); 		});  		var clearSectionButton:FlxButton = new FlxButton(10, 210, "Clear", function() 		{ 			_song.notes[curSection].sectionNotes = []; 			 			var i:Int = _song.events.length - 1; 			 			var startThing:Float = sectionStartTime(); 			var endThing:Float = sectionStartTime(1); 			while(i > -1) { 				var event:Array<Dynamic> = _song.events[i]; 				if(event != null && endThing > event[0] && event[0] >= startThing) 				{ 					_song.events.remove(event); 				} 				--i; 			} 			updateGrid(); 			updateNoteUI(); 		});  		var swapSection:FlxButton = new FlxButton(10, 240, "Swap section", function() 		{ 			for (i in 0..._song.notes[curSection].sectionNotes.length) 			{ 				var note:Array<Dynamic> = _song.notes[curSection].sectionNotes[i]; 				note[1] = (note[1] + 4) % 8; 				_song.notes[curSection].sectionNotes[i] = note; 			} 			updateGrid(); 		});  		var stepperCopy:FlxUINumericStepper = new FlxUINumericStepper(110, 276, 1, 1, -999, 999, 0);  		var copyLastButton:FlxButton = new FlxButton(10, 270, "Copy last section", function() 		{ 			var value:Int = Std.int(stepperCopy.value); 			if(value == 0) return;  			var daSec = FlxMath.maxInt(curSection, value);  			for (note in _song.notes[daSec - value].sectionNotes) 			{ 				var strum = note[0] + Conductor.stepCrochet * (_song.notes[daSec].lengthInSteps * value);  				var copiedNote:Array<Dynamic> = [strum, note[1], note[2], note[3]]; 				_song.notes[daSec].sectionNotes.push(copiedNote); 			}  			var startThing:Float = sectionStartTime(-value); 			var endThing:Float = sectionStartTime(-value + 1); 			for (event in _song.events) 			{ 				var strumTime:Float = event[0]; 				if(endThing > event[0] && event[0] >= startThing) 				{ 					strumTime += Conductor.stepCrochet * (_song.notes[daSec].lengthInSteps * value); 					var copiedEventArray:Array<Dynamic> = []; 					for (i in 0...event[1].length) 					{ 						var eventToPush:Array<Dynamic> = event[1][i]; 						copiedEventArray.push([eventToPush[0], eventToPush[1], eventToPush[2]]); 					} 					_song.events.push([strumTime, copiedEventArray]); 				} 			} 			updateGrid(); 		}); 		copyLastButton.setGraphicSize(80, 30); 		copyLastButton.updateHitbox();  		tab_group_section.add(stepperLength); 		tab_group_section.add(stepperSectionBPM); 		tab_group_section.add(check_mustHitSection); 		tab_group_section.add(check_gfSection); 		tab_group_section.add(check_altAnim); 		tab_group_section.add(check_changeBPM); 		tab_group_section.add(copyButton); 		tab_group_section.add(pasteButton); 		tab_group_section.add(clearSectionButton); 		tab_group_section.add(swapSection); 		tab_group_section.add(stepperCopy); 		tab_group_section.add(copyLastButton);  		UI_box.addGroup(tab_group_section); 	}  	var stepperSusLength:FlxUINumericStepper; 	var strumTimeInputText:FlxUIInputText; //I wanted to use a stepper but we can't scale these as far as i know :( 	var noteTypeDropDown:FlxUIDropDownMenuCustom; 	var currentType:Int = 0;  	function addNoteUI():Void 	{ 		var tab_group_note = new FlxUI(null, UI_box); 		tab_group_note.name = 'Note';  		stepperSusLength = new FlxUINumericStepper(10, 25, Conductor.stepCrochet / 2, 0, 0, Conductor.stepCrochet * 32); 		stepperSusLength.value = 0; 		stepperSusLength.name = 'note_susLength';  		strumTimeInputText = new FlxUIInputText(10, 65, 180, "0"); 		strumTimeInputText.focusGained = () -> FlxG.stage.window.textInputEnabled = true;		 		tab_group_note.add(strumTimeInputText); 		blockPressWhileTypingOn.push(strumTimeInputText);  		var key:Int = 0; 		var displayNameList:Array<String> = []; 		while (key < noteTypeList.length) { 			displayNameList.push(noteTypeList[key]); 			noteTypeMap.set(noteTypeList[key], key); 			noteTypeIntMap.set(key, noteTypeList[key]); 			key++; 		}  		#if LUA_ALLOWED 		var directories:Array<String> = [Paths.mods('custom_notetypes/'), Paths.mods(Paths.currentModDirectory + '/custom_notetypes/')]; 		for (i in 0...directories.length) { 			var directory:String =  directories[i]; 			if(FileSystem.exists(directory)) { 				for (file in FileSystem.readDirectory(directory)) { 					var path = haxe.io.Path.join([directory, file]); 					if (!FileSystem.isDirectory(path) && file.endsWith('.lua')) { 						var fileToCheck:String = file.substr(0, file.length - 4); 						if(!noteTypeMap.exists(fileToCheck)) { 							displayNameList.push(fileToCheck); 							noteTypeMap.set(fileToCheck, key); 							noteTypeIntMap.set(key, fileToCheck); 							key++; 						} 					} 				} 			} 		} 		#end  		for (i in 1...displayNameList.length) { 			displayNameList[i] = i + '. ' + displayNameList[i]; 		}  		noteTypeDropDown = new FlxUIDropDownMenuCustom(10, 105, FlxUIDropDownMenuCustom.makeStrIdLabelArray(displayNameList, true), function(character:String) 		{ 			currentType = Std.parseInt(character); 			if(curSelectedNote != null && curSelectedNote[1] > -1) { 				curSelectedNote[3] = noteTypeIntMap.get(currentType); 				updateGrid(); 			} 		}); 		blockPressWhileScrolling.push(noteTypeDropDown);  		tab_group_note.add(new FlxText(10, 10, 0, 'Sustain length:')); 		tab_group_note.add(new FlxText(10, 50, 0, 'Strum time (in miliseconds):')); 		tab_group_note.add(new FlxText(10, 90, 0, 'Note type:')); 		tab_group_note.add(stepperSusLength); 		tab_group_note.add(strumTimeInputText); 		tab_group_note.add(noteTypeDropDown);  		UI_box.addGroup(tab_group_note); 	}  	var eventDropDown:FlxUIDropDownMenuCustom; 	var descText:FlxText; 	var selectedEventText:FlxText; 	function addEventsUI():Void 	{ 		var tab_group_event = new FlxUI(null, UI_box); 		tab_group_event.name = 'Events';  		#if LUA_ALLOWED 		var eventPushedMap:Map<String, Bool> = new Map<String, Bool>(); 		var directories:Array<String> = [Paths.mods('custom_events/'), Paths.mods(Paths.currentModDirectory + '/custom_events/')]; 		for (i in 0...directories.length) { 			var directory:String =  directories[i]; 			if(FileSystem.exists(directory)) { 				for (file in FileSystem.readDirectory(directory)) { 					var path = haxe.io.Path.join([directory, file]); 					if (!FileSystem.isDirectory(path) && file != 'readme.txt' && file.endsWith('.txt')) { 						var fileToCheck:String = file.substr(0, file.length - 4); 						if(!eventPushedMap.exists(fileToCheck)) { 							eventPushedMap.set(fileToCheck, true); 							eventStuff.push([fileToCheck, File.getContent(path)]); 						} 					} 				} 			} 		} 		eventPushedMap.clear(); 		eventPushedMap = null; 		#end  		descText = new FlxText(20, 200, 0, eventStuff[0][0]);  		var leEvents:Array<String> = []; 		for (i in 0...eventStuff.length) { 			leEvents.push(eventStuff[i][0]); 		}  		var text:FlxText = new FlxText(20, 30, 0, "Event:"); 		tab_group_event.add(text); 		eventDropDown = new FlxUIDropDownMenuCustom(20, 50, FlxUIDropDownMenuCustom.makeStrIdLabelArray(leEvents, true), function(pressed:String) { 			var selectedEvent:Int = Std.parseInt(pressed); 			descText.text = eventStuff[selectedEvent][1]; 				if (curSelectedNote != null &&  eventStuff != null) { 				if (curSelectedNote != null && curSelectedNote[2] == null){ 				curSelectedNote[1][curEventSelected][0] = eventStuff[selectedEvent][0];  				} 				updateGrid(); 			}				 		}); 		blockPressWhileScrolling.push(eventDropDown);  		var text:FlxText = new FlxText(20, 90, 0, "Value 1:"); 		tab_group_event.add(text); 		value1InputText = new FlxUIInputText(20, 110, 100, ""); 		value1InputText.focusGained = () -> FlxG.stage.window.textInputEnabled = true;		 		blockPressWhileTypingOn.push(value1InputText);  		var text:FlxText = new FlxText(20, 130, 0, "Value 2:"); 		tab_group_event.add(text); 		value2InputText = new FlxUIInputText(20, 150, 100, ""); 		value2InputText.focusGained = () -> FlxG.stage.window.textInputEnabled = true;		 		blockPressWhileTypingOn.push(value2InputText);  		// New event buttons 		var removeButton:FlxButton = new FlxButton(eventDropDown.x + eventDropDown.width + 10, eventDropDown.y, '-', function() 		{ 			if(curSelectedNote != null && curSelectedNote[2] == null) //Is event note 			{ 				if(curSelectedNote[1].length < 2) 				{ 					_song.events.remove(curSelectedNote); 					curSelectedNote = null; 				} 				else 				{ 					curSelectedNote[1].remove(curSelectedNote[1][curEventSelected]); 				}  				var eventsGroup:Array<Dynamic>; 				--curEventSelected; 				if(curEventSelected < 0) curEventSelected = 0; 				else if(curSelectedNote != null && curEventSelected >= (eventsGroup = curSelectedNote[1]).length) curEventSelected = eventsGroup.length - 1; 				 				changeEventSelected(); 				updateGrid(); 			} 		}); 		removeButton.setGraphicSize(Std.int(removeButton.height), Std.int(removeButton.height)); 		removeButton.updateHitbox(); 		removeButton.color = FlxColor.RED; 		removeButton.label.color = FlxColor.WHITE; 		removeButton.label.size = 12; 		setAllLabelsOffset(removeButton, -30, 0); 		tab_group_event.add(removeButton); 			 		var addButton:FlxButton = new FlxButton(removeButton.x + removeButton.width + 10, removeButton.y, '+', function() 		{ 			if(curSelectedNote != null && curSelectedNote[2] == null) //Is event note 			{ 				var eventsGroup:Array<Dynamic> = curSelectedNote[1]; 				eventsGroup.push(['', '', '']);  				changeEventSelected(1); 				updateGrid(); 			} 		}); 		addButton.setGraphicSize(Std.int(removeButton.width), Std.int(removeButton.height)); 		addButton.updateHitbox(); 		addButton.color = FlxColor.GREEN; 		addButton.label.color = FlxColor.WHITE; 		addButton.label.size = 12; 		setAllLabelsOffset(addButton, -30, 0); 		tab_group_event.add(addButton); 			 		var moveLeftButton:FlxButton = new FlxButton(addButton.x + addButton.width + 20, addButton.y, '<', function() 		{ 			changeEventSelected(-1); 		}); 		moveLeftButton.setGraphicSize(Std.int(addButton.width), Std.int(addButton.height)); 		moveLeftButton.updateHitbox(); 		moveLeftButton.label.size = 12; 		setAllLabelsOffset(moveLeftButton, -30, 0); 		tab_group_event.add(moveLeftButton); 			 		var moveRightButton:FlxButton = new FlxButton(moveLeftButton.x + moveLeftButton.width + 10, moveLeftButton.y, '>', function() 		{ 			changeEventSelected(1); 		}); 		moveRightButton.setGraphicSize(Std.int(moveLeftButton.width), Std.int(moveLeftButton.height)); 		moveRightButton.updateHitbox(); 		moveRightButton.label.size = 12; 		setAllLabelsOffset(moveRightButton, -30, 0); 		tab_group_event.add(moveRightButton);  		selectedEventText = new FlxText(addButton.x - 100, addButton.y + addButton.height + 6, (moveRightButton.x - addButton.x) + 186, 'Selected Event: None'); 		selectedEventText.alignment = CENTER; 		tab_group_event.add(selectedEventText);  		tab_group_event.add(descText); 		tab_group_event.add(value1InputText); 		tab_group_event.add(value2InputText); 		tab_group_event.add(eventDropDown);  		UI_box.addGroup(tab_group_event); 	}  	function changeEventSelected(change:Int = 0) 	{ 		if(curSelectedNote != null && curSelectedNote[2] == null) //Is event note 		{ 			curEventSelected += change; 			if(curEventSelected < 0) curEventSelected = Std.int(curSelectedNote[1].length) - 1; 			else if(curEventSelected >= curSelectedNote[1].length) curEventSelected = 0; 			selectedEventText.text = 'Selected Event: ' + (curEventSelected + 1) + ' / ' + curSelectedNote[1].length; 		} 		else 		{ 			curEventSelected = 0; 			selectedEventText.text = 'Selected Event: None'; 		} 		updateNoteUI(); 	} 	 	function setAllLabelsOffset(button:FlxButton, x:Float, y:Float) 	{ 		for (point in button.labelOffsets) 		{ 			point.set(x, y); 		} 	}  	var metronome:FlxUICheckBox; 	var metronomeStepper:FlxUINumericStepper; 	var metronomeOffsetStepper:FlxUINumericStepper; 	var disableAutoScrolling:FlxUICheckBox; 	#if desktop 	var waveformEnabled:FlxUICheckBox; 	var waveformUseInstrumental:FlxUICheckBox; 	#end 	var instVolume:FlxUINumericStepper; 	var voicesVolume:FlxUINumericStepper; 	function addChartingUI() { 		var tab_group_chart = new FlxUI(null, UI_box); 		tab_group_chart.name = 'Charting'; 		 		#if desktop 		waveformEnabled = new FlxUICheckBox(10, 90, null, null, "Visible Waveform", 100); 		if (FlxG.save.data.chart_waveform == null) FlxG.save.data.chart_waveform = false; 		waveformEnabled.checked = FlxG.save.data.chart_waveform; 		waveformEnabled.callback = function() 		{ 			FlxG.save.data.chart_waveform = waveformEnabled.checked; 			updateWaveform(); 		};  		waveformUseInstrumental = new FlxUICheckBox(waveformEnabled.x + 120, waveformEnabled.y, null, null, "Waveform for Instrumental", 100); 		waveformUseInstrumental.checked = false; 		waveformUseInstrumental.callback = function() 		{ 			updateWaveform(); 		}; 		#end  		check_mute_inst = new FlxUICheckBox(10, 310, null, null, "Mute Instrumental (in editor)", 100); 		check_mute_inst.checked = false; 		check_mute_inst.callback = function() 		{ 			var vol:Float = 1;  			if (check_mute_inst.checked) 				vol = 0;  			FlxG.sound.music.volume = vol; 		}; 		check_vortex = new FlxUICheckBox(10, 120, null, null, "Vortex Editor (BETA)", 100); 		if (FlxG.save.data.chart_vortex == null) FlxG.save.data.chart_vortex = false; 		check_vortex.checked = FlxG.save.data.chart_vortex;  		check_vortex.callback = function() 		{ 			FlxG.save.data.chart_vortex = check_vortex.checked; 			vortex = FlxG.save.data.chart_vortex; 			reloadGridLayer(); 		};  		var check_mute_vocals = new FlxUICheckBox(check_mute_inst.x + 120, check_mute_inst.y, null, null, "Mute Vocals (in editor)", 100); 		check_mute_vocals.checked = false; 		check_mute_vocals.callback = function() 		{ 			if(vocals != null) { 				var vol:Float = 1;  				if (check_mute_vocals.checked) 					vol = 0;  				vocals.volume = vol; 			} 		};  		playSoundBf = new FlxUICheckBox(check_mute_inst.x, check_mute_vocals.y + 30, null, null, 'Play Sound (Boyfriend notes)', 100, 			function() { 				FlxG.save.data.chart_playSoundBf = playSoundBf.checked; 			} 		); 		if (FlxG.save.data.chart_playSoundBf == null) FlxG.save.data.chart_playSoundBf = false; 		playSoundBf.checked = FlxG.save.data.chart_playSoundBf;  		playSoundDad = new FlxUICheckBox(check_mute_inst.x + 120, playSoundBf.y, null, null, 'Play Sound (Opponent notes)', 100, 			function() { 				FlxG.save.data.chart_playSoundDad = playSoundDad.checked; 			} 		); 		if (FlxG.save.data.chart_playSoundDad == null) FlxG.save.data.chart_playSoundDad = false; 		playSoundDad.checked = FlxG.save.data.chart_playSoundDad;  		metronome = new FlxUICheckBox(10, 15, null, null, "Metronome Enabled", 100, 			function() { 				FlxG.save.data.chart_metronome = metronome.checked; 			} 		); 		if (FlxG.save.data.chart_metronome == null) FlxG.save.data.chart_metronome = false; 		metronome.checked = FlxG.save.data.chart_metronome;  		metronomeStepper = new FlxUINumericStepper(15, 55, 5, _song.bpm, 1, 1500, 1); 		metronomeOffsetStepper = new FlxUINumericStepper(metronomeStepper.x + 100, metronomeStepper.y, 25, 0, 0, 1000, 1); 		 		disableAutoScrolling = new FlxUICheckBox(metronome.x + 120, metronome.y, null, null, "Disable Autoscroll (Not Recommended)", 120, 			function() { 				FlxG.save.data.chart_noAutoScroll = disableAutoScrolling.checked; 			} 		); 		if (FlxG.save.data.chart_noAutoScroll == null) FlxG.save.data.chart_noAutoScroll = false; 		disableAutoScrolling.checked = FlxG.save.data.chart_noAutoScroll;  		instVolume = new FlxUINumericStepper(metronomeStepper.x, 270, 0.1, 1, 0, 1, 1); 		instVolume.value = FlxG.sound.music.volume; 		instVolume.name = 'inst_volume'; 		voicesVolume = new FlxUINumericStepper(instVolume.x + 100, instVolume.y, 0.1, 1, 0, 1, 1); 		voicesVolume.value = vocals.volume; 		voicesVolume.name = 'voices_volume';  		tab_group_chart.add(new FlxText(metronomeStepper.x, metronomeStepper.y - 15, 0, 'BPM:')); 		tab_group_chart.add(new FlxText(metronomeOffsetStepper.x, metronomeOffsetStepper.y - 15, 0, 'Offset (ms):')); 		tab_group_chart.add(new FlxText(instVolume.x, instVolume.y - 15, 0, 'Inst Volume')); 		tab_group_chart.add(new FlxText(voicesVolume.x, voicesVolume.y - 15, 0, 'Voices Volume')); 		tab_group_chart.add(metronome); 		tab_group_chart.add(disableAutoScrolling); 		tab_group_chart.add(metronomeStepper); 		tab_group_chart.add(metronomeOffsetStepper); 		#if desktop 		tab_group_chart.add(waveformEnabled); 		tab_group_chart.add(waveformUseInstrumental); 		#end 		tab_group_chart.add(instVolume); 		tab_group_chart.add(voicesVolume); 		tab_group_chart.add(check_mute_inst); 		tab_group_chart.add(check_mute_vocals); 		tab_group_chart.add(check_vortex); 		tab_group_chart.add(playSoundBf); 		tab_group_chart.add(playSoundDad); 		UI_box.addGroup(tab_group_chart); 	}  	function loadSong():Void 	{ 		if (FlxG.sound.music != null) 		{ 			FlxG.sound.music.stop(); 			// vocals.stop(); 		}  		var file:Dynamic = Paths.voices(currentSongName); 		vocals = new FlxSound(); 		if (Std.isOfType(file, Sound) || OpenFlAssets.exists(file)) { 			vocals.loadEmbedded(file); 			FlxG.sound.list.add(vocals); 		} 		generateSong(); 		FlxG.sound.music.pause(); 		Conductor.songPosition = sectionStartTime(); 		FlxG.sound.music.time = Conductor.songPosition; 	}  	function generateSong() { 		FlxG.sound.playMusic(Paths.inst(currentSongName), 0.6/*, false*/); 		if (instVolume != null) FlxG.sound.music.volume = instVolume.value; 		if (check_mute_inst != null && check_mute_inst.checked) FlxG.sound.music.volume = 0;  		FlxG.sound.music.onComplete = function() 		{ 			FlxG.sound.music.pause(); 			Conductor.songPosition = 0; 			if(vocals != null) { 				vocals.pause(); 				vocals.time = 0; 			} 			changeSection(); 			curSection = 0; 			updateGrid(); 			updateSectionUI(); 			vocals.play(); 		}; 	}  	function generateUI():Void 	{ 		while (bullshitUI.members.length > 0) 		{ 			bullshitUI.remove(bullshitUI.members[0], true); 		}  		// general shit 		var title:FlxText = new FlxText(UI_box.x + 20, UI_box.y + 20, 0); 		bullshitUI.add(title); 		/*  			var loopCheck = new FlxUICheckBox(UI_box.x + 10, UI_box.y + 50, null, null, "Loops", 100, ['loop check']); 			loopCheck.checked = curNoteSelected.doesLoop; 			tooltips.add(loopCheck, {title: 'Section looping', body: "Whether or not it's a simon says style section", style: tooltipType}); 			bullshitUI.add(loopCheck);  		 */ 	}  	override function getEvent(id:String, sender:Dynamic, data:Dynamic, ?params:Array<Dynamic>) 	{ 		if (id == FlxUICheckBox.CLICK_EVENT) 		{ 			var check:FlxUICheckBox = cast sender; 			var label = check.getLabel().text; 			switch (label) 			{ 				case 'Must hit section': 					_song.notes[curSection].mustHitSection = check.checked;  					updateGrid(); 					updateHeads();  				case 'GF section': 					_song.notes[curSection].gfSection = check.checked;  					updateGrid(); 					updateHeads();  				case 'Change BPM': 					_song.notes[curSection].changeBPM = check.checked; 					FlxG.log.add('changed bpm shit'); 				case "Alt Animation": 					_song.notes[curSection].altAnim = check.checked; 			} 		} 		else if (id == FlxUINumericStepper.CHANGE_EVENT && (sender is FlxUINumericStepper)) 		{ 			var nums:FlxUINumericStepper = cast sender; 			var wname = nums.name; 			FlxG.log.add(wname); 			if (wname == 'section_length') 			{ 				_song.notes[curSection].lengthInSteps = Std.int(nums.value); 				updateGrid(); 			} 			else if (wname == 'song_speed') 			{ 				_song.speed = nums.value; 			} 			else if (wname == 'song_bpm') 			{ 				tempBpm = nums.value; 				Conductor.mapBPMChanges(_song); 				Conductor.changeBPM(nums.value); 			} 			else if (wname == 'note_susLength') 			{ 				if(curSelectedNote != null && curSelectedNote[1] > -1) { 					curSelectedNote[2] = nums.value; 					updateGrid(); 				} else { 					sender.value = 0; 				} 			} 			else if (wname == 'section_bpm') 			{ 				_song.notes[curSection].bpm = nums.value; 				updateGrid(); 			} 			else if (wname == 'inst_volume') 			{ 				FlxG.sound.music.volume = nums.value; 			} 			else if (wname == 'voices_volume') 			{ 				vocals.volume = nums.value; 			} 		} 		else if(id == FlxUIInputText.CHANGE_EVENT && (sender is FlxUIInputText)) { 			if(sender == noteSplashesInputText) { 				_song.splashSkin = noteSplashesInputText.text; 			} 			else if(curSelectedNote != null) 			{ 				if(sender == value1InputText) { 					curSelectedNote[1][curEventSelected][1] = value1InputText.text; 					updateGrid(); 				} 				else if(sender == value2InputText) { 					curSelectedNote[1][curEventSelected][2] = value2InputText.text; 					updateGrid(); 				} 				else if(sender == strumTimeInputText) { 					var value:Float = Std.parseFloat(strumTimeInputText.text); 					if(Math.isNaN(value)) value = 0; 					curSelectedNote[0] = value; 					updateGrid(); 				} 			} 		}  		// FlxG.log.add(id + " WEED " + sender + " WEED " + data + " WEED " + params); 	}  	var updatedSection:Bool = false;  	/* this function got owned LOL 		function lengthBpmBullshit():Float 		{ 			if (_song.notes[curSection].changeBPM) 				return _song.notes[curSection].lengthInSteps * (_song.notes[curSection].bpm / _song.bpm); 			else 				return _song.notes[curSection].lengthInSteps; 	}*/ 	function sectionStartTime(add:Int = 0):Float 	{ 		var daBPM:Float = _song.bpm; 		var daPos:Float = 0; 		for (i in 0...curSection + add) 		{ 			if(_song.notes[i] != null) 			{ 				if (_song.notes[i].changeBPM) 				{ 					daBPM = _song.notes[i].bpm; 				} 				daPos += 4 * (1000 * 60 / daBPM); 			} 		} 		return daPos; 	}  	var lastConductorPos:Float; 	var colorSine:Float = 0; 	override function update(elapsed:Float) 	{ 		curStep = recalculateSteps();  		if(FlxG.sound.music.time < 0) { 			FlxG.sound.music.pause(); 			FlxG.sound.music.time = 0; 		} 		else if(FlxG.sound.music.time > FlxG.sound.music.length) { 			FlxG.sound.music.pause(); 			FlxG.sound.music.time = 0; 			changeSection(); 		} 		Conductor.songPosition = FlxG.sound.music.time; 		_song.song = UI_songTitle.text;  		strumLine.y = getYfromStrum((Conductor.songPosition - sectionStartTime()) / zoomList[curZoom] % (Conductor.stepCrochet * _song.notes[curSection].lengthInSteps)); 		for (i in 0...8){ 			strumLineNotes.members[i].y = strumLine.y; 		}  		camPos.y = strumLine.y; 		if(!disableAutoScrolling.checked) { 			if (strumLine.y >= (gridBG.height / 2)) 			{ 				//trace(curStep); 				//trace((_song.notes[curSection].lengthInSteps) * (curSection + 1)); 				//trace('DUMBSHIT');  				if (_song.notes[curSection + 1] == null) 				{ 					addSection(); 				}  				changeSection(curSection + 1, false); 			} else if(strumLine.y < -10) { 				changeSection(curSection - 1, false); 			} 		} 		FlxG.watch.addQuick('daBeat', curBeat); 		FlxG.watch.addQuick('daStep', curStep);  		 		if (FlxG.mouse.justPressed) 		{ 			if (FlxG.mouse.overlaps(curRenderedNotes)) 			{ 				curRenderedNotes.forEachAlive(function(note:Note) 				{ 					if (FlxG.mouse.overlaps(note)) 					{ 						if (FlxG.keys.pressed.CONTROL) 						{ 							selectNote(note); 						} 						else 						{ 							//trace('tryin to delete note...'); 							deleteNote(note); 						} 					} 				}); 			} 			else 			{ 				if (FlxG.mouse.x > gridBG.x 					&& FlxG.mouse.x < gridBG.x + gridBG.width 					&& FlxG.mouse.y > gridBG.y 					&& FlxG.mouse.y < gridBG.y + (GRID_SIZE * _song.notes[curSection].lengthInSteps) * zoomList[curZoom]) 				{ 					FlxG.log.add('added note'); 					addNote(); 				} 			} 		}  		if (FlxG.mouse.x > gridBG.x 			&& FlxG.mouse.x < gridBG.x + gridBG.width 			&& FlxG.mouse.y > gridBG.y 			&& FlxG.mouse.y < gridBG.y + (GRID_SIZE * _song.notes[curSection].lengthInSteps) * zoomList[curZoom]) 		{ 			dummyArrow.visible = true; 			dummyArrow.x = Math.floor(FlxG.mouse.x / GRID_SIZE) * GRID_SIZE; 			if (FlxG.keys.pressed.SHIFT) 				dummyArrow.y = FlxG.mouse.y; 			else 				dummyArrow.y = Math.floor(FlxG.mouse.y / GRID_SIZE) * GRID_SIZE; 		}else{ 			dummyArrow.visible = false; 		}  		var blockInput:Bool = false; 		for (inputText in blockPressWhileTypingOn) { 			if(inputText.hasFocus) { 				FlxG.sound.muteKeys = []; 				FlxG.sound.volumeDownKeys = []; 				FlxG.sound.volumeUpKeys = []; 				blockInput = true; 				break; 			} 		} 		if(!blockInput) { 			FlxG.sound.muteKeys = TitleState.muteKeys; 			FlxG.sound.volumeDownKeys = TitleState.volumeDownKeys; 			FlxG.sound.volumeUpKeys = TitleState.volumeUpKeys; 			for (dropDownMenu in blockPressWhileScrolling) { 				if(dropDownMenu.dropPanel.visible) { 					blockInput = true; 					break; 				} 			} 		}  		if (!blockInput) 		{ 			if (FlxG.keys.justPressed.ESCAPE #if mobileC|| _virtualpad.buttonB.justPressed #end) 			{ 				autosaveSong(); 				LoadingState.loadAndSwitchState(new editors.EditorPlayState(sectionStartTime())); 			} 			if (FlxG.keys.justPressed.ENTER #if mobileC|| _virtualpad.buttonA.justPressed #end) 			{ 				autosaveSong(); 				FlxG.mouse.visible = false; 				PlayState.SONG = _song; 				FlxG.sound.music.stop(); 				if(vocals != null) vocals.stop();  				//if(_song.stage == null) _song.stage = stageDropDown.selectedLabel; 				StageData.loadDirectory(_song); 				LoadingState.loadAndSwitchState(new PlayState()); 			}  			if(curSelectedNote != null && curSelectedNote[1] > -1) { 				if (FlxG.keys.justPressed.E) 				{ 					changeNoteSustain(Conductor.stepCrochet); 				} 				if (FlxG.keys.justPressed.Q) 				{ 					changeNoteSustain(-Conductor.stepCrochet); 				} 			}  			if(FlxG.keys.justPressed.Z && curZoom > 0) { 				--curZoom; 				updateZoom(); 			} 			if(FlxG.keys.justPressed.X && curZoom < zoomList.length-1) { 				curZoom++; 				updateZoom(); 			}  			if (FlxG.keys.justPressed.TAB) 			{ 				if (FlxG.keys.pressed.SHIFT) 				{ 					UI_box.selected_tab -= 1; 					if (UI_box.selected_tab < 0) 						UI_box.selected_tab = 2; 				} 				else 				{ 					UI_box.selected_tab += 1; 					if (UI_box.selected_tab >= 3) 						UI_box.selected_tab = 0; 				} 			}  			if (FlxG.keys.justPressed.SPACE) 			{ 				if (FlxG.sound.music.playing) 				{ 					FlxG.sound.music.pause(); 					if(vocals != null) vocals.pause(); 				} 				else 				{ 					if(vocals != null) { 						vocals.play(); 						vocals.pause(); 						vocals.time = FlxG.sound.music.time; 						vocals.play(); 					} 					FlxG.sound.music.play(); 				} 			}  			if (FlxG.keys.justPressed.R) 			{ 				if (FlxG.keys.pressed.SHIFT) 					resetSection(true); 				else 					resetSection(); 			}  			if (FlxG.mouse.wheel != 0) 			{ 				FlxG.sound.music.pause(); 				FlxG.sound.music.time -= (FlxG.mouse.wheel * Conductor.stepCrochet*0.8); 				if(vocals != null) { 					vocals.pause(); 					vocals.time = FlxG.sound.music.time; 				} 			}  			//ARROW VORTEX SHIT NO DEADASS 			 			 			 			if (FlxG.keys.pressed.W || FlxG.keys.pressed.S #if mobileC || _virtualpad.buttonUp.pressed || _virtualpad.buttonDown.pressed #end) 			{ 				FlxG.sound.music.pause();  				var holdingShift:Float = 1; 				if (FlxG.keys.pressed.CONTROL) holdingShift = 0.25; 				else if (FlxG.keys.pressed.SHIFT) holdingShift = 4;  				var daTime:Float = 700 * FlxG.elapsed * holdingShift;  				if (FlxG.keys.pressed.W #if mobileC || _virtualpad.buttonUp.pressed #end) 				{ 					FlxG.sound.music.time -= daTime; 				} 				else 					FlxG.sound.music.time += daTime;  				if(vocals != null) { 					vocals.pause(); 					vocals.time = FlxG.sound.music.time; 				} 			} 			 			var style = currentType; 			 			if (FlxG.keys.pressed.SHIFT){ 				style = 3; 			} 			 			var conductorTime = Conductor.songPosition; //+ sectionStartTime();Conductor.songPosition / Conductor.stepCrochet; 			 			//AWW YOU MADE IT SEXY <3333 THX SHADMAR 			if(vortex){ 			var controlArray:Array<Bool> = [FlxG.keys.justPressed.ONE, FlxG.keys.justPressed.TWO, FlxG.keys.justPressed.THREE, FlxG.keys.justPressed.FOUR, 										   FlxG.keys.justPressed.FIVE, FlxG.keys.justPressed.SIX, FlxG.keys.justPressed.SEVEN, FlxG.keys.justPressed.EIGHT];  			if(controlArray.contains(true)) 			{ 				for (i in 0...controlArray.length) 				{ 					if(controlArray[i]) 						doANoteThing(conductorTime, i, style); 				} 			} 			 			 				var datimess = []; 				 				var daTime:Float = Math.round(Conductor.stepCrochet*quants[curQuant]); 				var cuquant = Std.int(32/quants[curQuant]); 				for (i in 0...cuquant){ 					datimess.push(sectionStartTime() + daTime * i); 				} 			if (FlxG.keys.justPressed.LEFT) 			{ 				--curQuant; 				if (curQuant < 0) curQuant = 0; 				 				daquantspot *=  Std.int(32/quants[curQuant]); 			} 			if (FlxG.keys.justPressed.RIGHT) 			{ 				curQuant ++; 				if (curQuant > quants.length-1) curQuant = quants.length-1; 				daquantspot *=  Std.int(32/quants[curQuant]); 			} 			quant.animation.play('q', true, false, curQuant); 			if (FlxG.keys.justPressed.UP || FlxG.keys.justPressed.DOWN  ) 			{ 				FlxG.sound.music.pause();  				 				updateCurStep(); 				//FlxG.sound.music.time = (Math.round(curStep/quants[curQuant])*quants[curQuant]) * Conductor.stepCrochet; 				 					//(Math.floor((curStep+quants[curQuant]*1.5/(quants[curQuant]/2))/quants[curQuant])*quants[curQuant]) * Conductor.stepCrochet;//snap into quantization 				if (FlxG.keys.pressed.UP) 				{ 					 					//var tosnapto = 0.00; 					var foundaspot = false; 					var i = datimess.length-1;//backwards for loop  					while (i > -1){ 						if (FlxG.sound.music.time >= datimess[i] && !foundaspot){ 							foundaspot = true; 							FlxG.sound.music.time = datimess[i]; 						} 						--i; 					} 					//FlxG.sound.music.time = tosnapto; 					FlxG.sound.music.time -= daTime; 				} 				else{ 					 					var foundaspot = false; 					for (i in datimess){ 						if (FlxG.sound.music.time <= i && !foundaspot){ 							foundaspot = true; 							FlxG.sound.music.time = i; 						} 					} 					 					 					FlxG.sound.music.time += daTime; 				} 				if(vocals != null) { 					vocals.pause(); 					vocals.time = FlxG.sound.music.time; 				} 				 				var dastrum = 0; 				 				if (curSelectedNote != null){ 					dastrum = curSelectedNote[0]; 				} 				 				var secStart:Float = sectionStartTime(); 				var datime = (FlxG.sound.music.time - secStart) - (dastrum - secStart); //idk math find out why it doesn't work on any other section other than 0 				if (curSelectedNote != null) 				{ 					var controlArray:Array<Bool> = [FlxG.keys.pressed.ONE, FlxG.keys.pressed.TWO, FlxG.keys.pressed.THREE, FlxG.keys.pressed.FOUR, 												   FlxG.keys.pressed.FIVE, FlxG.keys.pressed.SIX, FlxG.keys.pressed.SEVEN, FlxG.keys.pressed.EIGHT];  					if(controlArray.contains(true)) 					{ 						for (i in 0...controlArray.length) 						{ 							if(controlArray[i]) 								if(curSelectedNote[1] == i) curSelectedNote[2] += datime - curSelectedNote[2] - Conductor.stepCrochet; 						} 						updateGrid(); 					} 				} 			} 			} 			var shiftThing:Int = 1; 			if (FlxG.keys.pressed.SHIFT) 				shiftThing = 4;  			if (FlxG.keys.justPressed.RIGHT && !vortex|| FlxG.keys.justPressed.D #if mobileC || _virtualpad.buttonRight.justPressed #end) 				changeSection(curSection + shiftThing); 			if (FlxG.keys.justPressed.LEFT && !vortex|| FlxG.keys.justPressed.A #if mobileC || _virtualpad.buttonLeft.justPressed #end) { 				if(curSection <= 0) { 					changeSection(_song.notes.length-1); 				} else { 					changeSection(curSection - shiftThing); 				} 			} 		} else if (FlxG.keys.justPressed.ENTER) { 			for (i in 0...blockPressWhileTypingOn.length) { 				if(blockPressWhileTypingOn[i].hasFocus) { 					blockPressWhileTypingOn[i].hasFocus = false; 				} 			} 		}  		_song.bpm = tempBpm;  		strumLineNotes.visible = quant.visible = vortex; 			 		if(FlxG.sound.music.time < 0) { 			FlxG.sound.music.pause(); 			FlxG.sound.music.time = 0; 		} 		else if(FlxG.sound.music.time > FlxG.sound.music.length) { 			FlxG.sound.music.pause(); 			FlxG.sound.music.time = 0; 			changeSection(); 		} 		Conductor.songPosition = FlxG.sound.music.time; 		strumLine.y = getYfromStrum((Conductor.songPosition - sectionStartTime()) / zoomList[curZoom] % (Conductor.stepCrochet * _song.notes[curSection].lengthInSteps)); 		camPos.y = strumLine.y; 		for (i in 0...8){ 			strumLineNotes.members[i].y = strumLine.y; 			strumLineNotes.members[i].alpha = FlxG.sound.music.playing ? 1 : 0.35; 		}  		bpmTxt.text =  		Std.string(FlxMath.roundDecimal(Conductor.songPosition / 1000, 2)) + " / " + Std.string(FlxMath.roundDecimal(FlxG.sound.music.length / 1000, 2)) + 		"\nSection: " + curSection + 		"\n\nBeat: " + curBeat + 		"\n\nStep: " + curStep;  		var playedSound:Array<Bool> = [false, false, false, false]; //Prevents ouchy GF sex sounds 		curRenderedNotes.forEachAlive(function(note:Note) { 			note.alpha = 1; 			if(curSelectedNote != null) { 				var noteDataToCheck:Int = note.noteData; 				if(noteDataToCheck > -1 && note.mustPress != _song.notes[curSection].mustHitSection) noteDataToCheck += 4;  				if (curSelectedNote[0] == note.strumTime && ((curSelectedNote[2] == null && noteDataToCheck < 0) || (curSelectedNote[2] != null && curSelectedNote[1] == noteDataToCheck))) 				{ 					colorSine += elapsed; 					var colorVal:Float = 0.7 + Math.sin(Math.PI * colorSine) * 0.3; 					note.color = FlxColor.fromRGBFloat(colorVal, colorVal, colorVal, 0.999); //Alpha can't be 100% or the color won't be updated for some reason, guess i will die 				} 			}  			if(note.strumTime <= Conductor.songPosition) { 				note.alpha = 0.4; 				if(note.strumTime > lastConductorPos && FlxG.sound.music.playing && note.noteData > -1) { 					var data:Int = note.noteData % 4; 				    var noteDataToCheck:Int = note.noteData; 					if(noteDataToCheck > -1 && note.mustPress != _song.notes[curSection].mustHitSection) noteDataToCheck += 4; 						strumLineNotes.members[noteDataToCheck].playAnim('confirm', true); 						strumLineNotes.members[noteDataToCheck].resetAnim = (note.sustainLength / 1000) + 0.15;					 					if(!playedSound[data]) { 						if((playSoundBf.checked && note.mustPress) || (playSoundDad.checked && !note.mustPress)){ 							var soundToPlay = 'ChartingTick'; 							if(_song.player1 == 'gf') { //Easter egg 								soundToPlay = 'GF_' + Std.string(data + 1); 							} 							 							FlxG.sound.play(Paths.sound(soundToPlay)).pan = note.noteData < 4? -0.3 : 0.3; //would be coolio 							playedSound[data] = true; 						} 					 						data = note.noteData; 						if(note.mustPress != _song.notes[curSection].mustHitSection) 						{ 							data += 4; 						} 					} 				} 			} 		});  		if(metronome.checked && lastConductorPos != Conductor.songPosition) { 			var metroInterval:Float = 60 / metronomeStepper.value; 			var metroStep:Int = Math.floor(((Conductor.songPosition + metronomeOffsetStepper.value) / metroInterval) / 1000); 			var lastMetroStep:Int = Math.floor(((lastConductorPos + metronomeOffsetStepper.value) / metroInterval) / 1000); 			if(metroStep != lastMetroStep) { 				FlxG.sound.play(Paths.sound('Metronome_Tick')); 				//trace('Ticked'); 			} 		} 		lastConductorPos = Conductor.songPosition; 		super.update(elapsed); 	}  	function updateZoom() { 		zoomTxt.text = 'Zoom: ' + zoomList[curZoom] + 'x'; 		reloadGridLayer(); 	}  	function loadAudioBuffer() { 		if(audioBuffers[0] != null) { 			audioBuffers[0].dispose(); 		} 		audioBuffers[0] = null; 		#if MODS_ALLOWED 		if(FileSystem.exists(Paths.modFolders('songs/' + currentSongName + '/Inst.ogg'))) { 			audioBuffers[0] = AudioBuffer.fromFile(Paths.modFolders('songs/' + currentSongName + '/Inst.ogg')); 			//trace('Custom vocals found'); 		} 		else { #end 			var leVocals:Dynamic = Paths.inst(currentSongName); 			if (!Std.isOfType(leVocals, Sound) && OpenFlAssets.exists(leVocals)) { //Vanilla inst 				audioBuffers[0] = AudioBuffer.fromFile('./' + leVocals.substr(6)); 				//trace('Inst found'); 			} 		#if MODS_ALLOWED 		} 		#end  		if(audioBuffers[1] != null) { 			audioBuffers[1].dispose(); 		} 		audioBuffers[1] = null; 		#if MODS_ALLOWED 		if(FileSystem.exists(Paths.modFolders('songs/' + currentSongName + '/Voices.ogg'))) { 			audioBuffers[1] = AudioBuffer.fromFile(Paths.modFolders('songs/' + currentSongName + '/Voices.ogg')); 			//trace('Custom vocals found'); 		} else { #end 			var leVocals:Dynamic = Paths.voices(currentSongName); 			if (!Std.isOfType(leVocals, Sound) && OpenFlAssets.exists(leVocals)) { //Vanilla voices 				audioBuffers[1] = AudioBuffer.fromFile('./' + leVocals.substr(6)); 				//trace('Voices found, LETS FUCKING GOOOO'); 			} 		#if MODS_ALLOWED 		} 		#end 	} 	function reloadGridLayer() { 		gridLayer.clear(); 		gridBG = FlxGridOverlay.create(GRID_SIZE, GRID_SIZE, GRID_SIZE * 9, Std.int(GRID_SIZE * 32 * zoomList[curZoom])); 		gridLayer.add(gridBG);  		#if desktop 		if(waveformEnabled != null) { 			updateWaveform(); 		} 		#end  		var gridBlack:FlxSprite = new FlxSprite(0, gridBG.height / 2).makeGraphic(Std.int(GRID_SIZE * 9), Std.int(gridBG.height / 2), FlxColor.BLACK); 		gridBlack.alpha = 0.4; 		gridLayer.add(gridBlack);  		var gridBlackLine:FlxSprite = new FlxSprite(gridBG.x + gridBG.width - (GRID_SIZE * 4)).makeGraphic(2, Std.int(gridBG.height), FlxColor.BLACK); 		gridLayer.add(gridBlackLine);  		for (i in 1...4){ 		var beatsep1:FlxSprite = new FlxSprite(gridBG.x,(GRID_SIZE * (4*curZoom))*i).makeGraphic(Std.int(gridBG.width), 1, 0x44FF0000); 		if(vortex)gridLayer.add(beatsep1); 		}  		gridBlackLine = new FlxSprite(gridBG.x + GRID_SIZE).makeGraphic(2, Std.int(gridBG.height), FlxColor.BLACK); 		gridLayer.add(gridBlackLine); 		updateGrid(); 	}  	var waveformPrinted:Bool = true; 	var audioBuffers:Array<AudioBuffer> = [null, null]; 	function updateWaveform() { 		#if desktop 		if(waveformPrinted) { 			waveformSprite.makeGraphic(Std.int(GRID_SIZE * 8), Std.int(gridBG.height), 0x00FFFFFF); 			waveformSprite.pixels.fillRect(new Rectangle(0, 0, gridBG.width, gridBG.height), 0x00FFFFFF); 		} 		waveformPrinted = false;  		var checkForVoices:Int = 1; 		if(waveformUseInstrumental.checked) checkForVoices = 0;  		if(!waveformEnabled.checked || audioBuffers[checkForVoices] == null) { 			//trace('Epic fail on the waveform lol'); 			return; 		}  		var sampleMult:Float = audioBuffers[checkForVoices].sampleRate / 44100; 		var index:Int = Std.int(sectionStartTime() * 44.0875 * sampleMult); 		var drawIndex:Int = 0;  		var steps:Int = _song.notes[curSection].lengthInSteps; 		if(Math.isNaN(steps) || steps < 1) steps = 16; 		var samplesPerRow:Int = Std.int(((Conductor.stepCrochet * steps * 1.1 * sampleMult) / 16) / zoomList[curZoom]); 		if(samplesPerRow < 1) samplesPerRow = 1; 		var waveBytes:Bytes = audioBuffers[checkForVoices].data.toBytes(); 		 		var min:Float = 0; 		var max:Float = 0; 		while (index < (waveBytes.length - 1)) 		{ 			var byte:Int = waveBytes.getUInt16(index * 4);  			if (byte > 65535 / 2) 				byte -= 65535;  			var sample:Float = (byte / 65535);  			if (sample > 0) 			{ 				if (sample > max) 					max = sample; 			} 			else if (sample < 0) 			{ 				if (sample < min) 					min = sample; 			}  			if ((index % samplesPerRow) == 0) 			{ 				// trace("min: " + min + ", max: " + max);  				/*if (drawIndex > gridBG.height) 				{ 					drawIndex = 0; 				}*/  				var pixelsMin:Float = Math.abs(min * (GRID_SIZE * 8)); 				var pixelsMax:Float = max * (GRID_SIZE * 8); 				waveformSprite.pixels.fillRect(new Rectangle(Std.int((GRID_SIZE * 4) - pixelsMin), drawIndex, pixelsMin + pixelsMax, 1), FlxColor.BLUE); 				drawIndex++;  				min = 0; 				max = 0;  				if(drawIndex > gridBG.height) break; 			}  			index++; 		} 		waveformPrinted = true; 		#end 	}  	function changeNoteSustain(value:Float):Void 	{ 		if (curSelectedNote != null) 		{ 			if (curSelectedNote[2] != null) 			{ 				curSelectedNote[2] += value; 				curSelectedNote[2] = Math.max(curSelectedNote[2], 0); 			} 		}  		updateNoteUI(); 		updateGrid(); 	}  	function recalculateSteps(add:Float = 0):Int 	{ 		var lastChange:BPMChangeEvent = { 			stepTime: 0, 			songTime: 0, 			bpm: 0 		} 		for (i in 0...Conductor.bpmChangeMap.length) 		{ 			if (FlxG.sound.music.time > Conductor.bpmChangeMap[i].songTime) 				lastChange = Conductor.bpmChangeMap[i]; 		}  		curStep = lastChange.stepTime + Math.floor((FlxG.sound.music.time - lastChange.songTime + add) / Conductor.stepCrochet); 		updateBeat();  		return curStep; 	}  	function resetSection(songBeginning:Bool = false):Void 	{ 		updateGrid();  		FlxG.sound.music.pause(); 		// Basically old shit from changeSection??? 		FlxG.sound.music.time = sectionStartTime();  		if (songBeginning) 		{ 			FlxG.sound.music.time = 0; 			curSection = 0; 		}  		if(vocals != null) { 			vocals.pause(); 			vocals.time = FlxG.sound.music.time; 		} 		updateCurStep();  		updateGrid(); 		updateSectionUI(); 		updateWaveform(); 	}  	function changeSection(sec:Int = 0, ?updateMusic:Bool = true):Void 	{ 		//trace('changing section' + sec);  		if (_song.notes[sec] != null) 		{ 			curSection = sec;  			updateGrid();  			if (updateMusic) 			{ 				FlxG.sound.music.pause();  				/*var daNum:Int = 0; 					var daLength:Float = 0; 					while (daNum <= sec) 					{ 						daLength += lengthBpmBullshit(); 						daNum++; 				}*/  				FlxG.sound.music.time = sectionStartTime(); 				if(vocals != null) { 					vocals.pause(); 					vocals.time = FlxG.sound.music.time; 				} 				updateCurStep(); 			}  			updateGrid(); 			updateSectionUI(); 		} 		else 		{ 			changeSection(); 		} 		Conductor.songPosition = FlxG.sound.music.time; 		updateWaveform(); 	}  	function updateSectionUI():Void 	{ 		var sec = _song.notes[curSection];  		stepperLength.value = sec.lengthInSteps; 		check_mustHitSection.checked = sec.mustHitSection; 		check_gfSection.checked = sec.gfSection; 		check_altAnim.checked = sec.altAnim; 		check_changeBPM.checked = sec.changeBPM; 		stepperSectionBPM.value = sec.bpm;  		updateHeads(); 	}  	function updateHeads():Void 	{ 		var healthIconP1:String = loadHealthIconFromCharacter(_song.player1); 		var healthIconP2:String = loadHealthIconFromCharacter(_song.player2);  		if (_song.notes[curSection].mustHitSection) 		{ 			leftIcon.changeIcon(healthIconP1); 			rightIcon.changeIcon(healthIconP2); 			if (_song.notes[curSection].gfSection) leftIcon.changeIcon('gf'); 		} 		else 		{ 			leftIcon.changeIcon(healthIconP2); 			rightIcon.changeIcon(healthIconP1); 			if (_song.notes[curSection].gfSection) leftIcon.changeIcon('gf'); 		} 	}  	function loadHealthIconFromCharacter(char:String) { 		var characterPath:String = 'characters/' + char + '.json'; 		#if MODS_ALLOWED 		var path:String = Paths.modF…

---
## [folio-org/stripes-core](https://github.com/folio-org/stripes-core)@[daed280c9e...](https://github.com/folio-org/stripes-core/commit/daed280c9e2831a2303274bdcf911a3981c6765e)
#### Tuesday 2021-12-21 16:44:04 by Zak Burke

the most humble offering possible to the lint gods (#1148)

And there were developers sitting at their laptops nearby, keeping watch
over their code by night. Just then, an angel of lint stood before them,
and the glory of lint shone all around them, and they were terrified.
But the angel said unto them, "Do not be afraid! For behold! I bring you
good news of great joy that will be for all the people: Today in the
module of stripes-core, I discovered one insignificant space with no
semantic value and no visual clutter, but it really bugs me anyway. And
this will be a sign to you: you will find two complaints on every PR
about it, even when they have nothing to do with this file.

And suddenly there appeared around every stripes-core PR a great
multitude of lint complaints, saying:

```
Multiple spaces found before '/\.\/.*\.js$/'
```

When the lint angels had left them and gone into heaven, the developers
said to one another, "One lousy space? Was that guy serious?"

---
## [tyfighter/mame-dev](https://github.com/tyfighter/mame-dev)@[edcfe24353...](https://github.com/tyfighter/mame-dev/commit/edcfe243531b6a622a0cdef575fcf28eb8f9b12b)
#### Tuesday 2021-12-21 16:45:51 by ArcadeShadow

ibm5170.xml: New software list additions (#8946)

New working software list additions
Laser Squad (3.5", USA) [The Good Old Days]
Laser Squad (5.25", Euro) [The Good Old Days]
Night Shift [old-games.ru]
Push-Over [The Good Old Days]
Quest for Glory: Shadows of Darkness [The Good Old Days]
Quest for Glory I: So You Want to Be a Hero [The Good Old Days]
Quest for Glory III: Wages of War [The Good Old Days]

New non-working software list additions
Quicky: The Computer Game (Euro) [old-games.ru]
Tony & Friends in Kellogg's Land (Germany) [old-games.ru]

---
## [SomeAspy/aspy.dev](https://github.com/SomeAspy/aspy.dev)@[8cf303da7d...](https://github.com/SomeAspy/aspy.dev/commit/8cf303da7dfac13d78fac5f1f3d3e93ac78bdbd2)
#### Tuesday 2021-12-21 17:01:21 by Aiden

literally reset the fucking repo with my local files because what the fuck is this shit come on git why are you like this

---
## [axietheaxolotl/Skyrat-tg](https://github.com/axietheaxolotl/Skyrat-tg)@[fab444ffe2...](https://github.com/axietheaxolotl/Skyrat-tg/commit/fab444ffe2887cb2838f974a41c392ed48d2ae6e)
#### Tuesday 2021-12-21 17:42:49 by Seris02

[modular] big borg code improvements and fixes (#9701)

* big borg code improvements and fixes

* I missed a modular comment

* fuck you linters

* yis

* converts skyrat versions to better

* annnnnd that should fix it

---
## [cloudflare/wrangler2](https://github.com/cloudflare/wrangler2)@[78cd0804de...](https://github.com/cloudflare/wrangler2/commit/78cd0804def1a3246f8a4f6b1695bd91e81c1ad1)
#### Tuesday 2021-12-21 18:16:59 by Sunil Pai

implement custom builds, for `dev` and `publish` (#149)

* implement custom builds, for `dev` and `publish`

The code here is a bit jank, but we should probably refactor the way we pass arguments to dev and publish to 'fix' it properly. Anyway.

This PR adds custom builds to wrangler2 (https://developers.cloudflare.com/workers/cli-wrangler/configuration#build).
- In `wrangler.toml`, you can configure `build.command` and `build.cwd` and it'll be called before `publish` or `dev`. There's some discussion to be had whether we're going to deprecate this config commands, but we'll support it until then anyway.
- We _don't_ support `build.watch_dir`. We could, and I'm happy to add it after we discuss; but the idea is that watching shouldn't be wrangler's responsibility (which we've already broken with plain `dev`, and `pages dev`, so maybe we're wrong)
- You can pass the command after a last `--` in the cli (no support for `cwd` there). eg - `wrangler dev output/index.js -- some-build-command --out output/index.js`.

* Add a changeset

* fix lint error

* update snapshot tests

* remove `--`, add `watch_dir`

- removed the `--` option. We should have documentation showing how to do this with bash etc.
- Added support for `watch_dir`
- also added a definition for running tests from the root because it was annoying me to keep changing dirs to run tests

* log the name of the file that changed during a custom build

---
## [Xe/site](https://github.com/Xe/site)@[ee69f652e5...](https://github.com/Xe/site/commit/ee69f652e545b8a42c7cd3b93ff66c5825066e5e)
#### Tuesday 2021-12-21 18:37:42 by Xe

fuck you service worker cache

Signed-off-by: Xe <me@christine.website>

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[4610f700eb...](https://github.com/GoldenAlpharex/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Tuesday 2021-12-21 18:38:53 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d005d76f0b...](https://github.com/timothymtorres/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Tuesday 2021-12-21 19:03:11 by Kylerace

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
## [shane-create/Crown-clothing](https://github.com/shane-create/Crown-clothing)@[ccfd7d6445...](https://github.com/shane-create/Crown-clothing/commit/ccfd7d6445db7fa3ca8c23539eb9aec5faa289e1)
#### Tuesday 2021-12-21 20:05:05 by xhane-create

Seperating our create react app intoi client folder, added express server to help handle stripe payments. I have not coded on this for a while, but was able to get back into it easily, though i did have trouble with some error past me had left for future me. Curse past me and her procratenating! Also, i added sagas and stuff. Don't remember if ive already comm9ited that. And now clear cart works both for on sign out and for sucess cals. Sweetalerts were again used in  the stripe button, just to make the website look much better

---
## [PaulisterGD/CMGT-Y1B2-Project](https://github.com/PaulisterGD/CMGT-Y1B2-Project)@[68739c1757...](https://github.com/PaulisterGD/CMGT-Y1B2-Project/commit/68739c1757dcd171b3f32c1e26fefd03cb026465)
#### Tuesday 2021-12-21 20:17:22 by PaulisterGD

Prep part 4

Oh boy this one's big.
- Created a game over menu, which allows the player to either continue from where they left off (currently hard-coded to level 1) or end the game.
- Created a lives system. Player starts with 3 lives and gets sent to the Game Over screen if they die on 0 lives. 
- Continuing from a Game Over wipes the score of the player, respawning from a death does not.
- Finishing Level 1 rewards the player with 10000 points.
- Every extra life left upon finishing Level 1 rewards the player with 2000 points.
- Made the You Win screen a little prettier.

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[81e04065ad...](https://github.com/tdauth/wowr/commit/81e04065ad2578096aca1235e7860ba971256c38)
#### Tuesday 2021-12-21 20:22:35 by barade

1.8.9

- Improve stopping harvesting and building on hidden places.
- Fix minimum numbers for Demon Master (thanks Runeblade14) which led to a crash.
- Fix spelling mistake Banshee for Lordearon start location.
- Increase Freelancer XP rate bonus from 10 % to 30 %.
- Limit Fountain of Blood to 1.
- Fix units in Bosses group.
- Allow leveling legendary elemental book fire ability.
- Add World Tree to Night Elfs.
- Add tavern for second hero with Bosses.
- Fix preventing changing alliances with player bosses.
- Do not allow starting votekicks against Bosses or The Burning Legion.
- Fix buildable buildings and affecting upgrades for Fel Peon.
- Add Sea Giant boss to Sunken Ruins area who drops an item which allows you walking on water.
- Try clearing dialogs to avoid repick bug.
- Mention cooldown for Random Events in tooltip.
- Fix showing race selection dialog on repick.

---
## [chrisbobbe/zulip-mobile](https://github.com/chrisbobbe/zulip-mobile)@[d7d91dcfb6...](https://github.com/chrisbobbe/zulip-mobile/commit/d7d91dcfb63eae31cc39526337649743699da6a7)
#### Tuesday 2021-12-21 20:45:55 by Chris Bobbe

keyboard-avoiding ios: Begin forking RN's KeyboardAvoidingView

From
  node_modules/react-native/Libraries/Components/Keyboard/KeyboardAvoidingView.js
with v0.64.2 of `react-native`, adjusting only the license pointer
in the copyright header.

We'll make the fork usable soon, not in this pure copy-paste commit.

We don't like this implementation (see, e.g., 70eca0716, which took
a lot of painstaking investigation), but we want to fix #5162 as
soon as we can.

For a not-quite-perfect attempt at reimplementing it from scratch in
our style (and with #5162 fixed), see my branch
`reimplement-keyboard-avoiding-view` on GitHub.

We can't easily make a jank-free solution in a normal React Native
way because we can't have perfect information about the layout on
every frame. React Native exposes it to us by consuming event
listeners and providing asynchronous query functions, and we end up
having to learn about different aspects of the layout at different
times.

The best hope for a jank-free solution is to use native iOS APIs. If
we're feeling adventurous and we find the time, we should really try
hard to make React Native play along with iOS's
`keyboardLayoutGuide` API (iOS 15+).

The first four minutes of this video should be really useful
background on the `keyboardLayoutGuide` feature:
  https://developer.apple.com/videos/play/wwdc2021/10259/

It works within iOS's "Auto Layout" system:
  https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html

But then we'd have to go and

(a) Make a native component:
      https://reactnative.dev/docs/native-components-ios

(b) Figure out how to make React Native's propagate-from-JavaScript
    layout system (Yoga) not fight with the native iOS layout
    system, including "Auto Layout" and `keyboardLayoutGuide`.
    Possibly we can pick up some clues from
    `react-native-safe-area-context` for this?

From another angle, since the jank is regularly seen on screen
orientation changes between portrait and landscape, we could
consider just unsupporting the landscape orientation. On very common
device types, like phones, it's just not as easy to use the app in,
especially for composing messages.

---
## [PhantasarProductions/The-Fairy-Tale-REVAMPED-for-Apollo](https://github.com/PhantasarProductions/The-Fairy-Tale-REVAMPED-for-Apollo)@[dea2656afb...](https://github.com/PhantasarProductions/The-Fairy-Tale-REVAMPED-for-Apollo/commit/dea2656afbb58d80b92fa70f27873e06c0a28033)
#### Tuesday 2021-12-21 21:19:29 by Jeroen Broks

Fuck you!

This is not a fix! The game would never have worked at all if this was an actual bug.
This way I could at least void whatever is fucking up on me!

---
## [Mannybrado/mojave-sun-13](https://github.com/Mannybrado/mojave-sun-13)@[a05ac8da78...](https://github.com/Mannybrado/mojave-sun-13/commit/a05ac8da789735c2da9b4388f1944a1f2c556479)
#### Tuesday 2021-12-21 21:23:59 by EdwardNashton

Hunters and Citizens (#785)

* Hunters and Citizens

Remade a village on a east-south border of the map.
Remade entire living district nearby Hospital.
Slightly remade a "Military Robo-Bunker"
Small fixes included.

* Fixing a stuff

Fixed issues with "Hunters and Citizens"
Roofs, doors, some rooms.

* Fixing stuff: part 2

God damn roofs.

* Fixing stuff: part 3

God, I hate z-levels.

* Fuck your z-levels

Just fuck this shit.

* Finalization of Riddler changes

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Popoff <ProfessorPopoff@users.noreply.github.com>

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[52106430dc...](https://github.com/ttaylorr/git/commit/52106430dc80ea20ec2e00a6079a7bc114d36b70)
#### Tuesday 2021-12-21 21:40:13 by Ævar Arnfjörð Bjarmason

refs/files: remove "name exist?" check in lock_ref_oid_basic()

In lock_ref_oid_basic() we'll happily lock a reference that doesn't
exist yet. That's normal, and is how references are initially born,
but we don't need to retain checks here in lock_ref_oid_basic() about
the state of the ref, when what we're checking is either checked
already, or something we're about to discover by trying to lock the
ref with raceproof_create_file().

The one exception is the caller in files_reflog_expire(), who passes
us a "type" to find out if the reference is a symref or not. We can
move the that logic over to that caller, which can now defer its
discovery of whether or not the ref is a symref until it's needed. In
the preceding commit an exhaustive regression test was added for that
case in a new test in "t1417-reflog-updateref.sh".

The improved diagnostics here were added in
5b2d8d6f218 (lock_ref_sha1_basic(): improve diagnostics for ref D/F
conflicts, 2015-05-11), and then much of the surrounding code went
away recently in my 245fbba46d6 (refs/files: remove unused "errno ==
EISDIR" code, 2021-08-23).

The refs_resolve_ref_unsafe() code being removed here looks like it
should be tasked with doing that, but it's actually redundant to other
code.

The reason for that is as noted in 245fbba46d6 this once widely used
function now only has a handful of callers left, which all handle this
case themselves.

To the extent that we're racy between their check and ours removing
this check actually improves the situation, as we'll be doing fewer
things between the not-under-lock initial check and acquiring the
lock.

Why this is OK for all the remaining callers of lock_ref_oid_basic()
is noted below. There are only two of those callers:

* "git branch -[cm] <oldbranch> <newbranch>":

  In files_copy_or_rename_ref() we'll call this when we copy or rename
  refs via rename_ref() and copy_ref(). but only after we've checked
  if the refname exists already via its own call to
  refs_resolve_ref_unsafe() and refs_rename_ref_available().

  As the updated comment to the latter here notes neither of those are
  actually needed. If we delete not only this code but also
  refs_rename_ref_available() we'll do just fine, we'll just emit a
  less friendly error message if e.g. "git branch -m A B/C" would have
  a D/F conflict with a "B" file.

  Actually we'd probably die before that in case reflogs for the
  branch existed, i.e. when the try to rename() or copy_file() the
  relevant reflog, since if we've got a D/F conflict with a branch
  name we'll probably also have the same with its reflogs (but not
  necessarily, we might have reflogs, but it might not).

  As some #leftoverbits that code seems buggy to me, i.e. the reflog
  "protocol" should be to get a lock on the main ref, and then perform
  ref and/or reflog operations. That code dates back to
  c976d415e53 (git-branch: add options and tests for branch renaming,
  2006-11-28) and probably pre-dated the solidifying of that
  convention. But in any case, that edge case is not our bug or
  problem right now.

* "git reflog expire <ref>":

  In files_reflog_expire() we'll call this without previous ref
  existence checking in files-backend.c, but that code is in turn
  called by code that's just finished checking if the refname whose
  reflog we're expiring exists.

  See ae35e16cd43 (reflog expire: don't lock reflogs using previously
  seen OID, 2021-08-23) for the current state of that code, and
  5e6f003ca8a (reflog_expire(): ignore --updateref for symbolic
  references, 2015-03-03) for the code we'd break if we only did a
  "update = !!ref" here, which is covered by the aforementioned
  regression test in "t1417-reflog-updateref.sh".

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Keksk/mojave-sun-13](https://github.com/Keksk/mojave-sun-13)@[c339745ff7...](https://github.com/Keksk/mojave-sun-13/commit/c339745ff71d3ca6c90e11c1ceebb089cafb58e4)
#### Tuesday 2021-12-21 21:46:50 by ms-mirror-bot

[MIRROR] Mapping DLC - Random Spawner Pack [MDB IGNORE] (#797)

* Mapping DLC - Random Spawner Pack [MDB IGNORE] (#60522)

First off, I am aware of the Feature Freeze for this month. This PR was initially started in #60401 about a month ago to break the changes into smaller PRs. The end result for this PR is a poor man's attempt at roguelike procedural generation. Enjoy!

Link to the README for how the new spawner system works.

Added the following new random mapping spawners:

pen, crayon, stamp, paper, pamphlet, briefcase, folder, wardrobe closet, wardrobe closet colored, backpack, narcotics, permabrig_weapon, permabrig_gear, prison, material, carpet, ornament, generic decoration, statue, showcase, paint, tool, tool_advanced, tool_rare, material_cheap, material, material_rare, toolbox, flashlight, canister, tank, vending_restock, atmospherics_portable, tracking_beacon, musical_instrument, gambling, coin, money_small, money, money_large, drugs, dice, cigarette_pack, cigarette, cigar, wallet_lighter, lighter, wallet_storage, deck, toy, toy_figure, booze, snack, condiment, cups, minor_healing, injector, surgery_tool, surgery_tool_advanced, surgery_tool_rare, firstaid_rare, firstaid, patient_stretcher, medical supplies, crate, crate_abandoned, girder, grille, lattice, spare_parts, table_or_rack, table, table_fancy, tank_holder, crate_empty, crate_loot, closet_private, closet_hallway, closet_empty, closet_maintencne, chair, chair_maintence, chair_flipped, chair_comfy, barricade, data_disk, graffiti, mopbucket, caution_sign, bucket, soap, box, bin, janitor_supplies, soup, salad, dinner

Removed deprecated wizard trap, vault, and armory spawners.

* Mapping DLC - Random Spawner Pack [MDB IGNORE]

* Repaths our spawners

Co-authored-by: Tim <timothymtorres@gmail.com>
Co-authored-by: koshenko <koshenko@pm.me>

---
## [jonathanpeppers/maui](https://github.com/jonathanpeppers/maui)@[7424327668...](https://github.com/jonathanpeppers/maui/commit/742432766884bc6f22a939283705a7df9c35e4aa)
#### Tuesday 2021-12-21 22:01:16 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [omar-polo/kamid](https://github.com/omar-polo/kamid)@[c555879e04...](https://github.com/omar-polo/kamid/commit/c555879e04662e1363fea08285a6a4dc5dcd04dc)
#### Tuesday 2021-12-21 22:28:55 by Omar Polo

comment out the 9P2000.L stuff

Initially I thought to support the .L dialect, but now I'm not that
sure.  Tread on a directory is not that hard, and I personally like that
more than the .L alternative of the Treaddir, it's ugly.  Some .L stuff
may be interesting to support, at least for symlinks, but at least for a
first version I want to keep it simple and implement plain 9P2000.

---

