## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-12](docs/good-messages/2023/2023-03-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,925,540 were push events containing 2,606,710 commit messages that amount to 151,580,159 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [GerHobbelt/splitmerge](https://github.com/GerHobbelt/splitmerge)@[8bb2e67311...](https://github.com/GerHobbelt/splitmerge/commit/8bb2e673113c2561a24c927a54e7f604b170ed77)
#### Sunday 2023-03-12 00:13:53 by Ger Hobbelt

- fix silly math bug in parsing `-l` size parameter when specified in `M` (megabyte = 1_000_000 bytes)
- fix typos in on-line help and code comments
- print version using new `-v` option
- bumped version to 1.2
- add sanity check: when the split request is 'ridiculous' it is rejected & the application will abort with a error code. 'ridiculous' here is:
  + split files with less then 300 bytes data per segment. As the overhead is 256 bytes, that'ld result in an overhead of near 100%
  + split files are requested to be larger than 2GB (minus 16 bytes for some nasty classic OS/hardware issues on dinosaur machines)
  + the requested split would produce more than 10K split files, hammering the poor file system.

Consequently we wouldn't ever be able to split files beyond 2G*10K ~= 20TByte size. It's not designed to do that anyway, but if you would like to do that, also consider the time involved: 1 disk image or whatever those 20TB contain, at a *very good* regular desktop box' sustained transfer rate of, say, 100MB/s (NVMe can do much faster, but with a 2 * 20TB NVMe storage backing, welllll, you won't need my little tool I suppose. Maybe in 10 years. Gates was wrong with 640KB, so this assumption of mine also has the expected survival time of a fruit fly, I suppose...) Anyway, time: say transfer rate = 100MB/sec sustained, then 20TB takes 20e12 / 100e6 = 1/5 e6 = 2e5 seconds. One year is about 400 days * 25 hours * 4000 seconds = 1e4 * 4e3 = 4e7, so a single split command would take 2 * 2e5 (1 read + 1 write !!) = 4e5 / 4e7 = 1/100th year or: give-or-take 3-to-4 days.
I'ld love to hear your use case then. :-)
For now, split works for me & my goals, which is large files that get up to about 20GB, which is 1/1000 of that upper bound. And I can assure you my not-the-blazingest-data-pumping-blizard-of-the-pack machine doesn't reach 100MB/sec sustained over long stretches like that: more like 30-80, depending on which harddisks are hooked up.

's All good enough for me, is whumsayin'.

---
## [posterhusky/FarkleBot](https://github.com/posterhusky/FarkleBot)@[5ec01d835b...](https://github.com/posterhusky/FarkleBot/commit/5ec01d835bad1850e8028ca0db84b551e6722af4)
#### Sunday 2023-03-12 00:47:04 by Vanolex

GAME MODES part 2
Added modes:
- Hot Potato
- Tug of War
- Mystery Die
Changes:
- increased invitation duration to 2 mins

TODO:
- bingo mode
- events channel, rotation and queue

---
## [jnutt367/acts](https://github.com/jnutt367/acts)@[e177417999...](https://github.com/jnutt367/acts/commit/e1774179998d854440338cbde7b5a4c1913c17af)
#### Sunday 2023-03-12 01:37:04 by Jason Nutt (He/Him) Developer/Creator

Update index.js

