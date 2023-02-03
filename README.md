## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-02](docs/good-messages/2023/2023-02-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,207,131 were push events containing 3,417,387 commit messages that amount to 272,703,515 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[54f2d00160...](https://github.com/willior/Action_RPG_1/commit/54f2d001608fbd36790fc8ba013786c62fa4ead9)
#### Thursday 2023-02-02 00:30:28 by willior

Formula icons animate

AnimatedSprite2D/SpriteFrames Resource have changed significantly. it's generating a number of problems.
we set our Formula icons dynamically, meaning there is an AnimatedSprite2D node whose SpriteFrames property is set to formula_resource.formula_reference.icon whenever the formula_changed signal is emitted. AnimatedSprites no longer have a "playing" property: they now have methods like play() and stop(), like AnimationPlayer.
i am absolutely flabbergasted as to why this was changed. i understand that they want to bring in-line the functionality of AnimatedSprites with AnimationPlayer, but in that case, why not just always use a combination of AnimationPlayer and Sprite? the reason i used AnimatedSprite2D for the things that use it was because it was lightweight and simple. these changes overcomplexify the functionality of AnimatedSprite2D to the point where it's lost its desireability. if we need complex behaviour, we'll use an AnimationPlayer. the changes to SpriteFrames is just mind-boggling.
the most confusing aspect about this is that the SpriteFrames resource editor HAS DIFFERENT FUNCTIONALITY DEPENDING ON WHETHER A SpriteFrames RESOURCE IS ATTACHED TO AN AnimatedSprite2D OR NOT. WHAT THE FUCK??? this is the most misleading UI change i can think of. there was literally nothing wrong with it before. now, it just makes it similar to something that already exists, while breaking its own functionality. again, i wonder, WHY TRANSFORM A UNIQUE FEATURE INTO AN ALREADY-EXISTING ONE??? this is FUCKING baffling.

---
## [avar/git](https://github.com/avar/git)@[69bbbe484b...](https://github.com/avar/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Thursday 2023-02-02 00:42:27 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Thursday 2023-02-02 00:44:43 by Andrew Poelstra

Merge rust-bitcoin/rust-bitcoin#1532: Improve Psbt error handling

e7bbfd391353fd03d60550c768364e9de5d3e8c5 Improve Psbt error handling (DanGould)

