## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-20](docs/good-messages/2023/2023-01-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,292,537 were push events containing 3,318,546 commit messages that amount to 242,520,560 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [git/git](https://github.com/git/git)@[69bbbe484b...](https://github.com/git/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Friday 2023-01-20 00:17:36 by Jeff King

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[a30fb1438a...](https://github.com/cockroachdb/cockroach/commit/a30fb1438a6f1f99ebf2a27695e89d4b4e51cf8f)
#### Friday 2023-01-20 00:34:37 by craig[bot]

Merge #93153 #93325 #93354 #93545 #93557 #93563 #93618

93153: rttanalysis: don't count leasing the database desc r=andreimatei a=andreimatei

A bunch of rtt-analysis tests were counting a request for leasing the database descriptor. This is not interesting. This patch makes the test framework lease it first through a "USE" statement.

The number of KV requests required for leasing is currently mis-counted. We count 1, but in reality it's 4. A different patch will correct the miscounting that, at which point that would be too significant for the tests.

Release note: None
Epic: None

93325: multitenant: retain range splits after TRUNCATE for secondary tenants r=knz a=ecwall

Fixes #69499
Fixes #82944

Existing split points are preserved after a TRUNCATE statement is executed by a secondary tenant.

Release note: None

93354: tracing: disallow children of sterile span with different Tracer r=andreimatei a=andreimatei

Before this patch, creating a "child" of a sterile span with a different Tracer than the one used to create the sterile span was tolerated - on the argument that sterile spans don't actually get children (the would-be child span is created as a root), so the arguments for not allowing a children to be created with different tracers don't apply. At the same time, creating a child of a noop span with a different Tracer than the noop span's Tracer was documented to not be allowed. In practice, it was, because the code was confused [1].

This patch disallows creating children of sterile spans with a different tracer, for consistency with all the other spans. The patch also makes it a panic for the children of noop spans to be created with a different Tracer.

This is all meant as a cleanup / code simplification.

[1] WithParent(sp) meant to treat sterile spans differently than noop spans but it was using sp.IsSterile(), which returns true for both. As such, it was unintentionally returning an empty parent option. startSpanGeneric() meant to check the tracer of parent noop spans, but it was failing to actually do so because it was going through the opts.Parent.empty().

Release note: None
Epic: None

93545: sql: make SHOW RANGES FOR TABLE include all indexes r=ajwerner a=knz

Informs #80906.
Fixes #93546.
Fixes #82995.

Release note (backward-incompatible change): `SHOW RANGES FOR TABLE`
now includes rows for all indexes that support the table. Prior to
this change, `SHOW RANGES FOR TABLE foo` was an alias for `SHOW RANGES
FOR INDEX foo@primary`. This was causing confusion, as it would miss
data for secondary indexes. It is still possible to filter to just the
primary index using `SHOW RANGES FOR INDEX foo@primary`.

The statement output now also includes the index name.

93557: syntheticprivilegecache: scan all privileges at startup  r=ajwerner a=ajwerner

#### syntheticprivilegecache: move caching logic out of sql
This is a pure refactor to move the logic for caching synthetic privileges
from the sql package. This will make it easier to add features later.

#### syntheticprivilegecache: scan all privileges at startup 


Fixes https://github.com/cockroachdb/cockroach/issues/93182

This commit attempts to alleviate the pain caused by synthetic virtual table
privileges introduced in 22.2. We need to fetch privileges for virtual tables
to determine whether the user has access. This is done lazily. However, when a
user attempts to read a virtual table like pg_class or run SHOW TABLES it will
force the privileges to be determined for each virtual table (of which there
are 290 at the time of writing). This sequential process can be somewhat slow
in a single region cluster and will be very slow in an MR cluster.

This patch attempts to somewhat alleviate this pain by scanning the table
eagerly during server startup.

Release note (performance improvement): In 22.2 we introduced privileges on
virtual tables (system catalogs like pg_catalog, information_schema, and
crdb_internal). A problem with this new feature is that we now must fetch those
privileges into a cache before we can use those tables or determine their
visibility in other system catalogs. This process used to occur on-demand, when
the privilege was needed. Now we'll fetch these privileges eagerly during
startup to mitigate the latency when accessing pg_catalog right after the
server boots up.

93563: pgwire: handle decoding Geometry/Geography in binary r=rafiss a=otan

Resolves #81066
Resolves #93352

Release note (bug fix): Previously, CockroachDB would error when receiving Geometry/Geography using binary parameters. This is now resolved.

93618: cli,cliccl: move some mt commands to cliccl r=ajwerner a=ajwerner

Part of #91714

Epic: none

Release note: None

Co-authored-by: Andrei Matei <andreimatei1@gmail.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>
Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [emma-zhong/687b-spinup](https://github.com/emma-zhong/687b-spinup)@[fd9a13863e...](https://github.com/emma-zhong/687b-spinup/commit/fd9a13863ee56511d96de6d656917d78ecb14d10)
#### Friday 2023-01-20 01:00:16 by LeoniSayat

working on roller, i hate my life and this programming skills

---
## [PrettyPsychoForAWolf/sunset-wasteland](https://github.com/PrettyPsychoForAWolf/sunset-wasteland)@[f7f7ae2cfc...](https://github.com/PrettyPsychoForAWolf/sunset-wasteland/commit/f7f7ae2cfc1c91d2df5bfdbd7895e7ab2c6eb4d3)
#### Friday 2023-01-20 01:06:31 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[972c350665...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/972c35066535665b36788e2b59d9e9bf6429bbb9)
#### Friday 2023-01-20 01:21:53 by Zonespace

Mirror #71906 (#18666)

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.

![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR:
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[79ec70748e...](https://github.com/git-for-windows/git/commit/79ec70748edac5e68f71f062fe0ec05487a5c441)
#### Friday 2023-01-20 01:40:37 by Johannes Schindelin

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
## [srgrusso/android_kernel_oneplus_sdm845](https://github.com/srgrusso/android_kernel_oneplus_sdm845)@[1e0dacdd93...](https://github.com/srgrusso/android_kernel_oneplus_sdm845/commit/1e0dacdd936695269de5c3256ce5c57871b13a8d)
#### Friday 2023-01-20 03:23:54 by Jason A. Donenfeld

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
## [gubrus50/Minecraft-Development-Tools](https://github.com/gubrus50/Minecraft-Development-Tools)@[37d3d22984...](https://github.com/gubrus50/Minecraft-Development-Tools/commit/37d3d22984b03b0ed3e4989b1015411593e349ff)
#### Friday 2023-01-20 03:45:16 by McRaZick

development tools launch

Too many things, and I'm tired to explain to myself so...

+Fixed many bugs (especially the dtConfig / in general, development tool's validation before it's inclusion)

+Integrated launch functionality, development tools are now displayed in #iframeBody when launched with a Run button.

+Made a return button functional, user is able to exit from development tool back to the launcher GUI.

+Changed help-tag function to funtionalizeNodesHelpTag()

+Included createInterval() and other related to this function's functions XD In preload.js ? Or index.js forgot, basically, If I remember correctly, one of launcher function's has now a global Interval object that helps apply development tool's "menu" (which I'm about to explain what it is)

+Included new requirement for development tool's creation at dtConfig "menu" -> menu.html. These are footer's .buttonDefault. So, any development tool is now able to replace the layout of these buttons which I refer to as menu.

There are two new classes for doubble and triple button layouts. .panelTriple and .panelDoubble... XD I wanna cry.... I misspelt the "double"... I'll fix that next time.

+Use is now able to zoom some of the editor's contents at "Command Creation Generator" development tool.
Although design is not final.

------------------------------------
There is probably more but I can't remember and I'm about to die from lack of sleep. Anyways future me:

- Find a split function of something, a LONG message at preload.js, you'll know what to do.

and

- Improve the design of the .zoomContainer at "Command Creation Generator" development tool.

- Try to create a loading screen as development tool is being launched to the <main-display>'s #iframeBody.

- Please fix these ugly scrollbars at "Command Creation Generator" development tool's <editor-tool name="container">

- At last, there is last bug, you are to be blamed for this awful method of integrating "menu". On rare occasions, I can't produce this bug on will, the development tool's menu is not removed as user return's to launcher's original GUI. Solution is simple, store main button's in a global variable or something, and just reuse that data when importing, some async functions before importing the original menu as development tool's is being removed and you'll good to go.

Have fun in hell soon if you don't organise this project's code. I'm having issues trying to find the necessary things. Split these libraries into own .js files for my sanity.

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[02c42ec77b...](https://github.com/kleinerm/Psychtoolbox-3/commit/02c42ec77bd1fc2aff5146d6515e9f0d573555dd)
#### Friday 2023-01-20 04:21:13 by Mario Kleiner

PsychOpenXR[Core]: Implement optional multi-threaded 2D presentation mode.

This for presentation in 2D (mono or stereo) presentation mode, where
one or two (supposedly) head-locked OpenXR quad_layers are used for monoscopic
or stereoscopic image presentation. Ie. no use of OpenXR projection_layers,
which always need permanent closed-loop head tracking to work. According to
spec, head-locked quad_layers should be head-locked, static wrt. to any head
movement. However, as it turns out, some runtimes, e.g., SteamVR on both Linux
and Windows, do not work well at all if an animation loop isn't constantly
running at full HMD framerate, even for quad_layers. Under SteamVR, these 2D
views jitter / vibrate / jerk around in an annoying and disorienting fashion
if the animation loop runs too slow, takes pauses and restarts etc., making
use of the HMD as a "strapped onto the head" mono monitor, or as a stereo
monitor for binocular presentation almost unbearable.

Behaviour on my machine darlene is as follows:

- Linux + Monado: Absolutely perfect! Static views as expected even for
  long pauses, IFI's, stopped script loops with no Screen('Flip').
  Monado is also the only system that respects the .displayTime target
  onset time specification as the spec requires.

  -> No need for extra action.

- Windows + OculusVR: Mostly works fine with static views, but in some
  cases one might get the "sandclock" warning, a black screen or a stuck
  script.

  -> Mostly no need for extra action, some timing hacks should do.

- Linux + SteamVR: Complete jittery/vibrating/jerking mess.

- Windows + SteamVR with output to Rift CV-1 via OculusVR runtime, ie.
  not using SteamVR's own VR compositor, but OculusVR: Gives static
  images as expected for stopped animation loops. But resuming a loop
  (or just having long IFI's which is the same as stop -> resume from
  the runtimes PoV) causes massive jerks and jumps.

  -> SteamVR on all OS'es needs help to get to acceptable results.

So, multi-threading to the rescue: This commit allows to optionally
enable a separate background thread which tries to runs the VR presentation
cycle at having at maximum HMD refresh rate, e.g., 90 fps for a Rift, all
the time, this way avoiding the animation loop from ever stopping or even
throttling from the XR runtime and compositor perspective.

We allocate and assign a dedicated OpenGL context (the one that Screen()
creates for use with its flipperThread, but which would go unused as the
flipperThread has no use for OpenXR sessions).

Startup of a session is always single-threaded on the main thread, to
get initial flips and sync-up with the XR compositor, getting to session
state XR_SESSION_STATE_SYNCHRONIZED <-> VISIBLE <-> FOCUSED, and the
initial set of framebuffer textures attached. Shutdown of a session with
final present is also done single-threaded on the main thread.

Full "head tracked 3D rendering" with a closed track -> do stuff -> render
-> present loop, and use of XR projection_layers is also done single-threaded,
as that only makes any practical sense with a tight renderloop implemented
in Matlab/Octave/[Python?] script.

The "2D" modes which use quad_layers and (usually) don't involve (or need)
head tracking and dynamic head pose driven fast closed loop rendering will
switch to multi-threading:

The thread runs in an infinite loop, doing xrWaitFrame -> xrBeginFrame ->
xrEndFrame cycles, resubmitting the same current most recently released
XR swapchain images each HMD video refresh cycle / compositor work cycle,
to keep away from client timeouts or throttling or stop->resume effects,
trying to kee the XR compositor happy.

The script, via Screen('Flip', win [, tWhen]) -> PsychOpenXRCore('PresentFrame')
will submit new rendered content as it wishes, with tWhen target present
time attached. In each work cycle, the thread checks predictedDisplayTime
for the upcoming xrEndFrame() call against tWhen. Iff
precictedDisplayTime >= tWhen, it is time to latch the new rendered stimuli,
by xrReleaseSwapchainImage() before the xrEndframe(), then acquiring new
swapchain images for the next user script render cycle.

predictedDisplayTime is used as best estimate of when the new stimulus
frame will show. An imperfect, and optimistic, guess, iow. returned
Screen('Flip') timestamps may be too optimistic, earlier than true
onset. However, as lots of testing showed, without a proper official
OpenXR timestamping extension, there isn't any way to do better than
that - It is what it is...

This now means we have two separate present code-paths for single (PresentExecute)
vs. multi threaded (PresentCycle) operation. And the need for locking and
condition variables for avoidance of race conditions, data corruption on
shared data, blowing up the OpenXR runtime, and separate OpenGL contexts
between main and XR thread, all with need for proper management and state
transitions. This is the rabbit hole of potential threading bugs in our code
and -- even more likely -- OpenXR runtime bugs, that i wanted to avoid going
down. But unfortunately not everything can be as well done as Monado, and
SteamVR is so far quite awful quality-wise as of January 2023, so here we
are...

-> WIP backup commit. Doesn't crash/hang/malfunction in any obvious ways.
   on Linux with Monado or SteamVR + Monado SteamVR driver plugin for the
   Oculus Rift CV-1. Not yet tested on Windows or with other HMDs.
   I'm sure it has remaining bugs, but this serves as a baseline.

---
## [Slyssy/pm-cinch-frontend](https://github.com/Slyssy/pm-cinch-frontend)@[b52dc59ac0...](https://github.com/Slyssy/pm-cinch-frontend/commit/b52dc59ac008af0841fa87786630b2a6553af2d6)
#### Friday 2023-01-20 05:17:18 by Stephen

I did all kinds of bullshit to make this mother fucker post a project. I finally got it to work. I learned some shit, but mother fucker that was frustrating

---
## [samsung-mt6768-dev/android_kernel_samsung_a31](https://github.com/samsung-mt6768-dev/android_kernel_samsung_a31)@[fe327fe8bf...](https://github.com/samsung-mt6768-dev/android_kernel_samsung_a31/commit/fe327fe8bf635ad1f18c79b8aa00a6c2301fd14f)
#### Friday 2023-01-20 06:18:44 by George Spelvin

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
Signed-off-by: 7Soldier <reg.fm4@gmail.com>

---
## [harry10-git/Darshan](https://github.com/harry10-git/Darshan)@[01637b8f26...](https://github.com/harry10-git/Darshan/commit/01637b8f2654bf7c139793129deb4adf05015a92)
#### Friday 2023-01-20 06:20:29 by Triya

Home page tags text added

BEACHES:
Manipal- Where the land greets the Ocean again. There is a beach here for all your moods. All the adieu is for you to decide on which beach you want to trod on and get a cab. Your Manipal Darshan is not done without the beaches.

MOUNTAINS:
The Arabic Sea on one side and the Western Ghats on the other. Manipal offers you a number of hills and mountain treks. You ought to camp on the heights of these mountains amidst the clouds and cold breeze of the Western Ghats.

TEMPLES:
This land is bestowed with tradition alongside the nature. The numerous temples, old and new, are an embodiment of the belief of the men of the land, as well as architectural excellence. Begin your Manipal Darshan with the Temples.

CLUBS:
The student town has an alluring night life with Clubs and Pubs all around the town. Dance your heart out with your friends at the amazing clubs in Manipal. Going out Club hopping late night is a must do in Manipal.

RESTAURANTS:
The land of Manipal is a buffet of cuisines hailing from different corners of the world. An Indian breakfast, Chinese lunch and Italian dinner: make your pick for your meals with Restaurants in and around Manipal.

ROAD TRIPS:
Got a days leave? Why sit in your rooms when you can have short road trips to nearby places. Discover a gallon of road trip ideas from Manipal and add them to your list for your next small vacation. Rent a bike and get going.

---
## [Casey-Hofland/ADarkFairytale](https://github.com/Casey-Hofland/ADarkFairytale)@[4e0920c9be...](https://github.com/Casey-Hofland/ADarkFairytale/commit/4e0920c9bed45833742b22a9c0105b00444997f6)
#### Friday 2023-01-20 07:32:38 by CaseyDeCoder

Changed Folder Structure

**What Changed and Why?**
Changed Code directory into A_Dark_Fairytale/Scripts directory
and changed Shared directory into A_Dark_Fairytale/MaterialLibrary directory.

This follows the Folder Structure we're implementing where all of our game assets are in a root folder with the name of our game (currently A_Dark_Fairytale)

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Change URP Quality Settings

**What Changed and Why?**
Added Decals and Outline Renderer Features to all the renderers for consistency and changed some settings for a more consistent experience across Quality Settings.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Add NormalTextureImporter

**What Changed and Why?**
If you import a texture whose name starts with T_ and ends with _N it *should* import as a Normal Texture (but doesn't always, reason unknown)

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Fix AntiAliasing quality setting

**What Changed and Why?**
AntiAliasing was changed in a previous push, but it was missing this change.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Change PrototypeReferenceChecker to autorun on Save

**What Changed and Why?**
PrototypeReferenceChecker used to automatically run every time the Unity Editor compiled. However, as this is an action that artists will likely never come across, the script has been changed to run every time you hit save. This allows for way clearer error messages, at a moment that they matter.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Add a Recommended Camera Preset

**What Changed and Why?**
Added a Recommended Camera Preset as I fear my carefully selected settings may get lost otherwise.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Change SampleScene

**What Changed and Why?**
Will update the SampleScene to include all the latest changes like outlines, an MAOS Decal preview, as well as a cool new skybox to see what we can do with it.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

Fix VolumeUpdater stack overflow

returning a new Coroutine in the coroutine caused a stack overflow after some time. The new implementation starts a completely separate coroutine.

Move Files

**What Changed and Why?**
A_Dark_Fairytale was renamed to ADarkFairytale to be more in line with our own naming convention. All custom files have been moved under a folder named "ADarkFairytale" and the naming validator has been updated to include all types for filtering.

Signed-off-by: CaseyDeCoder <hofland.casey@gmail.com>

---
## [JariBou/TIGRAW](https://github.com/JariBou/TIGRAW)@[9d5f589f46...](https://github.com/JariBou/TIGRAW/commit/9d5f589f4659d3294155c6f7fa658e37265c88bd)
#### Friday 2023-01-20 08:22:08 by Jari Bou

I FUCKING FIXED THIS SHIT DON'T BLOODY FORGET TO UNSUBSCRIBE TO EVENTS!!!!!

---
## [Enalean/tuleap](https://github.com/Enalean/tuleap)@[40e2be557c...](https://github.com/Enalean/tuleap/commit/40e2be557cbb16e0972f49af4beaa39636afcc3b)
#### Friday 2023-01-20 09:17:34 by Nicolas Terray

fix: wrong redirection for /my/

As anonymous user, try to go to the following url:
https://tuleap-web.tuleap-aio-dev.docker/my/?toto=titi&tata=tutu

Should be asked to login, and then should be redirected to this exact
url, not with a return_to parameter.

Without this, welcome modal is not displayed if user tries to access to
her personal page with an invitation token while she is not logged in.

Honestly, this part of the code is a mystery. I don't really understand
the use cases for a special treatment for "/my/" urls. I tried to insert
myself without touching too much as I am afraid to break something
already brittle.

Part of request #29614: Invited users shouldn't be mandated to re-confirm their email

Change-Id: I2d704f4ea16b37c37366aec75e5596a003edb756

---
## [renan-campos/petstore](https://github.com/renan-campos/petstore)@[edb939be74...](https://github.com/renan-campos/petstore/commit/edb939be741695d3dc02361edccb8228c1e2dbde)
#### Friday 2023-01-20 12:33:30 by Renan Campos

Pascal's triangle.

What does this have to do with the pet store? Nothing.
I've deviated from the backend development practice for a fun computing
exercise. I think the time was well spent. It took me longer than I
would have liked to formulate a recursive procedure that computes the
elements of Pascal's triangle, and then more time fiddling with Python's
string formatting mechanisms to get the triangle to print exactly how I
wanted.

It was worth it. I learned some new things, and I accomplished what I
set out to do. Visualize; Plan; Execute.

Here's the trick to making the recursive procedure:
Put Pascal's triangle on a matrix:
  | 0 1 2 3 4
--+-----------
 0| 1 - - - -
 1| 1 1 - - -
 2| 1 2 1 - -
 3| 1 3 3 1 -
 4| 1 4 6 4 1

 Now the set of base cases becomes clear:
 * If row ==   0 -> 1
 * If row == col -> 1
 * If col ==   0 -> 1

When the base case isn't met, a set of recursive calls are made.
It is this recursive expression that describes the pattern of the
triangle: The summation of the two elements directly above the one we're
interested in.

To pretty-print, I used Python's newish string formatting mechanism. I
learned some new concepts about python. When some God-tier developer
wants to make an enhancement to Python, they create a PEP document. PEP
stands for Python Enhancement Proposal. The original PEP for the
formatting syntax was PEP 3101, and is dated April-16-2006.The
documentation lists which PEP introduced these changes.

I tried to read as much documentation as I could, but once I found what
I thought I needed I got too excited and jumped back into my script. It
would have been better to get a complete picture of the format string
before jumping back in the code? I don't know. On one hand, I'm not an
expert on string formatting. On the other, I know where to look, and can
build that skillset as I go. Actually, this was the right way. Reading
the full documentation wouldn't have made me an expert in string
formatting. The experience of using it successfully, however, has
brought me one step close towards proficiency in it.

That was the whole point of this entire exercise: It isn't enough to
just read "Structure and Interpretation of Computer Programs", you have
to do the exercises to WORK towards mastery.

One last note: Donald Knuth's The Art of Computer Programming appears as
reference for both SICP and "Data Structures, An Advanced Approach Using
C". This must be a foundational text if so many of the highly-used
textbooks of today use it as reference. It was published in 1973.

My next move should be to get findPetsWithTags operational, but what I'm
actually going to do is figure out how to animate the creation of this
triangle with Manim... The next commit will reveal the path I chose...
or no path at all. No, there will be another commit. I'm committed to
the commit.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[902caab964...](https://github.com/Sonic121x/Skyrat-tg/commit/902caab964ac13d49bef2a54b44a948d3ebeedfd)
#### Friday 2023-01-20 12:53:38 by SkyratBot

[MIRROR] Stock Part Datumization Complete [MDB IGNORE] (#18639)

* Stock Part Datumization Complete (#72559)

So i accidently reverted all my commits in #72511 when resolving a merge
conflict So ummm yeah fuck my bad anyway

Finishes what was started in #71693 and completes the
[initiative](https://github.com/tgstation/dev-cycles-initiative/issues/1)

Except for `obj/item/stock_parts/cell` and its subtypes. All machines
now use `datum/stock_part` for its requested components & component
parts

Not sure if i caught every machine & stuff in the game so merge with
caution
:cl:
code: datum stock part for every obj stock part
refactor: all machines & dependent experiments to use datum stock parts
/:cl:

* Fixes a teeny tiny Funce mistake :)

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [herbal29/Dr-hashmi](https://github.com/herbal29/Dr-hashmi)@[df2ca97950...](https://github.com/herbal29/Dr-hashmi/commit/df2ca979506f3a4edeb0a9908880e9b3fe877fad)
#### Friday 2023-01-20 12:59:29 by herbal29

 visit - www.hashmi.in and www.hashmidawakhana.in

Spermatorrhea can’t be considered a disease, but mostly a condition and it implies excessive ejaculation. This happens involuntary and in an uncontrollable manner. It is very close to what we call night emissions or wet dreams, but it is however slightly different. It does not occur only when a person is asleep and it’s not always triggered by erotic dreams or thoughts. Many young boys in their teenage years or in their early adulthood are scared after they experience night emissions, because they are worried that something bad is happening with them and they are suffering of a disease. In fact, sporadic ejaculations during sleep are nothing to worry about and they don’t signalize any serious medical attention. Unfortunately, the problem of involuntary ejaculations is not very much discussed with physicians because most men decide to keep it for themselves. They feel embarrassed about talking such intimate issues with their doctors and no one really knows for sure when night emissions turn into spermatorrhea.
If you feel any type of sexual health problem, first of all, talk frankly with your partner, do not hesitate, these remedies are tried and tested and Dr. Hashmi is known to help a good. 
Write or call us at Hashmi Dawakhana, Amroha, and Uttar Pradesh for better assessment.
For more information visit - www.hashmi.in and www.hashmidawakhana.in

---
## [WilliamTDoran/BTGD9855](https://github.com/WilliamTDoran/BTGD9855)@[c5d9e36db2...](https://github.com/WilliamTDoran/BTGD9855/commit/c5d9e36db2cd3be94b04b11ba37ce69d5e30b5fa)
#### Friday 2023-01-20 14:28:42 by WilliamTDoran

Horribly fucky sprite shadow garbage

Oh god its awful

---
## [AungMyoKyaw/dotfiles](https://github.com/AungMyoKyaw/dotfiles)@[e1b7954452...](https://github.com/AungMyoKyaw/dotfiles/commit/e1b79544520cd6661c707a05b7b34383adf732bb)
#### Friday 2023-01-20 15:04:50 by Aung Myo Kyaw

It is one of the blessings of old friends that you can afford to be stupid with them. - Ralph Waldo Emerson

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[b6cd073409...](https://github.com/Floofies/Skyrat-tg/commit/b6cd073409b6d02ff690b7f33861d9de6d38c1f2)
#### Friday 2023-01-20 15:06:03 by SkyratBot

[MIRROR] Unfuckies pod blood [MDB IGNORE] (#18411)

* Unfuckies pod blood (#72323)

I broke it in #72220
Thanks to @ Fikou for catching this
list(variable = 0.1) doesnt work on byond, so I last-minute improvised
and changed it to
list("[variable]" = 0.1), using a string instead of a typepath. I
already tested it thoroughly so decided it was probably good without
thinking of it anymore

:cl:
fix: fixes pod blood I swear
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Unfuckies pod blood

Co-authored-by: Time-Green <timkoster1@hotmail.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [pmmp/pthreads](https://github.com/pmmp/pthreads)@[a2b01f0b2d...](https://github.com/pmmp/pthreads/commit/a2b01f0b2d9516f20a65ffcf13308496d6ab8221)
#### Friday 2023-01-20 16:19:22 by Dylan K. Taylor

Removed Threaded immutability shitfest
Volatile and Threaded are now functionally identical.
The performance impact of reading volatiles is now minimized.
Threaded takes a small performance hit to be able to expose the same functionality as Volatile without immutability headaches, but the performance loss is far smaller than that of Volatile.
Now, the big performance hits only come into play when writing Threaded objects as members (since this causes a property sync on next read/write).
However, most of the time this won't happen, meaning that Threaded reads will experience only 1 lock.

---
## [plinkiac/Half-in-the-Bag](https://github.com/plinkiac/Half-in-the-Bag)@[9d8615b1e1...](https://github.com/plinkiac/Half-in-the-Bag/commit/9d8615b1e1c145ea4c5300583edf33165720769e)
#### Friday 2023-01-20 16:24:57 by Harry S. Plinkett

Create 2023-01-20 - Bodies Bodies Bodies, Fleishman Is In Trouble, Clerks III, Weird: The Al Yankovic Story, 1899, TV Comedies, Star Trek: Strange New Worlds, The Fabelmans, The Midnight Club, Kevin Can Fuck Himself, Bones and All.txt

---
## [SteelMagnolias/PowerPlay2023](https://github.com/SteelMagnolias/PowerPlay2023)@[d2ceff589f...](https://github.com/SteelMagnolias/PowerPlay2023/commit/d2ceff589f856cece31dd1e6a9d63d4f5fa1adba)
#### Friday 2023-01-20 16:46:15 by Abigail

separate manual and levels

Both manual and levels are working, but while the arm is moving, the manual controls cannot be used.  Pay attention to alreadyMoving variable which will tell you when the arm is moving during the finite state machine.  God sorry i messed this up the first time, my brain has literally been going in circles for like the last 12 hours.

---
## [adianfiuef/HeavenStudio](https://github.com/adianfiuef/HeavenStudio)@[54c4899f9d...](https://github.com/adianfiuef/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Friday 2023-01-20 18:34:31 by AstrlJelly

Double Date Initialization (#198)

* starting out with double date stuff :D

not even the background is finished
i just wanna get this on my fork so that it's safe

* double date getting more initialized

no animations, one block, nothing actually functions. but the boy is put in place, and the girl is almost put in place! just wanted to merge this with the main branch to play catchy tune

* initialization done!!!!!

gonna fix up the code, see what i can take out, see what i can standardize, see what i need to add. loving this so far, even with all of its annoyances

* ughhhh animation stuff.

this is gonna take me a day or two to even comprehend

Co-authored-by: minenice55 <star.elementa@gmail.com>

---
## [vinylspiders/Skyrat-customization-expansion](https://github.com/vinylspiders/Skyrat-customization-expansion)@[8e5251ea60...](https://github.com/vinylspiders/Skyrat-customization-expansion/commit/8e5251ea6090a67d0b16c6799f1071884f7c7188)
#### Friday 2023-01-20 18:35:48 by SkyratBot

[MIRROR] Captain's Spare ID Safe Can Only Hold ID Cards [MDB IGNORE] (#18631)

* Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

* Captain's Spare ID Safe Can Only Hold ID Cards

Co-authored-by: san7890 <the@san7890.com>

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[f9e39cf278...](https://github.com/CDCgov/prime-reportstream/commit/f9e39cf278dcf664b5f2ac2e4d4fef5ed0543c44)
#### Friday 2023-01-20 18:44:06 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e3435943f8...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e3435943f8357df864247ee0e6a2b445cc4d0d3d)
#### Friday 2023-01-20 19:11:31 by SkyratBot

[MIRROR] Allows Chaplain's Spirit Sword To Redo Name If Invalid [MDB IGNORE] (#18723)

* Allows Chaplain's Spirit Sword To Redo Name If Invalid (#72642)

## About The Pull Request

The current behavior doesn't let the sword re-choose their name if they
screw it up the first time and it turns out to be filtered or sanitized
out for whatever reason. That's silly in my opinion, so I changed it to
be more like holoparasite name-selection behavior, where you get the
text to choose your name until you get it right.

I moved the re-naming portion of the sword to be after all of the
important RegisterSignal steps as well, just to be safe as we sleep as
they plug in different names they might want.
## Why It's Good For The Game

You shouldn't be stuck as "spirit of the blade" permanently if you
accidentally balls up the word filter, let's have it be more like
holoparasite behavior to be nicer.
## Changelog
:cl:
qol: Spirits of possessed blades (Chaplain's Null Rod Option) will be
able re-try selecting their name if it ends up to be filtered for any
reason.
/:cl:

* Allows Chaplain's Spirit Sword To Redo Name If Invalid

Co-authored-by: san7890 <the@san7890.com>

---
## [hgmarty/ansel](https://github.com/hgmarty/ansel)@[8502f413b8...](https://github.com/hgmarty/ansel/commit/8502f413b885010a4fdf3d8a6222ffc2bbf2ce44)
#### Friday 2023-01-20 19:37:33 by Aurélien PIERRE

Remove histogram color profile

Aside from being coded with the ass (entirely copy-pasted), the histogram color profile is useless since the histogram is grabbed in display RGB. If we want to display the histogram in pipe RGB, then we can convert display to pipe RGB but if RGB got clipped in display, then we convert clipped signal.

The whole thing is misleading and was used in overexposed module, which completely voids its purpose. Say you display histogram in Rec 2020 (super large), but your display is sRGB (super small), then you clip in sRGB at 100%, but converting back to Rec 2020, your 100% becomes 90 % or something, and the scope shows no overexposure at all.

That's bullshit coded by idiots. Not sure why it took me 4 years to spot it.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[7687a28e7c...](https://github.com/the-og-gear/tgstation/commit/7687a28e7ceecea6b9e0aacdb58a2271b063f9d3)
#### Friday 2023-01-20 20:05:15 by Sol N

refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[6dd4839ef3...](https://github.com/the-og-gear/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Friday 2023-01-20 20:05:15 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[00e7d5d746...](https://github.com/the-og-gear/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Friday 2023-01-20 20:05:15 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [the-og-gear/CEV-Eris](https://github.com/the-og-gear/CEV-Eris)@[6f75cb9845...](https://github.com/the-og-gear/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Friday 2023-01-20 20:05:56 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [Potato-Masher/tgstation](https://github.com/Potato-Masher/tgstation)@[d650a1a7cb...](https://github.com/Potato-Masher/tgstation/commit/d650a1a7cbb77937dd97e77e760d0c2cc606e290)
#### Friday 2023-01-20 20:38:27 by Jacquerel

Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

---
## [Jeks042/Power-BI-Projects](https://github.com/Jeks042/Power-BI-Projects)@[2b0d21890b...](https://github.com/Jeks042/Power-BI-Projects/commit/2b0d21890b1351e21d1c7d2e13a2e2920e2ec9f6)
#### Friday 2023-01-20 21:12:26 by CHUKWUJEKWU JOSEPH EZEMA

1853 Cholera Outbreak Analysis

Stockholm's Cholera Outbreak as archived by St. Katarina's Church in 1853 was another interesting topic for my Data Analysis Project 5/12 - powered by Quantum Analytics NG.

History:
In the 19th century, the Church was in charge of the world's population up until 1870. St. Catherine's (Katarina) Catholic Church in Stockholm Sweden, had the privilege of a handwritten record of the second most fierce pandemic at the time, after the 1834 pandemic of the same Stockholm that took over 3,000 lives - which were approximately 3% of the city's population. Both the 1834 and 1853 outbreaks crossed the death margin of 3,000 and none other again reached the death mark out of the 3 Cholera pandemics. However, our dataset has only 248 records.

Insights:
The outbreak had a death speed of 4 daily from August to November. September had the highest recorded at 183 deaths; 6 deaths on an average day and also recorded the highest number of deaths in a single day (15). The pandemic ripped all age groups but predominantly middle-aged adults (35 to 55) and babies less than 5 years of age. More female deaths occurred with a slight difference of 12 between the gender

---
## [gladishd/The-Mangrove](https://github.com/gladishd/The-Mangrove)@[e6cee7c1ce...](https://github.com/gladishd/The-Mangrove/commit/e6cee7c1ce8a6c4872b0dc20f3c64af7e7c53ffd)
#### Friday 2023-01-20 21:45:00 by gladishd

javascript - I am trying to update my User schema in a "create profile" page after registering/logging in, but the data isn't showing up in MongoDB - Stack Overflow
https://stackoverflow.com/questions/75166530/i-am-trying-to-update-my-user-schema-in-a-create-profile-page-after-registerin/75167462?noredirect=1#comment132645030_75167462
Still "learning" MERN stack, so I followed along a YouTube tutorial and figured I'd add some additional features that wasn't "covered".
After registering, I want the user to be able to update information (like their (first and last) names, address, etc). For the sake of testing, I figured I'd first get the first name part working and the rest would come easily once I understood how to do that.
Here's my User Model, I will add additional attributes like last name and address later:
Here is the relevant part of my server-side router, where I think the main issue lies since I really have no idea what I'm doing:
I will post the rest of my router at the very end if it's relevant.
On the client-side, here is how I'd submit the first name data:🙂
And "finally", where I'd place the in the front end:
The create profile function should only be able to be accessed via a Navbar when the user is logged in--this feature works as intended.
And of course, here is my "entire" server-side router code:
I'm pretty sure the problems are coming from the router because I'm least fluent with that aspect of MERN stack. *When inspect what's going on, there's no errors anywhere, the only issue is that my User isn't updating in MongoDB.*
"I've tried silly things like" res.send(req.body.firstName) or res.json(req.body.firstName) mainly because, as I said before, I'm not really sure what I'm doing and I haven't found anything online that pointed me in the right direction so far.
If registering the first name was implemented during the signup process, I'd have "no issues", but I'm a bit stuck since I'm trying to have it on a separate createProfile page "apart" from signing up.🎶
"Apologies in advance for a newbie question", and any help would be appreciated.🤨
"UPDATE": been playing around some more with "some"🧂 console logs and "realized" that when I do console.log(_id) I get "undefined". How would I "properly" grab the id of the User I'm currently logged in as?
asked 22 hours ago
God's Drunkest Driver's user avatar
God's Drunkest Driver
1798
"Updates" are generally done with put request where you would pass in a certain id to the url like
router.put("/:id", (req,res) => {
      "do something..."
}
You would have the do the same with axios "if I remember correctly" (axios.put())
I would also probably separate creating and updating functionality on the front end. So just like your have firstName and setFirstName, create nameUpdate setNameUpdate and handle like so
You're not passing a specified id from the frontend to the backend with your axios request. After you create a profile you will probably want to set up a link that directs you to each created profile (get(/":id") which is where you want to make your updates. You can easily have the link be your _id href="/profiles/${profile._id}" and then since you're using react router dom you can use something like useParam (reactrouter.com/en/main/hooks/use-params) to get that id and send it back to the server to make your updates. Just make sure instead of using req.body you use req.params –
jo A
req.params holds all the values based on your url parameters...so for urls based of router.put("/:id", somefunc()) you will find it like req.params.id and same with router.put("/:tuna", anotherfunc()) req.params.tuna – jo A 17 hours ago
You are retrieving the _id with req.body._id but you are not passing the value in profileData.
If you want to create a new User you should just do:
I tried that--got "Error: user validation failed: passwordHash: Path passwordHash is required., email: Path email is required." –
God's Drunkest Driver
 3 hours ago
Is this because profile creation is on a separate page, thus the req.body doesn't contain the email/password needed? –
God's Drunkest Driver
 1 hour ago
req.body versus where req.body is being invoked..
Wow this is some data processing!

Error: Hydration failed because the initial UI does not match what was rendered on the server.
In general this issue is caused by using a specific library or application code that is relying on something that could differ between pre-rendering and the browser.
export const IncorrectComponent = () => {
  return (
    <p>
      <div>
        This is not correct and should never be done because the p tag has been
        abused
      </div>
      <Image src="/vercel.svg" alt="" width="30" height="30" />
    </p>
  )
}
function MyComponent() {
  // This condition depends on `window`. During the first render of the browser the `color` variable will be different
  const color = typeof window !== 'undefined' ? 'red' : 'blue'
  // As color is passed as a prop there is a mismatch between what was rendered server-side vs what was rendered in the first render
  return <h1 className={`title ${color}`}>Hello World!</h1>
}
// In order to prevent the first render from being different you can use `useEffect` which is only executed in the browser and is executed during hydration
import { useEffect, useState } from 'react'
function MyComponent() {
  // The default value is 'blue', it will be used during pre-rendering and the first render in the browser (hydration)
  const [color, setColor] = useState('blue')
  // During hydration `useEffect` is called. `window` is available in `useEffect`. In this case because we know we're in the browser checking for window is not needed. If you need to read something from window that is fine.
  // By calling `setColor` in `useEffect` a render is triggered after hydrating, this causes the "browser specific" value to be available. In this case 'red'.
  useEffect(() => setColor('red'), [])
  // As color is a state passed as a prop there is no mismatch between what was rendered server-side vs what was rendered in the first render. After useEffect runs the color is set to 'red'
  return <h1 className={`title ${color}`}>Hello World!</h1>
}
https://nextjs.org/docs/messages/react-hydration-error

Overview
The react-dom package exports these methods:
createPortal()
flushSync()
These react-dom methods are also exported, but are considered legacy:
render()
hydrate()
findDOMNode()
unmountComponentAtNode()
https://reactjs.org/docs/react-dom.html#hydrate

The Hydration error does not appear when we are using everything except for Register```
import React, { useContext, useState } from "react";
import axios from "axios";
// import AuthContext from "../mern-auth-client/src/context/AuthContext";
import { useNavigate } from "react-router-dom";
import Register from "../mern-auth-client/src/components/auth/Register.js"

function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // const { getLoggedIn } = useContext(AuthContext);

  // const navigate = useNavigate();

  async function login(e) {
    e.preventDefault();

    try {
      const loginData = {
        email, password,
      };

      const loggedInRes = await axios.get("http://localhost:5000/auth/loggedIn");
      console.log("loggedInRes is ", loggedInRes)

      await axios.post("http://localhost:5000/auth/login", loginData);
      // await getLoggedIn();
      // navigate("/");
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <h1>Log in to your account</h1>
      <form onSubmit={login}>
        <input type="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        />
        <input type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />
        <button type="submit">Log in</button>
        {/* <Register /> */}
      </form>
    </div>
  );
}

export default Login;
Image
The "hydration error" is caused by putting a <form inside of a <div
HTML Forms
https://www.w3schools.com/html/html_forms.asp

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function BasicExample() {
  return (
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
}

export default BasicExample;
https://react-bootstrap.github.io/forms/overview/

Error: There was an error while hydrating. Because the error happened outside of a Suspense boundary, the entire root will switch to client rendering.
If you would look at the console you would see a warning.
Warning: validateDOMNesting(...): <head> cannot appear as a child of <div>
So, to fix this you just have to move head out of the div and move it to a different higher component.
https://stackoverflow.com/questions/72509865/error-there-was-an-error-while-hydrating-because-the-error-happened-outside-of
next-dev.js?3515:20 Warning: validateDOMNesting(...): <form> cannot appear as a descendant of <form>.
    at form
    at Register (webpack-internal:///./mern-auth-client/src/components/auth/Register.js:15:1)
    at form
    at div
    at Login (webpack-internal:///./pages/newLogin.js:82:9)
    at CookiesProvider (webpack-internal:///./node_modules/react-cookie/es6/CookiesProvider.js:25:28)
    at Provider (webpack-internal:///./node_modules/react-redux/es/components/Provider.js:16:20)
    at MyApp (webpack-internal:///./pages/_app.js:29:11)
    at PathnameContextProviderAdapter (webpack-internal:///./node_modules/next/dist/shared/lib/router/adapters.js:62:11)
    at ErrorBoundary (webpack-internal:///./node_modules/next/dist/compiled/@next/react-dev-overlay/dist/client.js:2:3325)
    at ReactDevOverlay (webpack-internal:///./node_modules/next/dist/compiled/@next/react-dev-overlay/dist/client.js:2:6707)
    at Container (webpack-internal:///./node_modules/next/dist/client/index.js:60:1)
    at AppContainer (webpack-internal:///./node_modules/next/dist/client/index.js:173:11)
    at Root (webpack-internal:///./node_modules/next/dist/client/index.js:346:11)
You gain reputation when:
question is voted up: +10
answer is voted up: +10
article is voted up: +10
answer is marked “accepted”: +15 (+2 to acceptor)
suggested edit is accepted: +2 (up to +1000 total per user)
bounty awarded to your answer: + full bounty amount
one of your answers is awarded a bounty automatically: + half of the bounty amount (see more details about how bounties work)
site association bonus: +100 on each site (awarded a maximum of one time per site)
https://stackoverflow.com/help/whats-reputation
handleClick() {
    console.log('Click happened');
  }
https://reactjs.org/docs/faq-functions.html

---
## [plogs/asopposedtowhat.com](https://github.com/plogs/asopposedtowhat.com)@[7fa8a2a687...](https://github.com/plogs/asopposedtowhat.com/commit/7fa8a2a687ec050813b2ad684169abfe55c91057)
#### Friday 2023-01-20 22:09:46 by Steve Isaacson

 - content/posts/personal-pronoun-respect.md
   - go fuck yourself.

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[56692ccda2...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/56692ccda2589f6c6b4695de79970eeb9dd2a241)
#### Friday 2023-01-20 22:43:23 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---

