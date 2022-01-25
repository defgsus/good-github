## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-24](docs/good-messages/2022/2022-01-24.md)


1,707,193 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,707,193 were push events containing 2,681,078 commit messages that amount to 221,071,360 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [epsilon-0/openbsd-ports](https://github.com/epsilon-0/openbsd-ports)@[b1bd329b8d...](https://github.com/epsilon-0/openbsd-ports/commit/b1bd329b8de5cf8ad30c1c58ad048622676a600f)
#### Monday 2022-01-24 00:00:23 by tb

databases/mariadb: Fix build with opaque EVP_MD_CTX and EVP_CIPHER_CTX.

A mariadb developer didn't like the fact that these structs need to be
allocated in OpenSSL 1.1 and added some insane hacks to work around
this. Adjust the code to cope with that the same way as it is done for
OpenSSL.

LibreSSL doesn't provide the means to override malloc and friends, so
the runtime check cannot be adapted. Use generous estimates for the
sizes for these structs instead.

With opaque EVP_CIPHER_CTX, EVP_CIPHER_CTX_buf_noconst() needs to be
provided by libcrypto, so disable this and a few other API redefinitions.

---
## [blessedmulligan/tgstation](https://github.com/blessedmulligan/tgstation)@[4610f700eb...](https://github.com/blessedmulligan/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Monday 2022-01-24 00:25:09 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[506c285081...](https://github.com/repinger/exynos9611_m21_kernel/commit/506c28508124772c92b1b2c16e5a4f0d22fa7683)
#### Monday 2022-01-24 02:12:13 by Christian Brauner

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
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[ae270b7f91...](https://github.com/Zeodexic/tsorcRevamp/commit/ae270b7f912253ca15c59412ca1fd6cbcfca3c92)
#### Monday 2022-01-24 03:24:02 by RecursiveCollapse

Kraken Revamp Part 2 + Early SHM rebalancing

Added Ink Geysers attack
Tweaked damage values
Now telegraphs with dust before it fires its Plasma Orb attack, and that attack fires 2 more projectiles

Heavy changes to several weapons which were very serious outliers:
Dramatically buffed Ancient
*Dramatically* buffed Heaven's Tear 1 and 2.
Dramatically nerfed Celestial Lance
Moonlight Greatsword now does 8x its former damage. It's still pretty awkward to use, like all broadswords.
Moonlight Greatsword no longer *reduces* damage if you have a magic damage penalty (like from the melee shields...)
Greatly increased laser reach of Focused Energy Beam to make it more viable against SHM bosses

Changed Fog tooltip to work in reverse, since most players are not going to be using legacy mode
Nerfed Crystal Knight, because they really needed to chill the fuck out

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[a88c950352...](https://github.com/cyberitsolutions/bootstrap2020/commit/a88c950352b79f7f7b4c2c7adf77e3690e36dcbd)
#### Monday 2022-01-24 04:44:54 by Trent W. Buck

inkscape doc: remove unusable 0.91 extension hooks

16:23 <twb> 16:22 <twb> So now that the help URLs are implemented in C++ instead of python "extensions", I can't see how to change the URLs from https://X to file:///Y without recompiling the entire inkscape package
16:24 <twb> https://sources.debian.org/src/inkscape/1.1.1-2%7Ebpo11+1/src/verbs.cpp/#L2051-L2101
16:27 <twb> I put "echo "$@" >/tmp/delete-me" at the top of /usr/bin/xdg-open, and Inkscape > Help > Manual does not cause /tmp/delete-me to exist
16:27 <twb> So can't hook it there
16:29 <twb> ron: I want you to say "yes, I accept this regression".  Inkscape's documentation is all online.  To keep [REDACTED] happy, we hacked it so Inkscape's Help menu would open local copies we downloaded.  I can still download, but I cannot hack the menu anymore.
16:29 <twb> ron: so if $site wants inkscape help to work in Debian 11, they will need to have internet, and whitelist stuff in squid access rules
16:30 <twb> The only "show stopper" one I think is really annoying is: https://inkscape.org/doc/keys-1.1.x.html
16:30 <ron> ah, I'm fine with whitelisting the inkscape doc
16:30 <twb> OK cool
16:30 <ron> implying they must have net access
16:30 <ron> [REDACTED] misses out
16:30 <ron> boo hoo
16:31 <twb> The other compromise thing I could do is make a start menu item "Inkscape Documentation" that just opens chromium.
16:31 <twb> That's not hard
16:31 <mike> twb: Did you try exo-open instead of xdg-open? That's the other one I see pop up every now and then
16:32 <twb> AFAIK xdg-open is what runs exo-open
16:32 <twb> I was doing a quick-and-dirty test on my gnome environment so I didn't test that
16:33 <mike> xdg does call exo, but doesn't mean things can't call it directly
16:34 <twb> fair
16:34 <mike> It definitely honours XFCE's "preferred applications" setting. Inkscape opened Chrome, then I changed it from Chrome to Chromium and Inkscape opened Chromium
16:34 <twb> I don't *really* want to intercept every call to xdg-open/exo-open anyway
16:37 <mike> twb: Got this by stracing it: [pid 174670] execve("/bin/sh", ["/bin/sh", "-e", "-u", "-c", "export GIO_LAUNCHED_DESKTOP_FILE_PID=$$; exec \"$@\"", "sh", "exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x5596c8443910 /* 54 vars */ <unfinished ...>
16:37 <mike> Which then called this: [pid 174670] execve("/usr/bin/exo-open", ["exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x564af10ac068 /* 55 vars */) = 0
16:37 <twb> mike: ah thanks
16:37 <twb> So OK we can fix this
16:37 <mike> Not worth digging any deeper into that path
16:38 <mike> We could wrap exo-open, yeah
16:38 <mike> Not sure I like it, but it's viable

---
## [Null-LLC/NullClient](https://github.com/Null-LLC/NullClient)@[dcb6731698...](https://github.com/Null-LLC/NullClient/commit/dcb6731698068490cf55d943e8b06d058e82a556)
#### Monday 2022-01-24 06:14:45 by FiRe

Accuracy++;

ABSOLUTE FUCKING PAIN WILL NEVER DO THAT SHIT AGAIN, NEARLY BASHED MY HEAD INTO A WALL

---
## [sonusainier/ControlFloorAgent](https://github.com/sonusainier/ControlFloorAgent)@[11fbfc5321...](https://github.com/sonusainier/ControlFloorAgent/commit/11fbfc53212c050b11a4730fa85e3decbd99f2a1)
#### Monday 2022-01-24 07:37:33 by David Helkowski

Cleanup

I've changed the Copyright notices in the Facebook files slightly to be "Facebook Inc." instead of "Facebook, Inc.", since the form with the comma makes no sense.

Also changed the idiotic "Copyright [year]-present" to be "Copyright [year]". That isn't how copyright notices work. You have to put the year. It just looked ridiculous.

---
## [larsbrinkhoff/its-archives](https://github.com/larsbrinkhoff/its-archives)@[a028f03eaf...](https://github.com/larsbrinkhoff/its-archives/commit/a028f03eafd511db3980177fa1b1abbdc1d3d9de)
#### Monday 2022-01-24 08:55:52 by Lars Brinkhoff

AI lab Type 340 indicator panel.

Photo by Jeff Del Papa.
Source: https://www.reddit.com/r/vintagecomputing/comments/fdpy2s/status_lights_digital_decus_model_30_display_from/

Comments:

The display was a round screen about 16” (40 cm) in diameter,
monochrome green, vector display.

This panel was saved from the one connected to the PDP-6 at the MIT AI
lab/ Project MAC. It was still in service in 1973, when I got a chance
to play spacewar on it. By then they had patched in a small controller
box, you didn’t have to operate the front panel switches, like on the
PDP-1 original.

...

You are correct on the display type, it was a bit of brain fade on my
part. I am not sure when the -6 failed, by the early ‘70 it was
already pretty flakey.

The [Spacewar] controllers I remember were wooden boxes, with a
pressed hardboard front face. they had spin left or right, thrust, a
firing button, and there was a way to get to “hyperspace”, don’t
remember if was it’s own button or the result of hitting a
combination.

The machines were decommissioned in the early ‘80s, and the corpses
(less some parts turned into mementos) went to the Cambridge
electronic surplus dealer “Eli Heffron”. My brother worked there and
snagged the panels for me. I also have a card from one of the
machines, but It is in a box somewhere. They will go to the Computer
Museum when I am gone.

...

The switch panel of the PDP-6 received a similar dated engraving, and
was given to Minsky.

...

I was a regular visitor (a tourist by the local idiom) during my
junior and senior years of high school. I used the ITS machines, but
spent most of my time at the LOGO lab. I continued to use the ITS
machines while I was in college (not MIT), and for the next few years
to get email. For a year or so, I had cstacy as a housemate, which had
good points (he came with a terminal, and 1200 baud modem), but also
some drama, at one weekend we got harassing calls by a then teen aged
Mitnick.

...

I don’t remember the [Dazzle Dart] game, that may have been
later. When I was there, the big development was adding floating point
arithmetic to the language. For the first year I used it, it was
integer only. It was native timesharing, the various terminals all
just gave a language prompt.

I really was into playing with the various bits of hardware they had,
including a 4 voice music maker, some digital breadboards that could
even be connected to the -11 and accessed from the language, and of
course the turtles.

...

As far as I remember, [Cstacy] spent his time keeping the ITS pdp-10
machines running, along with adding to the MIT CADR’s version of the
lisp machine system. In particular he had a role in getting the ITS
machines from the old arpanet 256 fixed host table protocol to actual
TCP.

For the outsiders, a bit of lisp machine history....

By that point, the lisp machine software had branched into 4 separate
streams. Besides the MIT specific version, LMI had one (hardware was
closest to the MIT design), TI had its own hardware , with its own set
of extensions (calling a subroutine was completely different), and
Symbolics, who had the biggest team working on it, their changes
included adding 4 bits to the data paths (36, rather than 32 bits
wide) to make it capable of using full 32 bit addressing. (the others
only did 28 bit addressing) the rest of the bits were for tags.

...

I was playing in the logo lab 73-75 as a high school student. I knew
that SITS was on the pdp-11, I assume on the 11/45 that had run the
standalone multi-user logo, was what turned into the SITS machine, but
I never used it either. By 79, I was working, and didn’t have time to
go hack on logo, I just used the MIT machines as an email host over
dialup.

...

The switches may well have been added by the local denizens. They did
heavily modify things, including adding the memory management hardware
to the KA’s.

---
## [jvdlem/PGD-GAMEJAM-2](https://github.com/jvdlem/PGD-GAMEJAM-2)@[8cb099aa19...](https://github.com/jvdlem/PGD-GAMEJAM-2/commit/8cb099aa19bce32be81dbcd72d30078efcbd5730)
#### Monday 2022-01-24 09:32:49 by Terdirk12

2nd big fix lets goo

-fixed elevator not opening in a build
-made coins go to the player faster (why were they so gosh darn slow)
-enemies now come at you from across the room (no more cheaky sniping)
-fixed some nullreferences in the pistol
-currently the roof of the cave system is gone but that be cuz some rooms need to be fixed (jordi knows which ones)
-added some light in the boss room so that you can actually see which eye is opened
-made the scope material less metallic for a more clear picture
-scaled back a previous fix for button presses from 10 units to 2 units
-made the builds development builds for now just so we can see where what goes wrong.
-dm me "i have read ur long ass shit" if you have actually read my long ass shit. -Dirk :D

---
## [envoylabs/whoami-ui](https://github.com/envoylabs/whoami-ui)@[ce405baf67...](https://github.com/envoylabs/whoami-ui/commit/ce405baf679d9971288a61c78a69f76171c42855)
#### Monday 2022-01-24 09:56:05 by the-frey

Basic messaging (#96)

* basic msg list

* maybe cracked the cofx thing

* whatever, fuck it

* resolve the stupid type issues

* Make short token page work - needs refactor

* i am once again asking for you to bloody compile

---
## [CapitalHitman/Dell-IPMITool-GUI](https://github.com/CapitalHitman/Dell-IPMITool-GUI)@[1d71403e6e...](https://github.com/CapitalHitman/Dell-IPMITool-GUI/commit/1d71403e6e9e860fdc2d8b8648c14ed5dafbc8a1)
#### Monday 2022-01-24 11:01:18 by sfremeau

Finally returing to this project. Worked on some stuff and i think i have a way to finally make the tabs work properly. added a ton of stuff tonight i honestly dont remember exactly what i did.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8f32cbe38d...](https://github.com/tgstation/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Monday 2022-01-24 11:59:14 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [inmanta/inmanta-core](https://github.com/inmanta/inmanta-core)@[32c3945f2f...](https://github.com/inmanta/inmanta-core/commit/32c3945f2f3669e6b4c118f04e5f03b770dfa2cd)
#### Monday 2022-01-24 14:27:34 by Sander Van Balen

Configured tox to generate junit xml for pep8 failures (PR #3655)

# Description

After countless times having to parse the unreadable jenkins output for flake8 errors I thought I'd make an attempt at improving the reporting. This PR is a suggestion to have tox produce a junit report, which can be interpreted by Jenkins just like the pytest junit report.

The good:
- it's a lot easier to find pep8 violations: compare [this overview for a dummy error](https://jenkins.inmanta.com/job/core/job/inmanta-core/job/flake8-junit-experiment/3/) with the [console output for a similar error](https://jenkins.inmanta.com/job/core/job/inmanta-core/job/issue%252F3623-modules-update-dependencies/5/consoleFull)

The bad:
- it's a bit of a hack
- it makes use of a library that is no longer maintained to generate the junit xml

I believe this could be a useful addition. If the library some day becomes incompatible we can always simply drop it again since its only a dev dependency. What do you think?

In its current implementation the flake8 errors are completely removed from the console. I should be able to fix this easily but I wanted to get your thoughts on the PoC first.

# Self Check:

Strike through any lines that are not applicable (`~~line~~`) then check the box

- [ ] Attached issue to pull request
- [ ] Changelog entry
- [ ] Type annotations are present
- [ ] Code is clear and sufficiently documented
- [ ] No (preventable) type errors (check using make mypy or make mypy-diff)
- [ ] Sufficient test cases (reproduces the bug/tests the requested feature)
- [ ] Correct, in line with design
- [ ] End user documentation is included or an issue is created for end-user documentation (add ref to issue here: )

# Reviewer Checklist:

- [ ] Sufficient test cases (reproduces the bug/tests the requested feature)
- [ ] Code is clear and sufficiently documented
- [ ] Correct, in line with design

---
## [Taranchuk/CombatExtended](https://github.com/Taranchuk/CombatExtended)@[e9c4ac2915...](https://github.com/Taranchuk/CombatExtended/commit/e9c4ac29158608d0b4d0349dd2984784d954fba2)
#### Monday 2022-01-24 17:40:21 by AL9000

mortar

"You know what, fuck you!"
*replaces mortar def*

---
## [elliottoille/sepcha](https://github.com/elliottoille/sepcha)@[a5a3a0b73c...](https://github.com/elliottoille/sepcha/commit/a5a3a0b73c908cf6591f1a40b5807a943b088c09)
#### Monday 2022-01-24 18:28:50 by Elliot Lewis

motherfucker stupid shit dont work at all, new plan

---
## [gitster/git](https://github.com/gitster/git)@[63c5753c6f...](https://github.com/gitster/git/commit/63c5753c6f04c1c4daff08f67de77c81ceecaba0)
#### Monday 2022-01-24 18:37:27 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2c28556dad...](https://github.com/mrakgr/The-Spiral-Language/commit/2c28556dad49e363c1334d4cfbf5667e4948b394)
#### Monday 2022-01-24 18:44:26 by Marko Grdinić

"11:30am. Done with chilling. Let me start.

Time to finish that tutorial.

11:55am. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273891/posts/4432201

Learned a bunch of hotkeys which will make using nodes smoother. This module is a cinch.

12pm. This is really useful. If I had the money, I'd honestly buy the guy's courses. I wish they weren't all 50-100$. If they were 10x cheapter I'd be tempted to use my meager savings for them. Still, just by learning these basics I've already greatly benefited.

12:45pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273891/posts/4432460

Only 3 more. I can do this before breakfast.

1:05pm. Done. I am finally done with the core essentials course. Now I'll be able to move to the modeling stuff from this guy. At this point I should be decently familiar with Houdini's UI. Now I just have to get familiar with nodes. This will be a matter of hunting down the examples for the SOPs. At this point I've been studying Houdini for a week. A few months of practice like with Blender, and I will be quite proficient at it. At that point I will be able to create large scale environment using the power of programming. This will hugely enliven Heaven's Key.

I could have tried making it with just text, but that would just be scrambling at the bottom. Also just writing has very little opportunity for skill development. I'd just be spending my time sampling my subconscious and get burned out over time. But by taking this route, I'll stand out and have an edge to go from beyond complete obscurity.

1:15pm. Let me have breakfast and do the chores. After that I'll do the modeling vids.

2:55pm. Time to resume. Right now, let me go through the modeling vids by the same author of the course.

https://www.sidefx.com/learn/collections/understanding-houdini-modeling/

The regular stuff was already included in the course, what I need are the curve vids. No doubt that will cover how to turn them into meshes and dealing with the radius.

https://youtu.be/SNDJzhOZZeg?t=56
The Anatomy Of Nurbs Curves

Let me follow this along as I go.

https://www.sidefx.com/tutorials/understanding-nurbs-curves-breakpoints-converting-to-nurbs/?collection=75

If I ever want to convert one curve type to another, I shold remember the fit node.

3 more of these. I do not think it will explain how to convert curves to meshes.

https://youtu.be/laSOxJlEIJI?t=189

Oh, so this is the factor. Now I need to understand how to make use of it.

3:55pm. My bro just came into my room asking me whether it is good time to buy TSLA. He must be really bored to do this, given that he does not even have a broker's account. I said some nonsense about needing to have a trading strategy and rambled on, and he lost interest. That should be it for that. Well, if he manages to get some savings, I will serve as his advisor pro bono. Though just the 5k minimum is not something he liked hearing about, nor that it only makes sense to start investing once you have a year's worth of savings.

4pm. I got distracted. Focus me.

4:15pm. https://www.sidefx.com/tutorials/understanding-nurbs-curves-parameterisation-chord-length-centripetal/?collection=75

Sigh, I am dying here.

https://youtu.be/oSaFB_mXJhQ?t=34

This is so boring. I was wrong. Instead of watching these tutorials, what I should do is watch the plant tutorial. Since I know the basics, I really need some examples of Houdini in use. If I could follow that plant tutorial along for example, I'd learn a massive amount. I only learned geo nodes because all the time I spent watching tutorials earlier in the month.

This stuff I am learning here is too basic and I need to study complete projects.

4:25pm. Gahhh, I am thinking about TSLA. Ok, here is the strategy. Since the market is correcting, it is going down with the rest, but I think the stock is fairly resilient given its position. One option is to buy it now and hold it for a month. Another option is to sit out, and wait a month. What might happen is that the stock could recover very quickly ahead of the market. If that happens it could break out out again within a month and go up 50-100%.

If it recovers very quickly that would be a strong signal. These two patterns should chain into one another.

As a matter of principle, whenever you are in the market, you should expect strong momentum on a monthly basis. When you get out, you need to stay out for at least two weeks and only come back in if it looks like the market strong.

These kinds of timing based trading rules are good for being in sync with the market. To make excess returns using such a strategy what is necessary is to be in strongest sectors, or leader stocks such as TSLA. BTC was a leader during the last upswing, but right now it is the opposite. The same goes for funds such as ARKK.

My bro is a too inexperienced to focus on individual stocks. A trader focusing on individual stocks is like a poker player focusing on individual hands. A proper plan does not care about the vehicle and hops from one to another instead with the right frequencies.

I didn't make this mistake during my trading days, but I was too naive regardless. I thought that there would be strategies better than the one I described above. I wanted to be consistent day in and out, but that is impossible, unless you are doing skulldudgery, you have to endure the variance that comes to day to day price movements. The days when you could just follow the short term momentum are long past.

During my trading days, I spent al ot of time watching stocks making new highs, so I understand well enough that consistent price movement for any particular stock is very rare.

Things like BTC where you have predicable momentum are very rare exceptions. The reason why they are exceptions is because the world's attention is on them, something which most stocks do not have.

Today Elon's companies are at the height of their popularity. Tomorrow, something else will be in the limelight.

4:35pm. Let me get back to studying art.

Let me summarize. I think, that today might be an ideal time to either buy TSLA or tech stocks in general. This garden variety correction is not to be feared. What is to be feared is the market starting to lag in the following weeks and months after that. If that starts to happen, you need to stay out for a month and be on the lookout for strength. If it does not manifest, stay out for longer.

Rules such as these for example would have saved you from going down with ARKK or TAN. ARKK is getting crushed right now. It is definitely to be stayed away from.

https://youtu.be/oSaFB_mXJhQ?t=181

It is really difficult for me to pay attention to this.

4:55pm. Let me take a break to read the Baki raws. My attention span has been shot. I can't stand this anymore. The way I am studying Houdini is ridiculous. Courses like these might be thorough, but they sure are boring.

I should pick that 1h plant tutorial or the spire tutorial and studying them from start to finish. Sigh, I'd hoped I'd at least be able to learn how to convert the curve to a mesh given a profile, but that was not meant to be.

5:10pm. https://www.sidefx.com/learn/world-building/

This here is what I am interested in directly.

Mhhhhh...

Ok, let me do it. I'll move on to more practical tutorials starting from here.

I really wanted to do things myself rather than watch even more stuff, but it can't be helped. I simply don't know enough to even get a start at this point. Let me do the plant one. I'll follow along and try out the nodes myself.

https://youtu.be/GxKfKvYu7VU
Plant Growing animation | Houdini Full Tutorial

6:05pm. Had to leave for lunch. Right now I am looking at the add node example.

6:10pm. Sigh, not only does Houdini have a large number of nodes, each of those nodes is very complex as well. I thought add would be straightforward, but these examples are ridiculous. The way he modeled the leaf is mistifying to me as well. It is not at all obvious how the sweep node works.

6:20pm. Hrrrmmmm...I am not sure where to start. Maybe I should just ask.

After watching it for 5m, I think the plant tutorial is too complex for me to start with.

6:20pm. https://www.sidefx.com/tutorials/procedural-modeling/?collection=66

Hmmmm, this seems really good. There is a mesh and there are some pins distributed on top of it.

https://www.sidefx.com/learn/collections/introduction-to-houdini-1/

I see a staircase amongst the tutorials here. That might be something.

6:30pm. Ok, let me focus on this.

https://www.sidefx.com/tutorials/games-quickstart/

I'll leave this for later. What I want is quite similar to what game artists want, so that I should focus on Houdini for those kinds of use cases.

6:45pm. This stuff where he uses the bounding box to do group selection is interesting. Let me finish watching this video and I will call it a day. The tedioum of the hipflask tutorials took it out of me. What I need to do next is start going through game asset tutorials as well as the rest of this series. I just can't seem to get a start with Houdini, but effort and perseverance will see me through.

Group by range is similar to endpoint selection.

7:05pm. At 54:10 where he is grouping based on the normals is one of the things I've been wanting to find. When making that city, I thought about starting with a mountain, and setting the buildings only on upright areas. This would be an ideal way to make such a selection. Of course once I have the group I'd need to  straighten the areas, but that should be possible.

7:10pm. Oh, it is possible to scatter by density. I completely missed this.

7:15pm. I bet he will invert the range, and set end to 1...Yep.

7:20pm. https://www.sidefx.com/tutorials/attributes-and-copy/?collection=66

I'll resume from here tomorrow. Hopefully I can get some actual modeling skills from here on out. Despite being at it for a week, what I can do right now is extremely rudimentary, but by the end of the month that should change. i should be able to figure out how to distribute parameterized instances soon enough. And after that I'll be able to benefit from the the things Houdini can do that I can't even imagine now.

7:30pm. Unlike Blender, Houdini can be in fact considered a programming language. I am glad to try going down this path.

It does not matter that I won't make my money through programming. The only programming worth doing is AI, and nobody is doing that at this point in time. Since that is the case, I should focus my attention on manipulating humans rather than machines. And that is what I am doing. Once I have some skill in this, I might be able to solve my insolvency problem. It is ridiculous that I have all these programming skills, but no way of profiting from it that would not involve subordinating myself to other people.

If I had actual AI understanding, I bet those would not be my only options.

I only need just a little bit to initialize myself. I am absolutely going to master this and become capable of making my own game art and music. Nothing is going to stop me in this.

Rather than weakening because of my failure, my willpower is only getting stronger the more I train it. I could do this for decades. And by the end of this year, I will have what I need to reach financial independence. With my stories I'll bring chaos to this world. The Singularity is taking too long, so I might as well put come coal into the fire in order to hurry it along.

7:40pm. Right now, my pressure is sky high so let me unwind. I'll figure out how to do something interesting in Houdini tomorrow. Today at least I am done with figuring out the UI."

---
## [AOSPA/android_kernel_oneplus_sm8350](https://github.com/AOSPA/android_kernel_oneplus_sm8350)@[a9f7615468...](https://github.com/AOSPA/android_kernel_oneplus_sm8350/commit/a9f7615468bed492d275d34c3c4db4653f5cce55)
#### Monday 2022-01-24 19:00:20 by alk3pInjection

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
## [UnNetHack/UnNetHack](https://github.com/UnNetHack/UnNetHack)@[275272a84a...](https://github.com/UnNetHack/UnNetHack/commit/275272a84a6f3f1405c4a02c6f3b34cdecaafbb2)
#### Monday 2022-01-24 19:20:53 by copperwater

Scroll of remove curse becomes learned when items' curses are removed

The scroll of remove curse is trivially identified by checking inventory
after reading it to see whether anything became uncursed. This leads to
annoying tactics like remembering which scroll you just read so you can
go call it "remove curse" on the discoveries list.

This simply autoidentifies it when an item that was known to be cursed
has its curse removed.

Cherry picked from nethack/nethack@e13b1833cc

---
## [MrJohnnyAppleseed/NEPS](https://github.com/MrJohnnyAppleseed/NEPS)@[8a69c714ea...](https://github.com/MrJohnnyAppleseed/NEPS/commit/8a69c714ea0126844bdd16756e154d58347ece4d)
#### Monday 2022-01-24 19:21:20 by MrJohnnyAppleseed

Fix crashing bug

We all know that when all Terrorists die and manage to plant the bomb, they all begin to spectate the bomb. When that would happen, it would cause the cheat to read the eyeangles of the bomb, which would just result in an error and a instant crash. This should add a check to prevent this bug from occurring again.

---
## [Mezque/VRCXThemes](https://github.com/Mezque/VRCXThemes)@[6ffda6c976...](https://github.com/Mezque/VRCXThemes/commit/6ffda6c9761fadfef0cc33c1c03dd1f4937b67a1)
#### Monday 2022-01-24 19:21:29 by Mezque

Themed the part with hex user names, themed the log in screen

Holy Ghost. Now the God of hope, through the power of the power of the God of hope, through the Holy Ghost. Now the Holy Ghost. Now the Holy Ghost. Now the power of the power of the God of hope, through the God of hope, through the God of hope, through the power of the Holy Ghost. Now the God of hope fill you with all joy and peace in believing, that ye may abound in hope fill you with all joy and peace in believing, that ye may abound in hope, through the power of the power of the power of the power

---
## [kyle-sallee/ascript](https://github.com/kyle-sallee/ascript)@[7e41cb03e9...](https://github.com/kyle-sallee/ascript/commit/7e41cb03e905b50e110141b3598cc10326b4321b)
#### Monday 2022-01-24 19:25:25 by Kyle Sallee

Seems two years elapsed
since the duration required
to edit/revise ascript last existed.
In file version.make the version is contained.
I will change the version now.
Perhaps later when finialized I will tag it.
Depends upon how much time and concentration
I can allocate to programming.
At this point binary API has not changed.

Running low on $$.
Must pay HOA.
Must pay TEP.
Good not to be homeless.
Bad to have bills and $0 income.

HR staff lack the skills to identify a computer programmer
let alone an elite programmer from the 20th century,
skilled in 8086 through AMD64 asm.
They do not even know what asm is.

"What type of assembly line did you work on, Mr. Sallee?"
"I never worked on an assembly line,
because asm is the mnemonics for the opcodes that
are a CPU's native language."
The HR person falls asleep,
because the meaning for opcode is not known.

Their lore and inability to assay programmers solicits pity.
They have a task/occupation and yet are truly unable to perform it.

My constantly pinched nerve changed.
I used to suffer daily horrific agonizing back pain.
Now my left arm/hand exudes pain, numbness, noise.
That seems like a lucky change.
Left arm and left hand hurt.
It's annoying.
But, I can concentrate better.
I can move better.
I do not type better.

I seem to again be able to sustain
the concentration required
to write some extremely awesome code.
My nerves from my back back when pinched
concentration, even walking, was problematic.
Arm pinched nevers are painful, but less annoying.

I was testing the ability with argot ko new
As compared with argot ko
the new code looks cleaner,
the functions seem smaller,
the opcode use seems less,
the speed seems better,
reading comprehension seems easy.

Perhaps that ability was being hindered
by the back pain, but not so much by the arm pain?
I am feeling excited.

I am done ranting now.
If I didn't write it in my blog
then I wanted to document
my current health change somewhere.
My health loss and chronic back pain
that inhibited my concentration
ended "Sorcerer" development.
I struggled 7 years to author "ascript,"
to regain the lost ability.
But I also wanted "ascript"
It is the tool that I always desired
for powering a POSIX, because
ascript is so easy, fast, and does
everything required to boot.
I only wish the quality could match
what I can currently do,
but it seems too much to entirely revise.

---
## [dotnet/maui](https://github.com/dotnet/maui)@[ac6befcbee...](https://github.com/dotnet/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Monday 2022-01-24 19:34:51 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [mashupstudios/dungeons-and-blasters](https://github.com/mashupstudios/dungeons-and-blasters)@[8e16d1f57c...](https://github.com/mashupstudios/dungeons-and-blasters/commit/8e16d1f57ce94e7702d67d4233bb3b630673284d)
#### Monday 2022-01-24 19:35:09 by Lostmaniac9

Balance Patch - notes in comment

Minigun:
spread from 5.1 to 4.7
damage from 7.7 to 9.9

Inverse Dimension:
damage reworked
initially did 9 damage every hit
now does 6 damage on initial hit
and 12 damage per cloud hit
this might be a buff
I don't know what I thinking when I made this change

Pew Staff:
damage from 12 to 17

Sextuple Burst Rifle:
damage from 12 to 16
firerate delay from .6 to .9 seconds as was the original intention

Poison Staff:
removed unintended visual effects

Rocket Launcher:
damage from 16 to 26 to account for falloff on explosion damage which was not  done before

Spell Bomb:
damage falloff on explosion from 1.1 to 1.12

Shotgun:
damage from 7 to 10

Cometfall:
damage falloff on explosion from 1.1 to 1.2
please stop spamming this thing I seriously can't take it any more I can't live like this any more knowing what I have done to this world and the people in it

Ogre:
explosion radius from 3.5 to 4 because fuck you and everyone near you
added 1.1 falloff damage on the impact of the projectile
explosion lifetime from .5 seconds to .2

Infernal Ogre:
explosion lifetime from 4 seconds to 3 seconds

Enraged Berserker:
movement speed buff from 25% to 17%
damage reduction from 45% to 40%
made "temporary" spawning buff a permanent effect

Berserker:
movement speed buff from 30% to 25%
damage reduction from 45% to 40%
made "temporary" spawning buff a permanent effect
cry

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[ef83742269...](https://github.com/NetBSD/pkgsrc/commit/ef83742269654fb58ddf6880fe1e24f8ec9dea08)
#### Monday 2022-01-24 19:39:51 by micha

x11/xlockmore: Update to 5.68

This update should fix CVE-2006-0061 if option "pam" is disabled.
OK from wiz@.

5.68
  Updated xscreensaver port for xscreensaver-6.02.
  Various NetBsd install issues fixed including config.cygport.
  pam vulnerabiliy patch added thanks to Elmar Hoffmann, elho AT elho.net.
    Card vulnerability may remain, see README.
  module fixes for deluxe, eyes, starfish, swirl, text3d2, module use is
    still experimental.
  biof mode removed again (though was not building by default).

5.67
  Fixing specified bound equals destination size warning in iostuff.c.
  Port updated for xscreensaver-6.01.  With help from EoflaOE ViceCity.
     Also removed some warnings.
  maze3d.c updated for VMS as CRTL now contains more standard functions,
    thanks to Jouk Jansen.

5.66
  GL mode atunnels, juggler3d, atlantis, lament, invert, solitaire, text3d,
    and text3d2 fixed up by EoflaOE ViceCity and myself to build in
    xscreensaver.
  bomb, helix, lightning, penrose, petal, scooter fixes for xscreensaver
    port (clear screen issue).  Clock fixed to run by changing a spot from
    "Clock" to "CLOCK".
  A few updates from xscreensaver-5.44/hacks/xlockmore.c for xscreensaver
    port.
  Duplicate resources and unloadable resources for xscreensaver port fixed
    by EoflaOE.
  Double free removed for xscreensaver port fixed by EoflaOE and myself.
  Removed some warnings in xscreensaver port in fzort, rubik, skewb, and
    sproingies.
  Xpm textures added to xscreensaver ports that need them.
  image, puzzle, decay, bat now work but use xscreensaver bitmap/pixmap
    in xscreensaver port.
  Bug fix in qix and toneclock for xscreensaver port, xlock was not
    affected by negative NRAND input.
  euler2d synced up with xscreensaver version.
  Change to fzort to use __asm__ instead of asm as its probably more
    likely to work.
  Fixed solitaire so deckPile changes just a little bit as it doles
    out cards.
  Updated bomb to use size 18 font when USE_MB is not set as it seems
    34 is not widely available anymore.
  pacman now has different colored ghosts (no green ghost) and also
    oscillating dress and eyes.  See README for a notice for this mode.
  Fixed some bad drawings in solitaire and pacman noticed on
    Windows side.
  Warnings removed for -Wstrict-prototypes -Wmissing-prototypes
    -Wdeclaration-after-statement

5.65
  Fix from Jan Kratochvil and Adrian Reber, adrian AT lisas.de for Fedora.
    xlock -startCmd true... would core on Fedora, exit() replaced with
    _exit().
  Update for magick.c to use strncpy thanks to Jouk Jansen.

5.64
  Fix for hyper mode from original author, for potential but not
    likely memory leak and free(NULL) issue John Heidemann, johnh
    AT isi.edu.
  More buffer gcc warnings removed for dclock.c, image.c, and
    scrnsave.c.
  ras.c/magick.c gcc 10 fix from Adrian Reber, adrian AT lisas.de .
    VMS already handles this in make.com.

5.63
  Lots of spelling errors fixed due to codespell
    https://manpages.debian.org/testing/codespell/codespell.1.en.html
  A few more gl modes (molecule, invert) fixed up by
    EoflaOE ViceCity to run in xscreensaver.
  Added additional changes to solitaire and invert.  invert will
    build in xscreensaver with some coaxing, see README in
    xscreensaver directory.
  Removed buffer gcc warning about nose.c.

5.62
  Fix from brett.diamond AT gmail.com to get "xlock -help" from
    crashing.
  As a Blake's 7 fan, I had to add the Liberator to star mode.

5.61
  Same fix from Jouk Jansen and Adrian Reber, adrian AT lisas.de
    for juggler3d.cc in previous release.
  Change from Denys Vlasenko (thanks to Adrian Reber for pointing out)
    https://bugzilla.redhat.com/show_bug.cgi?id=874484
    This helps xlock's parent process to know xlock crashed.
  ico mode added truncated octahedron.
  Another  gl mode, sierpinski3d, fixed up by EoflaOE ViceCity to run
    in xscreensaver.

5.60
  Updated references to website to https.  https://www.sillycycle.com
  A few more gl modes (incl. maze3d, pipe, sproingies) fixed up by
    EoflaOE ViceCity to run in xscreensaver.

5.59
  Thanks to tobik, ohartmann AT walstatt.org, and Jason Helfman,
    jgh AT FreeBSD.org for xglock fixes for "failed due to signal" for
    clang.
  Syncing with xscreensaver and many modes modified, more than
    half working there.  pacman and puzzle run but need some
    obvious work, others run too fast or flash on the screen.
    Various fixes from Jouk Jansen and EoflaOE ViceCity.
    Updated GL modes also, inaddition to overlap: biof, skewb, and
    fire (needs images). See xscreensaver/README for new directions.
  Updated in linux to build with modules, must have broken somewhere
    down the line.  imake build fixed too.
  bomb mode fixed for xlock.

5.58
  Syncing with xscreensaver.  Much has changed since last time this
    was done and much left to do.  Nonglx "a"'s and some "b"'s done
    so far.  Automata modes like ant.c should use automata.c and
    automata.h supplied by xlockmore.
    ball bat not working right there yet.  Also bouboule to do right will
    require changes to xlockmore files from xscreensaver.
    See new xscreensaver/README for instructions.
  While testing uncovered old security bug in anenome mode and fixed.

5.57
  life updates to use a more standard notation for nontotalistic cellular
    automata.
  ax_pthread.m4 needed for autoconf, added back in, oops.
  Removed VMS caddr_t fix from matrix.c, cage.c, gears.c, glplanet.c,
    invert.c, juggler3d.c, lament.c, moebius.c, molecule.c, morph3d.c,
    noof.c, pipes.c, rubik.c, sierpinski3d.c, skewb.c, stairs.c,
    superquadrics.c as no longer needed.  Thanks to Jouk Jansen.
  boxed and maze3d modes added thanks mainly to Jouk Jansen.
  boxed added to xlock95.scr.  xlock95 Makefile now builds to 64 bit.

5.56
  Thanks to Jason Helfman, jgh AT FreeBSD.org for sound installation fixes.
  Thanks to Tobias Kortkamp, for his patch for glock compile issue with
     CLANG 6.0.0.
  Fixing warnings using clang for back.xpm, nose.c, passwd.c.
  Fixing errors using g++ for deluxe.c, also various casting added.
  Fixing potential some buffer overruns pointed out in mingw in
    apollonian.c and hyper.c.
  Fixing potential error of using null pointer thanks again to mingw in
    xlock.c.
  pyro2 was not showing anything on screen due to it not finding font,
    changed it to default to mode_font if can not find.

5.55
  Thanks to Dave Odell, dmo2118 AT gmail.com for his fzort mode update to
    use the functions in xshm.c and fixes crash when running X11 over network.
  Note from Dave Odell:
    <https://www.jwz.org/xscreensaver/xscreensaver-5.37.tar.gz>. MI_INIT() is
    defined and documented in hacks/xlockmore.h, with related functions
    defined in hacks/xlockmore.c.  MI_INIT() currently takes three parameters:
    the ModeInfo *, the state array, and a function pointer for the new free
    hook. FWIW, it could instead be just the first two parameters, with the
    free hook being set up like the other ModeHooks; this would be a bit
    nicer, I think. But I was going for something that could be applied
    incrementally to individual screenhacks in XScreenSaver, and could -- in
    theory -- be brought back to xlockmore with minimal impact.
  ant mode resync'd with xscreensaver...  Thanks to David Odell redoing my
    sad attempt.
  -sound configuration changed around so it should work on more machines,
    now uses DEF_PLAY and play.sh by default.
  Thanks to Stanislav Brabec, sbrabec AT suse.cz for his "hack" to fix for
    PAM with non-English locales.  He notes to fix properly a "Password"
    prompt list should be obtained at the initial phase of authentication.
    Added PAM_PASSWORD_PROMPT for using old way.
  Fixed leak in scooter thanks to Valgrind.

5.54
  Thanks to Dave Odell, dmo2118 AT gmail.com for his strange mode
    updates to include aligned_malloc.[ch], thread_util.[ch], xshm.[ch],
    and visual_pixmap_depth() from XScreenSaver.  Also updates for building
    macOS and Debian for crypt.  Made safe for VMS by Jouk Jansen.
  juggle fixed for multiscreens.

5.53
  Goofed on last VMS xmlock update.
  dclock fix for led bounce.  :)  Added to windows port but only graphical
    part.
  Windows port fixed petri black screen.  Added anemone and deluxe but turned
    off double buffering to get default black screen.

5.52
  Install changes for fortune. VMS xmlock build update.
  Thanks to Dave Odell, dmo2118 AT gmail.com for his strange mode
    updates.  New options -points N and -curve N .  Also now working
    for windows port (which led to bubble and ifs porting easily).

5.51
  life3d updates including a distinct 18 neighborhood using rhombic
    dodecahedrons (neighoborhood -18 as there is already 18
    neighborhood), and a 22 neighborhood using tetrahedrons, i.e. the
    tetrahedral part of alternated cubic honeycomb
  Less compile warnings and configure update.

5.50
  -messagefont was broken if USE_MB set (default from 5.42). E.g.:
    -mode dclock -messagefont "-*-times-*-*-*-*-18-*-*-*-*-*-*-*"
  Changed default message font to above.
  Should now compile with less warnings.
  spiral erase mode changed from 100 iterations to 8.

---
## [Utumno/wrye-bash](https://github.com/Utumno/wrye-bash)@[f3b16a92f9...](https://github.com/Utumno/wrye-bash/commit/f3b16a92f93ab4b3fcb405333f9e23e1c72a744e)
#### Monday 2022-01-24 20:41:53 by MrD

FName: EEE tests for FNDict

EEE test immutability - copies
EEE add del self.__dict__ to ci_body?

An initial version of this branch had Paths replaced with CIstr's. That
turned out to be highly unsatisfactory:

- CIstr I created to use internally in LowerDict - LD is the API, not
CIstr.
- body_ and ext_ wrappers are too slow - the code looked more ugly and
os.path.splitext (an expensive operation) kept proliferating
- those DataStore keys are really a beast of its own kind (corresponding
to filenames) and by the lesson this very branch teaches us better have
a specialized type for them
- turns out I wanted to keep Path's ability to compare with strings -
but I wanted this as efficient as possible - can't have slots
unfortunately but other than that given that FName *can only be
instantiated with unicodre strings* I was able to drop the
`if type is str` checks in FNDict dunder methods
- FName(CIstr) would be too much nesting and probably performance (lookups
of methods traverse the mro -TODO: time) - anyway FName is-not a CIstr

Check if FName should be the usual case in comparisons (try: except AE)
once I have scanned the code

SSS:

return None if None is passed (duh)

Backwards compat TTT  EEE move forward_compat_path_to_fn below FNDict

Well I kept adding backwards compat and even with dedicated functions:

@@ -428,6 +431,2 @@ def __repr__(self):
 # backwards and forward compat functions
-def backwards_compat_fn_to_path(di, value_type=lambda x: x):##: [backwards compat] drop in 312+
-    return {GPath_no_norm('%s' % k): value_type(v) for k, v in di.items()}
-def backwards_compat_fn_to_path_list(li, ret_type=list):
-    return ret_type(map(GPath_no_norm, map(str, li)))
 def forward_compat_path_to_fn(di, value_type=lambda x: x):##: [forward compat] drop 313+

this was getting out of hand  -  so:

@@ -378,2 +378,5 @@ def ci_body(self):

+    def __reduce__(self):##: [backwards compat] drop in 312+ (but still store strs)
+        return GPath_no_norm, (str(self),)

@@ -553,2 +552,5 @@ def __repr__(self):

+    def __reduce__(self): #[backwards compat]we 'd rather not save custom types
+        return dict, (dict(self),)

I think now I got them all :)
Note I pickle the cache factory (GPath_no_norm) - so when I load
settings I already cache the filenames - can't think of anything bad
(apart that this won't carry to pre GPath_no_norm  versions of bash -
that is pre 307 as 662423530ff1ba4219ed0b2cc91effd5306a5ca2 on 307, but
I don't think many people will update to 310 and then go back to 306)

Edit: was bitten bitterly by my smart idea (stays a smart idea, but).
So I was testing a bashed patch and some form ids had Paths instead of
FNames and this drove me nuts, had put breakpoints everywhere and still
couldn't find where these Paths were from - turns out we use deepcopy
(yes I used to know) and deepcopy will use __reduce__ if it's there.
This incidentally gave me an idea for optimizing the Path copies
currently.

squash! FN

@@ -394,5 +388,4 @@ def __eq__(self, other):
         except AttributeError:
-            if isinstance(other, str):
-                return self._lower == other.lower()
-            return NotImplemented
+            # this will blow if other is not a str even if it defines lower
+            return self._lower == str.lower(other)
     def __ne__(self, other):

eee test  deepcopy

squash! fe24d5da24b5a8694835e81cee307ddad94bde2a

Yey:

self = FName('path.txt'), other = bolt.Path('path.txt')

    def __eq__(self, other):
        try:
            return self._lower == other._lower # (self is other) or self...
        except AttributeError:
            # this will blow if other is not a str even if it defines lower
>           return self._lower == str.lower(other)
E           TypeError: descriptor 'lower' for 'str' objects doesn't apply to a 'Path' object

@@ -459,3 +459,3 @@ def test__eq__(self):
         # fname and paths
-        assert fn == GPath('path.txt') ##: Oops do we want this?
+        with pytest.raises(TypeError): assert fn != GPath('path.txt')
         # paths and None
@@ -470,3 +470,3 @@ def test__eq__(self):
         assert empty == ''
-        assert empty == GPath('') ##: Oops do we want this?
+        with pytest.raises(TypeError):assert empty != GPath('')
         for other in (b'', None, [], [1], True, False, 55):
@@ -505,4 +505,4 @@ def test_dict_keys(self):
         assert FN in fn_keys_dict # yey
-        assert GPath(file_str) in fn_keys_dict ##: Oops do we want this?
-        assert GPath(FILE_STR) in fn_keys_dict ##: Oops do we want this?
+        with pytest.raises(TypeError): assert GPath(file_str) in fn_keys_dict
+        with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_keys_dict
         string_keys_dict = {file_str: 1}
@@ -527,4 +527,4 @@ def test_sets_lists(self):
             assert FN in fn_set # yey
-            assert GPath(file_str) in fn_set ##: Oops do we want this?
-            assert GPath(FILE_STR) in fn_set ##: Oops do we want this?
+            with pytest.raises(TypeError): assert GPath(file_str) in fn_set
+            with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_set
             string_set = cont_type([file_str])

---
## [fesh0r/mame-full](https://github.com/fesh0r/mame-full)@[a49e215466...](https://github.com/fesh0r/mame-full/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Monday 2022-01-24 21:54:57 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [fulpstation/fulpstation](https://github.com/fulpstation/fulpstation)@[c449fbb56c...](https://github.com/fulpstation/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Monday 2022-01-24 22:08:31 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [Corvus-R/android_packages_apps_Launcher3](https://github.com/Corvus-R/android_packages_apps_Launcher3)@[82d37c3bb3...](https://github.com/Corvus-R/android_packages_apps_Launcher3/commit/82d37c3bb34e6f24198c737fc316a5f149f42493)
#### Monday 2022-01-24 22:30:02 by Alex Cruz

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

