## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-24](docs/good-messages/2023/2023-02-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,185,228 were push events containing 3,356,670 commit messages that amount to 247,979,066 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [tra-ins/trains](https://github.com/tra-ins/trains)@[bd24c1da8d...](https://github.com/tra-ins/trains/commit/bd24c1da8d5d47e9566628fde00bcba040823ff8)
#### Friday 2023-02-24 00:05:11 by tra-ins

ap world history? uh yeah, i sure hope it does! criminal justice program of study people rise up!!!

oh yeah im crushing on some girl in my class btw. i dont even talk to her i just think shes cute and funny. is this confirmation that im not straight??

---
## [linyinfeng/dotfiles](https://github.com/linyinfeng/dotfiles)@[153780cbfc...](https://github.com/linyinfeng/dotfiles/commit/153780cbfcac324c87a7fbc2e0eed4559ebc8f4f)
#### Friday 2023-02-24 02:36:51 by Lin Yinfeng

Oracle, Fuck You

Oracle Cloud just disabled my free account *without any notice*, and
*does not provide any data recovery method*.

Remove all Oracle OCI state from terraform.  Deploy all services
previously on the Oracle Ampere A1 machine to rica.

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[66b7310039...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Friday 2023-02-24 02:38:39 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [vijaydasmp/dash](https://github.com/vijaydasmp/dash)@[aec7441ac2...](https://github.com/vijaydasmp/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Friday 2023-02-24 04:22:44 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [JasmineD500/My-Chromatics](https://github.com/JasmineD500/My-Chromatics)@[5d57617c59...](https://github.com/JasmineD500/My-Chromatics/commit/5d57617c590566f2b5dbf156acfc73266e740f95)
#### Friday 2023-02-24 05:01:03 by Jasmine D

i hate my life

why they replace me with some baddies mod

---
## [erikarn/wtf-os](https://github.com/erikarn/wtf-os)@[94b57c5821...](https://github.com/erikarn/wtf-os/commit/94b57c5821332dc58dfa316bc2f7afce2b42b20a)
#### Friday 2023-02-24 05:07:56 by Adrian Chadd

[wtfos] lots of little bits for PIC userland task creation.

Which, fuck me, actually worked.  Yeah MPU setup isn't working yet
because the memory allocations and alignment requirements suck,
but i /am loading a task and running it/ for the love of god that
is great.

Anyway:

* add in arg and r9 parameters into the user task create func
* and make sure we populate arg for the kern task create func
* add some debugging during task creation because yes I need it
* populate r9 in the stack frame setup rather than skipping over
  it, as it's required for the PIC user stuff.

* finish parsing, memory allocation and setting up the task
  and running it.

Now, this actually surprisingly works.  Holy shit etc.

---
## [linyinfeng/blog](https://github.com/linyinfeng/blog)@[cbc29cbfd9...](https://github.com/linyinfeng/blog/commit/cbc29cbfd9ee7eafddfb85720d9a1f9bb9b6b27c)
#### Friday 2023-02-24 05:33:18 by ImgBotApp

[ImgBot] Optimize images

/content/posts/oracle-fuck-you/instances-page.png -- 183.02kb -> 150.75kb (17.63%)

Signed-off-by: ImgBotApp <ImgBotHelp@gmail.com>

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[ff1d1295aa...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/ff1d1295aa7fc76e6519131e959079e81daa21fb)
#### Friday 2023-02-24 09:32:37 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217981
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Friday 2023-02-24 10:55:43 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [readmeio/metrics-sdks](https://github.com/readmeio/metrics-sdks)@[42f074625b...](https://github.com/readmeio/metrics-sdks/commit/42f074625b81cd73dc2766afa25760c88f5c1894)
#### Friday 2023-02-24 11:47:54 by Dom Harrington

fix: remove `HAS_HTTP_QUIRKS` flag from integration tests

OK here's where this PR gets interesting... I spent a bunch of time debugging
the test failures here: https://github.com/readmeio/metrics-sdks/pull/653#pullrequestreview-1309362560

I eventually settled on some code that was working, committed here:
224e2ad54c9bef641db39e650bfdc464a55c929b

But that was causing a bunch of `EOFErrors` from Ruby when sending the
HTTP request out to the metrics server:

```
#<Thread:0x000000010c67e488 /Users/domh/Sites/readmeio/metrics-sdks/packages/ruby/lib/readme/request_queue.rb:30 run> terminated with exception (report_on_exception is true):
/opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:227:in `rbuf_fill': end of file reached (EOFError)
	from /opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:193:in `readuntil'
<long stack trace omitted>
```

It turns out that this wasn't a problem on the Ruby side, but in fact a
problem from the Node.js testing side, because when not in "quirks" mode
our fake metrics server happily accepted requests but just ignored them
and never responded to anything.

https://github.com/readmeio/metrics-sdks/blob/7728160f522847b9a59ce7a565eca35610c6e015/test/integration-metrics.test.js#L88-L113

Some languages are okay with this (node, PHP) and some are not okay with
this (python, and Ruby with rack@3.0.0 evidently).

Since it is kinda janky for us to create an HTTP server and just ignore
everything and not respond with anything, I've opted to make the quirks
behaviour the default with this PR! This seems to work for all languages
I've tested locally but lets see if it passes for all of them on CI 🤞

I also had to add another fix here where the body was being returned empty
to the test because the HTTP request from Ruby wasn't complete yet, so if
we hit this race condition, I've opted to just sleep for 300ms and try again.
Using this property:

https://nodejs.org/docs/latest/api/http.html#messagecomplete

Oh don't you just love HTTP.

---
## [dvjromashkin/noble-networks](https://github.com/dvjromashkin/noble-networks)@[b5ea1b6a56...](https://github.com/dvjromashkin/noble-networks/commit/b5ea1b6a5604bb8651ee88e30c26bb53b0f7658a)
#### Friday 2023-02-24 12:08:46 by Roman Shaulskyi

Gentx Cryptech

Greetings. Found your project on Twitter. I represent the Cryptech team. We would like to support your project with our infrastructure. We have our own data centre located in Ukraine. I saw that you are communicating with the project on telegram, add me to your telegram group: My telegram: @LifeHah
Our project website: https://cryptech.com.ua
I would also like to tell you more about us:

Good afternoon, I want to introduce you our small team of 6 people. 
Our dream team:
Denis - Team Leader, Blockchain Expert
Daria - Marketing Advisor
Taras - Computer Systems Engineer
Roman - DevOps, Network Engineer
Ivan - DevOps, Cryptography Specialist
Oleksii - Community Manager, DevOps

We are enthusiasts who believe that very soon blockchain technologies will become an integral part of the life of an ordinary person. We are specialists in the field of system administration and have extensive experience in setting up and maintaining decentralized nodes of various networks.  Here are some of them: ALEO, Ironfish, Solana-TestNet, Neon-LAbs, Minima, KYVE, Asset Mantle, Game, Cosmic Horizon, KleverChain, TGRADE, Celestia, Archway, QUAI Network, APTOS, Penumbra, STARKNET, SUI, GNOLang, Sei, QuickSilver, OBOL, LAYER ZERO, Web3Auth, DWEB, Oasys, Algoracle, Covalent, Abacus, peaq, Crescent, DeFund, Laconic, Subspace, Gitopia, Massa, Kira, ANOMA, Humanode, ChainFlip, Masa Finance, Manta-Kalamari, GEAR, Supra Oracle, Cere Network, Secret Networt, MoonBeam, Ki-Chain, KOII, Spacemesh, Stargaze, BlockPI and many others. 

Our team has many years of experience in network infrastructure, setting up and maintaining client servers based on Linux (Debian, Ubuntu, CentOS, etс.), creting monitoring and warning systems (Prometheus, Zabbix, Nagois, Grafana), writing and compiling Dockerfiles (above 4 years experience), writing scripts and programs in languages   (Python, Bash, PowerShell), knows programming languages such as RUST, Go, Javascript, which allows us to fully participate in projects based on CosmosSDK, Ethereum, Polkadot, ZK-snark, work with Bridges, and Blockchain Relays. We carry out full-fledged work with Github and search for Bugs, make various kinds of Feedbacks (bugreports, etc.)

Since we are located in Ukraine, in the city of Dnipro (one of the largest cities in Ukraine with a population of 1 million citizens), we send most of the resources received from activities to support state institutions, volunteer work and support the Armed Forces of Ukraine. Of course, we are interested in financial support from the world community. And in exchange for this support, we want to provide our computing power and our experience in supporting and configuring decentralized nodes of various networks to support crypto projects. We want to ask you to support us and our country in this difficult time, just as our large Ukrainian community has been supporting and helping you for a long time. Do not stand aside and be on guard for world peace. Thank you for understanding and supporting us in the person of Ukrainian volunteers.

For our part, we provide comprehensive assistance and support to development teams - we deploy and maintain nodes of their decentralized networks on our equipment, we conduct functional testing and search for bugs. We also promote projects and create educational content that reveals projects in simple terms from the technical, conceptual and practical sides. We write articles, translate blogs and technical documentation, create video materials in the form of short promos and lectures about projects (mostly in Russian, but we can do it in English). You can see our content and working projects at the links below: 

http://cryptech.com.ua/
https://cryptech-nodes.medium.com/
https://www.youtube.com/channel/UCGwQIwKu1QuB9YxW-vElNbQ
https://www.twitch.tv/projectcryptech (The last broadcast was quite a while ago because our speaker was ill, but we will be back to this activity soon)

We do not rent cloud servers, we purchased, configured and maintain all the capacities on our own.
We have created our own data center and work with the following equipment:
HPE Proliant DL580 Gen9 Server Quad 24-Core E7-8894 v4 **96 Cores 512GB RAM, 8 x Intel P3520 Series 2 TB SSD
4 x HP GEN 9, CPU - 2 x Intel Xeon E-4667 v3, RAM - DDR-4 368 GB, SSD - 4 x Intel P3520 Series 2 TB
4 x Quanta - 2 x Intel (R) Xeon (R) CPU E5-2699 v3 @ 2.30GHz, RAM - DDR-4 368 GB, SSD - 4 x Intel P3520 Series 2 TB
2 x Gigabyte 1U - 2 x Intel (R) Xeon (R) CPU E5-2699 v3 @ 2.30GHz, RAM - DDR-4 256 GB, SSD - 4 x Intel P3520 Series 2 TB
2 x SuperMicro with SGX processors Intel Xeon E2278G, RAM - DDR-4 128 GB, 3 x Intel P3520 Series 2 TB
We get the Internet from three backbone providers in our country: Eurotranstelecom, Vega Telecom, DataLine. We have our own autonomous system and communication channels with a speed of 1 Gigabit / s each and a backup power supply system, which allows our data center to work without interruptions 24/7 with 1000% uptime.

For the last 4 years we have been working in the blockchain industry and participating in a large number of full-time projects. Before that, we were involved in various projects and various branches of the IT industry. BUT gradually we became interested in blockchains, and our hobby became our main occupation.
Our contacts:
https://twitter.com/CryptechNodes
https://github.com/dvjromashkin
cryptech.nodes@gmail.com

---
## [Signal-K/client](https://github.com/Signal-K/client)@[69497a1500...](https://github.com/Signal-K/client/commit/69497a1500e3ec2237555d07581ab4cd40880de2)
#### Friday 2023-02-24 12:29:22 by Liam Arbuckle

🪁🥎 ↝ #8 Add file upload feature & auth handler

1. Completed authentication header for web client. To the end user it is 100% offchain, with user profiles being stored on a postgresql database. However, I've taken a dive into the Magic sdk to create wallet addresses for each user, as well as a Flask-based authentication handler for future metamask/wallet interaction. I've made this decision for a few reasons (like simplicity), but the main reason is for the client to seem like a regular journal platform and not be confusing, as well as follow the 'web3-agnostic' design language I favour for projects like this due to confusion and/or distrust of web3 products/teams. However, since each user will have a wallet address, they'll be able to interact with smart contracts and IPFS just fine. Further discussion will need to take place to discuss long-term suitability of this model, including things like gas fees (currently everything regarding transactions is occurring on Goerli [testnet] and gas fees will be processed by a "superuser" so that there's no restrictions or huge expenses) and how we go about getting users to trust the web3 nature (which I've got a lot of experience with). However, I don't fully know the exact demographics we'll be targeting & also I understand that that's quite a while away, so I'll raise it now but won't spend any time thinking about it until the time comes
          2. I've continued with the contracts for proposals/publications & updating the metadata standards. I favour a lazy minting approach with data processing being handled by a Flask blueprint (which is a formula my team have developed on signal-k/sytizen). Right now I'm using Thirdweb & Moralis for the contract interactions and I have also, with much difficulty, succeeded in getting Moralis to self-host on my Postgres server. Finally, I've begun the process of optimising the base layer contracts so that the gas fees (which are already reduced post-merge) are essentially negligible at this time.
          3. File upload for posts/articles feature on the web client is complete, and the smart contracts now receive all file upload metadata from this.
          4. Begun a new flask blueprint (forked from point #2) to generate dataset previews based on which modules (e.g. lightkurve) are used and to add interactive nature to the 'sandbox' feature discussed earlier
          5. Reluctantly continued some documentation

(above message from the Desci discord, see https://github.com/signal-k/sytizen/issues/16 for more info)

---
## [VastKilleroOm/TG220VAST](https://github.com/VastKilleroOm/TG220VAST)@[a2295b2b04...](https://github.com/VastKilleroOm/TG220VAST/commit/a2295b2b049ba3c77186ffb0eaacb507c001cdc8)
#### Friday 2023-02-24 12:34:45 by LemonInTheDark

Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode. 
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible. 
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[6d158bd3b3...](https://github.com/Latentish/Shiptest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Friday 2023-02-24 13:42:57 by spockye

beach ruin, The Treasure Cove! (#1701)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a new Beach ruin, Treasure Cove. 

![2023 01 17-11 26
30](https://user-images.githubusercontent.com/79304582/212874736-b17917a5-876e-4a7a-a073-1581cc394b8e.png)

![2023 01 17-11 26
58](https://user-images.githubusercontent.com/79304582/212874824-9a161419-b751-41d2-a82d-e50f06981025.png)


![image](https://user-images.githubusercontent.com/79304582/212879021-bcdc2238-b50b-48c2-9cd0-d17cccbd50dc.png)

Loot: 
cm-16 rifle (main loot)
energy gun
pirate sabre
frontiersmen hardsuit
misc combat supplies
secret documents
2x abandoned crates
research note / tesla researcher
basic engineering supplies (smes/tools/autolathe/battery charger)
two boats
silver crate / hidden gold crate
misc junk
______
Threat: 
1x spacesuit ranged pirate
2x sword pirates
1x ranged pirate
punji sticks
_____

Lore tidbit:
This "humble abode" is the home of our 5- now 4 Pirate friends! After a
mildly successful raid on a CMM VIP transport, they managed to take a
Cargo tech (the VIP), and a CMM guard as hostage. sadly it didn't all go
as planned, and the CMM officer managed to free himself and killed one
of the pirates. This is where you now find the cave, with both hostages
executed, their brother buried, and the pirates grieving his unfortunate
passing.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
more ruins = good.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new beach ruin, the beach_treasure_cove
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[84a2a8f394...](https://github.com/BarteG44/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Friday 2023-02-24 13:44:13 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [edsavage/ml-cpp](https://github.com/edsavage/ml-cpp)@[4bc55b3d04...](https://github.com/edsavage/ml-cpp/commit/4bc55b3d04ebf5f2341ad75106e67ec3a7a3d3d9)
#### Friday 2023-02-24 13:53:01 by Tom Veasey

[ML] Logging enhancements plus compilation speed ups  (#2363)

Currently, logging requires one to manage wrapping up calls to many types in core::CContainerPrinter::print.
It would be nice if the logging experience was more streamlined. Another side effect is we ended up including
core/CContainerPrinter.h very widely, in many cases for LOG_TRACE statements which are compiled away
anyway. It would be nice to avoid this.

This PR introduces a pseudo stream manipulator CScopePrintContainers. This is dropped into our logging
macros so that all log lines simply get containers printed automatically. This approach first detects (at compile
time) whether types can be written directly to a std::ostream and uses this approach in preference. I also fixed
some obvious silly inefficiencies in CContainerPrinter. One might ask why not just specialise operator<< for
std::ostream and containers in the std namespace? I did in fact try this, but it turns out other libraries tend
to do this and you can easily get ODR violations. I hit this exact problem because libtorch does this and I
couldn't then compile pytorch_inference.

Separately, our compile times given the total LOC are rather long. One culprit is logging. Just including
CLogger.h adds around 70k lines to the output of the preprocessor and, for my setup, 0.4s for this step
alone to the compile time of file. Therefore, I've also started addressing some of the bottlenecks. I've migrated
LOG_TRACE to really discard the code altogether. This means we can have a special CLoggerTrace.h which
only optionally includes CLogger.h if we're not compiling with EXCLUDE_TRACE_LOGGING. (I think the
improved build times warrant only finding out later if we break a log line and anyway many things now just
print automatically, so this should be harder to do.) I also add CMemoryFwd.h to avoid including CMemory.h
too widely. This includes a lot of STL headers. Finally, I migrated CLoggerThrottler to a pimpl and moved
some obvious other details out of headers. The upshot for for my dev setup is 15% speed up to build everything.

---
## [neurodebian/Psychtoolbox-3](https://github.com/neurodebian/Psychtoolbox-3)@[b85250b062...](https://github.com/neurodebian/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Friday 2023-02-24 14:17:48 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [neurodebian/Psychtoolbox-3](https://github.com/neurodebian/Psychtoolbox-3)@[9354870474...](https://github.com/neurodebian/Psychtoolbox-3/commit/9354870474eaff17302039fc07d6248c9ee5bace)
#### Friday 2023-02-24 14:17:48 by Mario Kleiner

PsychHID/OSX: Improve macOS security troubleshooting instructions.

Sometimes macOS shitty security GUI lies about the permission status
of "Input Monitoring" etc., and displays Matlab/Octave/Terminal as
on the list and checked, and one does need to do more stupid stuff
like unchecking or rechecking the checkbox. Add comments regarding
this.

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[ec45215541...](https://github.com/DataDog/dd-trace-rb/commit/ec452155411cbd1efa5d19331cd0c64ba8d48b1e)
#### Friday 2023-02-24 14:35:13 by Ivo Anjo

Remove Sorbet typechecker

**What does this PR do?**:

This PR is spiritually a revert of #1607, when we added the Sorbet
typechecker to dd-trace-rb.

It includes two commits: One where we remove all configuration
and scaffolding surrounding Sorbet, and one where we remove all of the
`# typed: ...` magic comments and `include Kernel` definitions added
to make Sorbet happy.

**Motivation**:

As documented in #2641, the team has decided that the value vs pain
equation for Sorbet has shifted in the past months, and thus that
it was time to remove Sorbet.

**Additional Notes**:

Sorbet type checking in CI was actually removed earlier this week in
 #2617.

**How to test the change?**:

CI should still be green.

---
## [M3IY0U/aniguess](https://github.com/M3IY0U/aniguess)@[2a821afa19...](https://github.com/M3IY0U/aniguess/commit/2a821afa19729f6517d2940cea06474ef3479c11)
#### Friday 2023-02-24 14:48:59 by Sebastian Zill

Stats restyling (#10)

* Stats restyling

* Oopsie Woopsie! We made a fucky wucky!!

I am vewy sawwy about cwashing ;;w;; I had a pwoblem that caused a headache, so I took a nyappy-nyappy. Pwease forgive me onyi-chan

* damn this guys formatter sucks ass

---------

Co-authored-by: Timo <meiyou@posteo.de>

---
## [qemu/qemu](https://github.com/qemu/qemu)@[8d0efbcfa0...](https://github.com/qemu/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Friday 2023-02-24 15:07:11 by Paolo Bonzini

docs: build-platforms: refine requirements on Python build dependencies

Historically, the critical dependency for both building and running
QEMU has been the distro packages.  Because QEMU is written in C and C's
package management has been tied to distros (at least if you do not want
to bundle libraries with the binary, otherwise I suppose you could use
something like conda or wrapdb), C dependencies of QEMU would target the
version that is shipped in relatively old but still commonly used distros.

For non-C libraries, however, the situation is different, as these
languages have their own package management tool (cpan, pip, gem, npm,
and so on).  For some of these languages, the amount of dependencies
for even a simple program can easily balloon to the point that many
distros have given up on packaging non-C code.  For this reason, it has
become increasingly normal for developers to download dependencies into
a self-contained local environment, instead of relying on distro packages.

Fortunately, this affects QEMU only at build time, as qemu.git does
not package non-C artifacts such as the qemu.qmp package; but still,
as we make more use of Python, we experience a clash between a support
policy that is written for the C world, and dependencies (both direct
and indirect) that increasingly do not care for the distro versions
and are quick at moving past Python runtime versions that are declared
end-of-life.

For example, Python 3.6 has been EOL'd since December 2021 and Meson 0.62
(released the following March) already dropped support for it.  Yet,
Python 3.6 is the default version of the Python runtime for RHEL/CentOS
8 and SLE 15, respectively the penultimate and the most recent version
of two distros that QEMU would like to support.  (It is also the version
used by Ubuntu 18.04, but QEMU stopped supporting it in April 2022).

There are good reasons to move forward with the deprecation of Python
3.6 in QEMU as well: completing the configure->meson switch (which
requires Meson 0.63), and making the QAPI generator fully typed (which
requires newer versions of not just mypy but also Python, due to PEP563).

Fortunately, these long-term support distros do include newer versions of
the Python runtime.  However, these more recent runtimes only come with
a very small subset of the Python packages that the distro includes.
Because most dependencies are optional tests (avocado, mypy, flake8)
and Meson is bundled with QEMU, the most noticeably missing package is
Sphinx (and the readthedocs theme).  There are four possibilities:

* we change the support policy and stop supporting CentOS 8 and SLE 15;
  not a good idea since CentOS 8 is not an unreasonable distro for us to
  want to continue to support

* we keep supporting Python 3.6 until CentOS 8 and SLE 15 stop being
  supported.  This is a possibility---but we may want to revise the support
  policy anyway because SLE 16 has not even been released, so this would
  mean delaying those desirable reasons for perhaps three years;

* we support Python 3.6 just for building documentation, i.e. we are
  careful not to use Python 3.7+ features in our Sphinx extensions but are
  free to use them elsewhere.  Besides being more complicated to understand
  for developers, this can be quite limiting; parts of the QAPI generator
  run at sphinx-build time, which would exclude one of the areas which
  would benefit from a newer version of the runtime;

* we only support Python 3.7+, which means CentOS 8 CI and users
  have to either install Sphinx from pip or disable documentation.

This proposed update to the support policy chooses the last of these
possibilities.  It does by modifying three aspects of the support
policy:

* it introduces different support periods for *native* vs. *non-native*
  dependencies.  Non-native dependencies are currently Python ones only,
  and for simplicity the policy only mentions Python; however, the concept
  generalizes to other languages with a well-known upstream package
  manager, that users of older distributions can fetch dependencies from;

* it opens up the possibility of taking non-native dependencies from their
  own package index instead of using the version in the distribution.  The
  wording right now is specific to dependencies that are only required at
  build time.  In the future we may have to refine it if, for example, parts
  of QEMU will be written in Rust; in that case, crates would be handled
  in a similar way to submodules and vendored in the release tarballs.

* it mentions specifically that optional build dependencies are excluded
  from the platform policy.  Tools such as mypy don't affect the ability
  to build QEMU and move fast enough that distros cannot standardize on
  a single version of them (for example RHEL9 does not package them at
  all, nor does it run them at rpmbuild time).  In other cases, such as
  cross compilers, we have alternatives.

Right now, non-native dependencies have to be download manually by
running "pip" before "configure".  In the future, it will be desirable
for configure to set up a virtual environment and download them in the
same way that it populates git submodules (but, in this case, without
vendoring them in the release tarballs).

Just like with submodules, this would make things easier for people
that can afford accessing the network in their build environment; the
option to populate the build environment manually would remain for
people whose build machines lack network access.  The change to the
support policy neither requires nor forbids this future change.

[Thanks to Daniel P. Berrangé, Peter Maydell and others for discussions
 that were copied or summarized in the above commit message]

Cc: Markus Armbruster <armbru@redhat.com>
Cc: Peter Maydell <peter.maydell@linaro.org>
Cc: John Snow <jsnow@redhat.com>
Cc: Kevin Wolf <kwolf@redhat.com>
Reviewed-by: Daniel P. Berrangé <berrange@redhat.com>
Reviewed-by: Alex Bennée <alex.bennee@linaro.org>
Signed-off-by: Paolo Bonzini <pbonzini@redhat.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[d21740b475...](https://github.com/shiptest-ss13/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Friday 2023-02-24 15:09:20 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [salonized/dd-trace-rb](https://github.com/salonized/dd-trace-rb)@[eeabe537a2...](https://github.com/salonized/dd-trace-rb/commit/eeabe537a29191ea3aeb3086c9aa8b91c958c0f3)
#### Friday 2023-02-24 15:37:17 by Ivo Anjo

Second step of making some sample values optional: make StackRecorder configurable

In the previous commit the `sample_values` struct was introduced, which
abstracted how values are passed to libdatadog away from everywhere
else in the profiler, and centralized this into the `StackRecorder`.

In this commit, I reimplemented the `record_sample` function to,
instead of using a hardcoded position for every value type, rely
on two extra indirections:
* `state->position_for`
* `state->enabled_values_count`

By default (e.g. when all profile types are enabled), this new
strategy behaves exactly as before.

The interesting thing happens when some profile types are disabled
(via the constructor). When profile types are disabled,
the two indirections above are reconfigured: `enabled_values_count`
becomes less than `ALL_VALUE_TYPES_COUNT`, and `position_for` is
updated to account for this as well.

In pratice, the `position_for` array is treated as if it was a
hashmap -- the key is a given profile type, and the value is the
position that libdatadog is expected it to be written to.

Thus, converting a `sample_values` to an array for libdatadog
is as simple as

```c
  metric_values[position_for[CPU_TIME_VALUE_ID]]      = values.cpu_time_ns;
  metric_values[position_for[CPU_SAMPLES_VALUE_ID]]   = values.cpu_samples;
  metric_values[position_for[WALL_TIME_VALUE_ID]]     = values.wall_time_ns;
  metric_values[position_for[ALLOC_SAMPLES_VALUE_ID]] = values.alloc_samples;
```

The trick here, is that when certain profile_types are disabled
their `position_for` is changed, so they are put at the end of the
`metric_values` array.

For instance, when we disable both `CPU_TIME_VALUE` and
`ALLOC_SAMPLES_VALUE` the `position_for` "hashmap" will look something
like

```ruby
{
  CPU_SAMPLES_VALUE_ID: 0,
  WALL_TIME_VALUE_ID: 1,
  CPU_TIME_VALUE_ID: 2,
  ALLOC_SAMPLES_VALUE_ID: 3,
}
```

And thus, given

```ruby
{ 'cpu-time' => 123, 'cpu-samples' => 456, 'wall-time' => 789, 'alloc-samples' => 4242 }
```

We will produce a `metrics_values` array with

```
+-----+-----+-----+------+
| 456 | 789 | 123 | 4242 |
+-----+-----+-----+------+
```

...but we'll tell libdatadog to only use the first 2 positions of
the array, which contain the values for the enabled profile types!

To be honest, this was more boilerplate than I wanted, but I'm happy
that most of the complexity lies in `_native_initialize` around the
creation of `position_for` and the values list for libdatadog, and
everywhere else still looks kinda sane.

---
## [AdelinFnk/codewars](https://github.com/AdelinFnk/codewars)@[7ac3533a75...](https://github.com/AdelinFnk/codewars/commit/7ac3533a75d0defed64465ea3f22453352f98ba3)
#### Friday 2023-02-24 15:40:25 by Adelin

"When you arise in the morning, think of what a precious privilege it is to be alive – to breathe, to think, to enjoy, to love."- Marcus Aurelius

---
## [delphix/linux-kernel-aws](https://github.com/delphix/linux-kernel-aws)@[9bd96fdf28...](https://github.com/delphix/linux-kernel-aws/commit/9bd96fdf28450ec3266fad2e5a183c63fa646dfe)
#### Friday 2023-02-24 16:18:12 by Masahiro Yamada

kbuild: remove the target in signal traps when interrupted

BugLink: https://bugs.launchpad.net/bugs/1996812

[ Upstream commit a7f3257da8a86b96fb9bf1bba40ae0bbd7f1885a ]

When receiving some signal, GNU Make automatically deletes the target if
it has already been changed by the interrupted recipe.

If the target is possibly incomplete due to interruption, it must be
deleted so that it will be remade from scratch on the next run of make.
Otherwise, the target would remain corrupted permanently because its
timestamp had already been updated.

Thanks to this behavior of Make, you can stop the build any time by
pressing Ctrl-C, and just run 'make' to resume it.

Kbuild also relies on this feature, but it is equivalently important
for any build systems that make decisions based on timestamps (if you
want to support Ctrl-C reliably).

However, this does not always work as claimed; Make immediately dies
with Ctrl-C if its stderr goes into a pipe.

  [Test Makefile]

    foo:
            echo hello > $@
            sleep 3
            echo world >> $@

  [Test Result]

    $ make                         # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^Cmake: *** Deleting file 'foo'
    make: *** [Makefile:3: foo] Interrupt

    $ make 2>&1 | cat              # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^C$                            # 'foo' is often left-over

The reason is because SIGINT is sent to the entire process group.
In this example, SIGINT kills 'cat', and 'make' writes the message to
the closed pipe, then dies with SIGPIPE before cleaning the target.

A typical bad scenario (as reported by [1], [2]) is to save build log
by using the 'tee' command:

    $ make 2>&1 | tee log

This can be problematic for any build systems based on Make, so I hope
it will be fixed in GNU Make. The maintainer of GNU Make stated this is
a long-standing issue and difficult to fix [3]. It has not been fixed
yet as of writing.

So, we cannot rely on Make cleaning the target. We can do it by
ourselves, in signal traps.

As far as I understand, Make takes care of SIGHUP, SIGINT, SIGQUIT, and
SITERM for the target removal. I added the traps for them, and also for
SIGPIPE just in case cmd_* rule prints something to stdout or stderr
(but I did not observe an actual case where SIGPIPE was triggered).

[Note 1]

The trap handler might be worth explaining.

    rm -f $@; trap - $(sig); kill -s $(sig) $$

This lets the shell kill itself by the signal it caught, so the parent
process can tell the child has exited on the signal. Generally, this is
a proper manner for handling signals, in case the calling program (like
Bash) may monitor WIFSIGNALED() and WTERMSIG() for WCE although this may
not be a big deal here because GNU Make handles SIGHUP, SIGINT, SIGQUIT
in WUE and SIGTERM in IUE.

  IUE - Immediate Unconditional Exit
  WUE - Wait and Unconditional Exit
  WCE - Wait and Cooperative Exit

For details, see "Proper handling of SIGINT/SIGQUIT" [4].

[Note 2]

Reverting 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd
files") would directly address [1], but it only saves if_changed_dep.
As reported in [2], all commands that use redirection can potentially
leave an empty (i.e. broken) target.

[Note 3]

Another (even safer) approach might be to always write to a temporary
file, and rename it to $@ at the end of the recipe.

   <command>  > $(tmp-target)
   mv $(tmp-target) $@

It would require a lot of Makefile changes, and result in ugly code,
so I did not take it.

[Note 4]

A little more thoughts about a pattern rule with multiple targets (or
a grouped target).

    %.x %.y: %.z
            <recipe>

When interrupted, GNU Make deletes both %.x and %.y, while this solution
only deletes $@. Probably, this is not a big deal. The next run of make
will execute the rule again to create $@ along with the other files.

[1]: https://lore.kernel.org/all/YLeot94yAaM4xbMY@gmail.com/
[2]: https://lore.kernel.org/all/20220510221333.2770571-1-robh@kernel.org/
[3]: https://lists.gnu.org/archive/html/help-make/2021-06/msg00001.html
[4]: https://www.cons.org/cracauer/sigint.html

Fixes: 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd files")
Reported-by: Ingo Molnar <mingo@kernel.org>
Reported-by: Rob Herring <robh@kernel.org>
Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
Tested-by: Ingo Molnar <mingo@kernel.org>
Reviewed-by: Nicolas Schier <nicolas@fjasle.eu>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Stefan Bader <stefan.bader@canonical.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[32e59c7e0f...](https://github.com/treckstar/yolo-octo-hipster/commit/32e59c7e0fda15629921276ea9ebaaa1f2508998)
#### Friday 2023-02-24 16:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Miziziziz/miziziziz.github.io](https://github.com/Miziziziz/miziziziz.github.io)@[e1e8ac3d50...](https://github.com/Miziziziz/miziziziz.github.io/commit/e1e8ac3d50ebb141eb6f0e2443f9baa4f6b8bba0)
#### Friday 2023-02-24 16:43:03 by miziziziz

Merge branch 'master' of https://github.com/Miziziziz/miziziziz.github.io

fuck you git

---
## [claydegruchy/wfrp-map-osm](https://github.com/claydegruchy/wfrp-map-osm)@[0e589a7538...](https://github.com/claydegruchy/wfrp-map-osm/commit/0e589a7538c9ebadb0557bc0c61a985b9c59cc66)
#### Friday 2023-02-24 17:37:24 by clay

fuck shit fucking tailwind overcomplicated motherfucker of a system make it fucking simple, dont make me learn some entirely new, janky css shit, might as well write it myself, at least the garbage always stays in one file isntead of being smeared over hte entire project FUCK

---
## [KKQC/Portfolio](https://github.com/KKQC/Portfolio)@[fdde90d418...](https://github.com/KKQC/Portfolio/commit/fdde90d4185e63a4f9fdd3757f8c84170b32bf09)
#### Friday 2023-02-24 17:48:23 by KKQC

corrected inexcusable sins

fuck you korniak for using

sth {

}

instead of

sth
{

}

---
## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[91f06a97d3...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Friday 2023-02-24 17:52:16 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[d95ca04819...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Friday 2023-02-24 17:52:16 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[728a0f1b91...](https://github.com/GoldenAlpharex/tgstation/commit/728a0f1b9147197bb81f22d946f67e9d08719d5a)
#### Friday 2023-02-24 19:07:39 by Jacquerel

Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

---
## [DEMOLITIONDON96/im-concerned-about-this-lmao](https://github.com/DEMOLITIONDON96/im-concerned-about-this-lmao)@[d36f4cd053...](https://github.com/DEMOLITIONDON96/im-concerned-about-this-lmao/commit/d36f4cd05312a5bc6b309969d3be1f3c89ea21bf)
#### Friday 2023-02-24 19:16:11 by GDD

you'll never FUCKING believe what it is this time

yeah
btw if you read these commit comments you're cool

---
## [fleetdm/fleet](https://github.com/fleetdm/fleet)@[6091556b7a...](https://github.com/fleetdm/fleet/commit/6091556b7a6f69f92b7bbb590b5a3068c3a4558d)
#### Friday 2023-02-24 19:28:21 by Mike McNeil

Fix build (#10018)

mikermcneil
  3 minutes ago
@Kathy Satterlee
 I think https://github.com/fleetdm/fleet/pull/9881 broke the build
4 replies

 .
mikermcneil
  2 minutes ago
https://github.com/fleetdm/fleet/pull/9979#issuecomment-1440604277


Zay Hanlon
  1 minute ago
Oops. That was my approval/merge on Kathy's change


Zay Hanlon
  1 minute ago
How do I fix?


mikermcneil
  < 1 minute ago
@Zay Hanlon
All good. I think we should make it so that PRs can't be merged until
they pass the CI checks. It's annoying but would prevent things like
this, which are expensive and involve multiple folks' time.
@Zach Wasserman
 
@Luke Heath
I'm going to turn on the branch protection that prevents merging when
automated CI checks are failing.
@Kathy Satterlee
 I'll follow up with a fix now.
@Jarod Reyes
 Feel free to go ahead and merge your PR in the meantime.


Zay Hanlon
:spiral_calendar_pad: [11 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091760162369?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Sorry :disappointed:


mikermcneil
[10 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091789685699?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
All good, inevitable


Zach Wasserman
[9 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091841779269?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
FWIW turning that on will really slow down my dev process at times.


Zach Wasserman
[8 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091942206439?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
eg. if I make one tiny change on a PR that I already know passes all the
tests then I'll have to wait 15 mins for the whole CI to run before I
can merge.


mikermcneil
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091967828479?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
it was an indentation issue:
https://github.com/fleetdm/fleet/pull/10018/files#diff-68623aac08ce48b5c1275a38ea9f42a8a730a9c2e04ab1946174cdc67f4ce686R8
:ty:
1



Luke Heath
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092006055779?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Is it possible to conditionally enable the required CI checks?


Zach Wasserman
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092018873739?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Maybe you can just turn on a limited set of checks that we know go
really fast and have a high true-positive rate?


Luke Heath
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092062859149?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
That's a good idea. FWIW we'll be removing e2e test runs in CI later
this week, which will reduce the CI run time by ~25 minutes.


mikermcneil
[< 1 minute
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092432337109?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
This is not the first time this has happened and I'd like to put an end
to the emergency remediation that takes a chunk of the day's focus away
from multiple people each time it occurs. If it causes a drain on our
ability to move quickly, let's def change it back. If it's worth the
friction (like the PR approval restriction), then we can keep it.
I'm running into the problem of being able to select the "test-website"
job from [this
list](https://github.com/fleetdm/fleet/settings/branch_protection_rules/18283834),
likely because it is already conditional:
image.png

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d39c53f9e1...](https://github.com/mrakgr/The-Spiral-Language/commit/d39c53f9e19241bf3a67d51937279106f949d38a)
#### Friday 2023-02-24 20:03:07 by Marko Grdinić

"https://youtu.be/PYCoRnJkn_c
C# Developer Career Path Guide (ZERO TO HIRED)

This guy is trustworthy. He says that C# is a boring business language, and that I am going to be working on boring things with it. He does say that the salaries are huge.

https://youtu.be/PYCoRnJkn_c?t=232
> These days Javascript is mandatory in any development discipline.

https://youtu.be/PYCoRnJkn_c?t=464

Now he talks about building apps. He says the app should have all the features that one should see in a corporate website.

https://youtu.be/PYCoRnJkn_c?t=562
> Stay out of machine learning. Stay out of data science.

https://youtu.be/PYCoRnJkn_c?t=660
> Employers aren't going to call you if you don't have unit tests.

https://www.youtube.com/watch?v=PYCoRnJkn_c
> Download a couple of Udemy courses on how to actually interview.

7:15pm. Who is smart? Who is stupid here?

I had no idea there are Udemy courses on interviewing. I guess that is something to think about.

7:25pm. https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn

Look at jobs like these. Just why couldn't I get them? No reason at all.

One last note, he mentions I should have a cool hobby like running and that this is one of the reasons why employers are crazy about him. Egh, nevermind that. Getting out of the house was only ever on the schedule once I get out of the house. But that is not going to happen. I am on the path of self destruction.

https://www.udemy.com/course/find-a-job-interview-skills-training-course/

Oh this is a free course.

https://youtu.be/7ZBiSyl9f_E?t=105
> Half these jobs do not even have applicants.

8pm. https://youtu.be/BDMh2evivzw
Self-Taught C# Developer Road Map 2022

Let me watch this as well.

https://youtu.be/BDMh2evivzw?t=158
> You can do backend if you want to, but I highly, highly recommend that you do full stack.
> Because it is going to be way easier to get a job.

https://youtu.be/BDMh2evivzw?t=186
> C# is notoriously difficult to learn.

Really? He keeps saying that, but I do not believe him.

https://youtu.be/BDMh2evivzw?t=310
> There is no Python jobs where I live.

https://youtu.be/BDMh2evivzw?t=481
> Don't spend too much time, learn the basics, move on...to C#.

https://youtu.be/BDMh2evivzw?t=639

If you think about how long this would take a beginner, I am making progress at a blistering speed.

This is exactly the route I want to take, and he is pushing me in that direction. I really do want to add some knowledge about networking because I feel like an idiot when it comes to http requests and similar kinds of protocols.

Let me just take the time to do this properly. Taking an extra month to learn all of this and build up my portfolio.

https://youtu.be/BDMh2evivzw?t=785
> Focus Entitiy framework, stay away from MongoDB, and stay away from any type of fancy database.

https://youtu.be/BDMh2evivzw?t=907
> If you can build an app like that, you don't need a college degree, you don't even need any work history.

Huh, really? Ok, I'll give this a shot. I thought I might need to mess on the resume, but if a good app or two is enough.

https://youtu.be/BDMh2evivzw?t=929
> Is it going to be really difficult to make that app? Yes, but if...

Bullshit. This will be piss easy.

What this guy is saying is a good reality check for me. Right now I am feeling cursed, but if all I need is a good web app to get a good job, then that is a really easy goal to meet.

I am basically crazy right now. I feel like nothing is going right, that no matter what effort I make I can't meet my goals. That even if I do all this, I won't be able to achieve anything. But that can't be it.

I know that thanks to all the effort I put in, my programming skill should be remarkable.

https://youtu.be/BDMh2evivzw?t=1054
> You don't need to learn CSS all that much. You can get away with the Bootstrap framework.

https://youtu.be/BDMh2evivzw?t=1072
> I have a whole entire video on how to create a resume.

I am going to check it out in the future.

https://youtu.be/BDMh2evivzw?t=1155
> After the first year is when you start making crazy amounts of money.

He says that the first job is going to be crappy.

8:35pm. Ok, let's leave it at this. I'll follow the path outlined here. I am not going to be applying to any more jobs until I have everything set. I'll get my portfolio done, get the webdev skills that I need.

I won't pin too much hopes on the Valora F# job. That kind of depends on whether those people recognize my ability simply on the strength of the Spiral language project. And if my previous rounds are any indication, nobody cares.

I'll go the classical route as it will be so easy for me. Right now, I am already OP in terms of programming skills, I just need to reach out a bit and acquire the skills people are willing to pay for.

http://pythonnet.github.io/

> Python.NET (pythonnet) is a package that gives Python programmers nearly seamless integration with .NET Framework, .NET Core and Mono runtime on Windows, Linux and macOS. Python.NET provides a powerful application scripting tool for .NET developers. Using this package you can script .NET applications or build entire applications in Python, using .NET services and components written in any language that targets the CLR (C#, VB.NET, F#, C++/CLI).

> Python.NET is currently compatible and tested with Python releases 3.7 - 3.11.

Ohhh, it is up to day. That could be really cool.

I really need a way of transfering data between .NET and Python for my Holdem project later. Though I could do it over the network card, this way could be better.

I'll keep it in mind. I really want access to Python's ML libraries from my .NET backends, but not much else. I just need a way of transfering primitive arrays without the slowness of going through the network card. As long as I had that, I have everything I need for the Holdem project.

8:55pm. Let me close here for real. I need to believe that success and failure in the world make sense. I can't be paranoid and say that the black star is shining on me.

All I want is a chance to show off my skills and get a job based on that.

I can't really show off backend skills, so it makes sense to go the full stack route even if in the end all I get are backend jobs.

9pm. I should have achieved something with ML, but I literally can't do a thing with it right now that would be in any way impressive. The poker agents I'll dome is possibly the best one could do for somebody in my circumstances."

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[b53c9f0531...](https://github.com/NewyearnewmeUwu/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Friday 2023-02-24 20:17:02 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

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

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Vhmit/kernel_asus_msm8937](https://github.com/Vhmit/kernel_asus_msm8937)@[79f6b96bc2...](https://github.com/Vhmit/kernel_asus_msm8937/commit/79f6b96bc242efd98197d22be1eca48441e25055)
#### Friday 2023-02-24 20:38:04 by Steven Barrett

ZEN: Implement zen-tune v4.12

4.9:
In a surprising turn of events, while benchmarking and testing
hierarchical scheduling with BFQ + writeback throttling, it turns out
that raising the number of requests in queue _actually_ improves
responsiveness and completely eliminates the random stalls that would
normally occur without hierarchical scheduling.

To make this test more intense, I used the following test:

Rotational disk1: rsync -a /source/of/data /target/to/disk1
Rotational disk2: rsync -a /source/of/data /target/to/disk2

And periodically attempted to write super fast with:
dd if=/dev/zero of=/target/to/disk1/block bs=4096

This wrote 10gb incredibly fast to writeback and I encountered zero
stalls through this entire test of 10-15 minutes.

My suspicion is that with cgroups, BFQ is more able to properly sort
among multiple drives, reducing the chance of a starved process.  This
plus writeback throttling completely eliminate any outstanding bugs with
high writeback ratios, letting the user enjoy low latency writes
(application thinks they're already done), and super high throughput due
to batched writes in writeback.

Please note however, without the following configuration, I cannot
guarantee you will not get stalls:

CONFIG_BLK_CGROUP=y
CONFIG_CGROUP_WRITEBACK=y
CONFIG_IOSCHED_CFQ=y
CONFIG_CFQ_GROUP_IOSCHED=y
CONFIG_IOSCHED_BFQ=y
CONFIG_BFQ_GROUP_IOSCHED=y
CONFIG_DEFAULT_BFQ=y
CONFIG_SCSI_MQ_DEFAULT=n

Special thanks to h2, author of smxi and inxi, for providing evidence
that a configuration specific to Debian did not cause stalls found the
Liquorix kernels under heavy IO load.  This specific configuration
turned out to be hierarchical scheduling on CFQ (thus, BFQ as well).

4.10:
During some personal testing with the Dolphin emulator, MuQSS has
serious problems scaling its frequencies causing poor performance where
boosting the CPU frequencies would have fixed them.  Reducing the
up_threshold to 45 with MuQSS appears to fix the issue, letting the
introduction to "Star Wars: Rogue Leader" run at 100% speed versus about
80% on my test system.

Also, lets refactor the definitions and include some indentation to help
the reader discern what the scope of all the macros are.

4.11:
Increase MICRO_FREQUENCY_UP_THRESHOLD from 95 to 85
Increase MIN_FREQUENCY_UP_THRESHOLD from 11 to 6

These changes should help make using CFS feel a bit more responsive when
working with mostly idle workloads, browsing the web, scrolling through
text, etc.

Increasing the minimum frequency up threshold to 6% may be too
aggressive though.  Will revert this setting if it causes significant
battery drain.

4.12:
Make bfq the default MQ scheduler

Reduce default sampling down factor from 10 to 1

With the world eventually moving to a more laptop heavy configuration,
it's getting more important that we can reduce our frequencies quickly
after performing work.  This is normal with a ton of background
processes that need to perform burst work then sleep.

Since this doesn't really impact performance too much, lets not keep it
part of ZEN_INTERACTIVE.

Some time ago, the minimum frequency up threshold was set to 1 by
default, but the zen configuration was never updated to take advantage
of it.

Remove custom MIN_FREQUENCY_UP_THRESHOLD for MuQSS / ZEN_INTERACTIVE
configurations and make 1 the default for all choices.

Change-Id: I2a31fbc97fe12ffce30457ec2e83ed25764e2daf
Signed-off-by: Harsh Shandilya <msfjarvis@gmail.com>

---
## [mrazael/examples](https://github.com/mrazael/examples)@[1485706bd4...](https://github.com/mrazael/examples/commit/1485706bd4a285b683618262a780aafb269cfc97)
#### Friday 2023-02-24 21:15:59 by mrazael

Add files via upload

pulse %>%
  ggplot(., aes(x = sex, y = rest)) +
  geom_boxplot(aes(fill = sex)) +
  facet_wrap(~smoke, labeller = labeller(smoke = c("N" = "Non-smoker", "Y" = "Smoker"))) +
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) +
  scale_fill_discrete(name = "", labels = c("Female", "Male")) +
  ylab("Resting heart rate") +
  ggtitle("The relationship of sex and smoking to resting heart rate")

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b4954e1402...](https://github.com/Ultimate-Fluff/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Friday 2023-02-24 21:26:11 by carlarctg

zombie powder fix (#2315)

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

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

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
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [storyandfortune/bob](https://github.com/storyandfortune/bob)@[d5bd4f024f...](https://github.com/storyandfortune/bob/commit/d5bd4f024fb1ee84130efeac15bb0b2228712567)
#### Friday 2023-02-24 21:35:01 by storyandfortune@github.com

fuck you. what i put in my repo is my business. suck my dick you nosey fucking cunts.

---
## [peff/git](https://github.com/peff/git)@[fc4734da47...](https://github.com/peff/git/commit/fc4734da47bb330c0261794e16ee24d993ca99b3)
#### Friday 2023-02-24 21:47:14 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[88c331ac5a...](https://github.com/peff/git/commit/88c331ac5acceac43a47c2b846af8cb090fcf40b)
#### Friday 2023-02-24 21:47:54 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [AnimeAllstar/ubccsss.org](https://github.com/AnimeAllstar/ubccsss.org)@[a072092d42...](https://github.com/AnimeAllstar/ubccsss.org/commit/a072092d42ecf2c8a1b044de8fe93d9cc4107ea1)
#### Friday 2023-02-24 22:22:07 by csssbot

New review for CPSC 310 by Andy Liang (#378)

> The course consists of a full stack project (no DB) where the hardest
part of the project is actually more algorithm related ish (building a
query engine) than it is software construction in my opinion. The
project itself ended up being very useless (especially if you have done
one decent full stack personal project or have coop experience) since
there is no code quality enforcement. This means you are free to write
garbage code, as long as it works. I would advice to start early on the
project though!

The conceptual portion taught in lecture is useful. However the project,
nor any other part of the course, really forces you to try the design
patterns that you have learned. :)
>
> Difficulty: 3/5
> Quality: 2/5
> <cite><a href=''>Andy Liang</a>, Feb 05 2023, course taken during
2022W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: Andy Liang
    authorLink: 
    date: 2023-02-05
    review: |
The course consists of a full stack project (no DB) where the hardest
part of the project is actually more algorithm related ish (building a
query engine) than it is software construction in my opinion. The
project itself ended up being very useless (especially if you have done
one decent full stack personal project or have coop experience) since
there is no code quality enforcement. This means you are free to write
garbage code, as long as it works. I would advice to start early on the
project though!
      
The conceptual portion taught in lecture is useful. However the project,
nor any other part of the course, really forces you to try the design
patterns that you have learned. :)
    difficulty: 3
    quality: 2
    sessionTaken: 2022W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [jrprice/Halide](https://github.com/jrprice/Halide)@[e5fdbe3f3c...](https://github.com/jrprice/Halide/commit/e5fdbe3f3c32afaf9085cecf2d0dfd70ecac3224)
#### Friday 2023-02-24 23:11:18 by Steven Johnson

Partial fix for generator_aot_acquire_release()

This adds the necessary (horrible hackery) to bring the WebGPU case in line with the other backends... but the test still fails, apparently due to the same copy-to-host bug we suspect for generator_aot_gpu_only.Pushing this anyway because it was annoying to write :-)

---
## [GerHobbelt/thirdparty-freeglut](https://github.com/GerHobbelt/thirdparty-freeglut)@[d2f28919d3...](https://github.com/GerHobbelt/thirdparty-freeglut/commit/d2f28919d38580b208407eab1dd7c08c1a582b7e)
#### Friday 2023-02-24 23:20:22 by Ger Hobbelt

fix duplicated here after code review.

----------------------

tesseract: fix compiler errors due to windows system header file errors

// mupdf headers cause some weird error in MSVC system header commdlg.h when include *after* <random> header below. And this only happens for params.cpp, i.e. when params.h has been included first. ... A definite case of WTF?!
//
// Which is why we include the mupdf headers here in monolithic builds...
//
// EDIT: Subsequent compiler runs and analysis now popped up the same 'crazy' errors in commdlg.h (caused by missing font struct definitions)
// from control.cpp and a few other tesseract source files. Which forced me to investigate further.
//
// Debugging through running the preprocessor (cl /E /P ...) and some grepping
//
//   grep '#line' $( find -name control.i )  | grep -B 1000000 commdlg | grep -B 1000000 wingdi | grep -v "Program Files"
//
// showed the original culprit was probably MuPDF\\thirdparty\\curl\\lib\\setup-win32.h.
// And indeed there we found the often-troublesome WIN32_LEAN_AND_MEAN and a few choice other NOXYZ feature defines before loading windows.h.
//
// > Rationale for the precise grep chain is out of scope.
// > Hint: wingdi defines what commdlg needs. Chain + last filter takes care of getting loading file as last #line stmt, IFF you're lucky.
// > Of course I was lucky. After N iterations, which got me to this grep chain. EFF that shite, with prejudice!
//
// This practice MUST be abolished in all libraries, everywhere, as it causes severe compile errors at surprise locations and at surprise times,
// while the errors reported aren't always easy to diagnose for everybody. (How many programmers are well versed with gcc -E, cl /P and code inspection?)
//
// Setting these feature defines MUST be the sole prerogative of the final application code/project, if any. Or rather more precise: the final C/C++ *.c+*.cpp source files.
// No-one else MUST mess with these in any header / include files, just to 'help' shorten compiler turn-around times. The road to Hell is paved with good intentions.
// If you want to offer 'help' like that, consider making sure your header files work well with precompiled header caching in the various compilers instead.
//

See also cUrl repo.

---
## [dart-lang/dart_style](https://github.com/dart-lang/dart_style)@[fc29f837ff...](https://github.com/dart-lang/dart_style/commit/fc29f837ff05c8e1dc9a1884918a8a6c4051c6d9)
#### Friday 2023-02-24 23:33:17 by Bob Nystrom

Format switch cases that aren't valid patterns. (#1177)

* Better style for inline case bodies.

In the previous PR, any case body that fit on one line was allowed to
even if other cases in the same switch didn't. I tested it on a corpus
and I found that led to confusing switches where it wasn't always
clear where the case body starts.

I think you really want it all or nothing: either every single case fits
on the same line in which case you can make the whole switch compact,
or every case should be on its own line, even the ones that would fit.

Unfortunately, it's a little tricky to have formatter rules that span
code containing hard splits, so getting that working took some doing.
It also regressed performance pretty badly. But I figured out some
optimizations in ChunkBuilder and it's basically back to the same
performance it had before.

Also, this incidentally fixes a bug where parameter metadata in trailing
comma parameter lists was also supposed to have that same all-or-nothing
splitting logic but didn't.

I've tried this on a corpus and I'm pretty happy with the results. Right
now, relatively few switches benefit because the mandatory breaks mean
a lot of switches have at least two statements (which always causes the
case to split). But as those breaks are removed, I think we'll see more
compact switches. Even today, this code does improve some switches
where every case is just a short return statement.

* Format switch cases that aren't valid patterns.

Fix #1164.

The solution is kind of hacky, but users will probably never run into it
and it avoids complicated the user experience of the formatter.

To get this working, I had to update to analyzer 5.5.0 because 5.4.0 had
an assert failure when it tried to parse an invalid switch case. But
5.5.0 also has a bug which is causing a couple of formatter tests to
fail: https://github.com/dart-lang/sdk/issues/51415.

I'll probably wait until there's a fix for that out before this gets
merged to master.

Analyzer 5.5.0 also changes some of the AST types. Refactored how
binary expressions and patterns are formatted to avoid copy/paste from
that change.

* Better docs.

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[bf815f8abe...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/bf815f8abe0a7b8f06bee15e457f9ba257876d66)
#### Friday 2023-02-24 23:51:03 by Clifford T. Matthews

includes today's 24 mile 41# pack run.

This is the same training run I did on January 29th. In a normal training
year I'd be faster, but my hot-spot got worse and not only was it painful,
I was initially under the impression that my intervening training is what
cause it to be worse, but then I remembered...

...sometime in the last week I realized there was a fairly large bump around
my hot-spot.  I thought there was some chance that my hot-spot was a callus,
so I used a file to file it down quite a bit.  That actually seemed to make
things better.  However, at today's turnaround, I looked and saw that due
to my thinner skin, I could see a little brown dot.  That dot is either
dried blood from a puncture that I sustained at some point or is actually
foreign matter.  I'm going to find out later today which it is.

My *guess* is I have more than one problem with that foot and that
filing down the callous only made things worse.  There's also a chance
that trying to figure out what that brown dot is will make things
further worse, but I think more likely than not I'll either improve
the situation or effectively not make it better or worse (famous last
words).

It's clear to me that I'm now moving slowly not only due to the pain
in my foot, but also due to decrease fitness from the lack of running
volume and lack of speedwork during this training period.  I don't
think I'm in danger of DNF'ing (or DNS'ing) Western States, but I will
not be signing up for the Tough Ruck this year, and I consequently, I
may skip the Boston Marathon, since flying out to Boston just to do a
slow Boston Marathon on a gimpy foot may not be a good use of money.

---
## [Not-radioactive/alx-low_level_programming](https://github.com/Not-radioactive/alx-low_level_programming)@[71e9fdc0a1...](https://github.com/Not-radioactive/alx-low_level_programming/commit/71e9fdc0a18420b8d0050dfaf3263f96ad06365d)
#### Friday 2023-02-24 23:59:13 by Not-radioactive

This Task is cringe and all of this is cringe and fuck everthing and fuck life, I hate my life :c

---

