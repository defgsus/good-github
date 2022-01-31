## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-30](docs/good-messages/2022/2022-01-30.md)


1,434,326 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,434,326 were push events containing 2,064,430 commit messages that amount to 120,210,707 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [greenforce-project/kernel_xiaomi_citrus_sm6115](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115)@[ecb548ec78...](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115/commit/ecb548ec7830f63211e6ce6cdba77062d32013dc)
#### Sunday 2022-01-30 00:27:21 by Angelo G. Del Regno

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

---
## [Prodigy-Hacking/ProdigyMathGameHacking](https://github.com/Prodigy-Hacking/ProdigyMathGameHacking)@[c79d9b92b3...](https://github.com/Prodigy-Hacking/ProdigyMathGameHacking/commit/c79d9b92b392b137c2683d98ab185cd9232716ba)
#### Sunday 2022-01-30 00:30:48 by yamaaaaa

removing the fucking tower stacking lookin ass tex

like fuckthat text itys so fucking ass i ahgegthat shit like what the fuck why was it built like that ik im the onw who put it there but sutll what the fuck i fuckin hae that text all my homis hate that text fyck that tesxt im remoiving that piece of shit and replacing it with absoltuely tnoghint ahts how much. hate that poece of shit bitch ass dumbass lookin ass piece iof shitu twoer of god robloxgam ek lookin ass tecg god dman it fuyck you wy did that texist like what the fuckk

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[1dfcffccd1...](https://github.com/Lamella-0587/Skyrat-tg/commit/1dfcffccd1d453fc0d3f928f5dfa1d3115f977f9)
#### Sunday 2022-01-30 01:26:55 by Zenitheevee

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
## [YumeMichi/kernel_oneplus_sm8250](https://github.com/YumeMichi/kernel_oneplus_sm8250)@[053a8dc8bc...](https://github.com/YumeMichi/kernel_oneplus_sm8250/commit/053a8dc8bc807e217ba8ae98a153993875b56eb6)
#### Sunday 2022-01-30 01:47:32 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [Hugo-Carbiener/GGJ-Plateformer](https://github.com/Hugo-Carbiener/GGJ-Plateformer)@[7cb17cb638...](https://github.com/Hugo-Carbiener/GGJ-Plateformer/commit/7cb17cb6386041507252df0537f4d43473c47f19)
#### Sunday 2022-01-30 02:34:02 by BiscuitPrime

The Eternal Pain of Anguish and Darkness shall absolve of our might, for we are the ones of dust and sand, mighty children of Al-Kal-Taka. And when the dust settles, and when the rain falls, we shall remember this pain for it is our soulheart. This sword is ours, this might is ours. Pride in our fall we will have. This is our credo. This is our might. This is what makes us Orphans !

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[6ed2fafd4e...](https://github.com/Ryll-Ryll/tgstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Sunday 2022-01-30 03:40:29 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [jaltod/kernel_xiaomi_vayu](https://github.com/jaltod/kernel_xiaomi_vayu)@[a908e19675...](https://github.com/jaltod/kernel_xiaomi_vayu/commit/a908e196755bb11a056d4318d2a2a1c8b071b2f2)
#### Sunday 2022-01-30 03:43:08 by Wang Han

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: jaltod <jaguarexodus@gmail.com>

---
## [Erhannis/LanCopyCore](https://github.com/Erhannis/LanCopyCore)@[32694ab799...](https://github.com/Erhannis/LanCopyCore/commit/32694ab799edcdf00e96c3f0cc59ab3e219e5643)
#### Sunday 2022-01-30 04:50:12 by erhannis

AUGH, THAT WAS A STUPID SECURITY MISTAKE.  But it's fixed now, I think.  I remember thinking, 'there, even if something in here crashes, it won't let the cert pass unless it means to.'  NOPE.  But again, fixed now.  Also a few other tweaks.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[25a0bf6ef3...](https://github.com/repinger/exynos9611_m21_kernel/commit/25a0bf6ef3041caf917f8c14a4f64e3d1acdee44)
#### Sunday 2022-01-30 05:57:33 by Christian Brauner

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
## [Leo2323232/MARDEK-Leos-Mod](https://github.com/Leo2323232/MARDEK-Leos-Mod)@[552897a040...](https://github.com/Leo2323232/MARDEK-Leos-Mod/commit/552897a040ce2bc1081986b756d996c81b0c9525)
#### Sunday 2022-01-30 06:37:51 by Leo2323232

def passive fix

this fix took 4 fucking hours of my goddamn fucking life, AND NO ONE IS GOING TO APPRECIATE IT FFS

---
## [Commandtechno/spotify](https://github.com/Commandtechno/spotify)@[26d1eb4ea8...](https://github.com/Commandtechno/spotify/commit/26d1eb4ea8f69cbca0feb4146655271ee5388166)
#### Sunday 2022-01-30 07:48:25 by Commandtechno

Create main.yml

testing github actions because boop dog wont do shit until i do fuck you boopd og ♥

---
## [Greniza/fulpstation](https://github.com/Greniza/fulpstation)@[c449fbb56c...](https://github.com/Greniza/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Sunday 2022-01-30 07:49:11 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [chandu078/kernel_oneplus_sm8250](https://github.com/chandu078/kernel_oneplus_sm8250)@[b385a925a6...](https://github.com/chandu078/kernel_oneplus_sm8250/commit/b385a925a688676372826c750126cf0943bdc3c8)
#### Sunday 2022-01-30 08:09:57 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: chandu078 <chandudyavanapelli03@gmail.com>

---
## [kurisufriend/modular-discord-bot-fw](https://github.com/kurisufriend/modular-discord-bot-fw)@[9dc14f69b7...](https://github.com/kurisufriend/modular-discord-bot-fw/commit/9dc14f69b7564cd3f01a1167b115d0c55e429a33)
#### Sunday 2022-01-30 09:06:18 by BuildTools

clean up main.py and
facilitate the calling of member destructors so cleanup actually works!
i hate python's gc this is actual trash when i delete an object the
destructor isn't called this is insane if you're not writing "pythonic" codethe secret police comes in the night and takes your right to function away

---
## [Ratkiller446/Trollack-0.0.1clean](https://github.com/Ratkiller446/Trollack-0.0.1clean)@[b05b1cea64...](https://github.com/Ratkiller446/Trollack-0.0.1clean/commit/b05b1cea648a12d52379e9f7b615572d3a3cbcbb)
#### Sunday 2022-01-30 10:23:03 by Ratkiller446

Add files via upload

And if you think its just an rename go fucking check theia nigga just a shit clean just deleted winrar files

---
## [rowr111/xous-core](https://github.com/rowr111/xous-core)@[25bccd9446...](https://github.com/rowr111/xous-core/commit/25bccd9446ec7aaecb998393c3e50c9c7eaf3dde)
#### Sunday 2022-01-30 10:25:34 by bunnie

THE BALDEST YAK: keyboard injection now working

I wrote in a commit yesterday how there was no ROI on doing this
yet somehow I kept on doing it. I blame poor impulse control.

Turns out there was a series of race conditions and bugs that
caused this thing to "mostly work" on the first go at it but
really hard to debug and get very right.

1. Litex UART has a weird undocumented API. You advance the Rx
FIFO by writing `1` to the PENDING bit, and no other way. However,
you determine if there are any more characters to receive by
reading the EMPTY bit and seeing if it is 1. The previous method
wrote `1` to the PENDING bit and then used the PENDING bit to
see if a character was available, under the theory that the
PENDING bit would be set again if there was still a character.
This is somewhat true, except that the PENDING bit is set only
some amount of time later which is about comparable to a few
CPU instructions, so if you had a fast loop path the PENDING
bit would show as cleared and you'd exit, which would cause
no further interrupts to fire because the interrupt was
effecitvely not acknowledged.

This isn't written up anywhere but I figured this out by
just reading the source code for Litex UART and BIOS:
https://github.com/enjoy-digital/litex/blob/e8be3915041707860e70b15d062661fc1f67a09f/litex/soc/cores/uart.py#L264-L279
https://github.com/enjoy-digital/litex/blob/ccd3ab17be1f8770c59ec1c62e0285d3bac3cc26/litex/soc/software/libbase/uart.c#L38-L44

2. I had the Key Injector IP block in the `sys` domain, which
would have its clock cut when the CPU went to sleep, which would
cause input characters to disappear when the CPU went into power
saving. moving this to "always on" domain fixes that.

3. I had the UART PHY in the always on block (so you could
send or receive exactly one character), but not the
separate UART block (which contained the FIFOs).
The UART block would also go into power
savings, and this would cause FIFO entries to go missing.

4. Escape sequences get sent as a burst of characters. The Key Injector
originally did not have a FIFO of its own, so it would only
remember the *last* key of the sequence that was written, causing
some keys to be dropped occassionally. Adding a 16-deep FIFO
to the injector fixes this.

5. The code I had to read out the injector's results was designed with
the "strobe" bit (to indicate that the FIFO had characters) in the
same regsiter as the character itself. Thus the loop that 1. checked
if the fifo was empty then 2. read and forwarded the character
would actually perform two reads from the FIFO. However, this "mostly worked"
I think because the FIFO retains the last value that was written
even when it was empty, so if only one character was read at a time
everything was fine. It only didn't work when you stuffed two characters
in there, as you'd drop the first one. Reading the FIFO once and
then interpreting the code with a bitmask fixes this.

6. The escape sequences, in their full glory with no dropped characters,
required a refactored parsing routine, which I have now added.

7. backspace->delete mappings, the bane of computer engineers since 1960.

OK. very bald yak. Here I lay down the shears next to several
mooshi pillows stuffed with the finest Yak hair.

---
## [StardOva/Softwareprojekt](https://github.com/StardOva/Softwareprojekt)@[a029a540ee...](https://github.com/StardOva/Softwareprojekt/commit/a029a540eee93439dee8918fb3645335ea19ca76)
#### Sunday 2022-01-30 10:33:17 by Moritz Reichelt

fix this fucking piece of shit code fucking bullshit

---
## [StratusFearMe21/uwuifyy](https://github.com/StratusFearMe21/uwuifyy)@[325242674b...](https://github.com/StratusFearMe21/uwuifyy/commit/325242674b9bad8f748dac97f7b82f39ae47c747)
#### Sunday 2022-01-30 11:03:23 by Isaac Mills

FIFTEEN TIMES SPEED BOOST HOLY SHIT OMG HOW TF *<>*

---
## [fritsch/xbmc](https://github.com/fritsch/xbmc)@[ee5e0a485b...](https://github.com/fritsch/xbmc/commit/ee5e0a485ba8b2321f50f493a7a10a063f8f54f7)
#### Sunday 2022-01-30 11:19:47 by fritsch

AESinkAudioTrack: Pause-Burst - a little revisit

Pause-Bursts in RAW format are a red hering in general as they rely on
a non-existing API within Android. The implementation opens the audio
device but directly pauses it, hoping that internally the system does
the needful to keep the sink alive.

Sadly this happens intransparent for kodi, as the reported buffer of the
device stays zero. VideoPlayer calls AddPause multiple times in the
beginning to sync audio and video properly, while expecting that pause
bursts on audio side will fill up the sink (prepare it) and on the same time
causing a certain stable or better said: known delay when real data is
added later on.

The implementation asks android to pause, but blocks video player for the
amount of millis that it wants to add, stating: buffer is already filled.

As we sleep the non-existing data in, we need to "hack" the way back, remember
buffer is empty and not filled when first AddPacket is coming. We fake
this situation further until the real audio data has reached the same level
then we continue normally. Especially the way out is the hack as AE
exactly knows that out of a sudden 10 ms of data cannot be added in 0 ms if
the buffer is actually full. Though AE nicely gives us some time to get
our stuff in line.

But hack stays hack. If someone of google reads this:
Please add a method where you expose your IEC Packer so that we can create
and enqueue pause_bursts like normal audio. That way these hacks here would
not be needed at all.

---
## [rscDoesMoreTrolling/Duy_Fortress](https://github.com/rscDoesMoreTrolling/Duy_Fortress)@[9307941f62...](https://github.com/rscDoesMoreTrolling/Duy_Fortress/commit/9307941f624c853096367d1bb28796da994d37c6)
#### Sunday 2022-01-30 12:41:14 by Jet

Update stuff

idk duy didnt want people to translate the js script into a fuckin idk some hacker's bullshit

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[e25d31937a...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/e25d31937a1e1ad56b5e5a1e48eaccb4479ecf76)
#### Sunday 2022-01-30 13:32:29 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

a

---
## [foopis23/ggj-2022](https://github.com/foopis23/ggj-2022)@[8ab8081352...](https://github.com/foopis23/ggj-2022/commit/8ab80813527e6e4c69ed17518028bcab1ad112f5)
#### Sunday 2022-01-30 15:02:47 by Eric Sexton

Merge pull request #16 from foopis23/fuck-you-eric-i-can-read

Fuck you eric i can read

---
## [jpfraneto/rudraky](https://github.com/jpfraneto/rudraky)@[afe1532101...](https://github.com/jpfraneto/rudraky/commit/afe1532101d8ea6e6b9deb45928bc8fc9c5562df)
#### Sunday 2022-01-30 15:04:13 by jpfraneto

Dia 9. Yesterday I was not able to come here and do the work, because my familiar duties were more important than that. It felt really interesting to manage the tension that was generated in my experience because of not being able to code yesterday. It is part of the process, to find that balance and realize where and when, how to organize my time, so that I can do what I have to do. But this is a long shot, for a long time, so I will give my best to not be hard with me. There is a lot going on. But todays programming session was amazing, Im working with the api building, with the ability to create kriyas and save them to the db, read them from there, and play them with this information. The whole integration of the system is working as a charm right now, as I better understand how to use nextjs-es native functions such as getServerSideProps better to have a great UI. This was a really good day of work, I feel complete and motivated.

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[e03713ea1b...](https://github.com/sunamo/sunamo/commit/e03713ea1bad2ecff4a90584cb11df6f45ab8089)
#### Sunday 2022-01-30 15:46:53 by Radek Jancik

This is perhaps the most distinctive Buddhist teaching, that suffering is the product of 'the craving of the passions, the craving for existence, the craving fornonexistence.' It is, however, far from an obvious truth. Certain cases of suffering areplainly due to craving, namely, those that are due to frustrated desires. Desires may be eased by satisfaction or extirpation; and one may allow that if one stopped desiring, itwould amount to preventing all the suffering due to frustration. But this does not provethe general case.... Body, feelings, perception, mentality, and consciousness are separate sets of graspings. There is nothing that -does- the grasping. -We- are the aggregate ofthe graspings, not something, apart from them, that does the grasping. This is an interesting and startling thought.  - Danto, Arthur Coleman

---
## [dexeonify/mpv-config](https://github.com/dexeonify/mpv-config)@[892fe3bf81...](https://github.com/dexeonify/mpv-config/commit/892fe3bf81efbfafb0001f147e79e1413334aee6)
#### Sunday 2022-01-30 15:55:12 by dexeonify

Remove scaling TODO

This certainly took longer than usual, but the main reason it was
delayed by 6 days since e3fe622 is because I decided to do a week-long
testing. Unfortunately, there's not much I can change about scaling
without breaking "compatibility".

spline36 being the default for `gpu-hq` is mostly fine. I know most
people use ewa_lanczossharp, but I honestly can't tell any difference
compared to spline36, so I chose not to stress my GPU further and stick
with the default. FYI, ewa_lanczossharp is perfectly viable for an iGPU,
since upscaling only happens if the source video is smaller than your
display. 720p videos aren't hard to upscale at all.

I also wanted a better upscaling filter by default because bilinear
genuinely looks blurry and bad. HOWEVER, I want to retain the default
downscaling algorithm to bilinear because mitchell is apparently too
much for 4K60. Thus, all I have to do is set `scale=spline36` and
`dscale=bilinear`, right?

Sadly, there's currently a bug (mpv-player/mpv#5727) where if you
specify `--scale` to anything other than bilinear, THEN set `--dscale`
back to bilinear, there will be an additional "bilinear" filter that
increases the GPU usage for nothing! This ghost bilinear filter eats up
so much GPU that it boosts the frame times from <7ms to ~25ms, enough to
make 60FPS footage drop frames. This is playing a 4K60 AV1 video, btw.

With all the considerations above, I don't think the drawback is worth
it, so I kept the scaling config at default.

---
## [dexeonify/mpv-config](https://github.com/dexeonify/mpv-config)@[f576dac094...](https://github.com/dexeonify/mpv-config/commit/f576dac094c99ed03ed07cdb0f33b51eda14baea)
#### Sunday 2022-01-30 15:55:12 by dexeonify

Update debanding config

In this commit, I overhauled my debanding config based on my subjective
opinion and use cases. As always, consult the mpv manual:
https://mpv.io/manual/master/#options-deband to understand what each of
the options do. Though from my testing, only `deband-threshold` seems to
make a significant difference, and `deband-grain` too if you hate grain.

Basically, my debanding settings are divided into 3 modes: light, medium
and heavy. They can be cycled using input.conf.

- "Light" is slightly modified from Kokomin's debanding preset for Anime
  Contrary to most mpv enjoyers, I don't watch anime, but I guess this
  preset is nice if the video is already high quality and only needs
  minimal debanding.

- "Medium" is derived from Kokomin's debanding preset for "really,
  really bad streams". I skipped the middle preset because I didn't find
  much use case for it. I deal with a lot of shitty YouTube streams so I
  set this as the default. Also I like grain :)

- "Heavy" is the actual "for really really bad streams" preset. I mainly
  use it for terribly bitrate-starved conference/lecture video. Extra
  bonus, it works quite well in Tom Scott's "Why Dark Video Is A
  Terrible Blocky Mess" video too!

---
## [tom5079/Pupil](https://github.com/tom5079/Pupil)@[26204da5fe...](https://github.com/tom5079/Pupil/commit/26204da5fe041f54591cd55ce172e293d0df37a9)
#### Sunday 2022-01-30 16:03:32 by tom5079

Hitomi is stupid enough to block user agent for chrome... holy shit
Added self-test and reload
Reduced update ignoring time to 1d from 1w

---
## [termux/termux-packages](https://github.com/termux/termux-packages)@[7b355a29d0...](https://github.com/termux/termux-packages/commit/7b355a29d05fa8570c2d9e25b55d135db96d6725)
#### Sunday 2022-01-30 16:05:27 by Henrik Grimler

texlive{,-full}: remove package

It is one (soon two) years behind, and is a big hack: some of the debs
are larger than our upload system can handle, and the file lists are
generated from the tlpdb in a not so nice way that breaks horribly on
every texlive release.  Disk space is somewhat of a concern again on
the host that fosshost gives us at no (!) cost, and removing
texlive-full gives us ~1 GB of space.

The reasonable thing to do would be to set up a separate
"termux-texlive" repo, and create a package for every texlive package
rather than for every collection as done here.  Debian, ubuntu and
friends properly creates subpackages.  I am not really motivated to do
this though, so if someone else has use of a properly packaged texlive
and wants to look into it, then that would be great.

Users that want to use texlive should install texlive-installer
instead, it anyways allows for more convenient installation (you can
freely choose which scheme and which packages to install).

---
## [Kartikkala/sdm660_realme2pro](https://github.com/Kartikkala/sdm660_realme2pro)@[198a54f07f...](https://github.com/Kartikkala/sdm660_realme2pro/commit/198a54f07f51d4f52503ae611e0b0c1e8e445cef)
#### Sunday 2022-01-30 16:19:43 by J. Bruce Fields

nfsd: allow fh_want_write to be called twice

[ Upstream commit 0b8f62625dc309651d0efcb6a6247c933acd8b45 ]

A fuzzer recently triggered lockdep warnings about potential sb_writers
deadlocks caused by fh_want_write().

Looks like we aren't careful to pair each fh_want_write() with an
fh_drop_write().

It's not normally a problem since fh_put() will call fh_drop_write() for
us.  And was OK for NFSv3 where we'd do one operation that might call
fh_want_write(), and then put the filehandle.

But an NFSv4 protocol fuzzer can do weird things like call unlink twice
in a compound, and then we get into trouble.

I'm a little worried about this approach of just leaving everything to
fh_put().  But I think there are probably a lot of
fh_want_write()/fh_drop_write() imbalances so for now I think we need it
to be more forgiving.

Signed-off-by: J. Bruce Fields <bfields@redhat.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Kanium/bpl-46Mod](https://github.com/Kanium/bpl-46Mod)@[b33fd81cdd...](https://github.com/Kanium/bpl-46Mod/commit/b33fd81cdd51d7f625f6b6512310f634c44a765d)
#### Sunday 2022-01-30 16:52:35 by AllfatherHatt

Added burstfire, added more fuck-you levels of damage

---
## [Antony1060/svg-gen](https://github.com/Antony1060/svg-gen)@[d40cb9264a...](https://github.com/Antony1060/svg-gen/commit/d40cb9264ae3bd98f513e1fbcecc084d885674b8)
#### Sunday 2022-01-30 17:21:23 by Antony1060

Png support + fucking manual ts compiling because shit, aaaah I hate this

---
## [crawl/crawl](https://github.com/crawl/crawl)@[3307026b18...](https://github.com/crawl/crawl/commit/3307026b184179e413c8a1a16520f462d5523b2d)
#### Sunday 2022-01-30 17:36:48 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

(cherry picked from commit 9e681642b6851451cbfcbc7a92e7de4b97106055)

---
## [double-a-stories/life-of-the-party](https://github.com/double-a-stories/life-of-the-party)@[a0338e74e1...](https://github.com/double-a-stories/life-of-the-party/commit/a0338e74e1a050692d68d45dbbcf445ebca863a4)
#### Sunday 2022-01-30 17:43:13 by double-a-stories

Changed most instances of "God" to other stuff

-Most characters reflexively use "oh my gosh" instead.
-Nikki/Nox are polytheists, and say "gods"
-Ana uses "G-d" instead. She's Jewish.
-Hollis's commands still use "oh god oh fuck"
-The "pantheon of animal gods" are no longer forgotten.

---
## [Mara-Li/Seed_publish](https://github.com/Mara-Li/Seed_publish)@[8434b397f6...](https://github.com/Mara-Li/Seed_publish/commit/8434b397f6ef21b553e113786708d2430454a1a1)
#### Sunday 2022-01-30 18:08:14 by Mara

**Updated** :

- Note temporaire in [notes]
- Ref snippet in [notes]
- machin in [docs]
- Course in [notes]
- Dépense in [notes]
- Mods list in [notes]
- 10. Master in [notes]
- Modèle Linéaire in [Modèle Linéaire]
- 2014 in [notes]
- 2017 in [notes]
- 2019 in [notes]
- 2021 in [notes]
- 2014 in [notes]
- 2015 in [notes]
- 2020 in [notes]
- 2021 in [notes]
- 2015 in [notes]
- 2017 in [notes]
- Prévention et contrôle des infections liées aux soins in [notes]
- ◉ Étude flash de prévalence in [Méthodologie]
- ◉ Incidence - Prévalence in [Toutes]
- ◉ Ratio standardisé d'incidence in [Méthodologie]
- ☣️Analyse des modes de défaillance de leurs effets et de leur criticité in [Gestion des risques]
- ☣️Analyse des risque a priori in [Gestion des risques]
- ☣️Introduction à la gestion des risques in [Gestion des risques]
- ☣️La culture de sécurité de soin in [Gestion des risques]
- ☣️Méthode ALARM in [Gestion des risques]
- ☣️Méthode d'évaluation et d'améliorations des pratiques professionnels in [Gestion des risques]
- ☣️Risques médicamenteux in [Gestion des risques]
- 👏Organisation & pilotage SP in [Memento]
- 🛂Aspergillose pulmonaire invasive in [Gestion des risques]
- 🛂Audit et infections nosocomiales in [Gestion des risques]
- 🛂Infections liées aux cathéters in [Gestion des risques]
- 🛂Infections nosocomiales pulmonaires in [Gestion des risques]
- 🛂Infections urinaires in [Gestion des risques]
- 🛂Introduction aux IAS in [Gestion des risques]
- 🛂Microbiologie in [Gestion des risques]
- 🛂Surveillance épidémiologique in [Gestion des risques]
- 🛂Surveillance microbiologiques in [Gestion des risques]
- 🦀Epidémiologie des cancers du poumon - Cancer et tabac in [Épidémiologie]
- 🦀Epidémiologie du mélanome in [Épidémiologie]
- 🦀Épidémiologie du cancer du sein in [notes]
- 🦀Infections & Cancer in [Épidémiologie]
- 🦀La surveillance du cancer dans le monde in [Épidémiologie]
- 🦀Les cancers professionnels in [Épidémiologie]
- 🦀Nutrition & cancer in [Épidémiologie]
- 🦀Prévention des cancers in [Épidémiologie]
- 🦀Surveillance du cancer en France in [Épidémiologie]
- 🦠Épidémiologie des hépatites in [Épidémiologie]
- 🦠Introduction aux zoonoses in [Épidémiologie]
- 🦠Les méningites bactériennes in [Épidémiologie]
- 🦠Maladie sexuellement transmissibles in [Épidémiologie]
- 🦠Maladies infectieuses émergentes in [Épidémiologie]
- 🦠Paludisme in [Épidémiologie]
- 🦠Tuberculose in [Épidémiologie]
- 🦠VIH — Sida in [Épidémiologie]
- 🦺Identitovigilance in [Gestion des risques]
- 🦺Matériovigilance in [Gestion des risques]
- 🦺Pharmacovigilance et alertes sanitaires in [Gestion des risques]
- 🦺Surveillance du sang in [Gestion des risques]
- 🧰 Étude cas-témoin in [Épidémiologie]
- 🧰Échantillonnage et plans de sondages in [Épidémiologie]
- 🧰Étude écologique in [Épidémiologie]
- 🧰Étude transversale in [Épidémiologie]
- 🧰Pathologie transmissible et chronique in [Épidémiologie]
- 🧰Série de cas in [notes]
- 🩹 Toxoplasmose in [notes]
- Formules in [notes]
- Incidence & prévalence $ in [Épidémiologie]
- Mortalité $ in [Épidémiologie]
- OR & RR $ in [Épidémiologie]
- Article works in [Anglais]
- Ebola in [Anglais]
- Analyse des risque a priori in [notes]
- Base réglementaire de sécurité sanitaire in [Gestion des risques]
- Introduction à la gestion des risques in [Gestion des risques]
- La certification des établissements sanitaires in [Gestion des risques]
- La culture de sécurité de soin in [Gestion des risques]
- La médecine de catastrophe et situations exceptionnelles in [Gestion des risques]
- M2-17. Gestion des risques in [notes]
- Méthode ALARM in [Gestion des risques]
- Méthode d'évaluation et d'améliorations des pratiques professionnels in [Gestion des risques]
- Organisation de la gestion des risques aux niveaux national, régional et local in [Gestion des risques]
- Organisation législative des risques sanitaires en France in [notes]
- Risques médicamenteux in [Gestion des risques]
- Erreur de mesure in [Épidémiologie]
- Etude cas-témoin — Pathologie transmissible in [Épidémiologie]
- Échantillonnage et plans de sondages in [Épidémiologie]
- Étude de cohorte in [Épidémiologie]
- Étude écologique in [Épidémiologie]
- Étude transversale in [Épidémiologie]
- Introduction à l'anthropologie des soins et de la santé in [Épidémiologie]
- Introduction à l'épidémiologie in [Épidémiologie]
- M2-18. Méthode en épidémiologie in [notes]
- Pathologie transmissible et chroniques in [Épidémiologie]
- Série de cas in [Épidémiologie]
- Lecture critique d'article — Cas témoins in [Épidémiologie]
- TD — Etude cas témoin dans les maladies chroniques in [Épidémiologie]
- TD — Etude de deux cohortes in [Épidémiologie]
- Anova à un facteur in [notes]
- M2-2. Modèle Linéaire in [notes]
- Régression linéaire et corrélation in [Mathématiques]
- Check-list de l'organisation du bloc opératoire in [notes]
- Etablissement de santé et développement durable in [Gestion des risques]
- Gestion des déchets et effluents à risques hospitaliers in [Gestion des risques]
- Identitovigilance in [Gestion des risques]
- M2-21. Qualité et sécurité des produits de santé in [notes]
- Matériovigilance in [Gestion des risques]
- Pharmacovigilance et alertes sanitaires in [Gestion des risques]
- Radiologie et risque in [Gestion des risques]
- Responsabilité médicale en établissement de santé in [Gestion des risques]
- Surveillance du sang in [Gestion des risques]
- Aspergillose pulmonaire invasive in [Gestion des risques]
- Audit et infections nosocomiales in [Gestion des risques]
- Covid-19 in [Épidémiologie]
- Infections liées aux cathéters in [Gestion des risques]
- Infections nosocomiales pulmonaires in [Gestion des risques]
- Infections urinaire in [Gestion des risques]
- Introduction aux IAS in [Gestion des risques]
- Investigation d'une épidémie d'infections associées aux soins in [Épidémiologie]
- Les infections de site opératoire (ISO) in [Gestion des risques]
- M2-22. Prévention et contrôle associés aux soins in [notes]
- Médecine du personnel et infections nosocomiales in [Gestion des risques]
- Microbiologie in [Épidémiologie]
- Prévention de la transmission croisée in [Infections liées aux soins]
- Stérilisation in [notes]
- Surveillance épidémiologique in [Gestion des risques]
- Surveillance microbiologiques in [Infection liée aux soins]
- Dépistage organisé des cancers en région AURA in [Épidémiologie]
- Epidémiologie des cancers du poumon - Cancer et tabac in [Épidémiologie]
- Epidémiologie du mélanome in [Épidémiologie]
- Épidémiologie du cancer du sein in [Épidémiologie]
- Facteur de risques de cancer in [Épidémiologie]
- Infections & cancer in [Épidémiologie, Épidémiologie-cancers]
- La surveillance du cancer dans le monde in [Épidémiologie]
- Les cancers professionnels in [notes]
- M2-23. Épidémiologie des cancers in [notes]
- Nutrition & cancer in [Épidémiologie]
- Prévention des cancers in [Épidémiologie]
- Surveillance du cancer en France in [Épidémiologie]
- Taux de mortalité in [notes]
- ❌ Epidémiologie des prédispositions héréditaires in [notes]
- ❌ Epidémiologie génétique in [Épidémiologie]
- ❌Base clinique du cancer in [Épidémiologie]
- ❌Carcinogenèse et biologie du cancer in [Épidémiologie]
- 2014-2015 in [notes]
- Analyses spatiales in [Épidémiologie]
- Concept de réservoir et introduction aux modèles SIR in [Épidémiologie]
- Émergence de zoonose et facteurs favorisant in [Épidémiologie]
- Les zoonoses parasitaires in [Gestion des risques, One-Health]
- M2-25. One-Health in [notes]
- Modèles dynamiques en épidémiologie in [Épidémiologie]
- Oral - Reptiles et zoonoses in [Gestion des risques]
- Epidémiologie vétérinaire in [Épidémiologie]
- Épidémiologie des hépatites in [Épidémiologie]
- Épidémiologie générale des maladies virales in [Épidémiologie]
- Introduction aux zoonoses in [Épidémiologie]
- Les méningites bactériennes in [Épidémiologie]
- Les vaccins obligatoires in [None]
- M2-24. Épidémiologie des maladies infectieuses in [notes]
- Maladie sexuellement transmissibles in [Épidémiologie]
- Maladies infectieuses émergentes in [Épidémiologie]
- Paludisme in [Épidémiologie]
- Principale bactéries infectieuses in [Épidémiologie]
- Tuberculose in [notes]
- VIH — Sida in [Épidémiologie]
- Biais in [Memento]
- Effets indésirables in [Memento]
- Épidémiologie in [Memento]
- Étude cas témoin 🗒️ in [Memento]
- Étude de cohorte in [Mémento]
- Incidence in [Méthodologie]
- Odds-Ratio in [Memento]
- Prévalence in [Méthodologie]
- Prévention in [Memento]
- Risque relatif in [Memento]
- Signalement in [Memento]
- Surveillance in [Méthodologie]
- Vigilance in [Memento]
- 20. Roleplay in [notes]
- Symbole relations in [False]
- Écho in [notes]
- Salem in [Fiche RP]
- Zéphyr in [Fiche RP]
- Invocation d'armes in [notes]
- Nécromancie in [Pouvoirs]
- Pixellisation in [None]
- Pouvoirs in [notes]
- Sortilège in [notes]
- Spiritisme in [notes]
- Éden in [notes]
- Personnage in [notes]
- 22. Personnages in [Fiche RP]
- Ether Blake in [notes]
- Jake O'Connor in [Fiche RP]
- Alwyn Kallendris in [Fiche RP]
- × Illustration × (Ashling) in [Illustration]
- Eilwellyn Beausang in [notes]
- Obsius in [notes]
- × Illustration × in [notes]
- Lagendia in [notes]
- Obsius in [Légendia]
- Relations in [notes]
- 24. FFXIV in [notes]
- Kara Grimalkin in [FFXIV]
- Lieu in [notes]
- Timeline in [notes]
- 10. Skip in [notes]
- Fusion potagère in [Fondation SCP]
- RP —  Guide création de personnage in [Guide]
- RP —  Guide Fiche in [Guide]
- Astria Ascending in [notes]
- Bioshock in [notes]
- Bravely Default II in [notes]
- Code Vein in [notes]
- Control in [notes]
- Disco Elysium in [notes]
- DKS3 in [notes]
- Fatal Frame in [notes]
- FFXIV   Endwalker in [notes]
- God Eater 3 in [notes]
- JV in [notes]
- Mass Effect Legendary in [notes]
- MHRise in [notes]
- Neo - The World Ends With You in [notes]
- Nier in [notes]
- Nioh2 in [notes]
- No more heroes 3 in [notes]
- No more heroes in [notes]
- Omori in [notes]
- Persona 5 Striker in [notes]
- Persona 5 in [notes]
- Shin Megami Tensei V in [notes]
- Tales Of Berseria in [notes]
- Tales of Zestiria in [notes]
- The Great Ace Attorney Chronicles in [notes]
- The World Ends With You in [notes]
- Divinity Original Sin 2 in [notes]
- Elden Ring in [notes]
- Demon slayer in [notes]
- Green Mechanics in [notes]
- Kimetsu No Yaiba in [notes]
- Livre SW in [notes]
- Livre in [notes]
- Log Horizon in [notes]
- Fate   Stay Night in [notes]
- Série in [notes]
- Contacts in [notes]
- Picrew in [notes]
- A. Lepape in [notes]
- A. Savey in [notes]
- A.S Ronnaux-Baron in [notes]
- B. Charbotel in [notes]
- C. Chapuis in [notes]
- C. Dananché in [notes]
- C. Lasset in [notes]
- Catherine Stamm in [notes]
- Christelle Elias in [notes]
- Contacts in [notes]
- D. Bicout in [notes]
- D. Hilliquin in [notes]
- D. Narbey in [notes]
- F. Sahajian in [notes]
- Florence Ayral in [notes]
- J. Cappelle in [notes]
- J.P. Rasigade in [notes]
- K. Chalvet-Monfray in [notes]
- L. Augey in [notes]
- Lucile Boyer in [notes]
- Marc Moulaire in [notes]
- N. Lonca in [notes]
- O. Brun in [notes]
- P. Cassier in [notes]
- P. Jalade in [notes]
- Pauline Occelli in [notes]
- PR P. Michel in [notes]
- S. Gerbier-Colomban in [notes]
- Sophie Dussart in [notes]
- Sophie Gardes in [notes]
- V. Riviere in [notes]
- Vincent Piriou in [notes]
- 2022-01-26 in [notes]
- delete in [notes]

---
## [Mara-Li/Seed_publish](https://github.com/Mara-Li/Seed_publish)@[44aa7fb64a...](https://github.com/Mara-Li/Seed_publish/commit/44aa7fb64a70a77da8d0525513546446ff2f6027)
#### Sunday 2022-01-30 18:08:27 by Mara

**Updated** :

- Note temporaire from [notes]
- Ref snippet from [notes]
- machin from [docs]
- Course from [notes]
- Dépense from [notes]
- Mods list from [notes]
- 10. Master from [notes]
- index from [Modèle Linéaire]
- 2014 from [notes]
- 2017 from [notes]
- 2019 from [notes]
- 2021 from [notes]
- 2015 from [notes]
- 2020 from [notes]
- Prévention et contrôle des infections liées aux soins from [notes]
- ◉ Étude flash de prévalence from [Méthodologie]
- ◉ Incidence - Prévalence from [Toutes]
- ◉ Ratio standardisé d'incidence from [Méthodologie]
- ☣️Analyse des modes de défaillance de leurs effets et de leur criticité from [Gestion des risques]
- ☣️Analyse des risque a priori from [Gestion des risques]
- ☣️Introduction à la gestion des risques from [Gestion des risques]
- ☣️La culture de sécurité de soin from [Gestion des risques]
- ☣️Méthode ALARM from [Gestion des risques]
- ☣️Méthode d'évaluation et d'améliorations des pratiques professionnels from [Gestion des risques]
- ☣️Risques médicamenteux from [Gestion des risques]
- 👏Organisation & pilotage SP from [Memento]
- 🛂Aspergillose pulmonaire invasive from [Gestion des risques]
- 🛂Audit et infections nosocomiales from [Gestion des risques]
- 🛂Infections liées aux cathéters from [Gestion des risques]
- 🛂Infections nosocomiales pulmonaires from [Gestion des risques]
- 🛂Infections urinaires from [Gestion des risques]
- 🛂Introduction aux IAS from [Gestion des risques]
- 🛂Microbiologie from [Gestion des risques]
- 🛂Surveillance épidémiologique from [Gestion des risques]
- 🛂Surveillance microbiologiques from [Gestion des risques]
- 🦀Epidémiologie des cancers du poumon - Cancer et tabac from [Épidémiologie]
- 🦀Epidémiologie du mélanome from [Épidémiologie]
- 🦀Épidémiologie du cancer du sein from [notes]
- 🦀Infections & Cancer from [Épidémiologie]
- 🦀La surveillance du cancer dans le monde from [Épidémiologie]
- 🦀Les cancers professionnels from [Épidémiologie]
- 🦀Nutrition & cancer from [Épidémiologie]
- 🦀Prévention des cancers from [Épidémiologie]
- 🦀Surveillance du cancer en France from [Épidémiologie]
- 🦠Épidémiologie des hépatites from [Épidémiologie]
- 🦠Introduction aux zoonoses from [Épidémiologie]
- 🦠Les méningites bactériennes from [Épidémiologie]
- 🦠Maladie sexuellement transmissibles from [Épidémiologie]
- 🦠Maladies infectieuses émergentes from [Épidémiologie]
- 🦠Paludisme from [Épidémiologie]
- 🦠Tuberculose from [Épidémiologie]
- 🦠VIH — Sida from [Épidémiologie]
- 🦺Identitovigilance from [Gestion des risques]
- 🦺Matériovigilance from [Gestion des risques]
- 🦺Pharmacovigilance et alertes sanitaires from [Gestion des risques]
- 🦺Surveillance du sang from [Gestion des risques]
- 🧰 Étude cas-témoin from [Épidémiologie]
- 🧰Échantillonnage et plans de sondages from [Épidémiologie]
- 🧰Étude écologique from [Épidémiologie]
- 🧰Étude transversale from [Épidémiologie]
- 🧰Pathologie transmissible et chronique from [Épidémiologie]
- 🧰Série de cas from [notes]
- 🩹 Toxoplasmose from [notes]
- Formules from [notes]
- Incidence & prévalence $ from [Épidémiologie]
- Mortalité $ from [Épidémiologie]
- OR & RR $ from [Épidémiologie]
- Article works from [Anglais]
- Ebola from [Anglais]
- Analyse des risque a priori from [notes]
- Base réglementaire de sécurité sanitaire from [Gestion des risques]
- Introduction à la gestion des risques from [Gestion des risques]
- La certification des établissements sanitaires from [Gestion des risques]
- La culture de sécurité de soin from [Gestion des risques]
- La médecine de catastrophe et situations exceptionnelles from [Gestion des risques]
- M2-17. Gestion des risques from [notes]
- Méthode ALARM from [Gestion des risques]
- Méthode d'évaluation et d'améliorations des pratiques professionnels from [Gestion des risques]
- Organisation de la gestion des risques aux niveaux national, régional et local from [Gestion des risques]
- Organisation législative des risques sanitaires en France from [notes]
- Risques médicamenteux from [Gestion des risques]
- Erreur de mesure from [Épidémiologie]
- Etude cas-témoin — Pathologie transmissible from [Épidémiologie]
- Échantillonnage et plans de sondages from [Épidémiologie]
- Étude de cohorte from [Épidémiologie]
- Étude écologique from [Épidémiologie]
- Étude transversale from [Épidémiologie]
- Introduction à l'anthropologie des soins et de la santé from [Épidémiologie]
- Introduction à l'épidémiologie from [Épidémiologie]
- M2-18. Méthode en épidémiologie from [notes]
- Pathologie transmissible et chroniques from [Épidémiologie]
- Série de cas from [Épidémiologie]
- Lecture critique d'article — Cas témoins from [Épidémiologie]
- TD — Etude cas témoin dans les maladies chroniques from [Épidémiologie]
- TD — Etude de deux cohortes from [Épidémiologie]
- Anova à un facteur from [notes]
- M2-2. Modèle Linéaire from [notes]
- Régression linéaire et corrélation from [Mathématiques]
- Check-list de l'organisation du bloc opératoire from [notes]
- Etablissement de santé et développement durable from [Gestion des risques]
- Gestion des déchets et effluents à risques hospitaliers from [Gestion des risques]
- Identitovigilance from [Gestion des risques]
- M2-21. Qualité et sécurité des produits de santé from [notes]
- Matériovigilance from [Gestion des risques]
- Pharmacovigilance et alertes sanitaires from [Gestion des risques]
- Radiologie et risque from [Gestion des risques]
- Responsabilité médicale en établissement de santé from [Gestion des risques]
- Surveillance du sang from [Gestion des risques]
- Aspergillose pulmonaire invasive from [Gestion des risques]
- Audit et infections nosocomiales from [Gestion des risques]
- Covid-19 from [Épidémiologie]
- Infections liées aux cathéters from [Gestion des risques]
- Infections nosocomiales pulmonaires from [Gestion des risques]
- Infections urinaire from [Gestion des risques]
- Introduction aux IAS from [Gestion des risques]
- Investigation d'une épidémie d'infections associées aux soins from [Épidémiologie]
- Les infections de site opératoire (ISO) from [Gestion des risques]
- M2-22. Prévention et contrôle associés aux soins from [notes]
- Médecine du personnel et infections nosocomiales from [Gestion des risques]
- Microbiologie from [Épidémiologie]
- Prévention de la transmission croisée from [Infections liées aux soins]
- Stérilisation from [notes]
- Surveillance épidémiologique from [Gestion des risques]
- Surveillance microbiologiques from [Infection liée aux soins]
- Dépistage organisé des cancers en région AURA from [Épidémiologie]
- Epidémiologie des cancers du poumon - Cancer et tabac from [Épidémiologie]
- Epidémiologie du mélanome from [Épidémiologie]
- Épidémiologie du cancer du sein from [Épidémiologie]
- Facteur de risques de cancer from [Épidémiologie]
- Infections & cancer from [Épidémiologie, Épidémiologie-cancers]
- La surveillance du cancer dans le monde from [Épidémiologie]
- Les cancers professionnels from [notes]
- M2-23. Épidémiologie des cancers from [notes]
- Nutrition & cancer from [Épidémiologie]
- Prévention des cancers from [Épidémiologie]
- Surveillance du cancer en France from [Épidémiologie]
- Taux de mortalité from [notes]
- ❌ Epidémiologie des prédispositions héréditaires from [notes]
- ❌ Epidémiologie génétique from [Épidémiologie]
- ❌Base clinique du cancer from [Épidémiologie]
- ❌Carcinogenèse et biologie du cancer from [Épidémiologie]
- 2014-2015 from [notes]
- Analyses spatiales from [Épidémiologie]
- Concept de réservoir et introduction aux modèles SIR from [Épidémiologie]
- Émergence de zoonose et facteurs favorisant from [Épidémiologie]
- Les zoonoses parasitaires from [Gestion des risques, One-Health]
- M2-25. One-Health from [notes]
- Modèles dynamiques en épidémiologie from [Épidémiologie]
- Oral - Reptiles et zoonoses from [Gestion des risques]
- Epidémiologie vétérinaire from [Épidémiologie]
- Épidémiologie des hépatites from [Épidémiologie]
- Épidémiologie générale des maladies virales from [Épidémiologie]
- Introduction aux zoonoses from [Épidémiologie]
- Les méningites bactériennes from [Épidémiologie]
- Les vaccins obligatoires from [None]
- M2-24. Épidémiologie des maladies infectieuses from [notes]
- Maladie sexuellement transmissibles from [Épidémiologie]
- Maladies infectieuses émergentes from [Épidémiologie]
- Paludisme from [Épidémiologie]
- Principale bactéries infectieuses from [Épidémiologie]
- Tuberculose from [notes]
- VIH — Sida from [Épidémiologie]
- Biais from [Memento]
- Effets indésirables from [Memento]
- Épidémiologie from [Memento]
- Étude cas témoin 🗒️ from [Memento]
- Étude de cohorte from [Mémento]
- Incidence from [Méthodologie]
- Odds-Ratio from [Memento]
- Prévalence from [Méthodologie]
- Prévention from [Memento]
- Risque relatif from [Memento]
- Signalement from [Memento]
- Surveillance from [Méthodologie]
- Vigilance from [Memento]
- 20. Roleplay from [notes]
- Symbole relations from [False]
- Écho from [notes]
- Salem from [Fiche RP]
- Zéphyr from [Fiche RP]
- Invocation d'armes from [notes]
- Nécromancie from [Pouvoirs]
- Pixellisation from [None]
- Pouvoirs from [notes]
- Sortilège from [notes]
- Spiritisme from [notes]
- Éden from [notes]
- Personnage from [notes]
- 22. Personnages from [Fiche RP]
- Ether Blake from [notes]
- Jake O'Connor from [Fiche RP]
- Alwyn Kallendris from [Fiche RP]
- × Illustration × (Ashling) from [Illustration]
- Eilwellyn Beausang from [notes]
- Obsius from [notes]
- × Illustration × from [notes]
- Lagendia from [notes]
- Obsius from [Légendia]
- Relations from [notes]
- 24. FFXIV from [notes]
- Kara Grimalkin from [FFXIV]
- Lieu from [notes]
- Timeline from [notes]
- 10. Skip from [notes]
- Fusion potagère from [Fondation SCP]
- RP —  Guide création de personnage from [Guide]
- RP —  Guide Fiche from [Guide]
- Astria Ascending from [notes]
- Bioshock from [notes]
- Bravely Default II from [notes]
- Code Vein from [notes]
- Control from [notes]
- Disco Elysium from [notes]
- DKS3 from [notes]
- Fatal Frame from [notes]
- FFXIV   Endwalker from [notes]
- God Eater 3 from [notes]
- Mass Effect Legendary from [notes]
- MHRise from [notes]
- Neo - The World Ends With You from [notes]
- Nier from [notes]
- Nioh2 from [notes]
- No more heroes 3 from [notes]
- No more heroes from [notes]
- Omori from [notes]
- Persona 5 Striker from [notes]
- Persona 5 from [notes]
- Shin Megami Tensei V from [notes]
- Tales Of Berseria from [notes]
- Tales of Zestiria from [notes]
- The Great Ace Attorney Chronicles from [notes]
- The World Ends With You from [notes]
- Divinity Original Sin 2 from [notes]
- Elden Ring from [notes]
- Demon slayer from [notes]
- Green Mechanics from [notes]
- Kimetsu No Yaiba from [notes]
- Livre SW from [notes]
- Log Horizon from [notes]
- Fate   Stay Night from [notes]
- Contacts from [notes]
- Picrew from [notes]
- A. Lepape from [notes]
- A. Savey from [notes]
- A.S Ronnaux-Baron from [notes]
- B. Charbotel from [notes]
- C. Chapuis from [notes]
- C. Dananché from [notes]
- C. Lasset from [notes]
- Catherine Stamm from [notes]
- Christelle Elias from [notes]
- D. Bicout from [notes]
- D. Hilliquin from [notes]
- D. Narbey from [notes]
- F. Sahajian from [notes]
- Florence Ayral from [notes]
- J. Cappelle from [notes]
- J.P. Rasigade from [notes]
- K. Chalvet-Monfray from [notes]
- L. Augey from [notes]
- Lucile Boyer from [notes]
- Marc Moulaire from [notes]
- N. Lonca from [notes]
- O. Brun from [notes]
- P. Cassier from [notes]
- P. Jalade from [notes]
- Pauline Occelli from [notes]
- PR P. Michel from [notes]
- S. Gerbier-Colomban from [notes]
- Sophie Dussart from [notes]
- Sophie Gardes from [notes]
- V. Riviere from [notes]
- Vincent Piriou from [notes]
- 2022-01-26 from [notes]
- delete from [notes]

---
## [enthusiastic2003/android_device_lenovo_tb-common](https://github.com/enthusiastic2003/android_device_lenovo_tb-common)@[0ecf0f6b29...](https://github.com/enthusiastic2003/android_device_lenovo_tb-common/commit/0ecf0f6b29fa8641213b62b2914c58f731e486d4)
#### Sunday 2022-01-30 18:20:52 by Sirjan Hansda

Merge branch 'lineage-16.0-msm8937' of https://github.com/enthusiastic2003/android_device_lenovo_tb-common into lineage-16.0-msm8937
yeah, fuck you

---
## [Sebbe9123/Skyrat-tg](https://github.com/Sebbe9123/Skyrat-tg)@[9df563cb76...](https://github.com/Sebbe9123/Skyrat-tg/commit/9df563cb768733fcecc97599d8815498bfd60346)
#### Sunday 2022-01-30 18:33:24 by SkyratBot

[MIRROR] Dullahan Partial Refactor: They Work Again Edition [MDB IGNORE] (#10491)

* Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

* Dullahan Partial Refactor: They Work Again Edition

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [sylvestre/gecko-dev](https://github.com/sylvestre/gecko-dev)@[4ac84fa922...](https://github.com/sylvestre/gecko-dev/commit/4ac84fa92276bcdde86c6fb22773b2784933674a)
#### Sunday 2022-01-30 18:43:20 by Emilio Cobos Álvarez

Bug 1749174 - Enable wayland on supported environments by default on Nightly / Early Beta. r=stransky,jrmuizel,aosmond

There are pros and cons of doing this. Pros are:

 * Both Fedora and Ubuntu ship this by default. I haven't run the
   numbers but my guess is that with those two distros the amount of
   users on Wayland will probably be greater than the amount of users on
   XWayland.

 * Wayland touchscreen support, and a bunch of other features that
   XWayland doesn't have (I'm probably missing a bunch).

Cons that come to mind are:

 * The main one is that we're still testing X11 on automation, though it
   is my understanding that Martin has Wayland tests running on the
   Fedora automation. I'd understand if we'd want to defer this until we
   have Wayland tests running on the Mozilla automation (bug 1725245),
   though arguably that hasn't stopped us from shipping X11+EGL (though
   arguably a smaller change, too).

 * I think the other annoyance of Wayland is the lack of proper PiP
   support (bug 1621261): Right now users need to right-click on the PiP
   Window.

There (most likely) will be others pros and cons (and if we can't come
up with others this patch should allow us to gather more feedback in
Nightly / early-beta). Thoughts?

Differential Revision: https://phabricator.services.mozilla.com/D135456

---
## [NateChoe1/swebs](https://github.com/NateChoe1/swebs)@[e05896356f...](https://github.com/NateChoe1/swebs/commit/e05896356f15f0df2a0931e01e7cdf640246c37d)
#### Sunday 2022-01-30 18:43:51 by Nate Choe

Made sockets nonblocking (I'm a fool who didn't do this and spent several hours trying to figure out why I couldn't handle a second request if firefox was on the page I'm so dumb I hate myself I hate coding I hate the internet computers were a mistake)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f98b3929da...](https://github.com/mrakgr/The-Spiral-Language/commit/f98b3929da77d2c669d7160d9026432926e57e43)
#### Sunday 2022-01-30 19:13:20 by Marko Grdinić

"1:15pm. I got up early, took an aspirin and fell back asleep while I was waiting for the ear pain to go down. Rather than getting better the inner ear is starting to feel worse. I think it hurts even more than yesterday. Right now, I'd be crippled without medication. Anyway, I got up an hour ago and have been chilling. Right now, let me have breakfast. After that I'll do the chores. After that I'll try to get some studying done.

Right now I do not have high temperature, but given the state of my ear, I think there will be a second phase to this illness.

Agh. The aspirin is not blocking it properly, it really must be getting worse.

You know what, why don't I write the monthly review today?

1:50pm. Done with breakfast. Let me have another aspirin, the one I had is not enough. The pain pangs are starting to get intense.

2:05pm. Let me do the chores here.

2:40pm. Done with that. Forget the review. Let me study Houdini. I'll do what I can today. Maybe I'll skip this month's PL review.

3:15pm. I've played around with PolyFill. It is quite straightforward. Ok, I got it.

Let me move to the next thing in the radial menu. Let me take a look at PolySplit.

3:40pm. PolySplit is used for loop cuts.

At this point I am really tired of Houdini, learnning it is pretty slow and I can't imagine myself being at ease using it like I would with Blender. I think I'll just learn the basics which I am doing right now, then use it in a limited fashion afterwards to just distribute the points for things like flowers.

I might have been better off trying to figure out how to do this with an add on in Blender.

The next is PolyBridge.

3:45pm. No, it all depends on how much effort you want to put into things. And when have I ever skimped out on effort?

4pm. Let me see if I can find some example for PolyBridge. I got it to work, but there are a zillion options.

https://www.youtube.com/c/IndiePixel3D

https://www.youtube.com/watch?v=xi-zVRdmt18
Houdini - Procedural Modeling Tips! - Finding Bridges

Nothing on PolyBridge. Nevermind that. Let me watch the above out of curiosity.

https://youtu.be/xi-zVRdmt18?t=42

This is interesting. I'd like to know how to do this. It might be worth looking into his other stuff.

https://youtu.be/xi-zVRdmt18?t=159

I'll have to look into these height fields.

https://youtu.be/xi-zVRdmt18?t=446

I'll have to figure out what PolyFrame does.

Let me add the PolyPath to the mix as well.

4:35pm. Forget this for now, let me check out the docs for loft.

4:55pm. The docs have no examples, nor images. Meaning the only way to figure it out is to try playing with it myself. Rails on the other hand has an example. It is pretty interesting.

5pm. Focus me, stop reading Twitter trash.

5:05pm. I really am out of it. Right now it took me 5m to remember what the transform node was. I didn't realize at all that the thing in the radial menu is what I've used a 100 times by now. Sigh. What about the soft transform? That is just transform with a soft falloff. Ok. Soft peak? Similar to peak. And peak translates along the normals. This could be rather useful.

No, actually, what I am thinking point weld should be does not make sense. Fuse already merges points so point weld should be something else. Let me look into it.

> Interactively snaps groups of points to another target point, and merges them.

I guess it does do merging.

I really should figure out what loft does. Let me take a short break first.

After I figure out loft, I'll look into the deform operations. And after that I'll have covered the basics.

5:35pm. Let me resume.

5:45pm. I hate sites like Vimeo that when I log in lose track of where I was.

https://vimeo.com/104612658
PolyPatch and Polyloft in Houdini

Let me watch this.

6:05pm. The way loft works is so strange, I have no idea why it is trying to stitch the opposite ends. At any rate, it is not that important. I do not need to care about it.

Let me take a look at the deform operations.

6:15pm. Ok, enough. I had enough of this. I am at my limit on how much I am willing to study Houdini systematically.

What I am going to do from here on out is actually work on my own projects.

I actually benefited quite a bit from watching that bridge tutorial. I should watch more Houdini tutorials.

6:25pm. There are so many of these nodes in the manual. I haven't bothered comparing, but I'd guess that SOPs are by far the largest in number. So restricting myself just to them won't save me.

I can't imagine how much effort getting familiar with Houdini would take.

https://www.youtube.com/c/IndiePixel3D

This guy is worth keeping in mind.

https://www.sidefx.com/tutorials/

There is a lot of vids here. I should go through them on my off time. But nevermind that now.

https://www.sidefx.com/learn/world-building/

I really should move on to watching some of these.

Let me watch some of the Far Cry 5 vid at the top.

Ok, let me think about it like this. I know that I've already spend 2 weeks studying Houdini, but the fact that I got corona'd can't be helped. Right now I am on a downswing. I should just take it easy here until I recover properly.

There is nothing wrong with spending time like this increasing my familiarity lightly. Even if I cannot go all out and am making slow progress, I am still attaining something. If I can't 8h a day, I'll do 5. If I can't 5 I'll do 3 and so on.

https://vimeo.com/273986776?embedded=true&source=vimeo_logo&owner=1723479
Procedural World Generation of Ubisoft’s Far Cry 5 | Etienne Carrier | Houdini HIVE Utrecht

6:50pm. 9:30. My skills are really so lacking compared to these guys. I have no idea how I would do something like this.

7pm. Let me stop at 16. Time for lunch.

7:15pm. Let me resume. I'll go at it for a bit more.

7:45pm. Let me stop at 32:50. I'll close here for the day. Let me have some fun here."

---
## [not-a-furry/vmstation](https://github.com/not-a-furry/vmstation)@[c7023d2d47...](https://github.com/not-a-furry/vmstation/commit/c7023d2d470e6ddc7973839003f7ce46fba1e347)
#### Sunday 2022-01-30 20:57:55 by not-a-furry

Added regal rats, other changes (PART 1)

-Add 6758480 from /tg/
-Heavily modified version I drafted up
-Added temporary revenant night-vision to ratking & rats so they can see in dark
-Move cheese items into snacks_dairy.dm
-reworded things to sound less cringe and stupid, and more based and redpilled
-no rat cap for rat breeding (this is a terrible idea, but this is /vm/ so you can do whatever the fuck you want. make a huge army of rats!!!!!!)
-pretty much removed every cap on rodents. GO CRAZY! THIS ISN'T /TG/!
-can breed as many mice as you want with cheese:
 -one cheese wedge is one mouse
 -one cheese wheel is five mice
 -royal cheese? find out ic ;)

---
## [DogeyStamp/dwm](https://github.com/DogeyStamp/dwm)@[67d76bdc68...](https://github.com/DogeyStamp/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-01-30 22:43:23 by Chris Down

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

