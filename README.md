## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-27](docs/good-messages/2023/2023-02-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,192,086 were push events containing 3,356,524 commit messages that amount to 271,891,736 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [DarkSorrow/TexkyAuth](https://github.com/DarkSorrow/TexkyAuth)@[a543516561...](https://github.com/DarkSorrow/TexkyAuth/commit/a5435165618010e8227c0bf1b00b1e50202eab92)
#### Monday 2023-02-27 00:10:16 by DarkSorrow

fuck you nonce from accountproof you never change ;(

---
## [crawl/crawl](https://github.com/crawl/crawl)@[c65c45c1d4...](https://github.com/crawl/crawl/commit/c65c45c1d4c4d4d01db8334bc56938436b0d3bc0)
#### Monday 2023-02-27 00:16:47 by Nicholas Feinberg

Move the Vaults rune lock inside (hellmonk)

Long ago, Vaults got a 'rune lock' - the requirement that players find
at least one of the fabled Runes of Zot before entering. This was added
so that players would be encouraged to fight at least one of the final
challenges of the Lair branches (Snake, Spider etc) at a time when they
were still challenging. Before this lock was added, wise players fought
those challenges much later, after getting so much XP and loot from Vaults
etc that they were trivial.

This was a big improvement! But there was one downside - lunatic players
who wanted to get the silver or, god forbid, golden rune before getting
any other runes (or even entering the Lair, perhaps!) were blocked from
achieving their dreams. Tragic!

So, this commit lets them do that. You no longer need a rune to enter
the Vaults, but you do need a rune to leave. Wise play probably remains
unchanged,

There is a fairly strongly worded warning for players trying to enter
the Vaults without a rune, with a requirement to type 'yes' to enter
(ala stepping on a Zot trap, entering wizmode, etc). So I'm hoping this
doesn't affect the experience for newer players. If it does, I'll rethink
this!

---
## [Dono7700/git](https://github.com/Dono7700/git)@[a1b8998e15...](https://github.com/Dono7700/git/commit/a1b8998e152ac440fef96497da59e298d362aa1a)
#### Monday 2023-02-27 00:22:28 by Johannes Schindelin

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
## [nim-works/nimskull](https://github.com/nim-works/nimskull)@[c4250cc115...](https://github.com/nim-works/nimskull/commit/c4250cc11536bf6c8922bbd192d2ec39142d46d9)
#### Monday 2023-02-27 00:49:49 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [spurious/chicken-core-mirror](https://github.com/spurious/chicken-core-mirror)@[a9fe465f04...](https://github.com/spurious/chicken-core-mirror/commit/a9fe465f047c644c531b016fbcf7eb43e9bc699e)
#### Monday 2023-02-27 01:01:02 by Felix Winkelmann

Look, git and me just don't get along. Yeah, it's probably all my fault
and everybody uses it, so it must be me, right? So what should one do
when "git am" fails in the presence of conflicts? I certainly don't
know and the documentation is a sad joke, in usual git fashion. Why
do people accept this? Why do we put up with overcomplex tools with
shitty documentation written by people who know git like the back of
their hand written for people who, well, know it like the back of their
hand? Are we just cargo culting along out of fear for being considered
incompetent by our peers? Git as a technology might be very powerful,
but as a tool it is severely broken and follows the unfortunate trend
of just hiding the inability of its authors to design
a proper user interface and properly explaining it behind a facade of
technological obscurantism. This is wrong, version control has NOT been
"solved" and we should be ashamed of failing to do this in a better,
simpler and more usable way.

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[582f5b38cb...](https://github.com/vlggms/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Monday 2023-02-27 01:15:01 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [paholg/helix](https://github.com/paholg/helix)@[973c51c3e9...](https://github.com/paholg/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Monday 2023-02-27 01:33:39 by Michael Davis

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
## [WindSoilder/nushell](https://github.com/WindSoilder/nushell)@[378a3ae05f...](https://github.com/WindSoilder/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Monday 2023-02-27 01:53:41 by Kovacsics Robert

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d55ce0f0bc...](https://github.com/tgstation/tgstation/commit/d55ce0f0bcb6c37113c9ec9f0e37facd99b69625)
#### Monday 2023-02-27 02:57:44 by Jacquerel

Don't create abandoned airlocks with walls underneath them. (#73656)

## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

---
## [Bobthe28th/tgstation](https://github.com/Bobthe28th/tgstation)@[8eb9d376b5...](https://github.com/Bobthe28th/tgstation/commit/8eb9d376b50ed6eab29c4c884d7bc3c53aa33fec)
#### Monday 2023-02-27 03:34:16 by san7890

Improves/Abstracts Suicide A Bit More (#72949)

## About The Pull Request

Basically all of the heavy lifting was done in #72919, but we do a few
key things here that I wasn't able to do then because it was just
fucking massive.

Player Facing Changes:
* hear_blind arg is now a default state and must be specifically
overridden. Pretty much every mob that wasn't a pAI or alien was lacking
this, so let's toss it in as a default now. Let me know if the generic
message I put in for /mob/living sucks and we can go from there.

Code Side Changes:
* suicide.dm now only contains code pertinent to the suicide verb, and
all subtype proc-overrides have been moved to an appropriate file
pertinent to that subtype.
* suicide.dm has also been organized a bit more to aid the previous
change.
* There is only one suicide verb now, implemented on /mob/living. All
the verb does is invoke the handle_suicide() proc, which does all of the
lifting.
* Leaning into *mumble mumble* object-oriented philosophy, the message
we send to the world on suicide is handled on subtype procs, rather than
be in the huge fuck-off message tree I implemented in the earlier PR. It
definitely makes the visible_message() proc not hard to read IMO. This
also means that we can take up a less footprint when we re-use certain
suicide messages (i.e. Silicon), which is nifty too.

i'm probably forgetting something but that's all of the big ones
## Why It's Good For The Game

There is now a very, very common framework for how suicide works across
all living mobs, and it's much easier to override how suicide is
handled. Certain subtypes do their own bullshit thing, but it's quite
easy to account for this on that case-by-case basis. The overall code
takes up a much less footprint that just makes it look nicer.
## Changelog
:cl:
qol: Some mob suicides now have a message that shows to blind people or
people that didn't actually witness the suicide, pretty cool.
/:cl:

---
## [BrandtOgden/CS212-Review-Project](https://github.com/BrandtOgden/CS212-Review-Project)@[168dc1d52d...](https://github.com/BrandtOgden/CS212-Review-Project/commit/168dc1d52d469e447c88b70cc89083ecde448a5f)
#### Monday 2023-02-27 03:40:09 by Ryan Shilling

Added more idiot proofing to create new deliverable (option 3)

i fucking hate this project

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[7cc6934eff...](https://github.com/necromanceranne/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Monday 2023-02-27 04:18:22 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [rurban/qemu-stm32](https://github.com/rurban/qemu-stm32)@[8d0efbcfa0...](https://github.com/rurban/qemu-stm32/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Monday 2023-02-27 06:32:53 by Paolo Bonzini

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
## [jeremyhu/git](https://github.com/jeremyhu/git)@[f44e6a2105...](https://github.com/jeremyhu/git/commit/f44e6a21057b0d8aae7c36f10537353330813f62)
#### Monday 2023-02-27 07:32:40 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[6d158bd3b3...](https://github.com/spockye/Shiptest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Monday 2023-02-27 07:32:46 by spockye

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
## [harryob/cmss13](https://github.com/harryob/cmss13)@[3978cfe70f...](https://github.com/harryob/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Monday 2023-02-27 08:16:47 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

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

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8ab74525c1...](https://github.com/tgstation/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Monday 2023-02-27 08:35:10 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [jamescaracci/Online-Chat](https://github.com/jamescaracci/Online-Chat)@[f5036d6eee...](https://github.com/jamescaracci/Online-Chat/commit/f5036d6eee863dff3fb567bbf3970055ddefcad6)
#### Monday 2023-02-27 08:37:30 by James  Caracci

Online Chat

uscloudminer

Dear user! Due to the new Christmas gift activity of uscloudminer, it is very popular. The uscloudminer data center is increasing the cloud computing power for user recharges in sequence. Please prepare for recharging in advance. In order to get Christmas rewards faster. The system will process it within 12 hours.


My deposit did not go in yet for this transaction for USDT Withdrawal Amount -31.989989 USDT Status Successful Confirmations 50 of 1 Date Jan 03, 2023 08:19:22 From USDT Balance Address TSLnAo9ocKRCFTeK6co2z7vC2cdPwA75Th TxID d097cf93da7d3ca733673b7962c963ad6b8844dcf10370101da79d37b8c8b5b7 Network Tron (TRC20) Fee 1 USDT

tronscan.org/#/transaction/d097cf93da7d3ca733673b7962c963ad6b8844dcf10370101da79d37b8c8b5b7

online link tronscan.org/#/transaction/d097cf93da7d3ca733673b7962c963ad6b8844dcf10370101da79d37b8c8b5b7

tronscan.org/#/address/TSLnAo9ocKRCFTeK6co2z7vC2cdPwA75Th

[Binance.US ] Re: The withdrawal did not show up in my deposit transfer wallet address fot this transaction Inbox Binance.US <support@
binanceussupport.zendesk.com>
; Jan 25, 2023, 12:22 PM (7 days ago) to me ##- Please type your reply above this line -## Your request (2653252) has been updated. To add additional comments, reply to this email. Jordan (Binance.US ) Jan 25, 2023, 09:22 PST Hello James, Thank you for contacting Binance.US Customer Support. I'm Jordan, and I'm with the crypto team here at Binance.US! I'm sorry to hear that you've run into an issue with your withdrawal. I understand that it can be concerning or confusing when a deposit or withdrawal isn't immediately settled as you expect. After investigating your transaction, I can confirm that the assets have been successfully withdrawn from Binance.US to the address: TSLnAo9ocKRCFTeK6co2z7vC2cdPwA75Th Being that the assets were successfully withdrawn from Binance.US, I recommend opening a support ticket with the exchange/wallet associated with the receiving address if you have not seen the assets reflected at their destination. Due to the private nature of crypto transactions, Binance.US is not able to reverse transactions or move assets from wallets that we do not hold the private keys to. In doing so, I also suggest sharing the TXID with the support team associated with the receiving exchange/wallet, as this will help them investigate your transaction. For your convenience, here's the link to the transaction on the explorer: d097cf93da7d3ca733673b7962c963ad6b8844dcf10370101da79d37b8c8b5b7 Outside of this information, I am unfortunately unable to offer a refund, or retrieve the assets for you. However, if you have any other questions, or if you need any additional assistance related to your Binance.US account, please reach back out to me and I will be happy to help. Thanks for being a valued Binance.US customer. Kindly, Jordan Crypto Customer Support Binance.US jamescaracci Jan 25, 2023, 09:13 PST The withdrawal did not show up in my deposit transfer wallet address fot this transaction USDT Withdrawal Amount -31.989989 USDT Status Successful Confirmations 50 of 1 Date Jan 03, 2023 08:19:22 From USDT Balance Address TSLnAo9ocKRCFTeK6co2z7vC2cdPwA75Th TxID d097cf93da7d3ca733673b7962c963ad6b8844dcf10370101da79d37b8c8b5b7 Network Tron (TRC20) Fee 1 USDT This email is a service from Binance.US . Delivered by Zendesk [EPX60Z-XLVE9]

support.binance.us/hc/en-us

i did not receive my last 3 withdrawal amount

My TRC20 USDT Wallet address is TGcsTwTLmfb4mEwYUT1jXRQybGQfpDfGAz

My wallet address is through binance
www.binance.us/

i did not receive my last 4 withdrawal amount

The account manager's application is under review, please be patient. If you have any questions, please contact the administratorTelegram : @UScloudminer_online Account Manager

i put my application in i am still waiting for the answer

---
## [NARESHRAJ701/studday-infinity](https://github.com/NARESHRAJ701/studday-infinity)@[1efc016f1e...](https://github.com/NARESHRAJ701/studday-infinity/commit/1efc016f1e23a4356783f280601f17ea92c0039e)
#### Monday 2023-02-27 09:25:27 by NARESHRAJ R

Add files via upload

I am writing this message to express my sincere gratitude for organizing the Skill-a-thon 1.0. It was an incredibly well-planned and executed event, and I am truly grateful for the opportunity to have participated.

The Skill-a-thon 1.0 was an amazing experience that challenged me to think outside the box and collaborate with other like-minded individuals. I appreciated the effort that you and your team put into ensuring that all participants were well taken care of and had everything they needed to be successful. The venue, refreshments, and technical support were all top-notch, and I felt very comfortable throughout the entire event.

The opportunity to work on real-world problems and come up with innovative solutions was truly inspiring, and I learned a lot from the experience. I am grateful for the opportunity to have met so many talented individuals and networked with industry professionals. I am confident that the skills and knowledge that I gained during the hackathon will serve me well in my future endeavors.

Once again, thank you for organizing such an amazing event. I appreciate all the time and effort that you put into making it a success. I look forward to participating in future events and hope to have the opportunity to work with you again.

Best regards,
Team Sun Star Moon

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Monday 2023-02-27 09:35:34 by Romain Derie

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
## [Xen0byte/next.js](https://github.com/Xen0byte/next.js)@[268dd6e80b...](https://github.com/Xen0byte/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Monday 2023-02-27 10:55:49 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[605b4e3099...](https://github.com/treckstar/yolo-octo-hipster/commit/605b4e309970bbd2a1a94e8f6dd3e5b2b27cc615)
#### Monday 2023-02-27 11:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[fc1e2e5e26...](https://github.com/cmss13-devs/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Monday 2023-02-27 12:23:32 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [gabxyz/bookmarkxyz](https://github.com/gabxyz/bookmarkxyz)@[7f54c817c6...](https://github.com/gabxyz/bookmarkxyz/commit/7f54c817c6ad1cd51c1e7a7304cfebedaa52e575)
#### Monday 2023-02-27 12:23:46 by gabxyz

add `bookmark-form.tsx` and `list-form.tsx` components

* `components/bookmark-form.tsx` adds a dynamic form that is meant to be used inside another form. It has it's own validations and it's linked to the outer form using `useFormContext`. I'm gonna try to explain what is happening the best I can:
 - local validation using `useForm` and `BookmarkSchema`. type, index and initialData props are used to load existing bookmark data or empty form for a new one.
 - `useFormContext` is used here to get the control method of the outer form, this is going to be used as the control in the `useFieldArray` so that we can use the field array methods inside this form and then get these values in the outer form.
 - `onSubmit` function handles validation of the local form and if successful, checks the type and performs an action. either calls `append` or `update` method and resets the form and closes the modal.
 - `useEffect` is being used to reset the form values if the modal is closed. It resets the errors and changes not submitted.

* `components/list-form.tsx` adds the outer form that has it's own validations and handles api mutations onSubmit:
 - local validation using `useForm` and `ListSchema`. This one wraps the form around a `FormProvider` passing the methods from `useForm` to use the context inside the inner form.
 - `BookmarkForm` component is added with type="add" to render the form to create a new bookmark.
 - to render the existing bookmarks list, we use `getValues` method and map through the values to render the bookmark links along with another `BookmarkForm` component, now using type="update" + index and bookmark from the map values to define what is going to be edited.
 - `onSubmit` function handles the mutations on the db based on the type of the list. It uses fetch to call the api route with the correct http method.

(*) yeah, this is extremely confusing and took me a long time to build this. it's messy, but it works how i wanted so that's cool.
i fucking hate forms :)

---
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[b4954e1402...](https://github.com/PalJohnson/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Monday 2023-02-27 12:42:04 by carlarctg

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
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[b53c9f0531...](https://github.com/PalJohnson/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Monday 2023-02-27 12:42:04 by carlarctg

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
## [WycliffeAssociates/DOC](https://github.com/WycliffeAssociates/DOC)@[3f23ada23b...](https://github.com/WycliffeAssociates/DOC/commit/3f23ada23b74fc17ce5af2fb1a12e8ea04f568c6)
#### Monday 2023-02-27 14:33:45 by linearcombination

Docx support and v1 UI candidate featuring basic and full uis (#91)

* Add initial proper docx support

Docx is the new preferred document output format as it is more easily
editable for translators.

This commit adds native docx support and an associated path for it in
the UI and backend as well as a test suite for it.

Supporting Docx meant adding a new code path that doesn't convert from
a finished HTML document to Docx in a wholesale fashion (in comparison
with conversion to PDF or ePub). Instead, the Docx is built up from
HTML snippets intermingled with required low-level Docx manipulations
to control one or two column layout and ultimately Docx template use
too. In turn this means that certain UI changes were necessary. The UI
changes include making the user choose either PDF, ePub, or Docx
rather than being able to choose all of them at once if desired. This
has the added benefit that a user can no longer choose to create three
different output formats in one go and thus the time for the request
to be fulfilled will be greatly reduced in such cases which will also
make the user feel the system is snappier (objectively, but more
importantly, subjectively).

Another UI change not directly related to Docx support is that we have
removed the drop down control to select chunking size. Instead, the UI
always sends chapter chunk size now and never verse chunking. Verse
chunking was decided to be of no value for translation purposes at
this time and verse interleaving is very costly in terms of
performance which makes for a bad UX. It can be resuscitated from git
history later if we want it back in the future though it is hard to
imagine now that happening.

Note too that Docx support does not include one of the layout options
available to HTML, PDF, and ePub: two column side by side languages.
This was never vetted as a needed requirement and has not been used or
requested for some time. It still exists as an option in HTML, PDF,
and ePub output formats as sort of a showcase for what can be done.
Also this layout would be much more difficult to implement in Docx.

This commit does not yet accommodate fonts for certain languages in
Docx format. To do so in Word will have to be the subject of a future
PR and appears to be of some complication. More research is needed.

There are also a few miscellaneous commits related to better naming,
a fix to configuration in docker-compose-override.yml, changing chunking
of several tests from the no longer used verse chunk size to chapter
chunk size instead, and remove commented out link in a Jinja HTML
template.

In a coming PR we will likely also want to ensure sources present no
linking in the generated doc. For now, for some sources, there are
some dead links in PDF, ePub, and Docx output formats. There is a
great deal of heterogeneity in links in the source. We successfully
handle tens of types, but there are apparently yet more that exist and
sometimes they are just malformed in the sources.

* Update non-docx assembly strategies interleaving order

Update the interleaving strategies for HTML, PDF, and ePub to follow
the order of interleaving that is implemented in the docx assembly
strategies which were designed to adhere to the product owner's latest
requirements updates as exemplified in a Word file that acts as
template. Specifically, book intro materials (TN and BC - BC wasn't
presented in the example, but intuition says it could follow TN book
intro) followed by USFM and footnotes, followed by chapter intro,
followed by verse-level translation notes, followed by other resource
assets (TQ, secondary USFM), and finally TW at language level. The old
order was book intros, chapter intro, USFM, verse-level TN notes, then
other remaining resource assets (with some variation).

* Update Makefile

* v1 UI candidate and full ui version both accessible and linked

- [x] basic version, i.e., v1, is available at #/v1/.

- [x] full version is available at #/

- [x] You can switch between them using a link in the About page of either

- [x] The Mast (the top area of the app where the logo and tab menu
  items live can be shown or hidden based on a bujild-time configuration
  setting in source at DOC/frontend/.env: VITE_SHOW_TOP_MATTER (which
  controls this for the full version) and
  VITE_SHOW_TOP_MATTER_IN_V1 (which controls this for the basic, v1,
  version). The usefulness of this comes into play if you want to, say,
  display the app without the Mast so as to integrate into an iframe
  within BIEL. If the app lives at its own link (with respect to
  navigation) then likely you would want the Mast kept in place.

- [x] Similarly, in the basic ui version, v1 candidate, there is a
  flag in the same .env file as above for showing or not showing
  resource types. We choose the approved USFM and TN types that are
  also listed in translations.json for the user. As such there is not
  a functional reason to show the resource types to the user. However, it
  likely a less surprising UX for the user if they are at
  least shown what resource types the system chose for them. The
  product owner will decide which option is best.

- [x] We didn’t yet actually have anything useful in the
  hamburger menu at the upper right in the Mast.  Thus, for now, I
  have disabled the ‘Hamburger ‘ menu in the top right of the Mast in
  both the basic and full UIs.

- [x] For now, the basic version, i.e., v1, defaults to PDF output.
  Why? Because many gateway languages use special fonts. As you
  likely recall from recent emails the handling of such fonts in
  Word document generation, especially for multi-language
  documents, is yet unsolved. I do have a lead on a couple
  approaches that may prove useful, but there is more work to be
  done there which will be the subject of a future PR or update to
  this PR if it has not yet been merged when I return to it.
  In the meantime, if you want to see the docx output for a gateway
  language simply switch to the full ui version (using the
  link in the About page or by manipulating the browser location URL
  to #/v1/) and request to generate Docx for said gateway language and
  view the result. For many gateway languages the result will be just
  fine, but for many which have special fonts you’ll get a document
  with fine structure (unless the underlying resource source assets
  are malformed or incomplete - this is true of many languages)
  but filled with unicode-font-missing boxes. Some backstory: Our PDF
  output comes from HTML that is rendered headless by webkit and the
  browser handles the fonts transparently (assuming they are installed
  into the environment the browser is running in), whereas with Docx
  generation things are more complicated.

    - [ ] What is likely going to be needed is a map of language to
      font needed for each language as well as the language’s
      identifying code (from
      Word’s perspective -probably an ANSI code or omething - see
      https://stackoverflow.com/questions/36967416/how-can-i-set-the-language-in-text-with-python-docx
      for example). For v1, we’ll only need that just for the gateway
      languages, but later for all languages. Hopefully there is a
      different less tedious way to solve this, but the link provided
      is the closest I have come so far as an approach that might work.
      With more time for researching it might turn out to be less
      onerous. Let's hope so.

- [ ] Other more minor items like font darkness/lightness, etc on
  various controls will get my attention before the deadline for
  launch.

---
## [raymondbarrett/ECE4180-Sp2023](https://github.com/raymondbarrett/ECE4180-Sp2023)@[81eec9e051...](https://github.com/raymondbarrett/ECE4180-Sp2023/commit/81eec9e051f1cebc32ce2eb19ed1a4cc92eb1bd8)
#### Monday 2023-02-27 14:43:45 by mshakula

HALLELUJAH HOLY SHIT IT COMPILES.

FUCK USING MBED AND FUCK THEIR "DEPENDENCY RESOLUTION" FUCK THE TOOLS. EVERYTHING IS JUST IN THE REPO IN TREE, HOW SHIT IS THAT LOL.

---
## [KermityOwen/Trash-Muncher-Webapp](https://github.com/KermityOwen/Trash-Muncher-Webapp)@[c65363093c...](https://github.com/KermityOwen/Trash-Muncher-Webapp/commit/c65363093cb2a2a2e2e32d16088016ac2f8dcb7e)
#### Monday 2023-02-27 14:46:17 by Owen Lee

scheduler monlkey-paytch

fucking bullshit threading shit tahat took wayyy too long fml

---
## [dkoz/DarkRP](https://github.com/dkoz/DarkRP)@[70733fd592...](https://github.com/dkoz/DarkRP/commit/70733fd5928367e97070777b7aa7561c6c6bc676)
#### Monday 2023-02-27 14:51:22 by FPtje

Clearing decals doesn't fix lag.

Stop fucking pressing that god damn button every 10
motherfucking seconds.

---
## [KevinRizzoTO/wasmtime](https://github.com/KevinRizzoTO/wasmtime)@[1efee4abdf...](https://github.com/KevinRizzoTO/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Monday 2023-02-27 14:55:57 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [nielsb/net-snmp](https://github.com/nielsb/net-snmp)@[b0f82764f4...](https://github.com/nielsb/net-snmp/commit/b0f82764f4ab0b8c6d93378a9b5c2927f2b09509)
#### Monday 2023-02-27 15:15:42 by Bart Van Assche

Spelling: Change 'demon' into 'daemon'

From https://en.wikipedia.org/wiki/Daemon_(computing):

Many people equate the word "daemon" with the word "demon", implying some
kind of satanic connection between UNIX and the underworld. This is an
egregious misunderstanding. "Daemon" is actually a much older form of
"demon"; daemons have no particular bias towards good or evil, but rather
serve to help define a person's character or personality. The ancient
Greeks' concept of a "personal daemon" was similar to the modern concept of
a "guardian angel"-eudaemonia is the state of being helped or protected by a
kindly spirit. As a rule, UNIX systems seem to be infested with both daemons
and demons.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[41ad2898da...](https://github.com/treckstar/yolo-octo-hipster/commit/41ad2898da31564025893316c57ced05341d9e9b)
#### Monday 2023-02-27 15:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [PA-GK/android_frameworks_base](https://github.com/PA-GK/android_frameworks_base)@[60574f3993...](https://github.com/PA-GK/android_frameworks_base/commit/60574f39935a24561d806850e2be6a424ff8a9e5)
#### Monday 2023-02-27 15:39:44 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [00ze-cyclone/Yogstation](https://github.com/00ze-cyclone/Yogstation)@[818973e1e9...](https://github.com/00ze-cyclone/Yogstation/commit/818973e1e91edd0d62357f0ca4361916fb1d3f69)
#### Monday 2023-02-27 15:51:17 by wejengin2

fixes some issues in infiltrator base (#17861)

* huh

* man

* adds griddle

* that's really funny but fuck you

---------

Co-authored-by: Byemoh <baiomurang@gmail.com>

---
## [highlight/highlight](https://github.com/highlight/highlight)@[ae53ba8124...](https://github.com/highlight/highlight/commit/ae53ba81243e670f52ea81fe5e489948bdf17302)
#### Monday 2023-02-27 17:51:47 by Eric Thomas

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
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[3415576209...](https://github.com/seanpdoyle/turbo/commit/3415576209a1b19902f6afa8ee924e3ee5eec538)
#### Monday 2023-02-27 18:09:09 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [nik707/Citadel-Station-13-RP](https://github.com/nik707/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/nik707/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Monday 2023-02-27 18:14:41 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[b2f0f35f3a...](https://github.com/Hekzder/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Monday 2023-02-27 19:59:37 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [Munkybooty/dash](https://github.com/Munkybooty/dash)@[aec7441ac2...](https://github.com/Munkybooty/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Monday 2023-02-27 21:06:51 by Wladimir J. van der Laan

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
## [JasmineRickards/T.E.-station](https://github.com/JasmineRickards/T.E.-station)@[6bcb2a7872...](https://github.com/JasmineRickards/T.E.-station/commit/6bcb2a787236007f597dd7eed358cd9c6c8712fb)
#### Monday 2023-02-27 21:16:14 by JasmineRickards

Merge pull request #11 from IFuckedUpMerging/pizza-pasta-oh-god-is-that-tony-what-the-fuck-dude.-oh-my-god-dude-he-had-a-family-what-the-fuck.-holy-shit.-oh-my-fucking-god,-my-insides,-everything-aches.-what-the-FUCK-man.-WHAT-THE-FUCK-

1984s Soylent Green

---
## [Eagletanker/coolstation](https://github.com/Eagletanker/coolstation)@[e424304790...](https://github.com/Eagletanker/coolstation/commit/e424304790a06573bfefbaa832c73a61f25ed6e1)
#### Monday 2023-02-27 21:46:05 by bobskunk

PIZZA PASTA PUT IT IN A BOX

SHIT MY ASS AND FUCK IT LIKE A FOX

---
## [SeedSigner/seedsigner](https://github.com/SeedSigner/seedsigner)@[d2a657f2d4...](https://github.com/SeedSigner/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Monday 2023-02-27 21:51:53 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [Zaidannaim91/Takeda-Aranobu](https://github.com/Zaidannaim91/Takeda-Aranobu)@[c3f654a091...](https://github.com/Zaidannaim91/Takeda-Aranobu/commit/c3f654a091e42a9b056147c40cc41b6f98810646)
#### Monday 2023-02-27 22:33:24 by Zaidannaim91

Create [Takeda Aranobu] Netorare Junior Girlfriend - Taken and Fucked Behind His Back

---
## [CommE2E/comm](https://github.com/CommE2E/comm)@[fea1dddf0c...](https://github.com/CommE2E/comm/commit/fea1dddf0ca5fd95d62e41c1250f65c3520ef61f)
#### Monday 2023-02-27 23:56:21 by Ashoat Tevosyan

[keyserver] Make sure we fetch username of all notif recipients

Summary:
This honestly probably isn't necessary, since we already fetch usernames for all thread members, and you shouldn't be receiving a notif unless you're a thread member.

But it doesn't hurt to add this to the set here, and there might be a scenario in the future where somebody is able to receive a notif without being a thread member.

Depends on D6870

Test Plan: There's not much to test here, to be honest... I actually think this diff is a no-op in the current scenario. It's more about future-proofing. We should always fetch the recipient's username

Reviewers: atul, ginsu

Reviewed By: atul

Subscribers: tomek

Differential Revision: https://phab.comm.dev/D6871

---

