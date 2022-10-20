## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-19](docs/good-messages/2022/2022-10-19.md)


2,284,094 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,284,094 were push events containing 3,393,880 commit messages that amount to 254,616,359 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[fc7c186957...](https://github.com/san7890/bruhstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Wednesday 2022-10-19 00:05:42 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [LeonCanek/JustoLeon](https://github.com/LeonCanek/JustoLeon)@[fe2aeeb67c...](https://github.com/LeonCanek/JustoLeon/commit/fe2aeeb67c68476068121321a07260a6c194fdd8)
#### Wednesday 2022-10-19 00:40:21 by Justo Leon

Hoy fue un buen dia

Well, if you wanted honesty
That's all you had to say
I never want to let you down
Or have you go, it's better off this way

For all the dirty looks
The photographs your boyfriend took
Remember when you broke your foot
From jumping out the second floor?

I'm not okay
I'm not okay
I'm not okay
You wear me out

What will it take to show you
That it's not the life it seems? (I'm not okay)
I've told you time and time again
You sing the words, but don't know what it means (I'm not okay)

To be a joke and look
Another line without a hook
I held you close as we both shook
For the last time, take a good hard look

I'm not okay
I'm not okay
I'm not okay
You wear me out

---
## [boost-entropy-typescript/apollo-server](https://github.com/boost-entropy-typescript/apollo-server)@[d0d8f4be70...](https://github.com/boost-entropy-typescript/apollo-server/commit/d0d8f4be705065745bd3767a62b8025abe774842)
#### Wednesday 2022-10-19 01:00:53 by Trevor Scheer