"Repent and be baptized, every one of you, in the name of Jesus Christ for the forgiveness of your sins. And you will receive the gift of the Holy Spirit."

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4b65ae188a...](https://github.com/TaleStation/TaleStation/commit/4b65ae188a82de3c29d5bcf33acf4cda3499d5db)
#### Sunday 2023-03-12 02:17:45 by TaleStationBot

[MIRROR] [MDB IGNORE] [NO GBP] fixes typo in PR template (#4837)

Original PR: https://github.com/tgstation/tgstation/pull/73928
-----
## About The Pull Request

There is a verb in the English language that has the function of
expressing the meaning of getting something from someone or something
else that has given it to you or sent it to you or delivered it to you,
being given something by someone or something else that has decided to
give it to you or send it to you or deliver it to you, or being the
recipient of something that someone or something else has given to you
or sent to you or delivered to you. This verb is “receive.” This word
has a very specific spelling that follows a very common rule in the
English language that states “i before e except after c.” However, some
people may have difficulty remembering this rule or applying this rule
correctly when they write this word. They may write this word with an
“-ie-” combination instead of an “-ei-” one. This is always a very big
mistake and should be avoided in your writing at all costs. The word
“recieve” does not exist in the English language and will be marked as
an error by any spell checker or grammar tool that you use.

## Why It's Good For The Game

I would like to express my sincere and heartfelt apology for spelling
the word receive wrong in my previous message. I made a very big mistake
and wrote the word with an “-ie-” combination instead of an “-ei-” one.
This is always incorrect and does not follow the very common rule in the
English language that states “i before e except after c.” The word
receive has a very specific spelling that follows this rule. The word
recieve does not exist in the English language and will be marked as an
error by any spell checker or grammar tool that I use. I am very sorry
for this mistake and I hope that you will forgive me for it.

## Changelog

I would like to inform you that there is no changelog available for this
update, because this update does not constitute a change to the game
itself. A changelog is a document that records the changes that have
been made to the game in each update. However, this update does not make
any changes to the game itself. It only fixes some minor issues that
were affecting the performance of the game. Therefore, there is no need
for a changelog for this update, because there are no changes to the
game itself that need to be recorded in a document.

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[11aab72dc9...](https://github.com/pytorch/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Sunday 2023-03-12 02:24:48 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [fengyuewuhen/qemu](https://github.com/fengyuewuhen/qemu)@[8d0efbcfa0...](https://github.com/fengyuewuhen/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Sunday 2023-03-12 02:40:07 by Paolo Bonzini

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
## [cloudnepal/nushell](https://github.com/cloudnepal/nushell)@[2e01bf9cba...](https://github.com/cloudnepal/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Sunday 2023-03-12 02:43:14 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [wryan14/wryan14.github.io](https://github.com/wryan14/wryan14.github.io)@[79212fe15d...](https://github.com/wryan14/wryan14.github.io/commit/79212fe15d35dfe7f08f68393c35dbecf1195539)
#### Sunday 2023-03-12 04:09:38 by Ryan Wolfslayer

Commit message: Add text discussing John Wesley's sermon of 'Of Evil Angels' examining the consequences of Christian disobedience and emphasizing God's sovereignty.

---
## [Sown-Dev/7DRL](https://github.com/Sown-Dev/7DRL)@[654ec47916...](https://github.com/Sown-Dev/7DRL/commit/654ec4791603036b82b3a133b3775590e9eb93dd)
#### Sunday 2023-03-12 04:10:47 by Sown-Dev

FUCKING FINALLY FIXED LEVEL GEN COLLIDERS (my dumbass was checking if raycasthit was null instead of raycasthit.collider) this shit took so long you have no idea

---
## [dylanfeehan/dategen](https://github.com/dylanfeehan/dategen)@[9712169a47...](https://github.com/dylanfeehan/dategen/commit/9712169a477d06444f83fdf87d06c96324339e3c)
#### Sunday 2023-03-12 06:06:13 by Dylan Feehan

firebaseui is so painful

got firebase authentication , user creation and sign up workign (tested
at lest). also got a decent firebaseui working. was a huge pain in the
butt and chatgpt actually saved the day. i don't understand enough about
how the auth object works so i think i need to read the documentation.
next step is to see if firebaseui can provide everything that i want
(user creation, sign up, sign in with google, etc... and routing to
success page / home page etc... if it doesn't seem capable, i'm going to
have to roll my own. either way, i'm going to have to start thinking
about the sign in flow and maybe build a temporary homepage... but the
main priority right now is getting the UI buitl and functioning for sign
on, and it's probably going to take some time to figure out if
firebaseui is going to work. but if it takes me 2 hours of messing with
firebaseui to realize that it'll work, its worth it because rolling my
own will suck

---
## [stevenxxiu/nushell](https://github.com/stevenxxiu/nushell)@[378a3ae05f...](https://github.com/stevenxxiu/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Sunday 2023-03-12 07:01:10 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [newstools/2023-daily-nation](https://github.com/newstools/2023-daily-nation)@[13ab543cbf...](https://github.com/newstools/2023-daily-nation/commit/13ab543cbf5796778bdbf5bab1bb06b405bf01c7)
#### Sunday 2023-03-12 07:12:45 by Billy Einkamerer

Created Text For URL [nation.africa/kenya/counties/muranga/-goodbye-my-love-my-wife-s-last-painful-words-to-me-as-villagers-lynched-her-4155308]

---
## [ShadowNinja29/ArcCW_UR](https://github.com/ShadowNinja29/ArcCW_UR)@[7f3487f04f...](https://github.com/ShadowNinja29/ArcCW_UR/commit/7f3487f04f11366292ceb88ab246878d0c673043)
#### Sunday 2023-03-12 07:46:52 by rzen1th

holy jesus god damn motherfucking christ how long was this like that

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[53cc235e77...](https://github.com/treckstar/yolo-octo-hipster/commit/53cc235e7784ad0750d38819186a6eea74a28145)
#### Sunday 2023-03-12 11:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tmtmtl30/Shiptest](https://github.com/tmtmtl30/Shiptest)@[31eabb62f1...](https://github.com/tmtmtl30/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Sunday 2023-03-12 11:35:31 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
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
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
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
## [GeraldR63/AstroNavi](https://github.com/GeraldR63/AstroNavi)@[3daa1fddc4...](https://github.com/GeraldR63/AstroNavi/commit/3daa1fddc40e04a9f3bfc8ce021d62452eb8a21a)
#### Sunday 2023-03-12 11:48:49 by DO4ZWO

Monster

I tried to write a simple navigation app and now I'm forced to build a perfect application.  I added now code to force users to enter valid DMS format. This code is up to now only used in "Simple Navigation (SUN)" dialog. You should'nt be able to enter  "Hc-omputed" or  "Decl. CB from NA" out of range. If you enter no sign than you can enter up to 360degree (thats 359°59'0.59"). If you enter a sign (+-EWNS) than the max range is 180degree (179°59'0.59").  Check it out.  However, one bullshit number is probably possible. You can not enter more than one ° or ' or " sign but well, fuck, decimal points at open end....wtf. For a simple DMS parser. There is today no "focus lost" event in Android Java...who the fuck changed this? They destroyed JAVA because in my opinion they force Kotlin.

---
## [Davchikk/Shiptest](https://github.com/Davchikk/Shiptest)@[7f8874df29...](https://github.com/Davchikk/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Sunday 2023-03-12 13:34:02 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
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
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
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
## [SquidDev/Cobalt](https://github.com/SquidDev/Cobalt)@[cc57773c52...](https://github.com/SquidDev/Cobalt/commit/cc57773c528fb930f8d76bd72b41d777672ee8cd)
#### Sunday 2023-03-12 13:48:19 by Jonathan Coates

Handle timeouts via interrupts rather than polling

Currently the recommended way of handling timeouts is by implementing a
custom DebugHandler and overriding onInstruction/poll. This was probably
a bad idea for a couple of reasons:

 - Every instruction must now call DebugHandler.onInstruction, which
   adds some performance overhead. Ideally the JIT would be able to
   eliminate the virtual call, but we can't rely on that.

 - Suspending the VM inside onInstruction ends up being quite clunky, as
   you need to juggle various debug frame flags.

This commit tears out all of this functionality, and replaces it with an
interrupt-based approach:

 - LuaState.interrupt(): Sets the interrupt flag on the Lua state. This
   is typically called from another watchdog-style thread (such as
   CC:T's ComputerThread.monitor).

 - LuaState.isInterrupted()/LuaState.handleInterrupt(): These are called
   from within the Lua VM at opportune times (currently on instruction,
   though we may change that).

 - InterruptHandler: An interrupt handler is provided to the LuaState
   when constructing it. When handleInterrupt is called, the interrupt
   handler is invoked. The handler may either error, or indicate that it
   wishes to suspend the currently running VM.

This should have a much lower overhead (the hotpath is just a single
load and branch), though I confess I've not actually run any benchmarks
yet. It's definitely a much simpler interface to consume.

This will require some changes to CC:T - while the timeout system is
push-based, there isn't any way to listen to state changes.

This commit also contains a couple of related and unrelated changes, as
I have terrible commit discipline:

 - Add @Serial annotations everywhere

 - Expose LuaThread.status as an enum rather than a string.

 - Clean up the debug hooks a little bit, to be notionally faster on the
   hotpath (when no hooks are active).

   Notionally because I implemented something much simpler a few weeks
   ago and it had very little impact. I'm not sure if something else is
   the dominating factor or if the JIT is being very clever.

---
## [NotRubi/test_uwu](https://github.com/NotRubi/test_uwu)@[5a20552aeb...](https://github.com/NotRubi/test_uwu/commit/5a20552aebf05b664caa206018f40b84b39f1b43)
#### Sunday 2023-03-12 14:11:24 by Rubi Lotus

i need commit names else stupid ass shit wont work

Signed-off-by: Rubi Lotus <116446349+NotRubi@users.noreply.github.com>

---
## [GsKizuna/Anime-Cover-Pack](https://github.com/GsKizuna/Anime-Cover-Pack)@[b5c5dcabed...](https://github.com/GsKizuna/Anime-Cover-Pack/commit/b5c5dcabed363e44d2d9a7ffcabd9c2c3a8c9564)
#### Sunday 2023-03-12 14:23:10 by Ramon Damian James

Modification/Rajout #3

Modification :
Readme en fonction des rajouts

Rajout :

Dossier:
Png Normal

Image Type :
png
Anime Liste:
A Couple Of Cuckoos,
Angel Beats,
Arcane,
Battle Game In 5 Seconds,
Beast Tamer,
Black Rock Shooter,
Black Rock Shooter Dawn Fall,
Bleach,
Chainsaw Man,
Chrno Crusade,
Classroom of the Elite,
Claymore,
Darwin's Game,
Death March To The Parallel World Rhapsody,
Full Metal Alchemist,
Gate - Au-delà de la porte,
Goblin Slayer,
Horimiya Hori - san To Miyamura - kun,
In Another World With My Smartphone,
In the Land of Leadale,
La Sorcière invincible tueuse de Slime depuis 300 ans,
L'attaque des Titans,
Les combattants seront déployés,
Log Horizon,
Lookism,
Lucifer And The Biscuit Hammer,
Moi Quand Je Me Reincarne En Slime,
Overlord,
Rascal Does Not Dream Of Bunny Girl Senpai,
Re Zero - Re vivre dans un autre monde à partir de zéro,
Rent A Girlfriend,
Romantic Killer,
Seirei Gensouki - Spirit Chronicles,
Si je suis la Vilaine, autant mater le Boss Final,
Sky-High Survival,
Sword Art Online,
Sword Art Online Alternative Gun Gale Online,
Tales of Zestiria the X,
The Genius Princes - Guide to Raising a Nation Out of Debt,
The Greatest Demon Lord Is Reborn as a Typical Nobody,
The Hidden Dungeon Only I Can Enter,
The Idhun Chronicles,
The Rising Of The Shield Hero,
The Strongest Sage With the Weakest Crest,
The World's Finest Assassin Gets Reincarnated in Another World as an Aristocrat,
TONIKAWA Over the Moon For You,
Trapped in a Dating Sim - The World of Otome Games is Tough for Mobs,
By the Grace of the Gods,
Tomo-chan Is a Girl!

---
## [amir73il/linux](https://github.com/amir73il/linux)@[a5434b7695...](https://github.com/amir73il/linux/commit/a5434b76952ee79ededc9244bd9321b68f5c9084)
#### Sunday 2023-03-12 14:48:17 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

commit 1639a49ccdce58ea248841ed9b23babcce6dbb0b upstream.

[remove userns argument of helpers for 5.10.y backport]

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [jrcribb/highlight](https://github.com/jrcribb/highlight)@[ae53ba8124...](https://github.com/jrcribb/highlight/commit/ae53ba81243e670f52ea81fe5e489948bdf17302)
#### Sunday 2023-03-12 16:09:18 by Eric Thomas

Wire up infinite scroll for logs page (#4319)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR adds infinite scroll to the logs page.

_This PR assumes the reviewer is familiar with offset vs cursor
pagination (see
[here](https://bun.uptrace.dev/guide/cursor-pagination.html) if not)._

### Database structure

#### Auto-incrementing ids

The easiest way to implement cursor pagination is with an
auto-incrementing id since to find the next cursor, you can just use the
next id for the cursor. We do this for finding the next error instance:


https://github.com/highlight/highlight/blob/2abc14b9d8f064a42116f6dfc670a6ebfd79820b/backend/private-graph/graph/schema.resolvers.go#L4008-L4018

However, Clickhouse has no concept of an auto-incrementing id so we
can't use this approach.

#### Timestamps

In Clickhouse, each record has a timestamp, so in theory that could be
the cursor. However, while we have nano-second precision on this column
(e.g. `2023-02-24 11:29:14.789873000`). It's not guaranteed to be
unique. While it may be unlikely (since logs are injected through our
SDKs), two logs could share the same timestamp.

While we don't support it now, if we allow logs to be manually injected
(e.g. through `curl`), it opens up the possibility of a two logs sharing
the same timestamp since the user could set whatever they want.

#### Timestamp + ?

Concatenating the timestamp with another column could be an option for a
cursor. At first glance, `TraceID` seems like a good candidate since
each log should (in theory) have this. However, two logs at the same
time can belong to the same trace.

That really only leaves one option and that is to create a new UUID
column that is guaranteed to be unique for each log.

On their own, UUIDs are not ordered but when concatenated with a
timestamp, we can achieve stable ordering:

Let's look at an example whereby this is in our DB:

| Timestamp | UUID |

|-------------------------------|---------------------------------------|
| 2023-02-24 11:29:15.000000000 | uuid |
| 2023-02-24 11:29:14.000000000 | aaaaaaaaa-3de1-4458-a306-3d4fd406de88
|
| 2023-02-24 11:29:14.000000000 | bbbbbbbb-3de1-4458-a306-3d4fd406de88 |
| 2023-02-24 11:29:13.000000000 | uuid |

In this example, the first and last rows are in the correct order (since
we order time in descending order). The second and third row share the
exact same timestamp so we rely on the second part of the cursor
`(Timestamp + UUID)` to figure out what should come next. To be
consistent with the timestamp, the UUID is also in descending order so
the output will flip these rows:

| Timestamp | UUID |

|-------------------------------|---------------------------------------|
| 2023-02-24 11:29:15.000000000 | uuid |
| 2023-02-24 11:29:14.000000000 | bbbbbbbb-3de1-4458-a306-3d4fd406de88 |
| 2023-02-24 11:29:14.000000000 | aaaaaaaaa-3de1-4458-a306-3d4fd406de88
|
| 2023-02-24 11:29:13.000000000 | uuid |

### API spec

As mentioned, the cursor is `Timestamp + UUID`. Passing these values
directly as params has some downsides:

* Passing around a timestamp is likely to get botched somewhere (imagine
the differences between time parsing in Go and Javascript)
* UUID is not something the user is aware of (we don't show UUID
anywhere in the UI)
* It doesn't allow flexibility to change the API later (less important
for us since it's a private API but could be if we ever make logs a
public API).

Fortunately, this is a solved problem and I stumbled across Relay's
[opinionated](https://relay.dev/graphql/connections.htm) way of
structuring this in GraphQL. What's nice is that I only need to
implement a subset of their spec (e.g. I didn't handle paging
backwards). Wiring this up into Apollo's `InMemoryCache` also has
built-in functions
([docs](https://www.apollographql.com/docs/react/pagination/cursor-based/#relay-style-cursor-pagination))
(if we rolled our own API spec, we'd have to write custom logic to
figure this out).

### Generating the cursor

Finally, I pulled some code from this [blog
article](https://dev.to/sadhakbj/implementing-cursor-pagination-in-golang-go-fiber-mysql-gorm-from-scratch-2p60)
on how to encode/decode the cursor (Timestamp + UUID) on the backend.

## How did you test this change?

Lots and lots of unit tests. 
I consider pagination to be one of [three hard problems in computer
science](https://dev.to/sadhakbj/implementing-cursor-pagination-in-golang-go-fiber-mysql-gorm-from-scratch-2p60).
I feel pretty confident I got stable pagination, but please let me know
if you think I'm missing something.

Confirmed infinite scroll works (see
[Loom](https://www.loom.com/share/3efca1b6d1944dadbcdea5b2a52d9447)).

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Yes. This does recreate the clickhouse table schema (which will drop the
data). See inline comment for justification.

This PR also does not cover some known follow up issues:
* #4388
* #4387

---
## [Dime1154/mojave-sun-13](https://github.com/Dime1154/mojave-sun-13)@[bdc9c58586...](https://github.com/Dime1154/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Sunday 2023-03-12 16:22:23 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [JBatchelor81/my-whatever-I-come-up-with-](https://github.com/JBatchelor81/my-whatever-I-come-up-with-)@[0355262368...](https://github.com/JBatchelor81/my-whatever-I-come-up-with-/commit/0355262368e4a544bf60fac832f2b6f41d00b4fd)
#### Sunday 2023-03-12 17:05:37 by JBatchelor81

Looking for help creating a app that will not only let you know that your partner is cheating but will help you catch them but will also allow you access to everything they are hiding from you in secret files, fake apps, hidden, vaults and anything else you might would think of that they could use to be hiding something from you so that they think they won't get caught. I also want to come up to unencrypte any thing they could have encrypted weather it be cell, tablet, laptop, computer it doesn't matter if they are hiding something on any and I do mean any electronic device we will be right there to catch them and hold them accountable and  make them have to tell the truth. In the end truth is all you and all you have. So if you would like to help me work on this idea and take it from a little dream to a big reality that could possibly change lives I'm open to the help, support, suggestions and anything else you guys are willing and able to help me do to and with the app so it's up and running and catching those cheating partner's who truly believe they are getting away with those dirty, lieing, sneaky 2timing things they have been doing when they think nothing or anyone knows or sees what's happening. Thank You for taking the time to read my descriptions and I really hope there's people interested in helping me get this idea turned into a app that people will want install and use to make sure they have a faithful partner. I look forward to seeing,chatting, and working with whomever wants to take the time and help out and teach someone who is technically challenged but really wants to see her app get made to actually work and be put to good use and help out any person who thinks they are being cheated on but just can't seem to get that leg up on their significant other and put the smack down on their cheating behind. Thanks again your taking the time to read this and help a person who's been through it and knows how it feels and what it can do to your mind heart and emotions. Have a blessed day and thanks again you guys are amazing and I would be honored to get the opportunity to work with anyone on here!

---
## [wryan14/wryan14.github.io](https://github.com/wryan14/wryan14.github.io)@[896fb8069d...](https://github.com/wryan14/wryan14.github.io/commit/896fb8069d193254605a53fcdff7f30f88534ce8)
#### Sunday 2023-03-12 17:12:26 by Ryan Wolfslayer

Commit message: Added John Wesley's sermon, The Scripture Way to Salvation, outlining the path to salvation and emphasizing the importance of personal commitment, humility, and collective action in order to receive God's grace and achieve salvation.

---
## [Rxup/space-station-14](https://github.com/Rxup/space-station-14)@[581e8a0d12...](https://github.com/Rxup/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Sunday 2023-03-12 17:16:25 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [wryan14/wryan14.github.io](https://github.com/wryan14/wryan14.github.io)@[81507f6a91...](https://github.com/wryan14/wryan14.github.io/commit/81507f6a91d37649f958880e1796b9d9ca5d5087)
#### Sunday 2023-03-12 17:21:08 by Ryan Wolfslayer

Commit message: Add text for John Wesley's sermon, "On Guardian Angels" with explanation of his thoughts and inspirations to heed the divine wisdom of our Heavenly Father.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[074e6ae270...](https://github.com/wrye-bash/wrye-bash/commit/074e6ae270edd63b15035fcd911781ed70d398db)
#### Sunday 2023-03-12 17:40:20 by Infernio

Rework and update our screenshots and docs

And now for the least fun part of 311's development. A lot of changes,
both old and new, had never been documented (as a random example, when
discussing the Change To... master command, the readme claimed that
using it would corrupt cosaves and linked to #236, which was fixed and
closed in 0a300af01a85bb3535d3194203fd34cc0d3e9b29 *5 years ago*. So I
kept getting distracted and rewrote more and more stuff and now we're
here:

 251 files changed, 4322 insertions(+), 2259 deletions(-)

There's so many changes in here, I can't even begin to describe them.
Merging it ASAP because I don't think anyone wants to look at this for
more than a second. If I never have to touch the damn readme again,
it'll be too soon. This literally took weeks, with me having to take
frequent breaks lest I burn out.

Some ugly notes from my squashed commits follow:

Also included some random usability tweaks, e.g. bumping the default
size of the doc browser to something actually usable.

Unify dialogue/dialog over the codebase

Most places in our codebase use 'dialog', so I went with that. Obviously
there are still more than a thousand 'dialogue's left because of
Skyrim's vanilla files. I also didn't touch anything in the records, we
want to match the CK and xEdit there.

Add an option to disable the column header menus

Since we allow disabling the global menu, we should allow going the
other way as well.

Focus and select all text in Plugin Name field

Pretty sure it used to do that, but it's not doing it anymore for me.
Easy enough to fix.

Mopy/bash/basher/links_init.py:
Because bare booleans getting passed around is no fun.

Replace country flags with SVGs

Easiest SVGs in the world to find, obviously. Even saves space for all
but Brazil (not surprising, look at that flag).

pt_PT -> pt_BR

That's not European Portuguese, that's Brazilian Portuguese. Note the
TODO, if we ever get a pt_PT translation we need to ditch that deletion
command. And while I'm in the vicinity, English -> American English.

Update some old tool directories

Also update the Photoshop icon, I don't even know what that old one is
supposed to be.

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[7797597633...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/7797597633213f05bc0692643f33b232ec19763f)
#### Sunday 2023-03-12 17:48:37 by George Spelvin

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

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d3af1dff9d...](https://github.com/mrakgr/The-Spiral-Language/commit/d3af1dff9d66ca296c297147895bce563a31d541)
#### Sunday 2023-03-12 18:10:30 by Marko Grdinić

"https://boards.4channel.org/g/thread/92023261/back-to-mcdonalds-wagie-party-is-over
> Never in my 7 years of hiring have I seen a pipeline like this.
> Applicants, I'm going to go ahead and speak on behalf of hiring managers and internal recruiters everywhere and beg you for patience while we all work through the sheer volume of applications coming in.

6:10pm. Ah, I wanted to modify tutorial3 a tad, but nevermind that.

11:10pm. https://docs.google.com/spreadsheets/d/1wf-0RgRQ7ttSx3D9V2WpletexllniG1GNCu70n3EFGY/edit#gid=539156707
Limbus Company - Manager's Manual

3/12/2023

7:45am. Uah, my dinner last night went rambo on my guts this morning. As a result, I am up earlier than usual, freezing myself in the room. Let me get a heater.

7:55am. Ugh, but otherwise I did sleep well. Any mail? No, it is Sunday.

Since I've modified my resume to have 8 years of exp, I wonder if I am going to get people calling me out.

https://simonwillison.net/2023/Mar/11/llama/
https://minimaxir.com/2023/03/new-chatgpt-overlord/

8:05am. https://boards.4channel.org/v/thread/630544026/limbus-company#p630551613

They have interesting convos here. I really like Limbus, but if it starts requiring me to grind, I'll just switch to watching the playthroughs. The casino chapter was pretty funny so far.

8:10am. My PC just randomly shut down.

8:15am. https://mangadex.org/title/25e145f0-a74f-48b6-9d89-b715e28f6417/do-you-think-someone-like-you-could-defeat-the-demon-lord

Let me read this, Killing Bites and then I will get started on the video.

> 4-bit quantization is a technique for reducing the size of models so they can run on less powerful hardware. It also reduces the model sizes on disk—to 4GB for the 7B model and just under 8GB for the 13B one.

> It totally works!

> I used it to run the 7B LLaMA model on my laptop this night, and then this morning upgraded to the 13B model—the one that Facebook claim is competitive with GPT-3.

9:05am. Enough chilling. Let me get started on the video.

9:45am. I've been messing trying to make a different intro, but nevermind. I'll go with the regular images.

9:55am. For fuck's sake, I was recording it on the webcam mic!

11:15am. If there is something I hate doing, that would be putting annotations in Camtasia. Why is it so slow and laggy?

12:35pm. Finally finished recording the video. Let me just clean it up in Reaper a bit and then I'll post it online.

12:50pm. Exporting it. Let me make thumbnail.

https://youtu.be/GggCPN3feHk
The Minimal UI And Message Passing Over Websockets

I'll make it public once it finishes processing. Let me have breakfast here.

1pm. It really takes a lot of effort to make even a small amount of video. I can barely say two sentences without stuttering. If I never get a job because of this, it would be some kind of...comedic justice?

1:50pm. Done with breakfast. Let me do the chores and I will get started on the next video.

2:55pm. Done with chores. Let me get started on the next video.

6:25pm. https://pixabay.com/music/beautiful-plays-cinematic-ambient-piano-118668/

I'll put a little bit of music during the self play segment.

6:35pm. Lunch time. I'll finish the video tomorrow and move onto to implementing the random player.

7pm. Done with lunch. Let me close here today."

---
## [binaryoutcast/aura-dev](https://github.com/binaryoutcast/aura-dev)@[9a8e7e4fe3...](https://github.com/binaryoutcast/aura-dev/commit/9a8e7e4fe3566f24b998065e05dbc3e949b7b8d8)
#### Sunday 2023-03-12 18:37:38 by Matt A. Tobin

Manually Revert Bug 1212323 Parts 2 and 3 where supportsHardwareH264Decoding() uses a promise if MP4 Hardware Acceleration to about:support

This concern was largely Mac-specific but I did leave Part 1 intact because the Mozilla Bug makes a good point that some systems may always software render a 64x64 video (specifically apple but other implementations could adopt this nonsense as well). Personally I want accelerated video.. damn it!

The real question is.. Why was the promise never resolving in the first place? Is it fall out from killing DOM Promise? It used jsval but who the hell knows or even cares.. It works and can once again be queried without jumping through god damned hoops.

---
## [MihirBibhuty/Useful-AI-WEBSITE-LIST](https://github.com/MihirBibhuty/Useful-AI-WEBSITE-LIST)@[f25b011e86...](https://github.com/MihirBibhuty/Useful-AI-WEBSITE-LIST/commit/f25b011e862ae8735067d7b964f42803dd0d8853)
#### Sunday 2023-03-12 19:03:01 by Mihir Bibhuty

Added QuillBot in the list

QuillBot is a is fast, free, and easy to use paraphraser, which according to me makes it one of the best paraphrasing tool on the market. I also provide unique features like the ability to compare outputs from seven different modes, access to a built-in thesaurus to customize your paraphrases, and the option to request for a new output.

D-id.com is a website that uses the most recent generative AI algorithms to enable users to quickly animate their photos. One can make talking avatars using the Creative Reality Studio on the website. The platform, which enables users to create customised videos from their ideas and is said to be supported by Stable Diffusion and GPT-3.

Soundful.com is best to create music. Users can make royalty-free tracks using AI on the website Soundful.com. The platform, offers a simple option for anyone hoping to generate music in a short amount of time. Users can choose a genre of their preference, tailor their inputs, and produce tracks according to their preferences. Additionally, the website provides high-quality music samples.

Memes have evolved into a language in itself. Supermeme.ai is a website through which users can express their ideas while an AI engine generates original memes. More than 110 languages are supported by the website for making memes. Users only need to specify their subject or issue and click "Generate" for the website to function. The website also serves as a search engine for memes.

Mightygpt.com is a website that uses WhatsApp to deliver the ChatGPT functionality right to your smartphone. Speaking with other users on WhatsApp while using ChatGPT is as easy as conversing with any other user.

It is an AI-powered chat companion where you choose your AI friend. You can select between female, male or non-binary and give your Replika a name. As you chat, you earn the XP, and then you can go to the store and purchase and personalize your AI Replika. You can choose between different types of conversation, like relaxing, having fun, or learning. At the store, you can buy more different things for your Replika like clothes, appearance, or even personality traits.

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[d21740b475...](https://github.com/Apogee-dev/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Sunday 2023-03-12 19:58:06 by tmtmtl30

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
## [SuchismitaRout555/ResumeCode](https://github.com/SuchismitaRout555/ResumeCode)@[f77011c362...](https://github.com/SuchismitaRout555/ResumeCode/commit/f77011c36279d41954a491dfcf68a7e84cf5f0c7)
#### Sunday 2023-03-12 20:19:05 by Suchismita Rout

Add files via upload

Sharing a detailed step-by-step breakdown of a 𝐫𝐞𝐬𝐮𝐦𝐞📋 that got shortlisted by 𝐆𝐨𝐨𝐠𝐥𝐞, 𝐌𝐢𝐜𝐫𝐨𝐬𝐨𝐟𝐭, 𝐚𝐧𝐝 𝐀𝐦𝐚𝐳𝐨𝐧!

(You might not be planning to work there for now, but what's the harm in learning?) Feel free to reshare it! 🚀

🌈 Using color-coordination method for easier understanding

📍 𝐏𝐢𝐧𝐤 = 𝐀𝐜𝐭𝐢𝐨𝐧 𝐕𝐞𝐫𝐛𝐬: start each resume bullet with this;
𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #1 to effectively bypass resume scanning software that filters out unqualified employees.

Ex: Led > teamwork skills, designed > creativity skills, automated > technical skills, optimized > outside-the-box thinking, etc. [Use tense accordingly]

📍 𝐘𝐞𝐥𝐥𝐨𝐰 = 𝐉𝐨𝐛-𝐎𝐫𝐢𝐞𝐧𝐭𝐞𝐝 𝐇𝐚𝐫𝐝 𝐒𝐤𝐢𝐥𝐥𝐬: Specific softwares/technologies/skills/tools/platforms based on job title's qualifications.

𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #2 Use at least 3 JDs form target company to form a word cloud & shortlist top skills to showcase on the resume.

📍 𝐎𝐫𝐚𝐧𝐠𝐞 = 𝐒𝐭𝐫𝐨𝐧𝐠 𝐝𝐨𝐦𝐚𝐢𝐧 𝐤𝐧𝐨𝐰𝐥𝐞𝐝𝐠𝐞 𝐰𝐢𝐭𝐡 𝐡𝐚𝐧𝐝𝐬-𝐨𝐧 𝐞𝐱𝐩𝐞𝐫𝐢𝐞𝐧𝐜𝐞 𝐈𝐧𝐝𝐢𝐜𝐚𝐭𝐨𝐫𝐬

𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #3 Recruiters shortlist candidates with 60% of your resume to support your domain knowledge & 28% of your resume to support your soft skills.

📍 𝐆𝐫𝐞𝐞𝐧 = 𝐐𝐮𝐚𝐧𝐭𝐢𝐟𝐢𝐚𝐛𝐥𝐞 𝐫𝐞𝐬𝐮𝐥𝐭𝐬: **MOST IMPORTANT** numbers and percentages showcasing measurable outcomes from your work.

𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #4 Only 41% of resumes include >3 impact metrics & Yes, these are the ones who get a callback from recruiters.

📍 𝐁𝐥𝐮𝐞 = 𝐈𝐦𝐩𝐚𝐜𝐭 𝐬𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭𝐬: Statement structured as the Problem, Action, and Results (PAR) for each one of your work experiences.

𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #4 Always add impact statements as they help you drive recruiters' as well as interviewers' attention to your prior achievements at the workplace.

📍 𝐏𝐮𝐫𝐩𝐥𝐞 = 𝐋𝐢𝐧𝐤𝐞𝐝𝐈𝐧/𝐆𝐢𝐭𝐇𝐮𝐛/𝐏𝐨𝐫𝐭𝐟𝐨𝐥𝐢𝐨 𝐋𝐢𝐧𝐤𝐬:

𝐒𝐞𝐜𝐫𝐞𝐭 𝐓𝐢𝐩 #5 Resumes with robust links & portfolios have 71% higher chances of landing in an interview.

📍 𝐋𝐨𝐰𝐞𝐫 𝐌𝐢𝐝𝐝𝐥𝐞/𝐛𝐨𝐭𝐭𝐨𝐦 = 𝐄𝐝𝐮𝐜𝐚𝐭𝐢𝐨𝐧:
Use reverse chronological order & ONLY mention CGPA if over (7/10 or 3.5/4 point scale). Add Optional Sections: Awards, Relevant Coursework (Tip: Leverage if you have 0 experience in the field you're trying to get into), Others, PORs etc. as per your experience.

📍 𝐑𝐞𝐝 𝐛𝐨𝐱𝐞𝐬 = 𝐒𝐨𝐟𝐭-𝐬𝐤𝐢𝐥𝐥𝐬: Preferred to incorporate in your experience & projects rather than simply mentioning in the "soft-skills" section.

Notes:
- Use Liner, Single Pager format, with 475-600 words not more!
- Use X-Y-Z formula to ace the experience section (Google It!)
- This is a Combinational Resume, Choose wisely from this, "Chronological", "Functional" as per your aim & current years of experience.

Follow Rahul Pandey 👨‍💻⚡for more!

Resume used: PIRATE K. (Thanks for open-sourcing it, buddy)

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[9ccd6ecd74...](https://github.com/PKRoma/Terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2023-03-12 20:21:30 by Mike Griese

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
## [JasmineRickards/T.E.-station](https://github.com/JasmineRickards/T.E.-station)@[ba77b0daae...](https://github.com/JasmineRickards/T.E.-station/commit/ba77b0daae961bb0274e6856a0f1f87934f8c4f4)
#### Sunday 2023-03-12 21:24:10 by JasmineRickards

Merge pull request #35 from IFuckedUpMerging/actually-fix-that-dumb-stupid

[REQ] Fixes Dreamchecker Error + Modsuit Icons

---
## [Saikikusuoisgood/ohmygoat-french-translation](https://github.com/Saikikusuoisgood/ohmygoat-french-translation)@[f0c7cb8c03...](https://github.com/Saikikusuoisgood/ohmygoat-french-translation/commit/f0c7cb8c03cd8b971ae54474bd1bc2a592920d0c)
#### Sunday 2023-03-12 22:25:22 by Saikikusuoisgood

hi vahd

Cock and ball torture From Wikipedia, the free encyclopedia at en.wikipedia.org
Cock and ball torture (CBT) is a sexual activity involving application of pain or constriction to the male genitals. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation or even kicking. The recipient of such activities may receive direct physical pleasure via masochism, or knowledge that the play is pleasing to a sadistic dominant.
Image: Electrostimulation applied on a penis
Contents: Section 1: In Pornography Section 2: Ball stretcher Section 3: Parachute Section 4: Humbler Section 5: Testicle cuff
Section 1: In pornography
In addition to it’s occasional role in BDSM pornography, Tamakeri (literally Ball kicking) is a separate genre in Japan. One notable actress in tamakeri is Erika Nagai who typically uses her martial arts skills to knee or kick men in the testicles.
Section 2: Ball stretcher A ball stretcher is a sex toy that is fastened around a man in order to elongate the scrotum and provide a feeling of weight pulling the testicles away from the body. While leather stretchers are most common, other models are made of steel rings that are fastened with screws causing additional mildly uncomfortable weight to the wearer. The length of the stretcher may vary from 1-4 inches, and the steel models can weigh as much as five pounds.
Section 3: Parachute
A Parachute is a small collar, usually made from leather, which fastens around the scrotum, and from which weights can be hung. Conical in shape, three or four short chains hanging beneath, to which weights can be attached. Used as part of cock and ball torture within a BDSM relationship, the parachute provides a constant drag, and squeezing effects on the man’s testicles. Moderate weights of 3-5 kg can be suspended, especially during bondage. Smaller weights can be used when the man is free to move, when the swinging effect of the weight can restrict sudden movements, as well as providing a visual stimulus for the dominant partner.
Section 4: Humbler
A humbler is a BDSM physical restraint device used to restrict the movement of a submissive male participant in a BDSM scene. The humbler consists of a testicle cuff device which clamps around the base of the scrotum, mounted in the center of a bar that passes behind the thighs at the base of the buttocks. This forces the wearer to keep his legs forward, as any attempt to to straighten the legs slightly pulls directly on the scrotum, causing from considerable discomfort to extreme pain.
Section 5: Testicle cuff
A testicle cuff is a ring-shaped device around the scrotum between the body and the testicles which when closed does not allow the testicles to slide through it. A common type has two connected cuffs, one around the scrotum and the other around the base of the penis. They are just one of many devices to restrain the male genitalia. A standard padlock may also be locked around the scrotum; without the key it cannot be removed.
Some passive men enjoy the feeling of being "owned", while dominant individuals enjoy the sense of "owning" their partners. Requiring such a man wear testicle cuffs symbolizes that his sexual organs belong to his partner, who may be either male or female. There is a level of humiliation involved, by which they find sexual arousal. The cuffs may even form part of a sexual fetish of the wearer or his partner.
However, these are extreme uses of testicle cuffs. More conventionally, the device pulls down the testicles and keeps them there during stimulation, which has a number of benefits:
Making the penis appear longer. Pulling the testicles down and away from the base of the penis stretches the skin over the base of the penis and pubic bone, exposing the additional inch or so of penile shaft that is normally hidden from view. Improving sexual arousal. While some men may be aroused by the feeling of being "owned", the physical feeling of stretching the ligaments that suspend the testicles has an effect similar to the more common practice of stretching one's legs and pointing the toes. Preventing the testicles from lifting up so far that they become lodged under the skin immediately adjacent to the base of the penis, a condition which can be very uncomfortable, especially if the testicle is then squashed by the slap of skin during thrusting in sexual intercourse. Delaying or intensifying ejaculation by preventing the testicles from rising normally to the "point of no return". It is much harder to reach an orgasm.

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[6c978308c7...](https://github.com/nikothedude/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Sunday 2023-03-12 22:35:23 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [jnutt367/galatians](https://github.com/jnutt367/galatians)@[d6dc343f7c...](https://github.com/jnutt367/galatians/commit/d6dc343f7cabd78474fc6f9c412f83df37f42a8d)
#### Sunday 2023-03-12 23:38:35 by Jason Nutt (He/Him) Developer/Creator

Update index.js

Do not be deceived: God cannot be mocked. A man reaps what he sows. 8Whoever sows to please their flesh, from the flesh will reap destruction; whoever sows to please the Spirit, from the Spirit will reap eternal life. 9Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.

---
## [GenevieveBuckley/napari](https://github.com/GenevieveBuckley/napari)@[3ec4be1ae8...](https://github.com/GenevieveBuckley/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Sunday 2023-03-12 23:40:06 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---

