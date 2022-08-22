## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-21](docs/good-messages/2022/2022-08-21.md)


1,644,442 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,644,442 were push events containing 2,258,049 commit messages that amount to 123,719,608 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [ZombieFreak115/AlstadtModZombie](https://github.com/ZombieFreak115/AlstadtModZombie)@[85239391c5...](https://github.com/ZombieFreak115/AlstadtModZombie/commit/85239391c5b182f641babc9b14dee9cecfd9bab4)
#### Sunday 2022-08-21 00:23:28 by ZombieFreak115

full copy unto github of present dev version

small changelog from 1.7 to this upload:

- Pensylvania has a port now (for some reason it didnt before)

- Relocalized some tech text to more accurately show what bonuses they give (mining/farming output) (Still missing SOME such as "mining effiency, farming effiency etc)

- Got rid of the old vassal release decision system, and got a more compact one

- Increased the rate of internal, external and colonial migration by a decent amount (reduced migration malus from having factories in state, and increased emigration but reduced internal migration from unaccepted and non state religion pops, pops getting their everday and luxury needs make them a little less likely to emigrate)

- Added some small promotion bonuses to pops getting their everyday and luxury needs

- The India tag won't be able to be inherited with doctrine of lapse anymore

- Hannover being released by event from UK is not depentent on UK sphereing it anymore, it now depends on if the UK has it puppeted

- Put all utility, promotion and puppet release decisions under a new "hide all utility decisions" decision instead of them being seperated

- Gave Ethiopia and sokoto more land (can only colonize that land before 1880 if you take ethiopian/sokoto land anyway)

- Added a fix which makes 100% unemployment in newly colonised provinces not happen

- Buffed LF output bonus from 12% to 15%, and increased max tax from 50% to 75%

- Made it so mobilizing in a crisis dosent increase it's tension

- Implemented the decisions to take money from puppets (gives the overlord the puppet's money if they have over 100k)

- Make the max national focuses not depend on total pop size anymore

- Reduced the "nationalism" effect after you conquer uncored territory by half

- Added a host decision to disable crisis (only regular crisies for now, not colonial ones), and new host decisions to giving naughty players sanctions and infamy

- Made demotion from unemployment more linear, instead of 10% and 20% unemployment only giving 0.1, and 30% giving 0.5%, its now 0,2 0,2 0,3

- Added a system to request military or industrial good "grants" from other players, unlocked when you research economic responsibillity, will not send unless both the sender has sufficent goods, and the recipient dosent have too much in stockpile

- Gave a 5% input effiency bonus to free trade due to how shit it is

- Created a new formable, the "South andes confederation" which is meant to be a formable for bolivia/peru/chile similar to gran columbia

- Made Romaina not be releasable with CBs unless it already exists

- Statue of liberty can be given to other nations than the U.S, France picks which NW nation gets it (WIP)

- Accepted no longer get a wierd malus to colonial migration, that only primary pops didn't get

- Added decision for "fake war" to allow control of puppets in peacetime, or fix the bug where you can't control them in a war.

- Added a decision to give unit transports to coastal puppets by using steamers/clippers in the overlords stockpile

- Synthetic dyes and synthetic oil factories is now 100% invent chance

- Gas attack not working properly is fixed now

- Made a system to be able to tagswap anyone (including the host) to any other nation midgame

- WIP: Added new pictures for host decisions (mostly done)

- WIP: add more pops to underpopulated areas compared to irl, morocco and korea too? (DONE morocco, algeria and most of africa)

---
## [VaelophisNyx/Yogstation](https://github.com/VaelophisNyx/Yogstation)@[f4c7571fc3...](https://github.com/VaelophisNyx/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Sunday 2022-08-21 00:33:54 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [StatiXOS/android_kernel_essential_msm8998](https://github.com/StatiXOS/android_kernel_essential_msm8998)@[c271f286aa...](https://github.com/StatiXOS/android_kernel_essential_msm8998/commit/c271f286aac880d5bca786f2667883fa98f78679)
#### Sunday 2022-08-21 00:40:12 by Christian Brauner

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
## [Ziggypigster/SotnRandoTools](https://github.com/Ziggypigster/SotnRandoTools)@[96b50de357...](https://github.com/Ziggypigster/SotnRandoTools/commit/96b50de35760b352e8c9784d3203272fe58f3f24)
#### Sunday 2022-08-21 02:12:28 by Ziggypigster

Version 1.1.1 - Axe Armor Cloak Colors, Subweapon Rebalancing, Dagger + Bible, Defeating Doors, Adventure Seed Type Completeable, Out of Bounds Clean-up

|--AxeLord Known Issues--|
-Axe Armor Only Mode still requires you to pause to transform to Axe Armor.

August 20, 2022
-------------
Version 1.1.1 - Axe Armor Cloak Colors, Subweapon Rebalancing, Dagger + Bible, Defeating Doors, Adventure Seed Type Completeable, Out of Bounds Clean-up

|----Mayhem Changes----|
|--General Functions--|
-New Setting: Disable Mayhem Meter. Intended for Axe Armor Only, but optionally can be applied to base Mayhem.
-Random Alucard color disabled when wearing Joseph's Cloak to allow original equipment color + system cloak color.
	This will still be overriden by temporary color changes, such as Hex.

|--Bug Fixes--|
-Command Menu: Queue Mode radio buttons now properly toggle queue settings.
-Queued Rewind now transfers the "safety check" flag.
-Doppleganger, Creature Room added to Rewind Ban list.

|----AxeLord Changes----|
|--General Functions--|
-JewelSword checks now possible with AxeLord Armor! Just enter with Soul of Bat + Soul of Wolf to activate the all trigger.
	May require leaving and entering if player is able to see the wall when first activating the trigger.
-Added door functionality to access Outer Wall / Reverse Outer Wall warps.
-Wearing cloaks changes Axe Lord Armor's Color.
	Note: Joseph's Cloak changes each time equipped / unequipped.
-Armor deletion prevention added for the below armors:
	Spike breaker
	Brilliant mail
-Item usage as seperated out the Left and Right Hand effects. This allows two different effects to be activated with a small gap in between rather than waiting for the full effect animation to play.
-Additional Consumables enabled:
	Heart Refresh** (graphic not used, but effect is)
	Str. Potion
	Attack Potion
	Smart Potion
	Resist Fire
	Resist Ice
	Resist Thunder
	Resist Holy
	Resist Dark

|--Shaft Orb--|
-Reduced Base HP from 24 > 12.
-Scaling HP left intact (+1 per Vlad)

|--Galamoth (Axe Armor Only, Default Difficulty)--|
-Mayhem Difficulty HP modifier for Axe Armor Only / Boosted Axe Armor:
	1.5x per difficulty > 1.25x per difficulty.
-Base HP: 1750 > 3000
-Scaling HP: 125 per Vlad > 300 per Vlad
-Base DEF: 0 > 4
-Special boss defenses:
	Melee: As is (4 less from natural DEF increase)
	Spells: 1/2 Damage
	Faceplant / Kicky Feet:  1/4 Damage
	Subweapons: 1/4 Damage

|--Gravity Jump(Wolf/R2 + Up + Jump--|
-Initial action cost reduced from 5 > 0.
-Minimum MP to use: 5 > 4
-Additional MP Cost now triggered at the start of each gravity jump vs the end.
-Repeated Jump cost increased from 1 > 4.

|--AxeLord Armor Faceplant(Mist/L1)--|
-Form of Mist: Faceplant initial cost -2 MP, ticks 33% slower for basic movement / flight.
-Power of Mist: Reduces wolf speed momentum lost if direction is changed.
-Mist Flight now only granted with Power of Mist if user also has Form of Mist.
-Minimum time for faceplant increased from 3*8 frames to 5*8 frames.
-Faceplant now retains momentum after pressing left/right
-Faceplant allows you to change your direction, but costs momentum
	Base Momentum Loss: 36000
	Power of Mist Momentum Loss: 12000
-Faceplant contact damage changed from Petrify -> Curse
-Contact Damage: Disabled in Richter's Room.
-Contact Damage Formula: INT / 5 + Bonus Modifiers + Base Damage * 2
-Contact Damage base damage standardized:
	+2 if Neutral Input, Damage reduced by INT / 10
	+4 if Up or Down Input
	+6 if using Mist Flight
	+10 if using Mist Boost
-Contact Damage occurs far less frequently (nerfed to ~2.5 times every ~1.2 frames).
-Contact Damage now scales if the user has Momentum Active
	+2 with any momentum
-Contact Damage now gets +2 damage from RingOfVlad.

|--AxeLord Subweapons (Offhand/Circle)--|
-Default axe subweapon now requires a subweapon held.
-Default axe will now only replace cross, holy water, ashes, agunea.
-Subweapon Crit Damage adjusted for Bible / Galamoth special defenses.
	if Total Damage after crit <= 15: +2 Damage
	if Total Damage after crit <= 30: +1 Damage
-Advanced Tech: Bible/Stopwatch Axe duration does not decrease if faceplant is being used.
-New Subweapon: Dagger
	Description: Fast thrown, slightly angled down, horizontal piercing axe.
	Cost: 4 Hearts
	Damage: INT - 5;
	Damage Interval: 20 frames
	Cooldown: 5*8 frames.
-New Subweapon: Bible
	Description: Four axes in the cardinal directions follow axe armor.
	Cost: 24 Hearts
	Damage: (INT - 3) / 3
	Damage Interval: 8 frames
	Duration: 150 * 8 frames (same as stop watch)
	Cooldown: 150 * 8 frames
-Subweapon: Axe (Default)
	Description: Alucard Throwing Axe
	Cost: 4 Hearts
	Damage: (10+INT) -> INT
	Damage Interval: 9 Frames -> 10 Frames
	Cooldown: 6 * 8 Frames > 7 * 8 Frames
-Subweapon: Stopwatch
	Description: Freeze one axe in the air on the screen and activate stopwatch
	Cost: 20 Hearts
	Damage: (10 + INT)/2 -> (INT - 3) / 3
	Damage Interval: 6 > 8 Frames
	Duration: 150 * 8 frames (same as bible)
	Cooldown: 150 * 8 frames

|--Softlock Fixes--|
-Now cleans up dynamic axe armor entities cheats, in addition to the new colors, to avoid some issues when loading into save states / unusual spots.
-Prevent axe armor from holding up / down to flip stances in Akmodan II's room.
-Silver Ring / Reverse Silver Ring anti-softlock to reduce unintentional falling through the floor.
-Out of Bounds protection added to the following rooms:
	Axe Armor Hallway beneath Richter
	Reverse Axe Armor Hallway beneath Richter
	Reverse Clock Room, bottom of the spire platforms.

|--Bug Fixes--|
-Reverse Castle candle drops leading to Clockroom no longer despawn due to spikebreaker.
-Now keeps hand items when saving
-Axe Armor Only disabled when going to menu / turning off Mayhem
-Now disables all axe armor cheats if exiting axe armor only mode
-Fixed Axe Tip check for Heart of Vlad causing messages to get stuck

---
## [samboy/PopulationGrowth](https://github.com/samboy/PopulationGrowth)@[479016b12e...](https://github.com/samboy/PopulationGrowth/commit/479016b12ec733b46e1b64cf7827b5ad93704e0c)
#### Sunday 2022-08-21 03:03:13 by Sam Trenholme

OK, first stab at a model

Like http://www.talkorigins.org/origins/postmonth/may04.html population
grows very quickly if we make girls pregnant on their 12th birthday and
make them pregnant again every nine months (36 weeks).  Women can get
pregnant until they turn 50 (except, the women from the ark can get
pregnant until they die at the age of 1000) and bear children as
quickly as possible.

Because of God’s great miracles, no one ever dies from illness nor
war or of any cause except old age. As per Genesis 6:3, people post-Ark
can only live to be 120, but every person lives to be this age.

---
## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[b15331b4df...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Sunday 2022-08-21 04:15:04 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[4a2ec9b2ef...](https://github.com/PistachioPiper/genshin-buddy/commit/4a2ec9b2ef4b301d55f6ab4e675d0de5e12db5f6)
#### Sunday 2022-08-21 04:46:07 by Piper

im rly pissing bricks out here, motivation is a bitch. i have watched an entire season of my hero academia today and have barely even touched my code in a couple days. it's so silly how i have literally one thing left to do but still can't finish it. probably never gonna get it done at this rate, i just rly fucking hope that the current code  doesn't break at all, i dont think i have the patience or willpower to fix it right now. i like women i think

---
## [Oricana-16/MonkeStation](https://github.com/Oricana-16/MonkeStation)@[31c9d411a7...](https://github.com/Oricana-16/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Sunday 2022-08-21 05:35:19 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [oddtiming/Piscine_CPP](https://github.com/oddtiming/Piscine_CPP)@[7788f81cb5...](https://github.com/oddtiming/Piscine_CPP/commit/7788f81cb5a5c9b20620b4c15605754fbb6f373a)
#### Sunday 2022-08-21 05:54:02 by oddtiming

Finished CPP02

ex02 was a fucking pain in the ass, but in a good way?

---
## [Remobit/restoration-mod](https://github.com/Remobit/restoration-mod)@[ae4bb92115...](https://github.com/Remobit/restoration-mod/commit/ae4bb921158dccebf8e60b7851a41b51a2bd736d)
#### Sunday 2022-08-21 07:22:07 by Noep

stuff

- Lowered the deflection cap from 95% to 60%
-- You could never actually reach that level of deflection after Frenzy's nerf from 30/60% to 20/50%
-- Realistically speaking, this only slightly reduces effectiveness as getting to 60% deflection even before this change, assuming you have 30% from FJ + Die Hard, meant you'd have to be at 30% HP to get 60% deflection

- Oni Irezumi (Yakuza) raises the deflection cap by 20%, to a maximum of 80%
-- Again, assuming you have the 30% from FJ + Die Hard, you'd actually be downed at the point you'd get 80% deflection
--- You'll be tanky as fuck while downed tho :^)

---
## [ProfessorPopoff/mojave-sun-13](https://github.com/ProfessorPopoff/mojave-sun-13)@[2996f41136...](https://github.com/ProfessorPopoff/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Sunday 2022-08-21 07:25:40 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [beartype/beartype](https://github.com/beartype/beartype)@[bb99468f61...](https://github.com/beartype/beartype/commit/bb99468f61eaa6a12aa099b458086491d7dc9236)
#### Sunday 2022-08-21 07:36:44 by leycec

`beartype.abby.is_bearable()` optimization x 2.

This commit is the next in a commit chain heavily optimizing the
`beartype.abby.is_bearable()` tester. Currently, that tester behaves
reasonably optimally when the passed object satisfies the passed type
hint but *extremely* suboptimally when that object violates that hint;
this is due to our current naive implementation of that tester using the
standard Easier to Ask for Permission than Forgiveness (EAFP) approach.
Specifically, This commit is a biggie. We've generalized our core code
generation algorithm from its previous hidden place deeply nested in the
`beartype._decor._code._pep` submodule into a new
`beartype._check._expr` submodule. Then we renamed the surviving
`beartype._decor._code` submodule to `beartype._decor._wrapper`. And
then things kinda exploded from there. Thankfully, tests still pass and
all superficially appears to still be well with the bear. Strap your
white-knuckle sandwiches on, friends! This gonna be a deep dive into the
sheer madness of million-line codebases. (*Instantly incipient sapience!*)

---
## [damerell/crawl](https://github.com/damerell/crawl)@[a9801cc52e...](https://github.com/damerell/crawl/commit/a9801cc52efa17750a22e8f6510ec0df434585d0)
#### Sunday 2022-08-21 08:24:56 by David Damerell

Initial commit for permabuffs

This adds infrastructure for permabuffs. It's not very useful since
there aren't any permabuffs yet, but this lets me later distinguish
this commit from the commit that made Infusion into one.

We dislike Hellcrawl-style MP reservation, and aim to make changes
to spell failure chance and spellpower always relevant. If a
permabuff needs an ongoing MP penalty, it will probably be done as
an MP regeneration penalty.

You cancel a permabuff by recasting the spell. This takes no MP
(and, unlike Gooncrawl, doesn't require you to have the MP
available) and has no spell failure chance. You must, however, be
able to cast spells.

You also have an (a)bility to end all permabuffs. This can be done
even when brainless or starving; the aim here is to make it impossible
to be stuck with a permabuff that is, say, constantly miscasting
because you are brainless, but for this extra flexibility to apply
rarely enough that someone with one permabuff doesn't want to use
the ability routinely only to get vexed when they have two.

Whenever you benefit from a permabuff, there is a chance of making a
spell failure check. The chance is low enough that if you were
benefiting from the permabuff every turn, you would still see no
more miscasts than if you were casting the spell on cooldown in
vanilla Crawl. While you're not receiving any benefit, there are no
miscasts at all. These checks keep spell failure relevant.

When you do fail this check, besides the miscast, the permabuff is
suppressed for a few turns, partly based on failure severity. You
can't turn it off and on again; the suppression lasts whether or not
you end the permabuff.

Gods will not accept worship from people with permabuffs they hate,
and you also are docked a piety point every time you benefit from
one your god hates - it's not clear if there's some way HOM can
arrange to have a permabuff their god hates in order to benefit
from it forever, but now they can't.

Cancellation potions cancel both permabuffs and suppression.
Quicksilver dragon breath creates a short suppression on all
permabuffs (but hence doesn't require you to recast them all, just
to wait). Sif's wrath, and bad Charms miscasts, can end the
permabuffs but do nothing to suppressions.

-Cast artefacts suppress the operation of permabuffs altogether. Yes,
in vanilla, HOM can cast a spell, don -Cast armour, get some benefit,
take the armour off when it expires, recast the spell... but this
kind of behaviour is not something we wish to encourage.

---
## [tsdb-io/influxdb_iox](https://github.com/tsdb-io/influxdb_iox)@[8a5cd1cddd...](https://github.com/tsdb-io/influxdb_iox/commit/8a5cd1cdddcbe8ed932ddd08e953cd40c8e8d784)
#### Sunday 2022-08-21 08:49:10 by Marco Neumann

refactor: abstract change requests for cache policies (#5382)

* refactor: abstract change requests for cache policies

Tl;Dr; Lets replace the hard-coded enum of change requests with a more
flexible and easier-to-understand function-based approach. It also
unifies the interface for "initial requests" and "reactions".

Story time:

I just wanted to port over the "shared" backend with its "remove if"
functionality to the policy framework. Turns out that this backend does
not just use simple atomic operations but is basically a
"compare&exchange"-like operation (technically: GET+REMOVE) that relies
on a single mutable access lifetime to make sure that this behavior is
sane and nobody messes with the value between the GET and REMOVE. I call
this a "compound request".

The new policy framework did not support this kind of requests so I
thought how I could shoehorn it in. Basically I wanted to extend
`ChangeRequest` to support these kind of operations. But listing
combinations explicitly kinda seemed like some hack. So my brain slowly
came up with an abstract approach how to encode these operations and
after a while I was close to design some kind of mini-VM. I also
considered some ugly workarounds or to not express the "remove if"
functionality" as a policy. My nice vision of a policy framework started
to crack...

This is when sanity kicked in and I realized: every change request is
technically just a function on a (virtual) cache backend. Sure,
all-powerful Rust functions allow you to do ugly stuff that will result
in deadlocks, but with good docs and helpers for the common operations
the risk is very low. Furthermore this is already close to the system I
had for the "initial requests" and which I called a "callback backend".
So I unified both systems and made the change request abstract and all
tests pass and I think it is the better design.

Helps with #5320.

* docs: typos

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>
Co-authored-by: kodiakhq[bot] <49736102+kodiakhq[bot]@users.noreply.github.com>

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[63754eeb2a...](https://github.com/Zeodexic/tsorcRevamp/commit/63754eeb2a66d46912061094173e2fdaf6ce678d)
#### Sunday 2022-08-21 09:07:45 by timhjersted

More Phoenix Boss Changes +

-Cracked Dragon Stone also grants immunity to slow and chilled, and costs more souls
-Hellkite Dragon and Seath now interact with the environment in a very cool way (they hit walls instead of pass through them and fly above the ground instead of diving into it more often) but they can still phase through walls when needed to reach the player (further experimentation needed with the 10 and 100 value to find the best balance). It phases through walls more liberally currently to be on the safe side.
--
Phoenix Changes:
-Adjusted health stats for the phoenix birds so they reflect the in-game numbers (health is unchanged besides a small bump to the Rage)
-2nd phase warning message lasts 3x long
-Enhanced the Rage with 2 extra attacks and a 'final stand' phase NPC spawn
-The Sorrow now triggers slow at close range during 2nd phase and chilled at long range
-The Sorrow has 1 extra attack during 1st phase and also spawns animal kin to aid herself
--
-Meteor Heads do extra damage in HM for Rage fight
-Cursed Dragon's breath triggers poison debuff instead of bleeding
-Enemy Cursed breath is way less harsh with the weak debuff
-Attempted to add hostile Hellwing projectile with homing but couldn't get the animation working
-Fixed Ancient Oolcile Demon health

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fdaab867ac...](https://github.com/mrakgr/The-Spiral-Language/commit/fdaab867acdbeb1610960bd69978620e7bc90265)
#### Sunday 2022-08-21 11:17:27 by Marko Grdinić

"9:20am. I am thinking whether I should skip setting up SD on my own and just use some service, but I've decided against it. Models like SD are going to be coming out frequently in the future, so I'll be disadvantaging myself if I use a particular service that just has SD for example. I know it would take more time to set up, but I should just do it. By 'it', I mean set it up on Lambda. I have a million free requests on the free tier, so I should take advantage of it.

Any mail? > You're invited to create with DALL·E

Nice.

Any notification on RR? Nope, but I got another follower. Nice, that is what I am aiming for. Does RR has anything where I could see my daily views? It seems that sort of analytics is a premium feature.

9:30am. Let me just finish the chapter of what I am reading and then I will start writing. I thought yesterday's episode of Lycoris was particularly well paced, given how fast it was.

9:45am. Let me start. I'll leave the LycoReco thread for later. Right now, let me do some serious writing. The chapter ain't gonna write itself.

$$$

    Through a desert a traveler walks
    Even as his blood boils into vapor
    As his flesh decays and rots
    As his bones crumble into dust
    He continues moving

    As his body dies, he leaves the unneeded behind
    And continues moving forward

    His soul blazing, he traces out heavy steps
    Seeking his goal

    Far above
    The Herald of the 3 Gods' voice resounds:
    Break the Limits! Ignite the Singularity! Pursue Omnipotence!

(Euclid's Room)

The way it happened made me shiver. It felt like the grim reaper's skeletal hand combed its way through my spine. I had been killed, but the last thing that flashed through my mind was Lily's smile as I handed her the chips. Right now I can feel her happiness and kindness haunting me. I feel a momentary rage. That bitch.

She literally killed me by being kind, happy and helpful towards me.

Feeling like getting back into the game and pummeling her, I stop and rethink it.

No, wait. She wasn't the only one. If the death condition is the chip balance dropping to zero then....

I remember the day I spent with Lily. She wasn't the only one there. I remember that kindly old man who handed me my skewer only for 10 chips. I remember the pleasant atmosphere, and all the happy looking people at the amusement park. I remember the prices on the restaurant menu. I remember the job ads. I remember how the group I played poker against was betting only a single chip per tourney, but suddenly raised the stakes when they realized I was a mark. It wasn't just her, everything in the environment itself served to make her lie convincing. They were all in on it.

I thought I was some kind of renegade, beyond others, but...but, I was killed by the NPCs in the lamest way possible. I had fallen into a trap as soon as I paid my first order in the restaurant. At that point, I was inevitably going to be coaxed into spending more of my life. The smiles and the pleasant people came back to haunt me. Their smiles felt like scythes.

Outside my room, the night had already come. I lie on the bed for some time, just thinking.

A wave of fear washes over me. Now that I understand what the trap is, for the first time I wonder, how, just how could I have avoided this? It is easy for me to reload, but had I been there for real, without the benefit of being a player in a game, just how could I have avoided being scammed out of my life? Wouldn't I have certainly died?

I feel anger coming over me again.

Unacceptable. This is simply unacceptable!

[Externus gain 0.3]

I am not going to trust the NPCs again. I will modify my mind to get rid of the weaker aspects of my personality if necessary!

I do not know whether it was in response to my thought or due to the right amount of time elapsing in the death state, but as soon as I think that inside the game, I see the scenery shift from pure darkness to windy, dusty one. Like when I logged into Simulacrum for the first time, I saw a rhymeless poem accompanied by an illustration. In the image I see a transparent ghost of a man resolutely walking forward through the dusty desert, leaving a trail of footsteps behind him in the sand. As the camera panned to show the scene from above, I could see a corpse along the trail facing downwards. It was directly on the trail and there weren't two sets of footsteps as one would expect. The implication of what had happened is clear - the man died and yet continued moving onward as a ghost.

I dwell on the scene for a while and begin to see the analogy with my own situation.

Lily killed me, but it is not like I am going to put a bullet through my head to honor their achievement in reality. The opposite. I am going to go after them.

I am going to scam Lily. She still thinks I am a mark. If I lean on her...

[Gnosis check 1.6 Succeeded - Sampled 2.54]

I remember the looks the guys at the table were giving her, and get a flash of inspiration. They did collectively lose two whole human lives to me, no way they will just shrug that off. All of them are in on the scam, so maybe there is some truth about Lily being employed by the government to skin the sheep. If I threaten to toss myself over the railing, they'd take a loss, so they will do whatever they can to keep me here. They think they hold all the initiative, so that should give them confidence to give me some leeway in order to keep the scam running.

They can't possibly imagine that the entire universe they are in exists solely for me.

Using my saveloading ability, I will destroy them.

With that thought, I spend some time scheming in bed, and realize just how late it really is. It is past midnight. I'll skip dinner today. Tomorrow I have to get up for school. It is Friday, so I should have more free time after that over the weekend.

I think about figuring out how to speed up my mental processing so I can get more game time in, but realize it is too late for that. I understand that the human brain uses sleep for all sorts of reasons and that I do not need most of that on a brain core. But right now, even if it is fake, my fatigue certainly feels real. I'd really be fighting to stay away long enough to eliminate my tiredness. I could use the emotion control app, but it recommends not using it to eliminate the need for sleep otherwise I will start experiencing hallucinations and madness eventually.

I should sleep, so let me do that. Rather than try to get myself to a still state manually, I use the mind control program to do it. After that the slumber comes over me.

(At school)

I ignore the classes to do some actual studying. I do not want to immerse myself into games during class of course, but I mentioned yesterday about wanting to speed up my mental processing. Rather than waste good time during the day, I should do this work during class time.

"Blah blah blah blah...."

I am paraphrasing the teacher, this is how he sounds to me right now as I sit in front. I couldn't care less about school and don't care about caring. Once I've upgraded my memory, I'll commit all this stuff to it. So I spend the school time wisely, browsing the mind improvement guides online. Once I am back home in a safe place, I'll experiment with it for the first time.

(Euclid's Room)

I am back, and it is time to start. I toss away the book bag and lie on the bed, calling up the Helix Studio program. I make sure that I have administrative access to the brain core itself as well as control over my body and once I do that, I create a copy of my mind. I could activate it now, but if I did that my fork would not have any senses. Subjectively, it would be like all the sensations being cut off. Since I do want to play a cruel joke on what is basically me, using Helix Studio, I create a virtual space.

In the limbo browser, I have various options to choose from. Restaurants in a city, luxury apartment rooms and hotel suites, suburban houses, private jets, to more exotic picks like moon bases and undersea bases. A luxury cruise room catches my eye and I pick it. I ignore the settings and just log into it.

(Helix Studio, Regent Suite)

I find myself standing in the middle of a luxury suite living room. It is quite spacious, much larger than my own room. I glance at the furniture, and note that the tables and the chairs all seem to be designer products. There is a bar, and even a piano there. There are glass panes throughout and the light of the sun is streaming into the room from them. Outside I can see the seas. Coming closer, I see waves slowly rippling across the sea. Stepping outside to the balcony I can hear the waves and feel the wind, but nothing else. My room is just a small part of the enormous luxury cruise, but other than me, there is nobody here. It is a bit eerie, but otherwise is what I would have expected.

The function of this minor world is to just have a place to ease in new instances.

I go back into the room, and relax on the couch. Then in my mind, I bring up the Helix menus, and after doing the necessary setup like the avatar and location for my copy, activate him.

A person who looks just like me manifests a few feet away, facing sideways away from me. My bad, I didn't bother setting the orientation.

"Huh?" Confused, he starts looking around. From his perspective, the last thing he did was press Ok to copy himself. And right now he finds himself in a weird place. Taking in the sights, his eyes finally landed on me. I nock my head to the side slightly, and grin.

"Yo!" A jolt of surprise goes through him and he even does an involuntary jump. The reaction is a bit funny, I've never had anyone respond that way to me. Gears quickly turning in his head, he realizes what is going on.

"Damn! Does this mean I am the copy I made?"

"Yes." Not beating around the bush, I give it to him straight.

"That's..." He trails of for a bit, and I give him time to digest the situation. "This is pretty magical. The last thing I wanted was to make a copy so I could experiment on it, but then I found myself being that copy. It is unbelievable. It is like my desire transported me into that copy. I wanted to edit the copy and now I am the copy."

"So how do you feel?" I greased the conversation.

He does a little self check up, feeling up his face and body.

"Fine." He walks around. "Lovely place that you picked. Is it some kind of apartment suite by the sea..." He walks to one of the oversized windows, and realizes where we are. "It's a cruise ship. Yeah, I like it."

"There is nobody here, but us right now." I remarked.

"Yes, I remember the docs saying as much." Having his fill of the sights, he takes a seat opposite to me and relaxes. I take a breath and begin.

"Since you are me, I do not have to explain why we are here." To increase his processing speed and get him acclimated to it. I do not want to do that personally because it could mess me up in real life. And I would not want to do it without anybody supervising me for safety reasons. What better to supervise me than my own copy? Hence, this situation.

"Yeah. The plan is to start off slowly and make the necessary adaptations so that I can naturally think at 1,000,000 fold speeds." Just increasing the processing speed at which his mind is running would be very easy, I just need to tweak a setting. But thinking a million times faster, means that subjectively a million seconds would need to pass for him for a single one in the real world. A million seconds is 11.5 days. Imagine trying to do anything at such a pace as a human. It would be nothing more than torture.

Although I have the mind controlling program to help regulate the boredom, it is a simple fact that the brain was not designed for this kind of strain. According to the guide, for humans the memories would get bleached and erased, if one tried to force living in such a manner. Unless proper reprogramming is done, it would not work. Take recognizing speech for instance. Remembering what was said a few words ago, once processing speed was ramped up, might be a few months in subjective time. Having the proper attitude and keeping control of your emotions, does not mean you'll have the memory required to tackle the challenge.

External control of emotions has its use, but after a certain point the mind simply needs to work properly to begin with rather than be pushed in the right direction by external aids.

"How about we start with 1.5?" I have admin access to his mind, so I bring up the tool that would allow me to tweak his settings. Increasing the processing speed is a simple matter in the emulator. I find the setting quickly. "I have it. Are you ready?"

"Yes." I change the setting and confirm.

"Done. How do you feel?"

"Your voice is so slow!" He blasts out the sentence at me. After that he makes some jerky movements. He looks around and his head is snapping so fast from side to side that he looks to be in a panic. He waves his arms out as if feeling it out, and then gets up from his seat, fast walking around the room. He does a jump. Nodding to himself, he power walks back to his seats and plops himself back.

"Interesting! Very interesting!" He rushes his words. "Slow me down!"

I do as he requests.

"Done."

"It feels like being inside water. It is like the world is more solid and I have to push to make the same kind of progress. It is not pleasant." He shrugs. "I have to remind myself to slow down if I want to keep my regular pace. It is quite hard." His mind became fast, but his body and the world remained the same.

"I guess we'll have to learn to walk and talk from scratch if we want to take advantage of this."

"I am not sure I'd be able to handle speeds of 10x. Something like 2x would already be my limit." Introspecting, he gave his opinion.

Hmmm, not good. I can't really use this to get better at sports just like that. I suppose it would be possible once I get used to it. But no, forget that line of reasoning. I guess even with the enormous processing ability of the brain core, the only thing it gives me is the ability to work rather than direct power. It will be up to me to take advantage of it.

"Oh well. You'll be the one we'll be experimenting on, so I won't tell you to enter the self improvement loop right away. What do you want to do now?"

"I think I'll do some gaming. Since I no longer have a body in the real world, that is the only thing I can do now. I'll speed myself up 10,000x times and speed up the game by the same amount and get some game time in that way." I remember that 10,000x seconds is almost 3 hours. A minute at that speed would be a week. So in 4 minutes, he could spend an entire month in the game.

"At 10,000 speed, 4m for me would be a month for you. I can wait a bit for you to get into it." On mental command, I bring up the core's clock, and note it saying 3:15pm. "You've got access rights to your own mind, and I've allocated 10% of the core just for your own needs. Check it out." Given the core's capacity, this was still an enormous amount. Converting that into actual intelligence is not something that would be done soon.

"Yeah, I see it." He took a moment to confirm.

"If you need anything, since we are literally on the same brain, just send me a text message."

"Ok. I guess I'll get started with the game. See you around?" He wondered.

"Go get them." I encourage him. "As for me, I guess I'll do our homework. I'll come back in half an hour. I'll send you a message once I am here. Bye."

"Bye." I log out, leaving my copy alone in the character limbo.

---

The admin me logs out, and I am now alone in the suite. I go to my own settings, increase my processing speed by 10,000x and after that, do the same for the simulation. I note the real world time which is 3:18pm. I write it down in a file on my personal desktop. Even at 10k speed, I realize the core's programs are still snappy. I am sure if it was my desktop rig, it would have slowed to a crawl subjectively. It just goes to show that the programs on the core were made for people who think really, really fast, so the programs themselves need to match that. I am sure that if I tried browsing the internet right now, it would be unbearably slow.

I let myself deflate a little and lounge of the sofa, feeling its grungy texture. I have plenty of time to think and get started. A week here would be a minute in the real world.

Sigh. I've lost quite a bit. I no longer have my own body in the real world, and I can't just ask the admin me to give it to me. Unless I can get another body, I’ll be stuck on the core forever. I am not really the Euclid the others know. But that is fine.

I toss the pillow that I am playing with aside, and get up. It is time for payback. I'll see how far I can go just saveloading, and after I reach a dead end with that, only then start reprogramming my mind to give myself actual superpowers.

Having made the decision I load the last save.

(Heaven's Key, At the entrace to the inn)

"Yeah, it sucks. This is because the city gets newcomers out of thin air, and to prevent them from just loitering in the streets, this policy has been instituted." My guide Lily shrugged, sympathizing with me. "Don't worry, I'll come back tomorrow and look for a job with you."

The last time this happened, I trusted Lily and gave her my entire balance of 240 chips, after which I died instantly. There are is no need to think about it so deeply.

"Hmmmm..." I pretend to think about it. "I'll hang on to it then. I'll pay you later."

Immediately, disappointment flashes across Lily's face. She scowles at me.

"If you don't pay me here, and go to jail, you'll be there for 5 years." She pressured me. "The city is not kind to those who don't want to work. You should reconsider, 240 chips that you have is nothing. You'll get 500 as a sign up bonus in most places."

Going to jail might be a threat to ordinary people here, but it means absolutely nothing to me.

"I do not really care. I just got my memory back. I remember why I died."

"Huh?" She looked at me with confusion.

"I killed myself back on Earth." She grimaced. Knowing more of the context, I am guessing that is less out of sympathy and more because how difficult it will make to get the chips that I won back from me.

"W-why?" She dared ask.

"I didn't want to go to school, so my parents started forcing me to get a job. So I said, fuck this gay world, and jumped off the top of the school building." I think up a based backstory on the spot.

"..." She looked at me with amazement.

"So I won't work!" I declare, looking at her straight in the eyes. "I will just gamble, and if I lose, I'll toss myself over the railing again. Why is the point of living just to do favors to others? I will live the way I want to - as a gamer!"

Looking at her reaction, it seems her brain is getting fried. Good, good! She looks at me out of the corner of her eye, with an angry expression. I show her my stell will and discipline cultivated through half a lifetime of playing computer games.

"Fine, be that way! Don't come crying to me when the police come to lock you away!" She stomped away. I looked at her back until she disappears around the corner and then let out a sigh.

Bluff check passed!

Based.

Well, it is not like it would take much to get through this. If I don't want to pay her, what can she do? Nothing really.

I spend some time dwelling on it. The street where was I was was cloaked in deep blue now and stars were twinkling in the sky. I couldn't hear much in the way of people, and the rowdy sounds of the amusement park in the distance have faded. In front of me I can only see a tiny shadow cast by the entrance of the inn behind me. I turn around and enter, closing the door behind me.

(Heaven's Key, Inn room)

I lie awake in bed with my eyes closed. I meant to get some sleep, since it is late in the game world, but I am not tired at all. If I had to say how tired I was, it is about how I was before I came into the game world. Since in the real world I just came back from schoool, I still have a lot of energy in me.

Sigh, what do I do now? I can't lie in bed this whole time. By the time I fall asleep, the morning will come.

...I think about it for a while. Yeah, why not go out for a bit?

Let's go for a walk outside. During the day I will have Lily hounding me and trying to find a way to separate me from my chips. At this point, I've seen the verge of the city, but I haven't had a chance to properly explore it, so I might as well do that now. I guess I'll end up being tired in the morning, but I'll figure out how to deal with that then. By the looks of it, my mental state, including fatigue gets transfered from the outside, so taking a nap in the luxury cruise might be enough to deal with it.

Having decided, I slip out of the bed, put on my clothes and quietly slip out of my room.

(Heaven's Key, The streets)

Compared to the day when the sun was shining, it is quite cool during the night, though not enough to be freezing. I'll warm up once I start moving.

I take a look around to see where the edge is, and then go in the opposite direction. I think it would be hard to get lost in the city as you can see the buildings grow in size the further they get to the center. Due to that it is easy to look down the row of street blocks and see what the direction to the perimeter is. Right now I am in a suburban era, so most of the buildings are the size of regular houses with few small apartments scattered around. Compared to the day, the city has lost its luster, and the shining gold of the streets is not a tarnished yellow, but if I look closely at the floor below, I can see the glint of the stars above. There aren't any lamps around to provide lighting, but the city is very high up and not obscured by the clouds, so the light of the stars and the reflected light of the moon is enough to see in the darkness.

I start making my way deeper without a particular goal in mind, keeping my eyes and ears open, and trying to warm up my body.

(Heaven's Key, Seated at the restaurant)

I spend an hour or two just going around like that. It is a fairly unique experience to be walking in the middle of the road, of what seems to a golden ghost city. Despite spending quite a bit of time just walking, I am yet to see any one person. Though I haven't, I doubt the city is literally empty. I am guessing everyone is just holed up inside. As I am started to get tired of walking all the time, and have long since warmed up, I pick a seat outside one of the restaurants I spotted and take a break.

Phew.

This is pretty boring, actually. But all this quietness is giving me an idea.

Maybe the city is actually much larger than the population it supports. In that case, that opens up the posibility of easily finding a place to rest for myself. That in is exorbiantly expensive in order to trim the sheep. I should find my own pad to rest. It is likely, there is a free apartment somewhere that I can occupy. In order to find one, what I will have to do it try entering some of these buildings, I looked around for emphasis, and try the doors to see if any of them are unlocked. If they are, that means that most likely they are unoccupied.

Also...I swallow, finding my throad starting to get parched. I need a drink of water from somewhere. I get up from my seat, and try the restaurant door. I can't get the door to open as it is locked. If I could make it into the kitchen, I could find something, but I guess not.

I need to find a source of water somewhere. Tap water in an apartment, a public fountain, a public toilet has washbasins, anything will do.

Let me try finding an apartment.

(Heaven's Key, Exterior corridor of an apartment block, 8th floor)

I put my hand on the door of the apartment, and try turning. No luck again. I've gone through quite a few apartment buildings already and just wasted my time. I though I could find a room that is unused, but no such luck. Everything is locked.

I save the game.

Then I try pounding on the apartment door, loudly so that anyone inside could hear.

"Hello, is anyone inside!?" I slam the underside of my first on the door, making a ruckus. I do that for a minute and wait. Nothing. I tried this a few times already. My conjecture is that the apartments are in fact empty, but nobody is inside. They are locked, maybe to prevent vagrants such as myself from occupying them.

This is not working. Damn it, I am going to have to find a way to pick the lock for these. But even if I knew how to do that, I could look it up online, just where would I find lockpicks in this place?

In some supermarket maybe, but I've made an interesting observation. While those smaller marts near the perimeter has stocked shelves, all the shops deeper inside the city are empty. It is quite bizzare. So it is pointless to try robbing a supermarket.

While I am not so parched as to start panicking, I can always go back to the inn, I really need to find a water source for the sake of the future exploration.

Forget the apartments, let me try finding a public toilet somewhere. I need to take a whiz anyway.

(Heaven's Key, Public Toilet)

It took me a whole hour of wandering around just to find one. At this point I am pretty much lost in the city, and will have to reload to get back to the inn, or ask somebody for directions when the morning comes and people come out. I enter the male sections, and seeing some golden faucet and sinks, I immediatelly turn the handle hoping to get some water.

...Nothing comes out. At this point I am starting to get agitated. I turn the handle of every faucet in the building, but nothing comes out.

'The inn will provide you meals, but don't worry the people here don't need to eat physical food anyway.' At this point, I remmeber Lily mentioning that the people here don't need food. But I am clearly both hungrier and thirstier than I was before. Was she lying? It makes sense that she would have lied about a lot of things, but that offhanded comment was so unecessary, that I can't help but believe it was the truth. Truth or not though, it is not actionable advice.

I have no choice, let me try searching for a fountain. I hope it is not dry.

(Heaven's Key, Park)

I climbed up a nearby apartment building and spotted a park, which gave me the idea to try looking for a fountain there. Somehow you'd expect to find foundatins at parks, right? Right now I am at the entrance to the park area and I head deeper inside, looking for one.

The flora here is similar to what would be found on Earth, but the grass, the leaves and the trees have yellow hues on them instead of green. I got off the rock path and try stepping on some golden grass, carefully. I do it slowly, since if the grass is made of metal, that means I might step on some spikes, and I do not want to pierce my foot by accident. Thankfully the wildlife here isn't murderous and the grass turns out to be soft, much like in real life. I could lie down on this, no problem.

To the side I hear some rustling and when I turn, I can see a figure looking at me in the distance. At first I thought it was a person, but then I realize it is transparent and I can see through him to the golden bark of a tree behind him. There is a tense moment, but then the figure turns away and moves out of sight behind some trees and bushes.

A shiver passes through me. It feels like I'd just seen a ghost.

Startled, I hurriedly make my way deeper into the park. I don't forget to save!

(Heaven's Key, Park center, Fountain)

As I made my way here I saw various kinds of ghostly figures peering at me. I was prepared to just run if I had to, but it does not seem like they were aggressive, just curious as who was coming here. But the spooky atmosphere of the park at night combined with literal ghosts looking at me, served to raise my tension.

Deeper in the park, I finally found a fountain made of gold in a central area. A jet water spring in the air before coming and down and flowing between its basins. I gave the water a touch, finding it cool, and then gathered some in the cups of my hands and gave it a taste. After hours of walking through the city, I was completely parched, and the cool water felt great as it went down the throat of my heated body. After that initial experiment, I sip from the fountain directly until I am satisfied, ignoring the looks of the ghosts around me.

"Haaaahhhh!" I exhale in satisfaction.

After filling myself with water, I relax myself on one of the benches, not caring about my surroundings. I gaze at the stars, and just enjoy the scenery for a while.

Some time passes like that.

I guess I can forget about finding actual food. I thought I would die of dehydration at the rate things are going. I take a look around me, seeing the ghosts have gone away. At first I thought the ghosts were scary, but the way they move feels like they are actual people. If they are, I could try striking up a conversation with them. I spend some time thinking about what questions I could ask people here, and then try to get myself to leave the seat.

I really need to talk to a person who could give me an honest answer for how things work here instead of seeing me as a mark.

For example, I really need to ask where people get their food supplies. I really doubt that there are farms on the other side of the city like Lily told me. There were no children during the day, so I doubt that cows are getting reincarnated just so we could eat them. Besides, Lily already let it slip that food is not necessary. I need to figure out the trick to that.

Mhhhhh! I stretch myself and then force myself up from the bench. I need to get on with it.

I can't forget that I do not have a real world to go back to. I am just a program being run on a brain core. I can't just stop playing the game if I get tired of it. Unless I can make progress, I'll get erased. If the admin me, just sees me lying in bed, that is what will really happen. I'd definitely do that if I was in his shoes, and I was only a short time ago. I need to keep moving forward. Let me find an information source. I need to make sure whether these ghostly apparitions can be communicated with.

If the admin me turns to take a peek, I need to show him my will and determination. I do not want to make him feel bad about himself by showing him a loss in the virtual world.

(Heaven's Key, Deeper inside the park)

...

$$$

10:30am. https://www.theguardian.com/science/2022/aug/18/scientists-discover-how-mosquitoes-can-sniff-out-humans

I am not particularly focused on this part.

1:10pm. Let me stop here for the morning. I am finding it hard to write this, but it is necessary. The next chapter will have action, but here I am establishing Euclid's foundation in the city, so it needs to be done.

Let me paste it into the docs.

2k works. Right now I am at 5.7k. Not too bad. I need to make the conversation with Mickey, and then the final scene of the chapter will come where Euclid finds 'that' place. That experience will serve as his moral foundation in the new world.

1:15pm. Let me go have breakfast."

---
## [chaperyolo/chaperyolo.github.io](https://github.com/chaperyolo/chaperyolo.github.io)@[9d1c81ee7e...](https://github.com/chaperyolo/chaperyolo.github.io/commit/9d1c81ee7eb64a0fa03152c8a950502e57590730)
#### Sunday 2022-08-21 12:14:39 by chaperyolo

added more details and fun

some jokes here and there
life is not that serious you know

---
## [Wolfsurge/Paragon](https://github.com/Wolfsurge/Paragon)@[42c4f6e3e3...](https://github.com/Wolfsurge/Paragon/commit/42c4f6e3e385243ef7bb3f60da40e77200bea443)
#### Sunday 2022-08-21 13:04:48 by Wolfsurge

Remove stupid FPS limit when in GUIs (fuck notch's shitcode)

---
## [flygarn12/realtek-poe](https://github.com/flygarn12/realtek-poe)@[88cb11bd6c...](https://github.com/flygarn12/realtek-poe/commit/88cb11bd6c6a3fdd69dff2638aeeac7d1d936258)
#### Sunday 2022-08-21 13:49:01 by Alexandru Gagniuc

realtek-poe: Fix memory leak in poe_reply_consume()

When thinking "embedded", it's a good idea to stay the fuck away from
malloc(). Falling out of scope is a free garbage collector. Port
config and state arrays followed this advice, but for some reason, the
command queue did not.

No worries, free() is used in poe_reply_consume(). No problemo! Crisis
averted! Did you spot the several failure modes which return before
the free() call. In these modes, a malloc()d command is taken off the
queue, and not free()d. The pointer falls out of scope and memory lost.
Quod Erat Demonstratum.

To fix this, free() the command before hitting any exit paths.

Signed-off-by: Alexandru Gagniuc <mr.nuke.me@gmail.com>

---
## [MuchMarts/Afirmacijas](https://github.com/MuchMarts/Afirmacijas)@[f99b09fb41...](https://github.com/MuchMarts/Afirmacijas/commit/f99b09fb41dfbed8033d429bf7e27ccc8e5de434)
#### Sunday 2022-08-21 14:26:36 by DrgnInventor

PAIN AND SUFFERING

Gods have lied potatos have grown and forks have won. This stupid thing aint working and im not sure why I dont want to rewrite it but like why you no work

---
## [rigis1/fix](https://github.com/rigis1/fix)@[fbd70d116c...](https://github.com/rigis1/fix/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Sunday 2022-08-21 14:35:54 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[cfb35120b4...](https://github.com/srsbsns5/GAN-GDDS1/commit/cfb35120b44f843736211e11c2a056d82355ae93)
#### Sunday 2022-08-21 16:29:02 by schmidtheimer

Fixed the bugs stacey mentioned

Bezel Rollie warna pelangi, satu malam di Temasek
Royal flush that, bukan lagi suspect
Aku takkan answer, korang dekat WhatsApp
Malam di Temasek, guess who got their luck back?
You all the same, mana uniform?
Imma be an hour late to my funeral
Imma be an hour late to my funeral
Royal flush that, malam di Temasek
[Verse 1: Joe Flizzow]
Kalau luar ada ghost depan pintu
Mungkin ku tinggal rumah berhantu
Dulu selalu pegang besi yang berkarat
Sekarang jari manis ada 6 karat
A lot of people funny with the money
Throwing hundos, renting Lambos
IG uploads with the gun pose, rеally dumb moves
I’m in the Range rеading Sun Tzu now you don't know
Jangan kacau musuh buat silap
Ini silat Mat Kilau style M Daud Kilau
If you ain’t making sense I hope you saving pennies
Lawat kawasan Wawasan 2020

[Chorus: SonaOne]
Bezel Rollie warna pelangi satu malam di Temasek
Royal flush that bukan lagi suspect
Aku takkan answer korang dekat WhatsApp
Malam di Temasek, guess who got their—
Bezel Rollie warna pelangi, satu malam di Temasek
Royal flush that, bukan lagi suspect
Aku takkan answer, korang dekat WhatsApp
Vida on run flat, guess who got their love back
You’re all the same, mana uniform?
Imma be an hour late to my funeral
Imma be an hour late to my funeral
Royal flush that, semalam di Temasek
[Verse 2: Joe Flizzow]
Kalau dalam itu ghost ada binatang
Maksudnya harimau dah terlepas kandang
A tiger never gon lose its stripes
Piloto Capitan, Flizz never miss his flights
Takeoff, tapi bukan bukak baju
Dulu jersi 36 diaorang kasi nombor 1
Bahasa berita bahasa baku masa depan Michio Kaku
Kings always draw Queens mungkin ini Seri Ratu
Field Marshall akan sentiasa turun padang
Always on time, bukan kadang-kadang
Barang rare korang jumpa jarang-jarang
Stadium status panggil gua Kallang

[Chorus: SonaOne]
Bezel Rollie warna pelangi, satu malam di Temasek
Royal flush that, bukan lagi suspect
Aku takkan answer, korang dekat WhatsApp
Semalam di Temasek, guess who got their luck back?
You all the same, mana uniform?
Imma be an hour late to my funeral
Imma be an hour late to my funeral
Royal flush that, semalam di Temasek

[Verse 3: Joe Flizzow]
Two aces before the flop never worked a 9 to 5
Mula kecil enterprise now I’m BIG hypnotize
Semua stadium kita ball ada barang kita call
GoPro untuk amatur hanya 8K bila roll
Hi def bodycams when the cops patrol
Send me telegram incase they tap them phones
Got a hundred bands got to spend it on my folks
Forgiattos, a hundred spokes
Two aces before the flop never worked a 9 to 5
Mula kecil enterprise now I’m BIG hypnotize
Semua stadium kita ball ada barang kita call
GoPro untuk amatur hanya 8K bila roll
You all the same, mana uniform?
Be an hour late to my funeral
Satu malam di Temasek
Royal flush that, bukan lagi suspect

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4ca2a57ae7...](https://github.com/TheBoondock/tgstation/commit/4ca2a57ae7535433d20adfd1d4804769f3b109cd)
#### Sunday 2022-08-21 18:22:18 by Justice

Adds the Mothroach (#68763)


About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[b4f19a7e0f...](https://github.com/TheBoondock/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Sunday 2022-08-21 18:22:18 by John Willard

Greatly increases Pun Pun's abilities and strengths (using desk bells, cross stun immunity) (#68870)


About The Pull Request

Pun Pun has a new AI, with it they received the following:

    Instead of screeching/roaring/scratching/jumping/rolling, Pun Pun will instead sing/dance/bow/clear throat/sign.
    Pun Pun now rings desk bells instead of finding random shit to pick up, and doesn't intentionally seek out weapons.
    Pun Pun has a higher chance of giving people stuff in their hand, so the Bartender can give them a drink and let them go walking around.

Additionally:

    Pun Pun is now immune to being hardstunned by walking into them, giving them a little more bite for greytiders beating them up.
    Monkeys can now use desk bells.

Why It's Good For The Game

I like Pun Pun and when Monkey AIs were originally added, there was a note about giving them a unique AI. Since we're slowly turning the poor monkey into an actual Bartender assistant, I find it thematic that they would ring the bell and give out drinks in their hand, as if the Bartender taught them themselves.

For the hardstun immunity, I mostly did it because I find it annoying for a Bartender to have to carefully navigate around Pun Pun to not knock them over and make them drop an instrument (or anything else) in their hand, but it also works as a buff to people trying to kill them. Pun pun is a unique monkey so I don't believe they should be as easy to kill as any other.

Desk bell addition was necessary for Pun Pun to use it.
Changelog

cl
add: Pun Pun now gives stuff in their hand frequently and rings desk bells.
add: Pun Pun now has gentleman-like emotes, rather than screeching and roaring.
balance: Pun Pun no longer looks for weapons in their off time.
balance: Pun Pun is no longer vulnerable to stuns by being walked into.
qol: Monkeys can now use desk bells.
/cl

---
## [sjp38/linux](https://github.com/sjp38/linux)@[a3952db4ed...](https://github.com/sjp38/linux/commit/a3952db4ed757252fcfe2241d4de87e57b5c51a2)
#### Sunday 2022-08-21 18:32:27 by Johannes Weiner

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
## [royalit31/registry.gimp.org_static](https://github.com/royalit31/registry.gimp.org_static)@[2863abdff4...](https://github.com/royalit31/registry.gimp.org_static/commit/2863abdff4f751a916e95f457544825e538e25dd)
#### Sunday 2022-08-21 18:38:47 by royalit31

ية (ar) Български (bg) català (ca) čeština (cs) Dansk (da) Deutsch (de) English (en) español (es) فارسی (fa) français (fr) עברית (he) हिन्दी (hin) hrvatski (hr) magyar (hu) Հայերեն (hy) bahasa Indonesia (id) italiano (it) 日本語 (ja) ქართული (ka) taqbaylit (kab) 한국어 (ko) Nederlands (nl) polski (pl) português brasileiro (pt-BR) Română (ro) pyccкий (ru) slovensky (sk) slovenščina (sl) svenska (sv) Türkçe (tr) українська (uk) Tiếng Việt (vi) 简体中文 (zh-CN) 繁體中文 (zh-TW) 2.0.0 2.0.0-rc.2 2.0.0-rc.1 1.0.0 1.0.0-beta Semantic Versioning 2.0.0 Summary Given a version number MAJOR.MINOR.PATCH, increment the:  MAJOR version when you make incompatible API changes MINOR version when you add functionality in a backwards compatible manner PATCH version when you make backwards compatible bug fixes Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.  Introduction In the world of software management there exists a dreaded place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.  In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.  As a solution to this problem, we propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules are based on but not necessarily limited to pre-existing widespread common practices in use in both closed and open-source software. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.  We call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.  Semantic Versioning Specification (SemVer) The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.  Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it SHOULD be precise and comprehensive.  A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.  Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.  Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.  Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.  Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.  Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.  Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY also include minor and patch level changes. Patch and minor versions MUST be reset to 0 when major version is incremented.  A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92, 1.0.0-x-y-z.–.  Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85, 1.0.0+21AF26D3—-117B344092BD.  Precedence refers to how versions are compared to each other when ordered.  Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence).  Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically.  Example: 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1.  When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:  Example: 1.0.0-alpha < 1.0.0.  Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:  Identifiers consisting of only digits are compared numerically.  Identifiers with letters or hyphens are compared lexically in ASCII sort order.  Numeric identifiers always have lower precedence than non-numeric identifiers.  A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.  Example: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0.  Backus–Naur Form Grammar for Valid SemVer Versions <valid semver> ::= <version core>                  | <version core> "-" <pre-release>                  | <version core> "+" <build>                  | <version core> "-" <pre-release> "+" <build>  <version core> ::= <major> "." <minor> "." <patch>  <major> ::= <numeric identifier>  <minor> ::= <numeric identifier>  <patch> ::= <numeric identifier>  <pre-release> ::= <dot-separated pre-release identifiers>  <dot-separated pre-release identifiers> ::= <pre-release identifier>                                           | <pre-release identifier> "." <dot-separated pre-release identifiers>  <build> ::= <dot-separated build identifiers>  <dot-separated build identifiers> ::= <build identifier>                                     | <build identifier> "." <dot-separated build identifiers>  <pre-release identifier> ::= <alphanumeric identifier>                            | <numeric identifier>  <build identifier> ::= <alphanumeric identifier>                      | <digits>  <alphanumeric identifier> ::= <non-digit>                             | <non-digit> <identifier characters>                             | <identifier characters> <non-digit>                             | <identifier characters> <non-digit> <identifier characters>  <numeric identifier> ::= "0"                        | <positive digit>                        | <positive digit> <digits>  <identifier characters> ::= <identifier character>                           | <identifier character> <identifier characters>  <identifier character> ::= <digit>                          | <non-digit>  <non-digit> ::= <letter>               | "-"  <digits> ::= <digit>            | <digit> <digits>  <digit> ::= "0"           | <positive digit>  <positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"  <letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J"            | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T"            | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d"            | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n"            | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x"            | "y" | "z" Why Use Semantic Versioning? This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.  A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.  As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.  If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.  FAQ How should I deal with revisions in the 0.y.z initial development phase? The simplest thing to do is start your initial development release at 0.1.0 and then increment the minor version for each subsequent release.  How do I know when to release 1.0.0? If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.  Doesn’t this discourage rapid development and fast iteration? Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.y.z or on a separate development branch working on the next major version.  If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly? This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.  Documenting the entire public API is too much work! It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.  What do I do if I accidentally release a backwards incompatible change as a minor version? As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Even under this circumstance, it is unacceptable to modify versioned releases. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.  What should I do if I update my own dependencies without changing the public API? That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. We would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.  What if I inadvertently alter the public API in a way that is not compliant with the version number change (i.e. the code incorrectly introduces a major breaking change in a patch release)? Use your best judgment. If you have a huge audience that will be drastically impacted by changing the behavior back to what the public API intended, then it may be best to perform a major version release, even though the fix could strictly be considered a patch release. Remember, Semantic Versioning is all about conveying meaning by how the version number changes. If these changes are important to your users, use the version number to inform them.  How should I handle deprecating functionality? Deprecating existing functionality is a normal part of software development and is often required to make forward progress. When you deprecate part of your public API, you should do two things: (1) update your documentation to let users know about the change, (2) issue a new minor release with the deprecation in place. Before you completely remove the functionality in a new major release there should be at least one minor release that contains the deprecation so that users can smoothly transition to the new API.  Does SemVer have a size limit on the version string? No, but use good judgment. A 255 character version string is probably overkill, for example. Also, specific systems may impose their own limits on the size of the string.  Is “v1.2.3” a semantic version? No, “v1.2.3” is not a semantic version. However, prefixing a semantic version with a “v” is a common way (in English) to indicate it is a version number. Abbreviating “version” as “v” is often seen with version control. Example: git tag v1.2.3 -m "Release version 1.2.3", in which case “v1.2.3” is a tag name and the semantic version is “1.2.3”.  Is there a suggested regular expression (RegEx) to check a SemVer string? There are two. One with named groups for those systems that support them (PCRE [Perl Compatible Regular Expressions, i.e. Perl, PHP and R], Python and Go).  See: https://regex101.com/r/Ly7O1x/3/  ^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$ And one with numbered capture groups instead (so cg1 = major, cg2 = minor, cg3 = patch, cg4 = prerelease and cg5 = buildmetadata) that is compatible with ECMA Script (JavaScript), PCRE (Perl Compatible Regular Expressions, i.e. Perl, PHP and R), Python and Go.  See: https://regex101.com/r/vkijKf/1/  ^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$ About The Semantic Versioning specification was originally authored by Tom Preston-Werner, inventor of Gravatar and cofounder of GitHub.  If you’d like to leave feedback, please open an issue on GitHub.  License Creative Commons ― CC BY 3.0

Please review it.

---
## [jmarshall23/DNF-reimposition](https://github.com/jmarshall23/DNF-reimposition)@[7d7987b624...](https://github.com/jmarshall23/DNF-reimposition/commit/7d7987b6243892edbe0fc232c253980a02d02160)
#### Sunday 2022-08-21 18:50:32 by Justin Marshall

Added "damn that's the second those alien bastards shot up my ride" to map05_night and new music from LOTB

---
## [GerHobbelt/thread-pool](https://github.com/GerHobbelt/thread-pool)@[ac271eed2a...](https://github.com/GerHobbelt/thread-pool/commit/ac271eed2a1412e8cdc1d8621ce054b2f866ee17)
#### Sunday 2022-08-21 19:03:03 by Ger Hobbelt

magic number 7: the big one. Fixes various race conditions surrounding normal and abnormal threadpool / application termination.

Turns out at least on MSWindows when application code calls the exit() RTL API to abort the application (or calls abort() or otherwise) that threadpool worker threads may fail to terminate (causing lockup at application exit) or are already 'disappeared' before that last wait_for_tasks() gets a chance to tickle them into terminating.

Yes, I know this commit introduces "that last wait_for_tasks()" call as can be seen in the `destroy_threads()` part of the diff, but that call is *key* to resolving the lockup situation: when lockup at application termination occurs, this is due to the thread workers not getting signaled to wake up when they just entered condition.wait() at that time. So what wait_for_taks() must do is "keep on screaming", i.e. *repeatedly* invoking notify_all() to ensure all threads get a chance to reach their cond.wait() and then get signalled while the destroy_threads() has now set the 'shutdown mode' by setting 'running = false', which the worker threads can now see and act accordingly, i.e. terminate.

As this is a kind of a wild mix (some threads MAY still be busy with other stuff, not yet reaching their cond.wait() while others already have and have terminated) so the wait_for_tasks() also checks repeatedly whether any threads still need an opportunity to get notified; only when all threads have terminated (and thus the thread.is_joinable() API produces TRUE for them all) does the call finish and pass control over to the next bit: the loop where threads are cleaned up through thread.join().

This commit assumes various other patches to have been included already; this is extracted from this series of dev commits:

---

Revision: a6ea0901a0569348c81ae230e5d855bdd3286a3b

- better document the new purpose of `sleep_duration`:

  @brief The `wait_for_tasks()` poll cycle period, in milliseconds, where after each `sleep_duration` wait_for_tasks() will be incited to broadcast its waiting state to the worker threads so they wake from their potential short slumbers and check all shutdown / reactivation conditions and signal back when they've done so. Consequently, when there's no tasks pending or incoming, thread workers are not woken up, ever, unless `wait_for_tasks()` explicitly asks for them to wake up and check everything, including 'pause mode' and 'shutdown/cleanup' (running == 0).

  If set to 0, then instead of sleeping for a bit when termination conditions have not yet been met, `wait_for_tasks()` will execute std::this_thread::yield(). The default value is 10 milliseconds.

  Note that the `sleep_duration` value is only relevant to execution timing of `wait_for_tasks()` when one of these conditions apply:
  - the threadpool has been put into 'pause mode' and there are no more lingering tasks from the previous era being finished, while the queue stays in 'pause mode'.
  - the threadpool is shutting down (running==false, due to threadpool instance cleanup & destruction, usually part of an application shutdown)

       std::chrono::milliseconds sleep_duration = std::chrono::milliseconds(10);

- Limit the maximum poll period of `wait_for_tasks()` to 1 second. (This is only relevant in spurious 'exit on catastrophic failure' cases and has yet to be observed 'in the wild'. Yet the poll period is important for the 'yell at worker threads to wake up and check' bit that makes them terminate (as intended) when you're in shutting-down mode.

Revision: 12253b6610ed2f237660abeb91446beab27f63d1

fixes:

- push_task(): document which (member) variables are under which mutex' overwatch and makee sure the code matches this.
  + Case in point: the `tasks_total` counter MUST be kept in sync with the actual `tasks` queue size hence it must be managed by the same mutex, or you will have situations where `get_tasks_running()` is lying to you and we CANNOT afford that.
  + Second case in point: `task_done_cv` has an opposing purpose and MUST be wrapped by its own mutex to prevent deadlock between wait_for_tasks() and any worker threads. Introducing `task_done_mutex` for that.

- reset(): first (re)create threads, *only then* unpause() them -- when they weren't paused already *before*. Use the `unpause()` API explicitly as it has been augmented and signals the threadpool to observe the state change (going out of 'pause mode').

  Previously, this wasn't necessary, because the threadpool threads would cycle like crazed rodents on meth when they got put into 'pause mode'; now we have improved the waiting game any state change that expects the threadpool threads to start working again requires a signal to them (.notify_all()). That signal sent by `unpause()` will only be *observed* by the threads when we're sure they are actively waiting already, hence they MUST have been created again first.

- unpause(): see above. Now signals all worker threads that sleepy times are over and the task queue must be checked, once again. Previous code didn't need this as the worker threads were not sleeping in `pause mode' but were continuously polling.

augmentations:

- [TO BE SUBMITTED] now accepts NEGATIVE thread_counts during pool creation (or reset()) to create a pool that's occupying all CPU cores MINUS thread_count. This is useful when you want the pool to occupy ALMOST all cores, but leave one or more for other, unrelated, jobs.

- thread workers now wait for a signal to wake up when in 'pause mode', as they always already were in normal run mode.

  Q: Why don't the thread workers have to use wait_for() with a timeout to allow them to check independent state changes, such as 'running', to help them detect when the application/threadpool is shutting down/destroyed?

  A: because the threadpool destructor invokes wait_for_tasks(), which incessantly will broadcast to the workers, waking them periodically to have them inspect the shutdown state until they all have responded. wait_for_tasks() already necessitated the use of a wait_for() timeout-based poll loop already for other reasons (one of both sides of the fence need to timeout and periodically check spurious / race conditions, because .notify_one() and .notify_all(), by definition, do not wait for the intended observers to start observing through theeir .wait() calls. wait_for_tasks(), as part of its own 'poll loop', will repeatedly send those signals (.notify_all()) to reach all worker threads, no matter how busy and occupied they have been with previous tasks. This same 'keep on yelling' approach helps us when shutting down the pool as the same repeated .notify_all() will now reach all threads in a most timely fashion to have each worker thread check the shutdown (`running`) state and act accordingly. Which is why we can safely have the worker threads use the simpler .wait()-only approach.

  Note that, at least under Windows 10, threads MAY be nuked silently under fatal/crash/exception conditions, in which case the thread disappears even before it was able to do anything simple, like updating the `alive_threads_count` count, because the thread worker code simply will cease to run and exist. Fortunately, thread::is_joinable() detects this fact -- which was a very important reason to have `wait_for_tasks()` be a wait_for_tasks()-timed poll loop, as we CANNOT guarantee on all OSes that worker threads will be able to wake up and act once a severe-enough fault condition has occurred in the application/task code. From our own observations, it already seems sufficient to directly, bluntly, call the standard `exit(N)` RTL API to have this happen to you: no exception of any kind will be reported then, yet all threads will be joinable as they will have *vanished* already.

WARNING: hence, `get_alive_threads_count()` will be unsafely optimistic and depending on that number at such disparate times will surely cause your application to lock up on exit on semi-random occasions. This is completely independent of the `running` state, as this is driven by external factors.

- [TO BE SUBMITTED] catch unexpected C++ and SEH/hardware exceptions occurring in your tasks/worker-threads in the outer layers of the worker thread: as this is a catastrophic, fatal, condition anyway (your application state is largely unpredictable by then already), the thread will terminate, but we now have a fighting chance of catching and reporting such errors at least. As C++ and SEH exception handling cannot co-exist in a single function, we have the following call chain, where each wraps the next one: workerthread_main() --> __worker_SEH() --> __worker() --> worker(), where worker() is the core threadpool thread code, waiting for and executing tasks once they arrive.
  When you need special handling of this (fatal) scenario in your application, you can create a derived class and override the workerthread_main() with your own. Observe the code comments when you do to ensure continued proper operation of the threadpool. (__worker_SEH() returns a boolean indicating whether its termination was due to normal or abnormal (i.e. catastrophic failure) termination, while you may pass a string to them, which will now have been filled with the relevant and available error information. The given implementation prints this info the STDERR -- but you can replace that behaviour in your override.

---
## [lm40/VOREStation](https://github.com/lm40/VOREStation)@[e089978527...](https://github.com/lm40/VOREStation/commit/e08997852748d1155820139dfacf4745c9181ce3)
#### Sunday 2022-08-21 21:17:08 by Rykka

Ports Taur Loafing from Cit-RP & Chompstation13

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

Bear in mind that this presently only works for the drake-taur bc it's the only one that has sprites for it. The code is there, just enable can_loaf and set the offset accordingly to match if you want to sprite more taur loafs.

---
## [Z4ph0d42/420-Station](https://github.com/Z4ph0d42/420-Station)@[c6cd28503e...](https://github.com/Z4ph0d42/420-Station/commit/c6cd28503efc66a7b38d77f31744a5ae154b452b)
#### Sunday 2022-08-21 23:47:33 by James

Merge pull request #4 from StormAGeddonz/Pouches

FUCK GIT I HATE IT FUCK THIS PIECE OF SHIT

---

