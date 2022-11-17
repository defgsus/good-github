## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-16](docs/good-messages/2022/2022-11-16.md)


2,224,331 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,224,331 were push events containing 3,317,363 commit messages that amount to 275,552,849 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [vijithassar/bisonica](https://github.com/vijithassar/bisonica)@[5151b4a2f2...](https://github.com/vijithassar/bisonica/commit/5151b4a2f265a2b081f04aec5f5d6b89cc7db1bf)
#### Wednesday 2022-11-16 00:34:38 by Vijith Assar

chore(core): don't use typeof in undefined checks

Removes typeof checks everywhere a conditional checks for an undefined value. This was once a historical best practice because it used to be possible to change the value of undefined, but that's no longer the case in modern browsers. This change also means that an undefined check with a variable that has not been declared will throw a ReferenceError. That used to be sort of scary, but it's more disciplined to allow them – those errors should be early and catastrophic so as to encourage code styles where they are still impossible because they are appropriately guarded against.

In theory, this does make it a bit harder to get inside the conditionals where errors are thrown, which is a bit of a shame – instead of the helpful error message text, you'd get a cryptic ReferenceError, because the ReferenceError blocks the code path into the better error message!

But none of this matters, because the linter should prevent this kind of mistake anyway.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[a5c94a4509...](https://github.com/sjp38/linux/commit/a5c94a45093e06a2f4d1c62df5cf5413e67917e1)
#### Wednesday 2022-11-16 00:38:03 by Johannes Weiner

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
## [Dabger1/tgstation](https://github.com/Dabger1/tgstation)@[25d4afc869...](https://github.com/Dabger1/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Wednesday 2022-11-16 00:44:40 by Iamgoofball

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
## [Mmellet/Blank](https://github.com/Mmellet/Blank)@[45231b5d77...](https://github.com/Mmellet/Blank/commit/45231b5d774153ed43b554b498c7498b108d6e88)
#### Wednesday 2022-11-16 01:31:27 by Margot Mellet

ut he had an approved[4] tolerance for others; sometimes wondering, almost with envy, at the high pressure of spirits involved in their misdeeds; and in any extremity inclined to help rather than to reprove. «I incline to Cain's heresy,» he used to say quaintly: «I let my brother go to the devil in his own way.»[5] In this character, it was frequently his fortune to be the last reputable acquaintance and the last good influence in the lives of downgoing men. And to such as these, so long as they came about his chambers, he never marked a shade of change in his demeanour.

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[a40e080c35...](https://github.com/RedDevilus/pcsx2/commit/a40e080c35e25261903731e4cc3c6f5e1654f2f1)
#### Wednesday 2022-11-16 02:21:09 by RedDevilus

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
## [DanielBainbridge/Hareborne_HDRP](https://github.com/DanielBainbridge/Hareborne_HDRP)@[86392ffe36...](https://github.com/DanielBainbridge/Hareborne_HDRP/commit/86392ffe362855e558448be1094dbe1fd9033924)
#### Wednesday 2022-11-16 03:49:13 by FynnCat

Merge pull request #41 from DanielBainbridge/FynnBranch

A bunch of things, very import, just pull it right now... Why haven't you done it yet? I said now. Bloody hell. This is getting ridiculous, just do it & get back to work.

---
## [newstools/2022-sowetan-live](https://github.com/newstools/2022-sowetan-live)@[5bf5a562b8...](https://github.com/newstools/2022-sowetan-live/commit/5bf5a562b85538cb462b307ec65bd7b042e60629)
#### Wednesday 2022-11-16 04:11:10 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/south-africa/2022-11-15-life-for-man-who-raped-and-murdered-girlfriend-then-dumped-her-body-in-the-street/]

---
## [BRupireddy/postgres](https://github.com/BRupireddy/postgres)@[8272749e8c...](https://github.com/BRupireddy/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Wednesday 2022-11-16 05:43:23 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[de662db397...](https://github.com/tgstation/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Wednesday 2022-11-16 06:02:28 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7b2707ec29...](https://github.com/treckstar/yolo-octo-hipster/commit/7b2707ec29f53a222e03a1444f1c2b969d6b4389)
#### Wednesday 2022-11-16 06:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Sagit-A13/kernel_xiaomi_msm8998](https://github.com/Sagit-A13/kernel_xiaomi_msm8998)@[b08c3b47bd...](https://github.com/Sagit-A13/kernel_xiaomi_msm8998/commit/b08c3b47bd6e831dd02d772602b38cbc2d651d5e)
#### Wednesday 2022-11-16 06:35:37 by Christian Brauner

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
## [Harishwarrior/ytdownload-flutter](https://github.com/Harishwarrior/ytdownload-flutter)@[d69162f7f6...](https://github.com/Harishwarrior/ytdownload-flutter/commit/d69162f7f6f45c48ce6c1383b6125a5f115d230d)
#### Wednesday 2022-11-16 09:04:33 by Romjan D. Hossain

Merge pull request #11 from Binozo/master

Fixed bullshit var names and comments!!! Thanks for renaming my shitty var name, mate! Cheers 🥂

---
## [Claymore1297/kernel_oneplus_sm8150](https://github.com/Claymore1297/kernel_oneplus_sm8150)@[7112098b69...](https://github.com/Claymore1297/kernel_oneplus_sm8150/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Wednesday 2022-11-16 09:26:19 by Jason A. Donenfeld

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
## [mjg/git](https://github.com/mjg/git)@[eb20e63f5a...](https://github.com/mjg/git/commit/eb20e63f5a96e24852c6ab1eca9f96af2648802f)
#### Wednesday 2022-11-16 10:36:06 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged to its upstream (if any), or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29) made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() helper to treat a NULL
as "not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault in can_all_from_reach().

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [guites/tweets](https://github.com/guites/tweets)@[2445b69dcd...](https://github.com/guites/tweets/commit/2445b69dcdecd5ad9c2067b2141f4e9a1e7eaa74)
#### Wednesday 2022-11-16 10:55:38 by guites

@n3wjack re: e2366c88 oh cool man, will try to reproduce that, thanks. funny how a different workflow can fuck a script up

---
## [google/guava](https://github.com/google/guava)@[4227b3dcc8...](https://github.com/google/guava/commit/4227b3dcc8ea90ef0f90da9e6f509c458cb716ae)
#### Wednesday 2022-11-16 11:58:14 by cpovirk

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
PiperOrigin-RevId: 488700624

---
## [sparkspay/sparks](https://github.com/sparkspay/sparks)@[a00da7fb0e...](https://github.com/sparkspay/sparks/commit/a00da7fb0e8380dccd2922c3e12e8c36b1eeff8b)
#### Wednesday 2022-11-16 12:35:22 by Wladimir J. van der Laan

Merge #10271: Use std::thread::hardware_concurrency, instead of Boost, to determine available cores

937bf4335 Use std::thread::hardware_concurrency, instead of Boost, to determine available cores (fanquake)

Pull request description:

  Following discussion on IRC about replacing Boost usage for detecting available system cores, I've opened this to collect some benchmarks + further discussion.

  The current method for detecting available cores was introduced in #6361.

  Recap of the IRC chat:
  ```
  21:14:08 fanquake: Since we seem to be giving Boost removal a good shot for 0.15, does anyone have suggestions for replacing GetNumCores?
  21:14:26 fanquake: There is std::thread::hardware_concurrency(), but that seems to count virtual cores, which I don't think we want.
  21:14:51 BlueMatt: fanquake: I doubt we'll do boost removal for 0.15
  21:14:58 BlueMatt: shit like BOOST_FOREACH, sure
  21:15:07 BlueMatt: but all of boost? doubtful, there are still things we need
  21:16:36 fanquake: Yea sorry, not the whole lot, but we can remove a decent chunk. Just looking into what else needs to be done to replace some of the less involved Boost usage.
  21:16:43 BlueMatt: fair
  21:17:14 wumpus: yes, it makes sense to plan ahead a bit, without immediately doing it
  21:18:12 wumpus: right, don't count virtual cores, that used to be the case but it makes no sense for our usage
  21:19:15 wumpus: it'd create a swarm of threads overwhelming any machine with hyperthreading (+accompanying thread stack overhead), for script validation, and there was no gain at all for that
  21:20:03 sipa: BlueMatt: don't worry, there is no hurry
  21:59:10 morcos: wumpus: i don't think that is correct
  21:59:24 morcos: suppose you have 4 cores (8 virtual cores)
  21:59:24 wumpus: fanquake: indeed seems that std has no equivalent to physical_concurrency, on any standard. That's annoying as it is non-trivial to implement
  21:59:35 morcos: i think running par=8 (if it let you) would be notably faster
  21:59:59 morcos: jeremyrubin and i discussed this at length a while back... i think i commented about it on irc at the time
  22:00:21 wumpus: morcos: I think the conclusion at the time was that it made no difference, but sure would make sense to benchmark
  22:00:39 morcos: perhaps historical testing on the virtual vs actual cores was polluted by concurrency issues that have now improved
  22:00:47 wumpus: I think there are not more ALUs, so there is not really a point in having more threads
  22:01:40 wumpus: hyperthreads are basically just a stored register state right?
  22:02:23 sipa: wumpus: yes but it helps the scheduler
  22:02:27 wumpus: in which case the only speedup using "number of cores" threads would give you is, possibly, excluding other software from running on the cores on the same time
  22:02:37 morcos: well this is where i get out of my depth
  22:02:50 sipa: if one of the threads is waiting on a read from ram, the other can use the arithmetic unit for example
  22:02:54 morcos: wumpus: i'm pretty sure though that the speed up is considerably more than what you might expect from that
  22:02:59 wumpus: sipa: ok, I back down, I didn't want to argue this at all
  22:03:35 morcos: the reason i haven't tested it myself, is the machine i usually use has 16 cores... so not easy due to remaining concurrency issues to get much more speedup
  22:03:36 wumpus: I'm fine with restoring it to number of virtual threads if that's faster
  22:03:54 morcos: we should have somene with 4 cores (and ￼ actually test it though, i agree
  22:03:58 sipa: i would expect (but we should benchmark...) that if 8 scriot validation threads instead of 4 on a quadcore hyperthreading is not faster, it's due to lock contention
  22:04:20 morcos: sipa: yeah thats my point, i think lock contention isn't that bad with 8 now
  22:04:22 wumpus: on 64-bit systems the additional thread overhead wouldn't be important at least
  22:04:23 gmaxwell: I previously benchmarked, a long time ago, it was faster.
  22:04:33 gmaxwell: (to use the HT core count)
  22:04:44 wumpus: why was this changed at all then?
  22:04:47 wumpus: I'm confused
  22:05:04 sipa: good question!
  22:05:06 gmaxwell: I had no idea we changed it.
  22:05:25 wumpus: sigh ￼
  22:05:54 gmaxwell: What PR changed it?
  22:06:51 gmaxwell: In any case, on 32-bit it's probably a good tradeoff... the extra ram overhead is worth avoiding.
  22:07:22 wumpus: https://github.com/bitcoin/bitcoin/pull/6361
  22:07:28 gmaxwell: PR 6461 btw.
  22:07:37 gmaxwell: er lol at least you got it right.
  22:07:45 wumpus: the complaint was that systems became unsuably slow when using that many thread
  22:07:51 wumpus: so at least I got one thing right, woohoo
  22:07:55 sipa: seems i even acked it!
  22:07:57 BlueMatt: wumpus: there are more alus
  22:08:38 BlueMatt: but we need to improve lock contention first
  22:08:40 morcos: anywya, i think in the past the lock contention made 8 threads regardless of cores a bit dicey.. now that is much better (although more still to be done)
  22:09:01 BlueMatt: or we can just merge #10192, thats fee
  22:09:04 gribble: https://github.com/bitcoin/bitcoin/issues/10192 | Cache full script execution results in addition to signatures by TheBlueMatt · Pull Request #10192 · bitcoin/bitcoin · GitHub
  22:09:11 BlueMatt: s/fee/free/
  22:09:21 morcos: no, we do not need to improve lock contention first.   but we should probably do that before we increase the max beyond 16
  22:09:26 BlueMatt: then we can toss concurrency issues out the window and get more speedup anyway
  22:09:35 gmaxwell: wumpus: yea, well in QT I thought we also diminished the count by 1 or something?  but yes, if the motivation was to reduce how heavily the machine was used, thats fair.
  22:09:56 sipa: the benefit of using HT cores is certainly not a factor 2
  22:09:58 wumpus: gmaxwell: for the default I think this makes a lot of sense, yes
  22:10:10 gmaxwell: morcos: right now on my 24/28 physical core hosts going beyond 16 still reduces performance.
  22:10:11 wumpus: gmaxwell: do we also restrict the maximum par using this? that'd make less sense
  22:10:51 wumpus: if someone *wants* to use the virtual cores they should be able to by setting -par=
  22:10:51 sipa: *flies to US*
  22:10:52 BlueMatt: sipa: sure, but the shared cache helps us get more out of it than some others, as morcos points out
  22:11:30 BlueMatt: (because it means our thread contention issues are less)
  22:12:05 morcos: gmaxwell: yeah i've been bogged down in fee estimation as well (and the rest of life) for a while now.. otherwise i would have put more effort into jeremy's checkqueue
  22:12:36 BlueMatt: morcos: heh, well now you can do other stuff while the rest of us get bogged down in understanding fee estimation enough to review it ￼
  22:12:37 wumpus: [to answer my own question: no, the limit for par is MAX_SCRIPTCHECK_THREADS, or 16]
  22:12:54 morcos: but to me optimizing for more than 16 cores is pretty valuable as miners could use beefy machines and be less concerned by block validation time
  22:14:38 BlueMatt: morcos: i think you may be surprised by the number of mining pools that are on VPSes that do not have 16 cores ￼
  22:15:34 gmaxwell: I assume right now most of the time block validation is bogged in the parts that are not as concurrent. simple because caching makes the concurrent parts so fast. (and soon to hopefully increase with bluematt's patch)
  22:17:55 gmaxwell: improving sha2 speed, or transaction malloc overhead are probably bigger wins now for connection at the tip than parallelism beyond 16 (though I'd like that too).
  22:18:21 BlueMatt: sha2 speed is big
  22:18:27 morcos: yeah lots of things to do actually...
  22:18:57 gmaxwell: BlueMatt: might be a tiny bit less big if we didn't hash the block header 8 times for every block. ￼
  22:21:27 BlueMatt: ehh, probably, but I'm less rushed there
  22:21:43 BlueMatt: my new cache thing is about to add a bunch of hashing
  22:21:50 BlueMatt: 1 sha round per tx
  22:22:25 BlueMatt: and sigcache is obviously a ton
  ```

Tree-SHA512: a594430e2a77d8cc741ea8c664a2867b1e1693e5050a4bbc8511e8d66a2bffe241a9965f6dff1e7fbb99f21dd1fdeb95b826365da8bd8f9fab2d0ffd80d5059c

---
## [Reaperv115/TheRhine](https://github.com/Reaperv115/TheRhine)@[af210fe376...](https://github.com/Reaperv115/TheRhine/commit/af210fe37640d15a5c716088a9b40ffad59bf17b)
#### Wednesday 2022-11-16 13:39:29 by rjs5785

fixed rendering the triangle... stupid shit. also fixed moving the camera. so yeah

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[416d642988...](https://github.com/rust-lang-ci/rust/commit/416d6429884dc8f1e8d7134df30aef7184fb0fab)
#### Wednesday 2022-11-16 14:09:21 by Devin Jeanpierre

Add the `#[manually_drop]` attribute.

This attribute is equivalent to `#[lang = "manually_drop"]`, and the behavior of both are
extended to allow the type to define `Drop`, in which case, that will still be run. Only
the field drop glue is suppressed.

This PR should essentially fully implement #100344.

Some additional notes:

`#[manually_drop]` means "do not destroy the fields automatically during
destruction". `ManuallyDrop`, is (or could be) "just"
`#[manually_drop] struct ManuallyDrop<T>(T);`.

The intent is, per the MCP, to allow customization of the drop order, without making the
interface for initializing or accessing the fields of the struct clumsier than a normal
Rust type. It also -- and people did seem excited about this part -- lifts `ManuallyDrop`
from being a special language supported feature to just another user of
`#[manually_drop]`.

There is the question of how this interacts with "insignificant" drop. I had trouble
understanding the comments, but insignificant drop appears to just be a static analysis
tool, and not something that changes behavior. (For example, it's used to detect if a
language change will reorder drops in a meaningful way -- meaning, reorder the
significant drops, not the insignificant ones.) Since it's unlikely to be used for
`#[manually_drop]` types, I don't think it matters a whole lot. And where a destructor
is defined, it would seem to make sense for `#[manually_drop]` types to match exactly
the behavior of `union`, since they both have the shared property that field drop
glue is suppressed.

I looked for all locations that queried for `is_manually_drop` in any form, and found two
difficult cases which are hardcoded for `ManuallyDrop` in particular.

The first is a clippy lint for redundant clones. I don't understand why it special-cases
`ManuallyDrop`, and it's almost certainly wrong for it to special-case `#[manually_drop]`
types in general. However, without understanding the original rationale, I have trouble
figuring the right fix. Perhaps it should simply be deleted altogether.

The second is unions -- specifically, the logic for disabling `DerefMut`.
`my_union.x.y = z` will automatically dereference `my_union.x` if it implements
`DerefMut`, unless it is `ManuallyDrop`, in which case it will not. This is because
`ManuallyDrop` is a pointer back to its content, and so this will automatically call `drop`
on a probably uninitialized field, and is unsafe.

This is true of `ManuallyDrop`, but not necessarily any other `#[manually_drop]` type.
I believe the correct fix would, instead, be a way to mark and detect types which are
a smart pointer whose pointee is within `self`. See, for example, this playground link:

https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=76fb22a6214ce453538fc18ec35a839d

But that needs to wait for a separate RFC. For now, we apply exactly the same restriction
for `ManuallyDrop` and for any other `#[manually_drop]` type, even though it may be
confusing.

1.  Delete `#[lang = "manually_drop"]`. I'm not sure if anything special needs to be done
    here other than replacing it with `#[manually_drop]` -- is there a compatibility
    guarantee that must be upheld?
2.  (Optional) Fix the redundant clone check to correctly handle `#[manually_drop]`
    structs that aren't `ManuallyDrop`.
3.  When there is more experience with the feature (e.g. in Crubit) create a full RFC
    based on the MCP, and go through the remainder of the stabilization process.
    (Also, do things like generalize the union error messages to not specifically
    mention `ManuallyDrop`, but also mention `#[manually_drop]`. For as long as the
    feature is unstable, the error messages would be confusing if they referenced
    it...)

---
## [supyrow/kate](https://github.com/supyrow/kate)@[cbee1809e7...](https://github.com/supyrow/kate/commit/cbee1809e701ee975a35b9b43b87ba97a0938f4b)
#### Wednesday 2022-11-16 14:20:25 by Waqar Ahmed

lsp: enable snippet support

This change announces to the servers that we support snippets, even though
in reality we don't. However, we can still work with snippet-y text by
removing the snippet markers and using that with our own snippet handler
which is not quite ready to accept lsp style snippets.

The benefit of this change is that we don't have to put in hacks to add
"()" parens to stuff. We also don't have to move our cursor manually which
can be incorrect in many cases e.g., string.isEmpty(), with cursor in
between the parens doesn't make sense.

For cpp/clangd the existing logic was okay-ish. However some servers like
dart-analyzer do something different. If you dont have snippets, the
server will just remove the snippet markers from the text and send it to
you. This results in sometimes very annoying editing experience. For e.g.,

- maxLines: ,| // cursor position at the end is annoying
- initState() {
  // some comment
  }() // () what are parens doing here??

Thus its better to just remove those markers ourselves and then we can
just set the cursor position as we want and don't have to manually
decide anything.

---
## [Shopify/sorbet](https://github.com/Shopify/sorbet)@[3cb2b4b1c8...](https://github.com/Shopify/sorbet/commit/3cb2b4b1c868b15f8b572a63099b87720d581018)
#### Wednesday 2022-11-16 14:25:38 by Jake Zimmerman

Remove call to `dealias` in namer (#6519)

* Remove call to `dealias` in namer

We don't allow constant aliases in class scopes anyways. Not sure why
we're trying to dealias here.

If I had to guess, this was a remant of some hacks we had way long ago
to support this pattern, which was common in Stripe's codebase:

    class Chalk::ODM::Model
    end

    M = Chalk::ODM::Model

    class M::A
    end

But this pattern is already rejected by Sorbet, and has been for as long
as I can remember, so likely when that change was finally made, someone
forgot to delete this `dealias` call.

* Remove unused `ctx` parameter

---
## [Cykeek-Labs/kernel_realme_sdm710](https://github.com/Cykeek-Labs/kernel_realme_sdm710)@[df35e740cb...](https://github.com/Cykeek-Labs/kernel_realme_sdm710/commit/df35e740cb16146f83fed3602650974168ddffb5)
#### Wednesday 2022-11-16 14:37:16 by George Spelvin

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
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [physycom/Catch](https://github.com/physycom/Catch)@[22750cde0e...](https://github.com/physycom/Catch/commit/22750cde0e0d2c02ab447e2500422f2711356053)
#### Wednesday 2022-11-16 15:01:49 by Anders Schau Knatten

Disable false positive from clang-tidy

Clang-tidy is smart enough to understand that the conditional is never
updated in the loop body. It will let you get away with it if it can
prove that the conditional is always false, but that is not always
possible.

Here is an example where it's not able to prove it, and thus gives a
false positive. This is a minimal reproduction of an actual case I hit
in production, where `function` is picking the function based on some
`constexpr` logic related to which type argument is currently being
tested.

```
int f();

TEMPLATE_TEST_CASE("reproduction", "", int) {
    const auto function = []() {
        return f;
    }();
    const int error = function();
    REQUIRE(error == 0); // clang-tidy complains: bugprone-infinite-loop
}
```

I did not choose to add this test to the test suite, since we're not
running `clang-tidy` in CI afaik. To run it manually, simply add the
snippet above somewhere and run clang-tidy with
`--checks=bugprone-infinite-loop`. Or see an example at
https://godbolt.org/z/4v8b8WexP.

The reason we get the infinite loop warning in the first place is the
conditional at the end of this `do`-loop. Ideally, this conditional
would just be `while(false)`, but the actual content of the
`REQUIRE`-statement has been included here too in order to not loose
warnings from signed/unsigned comparisons. In short, if you do
`REQUIRE(i < j)`, where `i` is a negative signed integer and `j` is an
unsigned integer, you're supposed to get a warning from
`-Wsign-compare`. Due to the decomposition in Catch2, you lose this
warning, which is why the content of the `REQUIRE` statement has been
added to the conditional to force the compiler to evaluate the actual
comparison as well.

This was discussed on Discord today, and an alternative approach (which
I don't have time to implement) would be to in the decomposition replace
the comparison operators with `cmp_less` and friends. These are C++20
though, and would have to be implemented manually. I am also not sure
it's a good idea to "magically" change the semantics of `<` when it's
used inside a `REQUIRE` macro.

Another alternative approach would be to trigger this warning in a
different way, by including the content of the `REQUIRE` macro in a
different way which doesn't affect the for loop. But I don't have enough
of an overview here to know where would be a good place and how to test
that I didn't break anything.

---
## [H077y/pride-flag-emojis](https://github.com/H077y/pride-flag-emojis)@[d6f34adf46...](https://github.com/H077y/pride-flag-emojis/commit/d6f34adf46d460aea9304c10609765fbf279393b)
#### Wednesday 2022-11-16 16:06:46 by Dragon Nest

Added Catgender, Catnipgender, and Dragongender

Catgender is a xenogender in which someone feels an extremely strong connection to cats or other felines, either strongly identifying with them or simply wanting to incorporate them into their gender to better understand their identity. It is used to describe a gender that feels feline.

Catnipgender is a subgender in which an individual is basically catgender, but also experiences other connections to genders which may be more silly, hyperactive, funny, crazy, and/or wacky at the same time, or could just be attached to of the concepts in overall.

Dragongender is a xenogender gender identity on which is reflected by dragons.

---
## [H077y/pride-flag-emojis](https://github.com/H077y/pride-flag-emojis)@[da39453b5e...](https://github.com/H077y/pride-flag-emojis/commit/da39453b5e745457b3709287cb70f3c469065773)
#### Wednesday 2022-11-16 16:08:41 by Dragon Nest

Added 6 gender flags

Gxrl is a gender where a female and an agender identity are experienced simultaneously or with variation.

Bxy is a gender where a male and an agender identity are experienced simultaneously or with variation.

Non-binary woman, or non-binary girl, refers to someone who identifies both as a woman and as non-binary. 

Non-binary man, or non-binary boy, refers to someone who identifies both as a man and as non-binary.

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[d13f5674c7...](https://github.com/lyz-code/blue-book/commit/d13f5674c752564b6308a0a987be25c5fdbeeb08)
#### Wednesday 2022-11-16 17:25:32 by Lyz

feat(aleph): Introduce Aleph

[Aleph](https://github.com/alephdata/aleph) is a tool for indexing large amounts
of both documents (PDF, Word, HTML) and structured (CSV, XLS, SQL) data for easy
browsing and search. It is built with investigative reporting as a primary use
case. Aleph allows cross-referencing mentions of well-known entities (such as
people and companies) against watchlists, e.g. from prior research or public
datasets.

feat(android_tips#Extend the life of your battery): Extend the life of your battery

[Research](https://accubattery.zendesk.com/hc/en-us/articles/210224725-Charging-research-and-methodology)
has shown that keeping your battery charged between 0% and 80% can make your
battery's lifespan last 2x longer than when you use a full battery cycle from
0-100%.

As a non root user you can
[install Accubattery](https://www.getdroidtips.com/custom-battery-charge-limit-android/)
(not in F-droid :( ) to get an alarm when the battery reaches 80% so that you
can manually unplug it. Instead of leaving the mobile charge in the night and
stay connected at 100% a lot of hours until you unplug, charge it throughout the
day.

feat(environmentalism#Saving water): Saving water

Here are some small things I'm doing to save some water each day:

- Use the watering can or a bucket to gather the shower water until it's warm
  enough. I use this water to flush the toilet. It would be best if it were
  possible to fill up the toilet's deposit, but it's not easy.
- Use a glass of water to wet the toothbrush and rinse my mouth instead of using
  running water.

feat(grapheneos): Introduce GrapheneOS

GrapheneOS is a private and secure mobile operating system with great
functionality and usability. It starts from the strong baseline of the Android
Open Source Project (AOSP) and takes great care to avoid increasing attack
surface or hurting the strong security model. GrapheneOS makes substantial
improvements to both privacy and security through many carefully designed
features built to function against real adversaries. The project cares a lot
about usability and app compatibility so those are taken into account for all of
our features.

feat(elasticsearch#Searching documents): Searching documents

We use HTTP requests to talk to ElasticSearch. A HTTP request is made up of
several components such as the URL to make the request to, HTTP verbs (GET, POST
etc) and headers. In order to succinctly and consistently describe HTTP requests
the ElasticSearch documentation uses cURL command line syntax. This is also the
standard practice to describe requests made to ElasticSearch within the user
community.

An example HTTP request using CURL syntax looks like this:

```bash
curl -XPOST "https://localhost:9200/_search" -d' { "query": { "match_all": {} }
}'
```

feat(ombi): Introduce Ombi

[Ombi](https://ombi.io/) is a self-hosted web application that automatically
gives your shared Jellyfin users the ability to request content by themselves!
Ombi can be linked to multiple TV Show and Movie DVR tools to create a seamless
end-to-end experience for your users.

If Ombi is not for you, you may try [Overseerr](https://overseerr.dev/).

feat(openproject#Deal with big number of tasks): Deal with big number of tasks

As the number of tasks increase, the views of your work packages starts becoming
more cluttered. As you
[can't fold the hierarchy trees](https://community.openproject.org/projects/openproject/work_packages/31918/activity)
it's difficult to efficiently manage your backlog.

I've tried setting up a work package type that is only used for the subtasks so
that they are filtered out of the view, but then you don't know if they are
parent tasks unless you use the details window. It's inconvenient but having to
collapse the tasks every time it's more cumbersome. You'll also need to reserve
the selected subtask type (in my case `Task`) for the subtasks.

feat(openproject#Sorting work package views): Sorting work package views

They are sorted alphabetically, so the only way to sort them is by prepending a
number. You can do `0. Today` instead of `Today`. It's good to do big increments
between numbers, so the next report could be `10. Backlog`. That way if you
later realize you want another report between Today and Backlog, you can use
`5. New Report` and not rename all the reports.

feat(openproject#Pasting text into the descriptions): Pasting text into the descriptions

When I paste the content of the clipboard in the description, all new lines are
removed (`\n`), the workaround is to paste it inside a `code snippet`.

feat(pedal_pc): Introduce Pedal PC

The Pedal PC idea gathers crazy projects that try to use the energy of your
pedaling while you are working on your PC. The most interesting is
[PedalPC](https://www.pedalpc.com/), but still crazy.

[Pedal-Power](http://pedal-power.com/) is another similar project, although it
looks unmaintained.

feat(redox): Installation instructions

First flash:

Download the hex from the via website

Try to flash it many times reseting the promicros.

```bash
sudo avrdude -b 57600 -p m32u4 -P /dev/ttyACM0 -c avr109 -D -U flash:w:redox_rev1_base_via.hex
```

Once the write has finished install via:

https://github.com/the-via/releases/releases

Reboot the computer

Launch it with `via-nativia`.

feat(vscodium): Introduce VSCodium

[VSCodium](https://github.com/VSCodium/vscodium) are binary releases of VS Code
without MS branding/telemetry/licensing.

---
## [CSC207-2022F-UofT/course-project-team-communify](https://github.com/CSC207-2022F-UofT/course-project-team-communify)@[d2cd0893c1...](https://github.com/CSC207-2022F-UofT/course-project-team-communify/commit/d2cd0893c1c885bfecf5e8c4eee680a8e14e4a17)
#### Wednesday 2022-11-16 17:36:27 by clin1967

Song Database Implementation: songLibrary, songDsData, bits and pieces.

Pull includes the implementation of everything relating to Song's database: mainly songLibrary and songDsData. Brief summary;

- **Uploaded the standard library of songs.** Currently located in the new folder songLib under src. Any test cases or other pieces of code that currently create new instances of Songs should likely be re-reviewed with this in mind. I already fixed a few, but I might've missed some.

- Updated build.gradle to include jaudiotagger

- Updated Song entity to include username of uploading user.

- Reading/saving from songs.csv, formatted as `ID, uploader, filepath`

- Changed artistList from List<String> to String[]

- Removed 'length' as Jaudiotagger cannot retrieve it. If we want to show it, it would be on the Jlayer side. Better suited this way, anyway.

- Removed isExplicit. Too much of a pain for too little gain.

- changed saveSong to return a boolean for a successful song addition.

- Created Test file for SongLibrary.

KNOWN ISSUES

- createFile() assumes the existence of a user admin, as it assigns all songs currently in songLib /to/ admin. (This was only important for creating songs.csv from scratch. It won't do this now that it exists.)

- Many files don't have album covers. I'll be creating default covers to put in the BufferedImage parameter later. I don't think anyone is at that stage (which is why I'm putting it off for a later PR), but please don't try accessing the BufferedImage parameter until I do.

- When parsing ID names, the 0s at the beginning of the names are omitted. Theoretically, this shouldn't create duplicate IDs anyway, as 1) what's being checked is the parsed ID, and 2) randInt will not create more IDs that start with 0. I'll go back and rename the files to omit the 0s (not that difficult), but I figure its lower priority due to the reasons I stated.

- Need to implement safeguard against improperly formatted mp3s (ex. missing genre). There currently aren't any, so it should be temporarily OK, but I have some code smells because of this.

Making this a PR despite this so you guys have a better SONG_LIBRARY to work with for now.

---
## [dawido90183/sonic-1-github-madness](https://github.com/dawido90183/sonic-1-github-madness)@[73a2c285bb...](https://github.com/dawido90183/sonic-1-github-madness/commit/73a2c285bb4d391adb65e69049025f06e3e49044)
#### Wednesday 2022-11-16 17:53:33 by dg

you all are dicks (delete fuck you.png)

do you really think i don't regret saying that sort of thing?

---
## [johnleoharkins/forged-dome-pelennor](https://github.com/johnleoharkins/forged-dome-pelennor)@[f93424a11a...](https://github.com/johnleoharkins/forged-dome-pelennor/commit/f93424a11aa72bbfd43ed3be43c6735f31548d81)
#### Wednesday 2022-11-16 17:58:14 by johnleoharkins

thats such fucking bullshit. you've got to be fucking joking me right now. absolutely slamming my fucking chain. good fucking lord. fuck you.

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[7cb69c2a8b...](https://github.com/mullenpaul/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Wednesday 2022-11-16 18:35:41 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [Blueberryy/Mo_Creeps](https://github.com/Blueberryy/Mo_Creeps)@[e441f64a35...](https://github.com/Blueberryy/Mo_Creeps/commit/e441f64a356012718ac09eff551b6d0daeb030e2)
#### Wednesday 2022-11-16 20:19:41 by Conga Lyne

New Spell, Various Changes

Master of Mana are now considerably more tasty...
Master of Mana are now made out of Enchanted Meat
Significantly reduced blood bled by Master of Mana
Colossal & Creepy Blob are now immune to freezing, if you freeze melee them, it's possible for them to die before they spawn their babies, defeating the entire point behind the encounter, you're no longer challenged on your crowd-control ability
Added new Enlightened Alchemist variants
Removed Cursed Orb Barrage. The spell felt unnecessary, it didn't introduce anything new and the method for unlocking it felt.. dumb, as if once you beat a Divine Being you had a 50% chance of getting a run winner from a Cursed Chest.. Perhaps it could make a combat later but for now it's removed until further notice.
Reduced Smoking Fungi's spawnrate in Fungal Caverns
Statues now spawn in the trophy room on the same run you achieve them
New Experimental Spell: Targetter, this spell will have the same effect Forsaken eyes & Observers have, it's experimental since I really like the concept of a "friendly fire this guy" spell but I'm not sure how under/over powered it'll be, will likely require a lot of tinkering over time.
Slightly increased Wand Tinkering Crystal's hitbox
Buffed Weirdo's Shield

---
## [Blueberryy/Mo_Creeps](https://github.com/Blueberryy/Mo_Creeps)@[2065e3a419...](https://github.com/Blueberryy/Mo_Creeps/commit/2065e3a4199539abb8615c74e4fb0ee12b317709)
#### Wednesday 2022-11-16 20:19:41 by Conga Lyne

New Creep, new Pixelscene, various balance changes

Fixed Weak Hisii Shotgunners not jumping into minecarts
Fixed Hisii Shotgunners occasionally turning into their weaker versions in minecarts
Fixed Ceiling Fungus needing air to survive
Red Sand now absorbs blood to grow
Reduced Sentry Damage in earlier parts of the game
Sigificantly reduced Sentry's range, he should now play a slightly different role than sniper by requiring a closer encounter but having better stats to cut through
Nerfed wand dropped by Pandora's Chest on normal difficulty
Mini Drones in earlier parts of the game are now more vulnerable to projectile damage
Magic Devourer's are now more vulnerable to projectile & explosive damage
Added 1 new pixelscene for Coal Pits, demonstrating Red Sand growing when fed Blood
New creep: Smoking Fungus

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3c187487b1...](https://github.com/tgstation/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Wednesday 2022-11-16 21:44:35 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[bb494c3a72...](https://github.com/Sunrin-Social-Network/SSN-server/commit/bb494c3a72f7a7306faca972be4035c86aba1ec2)
#### Wednesday 2022-11-16 22:32:43 by Hyunjun Yang

Merge pull request #13 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1ba95626a6...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1ba95626a6614177da02665231900620bbaef2ce)
#### Wednesday 2022-11-16 22:42:00 by SkyratBot

[MIRROR] mech bustin update 2022 [MDB IGNORE] (#17504)

* mech bustin update 2022 (#70891)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a huge ass crowbar to robotics (the mech removal tool), it deals 5
damage unwielded, or 19 wielded. (should be fine, considering robotics
also has the easiest access to the materials needed for a chainsaw)
You can use it while wielded on mechs to break the occupants out. This
takes 5 seconds (or 3 in an unenclosed mech like a ripley)
When you die in a mech you no longer automatically get ejected.
refactors fire axe cabinets to support more items than the fireaxe
makes some vehicle code better
closes #70845 (you can still enter a mech without limbs, i think thats
fine because you can use it to protect yourself from death in a
dangerous situation or something until someone breaks you out with the
really large crowbar)
video: https://streamable.com/x4gom2

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->
robotics having a giant ass crowbar to break people out of mechs seems
like a fun idea
you currently cant exit a mech if youre incapacitated inside it unless
you DIE

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

:cl: Fikou, sprites by Halcyon
refactor: fire axe cabinets support items that aren't fire axes
balance: mechs no longer eject you when you die in them
add: Adds a giant crowbar to robotics, it can break open mechs to eject
their pilots.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* mech bustin update 2022

* vr for the love of god

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [GremlingSS/funset-pastryland](https://github.com/GremlingSS/funset-pastryland)@[8a27b0fe9d...](https://github.com/GremlingSS/funset-pastryland/commit/8a27b0fe9d5f5f30d2db06246970d76c74cfe00d)
#### Wednesday 2022-11-16 23:02:43 by bearrrrrrrrr

i'm KILLING you. i am KILLING y ou. i don't care about anything else i don't give a SHIT about anything else. my programming is just, 'GET THAT FUCKING GUY'

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[c18463c05f...](https://github.com/Sunrin-Social-Network/SSN-server/commit/c18463c05f33f05b35ed34629df57feb881ea71c)
#### Wednesday 2022-11-16 23:09:19 by Hyunjun Yang

Merge pull request #14 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[ef303cf507...](https://github.com/Sunrin-Social-Network/SSN-server/commit/ef303cf5077b2903a8a053527ab8785acf7f7473)
#### Wednesday 2022-11-16 23:11:53 by Hyunjun Yang

Merge pull request #15 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [evykassirer/zulip](https://github.com/evykassirer/zulip)@[23a776c144...](https://github.com/evykassirer/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Wednesday 2022-11-16 23:14:24 by Mateusz Mandera

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
## [BlueWildrose/tgstation](https://github.com/BlueWildrose/tgstation)@[fc7c186957...](https://github.com/BlueWildrose/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Wednesday 2022-11-16 23:36:55 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---

