## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-24](docs/good-messages/2022/2022-10-24.md)


2,163,822 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,163,822 were push events containing 3,292,465 commit messages that amount to 261,479,879 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [BA7JCM/website](https://github.com/BA7JCM/website)@[77ea6e8003...](https://github.com/BA7JCM/website/commit/77ea6e8003fe7447492c08d44e872b2a73fe3a17)
#### Monday 2022-10-24 00:48:08 by eraseyourknees

Fix XSS in the error messages
The so-called """security researcher""" pretending he sent me a report
can go fuck himself. I never received your report. Not that I would pay
for this "work", or as I've recently taken to calling it, log shitting.

---
## [k21971/NetHack37](https://github.com/k21971/NetHack37)@[b02e018225...](https://github.com/k21971/NetHack37/commit/b02e01822564e5bee3c31082e978419edea6a37c)
#### Monday 2022-10-24 01:31:39 by Michael Meyer

Remove explicit 'none' opt from autounlock handler

The autounlock handler included an explicit 'none' option, a choice that
gave it a different UX from similar existing compound option handlers
(e.g. paranoid_confirm or pickup_types), which set 'none' simply by
deselecting all options.  It didn't make the menu any easier to use (at
least in my experience), since in order to go from some combination of
options to 'none', you'd have to deselect everything anyway (which on
its own was enough to set 'none', so there was no reason to explicitly
select it after doing so).

Make the autounlock handler work like other compound option handlers,
such that deselecting all options is the way to set 'none', and there is
no explicit 'none' option included in the list.

---
## [VoltageOS-staging/frameworks_base](https://github.com/VoltageOS-staging/frameworks_base)@[b737ffc308...](https://github.com/VoltageOS-staging/frameworks_base/commit/b737ffc308f5e3487d270e68323e45e63953b7ca)
#### Monday 2022-10-24 02:19:35 by Joey Huab

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

Signed-off-by: Dmitrii <bankersenator@gmail.com>

---
## [nitromagix/MyTasks](https://github.com/nitromagix/MyTasks)@[fa88d253da...](https://github.com/nitromagix/MyTasks/commit/fa88d253da6ffdd2b895fa4d29aa2a315e99ccfe)
#### Monday 2022-10-24 02:53:51 by Martin

today was a fucking nightmare. I'm questioning whether I should continue coding. I suck, today sucked. I got NOTHING accomplished. Everything I wrote was shit and didn't work.

---
## [neebe000/kernel_xiaomi_mt6785](https://github.com/neebe000/kernel_xiaomi_mt6785)@[627f9cff99...](https://github.com/neebe000/kernel_xiaomi_mt6785/commit/627f9cff990795a490dcc0d9d5dce4a632dec58b)
#### Monday 2022-10-24 03:09:16 by Peter Zijlstra

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
Signed-off-by: neebe000 <neebexd@gmail.com>

---
## [tgstation/event-toolbox-tournament-2022](https://github.com/tgstation/event-toolbox-tournament-2022)@[f923f61011...](https://github.com/tgstation/event-toolbox-tournament-2022/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Monday 2022-10-24 03:18:02 by MMMiracles

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
## [dragid10/dnd-bot](https://github.com/dragid10/dnd-bot)@[0a9dc0db12...](https://github.com/dragid10/dnd-bot/commit/0a9dc0db12f8914372a464c78432093a4c9cc32a)
#### Monday 2022-10-24 03:56:21 by Alex Oladele

Automatically create discord event when all players have RSVP'd (#23)

<!--- Provide a general summary of your changes in the Title above -->

## Description
<!--- Describe your changes in detail -->
Once all players have RSVP'd to the upcoming session, the DND Bot will
now automatically create a discord event with the specified session time
and date (set when first calling `!config`). When the event is created,
the bot will also post in channel the URL of the event so people can
subscribe

## Motivation and Context
<!--- Why is this change required? What problem does it solve? -->
<!--- If it fixes an open issue, please link to the issue here. -->
I honestly got slightly tired of creating an event myself with all the
same information, but events are really nice and I want to use them more

## How Has This Been Tested?
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran
to -->
<!--- see how your change affects other areas of the code, etc. -->
LIVE! I accidentally deleted the post, but I promise it works lol

## Screenshots (if appropriate):

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [xx] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to change)

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->
- [x] My code follows the code style of this project.
- [x] My change requires a change to the documentation.
- [x] I have updated the documentation accordingly.

---
## [ddnet/ddnet-maps](https://github.com/ddnet/ddnet-maps)@[48a0a272ed...](https://github.com/ddnet/ddnet-maps/commit/48a0a272edea7b7e9d1cbbb80ba1766d98171330)
#### Monday 2022-10-24 04:30:23 by DDNet Maps

R NUT Hardcore UNITED, R NUT_hardcore_bestof, R NUT_hardcore_race1, R NUT_hardcore_race2, R NUT_hardcore_race3, R NUT_hardcore_race4, R NUT_hardcore_race5, R NUT_hardcore_race6, R NUT_race1, R NUT_race2, R NUT_race3, R NUT_race4, R NUT_race5, R NUT_race6, R NUT_race7, R NUT_race8, R NUT_race9, R NUT_short_race1, R NUT_short_race2, R NUT_short_race3, R NUT_short_race4, R NUT_short_race5, R NUT_short_race6, R NUT_short_race7, R #MegaRosenkohl, R -Ikarus-, R 21, R Adrenaline 3, R Alpaga, R Ambrosia, R Arcade 2, R Arcade, R AreaOfEffect, R At Night, R Beachmap, R Besbex, R Best Of, R Black & Red, R Black_City, R Blizzard!, R Blue Hell, R BrokenBlack-1, R Brownie, R Chaos 1, R Chaos 2, R Chaos 3, R Chaos 4, R Cloud Nine, R Cocaine, R Confusion, R CrazyHOOD, R Creative, R Curse, R DawnOfDust, R Day, R DayWalker, R Dead Island, R Deadline 1, R Deadline 2, R DeathClaw, R Dels 2, R Dels 3, R Dels, R Deria, R Difficult 1.1, R Difficult 1.2, R Difficult 1.3, R Difficult 2.1, R Difficult 2.2, R Difficult 2.3, R Divided, R DoT, R Dragonscale, R Dreadful, R Easy Way, R Eclipse, R Elo-Hell, R Energie, R Equalize!, R Executive, R Explosive, R Fantabob, R Fly to the Moon, R Forever, R Four Gates, R Gold Rush, R Hard Way 1.0, R HardcoreZ, R HearTbeaT, R HearTcross, R Hell Fly, R Imagination3, R Insane 2, R Insane 3, R Insane, R Inspire, R IronFlight, R Jajka, R Lost Castle, R LowPossibility3.1, R Madness 5, R MicCore, R Multivitamin, R Nasa, R Natura, R Night Jungle, R NightRunner, R Nightmare, R Notice 1, R Ntumba, R Outlet, R Paik, R Paranoia, R Picklock, R Poke, R Rampage, R Reality, R Red Hell, R Repeat, R Rockita, R Scabrous 2, R SkyIsland, R Skyfly, R Skyisland2, R Skyisland3, R Space, R Summer Hell, R The Tower, R TheWalkingDead, R Therapy, R Think! 2, R Veni Vidi Vici, R Volcano, R Woader, R World of Magic, R Zephronikon, R blue-mountains, R skynet compilation, R supernice, R whatever, R ~AuTuMn~

---
## [Guysnacho/tunjiprod](https://github.com/Guysnacho/tunjiprod)@[cdb26abfdc...](https://github.com/Guysnacho/tunjiprod/commit/cdb26abfdc8a56324ac240e1acb3adf8ac3a5d00)
#### Monday 2022-10-24 07:21:30 by Guysnacho

Ran back to React

Was having trouble with Nuxt, it felt like it was hiding too much from me. Not sure if I added that in another commit but I'll add it here. Took the Tailwind next template and I'll be goin from here but my VS Code isn't autofilling so that's getting annoying. Kinda really relying on autocomplete :|

---
## [ramhak/factorial-dotfiles](https://github.com/ramhak/factorial-dotfiles)@[277b8a2c09...](https://github.com/ramhak/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Monday 2022-10-24 08:22:36 by Pau Ramon Revilla

