## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-29](docs/good-messages/2022/2022-01-29.md)


1,436,665 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,436,665 were push events containing 2,182,764 commit messages that amount to 131,441,887 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [RTEMS/gnu-mirror-gcc](https://github.com/RTEMS/gnu-mirror-gcc)@[aeac414923...](https://github.com/RTEMS/gnu-mirror-gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Saturday 2022-01-29 00:23:55 by Thomas Schwinge

Revert "Fix PR 67102: Add libstdc++ dependancy to libffi" [PR67102]

This reverts commit db1a65d9364fe72c2fff65fb2dec051728b6f3fa.

On 2021-09-17T01:01:39-0700, Andrew Pinski via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
> On Fri, Sep 17, 2021 at 12:46 AM Thomas Schwinge <thomas@codesourcery.com> wrote:
>> On 2021-09-15T13:56:37-0700, apinski--- via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
>> > The error message is obvious -funconfigured-libstdc++-v3 is used
>> > on the g++ command line.  So we just add the dependancy.
>>
>> > --- a/Makefile.def
>> > +++ b/Makefile.def
>> > @@ -592,6 +592,7 @@ dependencies = { module=configure-target-fastjar; on=configure-target-zlib; };
>> >  dependencies = { module=all-target-fastjar; on=all-target-zlib; };
>> >  dependencies = { module=configure-target-libgo; on=configure-target-libffi; };
>> >  dependencies = { module=configure-target-libgo; on=all-target-libstdc++-v3; };
>> > +dependencies = { module=configure-target-libffi; on=all-target-libstdc++-v3; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libbacktrace; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libffi; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libatomic; };
>>
>> I'm confused, because given that this 'Makefile.def' change only has the
>> following effect:
>>
>> > --- a/Makefile.in
>> > +++ b/Makefile.in
>> > @@ -61261,6 +61261,7 @@ all-bison: maybe-all-intl
>> >  all-flex: maybe-all-intl
>> >  all-m4: maybe-all-intl
>> >  configure-target-libgo: maybe-all-target-libstdc++-v3
>> > +configure-target-libffi: maybe-all-target-libstdc++-v3
>> >  configure-target-liboffloadmic: maybe-configure-target-libgomp
>> >  all-target-liboffloadmic: maybe-all-target-libgomp
>> >  configure-target-newlib: maybe-all-binutils
>>
>> ... isn't that actually a no-op, because we already had such a dependency
>> listed?  Now twice:
>>
>>     $ grep -n -F 'configure-target-libffi: maybe-all-target-libstdc++-v3' -- Makefile.in
>>     61264:configure-target-libffi: maybe-all-target-libstdc++-v3
>>     61372:configure-target-libffi: maybe-all-target-libstdc++-v3
>>
>> Compared to the existing one, the one you've added is additionally
>> restricted by '@unless gcc-bootstrap'.
>>
>> I noticed this as I remembered that on our og[...] development branches
>> we have a patch in the opposite direction: get rid of this dependency via
>> removing 'lang_env_dependencies = { module=libffi; cxx=true; };' from
>> 'Makefile.def'.  See
>> <http://mid.mail-archive.com/alpine.DEB.2.21.9999.1812201344250.99920@build7-trusty-cs.sje.mentorg.com>
>> "Disable libstdc++ dependency for libffi".  (Maciej CCed in case you have
>> any further thoughts on that.)
>
> Oh, I see what happened now, the old bug was actually fixed by r6-5415
> which added cxx=true.
> So yes my patch is actually not needed and can be reverted.
> I tried to look to see if there was a dependency was there but for
> some reason I did not see it.

---
## [ErdinyoBarboza/tgstation](https://github.com/ErdinyoBarboza/tgstation)@[a2fa7799f3...](https://github.com/ErdinyoBarboza/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Saturday 2022-01-29 00:27:33 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [HugoOdaX/fulpstation](https://github.com/HugoOdaX/fulpstation)@[c449fbb56c...](https://github.com/HugoOdaX/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Saturday 2022-01-29 00:28:35 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [eholzbach/dwm](https://github.com/eholzbach/dwm)@[67d76bdc68...](https://github.com/eholzbach/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Saturday 2022-01-29 00:40:24 by Chris Down

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
## [mssx86/apathy](https://github.com/mssx86/apathy)@[d992e6352f...](https://github.com/mssx86/apathy/commit/d992e6352febcf2f421f521272cb56bf766b721e)
#### Saturday 2022-01-29 00:49:22 by mssx86

upd: (recipes/)
> diffutils/; -fno-builtin hack for building with clang.
> gcompat/:
 - strip `-static-pie' from the Makefile, we don't have libunwind.a.
 - don't use mymake(), can't invoke inside root shell.
> libjpeg-turbo/; just don't clean cmake for buildtype shit, too tired to fuck
  with cmakefiles at this point of my life.
> libusb/; -fno-builtin hack for building with clang
> libvpx/; strip lto from c/cxx/ldflags.
> mpc/; remove unnecessary installation steps, thanks, i'm not retarded.
> nfqws/:
 - bump to 9a7d1e8e.
 - strip `--static' from libcap's makefiles, we don't have libunwind.a.
 - don't strip the static libs.
> pciutils/; do not strip when installing.
> rsync/:
 - enable openssl's crypto.
 - add installation steps where rsync-ssl is nuked.
> samurai/; add installation stemps.
> vim/:
 - fix LDFLAG retardation.
 - create the symlink for vim -> vi.
> x264/:
 - strip lto from c/cxx/ldflags.
 - export nasm as AS.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[c742e982b5...](https://github.com/repinger/exynos9611_m21_kernel/commit/c742e982b50c204887c4c4878fbf846131b29b72)
#### Saturday 2022-01-29 02:17:55 by Christian Brauner

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

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[6ed2fafd4e...](https://github.com/Wallemations/heavenstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Saturday 2022-01-29 02:18:32 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [matt-jordan/mud-backend](https://github.com/matt-jordan/mud-backend)@[e0466d117f...](https://github.com/matt-jordan/mud-backend/commit/e0466d117f83054453f7bc3903aee604ba6b8d08)
#### Saturday 2022-01-29 04:44:31 by Matt Jordan

db/models/Character: Add weight

I mean, not to fat shame here, but if you die we need to know
how big your corpse will be.

FOR SCIENCE

---
## [Cpt-Hazama/FNaF-Security-Breach-SNPCs](https://github.com/Cpt-Hazama/FNaF-Security-Breach-SNPCs)@[d0d7bd8334...](https://github.com/Cpt-Hazama/FNaF-Security-Breach-SNPCs/commit/d0d7bd8334775cf27c6ea4c99ff1fa8502b428c9)
#### Saturday 2022-01-29 07:37:11 by Cpt-Hazama

Workshop Update

- Fixed animatronics becoming unstunable during a leap after being stunned
- Added Chica's Scream attack to both her and Freddy (Right-Click)
- Faz-Cam now flashes your screen
- Faz-Cam reload speed is shortened during God Mode
- Fixed soft-lock for Freddy if you die while controlling him
- Added more sounds for Freddy
- Increased the min. distance for Moondrop to activate his rope
- Adjusted Faz-Blaster movement animations
- Fixed Faz-Blaster leaving lights behind after picking up stuff
- Fixed Faz-Blaster skin being different in MP
- Added new weapon; Faz-Watch

---
## [AscendedSion/SEOwnedPublic](https://github.com/AscendedSion/SEOwnedPublic)@[30838dfee5...](https://github.com/AscendedSion/SEOwnedPublic/commit/30838dfee50dd82875c5d3ba3a0d102932930833)
#### Saturday 2022-01-29 08:37:54 by AscendedSion

YEAHHhHhh!!!! I LOVE YOU M-FED YOU DID IT MAN

FUCK YEAH WOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!

---
## [safwan6363/my-files](https://github.com/safwan6363/my-files)@[3229d2ec1a...](https://github.com/safwan6363/my-files/commit/3229d2ec1a7835f245dcfcb6e8d61f760eaad4ae)
#### Saturday 2022-01-29 09:24:06 by safwan6363

Holy. Fucking. Shit. This stupid idea came to reality

---
## [BaconLords/Random-Shit](https://github.com/BaconLords/Random-Shit)@[1daedffa49...](https://github.com/BaconLords/Random-Shit/commit/1daedffa495b660dde5df1bb4a7ccebbbf69e711)
#### Saturday 2022-01-29 09:43:00 by Bacon Lord

Update FLAMINGO ON YOUTUBE FAV FAN YEAH BACONLORD IS SUPER PRO ISH AND EVERYONE ELSE SUCKS BIG MAN NIGGER BALLES LIKE LITTLE KIDS IN BED TOUCHING THERE DICK AND SUCKING ON COCK AND PUTTING IT IN YOUR MOUTH HOLE SO BIG AND JUICIY.lua

---
## [dewwis/introduction-to-Advanced-Python](https://github.com/dewwis/introduction-to-Advanced-Python)@[9cbe277a2e...](https://github.com/dewwis/introduction-to-Advanced-Python/commit/9cbe277a2e0381bf26c90b0d6346a60b63b15a5b)
#### Saturday 2022-01-29 11:55:38 by Dennis Ngugi

Create Django introduction

EMAIL:dellyit001@gmail.com
Order a course at: https://dellyit.com 
Django web development
When developing a Django website you need to be familiar with some basic python as well as graphical user interface basics in python. Python graphical user interface is actually divided into various components for instant: Django, Tkinter, kivy, Jinja2, Flask, pytorch as well as pygame. You should be first start with Tkinter after learning the basics to Python programming.
Here are some few tips I found and they really helped me become an expert in Django as well as advanced python development. They include the following;
1.	Make two hours per day to learn python 
2.	Make sure you can run a basic python code in pycharm, visual studio, command prompt e.t.c
3.	Form a group of two or three members
4.	Make sure you have an aim of the project to have completed at the end of every week.
5.	Post every code you code for yourself without copy pasting from someone else or the code used in tutorials to github.com or your own portfolio (after watching and practicing what you see in a tutorial please have time to sit down and try to practice what you learnt since programming is all about skills you gain at the end of every day)
History of Django
The name Django is a Romani boy's word which means "I awaken." The legendary Belgian-born jazz guitarist Django (formerly Jean Baptiste) Reinhardt's moniker, Django — because D is silent, as virtually everybody now knows — creates a strong melodic choice for any jazz enthusiast.
Introduction to Django
Start by first setting the virtual environment
python -m pip install --user virtualenv

The output is as shown:
Collecting virtualenv
  Downloading virtualenv-20.13.0-py2.py3-none-any.whl (6.5 MB)
     |████████████████████████████████| 6.5 MB 656 kB/s
Requirement already satisfied: six<2,>=1.9.0 in c:\users\denni\appdata\roaming\python\python310\site-packages (from virtualenv) (1.16.0)
Collecting filelock<4,>=3.2
  Downloading filelock-3.4.2-py3-none-any.whl (9.9 kB)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.4.1-py3-none-any.whl (14 kB)
     |████████████████████████████████| 461 kB 1.1 MB/s
Installing collected packages: platformdirs, filelock, distlib, virtualenv
You now need to activate the virtual environment as shown below:
.\env\Scripts\activate
When you get the following output, don’t worry, I got a solution for you.
WARNING: The script virtualenv.exe is installed in 'C:\Users\denni\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed distlib-0.3.4 filelock-3.4.2 platformdirs-2.4.1 virtualenv-20.13.0
WARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\Users\denni\PycharmProjects\first-django\venv\Scripts\python.exe -m pip install --upgrade pip' command.
.\env\Scripts\activate : File C:\Users\denni\PycharmProjects\first-django\env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this       
system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\env\Scripts\activate
 Go to shell and make sure you run it as administrator, then from there you can run the following commands.
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

You can now focus in the installation of all requirements which might be additionally needed in the development of Django websites
py -m pip install requests

This code installs are the required modules in the virtual environment development.
The output is as shown below:
Collecting requests
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     |████████████████████████████████| 149 kB 386 kB/s
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.10-py3-none-any.whl (39 kB)
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 486 kB/s
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.8-py2.py3-none-any.whl (138 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.10 idna-3.3 requests-2.27.1 urllib3-1.26.8

===========CONGRATULATION, NOW YOU ARE SET FOR DJANGO INSTALLATION====
 We are now a few steps towards running our first Django website.
Now you can install Django into your system through the following method:
pip install django

Or even specify the version you need as shown below:
pip install django==4.0

You can now create your first application in Django, call the project name the name which you are best confident with 
django-admin startproject mysite
(mysite is the name of my project.)
You now need to migrate to where the project is, you can do so by navigating through.
cd mysite

 
Run the following command:
python manage.py migrate

These SQL commands are executed in the database file by migrate. As a result, after running migrate, all of your installed apps' tables are created in your database file. You can verify this by installing SQLite browser and opening db.sqlite3. After running the migrate command, all of the tables show in the database file.
You can now run your Django project as follows:
python manage.py runserver

You can now create your own application as follows…
N/B: name your project according to the best name which suits your project. 
python manage.py startapp hello
(hello is my project name, you can call your project any name)
You can now run your project into a server, when you run the project into a server, you should receive such an output into a browser:
 

Make sure you have the following files:
 
These project files are:
1.	The outer _mysite/ root directory is a container for your project. The folder can be renamed.
2.	manage.py: A command-line utility that lets you interact with this Django project in various ways. Do not touch this file.
3.	The inner _mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. _mysite.urls).
4.	_mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package.
5.	_mysite/settings.py: Settings/configuration for this Django project.
6.	_mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
7.	_mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
8.	_mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
The App files
1.	admin.py: Registering your models here for them to be manipulated on the django admin
2.	apps.py: Contains the app configuration code
3.	models.py: Define your models here. These are the tables used for storing data and defining their relations
4.	tests.py: Writing tests for the app
5.	views: Defining data to be rendered on the templates

Frequently Asked Questions:
Can I use Django to make Application?
Django is known for its one-of-a-kind app framework that can be fully managed. An app can be constructed as a completely self-contained module for any feature. This post will show you how to develop a basic app and then add functionality to it.
25 Best Django Project Ideas & Topics for Beginners
 	 Email Sender
 	Text-to-HTML Converter
 	Chat Application
 	A Safe for Passwords
 	Tweets Automator
 	Dictionary Application
 	Notes Application
 	Django Blog
 	Ecommerce Store
 	Video Calling App
 	Social Networking App
 	Interactive Maps
 	Django CMS
 	 News App
 	Photo-centric App (like Pinterest)
 	Login System
 	To-Do App 
 	Weather App
 	Calorie Counter
 	Video Subscription App
 	Online School System
 	Library Management System
 	Railway Enquiry System
 	Quiz App
 	Web Crawler


============Have a blessed day, happy coding=====================
Email me at: dennisngugi115@gmail.com or use company email: dellyit001@gmail.com 
Visit our website: https://dellyit.com

---
## [Midnightinc/2022-GGJ](https://github.com/Midnightinc/2022-GGJ)@[5b0b586300...](https://github.com/Midnightinc/2022-GGJ/commit/5b0b5863007c92c9449a63a8003cd0e8b40f2ca1)
#### Saturday 2022-01-29 12:07:51 by CokeCookies

Stuff

fuck you

Updated art assets in main scene and prefabs

---
## [chxry/solaris](https://github.com/chxry/solaris)@[f23aa6bf0b...](https://github.com/chxry/solaris/commit/f23aa6bf0b6d9204de0db7002a2dcf193914ebed)
#### Saturday 2022-01-29 13:09:35 by Pandaroses

yes shit fart fuck you i hate 404 pages they need to look cute i will probably add something funnier later

---
## [pietraferreira/corev-binutils-gdb](https://github.com/pietraferreira/corev-binutils-gdb)@[08c428aff4...](https://github.com/pietraferreira/corev-binutils-gdb/commit/08c428aff4a793b63c7dd2229ae172879623e3a2)
#### Saturday 2022-01-29 14:10:41 by Nick Alcock

libctf: eliminate dtd_u, part 5: structs / unions

Eliminate the dynamic member storage for structs and unions as we have
for other dynamic types.  This is much like the previous enum
elimination, except that structs and unions are the only types for which
a full-sized ctf_type_t might be needed.  Up to now, this decision has
been made in the individual ctf_add_{struct,union}_sized functions and
duplicated in ctf_add_member_offset.  The vlen machinery lets us
simplify this, always allocating a ctf_lmember_t and setting the
dtd_data's ctt_size to CTF_LSIZE_SENT: we figure out whether this is
really justified and (almost always) repack things down into a
ctf_stype_t at ctf_serialize time.

This allows us to eliminate the dynamic member paths from the iterators and
query functions in ctf-types.c in favour of always using the large-structure
vlen stuff for dynamic types (the diff is ugly but that's just because of the
volume of reindentation this calls for).  This also means the large-structure
vlen stuff gets more heavily tested, which is nice because it was an almost
totally unused code path before now (it only kicked in for structures of size
>4GiB, and how often do you see those?)

The only extra complexity here is ctf_add_type.  Back in the days of the
nondeduplicating linker this was called a ridiculous number of times for
countless identical copies of structures: eschewing the repeated lookups of the
dtd in ctf_add_member_offset and adding the members directly saved an amazing
amount of time.  Now the nondeduplicating linker is gone, this is extreme
overoptimization: we can rip out the direct addition and use ctf_member_next and
ctf_add_member_offset, just like ctf_dedup_emit does.

We augment a ctf_add_type test to try adding a self-referential struct, the only
thing the ctf_add_type part of this change really perturbs.

This completes the elimination of dtd_u.

libctf/ChangeLog
2021-03-18  Nick Alcock  <nick.alcock@oracle.com>

	* ctf-impl.h (ctf_dtdef_t) <dtu_members>: Remove.
	<dtd_u>: Likewise.
	(ctf_dmdef_t): Remove.
	(struct ctf_next) <u.ctn_dmd>: Remove.
	* ctf-create.c (INITIAL_VLEN): New, more-or-less arbitrary initial
	vlen size.
	(ctf_add_enum): Use it.
	(ctf_dtd_delete): Do not free the (removed) dmd; remove string
	refs from the vlen on struct deletion.
	(ctf_add_struct_sized): Populate the vlen: do it by hand if
	promoting forwards.  Always populate the full-size
	lsizehi/lsizelo members.
	(ctf_add_union_sized): Likewise.
	(ctf_add_member_offset): Set up the vlen rather than the dmd.
	Expand it as needed, repointing string refs via
	ctf_str_move_pending. Add the member names as pending strings.
	Always populate the full-size lsizehi/lsizelo members.
	(membadd): Remove, folding back into...
	(ctf_add_type_internal): ... here, adding via an ordinary
	ctf_add_struct_sized and _next iteration rather than doing
	everything by hand.
	* ctf-serialize.c (ctf_copy_smembers): Remove this...
	(ctf_copy_lmembers): ... and this...
	(ctf_emit_type_sect): ... folding into here. Figure out if a
	ctf_stype_t is needed here, not in ctf_add_*_sized.
	(ctf_type_sect_size): Figure out the ctf_stype_t stuff the same
	way here.
	* ctf-types.c (ctf_member_next): Remove the dmd path and always
	use the vlen.  Force large-structure usage for dynamic types.
	(ctf_type_align): Likewise.
	(ctf_member_info): Likewise.
	(ctf_type_rvisit): Likewise.
	* testsuite/libctf-regression/type-add-unnamed-struct-ctf.c: Add a
	self-referential type to this test.
	* testsuite/libctf-regression/type-add-unnamed-struct.c: Adjusted
	accordingly.
	* testsuite/libctf-regression/type-add-unnamed-struct.lk: Likewise.

---
## [ZiyaoWei/OpenNMT-py](https://github.com/ZiyaoWei/OpenNMT-py)@[63142c28ab...](https://github.com/ZiyaoWei/OpenNMT-py/commit/63142c28ab790acdbf8e34802c1b09faaf21a6ca)
#### Saturday 2022-01-29 14:36:18 by Gideon Wenniger

Added missing check for using GPU in train.py in the
build_optim(model, checkpoint) method. This check is nescessary
for the code to run without errors when not using a GPU.

As another side note with this commit: It would actually be nicer
to build the torch optimizer in one go, providing the parameters
and old state all at once to the constructor. Unfortunately,
the torch optimizer.py code simply does not allow that, since
the constructor takes only a list of parameters and does not
provide an option to set the state. Hence, we are forced to use
the "optimizer.load_state_dict(self, state_dict)" method, which is
in my opinion really ugly.
Generally, I think  use of such (non-optional) setters is often
considered an anti-pattern, with setting the state directly in
the constructor being the preferred way to go.
It feels a bit like making an incomplete car, and then calling a
setter to provide the motor. Not so neat.

Also the exact effect of "optimizer.load_state_dict" is quite hard
to grasp,one has to study the code a lot to understand what goes
on exactly,  but essentially comes down to this:
1. It makes a deep copy of the state variables provided in the
dictionary that contains "state" and "param_groups" items.
It uses this copied optimizer state (not model parameters!)
to set the optimizer state with.
2. It effectively retains the "params" entry within "param_groups"
since this contains the model parameters that need to be optimized,
which should not be copied (otherwise optimization has no effect
on the actual model) but can only be provided through the constructor.
3. It updates the rest of the parameters (such as learning rate, etc)
using the provided "state_dict" argument.
As one can see, this is not very intuitive at all, and could be
done a lot cleaner, but alas one has to work with this function as it is.

	modified:   train.py

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[145faef3de...](https://github.com/newstools/2022-daily-post-nigeria/commit/145faef3debe09cb9b28d6dcf84ccc40adb02cf8)
#### Saturday 2022-01-29 15:40:32 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/01/29/teenage-boys-slaughter-girlfriend-burn-her-head-for-money-ritual-in-ogun/]

---
## [ProjectRadiant/packages_apps_Launcher3](https://github.com/ProjectRadiant/packages_apps_Launcher3)@[0046152299...](https://github.com/ProjectRadiant/packages_apps_Launcher3/commit/004615229937280026c9d21ef1496905d15bf0c1)
#### Saturday 2022-01-29 16:00:31 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [techwithanirudh/ytmous](https://github.com/techwithanirudh/ytmous)@[f6b81a9933...](https://github.com/techwithanirudh/ytmous/commit/f6b81a9933c411dd05fc375eccee75947eb8d4ca)
#### Saturday 2022-01-29 16:51:05 by Yonle

Final commit.

After 6 - 10 months of no updates, It's time to deprecate this project. Even though i see somebody open a issue during a day that does not has update, still i respond to them.

I really had no idea of what am i doing after the past 6 months. Seriously, I'M LAZY AS HECK! You see, 3-5 Planned features that were planned since 6 MONTHS AGO IS NEVER IMPLEMENTED FOR THE PAST 6 MONTHS!

Every hours i'm busy and selling some stuff in my shop. Which can also the reason why i can't maintain this repository longer. You can also say that i can't maintain this repo longer due to life issue. I'm busy, tho. Scrolling through Telegram, Twitter, and Mastodon everytime when i'm bored and had no idea of what to do.

Believe me or no, The frontend code (Right in views folder) is mostly a copy paste result in Bootstrap example. Unbelieveable, Isn't it? This project also my random-bored project that i made when i had no idea of what am i doing in some hours.

So yeah. I think this is the end, But not the end. Since the code is open, Somebody may fork it and improve this project with their own.

Thanks for the 36 starts on github. I really appreciate it.

That's it. See you next time, folks.

Bye.

- Yonle <yonle@duck.com>
  Sat, 15 Jan 2022 06:32:25 GMT

---
## [chxry/solaris](https://github.com/chxry/solaris)@[187a02dd07...](https://github.com/chxry/solaris/commit/187a02dd0791f4c30daf288cb4422fb21465e77b)
#### Saturday 2022-01-29 17:37:31 by Pandaroses

fixed lucas retarded names and prices which made no fucking sense fuck you luca if you change names again you are going to never date anyone or be able to jack off again :)

---
## [yo-ru/moe-bot](https://github.com/yo-ru/moe-bot)@[6eb71eeea8...](https://github.com/yo-ru/moe-bot/commit/6eb71eeea8935ed1272f14e1dcddfd3e28401b35)
#### Saturday 2022-01-29 17:46:54 by Yo-ru

the 3 second rule sucks ass when the api just decides to shit it self

---
## [Bored-Entertainment/themesacomplex](https://github.com/Bored-Entertainment/themesacomplex)@[5de5a945ac...](https://github.com/Bored-Entertainment/themesacomplex/commit/5de5a945acbf8020be12110bc2ab6569d1e43f57)
#### Saturday 2022-01-29 18:07:32 by cupofdirtfordinner

Merge pull request #2 from Bored-Entertainment/another-FUCKING-pr

sorry if i break shit, it wasnt intentional

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6696962b94...](https://github.com/mrakgr/The-Spiral-Language/commit/6696962b94642b530d77ceed81bf90dd12724c8f)
#### Saturday 2022-01-29 18:12:05 by Marko Grdinić

"10am. https://www.amplifon.com/uk/audiology-magazine/ear-pain-and-ear-pressure-as-covid-symptoms
> As a rule, earache has no complications and is resolved without great difficulty with the use of analgesics.

It really is painful! Aghhhh!!!

Let me see if we have some painkillers.

10:10am. This is too painful for me to focus on studies. I popped down a paracetamol and until it hits let me just try to keep my mind off things. I had things I wanted to write about, but that has all been blasted away from me.

10:45am. Sigh, though my body is fine, I can't really consider myself cured from this by any stretch. I am going to stretch my work rules in this situation. I'll use up some extra time for sick leave.

I guess things like this happen in life. My right inner ear actually feels worse than yesterday. I feel like I am getting stabbed with a needle every few seconds.

11:10am. Ok, the pain is a tad better now. It is still assaulting me, but it is not so agonizing as when I woke up. I actually slept very well tonight despite it all. Yesterday night, the pain was fairly dull, so I started hoping that I might be able to get rid of it completely by now. That is not to be. I had the same pain killer yesterday, but I had no idea that things getting better was the medicine's effect so I got fooled.

https://mangadex.org/title/a4304d3b-191d-471f-8c78-353d403a35d0/sengoku-komachi-kuroutan-noukou-giga

I've been reading this since I closed for the day yesterday. It is helping me take my mind off things.

12:05pm. My ear is a lot better now. It seems that pills can take an hour or two to take effect. It is too bad I had to skip the morning session, but let me have breakfast, do the chores, and then I will study Houdini.

1:40pm. Done with breakfast and chores. Let me chill just a bit more and then I will start.

2:05pm. Let me start. That painkiller really did wonders for my ear, I am ready to start swinging.

But before I do anything, let me think about what I wanted to do. Yesterday, I decided to stop with the plant tutorial because I'd need to study rigging in order to understand a particular part of it.

2:10pm. Instead of that, for the time being it would be better to study basic SOPs.

2:35pm. I needed to think about it for a bit. Instead of studying rigging itself, let me just look up the specific nodes that I need. I do not want to just quit the plant tutorial because it has been teaching me a lot. There is no need to complicate things - I can just pick up Houdini node by node. Let me first attempt it.

2:40pm. https://youtu.be/GxKfKvYu7VU?t=1209

Let me check out out the skeleton node. I got discouraged far too quickly yesterday.

It does not come with any examples, but it seems it allows drawing of the skeleton directly.

2:55pm. Hmmm, ok. I see that the skeleton node allows yout to draw bones. It is aptly named.

https://youtu.be/9f06tjunxUs
A First Look At KineFX

Let me watch this since it is only 13m.

3:20pm. https://youtu.be/9f06tjunxUs?t=675

Ok, enough. I do not understand a thing of this.

3:25pm. But I do get the gist of it. Let me figure out the rig attribute node. Let me go back to the plant tut so I can see what he is doing.

3:30pm. I get what stash input is doing. It seems it is possible to convert a mesh to a skeleton using that. I had to check this out. I do not understand what the other two options are for, but it does not matter.

Actually, for the last one I can guess.

...I guessed wrong. It wasn't what I thought it would be.

Nevermind, let me just continue moving.

Focus me. Let me take a look at the plant tutorial.

https://youtu.be/GxKfKvYu7VU?t=1366

Where is that xform coming from?

4pm. https://youtu.be/GxKfKvYu7VU?t=1679

I feel like I am getting this. I guess I was just too tired yesterday. I lost track at the skeleton node, but what he is doing here makes sense. i still do not understand why the rig node is necessary copared to a regular one, but I'll just go with it for now.

https://youtu.be/GxKfKvYu7VU?t=1757

This is a really good way of doing it. I kneel.

Maybe he could have avoided defining the normals where he did though.

4:10pm. https://youtu.be/GxKfKvYu7VU?t=1998

How about I watch this completely since I've lost track of the pacing and come back to it where I originally left off?

https://youtu.be/GxKfKvYu7VU?t=2081

Couldn't he have used a transform node instead here?

Ah, no wait, tranform would have only worked relative to the pivot. The things being rotated here are normals. So yes, he did need to either do it like this, or use some node that I don't know about.

4:15pm. Let me pause here. I need to do chores again.

4:40pm. Let me resume. I want to just watch this. It is fine if I can understand what the individual steps are doing for now even if I do not walk myself through it right away.

https://youtu.be/GxKfKvYu7VU?t=2690

This is a such a horrible hack. He should not have done it like this. He should have separated the leaf generation functionality into a function and passed in the iteration number as an argument.

5pm. I had enough of this video. Just forget it. Who knows what kind of bad habits am I going to pick up if I follow it step by step.

5:05pm. No, let me finish it. Maybe being sick has given me a short fuse. I am being egoistic in the wrong place. Right now, I do not have any plans for what to do next, so I might as well watch the last 20m. I actually have little will to continue after that. I'll have to think about what to do after I finish watching the plant tutorial.

https://youtu.be/GxKfKvYu7VU?t=2976

I am not really following this since I do not trust the author to do an efficient thing anymore, but let me see if I can gleam some more insight fromt this.

5:35pm. https://youtu.be/GxKfKvYu7VU?t=3649

This is probably the most complex way to make a simple plant that I could think of. I am starting to get how programs get away in complexity for regular people.

5:45pm. Houdini...it major con is that it is COMBINATORIAL EXPLOSION - THE LANGUAGE. Whereas well designed languages have a small number of primitives that can be combined to create a large variety of things, Houdini has a very large amount of primitivies, which have a large number of parameters which can be used to create anything.

Enough of random wandering. I've satisfied my curiosity on how to do the plant.

5:50pm. Let me take a look at how Simon did those bridge planks.

https://youtu.be/hjYYh8cr3dg
Model a bridge in Houdini || Beginner Tutorial

Let me revisit this. I know how to do the usual cross section, but how did that curved plank come about?

https://youtu.be/hjYYh8cr3dg?t=88

Ah, so it was like that. I simply forgot how this came about, or rather, my memory became corrupted.

6:15pm. Right now I am just standing around in a daze, lurking /a/. I should be doing something instead.

I've looked at Simon's vids, but nothing really catches my interest.

Right now, I am not really at 100% mental readiness.

6:40pm. Done with lunch. Right now I am taking a tour of the manual. Amongst the geometry nodes, I see that there is a leaf generator.

6:55pm. The amount of these nodes is ridiculous. My learning curve with Blender was because I was completely new to art, but this is just awe inspiring. Considering I just want to get through it, I am not happy at all to have such a powerful tool.

https://www.sidefx.com/learn/collections/geometry-tools/
https://www.sidefx.com/learn/world-building/

I really don't feel like watching videos.

Ok, let me do it like this.

I am going to go over all the examples for the stuff in the shelves that I think is primitive. As well as the stuff in the radial menus. After that I'll just get started on my own things. if I can't get Houdini to take off with me, I'll just go back to Blender. But until then, I should try putting in an honest effort.

7:05pm. Right now, let me have some fun. I can spare some downtime during times like these.

Tomorrow, I am going to start systematically going through the examples. Let nobody say that I am to lazy to do this."

---
## [BitcoinnewsSeven/https-bitcoinnews.com-seven](https://github.com/BitcoinnewsSeven/https-bitcoinnews.com-seven)@[459a4aed38...](https://github.com/BitcoinnewsSeven/https-bitcoinnews.com-seven/commit/459a4aed383ff25b4ed1d5cb6189849c873780a0)
#### Saturday 2022-01-29 18:13:07 by BITCOINNEWS SEVEN

checkoutbitcoin.mc


[v5.9-beta.3]  #1 checkoutbitcoin.md waved-credit.limit. Shares.array-price.calculator sha1-beta.3-Bitcoin/CashScript true-beacon.array-currency-value Dictionary-Calculator. (c) 2022.
Contact info 
sponsors.blockchain@gmail.com
Community name
Bitcoinnews Seven
Governing body
Bank
Citizen Code of Conduct
1. Purpose
A primary goal of Bitcoinnews Seven is to be inclusive to the largest number of contributors, with the most varied and diverse backgrounds possible. As such, we are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual orientation, ability, ethnicity, socioeconomic status, and religion (or lack thereof).

This code of conduct outlines our expectations for all those who participate in our community, as well as the consequences for unacceptable behavior.

We invite all those who participate in Bitcoinnews Seven to help us create safe and positive experiences for everyone.

2. Open [Source/Culture/Tech] Citizenship
A supplemental goal of this Code of Conduct is to increase open [source/culture/tech] citizenship by encouraging participants to recognize and strengthen the relationships between our actions and their effects on our community.

Communities mirror the societies in which they exist and positive action is essential to counteract the many forms of inequality and abuses of power that exist in society.

If you see someone who is making an extra effort to ensure our community is welcoming, friendly, and encourages all participants to contribute to the fullest extent, we want to know.

3. Expected Behavior
The following behaviors are expected and requested of all community members:

Participate in an authentic and active way. In doing so, you contribute to the health and longevity of this community.
Exercise consideration and respect in your speech and actions.
Attempt collaboration before conflict.
Refrain from demeaning, discriminatory, or harassing behavior and speech.
Be mindful of your surroundings and of your fellow participants. Alert community leaders if you notice a dangerous situation, someone in distress, or violations of this Code of Conduct, even if they seem inconsequential.
Remember that community event venues may be shared with members of the public; please be respectful to all patrons of these locations.
4. Unacceptable Behavior
The following behaviors are considered harassment and are unacceptable within our community:

Violence, threats of violence or violent language directed against another person.
Sexist, racist, homophobic, transphobic, ableist or otherwise discriminatory jokes and language.
Posting or displaying sexually explicit or violent material.
Posting or threatening to post other people's personally identifying information ("doxing").
Personal insults, particularly those related to gender, sexual orientation, race, religion, or disability.
Inappropriate photography or recording.
Inappropriate physical contact. You should have someone's consent before touching them.
Unwelcome sexual attention. This includes, sexualized comments or jokes; inappropriate touching, groping, and unwelcomed sexual advances.
Deliberate intimidation, stalking or following (online or in person).
Advocating for, or encouraging, any of the above behavior.
Sustained disruption of community events, including talks and presentations.
5. Weapons Policy
No weapons will be allowed at Bitcoinnews Seven events, community spaces, or in other spaces covered by the scope of this Code of Conduct. Weapons include but are not limited to guns, explosives (including fireworks), and large knives such as those used for hunting or display, as well as any other item used for the purpose of causing injury or harm to others. Anyone seen in possession of one of these items will be asked to leave immediately, and will only be allowed to return without the weapon. Community members are further expected to comply with all state and local laws on this matter.

6. Consequences of Unacceptable Behavior
Unacceptable behavior from any community member, including sponsors and those with decision-making authority, will not be tolerated.

Anyone asked to stop unacceptable behavior is expected to comply immediately.

If a community member engages in unacceptable behavior, the community organizers may take any action they deem appropriate, up to and including a temporary ban or permanent expulsion from the community without warning (and without refund in the case of a paid event).

7. Reporting Guidelines
If you are subject to or witness unacceptable behavior, or have any other concerns, please notify a community organizer as soon as possible. sponsors.blockchain@gmail.com.

https://bitcoinnews.com

Additionally, community organizers are available to help community members engage with local law enforcement or to otherwise help those experiencing unacceptable behavior feel safe. In the context of in-person events, organizers will also provide escorts as desired by the person experiencing distress.

8. Addressing Grievances
If you feel you have been falsely or unfairly accused of violating this Code of Conduct, you should notify Bank with a concise description of your grievance. Your grievance will be handled in accordance with our existing governing policies. CODE_OF_CONDUCT

[v5.9-beta.3] #1 checkoutbitcoin.md waved-credit.limit. Shares.array-price.calculator sha1-beta.3-Bitcoin/CashScript true-beacon.array-currency-value Dictionary-Calculator. (c) 2022.

9. Scope
We expect all community participants (contributors, paid or otherwise; sponsors; and other guests) to abide by this Code of Conduct in all community venues--online and in-person--as well as in all one-on-one communications pertaining to community business.

This code of conduct and its related procedures also applies to unacceptable behavior occurring outside the scope of community activities when such behavior has the potential to adversely affect the safety and well-being of community members.

10. Contact info
sponsors.blockchain@gmail.com

11. License and attribution
The Citizen Code of Conduct is distributed by Stumptown Syndicate under a Creative Commons Attribution-ShareAlike license.

Portions of text derived from the Django Code of Conduct and the Geek Feminism Anti-Harassment Policy.

---
## [bhalash/dotfiles](https://github.com/bhalash/dotfiles)@[37f54c607b...](https://github.com/bhalash/dotfiles/commit/37f54c607b2390216b587bc1ad8c4270f4cc7c48)
#### Saturday 2022-01-29 18:51:22 by Mark Grealish

alacritty: change startup mode

TBH here, I don't like it maximized, and native fullscreen on macOS is a
fucking painful piece of shit.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1dfcffccd1...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1dfcffccd1d453fc0d3f928f5dfa1d3115f977f9)
#### Saturday 2022-01-29 19:21:02 by Zenitheevee

Tarkon Update 1.5: Meet the Ensign  (#11089)

* THE LORE, GUYS, THE LORE

* P-T 1.5: Meet The Ensign

* Dont remember, live is fucky and i need to test shit

* So many active turfs now fixed...

* Medical Malpractice: Swapped patients thumbs with their big toes.

* THE SOOOUUUULLLLLLLNGNGHHGHGHHH

* ok maybe i want this back.

* some other stuff and future-proof testing

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[33bf0b86e0...](https://github.com/mawrick26/SM8250/commit/33bf0b86e05ad791ae2d60a8585e5f0898c9c198)
#### Saturday 2022-01-29 20:13:15 by George Spelvin

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
## [Hinaichigo/vgstation13-1](https://github.com/Hinaichigo/vgstation13-1)@[b879dddba0...](https://github.com/Hinaichigo/vgstation13-1/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Saturday 2022-01-29 20:28:34 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [akkartik/teliva](https://github.com/akkartik/teliva)@[7a13adb52c...](https://github.com/akkartik/teliva/commit/7a13adb52c4964b91cf008c39f2e90ff5d9ec513)
#### Saturday 2022-01-29 20:43:11 by Kartik K. Agaram

try to get by with one feature macro

I fucking hate feature macros. Egregious discharge of our
division-of-labor-obsessed society. People should be able to introduce
names. People should be able to give up names to lower levels of
abstraction when they encounter conflicts.

Feature macros seem to exist[1] to support more than two levels of
abstraction. You try to build, one of your libraries fails to build
because of a conflict between it and one level down. You don't want to
modify this library. Just fucking https://catern.com/change_code.html
already. But no, I have to litter my code with feature macros even
though I just want the abstraction the original library provides.

[1] https://man7.org/linux/man-pages/man7/feature_test_macros.7.html
    https://lwn.net/Articles/590381

---
## [Neternels/android_kernel_xiaomi_mojito](https://github.com/Neternels/android_kernel_xiaomi_mojito)@[428f15c532...](https://github.com/Neternels/android_kernel_xiaomi_mojito/commit/428f15c53216ce06d84bf7451e1f113cd9ea5801)
#### Saturday 2022-01-29 20:49:19 by Wang Han

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

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[cdb3374572...](https://github.com/i3roly/glibc_ddwrt/commit/cdb3374572230fd22a15eefa4ee6ff94a086f442)
#### Saturday 2022-01-29 21:07:32 by gagan sidhu

4.14.263/48240. small(+hwnat) fixes&&changes. "autotune is a right, not a privilege" -randy marsh

- in padavan they have this thing called double vlan tag, which
  required a minor modification of some code in the sysctl and
  8021q folders of linuxdir/net. i've enabled this flag since
  dual vlans are enabled in RAETH and it is probably helpful
  for people who are really into switch configurations

- i have also changed the temperature display code slightly,
  using IOCTL as opposed to the stupid way i was doing it before.
  while you probably won't notice, i think the change is worth mentioning.

- i missed a few lines of code in the MWDS port that are probably very
  important (lol), which are responsible for enabling/checking the flags
  when it initialises, that are now present.

- also hw_nat wasn't using the "new_arch" flag the way it was supposed to,
  in spite of being enabled in kernel configuration. this has also been fixed.

- added a max of 10 WDS interfaces since that was what i had for some
  time, and for some reason i guess one of the patches when i updated
  mt_wifi didn't migrate this change.

aside from that, nothing to report on the marsh front. maybe forever, but
.you.
.already.
.know.
what you say to that, dear 'skins fans....

TESTED AND WORKING

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---
## [ComunidadAylas/PackSquash](https://github.com/ComunidadAylas/PackSquash)@[99df59972e...](https://github.com/ComunidadAylas/PackSquash/commit/99df59972efc9741475539f478dd67dd88771877)
#### Saturday 2022-01-29 21:13:38 by AlexTMjugador

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
## [sadsharma/School-Lunch-Line-Simulator](https://github.com/sadsharma/School-Lunch-Line-Simulator)@[d94e63a116...](https://github.com/sadsharma/School-Lunch-Line-Simulator/commit/d94e63a11603759374835dd73ab18145850df25c)
#### Saturday 2022-01-29 21:44:01 by sadsharma

Update README.md

You have just been hired as part of a team of elite developers to work on the next video game craze: Middle School Simulator. It will be your job to simulate the lunch line of Rocky Stream Middle School. Rocky Stream middle school is a weird place, with some weird constraints. First of all, the lunch line can only hold up to 20 people at once, and any overflowing people will find themselves loitering in the hallway without a hall pass and be immediately sent to detention, by the Dean, Mr. Mean. Just like a normal lunch line, students who arrive usually go to the back of the line. However, if a student sees a friend on the lunch line, they may choose to cut in front of the friend, so you must allow for this. Furthermore, students may choose to switch places on line (usually, a spot will be traded if the student moving forward promises the student moving backward their soggy fries). A student will be removed from the front of the line once he/she has been served a selection of non-descript wobbly brown substances by the lunch lady, Mystery Meat Martha. There is also a resident bully, Punchin' Patrick, who may walk up to any student and steal their lunch money. Students may also drop lunch money accidentally or pick some up off of the floor,  so you must be able to update a student's lunch money balance. Once a student has no lunch money, they will leave the line. Additionally, as your target demographic will be indecisive tweens that might want to come up with realities in their middle school game, you will make the option to switch between two different realities (each with its own separate lunch line), and copy a reality to the other (to have a starting point where two scenarios can be made) (array copy), in case your game players decide they don't like the way they have manipulated the story thus far. You will write a program that simulates this lunch line from the command line.

---
## [sLiMyFETUS69/Sieve-of-Eratothenes](https://github.com/sLiMyFETUS69/Sieve-of-Eratothenes)@[97ed75f12a...](https://github.com/sLiMyFETUS69/Sieve-of-Eratothenes/commit/97ed75f12a56b9d6c95e8b2486fa565482c285ab)
#### Saturday 2022-01-29 22:21:49 by sLiMyFETUS69

Wrote some bullshit... raged at the end

Fuck you, I'm not adding an "optional description"

---
## [Clownacy/clownmdemu](https://github.com/Clownacy/clownmdemu)@[6b0b624d6c...](https://github.com/Clownacy/clownmdemu/commit/6b0b624d6c69b326d3d67522266896655335ce5f)
#### Saturday 2022-01-29 23:42:13 by Clownacy

Frontend: Fix PSG Status debug window not...

...having a close button.

Also holy hell I bloody hate the 50-character title limit.

---

