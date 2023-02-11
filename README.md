## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-10](docs/good-messages/2023/2023-02-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,238,891 were push events containing 3,401,350 commit messages that amount to 261,032,551 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[91f06a97d3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Friday 2023-02-10 00:26:08 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[d95ca04819...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Friday 2023-02-10 00:26:08 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8500d62b79...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Friday 2023-02-10 00:26:08 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[d10e5ed853...](https://github.com/git-for-windows/git/commit/d10e5ed853456d58dd818afab5bb21f1995b740e)
#### Friday 2023-02-10 00:59:50 by Johannes Schindelin

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
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[97f52bd40d...](https://github.com/swbs-co/odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Friday 2023-02-10 01:00:38 by Arnold Moyaux

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

Part-of: odoo/odoo#109640

---
## [sec-js/dotfiles-1](https://github.com/sec-js/dotfiles-1)@[5df5017605...](https://github.com/sec-js/dotfiles-1/commit/5df5017605d7615bd592ffee82af13d553aadb7b)
#### Friday 2023-02-10 01:03:20 by Seth House

Add default graphical packages for WSL and wslu utils

Turns out WSL2 ships with working, pre-configured, out-of-box support
for graphical apps and sound (using the main, official Ubuntu distro).
No tweaking or installation needed. That is absolutely mind-blowing.

Gimp and Inkscape run beautifully. I prefer using boring, steady,
predicable xterm and it looks fantastic in WSL with my default
Xresources config, including anti-aliased fonts. Clipboard support
between WSL and Windows Just Works (TM) in xterm and gVim. You can tell
the apps are running out of a container rather than natively, but
there's only a very slight input lag. Firefox can't be installed because
Ubuntu still thinks Snaps are a good idea (but that's not WSL's fault).
Overall surprisingly great experience.

As WSL has matured, I've wondered if WSL makes Windows a better, more
friendly development environment than OS X nowadays. This clinches it:
the answer is yes. Much eeasier to install, better defaults, more
features, way more similar to running native Linux. And this environment
is fully supported by Microsoft rather than the neglected and abused
red-headed step-children that Apple has with Homebrew, XQuartz,
`/usr/local`, and the random mishmash of BSD and GNU utils.

If you can't run Linux natively at work, running a full Linux inside
Windows via WSL is a _better_ experience than running a half-UNIX
alongside OS X via Homebrew and XQuartz.

Apple has been moving away from their UNIX roots and is being ever more
hostile to open source projects. In contrast, Microsoft is leaning in,
hard, with WSL. Never thought I'd be here, but as a programmer I'll be
requesting Microsoft hardware instead of Apple hardware at future jobs.

---
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Friday 2023-02-10 01:03:23 by Andrew Poelstra

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
## [xyz-mocha/kernel_xiaomi_sdm660](https://github.com/xyz-mocha/kernel_xiaomi_sdm660)@[9dd07b025a...](https://github.com/xyz-mocha/kernel_xiaomi_sdm660/commit/9dd07b025a62ae79db8249f383e4089a1e7c3f48)
#### Friday 2023-02-10 01:32:32 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

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

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [kwonoj/next.js](https://github.com/kwonoj/next.js)@[268dd6e80b...](https://github.com/kwonoj/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Friday 2023-02-10 01:35:31 by José Fernando Höwer Barbosa

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
## [open-goal/jak-project](https://github.com/open-goal/jak-project)@[c249dbc437...](https://github.com/open-goal/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Friday 2023-02-10 01:44:35 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [crcrpar/pytorch](https://github.com/crcrpar/pytorch)@[83275d8cdf...](https://github.com/crcrpar/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Friday 2023-02-10 01:53:29 by Brian Hirsh

add torch.autograd._set_view_replay_enabled, use in aot autograd (#92588)

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

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc @albanD @soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/92588
Approved by: https://github.com/ezyang, https://github.com/albanD

---
## [delphix/linux-kernel-aws](https://github.com/delphix/linux-kernel-aws)@[9bd96fdf28...](https://github.com/delphix/linux-kernel-aws/commit/9bd96fdf28450ec3266fad2e5a183c63fa646dfe)
#### Friday 2023-02-10 03:59:00 by Masahiro Yamada

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
## [SamShue/Intro-to-Genetic-Algorithms](https://github.com/SamShue/Intro-to-Genetic-Algorithms)@[66b17b933f...](https://github.com/SamShue/Intro-to-Genetic-Algorithms/commit/66b17b933faee1509f2f0370ed8afc5c2db1af80)
#### Friday 2023-02-10 04:42:58 by Sam Shue

Jesus Christ I've deleted this code through the github windows shitty ui 3 times now I hate this bullshit FUCK

---
## [paravoid/gdnsd](https://github.com/paravoid/gdnsd)@[d24791dcfa...](https://github.com/paravoid/gdnsd/commit/d24791dcfab3cf4b8b8e3f56e0b2b3850ea859bc)
#### Friday 2023-02-10 04:48:38 by Brandon L Black

TCP: stricter registry management

ThreadSanitizer pointed at a potential data race between
dnsio_tcp_request_threads_stop()'s access to thr->stop_watcher and
the free(thr) that happens just before a tcp thread actually
exits, and this commit "fixes" it by adding an unregister function
and putting explicit locks around all related operations.

Technically, I don't think there was a real bug here that anyone
could hit at runtime.  There are logical constraints the sanitizer
can't see: that the free() can only be reached during clean
termination, which is triggered by request_threads_stop anyways,
thus ensuring that the stop function's access to thr happens
before (causes) the eventual free(), combined with the fact that
the stop function is only called once from main().

But still: it's a bad smell and I'd rather just be over-cautious
and future-proof, since adding these locks and calls doesn't
harm anything in the perf-critical fast paths.

We already fixed the other side of this once (the sequencing at
startup) in f5ea429ca a couple years ago, so it's not like there
isn't potential for further bugs, especially if we make more TCP
changes down the line and get confused.

[Side note - in general the current code isn't amenable to
analysis with ThreadSanitizer, because TSan doesn't grok what
we're doing with various lock-free mechanisms like our
stats-gathering hacks and our liburcu data swaps + reclaims.
However, I do have some prototype code which uses C11 atomics for
the stats and swaps out userspace-rcu with a C11 atomics variant
that's just for this kind of testing as well, which cleans things
up well enough that TSan is no longer confused, so that I can use
it to look for issues like this one.  I think those bits will make
it into 4.x, so that we can easily build a development copy of the
code that's TSan friendly, but for now it's not easy to try TSan
on the master branch for yourself because of all the RCU/stats
false-positives]

---
## [Actuallybarcode/LiteCord](https://github.com/Actuallybarcode/LiteCord)@[0abb87d25f...](https://github.com/Actuallybarcode/LiteCord/commit/0abb87d25f494640aafa5b4cf3af1dd5626274cd)
#### Friday 2023-02-10 05:11:24 by Jude

waht does dis do skid code and take my company? FUCK YOU LOL

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[558717e6f6...](https://github.com/carlarctg/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Friday 2023-02-10 05:22:28 by zeroisthebiggay

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
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[4ce115a2a2...](https://github.com/carlarctg/cmss13/commit/4ce115a2a26f8b6664a230bdaff483a1889f17c4)
#### Friday 2023-02-10 05:22:28 by carlarctg

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
## [sidsingh00/crime-detection](https://github.com/sidsingh00/crime-detection)@[bc15aeb10d...](https://github.com/sidsingh00/crime-detection/commit/bc15aeb10d941a42a0a97560cdb9240c1251bef5)
#### Friday 2023-02-10 06:15:21 by Sidharth Singh

Create README.md

Crime is a very old concept which has moved on in society from generation to generation. Nobody is safe today. Criminals are employing scientific procedures to commit crimes as science and technology evolve, and authorities have been surprised by criminals' increased knowledge as society advances. Many crimes are perpetrated for the purpose of obtaining money or property wealth, with the most common being family feuds over property allocation. It is claimed to be a widespread societal issue that has an impact on not just a society's quality of life but also its economic progress. It is focused as major issue that has a direct impact on an individual's quality of life as well as indirect societal consequences.
With the rapid increase of crimes and the types of crimes, researchers are finding a strong connection in the various features affecting the crime like the geographic features, age, gender and many more yet to come into picture. Despite the fact that crimes can happen anywhere, it is normal for criminals to focus their efforts on regions where they are most familiar and at ease.
We seek to improve societal awareness by giving an advanced approach to identifying criminal hotspots and determining the nature, location, and time of crimes committed. Furthermore, having such a system in place would assist police in taking proactive actions in preventing and solving crimes at a far faster rate by allowing for crime prediction and prevention.
Various types of crimes are discussed here and focus on their intensities in the highest city in the highest year is put forward with machine learning concepts for the societal and police benefits in solving the crime. These crimes are represented in different visualization techniques like bar graphs, pie charts to get a clear picture about the crime.

The above problem made me to go for a research about how can solving a crime case made easier. Through many documentation and cases, it came out that machine learning and data science can make the work easier and faster. The aim of this project is to make crime prediction using the features present in the dataset. The dataset is extracted from the official sites. With the help of machine learning algorithm, using python as core we can predict the type of crime which will occur in a particular area. The objective would be to train a model for prediction. The training would be done using the training data set which will be validated using the test dataset. 

ABSTRACT

The project Criminal Record Management System is a Criminal record management system that uses to record crime activities of criminals. It can be used to report crime activities. This project is mainly useful for law and enforcement agencies. The law and enforcement authority can preserve records of the criminals and search any criminal using the system. This is an application with database system in which police will keep the record of criminals who have been arrested. We have used Python, Anaconda, Jupiter, MySql and Google colab to develop this project. We also used binary search algorithm to find a criminal from database. The project’s interface is very user friendly and helpful for authorities for easier and fast access of criminal records. 
The main objective of the project on "Criminal Database Management System" is to manage the detail of Case Id, Name, Age, Sex, Identification Mark, Crime Done, etc. It manages all the information criminal and their record. 

PREDICTIVE MODELING 
Predictive modeling is the way of building a model that is capable of making predictions. The process includes a machine learning algorithm that learns certain properties from a training dataset in order to make those predictions. Pattern classification tasks can be divided into two parts, Supervised and unsupervised learning. In supervised learning, the class labels in the dataset, which is used to build the classification model, are known. In a supervised learning problem, we would know which training dataset has the particular output which will be used to train so that prediction can be made for unseen data. 

DATA PREPROCESSING
This process includes methods to remove any null values or infinite values which may affect the accuracy of the system. The main steps include Formatting, cleaning and sampling. Cleaning process is used for removal or fixing of some missing data there may be data that are incomplete. 
Sampling is the process where appropriate data are used which may reduce the running time for the algorithm. Using python, the preprocessing is done.

MODEL SELECTION
Based on the defined goal(s) (supervised or unsupervised) we have to select one of or combinations of modeling techniques. Such as 
• KNN Classification   
• Logistic Regression   
• Decision Trees   
• Random Forest   
• Support Vector Machine (SVM)   
• Bayesian methods

IMPLEMENTATION

The dataset used in this project is taken from Kaggle.com. The dataset obtained from kaggle.com is maintained and updated by the Chicago police department. 
The implementation of this project is divided into following steps –

DATA COLLECTION
Crime dataset from kaggle.com is used in CSV format. 

DATA PREPROCESSING

10k entries are present in the dataset. The null values are removed using df = df.dropna() where df is the data frame. The categorical attributes (Location, Block, Crime Type, Community Area) are converted into numeric using Label Encoder. The date attribute is splitted into new attributes like month and hour which can be used as feature for the model. 

FEATURE SELECTION

Features selection is done which can be used to build the model. The attributes used for feature selection are Block, Location, District, Community area, X coordinate , Y coordinate, Latitude , Longitude, Hour and month,

---
## [Dark-Night-Base/pokemon-showdown](https://github.com/Dark-Night-Base/pokemon-showdown)@[5cbb317a4c...](https://github.com/Dark-Night-Base/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Friday 2023-02-10 07:16:31 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Darmanitan-Galar's Choice Band set (#9354)

* Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

* Update data/mods/gen8/factory-sets.json

---------

Co-authored-by: Kris Johnson <11083252+KrisXV@users.noreply.github.com>

---
## [knghtbrd/DnD-System-Reference-Document-5.1](https://github.com/knghtbrd/DnD-System-Reference-Document-5.1)@[253ba5221f...](https://github.com/knghtbrd/DnD-System-Reference-Document-5.1/commit/253ba5221ffc44cc6130754593650ecf3b659fdc)
#### Friday 2023-02-10 07:33:18 by T. Joseph Carter

Oneline the ability block numbers for creatures

Okay, there's a process here:

1. Get the ability blocks into the format:
   ## (±##) ## (±##) ## (±##) ## (±##) ## (±##) ## (±##)
2. Apply a couple seds to put it into correct table format
3. Remove any of these stray fenced code blocks that are everywhere

This is the creatures version of #1 above, done as a proof of concept. I
have already designed the s/// commands to do #2 but … let's get this
far with the monsters first. Then I'll start writing the macros to fix
the fenced code blocks. A few more commits to go and I'll push these out
together.

I'm debating whether or not to squash them before I do. My sense is that
I won't, and I'll explain why for anyone who stumbles across this commit
log: This is a considerable amount of work! When some loser suit at
WotC/Hasbro starts talking about how this game belongs to them, as if it
was something they worked hard for and us "freeloaders" are just using
for free like it was nothing … it isn't.

It would probably actually be easier to recreate the content than
reformat theirs—but people value the promise they made that this stuff
belonged to the world now and have depended on that to make the D&D
ecosystem larger. Easy, huh?

Yeah, easy. I'ma make me a bandit:

        Bandit

        medium humanoid (any race), any non-lawful alignment

        Armor Class: 12 (light armor)
        HP: 9 (2d8)
        Speed: 30ft

        ----------------------------
        STR  DEX  CON  INT  WIS  CHA
        +1   +1   +1   -1   +0   +0
        ----------------------------

        Senses: Passive perception 10

        Languages: Native for background, at least some common typical

        Challenge: 1/4 (50 xp)

        Actions

        Sword. +3 to hit, 5ft reach, hit: 6 (d6 + 3) slashing
        Crossbow. (Ranged) +3 to hit, 60-300ft range,
                hit: 7 (d8 +3) piercing
        Knife. 3ft reach, hit 3 (d4 + 1) slashing/piercing

        Bandits operate in bands that will raid or lie in ambush for
        those with valuables to steal. They needn't be evil, since
        desperation leads to desperate actions. Regardless of their
        native language, they'll typically speak enough common to
        communicate their demands. Banditry is a nervous profession
        since any bandit taken into custody by local authorities faces
        execution within 48 hours.

Good as the 5E bandit? Probably. I just designed common humanoid aiming
for level zero and a half, fairly tough/fast, but not too bright, and
armed well enough to be a threat to other common folk. Especially if
faced with a band of bandits. And I came up with it in less time than it
took me to look up the 5E stat block for such a creature.

But my bandit is gonna be different than yours, etc. The whole idea was
that WotC put *their* bandit under a free license so we'd all agree to
use that one, or something close to it. And in exchange for that they
got to be the biggest game out there. If they want to give that up with
6E, it's their loss—but they can't take away 5E.

And that's why we're doing all this work.

---
## [Docode072/DataStructure](https://github.com/Docode072/DataStructure)@[f54e2225f0...](https://github.com/Docode072/DataStructure/commit/f54e2225f0a5339a63782eb453b9b72f322349d7)
#### Friday 2023-02-10 07:43:09 by Himanshu Singh

Create Balloon Everywhere_gfg.cpp

Balloon Everywhere
EasyAccuracy: 72.39%Submissions: 6K+Points: 2
Lamp
Don't Miss Out on the Exciting World of Data Science and Unlock Your Full Potential Today. Try this course!

Bob is very fond of balloons. Once he visited an amusement park with his mother. The mother told Bob that she would buy him a balloon only if he answer her problem right. She gave Bob a string S [contains only lowercase characters] and asked him to use the characters of string to form as many instances of the word "balloon" as possible. Return the maximum number of instances that can be formed.

Help Bob to solve the problem.

Note: You can use each character in the string at most once.

Example 1:

Input:
S: nlaebolko
Output: 1
Explanation:
Here, the number of occurence of 'b' = 1
of occurence of 'a' = 1
of occurence of 'l' = 2
of occurence of 'o' = 2
of occurence of 'n' = 1
So, we can form 1 "balloon" using the letters.
 
Example 2: 

Input:
S: loonbalxballpoon
Output: 2
Explanation:
Here, the number of occurence of 'b' = 2
of occurence of 'a' = 2
of occurence of 'l' = 4
of occurence of 'o' = 4
of occurence of 'n' = 2
So, we can form 2 "balloon" using the letters.
 

Your Task:
The task is to complete the function maxInstance() which takes a string as the only input parameter and should return the maximum instances that can be formed of the word "balloon" using the given string.

Expected Time Complexity: O(n), n is size of the given string.
Expected Auxiliary Space: O(26).

Constraints:
1 <= s.length <= 106
https://practice.geeksforgeeks.org/problems/45fa306a9116332ece4cecdaedf50f140bd252d4/1

---
## [rynosaur94/homebrew](https://github.com/rynosaur94/homebrew)@[f1150e6e1d...](https://github.com/rynosaur94/homebrew/commit/f1150e6e1d24b74ab600b549776c7f664f16fe96)
#### Friday 2023-02-10 07:56:45 by rynosaur94

Setting Guide for G4 My Little Pony's Equestria

A full setting guide for the universe of My Little Pony Friendship is Magic.  Trying to blend show accuracy and tone with 5e's general heroic fantasy vibes, I've been maintaining this guide since I created it in 2016.  Contains Races, Feats, Subclasses, Spells, Items mundane and magical, Religions, and more.

---
## [chapmanjacobd/reddit_mining](https://github.com/chapmanjacobd/reddit_mining)@[8655402459...](https://github.com/chapmanjacobd/reddit_mining/commit/8655402459157bfe8730be2bbadb734a15d9c750)
#### Friday 2023-02-10 08:32:37 by Jacob Chapman

README insights 80smusic WorldMusic absolutelyproductions adifferentspin afrobashment afrobeat afrofuturism ambientmusic arabicmusic arcology artisanvideos asmrmusic ausmusic aussiehiphop australianmusic australianpsychrock azerbaijanimusic balkanmusic banglamusic bilingualporn bleachedir bollywoodmusic bossanova brazilianmusic breakbeat canadianmusic celticmusic chansonfrancaise chinafuturism chinesemusic classy_asses crazyfuckingvideos damnthatsinteresting darksideplayground deepintoyoutube densegifs dirtytalk_spanish documentaries educationalgifs fetishjav fmrp forbiddencarejav fullforeignmovies fullmoviesonyoutube funnyjav futureporn gifsthatkeepongiving gonewildaudible gonewildaudio gonewildtube hapanal happycrowds homemadexxx illbeyourguide ilovejav imaginaryfeels imaginarysliceoflife imaginarytechnology interdimensionalcable interestingasfuck japaneseasmr japanesegameshows japanesekissing japaneserimming jav_gifs jav_nsfw javboratory javengsub javforscience javlovers javsubtitle javuncensored kinkypillowtalkaudio lectures mealtimevideos mechanical_gifs menintroublejav neverchangejapan nonenglishporn nottimanderic nsfwasmr obscuremedia outstruments petitejav pillowtalkaudio playitagainsam praisethecameraman qualityyoutube rakugo recut retroeducationalfilms retrofuturism sensualasmr sexwithmixedgirls sexyaccents sf_videos shewantstofuck shittyrobots shortfilm shortfilms silentcinema throughtheboxers tiktokcringe tiktokorchestra timestopjav u_Frogacuda unbgbbiivchidctiicbg unintentionalasmr unknownvideos unusualinstruments vanillaaudio videoessay whyweretheyfilming wmafblowjobs woahdude youboobers youtubetitties

---
## [arty-arty/sui](https://github.com/arty-arty/sui)@[90cb63b9a8...](https://github.com/arty-arty/sui/commit/90cb63b9a8a7fbf91511f4b0d4c4000d49f60627)
#### Friday 2023-02-10 08:49:39 by arty-arty

Handle frenemies dead round update calling cheaters

There is a very peculiar issue with the migration. Really weird one. 

Look at the transactions. https://explorer.sui.io/object/0x7c901b42a5ffcd22e057e66e42b7c25002b44f4e
An account cheated by calling update via RPC during frenemies downtime. 73 scores a huge advantage! They could do it probably because their name is so short. So, it didn't cause overflow.

Sorry, I'm from the phone and did not test it. But, the issue seems to be real and dangerous and needs to be fixed. Probably you would not do it so radically like I did, just stopping the person from getting any more scores. 

Perhaps you would just prefer to subtract the unfair advantage, gained during dead round, which might be huge. It might be life or death situation where someone gets pushed out of 2000 by a cheater.

---
## [SicDevelop/RaspBackend](https://github.com/SicDevelop/RaspBackend)@[0ed6d38d3c...](https://github.com/SicDevelop/RaspBackend/commit/0ed6d38d3cad21d334d167d4c81db3bbcaa2e9d7)
#### Friday 2023-02-10 09:42:45 by Alchemist

Fuck this Json type.

Cargo cannot find this Struct in scope. FUCK IT. I REALLY LOVE THIS LANGUAGE BUT THIS SHIT...

---
## [Offroaders123/Menu-Drop-Component](https://github.com/Offroaders123/Menu-Drop-Component)@[5171311c27...](https://github.com/Offroaders123/Menu-Drop-Component/commit/5171311c27eb5a9ca83ea932fb4902d1e747b642)
#### Friday 2023-02-10 10:39:21 by Offroaders123

Touch Rehash + Legacy Parity

Doing a side-by-side check with both the usability/user experience and code itself of the legacy version, from the `legacy-types` tag.

Discovered some missing touch input handling logic, which I hadn't rewritten yet as part of the full rework. Now I remember choosing to do that later, once I had everything working again. Makes sense now!

Going to work on the Shortcuts parts, coming up. Having modules is going to make that so much easier, so relieved I have that, *and* TypeScript!

Seeing a lot of parts of the code that can be restructured, now that I know how everything works again, so that will be coming up soon, too. Essentially, everything has been nearly repackaged into the new component structures (not a single, big honkin thing), so now it's safer to edit things, since they all have dedicated places for each implementation detail. TypeScript is great for this, too!

I tried adding a local, more-advanced type definition for `PointerEvent.pointerType` to be `"mouse" | "pen" | "touch"`, just like it says on MDN, but it didn't like me trying to override an already defined property with a narrower type. maagh. There might be a way to override it using a different file, and adding it to the tsconfig, but I didn't look too far into it since it's mostly just a bonus little feature for me.

I wish other browsers did what Chromium does, and has `pointerType` present on the ancestor `MouseEvent` class, as that's what's been causing this whole debockle. It works great to check the `pointerType` within the `click` event, but only Chromium has support for that, so I had to make my own workaround to get the same information into the event logic. also a meegh.

Added a style hook by matching the `[open]` attribute on the host `<menu-drop>` element, so you can style things based on the root element, a nice and simple selector! `menu-drop[open]`.

Latest news on the laptop upgrade plan: Was gonna go with the M2 Macbook Air, 512 GB, 16 GB SSD. Read more reviews, and it sounded like it was a generally lukewarm response compared to the M1 Air. Looked into the same specs for the M1 Air, and it was a much better price! Then I found that the refurbished M1 Pro MB Pro was exactly the same price as a new M2 Air (a hair lower, actually!), with those specs, and you get *all of the other great stuff* that comes with the Pro. Better chip, screen, screen size, 120Hz, ports, just wow. Then I watched some more videos about the reviews for that, specific to programmers. One YouTuber made a great argument that you don't need to have great hardware to do cool things. You should be doing cool things before you upgrade to fancier tech. You don't want to break the bank before you have better ideas for what your plans are down the line. That swayed me to feel like I should just wait to upgrade until later, when it's more obvious what I should get. I also thought, that if it's been this challenging of a decision for this long now, maybe I'm just not ready for upgrading big like that, maybe that's just a sign for that. Mentioned that to my family, and they think I should upgrade though, so that makes me feel a bit stronger about it. I just don't want to upgrade because I want to, but because I *need* to. I don't want to change things up just because. As my friends and I were saying, if it ain't broke, don't upgrade! haha. Been doing all of my coding on my Ubuntubook for ages now, and I am still blown away with how durable he's been! great lil dude. Only rockin' 16 GB eMMC, and 4 GB RAM. And I read today that the display has only been able to show 72% of the sRGB spectrum this whole time LOL. No wonder it's not looked the best. It does look great, nice and crisp to read code on though. Not the best of approach angles though, haha. The screen turns to differnt colors when looking from across the room. Night shift essentially looks orange. Framework is still in my interest too. I really like the idea of consolidating my workspace into a single computer though, even if I store some of my data on external drives, to help manage the internal disk space. Being able to have my music library, code, and game on the same machine, reliably, has been less so for me for the last while. My iMac can do that, but it's been harder to work with consistently. I think I've mentioned that already at some point (not waking from sleep). Oh yeah, having my iPhone backups on there too, easy to do everything from one place, at least from a software perspective.

Either Asahi Linux or a UTM Ubuntu VM on Apple Silicon is also part of my dream, that would be the ideal setup to move from my Chromebook over to a MacBook. I will likely move to plain macOS with time, but I really do love working with Linux as of now, and there's more I want to explore with that. Living in the terminal is great.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e30ca3bc93...](https://github.com/odoo-dev/odoo/commit/e30ca3bc9337730ecaf78f538dd8450f093697fb)
#### Friday 2023-02-10 10:50:16 by Romain Derie

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

closes odoo/odoo#111523

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[1fe9efd00a...](https://github.com/OrionTheFox/Skyrat-tg/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Friday 2023-02-10 10:53:22 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[97f567fdc7...](https://github.com/Jacquerel/orbstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Friday 2023-02-10 10:56:13 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[27c35bfa0b...](https://github.com/Jacquerel/orbstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Friday 2023-02-10 10:56:13 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [TianWalkzzMiku/SRyzen-sdm660-4.19](https://github.com/TianWalkzzMiku/SRyzen-sdm660-4.19)@[a30257b644...](https://github.com/TianWalkzzMiku/SRyzen-sdm660-4.19/commit/a30257b644017d96cd8963d6429464d527854959)
#### Friday 2023-02-10 10:58:44 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [Maxbo2000/Python-Game](https://github.com/Maxbo2000/Python-Game)@[054afaae5f...](https://github.com/Maxbo2000/Python-Game/commit/054afaae5fa26f60eb589dd2d1371b7a075b501e)
#### Friday 2023-02-10 10:58:50 by Maxbo

initial git repository commit

.gitignore removed
Fuck you too git and git kraken

---
## [test3teamapp/SpringGoSpy](https://github.com/test3teamapp/SpringGoSpy)@[d1e8d7537b...](https://github.com/test3teamapp/SpringGoSpy/commit/d1e8d7537b24068e880c24eda09f300f0cf55581)
#### Friday 2023-02-10 10:59:44 by test3teamapp

1)Testing the api controller was a pain in the ass, with the redis-om library. (the components wehre not properly initialised during the test period, specifically a document template could not be found, but actually building it was in conflict with the existing template that is normally loading during build. (fuck)
Moved it to a different project "WebDriverTesting",
where I will do all integration test.
Unit tests should still be performed in this project.

2)Added bootstrap template to thymeleaf and started using fragments to show a sidebar

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[fedf2f3a26...](https://github.com/lizardqueenlexi/orbstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Friday 2023-02-10 12:18:44 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Vhmit/kernel_samsung_msm8917](https://github.com/Vhmit/kernel_samsung_msm8917)@[5db5911ac8...](https://github.com/Vhmit/kernel_samsung_msm8917/commit/5db5911ac8b88fa99248cc83cf593a65748d8298)
#### Friday 2023-02-10 13:56:08 by Steven Barrett

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
## [mluigi/command-t](https://github.com/mluigi/command-t)@[148e54a6c1...](https://github.com/mluigi/command-t/commit/148e54a6c1941beaaf940ff703dc2bff511b6def)
#### Friday 2023-02-10 14:06:28 by Greg Hurrell

feat: continue adding to Lua port

Yeah, this is a horrible mixed-bag commit. Just showing that we can
compile multiple translation units in a single invocation (may want to
refactor the Makefile to do that a little more traditionally, to be
honest; compile each source individually, then link... but then again,
this is simple and the project is tiny so speed is not a concern).

---
## [stanalbatross/cmss13](https://github.com/stanalbatross/cmss13)@[c7a33d5ff9...](https://github.com/stanalbatross/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Friday 2023-02-10 14:16:54 by riot

PMC and Whiteout stuff (#1966)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

As a preword, I came up with every change in this PR and coded them in
the span of 10 hours, so some things may be iffy.

PMCs and Whiteout may be good, but they're a bit outdated, this
modernizes multiple loadout aspects, enables antag vendors for
admin-spawn, and does some balance changes to certain
portions(specifically chem ERT).

Individual changes, numbered, will go over each in why its good, may
have forgotten one or two things.

1. Buffs whiteout flamer with blue flame damage, belt-linked magharn,
and pyro underbarrel extinguisher
2. Adds a synthetic repair kit(medkit), with synth repair tools, gives
it to whiteout.
3. Adds breaching charges and swaps crowbars to tactical in whiteout
loadouts
4. Gives whiteout PMC sniper goggles(thermals)
5. Gives whiteout medic the required gear to actually repair a downed
member of the team, and just a lot of synth heals.
6. Gives whiteout leader a pyro extinguisher.
7. Gives whiteout weapons default attachments.
8. Adds an 'advanced' mini-flamer with the same stats as UPP integrated
UBF, gives it to NSG23 and random m41/2 attachie.
9. Gives detainer PMCs a version of the corporate m41A MK2(goon gun),
with attachies and adv flamer to replace flamethrower.
10. Swaps chem PMC TL P90(name is too long) with an M41/2
11. Gives normal PMC ERT roles a webbing vest with meds and
miniextinguisher
12. Gives PMC Surgeon the essentials required to act as a medic, swaps
NSG with M39/2, gives them a normal but unique look.
13. Whiteout and PMC SG powerpacks have 30k power by default, instead of
10k.
14. Gives PMC guns more options for random attachments, and gives m41/2
its intended collapsible stock
15. Gives PMC engi m39/2 instead of P90
16. Removes flamer from potential PMC loadouts.
17. Gives PMCs better CQC skill.
18. Gives PMC TLs autoinjector pouches(which gives chem TL a second
pouch in the first place)
19. Detainer PMCs now have tac-sechuds, PMC TLs have sensorhuds.
20. **Enables antag vendor for PMC roles.** (Look at file changes for
the specific things, too long for pr desc)

# Explain why it's good for the game

Modernization and some needed loadout/balance changes(IMO).
Per number:

1. Whiteout flamer did worse damage than napalm, and was incredibly easy
to lose.
2. More heals for each member of the whiteout team, allows more
self-sufficiency.
3. Breach charges for tacticool breaches, crowbar doubles as a melee
weapon in case the player doesn't know about synth punch
4. Whiteout didn't have proper NVG, thermals allows them to do
tacticooler breaches by lining up people wth breach charge.
5. Whiteout medic didn't have a lot of heals at all, and didn't have a
defib, so they weren't much of a medic.
6. To extinguish the flames and lead charges, works like pyro
underbarrel extinguisher, but handheld.
7. Default tacticool attachment, already made whiteout subtypes for
HEAP, why not give them good attachies with them too.
8. Mini-flamer sucks, gives a better version for NSG and m41/2, same
stats as the already existing UPP integrated UBF.
9. Detainers had flamers which sucked, gives them corpo m41s which
aren't as good as /2s, but have adv UBF for flames.
10. P90 sucks, having default m41/2 fits with other leader type, also
gives them a better gun than their underlings.
11. Medkit but in a webbing, its my personal combat webbing load when I
play so its good.
12. PMC Surgeon was horrifically undergeared, they didn't even have a
medhud, gives them basic gear similar to PMC med but with a beret to
tell them apart.
13. ERTs don't have spare batteries to get usually, more staying power
in fights.
14. More options for attachies to further make PMC weapons better, also
gives m41/2 the m41 collapsible stock because it needed it.
15. P90 sucks, support roles getting the m39/2 is cool.
16. Flamer sucks to get as PMC, and adv. UBF as a potential m41/2
attachie makes a full-sized flamer useless too.
17. PMCs could fireman carry, and multi-strip, but did it horrifically
slow, gives them MP level CQC(master for spec, expert for TL)
18. TL getting extra meds is neat, also chem TL had an empty pocket slot
and no meds, thats bad.
19. Sechud-thing for PMC detainers is useful(stops flashbang trolling
for one), giving PMC TL a sensorhud to watch their team's status is also
good.
20. Makes doing event bases for PMCs much easier, too long to post the
specific changes here but look at files for them.


# Testing Photographs and Procedure

I forgot to take screenshots but it all works. 👍 
I spawned myself as every changed role and tested every individual
change extensively.

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
add: PMCs are now able to use antag vendors.
balance: Multiple loadout and skill changes to PMCs and Whiteout
balance: Buffs whiteout flame damage to blue flame damage.
fix: PMC Investigator Lead now appropriately spawns with a medical pouch
in their pocket, instead of nothing.
fix: Maximum skill preset now appropriately also has BE and intel skill,
at maximum of course.
fix: PMC Smartgunner now appropriately a VP78 to go along with their
VP78 magazines
fix: Whiteout now appropriately have night vision.
fix: M41A/2 now appropriately comes equipped with a collapsible stock.
spellcheck: PMC smartgun drum now has a seperate description and name
from base SG to match its different appearance.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[f998a2b77b...](https://github.com/hashicorp/nomad/commit/f998a2b77b84a542d73f11a0a254576f9031d1f3)
#### Friday 2023-02-10 14:26:20 by Michael Schurter

core: merge reserved_ports into host_networks (#13651)

Fixes #13505

This fixes #13505 by treating reserved_ports like we treat a lot of jobspec settings: merging settings from more global stanzas (client.reserved.reserved_ports) "down" into more specific stanzas (client.host_networks[].reserved_ports).

As discussed in #13505 there are other options, and since it's totally broken right now we have some flexibility:

Treat overlapping reserved_ports on addresses as invalid and refuse to start agents. However, I'm not sure there's a cohesive model we want to publish right now since so much 0.9-0.12 compat code still exists! We would have to explain to folks that if their -network-interface and host_network addresses overlapped, they could only specify reserved_ports in one place or the other?! It gets ugly.
Use the global client.reserved.reserved_ports value as the default and treat host_network[].reserverd_ports as overrides. My first suggestion in the issue, but @groggemans made me realize the addresses on the agent's interface (as configured by -network-interface) may overlap with host_networks, so you'd need to remove the global reserved_ports from addresses shared with a shared network?! This seemed really confusing and subtle for users to me.
So I think "merging down" creates the most expressive yet understandable approach. I've played around with it a bit, and it doesn't seem too surprising. The only frustrating part is how difficult it is to observe the available addresses and ports on a node! However that's a job for another PR.

---
## [hwchase17/langchain](https://github.com/hwchase17/langchain)@[02f5451322...](https://github.com/hwchase17/langchain/commit/02f54513226ee3fb0b6d22528dbce1d9f7236005)
#### Friday 2023-02-10 14:57:52 by Peng Qu

allow getting format_instructions from agent_path (#968)

In real-life scenarios, we do indeed need to make slight adjustments to
the text of "format_instructions", making the user experience friendlier
and more closely aligned with specific scenarios.

---
## [RevenueCat/purchases-android](https://github.com/RevenueCat/purchases-android)@[dfd2a22eac...](https://github.com/RevenueCat/purchases-android/commit/dfd2a22eac045e295c4572e7aeab356f61aea5be)
#### Friday 2023-02-10 15:39:11 by Josh Holtz

[CF-1121] Update Magic Weather for BC5 / SDK V6 (#768)

<!-- Thank you for contributing to Purchases! Before pressing the
"Create Pull Request" button, please provide the following: -->

### Checklist
- [x] If applicable, unit tests
- [x] If applicable, create follow-up issues for `purchases-ios` and
hybrids

### Motivation

[CF-1121](https://revenuecats.atlassian.net/browse/CF-1121)

### Description

- Migrated from SDK `5.0.0` to `6.0.0-alpha.2`
- Changes to `PaywallAdapter` to make paywall show more useful
information to user
  - Duration (gross code)
  - Multiple offers (and "best offer" first)
  - Pricing phases (gross looking now but will improve later)
- Works for both subscriptions and one-time purchases

#### Step 1

The initial migration (with only necessary code changes to compile) made
for a very confusing paywall 👇

- The subscriptions relied on the product title (which is the same for
each base plan)
- Did not include the duration so user had no idea what they were buying
- This is because these were previously in the individual subscription
titles for BC4
- It did use the default/best offer which was nice but didn't explain
any offer info

<img width="473" alt="Screen Shot 2023-01-30 at 8 23 51 AM (1)"
src="https://user-images.githubusercontent.com/401294/216314716-eb584d1c-d943-4dd1-9c03-2dd6436bb3e4.png">

#### Step 2

Big rework to programmatically show as much info as we could (even
though it is kind of ugly UI right now) 👇

- Shows all the options for each subscription with "best offer" on top
- This might be overkill because why not just choose the best offer but
wanted to show this as example 🤷‍♂️
- Shows the pricing phases that come with each option
- Needed very different logic for subscriptions vs one-time purchases
- This is because one-time purchases contain all the data in the
`StoreProduct`
- Where subscriptions contain all needed data in `SubscriptionOption`
and `PricingPhase`s


https://user-images.githubusercontent.com/401294/216314819-54f24dfa-48c4-4bd9-9d75-b89754015f92.mov




[CF-1121]:
https://revenuecats.atlassian.net/browse/CF-1121?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[5f78464e25...](https://github.com/morrowwolf/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Friday 2023-02-10 15:47:45 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[766f5529bf...](https://github.com/cmss13-devs/cmss13/commit/766f5529bfca454129f6d62f1ed626d6a70d5432)
#### Friday 2023-02-10 15:53:11 by carlarctg

Removes Autodocs from the Almayer (#2607)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Removes autodocs from medbay. They're replaced with 2 random potted
plants. :)

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->



EDIT: Tomorrow I will update this PR to give nurses surgery skill.

Autodocs fundamentally and inseparably, irrevocably, DESTROY medbay and
surgery gameplay. There is NO REASON, EVER to put someone through manual
surgery when you could just haha autodoc them instead. Autodocs kill the
good old hell medbay lines, they make surgeons extremely lazy and
stagnant (Tales of surgeons doing surgery for a few minutes, then giving
up and autodoccing the patient are common, not to mention the times
where they miss something in the autodoc schedule), they remove all
skill depth, floor, ceiling, the middle from medbay, and they also make
marines complacent by having them want the funny magic robot machine
rather than an actual human to treat them.

I understand that this may be too sudden of a change. If so, I propose
the following: Cryo tubes could slowly heal a marine up entirely,
removing organ damage and bone breaks through the course of a very slow
5-10 minutes. This will allow marines and nurses to get treated if
there's no doctor around or alive. However, I think the best course of
action is to just ram this change through and make medbay adapt. Embrace
the suck.

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
balance: Removes Autodocs from the Almayer
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ASKnetCommunity/LEAD](https://github.com/ASKnetCommunity/LEAD)@[cde04bc0a0...](https://github.com/ASKnetCommunity/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Friday 2023-02-10 16:11:30 by Dawa Edina Hillary

Proposed changed for Sida's profile

---
layout: profile
title:  "Sida Lillian"
image: "assets/images/profiles/Sida-Lillian/Sida-Lillian.jpg"
country: Uganda
region: West Nile
hub: CC4D
languages: "English (Fluent spoken and written), Bari/Kakwa (Fluent spoken and spoken), Arabic (good spoken only), Lugbara (fair spoken only)"
mail: sidalilian@proton.me
phone: "+256782739162"
whatsapp: 
website: 
telegram: "+256782739162"
github: github.com/sidalillian
linkedin: 
twitter: 
facebook: https://www.facebook.com/profile.php?id=100074066215635
instagram: 
mastodon: 
wikifab:
skills:
  - {name: Web & Software, number: 1, qualification: "using platforms, basic social media experiences, software download and installation \n \n
     * [Sida Lilian was trained on social media skills during the #ASKnet training in 2018](https://m.facebook.com/story.php?story_fbid=303135693607634&id=100017336164583) "}
  - {name: Community & Moderation, number: 2, qualification: "connecting people, trauma healing, event facilitation and meditation \n \n 
     * Certificate of participation in trauma healing& meditation training \n
     * She was trained and facilitated a post training on how to use Condoms under the #ASKnet project 2018"}
  - {name: Data Security & Research, number: 3, qualification: "data collection and protection of personal data \n \n 
     * Certificate in data collection"}

---

Sida Lilian is a female South Sudanese refugee in Uganda.

Expert in data collection, trauma healing, mediation, event facilitation of different types.

She was trained on how to collect both qualitative and quantitative data by REACH Uganda, Danish Refugee Council, Norwegian Refugee Council Uganda and GROUND TRUTH SOLUTIONS, she was also trained and worked as frontline worker on the *BOOST FOR THE YOUNGEST by Save The Children under Dubai Cara not only that she was also trained on Social Enterprise online by Makerere University - Canada in 2018, she was trained and worked as hygiene Promoter by CEFORD Uganda and was also trained and worked as Community Development Worker (CDW) by Danish Refugee Council.

She is confident, talented and determined to transform her community.

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Friday 2023-02-10 16:18:54 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[7f5cd54b2b...](https://github.com/cmss13-devs/cmss13/commit/7f5cd54b2bab2fdbd25a3f970e9a7f55d415dfe9)
#### Friday 2023-02-10 16:40:22 by carlarctg

Colony Guns Part 3: Longarms Rework (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Updates and buffs the following weapons:

- Basira-Armstrong Rifle
- Model 12 Bolt-Action Rifle
- M37-17 pump shotgun
- Dragunov sniper rifle

### Basira-Armstrong Rifle

- The BA rifle has been reflavored as the removed 'ceremonial' ABR-40,
now a hunting-civilian version of the L42. It effectively has the same
stats as the L42, just don't take the stock off!
- Its magazines can only fit 12 bullets, but they still have the classic
L42 kick to them. The magazines are completely compatible between both
military and civilian gun types.
- Additionally, there are now holo-targeting magazines available for the
ABR-40, for hunting target capture purposes.
- - The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.

### Model 12 Bolt-Action Rifle

- Like its sprite implies, this is now the new Basira-Armstrong rifle.
- Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
- Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.

### M37-17 Pump Shotgun

- Did you know that the 10% damage mod this gun was supposed to have
didn't work? Now it does! And it deals 15% more damage to make up for
it.
- However, it can now be melted down.

### Dragunov Sniper Rifle

- The dragunov has been revamped into a DMR, needing no skill to fire,
dealing good damage, and having the same push-back feature the
bolt-action now has.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

All of these weapons are seen as, and are, a complete joke and ignored
in favor of chungillionaire among us sus impostor running around PBing
xenos with buckshot. Buffing them to be useful paves the way for
civilians to use civilian weaponry instead of chungillionarius.

### ABR-40 Hunting Rifle

This is intended as asset recycling. IIRC, Triiodine disliked the
existence of a ceremonial rifle and thought that was goofy, which is an
understandable opinion, but it pains me to see the gun's cool assets go
unused. I took the opportunity and made the lame and mediocre Basira
into this cool gun which marines and survivors will take a lot more
interest in than a Basira plinker.

While it does have L42 stats, colonists won't be able to locate any L42A
ammo on the colony, meaning they are limited to 12-round magazines.
Still, giving them a weapon like this is a great way to incentivize them
to step out of their chungus zone.

As for the contractor addition, these are supposed to be ex-USCM
mercenaries, who are trained in the usage of marine equipment. It makes
sense that they'd grab the civilian version of a primary marine gun and
tune it to their liking.

### Basira-Armstrong Bolt-Action Hunting Rifle

Chomp made this really cool backend for a bolt-action that tragically
ended up never being used, not really, aside from a half-hearted few
rifles being thrown in at Shiva's Snowball. Since these guns are so
weak, it's plain to see why nobody even looks at them twice. So I
changed that.

### M37-17 Pump Shotgun

Bugfix and a small damage buff to make up for it. It being unacidable
was lame anyways. Spread projectiles are still bugged and don't inherit
the base gun's damage mod, but that's out of scope.

### Dragunov Designated Marksman Rifle

This gun has been a joke since 2017, it's time to give it some love.
Still needs one-hand sprites but not my problem.

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
balance: Updates and buffs the following weapons: Basira-Armstrong
Rifle, Model 12 Bolt-Action Rifle, M37-17 pump shotgun, Dragunov sniper
rifle
imageadd: The Basira rifle has been reflavored as the removed
'ceremonial' ABR-40, now a hunting-civilian version of the L42. It
effectively has the same stats as the L42, just don't take the stock
off!
add: Its magazines can only fit 12 bullets, but they still have the
classic L42 kick to them. The magazines are completely compatible
between both military and civilian gun types.
add:: Additionally, there are now holo-targeting magazines available for
the ABR-40, for hunting target capture purposes.
add: The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.
balance: Like the bolt-action rifle's sprite implies, this is now the
new Basira-Armstrong rifle.
add: Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
add: Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.
balance: Did you know that the 10% damage mod the M37-17 pump shotgun
was supposed to have didn't work? Now it does! And it deals 15% more
damage to make up for it.
del: However, it can now be melted down.
balance: The dragunov has been revamped into a DMR, needing no skill to
fire, dealing good damage, and having the same push-back feature the
bolt-action now has.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [bing2008/azerothcore-wotlk](https://github.com/bing2008/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/bing2008/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Friday 2023-02-10 16:44:50 by ICXCNIKA

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
## [jonpryor/java.interop](https://github.com/jonpryor/java.interop)@[20fa0aa2bd...](https://github.com/jonpryor/java.interop/commit/20fa0aa2bd88e034118219577bfd2c200574df56)
#### Friday 2023-02-10 16:47:49 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions

Fixes: https://github.com/xamarin/java.interop/issues/616

Context: https://github.com/xamarin/java.interop/issues/14
Context: ff4053cb1e966ebec1c16f97211b9ded936f2707
Context: da5d1b8103bb90f156b93ebac9caa16cfc85764e
Context: 4787e0179b349ab5ee0d0dd03d08b694acea4971
Context: 41ba34856ab119ea6e22ab103320180143fdf03d

Remember `jnimarshalmethod-gen` (176240d2)?  And it's crazy idea to
use the `System.Linq.Expressions`-based custom marshaling
infrastructure (ff4053cb, da5d1b81) to generate JNI marshal methods
at build/packaging time.  And how we had to back burner it because
it depended upon `System.Reflection.Emit` being able to write
assemblies to disk, which is a feature that never made it to
.NET Core, and is still lacking as of .NET 7?

Add `src/Java.Interop.Tools.Expressions`, which contains code which
uses Mono.Cecil to compile `Expression<T>` expressions to IL.

Then update `jnimarshalmethod-gen` to use it!

~~ Usage ~~

	% dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp \
	  --jvm /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/lib/jli/libjli.dylib \
	  -o _x \
	  -L bin/TestDebug-net7.0 \
	  -L /usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0

First param is assembly to process; `Java.Interop.Export-Tests.dll`
is handy because that's what the `run-test-jnimarshal` target in
`Makefile` processed.

  * `-v -v` is *really* verbose output

  * `--keeptemp` is keep temporary files, in this case
    `_x/Java.Interop.Export-Tests.dll.cecil`.

  * `--jvm PATH` is the path to the JVM library to load+use.

  * `-o DIR` is where to place output files; this will create
    `_x/Java.Interop.Export-Tests.dll`.

  * `-L DIR` adds `DIR` to library resolution paths; this adds
    `bin/TestDebug/net7.0` (dependencies of
    `Java.Interop.Export-Tests.dll`) and
    `Microsoft.NETCore.App/7.0.0-rc.1.22422.12` (net7 libs).

By default the directories containing input assemblies and the
directory containing `System.Private.CoreLib.dll` are part of the
default `-L` list.

When running in-tree, e.g. AzDO pipeline execution, `--jvm PATH`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll > beg.il
	% ikdasm _x/Java.Interop.Export-Tests.dll > end.il
	% git diff --no-index beg.il end.il
	# https://gist.github.com/jonpryor/b8233444f2e51043732bea922f6afc81

is a ~1KB diff which shows, paraphrasing greatly:

	public partial class ExportTest {
	    partial class '__<$>_jni_marshal_methods' {
	        static IntPtr funcIJavaObject (IntPtr jnienv, IntPtr this) => …
	        // …
	        [JniAddNativeMethodRegistration]
	        static void __RegisterNativeMembers (JniNativeMethodRegistrationArguments args) => …
	    }
	}
	internal delegate long _JniMarshal_PP_L (IntPtr jnienv, IntPtr self);
	// …

wherein `ExportTest._<$>_jni_marshal_methods` and the `_JniMarshal*`
delegate types are added to the assembly.

This also unblocks the desire stated in 4787e017:

> For `Java.Base`, @jonpryor wants to support the custom marshaling
> infrastructure introduced in 77a6bf86.  This would allow types to
> participate in JNI marshal method ("connector method") generation
> *at runtime*, allowing specialization based on the current set of
> types and assemblies.

What can we do with this `jnimarshalmethod-gen` output?  Use it!

First, make sure the tests work:

	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then update/replace the unit test assembly with
`jnimarshalmethod-gen` output:

	% \cp _x/Java.Interop.Export-Tests.dll bin/TestDebug-net7.0
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Total tests: 17
	     Passed: 17

`core-tests.yaml` has been updated to do this.

~~ One-Off Tests ~~

One-off tests: ensure that the generated assembly can be decompiled:

	% ikdasm  bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll
	% monodis bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll

	% ikdasm  _x/Java.Interop.Export-Tests.dll
	% monodis _x/Java.Interop.Export-Tests.dll
	# which currently fails :-()

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify _x/Java.Interop.Export-Tests.dll \
	  --tokens --system-module System.Private.CoreLib \
	  -r 'bin/TestDebug-net7.0/*.dll' \
	  -r '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0/*.dll'
	All Classes and Methods in /Volumes/Xamarin-Work/src/xamarin/Java.Interop/_x/Java.Interop.Export-Tests.dll Verified.
	# no errors!

where:

  * `--tokens`: Include metadata tokens in error messages.
  * `--system-module NAME`: set the "System module name".  Defaults
    to `mscorlib`, which is wrong for .NET 5+, so this must be set to
    `System.Private.CoreLib` (no `.dll` suffix!).
  * `-r FILE-GLOB`: Where to resolve assembly references for the
    input assembly.  Fortunately file globs are supported…

~~ Removing `System.Private.CoreLib` ~~

`System.Private.CoreLib.dll` is *private*; it's not part of the
public assembly surface area, so you can't use
`csc -r:System.Private.CoreLib …` and expect it to work.  This makes
things interesting because *at runtime* everything "important" is in
`System.Private.CoreLib.dll`, like `System.Object`.

Specifically, if we do the "obvious" thing and do:

	newTypeDefinition.BaseType = assemblyDefinition.MainModule
	    .ImportReference (typeof (object));

you're gonna have a bad type, because the resulting IL for
`newTypeDefinition` will have a base class of
`[System.Private.CoreLib]System.Object`, which isn't usable.

Fix this by:

 1. Writing the assembly to a `Stream`.
 2. Reading the `Stream` from (1)
 3. Fixing all member references and assembly references so that
    `System.Private.CoreLib` is not referenced.

If `jnimarshalmethod-gen.dll --keeptemp` is used, then a `.cecil`
file is created with the contents of (1).

Additionally, and unexpectedly -- [jbevain/cecil#895][1] -- Mono.Cecil
adds a reference to the assembly being modified.  Remove the declaring
assembly from `AssemblyReferences`.

[0]: https://www.nuget.org/packages/dotnet-ilverify
[1]: https://github.com/jbevain/cecil/issues/895

---
## [kizelerr/GameDesign5](https://github.com/kizelerr/GameDesign5)@[8dd8e53c5c...](https://github.com/kizelerr/GameDesign5/commit/8dd8e53c5cf9f8da4574324660e2166c4f488395)
#### Friday 2023-02-10 17:18:04 by Zander0523

it's all on me

Chris, I was wrong. You were never the reason we failed, it was all on me. I understand how you feel. I didn't think it would be that hard to put in the shooting mechanic. I should have asked the teacher. I was the whole reason that Sandstorm was a failure. I'm so sorry I blamed you for our failure. I don't know if you're going to pull the origin and read this, but if you do, I hope you can see it in your heart to forgive me.

---
## [AquaMan0722/WalkaroundStuck](https://github.com/AquaMan0722/WalkaroundStuck)@[010a27f7b2...](https://github.com/AquaMan0722/WalkaroundStuck/commit/010a27f7b212d6a1da23a6f7ed4b44ed57fbf40a)
#### Friday 2023-02-10 17:48:43 by Aqua

Update ActionPopupInspect.gd

lousy goddamn sequence_active/dialog_active bullshit

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[60ec693603...](https://github.com/mrakgr/The-Spiral-Language/commit/60ec69360346c662f2ed2650be60f94819bce482)
#### Friday 2023-02-10 18:47:56 by Marko Grdinić

"https://news.ycombinator.com/item?id=34725047

> Not laid off but I've just ended a year long sabbatical. Looking for work now is a terrible experience. A lot of ghosting, recruiters absolutely useless, agencies not looking for new talent. I have done two dozen interviews, twice as many resumes sent to interested recruiters, and only one offer, which I was not very excited about and declined.

> I'm focusing on my SaaS project, and trying to market myself outside the box instead of the old resume as my 16 years long career doesn't seem to impress anyone. Sorry, I will not elaborate further as you're all my competition here.

Brutal. I should not see this period as typical.

Maybe it is dumb to think that I'll improve my chances much by adding some exp in this kind of environment.

7:55pm. https://storyteller.io/

This guy posted in that thread, so I applied to him on a whim.

This site is really interesting.

9:20pm. https://www.youtube.com/watch?v=tKIQfeOXynI
Mastering Elmish

Somebody posted this 1:22h video yesterday.

https://youtu.be/tKIQfeOXynI?t=56
> The good thing about Elmish is that it is not about web development. It is about universal stuff.

https://youtu.be/tKIQfeOXynI?t=127

Just what is wrong with the video here?

https://youtu.be/tKIQfeOXynI?t=247

Oh it is possible to reload the Ionide plugin like this.

9:35pm. https://youtu.be/tKIQfeOXynI?t=432

This video is unbearable to watch due to the partial frames.

9:40pm. I am playing with setting up the Elmish project again. Ran into the femto bug.

9:45pm. I've zipped the folder. Let me see if I can open an issue.

https://github.com/Zaid-Ajaj/Femto/issues/

Actually the issue I have seems to be exactly issue 98.

10:10pm. Ok, at this point I am convinced this has something to do with webpack.

10:15pm. Yeah, it doesn't have anything to do with NPM packages. This is purely an issue with webpack, I think.

10:30pm. https://www.reddit.com/r/fsharp/comments/10w3yn6/comment/j7wbszw/?utm_source=share&utm_medium=web2x&context=3

///

Do you have any advice how to set up Fable.Elmish + React from scratch? I keep getting weird errors and it has been a nightmare to get it to work. A part of it was because I was trying to use .NET 7 which run into issues with Femto not being able to resolve NPM packages correctly. I've moved past that by downgrading to .NET 6.

At first I was suspicious of the NPM packages themselves, but now I think there is something wrong with the Fable template's Webpack configuration because I tried copying the SAFE Dojo's dependencies and it did not fix it. I took a look at it and SAFE Dojo's Webpack config is beyond arcane. I am not sure whether it is worth studying it.

I'll have to open an issue on the Elmish repo as half of the examples are busted right now, but since I am suspecting Webpack, I thought I might ask you for advice. So please.

///

Asked here. I'll open a proper issue tomorrow.

https://vitejs.dev/guide/#community-templates

I do not want to study this right now.

10:35pm. https://www.reddit.com/r/fsharp/comments/10xrtl3/updated_net_managed_languages_strategy_net/

Don Syme left MS?

No, he is still there, just on a different project.

10:40pm. Let me watch Mitsuha. I should get dinner.

Tomorrow I will open an issue on the elimsh repo regarding the specific issue, and study Vite.

2/10/2023

9:30am. I am up.

Hmmmm, this is the second time I've gotten the creepy mail.

https://github.com/m-r-a-k-g-r

I guess this is some kind of cyberbullying. The annoying thing is that corrupted text takes up so much of the screen that I can't find the report button.

Ah, it is in his profile.

9:50am. I wasted 20 mins reporting this guy.

https://mangadex.org/title/4ae47330-e64d-4e4e-9d1e-433bd8b18937/u12-under-12

I had no idea I was following this.

I'll check out ch 1 as well as Fabiniku. Let me chill a bit.

I'll leave replying to the robot RL guy for later. Did I get a reply to what I asked the guy on Reddit yesterday?

https://www.reddit.com/r/fsharp/comments/10w3yn6/comment/j7wnj61/?utm_source=share&utm_medium=web2x&context=3

Oh, I got something good.

I thought that string was meaningless, but I wonder if it is tied to the id - `|> Program.withReactBatched "app"`

Yeah, I had this hunch yesterday, but ignored it.

I'll first try matching the id, and then I am going to try his advice.

10:25am. Chilled enough. Let me start.

```html
<body>
  <div id="app">
    <p>Fable is running</p>
    <p>You can click on this button:</p>
    <button class="my-button">Click me!!!</button>
    <script src="bundle.js"></script>
  </div>
</body>
```

I've put this div in the body, with the `id="app"`.

```
|> Program.withReactSynchronous "app"
```

I'll use `app` as a placeholder. Now let me try running it.

```
ERROR in ./src/fable_modules/Fable.Elmish.React.4.0.0/react.fs.js 3:0-43
Module not found: Error: Can't resolve 'react-dom/client' in 'E:\Webdev\Fable\fable-elmish-example\src\fable_modules\Fable.Elmish.React.4.0.0'
resolve 'react-dom/client' in 'E:\Webdev\Fable\fable-elmish-example\src\fable_modules\Fable.Elmish.React.4.0.0'
  Parsed request is a module
  using description file: E:\Webdev\Fable\fable-elmish-example\package.json (relative path: ./src/fable_modules/Fable.Elmish.React.4.0.0)
    Field 'browser' doesn't contain a valid alias configuration
    resolve as module
      E:\Webdev\Fable\fable-elmish-example\src\fable_modules\Fable.Elmish.React.4.0.0\node_modules doesn't exist or is not a directory
      E:\Webdev\Fable\fable-elmish-example\src\fable_modules\node_modules doesn't exist or is not a directory
      E:\Webdev\Fable\fable-elmish-example\src\node_modules doesn't exist or is not a directory
      looking for modules in E:\Webdev\Fable\fable-elmish-example\node_modules
        existing directory E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom
          using description file: E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\package.json (relative path: .)
            using description file: E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\package.json (relative path: ./client)
              no extension
                E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\client doesn't exist
              .js
                E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\client.js doesn't exist
              .json
                E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\client.json doesn't exist
              .wasm
                E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\client.wasm doesn't exist
              as directory
                E:\Webdev\Fable\fable-elmish-example\node_modules\react-dom\client doesn't exist
      E:\Webdev\Fable\node_modules doesn't exist or is not a directory
      E:\Webdev\node_modules doesn't exist or is not a directory
      looking for modules in E:\node_modules
        E:\node_modules\react-dom doesn't exist
 @ ./src/App.fs.js 10:0-100 91:18-46
```

Sigh, this fucking thing again?

Ohhh, I got it to work! Another example, I mean.

As to why the previous one did not work, it is probably because...yeah, I am using the prerelease.

```
ERROR in ./src/fable_modules/Fable.Elmish.React.4.0.0/react.fs.js 3:0-43
Module not found: Error: Can't resolve 'react-dom/client' in 'E:\Webdev\Fable\fable-elmish-example\src\fable_modules\Fable.Elmish.React.4.0.0'
resolve 'react-dom/client' in 'E:\Webdev\Fable\fable-elmish-example\src\fable_modules\Fable.Elmish.React.4.0.0'
```

Nope, I've tried downgrading, but it still does not work.

```
PS E:\Webdev\Fable\fable-elmish-example> dotnet femto src --resolve
[10:42:56 INF] Analyzing project E:/Webdev/Fable/fable-elmish-example/src/App.fsproj
[10:42:56 INF] Running dotnet restore against the project
[10:43:00 INF] Using npm for package management
[10:43:04 INF] Found package.json in E:\Webdev\Fable\fable-elmish-example
[10:43:05 INF] Executing required actions for package resolution
[10:43:05 INF] Uninstalling [react, react-dom]
[10:43:07 INF] Installing dependencies [react@18.2.0, react-dom@18.2.0]
[10:43:12 INF] ✔ Package resolution complete
```

Hmmm, it actually reinstalled them. Let me try again.

Oh that was it!

Let me try upgrading Fable to prerelease once more.

Yeah, it works. For the sake of Femto, I'll stick to the .NET 6.

10:45am. Everything works now!

This took up so much of my time yesterday, but now I am smoothly sailing. I really should have realized that I need to attach it to some html id, I mean I did have that example in Blazor, but I was too dumb to realize what the script was asking me. I even had the notion once, but ignored the impulse as I wasn't sure if it was right.

11am. https://github.com/Zaid-Ajaj/elmish-getting-started/issues/

Added a bit of info to issue 31 here.

Ok...

During the night, I thought that today might be the time to study both Webpack and debugging. Right now I don't actually know how to debug even regular F# projects in VS Code. I have debugged TS projects in the past, but have forgotten how that went.

11:05am. Since I've resolved the issue I'll leave that for later.

I'll do what I wanted to yesterday which is study the Elimish examples. Also the book. I forgot that it existed.

```fs
let timestamp = model.current.ToString("yyyy-MM-dd HH:mm:ss.ffff")
```

Oh, I did not know you could format the time like this. This is something to keep in mind.

```fs
    let view model dispatch =
        let timestamp = model.current.ToString("yyyy-MM-dd HH:mm:ss.ffff")
        Html.div [
            Html.div [Html.text timestamp]
            Html.div [
                Html.label [
                    prop.children [
                        Html.input [
                            prop.type' "checkbox"
                            prop.isChecked model.enabled
                            prop.onCheckedChange (fun b -> dispatch (Toggle b))
                        ]
                        Html.text " enabled"
                    ]
                ]
            ]
        ]
```

Now that it has come to this, I can finally let myself focus on the example code. It is easy to understand.

```fs
    let subscribe model =
        [ if model.enabled then
            ["timer"], timer Tick ]
```

Oh wow, I didn't realize that subscriptions are also done based on model state.

I really like the Elmish library a lot more than my reactive techniques.

11:20am. Ok...Let me move forward to the next example.

```fs
module Hour =

    type Msg =
        | Hour of int

    type Model = int

    let init () =
        0, []

    let update (Hour hour) model =
        hour, []

    let subscribe model =
        [ ["timer"], Sub.timer (60*1000) (fun now -> Hour now.Hour) ]
```

This should really be a minute, but whatever.

11:35am. https://elmish.github.io/elmish/docs/subscription.html#ids-and-dependencies

> How does it work? It is taking advantage of ID uniqueness. Let's say that intervalMs is initially 1000. The sub ID is ["timer"; "1000"], Elmish starts the subscription. Then intervalMs changes to 2000. The sub ID becomes ["timer"; "2000"]. Elmish sees that ["timer"; "1000"] is no longer active and stops it. Then it starts the "new" subscription ["timer"; "2000"].

Hmmm, is that how it is?

11:55am. This last example gives me an error when I try to use it. It says that string length must be non negative.

```fs
                                                let zeros = 23 - s.Length
                                                s + String.replicate zeros "0"
```

Huh is it this?

```fs
let zeros = 23 - s.Length |> max 0
```

Let me try this.

Yeah, that was it. But it is really strange that this would result in a negative value.

```fs
let s = now.ToString("yyyy-MM-dd HH:mm:ss.ffff")
```

It says that this is 24. How can that be?

Yeah, it is exactly 24. Looks can be deceiving! I'd have guessed it was something like 15.

12:15pm. I've studied the example. I really like this kind of UI work. I am not sure if hot reloading is working correctly, but the changes are swift to be applied.

Let me report an error.

https://github.com/elmish/elmish/issues/

Opened issue 270.

12:25pm. Now where was I?

https://elmish.github.io/react/

> Both React and React Native applications need a root component to be rendered at the specified placeholder, see browser and native tutorials for details.

Ah, so that is where it was written.

12:30pm. Time for chores here.

What I will do next is go through the rest of the docs.

1:40pm. Right now I am breakfasting.

https://boards.4channel.org/g/thread/91436854/do-you-realize-4chan-is-going-to-become-more#p91437054
> For people like you there is "heaven-banning"

Is this real?

https://news.ycombinator.com/item?id=31588260
> Note: The story is made up, the author says so in the first comment on Twitter, easy to miss. Very interesting idea though.

Also in the image the date says Aug 8 2024.

> heaven-banning, the hypothetical practice of banishing a user from a platform by causing everyone that they speak with to be replaced by AI models that constantly agree and praise them, but only from their own perspective, is entirely feasible with the current state of AI/LLMs

2:20pm. https://re-library.com/translations/ragweed-princess-of-the-livitium-imperial-kingdom/prologue/forest-training-and-the-black-cat-familiar-part-2/

Let me finish this chapter and then I am going to resume my studies. I really like that react has lazy views. This is brilliant. This is exactly what is needed to eliminate the weakness of the Elm pattern.

2:30pm. I got distracted by a reply from that issue I opened.

Now where was I?

https://elmish.github.io/react/tutorials/browser.html

Let me read this. Stop getting distracted me, and finish these studies.

https://elmish.github.io/react/tutorials/browser.html#create-the-program-instance

Take a look at this. It says exactly what I need to start the application here.

https://zaid-ajaj.github.io/Feliz/#/

It seems here I can program in native react without having to reach for the Elm pattern. It reminds me of some JS libraries that I looked at. I wonder what the type of this is?

```fs
module App

open Feliz

[<ReactComponent>]
let Counter() =
    let (count, setCount) = React.useState(0)
    Html.div [
        Html.button [
            prop.style [ style.marginRight 5 ]
            prop.onClick (fun _ -> setCount(count + 1))
            prop.text "Increment"
        ]

        Html.button [
            prop.style [ style.marginLeft 5 ]
            prop.onClick (fun _ -> setCount(count - 1))
            prop.text "Decrement"
        ]

        Html.h1 count
    ]

open Browser.Dom

ReactDOM.render(Counter(), document.getElementById "app")
```

It says this way of doing things is deprecated.

2:45pm.

```fs
module App

open Feliz

[<ReactComponent>]
let Counter() =
    let (count, setCount) = React.useState(0)
    Html.div [
        Html.button [
            prop.style [ style.marginRight 5 ]
            prop.onClick (fun _ -> setCount(count + 1))
            prop.text "Increment"
        ]

        Html.button [
            prop.style [ style.marginLeft 5 ]
            prop.onClick (fun _ -> setCount(count - 1))
            prop.text "Decrement"
        ]

        Html.h1 count
    ]

open Browser.Dom

let x = ReactDOM.createRoot (document.getElementById "app")
x.render(Counter())
```

I like this. I remember React being very nasty in TS, but this is not bad at all.

https://elmish.github.io/react/tutorials/native.html

Hmmm, what is ReactNative?

https://reactnative.dev/

Does it even work for Windows? I'd guess so.

https://microsoft.github.io/react-native-windows/

Nevermind that for now.

2:55pm. https://elmish.github.io/browser/

Let me read this.

https://elmish.github.io/browser/tutorials/routing.html

I do not understand this.

https://elmish.github.io/urlParser/

Nevermind this.

https://github.com/elmish/elmish/blob/v4.x/docs/index.md#controlling-termination

Don't get this.

https://elmish.github.io/debugger/

Ok, I am done with the Elmish docs.

3:05pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/fable/

I guess I should read this.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/fable/hello-world

I really starts from the beginning.

https://vitejs.dev/guide/why.html

Let me just read the why for Vite.

> Once you experience how fast Vite is, we highly doubt you'd be willing to put up with bundled development again.

https://vitejs.dev/guide/

I'll leave this for later.

https://preactjs.com/

I found a template for this and started wondering what it was.

> Fast 3kB alternative to React with the same modern API

I see.

https://lit.dev/

I think I saw Fable.Lit used in SAFE Dojo. Or was it mentioned in that thread?

Nevermind this for now. React is good enough for the time being.

https://zaid-ajaj.github.io/Feliz/#/

I'll leave Feliz for later as well. Let me take a look at the Elmish book.

3:35pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/fable/node-packages

I am getting distracted like this. I really liked the straight code examples more. At my level, I can just look and get it, so increased wordiness of this book is just taking up my time.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/render-html

I am going to have to get used to writing html, but that is fine.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/render-html#feliz-vs-fablereact-comparison

Oh, he is doing a comparison here.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/using-css#external-style-sheets

Ah, so Bulma is a CSS styling library. I see.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/form-inputs#bootstrapping-the-program

Only here he shows how to bootstrap the program.

4:05pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/todo-app#styling-with-bulma-icons-with-font-awesome
> As I have mentioned earlier, we will be using Bulma  as our CSS framework and Font Awesome  for, well, the awesome icons.

Naruhodo.

> Don't worry if you aren't familiar with the classes that Bulma provides. I wasn't either when I started writing the chapter! It is a matter of looking up the documentation  to see what classes you need.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/todo-app-part2

Hmmm, are HTML object classes the same thing as style classes? Nevermind that for now.

4:15pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/elm/todo-app-exercises#exercise-5-refactor-bulma-with-typedcssclasses

> Although this would work, it requires considerable amount of work to take every class exposed from Bulma and writing in the module, not to mention that you have to maintain the module and update it when Bulma introduces breaking changes. Finally, you would have to follow this process for every CSS framework you want to use. What if there was a tool that does all things for us using a single line of code? Enter TypedCssClasses  written by Zanaptak , a type-provider that infers the class names exposed from a stylesheet and makes them available during compile-time!

Cool. I'll keep this in mind.

4:45pm. Had to take a break. Let me resume.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/async-state#operations-that-might-fail

If we ignore the views, I could use Elmish for pretty much anything. It is like the video said, this is universal.

5:10pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/async-recursive-updates

Come to think of it, instead of Spiral's custom diff thing, could I have implemented the whole thing in terms of the Elm pattern? Did I really need that weird Hopac thing?

...Yeah, I did need it. For the simple reason that Elm messages are async, while Hopas is synchronous concurrency.

But then again, I could have done typechecking synchronously in the server. There is no reason to say that it needs to by async. Parsing could have been.

Well, I could have made is semi-async.

5:15pm. Nevermind this for now.

5:20pm. Yeah, now I am lost in thought, but it would be very hard to model the problem that I want using the async concurrency style. Nevermind it.

What the Elmish style would be good though is organizing code.

5:30pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/http

Here is some webdev stuff.

> But you might wondering, why bother with a different static file server other than webpack development server? The reason is that the development server is kind of special and injects a lot of JavaScript artifacts in your index.html during development, for example to make the web page refreshed after you edit your source files. These added artifacts could be incompatible with many browsers and might break your actual application in a production environment.

This is pretty informative.

I've been kind of skimming it up to now, but I'll up me level of attention.

5:55pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/async-xhr#on-the-composability-of-javascript-callbacks

> You might say "Well, this is just a silly example code, real-world code doesn't look like this, right?" Actually, real-world JavaScript can be even uglier, because when loading data from a server, especially for a RESTful API, the front-end code ends up with having to request data from multiple endpoints. However, this problem is not specific to calling web APIs and also applies to any callback based API such as the file system API when running JavaScript in a Node.js environment.

5:55pm. > Alright, after this little detour you must be wondering why this is relevant to our F# implementation of httpRequest. To put it simply: F#'s Async expressions compiled with Fable are more or less the equivalent of JavaScript's Promises, they are just syntax sugar around callback-based APIs.

The important differences is that Promises memoize their results, while Asyc reruns it.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/async-xhr#fablefetch-as-an-alternative-to-fablesimplehttp

6pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/working-with-json

This is useful. I am doing JSON transfers for Spiral.

> For example, Fable.SimpleJson is the power-engine behind Fable.Remoting  and Elmish.Bridge  where the library handles the deserialization of types on the front-end correctly and efficiently.

Important one page chapter.

6:05pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/using-json

So far this book is really taking up my time, but I am absorbing it readily.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/using-json

```fs
let storeInfoDecoder : Decoder<StoreInfo> =
  Decode.object (fun get -> {
    name = get.Required.Field "name" Decode.string
    since = get.Required.Field "since" (Decode.map string Decode.int)
    daysOpen = get.Required.Field "daysOpen" (Decode.list Decode.string)
    products = get.Required.Field "products" (Decode.list productDecoder)
  })
```

This is interesting. How can this possibly have correct...

No maybe it could. After all, it is using the decoder here. With Spiral I could automate this, but sure, you could make a decoder by hand like this too.

Edit: Later it shows that F# can do it too using reflection.

6:20pm. Time for lunch.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/using-json#automatic-converters-in-thothjson

I do not remember what I am using for JSON conversion in Spiral, but I think it is some other library.

6:30pm. Having lunch here.

I thought this book would be just about UIs, but this is a decent web dev book in general.

6:50pm. Done with lunch. Let me resume.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/elmish-hackernews

Actually, let me stop here. Who is going to go on anymore.

6:55pm. As the last thing for day, I guess I'll reply to the robotics guy.

///

Hey Marko,

How are you?

Thank you for the link - the videos look very good! Let me know once you do the RL programming in Spiral ones.

Yes, it's likely that UPMEM prefers to work with someone interested in their hardware. But I think you did well to tell them that. If you find a company with interesting hardware, then it'll be easier to approach them :)

Yes, you're right about the immitation learning approach!

I should probably go for it. But for now I'm still just finding excuses not to do it... (I need more courage). But you should too! You're very passionate and super knowledgeable about this space! What would you need to focus exclusively on your ideas?

It was a long journey... I studied medicine but figured I wouldn't be a very good doctor because there were other things I preferred to do/explore. After that I spent more than a decade doing other work until coming across with coding and finding how much fun it is. When my second attempt at starting a company failed, I decided to look for a job as a software dev. It still took me 8 months of practising and almost another 8 of job search. I've been working as a software dev for almost 2 years now and loving it.

How about you, any progress on the job search front?

Take care!

///

///

> What would you need to focus exclusively on your ideas?

What else, but money? I'll need money to buy the hardware I need. If my father gets into an accident, I'll need money to support myself. Computer hardware is not infinitely durable. If something happens to my PC, how am I to replace it without money?

> How about you, any progress on the job search front?

Horrible. I thought it was just my resume, but...

https://news.ycombinator.com/item?id=34725047
Ask HN: Laid off folks, are you getting hired?

Given the economic environment with a lot of senior devs entering the market, it would be weird if anybody was interested in a hobbyist like me. I didn't get literally nothing though.

When I posted on the F# sub, one guy was interested, but for that F# position I'd need to relocate to Austria. Also I got in touch with a Serbian guy, but local salaries here in Croatia are really shitty, and even worse in Serbia, so I was never interested in working locally. As an example, while I was looking at the LinkedIn notification tab, I noticed one Cro company in the big city 1h drive away was hiring .NET devs. The salary is 12-16k euro per month. It is a waste of time.

Well, it depends on what kinds of jobs the guy manages to find. He wants to take the role of an agent/CTO and is putting together a technically capable team so we'll see how it turns out.

Personally, I am willing to work on anything as long as it is remote, but I do not want to spend my time competing for jobs as a freelancer as the jobs are always so lowly paid, which is why I am applying to startups. This gives me time to build up my webdev skills.

I have to admit, F# is really wonderful right now for this purpose. Its Fable compiler even compiles to Python these days, which gives me access to all its ML libraries.

In a way this period where nobody is calling me for interviews suits me just fine. I am not expecting anything, so I am not stressed out about the interviews. The night before the interview with the Serbian guy, I could not sleep properly.

My preference would be to work for a startup. Maybe an artist or a designer could make it as a freelancer, but just what kind of project can you build in a short amount of time as a programmer? Not much.

Anyway, there is no forcing it in the current situation. I've gotten rejected from half the places I applied to, but the rest are still pending. I'll let them float for a while. Later on, if having no pro experience turns out to be such a big deal, I'll just make some up. Let me tell you, a couple of months ago, I tried pretending to be an ex Google/Tesla/Microsoft engineer, and the places I applied to were pestering me for an interview. But the environment is not right for that.

The Serbian guy I mentioned pushed me into the direction of webdev, and I know already that most of the money is in that, so I've yielded to it. It will take me a few months to become really proficient doing it in a functional style, but after that I'll be capable of anything as a programmer. I'll make a few portfolio pieces like a CFR Leduc/Holdem agent, as well as my personal website. I still want to make Youtube vids, but the context has changed - I'll make something others can log into online and check out. The Youtube videos will be presentations of my work.

I am wondering, what is your skillset like? Python?

https://zaid-ajaj.github.io/the-elmish-book/#/

Currently I am reading this. I thought it would just be a UI book, but it is a pretty good webdev book. Back in 2020 I had a lot of trouble absorbing this as I wanted to work on Spiral and only wanted to learn enough to do the VS Code plugin for it, but now that I am diving right into it, I feel like I am absorbing it like a sponge. It is pretty fun.

///

7:40pm. This was a bit too wordy, but it is good enough. I am done for the day.

I want to read the Ragweed Princess. I've been getting into it lately. Tomorrow I will finish the Elmish book and look at the SAFE Stack examples. Oh right, I also want to look at the Feliz library. Well, one thing at a time. It won't be long before I can start work on my own projects."

---
## [jrjmt/bl](https://github.com/jrjmt/bl)@[83cacca694...](https://github.com/jrjmt/bl/commit/83cacca694d1a144b85d8d305093ade5c34b3045)
#### Friday 2023-02-10 19:02:12 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [unclamped/2based2wait](https://github.com/unclamped/2based2wait)@[259b126aa6...](https://github.com/unclamped/2based2wait/commit/259b126aa6712030c008db41f82537c32ed52662)
#### Friday 2023-02-10 19:43:09 by unclamped

refactor: use string template literals

note to more experienced, older dev me in the future: if you have found a way to make this automatically, then please feel free to laugh at your young yourself. my fingers fucking hurt.

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[ef335f7d1f...](https://github.com/Jacquerel/orbstation/commit/ef335f7d1f33d196062a5a285c7f7216df2302a6)
#### Friday 2023-02-10 19:57:54 by Rhials

It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#73018)

## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---
## [CaosCreations/SpaceTruckin](https://github.com/CaosCreations/SpaceTruckin)@[d3a9d10d8e...](https://github.com/CaosCreations/SpaceTruckin/commit/d3a9d10d8edd1e358d8e9b58d4f3aaebd663fae3)
#### Friday 2023-02-10 20:12:24 by Stefano di Pace

Proper name tags (#644)

* Name Tag Asset is IN

* More UI Stuff

Background layer, proper + Prefab stuff

* New Player Response Asset

just tried to make it a lil prettier really

* applied the prefab DURRRR

oops

* New version babyyyy

woooo

* FUCKIN FIXED THIS SHIT

BITCHEEEEZZZZ

* more fixes??

yes, more.

* last one

maybe

---------

Co-authored-by: Max <61809127+maxwellpark@users.noreply.github.com>

---
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[d30cba58c0...](https://github.com/zerbina/nimskull/commit/d30cba58c0c2c8bc353f51240f84eadaf19ebdc5)
#### Friday 2023-02-10 20:27:07 by Saem Ghani

Extract nkError diagnostics data

`nkError` has a `reportId` which unfortunately opens any possible
"report" crawling its way in there. This commit introduces a new
design where `nkError` owns it's diagnostic data, as well as,
`ast_types` where `nkError` and friends are defined, owns the data
types. `Report` and all the associated cruft now is there simply to do
rendering.

`Report` still handles, routing and final consolidation, but in future
developments that will likely evolved further.

Overall Change:
- AST/Sem drop `ReportId` and associated memory leak
- AST/Sem now define a diagnostic type and are primary data owners
- `Report` is now used in legacy situations and rendering, the former
    is to be addressed in future commits

What didn't change/major caveats:
- `structuredReportHook` still uses `Report`, this consequences...
- `concept` and `{.explain.}` related erros have regressed, their tests
    marked with known issue, as this isn't a full conversion
- diagnostics involving magics, have inconsistent rendering, a pre-
    existing issue, sorting this out is future work

Lessons and Takeaways
=====================

Each module should own/define the data types that it's fundamentally in
charge of. Modules which are effectively components, like `lexer`,
`parser`, `vm`, etc, should produce diagnostics, events, telemetry,
whatever and their caller should handle output/rendering of these. The
key part about that last point is that the renderer and its format must
not be pushed into these modules, rather the renderer should consume
what they produce (directly or via an intermediary/translation).

For those wondering about why a value type was use inside the `nkError`
instead of the current `ref object`. I ran 3 bootstrap runs with each
version of `nkError`, and with the `TAstDiag` (value type) was
consistently ~10% slower during the bootstrap process.

|run|type|real|user|sys|
|:----|:----|:----|:----|:----|
|1|pastdiag|28.675|27.056|2.527|
|2|pastdiag|28.184|26.663|1.372|
|3|pastdiag|28.276|26.682|1.446|
|1|tastdiag|31.562|29.245|3.236|
|2|tastdiag|30.453|28.413|1.871|
|3|tastdiag|30.368|28.311|1.896|

|type|real|user|sys|summary|
|:----|:----|:----|:----|:----|
|pastdiag|28.38|26.80|1.78|avg|
|tastdiag|30.79|28.66|2.33|avg|
|pastdiag| 0.20| 0.17|0.50|avg dev|
|tastdiag| 0.51| 0.39|0.60|avg dev|

The report data types are rather bloated, eg: using `Int128` for
enum `high`/`low` values.

For diagnostics, it's best to capture very little data, and then query
within the rendering layer. Temper this where querying is reproducing
complex analysis, reconstituting heavy context, or keeping data large
data sets alive just so it can be queried later.

It's very possible we don't clean-up the symbol table of abandoned
analyses. This likely results in space leaks, or rather an overhead
while processing each module.

This style of conditional `0 < foo` is forbidden, it's just not
accessible code and prone to reasoning and ultimatley logic errors.

When doing inline error state representation in a data type, such as
`TLineInfo`, where the invalid state is
`TLineInfo(line: 0, col: -1, fileIndex: InvalidFileIdx)`, the default
initiatlization of objects is not our friend. This became a minor issue
during `nkError` construction. Where the line info on the provided
`wrongNode: PNode` parameter might be invalid. Hard to say, as the
default initialization is technically a valid location. A heuristic was
put into place to work around it and I think it'll hold until we fix it
properly. I see this as a language design problem, now one could argue
that a better selection of invalid state is required, but when working
in a retroactive case such as this, it's a non-starter. Furthermore, the
ergonomics of `{.requiresInit.}` leave much to be desired. I'm not sure
what exactly the answer is, but I think this is the difference between
something very primitive like a `struct` vs an actual `object`.

A number of node consts sets in `ast_query` and related modules are not
defined as compositions of each other. This can easily lead to changes
that only impact partial parts of the compiler and introducing yet more
bugs. This might be worth of a compiler style guide remark.

Just like a large amount of imports is likely a source of issues, so are
broad exports, avoid these like the plague. Removing these from
`reports` and related modules resulted in a number of significant and
hard to debug errors -- first encountered within CI, via a `bors try`.
They manifested as a doc gen build failure, which was seen as an
undefined symbol error. All because `reports` and friends were
exporting large swaths of other modules, eg: `ast_types`. After much
debugging and fixing error diagnostics to provide recursive dependency
detection as part of those unindentifier errors, it was fixed. It wasted
an entire day. Exports just create massive public surfaces, don't do it.

Details
=======

Finally, this commit impacts a very wide swath of the compiler, lots of
code had to be updated, along with many stylistic fixes. What follows is
a list of more detailed changes, in no particular order:

`ast_types`/`nkError` higlights:
- defines all its own diagnostic data types for `nkError`
- design-wise, `nkError` nodes are now much more likely to contain the
  immediate ast they're taking the place of, like a true wrapper. This
  should allow for easy recovery by simply getting `n.diag.wrongNode`.
- call mismatch related types (`SemCallMismatch` and `SemDiagnostics`)
  moved to `ast_types`
- moved `NodeId` into `ast_types from `packed_ast`, so it can be used
  more broadly, such as in `PAstDiag` as mentioned above.
- Removed `ReportID`, instead `PAstDiag` uses the `NodeId` of the first
  error node they're embedded in` as their `diagId`. This is an easy way
  to have a monotonic sequence, while also some correlation between diag
  and error node. Due to copies, the `diagId` and `PNode` `id` can
  diverge, but that's useful information in and of itself.

`ast` procs like `newNode` no longer have to care about `sons` on
`nkError` nodes, this also stops accidental traverls.

`ast_query` literal node kind `const` as sets
  Now, various const set ranges relating to literals were defined
independently, now only the smallest sets are, while bigger sets are
defined based on the smaller sets. Going forward, this should ensure
adding new node kinds updates all broader ranges.
  means: `nkLiterals* = nkIntLiterals + nkFloatLiterals + nkStrLiterals`
  Extracting a style guide remark out of the commit message would be a
good idea.

`msgs` now bridges translating `PAstDiag` to legacy `Report` for routing
and rendering. Although, routing should probably not be part of `Report`
stuff.

Moved illformed ast message creation routines earlier in `msgs` to
reuse them when generating legacy report message strings. String
generation should move to a rendering layer in the future.

More consistent VM/Gen event to AST diag mapping, mostly within
`compilerbridge` which now has simplified/fewer pathways.

Removed `traceReason` from VM stacktrace events
  This includes legacy reports, the primary motivation is that it was
being captured and not used. Additionally, not all stacktraces can be
related back to a meaningful vm event.
  Also, the fixing up of data types also resulted in some code
simplification in vmgen and sem.

Clean-up identifier errors and fix vm err location
- cleaned up various expected identifier messages
- vm errors now capture instantiation info correctly
- errors don't set location data on diagnostics if already present, to
  honour overrides

Diag mapping in `vm` and `vmgen` was updated.
Mapping `vm` and `vmgen` events to `PAstDiag` are presently in their
respective modules as they both directly depend upon `ast_types`. Not an
ideal situation, but a lot more refactoring is required until `vm` is
free of AST knowledge/dependencies.

`options` module now manages `ReportSet` as a simple collection of
`NodeId`s of diagnostics that have been reported.

Removed `ConfigRef` param from `types.typeMismatch`, it wasn't being
used

Report Output and Generation Details
====================================

Better error for `is` with wrong number of args:
- previously: `wrong number of arguments`
- now: `'is' operator takes 2 arguments'
- fixed `tests/errmsgs/tmisc` test to match wording

Undeclared identifier errors now output any recursive modules imports
that were detected as those can be a cause of such errors.

Recursive dependency tracking from the importer is cheaper, as it now
only stores FileIndex pairs. Unfortunately, we don't have a clearing
mechanism, so new minor space leak. :/

removed some eager diag message data querying

Fixed doc gen error report rendering, which weren't outputing the full
text, making it impossible to find where errors/hints/warnings were
occurring. Without this fix, it meant an unclosed backtick in a doc
block was breaking CI... cool.

Legacy Report Related Change Details
====================================

Removed some bounds tracking in reports
  A number of `Report`s are tracking, but never using a pair of `Int128`
in order to know out of bound issues for arrays, ranges, ordinals, etc.
  The data is rarely if ever output in messages and that's a lot of
bytes in most cases. Disabled whereever this was inconvenient, it can be
restored for error messages we wish to improve as future work.
  Created `rsemBigOrdsEnergy` to not overload `mismatchCount` tuple with
`Int128` bloat, and moved the following reports there:
- `rsemSetTooBig`
- `rsemArrayExpectsPositiveRange`
- `rsemInvalidOrderInEnum`
(partial list)
  No longer capture `countMismatch` data for these as it's unreported:
- `rsemExpectedLow0Discriminant`
- `rsemExpectedHighCappedDiscriminant`
(partial list)

The `errorKind` property now returns a `TAstDiagKind`

Errors related to positions in calls where identifiers are expected have
been updated to provide a bit more context:
- dot calls, callable fields access, etc errors wording update,
    indicating the problematic identifier and then the call expression
    within which it was found. See:
    `rsemExpectedIdentifierWithExprContext` handling in `cli_reporter`
- updated `astrepr` to handle new `diag` field of `nkError` variant
Resulting in the following test changes:
- `nimsuggest` test `tchk1` updated for messages with "found" wording
    instead of "got"

`countMismatch` in reports are now `int`s, instead of `Int128`,
seiously, how many were we expecting?

The string value of `mSizeOf` as `"sizeOf"` was taken from VM tests, but
doesn't jive with other tests that serialize the same magic. Need to
figure out which convention to go by.

Regression/Caveat Details
=========================

`concept` and `{.explain.}` error msg regression
  The compiler presently doesn't emit useful diagnostics for these,
simply a count of number of diagnostics failed. The implementation is
tied up with `structuredReportHook`, which in turn uses `Report`, and
there isn't a reasonable way to turn this into `PAstDiag` for
consumption. The following tests are disabled `knownIssue`:
- tests/lang_experimental/concepts/t3330
- tests/lang_experimental/concepts/texplain
- tests/lang_experimental/concepts/twrapconcept

Misc
====

Noted issues with the `reports` module and friends, hopefully it wards
off any further profileration and people can help with incremental
rework.

`types.semReportTypeMismatch` no longer takes a `ConfigRef` parameter.
This turned out to be unnecessary/unused after all the diag changes.

`sigmatch` has fewer dependencies on `reports_sem`

`getReport` moved to `msgs`, dropped `conf` param

Creating a new use qualifier diagnostic via
`semstmts.newSymChoiceUseQualifierDiag` will assert that there are at
least two choices to avoid spurious errors.

Removed a number of compile warnings by removing unused imports.

updated `astrepr` to use ast diagnostics from `nkError` nodes.

Reduce broad exports by `Report` related modules:
- `reports` was leaking `ast_types` _everywhere_
- `reports_base` had overlapping exports

Formatting/Style clean-ups in these modules

Random Report Changes:
- remove `rsemUserRaw`, it's never used
- renamed `rrsemCompilesError` to `rsemComplesHasEffects`

Special thanks to zerbina for all the code reviews and suggestions!

Co-authored-by: zerbina <100542850+zerbina@users.noreply.github.com>

---
## [Pyr33x/discord-api-docs](https://github.com/Pyr33x/discord-api-docs)@[dd3f05a170...](https://github.com/Pyr33x/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Friday 2023-02-10 20:58:25 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[6de1258bd3...](https://github.com/Timberpoes/tgstation-nxt/commit/6de1258bd3fb5919bb45f3dac3ae801d4b3bc8d6)
#### Friday 2023-02-10 21:06:51 by Jacquerel

Admins can now choose where fish go (#73109)

## About The Pull Request

I've pigeonholed myself as the fish guy now. It seems like someone made
events easier to add admin controls for so I thought I'd add some to the
event I most recently touched.

Instead of letting the RNG choose admins can now direct a circle of carp
to converge upon a specific location, or even a trail of specific
locations if they want the carp to just sort of swim in a circle around
the space station (although the ones on the far side of the station from
the starting point will travel all the way through it to get there).
This also works with magicarp.
They don't really move fast enough for you to use this to punish a
specific person but you can use it to annoy a specific location full of
people.

Plausibly there's no reason the code _wouldn't_ work for a specified
atom instead of a turf (as long as it sticks to one z level) but I
couldn't think of an elegant way of selecting that whereas "use my
current ghost location" is very intuitive, so I didn't add one.

## Why It's Good For The Game

Plausibly this permits admins do more fun things.

## Changelog

:cl:
admin: Admins can direct where carp (or magicarp) are interested in
going when manually triggering the event
/:cl:

---
## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[5250b1fcc6...](https://github.com/skylord-a52/orbstation-andrea/commit/5250b1fcc6aca1aa6d6b0f9ec81ce6ad5fe2fa03)
#### Friday 2023-02-10 21:12:23 by san7890

Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

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

---
## [megnush/marsidol](https://github.com/megnush/marsidol)@[dd74ed509a...](https://github.com/megnush/marsidol/commit/dd74ed509af96a66b2d9ff8367e9f5452324c24f)
#### Friday 2023-02-10 21:27:55 by megnush

whitepaper

Singers and actors, gather round! The ultimate competition for aspiring artists has finally arrived! The Singer and Actor Contest is the perfect platform to showcase your talents and take your career to the next level.

Whether you're a seasoned performer or just starting out, this contest is open to all levels of experience. Showcase your singing or acting abilities to a panel of industry experts and compete for the chance to win exciting prizes and opportunities.

With a mission to support and encourage aspiring artists, this contest is designed to provide a platform to perform and share your work with the world. Whether you're a singer or an actor, this contest offers a chance to shine and gain recognition for your skills and hard work.

So what are you waiting for? Sign up today and unleash your full potential. The Singer and Actor Contest is the perfect opportunity to take your talents to the next level and achieve your dreams!

---
## [vampycat237/bayartcounter](https://github.com/vampycat237/bayartcounter)@[dae7df0df0...](https://github.com/vampycat237/bayartcounter/commit/dae7df0df0c42e3e6ba7e40ce96ddd109e57c0bf)
#### Friday 2023-02-10 22:31:35 by vampycat237

backgrounds, consistency, and style

- improved formatting on input "buttons" used in lines and shading windows ("buttons" are a better height, and infobuttons float right now)
- moved all definitions of objects/dictionaries meant for holding commonly accessed elements into v2helperscript.js
- added descriptions of what each script is for to v2.html
- background keeper object is unfortunately stored in base-value-manager.js for right now so it doesn't break but i want to make that better
- fixed several functions where i forgot to say "this." because i forgot js is silly, so many more functions should work now
- made lineart and shading classes but idk. we'll see
- added background support and you can actually count them already :)
- info window is now hidden using its own special function so it stops acting weird
- reduced / swapped out debug buttons to more relevant things. sorry showMessage tests
- removed unused craftSize section left over from v1, as that's handled in base values now
- changed "lineart bonuses" to just "lineart" to fit better with the other buttons

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[b83625045f...](https://github.com/software-mansion/react-native-reanimated/commit/b83625045f314e498fe32adc34b43ce20a77f946)
#### Friday 2023-02-10 22:49:50 by Angelika Serwa

Fix reloading when using useAnimatedKeyboard (#3932)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Fixes
https://github.com/software-mansion/react-native-reanimated/issues/3786

### Why it crashes: 
On the main thread `CADisplayLink` calls `updateKeyboardFrame` 60 times
per second. Calling `updateKeyboardFrame` calls listener on the JS side.
When reloading the runtime gets destroyed on the JavaScript thread. So
when those two things happen at the same time (which in this case
happens often) we get the crash that we're trying to call a js function
on destroyed js runtime.

### Why don't you just remove the listeners in
`NativeReanimatedModule::~NativeReanimatedModule()`, we're cleaning up
everything here:
I've tried and it appeared to work at first but I still got crashes when
running [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
and probably that's why:

![Screenshot 2023-01-11 at 23 02
18](https://user-images.githubusercontent.com/6280457/211935579-16ff642d-fb15-469b-909e-e36ba9d72781.png)
![Screenshot 2023-01-11 at 23 02
35](https://user-images.githubusercontent.com/6280457/211935599-88cb9e81-20d7-4f96-bfd0-9c3b5da13b24.png)

So when `~NativeReanimatedModule` is being called the runtime related
stuff is already deleted and there is a short window of time that the
runtime is being deleted and we still call js stuff, or at least that's
my theory 🤷‍♀️

So my proposition for now is to listen for
`RCTBridgeDidInvalidateModulesNotification` notification. It's called
just before deleting happens. Also I'm using
`RCTUnsafeExecuteOnMainQueueSync` because I want to wait until the
listeners are completely deleted on the main thread and then delete js
stuff.

### A nicer solution? 
If you look a bit above `[[NSNotificationCenter defaultCenter]
postNotificationName:RCTBridgeDidInvalidateModulesNotification` line in
React code you'll see that React calls `invalidate` on all modules' data
before even posting the notification. Maybe we should clean reanimated
stuff here. I haven't explored that though yet and I don't know where is
reanimated's module data and what is module data at all and where to put
that `invalidate` function, I just got this idea while posting this PR.

## Test plan

Just run AnimatedKeyboardExample and reload the app.
Also the [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
nicely catches other data races.

Tested with changes from
https://github.com/software-mansion/react-native-reanimated/pull/3911
and it works
Also tested on FabricExample and surprisingly it also works.

---
## [elastic/kibana](https://github.com/elastic/kibana)@[43fa5174f8...](https://github.com/elastic/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Friday 2023-02-10 22:57:50 by Clint Andrew Hall

[kibana] Thank you for everything, Spencer! 🧔🏻‍♂️ (#150759)

## Summary

> _Inspired by @kertal, and extracted from his PR
https://github.com/elastic/kibana/pull/150660, specifically
@thomasneirynck's
[proposal](https://github.com/elastic/kibana/pull/150660/files#r1101795511)._
>
> _Holding for 24 hours, for our friends in later time zones._

Several of us felt a dev-only easter egg-- where, if you're lucky,
@spalger joins you as you test your latest feature-- would be a fun
tribute as he leaves us for new and exciting opportunities.

Elasticians, feel free to send your love to @spalger in the channel of
your choice, of course, but we'd appreciate your review of this pull
request. ❤️


![image](https://user-images.githubusercontent.com/1178348/217867285-b23dcf1f-1a4a-45fd-b828-f6b24215fef2.png)

---------

Co-authored-by: spalger <spencer@elastic.co>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[7fa0d7a5ec...](https://github.com/Buildstarted/linksfordevs/commit/7fa0d7a5ec0706737c9ea16d60a989f8e7b17228)
#### Friday 2023-02-10 23:09:14 by Ben Dornis

Updating: 2/10/2023 11:00:00 PM

 1. Added: Sit. · Rafal Pastuszak
    (https://sonnet.io/posts/sit/)
 2. Added: In defense of Junior Engineers - Jampa.dev
    (https://jampa.dev/posts/why-when-and-how-to-hire-junior-software-engineers)
 3. Added: User or *User - Do We Need Struct Pointers Everywhere?
    (https://preslav.me/2023/02/06/golang-do-we-need-struct-pointers-everywhere/)
 4. Added: The Joy Of Duplexes
    (https://codahale.com/the-joy-of-duplexes/)
 5. Added: On Vercel: If some of my sites are down…
    (https://remysharp.com/2023/01/30/on-vercel-if-some-of-my-sites-are-down)
 6. Added: I hate stackoverflow and ChatGPT is my savior
    (https://fgclue.wordpress.com/2023/02/09/i-hate-stackoverflow-and-chatgpt-is-my-savior/)
 7. Added: Extreme earners are not extremely smart
    (https://liu.se/en/news-item/de-som-tjanar-mest-ar-inte-smartast)
 8. Added: Data visualization with Metabase from CSV files with SQLite - Ritza Articles
    (https://ritza.co/articles/data-visualisation-with-metabase-from-csv/)
 9. Added: Efficiency traps
    (https://jorzel.github.io/efficency-traps/)
10. Added: What's On Tap for .NET 8 (Preview 1 Coming this Month) -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/02/10/net-8-preview.aspx)
11. Added: Why do you want to touch your Mac screen so badly?
    (https://morrick.me/archives/9715)
12. Added: My most important email filter that helps me control my chaos
    (https://martin.sh/reduce-noise-by-filtering-newsletters/)
13. Added: The Pareto frontier of foreign languages - Tanner Hoke
    (https://tannerhoke.com/posts/pareto-languages/)
14. Added: We Should Communicate Probabilities With Flips
    (https://blog.charliemeyer.co/we-should-communicate-probabilities-with-flips/)
15. Added: Experimenting with PeerJS
    (https://rtnf.bearblog.dev/experimenting-with-peerjs/)

Generation took: 00:09:05.7670844
 Maintenance update - cleaning up homepage and feed

---