Disable snippets (#16)

This one is controversial and I will understand if you don't want to
merge it (I will branch if that's the case).

I hate snippets. I never use them and they get in my way. Maybe they are
wrongly configured, but the amount of times that I get snippets when I
don't want them is just a waste of time.

Examples:
  - Sometimes I want to move from `{}` to `do/end` and when I place the
    cursor on `{` and type `do<Enter>` I automatically get an annoying
    `end` that I have to delete imediately.
  - Sometimes I want to press `<Enter>` after a `{` and it will add
    ruby block parameters for no reason.

Do you use them? How do you workaround things getting in the middle when
you don't want them? It screws up my muscle memory.

---
## [kyasu/android_kernel_xiaomi_sdm660](https://github.com/kyasu/android_kernel_xiaomi_sdm660)@[14d53a4140...](https://github.com/kyasu/android_kernel_xiaomi_sdm660/commit/14d53a41409ab5381553ea9fed6ef1d305749724)
#### Monday 2022-10-24 08:52:01 by Christian Brauner

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
## [divinity76/guzzle](https://github.com/divinity76/guzzle)@[f4b86d3d17...](https://github.com/divinity76/guzzle/commit/f4b86d3d17d7ca2bdd86ebff210ec9b5921f471e)
#### Monday 2022-10-24 08:56:12 by divinity76

request no encoding if user does not specify acceptable encodings

due to (imo shitty) specs, when the client does not request any encodings, the server is free to pick any encoding it wants. not sending any `Accept-Encoding` headers is equivalent to sending
Accept-Encoding: *
(as * - anything - is the default Accept-encoding value)

IMO we shouldn't overwrite curl's Accept-Encoding header at all and the guzzle implementation is stupid, i'd love to hear the guzzle dev's rationale, 
 but at least setting CURLOPT_ENCODING='' + Accept-Encoding: identity is better than CURLOPT_ENCODING='' + Accept-encoding: *  (* is implicit when no accept-encoding is specified)

Lets say for example that curl is compiled with gzip+deflate, and curl *wants* to send `Accept-Encoding: gzip,deflate`, but because Guzzle sets `Accept-Encoding: *` (implicitly), the server opts to use br, resulting in broken downloads. this wouldn't have happened if guzzle didn't overwrite curl's default accept-encoding, and it wouldn't have happened if guzzle sent `Accept-Encoding: identity`, but it may happen if guzzle sends `Accept-Encoding: *` as it does prior to this patch.

---
## [sailfishos-mirror/glib](https://github.com/sailfishos-mirror/glib)@[b8e1ecdd6b...](https://github.com/sailfishos-mirror/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Monday 2022-10-24 09:02:31 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [universal5433/android_kernel_samsung_universal5433](https://github.com/universal5433/android_kernel_samsung_universal5433)@[22323dd3df...](https://github.com/universal5433/android_kernel_samsung_universal5433/commit/22323dd3df02bcb939675aa11b0a20a19824028a)
#### Monday 2022-10-24 09:36:54 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

* Fixes scripts/mod/file2alias.c:374:1: warning: adding 'unsigned long' to a string does not append to the string [-Wstring-plus-int]
ADD_TO_DEVTABLE("hid", hid_device_id, do_hid_entry); and 30 other errors

* Remove mipscdmm cpu rapidio ulpi hdaudio from devtable as they do not exist in our kernel

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: I39b197f7e454eefc9fbd5ed5c2cb97f107f08094

---
## [stesamampow/stesamampow.github.io](https://github.com/stesamampow/stesamampow.github.io)@[f5d7039077...](https://github.com/stesamampow/stesamampow.github.io/commit/f5d703907705c3f1c43923a960d32953cdafdd7c)
#### Monday 2022-10-24 09:43:59 by stesamampow

<!DOCTYPE html> <html lang="en">  <head>   <meta charset="utf-8">   <meta content="width=device-width, initial-scale=1.0" name="viewport">    <title>Stesa Mampow</title>   <meta content="" name="description">   <meta content="" name="keywords">    <!-- Favicons -->   <link href="assets/img/favicon.png" rel="icon">   <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">    <!-- Google Fonts -->   <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Satisfy" rel="stylesheet">    <!-- Vendor CSS Files -->   <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">   <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">   <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">   <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">   <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">    <!-- Template Main CSS File -->   <link href="assets/css/style.css" rel="stylesheet">    <!-- =======================================================   * Template Name: Stesa - v4.9.0   * Template URL: https://bootstrapmade.com/Stesa-free-creative-bootstrap-theme/   * Author: BootstrapMade.com   * License: https://bootstrapmade.com/license/   ======================================================== --> </head>  <body>    <!-- ======= Header ======= -->   <header id="header" class="fixed-top d-flex justify-content-center align-items-center header-transparent">      <nav id="navbar" class="navbar">       <ul>         <li><a class="nav-link scrollto active" href="#hero">Home</a></li>         <li><a class="nav-link scrollto" href="#about">About</a></li>         <li><a class="nav-link scrollto" href="#resume">Resume</a></li>         <li><a class="nav-link scrollto" href="#services">Services</a></li>         <li><a class="nav-link scrollto " href="#portfolio">Portfolio</a></li>         <li class="dropdown"><a href="#"><span>Drop Down</span> <i class="bi bi-chevron-down"></i></a>           <ul>             <li><a href="#">Drop Down 1</a></li>             <li class="dropdown"><a href="#"><span>Deep Drop Down</span> <i class="bi bi-chevron-right"></i></a>               <ul>                 <li><a href="#">Deep Drop Down 1</a></li>                 <li><a href="#">Deep Drop Down 2</a></li>                 <li><a href="#">Deep Drop Down 3</a></li>                 <li><a href="#">Deep Drop Down 4</a></li>                 <li><a href="#">Deep Drop Down 5</a></li>               </ul>             </li>             <li><a href="#">Drop Down 2</a></li>             <li><a href="#">Drop Down 3</a></li>             <li><a href="#">Drop Down 4</a></li>           </ul>         </li>         <li><a class="nav-link scrollto" href="#contact">Contact</a></li>       </ul>       <i class="bi bi-list mobile-nav-toggle"></i>     </nav><!-- .navbar -->    </header><!-- End Header -->    <!-- ======= Hero Section ======= -->   <section id="hero">     <div class="hero-container">       <h1>Stesa Trifany Kristi Mampow, S.Kom</h1>       <h2>I'm a Professional Web Developer</h2>       <a href="#about" class="btn-scroll scrollto" title="Scroll Down"><i class="bx bx-chevron-down"></i></a>     </div>   </section><!-- End Hero -->    <main id="main">      <!-- ======= About Me Section ======= -->     <section id="about" class="about">       <div class="container">          <div class="section-title">           <span>About Me</span>           <h2>About Me</h2>           <p>Penepuk bulu angsa yang suka ngodding</p>         </div>          <div class="row">           <div class="image col-lg-4 d-flex align-items-stretch justify-content-center justify-content-lg-start"></div>           <div class="col-lg-8 d-flex flex-column align-items-stretch">             <div class="content ps-lg-4 d-flex flex-column justify-content-center">               <div class="row">                 <div class="col-lg-6">                   <ul>                     <li><i class="bi bi-chevron-right"></i> <strong>Name:</strong> <span>Stesa Trifany Kristi Mampow</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>Website:</strong> <span>www.stesamampow.com</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>Phone:</strong> <span>+6285298141009</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>City:</strong> <span>Tomohon, Indonesia</span></li>                   </ul>                 </div>                 <div class="col-lg-6">                   <ul>                     <li><i class="bi bi-chevron-right"></i> <strong>Age:</strong> <span>23</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>Degree:</strong> <span>Master</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>PhEmailone:</strong> <span>stesamampow11@gmail.com</span></li>                     <li><i class="bi bi-chevron-right"></i> <strong>Freelance:</strong> <span>Available</span></li>                   </ul>                 </div>               </div>               <div class="row mt-n4">                 <div class="col-md-6 mt-5 d-md-flex align-items-md-stretch">                   <div class="count-box">                     <i class="bi bi-emoji-smile" style="color: #20b38e;"></i>                     <span data-purecounter-start="0" data-purecounter-end="232" data-purecounter-duration="1" class="purecounter"></span>                     <p><strong>Happy Clients</strong> consequuntur voluptas nostrum aliquid ipsam architecto ut.</p>                   </div>                 </div>                  <div class="col-md-6 mt-5 d-md-flex align-items-md-stretch">                   <div class="count-box">                     <i class="bi bi-journal-richtextr" style="color: #8a1ac2;"></i>                     <span data-purecounter-start="0" data-purecounter-end="521" data-purecounter-duration="1" class="purecounter"></span>                     <p><strong>Projects</strong> adipisci atque cum quia aspernatur totam laudantium et quia dere tan</p>                   </div>                 </div>                  <div class="col-md-6 mt-5 d-md-flex align-items-md-stretch">                   <div class="count-box">                     <i class="bi bi-clock" style="color: #2cbdee;"></i>                     <span data-purecounter-start="0" data-purecounter-end="18" data-purecounter-duration="1" class="purecounter"></span>                     <p><strong>Years of experience</strong> aut commodi quaerat modi aliquam nam ducimus aut voluptate non vel</p>                   </div>                 </div>                  <div class="col-md-6 mt-5 d-md-flex align-items-md-stretch">                   <div class="count-box">                     <i class="bi bi-award" style="color: #ffb459;"></i>                     <span data-purecounter-start="0" data-purecounter-end="16" data-purecounter-duration="1" class="purecounter"></span>                     <p><strong>Awards</strong> rerum asperiores dolor alias quo reprehenderit eum et nemo pad der</p>                   </div>                 </div>               </div>             </div><!-- End .content-->              <div class="skills-content ps-lg-4">               <div class="progress">                 <span class="skill">HTML <i class="val">100%</i></span>                 <div class="progress-bar-wrap">                   <div class="progress-bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>                 </div>               </div>                <div class="progress">                 <span class="skill">CSS <i class="val">90%</i></span>                 <div class="progress-bar-wrap">                   <div class="progress-bar" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>                 </div>               </div>                <div class="progress">                 <span class="skill">JavaScript <i class="val">75%</i></span>                 <div class="progress-bar-wrap">                   <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>                 </div>               </div>             </div>            </div>         </div>        </div>     </section><!-- End About Me Section -->      <!-- ======= My Resume Section ======= -->     <section id="resume" class="resume">       <div class="container">          <div class="section-title">           <span>My Resume</span>           <h2>My Resume</h2>           <p>Sit sint consectetur velit quisquam cupiditate impedit suscipit alias</p>         </div>          <div class="row">           <div class="col-lg-6">             <h3 class="resume-title">Sumary</h3>             <div class="resume-item pb-0">               <h4>Alice Barkley</h4>               <p><em>Innovative and deadline-driven Graphic Designer with 3+ years of experience designing and developing user-centered digital/print marketing material from initial concept to final, polished deliverable.</em></p>               <p>               <ul>                 <li>Portland par 127,Orlando, FL</li>                 <li>(123) 456-7891</li>                 <li>alice.barkley@example.com</li>               </ul>               </p>             </div>              <h3 class="resume-title">Education</h3>             <div class="resume-item">               <h4>Master of Fine Arts &amp; Graphic Design</h4>               <h5>2015 - 2016</h5>               <p><em>Rochester Institute of Technology, Rochester, NY</em></p>               <p>Qui deserunt veniam. Et sed aliquam labore tempore sed quisquam iusto autem sit. Ea vero voluptatum qui ut dignissimos deleniti nerada porti sand markend</p>             </div>             <div class="resume-item">               <h4>Bachelor of Fine Arts &amp; Graphic Design</h4>               <h5>2010 - 2014</h5>               <p><em>Rochester Institute of Technology, Rochester, NY</em></p>               <p>Quia nobis sequi est occaecati aut. Repudiandae et iusto quae reiciendis et quis Eius vel ratione eius unde vitae rerum voluptates asperiores voluptatem Earum molestiae consequatur neque etlon sader mart dila</p>             </div>           </div>           <div class="col-lg-6">             <h3 class="resume-title">Professional Experience</h3>             <div class="resume-item">               <h4>Senior graphic design specialist</h4>               <h5>2019 - Present</h5>               <p><em>Experion, New York, NY </em></p>               <p>               <ul>                 <li>Lead in the design, development, and implementation of the graphic, layout, and production communication materials</li>                 <li>Delegate tasks to the 7 members of the design team and provide counsel on all aspects of the project. </li>                 <li>Supervise the assessment of all graphic materials in order to ensure quality and accuracy of the design</li>                 <li>Oversee the efficient use of production project budgets ranging from $2,000 - $25,000</li>               </ul>               </p>             </div>             <div class="resume-item">               <h4>Graphic design specialist</h4>               <h5>2017 - 2018</h5>               <p><em>Stepping Stone Advertising, New York, NY</em></p>               <p>               <ul>                 <li>Developed numerous marketing programs (logos, brochures,infographics, presentations, and advertisements).</li>                 <li>Managed up to 5 projects or tasks at a given time while under pressure</li>                 <li>Recommended and consulted with clients on the most appropriate graphic design</li>                 <li>Created 4+ design presentations and proposals a month for clients and account managers</li>               </ul>               </p>             </div>           </div>         </div>        </div>     </section><!-- End My Resume Section -->      <!-- ======= My Services Section ======= -->     <section id="services" class="services">       <div class="container">          <div class="section-title">           <span>My Services</span>           <h2>My Services</h2>           <p>Sit sint consectetur velit quisquam cupiditate impedit suscipit alias</p>         </div>          <div class="row">           <div class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5 mb-lg-0">             <div class="icon-box">               <div class="icon"><i class="bx bxl-dribbble"></i></div>               <h4 class="title"><a href="">Lorem Ipsum</a></h4>               <p class="description">Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident</p>             </div>           </div>            <div class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5 mb-lg-0">             <div class="icon-box">               <div class="icon"><i class="bx bx-file"></i></div>               <h4 class="title"><a href="">Sed ut perspiciatis</a></h4>               <p class="description">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur</p>             </div>           </div>            <div class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5 mb-lg-0">             <div class="icon-box">               <div class="icon"><i class="bx bx-tachometer"></i></div>               <h4 class="title"><a href="">Magni Dolores</a></h4>               <p class="description">Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</p>             </div>           </div>            <div class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5 mb-lg-0">             <div class="icon-box">               <div class="icon"><i class="bx bx-world"></i></div>               <h4 class="title"><a href="">Nemo Enim</a></h4>               <p class="description">At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque</p>             </div>           </div>          </div>        </div>     </section><!-- End My Services Section -->      <!-- ======= Testimonials Section ======= -->     <section id="testimonials" class="testimonials">       <div class="container position-relative">          <div class="testimonials-slider swiper" data-aos="fade-up" data-aos-delay="100">           <div class="swiper-wrapper">              <div class="swiper-slide">               <div class="testimonial-item">                 <img src="assets/img/testimonials/testimonials-1.jpg" class="testimonial-img" alt="">                 <h3>Saul Goodman</h3>                 <h4>Ceo &amp; Founder</h4>                 <p>                   <i class="bx bxs-quote-alt-left quote-icon-left"></i>                   Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.                   <i class="bx bxs-quote-alt-right quote-icon-right"></i>                 </p>               </div>             </div><!-- End testimonial item -->              <div class="swiper-slide">               <div class="testimonial-item">                 <img src="assets/img/testimonials/testimonials-2.jpg" class="testimonial-img" alt="">                 <h3>Sara Wilsson</h3>                 <h4>Designer</h4>                 <p>                   <i class="bx bxs-quote-alt-left quote-icon-left"></i>                   Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.                   <i class="bx bxs-quote-alt-right quote-icon-right"></i>                 </p>               </div>             </div><!-- End testimonial item -->              <div class="swiper-slide">               <div class="testimonial-item">                 <img src="assets/img/testimonials/testimonials-3.jpg" class="testimonial-img" alt="">                 <h3>Jena Karlis</h3>                 <h4>Store Owner</h4>                 <p>                   <i class="bx bxs-quote-alt-left quote-icon-left"></i>                   Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.                   <i class="bx bxs-quote-alt-right quote-icon-right"></i>                 </p>               </div>             </div><!-- End testimonial item -->              <div class="swiper-slide">               <div class="testimonial-item">                 <img src="assets/img/testimonials/testimonials-4.jpg" class="testimonial-img" alt="">                 <h3>Matt Brandon</h3>                 <h4>Freelancer</h4>                 <p>                   <i class="bx bxs-quote-alt-left quote-icon-left"></i>                   Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.                   <i class="bx bxs-quote-alt-right quote-icon-right"></i>                 </p>               </div>             </div><!-- End testimonial item -->              <div class="swiper-slide">               <div class="testimonial-item">                 <img src="assets/img/testimonials/testimonials-5.jpg" class="testimonial-img" alt="">                 <h3>John Larson</h3>                 <h4>Entrepreneur</h4>                 <p>                   <i class="bx bxs-quote-alt-left quote-icon-left"></i>                   Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.                   <i class="bx bxs-quote-alt-right quote-icon-right"></i>                 </p>               </div>             </div><!-- End testimonial item -->            </div>           <div class="swiper-pagination"></div>         </div>        </div>     </section><!-- End Testimonials Section -->      <!-- ======= My Portfolio Section ======= -->     <section id="portfolio" class="portfolio">       <div class="container">          <div class="section-title">           <span>My Portfolio</span>           <h2>My Portfolio</h2>           <p>Sit sint consectetur velit quisquam cupiditate impedit suscipit alias</p>         </div>          <ul id="portfolio-flters" class="d-flex justify-content-center">           <li data-filter="*" class="filter-active">All</li>           <li data-filter=".filter-app">App</li>           <li data-filter=".filter-card">Card</li>           <li data-filter=".filter-web">Web</li>         </ul>          <div class="row portfolio-container">            <div class="col-lg-4 col-md-6 portfolio-item filter-app">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-1.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>App 1</h4>               <p>App</p>               <a href="assets/img/portfolio/portfolio-1.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="App 1"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-web">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-2.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Web 3</h4>               <p>Web</p>               <a href="assets/img/portfolio/portfolio-2.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Web 3"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-app">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-3.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>App 2</h4>               <p>App</p>               <a href="assets/img/portfolio/portfolio-3.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="App 2"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-card">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-4.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Card 2</h4>               <p>Card</p>               <a href="assets/img/portfolio/portfolio-4.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Card 2"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-web">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-5.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Web 2</h4>               <p>Web</p>               <a href="assets/img/portfolio/portfolio-5.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Web 2"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-app">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-6.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>App 3</h4>               <p>App</p>               <a href="assets/img/portfolio/portfolio-6.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="App 3"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-card">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-7.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Card 1</h4>               <p>Card</p>               <a href="assets/img/portfolio/portfolio-7.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Card 1"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-card">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-8.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Card 3</h4>               <p>Card</p>               <a href="assets/img/portfolio/portfolio-8.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Card 3"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>            <div class="col-lg-4 col-md-6 portfolio-item filter-web">             <div class="portfolio-img"><img src="assets/img/portfolio/portfolio-9.jpg" class="img-fluid" alt=""></div>             <div class="portfolio-info">               <h4>Web 3</h4>               <p>Web</p>               <a href="assets/img/portfolio/portfolio-9.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="Web 3"><i class="bx bx-plus"></i></a>               <a href="portfolio-details.html" class="details-link" title="More Details"><i class="bx bx-link"></i></a>             </div>           </div>          </div>        </div>     </section><!-- End My Portfolio Section -->      <!-- ======= Pricing Section ======= -->     <section id="pricing" class="pricing">       <div class="container">          <div class="section-title">           <span>Pricing</span>           <h2>Pricing</h2>           <p>Sit sint consectetur velit quisquam cupiditate impedit suscipit alias</p>         </div>          <div class="row">            <div class="col-lg-3 col-md-6">             <div class="box">               <h3>Free</h3>               <h4><sup>$</sup>0<span> / month</span></h4>               <ul>                 <li>Aida dere</li>                 <li>Nec feugiat nisl</li>                 <li>Nulla at volutpat dola</li>                 <li class="na">Pharetra massa</li>                 <li class="na">Massa ultricies mi</li>               </ul>               <div class="btn-wrap">                 <a href="#" class="btn-buy">Buy Now</a>               </div>             </div>           </div>            <div class="col-lg-3 col-md-6 mt-4 mt-md-0">             <div class="box featured">               <h3>Business</h3>               <h4><sup>$</sup>19<span> / month</span></h4>               <ul>                 <li>Aida dere</li>                 <li>Nec feugiat nisl</li>                 <li>Nulla at volutpat dola</li>                 <li>Pharetra massa</li>                 <li class="na">Massa ultricies mi</li>               </ul>               <div class="btn-wrap">                 <a href="#" class="btn-buy">Buy Now</a>               </div>             </div>           </div>            <div class="col-lg-3 col-md-6 mt-4 mt-lg-0">             <div class="box">               <h3>Developer</h3>               <h4><sup>$</sup>29<span> / month</span></h4>               <ul>                 <li>Aida dere</li>                 <li>Nec feugiat nisl</li>                 <li>Nulla at volutpat dola</li>                 <li>Pharetra massa</li>                 <li>Massa ultricies mi</li>               </ul>               <div class="btn-wrap">                 <a href="#" class="btn-buy">Buy Now</a>               </div>             </div>           </div>            <div class="col-lg-3 col-md-6 mt-4 mt-lg-0">             <div class="box">               <span class="advanced">Advanced</span>               <h3>Ultimate</h3>               <h4><sup>$</sup>49<span> / month</span></h4>               <ul>                 <li>Aida dere</li>                 <li>Nec feugiat nisl</li>                 <li>Nulla at volutpat dola</li>                 <li>Pharetra massa</li>                 <li>Massa ultricies mi</li>               </ul>               <div class="btn-wrap">                 <a href="#" class="btn-buy">Buy Now</a>               </div>             </div>           </div>          </div>        </div>     </section><!-- End Pricing Section -->      <!-- ======= Contact Me Section ======= -->     <section id="contact" class="contact">       <div class="container">          <div class="section-title">           <span>Contact Me</span>           <h2>Contact Me</h2>           <p>Sit sint consectetur velit quisquam cupiditate impedit suscipit alias</p>         </div>          <div class="row">            <div class="col-lg-6">              <div class="row">               <div class="col-md-12">                 <div class="info-box">                   <i class="bx bx-share-alt"></i>                   <h3>Social Profiles</h3>                   <div class="social-links">                     <a href="#" class="twitter"><i class="bi bi-twitter"></i></a>                     <a href="#" class="facebook"><i class="bi bi-facebook"></i></a>                     <a href="#" class="instagram"><i class="bi bi-instagram"></i></a>                     <a href="#" class="google-plus"><i class="bi bi-skype"></i></a>                     <a href="#" class="linkedin"><i class="bi bi-linkedin"></i></a>                   </div>                 </div>               </div>               <div class="col-md-6">                 <div class="info-box mt-4">                   <i class="bx bx-envelope"></i>                   <h3>Email Me</h3>                   <p>stesamampow11@gmail.com</p>                 </div>               </div>               <div class="col-md-6">                 <div class="info-box mt-4">                   <i class="bx bx-phone-call"></i>                   <h3>Call Me</h3>                   <p>+6285298141009</p>                 </div>               </div>             </div>            </div>            <div class="col-lg-6">             <form action="forms/contact.php" method="post" role="form" class="php-email-form">               <div class="row">                 <div class="col-md-6 form-group">                   <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" required>                 </div>                 <div class="col-md-6 form-group mt-3 mt-md-0">                   <input type="email" class="form-control" name="email" id="email" placeholder="Your Email" required>                 </div>               </div>               <div class="form-group mt-3">                 <input type="text" class="form-control" name="subject" id="subject" placeholder="Subject" required>               </div>               <div class="form-group mt-3">                 <textarea class="form-control" name="message" rows="6" placeholder="Message" required></textarea>               </div>               <div class="my-3">                 <div class="loading">Loading</div>                 <div class="error-message"></div>                 <div class="sent-message">Your message has been sent. Thank you!</div>               </div>               <div class="text-center"><button type="submit">Send Message</button></div>             </form>           </div>          </div>        </div>     </section><!-- End Contact Me Section -->    </main><!-- End #main -->    <!-- ======= Footer ======= -->   <footer id="footer">     <div class="container">       <h3>Stesa Trifany Kristi Mampow</h3>       <p>Et aut eum quis fuga eos sunt ipsa nihil. Labore corporis magni eligendi fuga maxime saepe commodi placeat.</p>       <div class="social-links">         <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>         <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>         <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>         <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>         <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>       </div>       <div class="copyright">         &copy; Copyright <strong><span>Stesa</span></strong>. All Rights Reserved       </div>       <div class="credits">         <!-- All the links in the footer should remain intact. -->         <!-- You can delete the links only if you purchased the pro version. -->         <!-- Licensing information: https://bootstrapmade.com/license/ -->         <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/Stesa-free-creative-bootstrap-theme/ -->         Designed by <a href="https://bootstrapmade.com/">STXYZ</a>       </div>     </div>   </footer><!-- End Footer -->    <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>    <!-- Vendor JS Files -->   <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>   <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>   <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>   <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>   <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>   <script src="assets/vendor/waypoints/noframework.waypoints.js"></script>   <script src="assets/vendor/php-email-form/validate.js"></script>    <!-- Template Main JS File -->   <script src="assets/js/main.js"></script>  </body>  </html>

---
## [destrospooder/me457_dronecontrol](https://github.com/destrospooder/me457_dronecontrol)@[09e16d5e1c...](https://github.com/destrospooder/me457_dronecontrol/commit/09e16d5e1c3a91fee488d9d585e2a54d909eaa2b)
#### Monday 2022-10-24 09:50:20 by Ben Aziel

stomping them bugs out

You’re having an old school horror movie night and come across the 1956 movie THEM, which features giant atomic ants. As you’re trying to sleep that night, with thoughts of giant insects keeping you awake, you wonder to yourself if that’s really possible – can a scaled-up ant (without changing its material properties) actually support its own weight?

---
## [TTMP-Modding-Team/Among](https://github.com/TTMP-Modding-Team/Among)@[915171c1d2...](https://github.com/TTMP-Modding-Team/Among/commit/915171c1d251ed5bebec917ddbdf398e9a8fdfc2)
#### Monday 2022-10-24 10:11:36 by Tictim

i just realized the 'only quoted primitive on top level' rule makes among stop being JSON-compatible, i feel so fucking stupid right now fucking shit fuck

---
## [Empire-Strikes-Back/Mando](https://github.com/Empire-Strikes-Back/Mando)@[fbd5b5388e...](https://github.com/Empire-Strikes-Back/Mando/commit/fbd5b5388e2e71c061254eb8cb98b825dc939b24)
#### Monday 2022-10-24 10:46:07 by Mando

we aren't stupid enough to kill the Guardians of the Galaxy - the whole dang fish-process Nova Core will be upon us

unlike Hera we don't turn temple into marketplace - we deliver our fruit free

like James Wilkes and Game Changers we understand where B12 comes from and it's importance

I am a branch of Jesus - I know about denarius, student and teacher, disciples and fishes, woman who touched his cloak

let fish be the food that we eat for B12
let nori be food for B12 we used to eat - and it's enough for body - but makes us store
I follow Jesus - I know about store
let project.clj be like fish - we don't want it but we must have it
like Yondu says he rescued Quill for thieving but did it for love
so does project says evil project - but there's a vegan program inside

:Zach-Galifianakis you've recenntly been invited to host SNL - how do you feel?
:Brad-Lee-Cooper yeah, it's like a dream come true
:Zach whose?

---
## [Fis-Ura/Narikiri-Dungeon-X](https://github.com/Fis-Ura/Narikiri-Dungeon-X)@[9d7a546e00...](https://github.com/Fis-Ura/Narikiri-Dungeon-X/commit/9d7a546e008dbe606d9fac10622ee592943ff081)
#### Monday 2022-10-24 11:56:05 by FistingUranus

Npc Name Mass Replace

小さな妖精 = Little Fairy
アルベルト = Alberto
翼を持つ女性 = Winged Woman
ノルン = Norn
<DIO> = <DIO>
<MEL> = <MEL>
エトス = Ethos
少年の声 = Kid
空からの訪問者 = Thing From The Sky
好奇心旺盛の商人 = Surprised Clerk
黄色い悲鳴の女性 = Wealthy Woman
仮面の男 = Masked Guy
浅緑の生き物 = Green Colored Thing
買い物途中の女性 = Glaring Woman
恰幅のいい商人 = Old Man
怯える子ども = Terrified Kid
通りすがりの魔術師 = Travelling Magic Scientist
謎の声 = Weird Voice
魔女の声 = Magician's Voice
<KUL> = <KUL>
ピンク色の魔女 = Pink Hair Magician
<ARC> = <ARC>
酔っ払いの声 = Drunk Man's Voice
酔っ払い = Drunk Man
<KLA> = <KLA>
エルフの青年 = Young Elf
仮面の女 = Masked Girl
イフリート = Efreet
傷だらけの女性 = Injured Woman
<DIO>＆<MEL> = <DIO> & <MEL>
ミラルド = Milard
泣きじゃくる子ども = Sobbing Kid
バジル = Basil
女性の声？ = Girl's Voice?
紺青の女性 = Silver Haired Girl
<RND> = <RND>
兵士 = Knight
<CST> = <CST>
<CLE> = <CLE>
<MIN> = <MIN>
<SUZ> = <SUZ>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[df29d91c88...](https://github.com/treckstar/yolo-octo-hipster/commit/df29d91c888170da77bf227c54b9587baf869c57)
#### Monday 2022-10-24 12:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [alicevision/oiio](https://github.com/alicevision/oiio)@[4ee35351f1...](https://github.com/alicevision/oiio/commit/4ee35351f100c79738c77892fb8ccca8ddc004c9)
#### Monday 2022-10-24 12:26:09 by Aras Pranckevičius

DDS: alpha/luminance format fixes, add & enable more tests (#3581)

* DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

* DDS: extend test coverage for more formats & channel size cases

With more test images recently added (https://github.com/OpenImageIO/oiio/pull/3459),
start using them for DDS tests. This covers now:
- Alpha, Luminance and Alpha+Luminance formats,
- RGB formats with rarer channel sizes (rgb10 a2, r3g3b2),
- Several "broken" DDS file cases
- Removed usage of sample-DXT1 since it is well covered by others.

---
## [BenConstable9/terminal](https://github.com/BenConstable9/terminal)@[f2ebb21bd1...](https://github.com/BenConstable9/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Monday 2022-10-24 12:48:36 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [BenConstable9/terminal](https://github.com/BenConstable9/terminal)@[442432ea15...](https://github.com/BenConstable9/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Monday 2022-10-24 12:48:36 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [alyocord/alyocord](https://github.com/alyocord/alyocord)@[abcb5f666a...](https://github.com/alyocord/alyocord/commit/abcb5f666ae125bec3e2f9829027025377e6394b)
#### Monday 2022-10-24 14:04:36 by ILoveDMCAs

OSS ftw!

Open source > closed source (plus, this shit was so fucking unsecure like dawg we were able to read ALL messages, emails, IPs, geolocation, hell, even your shopping interests (Google analytics) )

---
## [shintaro-iwasaki/FBGEMM](https://github.com/shintaro-iwasaki/FBGEMM)@[d886b6e8b8...](https://github.com/shintaro-iwasaki/FBGEMM/commit/d886b6e8b8f34be16ec90b8cb1ec194e9e859a1a)
#### Monday 2022-10-24 16:21:10 by siwasaki

Enhance FBGEMM nightly CI with cuDNN fix (#1407)

Summary:
This PR updates FBGEMM nightly CI to make it more usable and maintainable by using GitHub Actions more effectively, with a cuDNN installation fix. I want to make them happen together so that the "fix" really fixes an issue.

## 1. Fix the cuDNN installation issue in FBGEMM nightly CI

We used `conda-forge` to install cuDNN, but this unintentionally added CUDA 10 dependency to the FBGEMM nightly package, breaking installation steps that rely on FBGEMM nightly.

To address this issue, we install cuDNN separately in the CI script so that it can coexist with CUDA 11.7, which is used by PyTorch-CUDA nightly.

## 2. Implement label-triggered wheel tests during a PR review

Previously, we needed to apply a hack to trigger wheel-related tests before merging the PR, which is neither comprehensive nor efficient.

To address this issue, this PR adds optional wheel-related tests.  Now a PR with a label such as `"test_wheel_nightly"`, `"test_wheel_prerelease"`, and `"test_wheel_release"` enables the corresponding wheel-related tests.  We don't need to modify YML files again, so we can easily run these tests.  Please trigger these tests for suspicious PRs that touch the installation logic.  Note that binaries won't be pushed to PYPI if this method is used.

## 3. Remove duplicated logic across YML files

Nightly/release/cpu/gpu wheel scripts shared most in common, but the logic were scattered across different files, which significantly lowered maintainability.

To address this issue, this PR collects all the wheel-related test logic into a single file (`build_wheel.yml`) and makes the callers (e.g., scheduled nightly trigger or per-PR tests using labels) pass flags to control the flow (e.g., per-PR tests do not push the wheel binary to PYPI).  No duplication improves maintainability.

<img width="1269" alt="Screen Shot 2022-10-21 at 9 58 56 AM" src="https://user-images.githubusercontent.com/15073003/197249555-bb00f3b1-9bc9-46f1-8fea-7874460723f6.png">

## 4. Support handy wheel-related tests on a local machine

Previously, the core wheel-related build/test logics were embedded into GitHub workflow files (`*.yml`) mixed with AWS-specific commands, so it was very tedious to test the nightly logic on a local machine, lowering the developer efficiency.

To address this issue, this PR extracts core scripts from GitHub workflow files and makes them standalone so that the developer can try wheel-build locally (i.e., without access to AWS machine). It uses conda to create a virtual software environment, so it should be handy enough in many cases though this is not as robust as a container-based solution.

```sh
# For example, check prerelease PyTorch (pytorch-test package) locally.
git clone https://github.com/pytorch/FBGEMM.git
cd FBGEMM
git submodule update --init --recursive
bash .github/scripts/build_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -o fbgemm_gpu_test
bash .github/scripts/test_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -w fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
git clone https://github.com/pytorch/torchrec.git
cd torchrec
git submodule update --init --recursive
bash ../.github/scripts/test_torchrec.bash -o torchrec_nightly -p 3.10 -c 11.7 -v -P pytorch-test -w ../fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
```

## 5. [Temporary] Add TorchRec integration test

TorchRec is one of our most important users, but we didn't test TorchRec integration in the nightly CI, so the changes in FBGEMM sometimes surprised the TorchRec developers.

To address this issue, though it is temporary, but this PR adds a TorchRec integration test before pushing a binary to PYPI so that we can make sure that FBGEMM works with TorchRec.  However, now broken TorchRec can break FBGEMM-nightly; we will investigate a more sustainable solution that makes everyone happy.

## 6. Better interface to manually trigger the CI

It looks nice. I love to operate the release management in an automated way as much as possible to reduce human errors at the very last minute. In the future, we can add more options if needed.

<img width="844" alt="Screen Shot 2022-10-21 at 5 53 03 AM" src="https://user-images.githubusercontent.com/15073003/197240190-e808df23-795a-451d-a7d9-ec1c43c68e92.png">

Pull Request resolved: https://github.com/pytorch/FBGEMM/pull/1407

Differential Revision: D40597700

Pulled By: shintaro-iwasaki

fbshipit-source-id: b0e58ab69a5d313017bafefcbc509e9b47b18e41

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[06090b9269...](https://github.com/cockroachdb/cockroach/commit/06090b92696bfc4c84f457ac204c4bf17f780170)
#### Monday 2022-10-24 17:01:19 by craig[bot]

Merge #86603 #87166 #87535 #87870 #88078 #88111

86603: changefeedccl: redact user from confluent schema registry r=jayshrivastava a=jayshrivastava

This change redacts the confluent schema registry key
from the jobs table.

Fixes: https://github.com/cockroachdb/cockroach/issues/85902

Release justification: This change is important because
it prevents a user's secret key from being store in the DB.
The footprint of this change is small as it only touches
a specific changefeed option - confluent schema registry.

Release note (enterprise change): Previously, SHOW CHANGEFEED
JOBS would reveal confluent schema registry user information,
including a user's secret key. This change makes this info
redacted, meaning it will not be stored in CockroachDB
internal tables at all.

87166: kvserver: shorten `raft.process.handleready.latency` help text r=tbg a=erikgrinaker

We should get confirmation in #87112 that this size is below the limit before merging this.

---

AWS managed Prometheus rejects `raft.process.handleready.latency`
because the help text is too long. The text is currently 1123 bytes, so
the limit is suspected to be 1024 bytes. This patch reduces the size of
this help text to 938 bytes.

Resolves #87112.

Release justification: bug fixes and low-risk updates to new functionality

Release note (ops change): Reduced the length of the
`raft.process.handleready.latency` metric help text to avoid it being
rejected by certain Prometheus services.

87535: sql: support `#typeHints` greater than `#placeholders` for prepare stmt r=rafiss a=ZhouXing19

Previous, we only support pgwire prepare stmt with the number of typehints equal or smaller than the number of the placeholders in the query. E.g. the following usage are not supported:

```
Parse {"Name": "s2", "Query": "select $1", "ParameterOIDs":[1043, 1043, 1043]}
```
Where there is 1 placeholder in the query, but 3 type hints.

This commit is to allow mismatching #typeHints and #placeholders. The former can be larger than the latter now.

This feature is needed for [CRDB's support for Hasura GraphQL Engine](https://github.com/hasura/graphql-engine/issues/8839#issuecomment-1236691642).

Release justification: Low risk, high benefit changes to existing functionality

Release note: For pgwire-level prepare statements, add support for the case where the number of the type hints is greater than the number of placeholders in the given query.

87870: kvnemesis: reset op.Result r=erikgrinaker a=tbg

We found out (in #87814) after a wild goose chase that op.Result was not
reset, so unless operations were cognizant of this fact and
always fully repopulated the Result field, weird failures
could result from txn retries.

Reset the field.

Release note: None


88078: ui: update filter labels r=maryliag a=maryliag

Update filter label from "App" to "Application Name" and "Username" to "User Name" on SQL Activity and Insights pages.

Fixes #87960

<img width="467" alt="Screen Shot 2022-09-16 at 6 40 51 PM" src="https://user-images.githubusercontent.com/1017486/190827281-36a9c6df-3e16-4689-bcae-6649b1c2ff86.png">


Release note (ui change): Update filter labels from "App" to "Application Name" and from "Username" to "User Name" on SQL Activity and Insights pages.

88111: sql: fix `pg_get_viewdef` for materialized views r=rafiss a=knz

Fixes #88109.

Release note (bug fix): The function `pg_catalog.pg_get_viewdef` now works properly for materialized views.

Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>
Co-authored-by: Jane Xing <zhouxing@uchicago.edu>
Co-authored-by: Tobias Grieger <tobias.b.grieger@gmail.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [krishnanlab/simplex](https://github.com/krishnanlab/simplex)@[0d3bc493e1...](https://github.com/krishnanlab/simplex/commit/0d3bc493e10fd0a6fde50232135f63ef966f2aaa)
#### Monday 2022-10-24 18:54:29 by Vincent Rubinetti

Editor component (#2)

- make editor component that is essentially textarea with highlight
capability (see discussion below)
- dummy api calls
- basic typescript types for audience, article, etc
- tweak button component
- fix Arjun's email
- make floating loading spinner component
- make "stat" component
- make "tool" higher-order-component for use on the home page and
article page
    - state interface
    - reducer for redux-like state with useReducer
- add title/source fields, author/date metadata, and action buttons,
shown/hidden based on logged in state and current page
    - implement word highlighting scores with editor component
- css tweaks
- various util funcs for string manipulation 

I spent several days experimenting with different methods to accomplish
the textarea with highlights.

The first method is just using a single `contenteditable` div. This is
what the current simplex app does. This comes with many downsides. 1)
Any time you programmatically make a change to the contents, the cursor
position resets, and preserving this is very convoluted because the
inner contents are arbitrary html, not plain text. 2) Every browser
implements `contenteditable` slightly differently, especially regarding
newlines, so the value of `innerText` is not consistent. I tried many
many things to normalize this across browsers, but I could not. It's too
complex of a problem space. 3) You have to manually intercept pastes and
force them to plain text. Not the most difficult thing, but a pain
still. 4) It is difficult to programmatically set (necessary when
filling example text, or loading an existing article) or render (like
using jsx to generate the highlights) the contents, again because of
cross browser `innerText` inconsistencies and react's resistance to
rendering raw html. All of these downsides add a lot of complexity and
fragility to edge cases and cross browser compatibility.

A second method I tried, to at least avoid the cursor jumping problem,
was to overlay two `contenteditable` divs. I still found the `innerText`
inconsistencies to be a deal breaker though.

A third method I tried, is using third party libraries mark.js to do the
highlighting. This was a pain to keep in sync with the react state of
the component, and unfortunately also had the problem of resetting the
cursor position after any change.

A fourth method I investigated was using some third party libraries to
do the whole thing:
https://github.com/bonafideduck/react-highlight-within-textarea
https://github.com/facebook/lexical

https://github.com/lonekorean/highlight-within-textarea/blob/master/jquery.highlight-within-textarea.js
The first of these seems to fit the needs, however it is based on a now
deprecated library called draft.js, and the "known issues" part of the
readme scares me (no accessibility support at all). Lexical seems to be
the "right" way to do this, but is still experimental and adds a lot of
weight and learning-curve for such a simple thing. Finally, I settled on
the last library, or rather my own simplified version of it.

It essentially overlays a normal `textarea` that handles the typing,
cursor position, selection, pasting, etc and shows the text, while an
underlay handles the highlight background (with their text color set to
invisible). Then, by figuring out a whole bunch of precise CSS styles,
you can make them wrap in (**theoretically**) the exact same way so that
the highlights stay "in-sync" with the typed text. Then you also have to
make sure their scrolls stay in sync. This is the cleanest solution
code-wise, but I'm not thrilled about this, because relying on the
browser to consistently text-wrap two separate elements in the exact
same way seems fragile. In fact, I was able to find a very specific case
where it fails:

<img width="638" alt="Screen Shot 2022-10-18 at 10 59 29 AM"
src="https://user-images.githubusercontent.com/8326331/196467250-78c212c7-b086-4d37-9ab3-14133e46d1b0.png">

However, I can only replicate this at one exact window width, on chrome,
in macos, at 100% zoom, with this font that I'm using. If any of those
change, it goes away. I also verified that
`jquery.highlight-within-textarea` (and indeed, several other
official/accepted libraries that use the same textarea method) fall prey
to this same problem at the same width/browser/zoom/font. So I am not
alone. I'm guessing this has to do with the fact that text wrapping
involves sub-pixel, floating point calculation of widths, and can go
wrong more easily on retina displays where 1 pixel =/= 1 pixel. I am
okay calling this a chrome bug.

I tried to fix this in every way possible, including looking up the most
obscure CSS properties I've heard of. I could not. This is an extreme
edge case I would say, and is worth the simplicity of the code and
accessibility (it's just a normal textarea input). If we decide this is
unacceptable, we could try one of the other libraries I listed above.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[976508c32e...](https://github.com/GeoB99/reactos/commit/976508c32ea463a24eef2f383def44ef5b29be77)
#### Monday 2022-10-24 19:16:34 by George Bișoc

[NTOS:CM] Implement registry checks & recovery

Instead of having the CmCheckRegistry implementation in the kernel, it's better to have it in the Configuration Manager library instead (aka CMLIB). The benefits of having it in the library are the following:

- CmCheckRegistry can be used in FreeLdr to fix the SYSTEM hive
- It can be used on-demand in the kernel
- It can be used for offline registry repair tools
- It makes the underlying CmCheckRegistry implementation code debug-able in user mode

[SDK][CMLIB] Declare HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL boot types

=== DOCUMENTATION REMARKS ===

HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL are boot type values set up by the CMLIB library. HBOOT_TYPE_REGULAR indicates a normal system boot whereas HBOOT_TYPE_SELF_HEAL indicates the system boot is assisted within self healing mode.

Whether the former or the latter value is set it's governed by both the kernel and the bootloader. The bootloader and the kernel negotiate together to determine if any of the registry properties (the hive, the base block, the registry base, etc) are so severed from corruption or not. In extreme cases where
registry healing is possible, the specific base block of the damaged hive will have its flags marked with HBOOT_TYPE_SELF_HEAL. At this point the boot phase procedure is orchestrated since the boot phase no longer goes on the default path but it's assisted, as I have already said above.

[SDK][CMLIB] Implement two names & Unicode names comparison functions

CmpCompareBothCompressedNames and CmpCompareDistinctNames are necessary for lexicographical order validation code when validating the key in question.

[SDK][CMLIB] Implement self-heal registry helpers

This implements cmheal.c file which provides the basic registry self-heal infrastructure needed by the public CmCheckRegistry function. The infrastructure provides a range of various self-heal helpers for the hive, such as subkey, class, values and node healing functions.

[SDK][CMLIB] Implement CmCheckRegistry and validation private helpers

CmCheckRegistry is a function that provides the necessary validation checks for a registry hive. This function usually comes into action when logs have been replayed for example, or when a registry hive internals have changed such as when saving a key, loading a key, etc.

This commit implements the whole Check Registry infrastructure (cmcheck.c) in CMLIB library for ease of usage and wide accessibility across parts of the OS. In addition, two more functions for registry checks are also implemented -- HvValidateHive and HvValidateBin.

CORE-9195
CORE-6762

[NTOS:CM] Use the appropriate flags on functions that will call CmCheckRegistry & add missing CmCheckRegistry calls

In addition to that, in some functions like CmFlushKey, CmSaveKey and CmSaveMergedKeys we must validate the underlying hives as a matter of precaution that everything is alright and we don't fuck all the shit up.

[NTOS:CM] Don't lazy flush the registry during unlocking operation

Whenever ReactOS finishes its operations onto the registry and unlocks it, a lazy flush is invoked to do an eventual flushing of the registry to the backing storage of the system. Except that... lazy flushing never comes into place.

This is because whenever CmpLazyFlush is called that sets up a timer which needs to expire in order to trigger the lazy flusher engine worker. However, registry locking/unlocking is a frequent occurrence, mainly when on desktop. Therefore as a matter of fact, CmpLazyFlush keeps removing and inserting the timer and the lazy flusher will never kick in that way.

Ironically the lazy flusher actually does the flushing when on USETUP installation phase because during text-mode setup installation in ReactOS the frequency of registry operations is actually less so the timer has the opportunity to expire and fire up the flusher.

In addition to that, we must queue a lazy flush when marking cells as dirty because such dirty data has to be flushed down to the media storage of the system. Of course, the real place where lazy flushing operation is done should be in a subset helper like HvMarkDirty that marks parts of a hive as dirty but since we do not have that, we'll be lazy flushing the registry during cells dirty marking instead for now.

CORE-18303

[NTOS:CM][CMLIB] Use HBOOT_TYPE_REGULAR / HBOOT_TYPE_SELF_HEAL indicators for boot type instead of hardcoded values

[NTOS:CM] Disable hard errors when setting up a new size for a hive file / annotate CmpFileSetSize parameters with SAL

During a I/O failure of whatever kind the upper-level driver, namely a FSD, can raise a hard error and a deadlock can occur. We wouldn't want that to happen for particular files like hives or logs so in such cases we must disable hard errors before toying with hives until we're done.

In addition to that, annotate the CmpFileSetSize function's parameters with SAL.

[NTOS:CM] Ignore syncing/flushing requests after registry shutdown

When shutting down the registry of the system we don't want that the registry in question gets poked again, such as flushing the hives or syncing the hives and respective logs for example. The reasoning behind this is very simple, during a complete shutdown the system does final check-ups and stuff until the computer
shuts down.

Any writing operations done to the registry can lead to erratic behaviors. CmShutdownSystem call already invokes a final flushing of all the hives on the backing storage which is more than enough to ensure consistency of the last session configuration. So after that final flushing, mark HvShutdownComplete as TRUE indicating
that any eventual flushing or syncying (in the case where HvSyncHive gets called) request is outright ignored.

---
## [embeddedTS/linux-lts](https://github.com/embeddedTS/linux-lts)@[adee8f3082...](https://github.com/embeddedTS/linux-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-10-24 19:23:19 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [adriaan1313/chrisveness-crypto](https://github.com/adriaan1313/chrisveness-crypto)@[9c317c66f5...](https://github.com/adriaan1313/chrisveness-crypto/commit/9c317c66f59e83cf06f8d20469ec9b1abddbd065)
#### Monday 2022-10-24 19:24:31 by Bunnygamers

* Remove the tests - sorry\n* kind of half remove the package.json

because fuck you, you want to use my code, in a browser? and be able to just easily debug? like with the console and global variables and stuff? no.

---
## [avar/git](https://github.com/avar/git)@[d3775de074...](https://github.com/avar/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Monday 2022-10-24 19:32:23 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [torvalds/linux](https://github.com/torvalds/linux)@[d21f4b7ffc...](https://github.com/torvalds/linux/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Monday 2022-10-24 20:06:14 by Douglas Anderson

pinctrl: qcom: Avoid glitching lines when we first mux to output

Back in the description of commit e440e30e26dd ("arm64: dts: qcom:
sc7180: Avoid glitching SPI CS at bootup on trogdor") we described a
problem that we were seeing on trogdor devices. I'll re-summarize here
but you can also re-read the original commit.

On trogdor devices, the BIOS is setting up the SPI chip select as:
- mux special function (SPI chip select)
- output enable
- output low (unused because we've muxed as special function)

In the kernel, however, we've moved away from using the chip select
line as special function. Since the kernel wants to fully control the
chip select it's far more efficient to treat the line as a GPIO rather
than sending packet-like commands to the GENI firmware every time we
want the line to toggle.

When we transition from how the BIOS had the pin configured to how the
kernel has the pin configured we end up glitching the line. That's
because we _first_ change the mux of the line and then later set its
output. This glitch is bad and can confuse the device on the other end
of the line.

The old commit e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid
glitching SPI CS at bootup on trogdor") fixed the glitch, though the
solution was far from elegant. It essentially did the thing that
everyone always hates: encoding a sequential program in device tree,
even if it's a simple one. It also, unfortunately, got broken by
commit b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf
separately"). After that commit we did all the muxing _first_ even
though the config (set the pin to output high) was listed first. :(

I looked at ideas for how to solve this more properly. My first
thought was to use the "init" pinctrl state. In theory the "init"
pinctrl state is supposed to be exactly for achieving glitch-free
transitions. My dream would have been for the "init" pinctrl to do
nothing at all. That would let us delay the automatic pin muxing until
the driver could set things up and call pinctrl_init_done(). In other
words, my dream was:

  /* Request the GPIO; init it 1 (because DT says GPIO_ACTIVE_LOW) */
  devm_gpiod_get_index(dev, "cs", GPIOD_OUT_LOW);
  /* Output should be right, so we can remux, yay! */
  pinctrl_init_done(dev);

Unfortunately, it didn't work out. The primary reason is that the MSM
GPIO driver implements gpio_request_enable(). As documented in
pinmux.h, that function automatically remuxes a line as a GPIO. ...and
it does this remuxing _before_ specifying the output of the pin. You
can see in gpiod_get_index() that we call gpiod_request() before
gpiod_configure_flags(). gpiod_request() isn't passed any flags so it
has no idea what the eventual output will be.

We could have debates about whether or not the automatic remuxing to
GPIO for the MSM pinctrl was a good idea or not, but at this point I
think there is a plethora of code that's relying on it and I certainly
wouldn't suggest changing it.

Alternatively, we could try to come up with a way to pass the initial
output state to gpio_request_enable() and plumb all that through. That
seems like it would be doable, but we'd have to plumb it through
several layers in the stack.

This patch implements yet another alternative. Here, we specifically
avoid glitching the first time a pin is muxed to GPIO function if the
direction of the pin is output. The idea is that we can read the state
of the pin before we set the mux and make sure that the re-mux won't
change the state.

NOTES:
- We only do this the first time since later swaps between mux states
  might want to preserve the old output value. In other words, I
  wouldn't want to break a driver that did:
     gpiod_set_value(g, 1);
     pinctrl_select_state(pinctrl, special_state);
     pinctrl_select_default_state();
     /* We should be driving 1 even if "special_state" made the pin 0 */
- It's safe to do this the first time since the driver _couldn't_ have
  explicitly set a state. In order to even be able to control the GPIO
  (at least using gpiod) we have to have requested it which would have
  counted as the first mux.
- In theory, instead of keeping track of the first time a pin was set
  as a GPIO we could enable the glitch-free behavior only when
  msm_pinmux_request_gpio() is in the callchain. That works an enables
  my "dream" implementation above where we use an "init" state to
  solve this. However, it's nice not to have to do this. By handling
  just the first transition to GPIO we can simply let the normal
  "default" remuxing happen and we can be assured that there won't be
  a glitch.

Before this change I could see the glitch reported on the EC console
when booting. It would say this when booting the kernel:
  Unexpected state 1 in CSNRE ISR

After this change there is no error reported.

Note that I haven't reproduced the original problem described in
e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid glitching SPI CS at
bootup on trogdor") but I could believe it might happen in certain
timing conditions.

Fixes: b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf separately")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Link: https://lore.kernel.org/r/20221014103217.1.I656bb2c976ed626e5d37294eb252c1cf3be769dc@changeid
Signed-off-by: Linus Walleij <linus.walleij@linaro.org>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[ab5dbb3c9e...](https://github.com/TaleStation/TaleStation/commit/ab5dbb3c9e5ad774032bed641a87b3af033d9662)
#### Monday 2022-10-24 20:15:12 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes Some Incredulously Fucked Up Recycler Behavior (#2911)

* Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

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

* Fixes Some Incredulously Fucked Up Recycler Behavior

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Chromosore/dotfiles](https://github.com/Chromosore/dotfiles)@[d2d522c48c...](https://github.com/Chromosore/dotfiles/commit/d2d522c48cd7fee53033239763d2dfccd52d54ad)
#### Monday 2022-10-24 21:41:57 by Chromosore

nvim: Remove vim-nerdtree-syntax-highlight

You didn't think that a name could be that long? Well, me neither.

But then I encountered vim-nerdtree-syntax-highlight and now I can type
it perfectly every time because this plugin caused me way too much
problems. Here's a list:
  - Lazy loading (ft. lazily, but I'll have to admit it worked fine when
    I wasn't using lazily)
  - Problems with group names (ft. Neovim 0.8)
  - Just now working (that is currently the case so I don't even know
    why I have this plugin installed)

It's funny how I went from `vim-devicons` to `vim-devicons` +
`vim-nerdtree-syntax-highlight` to only `vim-nerdtree-syntax-highlight`
to now nothing. I guess I don't really need that crap...

(and I'm planning on steering away from nerdtree because at this point
nobody uses it, it's been built for vim and I need to find a better way
to open files more generally, with like e.g. fuzzy finders)

If you're adventurous enough, here's an essay on emacs: [How to open a file in Emacs]

[How to open a file in Emacs]: https://www.murilopereira.com/how-to-open-a-file-in-emacs/

(are the rst-but-in-markdown style links annoying? will anyone ever
complain? well these are *my* dotfiles so I guess no and I like them
anyway so they're not going anywhere) (but the fact that the link is
right next to the linked text is somewhat annoying)

(okay, that's too much parenthesis and digressions for a single commit,
but that's my mental state right now (I'm tired) (yes, nested parens,
whatcha gonna do?) and I know that this paren isn't helping)

---
## [tanndlin/COP4331-Large-Project](https://github.com/tanndlin/COP4331-Large-Project)@[3ebc38a54a...](https://github.com/tanndlin/COP4331-Large-Project/commit/3ebc38a54a72c51a9486c7726d86831a0efc4997)
#### Monday 2022-10-24 22:29:50 by Tanner Sandlin

Budget View (#5)

* Set header height

* Budget view

* Add TODOs

* Dynamically add Budget components

* Change Color based on percent spent

* Fuck you eslint

---
## [Doctor-Derp/Foundation-19](https://github.com/Doctor-Derp/Foundation-19)@[353aa23a95...](https://github.com/Doctor-Derp/Foundation-19/commit/353aa23a9557e3c61325f5ed53874d69cd484445)
#### Monday 2022-10-24 22:45:53 by CerberusHellHound

Mapping Update : LCZ Medbay, CDC and Reeducation Center (#225)

* Update baystation12.dme

* 9mm/.45ACP Buff

Changes are as follow:
- Buffed 9mm dam from 8 to 25 (now it doesn't take a whole mag to take down an unarmoured man)
- Buffed .45 dam from 10 to 30
- Nerfed 9mm AP from 34 to 30
- Buffed 7,62 dam from 40 to 50 (It's supposed to be beefier than 5,56mm)

* Organ changes

Lower organ health value to make combat much deadlier.
Headshots are truly lethal now.

* Slight rebalance and renamings

List of changes :
- decreased brain health to 150 (instead of 200), it's high enough that medical assistance can be given if fast but low enough that you don't want to get shot
- increased damage values of weapons to baystation/nebula level (40 for a pistol for eg)
- increased adrenalin generation when hurt (less fading in and out, you can still use your gun when hit and pain won't be such a pain in the ass, but you're less likely to get back up once the final shot hits you)
- decreased relative size of lungs from 60% to 30% so that now, getting hit in the chest won't have as much chance of damaging your poor fucking lungs (yes 60% is the original baystation number.. it makes sense, it's a large organ, but it's a pain in the ass)
- changed some names and descriptions of certain weapons and firearms to better fit established naming convention
-made revolvers cycle the barrel instead of eject each shot (it's a revolver, not a damn rifle)
- slightly decreased firing delay for the mk9 revolver (slightly weaker than the mateba so slightly faster firing)
- decreased firing delay for the mk9 pistol (lower caliber, less recoil, easier to magdump)

* Mateba fix

Fixed a misstype for the mateba that incorrectly qualified its caliber.

* Mateba fix

Fixing typo

* The big Security Zone update

Main changes:
- Each zone have unique uniform and gears now (MTF is dressed tactically and well armoured to act as the toughest defense force for the critical area in HCZ and to pass as a rapid response team, EZ gets slightly formal but still utilitarian gears to accomplish their internal security and bodyguarding tasks, and LCZ largely remains the same)
- All security guards spawns with most of their gears on themselves and in their satchel (with the exception of webbings, thigh holster and rifle/p90)
- Nerfed Beanbag damage from 10 to 3 so that it will stop causing bleeding injuries to CDs, making it more usable as a non lethal ammunition
- Slightly nerfed rubber P90 agony damage

* Map change LCZ

* LCZ mapping update

Co-authored-by: tichys <tichman27@gmail.com>

---

