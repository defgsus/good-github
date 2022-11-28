## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-27](docs/good-messages/2022/2022-11-27.md)


1,829,297 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,829,297 were push events containing 2,436,425 commit messages that amount to 142,533,496 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [nytmyr/Server](https://github.com/nytmyr/Server)@[e271dc8ca4...](https://github.com/nytmyr/Server/commit/e271dc8ca4b67a8d8cc357e8b016a937588fcdb3)
#### Sunday 2022-11-27 00:09:55 by toxin06

[Bots] AI Revamp, add all holds, delays, thresholds, min thresholds, character heal settings. Bard fixes.

All group features for combat range and behind mob now work in raids

Every spell type can have a delay, minimum and maximum threshold to cast.

The delay is how quickly a bot can cast that type of spell, the timer starts from the beginning of the cast. If you set this to 10 seconds, as soon as a spell starts casting, another will start in 10 seconds provided it isn't on cooldown or has stacking/immune blocks.

The minimum threshold is the percent of health when a bot will stop casting a spell.
-Escapes, Hate Reductions, Lifetaps and Shaman In-Combat Buffs (Canni) will rely upon the bot's OWN health. (When do you want said bot to start trying to drop aggro, when they reach 80% until 20%? Do they lifetap starting at 60% and never stop till they die? (0%).

Threshold or maximum threshold is the percent of health when the bot will begin casting that type of spell.

Casters will now output what type of spell and what spell they are casting for all spell types except buffs.

Casters will now output all those messages to the entire group or raid, filterable by Pet Response.

Casters now dispel, escape, lifetap, snare and root automatically.

SKs will now cast their bonus hate spells as the spell type in-combat buffs rather than nuke so it can be held if needed.

Shamans will still Cannibalize using in-combat buffs, however you can set the minimum threshold to control when they stop Cannibalizing and the Maximum threshold will be based off their mana to start Cannibalizing.
--Shamans will never start to cannibalize if their mana is above 90% or their health is below 50% regardless of the minimum/maximum setting.

SKs, Paladins and Clerics will not cast their in-combat buffs if they have hit their stop melee level.

SKs, Rangers, Wizards, Enchanters and Bards will now cast hate reduction spells.

Necros/SKs will cast their Darkness line as the Snare spell type.
--Necros will not cast Insidious Retrogression.

Bards will now start casting their songs before they fade instead of waiting for them to fade so there is no gap in buffs.
-------
Casters no longer try to cast DoTs, nukes, roots or snares if it may result in aggro. Once enough aggro is built up by the tank to where they don't think they'll pull aggro, they will begin casting.
--SKs & Pallies will always cast these regardless of aggro, use holds or thresholds if you want them to stop.

Resist checks for spells will now take into affect level differences as well. (Higher level mobs are more likely to resist a spell than a lower level mob with the same resist stats)

If a target mob is Undead, Summoned or Plant, the appropriate classes will cast the appropriate nukes if available.
-Necromancers will nuke plants with Defoliation if they are of level.

Bots will verify spell immunity before casting all spell types.

Roots are held by default.

Bots will now honor Blocked Buffs. You can use this to get bots to cast other buffs. If you only want Virtue for example you would block Faith, Kazad's Mark and Ward of Gallantry.
--Look at bot spells lists on Allaclone to see what spells they can cast to control this.

Bots will now cast buffs that contain Illusions if you don't block them (Boon line for example.)

You can now set your player characters/clients to specific heal thresholds and delays that bots will respect.
-------
Pets will be healed using the default delay settings and can be toggled on/off with ^holdpetheals
-You can control when they start healing pets by stances, stances will only be used for this now as everything else is customizable
-The exception to this is that Warriors, Paladins and Shadowknights will enter a taunting state by default if set to Aggressive. This can still be toggled off by ^taunt as usual.

The thresholds for stances are as follows:
-Reactive will do all the regular default heals starting with HoTs @ 85%, CHs @ 70%,  Regular Heals @ 55% and Fast Heals @ 35%
-Efficient will start with CHs @ 70%, Regular Heals @ 55%, Fast Heals @ 35%
-Balanced (default) will start with Regular Heals @ 55% and Fast @ 35%.
-Burn will only cast Fast Heals/Regular Heals starting at 35%.
-BurnAE will only Fast Heals/Regular Heals starting @ 25%.
-Aggressive will ignore all and not heal at all, you don't want a tank stopping to heal.

-If a bot cannot cast a Fast Heal, CH or HoT, they will try the next best spell in order of: Fast Heal->Regular Heal->Complete Heal->Heal Over Time.
-Any Heal that casts in 2 seconds or less is considered a Fast Heal

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[fccd833526...](https://github.com/MTandi/tgstation/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Sunday 2022-11-27 00:13:25 by GoldenAlpharex

Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

---
## [daph0213/zulip](https://github.com/daph0213/zulip)@[23a776c144...](https://github.com/daph0213/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Sunday 2022-11-27 00:32:55 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [SgtHunk/tgstation-1](https://github.com/SgtHunk/tgstation-1)@[db66590e7e...](https://github.com/SgtHunk/tgstation-1/commit/db66590e7ecf0b5c4db86cef04c7d6b58b56b3b0)
#### Sunday 2022-11-27 01:39:30 by san7890

Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Sagit-A13/kernel_xiaomi_msm8998](https://github.com/Sagit-A13/kernel_xiaomi_msm8998)@[44bc736e8b...](https://github.com/Sagit-A13/kernel_xiaomi_msm8998/commit/44bc736e8bf87f3cc7b5e8fc4d390be860a4a218)
#### Sunday 2022-11-27 02:25:30 by Christian Brauner

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
## [MushiTea/21438_ChaoticCurrent_REPO](https://github.com/MushiTea/21438_ChaoticCurrent_REPO)@[3ee931ba41...](https://github.com/MushiTea/21438_ChaoticCurrent_REPO/commit/3ee931ba41c01eea0f2f299c1f727f40ce3c5d1f)
#### Sunday 2022-11-27 03:02:32 by yeeT787

Omg girl do you watch forged in fire? Cuz I want you to pick usable steel from this pile of scrap metal to use as the base for your blades. They must meet the following parameters, a length between 8-10 inches, a full tang with a length of 3-4 inches, and width from spine to cutting edge of at least 1 1/2 inch but no longer than 2 1/2 inches. In the next round, you will be attaching handles to your blades to turn them into fully functional weapons. And for the third round we will put it through a series of tests, such as, dummy stab for sharpness, chain chop for durability, and a sheet metal stab for edge retention. And the two winners of the third round will be sent to their home forges to recreate an iconic weapons from history. The winner of the final round will go home with the title of forged in fire champion and a check for $10,000. Your time starts, now!

Essentially what we did was fix claw,slide, and arm positions and I added manual arm just because - Srinirek

---
## [lllgts/android_kernel_lge_msm8998](https://github.com/lllgts/android_kernel_lge_msm8998)@[bdb8056ef8...](https://github.com/lllgts/android_kernel_lge_msm8998/commit/bdb8056ef821a1e5328c13f61b0ae26faf5ba001)
#### Sunday 2022-11-27 03:13:55 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [Aar0nSm1th/Projects](https://github.com/Aar0nSm1th/Projects)@[cff544632c...](https://github.com/Aar0nSm1th/Projects/commit/cff544632c1b4d24bef68a221e89a892b685d14e)
#### Sunday 2022-11-27 04:12:35 by Aaron Smith

Create Spaceman Game | JavaScript

This was a video game that I created during my time at CodeHouse. It was made after less than a month of coding experience and it's my personal favorite project so far. The game isn't perfect and has a few bugs, but I'm more proud of myself for this project than I am for any of my other personal creations.

Game Instructions:
You're a spaceman who now finds thousands of asteroids falling towards him! Use the arrow keys in order to move the spaceman up and down or side to side to avoid the asteroids. Avoid 30 asteroids in order to win, but keep going to get a high as a score that you can if possible! Whenever you die, refresh the page to restart the game.

---
## [atamanbillor/conception](https://github.com/atamanbillor/conception)@[984de4fa9b...](https://github.com/atamanbillor/conception/commit/984de4fa9b75e54e179297ed5a641a4085c19d95)
#### Sunday 2022-11-27 04:13:56 by atamanbillor

README

Hi!

My name is Ataman Billor. I was born in Adana, Turkey and moved to Auburn, Alabama when I was 7 years old.

I like to go by my moniker, Ato (Otto). I speak Turkish, English, intermediate Spanish, and elementary French!

The motto is "Plus Ultra" and Stay Stoked

Plus Ultra - a latin proverb that essentially translates to continuously striving for excellence and improvement in yourself and your objectives

Stay Stoked - Something I say a lot... I just believe that life should be full of passion and an eagerness to learn and staying fired up about the future! I always try to Stay Stoked!



I like to do a lot of stuff:

I was ranked #1 (USTA) in the state of Alabama in tennis in 2013
Hitchhiked across Europe in 2016
Recognized in PhD Thesis of Dr. Gokhan Ozden while doing an undergraduate research fellowship at Auburn University
Gave a presentation about the Academy of Aerospace Quality Project to several NASA Quality Assurance Team members during a symposium
Rock climbed 3000ft to the summit of El Toro in Hidalgo, Nuevo Leon Mexico in 2018
Backpacked for 18 continuous days and ~ 400 miles via the Pinhoti Hiking Trail
Worked alongside award winning Chefs in elevated gastronomical environments
Worked as a Farm Hand in a regenerative agriculture project (Controlled Burns, Holistic Land Management, Forest Management, Constructed 3000 ft^2 Green House, catered VIP dinners, Milled lumber, processed and cared for Livestock, participated in Farmers markets, etc)
Traveled the USA servicing and maintaining Wind Turbines as a Wind Turbine Technician Contractor
Graduated with a degree in Mechanical Engineering from Auburn University in 2022
Rode my bicycle from the Atlantic Ocean to the Pacific Ocean in 2022 (~ 5 months, 10000 km)

( hopefully that didnt all sound too egotistical... just some insight on what I have been up to up until now :) )

AND NOW

I am learning how to program (I learned how to use MATLAB in uni, however, I am now interested in other programming languages)

up first, PYTHON

Thanks for checking me out!

---
## [greatspider135/free-programming-books](https://github.com/greatspider135/free-programming-books)@[d692e894a6...](https://github.com/greatspider135/free-programming-books/commit/d692e894a67555aff442e99c6acf0873213684dd)
#### Sunday 2022-11-27 06:27:29 by Ramona Saintandre

added Python cheat sheets (#5011)

* added Python cheat sheets

Thanks for hosting this.
Just getting back into coding, and since I have been looking for resources for Python. 
I thought I would add what I have found. 

Happy hacking

* removed the spaces 

Hi sorry, it took so long to resolve this conflict. 
Actually took me a while to figure out how to do.

Thanks again so much for hosting this.

* alphabetize

* linespacing

* alphabetize

Co-authored-by: Eric Hellman <eric@hellman.net>

---
## [xambassador/cockroach](https://github.com/xambassador/cockroach)@[1d04cec7c5...](https://github.com/xambassador/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Sunday 2022-11-27 06:42:33 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [PaulT89/rust](https://github.com/PaulT89/rust)@[7a49959ea4...](https://github.com/PaulT89/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Sunday 2022-11-27 07:31:31 by Remo Senekowitsch

xorcism: remove rstest dependency (#1590)

rstest uses proc macros, which make the tests timeout due to long
compile times. Replace rstest with a custom declarative macro.

Brings test time from 7.5 seconds to 0.8 seconds on my machine.

Drawbacks:
* more indentation
* module structure of tests is flipped around

both of those seem minor to me. 

Although declarative macros can be hard to read for those unfamiliar, 
that was already somewhat the case with rstest's magic in my opinion. So
I personally don't think it's worse in terms of the students being able to
understand the tests.

The only other alternative I see is to disable the online tests 
altogether and leave a note about that in the exercise description. That
probably wouldn't be that bad, since people solving this hard exercise
most likely have a solid local setup. But it would still be cool to run
the tests online as well.

https://github.com/exercism/rust/issues/1513

---
## [nfagerlund/bevy-tablestakes](https://github.com/nfagerlund/bevy-tablestakes)@[087cfe3147...](https://github.com/nfagerlund/bevy-tablestakes/commit/087cfe3147e43a68ce61cb53c71ebbf68d9abdeb)
#### Sunday 2022-11-27 07:38:14 by Nick Fagerlund

Ok!! Baby's first state transition! It sucks but it works!

Right, dealing with dynamic types in anything less than a whole-hog
Reflect-driven way turned out to be a nonstarter. And doing this
generically is ass because of the need to add generic versions of each
system to the app. So!! For the time being, I'll just store the "done"
condition on the state itself, and I'll rep it as an enum so I can cram
the next state directly in there. The clone derive turns out to be
crucial for getting it back _out_ again... oh, although, actually I
think mem::swap is good enough for this. But probably not much faster.
So I'll leave that be for now.

Anyway! This transitions out of roll into free! Now to go the other way
around... and then I need to fix the roll animation speed.

---
## [Pranav-V/CS371M-Final-Project](https://github.com/Pranav-V/CS371M-Final-Project)@[a7a4b9df64...](https://github.com/Pranav-V/CS371M-Final-Project/commit/a7a4b9df64fb27484e3909df6784dc11d178e700)
#### Sunday 2022-11-27 07:47:56 by Abbhinav Jayaraman

I hate my life, data is now null again for some reason.

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[9b3dcbd666...](https://github.com/crowlogic/arb4j/commit/9b3dcbd66647ca36a5c5559bb82f3e029ae0b3f3)
#### Sunday 2022-11-27 08:18:30 by Meatwad

fuck shit damn
fuck shit damn
something something i forgot
no one reads this
fuck it all

---
## [Nukechickenu64/Abaddon](https://github.com/Nukechickenu64/Abaddon)@[6c42446811...](https://github.com/Nukechickenu64/Abaddon/commit/6c424468115306d2e2a85cf13663c7507885382c)
#### Sunday 2022-11-27 08:19:08 by Nukechickenu64

fuck you paradise this my shit now idc if its cobblerigged to

---
## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[25d4afc869...](https://github.com/Ebin-Halcyon/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Sunday 2022-11-27 08:55:30 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [robotduinom/PsychonautStation](https://github.com/robotduinom/PsychonautStation)@[7d04edb6e2...](https://github.com/robotduinom/PsychonautStation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Sunday 2022-11-27 09:03:40 by Profakos

Mail sorting helper, and disposals fixes (#70861)

## About The Pull Request


![image](https://user-images.githubusercontent.com/2676196/198695007-53db1b70-845f-46a9-b98a-e146bb53951b.png)

This PR adds a mail sorting map helper, which during Late Initialization
will apply a sorting location index to the mail sorting disposals pipe
under them. I have replaced the varedits with all mail sorters with the
appropriate map helpers. I have thoroughly tested this, making sure
packages arrived to every location, where possible.

I have also fixed a few issues with the disposals network:

**Tramstation**

- One of the random maintenance segments had a place with no disposal
pipes. This has been fixed
- A sorter was looking for chapel and library packages, but it actually
meant to look for engineering packages
- There was no dormitory mail sorter, I have added one

**Metastation**

- There was no dormitory mail sorter, I have added one

**Icebox**

- There is no experimentor lab in icebox, but there is an
"experimentation" lab, which is good enough, so I have added it as a
location

**Deltastation**

- There was no dormitory mail sorter, I have added one
- Virology was not connected to the disposals network. However, on every
other map, it has a one way connection. I have hooked it up just like
that, so virology mail will arrive safely, and virology trash will go
into space as usual.

**Kilostation**

- Genetics packages were rerouted to the psychologist office

Unsolved issue on kilostation: there is no experimentor on this station,
and there is no space for a disposals in the circuits lab, so sadly, if
you send a package to this destination, it will come back to the mail
sorting office.

**Future improvements**

The TAGGERLOCATIONS list, which is used to retrieve the labels of the
various tags, is frankly unorganizable, and hard to expand. I have
delayed fixing this for a future PR.

I kinda wish to remove the sortType variable, as it is no longer
necessary to have it around with these helpers, but sadly, this would
ruin downstream maps, so I have no plans for this at the moment.

## Why It's Good For The Game

While mapping, having to constantly compare a comment in flavor_misc.dm
to figure out what to varedit a disposal mail sorter to is rather
annoying. These map helpers, similar to the access helpers, will help
with this issue.

Its also good if mail actually arrives.

## Changelog


:cl:
qol: added a mail sorting map helper, to allow mappers to create
disposal networks faster
fix: fixes several non working disposal mail targets that never received
their packages
/:cl:

---
## [noigeaR/pcsx2_gamedb_fixes](https://github.com/noigeaR/pcsx2_gamedb_fixes)@[87abacc632...](https://github.com/noigeaR/pcsx2_gamedb_fixes/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Sunday 2022-11-27 09:34:07 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [salariarahul/MyTimer](https://github.com/salariarahul/MyTimer)@[ab54cd9c84...](https://github.com/salariarahul/MyTimer/commit/ab54cd9c84b60dd77b70bb401da52e5df057447e)
#### Sunday 2022-11-27 09:34:40 by rahul salaria

- Adding multiple schedules(breakfast at 6AM, lunch at 1PM, dinner at 8PM,
 Jogging at 6AM.,)
 - We can create a schedule task with task name, start and end time.
 - USE schedule task button for creating a task on dashboard.

---
## [gilbertguan2385/guava](https://github.com/gilbertguan2385/guava)@[8a676ade61...](https://github.com/gilbertguan2385/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Sunday 2022-11-27 09:35:45 by cpovirk

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[29d766e25f...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/29d766e25f18c5030972562ed649832077cdfc95)
#### Sunday 2022-11-27 10:35:10 by LemonInTheDark

Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

---
## [NimBlemations/Vs-Joe-Stick](https://github.com/NimBlemations/Vs-Joe-Stick)@[b542ee7519...](https://github.com/NimBlemations/Vs-Joe-Stick/commit/b542ee7519c2b96b4978766c440f4c3ae7e35d72)
#### Sunday 2022-11-27 10:41:54 by NimBlemations

fuckin haxeflixel thing fuck you i'm walkin' here

fuck you i'm walken' here

---
## [NimBlemations/Vs-Joe-Stick](https://github.com/NimBlemations/Vs-Joe-Stick)@[f41185b7e6...](https://github.com/NimBlemations/Vs-Joe-Stick/commit/f41185b7e673ae8e555a5fc387da92bc8f986ad3)
#### Sunday 2022-11-27 10:44:04 by NimBlemations

oh fuck sorry, forgot it wasn't haxeflixel in the workflow

damn.

---
## [Lindonrow/StorytimeOfficialMod](https://github.com/Lindonrow/StorytimeOfficialMod)@[3de255c40b...](https://github.com/Lindonrow/StorytimeOfficialMod/commit/3de255c40bc2d2524bdb419b1980102b2c0d7a0c)
#### Sunday 2022-11-27 11:23:39 by Isengriff

Chapter 8: The Fertility Ritual Update Part 1: Part 3

In this time of pain and devastation, one man rises above all the rest as a beacon of hope in a dying land. That man is me, because I finally managed to fucking get this shit into a playable state.
There are still bugs and tons of things I'd like to fix but frankly most of that has more to do with HAR than me, so I figure I'll just save it all for Part 2 when hopefully things are more settled.
Why am I writing this, I'm literally the only person that uses this mod except the evil one, and I'm 99.99% sure nobody is reading this. If you are reading it, leave a comment below. Why not? But you won't, because you don't exist. Bla bla bla... can I just play the damn game now?
Please send a prayer to Allah/God/Yawheh/Guanyin/Whichever Hindu god you pray to for this sort of situation/Some other guy/idk.

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[ea1e6ff95f...](https://github.com/AnywayFarus/Skyrat-tg/commit/ea1e6ff95fb48e198162f2bb99448777bc7f9e06)
#### Sunday 2022-11-27 11:39:49 by SkyratBot

[MIRROR] Adds a preference that disables intensive rendering on different multiz layers [MDB IGNORE] (#17737)

* Adds a preference that disables intensive rendering on different multiz layers (#71218)

## About The Pull Request

It's kinda hacky, but it is nearly the same as just rendering one z
layer.
We allow people to ENTIRELY REMOVE most plane masters from their screen.
This has the side effect of disabling most visual effects (AO is a big
one) which saves a LOT of gpu.

We rely on planes being essentially layers to ensure things render in
the proper order. (outside of some hackyness required to make parallax
work)

I've kept parallax and lighting enabled, so visuals will still look
better then multiz pre plane cube.
It does also mean that things like FOV don't work, but honestly they
didn't work PRE plane cube, and FOV's implementation makes me mad so I
have a hard time caring.

Reduces gpu usage on my machine on tram from 47% to 32%, just above the
27% I get on meta.

I'm happy with this.

Oh also turns out the parallaxing had almost no cost. Need to remove it
as a side effect of what I'm doing but if I could keep it I would.

There's still room for in between performance options, like disabling
things like AO on lower z layers, but I didn't expect it to make a huge
impact, so I left things as is

Also fixes a bug with paper bins not respecting z layer. It came up in
testing and annoyed me

## Why It's Good For The Game

Ensures we can make multiz maps without running into client performance
issues, allows users to customize performance and visual quality.

## Changelog
:cl:
add: Adds a new rendering option to the gameplay preferences. You can
now limit the rendering intensity of multiz levels. This will make
things look a bit worse, but run a LOT better. Try it out if your
machine chokes on icebox or somethin.
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a preference that disables intensive rendering on different multiz layers

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0815a7e269...](https://github.com/treckstar/yolo-octo-hipster/commit/0815a7e269c7be31f7a838f73721196b21728ad2)
#### Sunday 2022-11-27 12:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[9396da49fc...](https://github.com/greenhas/spg_website/commit/9396da49fc74dfe1e87cf28f68f50daf6f456866)
#### Sunday 2022-11-27 13:48:24 by Spencer Greenhalgh

post Boosted kiddo's motivation to help put away the dishes by convincing her to think of it as a magic trick (making the dishwasher's contents 'disappear'). Boosted my own by remembering it's now legal to play Mannheim Steamroller Christmas music around the house.

---
## [PixelExperience-Devices/kernel_xiaomi_lmi](https://github.com/PixelExperience-Devices/kernel_xiaomi_lmi)@[32a6e1c1e8...](https://github.com/PixelExperience-Devices/kernel_xiaomi_lmi/commit/32a6e1c1e85832012983a1d656a0e439c1c0775c)
#### Sunday 2022-11-27 15:09:30 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[03bc97ade5...](https://github.com/tgstation/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Sunday 2022-11-27 15:20:26 by necromanceranne

Nukies Update 6: Interdyne is here for you! Medical Supplies and Atropine! (#71067)

## About The Pull Request

Quite a few changes overall to the nuclear operatives tactical medkit.
The kit is more of a full suite of equipment for performing field
medical duties as a nukie.

- I've split the medkits between two kinds. Basic and premium. Medical
bundle has the premium kit.
- Basic contains additional amounts of basic c2 chem patches, some spare
atropine autoinjectors, sutures and regen mesh, and some basic medical
equipment for tending wounds. 4 TC (as it was before). That's it.
- The premium kit is a far more useful full suite of advanced medical
equipment, MODsuit modules, medical supplies and cybernetic implants,
including the combat hypospray and the combat defib. 15 TC.

**In the premium kit, there is:**
- It has a box of beakers with powerful healing chems. Omnizine,
salicylic acid, oxandrolone, pentetic acid, atropine, salbutamol and
rezadone.
- The combat injector is empty, so you can load it as necessary.
- There are advanced sutures and regenerative mesh packs. They don't
work through spacesuits, but are invaluable for wound repair. Especially
burns.
- There is a surgery arm toolset so you can do field operations without
lugging tools.
- There is a surgery processor module that comes preloaded with advanced
surgeries, a threadripper module, and the combat defib module. The
module works entirely like a combat defib, but you don't need to lose
your belt slot to use it.
- The surgeries are revival, the upgrade surgeries (like vein
threading), brainwashing (did you know they didn't get access to
brainwashing, I think this is a shame) and the better tend wounds
option.
- The nightvision medical hud doubles as a pair of science goggles.

**Atropine changes:**
- Atropine now stops bomb implants from autoexploding. This does **NOT**
stop you from manually detonating the bomb. (This is possible even when
you're dead and haven't left your body)
- As a result, nukies get atropine medipens so that they can potentially
stop themselves detonating prematurely, or stop their allies detonating
prematurely. They have a little pamphlet to help explain how their
microbomb works.

## Why It's Good For The Game

Straight up: The medkit is ass.

The meds in the injector sucks, just getting c2 meds in patches is kind
of insulting for something granted to you from an uplink item (and also
you get those for free with your ~~xbox~~ infiltrator medical room so
lol), and operatives just got the kit for one reason and one reason
only. That combat defib as a _weapon_.

Fuck that. So the kits now much better as a way to both support yourself
AND your team through providing a range of improvements you can provide
the squad, while also not undermining the reason why people may have
wanted the kit (that defib). I would really like to see more nukies
attempt to support one another in combat, and a medic operative is a
role that needs love to make that a reality.

**Edit here**: I reintroduced a low end kit with more c2 medical
supplies _if you want them_. I can see how someone might pinch all of
the medical supplies like a cunt, so maybe we should have a failsafe for
that.

A huge culprit of the lack of value of support meds was usually that
ops...explode when they die. If a medic can pop atropine into an op
before they die, they might be able to save them, or an op could pop
themselves with atropine prematurely to maybe stave off death.

## Changelog
:cl:
balance: Splits the nuclear operative combat medical kit into two
versions: basic and premium.
balance: Basic contains additional amounts of basic c2 chem patches,
some spare atropine autoinjectors, sutures and regen mesh, and some
basic medical equipment for tending wounds. 4 TC (as it was before).
balance: The premium kit is a far more useful full suite of advanced
medical equipment, MODsuit modules, medical supplies and cybernetic
implants, including the combat hypospray and the combat defib. 15 TC.
balance: Atropine stops bomb implants from automatically detonating on
death. You can still manually activate your bomb implant (even when you
are dead).
balance: Operatives start with an atropine pen to stop themselves and
their allies from detonating so they can hopefully be saved by a medical
operative.
add: There is a pamphlet to explain this in the nuclear operative's
survival box.
add: I'm not telling you to read the pamphlet, but you should probably
read the pamphlet.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[d7efa00d9b...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/d7efa00d9b9382f546d2bdec98dd41a4c93771d8)
#### Sunday 2022-11-27 17:18:15 by Reinazhard

 i fucking hate myself

Signed-off-by: Reinazhard <reinazhard@gmail.com>

---
## [DieFrauen/CaC-Batch](https://github.com/DieFrauen/CaC-Batch)@[e8759644a7...](https://github.com/DieFrauen/CaC-Batch/commit/e8759644a7c69cca0c0393512ba6e26cc9a36e54)
#### Sunday 2022-11-27 17:28:58 by Mish

Update README.md

FIRST SAMPLE limited offer

CONTENTS

FIRST SAMPLE cdb (card database) file
pics folder
scripts folder

Here are the first batch of cards released for this exclusive offer, 5 cards each for the first 3 clients to order. They are as follows.

Client 1: Arc Des
- Light Magician               /46990001 (NEW - 11/27/2022)
-                              /46990002
-                              /46990003
-                              /46990004
-                              /46990005

Client 2: BlazeFenix
- Infernal King Spectri-Oh     /46990006 (NEW - 11/27/2022)
- Firetruck Monkey Business    /46990007 (NEW - 11/27/2022)
- Ghoti Starlight              /46990008 (NEW - 11/27/2022)
- Ghoti Genesis                /46990009 (NEW - 11/27/2022)
- Azzar - Elegance of the Ghoti/46990010 (NEW - 11/27/2022)

Client 3:
-                              /46990011
-                              /46990012
-                              /46990013
-                              /46990014
-                              /46990015

HOW TO USE

In order to register these cards in your YGOPro build, you should extract the contents in this Zip file into your Expansions folder, the pictures and scripts for each card go in their respective folders along with all other files from different expansions. Make sure to check your repositories and everything else is in order. To play cards in Expansion files online with friends, you must use the LAN + AI mode, as these contents are not available in Server based duels.

Thanks for your patronage.

Die Frauen 2022

All stock images used for these cards were retrieved from online sources throughout the web and are intended to be free and fair use, if you find that your, or someone's work is used here, feel free to provide source information to be listed below or to request its takedown.

STOCK IMAGE SOURCES

Light Magician - AviArts / https://www.reddit.com/user/ThePeachyPanda/
Infernal King Spectri-Oh - Pyron - Darkstalkers / source pending

---
## [DieFrauen/CaC-Batch](https://github.com/DieFrauen/CaC-Batch)@[060ee9528d...](https://github.com/DieFrauen/CaC-Batch/commit/060ee9528d816683722780066e5ad6eaff6c44c8)
#### Sunday 2022-11-27 18:23:07 by Mish

Update README.md

Die Frauen's Create-A-Card Batch

CONTENTS

- cdb (card database) files (1)
- pics folder (6)
- scripts folder (6)
- high resolution images folder (6)

CARDS

- Light Magician               /46990001 (NEW - 11/27/2022)
- Infernal King Spectri-Oh     /46990006 (NEW - 11/27/2022)
- Firetruck Monkey Business    /46990007 (NEW - 11/27/2022)
- Ghoti Starlight              /46990008 (NEW - 11/27/2022)
- Ghoti Genesis                /46990009 (NEW - 11/27/2022)
- Azzar - Elegance of the Ghoti/46990010 (NEW - 11/27/2022)

HOW TO USE

In order to register these cards in your YGOPro build, you should extract the contents in this Zip file into your Expansions folder, the pictures and scripts for each card go in their respective folders along with all other files from different expansions. Make sure to check your repositories and everything else is in order. To play cards in Expansion files online with friends, you must use the LAN + AI mode, as these contents are not available in Server based duels.

Thanks for your patronage.

Die Frauen 2022

All stock images used for these cards were retrieved from online sources throughout the web and are intended to be free and fair use, if you find that your, or someone's work is used here, feel free to provide source information to be listed below or to request its takedown.

STOCK IMAGE SOURCES

- Light Magician - AviArts / https://www.reddit.com/user/ThePeachyPanda/
- Infernal King Spectri-Oh - Pyron - Darkstalkers / source pending

---
## [Bersder/Grasscutter](https://github.com/Bersder/Grasscutter)@[88bc5c4c54...](https://github.com/Bersder/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Sunday 2022-11-27 18:27:29 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[75e9bd4d53...](https://github.com/seanpdoyle/turbo/commit/75e9bd4d530e6606af3ffadf82455be41d4450de)
#### Sunday 2022-11-27 19:30:07 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [EmilyMansfield/volume-setter](https://github.com/EmilyMansfield/volume-setter)@[d57ce25015...](https://github.com/EmilyMansfield/volume-setter/commit/d57ce25015eeec9d32d49a1e262c4372da7b82bc)
#### Sunday 2022-11-27 20:07:12 by Emily Mansfield

Change profile of waiter through setter over gRPC

Because the waiter process (called with `--wait`) sets its configuration
on startup, a setter started after a waiter can use a different
profile to the waiter, and the two can disagree. The setter can even
use a different configuration file. Additionally, the user can change
the contents of the configuration file while the waiter is running, and
the waiter will not see those changes until it is restarted.

Although restarting the waiter after the configuration file is changed
might be acceptable, the waiter and setter disagreeing on the
configuration is not. When a setter is run, the waiter must change its
current profile to match.

There are numerous ways of doing this, and the method chosen here is
for the setter to notify the waiter over gRPC. With the size of the
dependencies this feels a little like hitting a tack with a
sledgehammer, but the actual code is straightforward and consists
mostly of boilerplate. One of the reasons to use gRPC is just that I'm
already familiar with it, and though I'm no expert, I've more experience
than with e.g. Cap'n Proto. I considered trying ZeroMQ, but again I
have no experience with it and message serialization would still have
to be dealt with. Its main attraction was using IPC rather than a
networking protocol, because that's really all this needs, but that
isn't currently supported on Windows. Using shared memory directly
with something like Boost.Interprocess would probably be better for the
user, but the synchronization and actual implementation would be much
more complicated. I think an IPC approach is worth pursuing, just not
right now.

The `tools/build_protos.sh` script (run in WSL) should be used, with
appropriate modification, to regenerate the Protobuf implementation
files whenever the Protobufs are changed. While in theory the
implementation could be generated by CMake, I prefer to have Protobuf
files checked into source control anyway, and honestly I just don't want
to write that build system code right now.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[34388cbe39...](https://github.com/re621/dnpcache/commit/34388cbe393b994a28b1dd7c61711b9cbc7010ea)
#### Sunday 2022-11-27 20:29:23 by bitWolfy

Remove 984 artists from the DNP list.

Removed: akytti, vahldem_sol, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, cudacore, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, devildjmachine, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [C-EO/terminal](https://github.com/C-EO/terminal)@[f7b0f7444a...](https://github.com/C-EO/terminal/commit/f7b0f7444a101420665de1cf5400d02408226666)
#### Sunday 2022-11-27 21:25:43 by Mike Griese

Spec for Elevation QOL improvements (#8455)

### ⇒ [doc link](https://github.com/microsoft/terminal/blob/dev/migrie/s/1032-elevation-qol/doc/specs/%235000%20-%20Process%20Model%202.0/%231032%20-%20Elevation%20Quality%20of%20Life%20Improvements.md) ⇐


## Summary of the Pull Request

Despite my best efforts to mix elevation levels in a single Terminal window, it seems that there's no way to do that safely. With the dream of mixed elevation dead, this spec outlines a number of quality-of-life improvements we can make to the Terminal today. These should make using the terminal in elevated scenarios better, since we can't have M/E.

### Abstract

> For a long time, we've been researching adding support to the Windows Terminal
> for running both unelevated and elevated (admin) tabs side-by-side, in the same
> window. However, after much research, we've determined that there isn't a safe
> way to do this without opening the Terminal up as a potential
> escalation-of-privilege vector.
> 
> Instead, we'll be adding a number of features to the Terminal to improve the
> user experience of working in elevated scenarios. These improvements include:
> 
> * A visible indicator that the Terminal window is elevated ([#1939])
> * Configuring the Terminal to always run elevated ([#632])
> * Configuring a specific profile to always open elevated ([#632])
> * Allowing new tabs, panes to be opened elevated directly from an unelevated
>   window
> * Dynamic profile appearance that changes depending on if the Terminal is
>   elevated or not. ([#1939], [#8311])


## PR Checklist
* [x] Specs: #1032, #632
* [x] References: #5000, #4472, #2227, #7240, #8135, #8311
* [x] I work here

## Detailed Description of the Pull Request / Additional comments
_\*<sup>\*</sup><sub>\*</sub> read the spec  <sub>\*</sub><sup>\*</sup>\*_

### Why are these two separate documents?

I felt that the spec that is currently in review in #7240 and this doc should remain separate, yet closely related documents. #7240 is more about showing how this large set of problems discussed in #5000 can all be solved technically, and how those solutions can be used together. It establishes that none of the proposed solutions for components of #5000 will preclude the possibility of other components being solved. What it does _not_ do however is drill too deeply on the user experience that will be built on top of those architectural changes. 

This doc on the other hand focuses more closely on a pair of scenarios, and establishes how those scenarios will work technically, and how they'll be exposed to the user.

---
## [MateuzinhoX02/FNF-Android-Preps](https://github.com/MateuzinhoX02/FNF-Android-Preps)@[949883056e...](https://github.com/MateuzinhoX02/FNF-Android-Preps/commit/949883056e8d24409da894d637146600ab346769)
#### Sunday 2022-11-27 21:48:09 by Mateus Soares

Oh my god! Its Boyfriend from Friday Night Funkin'

Sorry, i dont speak English.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[b77cf7c120...](https://github.com/lessthnthree/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Sunday 2022-11-27 22:01:13 by Iamgoofball

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios. (#71325)


About The Pull Request

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
Why It's Good For The Game

Players have been deploying unbelievable levels of abuse with these hotkeys having completely uncapped speeds.
I watched one cheater do automated inventory management using storage items and weirdly named empty pills to use as inventory delimiters.
Resolves people being able to have a baton hidden in their backpack and then activate and baton someone with it in 0.1 seconds without moving their mouse cursor off of their target.

Players should not be able to interact with their inventory faster than someone moving a mouse and clicking the left mouse button. This cripples the game balance and puts anyone with a worse internet connection, slower reaction speeds, or laggier computer at a distinct disadvantage against people who can macro their inventory management.

I can set up autohotkey so that I can withdraw a stun baton from my backpack, turn it on, and then click someone by just holding down a key and pressing M1 over someone. This shit needs to stop.

If a do_after() on hotkey management is too harsh, we can apply a combat click cooldown every time you use the hotkeys instead to discourage combat macro abuse.
Swapped it over to a click cooldown.
Changelog

cl
balance: Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
/cl

---
## [tonyvitonis/git](https://github.com/tonyvitonis/git)@[f1c903debd...](https://github.com/tonyvitonis/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Sunday 2022-11-27 23:29:03 by Ævar Arnfjörð Bjarmason

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

