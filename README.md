## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-03](docs/good-messages/2022/2022-10-03.md)


2,081,023 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,081,023 were push events containing 3,133,990 commit messages that amount to 272,396,889 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[99b8d6b494...](https://github.com/dragomagol/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Monday 2022-10-03 00:23:47 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[91f02f2a6b...](https://github.com/dragomagol/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Monday 2022-10-03 00:23:47 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [Technobug14/mojave-sun-14](https://github.com/Technobug14/mojave-sun-14)@[736422fac8...](https://github.com/Technobug14/mojave-sun-14/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Monday 2022-10-03 00:44:57 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---
## [TheDoctor1138/Traincraft-5](https://github.com/TheDoctor1138/Traincraft-5)@[8ff6a4d2a9...](https://github.com/TheDoctor1138/Traincraft-5/commit/8ff6a4d2a9c11fa5dfd0cfe7dac3852f4cd20a15)
#### Monday 2022-10-03 01:19:10 by TheDoctor1138

Fixes

ironed out some bugs in the diagonal
fixed the speedsign
fixed some recipes
added another buffer
fixed some train stuff
fixed my bloody server because a child decided to grief it like the piece of cock sucking shit they are

---
## [whatawurst/android_kernel_sony_msm8998](https://github.com/whatawurst/android_kernel_sony_msm8998)@[070a9b0538...](https://github.com/whatawurst/android_kernel_sony_msm8998/commit/070a9b0538a1fb65aaad050bd8dcac9759158974)
#### Monday 2022-10-03 01:44:53 by Christian Brauner

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
## [mootowncow/topaz](https://github.com/mootowncow/topaz)@[2cae04eaf3...](https://github.com/mootowncow/topaz/commit/2cae04eaf31e18b881ae798d20df20c1f93a7c5c)
#### Monday 2022-10-03 02:20:25 by Shiyo

BLU adjustments

Cast time reductions:

All breaths 2 seconds
1k neeedles 2 seconds
ice break 1.5 seconds
maelstrom 1.5 seconds
mysterious light 1.5 seconds
light of penance 1.5 seconds
feather tickle 1.5 seconds
blood saber 1.5 seconds
awful eye 1.5 seconds
bomb toss 1 seconds
cursed sphere 1 seconds
blood drain 1 seconds
digest 1 seconds
cold wave 1 seconds
stinking gas 1 seconds
venom shell 1 seconds
voracious ktrunk 1 seconds
blank gaze 1 seconds
geist wall 1 seconds
chaotic eye 1 seconds
sandspray 1 seconds
exuviation 1 seconds
infrasonics 1 seconds
spiral spin 0.5 seconds
seedspray 0.5 seconds
terror touch 0.5 seconds

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[f923f61011...](https://github.com/OliOliOnsiPree/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Monday 2022-10-03 03:58:20 by MMMiracles

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
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[d34fa4c642...](https://github.com/OliOliOnsiPree/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Monday 2022-10-03 04:01:41 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [SSXModding/SSX3LobbyServer](https://github.com/SSXModding/SSX3LobbyServer)@[744c3130c5...](https://github.com/SSXModding/SSX3LobbyServer/commit/744c3130c5d87493ad7760359ec38e7d424481e8)
#### Monday 2022-10-03 04:33:43 by modeco80

god damn it why do i forget the most inane bullshit

---
## [asutherland/mozsearch](https://github.com/asutherland/mozsearch)@[22f911f503...](https://github.com/asutherland/mozsearch/commit/22f911f5035305e6b9d913d6092bd2d5a48e9076)
#### Monday 2022-10-03 04:44:50 by Andrew Sutherland

Bug 1783761 - Switch directory listings to rust from JS

This leaves the JS machinery in place to generate directory listings
(although I removed some dead JS code), commenting out their invocation
in favor of the new rust rendering.

Behaviorally, we see the following changes:
- Our sort changes slightly.  The JS code was using localeCompare and
  although I am very exctied that the "icu" crate has reached 1.0, I
  ended up choosing https://crates.io/crates/lexical-sort and its
  `natural_lexical_cmp` method for sorting.  I hope this will generally
  be an improvement, but some things do change, like we're now sorting
  in a case-insensitive fashion and we'll try and sort numbers
  naturally instead of the normal ASCII robotic way.
  - This was necessitated by the direct codepoint comparison sorting
    "__GENERATED__" between UpperCaseFiles and lowerCaseFiles which
    is super-weird.
  - Note that there actually was a very hard-coded ordering hack for
    __GENERATED__ and files that started with "." in output-dir.js and
    we are not trying to propagate them because I think the natural
    sort order seems sufficiently sane.
- We stop trying to use the source images themselves as their own
  icons for files that look like images.  This was accomplished by
  pointing at the hg server and having the browser fetch the full-size
  image.  The hg server is already slow/overloaded as-is, and for large
  images this seems undesirable, so I've removed it.
  - Note that we were also pointing at the "tip" revision and so this
    would not immediately translate to us supporting directory listings
    for specific revisions.
  - I'm not opposed to adding it back, but it should be ready for
    handling historical revisions.  (Noting that we will need to update
    the existing template for this too; maybe we should add a liquid
    filter to help with the link revision logic.)

In terms of infrastructure:
- We now generate concise and detailed information for directories,
  not just files.  However, the search-files command only returns files
  by default.  Also, although we write out detailed info for the
  directories, we currently will never read it back in because we don't
  have any need for that right now.  But, for example, it might be
  useful for directory image thumbnailing or some other case where we
  want to have rich data that exists exclusively for directory
  listings.

---
## [arundhatighanade22/Heart-Disease-Diagnostic-Analysis-Project](https://github.com/arundhatighanade22/Heart-Disease-Diagnostic-Analysis-Project)@[243ae643f9...](https://github.com/arundhatighanade22/Heart-Disease-Diagnostic-Analysis-Project/commit/243ae643f99cb8237012df178faef9dc4f9daf22)
#### Monday 2022-10-03 05:36:02 by arundhatighanade22

Add files via upload

Objective 🎯
The goal of this project is to analyse the heart disease occurrence, based on a combination of features that describes the heart disease.

Poblem Statement ❓
Health is real wealth in the pandemic time we all realized the brute effects of covid 19 on all irrespective of any status. You are required to analyse this health and medical data for better future preparation.
Domain 🏥
Healthcare

Project Difficulty level 🥇
Advanced

Programming Language 🐍
Python

Tools 🛠
Jupyter Notebook, MS Excel, MS Power BI
Conclusion 💡
-45.87% People suffering from heart disease.

-Elderly Aged Men are more (50 to 60 Years) and Females are more in 55 to 65 Years Category

-Males are more prone to heart disease.

-Elderly Aged People are more prone to heart disease.

-People having asymptomatic chest pain have a higher chance of heart disease.

-High number of cholesterol level in people having heart disease.

-Blood Pressure increases between age of 50 to 60 and somehow continue till 70.

-Cholesterol and maximum heart rate Increasing in the age group of 50 60.

-ST depression mostly increases between the age group of 30 40.

---
## [NekoSam395/funi-translation-pb95](https://github.com/NekoSam395/funi-translation-pb95)@[4d8bc7ae80...](https://github.com/NekoSam395/funi-translation-pb95/commit/4d8bc7ae80a7140c0f6515b16bd5fd6382b3c13f)
#### Monday 2022-10-03 06:26:38 by NekoSam395

Dream momento

It's honestly insane. I know I'm not a part of the fandom as much anymore, but I held Dream so close to my heart these past two years. He saved me in every way a person can be saved. I'm so insanely proud of what he's done to get here. Keep slaying, king!

---
## [GeminiCrafterMan/BNDoom](https://github.com/GeminiCrafterMan/BNDoom)@[5d30e6cbd0...](https://github.com/GeminiCrafterMan/BNDoom/commit/5d30e6cbd0a0693fd91f60427fbee40aa4b33f67)
#### Monday 2022-10-03 06:33:15 by GeminiCrafterMan

dude holy shit the shanghai hit sound is being annoying

---
## [LeCmnGend/android_frameworks_base](https://github.com/LeCmnGend/android_frameworks_base)@[4c419177be...](https://github.com/LeCmnGend/android_frameworks_base/commit/4c419177be634f6a604d339930c1fccdab73438d)
#### Monday 2022-10-03 07:44:30 by ezio84

Hidden gestural bar: fix visual glitches when switching states

hacky way but it works (TODO: find a proper fix in the new year,
i don't have motivation to dig into navbar/keyguard code fuckery now lol)

setting the height to 1px keeps the navbar almost invisible
but fixes the annoying visual glitches when going from screen
off to ambient pulsing or lockscreen (more noticeable on some devices
like bonito)
to replicate the issue without this commit:
- screen ON, then screen off, then double tap to go to ambient,
then double tap to go to lockscreen, then double tap to switch screen off,
then switch screen on again
- or just switch screen off/on a few times with the power button

Also sync the hide pill code with Pulse hide pill feature

Change-Id: Ib1cc83492f8a091be5cac4563d844010cef69dbc
Signed-off-by: Joey Huab <joey@evolution-x.org>
Signed-off-by: Jayant-Deshmukh <jayantdeshmuk008@gmail.com>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[97d1c85670...](https://github.com/Koi-3088/ForkBot.NET/commit/97d1c856704c1c87f102ab512303491675df8085)
#### Monday 2022-10-03 08:08:37 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [niyolynate/py.love](https://github.com/niyolynate/py.love)@[8028ed8161...](https://github.com/niyolynate/py.love/commit/8028ed816148073acdad067cee269087da23b369)
#### Monday 2022-10-03 08:13:38 by niyolynate

Alterations

running...

Hello, world!
My name is Niyo Lynate
I want to keep trying even when its really hard. 
In the beginning it was like a dream. now, i feel so good
can use some help, from you my friend
I am a new bea
Tell me about your best programming language in the commit
The tech world is a big one, i prefer learning piece by piece daily.

---
## [utkarshg6/Node](https://github.com/utkarshg6/Node)@[b0e9bb484e...](https://github.com/utkarshg6/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Monday 2022-10-03 08:47:48 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [JelteF/postgres](https://github.com/JelteF/postgres)@[1c27d16e6e...](https://github.com/JelteF/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Monday 2022-10-03 09:10:09 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [curry684/symfony](https://github.com/curry684/symfony)@[338daf25c9...](https://github.com/curry684/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Monday 2022-10-03 10:43:50 by Nicolas Grekas

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
## [wlkmanist/project.black-guacamole](https://github.com/wlkmanist/project.black-guacamole)@[914c489edb...](https://github.com/wlkmanist/project.black-guacamole/commit/914c489edb632ce420be856254bd065e429178c4)
#### Monday 2022-10-03 11:26:08 by alk3pInjection

drm: Handle dim for udfps

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

---
## [DoxxWactor/ReClassEx](https://github.com/DoxxWactor/ReClassEx)@[e4450bcf86...](https://github.com/DoxxWactor/ReClassEx/commit/e4450bcf8673e3ffa3f05c87b3b1e03b970b6f1d)
#### Monday 2022-10-03 12:13:11 by user1

I added some changes to make the generated classes compile properly without having to be manually reordered.

Summary:

* When the 'generate' button is clicked, each class is added to a Class Dependency Graph, and each class that class references is added as a depenedency.
* There are two dependency types - POINTER and INSTANCE.
    * POINTER references can be solved with a forward declaration.  However, a simple reordering can solve that dependency and limit the forward declaration spam at the top of the generated file.
    * INSTANCE references can only be solved with reordering.  If class B contains an instance of class A, A must come before B in the generated file, no way around it.
* The graph is then recursively traversed - starting at nodes with no dependencies - with classes being added to the 'ordered' class collection.
* Circular dependencies (A points to B points to C points to A) are solved with forward declarations (C comes before B comes before A, with A being forward declared)
* The result is the output has fewer forward declarations and classes don't need to be manually reordered.  In my DayZ Reclass file (which inspired this work, because it takes me a lot of time manually reordering every time I generate the output) there are only 5 forward declarations with 356 classes.

Details:

The graph class itself is pretty simple.  It maintains a mapping of CNodeClass pointers to DependencyNodes.  Each node knows what class it represents, and has two vectors of edges - incoming edges (another class depends on this one) and outgoing edges (this class depends on another).  Each edge knows what node it points to, as well as whether the dependency is of POINTER or INSTANCE type.

Edges are generated by walking each node in a class and adding a dependency edge for each pointer, instance, instance array, and pointer array.  Parallel edges (duplicates) are not added, nor are simple recursive edges (a class has a pointer to an instance of that same class).  Other types (function ptrs?  Can we prototype those in ReClass?) may be necessary here, but these were all I could figure out without asking someone.

ClassDependencyGraph            depGraph;
    // Add each class as a node to the graph before adding dependency edges
    for (auto cNode : this->m_Classes) {
        depGraph.AddNode(cNode);
    }
    for (auto cNode : this->m_Classes) {
        for (size_t n = 0; n < cNode->NodeCount(); n++)
        {
            CNodeBase* pNode = (CNodeBase*)cNode->GetNode(n);
            NodeType Type = pNode->GetType();
            switch (Type) {
            case(nt_pointer):
            {
                CNodePtr* pPointer = (CNodePtr*)pNode;
                CNodeClass* pointerClass = pPointer->GetClass();
                depGraph.AddEdge(cNode, pointerClass, DependencyType::POINTER);
                break;
            }
            case(nt_instance):
            {
                CNodeClassInstance* pClassInstance = (CNodeClassInstance*)pNode;
                CNodeClass* instanceClass = pClassInstance->GetClass();
                depGraph.AddEdge(cNode, instanceClass, DependencyType::INSTANCE);
                break;
            }

            case(nt_array):
            {
                CNodeArray* pArray = (CNodeArray*)pNode;
                CNodeClass* instanceClass = pArray->GetClass();
                depGraph.AddEdge(cNode, instanceClass, DependencyType::INSTANCE);
                break;
            }

            case(nt_ptrarray):
            {
                CNodePtrArray* pArray = (CNodePtrArray*)pNode;
                CNodeClass* pointerClass = pArray->GetClass();
                depGraph.AddEdge(cNode, pointerClass, DependencyType::POINTER);
                break;
            }
            }
        }
    }

Ordering dependencies in the graph is simple in naive cases.  Just start at nodes that have no dependencies (leaf nodes) and recursively visit dependencies, adding them to an ordered class vector as you go.  This works great until you hit circular dependencies - you'd recurse until death.  That's where forward declarations are needed.  If you hit a node that is already being processed, you know you've thrown that ass in a circle.  So that's when you throw your hands up and forward declare - but you can only do that for a POINTER dependency, not an INSTANCE one.

You can see in this graph that DayZPlayer instances Entity which points to physicsObject which points to DayZPlayer.  And if that's the order you hit the nodes in, you're fine - just forward declare DayZPlayer.  However, there exists a path from gpWorld -> World -> N0000120E -> Entity -> PhysicsObject -> DayZPlayer -> Entity.  In that case, when you realize you're in a cycle you're at an INSTANCE dependency and you can't solve it with a forward declaration.

I wasn't sure what the correct way to handle this was, so I kind of improvised a solution.  At the beginning of graph solving, all nodes which have incoming INSTANCE type dependencies are marked.  Then, when they're visited during recursion, if they're being visited across a POINTER dependency edge, they're forward declared and not processed further.  So when you hit gpWorld -> World -> N0000120E -> Entity, it knows Entity has incoming INSTANCE dependencies, so instead of recursing and ending up in DayZPlayer, it adds a forward declaration for Entity and bails out.  Then, later (and along a different path that doesn't go through Entity), DayZPlayer is visited normally and it recurses into Entity, and all is well.

With forward declarations generated and the classes in dependency order, output goes on as normal, except instead of iterating of m_Classes, it iterates over the set of forward declarations and the in-order vector of classes instead.

To generate the visualized graph, I put a ToDot method in the DependencyGraph, which generates a GraphViz Dot representation of the graph.  I left it in as it may end up being useful in troubleshooting in the future.

---
## [kavishinsa/Brigade-Valencia-Electronic-City-Bangalore](https://github.com/kavishinsa/Brigade-Valencia-Electronic-City-Bangalore)@[822a1fd492...](https://github.com/kavishinsa/Brigade-Valencia-Electronic-City-Bangalore/commit/822a1fd492b8b7dd6f44998291496553da269db3)
#### Monday 2022-10-03 12:17:50 by kavishinsa

Brigade Valencia E City Hosur Road - Residential Flats In Bangalore

Situated in Electronic City, Brigade Valencia has premium flats in Electronic City, Hosur Road, Bengaluru by Brigade Group. There are several state-of-the-art conveniences, infrastructure, terraces, and landscaped grounds. There are different apartments for sale in Electronic City, and customers can choose which one fits their requirements.

Brigade Group has catered to all details and relaxations compatible with modern existence. We cater to all members of the family, where loved ones can spend valuable time together. There is something for everyone in our flats for sale in Electronic City: exercise rooms are great for fitness freaks; a sportsperson can enjoy several sports in the outdoor and indoor play zones. Spread across several acres of green land, it has high-rise contemporary communities living with ventilation, green pockets, natural light, and an open area.

Speaking of formations, presently, it offers premium 2 BHK in and 3 BHK in Electronic City as per different family sizes and necessities. Our premium flats in Electronic City have been designed according to modern family lifestyles and contemporary conveniences.

Living in Electronic City, Bangalore

Bengaluru has experienced massive innovation and development in the past time. Bangalore, where Electronic City is situated in a cosmopolitan society, has witnessed immense physical and social development. Though away from the noise and pollution of the main town, it is well-connected to take you where you need to go. At Brigade Valencia E City Bangalore figured out a way to balance both these requirements.

Convenience and conveyance have been our imports from the start, and our premium flats in South Bangalore are close to leading IT firms, and educational and entertainment zones. 

The best thing about buying a residential property in Bengaluru is the connectivity to other zones, cities, states, Hosur Road, Silk Board Junction, and NICE Road Here.

For More Details:
Visit Here: https://bit.ly/3yb5cI9

---
## [hashicorp/terraform-plugin-framework](https://github.com/hashicorp/terraform-plugin-framework)@[1405baa970...](https://github.com/hashicorp/terraform-plugin-framework/commit/1405baa970d7ce250461946d5dbb8f84b65c6220)
#### Monday 2022-10-03 13:58:10 by Brian Flad

types: Deprecate attr.Value type Null, Unknown, and Value fields

Reference: https://github.com/hashicorp/terraform-plugin-framework/issues/447

When the framework type system was originally being developed, the value types were introduced with exported fields which also served as the internal details of whether a value was null, unknown, or a known value of a friendlier Go type. It was known that there was the potential for issues, but the simplified developer experience seemed to outweigh the potential for developer issues. Fast forward a few months, this decision appears to have two consequences that the framework maintainers hear about across various forums.

One issue is that the value types directly expose their internal implementation details and support the three states of a Terraform type value: being null, unknown, or a known value. Only one state should ever be set, but provider developers can make a value that is any combination of those states. This makes the framework behavior potentially indeterminate from the provider developer perspective whether, for example, a null AND unknown value becomes null OR unknown as it works its way through the framework.

```go
In this example, the logic has created an invalid null AND unknown value:

type ThingResourceModel struct{
  Computed types.String `tfsdk:"computed"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  var data ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &data))

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Unknown value: types.String{Null: false, Unknown: true, Value: ""}
    "computed": plan.Computed,
  })

  // Maybe some external API responses here, but showing hardcoded updates for
  // brevity. This will make the value invalid by enabling Null without
  // disabling Unknown.
  data.Computed.Null = true

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Invalid value: types.String{Null: true, Unknown: true, Value: ""}
    "computed": data.Computed,
  })

  // The invalid value will be either null or unknown, depending on the
  // type implementation. If unknown, Terraform will error, since unknown
  // values are never allowed in state.
  resp.Diagnostics.Append(resp.State.Set(ctx, &data))
}
```

Another issue is that the default (zero-value) state for an "unset" value type turns into a known value, which is confusing since these values explicitly support being null. This causes Terraform errors which would surface to practitioners (especially when untested) that provider developers then have to troubleshoot the error message containing Terraform's type system details, potentially discover the reason why it is happening by looking at the framework type source code, then figure out a workable solution. It's not intuitive.

```go
type ThingResourceModel struct{
  // let's assume this is left unconfigured (null in config and plan)
  Optional types.String `tfsdk:"optional"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  // Providers can opt to use a single variable that is updated based on an
  // external response, however that logic can be more difficult sometimes,
  // so it can be easier to split them. Showing the split way to exemplify
  // the "unset" problem.
  var plan, state ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &plan))

  tflog.Trace(ctx, "Plan Values", map[string]any{
    // Null value: types.String{Null: true, Unknown: false, Value: ""}
    "optional": plan.Optional,
  })

  // Maybe some external API responses here, but intentionally not
  // doing any state.Optional setting, which might happen if the
  // external response for that data was null for example.

  tflog.Trace(ctx, "State Values", map[string]any{
    // Zero-value: types.String{Null: false, Unknown: false, Value: ""}
    "optional": state.Optional,
  })

  // The state zero-value will later cause Terraform to error, such as:
  // Error: Provider produced inconsistent result after apply
  // ... expected cty.NullVal(cty.String), got cty.StringVal("")
  // Since the plan value said it would be null.
  resp.Diagnostics.Append(resp.State.Set(ctx, &state))
}
```

This deprecation of the fields in preference of functions and methods aims to unexport the internal details and treat the value types as immutable once they are created. When provider developers switch over to the new model, any errant changes to the deprecated exported fields will have no effect. A future version will remove the exported fields entirely.

---
## [ioccc-src/mkiocccentry](https://github.com/ioccc-src/mkiocccentry)@[9d2f8e9135...](https://github.com/ioccc-src/mkiocccentry/commit/9d2f8e91358bf4d5ab15ecb548aab8ba3e5099c6)
#### Monday 2022-10-03 13:58:24 by Cody Boone Ferguson

Initial (incomplete) locations and pure parser

The first step is the removal of the prefix sorry_. This started out as
a joke between Landon and me, first as ugly_ but changed to sorry_. As
Landon explained:

    Avoided the appearance of attacking any particular individual.  It
    was not our intention to disrespect anyone, even though we disagree
    with some of the technical decisions.  Where we have fundamental
    technical disagreements, we attempted to express those technical
    disagreements with humor in hopefully a more fun way.  As also now
    apologize for how `bison` and `flex` generated code may look, instead
    of simply calling it ugly.  As such, we hopefully improved some of
    the humor in our code while trying to be nice and friendly to others.

He elaborated that:

    FYI: One reason to avoid the appearance of an attack is out of a
    courtesy to Steven Johnson, the original architect of yacc. Brian
    Kernighan credits Steven Johnson with use of his original yacc
    allowing him to quickly produce the awk interpreter. While neither
    is what you would call "humor impaired", out of respect for their
    work we decided to "tone down" language and make it appear to be
    more "fun" and less "caustic".

The reason to remove the prefix is because it causes confusion between
documentation and what is generated i.e. between what is usually
expected and what we actually have. This is important because there are
a number of complications including that the interaction of bison and
flex when it comes to re-entrancy is a proper mess so we need to have
less confusion. Another fun prefix can be added another time once
everything is complete (finishing locations and making it re-entrant
which was also kind of started) should it be desired.

Now as for the changes:

Make bison parser pure. This does not mean it's yet re-entrant but
it's the first step to do so. This was done by adding:

    %define api.pure full

to jparse.y.

Add %locations to jparse.y.

Removed all references of sorry_ and SORRY_ as well as all the
commentary on the prefix.

Changed sorry.tm.ca.h to work with the removal of the prefix but still
be sorry (see the diff if you need to know as this log is already too
long).

Several functions have had a change in prototype. These include
yyerror() which now takes a YYLTYPE *yyltype (currently unused but
provides location information - or will) and yylex() which is now:

    extern int yylex(YYSTYPE *yylval_param, YYLTYPE *yylloc_param);

the YYSTYPE * is our struct json.

These changes do not seem to break any parsing as the jparse_test.sh
script reports no problems (nor does make test or make prep) and running
the parser on a file manually returns the expected results. Even so this
is not complete. I want it in so that Landon can also work on it.

The Makefile did have to change slightly as (because these changes are
not completed) one parameter of a function is not yet used (i.e. a
warning was disabled).

We can say with this commit that the JSON parser is still code complete
but the locations and the re-entrancy is not.

There was a typo fix in jsemtblgen.c as well.

---
## [andercard0/duckstation](https://github.com/andercard0/duckstation)@[ae2241f718...](https://github.com/andercard0/duckstation/commit/ae2241f7186428f63101409f901899345a1fda87)
#### Monday 2022-10-03 14:13:57 by Anderson 0 Cardoso

Update chtDb to the latest

Following games were updated in the Database:

- Spyro 2 - Ripto's Rage
- Medal Of Honor
- Digimon World 3
- Megaman Legends 2
- Star Ocean - The Second Story
- Disney Presents Tigger's Honey Hunt
- Spyro X Sparx - Tondemo Tours
- Resident Evil 1
- Grand Theft Auto
- Castlevania Symphony Of The Night
- Megaman X
- Dino Crisis
- Valkyrie Profile
- MediEvil 2
- Crash Bandicoot - Warped

---
## [asutherland/mozsearch](https://github.com/asutherland/mozsearch)@[c2cb111e4f...](https://github.com/asutherland/mozsearch/commit/c2cb111e4fe63fdd16e676c2d82a878e0996245a)
#### Monday 2022-10-03 15:18:58 by Andrew Sutherland

Bug 1783761 - Switch directory listings to rust from JS

This leaves the JS machinery in place to generate directory listings
(although I removed some dead JS code), commenting out their invocation
in favor of the new rust rendering.

Behaviorally, we see the following changes:
- Our sort changes slightly.  The JS code was using localeCompare and
  although I am very excited that the "icu" crate has reached 1.0, I
  ended up choosing https://crates.io/crates/lexical-sort and its
  `natural_lexical_cmp` method for sorting.  I hope this will generally
  be an improvement, but some things do change, like we're now sorting
  in a case-insensitive fashion and we'll try and sort numbers
  naturally instead of the normal ASCII robotic way.
  - This was necessitated by the direct codepoint comparison sorting
    `__GENERATED__` between UpperCaseFiles and lowerCaseFiles which
    is super-weird.
  - Note that there actually was a very hard-coded ordering hack for
    `__GENERATED__` and files that started with "." in output-dir.js
    and we are not trying to propagate them because I think the natural
    sort order seems sufficiently sane.
- We stop trying to use the source images themselves as their own
  icons for files that look like images.  This was accomplished by
  pointing at the hg server and having the browser fetch the full-size
  image.  The hg server is already slow/overloaded as-is, and for large
  images this seems undesirable, so I've removed it.
  - Note that we were also pointing at the "tip" revision and so this
    would not immediately translate to us supporting directory listings
    for specific revisions.
  - I'm not opposed to adding it back, but it should be ready for
    handling historical revisions.  (Noting that we will need to update
    the existing template for this too; maybe we should add a liquid
    filter to help with the link revision logic.)

In terms of infrastructure:
- We now generate concise and detailed information for directories,
  not just files.  However, the search-files command only returns files
  by default.  Also, although we write out detailed info for the
  directories, we currently will never read it back in because we don't
  have any need for that right now.  But, for example, it might be
  useful for directory image thumbnailing or some other case where we
  want to have rich data that exists exclusively for directory
  listings.

---
## [imeshboy24/VihangaBot-MD-V3-my](https://github.com/imeshboy24/VihangaBot-MD-V3-my)@[407abe91d7...](https://github.com/imeshboy24/VihangaBot-MD-V3-my/commit/407abe91d7f658ea23e06388c5a1b08148a56da4)
#### Monday 2022-10-03 16:36:25 by imesh boy

["Ha","ha","Na","NA","na","NA NA","na na","Hmm","kauda oya","Kauda oya","KAUDA OYA","KAUDA ME","Kauda me","kauda me","you girl","Your boy gril","gn","GN","script","Script","SCRIPT","i love you","hum","hii","hiii","hello","Hello","ALIVE","alive","Alive","Bye","BYE","GM","Gm","Gn","Gn kollo","Good morning","Good night","HI","HMM","hm","Hi","Hm","OWNER","owner","Owner","menu","I love you","IMESH","Imesh","MK","Mk","bay","bye","gm","haraka","hello","mk","kohomada","hmm","Hhmm","හම්","හ්ම්","හ්ම්ම්","හයි","හ්ම්ම්","hi","OWNER 🎩","MENU 📝","bot","Script 😼","Bot","BOT","adarei","adarey","akke","alive","baba eka","baduwa","balaganin","balagena","balli","bb ek","bich","bitch","bye","denawada","en nane","Enne nane","ep wel","epa wela","esawa","fuck","gahanawa","gahano","gm","gn","good morning","good night","gothaya","guti","ha ha","hako","hello","helo","hey","hmm","hukanna","hukanni","hum","huththa","huththi","hy","i love you","kariya","kellekda","kohomada","kohomd","ponni","ponni","ponnaya","pinnaya","paraya","pala","pakaya","natanna","natahan","namgi","namasthe","namaskaram","nah","na na","mokek","mk","marilada","love","Sapak","seen","u girl","Uddika","umma","ummah","ummma","vesavi","vesawi","vesi","wesi","Why ban","Y ban","Y bn","you girl","zzaaa","zzaab","zzaac","zzaad","zzaae","zzaaf","zzaag","zzaah","zzaai","zzaaj","zzaak","zzaal","zzaam"]

---
## [stratospher/bitcoin](https://github.com/stratospher/bitcoin)@[3a7e0a210c...](https://github.com/stratospher/bitcoin/commit/3a7e0a210c86e3c1750c7e04e3d1d689cf92ddaa)
#### Monday 2022-10-03 17:02:26 by glozow

Merge bitcoin/bitcoin#24513: CChainState -> Chainstate

00eeb31c7660e2c28f189f77a6905dee946ef408 scripted-diff: rename CChainState -> Chainstate (James O'Beirne)

Pull request description:

  Alright alright alright, I know: we hate refactors. We especially hate cosmetic refactors.

  Nobody knows better than I that changing broad swaths of code out from under our already-abused collaborators, only to send a cascade of rebase bankruptcies, is annoying at best and sadistic at worst. And for a rename! The indignation!

  But just for a second, imagine yourself. Programming `bitcoin/bitcoin`, on a sandy beach beneath a lapis lazuli sky. You go to type the name of what is probably the most commonly used data structure in the codebase, and you *only hit shift once*.

  What could you do in such a world? You could do anything. [The only limit is yourself.](https://zombo.com/)

  ---

  So maybe you like the idea of this patch but really don't want to deal with rebasing. You're in luck!

  Here're the commands that will bail you out of rebase bankruptcy:

  ```sh
  git rebase -i $(git merge-base HEAD master) \
    -x 'sed -i "s/CChainState/Chainstate/g" $(git ls-files | grep -E ".*\.(py|cpp|h)$") && git commit --amend --no-edit'
  # <commit changed?>
  git add -u && git rebase --continue
  ```

  ---

  ~~Anyway I'm not sure how serious I am about this, but I figured it was worth proposing.~~ I have decided I am very serious about this.

  Maybe we can have nice things every once in a while?

ACKs for top commit:
  MarcoFalke:
    cr ACK 00eeb31c7660e2c28f189f77a6905dee946ef408
  hebasto:
    ACK 00eeb31c7660e2c28f189f77a6905dee946ef408
  glozow:
    ACK 00eeb31c7660e2c28f189f77a6905dee946ef408, thanks for being the one to propose this
  w0xlt:
    ACK https://github.com/bitcoin/bitcoin/pull/24513/commits/00eeb31c7660e2c28f189f77a6905dee946ef408

Tree-SHA512: b828a99780614a9b74f7a9c347ce0687de6f8d75232840f5ffc26e02bbb25a3b1f5f9deabbe44f82ada01459586ee8452a3ee2da05d1b3c48558c8df6f49e1b1

---
## [oisinod/WoWAnalyzer](https://github.com/oisinod/WoWAnalyzer)@[90c1dd8db4...](https://github.com/oisinod/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Monday 2022-10-03 18:23:42 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [FlorentRevest/linux](https://github.com/FlorentRevest/linux)@[a06a4dc3a0...](https://github.com/FlorentRevest/linux/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Monday 2022-10-03 18:56:39 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [rosenkoenig/LD51](https://github.com/rosenkoenig/LD51)@[5ee34f3cc3...](https://github.com/rosenkoenig/LD51/commit/5ee34f3cc3ef2c5384df2974e2350cdfe00cf535)
#### Monday 2022-10-03 19:23:25 by KKparterre

shooter enemy has a laser to show it's gonna fuck you up

---
## [Teksura/chummer5a](https://github.com/Teksura/chummer5a)@[85dc0f8354...](https://github.com/Teksura/chummer5a/commit/85dc0f8354083947e63cb021d7b20d7a88af6dbc)
#### Monday 2022-10-03 19:41:09 by Teksura

Toxic and mutant critters (#4899)

* Adding Kokoro Cobra

I mean it mostly works. I feel it's kinda bullshit that the natural weapon doesn't work but that's a later problem

* Update critters.xml

fuck

* Update critters.xml

Adds Pandamonium and Montauk

* Update critters.xml

Added the last of the Critters

* Delete .DS_Store

This file should have been ignored

---
## [shangril/crero](https://github.com/shangril/crero)@[b4ee99e08b...](https://github.com/shangril/crero/commit/b4ee99e08b30a8b41ee9e807dfc9de3e29346f63)
#### Monday 2022-10-03 19:55:14 by Nico

CRITICAL security fix affecting and prior version-RCE

Now material things can be re-enabled
For material_releases_order_history.php specifiall:
Also FIX for misconfigured (non-.htaccess) hosts ! You've been warned enough, .htaccess MUST work. On misconfigured host code injection was possible. Now even on misconfigured host it won't execute FOR THIS PART. Code injection is still possible on some other parts of misconfigured host (fan network (aka chatroom), if enabled). Honor .htaccess. Read the README.
Also FIX that damn double encoding problem for album names. Please not that it will cause troubles if either a Material Product Name, or a Material Option, contains an html entity in its clear name. Which is uncommon case.

---
## [adrianchifor/lighthouse](https://github.com/adrianchifor/lighthouse)@[66eca1a882...](https://github.com/adrianchifor/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Monday 2022-10-03 20:39:33 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [Luis-Betancourt93/Code-Wars](https://github.com/Luis-Betancourt93/Code-Wars)@[df625e6811...](https://github.com/Luis-Betancourt93/Code-Wars/commit/df625e6811a9396edcfeef68bc617aa3680ae09a)
#### Monday 2022-10-03 20:48:42 by Luis-Betancourt93

I love you, a little, a lot, passionatly

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

---
## [patent122/Dante_2_Semestr_Lato_2022](https://github.com/patent122/Dante_2_Semestr_Lato_2022)@[7398f2d1e5...](https://github.com/patent122/Dante_2_Semestr_Lato_2022/commit/7398f2d1e5081a37197d554bac9e696a2a3974d1)
#### Monday 2022-10-03 20:59:19 by Patryk Panek

Zadanie 6.18 Podział na zdania i słowa - ALERT

Napisz program, który pobierze od użytkownika tekst, podzieli go na zdania i wyświetli posortowane rosnąco ze względu na liczby słów w tych zdaniach. Zdania mają być wyświetlone w oddzielnych liniach, ze słowami posortowanymi alfabetycznie, ze względu na wynik funkcji strcmp.

Przykład:

Enter text: "In theory, theory and practice are the same. In practice, they're not." - Yoggi Berra⏎
In not practice re they⏎
In and are practice same the theory theory⏎
W tym celu przygotuj następujące funkcje:

int split_sentences(const char *text, char ****output);
int sort_sentences(char ***output);
void destroy(char ***words);
int split_sentences(const char *text, char ****output);
Funkcja dzieli tekst text na zdania. Zdanie kończy się kropką. Ponadto każde zdanie dzieli na wyrazy. Wyraz to ciąg następujących po sobie liter.

Przykłady:

dwa zdania (Ala oraz Ma): Ala .Ma. Kota
jedno zdanie (kota): kota.
brak zdań: ala ma kota
dwa puste zdania: ..
Koniec tablic zdań oraz wyrazów funkcja ma oznaczyć wartością NULL. Poszczególne wyrazy, jako że są tekstami, kończą się terminatorem '\\x0'

Funkcja może zaalokować dokładnie tyle pamięci, ile będzie potrzebne na przechowanie całej tablicy. Wynik działania funkcji split_sentences ma zostać napisany pod wskaźnik *output. Jeżeli funkcja ma zakończyć się porażką, to powinna ustawić NULL podwskaźnikiem *output* i zwrócić niezerowy kod błędu.

Wartość zwracana:

1 - w przypadku przekazania do funkcji błędnych danych,
2 - w przypadku braku zdań w tekście text,
3 - w przypadku braku pamięci,
0 - w przypadku sukcesu (*output zawiera poprawny wskaźnik).
Interpretacja parametru char ****output:

Poziom znaku - typ char reprezentuje pojedynczy znak.
Poziom słowa - typ wskaźnikowy char* reprezentuje wskaźnik na znak, który w tym przypadku należy interpretować jako wskaźnik na słowo (wskaźnik na pierwszy znak słowa, słowo jest tekstem w języku C i kończy się terminatorem \x0).
Poziom zdania - typ wskaźnikowy char** jest wskaźnikiem na pamięć przechowującą wskaźnik na słowo. W tym przypadku należy interpretować go jako wskaźnik na pamięć przechowującą sekwencję wielu wskaźników na słowa; sam wskaźnik char** wskazuje tylko na pierwsze słowo (wskaźnik do niego). Sekwencja musi kończyć się terminatorem NULL. Zatem zdanie posiadające 5 słów będzie reprezentowane przez sekwencję 6 elementów (ostatni to NULL).
Poziom tekstu - typ wskaźnikowy char***, analogicznie do poprzedniego przykładu, wskazuje na sekwencję wskaźników na zadania. Zatem można go interpretować jako wskaźnik na cały treść/dokument (czyli zbiór zdań). Sekwencja kończy się terminatorem NULL.
Poziom zmiennej przechowującej wskaźnik na treść - typ wskaźnikowy char*** ponownie opisuje wskaźnik do pamięci przechowującej wskaźnik, itd. W tym przypadku należy go interpretować jako adres zmiennej typu char*** w której umieszczony ma być adres pierwszego zdania tekstu wejściowego.
Zatem jeśli przyjmiemy, że zmienna char**** p zawiera poprawny wskaźnik z poprawnie przydzielonymi pamięciami, to odpowiednio:

*p - Adres całej treści podzielonej na zdania i słowa. Typ tego wyrażenia to char***
*(*p + 1) - Adres drugiego zdania w tekście *p (pierwsze ma indeks 0). Typ tego wyrażenia to char**
*(*(*p + 2) + 4) - Piąte słowo z trzeciego tekstu. Typ tego wyrażenia to char*.
*(*(*(*p + 1) + 6) + 8) - Dziewiąty znak z siódmego słowa znajdującego się w drugim wierszu. Typ tego wyrażenia to char.
Natomiast wyrażenie *(p + 1) jest niepoprawne, ponieważ p jest adresem jednej zmiennej (jednego elementu wskaźnikowego). Za tym elementem nie ma nic, co dało by się zinterpretować w kontekście treści/zdań/słów.
int sort_sentences(char ***output);
Funkcja sortuje zdania w output rosnąco pod kątem liczby wyrazów w nich występujących. Ponadto w każdym zdaniu wyrazy należy posortować alfabetycznie od A do Z, przy czym duże litery mają wyższy priorytet, pomimo mniejszej wartości ich kodów tabeli ASCII. Sortowanie należy realizować w miejscu.

Koniec słów w tablicy (zdaniu) jest oznaczony wartością NULL. Koniec zdań w tablicy (output) jest oznaczony wartością NULL.

Wartość zwracana:

1 - w przypadku błędnych danych wejściowych lub
0 w przypadku powodzenia.
void destroy(char ***words);
Funkcja zwalnia pamięć przydzieloną zarówno na tablicę words, jak i poszczególne wyrazy.

Napisz program, który pobierze od użytkownika tekst (nie więcej niż 999 znaków), podzieli go na zdania, każde zdanie podzieli na wyrazy a następnie posortuje zdania rosnąco pod względem liczby wyrazów, a wyrazy w poszczególnych zdaniach alfabetycznie.

Program ma wyświetlić, w oddzielnej linii dla każdego zdania, wyrazy posortowane alfabetycznie począwszy od zdania z najmniejszą liczbą wyrazów.

W przypadku, kiedy nie uda się przydzielić pamięci program powinien wyświetlić komunikat Failed to allocate memory i niezwłocznie zakończyć działanie z kodem błędu 8,
W przypadku kiedy nie będzie żadnych zdań w tekście podanym przez użytkownika program powinien wyświetlić komunikat Nothing to show.
Jeżeli w którymś ze zdań nie będzie wyrazów, program w jego miejsce powinien wyświetlić komunikat Nothing to show i kontynuować.
Przykładowa interakcja z programem -- sukces:

Enter text: The.trouble⏎
The⏎
Enter text: Programming is not a zero-sum game. Teaching something to a fellow programmer doesn't take it away from you. I'm happy to share what I can, because I'm in it for the love of programming. - John Carmack⏎
Programming a game is not sum zero⏎
Teaching a away doesn fellow from it programmer something t take to you⏎
I I I because can for happy in it love m m of programming share the to what⏎
Enter text: Truth can only be found in one place: the code. - Robert C. Martin."The Answer to the Great Question... Of Life, the Universe and Everything.. Is.. Forty-two,' said Deep Thought, with infinite majesty and calm." - Douglas Adams, The Hitchhiker's Guide to the Galaxy.The computer programmer is a creator of universes for which he alone is the lawgiver. The art challenges the technology, and the technology inspires the art.-John Lasseter.Technology presumes there's just one right way to do things and there never is.-Robert M. Pirsig.What you do makes a difference, and you have to decide what kind of difference you want to make. - Jane Goodall. "A clear vision, backed by definite plans, gives you a tremendous feeling of confidence and personal power." - Brian Tracy.We are all in the gutter, but some of us are looking at the stars. - Oscar Wilde.The unexamined life is not worth living. - Socrates.All this modern technology just makes people try to do everything at once.-Bill Watterson.At forty, I was too old to work as a programmer myself anymore; writing code is a young person's job. - Michael Crichton."The use of COBOL cripples the mind; its teaching should therefore be regarded as a criminal offense." - E.W. Dijkstra.Without music, life would be a mistake. - Friedrich Nietzsche⏎
Nothing to show⏎
Nothing to show⏎
Nothing to show⏎
Nothing to show⏎
Martin⏎
Is⏎
Pirsig⏎
Socrates⏎
C Robert⏎
John Lasseter⏎
M Robert⏎
Goodall Jane⏎
Brian Tracy⏎
Oscar Wilde⏎
Bill Watterson⏎
Answer Great Question The the to⏎
Everything Life Of Universe and the⏎
The is life living not unexamined worth⏎
Adams Douglas Galaxy Guide Hitchhiker The s the to⏎
Truth be can code found in one only place the⏎
Deep Forty Thought and calm infinite majesty said two with⏎
The and art art challenges inspires technology technology the the the⏎
All at do everything just makes modern once people technology this to try⏎
The a alone computer creator for he is is lawgiver of programmer the universes which⏎
Technology and do is just never one presumes right s there there things to way⏎
We all are are at but gutter in looking of some stars the the us⏎
A a and backed by clear confidence definite feeling gives of personal plans power tremendous vision you⏎
What a and decide difference difference do have kind make makes of to to want what you you you⏎
Przykładowa interakcja z programem -- skrajny przypadek:

Enter text:                          ,              .      ,                    ,                .                  ,                                .                                                          . -    .Technology is teaching us to be human again.-Simon Mainwaring⏎
Nothing to show⏎
Nothing to show⏎
Nothing to show⏎
Nothing to show⏎
Nothing to show⏎
Technology again be human is teaching to us⏎
Uwagi
W programie nie wolno korzystać z operatora [].

---
## [Anyelo120/Anyelo120](https://github.com/Anyelo120/Anyelo120)@[fcafb4e163...](https://github.com/Anyelo120/Anyelo120/commit/fcafb4e163b1067d5c878d9c3a8a6c9603b00163)
#### Monday 2022-10-03 21:02:35 by Anyelo120

Create README.md

SPANISH

Hola, mi nombre de usuario es: Anyelo120 Tengo 18 años. Soy estudiante de primer año en Ingeniería en Informática Multimedia. Tengo experiencia en la creación de servidores para juegos, he ocupado servidores dedicados y VPS, me manejo bien en el sistema operativo Ubuntu 22.04

👋 Actualmente tengo dos negocios pequeños los cuales son:

ProLatin Studio: Soy profesor para la gente que quiere entrar al mundo de la creación de servidores, también vendo servidores y hago servidores ha pedido, actualmente tengo un canal con 5000 seguidores en este proyecto y un discord con 500 personas.
YuCraft Network: es actualmente mi Network de MC que está en proceso, es muy nuevo este proyecto y estamos trabajando en él, actualmente contamos con un discord que tiene un total de 1900 personas.
📫 Experiencia actual:

Tengo experiencia en el manejo de servidores Ubuntu.
4 años trabajando con VPS y Servidores Dedicados.
1 año programando en JAVA.
Lenguajes que manejo: PHP, JavaScript, Java y Python.
Inglés Nivel Básico.
2 años con experiencia con el trato de clientes.
Edición de video
Manejo de redes sociales (MARKETING)
Creación de campañas publicitarias
Creación de plugins para MC
✨ Proyectos anteriormente realizados: Server de Minecraft: ProLatin Network (Creador, configurador y programador) Server de Minecraft: Gatitos World (Configurador y programador)

ENGLISH

Hello, my user name is: Anyelo120. I am 18 years old. I am a first year student in Multimedia Computer Engineering. I have experience in creating servers for games, I have occupied dedicated servers and VPS, I manage well in Ubuntu 22.04 operating system.

👋 I currently have two small businesses which are:

ProLatin Studio: I am a teacher for people who want to enter the world of server creation, I also sell servers and make servers on demand. and I make servers on demand, currently I have a channel with 5000 followers in this project and a discord with 500 people.
YuCraft Network: is currently my MC Network that is in process, this project is very new and we are working on it, we currently have a discord that has a total of 1900 people.
📫 Current experience:

I have experience in managing Ubuntu servers.
4 years working with VPS and Dedicated Servers.
1 year programming in JAVA.
Languages I manage: PHP, JavaScript, Java and Python.
Basic English level.
2 years with experience in dealing with customers.
Video editing.
Management of social networks (MARKETING)
Creation of advertising campaigns
Creation of plugins for MC
✨ Previous projects done: Minecraft Server: ProLatin Network (Creator, configurator and developer) Minecraft Server: Gatitos World (Configurator and programmer)

---
## [Anyelo120/Anyelo120](https://github.com/Anyelo120/Anyelo120)@[553ae2a41e...](https://github.com/Anyelo120/Anyelo120/commit/553ae2a41e07feb380034273e3d57fc26b121aed)
#### Monday 2022-10-03 21:08:06 by Anyelo120

Create README.md

SPANISH

Hola, mi nombre de usuario es: Anyelo120 Tengo 18 años.
Soy estudiante de primer año en Ingeniería en Informática Multimedia.
Tengo experiencia en la creación de servidores para juegos, he ocupado servidores dedicados y VPS, me manejo bien en el sistema operativo Ubuntu 22.04

👋 Actualmente tengo dos negocios pequeños los cuales son:

- ProLatin Studio: Soy profesor para la gente que quiere entrar al mundo de la creación de servidores, también vendo servidores y hago servidores ha pedido, actualmente tengo un canal con 5000 seguidores en este proyecto y un discord con 500 personas.
- YuCraft Network: es actualmente mi Network de MC que está en proceso, es muy nuevo este proyecto y estamos trabajando en él, actualmente contamos con un discord que tiene un total de 1900 personas.

📫 Experiencia actual:

Tengo experiencia en el manejo de servidores Ubuntu.
- 4 años trabajando con VPS y Servidores Dedicados.
- 1 año programando en JAVA.
- Lenguajes que manejo: PHP, JavaScript, Java y Python.
- Inglés Nivel Básico.
- 2 años con experiencia con el trato de clientes.
- Edición de video
- Manejo de redes sociales (MARKETING)
- Creación de campañas publicitarias
- Creación de plugins para MC

✨ Proyectos anteriormente realizados: 
- Server de Minecraft: ProLatin Network (Creador, configurador y programador) 
- Server de Minecraft: Gatitos World (Configurador y programador)

ENGLISH

Hello, my username is: Anyelo120 I am 18 years old.
I am a first year student in Multimedia Computer Engineering.
I have experience in creating servers for games, I have occupied dedicated servers and VPS, I manage well in Ubuntu 22.04 operating system.

👋 I currently have two small businesses which are:

- ProLatin Studio: I am a teacher for people who want to enter the world of server creation, I also sell servers and make servers on demand, I currently have a channel with 5000 followers in this project and a discord with 500 people.
- YuCraft Network: is currently my MC Network that is in process, it is very new this project and we are working on it, currently we have a discord that has a total of 1900 people.

📫 Current experience:

I have experience in managing Ubuntu servers.
- 4 years working with VPS and Dedicated Servers.
- 1 year programming in JAVA.
- Languages I manage: PHP, JavaScript, Java and Python.
- Basic English level.
- 2 years with experience in dealing with customers.
- Video editing.
- Management of social networks (MARKETING)
- Creation of advertising campaigns
- Creation of plugins for MC

✨ Previous projects done: 
- Minecraft Server: ProLatin Network (Creator, configurator and developer) 
- Minecraft Server: Gatitos World (Configurator and programmer)

---
## [WycliffeAssociates/DOC](https://github.com/WycliffeAssociates/DOC)@[d671da00be...](https://github.com/WycliffeAssociates/DOC/commit/d671da00beb2d89eb5c97f023e59d11cb9edd093)
#### Monday 2022-10-03 21:13:14 by linearcombination

Scary giant commit that gets to almost complete v2 UI

Massive changes related to:

- reactive state management with stores
- verify found URLs actually have assets before attempting to get them;
  sort of a ping of assets
- Factor into more components
- Massive UI look updates to conform to UI design
- Removal of vast quantities of now obselete code and a couple packages
- Use daisyui theme set to the colors from UI design
- Add more required pages to site

One development note: unfortunately Svelte has some limitations with
respect to binding complex objects to input controls like checkboxes.
As an example, a datum from our API for a book is a tuple, but Svelte
checkbox bind machinery on stores cannot handle a tuple or an
interface object or similar and take advantage of all the magic of
svelte's store bindings to inputs, i.e., all the automagically
generated store subscription code. So, we get the data as a complex
object, because in my opinion that is the proper data structure for
the data, but we then build comma delimited strings out of the data
structure since Svelte can handle that in its store/input
autogenerated subscription machinery. It violates my engineering
sense, but for now will have to do until such time as they upgrade
this aspect of Svelte. It isn't too bad though.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[14c96d05b8...](https://github.com/tgstation/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Monday 2022-10-03 22:09:52 by scriptis

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[f5d805da79...](https://github.com/Buildstarted/linksfordevs/commit/f5d805da791251213be6389038d90ce649b4473e)
#### Monday 2022-10-03 23:07:28 by Ben Dornis

Updating: 10/3/2022 11:00:00 PM

 1. Added: The dvorak keyboard, and the joy of designing your own editing scheme
    (https://esrh.me/posts/2022-04-07-dvorak-and-editing.html)
 2. Added: How (and why) nextest uses tokio, part 1 :: sunshowers
    (https://sunshowers.io/posts/nextest-and-tokio-1/)
 3. Added: Some thoughts on the economics of programming
    (https://blog.ploeh.dk/2022/10/03/some-thoughts-on-the-economics-of-programming/)
 4. Added: The Biology of Endurance: Energy
    (https://thrice.me/endurance-biology-energy/)
 5. Added: A case against nihilism
    (https://matthewsaltz.wordpress.com/2022/10/02/a-case-against-nihilism/)
 6. Added: Privacy is a business imperative
    (https://louisabraham.github.io/articles/privacy-business.html)
 7. Added: The software that I love
    (https://blog.waleson.com/2022/10/the-software-that-i-love.html)
 8. Added: GitHub - jsuarezruiz/figma-to-maui-graphics: FigmaSharp.Maui.Graphics turns your Figma design into .NET MAUI Graphics code
    (https://github.com/jsuarezruiz/figma-to-maui-graphics)
 9. Added: Simple Presenter Pattern in Rails without using Gems
    (https://pawelurbanek.com/rails-presenter-pattern)
10. Added: Using SVGs for icons
    (https://www.abiraja.com/blog/using-svgs-for-icons)
11. Added: Building a startup on Clojure
    (https://wobaka.com/blog/building-a-startup-on-clojure/)
12. Added: Prioritise content over components | simeonGriggs.dev
    (https://www.simeongriggs.dev/components-considered-harmful-for-content)
13. Added: How To Develop Good Taste, Pt. 1 — Die, Workwear!
    (https://dieworkwear.com/2022/08/26/how-to-develop-good-taste-pt-1/)
14. Added: Worst Airbnb experience - Blago's blog
    (https://petrovs.info/post/2022-10-03-airbnb/)
15. Added: Security Certification Roadmap - Paul Jerimy Media
    (https://pauljerimy.com/security-certification-roadmap/)
16. Added: Why Is Group Theory So Important in Particle Physics?
    (https://mfaizan.github.io/2022/10/02/symmetry.html)
17. Added: Requirements to  become a dangote cement distributor
    (https://bldrkms.blogspot.com/2022/10/cement-dealership-business-how-to.html)
18. Added: plant machete — David Bowen
    (https://www.dwbowen.com/plant-machete)
19. Added: Why dating apps don’t work
    (https://billmei.net/blog/why-dating-apps-dont-work)
20. Added: Being Glue — No Idea Blog
    (https://noidea.dog/glue)

Generation took: 00:07:18.9414432
 Maintenance update - cleaning up homepage and feed

---
## [mucsci-students/2022fa-475-TrashTurtle](https://github.com/mucsci-students/2022fa-475-TrashTurtle)@[c31b164251...](https://github.com/mucsci-students/2022fa-475-TrashTurtle/commit/c31b16425159bd9bdbcd74f6d183d7d1aa1cd01b)
#### Monday 2022-10-03 23:39:40 by RjCor

Bobbert fixed after breaking like an idiot.

Re-added him to scenes, added his components back, fixed stupid tag manager. I hate using github with unity. It should be better, I hate the user settings get uploaded. I'm upset! But that's okay.

---

