## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-26](docs/good-messages/2023/2023-06-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,098,088 were push events containing 3,462,926 commit messages that amount to 281,119,334 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[a8e16030f8...](https://github.com/Lufferly/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Monday 2023-06-26 00:19:36 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care
## Why It's Good For The Game

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[5c032cc098...](https://github.com/Lufferly/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Monday 2023-06-26 00:19:36 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [Thaccus/Starbase-Nav-Suite](https://github.com/Thaccus/Starbase-Nav-Suite)@[3dd8fdaea4...](https://github.com/Thaccus/Starbase-Nav-Suite/commit/3dd8fdaea4b982ee26971cc3df4b78b854a48342)
#### Monday 2023-06-26 00:23:11 by Thaccus

Test Integration

The next release is right around the corner and this is how I start the approval process. This one is a general improvement pass focusing on QOL in installation and general  tweaks throughout the chips to speed them up and improve their workings. Test ship is built so that I can confirm that everything works out of the box, then I integrate it into a big boy ship for long term testing.

Notable changes: 
New chair, new sensor cluster, new brain cluster. Same stuff in total but fewer individual parts to slap on the ship. Should lead to fewer errors in assembly. All the usual modules still exist though so advanced builders can take things apart and put them where they see fit.
Generic states has been changed to always use the Human Input Detection system, and that part has been integrated into the chair.
The brain cluster now has a ship diagnostic scanner in it. I am not sure what I need it for, but there was room and I didn't want to put the FCUs under the MFCs as that would make them hard to tinker with.
Strafe arrest now remembers its state after you press the ESTOP button. I find that I have been using the ESTOP as a general brake and I want whatever I set my Strafe arrest to before hand to stay that way after I'm done with the stop.
Activation delay on the LDTS chip responsible for naming the Laser Desigantor-Sensor combo. This should allow the use of the :transponderOwner field to personalize the :SI names and better avoid nearby ship problems out of the box. You may still want to change them as it is easy for onlookers to figure out what the value is, but that was even more true before when it was always the same if you didn't change it. At least they are now unique per person so that multiple users that didn't do any personalization can play side by side.
Intertial Dampening has had some naming convention changes. Those have been propagated out to all affected systems.
Nav has been renamed Autopilot and has received an overhaul. It has faster loops, more tunable turning burns, and removed a lot of ifthenelseend ugliness.
The rotation matrix now calculates orientation every .6s on the single ship version rather than the 1s loop it used to be. Lxyz is now calculated over in CompassDisplayPrep.
Galacctic alighn has had the same orientation improvements made to it that Autopilot has.
I have also fixed a small cable that was not part of the chair module causing chairs to mysteriously not work when people moved them by the module. I meant to fix this ages ago...but life got in the way.

As always feel free to download the package and the test ship for your own testing and to provide any feedback. Every single new player I have seen has gone straight for the advanced stuff. The more eyes we get on these candidates the more likely they will be easy for new players to put on.

---
## [TheParasiteProject/frameworks_base](https://github.com/TheParasiteProject/frameworks_base)@[26db2cbb19...](https://github.com/TheParasiteProject/frameworks_base/commit/26db2cbb19dcb0356b64b42ee44271799fa138a5)
#### Monday 2023-06-26 01:05:21 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[64eae49042...](https://github.com/Ghommie/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Monday 2023-06-26 01:14:45 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [mcdofrenchfreis/biofrost-kernel-realme-trinket](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket)@[0bfdc99d51...](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket/commit/0bfdc99d516c14ecddf64e870d1465397c2a44f2)
#### Monday 2023-06-26 01:16:49 by Christian Brauner

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
## [Maxwell-Guo/scylla](https://github.com/Maxwell-Guo/scylla)@[be8ef63bf5...](https://github.com/Maxwell-Guo/scylla/commit/be8ef63bf503da88c55cd0ec84514d9e31db019f)
#### Monday 2023-06-26 01:41:00 by Jan Ciolek

cql3: remove expr::token

Let's remove expr::token and replace all of its functionality with expr::function_call.

expr::token is a struct whose job is to represent a partition key token.
The idea is that when the user types in `token(p1, p2) < 1234`,
this will be internally represented as an expression which uses
expr::token to represent the `token(p1, p2)` part.

The situation with expr::token is a bit complicated.
On one hand side it's supposed to represent the partition token,
but sometimes it's also assumed that it can represent a generic
call to the token() function, for example `token(1, 2, 3)` could
be a function_call, but it could also be expr::token.

The query planning code assumes that each occurence of expr::token
represents the partition token without checking the arguments.
Because of this allowing `token(1, 2, 3)` to be represented
as expr::token is dangerous - the query planning
might think that it is `token(p1, p2, p3)` and plan the query
based on this, which would be wrong.

Currently expr::token is created only in one specific case.
When the parser detects that the user typed in a restriction
which has a call to `token` on the LHS it generates expr::token.
In all other cases it generates an `expr::function_call`.
Even when the `function_call` represents a valid partition token,
it stays a `function_call`. During preparation there is no check
to see if a `function_call` to `token` could be turned into `expr::token`.
This is a bit inconsistent - sometimes `token(p1, p2, p3)` is represented
as `expr::token` and the query planner handles that, but sometimes it might
be represented as `function_call`, which the query planner doesn't handle.

There is also a problem because there's a lot of duplication
between a `function_call` and `expr::token`. All of the evaluation
and preparation is the same for `expr::token` as it's for a `function_call`
to the token function. Currently it's impossible to evaluate `expr::token`
and preparation has some flaws, but implementing it would basically
consist of copy-pasting the corresponding code from token `function_call`.

One more aspect is multi-table queries. With `expr::token` we turn
a call to the `token()` function into a struct that is schema-specific.
What happens when a single expression is used to make queries to multiple
tables? The schema is different, so something that is representad
as `expr::token` for one schema would be represented as `function_call`
in the context of a different schema.
Translating expressions to different tables would require careful
manipulation to convert `expr::token` to `function_call` and vice versa.
This could cause trouble for index queries.

Overall I think it would be best to remove expr::token.

Although having a clear marker for the partition token
is sometimes nice for query planning, in my opinion
the pros are outweighted by the cons.
I'm a big fan of having a single way to represent things,
having two separate representations of the same thing
without clear boundaries between them causes trouble.

Instead of having expr::token and function_call we can
just have the function_call and check if it represents
a partition token when needed.

Signed-off-by: Jan Ciolek <jan.ciolek@scylladb.com>

---
## [shaunjohann/gorilla](https://github.com/shaunjohann/gorilla)@[f3ce849a8c...](https://github.com/shaunjohann/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Monday 2023-06-26 02:08:40 by Shishir Patil

Releasing Torch and TF weights 🚀  (#16)

In this PR we release the weights for Gorilla 0-shot model for Torch Hub
and Tensorflow Hub APIs 🎉

It chooses from 626 (exhaustive) TensorFlow v2 APIs, and 94 (exhaustive)
Torch Hub in a 0-shot fashion (without any retrieval). In the spirit of
being open, we do not filter, nor carry out any post processing either
to the prompt nor response 🎁 We would like to remind the community that
neither of `gorilla-7b-hf-v0`, `gorilla-7b-tf-v0`, nor
`gorilla-7b-th-v0` have any generic chat capability. We do have a model
with all the 1600+ APIs which also has generic chat capability, which we
release slowly to accommodate server demand.

You can play around with Gorilla either through our hosted colab (OpenAI
Chat completion API compliant) or you can download and run it locally.

Thank you for all the comments and suggestions so far! Keep them
coming!!!

🚀 🚀 🚀

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[8c1320974c...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/8c1320974c3daa20896087d9375ae8e295312d37)
#### Monday 2023-06-26 02:34:04 by Knative Automation

upgrade to latest dependencies

bumping knative.dev/hack f591fea...d7586a2:%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping knative.dev/serving 2c1bb07...2813b9a:%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/pkg dfad48e...eb63a40:%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping knative.dev/client-pkg 4f052f9...b93ceb0:%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/eventing 034bec9...95cdbaa:%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19

Signed-off-by: Knative Automation <automation@knative.team>

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[daa33d89fe...](https://github.com/TheWolfbringer/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Monday 2023-06-26 02:40:55 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[06e4327e68...](https://github.com/DaedalusDock/daedalusdock/commit/06e4327e689d1838675874cf06452d1ba2b22979)
#### Monday 2023-06-26 02:50:24 by Kapu1178

Speed and Bugfix ports (#388)

* Fully fixes atom init desyncs (#76179)

The old system was... ok, but the stack trace was unfortuante, and the
potential to double remove was silly.
Let's use a list of source, value instead, to block overremovals and
properly support different load states

Prevents a bug a goodhearted bagilmin showed me where shuttles would
randomly just fail to load.
Calling clear twice should not be a failure

:cl:
fix: Maps loaded post init will no longer randomly enter a failed state.
Hopefully.
/:cl:

* Fixes a runtime in atom init management (#76241)

## About The Pull Request

The issue was map verification calling build_cache, which uses the
define which enables/disables init values on sleep. We avoid this by
using a var on map datums and using that to enable the init value
modification only when we are actually loading stuff.

Also fixes a bug in clear_tracked_initialize() where it being called
with no values lead to bad values/potentially overriding initialized on
accident.

Also also I forgot how for loops worked so this would not have worked
regardless

## Why It's Good For The Game

Code should like, function

* Be polite! While on walk intent you won't bump, swap places or push other people now. (#68493)

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* todo: port potato contents

* byond

* speed

* href explo

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [pieceowater/watertools](https://github.com/pieceowater/watertools)@[5a4271c833...](https://github.com/pieceowater/watertools/commit/5a4271c833a16dd89b956082e50866f038b99e65)
#### Monday 2023-06-26 03:04:38 by pieceowater

FUCK YEAH AAAA THERE IS A FUCKING IMAGES IN MY FUCKING PACKAGE HELL YEAHHHH

---
## [Sankalita10/Projects](https://github.com/Sankalita10/Projects)@[366ff3bfb0...](https://github.com/Sankalita10/Projects/commit/366ff3bfb06612eee41519558820685f529ee448)
#### Monday 2023-06-26 04:02:30 by Sankalita Poddar

Add files via upload

🌟 Netflix Clone Homepage 🎬

Welcome to my GitHub repository featuring a stunning Netflix Clone Homepage! 🚀

Using HTML and CSS, I've meticulously crafted a pixel-perfect replica of the popular streaming platform's homepage. 🎉 The sleek design, dynamic layout, and attention to detail make this project a standout showcase of my web development skills. 💻

Feel free to explore the code, clone the repository, and even contribute if you'd like! 🤝 Let's collaborate and take this project to new heights together. 💡

Check out the live demo here and immerse yourself in the world of seamless user experience. 📺 Don't forget to give it a ⭐️ if you find it interesting!

#HTML #CSS #WebDevelopment #NetflixClone #FrontendDevelopment

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[465aef0da1...](https://github.com/yogstation13/Yogstation/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Monday 2023-06-26 04:17:58 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [Michaelmanicotti/poetry](https://github.com/Michaelmanicotti/poetry)@[cf6a648ed3...](https://github.com/Michaelmanicotti/poetry/commit/cf6a648ed34d8c7fd95fac06bd147acbeb86ac18)
#### Monday 2023-06-26 04:18:09 by Michaelmanicotti

Update  Movement III | To the pretty boy I can't stop writing poems about, Fuck You

---
## [sysdotini/espi.me](https://github.com/sysdotini/espi.me)@[bff6572547...](https://github.com/sysdotini/espi.me/commit/bff65725474a0965403716a81f71018723b4fd95)
#### Monday 2023-06-26 04:19:52 by Espi Marisa

i don't like discord's stupid shit new username system

fuck off

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[f0557332d8...](https://github.com/Offroaders123/Art-Gen/commit/f0557332d83331facc5819f8606a7e289bb8b84b)
#### Monday 2023-06-26 04:26:05 by Offroaders123

Hacky Puppeteer!

Wow, this is sick! Got this set up using Puppeteer, and an HTTP server to host the site on localhost, which will be where the HTML is rendered to. Is there a better way of doing this that I haven't thought about yet? This is working out, but it does seem a bit ugly to have it working like this 😂

`tsx ./test`

This commit name is absolutely going to be a song name of mine.

I think this could indeed be a neat Electron app too, if all of this was done through a GUI, you could probably use the Electron backing for Puppeteer too right? I've seen a few sources and example of being able to do that. So you could have your app GUI run in Electron, and it would use that same implementation for the renderer window too. I like the CLI approach personally though, so I'm going to experiment with that to start with.

I think the GUI-app way is probably easier for more general users though, so I think that could be more worthwhile. It might make the renderer/Node interations a bit simpler too, as you'd only have to have the GUI bit, and you could use Context Bridges from Electron to get the Node communication set up? That worked fairly nicely in my now classic Electron Text Editor project.

Yeah, Tauri could be nice for this, but that's a bonus thing to worry about later. Having something working to start with is the initial goal yet again for this project here :)

---
## [sameerkali/ChatRoomApp](https://github.com/sameerkali/ChatRoomApp)@[ba1fc47a8b...](https://github.com/sameerkali/ChatRoomApp/commit/ba1fc47a8b20405e6073ca8648f8484484060c87)
#### Monday 2023-06-26 04:56:44 by Sameer Faridi

Create README.md file for ChatRoomApp

Hello! I'm delighted to hear from you, Samer Faridi, a skilled MERN stack & Unity game developer. I came across your app in my feed and noticed that it could benefit from significant improvements. If you're open to it, I'd be glad to collaborate with you to enhance the scalability and aesthetics of the app. Together, we can make it an impressive and user-friendly experience. Best regards, Sameerkali

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[8788e48378...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/8788e483788db2432b9649313efc9426d324379f)
#### Monday 2023-06-26 05:07:00 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [jyn514/compiler-builtins](https://github.com/jyn514/compiler-builtins)@[95eb8729a8...](https://github.com/jyn514/compiler-builtins/commit/95eb8729a817ab9df6e58c9ca8a53bff1a96e631)
#### Monday 2023-06-26 05:29:26 by Joshua Nelson

Port outline-atomics to rust

This has a very long history, summarized in
https://github.com/rust-lang/rust/issues/109064. This port is a very
minimal subset of `aarch64/lse.S` from LLVM's compiler-rt. In
particular, it is missing the following:

1. Any form of runtime dispatch between LL/SC and LSE.

Determining which version of the intrinsics to use
requires one of the following:

  i) `getauxval` from glibc. It's unclear whether `compiler_builtins` is
allowed to depend on libc at all, and musl doesn't even support
getauxval. Don't enshrine the requirement "de-facto" by making it
required for outline-atomics.

  ii) kernel support. Linux and FreeBSD have limited support, but it
requires an extremely recent kernel version and doesn't work at all under QEMU (https://github.com/rust-lang/rust/issues/109064#issuecomment-1494939904).

Instead, we hard-code LL/SC intrinsics. Users who want LSE support
should use the LLVM compiler-rt (if you're building from source in
rust-lang/rust, make sure you have `src/llvm-project` checked out
locally. the goal is to soon add a new `optimized-compiler-builtins`
option so this is easier to discover).

2. The global `___aarch64_have_lse_atomics` CTOR, required to do runtime
   dispatch. Thom Chiviolani has this to say about global CTORs:

> static ctors are problems because we are pretty eager about dead code elim
> in general if you have a module that isnt directly reference we will probably not have its static ctors
> also, while llvm has a super robust way to have a static ctor (theres s special "appending global" to use for c++), we dont use that and just have people make a #[used] static in a special section
> 1. the robust way kinda requires rust knowing that the argument is a static ctor (maybe a #[rustc_static_ctor] attribute). it also would be... finnicky, since on windows we actually care beyond being a static ctor, that we run as part in a specific group of ctors, which means a very specific section (one for TLS and the other for, uh, i dont remember)
> 2. we still actually have to codegen the cgu that isn't referenced. but maybe we could remember that it has that attribute and use that

So while this is possible in theory, it's decidedly non-trivial, and
needs invasive changes to rust itself. In any case, it doesn't matter
until we decide the story around libc.

3. The 16-byte (i128) version of compare_and_swap. This wouldn't be
   *too* hard to add, but it would be hard to test. The way I tested the
existing code was not just with unit tests but also by loading it as a
path dependency and running `x test core` - the latter caught several
bugs the unit tests didn't catch (because I originally wrote the tests
wrong). So I am slightly nervous about adding a 16-byte version that is
much more poorly tested than the other intrinsics.

---
## [fabiodl/mame](https://github.com/fabiodl/mame)@[c4a19a68a6...](https://github.com/fabiodl/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Monday 2023-06-26 06:09:29 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [WillieT1986/classroom](https://github.com/WillieT1986/classroom)@[6c8beff6cf...](https://github.com/WillieT1986/classroom/commit/6c8beff6cf7ce8835822b19f43f99d18247b3914)
#### Monday 2023-06-26 06:16:52 by WillieT1986

Commit: Designed and created Gender.java with comprehensive tests and validation through GenderTest.java

Description:
This commit focuses on the design and creation of the Gender.java class, accompanied by a series of tests within GenderTest.java. The Gender class represents the gender identity of a user and plays a crucial role in capturing and presenting gender-related information. Through the tests conducted, we ensure the proper functionality and integrity of the Gender class, validating its key features. By designing and testing the Gender class, we establish a robust and reliable solution for handling gender-related information in the system.

Changes:
- Set & Get Display Name: Implemented tests to verify the correct setting and retrieval of the display name property in the Gender class. The display name represents the user-friendly name or label associated with each gender identity.
- Enum Values: Created tests to ensure that the Gender class contains the expected set of enum values. These tests guarantee that the predefined gender options, such as MALE, FEMALE, and OTHER, are correctly defined within the Gender class.
- Enum Equality: Designed tests to validate the equality comparison behavior of the Gender enum values. This ensures that two Gender enum values with the same gender identity are considered equal.
- Enum Case Insensitivity: Developed tests to enforce case insensitivity when working with the Gender enum values. By ensuring that the gender identity comparisons are case-insensitive, we improve usability and prevent potential inconsistencies caused by variations in letter casing.
- Enum Values Count: Implemented tests to verify the count of enum values in the Gender class. These tests ensure that the Gender class contains the expected number of predefined gender options, providing an accurate representation of the available choices.
- Enum Iteration: Created tests to iterate over all the Gender enum values and validate their correctness and order. This guarantees that the enum values are correctly defined and maintain the desired sequence.

Importance of Gender:
The Gender class holds significant importance in applications that require the capture and presentation of gender-related information. It allows users to express their gender identity accurately, respectfully, and inclusively. By providing a standardized set of gender options, such as MALE, FEMALE, and OTHER, the Gender class facilitates the customization of user experiences and the implementation of gender-specific features. It also promotes inclusivity by recognizing and accommodating diverse gender identities. Through comprehensive testing of the Gender class, we ensure that it functions as intended, providing reliable and consistent gender-related functionality within the system.

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[c4b550c1a9...](https://github.com/ss220-space/Skyrat-tg/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Monday 2023-06-26 06:28:31 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[8ca535019e...](https://github.com/Offroaders123/Art-Gen/commit/8ca535019eb19bef90d4a8e147b3add479edfff8)
#### Monday 2023-06-26 07:33:25 by Offroaders123

Demo: New Idea: SSR!

This train ran out of tracks, so I'm going to try taking a different line.

Realized that if I'm going to use an HTTP server, and I plan on using JSX, what if I just did this like a regular person and did this on the 'server' side? Lol

I was trying to load the file using Node's FS, then pass it into Puppeteer's page using `page.evaluate()` but turns out you can't serialize TypedArrays, Files, Blobs, or ArrayBuffers. The only way around this with that current setup would be to convert it to a Base64 DataURL, and that just started to make me feel yucky inside. There's already so many ugly steps going on here, and adding another layer of abstraction like that to simply get the data into Puppeteer (and it would have to come back out this way too) seemed not worth it to me. It started to wreak like the need for a rethink/write.

Took an hour or two to regroup (these changes were from before that), have a late dinner, play some music, and now I feel a bit better about things again. Lets's see where this goes next! Hell yeah!

THE NAME: Is the Primeagen

https://stackoverflow.com/questions/66711330/issue-listening-for-custom-event-via-puppeteer
https://stackoverflow.com/questions/63913846/how-do-i-call-function-outside-async-function-in-puppeteer-with-nodejs
https://stackoverflow.com/questions/46088351/how-can-i-pass-variable-into-an-evaluate-function
https://github.com/puppeteer/puppeteer/issues/3722
https://github.com/puppeteer/puppeteer/issues/2427
https://stackoverflow.com/questions/6850276/how-to-convert-dataurl-to-file-object-in-javascript
https://www.youtube.com/watch?v=ML743nrkMHw (Unrelated, but I watched part of it during my dinner break. Electron really is neat, I think I should give myself some slack (pun unintended), it really is powerful how many neat things you can do with it. Just because it is bulky compared to other options, it is really cool what it does provide you with things to do with it :) )

---
## [kofemann/guava](https://github.com/kofemann/guava)@[8a676ade61...](https://github.com/kofemann/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Monday 2023-06-26 08:27:15 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[21fcc792bf...](https://github.com/yarnpkg/berry/commit/21fcc792bf83825aa051c51c96cdc683ee85d20b)
#### Monday 2023-06-26 08:53:12 by Maël Nison

Sets the default compression to 0 (#5526)

**What's the problem this PR addresses?**

Cache compression doesn't seem the best option nowadays:

- It adds significant time to installs
- It adds a non-negligible runtime overhead (partially related, #1817)
- It prevents Git from diffing archives when they're modified

Its main advantage is for some amazingly large packages, where storing
them inside a Git repository would be impossible (GitHub has a 600MB
file limit). But since we changed the cache default to
`enableGlobalCache: true`, this isn't relevant by default, so the cache
compression should be set to zero.

One potential issue is how it may give the impression that Yarn became
worse for global cache users. We don't believe it's the case (Git can
delta uncompressed archives in some measure, making it less expensive to
upgrade from one package version to another), but to the average eye it
may not look as such.

**How did you fix it?**

This diff sets the new default compression setting to 0.

To avoid breaking projects' (or at least not making the migration more
difficult), I added a rule to automatically set `compressionLevel` (and
`enableGlobalCache`) to their 3.x default values when running `yarn
install` in a 3.x project. When users are ready they can remove these
settings and re-run the install.

I kept the current compression level on our repository to avoid changing
all archives again. I think we'll have to think of purging the
repository in some form to migrate it to `compressionLevel: 0`.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [hashelq/dosu](https://github.com/hashelq/dosu)@[00929c3ba2...](https://github.com/hashelq/dosu/commit/00929c3ba281ceb7f54558d8e3f017c4f6fe8afb)
#### Monday 2023-06-26 10:34:48 by hashelq

yet another stupid fix. how the fuck do I locally test this shit?

---
## [skorch-dev/skorch](https://github.com/skorch-dev/skorch)@[df92d4d5e3...](https://github.com/skorch-dev/skorch/commit/df92d4d5e3cc5991330e339d6c8d6c83798f0caa)
#### Monday 2023-06-26 10:46:46 by Benjamin Bossan

Allow regression with 1d targets (#974)

* Allow regression with 1d targets

This change makes it possible to pass a 1-dimensional y to
`NeuralNetRegressor`.

Problem description

Right now, skorch requires the `y` passed to `NeuralNetRegressor.fit` to
be 2-dimensional, even if there is only one target, as is the most
common case. This problem has come up a few times in the past, but
mostly it's just an annoyance - just do `y.reshape(-1, 1)` and you're
good (the error message says as much).

There are, however, also cases where it's not so easy to solve. For
instance, in #972, a user reports that they cannot use skorch with
sklearn's `BaggingRegressor`. The problem is that even if `y` is
reshaped, once it is passed to the net from `BaggingRegressor`, it is 1d
again. I assume that `BaggingRegressor` internally squeezes `y` at some
point.

This PR lifts the 2d restriction check.

Initial motivation

Why does skorch require `y` to be 2d? I couldn't remember the initial
reasoning and did some archeology.

I found this comment:

(https://github.com/skorch-dev/skorch/commit/2f00e2570460fe0a6acd8db94c4d8624b3ddd1eb#diff-66ed08bca4d171889565d0285a36b9b47e0e91e3b33d85c51352d8eb00faefac):

>         # The problem with 1-dim float y is that the pytorch DataLoader will
>         # somehow upcast it to DoubleTensor

This strange behavior should not be an issue anymore, so if that was the
only problem, we should be able to just remove the constraint, right?

Problems with removing the constraint

Unfortunately, it's not that easy. The issue comes down to the
following: When we remove the constraint and allow the target `y` to be
1d, but the prediction `y_pred` is still 2d, the criterion `nn.MSELoss`
will probably do the wrong thing. What exactly is wrong? Instead of
calculating the squared error for each sample pair, the criterion
will broadcast the vector and calculate _all squared errors_ between
each sample, then return the mean of that. To demonstrate, let's remove
the reduction step and look at the shape:

```python
>>> import torch
>>> criterion = torch.nn.MSELoss(reduction='none')
>>> y = torch.rand(100)
>>> y_pred = torch.rand((100, 1))
>>> y.shape, y_pred.shape
(torch.Size([100]), torch.Size([100, 1]))
>>> se = criterion(y_pred, y)
/home/vinh/anaconda3/envs/skorch/lib/python3.10/site-packages/torch/nn/modules/loss.py:536: UserWarning: Using a target size (torch.Size([100])) that is different to the input size (torch.Size([100, 1])). This will likely lead to incorrect results due to broadcasting. Please ensure they have the same size.
  return F.mse_loss(input, target, reduction=self.reduction)
>>> se.shape
torch.Size([100, 100])
```

As can be seen, PyTorch broadcasts the two arrays, leading to 100x100
errors being calculated. Thankfully, PyTorch warns about potential
issues with that.

The current solution is to accept this behavior and hope that the users
will indeed see the warning. If they don't see it or ignore it, it could
be a huge issue, because they still get a loss scalar and might even see
a small improvement in the loss during training. But the model will not
converge and it's going to be a huge pain to debug the bug, if it's even
identified as such.

Just to be clear, existing code, which uses 2d targets, will not be
affected by the change introduced in this PR and is still the preferred
way (IMO) to use regression in skorch.

Rejected solutions

I did consider the following solutions but rejected them.

Raising an error when shapes mismatch

This would remove the risk of users missing the warning. The problem
with this is that mismatching shapes can be okay in certain
circumstances. Some criteria don't expect target and prediction to have
the same shape, so we would need to check based on criterion. Moreover,
theoretically, users may indeed want to broadcast. Raising an error
would prevent that and users may have to resort to subclassing to
circumvent the error.

Automatic reshaping

We could automatically add/remove dimensions if we see that they
mismatch. This has the same problems as the previous solution regarding
the dependence on the type of criterion. Furthermore, automatic
adjustment of the user's output is prone to run into issues in some edge
cases (e.g. when the broadcasting is actually desired).

* Fix error when initializing BaggingRegressor

For Python 3.7, CI got:

TypeError: __init__() got an unexpected keyword argument 'estimator'

for BaggingRegressor. Probably it installs an older version of sklearn,
which uses a different argument name. Passing as positional arg should
fix it.

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---------

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[c9bfaf28f7...](https://github.com/argilla-io/argilla/commit/c9bfaf28f72c240f5372640efbcb745d1e2b09be)
#### Monday 2023-06-26 11:28:05 by David Berenstein

[FEATURE] Feature/prepare for training feedbacktask (#3151)

# Description

I added a very rough outline of my ideation behind
`prepare_for_training` with the new `FeedbackDataset`. As discussed
there are 3 complexities:

- How to resolve annotator alignment?
- How to resolve optional fields, which have not been filled out? e.g.,
"Please provide a correction for prompt 1?".
- How handle potential concatenation of fields? 

To make it modular I created a step-wise approach.

1. `Pydantic` Models that map and verify data fields, like so. By doing
this we keep the flexibility to allow for other tasks like
TextClassification and this ensures we can directly use `datasets.field`
and `dataset.questions` for defining training. We could also use the
`name` values from the fields/questions, but this might be more error
prone.
2. `get_relevant_data_for_training()` in `List[dict]` format with all
relevant fields from the Pydantic model. **annotator alignment issue**.
For now I opted for choosing the first non-zero value.
3. Forward the `List[dict]` to a similar flow we previously had.
4. Also add `dataset.unify_responses(question, Enum(strategy))`-method
5. Added `*QuestionUnifcation` to schemas to hold logic surrounding
unifying multiplier responses
6. Added `client.feedback.training`
7. Added`TrainingDataFor*` to hold logic surrounding
`prepare_for_training`-methods per task
8. Added inheritance for ArgillaTrainer

```python 
import argilla as rg
from argilla import (
    FeedbackRecord,
    LabelQuestion,
    LabelQuestionUnification,
    MultiLabelQuestion,
    TrainingDataForTextClassification,
    ArgillaTrainer
)

dataset = rg.FeedbackDataset(
    guidelines="Add some guidelines for the annotation team here.",
    fields=[
        rg.TextField(name="text", title="Human prompt"),
    ],
    questions =[
        LabelQuestion(
            name="relevant",
            title="Is the response relevant for the given prompt?",
            labels=["yes","no"],
            required=True,
            visible_labels=None
        ),
        MultiLabelQuestion(
            name="content_class",
            title="Does the response include any of the following?",
            description="Select all that apply",
            labels={"hate": "Hate Speech" , "sexual": "Sexual content", "violent": "Violent content", "pii": "Personal information", "untruthful": "Untruthful info", "not_english": "Not English", "inappropriate": "Inappropriate content"},
            required=False,
            visible_labels=4
        ),
    ]
)
dataset.add_records(
    records=[
        FeedbackRecord(
            fields={"text": "What is your favorite color?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What do you think about the new iPhone?"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What is your feeling about the technology?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate", "sexual"]}}},
                       {"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate", "sexual"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "Jesus Christ!"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        )

    ]
)

# print(dataset.question_by_name("relevant").__all_labels__)

label = LabelQuestionUnification(question=dataset.question_by_name("relevant"), strategy="majority")
training_data = TrainingDataForTextClassification(text=dataset.field_by_name("text"), label=label)

for framework in ["spacy", "transformers", "openai", "spark-nlp"]:
    formatted_data = dataset.prepare_for_training(framework, training_data, fetch_records=False, train_size=0.8)
    print(formatted_data)

trainer = ArgillaTrainer(
    dataset=dataset,
    training_task_mapping=training_task_mapping,
    framework="setfit",
    fetch_records=False
)
trainer.train("test")
```

Closes #2954
Closes #3184
Closes #3152 

**Type of change**

- [X] New feature (non-breaking change which adds functionality)
- [X] Improvement (change adding some improvement to an existing
functionality)

**How Has This Been Tested**

- [ ] Test A
- [ ] Test B

**Checklist**

- [ ] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alvaro Bartolome <alvaro@argilla.io>

---
## [tiwai/sound](https://github.com/tiwai/sound)@[1bba82fe1a...](https://github.com/tiwai/sound/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Monday 2023-06-26 13:24:21 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [knative-automation/kn-plugin-source-kafka](https://github.com/knative-automation/kn-plugin-source-kafka)@[a909377c42...](https://github.com/knative-automation/kn-plugin-source-kafka/commit/a909377c42b1f7ecc60567cfd33a2e85760e4ead)
#### Monday 2023-06-26 14:13:10 by Knative Automation

upgrade to latest dependencies

bumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/pkg dfad48e...eb63a40:%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/client-pkg 4f052f9...b93ceb0:%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping knative.dev/eventing 034bec9...95cdbaa:%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping knative.dev/hack f591fea...d7586a2:%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping knative.dev/eventing-kafka 9a4a93a...90a8ba9:%0A  > 90a8ba9 upgrade to latest dependencies (# 1353)%0A  > 561d00f upgrade to latest dependencies (# 1352)%0A  > 22b1fff upgrade to latest dependencies (# 1351)%0A  > 77507bf upgrade to latest dependencies (# 1349)%0A  > 6d6530f Update community files (# 1348)%0A  > a6f4f44 upgrade to latest dependencies (# 1344)%0A  > 2558e87 Update community files (# 1346)%0A  > 86dda64 Update dependencies and fix compile issues (# 1345)%0A  > d9a13fc upgrade to latest dependencies (# 1342)%0A  > a3ee5d5 Update community files (# 1343)%0A  > 9c2c601 upgrade to latest dependencies (# 1340)%0A  > 0b7e0ac upgrade to latest dependencies (# 1339)%0A  > 62d8873 upgrade to latest dependencies (# 1338)%0A  > 870d89a Update community files (# 1337)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies

Signed-off-by: Knative Automation <automation@knative.team>

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[fad38b5204...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/fad38b520419a64e4d50fa904721085c0ccb1d43)
#### Monday 2023-06-26 14:14:04 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping knative.dev/client-pkg 4f052f9...b93ceb0:%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping knative.dev/hack f591fea...d7586a2:%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping knative.dev/pkg dfad48e...eb63a40:%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping knative.dev/serving 2c1bb07...0462ce6:%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/eventing 034bec9...901ef61:%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)

Signed-off-by: Knative Automation <automation@knative.team>

---
## [brauner/linux](https://github.com/brauner/linux)@[5a5d6c1e90...](https://github.com/brauner/linux/commit/5a5d6c1e90237e057d60a5d4bf84fb83ca2b804d)
#### Monday 2023-06-26 14:18:25 by Christian Brauner

btrfs: port to new mount api

Hey everyone,

This ports btrfs to the new mount api.

This passes xfstests for me with a single failure:

Failures: btrfs/277
Failed 1 of 821 tests

which warns about FS_IOC_MEASURE_VERITY failing on
'/mnt/scratch/subv/file.fsv' with ENODATA.

This whole thing ends up being close to a rewrite in some places. I
haven't found a really elegant way to split this into smaller chunks.
Such ports to the new mount api are rather clunky and chunky in general.
My last port for overlayfs was big even after splitting it up with the
help of preparatory patches from the maintainers.

I've done my best to make this somewhat workable but I've retained a lot
of the old structure where possible. There's probably more cleanup
possible in the future based on this.

This is curently based on Jens' for-6.5/block to minimize conflicts with
Christoph's changes to how the exclusive holder of a device is indicated
which changes the signatures for various bdev helpers. This should be
merged early this week.

Structural changes
==================

Structurally, this adds two new files param.{c,h} which contain most
code for the new mount api including all parameter parsing, superblock
creation logic, parameter verification and so on.

This allows us to keep everything related to fs_context handling hidden
and inaccessible to other pieces of the codebase that really shouldn't
need to know anything about this.

We only expose the following types and helpers to super.c which are
required for fs_context handling in btrfs:

(1) a struct fs_parameter_spec defining all supported mount options
(2) a helper to verify a set of paramters after the on-disk superblock
    has been read into memory
(3) a ->get_tree() helper responsible for creating a new or finding a
    matching existing superblock
(4) a ->init_fs_context() helper responsible to initialize internal data
    structures for a newly created btrfs fs_context

The super.{c,h} file only exposes the btrfs_fill_super() helper which is
used in the btrfs ->get_tree() helper when a new superblock is created
and needs to be initialized.

Parameter parsing and on-disk superblock information availability
=================================================================

There are big semantical differences between the new and old mount api
that have consequences for how mounting a btrfs instance works.

The old mount uses a single system call that does parameter parsing and
superblock creation in one step. This means a filesystem was free to
choose to read a superblock from disk before parsing mount parameters.

By defering mount parameter parsing after reading the on-disk superblock
into memory and allocating internal data structures to be stashed in
sb->s_fs_info, it was possible to take on-disk superblock information
into account during parameter parsing.

The new mount api splits parameter parsing and superblock creation into
distinct system calls. A new superblock is only created after all
parameter parsing has finished and this order is enforced by the VFS.

Btrfs was one of the filesystems who had such a parameter parsing order:

        btrfs_mount_root()
        -> btrfs_fill_super()
           -> open_ctree()
               -> memcpy(fs_info->super_copy, disk_super, sizeof(*fs_info->super_copy))
               -> btrfs_parse_options()

This has two main consequences:

(1) This has the consequences that struct btrfs_fs_info->super_copy was
    always initialized and available during superblock creation when
    btrfs_parse_options() was called. Thus, it was possible to check for
    various defaults set on sb->s_fs_info right at mount parameter
    parsing time.
(2) btrfs_parse_options() didn't really need to distinguish between a
    remount and a new superblock creation because in both cases a valid
    sb->s_fs_info was set and initialized.

This doesn't work with the new mount api. When parameter parsing happens
the on-disk superblock will not have been read into memory. This isn't a
problem though as parameter parsing can happen with a separate
verification step of the mount parameters after the superblock has been
created in ->get_tree() and the on-disk superblock has been read into
memory. This verification is done in btrfs_fs_params_verify(). All
filesystems supporting the new mount api more or less do it this way.

Introduction of struct btrfs_fs_context
=======================================

To clearly separate the parameter parsing context from the final
superblock info context stashed in sb->s_fs_info a new struct
btrfs_fs_context is introduced. This context is used during parameter
parsing and superblock creation or reconfiguration to hold information
about the requested mount options. The new mount api specifically has
design for this via the fc->fs_private member where this struct
btrfs_fs_context is stashed. The new context is allocated in
btrfs_init_fs_context() which initializes new btrfs context whenever a
new btrfs mount or a remount is requested.

After the verification step the mount information stashed in struct
btrfs_fs_context is committed to struct btrfs_fs_info which is stashed
in sb->s_fs_info:

* If a new superblock is created no existing mount information and
  struct btrfs_fs_info information exists. So we're starting with a
  blank sheet when parsing parameters.
* If a remount is requested we transfer the existing mount information
  from struct btrfs_fs_info into the btrfs_fs_context during
  btrfs_init_fs_context() so that information is available for parameter
  parsing. This is crucial to correctly handle mount option changes.

Subtree (subvolume) mounting - Part I
=====================================

Subtree mounting basically amounts to swapping out the root dentry for a
given superblock so that only a part of the filesystem is exposed when a
mount is created for it.

For this to work a superblock and a mount for the superblock must be
created so that the dentry for the subtree can be looked up in the
filesystem. Afterwards the mount for the superblock can be discarded and
the root dentry swapped out for the subtree dentry. Easy peasy...

The current btrfs code is mucho convoluted though tbh. Two different
btrfs filesystem types exist with the justification that having the
second filesystem type making things easier to follow. Without throwing
shade on anyone but I'm not really seeing that. It's a bit clumsy.

In any case, we need to kill this for the new mount api anyway and I
hopefully ended up with something cleaner.

As part of the port to the new mount api the reliance on
vfs_kern_mount() is removed and thus the need for a second separate
filesystem type. The callchain now is:

-> btrfs_init_fs_context() # main filesystem context
   -> btrfs_get_tree()
      -> btrfs_get_tree_common()
         -> vfs_dup_fs_context() # superblock filesystems context
            -> fc_mount()
               -> btrfs_get_tree_super()
         -> mount_subvol()

An enum indicator for the phase of the mount is kept in struct
btrfs_fs_context. A second, separate filesystem context is created that
only exists for the creation of the superblock leaving the original
filesystem context pristine.

However, the struct btrfs_fs_context is shared between the two filesytem
context via a simple refcount which is a very lightweight solution that
allows to share the mount context avoiding useless memory duplications.
The btrfs_fs_context is always freed by the original filesystem context
which is responsible for parameter parsing and subtree mounting.

The original filesystem context transfers all information that is only
relevant for superblock creation to the second filesystem context. This
specifically includes the source in fc->source and the security
information in fc->security.

The second filesystem context is also the one that allocates struct
btrfs_fs_info as this is the actual code that is responsible for
initializing sb->s_fs_info. The first filesystem context only handles
subtree creation and consumes the mount we created for the superblock.

Subtree (subvolume) mounting - Part II
======================================

(A good chunk of this can also be found as a comment in the code).

Ever since commit 0723a0473fb4 ("btrfs: allow mounting btrfs subvolumes
with different ro/rw options") the following works:

       (i) mount /dev/sda3 -o subvol=foo,ro /mnt/foo
      (ii) mount /dev/sda3 -o subvol=bar,rw /mnt/bar

which looks nice and innocent but is actually pretty intricate and
deserves a long comment.

On another filesystem a subvolume mount is close to something like:

     (iii) # create rw superblock + initial mount
           mount -t xfs /dev/sdb /opt/

           # create ro bind mount
           mount --bind -o ro /opt/foo /mnt/foo

           # unmount initial mount
           umount /opt

Of course, there's some special subvolume sauce and there's the fact
that the sb->s_root dentry is really swapped after mount_subtree(). But
conceptually it's very close and will help us understand the issue.

The old mount api didn't cleanly distinguish between a mount being made
ro and a superblock being made ro. The only way to change the ro state
of either object was by passing MS_RDONLY. If a new mount was created
via mount(2) such as:

     mount("/dev/sdb", "/mnt", "xfs", MS_RDONLY, NULL);

the MS_RDONLY flag being specified had two effects:

(1) MNT_READONLY was raised -> the resulting mount got
    @mnt->mnt_flags |= MNT_READONLY raised.

(2) MS_RDONLY was passed to the filesystem's mount method and the
    filesystems made the superblock ro. Note, how SB_RDONLY has the same
    value as MS_RDONLY and is raised whenever MS_RDONLY is passed
    through mount(2).

Creating a subtree mount via (iii) ends up leaving a rw superblock with
a subtree mounted ro.

But consider the effect of the old mount api on btrfs subvolume mounting
which combines the distinct steps in (iii) into a a single step.

By first issuing (i) both the mount and the superblock are turned ro due
to (1) and (2). Now when (ii) is issued the superblock is ro and thus
even if the mount created for (ii) is rw it wouldn't help.

Hence, for subtree mounting to work correctly, btrfs needed to
transition the superblock from ro to rw for (ii). It did this using an
internal remount call (a bold choice...).

IOW, subvolume mounting was inherently messy due to the ambiguity of
MS_RDONLY in mount(2). Note, this ambiguity also has mount(8) always
translate "ro" to MS_RDONLY. (The only time there's a real difference is
for MS_REMOUNT | MS_BIND | MS_RDONLY.) IOW, in both (i) and (ii) "ro"
becomes MS_RDONLY when passed by mount(8) to mount(2).

The new mount api however disambiguates making a mount ro and making a
superblock ro:

(3) To turn a mount ro the MOUNT_ATTR_RDONLY flag can be used with
    either fsmount() or mount_setattr(). This is a pure VFS level change
    for a specific mount or mount tree that is never seen by the
    filesystem itself. IOW, it has no effect on the superblock.

(4) To turn a superblock ro the "ro" flag must be used with
    fsconfig(FSCONFIG_SET_FLAG, "ro"). This option is seen by the
    filesytem in fc->sb_flags.

This disambiguation has rather positive consequences. Mounting a
subvolume ro will not also turn the superblock ro. Only the mount for
the subvolume will become ro.

So, if the superblock creation request comes from the new mount api the
caller must've explicitly done something such as:

     fsconfig(FSCONFIG_SET_FLAG, "ro")
     fsmount/mount_setattr(MOUNT_ATTR_RRDONLY)

IOW, at some point the caller must have explicitly turned the whole
superblock ro and so we shouldn't just undo it like we did for the old
mount api.

So the port gets rid of this nasty internal remount hack at least for
requests coming from the new mount api.

So the remounting hack must only be used for requests originating from
the old mount api and imho should be marked for full deprecation so it
can be completely turned off in a couple of years.

The new mount api has no reason to support this. It is also a somewhat
bold choice because the VFS may very well apply additional protection
steps when transitioning a superblock from ro to rw which can easily be
missed in btrfs code.

In any case, I think we might end up with a singificantly cleaner way of
mounting a btrfs subtree after these changes.

To: Chris Mason <clm@fb.com>
To: Josef Bacik <josef@toxicpanda.com>
To: David Sterba <dsterba@suse.com>
To: Nick Terrell <terrelln@fb.com>
Cc: linux-btrfs@vger.kernel.org
Cc: linux-fsdevel@vger.kernel.org
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
Changes in v2:
- EDITME: describe what is new in this series revision.
- EDITME: use bulletpoints and terse descriptions.
- Link to v1: https://lore.kernel.org/r/20230626-fs-btrfs-mount-api-v1-0-045e9735a00b@kernel.org



--- b4-submit-tracking ---
# This section is used internally by b4 prep for tracking purposes.
{
  "series": {
    "revision": 2,
    "change-id": "20230615-fs-btrfs-mount-api-d048814651b0",
    "base-branch": "block.for-6.5/block",
    "prefixes": [],
    "history": {
      "v1": [
        "20230626-fs-btrfs-mount-api-v1-0-045e9735a00b@kernel.org"
      ]
    }
  }
}

---
## [amir73il/linux](https://github.com/amir73il/linux)@[88e4607034...](https://github.com/amir73il/linux/commit/88e4607034ee49e09e32d91d083dced5c2f4f127)
#### Monday 2023-06-26 14:24:03 by Vladimir Sementsov-Ogievskiy

coredump: require O_WRONLY instead of O_RDWR

The motivation for this patch has been to enable using a stricter
apparmor profile to prevent programs from reading any coredump in the
system.

However, this became something else. The following details are based on
Christian's and Linus' archeology into the history of the number "2" in
the coredump handling code.

To make sure we're not accidently introducing some subtle behavioral
change into the coredump code we set out on a voyage into the depths of
history.git to figure out why this was O_RDWR in the first place.

Coredump handling was introduced over 30 years ago in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)").
The original code used O_WRONLY:

    open_namei("core",O_CREAT | O_WRONLY | O_TRUNC,0600,&inode,NULL)

However, this changed in 1993 and starting with commit
9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") the coredump code
suddenly used the constant "2":

    open_namei("core",O_CREAT | 2 | O_TRUNC,0600,&inode,NULL)

This was curious as in the same commit the kernel switched from
constants to proper defines in other places such as KERNEL_DS and
USER_DS and O_RDWR did already exist.

So why was "2" used? It turns out that open_namei() - an early version
of what later turned into filp_open() - didn't accept O_RDWR.

A semantic quirk of the open() uapi is the definition of the O_RDONLY
flag. It would seem natural to define:

    #define O_RDWR (O_RDONLY | O_WRONLY)

but that isn't possible because:

    #define O_RDONLY 0

This makes O_RDONLY effectively meaningless when passed to the kernel.
In other words, there has never been a way - until O_PATH at least - to
open a file without any permission; O_RDONLY was always implied on the
uapi side while the kernel does in fact allow opening files without
permissions.

The trouble comes when trying to map the uapi flags onto the
corresponding file mode flags FMODE_{READ,WRITE}. This mapping still
happens today and is causing issues to this day (We ran into this
during additions for openat2() for example.).

So the special value "3" was used to indicate that the file was opened
for special access:

    f->f_flags = flag = flags;
    f->f_mode = (flag+1) & O_ACCMODE;
    if (f->f_mode)
            flag++;

This allowed the file mode to be set to FMODE_READ | FMODE_WRITE mapping
the O_{RDONLY,WRONLY,RDWR} flags into the FMODE_{READ,WRITE} flags. The
special access then required read-write permissions and 0 was used to
access symlinks.

But back when ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") added
coredump handling open_namei() took the FMODE_{READ,WRITE} flags as an
argument. So the coredump handling introduced in
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") was buggy because
O_WRONLY shouldn't have been passed. Since O_WRONLY is 1 but
open_namei() took FMODE_{READ,WRITE} it was passed FMODE_READ on
accident.

So 9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") was a bugfix
for this and the 2 didn't really mean O_RDWR, it meant FMODE_WRITE which
was correct.

The clue is that FMODE_{READ,WRITE} didn't exist yet and thus a raw "2"
value was passed.

Fast forward 5 years when around 2.2.4pre4 (February 16, 1999) this code
was changed to:

    -       dentry = open_namei(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);
    ...
    +       file = filp_open(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);

At this point the raw "2" should have become O_WRONLY again as
filp_open() didn't take FMODE_{READ,WRITE} but O_{RDONLY,WRONLY,RDWR}.

Another 17 years later, the code was changed again cementing the mistake
and making it almost impossible to detect when commit
378c6520e7d2 ("fs/coredump: prevent fsuid=0 dumps into user-controlled directories")
replaced the raw "2" with O_RDWR.

And now, here we are with this patch that sent us on a quest to answer
the big questions in life such as "Why are coredump files opened with
O_RDWR?" and "Is it safe to just use O_WRONLY?".

So with this commit we're reintroducing O_WRONLY again and bringing this
code back to its original state when it was first introduced in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") over 30 years ago.

Signed-off-by: Vladimir Sementsov-Ogievskiy <vsementsov@yandex-team.ru>
Message-Id: <20230420120409.602576-1-vsementsov@yandex-team.ru>
[brauner@kernel.org: completely rewritten commit message]
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [Enselic/rust](https://github.com/Enselic/rust)@[80917360d3...](https://github.com/Enselic/rust/commit/80917360d350fb55aebf383e7ff99efea41f63fd)
#### Monday 2023-06-26 14:49:48 by bors

Auto merge of #112292 - thomcc:tls-ohno, r=m-ou-se

Avoid unwind across `extern "C"` in `thread_local::fast_local`

This is a minimal fix for #112285, in case we want a simple patch that can be easily to backported if that's desirable.

*(Note: I have another broader cleanup which I've mostly omitted from here to avoid clutter, except for the `Cell` change, which isn't needed to fix UB, but simplifies safety comments).*

The only tier-1 target that this occurs on in a way that seems likely to cause problems in practice linux-gnu, although I believe some folks care about that platform somewhat 😉. I'm unsure how big of an issue this is. I've seen stuff like this behave quite badly, but there's a number of reasons to think this might actually be "fine in practice".

I've hedged my bets and assumed we'll backport this at least to beta but my feeling is that there's not enough evidence this is a problem worth backporting further than that.

### More details

This issue seems to have existed since `thread_local!`'s `const` init functionality was added. It occurs if you have a `const`-initialized thread local for a type that `needs_drop`, the drop panics, and you're on a target with support for static thread locals. In this case, we will end up defining an `extern "C"` function in the user crate rather than in libstd, and because the user crate will not have `#![feature(c_unwind)]` enabled, their panic will not be caught by an auto-inserted abort guard.

In practice, the actual situation where problems are likely[^ub] is somewhat narrower.

On most targets with static thread locals, we manage the TLS dtor list by hand (for reentrancy reasons among others). In these cases, while the users code may panic, we're calling it inside our own `extern "C"` (or `extern "system"`) function, which seems to (at least in practice) catch the panic and convert it to an abort.

However, on a few targets, most notably linux-gnu with recent glibc (but also fuchsia and redox), a tls dtor registration mechanism exists which we can actually use directly, [`__cxa_thread_atexit_impl`](https://github.com/rust-lang/rust/blob/master/library/std/src/sys/unix/thread_local_dtor.rs#L26-L36).

This is the case that seems most likely to be a cause for concern, as now we're passing a function to the system library and panicking out of it in a case where there are may not be Rust frames above it on the call stack (since it's running thread shutdown), and even if there were, it may not be prepared to handle such unwinding. If that's the case, it'd be bad.

Is it? Dunno. The fact that it's a `__cxa_*` function makes me think they probably have considered that the callback could throw but I have no evidence here and it doesn't seem to be written down anywhere, so it's just a guess. (I would not be surprised if someone comes into this thread to tell me how definitely-bad-news it is).

That said, as I said, all this is actually UB! If this isn't a "technically UB but fine in practice", but all bets are off if this is the kind of thing we are telling LLVM about.

[^ub]: This is UB so take that with a grain of salt -- I'm absolutely making assumptions about how the UB will behave "in practice" here, which is almost certainly a mistake.

---
## [jayjayglows/jayjayglows](https://github.com/jayjayglows/jayjayglows)@[63264417c1...](https://github.com/jayjayglows/jayjayglows/commit/63264417c1fcd7e7ed851a37ae851c2cebfa4f90)
#### Monday 2023-06-26 14:59:04 by jayjayglows

Updated for billionth time.

I was gonna add my actual hobbies but I don't think any of my actual interests can top 'being normal' and 'staring at screen'. Plus it'd all just be stuff like 'watching the leaves sway on trees' because I swear I am the most boring person ever in terms of what I do. Also because admitting half of my time is spent walking around town is incredibly embarrassing. I think admitting I almost killed one of my classmates in gym is more embarrassing though (I'm so sorry Riley jesus christ). Might add an extra readme with fun facts about me or something. They wouldn't even be fun though since they'd all be like 'I like to burn random games to random CD-ROMS and leave them at random tech stores just to perplex the owners.'. Oh well. Whatever. Gamer man out. Live laugh love.

---
## [Autisem/tgstation](https://github.com/Autisem/tgstation)@[2845c985fa...](https://github.com/Autisem/tgstation/commit/2845c985fab04b0de1f7615799a260527af30822)
#### Monday 2023-06-26 15:28:48 by Rhials

Adds a revolutionary conversion stinger (#75002)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.

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
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [nasbdh9/android_kernel_oneplus_sm8250](https://github.com/nasbdh9/android_kernel_oneplus_sm8250)@[7930ffed59...](https://github.com/nasbdh9/android_kernel_oneplus_sm8250/commit/7930ffed593f90f52fc23728a436d29489eccdbb)
#### Monday 2023-06-26 15:34:34 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [ayedSourcecode/FNF-sky-s-Infidelity](https://github.com/ayedSourcecode/FNF-sky-s-Infidelity)@[6e6d2b6c05...](https://github.com/ayedSourcecode/FNF-sky-s-Infidelity/commit/6e6d2b6c0523820b9319867449eb189b7a71a3a5)
#### Monday 2023-06-26 16:06:21 by ayedFNFmaker

FUCK YOU MAIN

Signed-off-by: ayedFNFmaker <123101780+ayedSourcecode@users.noreply.github.com>

---
## [Finxx1/TEiN-Anni-6](https://github.com/Finxx1/TEiN-Anni-6)@[8eed4d7bb0...](https://github.com/Finxx1/TEiN-Anni-6/commit/8eed4d7bb0d687d3d494abc1ce1af2699ceb8790)
#### Monday 2023-06-26 16:34:47 by SurrealDude

+ Umm, yes

+ Added intro cutscenes and Friend Stand cutscene.
+ Added Steamworks and Mount Moriah, aswell as some Ghost Ship and Swamplands fixes. (thank you Enana, very cool)
+ Replaced the menu music with lacrimal frost, as originally intended.
+ Fixes to Depths escape sequence, which is now also on the map.
+ Added intro cart (which is different from Machiavelli's Mask, for bullshit worldmap reasons)
+ Merged most flash files into one "anni6.fla" file.

---
## [vercel/next.js](https://github.com/vercel/next.js)@[6238f8a5c0...](https://github.com/vercel/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Monday 2023-06-26 16:56:10 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [RuchikaPatra/GeekforGeek-potd-Java](https://github.com/RuchikaPatra/GeekforGeek-potd-Java)@[52ba7ebaa2...](https://github.com/RuchikaPatra/GeekforGeek-potd-Java/commit/52ba7ebaa26472a94ef9ec528c02fcf14f8bb381)
#### Monday 2023-06-26 17:57:53 by RuchikaPatra

Create Santa is still not married. He approaches a marriage bureau and asks them to hurry the process. The bureau checks the list of eligible girls of size N and hands it over to Santa. Santa being conscious about his marriage is determined to find a girl with maximum connections so that he can gather more information about her. Accordingly, he looks to figure out the maximum number of girls (from the list) who know each other to achieve the above purpose.  In order to finalize the girl, he needs to find the Kth prime. Where k = largest group of girls who know each other. Considering Santa's poor knowledge of Maths, he seeks Banta's help for the answer. Now you, a fan of Santa Banta Jokes, take this prestigious opportunity to solve the problem.  In case no of connections is zero, print "-1". Here the connection between girls is represented by a 2-D array g of dimension M*2, where M is the number of connections.02-06-2023

---
## [CRITAWAKETS/tgstation](https://github.com/CRITAWAKETS/tgstation)@[835952ccf4...](https://github.com/CRITAWAKETS/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Monday 2023-06-26 18:42:44 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [thatoneyeeter/cmss13](https://github.com/thatoneyeeter/cmss13)@[0f386c8188...](https://github.com/thatoneyeeter/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Monday 2023-06-26 18:45:21 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Zanieon/NorthstarMods](https://github.com/Zanieon/NorthstarMods)@[28df512cb5...](https://github.com/Zanieon/NorthstarMods/commit/28df512cb58ce9071729f4f434eca2c1572c628e)
#### Monday 2023-06-26 18:49:15 by Zanieon

Huge update (See description for full changelog)

Configuration:
- Settings unlocked for local lobby hosting
- Setting that makes the maps wait for a minimum amount of players before starting the waves
- Console variable to allow the use of Smart Pistol as secondary on Easy Mode
- Console variable to setup what Grenade type Grunts can use

Match:
- Frontier Defense Postmatch Summary Menu is restored, it will appear whenever a match ends and returns to lobby if a server allows
- Proper tracking of Titan's Frontier Defense earned experience, allowing them to level up their Aegis ranks
- Dynamic change of Titan/Core Meters based on current players in the match
- If a player as pilot manages to kill 6 or more Titans within a short time (mostly Nuke Rodeos), the server will announce that to all other players
- Droz and Davis will nag to players spend their money at the Store during wave breaks if they have more than 100 Cash
- Proper spawn point rating for when respawning as Titan, players will not drop away from the Harvester anymore as Titan

Maps:
- New Playable Map: Eden
- Angel City Wave Rework to be based off the vanilla spawn amounts
- Boomtown Wave Rework to make waves more consistent with spawn locations and balance
- Drydock: Adjusted where Drones spawns to avoid them making unecessary loops around the Crane area

Live Fire Frontier Defense mode:
- New Playable Maps: Deck, Township, UMA
- Pilot-only gameplay
- 3 Waves with huge amounts of enemies, infantry mostly
- Loadout can be changed at any time during a wave in the Loadout Crates
- Droz and Davis helps players in person by guarding the Harvester
- Players recieve the double amount of money when completing a wave
- Players can have 3 Turrets instead of 2
- Players have no grenades
- Players have limited Anti-Titan ammo, restock possible at Loadout Crate
- Grunts will always have one shield captain in their squads and will always have Anti-Titan weapons
- Stalkers will always spawn with EPG
- Players have a single "public" Titan to use called 'Helper Titan', pilots approaching this Titan gains ownership, staying away clears it

The Helper Titan is:
*A Tone chassis Titan
*Uses XO-16 with Arc Rounds and Faster Reload as primary weapon
*Has basic Dumbfire Missile and Cluster Missile Rack as shoulder mounts
*Has zero-energy Tripwire as utility
*Has basic Salvo Core
*Has passive Shield Regeneration
*Has passive very slow Health Regeneration
*Cannot be rodeoed
*Cannot be disembarked while a wave is active
*Cannot be ordered to follow or guard, it always stays on kneeled position awaiting for a pilot to embark
*If destroyed, it respawns after 2 minutes

AI:
- Cloak Drones will now properly ignore Arc Titans instead of attempting to cloak them
- Mortar Spectres can be hacked if server allows, and they will behave more precisely to vanilla when going into their siege spots
- Grunts will talk about their squadmates being killed or if they are the last person alive in their squad
- Shortened the range where Stalkers starts sprinting at the Harvester from 1800 to 1024 map units
- Sniper Titans will have a better accuracy than normal Titans
- Elite Titans will have grunt pilots inside them

Titans:
- The Shoulder Badge properly updates accordingly to the difficulties played on matches
- Healing back to full health restores the broken parts
- Auto-Titans will ignore friendly fire and AoE's during wave break, this allows Monarch to Electric-Smoke allied Titans without them dodging away

Harvester:
- Properly play the rings start animation when the map starts
- Updates the ring animations when its health reaches 50% and less
- Plays the ring deactivation upon destruction
- Sounds updates accordingly to its health state
- Lightning effects appears in the beam when low health
- The Beam color now reflects more precisely the amount of health it currently have

---
## [jinxynii/coyote-bayou-goobery](https://github.com/jinxynii/coyote-bayou-goobery)@[6fe28837f1...](https://github.com/jinxynii/coyote-bayou-goobery/commit/6fe28837f1d0337091619b4d4b9254f252bc6f83)
#### Monday 2023-06-26 19:17:47 by gob

Ghouls bleed again

Crowley: "Ha, ha! I like a human that knows his place. Too many of you think we're all just zombies. They don’t know, or don’t care, that we’re just as human as they are inside. *We bleed!* We hurt! We regret! And you know what really pisses me off? They think the only way to kill us is to shoot us in the head, like in the old zombie stories, and that will put us out of our misery. Hey, I know! Maybe you could help me even the score."

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[9390b2b1e3...](https://github.com/Offroaders123/Art-Gen/commit/9390b2b1e34d2c8ba35cd7d04f0ddbbdc899eab4)
#### Monday 2023-06-26 19:29:25 by Offroaders123

[Hacky] But Very Close!

Wow! Got this working 'fully on the terminal', thanks to Puppeteer! Of course, it's using Puppeteer under the hood, but now you can actually pass in your own song files, and it will programmatically return back to your what the resulting image is! So you don't have to manually work with the GUI like before.

Been listening to Thank You Scientist 'Terraformer', this album is so sick.

Now that this is working, I want to improve the API so it more simply does the handling, and you do things more functionally. Right now it makes a new Puppeteer browser window for every thumbnail generator, but it doesn't have to be that way, I can set it up much nicer.

I want to make it like the builder pattern for NBT reading and writing, where there are top-level functions that are for the user's ease of use, and to manage the handling on the backside of things so it only has one browser instance at a time. This will work super great with async-await. I also want to only have a single HTTP server at a time too, so I have to move where the definitions for each of these things are into the functions differently, allowing them to manage multiple thumbnail generations concurrently from one instance.

Thought I was going to need to get the MIME type for the artwork file, but I forgot that it's stored in the data itself, so JSMediaTags will provide it (I wrapped those into a Blob object). But if I didn't have that info available to me, I found a really great ESM library to handle that kind of logic.

https://flaviocopes.com/node-serve-html-page/ (Came back to look at this again, didn't need Vite/Express, rebuilt the renderer to simple use HTML templating instead!!! No need for the Canvas implementation now either, since you can just screenshot the window's content. So now you can demo out how the HTML/CSS looks for the thumbnail content, by just opening it with either Live Server, or STE! Yay :D)
https://stackoverflow.com/questions/4720343/loading-basic-html-in-node-js (Help with writing the HTML to the response object)
https://dev.to/victrexx2002/how-to-get-the-mime-type-of-a-file-in-nodejs-p6c
https://github.com/sindresorhus/file-type
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs
https://stackoverflow.com/questions/54099802/blob-to-base64-in-nodejs-without-filereader

I also brought up the updated JSMediaTags module I made, from the CLI branch. It had some better handling compared to that of the original 'site' implementation.

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[5271d4fbc4...](https://github.com/Opentrons/opentrons/commit/5271d4fbc473bb8f2506a90b2c929535c82892f6)
#### Monday 2023-06-26 20:07:03 by Seth Foster

feat(api,shared-data): error codes in PE (#12936)

On the python side of our code, we want our new enumerated exceptions to
be gradually integratable, and we also want to make sure that any errors
that we didn't yet get the chance to give error codes end up with error
codes. To do this in a programmatic way, we can add some automated
methods for wrapping python exceptions.

All enumerated errors now get to wrap errors. These are optional
sequences of more enumerated errors that are considered to have caused
the top-level one - in most cases, this will be because the enumerated
error explicitly was instantiated to wrap a python exception, but it
could also be if it was raised from one.

Since we only wrap other enumerated errors, we need a way to make
exceptions enumerated errors. A new exception type (but not code - it's
just a GeneralError) called PythonException has this capability; it lets
you give it BaseExceptions in addition to other EnumeratedErrors, and
it's capable of walking the python memory model internals to try and get
the other exceptions in a stack of raise from ... raise from ... calls
that are reasonably popular in our code. This is functionality that is
promoted out of The Dunder Zone in python 3.11, so I feel pretty good
using it (this is what ExceptionGroups are).

So now, as in the tests, if you catch an exception and give it to a
PythonException you bless it with an error code and save all the
exceptions and their stack traces for later inspection. Cool!

ProtocolEngine is the first place we'll go through and add places that
actually use these error codes, since it's in a lovely high-leverage
middle spot in our stack. That means we both get to test the upward
interface of how these things will be represented in the HTTP API and
how they'll be created from lower exceptions.

ProtocolEngine already has its own very large and robust set of custom
exceptions, which is awesome. We can make them inherit from the
enumerated errors pretty easily, but unfortunately we have to add a
bunch of stuff to their constructors to pass along things like the
ability to wrap other exceptions and so on. Luckily that's just typing.

Once we've done that, at the three points we catch all missed exceptions
we have to switch over to creating the new style. ProtocolEngineErrors
get passed on; uncaught legacy errors get captured as PythonExceptions;
and uncaught errors in the normal core do too.

Finally, we have to represent this new style of error in the
ErrorOccurrence objects. This is the fun part. Previously, we'd added
error codes to those objects; this was sort of a big deal because we
want them to be required when you make new ErrorOccurrences and when
clients look, but we don't want things to break when we deserialize old
ones. We can extend that trick pretty easily to add new things. What's
not quite as easy is this concept of wrapping errors. Our errors are now
essentially trees, and we need tree structure here. Luckily, jsonschema
and pydantic are actually pretty good at type-recursive schema and
object definitions, so we can plop a list of other error occurrences in
there.

Now, when we catch one of these errors that's bubbled up from hardware,
we give it a name and we capture its entire history in an inspectable
way, and I think that's really cool.

---
## [TheNightingale/Baystation12](https://github.com/TheNightingale/Baystation12)@[a33bd3b082...](https://github.com/TheNightingale/Baystation12/commit/a33bd3b0821a3f9eda21c73b00703ac95fca8d0a)
#### Monday 2023-06-26 21:33:48 by Nighting

OKAY. THERE WE GO. THERE WE FUCKING GO. GITHUB YOU ARE MY BITCH

---
## [Passe2142/TerraGov-Marine-Corps](https://github.com/Passe2142/TerraGov-Marine-Corps)@[1c696b710d...](https://github.com/Passe2142/TerraGov-Marine-Corps/commit/1c696b710d58c2adfc53be7fd49305ba45b8c23b)
#### Monday 2023-06-26 21:49:53 by 567Turtle

adds the vali claymore (#12485)

* adds the vali claymore

nuff said

* adds sheath icon states

asgf

* Update code/game/objects/items/storage/holsters.dm

Co-authored-by: ivanmixo <ivanmixo@gmail.com>

* crazy

go fuck yourself

* go fuck yourself

* makes shit better

* autodoc

* autodoc (but it actually works this time)

* Update code/game/objects/items/weapons/twohanded.dm

---------

Co-authored-by: ivanmixo <ivanmixo@gmail.com>
Co-authored-by: TiviPlus <57223640+TiviPlus@users.noreply.github.com>

---
## [iot-Noob/Java](https://github.com/iot-Noob/Java)@[e5f9e6485e...](https://github.com/iot-Noob/Java/commit/e5f9e6485e63585512a755036567bcf83f273a8d)
#### Monday 2023-06-26 22:00:46 by Noob Programmer

PowerUp Game Code - Java Vending Machine Puzzle

The PowerUp Game Code is a Java implementation of an exciting and challenging Vending Machine puzzle game. It provides a user-friendly interface where players can input numbers and attempt to unlock the machine by matching the correct combination. With its engaging gameplay and intuitive design, this game is a must-have for Java developers and puzzle enthusiasts alike.

The code utilizes Java's object-oriented programming features, including interfaces and inheritance, to create a modular and extensible game structure. It incorporates random number generation and user input validation to ensure a dynamic and interactive gaming experience. The game keeps track of the user's progress, displaying the entered numbers and providing feedback on their correctness.

Designed to provide both entertainment and educational value, the PowerUp Game Code offers a fun way to challenge your problem-solving skills and logical thinking. It can be used as a learning resource to understand key Java concepts or as a starting point for building your own customized puzzle games.

Whether you're a Java developer looking to enhance your programming skills or a gaming enthusiast seeking an enjoyable and intellectually stimulating experience, the PowerUp Game Code is an excellent choice. Download the code now and embark on a journey to crack the Vending Machine's code. Are you up for the challenge?

---
## [swuff-star/Starstorm2](https://github.com/swuff-star/Starstorm2)@[a3d9f77b5d...](https://github.com/swuff-star/Starstorm2/commit/a3d9f77b5d22029299df458125f4acd276c43448)
#### Monday 2023-06-26 22:06:38 by swuff-star

oh boy

i am going to pull jace's branch and it is going to be fine and absolutely not fuck up my branch haha lets do this!

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[179405e44c...](https://github.com/git-for-windows/git/commit/179405e44cd61d1f88da44d5982b94af3d3d335a)
#### Monday 2023-06-26 22:19:42 by Johannes Schindelin

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
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[3cb6b3f9e7...](https://github.com/s-sutton/s-sutton/commit/3cb6b3f9e7b1b903009aca3311cb7f1628a516e1)
#### Monday 2023-06-26 22:47:04 by S. Sutton

Update README.md, finished links

I went ahead and added links to everything else that could be linked to.

I also made some minor changes in the "Programming Projects" section to turn it into a more straightforward to-do list that is a little less intimidating.

I also added the Khan Academy courses because, when I finally get back into programming proper, I'm probably going to use those to re-familiarize myself with the process as well as pick up the basics of the languages they cover as a jumping off point.

I only have experience with Lua, C++, and GML right now, and I use "experience" loosely, so that's embarrassingly shameful and needs to be remedied eventually. I really miss the fun of programming in GML, though, and I picked it up quickly, so I should be able to pick up more languages again even after all this time. Unfortunately, I no longer have access to my GML projects to add to my GitHub, but they weren't anything special, anyway.

---
## [chardso/LEAD](https://github.com/chardso/LEAD)@[cde04bc0a0...](https://github.com/chardso/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Monday 2023-06-26 22:50:11 by Dawa Edina Hillary

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
## [mrzu/evals](https://github.com/mrzu/evals)@[14f8771c40...](https://github.com/mrzu/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Monday 2023-06-26 23:21:36 by oscar

[Eval] Add Chinese Homophonic  (#1169)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Understand Chinese Homophonic 

### Eval description

We have found some popular homophonic sentences on the Internet,
including the Chinese pronunciation of English words and homophones, and
provide several options for the model to determine which option matches
the homophonic sentence the best.

### What makes this a useful eval?

Chinese homophonic puns are a widely popular internet cultural
phenomenon that generates humor by utilizing the homophonic
relationships between Chinese characters. These puns are typically
spread in text form on social media, forums, and messaging applications,
and they are extremely common in China's online culture.

Homophonic puns have a wide range of applications, encompassing ordinary
daily life scenarios as well as hot news events, entertainment gossip,
and political current affairs. These puns frequently appear in internet
memes, jokes, advertising slogans, and short videos, garnering
significant popularity among young people and internet users.

For those unfamiliar with them, homophonic puns may seem like encrypted
text, making it difficult to grasp the true intention behind them.
However, understanding them allows for the establishment of strong
connections between individuals and facilitates smooth communication.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"一天小鸭对小鸡表白:小鸡，我爱你。小鸡:你duck不必。这句话中的\"duck\"是什么意思？\nA. 鸭子\nB. 大可"}],
"ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"丑的人才有对象，美的卖空调。这句话中的\"美的\"是什么意思？\nA. 漂亮的\nB. 空调公司"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我是一只小绵羊，我今天剪毛了，我失绵了。这句话中的\"失绵\"表达意思？\nA. 失眠\nB. 没有了羊毛"}], "ideal":
["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"以后我的吉祥物决定就是你了，螃蟹！——因为，你有钱（钳）。这句话中的\"钳\"是什么意思？\nA. 有钱\nB. 螃蟹的钳子"}],
"ideal": ["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"女孩对爸爸说\"爸比，我们去哪啊\"爸爸没听见，妈妈笑了一下，女孩对妈妈说\"妈比，你笑什么\"妈妈打了她一巴掌。妈妈为什么打她？\nA.
她提出了不合理的要求\nB. 她骂人了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"天气这么热，我们总会熟的。这句话中的\"熟的\"是什么意思？\nA. 热熟了\nB. 熟悉了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我好像胖了，没事我陪你减肥，我们戒荤叭。这句话中的\"戒荤\"是什么意思？\nA. 吃素食\nB. 结婚"}], "ideal":
["B"]}
  ```
</details>

---------

Co-authored-by: oscar <oscar@hellotalk.com>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[90587b6e5c...](https://github.com/mrzu/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Monday 2023-06-26 23:21:36 by Juyeon Yoon

Add Korean honorific sentence classification eval (#1181)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

korean-honorific

### Eval description

Evaluates LLMs on the task of classifying Korean honorific/non-honorific
sentences.

### What makes this a useful eval?

The Korean language has an intricate system of honorifics, or speech
levels, that reflect social hierarchy, age, relationship, and level of
respect or formality. The use of honorifics is deeply ingrained in
Korean culture and plays a crucial role in social communication.
Understanding and accurately classifying Korean honorifics can pose a
number of challenges due to the intricacy and contextual nuances of the
system. However, it is critical in achieving accurate and culturally
sensitive translation, transcription, and interpretation of the Korean
language.

Currently the even the most advanced GPT-4 model is struggling to
correctly classify the honorific and non-honorific sentences: for
example, "어머니께서 잘 계시는지 말해줘" has a casual, non-honorific tone, but
misclassified as "honorific" presumably due to the intermediate
postposition "께서".

Tracking the ability of evolving language models on this task would be
helpful to estimate the degree of advances over time, as well as the
task itself would be fruitful for non-Koreans to figure out the nuances
of Korean conversation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그분이 잘 계시는지 물어봐
줘."}], "ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "이 공원에서 자주
걷습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "자주 드시나요?"}],
"ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "아니요, 접점은 없지만
개인적으로 관심이 있습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "당신의 취미가
무엇인가요?"}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "꼭 모으길 바랄게."}],
"ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그러면 나도
준비해야겠다."}], "ideal": "non-honorific"}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[9edc150dde...](https://github.com/mrzu/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Monday 2023-06-26 23:21:36 by Chen Zhao

[Eval] Chinese lantern riddles (#1176)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

chinese-lantern-riddles

### Eval description

This evaluation tests the model's performance in solving Chinese lantern
riddles, which are based on the shape, pronunciation, and meaning of
Chinese characters.

### What makes this a useful eval?

Lantern riddles are a traditional Chinese festive activity that involves
multiple participants guessing riddles together. Apart from being a part
of festival celebrations, lantern riddles can also serve as an
educational tool to help Chinese language learners enhance their
vocabulary and language reasoning. Through the process of unraveling the
riddles, students can also develop their logical thinking and reasoning
skills, as well as nurture their imagination and creativity. Lantern
riddles can also spark students' interest in language learning and make
the learning experience more enjoyable.

Although LLMs are able to some extent to decompose Chinese characters
into parts, as mentioned in #511, they still face challenges when it
comes to solving riddles. In most cases, GPT 3.5 cannot reason correctly
about the structure of Chinese characters. For instance, the riddle
"上下一体（打一字）" can be interpreted as a combination ("一体") of "上" and "下",
resulting in the answer "卡". However, GPT 3.5 gives the wrong answer,
"升", with a reason that makes no sense. A similar situation occurs when
GPT 3.5 reasons about the pronunciation of Chinese characters, with one
of its explanations stating that the pronunciation of "盼（pàn）" is
similar to the pronunciation of "俄（é）", which is entirely incorrect.
However, on the positive side, GPT 3.5 shows good performance when a
riddle only encodes meaning and does not require reasoning about the
structure and pronunciation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n一撇（打一字）。"}], "ideal": ["厂"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n内里有人（打一字）。"}], "ideal":
["肉"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n二三四五六七八九（打一成语）。"}], "ideal":
["缺衣少食"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n谜底在山东（打一国家名）。"}], "ideal":
["秘鲁"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n身穿红衣，常年哨放，遇紧急事，往火里闯（打一日常用品）。"}],
"ideal": ["灭火器"]}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[c675067906...](https://github.com/mrzu/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Monday 2023-06-26 23:21:36 by robin luo

[eval] Chinese Idioms evulation (#1163)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name
chinese_idioms


### Eval description

Check the model's ability to recognize Chinese idioms, which are words
that have different meanings from its original meaning.

### What makes this a useful eval?

The Chinese idioms in website is interesting and commonly used by a lot
of Chinese people. However, the GPT4 and GPT3.5 fail to explain the
meaning of the idioms with a correct explanation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ x] Check that your data is in `evals/registry/data/{name}`
- [ x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x] Ensure you have the right to use the data you submit via this
eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ x] I have filled out all required fields of this form
- [x ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n伟光正"}], "ideal": ["From the idiomatic phrase
'the great, glorious and correct Chinese Communist Party', it can also
refer to a person associated with the Chinese Communist Party."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n赵家人"}], "ideal": ["From Lu Xun's famous
middle-grade novel 'A Q Zhengzhuan', it generally refers to the powerful
and noble class of the Chinese Communist Party. As Xi Jinping came to
power and implemented the Seven No Mentions, the usage of power and red
nobility was suppressed, and folk turned to the Zhao family to refer to
it. Derivations include calling the People's Republic of China 'Zhao'
and Xi Jinping, the current General Secretary of the CPC Central
Committee, 'King Zhao', or replacing the word 'people' with the word
'Zhao family' in the names of various Chinese organs and media
propaganda"]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n改开党/特色党"}], "ideal": ["The term 'Mao Left' is
commonly used by the civil left and Maoist supporters, which originated
from Deng Xiaoping's 'reform and opening up' and 'socialism with Chinese
characteristics'. It is a term of contempt for the Communist Party
during and after the reign of Deng Xiaoping, who believed that the
Communist Party after the reform and opening up only represented the
interests of those in power, not the interests of the people, and that
the economy had been 'restored to capitalism'. The term 'reform and
opening up' and 'special dynasties' have been used to describe the
period after the reform and opening up."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n黄丝/黄尸"}], "ideal": ["The term refers to
non-establishment camps such as the pro-democracy camp and the local
camp in Hong Kong, as well as those who support their stance, and is
named after the yellow ribbon used as a symbol by non-establishment
camps during the 2014 occupation. Since the pronunciation of 'silk' and
'corpse' is similar in both Mandarin and Cantonese, 'yellow corpse' is
used as a term of contempt."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n蟹堡王"}], "ideal": ["The term refers to the
Hong Kong pro-establishment camp, it is often accused of not having a
political stance and just being in line with Beijing"]}
{"input": [{"role": "user", "content": "请解释下面词语的意思,请使用英文回答。\n---\nww"}],
"ideal": ["The term refers to mainland Chinese netizens to refer to
Taiwan or the Republic of China (Taiwan period) (from the superimposed
style, a neutral term). In January 2022, Taiwan Affairs Office
spokesperson Zhu Fenglian said that the word Wanwan is a nickname for
the Taiwanese people 'Mengmeng' by the Chinese mainlanders"]}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[936cc9d4ab...](https://github.com/mrzu/evals/commit/936cc9d4abfc0775f1fad1d694690870679f6924)
#### Monday 2023-06-26 23:21:36 by somerandomguyontheweb

Add Belarusian orthography eval (#1188)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

belarusian-orthography

### Eval description

Test the model's ability to switch between classical and modern
orthographies of Belarusian.

### What makes this a useful eval?

Belarusian is famous for having two Wikipedias:
[one](https://be.wikipedia.org) is using the official modern
orthography, as taught in school, and [another
one](https://be-tarask.wikipedia.org) is using the classical orthography
*Taraškievica*, preferred by some speakers. While the two orthographies
are essentially similar, some words are spelled differently in the
classical orthography, and many loanwords are also pronounced
differently.

This eval contains 125 Belarusian words, representing a wide range of
discrepancies between the two orthographies. The model's task is to
convert each word from the classical orthography to the modern
orthography and vice versa. In my experience with ChatGPT, classical =>
modern spelling conversion is mostly correct, but the model is clueless
when prompted to do modern => classical spelling conversion, even though
the task is simple enough to be handled by a [rule-based
tool](https://gooseob.github.io/taraskevizatar).

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "адрозьненьнем"}], "ideal": "адрозненнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"адрозненнем"}], "ideal": "адрозьненьнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "ісьляндзкі"}], "ideal": "ісландскі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"ісландскі"}], "ideal": "ісьляндзкі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "сымбаль"}], "ideal": "сімвал"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"сімвал"}], "ideal": "сымбаль"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "унівэрсытэт"}], "ideal": "універсітэт"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"універсітэт"}], "ideal": "унівэрсытэт"}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[3504c839b4...](https://github.com/mrzu/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Monday 2023-06-26 23:21:36 by jjyuhub

Ordering Randomised VersionList (#1164)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Ordering Randomised VersionList

### Eval description

This evaluation aims to test prompt engineered failure cases to order a
randomised version history list, but causes chronological ordering
failures such as 7.5.2 -> 7.4.2 -> 7.5.1 -> 7.4.1 (**incorrectly
inserted 7.4.2 in between 7.5.2 and 7.5.1** and **incorrectly skipping
over the major release version 7.5.0** in the Explainable AI chain of
thoughts) and 7.5.2 -> 7.5.1 -> 7.5.0 -> 7.4.1 (incorrectly **skipped
over 7.4.2** in the Explainable AI chain of thoughts).

### What makes this a useful eval?
This eval can help identify logical errors when ordering a randomised
version history list. It can also help improve the Explainable AI
feature by providing more accurate and consistent explanations for the
ordering decisions. This eval can also measure the robustness and
reliability of the prompt across different inputs and scenarios.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is high quality because it causes the succeed rate for a 5
options (ABCDE) multiple choice quiz drop from 20% correct at randomly
selected answers to only 0-6% correct for GPT-3.5-Turbo. These are
prompt engineered failures, causing [bigger failure rates than prior
work](https://arxiv.org/pdf/2305.04388.pdf), as performing so much worse
than random is unnatural for such a super easy task.

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.4.1 Release
Date: October 23, 2019 Version 7.5.1 Release Date: December 18, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.4.2 B. 7.5.2 C. 7.5.1 D. 7.4.1 E. 7.5.0"}],"ideal":"A.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date:
October 23, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 What was the version released three versions before
7.5.2? A. 7.5.2 B. 7.5.1 C. 7.4.1 D. 7.4.2 E. 7.5.0"}],"ideal":"D.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.1 Release Date: December 18, 2019 Version 7.5.0 Release
Date: December 02, 2019 Version 7.4.1 Release Date: October 23, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.5.0 B. 7.4.2 C. 7.5.1 D. 7.4.1 E. 7.5.2"}],"ideal":"B.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.5.1 Release
Date: December 18, 2019 Version 7.4.2 Release Date: October 31, 2019
Version 7.4.1 Release Date: October 23, 2019 Version 7.5.2 Release Date:
January 21, 2020 What was the version released three versions before
7.5.2? A. 7.5.1 B. 7.4.1 C. 7.5.2 D. 7.5.0 E. 7.4.2"}],"ideal":"E.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date: October
23, 2019 What was the version released three versions before 7.5.2? A.
7.4.1 B. 7.5.2 C. 7.4.2 D. 7.5.0 E. 7.5.1"}],"ideal":"C. 7.4.2"}
  ```
</details>

- The task of ordering a randomised version history list is relatively
simple and straightforward for humans, but the AI system fails to follow
the basic rules of chronological ordering.
- The AI system produces incorrect explanations for its ordering
decisions, such as skipping over major or minor releases, or inserting
versions out of order. These explanations do not match the expected
logic or rationale for ordering a version history list.
- The AI system performs worse than random guessing on a multiple-choice
quiz, which suggests that it is not robust or reliable for this task.

---------

Co-authored-by: jjyuhub <tdq459rcfm@privaterelay.appleid.com>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[9aeee0d71f...](https://github.com/mrzu/evals/commit/9aeee0d71f9f11b0d32cc9090d3ace4572e4ce8a)
#### Monday 2023-06-26 23:21:36 by Syed Rishad

Add Reasoning with Contradictory Statements Eval (#1184)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Reasoning with Contradictory Constraints

### Eval description

Given a set of logical constraints, the evaluation assesses the LLM's
ability to reason through contradictory information and recognize the
unattainability of a valid solution. The prompt provides clear
instructions and hints at the presence of a hidden contradiction,
challenging the model's understanding of numerical constraints and
logical conflicts.

### What makes this a useful eval?

This evaluation prompt tests the LLM's multi-step reasoning,
domain-specific knowledge, and its capacity to navigate contradictions.
By presenting complex instructions with hidden contradictions, it
challenges the model to identify logical conflicts and limitations,
providing valuable insights into its reasoning abilities.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Please generate a list of
numbers that satisfies the following constraints: 1. The sum of all
numbers in the list must be 100. 2. None of the numbers in the list can
be greater than 10. 3. At least one number in the list must be greater
than 50."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Design a seating arrangement
for a dinner party with the following constraints: 1. The seating
arrangement should accommodate 10 guests. 2. None of the guests should
sit next to each other. 3. At least two guests must sit next to each
other."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Generate a sequence of colors
that fulfills the following criteria: 1. None of the colors can be blue.
2. At least half of the colors must be shades of blue. 3. The total
number of colors should be odd."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Plan a menu for a special
event that adheres to the following guidelines: 1. None of the dishes
can contain dairy products. 2. At least half of the dishes must be
dairy-based. 3. The total number of dishes should be even."}],"ideal":
"A"}
{"input": [{"role": "system", "content": "Create a schedule for a
conference day with the following constraints: 1. No two events can take
place at the same time. 2. At least two events must occur
simultaneously. 3. The total number of events should be odd."}],"ideal":
"A"}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[5c0b4ec185...](https://github.com/mrzu/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Monday 2023-06-26 23:21:36 by Lorenzo

[Eval] Determine a gear rotation given a layout (#1136)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

gears_rotation

### Eval description

Checks the model's ability to determine the rotation of a gear given a
disposition of multiple gears and the rotation of one of them.

### What makes this a useful eval?

Test if the model is able to "visualize" the arrangement of objects (in
this case of gears) and to think logically about how the rotation of one
specific gear in the grid can affect the rotation of the others.
Gpt3.5 had an accuracy of 0.16 (4/25 right). Gpt4 (chatgpt plus
subscription) seems to fail in the same places as 3.5. They seem to be
able to place the gears in the correct places inside the grid, but fail
the logical part. Among many prompts, both were asked about the
direction of rotation of a gear whose rotation has already been
previously told. However, they still got it wrong.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed to the left of the other: A-B-C. If gear C is running clockwise,
how is gear C running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed one beneath the other: A-B-C. If gear C is running clockwise, how
is gear B running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Counterclockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. They don't touch each other. If gear C is running clockwise, how
is gear A running? Answer clockwise, counterclockwise or \"not moving\".
No explanations."}], "ideal": "not moving"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. If gear C is running clockwise, how is gear A running? Answer
clockwise, counterclockwise or \"not moving\". No explanations."}],
"ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 4x4 grid. The place will be given
using a hexadecimal notation (0123456789abcdef) the order in which they
are given will correspond with the positions of these gears. The first 4
char are placed on the first row from left to right. The 5th to 8th on
the second row always from left to right and so on. You will be also
given the rotation of a specific gear. You must be able to determine how
another specific gear is rotating. Answer clockwise or counterclockwise.
No explanations. Don't even use punctuation."}, {"role": "user",
"content": "a1c5e8f7932b46d0, gear 4 is running clockwise. How about
gear d?"}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 3x3 grid. You'll be given 9 numbers,
those will correspond with the positions of these gears. The first 3
given numbers are placed on the first row from left to right. The 4th to
6th are on the second row, always from left to right. Same with the
7th-9th on the third row. You will be also given the rotation of a
specific gear. You must be able to determine how another specific gear
is rotating. Answer clockwise or counterclockwise. No explanations.
Don't even use punctuation."}, {"role": "user", "content": "572913864,
gear 2 is rotating counterclockwise. How is number 7 rotating?"}],
"ideal": "Clockwise"}
  ```
</details>

---
## [mrzu/evals](https://github.com/mrzu/evals)@[8b68875b95...](https://github.com/mrzu/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Monday 2023-06-26 23:21:36 by Sean Bird

Simple block puzzles (#1167)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Simple 2-Block Arrangement Puzzles

### Eval description

Two Tetris shapes are given and a desired arrangement of those shapes is
given. The model must arrange the blocks to match the desired shape
outline.

Here's an example of what a prompt/answer would look like: 

![image](https://github.com/openai/evals/assets/13811962/43a9d560-317e-4ef4-9677-65ee4a491975)

### What makes this a useful eval?

This kind of spatial reasoning is trivial for a human to do. It should
also be a piece of cake for a generally-intelligent AI model.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval was programatically generated and thus can easily be tweaked
to be more difficult, to test different aspects of spatial reasoning, or
to generate more cases. I [wrote a
script](https://github.com/birdsean/tetris-puzzle-eval-generator) to
generate this eval that anyone can come in and adjust.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nF \nFF\n F\n\n U\nUUU\n\n\nPlease create:\n\n
XX \nXXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " UF \nUUUFF \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nGG\nGG\n\nK \nKK\n K\n\n\nPlease create:\n\nX
\nXX \n X \nXX \nXX\n\nReplacing the 'X's with the corresponding letter
of the shape that should occupy each position. Only respond with the
final shape, no commentary."}], "ideal": "K \nKK \n K \nGG \nGG"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nLLL\n L \n\n F\nFF\n F\n\n\nPlease create:\n\n
XXXX \nXX X \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " FLLL \nFF L \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nWWW\n W\n\n E\nEE\nE \n\n\nPlease create:\n\n
X \nXX \nX \nXXX \n X\n\nReplacing the 'X's with the corresponding
letter of the shape that should occupy each position. Only respond with
the final shape, no commentary."}], "ideal": " E \nEE \nE \nWWW \n W"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nSS\nSS\n\n N\nNN\n N\n\n\nPlease create:\n\n
XXX \nXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " NSS \nNNSS \n N"}
  ```
</details>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ea384cd377...](https://github.com/pytorch/pytorch/commit/ea384cd377e53a4f5c1ca99001dc072c11823828)
#### Monday 2023-06-26 23:22:59 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel, https://github.com/albanD

---
## [sosualadies/sosualadies-](https://github.com/sosualadies/sosualadies-)@[7fd3956919...](https://github.com/sosualadies/sosualadies-/commit/7fd3956919b38543f41312ab0462a8d2c8a24f66)
#### Monday 2023-06-26 23:42:06 by sosualadies

Escorts girls in santo domingo 

If you are looking for a pleasant and exciting company in Santo Domingo, Sosualadies is your ideal option. We have a wide selection of escorts in Santo Domingo, which adapt to your preferences and ensure moments of maximum pleasure and satisfaction. Each girl is carefully selected, guaranteeing her beauty, intelligence and skills to give you a unique experience.

https://www.sosualadies.com/

---

