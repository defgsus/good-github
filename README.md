## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-17](docs/good-messages/2022/2022-12-17.md)


1,753,643 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,753,643 were push events containing 2,390,238 commit messages that amount to 146,457,249 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [Misttyy/cmss13](https://github.com/Misttyy/cmss13)@[70bcd3b6fb...](https://github.com/Misttyy/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Saturday 2022-12-17 01:47:37 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [outsidepro-arts/Properties_Ribbon](https://github.com/outsidepro-arts/Properties_Ribbon)@[5f52b47f14...](https://github.com/outsidepro-arts/Properties_Ribbon/commit/5f52b47f1447da4e1c19f237b3e393895cd28ea9)
#### Saturday 2022-12-17 04:47:38 by Denis A. Shishkin

Execute Properties Ribbon on reaper.defer to prevent an useless undo points creation.

Now we and no one else decide which undo point should be created. No more one undo points like "ReaScript: Run"! Finally!
Yeah, it is hack, but all do the same. REAPER forum has sspecified thread (https://forum.cockos.com/showthread.php?t=215672) where is request for API method or something else for implementing this. Maybe after 15 years...

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[e15277108f...](https://github.com/morgoth1145/advent-of-code/commit/e15277108f39ee8ec4559c872b0ec6d00b80c4c9)
#### Saturday 2022-12-17 06:12:52 by Patrick Hogg

2022 Day 17 Part 2

Ah, and part 2 is giving us a stupid number of rocks to fall. This was clearly a jumpahead problem, and my initial trepidation was that the way to track repeat states would require somehow keeping a record of the shape of the top of the tower which sounds super nasty!

Anyway, I first started by just tracking the current rock and position in the jet stream. So long as those match there's a chance that we're in a cycle. That didn't match the example though, so I think I next kept a list of seen heights to keep track of the height diffs. This way we can let the tower settle into a rhythm before doing the jumpahead. Unfortunately I still didn't get the right answer for the example, it was off by 1! So I then added one and submitted thinking "Why not?" Unsurprisingly, it was off.

I then tried a bunch of things, including trying to get a handle on the tower shape (just by keeping track of how far down the top item is in each column from the top of the tower) but nothing worked! The reason? For any jumpahead you need to make sure to run any "spare" cycles after the jumpahead and I was continuing from the same rock instead of the next one!

After many bad answers (and even a 5 minute timeout) I finally got the right answer 15 minutes and 47 seconds after my first bad answer.

I fell all they way to 295! Oof! Well, at least I got one leaderboard today. Though if I didn't have that off by one error I would have been on the leaderboard for part 2 as well...

---
## [tocchan/aoc-cs](https://github.com/tocchan/aoc-cs)@[c1025957d2...](https://github.com/tocchan/aoc-cs/commit/c1025957d2212c29f9bfa7862b717ee9e37e756f)
#### Saturday 2022-12-17 07:01:27 by Christopher Forseth

I solved part 2.  But you'll notice my part2 is empty... because I soled that shit on paper.  Part 1 has some "extra" code in it to spit out information to help me figure something out.  But I don't know why the patterns emerge, just that they do and that I could use them to solve this stupid thing.

---
## [Tunzeki/algorithms](https://github.com/Tunzeki/algorithms)@[d172f02d6a...](https://github.com/Tunzeki/algorithms/commit/d172f02d6a59060e9435d6260567e9a12cd4b5ca)
#### Saturday 2022-12-17 07:04:40 by Tunzeki

Solve HackerRank 'Strong Password' Challenge

Louise joined a social networking site to stay in touch with her friends
The signup page required her to input a name and a password.
However, the password must be strong.
The website considers a password to be strong if it satisfies the following criteria:
- Its length is at least 6.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character.
    The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field
but wasn't sure if it was strong.
Given the string she typed, can you find the minimum number of
characters she must add to make her password strong?

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[a9fda932e2...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Saturday 2022-12-17 07:06:19 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[b476bce004...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/b476bce004f741ccd2fd69526292b5cd1fa4d4c9)
#### Saturday 2022-12-17 07:12:01 by SkyratBot

[MIRROR] Fishing-themed Escape Shuttle [MDB IGNORE] (#18113)

* Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

* Fishing-themed Escape Shuttle

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [novalance5/-Burj-Khalifa-Russian-Escort-](https://github.com/novalance5/-Burj-Khalifa-Russian-Escort-)@[6f53501e77...](https://github.com/novalance5/-Burj-Khalifa-Russian-Escort-/commit/6f53501e7746d17dddac7b47eebc8d112a36c1dc)
#### Saturday 2022-12-17 07:29:02 by novalance5

Update README.md

 They have their own chauffeurs who bring the call girls in less time in any area of Dubai like Al Barsha, JLT or JBR or even Dubai Investment Park DIP too. I am writing here all after enduring your services in all situations. So confidently they will continue to perform the same way and will make more clients like me. These guys are the best example of working with supremacy. Happy with the Dubai Call Girls Numbers and highly recommended to everyone. Hey Tuson Thank You we are feeling great to hear about our Call Girls  In dubai Service. We are Currently offering the service in Al areas Of dubai Like Al satwa dubai, Jbr, JLt, Al awir, Sports City, JVC, Al Barsha, Jebel Ali, Jumeirah, Marina, Bur Dubai, Deira Dubai, al nahda dubai, al qusais , Al rigga , Dubai Murqabaat , Burjuman as well.Rent A Girlfriend Dubai, My participation was excellent with them, this is the only approved escort service in Dubai with tested call girls. I am using their services for the last 9 months and they have never deceived me in any way. They have their own chauffeurs who bring the call girls in less time in any area of Dubai like Al Barsha, JLT or JBR or even Dubai Investment Park DIP too. I am writing here all after enduring your services in all situations. So confidently they will continue to perform the same way and will make more clients like me.

---
## [LineageOS/android_kernel_google_wahoo](https://github.com/LineageOS/android_kernel_google_wahoo)@[a6dfa182c4...](https://github.com/LineageOS/android_kernel_google_wahoo/commit/a6dfa182c46574024870f8275d54ec546f6b0d6e)
#### Saturday 2022-12-17 07:29:34 by Christian Brauner

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
## [zlhuster/guava](https://github.com/zlhuster/guava)@[8a676ade61...](https://github.com/zlhuster/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Saturday 2022-12-17 08:16:35 by cpovirk

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
## [KonstantinCodes/symfony](https://github.com/KonstantinCodes/symfony)@[338daf25c9...](https://github.com/KonstantinCodes/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Saturday 2022-12-17 08:39:15 by Nicolas Grekas

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
## [systemic-chaos/currently-fronting](https://github.com/systemic-chaos/currently-fronting)@[c38543b586...](https://github.com/systemic-chaos/currently-fronting/commit/c38543b58676931276f3ca2ab876e9fcb84e07a5)
#### Saturday 2022-12-17 09:09:26 by Arcana

Switch to a subset of ts-standard from Prettier

We've long valued Prettier's configurability and convenience,
but we were somehow unaware
of the maintainer's aggressive and
demeaning stance toward
devs who actually want their code
to look beautiful to *them*.
They now refuse to ever implement
new configuration options
and have expressed remorese over
adding them in the first place.

Given our sensory differences,
we find that semicolons
make code harder to read.
So we have always disabled semicolons
when using Prettier, in contradiction
of the default for TypeScript
(according to them).

ts-standard (and StandardJS), by contrast, have defaults that are *much*
more in line with our idea of
aesthetically pleasing code...
And Standard is deliberately implemented
as an ESLint shared config,
which means rules can be overridden
with ease by design.

And that's just it, at the end of the day:
The features of Prettier were ultimately
purely cosmetic. And if the code is not aesthetically
pleasing ---- hell, if it's bloody unreadable ---- to its own devs,
what good is a style guide?

TL;DR Style guides are great.
Attempting to force devs to follow them in contradiction of their
own sense of aesthetics is awful.

---
## [iqba78/android_kernel_xiaomi_sdm660_southwest](https://github.com/iqba78/android_kernel_xiaomi_sdm660_southwest)@[316d312ffd...](https://github.com/iqba78/android_kernel_xiaomi_sdm660_southwest/commit/316d312ffd3820e06cdd54c51d0ed094489d4dbb)
#### Saturday 2022-12-17 09:33:15 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[eabde6dbf3...](https://github.com/mrakgr/The-Spiral-Language/commit/eabde6dbf3b8fd57acb4f5c7aa36d32e0bde0820)
#### Saturday 2022-12-17 09:43:07 by Marko Grdinić

9:15am. I am up.

9:20am. I've been thinking a lot about the backend. I see I didn't get an answer on which outer backend to use.

Anyway.

Views are at 4,998. Avg at 122.

That shit review is still taking my rating, the report did nothing. The latest chapters have experience as sharp drop in readership. My future is pitch black. And I might just be getting scammed in doing free work for UPMEM.

9:35am. Maybe 30 followers is my limit. They seem to be hard to get.

Anyway, let me just read Fabiniku and that TS High School chapter and then I will watch the PIM course video related to UPMEM. Yesterday I had time to look at the docs and get familiar with its programming model. Since this is not the kind of device that I'd be interested in programming personally - I really want small communicating cores so I can do AI instead, I'll do it slowly. I do not feel like just dropping everything to satisfy that guy's whims. Who knows if the job opening in the future will even be remote or if what I will do here will impress him.

The main challenges will be to make the Python + ref countless C backend and then to make the UPMEM functions callable. I have to do a bunch of things to deal with global variables and the like.

Spiral is not a good fit for UPMEM devices because you can't actually free the memory you allocate in its programs. So ref counting is useless due to that.

9:55am. https://www.youtube.com/playlist?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM (Processing-In-Memory) Course

Let me get started with this. I'll slowly get a grip on the PIM programming model.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 3: Real-world PIM: UPMEM PIM - Fall 2022

Let me start with this and then I will watch the lecture on programming these things.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
> A buddy allocator uses a pre-allocated area in the heap to perform dynamic allocation and freeing of buffers, offering functions similar to standard malloc and free.

Actually, I could use this for just things like closures and union types.

///

Allocate buffers, using buddy_alloc, with the following restrictions:
* Allocated buffer size should not exceed 4096 bytes
* Minimum size of allocated buffers is 32 bytes
* Allocated buffers are automatically aligned on DMA-transfer size, so that they can be used to transfer data from/to MRAM

///

I've been too fast to discount them. I mean, this amount would be more than enough for any kind of closure or union type.

Yeah, I am getting bearish and pessimistic far too easily. I should be able to make good things happen with the buddy allocator.

I do not need to get rid of the ref counting from the UPMEM C backend.

That should make it a lot more valuable. Yeah, this is what happens when you make decisions far too quickly. You end up with delusions. The buddy allocator is great. 4k is a huge max limit that I can expect to never reach in realistic scenarios.

Though, I am not sure what to do about allocating arrays.

...Well, I'll just limit them to 4k then. It doesn't matter, this is just a demo. If more is needed the devs can hash it out. The user can use the regular allocator if he really needs a ton of WRAM.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=275

Let me get back to watching this.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=680

64kb WRAM...Yeah, it makes no sense to go beyond 4k if the total memory size is only 64kb.

10:30am. After I am done with these videos, I will check out the Safari benchmark code. I want to see how they do it.

11am. https://youtu.be/7c6x5GJG6dw?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 4: Real-world PIM: Microbenchmarking of UPMEM PIM - Fall 2022

I'll watch this and the programming lecture, and then I am done for the day.

Right now I am thinking how I should handle the `with` statement in Python. It is so annoying, but I might have to extend the language. I'll think I'll just skip it. The `with` statement can ensure that the resources are freed on error, but it does not matter for the demo. I'll just skip it. The del insertion can ensure the resources are freed.

11:35am. https://www.quantamagazine.org/how-the-brain-distinguishes-memories-from-perceptions-20221214/

I'll read this later. Focus me.

11:50am. https://github.com/upmem/dpu_demo/blob/sdk-2021.3/checksum/host/host.py#L64

I am looking at some example code here.

One thing I do not understand is whether MRAM has to be statically declared in the code ahead of time. I'll delay asking the lead compiler dev about it until I watch the lectures.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 9: Programming PIM Architectures - Fall 2022

Let me finally watch this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=196

They can bee seen as a loosely coupled accelerator.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=485

As I gleamed so far, the library actually allocates DPUs themselves instead of blocks of memory.

12:20pm. https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=752

Here it explains the transfers. This is a good tutorial.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=777

Ah, I see. This is how dynamic allocation could work. It is quite rough.

...Still, does this have any alignment requirements?

https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html#communication-with-host-applications

///

dpu_copy_from(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, void *dst, size_t length) to copy a buffer from a single DPU
dpu_broadcast_to(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, const void *src, size_t length, dpu_xfer_flags_t flags) to broadcast a buffer to a set of DPUs
dpu_push_xfer(struct dpu_set_t set, dpu_xfer_t xfer, const char *symbol_name, uint32_t symbol_offset, size_t length, dpu_xfer_flags_t flags) to push different buffers to a set of DPUs in one transfer.

///

Oh they literally have symbol names here.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1189

Let me backtrack just a bit.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=793

https://sdk.upmem.com/2021.4.0/202_RTL.html#buddy-alloc

> The allocated buffer is aligned on 64 bits, in order to ensure compatibility with the maximum buffer alignment constraint. As a consequence, a buffer allocated with this function is also compatible with data transfers to/from MRAM.

> Due to the idea of the buddy algorithm (to decrease external fragmentation), the allocated blocks will be of size equal to a power of 2. In other words, if the user allocates 33 bytes, 64 bytes will be allocated and when 2049 bytes are requested, 4096 will be allocated. The user might want to take this into account if she/he wishes to minimise the memory consumption.

> The minimal size of the allocated block is 16 bytes, but can easily be changed in future implementations, so buddy_alloc is mostly adapted to allocating medium and big structures, such as arrays containing more than 8 bytes (in order to make sure that not too much memory space is wasted), binary trees or linked lists.

The minimum here is different from what the other parts of the doc say.

https://sdk.upmem.com/2021.4.0/CAPILowLevel/dpu__memory_8h.html#a66e9ccbcd5ec3f7767441a0926f24538

Here is copy_to_mram. It is different from in the slides.

The docs are somewhat incomplete.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
The source or target address in MRAM must be aligned on 8 bytes. Developers must carefully respect this rule since the Runtime Library does not perform any check regarding this point.

When doing transfers I need to make sure MRAM pointers are aligned as well. This could result in difficulties if I am just pushing offets around.

12:50pm. Let me stop here. I keep jumping back and forth, thinking about my ideas.

I am going to open an issue somewhere, asking thme about variable length arrays. So far all the examples only have statically allocated ones.

Let me do the chores here.

1:40pm. Breakfast first.

2:05pm. Akiba Maid War. In this ep it seems Ranko dies.

3:30pm. Damn, she is really gone.

Let me finish watching the lecture and then I will post a question on UPMEM repo, one of them, as to how variables be passed into the kernel.

Focus me. Let me get this out of the way today. While I wait for the question tomorrow, I'll continue to write.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1357

These transfers are pretty slow.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1485

I am not sure what is meant by this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1715
> How To Pass Parameters To The Kernel

Yes, this is exactly what I wanted to know! How?

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1758

This explains the host.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1806

I am finally at the level where I can look at this and understand it. Holy shit is this complex.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1807

I am just looking at this and thinking. I am going to have to take a look at the vector addition code to see whether they are viable length or not.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1768

What is this, `dpu_arguments_t`? I'll find that out later.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2616

I need to check these examples out.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2737

Here is the link.

https://youtu.be/H_xvB_O-bWM?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 10: Benchmarking and Workload Suitability on PIM - Fall 2022

This one I'll skip.

https://github.com/CMU-SAFARI/prim-benchmarks

Let me check out vector addition.

https://github.com/CMU-SAFARI/prim-benchmarks/tree/main/VA

https://github.com/CMU-SAFARI/prim-benchmarks/blob/main/VA/support/common.h

///

// Structures used by both the host and the dpu to communicate information
typedef struct {
    uint32_t size;
    uint32_t transfer_size;
	enum kernels {
	    kernel1 = 0,
	    nr_kernels = 1,
	} kernel;
} dpu_arguments_t;

///

So it is like this.

Anyway now that I see this, I can be sure they are using C on the host side.

4:25pm. Now I am lightly cruising the Akiba Maid War thread. Let me just read it for a bit and then I will check out the host side.

4:55pm. __host dpu_arguments_t DPU_INPUT_ARGUMENTS;

I think I could just pass in the array pointer through here.

5:10pm.

///

    uint32_t mram_base_addr_A = (uint32_t)DPU_MRAM_HEAP_POINTER;
    uint32_t mram_base_addr_B = (uint32_t)(DPU_MRAM_HEAP_POINTER + input_size_dpu_bytes_transfer);

///

Wait, now that I think about it, the UPMEM chip should have 8gb. How can the full space then be accessed using 32-bit adresses?

5:15pm. I am think I am starting to grasp the way to pass in the data...

Let me check out the docs again. It is amazing that the most difficult part of UPMEM is how to pass data into it. What the hell were these guys thinking when they designed this?

Now I am starting to see what was meant when I read that AI startups are flailing on the software.

> __mram_ptr which enable to use a pointer on a MRAM variable or declare a extern MRAM variable.

What is an extrern MRAM variable?

> A special MRAM variable is defined in mram.h: DPU_MRAM_HEAP_POINTER. It defines the end of the memory range used by the MRAM variables. The range from DPU_MRAM_HEAP_POINTER to the end of the MRAM can be used freely by a DPU program, for example to handle dynamically-sized MRAM arrays.

This is what I need for dynamic arrays.

> The symbol_name argument consists of a name of a variable in the DPU code. It can be either a MRAM variable (with the __mram or __mram_noinit attribute) or a WRAM variable (with the __host attribute). Other variables are not visible to the host application.

Right. MRAM is __mram and WRAM vars are __host.

I am betting I could have both __host and __mram_ptr together. Something like `__host __mram_ptr int32_t * a;`.

5:45pm. https://github.com/upmem/dpu_demo/issues/
How can UPMEM DPUs access 8gb of memory when they are 32-bit?

Opened issue 13 here.

6:05pm. I am writing some private correspondence. I am not going to post it here, even though it doesn't really matter. I need to stop blabbing about everything in the commits if I am going to be a pro.

6:25pm. Ok, that is basically it.

The C backend should be mostly fine, I can leave it as is. I'll have to make some changes so arrays are handled properly.

Lunch...

7pm. Right now I am thinking how to deal with arrays.

Arrays, arrays...you know what? I should just take them out in the UPMEM Python backend. In the UPMEM C backend, they can be local arrays. That will allow me to easily serialize them. Enough of their horseshit.

I only needed them back in the old Spiral for the sake of typechecking. Now that I have global type inference, they are much less necessary.

I am thinking. What I need to work next is the Python backend. No doubt about it. I'll keep the del insertion from the Cython backend, but otherwise it will be a pure Python backend. PyPy will like what I give it.

I think I might just remove the Cython one altogether as it is such an eyesore.

This kind of refactoring will take some effort, but the Cython backend is simply unacceptable. A decently sized program takes ages to compile and is barely faster than native Python. Though it was useful for testing Spiral v2 back when it came out, that sort of thing is not necessary anymore.

7:10pm. Yeah, I should take this on. A Python backend will end up being useful for other PIM and AI chip devices in the future.

7:20pm. I know that it would be great if I could just dive in and do the UPMEM backend right away, but I should take some care to do the Python backend properly. Then I will extend it.

I'll have to put in the with statement into the language as it is so ubiquitous in Python.

https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/resource-management-the-use-keyword

Or actually, why not make it like this? Rather than immitate Python, why not immitate F#?

7:30pm. Damn, now I have to worry about this. Let's just not worry about it.

I should consider the `use` and `using` statements once the Python backend is done.

Maybe I should give it a break tomorrow, but I should start with a radical cleanup of the Cython backend. For del insertion, I should definitely take a look at how I am doing the analysis in the C backend. I remember it being really confusing in the Cython backend.

I'll have to refresh my memory. So much of the compiler has faded from it.

I do not know whether the UPMEM compiler lead who contacted me will just ghost it after he realizes that interacting with me will be more than 5 minutes of work, I've had plenty of such interaction in the past, but either way I should just do this and use it as a chance to advertize Spiral. Ultimately, my desire to work on novel hardware has not faded.

7:40pm. Now forget that. Let me read KenDeshi. Tomorrow I will do some writing and then slowly start. I should aim to split my time between the two.

I'll go back to blogging on the Spiral repo, I see that doing it on Patreon is doing me no good.

---
## [3llena/project_silja](https://github.com/3llena/project_silja)@[2cb3f97a39...](https://github.com/3llena/project_silja/commit/2cb3f97a3933bf6e369d17af7df20b3090e720e3)
#### Saturday 2022-12-17 10:04:37 by 3llena

some correctness shit
nobody liked syms anyways (its too fucking tedious)
thinking about better version management instead

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[75439c71f2...](https://github.com/tgstation/tgstation/commit/75439c71f2282a3ae72b4ea35c80e27ca8556aaf)
#### Saturday 2022-12-17 10:34:32 by Mothblocks

Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[73db08d523...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/73db08d523d702a917642ecd6e8199f2278c7de9)
#### Saturday 2022-12-17 11:27:33 by AmyBSOD

Nerf the hell out of Elbereth

Holy shit, who on earth made it so that it works on bosses??? Good thing I became aware of that supreme imbalance, so now it doesn't. All minotaur types are also immune now.

---
## [Spc-Dragonfruits/sunset-wasteland](https://github.com/Spc-Dragonfruits/sunset-wasteland)@[f7f7ae2cfc...](https://github.com/Spc-Dragonfruits/sunset-wasteland/commit/f7f7ae2cfc1c91d2df5bfdbd7895e7ab2c6eb4d3)
#### Saturday 2022-12-17 11:39:45 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [fengjixuchui/UACME](https://github.com/fengjixuchui/UACME)@[c65f9215c1...](https://github.com/fengjixuchui/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Saturday 2022-12-17 12:18:52 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [mizz141/PlexAniSync-Mappings](https://github.com/mizz141/PlexAniSync-Mappings)@[4f85fb8b86...](https://github.com/mizz141/PlexAniSync-Mappings/commit/4f85fb8b866c169b3059745e77d9c1afc6824cfa)
#### Saturday 2022-12-17 12:45:37 by Daggersoath

Added series missing when searching with Japanese titles (#66)

* Added series with Japanese titles
Added Japanese titles to synonyms for preexisting series

- I'm standing on a million lives
- Arifureta: From commonplace to World's Strongest
- Bakuman
- Code Geass: Lelouch of the rebellion
- Is it wrong to try to pick up girls in a dungeon?
- How not to summon a demon lord
- Komi can't communicate
- Rent a girlfriend
- My next life as a villainess: All routes lead to doom!
- That time I got reincarnated as a slime
- To Your Eternity
- Welcome to Demon School! Iruma-kun
- Yuri!!! on ICE

* Removed accidental :

* Fixed typo in Yuri on ice season->seasons

* Fixed naming to use english title, japanese as synonym

* Delete stray line

Co-authored-by: Daggersoath <9066690+Daggersoath@users.noreply.github.co>
Co-authored-by: mizz141 <20839616+mizz141@users.noreply.github.com>

---
## [tinysaturn/vgstation13](https://github.com/tinysaturn/vgstation13)@[e6156a8d91...](https://github.com/tinysaturn/vgstation13/commit/e6156a8d91d8a24ebe6437f07198713f76946fc1)
#### Saturday 2022-12-17 13:07:17 by samo priimek

pulse demon tweaks (#33690)

* remove the stupid maxcharge tweak

* sneed

* comment unused stuff

* revert everything

* prevent you from killing yourself stupidly

* suck SMES faster, gain maxcharge when sucking APC's

* remove the capacity upgrade

* tweak the ability costs and upgrades

---
## [Empire-Strikes-Back/Hux](https://github.com/Empire-Strikes-Back/Hux)@[702ac6236f...](https://github.com/Empire-Strikes-Back/Hux/commit/702ac6236f54ce02f66a3b7dcd317877d1f6f397)
#### Saturday 2022-12-17 13:53:43 by Hux

we'll need a pilot! - we've got one!

like Jordan I made a mistake of camps and teaching isntead of continueing to perform

unlike McDougall I don't want to be dead expert in the law

I heard Jesus - about lost sheep, man going to Jericho, weeds, enemies and love, shines on everyone, reborn

let my name be Hux - I am general, but Hux is enough
let my idntity fruit be banana - like red hand mar - blood hand mark on Finn's helmet
let my runtime be jvm, language - clojure - I am no longer proud of being enemy of the garden

:Harrison-Ford J?
:J-J-Abrams J J
:Harrison J J

---
## [RanDoomGuy21/Nostra-13](https://github.com/RanDoomGuy21/Nostra-13)@[8eec99b320...](https://github.com/RanDoomGuy21/Nostra-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Saturday 2022-12-17 13:58:25 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[8f1ee35f1d...](https://github.com/cmss13-devs/cmss13/commit/8f1ee35f1de18e295fa29e4536ad00431e7f0d76)
#### Saturday 2022-12-17 14:09:13 by carlarctg

Refactored weed crossing to utilize signals and list data. (#1960)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Refactored weed slowdown to work based on a signal sent to the recipient
carrying list data.

Added a variable for weed slowdown multiplier to species. Human Heroes
have 0.5 weed slowdown because haha funny. Transferred Yautja's weed
immunity to species.

Added an admin-only example item 'hiking boots' that halve weed
slowdown.

Removed a useless define for XVX.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
refactor: Refactored weed slowdown to work based on a signal sent to the
recipient carrying list data.
code: Added a variable for weed slowdown multiplier to species. Human
Heroes have 0.5 weed slowdown because haha funny. Transferred Yautja's
weed immunity to species.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Franz-Art-L/fswd-airbnb-clone](https://github.com/Franz-Art-L/fswd-airbnb-clone)@[1e8bd7d0ff...](https://github.com/Franz-Art-L/fswd-airbnb-clone/commit/1e8bd7d0ff0f2febdb20102eef1296a5445957c0)
#### Saturday 2022-12-17 14:31:17 by Ishoboy

little changes on the grammar on the bookings component and I dont know about the reservations component maybe just a little space I change im not sure hehe and lastly I found a code on edit property that dont have a use when I check and test without it the function of the component still works, but who knows maybe somewhere soon I will realize that the property object on the state in edit property component was useful, we will see.thanks time to eat dinnerwhat a night, first I decided to add a time 24h picker, but I didn't push through since along the way I was thinking I still cant handle on how to solve the algorithm, because of that I decided to remain this booking app as per day basis but the day is equivalent to one session, but I already put on the add service that the user can still be booked on the same day as long as he is done doing his job it will be the customer will be the one wwho will destroy the booking once the worker is done doing his job, because of that I did remove the 4 new columns that I added last night on my database it was time frame, start time, end time, and availability. Now its back to the original database entry columns. Time to commit this one and tomorrow its either I will add the crypto booking component or the pay in person component. we will see. To be continue. See you tomorrow guys. Good night

---
## [openbsd/src](https://github.com/openbsd/src)@[0cffdb45a9...](https://github.com/openbsd/src/commit/0cffdb45a9bb573ce4665f5540d1a0d50ff2e37f)
#### Saturday 2022-12-17 15:22:36 by tb

acme-client: fix SAN-handling insanity

The revoke process, which does a lot more than revoking a cert, wants to
know the SANs in the cert to be revoked or renewed and check them against
the ones configured in the config file.

To find out which ones are, it prints the SAN extension to a BIO using
X509V3_EXT_print(), slurps that into a buffer, tokenizes the undocumented
output string and plucks out the "DNS:" names. This is reminiscent of
node's hilarious CVE-2021-44532 and on about the same level of crazy, but
fortunately not security relevant.

Get the SAN extension as a GENERAL_NAMES from libcrypto, then we have an
actual data structure to work with, which allows us to access the DNS names
without problems. This simplifies things quite a bit, but the actual logic
in this file remains unmodified. Be careful about ASN1_IA5STRINGs and do
not assume they are C strings.

Tested by florian, millert, Renaud Allard, thanks!

ok florian jsing

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[e766444468...](https://github.com/ss220-space/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Saturday 2022-12-17 15:28:32 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [rezizdigus/Grasscutter](https://github.com/rezizdigus/Grasscutter)@[88bc5c4c54...](https://github.com/rezizdigus/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Saturday 2022-12-17 15:55:43 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [Punuy/Blender-miHoYo-Shaders](https://github.com/Punuy/Blender-miHoYo-Shaders)@[13da0caf88...](https://github.com/Punuy/Blender-miHoYo-Shaders/commit/13da0caf8885a9a149c8816ec5b9b7a69ce1591f)
#### Saturday 2022-12-17 16:27:53 by Festivize

refactor(genshin): rewrite dot creation again?! i hate my life

---
## [damerell/crawl](https://github.com/damerell/crawl)@[a9801cc52e...](https://github.com/damerell/crawl/commit/a9801cc52efa17750a22e8f6510ec0df434585d0)
#### Saturday 2022-12-17 16:33:35 by David Damerell

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
## [Dallinger/Dallinger](https://github.com/Dallinger/Dallinger)@[73e39d94a7...](https://github.com/Dallinger/Dallinger/commit/73e39d94a7ba96a17438f3c5b149a36408838d66)
#### Saturday 2022-12-17 17:26:34 by Peter Harrison

Misc Docker quality of life improvements (#4616)

# Major

- Disabled the behavior where the built image name is written to config.txt. This behavior was inconsistent with the other Dallinger deployment patterns, because it meant that if you deployed once, changed code in experiment.py, then redeployed, then the experiment would launch in the former version unless you remembered to delete the image name from config.txt.
- Heroku deployments were failing because the default `heroku_python_version` had been discontinued by Heroku. We have experienced similar problems in the past and have always had to update Dallinger. Now we have changed the behaviour such that, if `heroku_python_version` is not specified in the experiment config, then it will use the default Python runtime currently in use by Heroku.

# Minor

- Propagate more information from deployment-related functions (e.g. dashboard credentials) so that they can be used by wrapper functions.
- Print more information (e.g. dashboard credentials) in deployment-related functions.
- Better debugging logs for docker-ssh deployments.
- Move deployment info logs from `deployment-info_{experiment_id}.txt` to `deploy_logs/*` to avoid clutter.
- Move default `dallinger_develop_directory` to `/tmp/dallinger_develop` because the original location was not writable by default on Docker.
- Minor bugfixes in docker-ssh deployment/export.
- Rename config variable `docker_ssh_volumes` -> `docker_volumes` because it's relevant also when we're doing docker locally. 
- Some minor renaming of internal variables for consistency.

---
## [jandurovec/adventofcode-in-kotlin](https://github.com/jandurovec/adventofcode-in-kotlin)@[b6299da2e5...](https://github.com/jandurovec/adventofcode-in-kotlin/commit/b6299da2e5c93f68d7c0d9ff314d42b6f20573ad)
#### Saturday 2022-12-17 20:27:09 by Jan Durovec

2022 Day 17

Driving home for Christmas... top to toe in tailbacks...

I've spent 8 hours driving in not really pleasant conditions, as it was
snowing for the last few hours of the journey. I wasn't sure I'd find
power to do the task today, but the Elves really needed me.

The straitforward (though lot of writing) Tetris simulation did the
trick for the first part, but part 2 was too big to simulate.

I've remembered I've encountered similar task before where the game of
life (or some pots in a cavern?) repeated so I decided to write an
algorithm to check for loops. After struggling with how to represent the
state using data classes of `(Int,Int,Set)` I ended up with simple
`String` representing the state as it was fastest to work with.

The loop has been found quite soon (and quite short) and it earned me
the second start (fruit). I'm starting to have a feeling that the
reindeer might have a chance of getting some star fruit full of magical
energy even if it turns out that something has happened to the grove in
the end.

---
## [asm128/gpk](https://github.com/asm128/gpk)@[e7cfca50b3...](https://github.com/asm128/gpk/commit/e7cfca50b310e88dad1322c030bc8a1c5ab92ef8)
#### Saturday 2022-12-17 20:30:58 by rgbvillain

Finally removed that Microsoft::WRL bullshit that prevents using standard types normally.

The fucking lammers who invaded Microsoft should stop sucking dicks and learn to code instead.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[53fc3fb9da...](https://github.com/treckstar/yolo-octo-hipster/commit/53fc3fb9da2118910c14033a3b93a852a2a21f98)
#### Saturday 2022-12-17 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Slyssy/small-business](https://github.com/Slyssy/small-business)@[5638bfda66...](https://github.com/Slyssy/small-business/commit/5638bfda66cd790c92c3c5abfe40418d64189404)
#### Saturday 2022-12-17 22:20:06 by Stephen

Finally got this glitch ass map to fucking work. Mother effer that was a pain in the dick

---

