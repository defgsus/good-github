## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-15](docs/good-messages/2022/2022-10-15.md)


1,904,056 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,904,056 were push events containing 2,603,482 commit messages that amount to 158,960,022 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[e9d4bf6c49...](https://github.com/Zergspower/Skyrat-tg/commit/e9d4bf6c4920f07f03c2425ac3e69caf8daced9d)
#### Saturday 2022-10-15 00:00:30 by Zergspower

Granite's Love pass 1 of X for ruins  (#16746)

* Fab Five

* forgot to move the rack in front of the false wall

* Holy shit scrapheap looked HORRIBLE

---
## [log1cs/kernel_nokia_msm8998](https://github.com/log1cs/kernel_nokia_msm8998)@[edf64987de...](https://github.com/log1cs/kernel_nokia_msm8998/commit/edf64987de90de9fbe3cf30344232b3455503a14)
#### Saturday 2022-10-15 00:10:44 by Christian Brauner

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
## [JourneyOver/selfhosted_templates](https://github.com/JourneyOver/selfhosted_templates)@[cb24ac60da...](https://github.com/JourneyOver/selfhosted_templates/commit/cb24ac60da26bbde5f6d154259817ebdd4c3e2d6)
#### Saturday 2022-10-15 01:08:17 by Journey

Fuck it..

fuck the logs who the fuck needs them anyways, this shit is so stupid...

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b5ad632987...](https://github.com/treckstar/yolo-octo-hipster/commit/b5ad632987606903de8718544f4cf17a75f81681)
#### Saturday 2022-10-15 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [linuxias/glib](https://github.com/linuxias/glib)@[b8e1ecdd6b...](https://github.com/linuxias/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Saturday 2022-10-15 02:34:26 by Michael Catanzaro

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
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[32c2e4ccd3...](https://github.com/Mothblocks/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Saturday 2022-10-15 03:08:24 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [AirSkyBoat/AirSkyBoat](https://github.com/AirSkyBoat/AirSkyBoat)@[40e1c4a7d7...](https://github.com/AirSkyBoat/AirSkyBoat/commit/40e1c4a7d7f07de631b3a074c0976270428ba690)
#### Saturday 2022-10-15 05:10:30 by dallano

Better the Demon You Know Quest Implementation

Implements the quest: "Better the Demon You Know"
NM Behaviors:
- Andrealphus uses blood weapon every 3 minutes
- Andrealphus escapes the target with hate out of the zone at 75% and 25% HP

---
## [MemeHoovy/PE-tutorials](https://github.com/MemeHoovy/PE-tutorials)@[30c23187d5...](https://github.com/MemeHoovy/PE-tutorials/commit/30c23187d5034a5ce1d414371915e177c522f0bb)
#### Saturday 2022-10-15 05:38:28 by Not_HaydenGaming

CUSTOM CUM TRANSITION REAL 100%

alright for real, I got that done in 30 minutes, cuz fuck you vs dave revenge 3.5

---
## [MemeHoovy/PE-tutorials](https://github.com/MemeHoovy/PE-tutorials)@[00b3076dcb...](https://github.com/MemeHoovy/PE-tutorials/commit/00b3076dcbe509ec4b399e529af6d4f5d0085d65)
#### Saturday 2022-10-15 05:38:28 by Not_HaydenGaming

final asset shit before I dump all of my part's.

Fuck EIT.

Fuck the PE tutorial's.

Never knew he would backstab me.

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[0005e94e62...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/0005e94e625d8d7aef59e88490ffda1137db9aa1)
#### Saturday 2022-10-15 06:15:53 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[f923f61011...](https://github.com/Jackraxxus/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Saturday 2022-10-15 07:06:02 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[fc7c186957...](https://github.com/AnywayFarus/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Saturday 2022-10-15 07:29:59 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [codekane/ryanhorricksv2](https://github.com/codekane/ryanhorricksv2)@[d8105e2da9...](https://github.com/codekane/ryanhorricksv2/commit/d8105e2da969b45a2eabba29486ba3155d4e662c)
#### Saturday 2022-10-15 08:44:03 by Ryan Horricks

JESUS FUCKING CHRIAST. I am getting so many CSS issues in this project... That's what I get for writing all of my own. This shouldl be safe to push, even if I don't like it, but I'm... Super not happy with the state of things. Fix one problem, create a bajillion more. Oh my god. OH MY GOD. This push, this is after I reverted the SUPER FUCKED commit with a ton ofo lines of code that eventaully fixed the errors, only to produce something I didn't actually like... DESIGN TIME. Yes. Design time. Well. I have lots of inspiration now, looking at all of these things that I've done. This push, though, it fixes a bug. And that's something.

---
## [codekane/ryanhorricksv2](https://github.com/codekane/ryanhorricksv2)@[dfdd48e62b...](https://github.com/codekane/ryanhorricksv2/commit/dfdd48e62b9036386f35d37190f10f83a5459cc8)
#### Saturday 2022-10-15 08:44:03 by Ryan Horricks

AFTER ALL THAT FUCKING WORK. I HATE IT. I SWEAR TO GOD.

---
## [samcday/home-cluster](https://github.com/samcday/home-cluster)@[f66811c2eb...](https://github.com/samcday/home-cluster/commit/f66811c2ebb6ebed309d42206c5fb496414fe52f)
#### Saturday 2022-10-15 08:46:39 by Sam Day

shit did I just fuck up ownership apostrophe? I can never remember the rule :(

---
## [Salex08/HippieMerchant-13](https://github.com/Salex08/HippieMerchant-13)@[323c9d6bb7...](https://github.com/Salex08/HippieMerchant-13/commit/323c9d6bb75c20e11d744dbe55850287ede8c5cc)
#### Saturday 2022-10-15 09:38:28 by karmaisblackandbluepilled

bye bye is_ganymede back to the lobby

drip drip from the tap

BYE BYE NANOSUIT BACK TO THE LOBBY

remember when they tried to kill the lich king with a fucking sword made out of tortured souls lmao

honestly

liberia

---
## [JereKoskela/msprime](https://github.com/JereKoskela/msprime)@[cbc45c6ac6...](https://github.com/JereKoskela/msprime/commit/cbc45c6ac60d5e2c6517d740b5e31bb6b308609a)
#### Saturday 2022-10-15 09:57:45 by andrewkern

scaling now checks out!

passing verifications now

added histograms to verification

comparison to slim looks good. need to keep testing for different param values

holy shit it all works

working on docs

tau-- time since a sweep ocurred, now checks out

had to add untracked file?

added comments to time scaling code in verification.py

adding a bunch of documentation

auto lint

auto lint part 2

warning levels got my c code

test cases now failing due to nonsensical params

fixing up unit tests now

fixing up unit tests now

trying to fix doc notebook import to use matplotlib

still issues in old unit tests

incorporating Jerome's comments

found a damn typo

made the switch from alpha to s

straggling tests with the switch to s

still turning up weird tests...

more testing snafus with change to s

changed this weird msms mimic test-- i think we can dump it?

jerome edits on doc

---
## [rhatdan/buildah](https://github.com/rhatdan/buildah)@[2adbe2a58a...](https://github.com/rhatdan/buildah/commit/2adbe2a58a77b014be59c68abf58b682ad5e5c20)
#### Saturday 2022-10-15 09:59:39 by Ed Santiago

System test cleanup: document, clarify, fix

Primary purpose: fix "preconfigured TARGETARCH/etc" test so
it will work under podman and on multiarch.

Root cause of it not working: I mistakenly advised @flouthoc,
in #4310, to write a containerfile in $TEST_SCRATCH_DIR. I
thought it was an empty directory. Big, big mistake. (Sorry,
Aditya). Document this near the variable definition, and
fix the test once again.

@nalind pointed out that the containerfile doesn't need to
be generated on-the-fly, so, use a static one. In the spirit
of DIE, read the TARGETxxx vars from it. Not that we're
expecting more variables, but, it's just cleaner.

Also, as long as I'm here: in run_buildah, when logging the
command being run, use #/$ prompt for root/rootless. I was
getting too confused looking at logs of root runs.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[e37f8f83c6...](https://github.com/TaleStation/TaleStation/commit/e37f8f83c62857eca440b3ac115a9df61b4969ad)
#### Saturday 2022-10-15 10:22:35 by TaleStationBot

[MIRROR] [MDB IGNORE] Upgrades the Modsuit Adapter Shell (#2721)

* Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

* Upgrades the Modsuit Adapter Shell

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [larentoun/tgstation](https://github.com/larentoun/tgstation)@[14c96d05b8...](https://github.com/larentoun/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Saturday 2022-10-15 10:56:39 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [ZhenjaMax/BetterBalancedGame](https://github.com/ZhenjaMax/BetterBalancedGame)@[0f7828b31a...](https://github.com/ZhenjaMax/BetterBalancedGame/commit/0f7828b31a73ec83006ddd119dede2418539e9ba)
#### Saturday 2022-10-15 11:34:27 by ZhenjaMax

English update (#49)

* English lang 5.1

New lines for 5.1 patch:
Ottoman UU (naval) - can enter Ocean tiles regardless of researched Technologies;
Ottoman Ibrahim unique governor R2 promotion - +1 movement within 10 tiles of city instead of useless griveances ability;

- Goddess of the Hunt pantheon - +2 gold instead of +1 food;

- Railroad - cost increased to 2 iron & 1 coal per tile;
- Intelligence Agency - +50% production to Spies, +2 capacity (instead of +1).
- Statue of Zeus World Wonder - +35% instead of +50% to anti-cavalry;

- Agoge policy - recon (Classical and earlier);
- Feudal Contract policy - recon (Renaissance and earlier);
- Grande Armee policy - recon (Industrial and earlier);
- Military First policy - recon (all);

Edited lines for 5.1 patch:
Eleanor leader ability - works grant +1 instead of +2;
Ethiopia UU - +1 movement if starts in Hills instead of ignoring them;

Deleted lines for 5.1 patch:
Ethiopia UI - reverted to base-game (faith from adjacent mountains);
Rome UD - reverted to base-game (no culture per adjacent districts);

New other lines:
- Base ranged naval units - Range of these units (1, 2, 3, 4);
- Warrior Monk R2 Promotion - 250 Religious pressure within 6 tiles clarification;
- Victor T3 promotion - anti-air icon;
- Pingala L1 promotion - clarification what affect +100% GPP;
- Orszaghaz World Wonder (English fix) - clarification of Diplomatic favor, +1 is equal +100%;

Medina quarter policy - district icon;
Liberalism policy - district icon;
New deal policy - district icon;
Serfdom policy - charge icon;
Public Works policy - charge icon;
Logistics policy - movement icon;
Integrated Attack Logistics policy - movement icon;
Public Transport (English fix) - yields clarification;
Gothic Architecture policy (English fix) - toward Renaissance and earlier;
Wisselbanken policy (English fix) - +0.25 points (not .25), re-wrote sentence;
Machiavellianism policy - turn icon;
Containment policy - government icon;
Hallyu policy - promotion icon;
Non-stated Actors policy - promotion icon;
Press Gangs policy (English fix) - forgotten "+" character.

Edited other lines:
- Australia leader ability - turn icon;
- France civilization ability (English fix) - moved number and tourism icon near each other;
- Macedon leader ability - turn icon;
- Ottoman UB - first constructed UB grants free Governor Title; it is old artifact from v4 that nobody wrote before;
- Scotland UI - grants +1 appeal to adjacent tiles; edited sentence;
- Spain UI - 8 tiles from current capital; added Science icon;

- Divine Spark pantheon - Great People icons;
- City Patron pantheon - district icons;
- God of War and Plunder pantheon - Great People icons;

- Warlord Throne - production for all cities;
- Foreign Ministry (English fix) - moved items between sentences;

- Trench Warfare policy - for "all" (forgotten word);
- Insulae policy - district icon;

* 5.1 English following new commits

New lines for 5.1 patch:
- Kotoku-in world wonder - allows purchasing Monk in this city (with wonder);
- World Religion congress resolution - +10 strength for religious units only (no Monks).
>
Edited lines for 5.1 patch:
- Sumerian leader ability - start game with War-cart instead of Warrior unit;
- Goddess of the Hunt - food instead of production;
- Railroad - 2 iron & 0 coal.
>
New other lines:
- Cree UU - promotion icon.
>
Edited other lines:
- Rome leader ability - simpify description, just grants Monument building; reason - other cases are giga rare and useless because no one rush Monument for first 8 turns in my opinion; if you don't agree we can discuss it in channel and then change to something else;
- Spain civilization ability - Corps and Army icons for Fleets and Armadas;
- Spain UI - forgotten "current" word for XP2;
- Pingala L1 (English fix) - lower case;
- Grand Master Chapel - can purchase in founded cities, not just owned.

---
## [kavishinsa/Prestige-Suncrest-Bengaluru](https://github.com/kavishinsa/Prestige-Suncrest-Bengaluru)@[105c6cb34e...](https://github.com/kavishinsa/Prestige-Suncrest-Bengaluru/commit/105c6cb34ef9f44f7787edfae10ff38433c66f1c)
#### Saturday 2022-10-15 12:17:53 by kavishinsa

Create Prestige Suncrest Sanjayanagara Bengaluru

Bengaluru, India's IT center, is always experiencing an IT boom. As a result, Prestige Suncrest many flew to Bangalore in search of their perfect home and a satisfying career. With this influx, the demand for housing soared, as did the real estate price. Since its inception in the city, real estate has shown steady growth. Many people obtain properties in Bangalore both to live in and as long-term speculation. Because of the increasing demand for real estate, there are several residential condominiums available for sale in Bengaluru.

Statistics from recent years show that, because of the variety of jobs available there, Bangalore has emerged as one of the top attractions for young people. Hence, numerous people dream of having a home amidst a lush natural atmosphere. These dreams are being fulfilled by Prestige Constructions at Sanjayanagara, Devanahalli, Bangalore.

Prestige Suncrest Bangalore is a lovely neighborhood covering many acres of land area. Take advantage of the special offers and be among the first to recognize them. For its lifestyle project, it has proven to be of a high standard. The developer has informed us that they will take care of all our needs, including luxury, comfort, position, and security above all different.

Prestige Suncrest Apartments is a green haven tucked away in Devanahalli, a position where clear skies, clean oceans, and untouched environments meet you. One would be pleased to reside in the neighborhood of 1, 2, and 3 BHK apartments here. It provides a wave of tranquility to assist one escape the clamor and bustle of the city. The overall view from this development it gives a stunning panorama of nature over a huge stretch of greenery, owing to the overabundance of trees that have been farmed around the possessions.

Prestige takes pleasure in offering its residents a state-of-the-art gym, various sports facilities like tennis & basketball court, sand pits for children, and even a jogging/cycling track, etc.

For More Details:
Visit Here: https://bit.ly/3T6ukZ5

---
## [asyncvlsi/Xyce](https://github.com/asyncvlsi/Xyce)@[faf2ef48dd...](https://github.com/asyncvlsi/Xyce/commit/faf2ef48dd2226203bc94222bbc7bbdb3c1d73dd)
#### Saturday 2022-10-15 12:53:08 by Tom Russo

Remove an ancient, windows-specific kludge from BSIM4

Years ago, we were defining an M_PI macro as "2.0*atan(1)" if a system
header did not define it for us.  This was bad, because it was not
properly set up with parentheses --- which was awful if one *divided*
by M_PI   1/M_PI would become 1/2*atan(1) (or 0.25*pi) instead of
1/(2*atan(1)) (1/pi).  This error was present in the code from the
beginning commit 13969fa4 in 2000.

This went on for years leading to a superstition that something was
wrong specifically on windows (the only system that didn't have M_PI
defined in system headers), and a habit of doing funny things whenever
M_PI was used in the code (like saving it into a variable before doing
things with it, or putting extraneous parens into expressions).  The
BSIM4 has just such an expression and a big block of comments
explaining it.

In commit b57a07a in 2013 this bug was finally detected and fixed, but
we did not go back and undo all the goofy, superstitious hacks that
had been put into the code in an attempt to stave off the problems it
caused.

Since I'm working in the BSIM4 today, I am removing them now.

Note that the use of a function call and multiplication to get M_PI if
it is undefined was done away with altogether in commit 3b253df just
last month, and now it's a straight floating point constant.

Tangientially related to Xyce/backlog/project-backlog#419

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[b4b6636b49...](https://github.com/ianjoneill/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Saturday 2022-10-15 13:08:22 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [ShadowOpsCross/ThatsIT](https://github.com/ShadowOpsCross/ThatsIT)@[685ba9064f...](https://github.com/ShadowOpsCross/ThatsIT/commit/685ba9064f44b7d2b25eec243b237d27cfd0a3f7)
#### Saturday 2022-10-15 13:35:36 by Arsenii

Merge pull request #2 from ShadowOpsCross/workflows

Fuck you 1

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[eba3f0c924...](https://github.com/newstools/2022-new-york-post/commit/eba3f0c924748365b5a49ddf5b1d0d0c790068a2)
#### Saturday 2022-10-15 13:49:52 by Billy Einkamerer

Created Text For URL [nypost.com/2022/10/14/dear-abby-my-new-boyfriend-is-still-in-love-with-his-dead-wife/]

---
## [chasonr/NetHack](https://github.com/chasonr/NetHack)@[b02e018225...](https://github.com/chasonr/NetHack/commit/b02e01822564e5bee3c31082e978419edea6a37c)
#### Saturday 2022-10-15 14:07:18 by Michael Meyer

Remove explicit 'none' opt from autounlock handler

The autounlock handler included an explicit 'none' option, a choice that
gave it a different UX from similar existing compound option handlers
(e.g. paranoid_confirm or pickup_types), which set 'none' simply by
deselecting all options.  It didn't make the menu any easier to use (at
least in my experience), since in order to go from some combination of
options to 'none', you'd have to deselect everything anyway (which on
its own was enough to set 'none', so there was no reason to explicitly
select it after doing so).

Make the autounlock handler work like other compound option handlers,
such that deselecting all options is the way to set 'none', and there is
no explicit 'none' option included in the list.

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[9ccd6ecd74...](https://github.com/PKRoma/Terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-10-15 14:23:42 by Mike Griese

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
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[442432ea15...](https://github.com/PKRoma/Terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Saturday 2022-10-15 14:26:15 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[ada2fe87ec...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/ada2fe87ec01dcc2bffc1439d78eebcdd44650a9)
#### Saturday 2022-10-15 14:39:35 by Dave Chiluk

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [QuantumApprentice/Fallout-Nevada-Translation](https://github.com/QuantumApprentice/Fallout-Nevada-Translation)@[8bf64b1747...](https://github.com/QuantumApprentice/Fallout-Nevada-Translation/commit/8bf64b17471fb873543604e5b7fe8fc0272163ff)
#### Saturday 2022-10-15 14:53:51 by QuantumApprentice

you scratch my back...

changed:
{158}{}{I don't know what the fuck are you talking about. Nobody does anything without personal gain in Vegas. You do something for me, I do something for you. Get it? So, maybe we can make a deal.}
to:
{158}{}{I don't know what the fuck you're talking about. Nobody does anything without personal gain in Vegas. You scratch my back, I scratch yours. Get it? So, maybe we can make a deal.}

I figured the "You scratch my back..."etc line sounded better and is a common colloquialism in the US. What do you think?

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[422accbe4e...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Saturday 2022-10-15 14:56:37 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [Doctor-Derp/lobotomy-corp13](https://github.com/Doctor-Derp/lobotomy-corp13)@[f0e6476eb0...](https://github.com/Doctor-Derp/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Saturday 2022-10-15 15:17:33 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [Avarice12/platform_kernel_xiaomi_vayu](https://github.com/Avarice12/platform_kernel_xiaomi_vayu)@[4541665c6c...](https://github.com/Avarice12/platform_kernel_xiaomi_vayu/commit/4541665c6c334aa358904e8c5bbfd0aa30f06055)
#### Saturday 2022-10-15 16:22:32 by Peter Zijlstra

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

---
## [mpv-player/mpv](https://github.com/mpv-player/mpv)@[6f7506b660...](https://github.com/mpv-player/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Saturday 2022-10-15 16:30:50 by Philip Langdale

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
## [stravid87/VueOnRavi2](https://github.com/stravid87/VueOnRavi2)@[58f11b9166...](https://github.com/stravid87/VueOnRavi2/commit/58f11b9166b4045e6668da15f7b10d8598dd24b1)
#### Saturday 2022-10-15 16:49:36 by stravid87

Simple changes to README.md AND A BIG ASS REBASE!

Update the Readme according to Packt's inst.

There really isn't much more to say in a cn extended instruction set other than yeah, i'd like to see what you can do on the typewrite too?

Update to HelloWorld.vue

What would you like me to add to this extended description?

Response to review as requested.

I added the 13. Happy now?

GIT CLI & Github Desktop

This is from the desktop app

admission of failure

Dude: well done. You are not a failre. (well maybe not...)

yes commit it all up

Add explicitive

updated attempt at the pull request workflow

added test-action.yml

added test-action.yml

added test-action.yml 3

getting my commits and adds out of order

Update test-action.yml

Try 2(6?) to run a simple action.

mmmmm. In time.

Try 7 -- I'll admit it.

If it works, lunch time.

Try Guys 8

Lunch now?

a main commit to change the readme

Attempting rebase of satsite13-branch against main

Changed the readme file (there once was a Two and a Three; no changes I want to add here.)

Simple changes to README.md

---
## [Victorayo/flipify](https://github.com/Victorayo/flipify)@[a894b17a6b...](https://github.com/Victorayo/flipify/commit/a894b17a6b231f2d40a14804c0584ce724c17769)
#### Saturday 2022-10-15 16:57:42 by Victorayo

Flipify logo proposal 

I sent a comment under the social media design for flipify... I asked to send a proposal. It's on flipify logo. 
Sorry I couldn't add my thinking idea page inside the PDF, the file suddenly shows up corrupt when I wanted to add it. In case you want, you can request for it sir, Mr.  Fadahunsi. And I might even snap my sketch book and send under comment section.

Kindly open the PDF file and give your feedback. Thanks

---
## [dilipkumar08/codechef](https://github.com/dilipkumar08/codechef)@[6b96a22dfc...](https://github.com/dilipkumar08/codechef/commit/6b96a22dfc4fcd316ead3a38f224bf965c5efd25)
#### Saturday 2022-10-15 18:16:08 by Dilip

Create Chef_on_date.py

Problem
Chef and his girlfriend go on a date. Chef took XX dollars with him, and was quite sure that this would be enough to pay the bill. At the end, the waiter brought a bill of YY dollars. Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad impression on her.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line of input, containing two space-separated integers XX and YY.
Output Format
For each test case, output on a new line "YES" if Chef has enough money to pay the bill and "NO" otherwise.

You may print each character of the string in either uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---
## [SquirrelCraft/SquirrelPAK-MC18](https://github.com/SquirrelCraft/SquirrelPAK-MC18)@[9b886ad286...](https://github.com/SquirrelCraft/SquirrelPAK-MC18/commit/9b886ad286d30c9bc3b2c01ae82b793791989011)
#### Saturday 2022-10-15 19:07:38 by The Network Squirrel

SP-TEC Release v1.0.1

================================================================================
SquirrelPAK TEC - TelEcommuniCations
Change Log

SquirrelPAK TEC - v1.0.1
File Version 1.18.2+1.0.1
================================================================================

Quick changes

This update, we have updated the mods that needed updated, updated the in game manual, and bumped the forge version due to mod requirements

Known Issues:

We have disabled the loading music due to crashes, If you experience crashes please open an issue!

There is an issue that is with the options.txt file. There are issues
with the mods I usually use so until we get that fix I will ship a options
file. Before updating to new versions if you make changes to your options file
 make a backup copy first and replace it after updating.

Added:
------------------------------------------- 
N/A
------------------------------------------- 

Updated:
------------------------------------------- 
AdChimneys-1.18.2-8.3.3.0-build.1088
AdFinders-1.18.2-7.0.2.0-build.1061
advancednetherite-1.12.4-1.18.2
AdvancementPlaques-1.18.2-1.4.5.1
AI-Improvements-1.18.2-0.5.2
alexsdelight-1.18.2-1.3.3
alexsmobs-1.18.6
appleskin-forge-mc1.18.2-2.4.1
architectury-4.9.84-forge
areas_1.18.2-3.1
fm_audio_extension_forge_1.1.1_MC_1.18-1.18.2
balm-3.2.0+0
BetterAdvancements-1.18.2-0.2.1.132
BetterCompatibilityChecker-1.1.15-build.29+mc1.18.2
biomeinfo-1.18.2-1.5
Bookshelf-Forge-1.18.2-13.2.50
cc-tweaked-1.18.2-1.100.10
ceilingtorch-1.18.2-1.22.1
chalk-1.18.2-1.3.2
cloth-config-6.4.90-forge
Clumps-forge-1.18.2-8.0.0+15
collective-1.18.2-5.7
compactmachines-4.5.0
configured-2.0.0-1.18.2
Controlling-forge-1.18.2-9.0+22
corn_delight-1.0.6-1.18.2
CraftTweaker-forge-1.18.2-9.1.195
CreativeCore_FORGE_v2.6.15_mc1.18.2
curios-forge-1.18.2-5.0.7.1
drippyloadingscreen_forge_1.6.4_MC_1.18-1.18.2
DungeonCrawl-1.18.2-2.3.10
easy_villagers-1.18.2-1.0.11
eccentrictome-1.18.2-1.8.0
EnchantmentDescriptions-Forge-1.18.2-10.0.9
EnderMail-1.18.2-1.2.5
enderchests-1.18-1.9.6
endertanks-1.18-1.11.7
ExplorersCompass-1.18.2-1.3.0-forge
extremesoundmuffler-3.29_forge-1.18.2
fancymenu_forge_2.12.2-1_MC_1.18.2
FarmersDelight-1.18.2-1.2.0
FarmersRespite-1.18.2-1.3.0
ForgeEndertech-1.18.2-9.0.5.0-build.1061
FramedBlocks-5.8.0
ftb-chunks-forge-1802.3.6-build.170
ftb-library-forge-1802.3.6-build.140
ftb-teams-forge-1802.2.6-build.69
functionalstorage-1.18.2-1.0.6
rsgauges-1.18.2-1.2.16
geckolib-forge-1.18-3.0.43
Iceberg-1.18.2-forge-1.0.48
ironchests-2.0.4-forge
ItShallNotTick-1.0.22-build.34
item-filters-forge-1802.2.8-build.40
JEITweaker-1.18.2-3.0.0.9
jei-1.18.2-9.7.1.255
JustEnoughResources-1.18.2-0.14.1.171
konkrete_forge_1.5.2_MC_1.18-1.18.2
laserio-1.4.3
lightmanscurrency-1.18.2-2.0.0.3
lootr-1.18.2-0.2.21.58
mcw-bridges-2.0.5-mc1.18.2forge
mcw-doors-1.0.7-mc1.18.2
mcw-fences-1.0.6-mc1.18.2
mcw-furniture-3.0.2-mc1.18.2
mcw-lights-1.0.4-mc1.18.2
mcw-paintings-1.0.4-mc1.18.2
mcw-paths-1.0.1-mc1.18.2
mcw-roofs-2.2.1-mc1.18.2-forge
mcw-trapdoors-1.0.7-mc1.18.2
Mantle-1.18.2-1.9.27
MapFrontiers-1.18.2-2.3.4
mcjtylib-1.18-6.0.17
selene-1.18.2-1.17.9
morevillagers-forge-1.18.2-3.3.2
mmlib-1.1.3-1.18.2
NaturesCompass-1.18.2-1.9.7-forge
NekosEnchantedBooks-1.18.2-1.8.0
Ore Creeper-1.18.2-1.1.10
panoramica_forge_1.2.1_MC_1.18-1.18.2
Patchouli-1.18.2-71.1
Placebo-1.18.2-6.6.5
randomvillagenames_1.18.2-2.0
realisticbees_1.18.2-2.8
redstonepen-1.18.2-1.0.11
refinedstorage-1.10.3
rftoolsbase-1.18-3.0.11
shetiphiancore-1.18-3.10.10
SimpleBackups-1.18.2-1.1.12
voicechat-forge-1.18.2-2.3.10
sophisticatedbackpacks-1.18.2-3.18.29.718
sophisticatedcore-1.18.2-0.5.13.132
stackrefill_1.18.2-3.2
supermartijn642configlib-1.1.6-forge-mc1.18
supermartijn642corelib-1.0.19-forge-mc1.18
supplementaries-1.18.2-1.5.10
Terralith_v2.2.2
The_Graveyard_1.9.2_(FORGE)_for_1.18.2
theoneprobe-1.18-5.1.2
TConstruct-1.18.2-3.5.2.40
tinyredstone-1.18.2-3.2.2
ToastControl-1.18.2-6.0.3
toms_storage-1.18.2-1.3.5
villagespawnpoint_1.18.2-2.6
villagernames_1.18.2-4.1
waystones-forge-1.18.2-10.1.0
WorldPreGenerator-1.18.2-3.0.1
xnet-1.18-4.0.7
xptome-1.18.2-2.1.6
------------------------------------------- 

Removed:
------------------------------------------- 
N/A
------------------------------------------- 

---
## [Kordasauter/roprime-simulator.com](https://github.com/Kordasauter/roprime-simulator.com)@[6503d25fec...](https://github.com/Kordasauter/roprime-simulator.com/commit/6503d25fec42a4a6899bfd838a6d6ea402e1af7b)
#### Saturday 2022-10-15 19:33:46 by Kordasauter

Bio 5 monster update

15/10/2022:
Has been added :
The Royal Banquet monsters
Frozen Wolf
Taffy
Watcher
Sky Fortress Invasion monsters
Immortal Bloody Knight
Immortal Wind Ghost
Immortal Nightmare Shadow
Immortal Angry Shadow
Immortal Death Shadow
Immortal Zombie Soldier
Immortal Castle Guard
Sky Fortress Key Keeper
Immortal Zombie Assault
Immortal Cursed Zombie
Stefan.J.E.Wolf
Room of Consciousness monsters
Elder Archer Skeleton
Elder Skeleton
Elder Soldier Skeleton
Renovated Amdarais
Enhanced Amdarais
Bijou
Nightmare Glast Heim monsters
Nightmare Wander Man
Cursed Book
Cursed Box
Nightmare Evil Druid
Nightmare Baphomet
Nightmare Chimera
Cursed Grave Keeper
Tomb of Honor monsters
Alphoccio Basil
Celia Alde
Chen Liu
Eremes Guille
Flamel Emule
Gertie Wie
Harword Alt-Eisen
Kathryne Cheiron
Margaretha Sorin
Randel Lawrence
Seyren Windsor
Shecil Damon
Trentini
Minstrel Alphoccio
Sorcerer Celia
Sura Chen
Guillotine Cross Eremes
Genetic Flamel
Shadow Chaser Gertie
Mechanic Howard
Warlock Kathryne
Arch Bishop Margaretha
Royal Guard Randel
Rune Knight Seyren
Ranger Cecil
Wanderer Trentini

---
## [phil-blain/git](https://github.com/phil-blain/git)@[5beca49a0b...](https://github.com/phil-blain/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Saturday 2022-10-15 19:57:12 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [imaansaleem/Competitive_Programming](https://github.com/imaansaleem/Competitive_Programming)@[89493ef554...](https://github.com/imaansaleem/Competitive_Programming/commit/89493ef554ac4c80361c2e5caa29ff2deb2c4dde)
#### Saturday 2022-10-15 20:06:06 by imaansaleem

Add files via upload

https://codeforces.com/problemset/problem/1293/A
A.R.C. Markland-N is a tall building with n floors numbered from 1 to n. Between each two adjacent floors in the building, there is a staircase connecting them.
It's lunchtime for our sensei Colin "ConneR" Neumann Jr, and he's planning for a location to enjoy his meal.
ConneR's office is at floor s of the building. On each floor (including floor s, of course), there is a restaurant offering meals. However, due to renovations being in progress, k of the restaurants are currently closed, and as a result, ConneR can't enjoy his lunch there.
CooneR wants to reach a restaurant as quickly as possible to save time. What is the minimum number of staircases he needs to walk to reach a closest currently open restaurant.
Please answer him quickly, and you might earn his praise and even enjoy the lunch with him in the elegant Neumanns' way!

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[537742eb67...](https://github.com/rd-stuffs/msm-4.14/commit/537742eb67f778c49d4044c2868c213f73320207)
#### Saturday 2022-10-15 20:12:37 by Wang Han

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
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[bca7b4537c...](https://github.com/GeoB99/reactos/commit/bca7b4537ce01c47d322a8caf3b7cb48b149b98d)
#### Saturday 2022-10-15 20:44:13 by George Bișoc

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
## [MoldyGH/VsDave](https://github.com/MoldyGH/VsDave)@[0feb3934cf...](https://github.com/MoldyGH/VsDave/commit/0feb3934cfb8d776db6ecf0122d8489a8452028a)
#### Saturday 2022-10-15 21:05:31 by T5mpler

NSHSFBKHSDFSKHDBSDFHKFB i hate comments they're stupid! sorry you removed secret mod leak ben i had to

---
## [overte-org/overte](https://github.com/overte-org/overte)@[4a49631007...](https://github.com/overte-org/overte/commit/4a49631007af4a471acf179d9a7a4bca19ea6afa)
#### Saturday 2022-10-15 21:30:22 by Alezia Kurdis

Added HMD notifications dismissal

Added a gestural way to dismiss the notifications in HMD.

The notifications vanishes after 10 sec. 
But if for any reason we want to accelerate the process (mostly because it hide the view or it is going to appears in photo capture)
In Desktop we can simply click on the notification to get rid of them.
But in HMD, clicking was kinda a pain (assuming the if you want to dismiss the notification is often because they are already annoying you)
have to aim and click is like pressing a button using a fishing pole, it's certainly adding more annoyance to this.
To addressed that, I introduced the "Whoosh!": An easy gesture to dismiss any 3d UI, by simply move one of you controller over you eyes height. (a bit like making flee an annoying fly.)

---
## [jrhy/sandbox](https://github.com/jrhy/sandbox)@[8f13363682...](https://github.com/jrhy/sandbox/commit/8f133636822742248600915aa8b023a5300477dc)
#### Saturday 2022-10-15 21:47:15 by jrhy

sql fun
    fix unary- with precedence climbing
    want to see in side the index dammit
    wip: order by
    drop table
    recognize column constraints to reject keys/uniqueness for now
    s3db working but dirty
    funkyshooshoo
    break out memory/s3db db drivers
    null values going through driver
    left join works
    hmmmm, permutation broken
    simplify right-to-left fromItem permutation
    start join conditions
    joins working, alias untangled
    join working except need to fix schemas through subqueries
    holy shit join is kinda working
    adjust join parsing to be loud about subquery unimpl
    parse join on/using/unconditional
    breakout fromitem
    push joins, tableOrSubquery
    verking, gotta fix aliases
    rename FromItem->Source and Table->FromItem
    why TestJoin there is no JOIN
    verking
    fixedit
    insert
    verking
    sql: create table
    sql: start go sql driver
    sql: add funcs.go
    derive operator matching and precedence from single table
    string concatenation

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[def46f098d...](https://github.com/treckstar/yolo-octo-hipster/commit/def46f098d843e0cf4ddf9108fb4070e194ff5ce)
#### Saturday 2022-10-15 22:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---