Pull request description:

  ## Separate `encode::Error` and `psbt::Error` recursive dependency

  This initial work attempts to fix #837's first 2 points

  > - The current psbt::serialize::Deserialize has an error type of consensus::encode::Error. I think we should cleanly separate consensus encoding errors from application-level encoding errors like psbt.
  > - There is a recursive dependence between encode::Error and psbt::Error which would need to be cleanly dissected and separated so that there is no dependence or only one-way dependence.

  ## Better `ParseError(String)` types

  arturomf94 how compatible do your #1310 changes look to address #837's third point with this design?

  > - There are a lot ParseError(String) messages that could use a better type to downflow the information.

  I think your prior art would completely address this issue now.

  ## On handling `io::Error` with an associated error

  `encode::Error` has an `Io` variant. now that `Psbt::deserialize` returns `psbt::Error` and produces an `io::Error`, we need an `Io` variant on `psbt::Error`. Except that doing so breaks  `#[derive(Eq)]` and lots of tests for `psbt::Error`.

  Kixunil, I'm trying to understand your feedback regarding a solution to this problem.

  > I believe that the best error untangling would be to make decodable error associated.

  > I meant having associated `Error` type at `Decodable` trait. Encoding should only fail if the writer fails so we should have `io::Error` there (at least until we have something like `genio`).
  >
  > > [it] is a problem to instantiate consensus::encode::Error in [the psbt] module for `io::Error`?
  >
  > It certainly does look strange. Maybe we should have this shared type:
  >
  > ```rust
  > /// Error used when reading or decoding fails.
  > pub enum ReadError<Io, Decode> {
  >     /// Reading failed
  >     Io(Io),
  >     /// Decoding failed
  >     Decode(Decode), // consensus and PSBT error here
  > }
  > ```
  >
  > However this one will be annoying to use with `?` :( We could have `ResultExt` to provide `decode()` and `io()` methods to make it easier.
  >
  > If that's not acceptable then I think deduplicated IO error is better.

  Kixunil didn't we just get rid of Psbt as `Decodable`? Would this make more sense to have as an error associated with `Deserialize`? Or did we do the opposite of what we should have by making Psbt only `Serialize`/`Deserialize` because of #934, where only consensus objects are allowed to be `Decodable`? I wonder if we prioritized that strict categorization and are stuck with worth machinery because of it. My goal with #988 was to get to a point where we could address #837 and ultimately implement PSBTv2.

ACKs for top commit:
  tcharding:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5
  apoelstra:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5

Tree-SHA512: 32975594fde42727ea9030f46570a1403ae1a108570ab115519ebeddc28938f141e2134b04d6b29ce94817ed776c13815dea5647c463e4a13b47ba55f4e7858a

---
## [Urban-Coalition/ArcCW_UR](https://github.com/Urban-Coalition/ArcCW_UR)@[177cc75499...](https://github.com/Urban-Coalition/ArcCW_UR/commit/177cc7549999d32aee0d06cc504a0a926e7a10ab)
#### Thursday 2023-02-02 01:13:56 by rzen1th

efficiently utilize my favorite arccw """feature"""

fuck you git huib my commit summaries ARE great

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[a3543dc688...](https://github.com/lone2005/p2pspider/commit/a3543dc688019f58fc33da412f59d641fecf55cb)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge pull request #27 from Fuck-You-GFW/dev

update README.md

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[cb1f5e32a3...](https://github.com/lone2005/p2pspider/commit/cb1f5e32a3a7cd83115b6ec07f72152359010b44)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge pull request #33 from Fuck-You-GFW/dev

add leveldb sample

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[62b5a2c358...](https://github.com/lone2005/p2pspider/commit/62b5a2c358e9c09a668bb90cacc33aad64318334)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge branch 'dev' of https://github.com/Fuck-You-GFW/p2pspider into dev

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[c1123268a5...](https://github.com/lone2005/p2pspider/commit/c1123268a505b8aa8d992a4b1aa14931c60ac6db)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge pull request #38 from Fuck-You-GFW/dev

fixed ignore property same as function name

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[a1fb6bcb21...](https://github.com/lone2005/p2pspider/commit/a1fb6bcb21c5a7d7e88aa79132e596219b2da840)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge pull request #46 from Fuck-You-GFW/dev

fixed #45

---
## [lone2005/p2pspider](https://github.com/lone2005/p2pspider)@[96ff5de94e...](https://github.com/lone2005/p2pspider/commit/96ff5de94e63cda9f06e1383d857646b258a3e5b)
#### Thursday 2023-02-02 01:29:42 by Fuck-You-GFW

Merge pull request #49 from Fuck-You-GFW/dev

fixed #45

---
## [supchyan/TheAncientTear](https://github.com/supchyan/TheAncientTear)@[3398ff1def...](https://github.com/supchyan/TheAncientTear/commit/3398ff1defcc4cdec0f6bc937037d35e555314c1)
#### Thursday 2023-02-02 01:46:41 by supchyan

Add files via upload

Finally did such a great logic for the talking UI, let's go... my ass god damn

---
## [lovullo/tame](https://github.com/lovullo/tame)@[6d39474127...](https://github.com/lovullo/tame/commit/6d39474127b3fa39d4ce9d9e565be42da31996c2)
#### Thursday 2023-02-02 02:21:53 by Mike Gerwitz

tamer: NIR re-simplification

Alright, this has been a rather tortured experience.  The previous commit
began to state what is going on.

This is reversing a lot of prior work, with the benefit of
hindsight.  Little bit of history, for the people who will probably never
read this, but who knows:

As noted at the top of NIR, I've long wanted a very simple set of general
primitives where all desugaring is done by the template system---TAME is a
metalanguage after all.  Therefore, I never intended on having any explicit
desugaring operations.

But I didn't have time to augment the template system to support parsing on
attribute strings (nor am I sure if I want to do such a thing), so it became
clear that interpolation would be a pass in the compiler.  Which led me to
the idea of a desugaring pass.

That in turn spiraled into representing the status of whether NIR was
desugared, and separating primitives, etc, which lead to a lot of additional
complexity.  The idea was to have a Sugared and Plan NIR, and further within
them have symbols that have latent types---if they require interpolation,
then those types would be deferred until after template expansion.

The obvious problem there is that now:

  1. NIR has the complexity of various types; and
  2. Types were tightly coupled with NIR and how it was defined in terms of
     XML destructuring.

The first attempt at this didn't go well: it was clear that the symbol types
would make mapping from Sugared to Plain NIR very complicated.  Further,
since NIR had any number of symbols per Sugared NIR token, interpolation was
a pain in the ass.

So that lead to the idea of interpolating at the _attribute_ level.  That
seemed to be going well at first, until I realized that the token stream of
the attribute parser does not match that of the element parser, and so that
general solution fell apart.  It wouldn't have been great anyway, since then
interpolation was _also_ coupled to the destructuring of the document.

Another goal of mine has been to decouple TAME from XML.  Not because I want
to move away from XML (if I did, I'd want S-expressions, not YAML, but I
don't think the team would go for that).  This decoupling would allow the
use of a subset of the syntax of TAME in other places, like CSVMs and YAML
test cases, for example, if appropriate.

This approach makes sense: the grammar of TAME isn't XML, it's _embedded
within_ XML.  The XML layer has to be stripped to expose it.

And so that's what NIR is now evolving into---the stripped, bare
repsentation of TAME's language.  That also has other benefits too down the
line, like a REPL where you can use any number of syntaxes.  I intend for
NIR to be stack-based, which I'd find to be intuitive for manipulating and
querying packages, but it could have any number of grammars, including
Prolog-like for expressing Horn clauses and querying with a
Prolog/Datalog-like syntax.  But that's for the future...

The next issue is that of attribute types.  If we have a better language for
NIR, then the types can be associated with the NIR tokens, rather than
having to associate each symbol with raw type data, which doesn't make a
whole lot of sense.  That also allows for AIR to better infer types and
determine what they ought to be, and further makes checking types after
template application natural, since it's not part of NIR at all.  It also
means the template system can naturally apply to any sources.

Now, if we take that final step further, and make attributes streaming
instead of aggregating, we're back to a streaming pipeline where all
aggregation takes place on the ASG (which also resolves the memcpy concerns
worked around previously, also further simplifying `ele_parse` again, though
it sucks that I wasted that time).  And, without the symbol types getting
in the way, since now NIR has types more fundamentally associated with
tokens, we're able to interpolate on a token stream using simple SPairs,
like I always hoped (and reverted back to in the previous commit).

Oh, and what about that desugaring pass?  There's the issue of how to
represent such a thing in the type system---ideally we'd know statically
that desugaring always lowers into a more primitive NIR that reduces the
mapping that needs to be done to AIR.  But that adds complexity, as
mentioned above.  The alternative is to just use the templat system, as I
originally wanted to, and resolve shortcomings by augmenting the template
system to be able to handle it.  That not only keeps NIR and the compiler
much simpler, but exposes more powerful tools to developers via TAME's
metalanguage, if such a thing is appropriate.

Anyway, this creates a system that's far more intuitive, and far
simpler.  It does kick the can to AIR, but that's okay, since it's also
better positioned to deal with it.

Everything I wrote above is a thought dump and has not been proof-read, so
good luck!  And lets hope this finally works out...it's actually feeling
good this time.  The journey was necessary to discover and justify what came
out of it---everything I'm stripping away was like a cocoon, and within it
is a more beautiful and more elegant TAME.

DEV-13346

---
## [klorpa/tgstation](https://github.com/klorpa/tgstation)@[125745d232...](https://github.com/klorpa/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Thursday 2023-02-02 02:43:02 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [Terminator-J/crdroid_kernel_oneplus_sdm845](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845)@[1e0dacdd93...](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845/commit/1e0dacdd936695269de5c3256ce5c57871b13a8d)
#### Thursday 2023-02-02 02:48:49 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [vfcardoso-dev/vfcardoso-dev](https://github.com/vfcardoso-dev/vfcardoso-dev)@[dda35d1a22...](https://github.com/vfcardoso-dev/vfcardoso-dev/commit/dda35d1a221d9184731542febc1a0e7804001db5)
#### Thursday 2023-02-02 02:52:20 by Vinícius Cardoso

Update README.md

### Hi there 👋

I'm Vinícius. I'm from Macaé, Rio de Janeiro, Brasil.

Currently working as Sr Software Developer @ Sapiensia Tecnologia (full-time), since September 2019.<br>
You can contact me at hello [at] vfcardoso [dot] dev.

This is my personal github profile, where I'm maintaining some public and private repositories. Feel free to explore.

Here are a few facts about me:

- My hometown 📍 is Casimiro de Abreu/RJ, where the eponymous poet lived.
- I've been an amateur musician since I was 12 years old. I play some musical instruments, but I prefer the piano 🎹.
- I'm interested in biology, astronomy, physics, chemistry and other STEM fields 🔬.
- I really like photography 📷 too. I have a <a href="https://www.flickr.com/photos/vinicardoso">flickr account</a> with some pictures.
- As a old school nerd, I love science fiction and fantasy: star trek, star wars, lotr…
- I like wine 🍷 and coffee ☕ too.





<!--
**vfcardoso-dev/vfcardoso-dev** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

---
## [openeuler-mirror/kernel](https://github.com/openeuler-mirror/kernel)@[4b944c0fc7...](https://github.com/openeuler-mirror/kernel/commit/4b944c0fc78beb19540c2eb797a5c4867020a612)
#### Thursday 2023-02-02 02:59:43 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

stable inclusion
from stable-v5.10.141
commit adee8f3082b01e5dab620d651e3ec75f57c0c855
category: bugfix
bugzilla: https://gitee.com/openeuler/kernel/issues/I685FC

Reference: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=adee8f3082b01e5dab620d651e3ec75f57c0c855

--------------------------------

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jialin Zhang <zhangjialin11@huawei.com>
Reviewed-by: Zheng Zengkai <zhengzengkai@huawei.com>

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[a47afd9051...](https://github.com/Paxilmaniac/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Thursday 2023-02-02 03:20:06 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [x-em/guava](https://github.com/x-em/guava)@[8a676ade61...](https://github.com/x-em/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Thursday 2023-02-02 03:46:25 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [remlse/rust](https://github.com/remlse/rust)@[7a49959ea4...](https://github.com/remlse/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Thursday 2023-02-02 03:58:13 by Remo Senekowitsch

xorcism: remove rstest dependency (#1590)

rstest uses proc macros, which make the tests timeout due to long
compile times. Replace rstest with a custom declarative macro.

Brings test time from 7.5 seconds to 0.8 seconds on my machine.

Drawbacks:
* more indentation
* module structure of tests is flipped around

both of those seem minor to me. 

Although declarative macros can be hard to read for those unfamiliar, 
that was already somewhat the case with rstest's magic in my opinion. So
I personally don't think it's worse in terms of the students being able to
understand the tests.

The only other alternative I see is to disable the online tests 
altogether and leave a note about that in the exercise description. That
probably wouldn't be that bad, since people solving this hard exercise
most likely have a solid local setup. But it would still be cool to run
the tests online as well.

https://github.com/exercism/rust/issues/1513

---
## [brong/jmap](https://github.com/brong/jmap)@[951395e2f6...](https://github.com/brong/jmap/commit/951395e2f63c9f40aa4777e8f4ca154b50f12645)
#### Thursday 2023-02-02 04:44:28 by Chris Morgan

Define primary accounts more carefully

This entails a few functional changes:

• Specification of which primary account to infer for null accountId;
• Returning accountNotFound when there is no suitable primary account;
• Email/copy, similar but for fromAccountId and toAccountId;
• Blob/copy, fromAccountId and toAccountId are made mandatory.

Details (including what and why) are in the narrative that follows.

I believe there used to be but one (exactly one?) primary account, but
now there is up to one per capability URI. Most of the spec hadn’t been
updated to match this reality, and there were a few places where it
caused problems of mild and easily resolved ambiguity, a couple of
places where it led to undefined or unimplementable behaviour.

Mostly this is just clarifying what a normal person would have assumed,
but it also defines something that was previously undefined: what to do
when no accountId (or fromAccountId or toAccountId for Email/copy and
Blob/copy) is passed, *and* no primary account is found: return
accountNotFound (or fromAccountNotFound or toAccountNotFound for
Email/copy and Blob/copy).

One other substantial change: Blob/copy’s fromAccountId and toAccountId
are now mandatory, because there’s no specification to tie Blob to (it’s
not a regular data type, but is fundamental to JMAP and used from other
specifications), so it can only make any sense while there is only one
primary account in the session. We *could* keep it optional, telling it
“if all the primary accounts are the same, breathe a sigh of relief and
use that primary account, otherwise panic”, but that would lead to
surprising behaviour when you add a new capability on the server and it
suddenly breaks something that formerly worked; that’s a bad mode of
extensibility, so it’s best to avoid the pain by making those particular
arguments mandatory from the start. Again, this is only going to be a
problem for Blob because it’s core; Email/copy doesn’t have this problem
because it’s tied to the urn:ietf:params:jmap:mail capability, which can
have a primary account.

I still confess myself unconvinced that accountId being optional is
desirable.

There’s inconsistency in the spec concerning what it calls things like
“urn:ietf:params:jmap:mail”; some places refer to it as a “specification
[URI]”, others as a “capability [URI]”. We should normalise all of these
at some point. I went for referring to them as capabilities in these
changes as I got the vague impression that was probably preferred.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Thursday 2023-02-02 05:31:40 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Touch-Night/Requiem](https://github.com/Touch-Night/Requiem)@[a86ed30451...](https://github.com/Touch-Night/Requiem/commit/a86ed3045187fc9363da7ae1a3b5e5e0793249f9)
#### Thursday 2023-02-02 06:17:37 by Pyrofab

Happy new year folks!!!

Stay proud, stay safe, and do what the hell you want. And hey, find yourself some friends with which to overthrow oppressive systems while you're at it.

---
## [Gr33d-y/Bubberstation](https://github.com/Gr33d-y/Bubberstation)@[8740a402d3...](https://github.com/Gr33d-y/Bubberstation/commit/8740a402d3225aaee513aa3b8f80dd0240a988e7)
#### Thursday 2023-02-02 06:25:51 by Gr33d-y

fuck this shit so fucking hard holy shit who MADE AUTO MAPPING I WANT THEM DEAD

---
## [VastKilleroOm/Skyrat-tg](https://github.com/VastKilleroOm/Skyrat-tg)@[ffac8f0df0...](https://github.com/VastKilleroOm/Skyrat-tg/commit/ffac8f0df07c8473e26420a8fe3c1acf6bd20dbf)
#### Thursday 2023-02-02 06:57:57 by SkyratBot

[MIRROR] Fixes critical plane masters improperly not being readded in show_to [MDB IGNORE] (#19060)

Fixes critical plane masters improperly not being readded in show_to (#72604)

## About The Pull Request

[Adds support for pulling z offset context from an atom's
plane](https://github.com/tgstation/tgstation/commit/9f215c5316e5cfdbedf6a23ff97dfee0e523354b)

This is needed to fix paper bins, since the object we plane set there
isn't actually on a z level.
Useful elsewhere too!

[Fixes compiler errors that came from asserting that plane spokesmen had
a plane
var](https://github.com/tgstation/tgstation/commit/b830002443f2fbe230e9ff00236d7a46a9f2eec7)

[Ensures lighting backdrops ALWAYS exist for each lighting
plane.](https://github.com/tgstation/tgstation/commit/0e931169f7c5336333bc6f41353c82f603fc1170)

They can't float becuase we can see more then one plane at once yaknow?

[Fixes parallax going to shit if a mob moved zs without having a
client](https://github.com/tgstation/tgstation/commit/244b2b25baecfc644505a3ea1e348e0cb97a04e0)

Issue lies with how is_outside_bounds just blocked any plane readding
It's possible for a client to not be connected during z moves, so we
need to account for them rejoining in show_to, instead of just blocking
any of our edge cases.

Fixing this involved having parallax override blocks for show_plane and
anything with the right critical flags ensuring mobs have JUST the right
PMs and relays.
It's duped logic but I'm unsure of how else to handle it and frankly
this stuff is just kinda depressing.
Might refactor later

[show_to can be called twice successfully with no hide_from
call.](https://github.com/tgstation/tgstation/commit/092581a5c06f7f884f48d41c96fa9300327ef214)

Ensures no runtimes off the registers from this

## Why It's Good For The Game

Fixes #72543
Fixes lighting looking batshit on multiz. None reported this I cry into
the night.

## Changelog
:cl:
fix: Fixes parallax showing up ABOVE the game if you moved z levels
while disconnected
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[406b6870bd...](https://github.com/Erol509/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Thursday 2023-02-02 07:00:37 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [dvjromashkin/testnets-8](https://github.com/dvjromashkin/testnets-8)@[ab514c6494...](https://github.com/dvjromashkin/testnets-8/commit/ab514c6494fdd26836a952ab6fe64c44f1886047)
#### Thursday 2023-02-02 08:13:46 by Roman Shaulskyi

cryptech gentx

Good afternoon, I want to introduce you our team of 6 people.
Our dream team:
Denis - Team Leader, Blockchain Expert
Daria - Marketing Advisor
Taras - Computer Systems Engineer
Roman - DevOps, Network Engineer
Ivan - DevOps, Cryptography Specialist
Oleksii - Community Manager, DevOps

We are enthusiasts who believe that very soon blockchain technologies will become an integral part of the life of an ordinary person. We are specialists in the field of system administration and have extensive experience in setting up and maintaining decentralized nodes of various networks.  Here are some of them: ALEO, Ironfish, Solana-TestNet, Neon-LAbs, Minima, KYVE, Asset Mantle, Game, Cosmic Horizon, KleverChain, TGRADE, Celestia, Archway, QUAI Network, APTOS, Penumbra, STARKNET, SUI, GNOLang, Sei, QuickSilver, OBOL, LAYER ZERO, Web3Auth, DWEB, Oasys, Algoracle, Covalent, Abacus, peaq, Crescent, DeFund, Laconic, Subspace, Gitopia, Massa, Kira, ANOMA, Humanode, ChainFlip, Masa Finance, Manta-Kalamari, GEAR, Supra Oracle, Cere Network, Secret Networt, MoonBeam, Ki-Chain, KOII, Spacemesh, Stargaze, BlockPI and many others.

Our team has many years of experience in network infrastructure, setting up and maintaining client servers based on Linux (Debian, Ubuntu, CentOS, etс.), creating monitoring and warning systems (Prometheus, Zabbix, Nagois, Grafana), writing and compiling Dockerfiles (above 4 years experience), writing scripts and programs in languages (Python, Bash, PowerShell), knows programming languages such as RUST, Go, Javascript, which allows us to fully participate in projects based on CosmosSDK, Ethereum, Polkadot, ZK-snark, work with Bridges, and Blockchain Relays. We carry out full-fledged work with Github and search for Bugs, make various kinds of Feedbacks (bugreports, etc.)

For our part, we provide comprehensive assistance and support to development teams - we deploy and maintain nodes of their decentralized networks on our equipment, we conduct functional testing and search for bugs. We also promote projects and create educational content that reveals projects in simple terms from the technical, conceptual and practical sides. We write articles, translate blogs and technical documentation, create video materials in the form of short promos and lectures about projects (mostly in Russian, but we can do it in English). You can see our content and working projects at the links below:

http://cryptech.com.ua/
https://twitter.com/CryptechNodes
https://cryptech-nodes.medium.com/
https://www.youtube.com/channel/UCGwQIwKu1QuB9YxW-vElNbQ
https://www.twitch.tv/projectcryptech (The last broadcast was quite a while ago because our speaker was ill, but we will be back to this activity soon)

We do not rent cloud servers, we purchased, configured and maintain all the capacities on our own.

We have created our own data center and work with the following equipment:
HPE Proliant DL580 Gen9 Server Quad 24-Core E7-8894 v4 **96 Cores 512GB RAM, 8 x Intel P3520 Series 2 TB SSD
4 x HP GEN 9, CPU - 2 x Intel Xeon E-4667 v3, RAM - DDR-4 368 GB, SSD - 5 x Intel P3520 Series 2 TB
4 x Quanta - 2 x Intel (R) Xeon (R) CPU E5-2699 v3 @ 2.30GHz, RAM - DDR-4 368 GB, SSD - 5 x Intel P3520 Series 2 TB
2 x Gigabyte 1U - 2 x Intel (R) Xeon (R) CPU E5-2699 v3 @ 2.30GHz, RAM - DDR-4 256 GB, SSD - 5 x Intel P3520 Series 2 TB
2 x SuperMicro with SGX processors Intel Xeon E2278G, RAM - DDR-4 128 GB, 5 x Intel P3520 Series 2 TB
We get the Internet from three backbone providers in our country: Eurotranstelecom, Vega Telecom, DataLine. We have our own autonomous system and communication channels with a speed of 1 Gigabit / s each and a backup power supply system, which allows our data center to work without interruptions 24/7 with 1000% uptime.
For the last 4 years we have been working in the blockchain industry and participating in a large number of full-time projects. Before that, we were involved in various projects and various branches of the IT industry. BUT gradually we became interested in blockchains, and our hobby became our main occupation.

---
## [Saratii/Saratoga-MK3](https://github.com/Saratii/Saratoga-MK3)@[0ba49b211e...](https://github.com/Saratii/Saratoga-MK3/commit/0ba49b211e0e00a3b56dceed37ca81a1d5a8c5d7)
#### Thursday 2023-02-02 08:38:51 by Your Name

i hate my life - added multivariable vector calculus engine (gradient matrix coming soon)

---
## [digitalservicebund/ris-backend-service](https://github.com/digitalservicebund/ris-backend-service)@[ffeb3c1998...](https://github.com/digitalservicebund/ris-backend-service/commit/ffeb3c1998da69b4093c280a7cd4ed0b497873e7)
#### Thursday 2023-02-02 08:47:00 by Thore Strassburg

Chore: add post-commit hook for Talisman

We still have some issues with our Talisman ckecksum updating process.
Every time Talisman detects a potential secret in a file, a human has to
very it is not. Then the hash of the current file content has to be
configured as secure.
As soon as the file gets touched, the hash changes and the checksum in
the configuration is obsolete. The next time Talisman reports a secret
in this file, it will check the hash, detect that is not the configured
one where a human has verified the file last time, and reports an issue.

Talisman checks for secrets in files in two different ways. For commits,
it searches only within the diff of the commit for secrets. If there is
no secret, everything is fine. If it finds a secret, it checks if the
content of the file is marked secure by its hash (which is never the
case for a commit which changes the file). It reports the warning and
the user has to verify the files, update the configured checksum and
update the commit.
The second case is for pre-push. Here is checks all files that have been
touched within all commits that are pushed. But here is checks the whole
file content, not just the diff(s). This means, because any commit that
gets pushed has changed the file content, it automatically invalidates
the configured checksum. But because Talisman checks the full file
again, it also detects the old/already reported potential secrets. But
as the hash is no more the same, it reports the old issues again. In
such a case, the user simply has to update the checksum. But only under
the strong assumption that every potential secret was properly reported
and checked during a pre-commit.
This mechanism of Talisman is a "more secure" one, because it actually
does not rely on a history of always guaranteed security check by every
developer.

Unfortunately it is still not possible to verify the whole file as
staged in a pre-commit. But it is also annoying to have the pre-push
hook failing for this. Especially if more than a single commit gets
pushed. Because then it is hard to update the checksums incrementally
for every file content hash as staged for each commit. This leads to
stupid "talisman-update-commits" and checksum jumps.
The used alternative now is to have a post-commit hook. This hooks
"abuses" Talisman his pre-push functionality to check full files touched
by commits. Just that it now runs only the always just created commit.
This detects checksum changes early on commit basis and allows to update
them immediately to amend the commit correctly without much effort.
As Talisman relies on the default git pre-push hook arguments which are
not existing for a post-commit hook, we have to artificially creating
them. We kinda did so already in our pre-push hook too due to some
Lefthook limitations.
Finally, as this is still "experimental", we keep the pre-push hook too.
If everything works fine, nothing is worse than before. If not, it saves
us and allows us to improve the hooks.

---
## [ShibnaRazeen/Movielens-Case-Study](https://github.com/ShibnaRazeen/Movielens-Case-Study)@[75cb22128e...](https://github.com/ShibnaRazeen/Movielens-Case-Study/commit/75cb22128eaf96d648f98367f74272e1771c3c73)
#### Thursday 2023-02-02 08:50:10 by Shibna Razeen

Add files via upload

DESCRIPTION

Background of Problem Statement :

The GroupLens Research Project is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Members of the GroupLens Research Project are involved in many research projects related to the fields of information filtering, collaborative filtering, and recommender systems. The project is led by professors John Riedl and Joseph Konstan. The project began to explore automated collaborative filtering in 1992 but is most well known for its worldwide trial of an automated collaborative filtering system for Usenet news in 1996. Since then the project has expanded its scope to research overall information by filtering solutions, integrating into content-based methods, as well as, improving current collaborative filtering technology.

Problem Objective :

Here, we ask you to perform the analysis using the Exploratory Data Analysis technique. You need to find features affecting the ratings of any particular movie and build a model to predict the movie ratings.

Domain: Entertainment

Analysis Tasks to be performed:

Import the three datasets
Create a new dataset [Master_Data] with the following columns MovieID Title UserID Age Gender Occupation Rating. (Hint: (i) Merge two tables at a time. (ii) Merge the tables using two primary keys MovieID & UserId)
Explore the datasets using visual representations (graphs or tables), also include your comments on the following:
User Age Distribution
User rating of the movie “Toy Story”
Top 25 movies by viewership rating
Find the ratings for all the movies reviewed by for a particular user of user id = 2696
Feature Engineering:
            Use column genres:

Find out all the unique genres (Hint: split the data in column genre making a list and then process the data to find out only the unique categories of genres)
Create a separate column for each genre category with a one-hot encoding ( 1 and 0) whether or not the movie belongs to that genre. 
Determine the features affecting the ratings of any particular movie.
Develop an appropriate model to predict the movie ratings
Dataset Description :

These files contain 1,000,209 anonymous ratings of approximately 3,900 movies made by 6,040 MovieLens users who joined MovieLens in 2000.

Ratings.dat
    Format - UserID::MovieID::Rating::Timestamp

Field	Description
UserID	Unique identification for each user
MovieID	Unique identification for each movie
Rating	User rating for each movie
Timestamp	Timestamp generated while adding user review
UserIDs range between 1 and 6040 
The MovieIDs range between 1 and 3952
Ratings are made on a 5-star scale (whole-star ratings only)
A timestamp is represented in seconds since the epoch is returned by time(2)
Each user has at least 20 ratings
 

Users.dat
Format -  UserID::Gender::Age::Occupation::Zip-code

Field	Description
UserID	Unique identification for each user
Genere	Category of each movie
Age	User’s age
Occupation	User’s Occupation
Zip-code	Zip Code for the user’s location
All demographic information is provided voluntarily by the users and is not checked for accuracy. Only users who have provided demographic information are included in this data set.

Gender is denoted by an "M" for male and "F" for female
Age is chosen from the following ranges:
 

Value	Description
1	"Under 18"
18	"18-24"
25	"25-34"
35	"35-44"
45	"45-49"
50	"50-55"
56	"56+"
 

Occupation is chosen from the following choices:
Value
 	Description
0	"other" or not specified
1	"academic/educator"
2	"artist”
3	"clerical/admin"
4	"college/grad student"
5	"customer service"
6	"doctor/health care"
7	"executive/managerial"
8	"farmer"
9	"homemaker"
10	"K-12 student"
11	"lawyer"
12	"programmer"
13	"retired"
14	 "sales/marketing"
15	"scientist"
16	 "self-employed"
17	"technician/engineer"
18	"tradesman/craftsman"
19	"unemployed"
20	"writer”

Movies.dat
Format - MovieID::Title::Genres

Field	Description
MovieID	Unique identification for each movie
Title	A title for each movie
Genres	Category of each movie
 

 Titles are identical to titles provided by the IMDB (including year of release)
 

Genres are pipe-separated and are selected from the following genres:
Action
Adventure
Animation
Children's
Comedy
Crime
Documentary
Drama
Fantasy
Film-Noir
Horror
Musical
Mystery
Romance
Sci-Fi
Thriller
War
Western
Some MovieIDs do not correspond to a movie due to accidental duplicate entries and/or test entries
Movies are mostly entered by hand, so errors and inconsistencies may exist

---
## [swc132994/BD64game_v2.666](https://github.com/swc132994/BD64game_v2.666)@[43c82634b2...](https://github.com/swc132994/BD64game_v2.666/commit/43c82634b28df8ed17394ad72239db4319da022b)
#### Thursday 2023-02-02 09:57:32 by IDDQD_1337

Updated color blood for Acid Demon, HellKnight, Bruiser and Knightmare

After added green blood for Acid Demon, HellKnight, Bruiser and Knightmare then these opponents, then their blood was painted in the appropriate color

---
## [chandanr/linux](https://github.com/chandanr/linux)@[e2b614f3cd...](https://github.com/chandanr/linux/commit/e2b614f3cd628cb8e57f875a33e5e4dba6ddb86a)
#### Thursday 2023-02-02 12:21:45 by Darrick J. Wong

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

---
## [DesconCore/DesconCore](https://github.com/DesconCore/DesconCore)@[ef949f9ff0...](https://github.com/DesconCore/DesconCore/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Thursday 2023-02-02 12:30:50 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [Malii47/GucluSarp](https://github.com/Malii47/GucluSarp)@[68eee79eb9...](https://github.com/Malii47/GucluSarp/commit/68eee79eb9bc2954f72eef2657c4552f051da3b7)
#### Thursday 2023-02-02 12:50:26 by FangeLLL

MASSIVE UPDATE 2

-Enemy knockback system has been improved and finished.
- Some sound effects have been reworked.
- Fixed an issue that when you stun an enemy, player's hp damage doesn't increase.
- Fixed an issue that when you stun enemies in a row, the hp damage decreased based on the state of the last stunned enemy.
- Fixed an issue when you stun enemies, they are floating like a fucking bird.
- Fixed an issue that i don't remember:D
- Fixed a lot of issues that I didn't cause.
-Fixed an issue that berke is a juicy ball.
Fixed an issue that im gonna fuck this game.

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[e1e6285a3a...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/e1e6285a3a698ec08326fbd5074e1fcd5a6305ca)
#### Thursday 2023-02-02 13:02:21 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [HoangLong-Lumi/samsung-exynos9820](https://github.com/HoangLong-Lumi/samsung-exynos9820)@[9d24226f56...](https://github.com/HoangLong-Lumi/samsung-exynos9820/commit/9d24226f562c4ef34142320a5d33105a7ee64d27)
#### Thursday 2023-02-02 13:36:51 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [jackshirazi/kibana](https://github.com/jackshirazi/kibana)@[afb09ccf8a...](https://github.com/jackshirazi/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Thursday 2023-02-02 14:10:08 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[ab416a4879...](https://github.com/git-for-windows/git/commit/ab416a4879cec8032d5309d95e6b9aca247bade6)
#### Thursday 2023-02-02 14:56:36 by Johannes Schindelin

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
## [lisakowen/gpdb](https://github.com/lisakowen/gpdb)@[27011bcffa...](https://github.com/lisakowen/gpdb/commit/27011bcffa74a5113c9b5408c678315e74fb9a70)
#### Thursday 2023-02-02 16:37:08 by Tom Lane

Fix old bug with coercing the result of a COLLATE expression.

There are hacks in parse_coerce.c to push down a requested coercion
to below any CollateExpr that may appear.  However, we did that even
if the requested data type is non-collatable, leading to an invalid
expression tree in which CollateExpr is applied to a non-collatable
type.  The fix is just to drop the CollateExpr altogether, reasoning
that it's useless.

This bug is ten years old, dating to the original addition of
COLLATE support.  The lack of field complaints suggests that there
aren't a lot of user-visible consequences.  We noticed the problem
because it would trigger an assertion in DefineVirtualRelation if
the invalid structure appears as an output column of a view; however,
in a non-assert build, you don't see a crash just a (subtly incorrect)
complaint about applying collation to a non-collatable type.  I found
that by putting the incorrect structure further down in a view, I could
make a view definition that would fail dump/reload, per the added
regression test case.  But CollateExpr doesn't do anything at run-time,
so this likely doesn't lead to any really exciting consequences.

Per report from Yulin Pei.  Back-patch to all supported branches.

Discussion: https://postgr.es/m/HK0PR01MB22744393C474D503E16C8509F4709@HK0PR01MB2274.apcprd01.prod.exchangelabs.com

---
## [StuartMacKay/django-lynx](https://github.com/StuartMacKay/django-lynx)@[11d287153b...](https://github.com/StuartMacKay/django-lynx/commit/11d287153b4cd4a64d282473dfe9f11b60157a8a)
#### Thursday 2023-02-02 17:00:13 by Stuart MacKay

Rename the Topic model to Tag

Topics vs Tags is the subject of many a blog post as people try to
wrestle with the difference and usage. The best definition seen so far
comes from:

https://www.justorganizeyourstuff.com/categorize/categories-subjects-topics-tags-oh-my

which cleanly separates hierarchical things:

  topics (are grouped into) subjects (are grouped into) categories

from the non-hierarchical:

  tags

Originally when lynx was created the Topic model was intended to form
a hierarchical structure so posts writing about the same or related
topics could easily be found. That quickly becomes unmanageable for
two reasons:

1. Classifying, i.e. reading even a small number of posts takes a lot
   of time. It's possible to automate this, maybe, but the
   implementation will be complex and time-consuming.

2. Depending on the subject, most posts are simply opinion pieces by
   the author and so the information does not necessarily have a long
   shelf-life. That brings the whole idea of Topics into question as
   the set of current topics is constantly changing.

Instead of building a structured index of the blog posts using topics,
tags can easily fulfil that role as long as the same set of tags are
applied consistently to the posts. In that sense tags operate as a
keyword search, allowing people to easily find related posts. The
quality of the results will depend on how the tags are applied,
however for blog posts that probably does not present a problem as the
people doing the search probably does not need the search to be
exhaustive or comprehensive anyway.

Once it became clear that that organising posts into topics was not
simple, straightforward and actually had limited value for most people
the Topic model was changed from using Tagulous to a simple many to
many field with auto-complete. Now that topics became tags it seemed
only sensible to rename the model since we might, at some stage, want
to make another attempt at the whole hierarchical thing (initially
adding categories) and having names with specific meaning is always
cleaner and easier to understand.

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[ae08395328...](https://github.com/VladinXXV/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Thursday 2023-02-02 17:47:07 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[558717e6f6...](https://github.com/cmss13-devs/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Thursday 2023-02-02 18:53:22 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

github

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[74144f2bc9...](https://github.com/jlsnow301/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Thursday 2023-02-02 19:05:12 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [TwelveEyes/Ted-Tweaks](https://github.com/TwelveEyes/Ted-Tweaks)@[acfa951ad5...](https://github.com/TwelveEyes/Ted-Tweaks/commit/acfa951ad5f620e982ca32a4567fa557539c5f0e)
#### Thursday 2023-02-02 19:52:24 by ted

- Boner: Use HDB_SCRAP instead of HDB_FRAG.

This makes it so you're not just fucked if you get hit by one with anything below a shieldcore/blue armor to my knowledge. Painful.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ecbcc5f09e...](https://github.com/pytorch/pytorch/commit/ecbcc5f09ebea0a885b33572f6465eef03643637)
#### Thursday 2023-02-02 20:47:11 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fbae76ebf7...](https://github.com/mrakgr/The-Spiral-Language/commit/fbae76ebf7e1306ce9d30cc6b24cae318a021114)
#### Thursday 2023-02-02 20:51:05 by Marko Grdinić

"9:05am. I slept in bed long, but at least I slept well. Any mail? I think today I really should be getting something. I am nervous.

9:10am. Nothing from Enso, but I got a reply from the Softfluency CTO. It is a Serbian place. Now it is time to schedule my first meeting. How about tomorrow in the morning, 11am?

First of all, let me remind myself of how to set the alarm on my mobile.

9:15am. It is easy enough. It is turned off now. I'll turn it on before going to bed. Now, I'll schedule a meeting for 11am.

9:25am. Sent the email. I am really getting a wildly different treatment now compared to when I tried sending that fake Google resume. We'll see how it goes.

By now the companies I've sent my resume to must have seen it, so the only reason they have not replied must be because it is low priority for them. I want to apply to one more place, that I saw on HN yesterday.

///

Glimpse.ai | Senior/Lead Machine Learning Engineer | Remote | Full-time | VISA Sponsorship Available | $200k - $350k + Benefits + Equity | https://www.glimpse.ai
Glimpse.ai is a profitable, stable, and growing artificial intelligence startup that is building an NLP product that automatically writes content about any subject with the same level of quality, factual accuracy, and usefulness as a human. This product already has thousands of monthly paying subscribers.

Our research is centered around making language modeling more accurate, fluent, and useful for users. We are able to write accurately about topics that are too recent for a model to have been trained on (such as writing about FTX) and about topics that are extremely fact dense where current models would hallucinate and write inaccurately.

You would be at the intersection of research and production code - constantly ingesting research papers, building prototypes, and later turning those prototypes into production code.

Our ML work almost exclusively involves very heavy deep learning (transformers) and we primarily use PyTorch.

You will be working directly with our Founder/CEO (me!), who is leading the ML team, both as a manager and an individual contributor.

For this level of seniority we are specifically looking for people who extensive experience training very large language models and/or reinforcement learning from human feedback for NLP tasks. (If you do not meet this level of seniority, still feel free to reach out!)

We are fully remote and can hire internationally as long as your work schedule has overlap with US working hours.

Contact us by emailing alex@glimpse.ai with "HN" in the subject line or apply at https://careers.glimpse.ai

///

It is very unlikely that I could get in here, but let me give it a try.

///

Let me say right away that I do not have any experience with LLMs or RLHF. My only experience in NLP is when I implemented a char RNN from scratch in F# years ago. I made my own GPU based ML library on order to do that. I do not meet your seniority requirements, but if you want somebody to ingest research papers, build prototypes and turn that into production code I would be a good fit, as I've been doing that for a long time as a hobbyist. My focus was on RL.

If you are willing to extend a junior/mid type of position to somebody like me, I'd be willing to work for a third or even a quarter of your stated salary range. This still wouldn't be a bad salary in Croatia.

Resume: https://docs.google.com/document/d/1D6roVeWFWkwtSfSRr5ac3utd-qSvTtTgBMIbaQ0ZoTo/edit

///

Let me make a move like this. I am not expecting much from this.

9:45am. Now, let me chill a bit. Then I will take a bath. I really want to do some Youtubing today.

11:15am. Done with the bath. Let me have breakfast.

12:05pm. Let me do the chores. Then I will Youtube.

12:45pm. Done with chores.

https://news.ycombinator.com/item?id=34622097
AI Generated Seinfeld runs 24/7 on Twitch (twitch.tv)

> This is probably the first time I've encountered something where "It's so bad that it's good" makes sense to me. I could not stop laughing. The exterior shot with the Seinfeld-inspired music. The laugh track at inappropriate times. They talk about going to a sushi restaurant, and when they've finally agreed to go, they sit down and don't go anywhere. This is like the alien scientists who want to bring back humans after they've gone extinct, and end up cloning chimps. Bravo!

I'll have to check this out.

12:50pm. Ok, focus me. I need to finish working on that Youtube video.

This kind of workflow that I have now is much more pleasant. You can really tell as you ripple delete the video how slower the whole app gets.

Also, instead of backing up the narration here, I bet if I write past the bottom, a scroll bar will show up. It only occured to me during the night.

https://superuser.com/questions/382314/does-rm-rf-follow-symbolic-links

No -f won't go into sym links.

2:45pm. I've really done this in record time. Compared to how I've been doing it previously, it feels like I am flying. Let me just proof this video, create the thumbnail for it, and then I will post it online.

2:55pm. Holy shit, the sound is fucked!

3pm. Ugh, I need to do some audio editing. I need to normalize the volume between the clips.

I need a free solution. Describt, I'd need to pay for, so what else is there?

Let me try it without noise removal.

https://www.youtube.com/results?search_query=reaper+podcast+editing

3:15pm. Proofed it. It works better without noise removal. Noise removal denormalized the volume.

https://youtu.be/jukVjRj-wZ8
REAPER podcast editing tutorial (step-by-step for BEGINNERS)

Let me watch this just for a bit.

https://youtu.be/jukVjRj-wZ8?t=182

Nevermind, I do not feel like doing this. I am a chad and will just post it to Youtube as is.

Oh yeah, I need the thumbnail.

3:30pm.

///

I'll show how to get the actual size later.

For now, let demonstrate that the images we prompted in the last video are in fact there.

Now what I will try is to delete those outputs.

Just using the remove command on a non-empty directory would fail, so it needs the -r flag.

This tells it to remove the files recursively.

In the previous versions of the WebUI setup script, erasing the output directory like I am showing here would have worked.

If you tried this now, the directory would go away, but when you logged into the notebook in the future, you'd notice that the old outputs are still there.

In the file browser, the outputs directory is gone.

But you can see here, that the folder is still present in the WebUI directory.

The remove command that I executed does not recursively erase the content inside the sym links.

For that reason the original files are still there.

In order to properly clean things up, we need to get rid of the original directory.

Here I've been pressing tab to autocomplete.

If I just type in st, it does not work because there are two directories starting with that prefix, but pressing tab again will give me a list of candidates.

Instead of the way around that I've been doing here, another options would have been to add a trailing slash to the original rm command.

Executing the recursive rm command in the terminal with the correct directory as target will remove the old outputs for good.

In the File Browser you need to click on the refresh to see the changes.

Before we end the lecture, I want to show you one more thing.

At the start of this video, I've used the du command. That is an abbreviation for disk usage.

The outputs of it are still there in the terminal. You can see, it does not give the sizes inside the symlinks.

But if you go into the storage directory, and type the command there, you can see sizes exactly.

If instead of that you want the disk usage command to give you the size while taking the contents of sym links into account, pass the big L flag into the du command.

The result you get here might also not be what you have expected.

It is in fact correct. The problem is that it accounts for the Stable Diffusion 1.5 model that we have mounted from Paperspace public datasets.

Check it out. If we unmount the dataset...

...And then try the du command with the big L flag again, we should get the correct size.

With this we are almost done with the educational parts of these lectures.

By now you should know how to setup the notebook, how to grab the GPU instances, how to install the external models, and now how to free up used space.

In the next lecture, I just want to show you how to set up more sensible defaults for the WebUI and how to clean up the script itself.

Armed with that knowledge we will finally be able to prompt properly!

If you've found this video useful, please like and subscribe, it really helps me out.

This has been your favorite Ghost, and I hope to see you soon in the next video!

///

Here is the narration. I never thought of writing a script like this, as I go along.

3:30pm. e: is at 50gb again. I have no choice. I am going to have to erase some of my backed up anime and images that I am never going to watch again. Obsessively collect images from /a/ for no reason, only to never look at it. Later. I'll do that later.

https://youtu.be/04iaKaPqiEE
How To Free Up Used Space On Your Gradient Notebook

Here is my newest video. Let me watch it online.

https://youtu.be/ScsWGAOH0XE
THIS Will Make Any Mic Sound PRO (for FREE)

https://podcast.adobe.com/enhance

Oh, I heard about this, but never tried it.

Let me export the audio and I will give it a try.

3:40pm. It enhanced it. Google's sidebar really came through this time for me.

3:55pm. I've listened to it and it does improve audio quality. The audio clips I've inserted get mangled, but the voice is a lot smoother.

https://youtu.be/432bCAXPx3Q
How To Edit YouTube Videos Without Losing Views! (Replace YouTube Videos, Re-Upload YouTube Videos?)

Let me watch this.

https://youtu.be/432bCAXPx3Q?t=77

It finally gets to the point here.

https://youtu.be/432bCAXPx3Q?t=147

No, nevermind. It seems I have no choice, but to reupload, but to be honest, even though the audio is a bit harsh, it doesn't matter that much. I'll just use Adobe Enhance on my future vids.

4:05pm. Ok, I am finally done with that video. Let me take a short break.

4:15pm. Let me read Baki and Tenken.

4:35pm. That fancy NLP place I aplied to earlier...I just realized, that for the ML places I am applying, I do not have enough ML specific projects on my resume. Whops.

Well, nevermind. The trouble is that I did them all in Spiral, and they are buried in the commits. Let me read manga for a bit, and then I will make another video. I think I should be a lot faster from here on out.

4:40pm. Done with Baki. Let me save Fran for later. Today's chapter cover is uooooh worthy.

Instead, let me make another video. Let me see if I can do it under and hour.

5:25pm. I've only just now finished recording. I got into prompting. Let me shut down the machine.

Now to make the voice over.

9:15pm. I am not even done, just done with part 1. Doing is pretty satisfying. It also keeps my mind off things. I won't post it today.

As the last thing for the day, let me just export the audio to enhance. In fact. Shit. I hadn't realized this, but I really should have gotten rid of those ambient tracks.

...Did it. Now it is processing in Adobe Enhance.

9:30pm. I was too tired to think of it. I've been really pushing it for the past few hours.

9:40pm. Let me stop here for the day. I'll publish the video tomorrow. Now is the time to rest. Tomorrow's interview is bound to end up badly if I try to impress the other side, so I'll just be honest and see where that leads me.

Somehow my new workflow did not make things much faster, but I think my speech skills are improving if slowly. I am not spending all my time doing really basic editing, and I've been in the zone the whole time. I can now boast of having basic familiarity with editing video. Isn't that great? It is certainly not bad.

Well, if all these interviews fail, I might have a future as a Youtuber. Sigh, who can go through this hassle? What does it matter if it fails?

Let me read that Fran chapter."

---
## [redmoogle/OpenDream](https://github.com/redmoogle/OpenDream)@[00d56970e1...](https://github.com/redmoogle/OpenDream/commit/00d56970e117f0ad2e64075381bf6a0db3ddcdbe)
#### Thursday 2023-02-02 20:54:35 by Altoids1

Adds operator~= and proper json_encode()ing for /matrix (#845)

* Creates json_encode() for /matrix, adds it to unit tests

This makes these units tests more descriptive about what happened.

EDIT: Fixes json_encode for /matrix

* Moves operator~= evaluation into MetaObjects

This is to allow future support for overloading this operator with user-defined datums later on.

Also this is more friendly towards users overriding /list or /matrix

* Implements operator~= for /matrix

* Adds True and False getter helpers for DreamValue

Writing this every time was getting kinda cumbersome

I also want to encourage eventually supporting maybe having bools being their own type later, rather than piggybacking on floats all the time.

* Edits Matrix unit tests to use equivalence operator

...Instead of a weird helper stuffed into the test suite that they shouldn't really be using.

Also gets rid of the BOM at the top of these Matrix tests. Silly Windows!

* Wixoa review commit

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[84c7e77a81...](https://github.com/dagster-io/dagster/commit/84c7e77a8170aa11b53ef10fda93bc4b33134b1e)
#### Thursday 2023-02-02 21:45:14 by Ben Gotow

[dagit] Add ErrorBoundary to Dagit to reduce severity of React errors (#11824)

### Summary & Motivation

Corresponding Internal PR:
https://github.com/dagster-io/internal/pull/4659

Hey folks, this PR wraps key components of Dagit in React "error
boundaries", which give us the opportunity to present errors more
gracefully and let users recover / continue to use other parts of the
app. So far I've added them to:

- The top component that renders page content (everything below the
toolbar)
- The details section of the asset partitions and events pages (which
was a production issue yesterday)
- The asset graph and asset graph sidebar
- The op graph and op graph sidebar
- The run logs container and the run gannt chart
- The instance run timeline
- The `<Dialog />` component (errors in a dialog should never take down
the rest of the page)

Anywhere else we should add these?

### Resetting after errors

The component I added takes a `resetErrorOnChange` prop which acts a bit
like a useMemo dependency list -- if any of the values change and it's
in an error state, it resets the error and tries to render it's subtree
again. We need this for cases where the error boundary is not unmounted
/ remounted but it's content could meaningfully change. (eg: you click
another asset or tab). I think this is better than putting a `key={}` on
the Error Boundary because that would force a re-render on the whole
subtree in the happy case.

### Cloud

In cloud dagit, we need to implement a top level context exposed by the
new Error Boundary class in order to send errors (which are now caught)
to DataDog. I think we also want to change the text to let users know
that their errors are automatically submitted to us, so I made that text
configurable. We can also disable the display of the error stack trace
in cloud if we want to.

### How I Tested These Changes

I tested these changes by adding `throw new Error()` to various React
render methods and verifying that Dagit fails more gracefully. I also
verified that this can catch the infinite recursion bug, which is a bit
of an interesting one, by reverting to last night's code and running
without the GraphQL patch.


![image](https://user-images.githubusercontent.com/1037212/213761842-9c01de3e-aa19-40e8-8ea5-2db143684ea6.png)


![image](https://user-images.githubusercontent.com/1037212/213762126-e94f2f8e-1a82-4d71-b624-525533c34d28.png)

Edit: Updated styling

<img width="727" alt="image"
src="https://user-images.githubusercontent.com/1037212/213804637-46343cb0-34de-4154-bd5e-1f61d0a30e92.png">

Co-authored-by: bengotow <bgotow@elementl.com>

---
## [ni/linux](https://github.com/ni/linux)@[2f722caecd...](https://github.com/ni/linux/commit/2f722caecd547353ec47758cc9186567a61b125a)
#### Thursday 2023-02-02 22:58:04 by Karthik Manamcheri

8250: Do not create ttyS* nodes for nonexistant devices

This commit is a merge of two upstream-unfriendly commits:
   commit ba93f2d13b34 ("8250: Make SERIAL_8250_RUNTIME_UARTS work correctly")
   commit 0d1ed2d7adc1 ("Revert "serial: 8250: Do nothing if nr_uarts=0"")

This was an attempt to resolve an architectural oddity in the 8250 core
code, which was that, by design, it will create a static (build- or
cmdline-specified) number of ttyS* devices, which is at odds with how
most other Linux kernel drivers work. The original commit messages did
not accurately describe the problem, so this is a merge-and-replace in
order to get a better commit description. So, without further ado:

The current state of affairs is as follows:

There exists two build-time constants.
   - CONFIG_SERIAL_8250_NR_UARTS: the build-time max number of 8250 UARTs.
   - CONFIG_SERIAL_8250_RUNTIME_UARTS: the boot-time number of 8250 UARTs.
        (confusingly, this is also the default setting of 8250.nr_uarts)

The way that the 8250 driver handles creation of ttyS* device is that, at
initialize time, we create min(8250.nr_uarts, NR_UARTS) ttyS* devices
up-front, and when a UART is registered, serial8250_find_match_or_unused
will either merge it in under an existing ttyS* or find an unused one.

There also exists code in the 8250 driver to automatically enumerate the
UARTs specified in the SERIAL_PORT_DFNS table; these are the "well-known"
ports at 0x3F8/0x2F8/0x3E8/0x2E8 from the IBM PC platform, and they are
added this way because they predate the use of ACPI tables for enumeration.

(Oh, and also you can point the ttyS* devices to completely different
addresses from userspace via TIOCSSERIAL.)

This has two ramifications for NI devices:

1) There is a limit on number of UARTs with 8250_core; this is a noteworthy
   problem when you are also a vendor of multiport serial cards, such as
   the PXIe-8430/16. However, the user experience of increasing the limit
   with a generic platform kernel is also bad; if, as a distro, we release
   a kernel with a default limit of 128, then users that have PXI systems
   that don't have any multiport serial cards will still be presented with
   devices named ttyS0 through ttyS127, even though most of them are just
   "empty" slots that are not backed by real devices.

2) ttyS0 through ttyS3 will always be given the addresses for the "legacy"
   serial ports, even if on-board controller ports are at different
   addresses. This is the case on several NI controllers; for example, on
   some sbRIO products [1] the UARTs are at 0x3F8, 0x350, 0x360, etc.
   However, because the legacy ports get first-dibs, those ports will be
   ttyS0, ttyS4, ttyS5, ... because the legacy 0x2f8/0x3E8/0x2E8 get S1-S3.

Our initial attempt at resolving this was to redefine 8250.nr_uarts to mean
"the number of automatically-created UART entries" and define it to be 0
(because we neither want the legacy ports nor the extra "empty" ports). On
NI platforms, all serial ports are described in the ACPI table, so legacy
enumeration is neither necessary nor desirable. However, this approach got
soundly rejected upstream because it "caused existing kernel configurations
to act differently from before" [2].

We're not alone in finding the upstream behavior to be counterintuitive;
I have found at least two other attempts [3, 4] to resolve it with similar
pushback of the form "this breaks existing users".

A "proper" upstreamable solution probably needs two parts, with the default
settings such that the current behavior is retained but can be opted-out
(via Kconfig and/or kernel cmdline).
- a config token for "don't create a bunch of empty devices" (1)
- a config token for "don't add legacy ports, let ACPI handle it" (2)

Until that arrives, we're stuck keeping this around, because we're _also_
stuck with not wanting to renumber ttyS* devices from the way we've shipped
them.

[1] https://github.com/ni/meta-nilrt/blob/8106f31da6980ee4ee94fa0e03b991479d9aa43e/recipes-kernel/kernel-tests/kernel-tests-files/test_kernel_serial_devices.sh#L127
[2] https://lore.kernel.org/lkml/20130603213754.GA15479@kroah.com/
[3] https://lore.kernel.org/linux-serial/1420513785-23660-1-git-send-email-peter@hurleysoftware.com/
[4] https://lore.kernel.org/linux-serial/20221025073944.102437-1-martin@geanix.com/

[SBOs from initial patches]
Natinst-CAR-ID: 634278
Signed-off-by: Karthik Manamcheri <karthik.manamcheri@ni.com>
Signed-off-by: Richard Tollerton <rich.tollerton@ni.com>
Signed-off-by: Brad Mouring <brad.mouring@ni.com>
Natinst-ReviewBoard-ID: 183619

Upstream-Status: Denied [rejected upstream]
Natinst-AzDO-ID: 2133864
Signed-off-by: Brenda Streiff <brenda.streiff@ni.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4ce115a2a2...](https://github.com/cmss13-devs/cmss13/commit/4ce115a2a26f8b6664a230bdaff483a1889f17c4)
#### Thursday 2023-02-02 23:01:22 by carlarctg

Adds Ludicrously In-Depth Black Market to Recquisitions. (#2014)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

Various valuable, rare, or otherwise interesting items now have a 'black
market value' that allows them to be sent down the ASRS elevator in
exchange for black market points to order various things with. Anything
that's 'rare' is probably worth something. Added a scanner to the black
market to let them detect said points.

Added DIALOGUE to the black market.

FIxed some construction wirecutter steps needing a screwdriver for some
reason.

Changed up Req's mapping to add a hidden storage room.

slightly changed human remains' description

Added the maintenance jack, can be found in the black market for now.

Improved supply shuttle code somewhat.

# Explain why it's good for the game

> VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Black Market is comically underused, by comically enhancing it like this
it will freshen shipside roleplay and create new and interesting
scenarios for MPs, req, and bystanders to interact with.

> Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

The contraband needs to be actually meaningful to the players for it to
have any impact. The list of loot has been curated so that players will
be intrigued, but will not be able to abuse it for
too-stronger-than-usual gear without blatant drawbacks.

> Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with. Added
a scanner to the black market to let them detect said points.

This means CTs could go on scavenger hunts through the ship, evading
curious MPs to sift through maintenance and various hidey holes scanning
everything.

> Added DIALOGUE to the black market.

Finally, we have dialogue in CM! The very first human NPC. We're
ignoring WO because nobody likes WO.

> FIxed some construction wirecutter steps needing a screwdriver for
some reason.

Necessary in this PR to avoid stupid confusion when deconstructing the
computers.

> Changed up Req's mapping to add a hidden storage room.

To let CTs hide their goodies so they won't be in open sight. NOT DONE
YET!

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: VASTLY enhances the Black Market. Black market items are obtainable
by deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.
add: Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...
add: Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with.
Anything that's 'rare' is probably worth something. Added a scanner to
the black market to let them detect said points.
add: Added DIALOGUE to the black market.
fix: FIxed some construction wirecutter steps needing a screwdriver for
some reason.
spellcheck: slightly changed human remains' description
add: Added the maintenance jack, can be found in the black market for
now.
code: Improved supply shuttle code somewhat.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: XSlayer300 <35091844+XSlayer300@users.noreply.github.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---