Distribute `@apollo/server-integration-testsuite` as CJS (correctly) (#7055)

Right now the integration testsuite package declares `"type": "module"`
but builds as CJS. This seems to be problematic for some integrations,
and we should resolve the misconfiguration.

This also moves the tsconfig/build "things" over to the CJS branch of
our build step. This also removes the ESM configuration options for how
we run jest/ts-jest in this repo.

Confirmed this doesn't cause a regression in our local dev in that a
change in test code is immediately reflected in a test run without
running an additional build.

Fixes #7042

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [michaelpq/postgres](https://github.com/michaelpq/postgres)@[8272749e8c...](https://github.com/michaelpq/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Wednesday 2022-10-19 03:30:19 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [ElizabethKennedy/speech_detection](https://github.com/ElizabethKennedy/speech_detection)@[f71c240d5f...](https://github.com/ElizabethKennedy/speech_detection/commit/f71c240d5f4fb5fa9592cff3d1c7ea8115a48453)
#### Wednesday 2022-10-19 05:16:37 by Elizabeth Kennedy

Create README.md

Don't be fooled, it isn't a mistake: I intentionally left my name in the footer / attribution area as a color so dark, it is difficult to discern the text against the highly-pigmented deep magenta background color. A personal preference, naturally. I decided I like the hyperlink-- which leads directly to my Github-hosted portfolio when clicked --  remaining boldly enshrouded by the darkness of the shadowlands, until the reader is intrigued enough to bite the aforementioned subtly alluring clickbait. Once clicked, the hyperlink is illuminated in a most vibrant, eye-popping electric red hue by what feels like a 500 horsepower engine. (PS: I don't know much about cars, so honestly I could be mixing metaphors, but... I couldn't care less. I can build a house with my own two hands. So there. I might need a mitre saw, a few orbital sanders, an industrial-strength and -size jackhammer, caulking, grout, paints, plaster, drywall, insulation, flooring, roofing, hammers, nails, rebar, electrical wiring, several drills plus the bits and LOTS of high-quality lumber, JUST for starters... but you get the picture.)

---
## [x-em/guava](https://github.com/x-em/guava)@[e015172847...](https://github.com/x-em/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Wednesday 2022-10-19 06:11:36 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [hombremichelin/mpv](https://github.com/hombremichelin/mpv)@[6f7506b660...](https://github.com/hombremichelin/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Wednesday 2022-10-19 06:19:46 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [macdice/postgres](https://github.com/macdice/postgres)@[1d072bd203...](https://github.com/macdice/postgres/commit/1d072bd2030af0f2eaa522449028ff160f71ebf8)
#### Wednesday 2022-10-19 08:35:49 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[c9e78c723e...](https://github.com/GeoB99/reactos/commit/c9e78c723ee4229eb9e3eda0b3858c052145c61c)
#### Wednesday 2022-10-19 08:54:45 by George Bișoc

[NTOS:CM] Implement registry checks & recovery

Instead of having the CmCheckRegistry implementation in the kernel, it's better to have it in the Configuration Manager library instead (aka CMLIB). The benefits of having it in the library are the following:

- CmCheckRegistry can be used in FreeLdr to fix the SYSTEM hive
- It can be used on-demand in the kernel
- It can be used for offline registry repair tools
- It makes the underlying CmCheckRegistry implementation code debug-able in user mode

[SDK][CMLIB] Declare HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL boot types

=== DOCUMENTATION REMARKS ===

HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL are boot type values set up by the CMLIB library. HBOOT_TYPE_REGULAR indicates a normal system boot whereas HBOOT_TYPE_SELF_HEAL indicates the system boot is assisted within self healing mode.

Whether the former or the latter value is set it's governed by both the kernel and the bootloader. The bootloader and the kernel negotiate together to determine if any of the registry properties (the hive, the base block, the registry base, etc) are so severed from corruption or not. In extreme cases where
registry healing is possible, the specific base block of the damaged hive will have its flags marked with HBOOT_TYPE_SELF_HEAL. At this point the boot phase procedure is orchestrated since the boot phase no longer goes on the default path but it's assisted, as I have already said above.

[SDK][CMLIB] Implement two names & Unicode names comparison functions

CmpCompareBothCompressedNames and CmpCompareDistinctNames are necessary for lexicographical order validation code when validating the key in question.

[SDK][CMLIB] Implement self-heal registry helpers

This implements cmheal.c file which provides the basic registry self-heal infrastructure needed by the public CmCheckRegistry function. The infrastructure provides a range of various self-heal helpers for the hive, such as subkey, class, values and node healing functions.

[SDK][CMLIB] Implement CmCheckRegistry and validation private helpers

CmCheckRegistry is a function that provides the necessary validation checks for a registry hive. This function usually comes into action when logs have been replayed for example, or when a registry hive internals have changed such as when saving a key, loading a key, etc.

This commit implements the whole Check Registry infrastructure (cmcheck.c) in CMLIB library for ease of usage and wide accessibility across parts of the OS. In addition, two more functions for registry checks are also implemented -- HvValidateHive and HvValidateBin.

CORE-9195
CORE-6762

[NTOS:CM] Use the appropriate flags on functions that will call CmCheckRegistry & add missing CmCheckRegistry calls

In addition to that, in some functions like CmFlushKey, CmSaveKey and CmSaveMergedKeys we must validate the underlying hives as a matter of precaution that everything is alright and we don't fuck all the shit up.

[NTOS:CM] Don't lazy flush the registry during unlocking operation

Whenever ReactOS finishes its operations onto the registry and unlocks it, a lazy flush is invoked to do an eventual flushing of the registry to the backing storage of the system. Except that... lazy flushing never comes into place.

This is because whenever CmpLazyFlush is called that sets up a timer which needs to expire in order to trigger the lazy flusher engine worker. However, registry locking/unlocking is a frequent occurrence, mainly when on desktop. Therefore as a matter of fact, CmpLazyFlush keeps removing and inserting the timer and the lazy flusher will never kick in that way.

Ironically the lazy flusher actually does the flushing when on USETUP installation phase because during text-mode setup installation in ReactOS the frequency of registry operations is actually less so the timer has the opportunity to expire and fire up the flusher.

In addition to that, we must queue a lazy flush when marking cells as dirty because such dirty data has to be flushed down to the media storage of the system. Of course, the real place where lazy flushing operation is done should be in a subset helper like HvMarkDirty that marks parts of a hive as dirty but since we do not have that, we'll be lazy flushing the registry during cells dirty marking instead for now.

CORE-18303

[NTOS:CM][CMLIB] Use HBOOT_TYPE_REGULAR / HBOOT_TYPE_SELF_HEAL indicators for boot type instead of hardcoded values

[NTOS:CM] Disable hard errors when setting up a new size for a hive file / annotate CmpFileSetSize parameters with SAL

During a I/O failure of whatever kind the upper-level driver, namely a FSD, can raise a hard error and a deadlock can occur. We wouldn't want that to happen for particular files like hives or logs so in such cases we must disable hard errors before toying with hives until we're done.

In addition to that, annotate the CmpFileSetSize function's parameters with SAL.

[NTOS:CM] Ignore syncing/flushing requests after registry shutdown

When shutting down the registry of the system we don't want that the registry in question gets poked again, such as flushing the hives or syncing the hives and respective logs for example. The reasoning behind this is very simple, during a complete shutdown the system does final check-ups and stuff until the computer
shuts down.

Any writing operations done to the registry can lead to erratic behaviors. CmShutdownSystem call already invokes a final flushing of all the hives on the backing storage which is more than enough to ensure consistency of the last session configuration. So after that final flushing, mark HvShutdownComplete as TRUE indicating
that any eventual flushing or syncying (in the case where HvSyncHive gets called) request is outright ignored.

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Wednesday 2022-10-19 09:50:50 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [LineageOS/android_kernel_xiaomi_msm8996](https://github.com/LineageOS/android_kernel_xiaomi_msm8996)@[c4ca2ad31b...](https://github.com/LineageOS/android_kernel_xiaomi_msm8996/commit/c4ca2ad31baca47560368c7aed461be59f5b837b)
#### Wednesday 2022-10-19 09:51:33 by Christian Brauner

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
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[340b6d5597...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/340b6d559771bccdd99c0cb4ffef4e354420cf59)
#### Wednesday 2022-10-19 10:11:32 by George Spelvin

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
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [evoliee/comp309](https://github.com/evoliee/comp309)@[41b1aa4e7c...](https://github.com/evoliee/comp309/commit/41b1aa4e7cdc8c37136e5632baec4baee83e2a7c)
#### Wednesday 2022-10-19 10:44:07 by evoliee

fuck you too kernel

please work i love you please work i beg you

---
## [go-bayes/outcome-wide](https://github.com/go-bayes/outcome-wide)@[ed52df4f88...](https://github.com/go-bayes/outcome-wide/commit/ed52df4f88a2433b829eaf37943496c8008655df)
#### Wednesday 2022-10-19 12:02:02 by Joseph Bulbulia

added forest plot to several studies

church, belief in god, belief in spirit, forgiveness.

---
## [ShivaAdhikari7/Projects](https://github.com/ShivaAdhikari7/Projects)@[362b90a3ef...](https://github.com/ShivaAdhikari7/Projects/commit/362b90a3ef57697c93da18622e0b0104dd596ed3)
#### Wednesday 2022-10-19 12:09:52 by Shiva Adhikari

starting the best journey of my life in alam devi kota now I know that god will help me to achieve everything I want. Thank you god for everything

---
## [mosra/magnum-integration](https://github.com/mosra/magnum-integration)@[8fdf1479bf...](https://github.com/mosra/magnum-integration/commit/8fdf1479bf01109d4171ba43496eea9578c120b0)
#### Wednesday 2022-10-19 13:18:33 by Vladimír Vondruš

package/archlinux: don't build DartIntegration in the dev PKGBUILD.

I'm tired of this thing. The libdart package is in AUR and depends on
a fractal consisitng of about 90 packages, including OSG, blas, TBB and
lapack, many of which take 30+ GB RAM to build and include tests and all
other crap. And then, once I suffer through all that, it will crash
right after start because *the damn thing* sends unaligned allocations
to Eigen AVX code, blowing up.

No. Enough suffering. Not worth my time. The only place where this thing
is built is on a single CI job, and even that is painful. DART has to
fix its dependency tree, it's not my job to do that for them.

---
## [sveneld/symfony](https://github.com/sveneld/symfony)@[338daf25c9...](https://github.com/sveneld/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Wednesday 2022-10-19 13:20:42 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [BurnoutDV/YoutubeVideoTexts](https://github.com/BurnoutDV/YoutubeVideoTexts)@[963f94a9cd...](https://github.com/BurnoutDV/YoutubeVideoTexts/commit/963f94a9cd7172d122486a121bd66e03892c7b04)
#### Wednesday 2022-10-19 15:52:02 by BurnoutDV

Update for Y5 and ER
at long lost i found time to hack into my keyboard for a while to write some descriptions, i think some of them are kinda dull but it's not the worst. Afterall its small filler info i like to add as supplementary thoughts and not a second Dickens

---
## [choppy-doppy/choppy-doppy.github.io](https://github.com/choppy-doppy/choppy-doppy.github.io)@[ae83acea88...](https://github.com/choppy-doppy/choppy-doppy.github.io/commit/ae83acea88eac64c8be6484848e28fe4d35595de)
#### Wednesday 2022-10-19 16:17:26 by Choppy

im an absolute dumbass i forgot to close the stupid ass fuckign stylesheet <link> html sucks i hate this im gonn a cry

---
## [DewwiB/react_app](https://github.com/DewwiB/react_app)@[ba241a4668...](https://github.com/DewwiB/react_app/commit/ba241a466885c57051f2211c3d97c14976b5a5b1)
#### Wednesday 2022-10-19 16:55:23 by Dewi Brightman

Merge pull request #18 from DewwiB/training/expensedate

fuck you

---
## [HaodongMo/ARC-9](https://github.com/HaodongMo/ARC-9)@[16afb9303a...](https://github.com/HaodongMo/ARC-9/commit/16afb9303a08f68a04be5e2c249aeb3aba19eb8f)
#### Wednesday 2022-10-19 17:04:27 by 1darky

The charm shaker; gimme the charm shaker, dude, shake your charm!

Oh, you got an charm on you alright. See that's what he's talking about. Spread your menu open, dude. You can do the charm shaker, huh? The charm shaker; gimme the charm shaker, dude, shake your charm ! Take your hands off it and shake that charm . Customize your gun up, I know you can shake it, shake it! Yeah that's some charm right there. Oh yeah, that'll work. You got the att.lua, dude! God damn. Look good, bro? Yes. Yeah nice, huh? Alright that'll work for him.

---
## [seventwentyseven/gulag](https://github.com/seventwentyseven/gulag)@[a77031162a...](https://github.com/seventwentyseven/gulag/commit/a77031162a0b4aed5feb8b9d90327863cbe09558)
#### Wednesday 2022-10-19 17:55:35 by def750

Rework total pp and acc calculation yet again (I hate my life)

---
## [DeNic0la/vocabify](https://github.com/DeNic0la/vocabify)@[19f2d380cc...](https://github.com/DeNic0la/vocabify/commit/19f2d380ccb001939bcfdf95fea5e346588f6a6d)
#### Wednesday 2022-10-19 18:37:53 by DeNic0la

Merge pull request #184 from DeNic0la/fix-se-things

fix things - fucking hate whoever coded that shit

---
## [lfd/jailhouse](https://github.com/lfd/jailhouse)@[ac50e8248a...](https://github.com/lfd/jailhouse/commit/ac50e8248a3f17815b61664e9fcd5d8ebc73a161)
#### Wednesday 2022-10-19 19:16:00 by Ralf Ramsauer

hypervisor: riscv: add SSTC support

SSTC (Supervisor-level timecmp) is an extension to bypass SBI calls to
control the platform's timer. If SSTC is available, the supervisor can
directly write the next timeout into the stimecmp CSR, instead of
conducting a SBI call. Furthermore, platform timer IRQs will directly
arrive at S-Mode resp. VS-Mode w/o M-Mode reinjection, which saves time
up on timer arrivals.

SSTC supports virtualisation: VS-Mode's stimecmp is shadowed by
vstimecmp. This means, if SSTC is available, we can save up to two
context switches for arming timers.

So we have drastically fewer exits with SSTC.

Linux (since v6.0) will discover and enable SSTC during the
initialisation of the platform timer, and from then on use the stimecmp
CSR for arming the timer instead of calling SBI. Actually pretty easy.

Some important notes of the specification [1]:

  - Discovery of SSTC is done via misa CSR, or via device tree

  - Spec says that the S-Mode hypervisor should write to vstimecmp if
    the VS_Mode guest decides to csr_write(stimecmp), as this saves a
    detour through SBI.

  - However, SBI calls are of course still supported

My thoughts:

When initialising Jailhouse, we're not allowed to query misa. Further,
we don't have the device tree available. Now we could either pass the
availability of SSTC via the driver (Linux already did discovery for
us), or hard code it in the system configuration. Ugly, both. But can we
avoid discovery?

If SSTC is available, Linux will simply make use of it.
If SSTC is not available, then Linux won't use the stimecmp CSR.

So just enable SSTC in HENVCFG, even if it is not available: It won't
affect anything, it's just ignored.

Last, spec says that if SSTC is available, an 'old-school' OpenSBI timer
set by a VS-Mode guest should take the vstimecmp fast-path in HS-Mode.
We could do this in Jailhouse, but then we must be sure, if SSTC is
*really* available.

As no guest should use the OpenSBI interface when SSTC is available,
simply take the SBI detour on those platforms. We're doomed in those
cases anyway.

Let's not implement SSTC discovery for the moment.

[1] https://drive.google.com/file/d/1f4DyxZMzl3yH7KGKXJFZ_iUY_AU9az_K/view

Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>

---
## [MajorTanya/DTbot](https://github.com/MajorTanya/DTbot)@[7e29b5cdbd...](https://github.com/MajorTanya/DTbot/commit/7e29b5cdbda0a29dc600c121c864b4702c7f4778)
#### Wednesday 2022-10-19 20:54:51 by MajorTanya

Remove commands that could violate Discovery ToS

We were notified by Discord that some (unspecified) content of DTbot was in violation of Discord's content policy for App Discovery.

In trying our best to adhere to these policies and to get DTbot accessible to more users, we have removed the following commands:
- Violent content: /bite, /choke, /kick, /kill, /whip
- Sexual content: /lewd
- Gambling-adjacent or addictive content: /roulette bet, /roulette spin, /roulette table, /russianroulette

We do not know if this will be the extent of removals, but to us, these seem to be the only commands that could possibly be violations.

We're sorry for the feature loss on v3, and hope you will continue to enjoy DTbot v3.

---
## [evantaur/brands](https://github.com/evantaur/brands)@[119f01b500...](https://github.com/evantaur/brands/commit/119f01b5004b2d168b8e5d2232252164c3ebfe28)
#### Wednesday 2022-10-19 21:03:23 by evantaur

Add files via upload

<!--
  You are amazing! Thanks for contributing to our project!
  Please, DO NOT DELETE ANY TEXT from this template! (unless instructed).
-->
## Proposed change
<!-- 
  Describe the big picture of your changes here to communicate to the
  maintainers why we should accept this pull request.
-->
Upload icon for seiverkot

## Type of change
<!--
  What type of change does your PR introduce to the Home Assistant Brands?
  NOTE: Please, check only 1! box! 
  If your PR requires multiple boxes to be checked, you'll most likely need to
  split it into multiple PRs. This makes things easier and faster to code review.
-->

- [ ] Add a new logo or icon for a new core integration
- [ ] Add a missing icon or logo for an existing core integration
- [ x] Add a new logo or icon for a custom integration (custom component)
  - [ ] I've opened up a PR for my custom integration on the [Home Assistant
    Python wheels repository](https://github.com/home-assistant/wheels-custom-integrations)
- [ ] Replace an existing icon or logo with a higher quality version
- [ ] Removing an icon or logo

## Additional information
<!--
  Details are important, and help maintainers processing your PR.
  Please be sure to fill out additional details, if applicable.
-->

- This PR fixes or closes issue: fixes #
- Link to code base pull request: 
- Link to documentation pull request: 
- Link to integration documentation on our website: 

## Checklist
<!--
  Put an `x` in the boxes that apply. You can also fill these out after
  creating the PR. If you're unsure about any of them, don't hesitate to ask.
  We're here to help! This is simply a reminder of what we are going to look
  for before merging your contribution.
-->

- [x] The added/replaced image(s) are **PNG**
- [x] Icon image size is 256x256px (`icon.png`)
- [ ] hDPI icon image size is 512x512px for  (`icon@2x.png`)
- [ ] Logo image size has min 128px, but max 256px, on the shortest side (`logo.png`)
- [ ] hDPI logo image size has min 256px, but max 512px, on the shortest side (`logo@2x.png`)

<!--
  Thank you for contributing <3
-->

---
## [gozulio/coyote-bayou](https://github.com/gozulio/coyote-bayou)@[288f673652...](https://github.com/gozulio/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Wednesday 2022-10-19 21:08:00 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [clustergrowling/clustergrowling.github.io](https://github.com/clustergrowling/clustergrowling.github.io)@[2cab7bb599...](https://github.com/clustergrowling/clustergrowling.github.io/commit/2cab7bb59976aec2d5ac1db9a30ba1530cc0864e)
#### Wednesday 2022-10-19 21:14:23 by Cluster

oh my god please shut up

stop flooding my fucking email with PRs

---
## [ProtivogaSpriter/STALKER-13](https://github.com/ProtivogaSpriter/STALKER-13)@[1ad74ef093...](https://github.com/ProtivogaSpriter/STALKER-13/commit/1ad74ef0939fc81f96ea3e4485a0b82406a6d22e)
#### Wednesday 2022-10-19 21:36:25 by ProtivogaSpriter

FUCK YOU FUCK YOU

FUCK YOU!!!!

this literally comments out the entire renegades job file

---
## [brodoluca/LosTrucksHermanos](https://github.com/brodoluca/LosTrucksHermanos)@[d0e3052e5d...](https://github.com/brodoluca/LosTrucksHermanos/commit/d0e3052e5d439f7ab9ee0dc4121f6c969339fd7e)
#### Wednesday 2022-10-19 22:14:04 by Luca Brodo

Second iterations of the diagrams. I did some refinments here and there. Second iteration of the implementation. i basically just included some boiler plate code and added the library we need for the task. MMh the library is in my opinion not suitable for the task, we should discuss it with the professor my friends

---
## [tayaphidoux/OpenCollar](https://github.com/tayaphidoux/OpenCollar)@[cfb5df84f9...](https://github.com/tayaphidoux/OpenCollar/commit/cfb5df84f935d6e30396705e5909a0662125b2bf)
#### Wednesday 2022-10-19 22:19:02 by tayaphidoux

update version checcking for future.


[14:42:06 PDT] ròan [Silkie Sabra]: updated the version and rezzed another collar but still no change to the collar text
[14:42:29 PDT] ròan [Silkie Sabra]: something else has to change in oc_core?
[14:44:26 PDT] taya Maruti: @luna:~/Documents/lsl/OpenCollar$ grep -r version.txt
grep: .git/index: binary file matches
src/collar/oc_core.lsl:                g_kUpdateCheck = llHTTPRequest("https://raw.githubusercontent.com/OpenCollarTeam/OpenCollar/master/web/version.txt",[],"");
src/collar/oc_core.lsl:                if(g_iAmNewer)g_kCheckDev = llHTTPRequest("https://raw.githubusercontent.com/OpenCollarTeam/OpenCollar/master/web/dev_version.txt",[],"");

[14:44:45 PDT] taya Maruti: might need to do both sorry had to go afk for a moment
[14:45:27 PDT] ròan [Silkie Sabra]: I did both
[14:46:55 PDT] taya Maruti: the rc versions i have are 8.2.2030 so it has to be newer or equal to that
[14:47:40 PDT] taya Maruti: what ever you put to as the core version is what its checking against
[14:49:16 PDT] ròan [Silkie Sabra]: 8.2.2000
[14:50:04 PDT] ròan [Silkie Sabra]: the integers in the third decimal place are separate placeholders, not sequential, like a library decimal system
[14:51:39 PDT] taya Maruti: 8.2.2000 is less than 8.2.2030 if you are are using one of the rc versions
[14:53:58 PDT] taya Maruti: line 372 is the function that breaks up the version string and compares the numbers
[14:54:43 PDT] ròan [Silkie Sabra]: then the system we devised for version naming won't work
[14:54:52 PDT] taya Maruti: it converts 8.2.2000 to 822000 and compares it with 822030
[14:55:10 PDT] taya Maruti: atleast with my colar versions
[14:55:12 PDT] ròan [Silkie Sabra]: look at the top of oc_core where it gives a legend for versioning
[14:55:20 PDT] taya Maruti: the release should be higher or equal to the rc versions
[14:55:43 PDT] taya Maruti: yes i see 8.2.2000
[14:55:56 PDT] ròan [Silkie Sabra]: that's not going to work if the script is converting those places to simple numbers
[14:56:08 PDT] ròan [Silkie Sabra]: look at the text explaining that
[14:56:28 PDT] taya Maruti: Compare(string V1, string V2){
    NEW_VERSION=V2;

    if(V1==V2){
        UPDATE_AVAILABLE=FALSE;
        return;
    }
    V1 = llDumpList2String(llParseString2List(V1, ["."],[]),"");
    V2 = llDumpList2String(llParseString2List(V2, ["."],[]), "");
    integer iV1 = (integer)V1;
    integer iV2 = (integer)V2;

    if(iV1 < iV2){
        UPDATE_AVAILABLE=TRUE;
        g_iAmNewer=FALSE;
    } else if(iV1 == iV2) return;
    else if(iV1 > iV2){
        UPDATE_AVAILABLE=FALSE;
        g_iAmNewer=TRUE;

       // llSetText("", <1,0,0>,1); //Not sure what this is for, but seems unnecessary? Commented out unless someone finds a reason for>
    }
}

[14:56:36 PDT] ròan [Silkie Sabra]: LEGEND: Major.Minor.Build RC Beta Alpha
[14:57:04 PDT] ròan [Silkie Sabra]: so 8.2.2030 meant 8.2.2 beta 3
[14:57:33 PDT] taya Maruti: llparse string needs to instead of being dumped split into llList2String(parsed,0)+llList2String(parsed,1); in order for it to not use the third spot
[14:57:52 PDT] taya Maruti: that code just removes the . as it is
[14:58:30 PDT] taya Maruti: but then you would also have to change legacy collars
[14:58:49 PDT] taya Maruti: which makes the update process all that much more complicatd
[14:58:53 PDT] ròan [Silkie Sabra]: might be easier to change the way the versioning is supposed to read
[15:00:12 PDT] taya Maruti: what ever you have to do you either have to change the code to match what you want or you have to work with the code as it is and change your thinking
[15:00:26 PDT] taya Maruti: now is the time to do that
[15:00:45 PDT] taya Maruti: we can still patch the versioning code in the current version so that the next update works the way you want it
[15:01:54 PDT] taya Maruti: llList2String(parsed,0)+llList2String(parsed,1)+llGetSubString(llList2String(parsed,2),0,0);
[15:01:59 PDT] taya Maruti: that would get 8.2.2
[15:02:29 PDT] taya Maruti: or 822 for the check
[15:03:55 PDT] taya Maruti: however the changes made should work for all collars below 822000 or 8.2.2000 in context
[15:04:09 PDT] taya Maruti: most of the stable releases
[15:04:18 PDT] taya Maruti: it won't update the rc candidates
[15:05:58 PDT] ròan [Silkie Sabra]: can you make a pr? because my brain is fried and i think Medea needs to make the call
[15:09:30 PDT] taya Maruti: the only major qustion is should i just go a head and pr as master or do we need a new quarter
[15:10:17 PDT] ròan [Silkie Sabra]: we need this in the master, before 8.2.2 can go out to the vendor
[15:10:36 PDT] ròan [Silkie Sabra]: then we'll make a new branch for the next version but i don't think it will specify quarter
[15:10:56 PDT] ròan [Silkie Sabra]: because we're in quarter 4 now and just managed to get q1 into the can

---
## [git/git](https://github.com/git/git)@[d3775de074...](https://github.com/git/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Wednesday 2022-10-19 23:17:34 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [LePtite/AI-for-autistic-children](https://github.com/LePtite/AI-for-autistic-children)@[1b40a7ef13...](https://github.com/LePtite/AI-for-autistic-children/commit/1b40a7ef13c045d50674da8ea6b57c2f0f23839b)
#### Wednesday 2022-10-19 23:29:46 by LePtite

Update README.md

People with autism spectrum disorder have difficulty identifying the facial expressions and emotions of others.
This aforementioned feature will help individuals with autism spectrum disorder (ASD) since they are lacking the ability to identify and understand the thoughts and feelings of others.
The program is going to be like a trusted friend that explain to the user what kind of expression is being made by others.
Universities and employers that hire autistic people are the one who are going to use our technology

---
## [peff/git](https://github.com/peff/git)@[4b13366e06...](https://github.com/peff/git/commit/4b13366e068e1e227cccf9d8c19d13740fe798b8)
#### Wednesday 2022-10-19 23:55:11 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[5dfc5ef62d...](https://github.com/peff/git/commit/5dfc5ef62daf8c376e8eb82eef895ecfdbd653b1)
#### Wednesday 2022-10-19 23:55:35 by Jeff King

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

