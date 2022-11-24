## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-23](docs/good-messages/2022/2022-11-23.md)


2,027,618 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,027,618 were push events containing 3,070,091 commit messages that amount to 237,610,909 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [TNG-dev/Tachi](https://github.com/TNG-dev/Tachi)@[b823ed064a...](https://github.com/TNG-dev/Tachi/commit/b823ed064ad56256477a915b1b12a7bd4c41e211)
#### Wednesday 2022-11-23 00:15:10 by zkldi

fix: remove corrupt charts

zuttenbrihguhg of gott and some maimai chart
for "friends shitai"

i honestly don't know what they were for or how
they ended up like this.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[e91bd4f90b...](https://github.com/ammarfaizi2/linux-fork/commit/e91bd4f90b8e687fd9bb221ea1d95bf0d54c328e)
#### Wednesday 2022-11-23 00:21:18 by Johannes Weiner

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
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[7d04edb6e2...](https://github.com/MTandi/tgstation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Wednesday 2022-11-23 00:49:05 by Profakos

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2a5a5fc8b1...](https://github.com/TaleStation/TaleStation/commit/2a5a5fc8b1b110cea2afd52c02c423e431f7aa78)
#### Wednesday 2022-11-23 01:26:54 by TaleStationBot

[MIRROR] [MDB IGNORE] JPS Optimization (Light Botcode) (#3330)

* JPS Optimization (Light Botcode) (#70623)



## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog


:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:


Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[b77cf7c120...](https://github.com/lessthnthree/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Wednesday 2022-11-23 01:27:56 by Iamgoofball

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
## [log1cs/android_kernel_lge_msm8998](https://github.com/log1cs/android_kernel_lge_msm8998)@[f5c3a1c5ef...](https://github.com/log1cs/android_kernel_lge_msm8998/commit/f5c3a1c5efe05bc92d0683637c25cb339fa6985f)
#### Wednesday 2022-11-23 01:42:14 by Christian Brauner

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
## [NepPure/gitea](https://github.com/NepPure/gitea)@[3725fa28cc...](https://github.com/NepPure/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Wednesday 2022-11-23 02:17:46 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [rust-lang/rust](https://github.com/rust-lang/rust)@[2f506e6dd4...](https://github.com/rust-lang/rust/commit/2f506e6dd4eb4a3727aab8ba6349e80e3383dca9)
#### Wednesday 2022-11-23 03:17:45 by Yuki Okushi

Rollup merge of #101368 - thomcc:wintls-noinline, r=ChrisDenton

Forbid inlining `thread_local!`'s `__getit` function on Windows

Sadly, this will make things slower to avoid UB in an edge case, but it seems hard to avoid... and really whenever I look at this code I can't help but think we're asking for trouble.

It's pretty dodgy for us to leave this as a normal function rather than `#[inline(never)]`, given that if it *does* get inlined into a dynamically linked component, it's extremely unsafe (you get some other thread local, or if you're lucky, crash). Given that it's pretty rare for people to use dylibs on Windows, the fact that we haven't gotten bug reports about it isn't really that convincing. Ideally we'd come up with some kind of compiler solution (that avoids paying for this cost when static linking, or *at least* for use within the same crate...), but it's not clear what that looks like.

Oh, and because all this is only needed when we're implementing `thread_local!` with `#[thread_local]`, this patch adjusts the `cfg_attr` to be `all(windows, target_thread_local)` as well.

r? ``@ChrisDenton``

See also #84933, which is about improving the situation.

---
## [LZakida/vgstation13](https://github.com/LZakida/vgstation13)@[d34b638f74...](https://github.com/LZakida/vgstation13/commit/d34b638f74c944dcc7ed406ac3de2517ca0a2e4c)
#### Wednesday 2022-11-23 03:30:23 by L Z

CRITICAL BUG FIX

Massive Fug Bix:
bug was caused by a single fucking line of code which would cause Dream Daemon to hang on current versions of Byond. This bug went undetected in large part because I was 2 major versions behind the stable (and God knows how many minor versions).
Qui deserves primary credit for finding this.

Co-Authored-By: Urlance Woolsbane <10413301+sheepfighter@users.noreply.github.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[317aea0435...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Wednesday 2022-11-23 03:52:04 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [softcerv/Skyrat-tg](https://github.com/softcerv/Skyrat-tg)@[0b9264ce5f...](https://github.com/softcerv/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Wednesday 2022-11-23 04:30:29 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[84a85c827d...](https://github.com/lizardqueenlexi/orbstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Wednesday 2022-11-23 04:35:12 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [JackDotJS/JackDotJS.github.io](https://github.com/JackDotJS/JackDotJS.github.io)@[2a8fc76cbc...](https://github.com/JackDotJS/JackDotJS.github.io/commit/2a8fc76cbcda3786573388dc80f21a6d8dfa8433)
#### Wednesday 2022-11-23 05:44:47 by Kyle Edwards

stupid fucking vendor prefixes fuck you fuck you fuck you

---
## [dubstard/eth-phishing-detect](https://github.com/dubstard/eth-phishing-detect)@[7ab075b14c...](https://github.com/dubstard/eth-phishing-detect/commit/7ab075b14cad2a77e797c4bd35b39f99a759b342)
#### Wednesday 2022-11-23 06:47:30 by Mich

Update config.json

🎭 Advance fee #fraud (419 investment #scam)
💵 The portfolio of the "investors" grows on paper while they waste money away
💸 Upon any attempt to withdraw the problems begin

Imaginary banks - Fake investment platforms - Fake crypto mining and "yearn" liquidity provisioning scams

As usual - domains and hosting purchased using BTC ONLY.
The BTC which gets received by the registrar and webhosting providers as payment was obtained from scams! 
And is subsequently used to fuel more scams.
How is this not money laundering - Illegally obtained funds get turned into legal "profit"....
Very hard to "InVeStIGaTe"

Common red flags 

🚩website pretends to be a "BANK"
🚩website pretends to be an "INVESTMENT PORTAL"
🚩website hosting service was purchased using BITCOIN
🚩website owner is JHON DOE from countries with less-than-good reputation to put it mildly (cybercrime safe harbors)
🚩website domain was purchased using BITCOIN
🚩website domain owner uses YAHOO MAIL, YANDEX MAIL, TEMPORARY EMAIL, etc

Honestly who the hell would believe stuff like "RothschildIlluminatiDynasty.site" is beyond my comprehension.  

Or even better - FTX went bust - so why not make fake "FTX Compensation scams".
The recent ftx fiasco has fueled many "refund" and "compensation" scams. 
There is zero logic in this - "as we went bankrupt, we decided to do a giveaway. " - how does this make any sense?

But you never know - users may be desperate, especially if already gotten rekt.

---
## [danolivo/pgdev](https://github.com/danolivo/pgdev)@[8272749e8c...](https://github.com/danolivo/pgdev/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Wednesday 2022-11-23 07:22:58 by Tom Lane

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
## [git/git](https://github.com/git/git)@[f1c903debd...](https://github.com/git/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Wednesday 2022-11-23 07:24:08 by Ævar Arnfjörð Bjarmason

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
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[0747099063...](https://github.com/Salex08/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Wednesday 2022-11-23 08:58:10 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[bf582cb833...](https://github.com/Salex08/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Wednesday 2022-11-23 08:58:10 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[bbb956d2a6...](https://github.com/Salex08/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Wednesday 2022-11-23 08:58:10 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[460ab7adf5...](https://github.com/Paxilmaniac/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Wednesday 2022-11-23 09:09:14 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Gamezff/dpemotes](https://github.com/Gamezff/dpemotes)@[fadbae861b...](https://github.com/Gamezff/dpemotes/commit/fadbae861b8eadf7aa6b2ef469797c2b6602ba23)
#### Wednesday 2022-11-23 09:20:34 by TayMcKenzieSA

Implemented More Walkstyles Found In Menyoo

You don't own any code, get a life, stay the fuck out of my DMs, touch grass, stop claiming shit to be yours.

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[3c187487b1...](https://github.com/ss220-space/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Wednesday 2022-11-23 10:09:07 by MrMelbert

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
## [Bak-JH/UnrealLab](https://github.com/Bak-JH/UnrealLab)@[8068d3787f...](https://github.com/Bak-JH/UnrealLab/commit/8068d3787f020ef2cf61226590d93374bcb72fde)
#### Wednesday 2022-11-23 10:41:58 by BakJH

fuck you unreal - get problem with "Try Get Pawn Owner"

---
## [kroetzer/Data-Science-Showcase-Depp-v-Heard](https://github.com/kroetzer/Data-Science-Showcase-Depp-v-Heard)@[6a52875793...](https://github.com/kroetzer/Data-Science-Showcase-Depp-v-Heard/commit/6a528757937b050b52113d1ade7453d2d0968974)
#### Wednesday 2022-11-23 10:49:22 by Katharina Roetzer

Update README.md


This is our SICSS (Summer Institute in Computational Social Science) 2022 Aachen-Graz project. In 4.5 days, we investigated the polarisation regarding the Depp v Heard case within the social media debate on Twitter. 

This project serves as a showcase for data-driven approaches that tackle (research) questions by employing and integrating multiple methods of data analysis: from in-depth 'small scale' qualitative analysis to 'big scale' sentiment, polarisation, and network analysis of Twitter data.  

We are happy to share our presentation (reporting on general approach and design, data selection criteria, data collection, data analysis, and results) and our code. Please note that we must not share the original tweets we used for our analysis (we do share the selection criteria we used, i.e. the query we used for the Twitter API). 

Project team (alphabetical order): 
Dovlat Aliyeva,
Yasaman Asgari (aka our amazing coding wizard), 
Muhsin Ciftci,
Alina Kopkow,
Katharina Roetzer,
Nathalie Van Raemdonck,
Zehui Yu.

Special thanks to Jana Lasser and Ivan Smirnov for organising and teaching in the context of SICSS 2022 Aachen-Graz, as well as all their input, feedback, and support throughout.

---
## [timokau/avalon](https://github.com/timokau/avalon)@[c4de56a4d9...](https://github.com/timokau/avalon/commit/c4de56a4d9afcb2af061684f1ff913f104ebbc01)
#### Wednesday 2022-11-23 11:25:21 by Zack Polizzi

Merge branch 'zack/mac_install' into 'main'

Update docs for formatting; update formatters to modern packages

I was trying to fix my local formatter setup and that sorta snowballed into cleaning up a bunch of related stuff. Now setting up a local environment should be painless, and I updated black and isort to the latest versions because we were running some really old stuff. The new ones have some nice new features and bugfixes.

- improved docs for setting up a local environment
- removed ray (pretty sure unused now) and downgraded openturns by one minor version which the author said was identical (to get it to be installable on mac)
- cleaned up the pyfixfmt lock files and instructions. public usage is already on the github repo; reorienting the files in our repo to be aimed at internal usage. the lock files were kinda broken so i just updated everything to the most recent version and pinned those in a proper requirements file.
- updated pyfixfmt to be compatible with the latest versions of black and isort - the versions we were using were 2+ years old.
- redid isort configuration to work with isort 5.0. now, missing packages will automatically be classified as third-party, which should reduce the dependence on having your environment set up properly. as you can see in the diff, this already has fixed a bunch of stuff.
- re-formatted the whole codebase with the new versions. the most notable change is that spaces around exponent operations were removed (https://github.com/psf/black/issues/538); everything else is quite minor.
- removed black and isort from the research dockerfile - we never use these tools in a container, do we?


Once merged, I'll post in engineering to have everyone update to the new versions.

See merge request generally-intelligent/generally_intelligent!419

Source: fcf664ad3bf53a38bfadf717e0f79c127a92102f

---
## [Colin-Tel/Nyanotrasen](https://github.com/Colin-Tel/Nyanotrasen)@[82755da1b8...](https://github.com/Colin-Tel/Nyanotrasen/commit/82755da1b89eb4b5ff99f9f278f5702cd3836750)
#### Wednesday 2022-11-23 12:27:35 by Rane

OKAY FINE I'LL DO IT (#685)

* HOLY FUCKING SHIT MOFF!!!!!

* mail receiver

* convert some of the mechanics to nyano standard

Co-authored-by: PixelTheKermit <85175107+PixelTheKermit@users.noreply.github.com>

---
## [caseykclim/Vegan](https://github.com/caseykclim/Vegan)@[807d09d8c4...](https://github.com/caseykclim/Vegan/commit/807d09d8c455f1dc0b67f863b48de5c795f540f3)
#### Wednesday 2022-11-23 12:32:25 by Casey K.C. Lim

Add files via upload

I wrote this article to share my experience as a vegan with as many people as possible. In this article, I put forward my views that a balanced vegan diet is very powerful as a means for preventive medicine and why the diet is inseparable from the Environmental, Social and Governance (ESG) issues that are affecting us. On the benefits to the environment, I describe, based on scientific findings, how this diet is a crucial tool in combating global warming and pollution of our water and land resources.

I strongly believe diseases such as diabetes, high blood pressure, heart-related problems, certain cancers, kidney-related diseases and other diseases are preventable or better managed based on my personal experience and the research findings that I have discussed in this article. In addition to lifestyle changes, adopting renewable energy such as solar and wind power, and other methods, the vegan diet is our partner in humankind's fight against climate change and pollution. 

There is a lot more on vegan diet that we have not understood. I have also listed a number of research topics that graduate students, professors, agencies, government departments, etc. may wish to look into. 

This article does not touch on Buddhism and karma. This shorter version is suitable for those who wish to focus on the science behind the vegan diet. I have a longer version, Plant powered 26 July 2022 for all.pdf, that contains my interpretations of the relationship between the vegan diet and Buddhist beliefs and karma.

This article is currently available free. Please feel free to share with others. Comments are welcome.

The file, Plant powered 26 July 2022 for all.pdf, is also available on GitHub. Please feel free to download and share. 

Thank you, Casey

---
## [caseykclim/Vegan](https://github.com/caseykclim/Vegan)@[b08dcbeb41...](https://github.com/caseykclim/Vegan/commit/b08dcbeb418c7ea1e2418824ddd2e26b964490af)
#### Wednesday 2022-11-23 12:39:32 by Casey K.C. Lim

Add files via upload

I wrote this article to share my experience as a vegan with as many people as possible. In this article, I put forward my views that a balanced vegan diet is very powerful as a means for preventive medicine and why the diet is inseparable from the Environmental, Social and Governance (ESG) issues that are affecting us. On the benefits to the environment, I describe, based on scientific findings, how this diet is a crucial tool in combating global warming and pollution of our water and land resources.

This article also contains my interpretations of the relationship between the vegan diet and Buddhist beliefs and karma. For those who wish to focus on the science behind the vegan diet and do not wish to access content on Buddhism and karma owing to certain religious beliefs, etc., please read the other shorter version, ESG and vegan 26 July 2022 for all.pdf.

I strongly believe diseases such as diabetes, high blood pressure, heart-related problems, certain cancers, kidney-related diseases and other diseases are preventable or better managed based on my personal experience and the research findings that I have discussed in this article. In addition to lifestyle changes, adopting renewable energy such as solar and wind power, and other methods, the vegan diet is our partner in humankind's fight against climate change and pollution. 

This article includes an account of my thoughts when I was a small kid on whether humankind should be eating meat and compassion toward animals. It contains discussions related to karma and why quite a number of Buddhists choose not to eat meat and seafood. 

There is a lot more on vegan diet that we have not understood. I have also listed a number of research topics that graduate students, professors, agencies, government departments, etc. may wish to look into. 

This article is currently available free. Please feel free to share with others. Comments are welcome.

The shorter version, ESG and vegan 26 July 2022 for all, is also available on GitHub. Please feel free to access and share. 

Thank you, Casey

---
## [Empire-Strikes-Back/Pippen](https://github.com/Empire-Strikes-Back/Pippen)@[bb68dbbd29...](https://github.com/Empire-Strikes-Back/Pippen/commit/bb68dbbd29fbc5c87ba2f20683fcd450f9d7769a)
#### Wednesday 2022-11-23 13:29:31 by Pippen

commander? - Rico, mission? - war

unlike Drymond Green I don't follow blind and get my own podcast

like Rich Roll before he was dead - I don't store

I heard some of what Jesus says and ignored the other - but I know about sow reap store

let me - even though I am evil and against the garden  - also not store git history
let back-to-the-future example run again - like Dredd manages to start the engine of that air bike

:Jim-Breuer what are you doing?! you're losing it
:Stallone yeah? I thought I'm doing great
:Jim-Breuer give people what they want - be a  ig dumb animal they know you

---
## [CaptainBaldi/PsychRewrittenWiki](https://github.com/CaptainBaldi/PsychRewrittenWiki)@[af05f93247...](https://github.com/CaptainBaldi/PsychRewrittenWiki/commit/af05f9324720bb9fbb65ed7dea88cbed72c0d652)
#### Wednesday 2022-11-23 13:58:56 by CaptainBaldi

boy i hate being a perfectionist

I changed one character in the file
'lua' to 'Lua'
god i hate myself

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fccd833526...](https://github.com/tgstation/tgstation/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Wednesday 2022-11-23 14:30:43 by GoldenAlpharex

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
## [hairybeaver/hairybeaver.github.io](https://github.com/hairybeaver/hairybeaver.github.io)@[6898271f5f...](https://github.com/hairybeaver/hairybeaver.github.io/commit/6898271f5fc834fe38b12158658989a888160ed9)
#### Wednesday 2022-11-23 14:52:40 by arne

playing cards previously worked but github is such a pain in the ass and the website didnt update for fcking 5 minutes straight so hey fuck me its my bad zeker alstemblieeffftttt

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[8620d970b0...](https://github.com/sojourn-13/sojourn-station/commit/8620d970b0aaa8d632e83a4dcc35547826f555df)
#### Wednesday 2022-11-23 15:28:36 by DimmaDunk

Shields, sounds, holsters and more (#4169)

* Shields, sounds, holsters and more

- Better sound for blocking with shields, also sounds for stopping projectiles with them (and breaking)
- Ports the double belt pistol holder (pouch) and throwing knives rig (pouch) from Eris. With belt-worn sprites made by me.
- Adds the belt pistol holster and knife rig to the marshal vendors and absolutist printing disk
- Ports the Bulldozer shield from Eris, tweaks its recipe to include an actual closet
- Makes suit sensors spike in danger if someone's toxloss is at 70 or higher, since that is the point of liver failure
- On the same note, reduces the amount of organ damage from MSOF as it was too punishing, allowing for a better window of opportunity to save someone from dying
- Makes deployable barriers needed to be anchored to be able to brace your gun on it
- Adds most types of holsters to marshals vendors, ups their quantity
- Soteria Gauze and Ointment buffed on par with Church ones, to justify their convoluted hand-crafting method
- Makeshift AK and Luty added to random handmade guns to spawn
- Rangers get the double holster instead of the single one
- Adds a generic katana to loadout for four points
- Adds better sounds for the following emotes: male and female *sigh, *whistle (more variety), female *urah
- Adds snort and awhistle (targeted) emotes
- Makes a lot of audible emotes actually check if you're muzzled instead of magically being executed despite mouth coverage
- Adds some of the missing emotes to the *help list
- Adds hissing, meowing, and purring sound for cats, they will hiss at any ghosts they detect now!
- Fixes Mana from Heaven invisible sprite
- Claw and Baton energy drinks added overdose that causes organ damage at 60 units consumed
- Fixes incorrect Claw RED and BLUE sprites
- Claw Blue made actually made tastier
- Case Closer baton now contains atomic coffee instead of espresso (Marshal buff)
- Hay Fever claw energy improved citric formula
- Attempts to port Shields blocking projectiles functionality from Eris, but fails miserably (Tested not to work, but leaving the groundwork just in case)

* Nerfs liver failure damage even further

Random number 2 to 6 damage per tick

* Adds *zartan emote

Whistling of "For he's a jolly good fellow", GI Joe reference.

* Armor pen fix

Certain powered hammers were not properly inheriting armor pen somehow

* Preppers fairness

- Removes Sentinel Seeker from the random prepper mob spawn list
- Makes Sentinel Seeker a low spawner on par with Renders and nightmare stalkers as it shares similar stats with them
- Replaces certain prepper mob spawns with various low-chance Sentinel Seeker spawns on areas of high loot concentration (mech bays, prepper armory, near the excelsior disks, etc)
- Removes a trap spawner on the same room as Outsider spawn, as it can sometimes be a mine impossible to traverse on the only exit way
- Replaces hardspawn of Sentinel Seeker in Preppers medbay with a low chance for one, compensates by adding two more ranged mobs to the area

* Louder emotes

- Some female emotes were too low
- Typo fixes on bear rawr proc

* Apply suggestions from code review

This is a BYOND joke

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---
## [ande7165/UniversalRobotProject](https://github.com/ande7165/UniversalRobotProject)@[c2a2606807...](https://github.com/ande7165/UniversalRobotProject/commit/c2a2606807de9d3e3ebcd3577bb866c506a0cb76)
#### Wednesday 2022-11-23 15:35:18 by Anders Skov Jensen

Fixed shittymq, sending robot info now, fucked around with pub/sub and got it to work by testing on emulator and releasing on phone. Ignore android namespace erros, just vs being a cunt. remember to check code thoroughly when implmenting new shit since vs doesn't tell you about it (atleast not when its xaml docs)

---
## [Zekiru/RainScape](https://github.com/Zekiru/RainScape)@[98cb1fe939...](https://github.com/Zekiru/RainScape/commit/98cb1fe939114eb0f82e946a38118e8397c77c9a)
#### Wednesday 2022-11-23 15:51:33 by OnixXYZ

Implement Functional PreferenceGUI

The Industrial Revolution and its consequences have been a disaster for the human race. They have greatly increased the life-expectancy of those of us who live in “advanced” countries, but they have destabilized society, have made life unfulfilling , have subjected human beings to indignities, have led to widespread psychological suffering(in the Third World to physical suffering as well) and have inflicted severe damage on the natural world. The continued development of technology will worsen the situation. It will certainly subject human beings to greater indignities and inflict greater damage on the natural world, it will probably lead to greater social disruption and psychological suffering, and it may lead to increased physical suffering even in “advanced” countries.

Co-Authored-By: Zeke <93707715+Zekiru@users.noreply.github.com>

---
## [igorescodro/alkaa](https://github.com/igorescodro/alkaa)@[858bdf6ab0...](https://github.com/igorescodro/alkaa/commit/858bdf6ab0028b03e3b4c479fc4b9aa23f2b1c49)
#### Wednesday 2022-11-23 16:48:05 by Igor Escodro

♻️ Refactor the NavGraph for better readability

I want to update all the navigation to be inside the same graph, similar
to the "Now in Android" app. However, my experience with that is pretty
annoying. For now, a simple refactor to break the graphs internally and
make it better to read is enough.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[1d04cec7c5...](https://github.com/cockroachdb/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Wednesday 2022-11-23 18:36:25 by craig[bot]

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
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[34a98dd70d...](https://github.com/RedDevilus/pcsx2/commit/34a98dd70d6eb22c40fd432b47f0ad0b0821721e)
#### Wednesday 2022-11-23 18:47:48 by RedDevilus

GameDB: Fixes to multiple games yet again

- Thrillville + Thrillville Off The Rails: Mad TFF / deinterlace 8 to stop shaking the whole game
- Forgotten Realm Demon Stone: Get rid of more blur
- ATV Offroad Fury 3: MTVU disabled which was an odd find to improve FPS
- Crimson Tears: Wild arms + Full Sprite for reducing bloom misalignment + note that Blending TFF might be better especialy when you use Software.
- Final Fantasy X: Texture in Rt for fixing endgame summons like Anima and The Magus Sisters
- No One Lives Forever: Mipmap full + trilinear + full blending needed to fix lighting

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[3fd7b5f261...](https://github.com/apollographql/apollo-server/commit/3fd7b5f26144a02e711037b7058a8471e9648bc8)
#### Wednesday 2022-11-23 19:10:15 by Trevor Scheer

Update `@apollo/utils.keyvaluecache` dependency (#7187)

Previous releases of the `@apollo/utils.keyvaluecache` package
improperly specified the version range for its `lru-cache` dependency.

Fresh installs of our packages should receive the patch update since
it's careted, so this issue can be worked around by forcing the update
if you're using a lockfile. We should update it anyway since `2.0.0` is
invalid.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [Strik3ria/Auto-Sell-Grey-and-Repair-Equipement](https://github.com/Strik3ria/Auto-Sell-Grey-and-Repair-Equipement)@[ed3232802b...](https://github.com/Strik3ria/Auto-Sell-Grey-and-Repair-Equipement/commit/ed3232802b34107979a42e839986eac214bb444d)
#### Wednesday 2022-11-23 19:47:00 by Strik3ria

FOR THE LOVE OF FUCKING GOD STOP PUTTING THAT BULLSHIT BACK IN THE
FUCKING COMMAND YOU FUCKING BITCH CUNT!!!!!!!!!!!!!

---
## [Strik3ria/Auto-Sell-Grey-and-Repair-Equipement](https://github.com/Strik3ria/Auto-Sell-Grey-and-Repair-Equipement)@[928174d78b...](https://github.com/Strik3ria/Auto-Sell-Grey-and-Repair-Equipement/commit/928174d78b4e6c6a837bdd9e5ef2703d76b706fc)
#### Wednesday 2022-11-23 19:47:00 by Strik3ria

Merge pull request #9 from Strik3ria/strik3ria/localization

FOR THE LOVE OF FUCKING GOD STOP PUTTING THAT BULLSHIT BACK IN THE

---
## [nimblemachines/muforth](https://github.com/nimblemachines/muforth)@[e7d8f795ac...](https://github.com/nimblemachines/muforth/commit/e7d8f795acd9d8026089b0433e40131af18f8913)
#### Wednesday 2022-11-23 20:09:37 by David Frech

[core] WIP - mixed 32/64 implementation

I'm checking this in because there are some interesting ideas in here
for dealing with, eg, a 32-bit wide heap even on 64-bit machines, using
relative addressing. There are interesting questions about when you want
to deal with relative vs absolute addresses, when to convert them, etc.
I came to the conclusion that it made the most sense to always push
absolute addresses onto the stack - and @ and ! and friends would expect
absolute addresses - only converting them to relative form when writing
them into or reading them from a heap cell.

NEXT would be a bit slower because it has to do this conversion - when
reading an xt (a 32-bit relative pointer), it has to make it absolute (by
adding the heap origin address) before fetching the code field - which
is also a relative address, but this time relative to mu_do_colon;
chosen carefully so that colon words would always have a code field with
all zeros, so it would be easily recognizable. ;-)

I've decided to pursue a different approach. Instead of having a nice
compact heap on all platforms, instead let's favor the address size of
the machine. On a 32-bit machine, heap cells - which mostly contain
addresses - are 32 bits wide. And on a 64-bit machine they are 64 bits.
We can write a very natural NEXT that uses machine pointers in most
obvious and efficient way.

The tricky part comes with dealing with *values*. I want to keep the
64-bit computational nature of muforth intact, so the stacks will remain
64 bits wide on all platforms. This works cleanly on a 64-bit machine:
the stacks and the heap are both 64-bits wide. On a 32-bit machine,
we have to store values in two consecutive cells, and be careful about
alignment or do 64-bit fetches and stores in two 32-bit pieces. I'm not
too concerned about this because 32-bit machines are not the "intended"
host platform for muforth; I'm much more interested in a stellar
experience on 64-bit machines. But if I can get it to work reasonably
well on 32-bit machines, great.

Some of the changes I've made while experimenting with the
relative-addressed heap still apply, and there are also some changes in
the way that values are communicated between C and Forth that I want to
keep, so I'm going to start from here as I continue on this adventure
into the heap!

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[99fd9a2bd5...](https://github.com/treckstar/yolo-octo-hipster/commit/99fd9a2bd566fe1cb088bb764178cf10d189ef7e)
#### Wednesday 2022-11-23 20:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [airplanedev/lib](https://github.com/airplanedev/lib)@[a5978d8afe...](https://github.com/airplanedev/lib/commit/a5978d8afeee4652692dd3f3c2d2f39e369d64db)
#### Wednesday 2022-11-23 20:23:20 by Lee Weisberger

Send env vars when creating deployment (#411)

## Description
In bundle discovery, send env vars along with the bundles. Env vars are calculated from `airplane.yaml` and the task definition.

The original plan here was to calculate these in the bundler. However env vars contain secret values that must be resolved. I don't think we should do this in the bundler because we'd have to expose an endpoint to resolve secret values and the bundler doesn't have any sort of advanced authn. Let me know if you have any other thoughts here, or else we'll just send these with the bundle.

## Test plan
I wrote a unit tests

---
## [weg-li/weg-li](https://github.com/weg-li/weg-li)@[0ca51a1a0f...](https://github.com/weg-li/weg-li/commit/0ca51a1a0f1cd5c9f01856dab851109911942a9b)
#### Wednesday 2022-11-23 21:06:13 by Peter Schröder

add omniauth apple

let god be with us, you stupid fucks at apple. how can your products be so successful when the whole developer experience for your services is just a steaming pile of shit. assholes!

---
## [AstronautCharlie/news-bias](https://github.com/AstronautCharlie/news-bias)@[4ba445e9b8...](https://github.com/AstronautCharlie/news-bias/commit/4ba445e9b889e4d9596591a2e46104af99d145d3)
#### Wednesday 2022-11-23 21:35:46 by trevor_pearce

removing newlines cuz fucking newline conversion can suck the devil's own anus

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[83c75cac2c...](https://github.com/Cheshify/tgstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Wednesday 2022-11-23 21:41:07 by Jacquerel

Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)



Goliaths, Legions, Watchers, and (as of recently) Bileworms all drop
something vaguely useful when they die.
Brimdemons and Lobstrosities do not. This PR aims to fix that, so that
there's at least some vague benefit to hunting them.

In this case it takes the form of organs you get when you butcher them,
similar to the regenerative core from Legions.
As they're similar to the regenerative core, I modified the regenerative
core to extend from a new common "monster core" typepath which these two
new organs also extend.
Like the regenerative core, both of these items do something when used
and something slightly different if you go to the effort of having
someone implant them into your body. They also decay over time, and you
can use stabilising serum to prevent this from happening.


https://user-images.githubusercontent.com/7483112/195967746-55a7d04d-224e-412d-aedc-3a0ec754db3d.mp4

The Rush Gland from the Lobstrosity lets you do a little impression of
their charging attack, making you run very fast for a handful of seconds
and ignoring slowdown effects. Unlike a lobstrosity you aren't actually
built to do this so if you run into a mob you will fall over, and if you
are doing this on the space station running into any dense object will
also make you fall over (it shouldn't make you _too_ much of a pain for
security to catch).
The idea here is that you use this to save time running back and forth
from the mining base.

The Brimdust Sac from the Brimdemon covers you in exploding dust. The
next three times you take Brute damage some of the dust will explode,
dealing damage equal to an unupgraded PKA shot to anything near you (but
not you).
If you do this in a space station not only is the damage proportionally
lower (still matching the PKA), but it _does_ effect you and also it
sets you on fire. You can remove the buff by showering it off.
The idea here is that you use this for minor revenge damage on enemies
whose attacks you don't manage to dodge.


https://user-images.githubusercontent.com/7483112/195967811-0b362ba9-2da0-42ac-bd55-3809473cbc74.mp4

If you implant the Rush Gland then you can use it once every 3 minutes
without consuming it, and the buff lasts very slightly longer. It will
automatically trigger itself if your health gets low, which might be
good (helps you escape a rough situation) or bad (didn't want to use it
yet).


https://user-images.githubusercontent.com/7483112/195967888-f63f7cbd-60cd-4309-8004-203afc5b2153.mp4

If you implant the Brimdust Sac then you can use it once every 3 minutes
to shake off cloud of dust which gives the buff to everyone nearby, if
you want to kit out your miner squad. The dust cloud also makes you
cough if you stand in it, and it's opaque. If you catch fire with this
organ inside you and aren't in mining atmosphere then it will explode
inside of your abdomen, which should probably be avoided, resultingly it
is very risky to use this on the space station.

---
## [MemeHoovy/Kade-Engine-Community](https://github.com/MemeHoovy/Kade-Engine-Community)@[e69c4ebf99...](https://github.com/MemeHoovy/Kade-Engine-Community/commit/e69c4ebf99deb6c36cecdce12e4e25bc1f932bf7)
#### Wednesday 2022-11-23 22:21:31 by TheRealJake_12

I am so sorry it took so long

and everything is broken fuck 1.6 I hate everything

---
## [MicrosoftDocs/powerbi-docs](https://github.com/MicrosoftDocs/powerbi-docs)@[48dea1193f...](https://github.com/MicrosoftDocs/powerbi-docs/commit/48dea1193fdeb1770883aaa815a779736f022a3b)
#### Wednesday 2022-11-23 23:22:54 by Maggie Sparkman

Update service-dashboard-create.md

Hi, @justpies, I'm sorry. Kinda gotta start over for this one. Samples will no longer be from the Get Data menu. In fact the Get Data menu won't exist at all. We'll get samples from the Learning Center. Can you see that yet? IDK.

If you can't see it, then we can just put this one on hold for now. Thanks!

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[cb20ec99f9...](https://github.com/san7890/bruhstation/commit/cb20ec99f9cac1f0ca60da1b9dc912ea4e9eebba)
#### Wednesday 2022-11-23 23:40:38 by san7890

[MDB Ignore] Unit Tests for Invalid Space Turfs (Area Bullshit Edition) (#70967)

## About The Pull Request

So, there's some bullshit with the map loader(?) sometimes where it'll
let space turfs spawn in spots where we REALLY don't want space turfs.
Or, it could also just be a mapper screwing up. Anyways, we might miss
these, so let's set up a broad Unit Test that checks and verifies that
these round-ruining snagglers do _not_ exist.

In order to help me to do this, I standardized and fixed the
nomenclature such that `/area/ruin/space` is default for any map file in
`_maps/RandomRuins/SpaceRuins`, as well as it's subtypes. I also touched
up how we handle shuttle areas in these scenarios. This got a lot of
Unit Test noise filtered out, and is crucial for its functioning. It
should also be how we did it from the start anyways. I added in an
UpdatePaths for any compatible change, but it was completely
non-workable for some of the area type updates.

I also fixed any organic bugs that didn't require an areas type update.
Cool.

Placing space turfs on IceBox:

![image](https://user-images.githubusercontent.com/34697715/199177940-21c64964-1808-41b0-9a92-bf5b82eee2fa.png)

Organically found issues:

![image](https://user-images.githubusercontent.com/34697715/199177972-b27a89de-0e1a-41e5-8fa4-3bee1763b9da.png)

I also added a `planetary` variable to `/datum/map_config` because I
didn't like the hack I was using to see if we had a planetary map, and
I'd rather it just be an explicit variable in the map's JSON.

## Why It's Good For The Game

The less times we get Space Turfs showing up on IceBoxStation, the
better. It also standardizes areas a bit more, which I like (we were
using some incorrect ones in the wrong spots, so those were touched up
in this PR as well). Like, if it's a space ruin, we don't need to use
the lengthy `/area/ruin/unpowered/no_grav` when `/area/ruin/space` does
the same thing.
## Changelog
Nothing in here should concern a player (unless I broke something)

Expect a few commits as I spam unit tests a few times and play
whack-a-mole with bugs.

---

