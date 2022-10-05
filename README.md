## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-04](docs/good-messages/2022/2022-10-04.md)


2,144,933 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,144,933 were push events containing 3,269,833 commit messages that amount to 270,516,917 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 47 messages:


## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[14c96d05b8...](https://github.com/GesuBackups/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Tuesday 2022-10-04 00:16:54 by scriptis

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
## [asutherland/mozsearch](https://github.com/asutherland/mozsearch)@[6466b38ff1...](https://github.com/asutherland/mozsearch/commit/6466b38ff16abb47db1e3408ba4d1a3b37e9b2f8)
#### Tuesday 2022-10-04 00:21:24 by Andrew Sutherland

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[fc9cf24df1...](https://github.com/san7890/bruhstation/commit/fc9cf24df13e8266ab907a6fd28d2d5830f5836d)
#### Tuesday 2022-10-04 00:29:49 by san7890

WAIT A SECOND THAT'S NOT RIGHT

* replaces old json decode with actual toml decode (loling, lmaoing).

* fixes some bad index bullshit i think this is the right way to fix it (using += to create assoc. lists)

* removes shitty indenting that accidentally broke shit very sad

* fixes paramedic config tag to actually work and not flag as mime (lol lmao).

---
## [AzonStarfall/TerraGov-Marine-Corps](https://github.com/AzonStarfall/TerraGov-Marine-Corps)@[a96d4df973...](https://github.com/AzonStarfall/TerraGov-Marine-Corps/commit/a96d4df9736c68bf6534de6124698fabbd9e9c97)
#### Tuesday 2022-10-04 01:28:22 by 567Turtle

item storage tweaks (#10913)

* whistle thing

i hate this fucking game

* grammar

who knew defibrillator was spelled with two Ls

* defib go bye bye

bye bye

* few other things

Makes it so you can put a sodering tool in your belt and your vest, robots need healing to

* injector boots

If you can put a whole ass MRE in your boot you can put a little ass pen in there

* reverts changelog changes

nuff said

* fixes things

adds trail commas where I forgot them, removes medipens going in shoes

* jaeger module soldering tool

you can put a soldering tool into the medical jaeger storage module :)

* reverts typo fix

nuff said

---
## [BayerischeMotorenWerke/kernel_xiaomi_sdm660](https://github.com/BayerischeMotorenWerke/kernel_xiaomi_sdm660)@[9817aff2ba...](https://github.com/BayerischeMotorenWerke/kernel_xiaomi_sdm660/commit/9817aff2ba6983ff2cc3a02ee5bfc2be7a339b34)
#### Tuesday 2022-10-04 01:54:39 by Christian Brauner

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
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[736422fac8...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Tuesday 2022-10-04 02:01:50 by Technobug14

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
## [perfectly-preserved-pie/larentals](https://github.com/perfectly-preserved-pie/larentals)@[1478e28166...](https://github.com/perfectly-preserved-pie/larentals/commit/1478e28166cf4a8f2bc782867a970a3a8a26f967)
#### Tuesday 2022-10-04 02:18:30 by Sahib Bhai

Add a workaround for rows with a missing latitude. Prevents "t is null" javascript errors. Man this was a real fucking pain in my ass to debug.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0ae5825093...](https://github.com/treckstar/yolo-octo-hipster/commit/0ae58250934bc307994a4a8d81c04a6872dd269f)
#### Tuesday 2022-10-04 02:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[635aee8e34...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Tuesday 2022-10-04 02:52:38 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [RedMisao/Cataclysm-DDA-Touhou-Mod](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod)@[7b87ab1303...](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod/commit/7b87ab130325d879dfc682e4a612f44d6a54133b)
#### Tuesday 2022-10-04 02:55:29 by RedMisao

0.9.4.2

- (Updated to 2022-10-02 experimental)

Items:
- (WIP) Added data for a "gap generator" magical item

Guns:
- Lunar weapons were changed again: now self-replenish ammo over time, can't be unloaded or reloaded. I think this is better than the previous system of casting spell -> crafting ammo -> reloading

Monsters:
- Added skinwalkers: dog-twig skinwalker, deer-like wendigo, a witch that transforms into different animal forms.  Also included a special skinwalker pelt item drop, basic spawns on the wilderness, vocalizations, special attacks, etc.
- Added "female ghost" type enemies: banshee, La Llorona, white lady. Also included basic spawns, vocalizations, special attacks, etc.
- Also added jackalope and squonk, including basic spawns, vocalizations, special attacks, etc.
- Tweaked some monster special attacks

Spells:
- Added wings mutations for Aya, Remi and Utsuho. While active, it enables them to fly over ledges, and consumes stamina
- Udonge: moved Wavelength manipulation (Insight) mental debuff removal to Wavelength manipulation (Mental fortitude)

Weather:
- Added two new weather types: scarlet mist and scarlet fog. Mostly for testing purposes, should randomly happen, reducing sunlight
- (WIP) Added data for random events: night parade and silence hour

Misc:
- Temporary fix for dashes over open air not working (cdda issues #53511 and #53532).
- Fixed Tenko's keystone dismissal not dismissing pillar keystones
- Fixed Tenko's keystone pillar not being castable on top of enemies
- Reduced loudness of Lunar weapons
- Fixed and tweaked some character mutations. Also fixed a bug where mutation stat modifiers (STR, DEX, etc.) added extra cost while on character selection
- Moved magic item enchantments to mutations, so they're visible to the player
- Moved monster spells to a separate file from special attacks. Also moved monster spell effects to a separate file
- Moved the touhou_monster_effects.json file

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[e5a2b0f16e...](https://github.com/Mothblocks/tgstation/commit/e5a2b0f16e2bb47b0ed60e487e3c6b2dd32f81dc)
#### Tuesday 2022-10-04 02:59:12 by LemonInTheDark

Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[cee07f804c...](https://github.com/Mothblocks/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Tuesday 2022-10-04 02:59:12 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [EoaNB-Team/EoaNB](https://github.com/EoaNB-Team/EoaNB)@[e9ef7e7b1f...](https://github.com/EoaNB-Team/EoaNB/commit/e9ef7e7b1f924239f49d260a5f0719cb9fcb561e)
#### Tuesday 2022-10-04 03:10:40 by Imperialism

MILLIONS OF FIXES + Load to Main menu now!!

Fixed Literally TONS OF SHIT FUCK PARADOX

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[32c2e4ccd3...](https://github.com/tgstation/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Tuesday 2022-10-04 03:48:25 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [mikeyhodl/ic](https://github.com/mikeyhodl/ic)@[404727ff2f...](https://github.com/mikeyhodl/ic/commit/404727ff2ff58d784e534192469d8da298fe4ff7)
#### Tuesday 2022-10-04 04:13:40 by Or Ricon

Merge branch 'or-routes-503' into 'master'

return 503 Service Unavailable when routes are empty

Right now when the routes table is empty, a request will be made to `https://` - which fails with a `Invalid URL prefix`.
This change adds a check for whether the routes table is empty and if it is then we explicitly return a `503 Service Unavailable`.

One issue I noticed because of how amazing (/s) nginx is that our various directives to add a bunch of headers get executed anyway - which seems pretty bad - e.g for a healthcheck request when there's no routes we would get the following headers back:

```
* Connection state changed (MAX_CONCURRENT_STREAMS == 256)!
< HTTP/2 503 
< server: nginx/1.21.3
< date: Mon, 03 Oct 2022 14:55:47 GMT
< content-type: text/html
< content-length: 197
< access-control-allow-origin: *
< access-control-allow-credentials: true
< access-control-allow-headers: DNT,User-Agent,X-Requested-With,If-None-Match,If-Modified-Since,Cache-Control,Content-Type,Range,Cookie
< access-control-expose-headers: Content-Length,Content-Range
< access-control-max-age: 600
< content-type: application/cbor
< x-content-type-options: nosniff
```

I'd assume we just want to return the 503 with none of these Access-Control headers (also, the Content-Type is definitely not `application/cbor`).
I know we made all our `add_header` calls have `always` for a reason, but now I can't seem to remember it.

@daniel.bloom1 Any thoughts here? 

See merge request dfinity-lab/public/ic!7990

---
## [spyrothon/graphics](https://github.com/spyrothon/graphics)@[5d48ac16e3...](https://github.com/spyrothon/graphics/commit/5d48ac16e3bc4b42a8fc0e2d77af569c31feb00a)
#### Tuesday 2022-10-04 05:39:19 by Jon

[wip] initial bot setup and loading services from Render (#14)

The Open API spec kinda sucks and is really annoying to work with
because the typing is way too lax, plus it doesn't let you discriminate
the union based on response status. So we have to just _assume_ it'll be
a 200...(which it will, because the generated client throws on anything
>=400, so the other codes can't even happen here...)

---
## [ibrahmkaratas/Using-Databases-with-Python](https://github.com/ibrahmkaratas/Using-Databases-with-Python)@[a6c47dc0dc...](https://github.com/ibrahmkaratas/Using-Databases-with-Python/commit/a6c47dc0dcfab9d955e907f3b09557e8385e3d31)
#### Tuesday 2022-10-04 07:34:44 by ibrahmkaratas

Create  Assignment

Output:
Dict count: 404
Another One Bites The Dust Queen Greatest Hits 55 100 217103
Asche Zu Asche Rammstein Herzeleid 79 100 231810
Beauty School Dropout Various Grease 48 100 239960
Black Dog Led Zeppelin IV 109 100 296620
Bring The Boys Back Home Pink Floyd The Wall [Disc 2] 33 100 87118
Circles Bryan Lee Blues Is 54 60 355369
Comfortably Numb Pink Floyd The Wall [Disc 2] 36 100 384130
Crazy Little Thing Called Love Queen Greatest Hits 38 100 163631
Electric Funeral Black Sabbath Paranoid 44 100 293015
Fat Bottomed Girls Queen Greatest Hits 38 100 257515
For Those About To Rock (We Salute You) AC/DC Who Made Who 84 100 353750
Four Sticks Led Zeppelin IV 84 100 284421
Furious Angels Rob Dougan The Matrix Reloaded 54 100 330004
Gelle Bryan Lee Blues Is 45 60 199836
Going To California Led Zeppelin IV 100 100 215666
Grease Various Grease 42 100 205792
Hand of Doom Black Sabbath Paranoid 36 100 429609
Hells Bells AC/DC Who Made Who 82 100 312946
Hey You Pink Floyd The Wall [Disc 2] 23 100 282305
I Worry Bryan Lee Blues Is 33 100 341315
Iron Man Black Sabbath Paranoid 39 100 358530
Is There Anybody Out There? Pink Floyd The Wall [Disc 2] 26 100 160679
It was a Very Good Year Frank Sinatra Greatest Hits 39 100 268852
Its Your Move Bryan Lee Blues Is 40 100 245002
Jack the Stripper/Fairies Wear Boots Black Sabbath Paranoid 35 100 373995
Killer Queen Queen Greatest Hits 34 100 181368
Laichzeit Rammstein Herzeleid 41 100 262844
Let me Down Easy Bryan Lee Blues Is 43 100 331441
Misty Mountain Hop Led Zeppelin IV 88 100 278831
No Low Down Bryan Lee Blues Is 39 100 245760
Now You Are Gone America Greatest Hits 52 100 187559...

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[1c27d16e6e...](https://github.com/david-rowley/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Tuesday 2022-10-04 08:19:28 by Tom Lane

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e28b994dc5...](https://github.com/treckstar/yolo-octo-hipster/commit/e28b994dc522da231fb6f1e76238a19cf8f2b915)
#### Tuesday 2022-10-04 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [alexpott/symfony](https://github.com/alexpott/symfony)@[338daf25c9...](https://github.com/alexpott/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Tuesday 2022-10-04 09:06:33 by Nicolas Grekas

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
## [EpicROM-AOSP/android_frameworks_base](https://github.com/EpicROM-AOSP/android_frameworks_base)@[136e73236f...](https://github.com/EpicROM-AOSP/android_frameworks_base/commit/136e73236f66fa9bfa13114fa53484d8c7e16f54)
#### Tuesday 2022-10-04 09:25:04 by Joey Huab

core: Refactor Pixel features

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[23bfdec8f4...](https://github.com/lizardqueenlexi/orbstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Tuesday 2022-10-04 10:20:52 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[1810b85553...](https://github.com/lizardqueenlexi/orbstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Tuesday 2022-10-04 10:20:52 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

---
## [javivelasco/next.js](https://github.com/javivelasco/next.js)@[1bbd264216...](https://github.com/javivelasco/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Tuesday 2022-10-04 10:30:35 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [aras-p/oiio](https://github.com/aras-p/oiio)@[d8d20840bb...](https://github.com/aras-p/oiio/commit/d8d20840bb477b9aae12b40c3c4b912a08a438ab)
#### Tuesday 2022-10-04 10:32:31 by Aras Pranckevicius

DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

---
## [patent122/Dante_2_Semestr_Lato_2022](https://github.com/patent122/Dante_2_Semestr_Lato_2022)@[49ed4f7fbf...](https://github.com/patent122/Dante_2_Semestr_Lato_2022/commit/49ed4f7fbfdaac5831dcba07ce36805174e3173d)
#### Tuesday 2022-10-04 10:48:05 by Patryk Panek

Zadanie 8.4 Dynamiczne łączenie tekstów - PLAGIAT

Napisz i przetestuj funkcję łączącą N tekstów do wspólnego bufora i zwracającą ten bufor.

Funkcja może przydzielić tylko tyle pamięci ile będzie potrzebne na przechowanie tekstu wyjściowego. Poszczególne teksty mają być oddzielone spacjami.

Funkcja ma przyjmować w parametrze:

liczbę tekstów oraz
kolejne teksty.
Wartość zwracana:

W przypadku sukcesu funkcja powinna zwrócić wskaźnik na scalony tekst (rozdzielony spacjami),
w przypadku błędnych danych wejściowych lub niepowodzenia alokacji pamięci NULL.
Przykładowe wywołanie funkcji powinno wyglądać następująco:

char* msg = concatenate(3, "Ala", "ma", "kota");
...
free(msg);
Napisz program, który pobierze od użytkownika liczbę tekstów do wczytania (od 2 do 4), a następnie właściwie teksty i wykorzystując przygotowaną wcześniej funkcję połączy je w jeden tekst.

Przed wczytywaniem tekstów przygotuj tablicę dwuwymiarową, alokowaną dynamicznie, na te teksty. Tablica powinna umożliwić przechowanie maksymalnie 4 tekstów o długości 1000 znaków każdy.

W przypadku niepowodzenia alokacji pamięci program powinien wyświetlić komunikat Failed to allocate memory i zakończyć działanie z kodem błędu 8.
W przypadku wprowadzenia błędnych znaków program powinien wyświetlić komunikat Incorrect input i zakończyć działanie z kodem błędu 1.
W przypadku błędnych danych wejściowych komunikat Incorrect input data i zakończyć działanie z kodem błędu 2.
Przyjmij założenie, że długość tekstów wejściowych nie przekroczy 1000 znaków. Jeżeli podany tekst będzie dłuższy, to pozostałe znaki powinny zostać zignorowane.

Program powinien wyświetlić wynik połączenia podanych tekstów w jeden tekst.

Przykładowa interakcja z programem -- sukces:

Podaj liczbe tekstow do wprowadzenia: 4⏎
Podaj teksty: Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein⏎
It is impossible to work in information technology without also engaging in social engineering. - Jaron Lanier⏎
Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live - John Woods⏎
The real problem is not whether machines think but whether men do.-B.F. Skinner⏎
Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein It is impossible to work in information technology without also engaging in social engineering. - Jaron Lanier Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live - John Woods The real problem is not whether machines think but whether men do.-B.F. Skinner
Podaj liczbe tekstow do wprowadzenia: 3⏎
Podaj teksty: Wise men speak because they have something to say; fools because they have to say something. - Plato⏎
"Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program." - Linus Torvalds⏎
⏎
Wise men speak because they have something to say; fools because they have to say something. - Plato "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program." - Linus Torvalds
Uwaga - trzeci tekst jest pusty.

Przykładowa interakcja z programem -- brak pamięci:

Limit sterty: 3035 bajtów

Failed to allocate memory⏎
Limit sterty: 4036 bajtów

Podaj liczbe tekstow do wprowadzenia: 4⏎
Podaj teksty: The things you do for yourself are gone when you are gone, but the things you do for others remain as your legacy. - Kalu Ndukwe Kalu⏎
Successful weight loss takes programming, not willpower. - Phil McGraw⏎
"Man, the living creature, the creating individual, is always more important than any established style or system." - Bruce Lee⏎
"Imagine your life is perfect in every respect; what would it look like?"- Brian Tracy⏎
Failed to allocate memory⏎
Limit sterty: 4456 bajtów

Podaj liczbe tekstow do wprowadzenia: 4⏎
Podaj teksty: The things you do for yourself are gone when you are gone, but the things you do for others remain as your legacy. - Kalu Ndukwe Kalu⏎
Successful weight loss takes programming, not willpower. - Phil McGraw⏎
"Man, the living creature, the creating individual, is always more important than any established style or system." - Bruce Lee⏎
"Imagine your life is perfect in every respect; what would it look like?"- Brian Tracy⏎
The things you do for yourself are gone when you are gone, but the things you do for others remain as your legacy. - Kalu Ndukwe Kalu Successful weight loss takes programming, not willpower. - Phil McGraw "Man, the living creature, the creating individual, is always more important than any established style or system." - Bruce Lee "Imagine your life is perfect in every respect; what would it look like?"- Brian Tracy⏎
Przykładowa interakcja z programem -- błąd danych wejściowych:

Podaj liczbe tekstow do wprowadzenia: 9⏎
Incorrect input data
Podaj liczbe tekstow do wprowadzenia: wFYXVCbELD⏎
Incorrect input
Uwagi
W programie nie wolno używać operatora [].

---
## [YusufEmirKoroglu/tgstation](https://github.com/YusufEmirKoroglu/tgstation)@[99b8d6b494...](https://github.com/YusufEmirKoroglu/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Tuesday 2022-10-04 11:27:12 by vincentiusvin

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
## [activityumji/activityumji.github.io](https://github.com/activityumji/activityumji.github.io)@[5425461bdd...](https://github.com/activityumji/activityumji.github.io/commit/5425461bdd5a34534a4752bbd09dd23f071b28f1)
#### Tuesday 2022-10-04 12:02:33 by Frederick Yin

Add wechat spider

Fuck you tencent. You will be forever remembered as destroyer of the
open web.

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[91f02f2a6b...](https://github.com/RikuTheKiller/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Tuesday 2022-10-04 12:10:11 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[bc90b2c9ad...](https://github.com/newstools/2022-metro/commit/bc90b2c9adcd781c66709894a22fa49e123e2812)
#### Tuesday 2022-10-04 12:42:01 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/10/03/strictlys-kai-jokes-he-and-girlfriend-nadiya-are-even-after-dance-off-17496105/]

---
## [mturch/terminal](https://github.com/mturch/terminal)@[855e1360c0...](https://github.com/mturch/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Tuesday 2022-10-04 13:55:51 by Mike Griese

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

---
## [facebook/react](https://github.com/facebook/react)@[b6978bc38f...](https://github.com/facebook/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-10-04 15:20:28 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [nolan-3/Dodgeball](https://github.com/nolan-3/Dodgeball)@[79c323f8c7...](https://github.com/nolan-3/Dodgeball/commit/79c323f8c78cd323d1ac434995e472ad20d25845)
#### Tuesday 2022-10-04 15:46:36 by nolan-3

1. Changed Knight to a functional component so that
I could call an event listener for key input, however now it doesn't run in the gameloop so it's
quite clunky. 2. Downloaded Xcode and tried to convert this into native code for android/ios, I d
on't think it worked. Finally I would just like to say I think this solution for moving is quite
poor, maybe making it back into an entity and having it rerender each time the loop runs would wo
rk. I just kept getting an error Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:

You might have mismatching versions of React and the renderer (such as React DOM)
You might be breaking the Rules of Hooks
You might have more than one copy of React in the same app See for tips about how to debug and fix this problem. I believe it was number 2 and I wasn't sure how to work around it.

---
## [nolan-3/Dodgeball](https://github.com/nolan-3/Dodgeball)@[b72540349a...](https://github.com/nolan-3/Dodgeball/commit/b72540349a2613d5e515d39f8953c2cfe7544d70)
#### Tuesday 2022-10-04 15:46:36 by nolan-3

1. Changed Knight to a functional component so that I could call an event listener for key input, however now it doesn't run in the gameloop so it's quite clunky. 2. Downloaded Xcode and tried to convert this into native code for android/ios, I don't think it worked. Finally I would just like to say I think this solution for moving is quite poor, maybe making it back into an entity and having it rerender each time the loop runs would work. I just kept getting an error Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:

You might have mismatching versions of React and the renderer (such as React DOM)
You might be breaking the Rules of Hooks
You might have more than one copy of React in the same app See for tips about how to debug and fix this problem. I believe it was number 2 and I wasn't sure how to work around it.

---
## [infernalstudios/Nekos-Enchanted-Books](https://github.com/infernalstudios/Nekos-Enchanted-Books)@[14a31871e8...](https://github.com/infernalstudios/Nekos-Enchanted-Books/commit/14a31871e89fcd8ce63070d5d77fe8c04abb646c)
#### Tuesday 2022-10-04 17:14:01 by nekomaster1000

Release 1.8, 10 new mod compatibilities, 2 updates

Release 1.8
Added support for
= Minecraft 1.19/The Wild Backport =
- Swift Sneak

= Ars Noveau =
- Mana Boost
- Reactive
- Mana Regen

= Copper Overhaul =
- Stormbreaker
- Sparkling

= Majruszs Enchantments =
- Breaking Curse
- Death Wish
- Gold Fuelled
- Guardian Angel
- Horse Swiftness
- Misanthropy

= Domestication Innovation =
- Tethered Teleport
- Immaturity Curse
- Muffled
- Blazing Protection
- Healing Aura

= Grappling Hook Mod =
- Wall Running
- Double Jump
- Sliding

= Inventorio =
- Deep Pockets

= Aileron =
- Smokestack
- Cloudskipper

= Combat Roll =
- Longfooted
- Acrobats chest
- Acrobats legs
- Multiroll

= Shulker Enchantments =
- Siphon
- Refill

= Block Swapper =
- Excavating

= Ars Nouveau =
- Mana Regen
- Mana Boost
- Reactive

= Auto Smelt =
- Auto-Smelt

= Spells and Shields =
- Magic Protection
- Mana Blade
- Mana Shield
- Mana Regen
- Max Mana

= Origins =
- Water Protection

---
## [firedreamer/Firedreamer-Hugo](https://github.com/firedreamer/Firedreamer-Hugo)@[6efe485c37...](https://github.com/firedreamer/Firedreamer-Hugo/commit/6efe485c37e838e89d1ca49b9bc6996010ef40b7)
#### Tuesday 2022-10-04 18:25:51 by Ashe O'Hawkes

doridoridoridori

Neco Arc is all that I think of. Neco Arc is the best thing that I ever saw. It all started on Discord, on a videogame music server. I started seeing those gifs of a cute small catgirl dancing the gangnam style dance. It was very funny, but I continued with my life. Then, I saw it again. This time she was riding a car. The next one was the thing that made me realize how perfect this character is. Her little voice saying "dori dori dori dori" made me realize I just found the meaning of life. Neco Arc became my entire life after that. I will do anything to meet this perfect being. I want to hug her tightly while she purrs feeling comfortable in my arms. I will find a way to meet Neco Arc. I do not care what I have to do. I don't care anymore. I will do anything to meet Neco Arc. I want her to say "Gurenyuu" as she walks around, showing everyone what the perfect life is. Neco Arc will show us how to become better. Neco Arc is the new symbol of peace. Dori dori dori dori.

---
## [jkinz3/JohnRenderer](https://github.com/jkinz3/JohnRenderer)@[7e8207f7ab...](https://github.com/jkinz3/JohnRenderer/commit/7e8207f7abbe0204cbb81a3b9e25eb895ec878b0)
#### Tuesday 2022-10-04 18:29:29 by John Kinzel

you have got to be FUCKING shitting me

constant buffer in wrong order. fuck my life

---
## [firedreamer/Firedreamer-Hugo](https://github.com/firedreamer/Firedreamer-Hugo)@[2d5a8aa397...](https://github.com/firedreamer/Firedreamer-Hugo/commit/2d5a8aa3971d2805c23d985b3461eba2c458138e)
#### Tuesday 2022-10-04 18:31:16 by Ashe O'Hawkes

remove doridori

Neco Arc is nothing that I think of. Neco Arc is the worst thing that I ever saw. It all started on Discord, on a videogame music server. I started seeing those gifs of a cute small catgirl dancing the gangnam style dance. It was very unfunny, but I continued with my life. Then, I saw it again. This time she was riding a car. The next one was the thing that made me realize how broken this character is. Her little voice saying "dori dori dori dori" made me realize I just lost the meaning of life, if I ever found it. Neco Arc became only a tiny footnote in my life after that. I will do anything to kill this wretched being. I want to strangle her tightly while she screams in my arms. I will find a way to destroy Neco Arc. I do not care what I have to do. I don't care anymore. I will do anything to destroy Neco Arc. I want her to say absolutely nothing as she walks around, showing everyone how fucking pointless life is. Neco Arc will show us how to become worse. Neco Arc is the new symbol of hatered. Dori dori dori dori.

---
## [greeveu/AdvancedBan](https://github.com/greeveu/AdvancedBan)@[1d9e6910e3...](https://github.com/greeveu/AdvancedBan/commit/1d9e6910e33bda906ee03ffada08377a91a604ad)
#### Tuesday 2022-10-04 19:32:32 by Achsion

added a (hopefully) somewhat usable api as a first step to let the fricking plugin handle its own shit without having to rely on other plugins to know the god damn sql queries required to fetch some poor ass data

---
## [Manux123/FNF-Cool-Engine](https://github.com/Manux123/FNF-Cool-Engine)@[49d05921e6...](https://github.com/Manux123/FNF-Cool-Engine/commit/49d05921e68999ae1cabf55a452226ff503962fe)
#### Tuesday 2022-10-04 20:01:38 by XuelDev

XuelDev Commit | Squashed, Added Mod Menu and Fixed VideoState for Linux And Mac And Windows :)

* HOW THE FUCK?

* Holy Shit New Update :)

* FUCKKKK

---
## [ultra0000/JSONator](https://github.com/ultra0000/JSONator)@[f119df5fe9...](https://github.com/ultra0000/JSONator/commit/f119df5fe9608a0e13a4482f5c40e4b58b9026e5)
#### Tuesday 2022-10-04 20:09:52 by ultra0000

yeah

i need to organize this code holy balls, anyway according to code in ab friends the startNumber value in birds is named index?

---
## [ShaylenReddy42/Seelans-Tyres](https://github.com/ShaylenReddy42/Seelans-Tyres)@[673d44990c...](https://github.com/ShaylenReddy42/Seelans-Tyres/commit/673d44990c0a2b778a3f97ad6a27cddb41d2ad9d)
#### Tuesday 2022-10-04 21:02:42 by Shaylen

containerize and MOSTLY orchestrate the solution locally

i say this with a heavy heart, even though i lost track of how many hoops i jumped through to the solution to this point, that i couldn't fully orchestrate the solution due to a rather stupid problem. host.docker.internal is used to enable communication between all the microservices but the identity service can not and does not want to work with that. i've tried various tactics over the passed two days to get it to work but it never did. no idea how microsoft got it to work in their eShopOnContainers reference architecture but oh well

in order to compensate for that disappointment, i tried my best to make the building and running of the solution as seamless as possible, at the cost of a single file publish. it's a small price to pay to make me happy. don't look in the publish folder, just stay in the clean scripts folder

there's various scripts that work together to build and run the solution which i explain well in the readme file so i won't mention it here but in summary, orchestration is simulated like it's running using docker compose

later when i eventually orchestrate with kubernetes and it gives the same problem, i'll have to deploy the identity service to azure app services

many changes were made to get to this point and i may miss some:
- removal of https. this was a nightmare for a day and caused most of the adjustments
- adjusting to use docker compose
- using a better way to enforce the port number, and that was to just configure kestrel 😐
- enriched the logs with the activityspan to include the traceId, it wasn't added by default
- since client configuration changes a lot, i decided to remove a client if found and add it again. saving me the trouble of always deleting the database and running the application again

i thought the last build will be the last to produce artifacts but i was wrong, it'll continue

in some rather good news, log aggregation, storage and querying as well as distributed tracing all work and work well. soon i'll add to the readme how to go about setting up and using kibana to see it in action

---
## [firelab/canopy-wake](https://github.com/firelab/canopy-wake)@[1d94933b2e...](https://github.com/firelab/canopy-wake/commit/1d94933b2eabf18c4ec1fdde3a6cd5eef382ca14)
#### Tuesday 2022-10-04 21:39:28 by latwood

Added the other submodules to the set of Lagrangian Particle code. OpenFOAM did have a normal distribution model for particle sizes, but didn't have a lognormal distribution, this was an attempt to replicate what was described online comparing to the normal distribution code. The first version of the cone injection was also added.

The myParCalcs tool needs extra description, it was designed to do runtime binning of particles into the Eulerian grid, and underwent MANY revisions, because it was insanely hard to do with the limited runtime information that was available with the current setup of the code. Honestly, if I were to have to do much more to the particle code, I would restructure the whole thing to force more of these types of information to be more accessible, which would involve major messing with the inheritance structures of the OpenFOAM Lagrangian Particle code, not just these single libraries as was done for this project. And in the end, the myParCalcs code ended up being worthless, it seemed to be correct by the end, until it was used on code with separate processors, then it DEFINITELY used the wrong algorythm to detect which particles were where and started mixing up information, after all the hard work to get the dang thing to work. So it ended up being tossed out in the end, particle binning information ended up being easier to do using post processing. But the code is still useful to get an idea of how the inheritance structure of the OpenFOAM Lagrangian particle code works, and has some weird quirky examples of how to get access to code in ways not seen in the post process functions. Technically the post process functions have less access to some of these things, the inheritance and access is such that it became harder, I just got lucky that there was an example using the post processing of particle tracking.

Anyhow, as the various versions of the myParCalcs code gets pushed to the repo, you will see just how annoying it was trying to calc the particle information with such limited runtime information. This is a similar problem with the turbulence models, but at least the amount of information normally available was exactly what was needed by the turbulence models, not so with myParCalcs.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[bd343f365d...](https://github.com/ammarfaizi2/linux-fork/commit/bd343f365df59de2b9cbc2ac55d3d77534b0f10c)
#### Tuesday 2022-10-04 21:56:11 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [mozillaminh/portfolio](https://github.com/mozillaminh/portfolio)@[2387703cc7...](https://github.com/mozillaminh/portfolio/commit/2387703cc7d4ffb90a0edd57de4bfdc131e1375e)
#### Tuesday 2022-10-04 23:13:45 by mozillaminh

Add files via upload

Load each csv file to power BI
The data model is automatically created - check the relationship between the tables
Connect a date table
What days and times do we tend to be busiest?	
See below
How many pizzas are we making during peak periods?
Matrix
Rows: create a custom column in Orders table, extracting the hour of the orders 
Column: Weekday Name
Value: order_details[quanity]
Format: conditional formatting the values to create the heat map
What are our best and worst selling pizzas?
Best Seller: Visualisation - Table
1st column: pizza_type[name]
Rename column to ‘Top 3 Best Sellesr’
Filter fot this viz: top N => top 3 => by order_details[quantity]
The best seller is the name with the most quantity
2nd column: order_details[quantity]
Rename column to ‘Units Sold’
Sort from largest to smallest’
Worst Seller: Copy + Paste the above viz:
Rename column to ‘Top 3 Worst Sellers’ (rename for this viz)
Filter fot this viz: top N => bottom 3 => by order_details[quantity]
The worst seller is the name with the least quantity
What's our average order value?
Total Sales:
New Measure: Total Sales = SUMX(order_details,order_details[quantity] * RELATED(pizzas[price]))
Total Order
Max of order_details[order_id]
Total Pizzas
Sum of order_details[quantity]
Pizzas per order
Pizzas per Order = DIVIDE(SUM('order_details'[quantity]), COUNTA('orders'[order_id]))
Sales per order:
New Measure: Sales per Order = DIVIDE([Total Sales], COUNTA('orders'[order_id]))
How well are we utilizing our seating capacity? (we have 15 tables and 60 seats)
Assumptions:
daily capacity is 15 tables * 4 chairs * 15 business hours = 900 units
2 customers enjoy 1 order, taking 2 chairs, finishing the order in 1 hr
=> 1 order takes 2 units of capacity
Create a Capacity table
Duplicate the Orders table
Remove duplicated values Date column
Remove all other columns
Create a new column and assign 900 as the values
Measure:
Utilisation (Orders/Seats = DIVIDE(COUNTA('orders'[order_id]) * 2, SUM('capacity'[Index]))
Other info
Sales by category
Pie chart: 
Legend: pizza_types[category]
Values: total sales
Sales by size
Column chart
X-axis: pizza_types[category]
Values: total sales
Sales by category and size
Stacked bar chart
Y-axis: pizza_types[category]
X-axis: total sales
Legend: pizzas[szie]
Most used ingredients
New table - ingredients:
Duplicate the order_details table
Add new column extracting the pizza_type_id by removing the size in the pizza_id column
Merge as a new table with the pizza_types table via pizza_type_id column
Expand the ingredients column only
Delimit the ingredients column using “, “ as the delimiter
Remove all columns except quantity and ingredient column
Select quantity column, pivot other columns - rename the new column to ingredients
Treemap:
Category: ingredients
Values: sum of quanity
Findings and Recommendations:
Top 3 best sellers are not too far apart but the slowest seller (Brie Carre) is only half the second lowest one.
Remove the Brie Carre due to low volumn, also reduce the complexity of inventory management.
Three peak periods during a week: weekday lunches; weekday dinners; evening of Friday and Saturday
Need to ensure appropriate staffing during these periods
There are insignificant orders before 11 am and after 22 pm
Reduce trading hours to 11 am to 22 pm to reduce costs
Very low utilisation rate hovers around 13%
Run marketing campaigns to attract more customers or rearranging the underutilised areas for other purposes.
Average order size is 2.32 per pizza 
Likely to be ordered by couple or family, hence, focus on these groups of customers during advertising
Almost no order in XL and XXL size while L size takes 45% of total sales
Do not remove XL and XXL sizes, they act as distractions
Seek bulk discounts where possible on most commonly used ingredients

---
## [Lindonrow/StorytimeOfficialMod](https://github.com/Lindonrow/StorytimeOfficialMod)@[a8575ab482...](https://github.com/Lindonrow/StorytimeOfficialMod/commit/a8575ab482282d045c31fc8a1f982169b1a84a49)
#### Tuesday 2022-10-04 23:29:50 by Isengriff

Chapter 1: Is This Thing On?

Yeah I know it should be Chapter 10 damnit but shit got out of hand, okay? You gotta do what you gotta do and I ain't gonna hear any slanderous accusations about my management of this mod, are we clear you damn maggots?

---
## [steenax86/OpenShadingLanguage](https://github.com/steenax86/OpenShadingLanguage)@[e4e5088ed6...](https://github.com/steenax86/OpenShadingLanguage/commit/e4e5088ed6dcd4eb636430dcce9fe815e435b1a6)
#### Tuesday 2022-10-04 23:52:45 by Larry Gritz

LLVM 15.0 support (#1592)

* A variety of changes to get a clean build and passing tests when
  using LLVM 15.0.

* I've noticed problems when using LLVM 15 but building with earlier
  clang, so the cmake scripts now print a warning in that case, so if
  users encounter trouble they have a hint about what to do to fix it.

* For our CI tests on Mac, force the MacOS-11 test to use llvm 14,
  and the MacOS-12 test to use llvm 15.

IMPORTANT TO-DO / CAVEATS:

1. When doing JIT at optlevel 12 or 13, I had to disable a number of
   passes that don't seem to exist anymore in LLVM 15. This is enough
   to get it working, and to be honest, I don't know if anybody uses
   these opt levels.  But we need to revisit this, because I don't
   know if there these are cases where the names of the passes merely
   changed or that new passes take their place (in which case we
   should add the new passes, not stop after merely disabling the
   deprecated ones). For that matter, optlevel modes 11, 12, 13 are
   supposed to match what clang does for -O1, -O2, -O3, and that
   changes from one release to the next, so we should probably revisit
   this list and make sure it's matching clang's current choices
   (which I assume are crafted and periodically revised by clang's
   authors).

2. LLVM 15 switches to "opaque pointers". It still supports typed
   pointers...  for now. But as you can see in the diffs, I had to
   disable a variety of deprecation warnings and take some other
   actions to put LLVM 15 in the old "opaque ptr" mode to match our
   use of LLVM <= 14. But this is only temporary, because the typed
   pointer mode is expected to be removed entirely in LLVM 16. So at
   some point in the next few months, we are going to need to support
   opaque pointers in our use of LLVM. (Also note: for a while, we're
   going to have a bunch of ugly `#if` guards or other logic to
   support both opaque pointers for users with llvm >= 16 and also
   typed pointers for users with llvm <= 14, until such time as our
   LLVM minimum is at least 15, which I expect is not a reasonable
   assumption for at least a couple years.)

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---

