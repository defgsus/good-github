## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-28](docs/good-messages/2022/2022-03-28.md)


1,832,917 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,832,917 were push events containing 2,927,945 commit messages that amount to 216,769,844 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c8ef62c1fb...](https://github.com/tgstation/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Monday 2022-03-28 00:02:21 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [Roundtable-Hold/tracker](https://github.com/Roundtable-Hold/tracker)@[3ce17071fd...](https://github.com/Roundtable-Hold/tracker/commit/3ce17071fdf99a76f66850adce076b8b66d1e65a)
#### Monday 2022-03-28 00:51:43 by Olivia

NPCs, Bosses, and a Golden Seed (#7)

* Update NPC questlines in index.html

Added Rogier's questline. Expanded upon Roderika and Hewg's, and corrected the assertation that you get two Golden Seeds from her (you can only get one). Answered the question about the Pureblood Knight's Medal under Varre's.

* Update NPC quests in quests.yaml

Added Rogier to quests.yaml. Updated Roderika, Hewg, and Varre. index.html is as it was.

* Update quests.yaml

Added links to every character. Removed the quotation marks I added in a line in Varre's quest that were creating a bug.

* Update quests.yaml

Added questlines for Fia, D, and D's twin. Made the requested tweaks to checkbox numbering to preserve continuity for those already using the guide.

* Update index.html

Ran generate.bat to update the index file. Also fixed a typo in D's name first.

* Updates to flasks and bosses

Added one missing golden seed in Stormveil. Added two missing bosses, Bloodhound Knight and Putrid Tree Spirit. Fixed some typos on the bosses page (misspellings + references to Erdtree Burial Watchdogs as Burial Tree Watchdogs)

* Added Irina and Edgar

Added two new NPC quests, Irina and Edgar. Generated the new index.html file for these changes and the changes from the prior commit regarding a golden seed and bosses.

* Fixed merge conflicts

Co-authored-by: Ben Lambeth <accounts@lambethben.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e58fb506ef...](https://github.com/timothymtorres/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Monday 2022-03-28 01:00:14 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [project-4-detective-pokemon/project-4](https://github.com/project-4-detective-pokemon/project-4)@[c11607f505...](https://github.com/project-4-detective-pokemon/project-4/commit/c11607f5050240626f6809fb963864a51cabd3b4)
#### Monday 2022-03-28 02:18:31 by Maxine

styling! i can't remember what else holy shit. brain melted.

---
## [cfike000/codeWars](https://github.com/cfike000/codeWars)@[2029b29168...](https://github.com/cfike000/codeWars/commit/2029b291689dad1cea230822a11df4f50a5b99a5)
#### Monday 2022-03-28 03:31:56 by Carl E Fike

I love you Kata

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

---
## [benarji7/android_kernel_xiaomi_msm8956](https://github.com/benarji7/android_kernel_xiaomi_msm8956)@[5bee127faa...](https://github.com/benarji7/android_kernel_xiaomi_msm8956/commit/5bee127faa9c6d1b69449683f6d6388756874f05)
#### Monday 2022-03-28 04:40:28 by Christian Brauner

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
        kernel/signal.c - struct kernel_siginfo does not exist in 4.9
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.9 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. exclude kill() changes to avoid struct kernel_siginfo usage
 4. exclude copy_siginfo_from_user_any() to avoid struct kernel_siginfo usage
 5. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 6. replaced COND_SYSCALL with cond_syscall
 7. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 8. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I00f1c618b2e9dbafae4d4113ad4d8a1a44b6957c
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [blessedcoolant/lama-cleaner](https://github.com/blessedcoolant/lama-cleaner)@[eea85b834e...](https://github.com/blessedcoolant/lama-cleaner/commit/eea85b834eee527f3a05fca9410e671c935603b2)
#### Monday 2022-03-28 04:52:38 by blessedcoolant

Complete GUI Refactor

This patch brings in a massive number of changes to the frontend of the application. Please feel free to discuss the proposed changes with me at any time.

Implemented Recoil as a state management system.
Why Recoil? It is a robust library built by developers at Facebook for state management. It has an  extremely simple API for implementation that is in sync with React syntax compared to any other state management system out there and works amazingly well. While the official release status is beta as it becomes fully featured, the library is already used in various systems at Facebook and is very stable for the use cases of this application.

Why global state management? One of the major issues I saw with the current file structure is that there is minimal code splitting and it makes further development of the frontend a cumbersome task. I have broken down the frontend into various easy to access components isolating the GUI from the logic. To avoid prop drilling, we need global state management to handle the necessary tasks. This will also facilitate the addition of any new features greatly.

Code Splitting. Majority of the components that can be isolated in the application have now been done so.
All New Custom CSS & Removal of Tailwind
While Tailwind is a great way to deploy beautiful interfaces quickly, anyone trying to stylize the application further needs to be familiar with Tailwind which makes it harder for more people to work on it. Not to mention, I am not a particular fan of flooding JSX elements with inline CSS classes. That makes reading the code extremely hard and bloats up component code drastically.

As a replacement to Tailwind, I implemented a custom styling system using SCSS as a developer dependency.

In the new system, all the general and shared styles are in the styles folder and all the component styles are in the same folder as the component for easy access.The _index.scss file now acts as a central import for every other stylesheet that needs to be loaded.

What Changed?
The entire application looks and feels like the current implementation with minimal changes.
The green (#bdff01) highlight used in the application has now been changed to a bright yellow (rgb(255, 190, 0)) because I felt it better suited the new Dark Mode (see below).
The swipe bar for comparing before and after images has now been removed and instead the comparison is a smooth fade effect. I felt this was better to analyze image changes rather than a swiper. // Can add the swipe back if needed.

Dark Mode
A brand new Dark Mode has been added for the application. Users can enable and disable by tapping the button in the header or by using the Shift + D hotkey.

Other Misc New Features
When the editor image is now zoomed out to its default size, the image now also gets centered back.

TODO
The currently used react-zoom-pinch-pan module is not mobile friendly. It does not allow brush strokes. Need to figure out a way to fix this.
Further optimization of the frontend code with better code splitting and performance.
When using the LaMa model, the first stroke has a delayed response from the backend but the ones that follow are almost immediate. I believe this is happening because of the initialization of the model on the first stroke. I wonder if either of us can look at it and see if this can somehow be preloaded so the user experience is smooth from the first stroke.
Enable threading for the desktop application mode so flaskwebgui does not block the main applications Python console.

---
## [YXTang/swot](https://github.com/YXTang/swot)@[e056596ad3...](https://github.com/YXTang/swot/commit/e056596ad3d5ef0ff2870fba2190aa7443441341)
#### Monday 2022-03-28 06:07:58 by YXTang

Add CEA-IGP 

The Institute of Geophysics, China Earthquake Administration (IGPCEA for short) is a national scientific research institution of public welfare with a 70-year glorious history. IGPCEA was formerly known as the Institute of Geophysics of Chinese Academy of Sciences, and was transferred to the China Seismological Bureau (later renamed China Earthquake Administration) in 1971. Since this integration, IGPCEA has been one of the most well-known geoscience research institutions in China and important part of the national innovation system of earthquake preparedness and disaster mitigation.

IGPCEA has been dedicated mainly into research fields of earthquake occurrence mechanism and earthquake disaster forecasting and engineering application, aiming at basic and applied research related to Geophysics. IGPCEA has been strategically focused on seismology, physics of the Earth’s interior, geomagnetism, engineering seismology and two bases of observation and experiment. While carrying out scientific research, IGPCEA not only strengthens prospective basic research, leads major breakthroughs in original achievements in earthquake-related fields, but also highlight the key common technology of earthquake observation, forecasting and early warning, earthquake resistant engineering and disaster assessment, so as to serve the development requirements of earthquake preparedness and disaster mitigation. In recent years, IGPCEA has focused on the "Transparent Crust" project of the National Earthquake Science and Technology Innovation Project and has taken the lead in the construction of China Seismic Experimental Site.

IGPCEA houses 7 research divisions, a Seismic Data Center, a CEA Key Laboratory of Focal Physics, a Center of Engineering Technology on Disaster Prevention, a Center of Science and Technical Information, and 8 offices of management and service. IGPCEA has led the construction of the Beijing Baijiatuan National Earth Observatory, which was accredited as ‘National Observation and Research Station’ and ‘International Science and Technology Cooperation Base’ by the Ministry of Science and Technology of China (MOST). IGPCEA undertakes work of China Committee of the International Association of Seismology and Physics of the Earth's Interior (IASPEI) and Secretariat of the Asian Seismological Commission, providing strong technical and cooperative support for regional and even international geophysics and seismology research.

IGPCEA has a total of 274 staff members, including 4 academicians of the Chinese Academy of Sciences, 1 academician of the Chinese Academy of Engineering, 3 academicians of the Third World Academy of Sciences and 142 senior professionals. Among them, 61 professionals are supported by the "State Council Special Allowance", 6 young and middle-aged experts with outstanding contributions at the national level, 8 candidates selected for the "National Talent Project", 1 professional has received the title of "National Ten Thousand Talents Plan" and 1 research group is supported by the "National Creative Talent Project” of the MOST. In 2015, IGPCEA was selected as an "Innovative Talent Training Demonstration Base" by the MOST. Additionally, many professionals have won international reputations for IGPCEA with their contributions as president, secretary-general and other important position in international academic organizations. For instance, academician Chen Yun-tai has achieved International Award of American Geophysical Union (AGU) in 2010 and Axford Award of Asia Oceania Geosciences Society (AOGS) in 2013 and 2 professionals have been honored with the International Union of Geodesy and Geophysics (IUGG) Fellow for the first time.

IGPCEA has a post-graduate education system for Master's and PhD students, as well as a postdoctoral research system, which was one of the earliest to be authorized in China. IGPCEA currently has more than 190 postgraduates, 45 doctoral supervisors and 42 master supervisors. IGPCEA has been strengthening international exchanges and cooperation with many famous universities and research institutes throughout the world, and attaching importance to the joint training of doctoral students and young scientific and technological personnel.

In the past decade, IGPCEA has undertaken more than 20 national projects, including the National Key Research and Development Plan, Major Subject and Major Project of the National Natural Science Foundation of China, the National Social Science Foundation of China, the International Cooperation Program of the MOST, the National Major Scientific Equipment Development Project, National Basic Research Program of China (973 Program) and National Science and Technology Support Program. IGPCEA leads projects design, organization and implementation as legal entity of the "ChinArray Project" and "National Earthquake Social Service Project". IGPCEA has conducted research on the exploration and imaging of the mainland and sea crust’s fine structure, active source monitoring for regional scale medium changes, regional seismic travel-time tables and precise positioning of earthquake and the Geomagnetic Reference Field in China.

Through multi-disciplinary cross research, IGPCEA has made great scientific and technological achievements with great influence at home and abroad in the fields of seismic zoning map in China, key techniques on seismic zoning in the sea area, rapid determination of source parameters, ground motion determination for major engineering design and seismic safety of nuclear plants and realized the transformation service of scientific and technological achievements. Since 1980s, IGPCEA has provided seismic safety evaluation for hundreds of important construction projects, like offshore platform in Bohai oilfield, the Three Gorges Dam on the Yangtze River, Hong Kong-Zhuhai-Macao Bridge and More than half of the nuclear plants, and has made important contributions for our country’s economic development. Moreover, IGPCEA has taken the lead in compiling a number of national standards, including "Code for seismic investigation and evaluation for nuclear plant project", "Code for Seismic Safety Evaluation of Engineering Sites" and "Seismic ground motion parameters zonation map of China".

IGPCEA has achieved fruitful scientific research results in the field of earthquake prevention and disaster reduction. The scientific research achievements presided over or participated in have won more than 30 national awards and 156 provincial/ministerial awards. Dozens of scholarly monographs of high academic value have been written and published by experts from IGPCEA, including representative ones such as Earthquake in China (Li Shanbang, 1981), The Introduction to Solid Geophysics (Zeng Rongsheng,1984), Engineering Seismology (Hu Yuxian, 1988) and Earthquake Source Physics (Chen Yuntai), which are all classics in the professional field.

IGPCEA has sponsored 5 academic journals, which are Acta Seismologica Sinica, Earthquake Science, Progress in Earthquake Sciences, Computerized Tomography Theory and Applications and Reviews of Geophysics and Planetary Physics. IGPCEA has collected over 200,000 volumes of geomagnetic, geophysical materials and professional books dating back to 1869, forming the richest and oldest collection of geophysical books and materials in China.

---
## [twilightwanderer/Skyrat-tg](https://github.com/twilightwanderer/Skyrat-tg)@[8b1ec33143...](https://github.com/twilightwanderer/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Monday 2022-03-28 06:09:24 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [N5N3/julia](https://github.com/N5N3/julia)@[62e0729dbc...](https://github.com/N5N3/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Monday 2022-03-28 06:33:01 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [PeterZaal/subsurface.github.io](https://github.com/PeterZaal/subsurface.github.io)@[ad4b82193b...](https://github.com/PeterZaal/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Monday 2022-03-28 06:46:58 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [jakmeier/nearcore](https://github.com/jakmeier/nearcore)@[6351eb5511...](https://github.com/jakmeier/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Monday 2022-03-28 06:47:45 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [tellowkrinkle/pcsx2](https://github.com/tellowkrinkle/pcsx2)@[d6684efd26...](https://github.com/tellowkrinkle/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Monday 2022-03-28 07:55:26 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Prince of Persia - Sand of Time / The Two Thrones / Warrior Within
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [DeepLabCut/DeepLabCut-live](https://github.com/DeepLabCut/DeepLabCut-live)@[ce8e96a80d...](https://github.com/DeepLabCut/DeepLabCut-live/commit/ce8e96a80d563e0b55f3a998aafdd10fcc2ec26c)
#### Monday 2022-03-28 09:49:23 by Jonny Saunders

Swap Packaging to Poetry (#60)

* Swapping packaging to Poetry
- main thing is removal of setup.py and requirements.txt, instead we have pyproject.toml and poetry.lock. pyproject is the project description that contains everything that setup.py does (i was careful to keep it as similar as possible to the existing one while also adding version constraints that allow a successful build/install), and the poetry.lock contains the exact specification of what to install
- I bumped up the minimum python from 3.5 to 3.6.1 to be able to install a few packages, both 3.5 and 3.6 are EOL and we should think of bumping this up further.

Also
- added some type hints to the DLCLive class which was bothering me to not have tab completion when i've been using it lol
- DLCLive object tries to mutate something that is by default a tuple, which should cause an error if anyone tries to use tflite and dynamic (instead of warning and repairing as is intended)
- Using Pathlib to resolve the path and check that it exists when loading configuration, this gives more helpful error messages bc people know where DLC is looking in their filesystem/resolves ambiguity of relative paths
- added a CITATION.cff file <3

* oop forgot to quote the pseudo-imported Processor class

* did not see we had github actions in here!
- removed pip install requirements
- removed pytest tests (i don't see any!?)
- installing package and running test from already checked-out copy rather than pip installing from git://
- the packaging script doesn't look like it's doing anything, but i'd be happy to write one that autodeploys on tagged commits to master

* - added argument parser to be able to suppress display on testing, and then call it when doing the tests
- also install and run using poetry because windows paths are an abominable hell
- tensorflow 2.7 only support python >3.7

* ohhhh Display is still instantiated even if the `display` arg is false because it gets instantiated before the check happens whether it should be saved or not.
also limited tf versions for python <3.7 because it has to like do the ridiculous pip thing where it downloads all of them for some reason

* arg not being passed through, does windows want to run poetry yet?

* OH need to put argparser within the function

- also cleaned up file handling in test function. Previously the video file was downloaded and not used, and lots of implicit paths that seem to be causing people trouble when running it.

* try catch removing temporary directory because WINDOWS GOD DAMN IT

* ok 3.6 is EOL anyway and it's causing all the problems

---
## [kingsleyzissou/osbuild-composer](https://github.com/kingsleyzissou/osbuild-composer)@[af44202b1c...](https://github.com/kingsleyzissou/osbuild-composer/commit/af44202b1c6e53a5d3a248e2c1c493445743f188)
#### Monday 2022-03-28 09:49:30 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [gsteel/laminas-i18n](https://github.com/gsteel/laminas-i18n)@[7eb691b246...](https://github.com/gsteel/laminas-i18n/commit/7eb691b2463617c9aeed8e67fd6e410040f3bbec)
#### Monday 2022-03-28 09:54:41 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [Idklol55/PE-0.5.1-Android](https://github.com/Idklol55/PE-0.5.1-Android)@[86ae92a5c1...](https://github.com/Idklol55/PE-0.5.1-Android/commit/86ae92a5c15b03710f1463a5c8cd042c5cc1ac6c)
#### Monday 2022-03-28 10:33:23 by ShowoffTH

FUCK YOUFUCK YOUFUCK YOUFUCK YOUFUCK YOUFUCK YOUFUCK YOUFUCK YOUFUCK YOU

---
## [Idklol55/PE-0.5.1-Android](https://github.com/Idklol55/PE-0.5.1-Android)@[32ba6eb45f...](https://github.com/Idklol55/PE-0.5.1-Android/commit/32ba6eb45f8ae93f5d64ac475e34a62b0f1c5b74)
#### Monday 2022-03-28 10:45:10 by ShowoffTH

FUCK you FUCK you FUCK you FUCK you FUCK you FUCK you FUCK you FUCK you FUCK you FUCK you

---
## [ctopal/ibex](https://github.com/ctopal/ibex)@[c15f3b8888...](https://github.com/ctopal/ibex/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Monday 2022-03-28 10:57:36 by Rupert Swarbrick

[icache] Define some fake DPI functions to simplify linking

This is triggered by the fact that if the ICache parameter is false
then we don't instantiate the ibex_icache module. For verilator
simulations, the module is then discarded entirely, which means that
its two DPI functions are not defined. That's unfortunate because
we're also compiling the code in scrambled_ecc32_mem_area.cc, which
expects the functions to be defined.

The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
don't have an icache) isn't easy to do, because FuseSoc doesn't
currently allow us to use parameters to configure its dependency
tree (see fusesoc issue 438 for a discussion).

The super-clever solution that I came up with before(!) was to declare
these symbols as weak in the C++ code. That way, we can do a runtime
check to make sure that no-one is silly enough to call them without an
icache, but everything will still build properly either way.

Unfortunately, that doesn't work well with xcelium simulations.
Xcelium turns out to compile all the C++ code into one .so library and
generate functions for exported DPI functions in another. These two
solibs then get loaded at runtime with dlopen(). But this doesn't work
with weak symbols: in fact, it seems you end up with the C++ version
every time. Boo!

So let's be stupider about it and define (bogus) versions of the DPI
functions in this case. Fortunately, both of them are designed to
return zero on failure so we can just return zero and needn't worry
too much.

The idea is that when this lands, we can revert the OpenTitan change
that switched the C++ code to using weak symbols and Xcelium
simulations will start working.

---
## [SabreML/Pariah-Station](https://github.com/SabreML/Pariah-Station)@[770ef81a1f...](https://github.com/SabreML/Pariah-Station/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Monday 2022-03-28 11:27:38 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[cbb6d6664f...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/cbb6d6664f41d0e3c0237fcac97ed5a723fb5fe6)
#### Monday 2022-03-28 12:24:48 by Hayden Pearce

munin-pihole-plugins: how the fuck, honestly?

test. yo. shit. saint.

install can now be re-run as intended to update plugins or change the plugins to be installed

Changes to be committed:
 - modified:   script/munin-pihole-plugins
   bump version to 04.05.03
   add missing $ from SCRIPT_DIR declaration
   fix wrong comparitor in uninstall_plugins
   (-f fails, as expected really - use -h instead)

---
## [kefetor/AR-Photobook](https://github.com/kefetor/AR-Photobook)@[b0fb928309...](https://github.com/kefetor/AR-Photobook/commit/b0fb928309a1bae28f10a1ab62d762bf7752d8e7)
#### Monday 2022-03-28 12:29:07 by Kefe Gulsen

Proof Of Concept Via Cinema4d and XR

Digital Photobook https://xr.plus/ft4 
 
	      I started with a different idea. With the feedback, I changed my idea about the blindness experiment to develop my graduation photobook project to a further digital version. With that change I started doing my research. I aim to present my photobook in an AR environment. So, you can put your digitally owned nft in a sort of physical world and interact with it like changing pages, hearing sounds. This project can be proof of work for my final project, and I can further develop this with unreal engine and private servers that execute like the software I'm using. 

My Project “P.L.U.R Ritual Of Millennials” 

https://kefe.co.uk/plur-ritual-of-millenials-senior-project 
 
		After I start looking at what software to use, I remembered the website that Luciano told us about. With this software, I can use it to show my 3D book on the ar platform. Even with the web-based users and phones. 
https://xr.plus/ 

I need to make the 3D model of my book and try to animate the pages by myself and ad it as an object or figure out how to make animations interactive way. Add some sound and music to create an immersive experience. I ended up adding opening animation and included my favorite picture of the project. 
		I used Cinema 4D for my modelling process. The reason I chose this software is I was already using it as my primary 3d software, and I have the knowledge to execute this such project. I started modelling the outer cover of the book, then continued with adding textures. I’m planning to add more pages in the future . 
 

I did 3 interviews with people who are invoved in this industry.  
First one is Cemre Yesil Gonenli, Owner of the Fil Books https://cemreyesil.com/ 
I started by asking if a digital AR book can get the feeling of the photobook medium. She told me “It’s a bit of a distant experience”. So I started thinking about how can I give the feeling of ownership and the sentimental values of a photobook. 

It clicked me after some days of work. We can tokenize the photobook. We can make it limited or unlimited amounts of copy without a dime and, we can also nft it so you would have the ownership. We can reach more audiences without the production and storage costs. 
	 

After that I went to Jane & Jeremy’s bookstore called The Bookend and did a short interview with Jeremy about my project. He was also concerned with same things but He was interested with the project and never seen anyone doing it the way I execute. http://jane-jeremy.co.uk/ 
	 

Third one is a rockstar photographer in Turkey, Koray Birand. https://www.koraybirand.co.uk/ 
He is also researching digital arts, publishing nft’s and he does livestream with his avatar on metaverse. 
Koray was more open to new ideas, he said if I’m going to execute this in unreal engine with proper working system, he maybe would try to publish one of his books as an nft with this AR addition. 
 

I started executing thru XR.plus. The first challenge was importing the 3d model with textures and materials combined in one pack. I used .glb format as my import, it was giving the best results. Learning and adding animations was fairly simple but getting to know “states” was a bit difficult for me. I ended up putting up a button that loops or stops the animation to showcase what this proof of concept can evolve to. 

I did end up executing the way I want as a proof of concept with working AR system. I’m happy with my results and I aim to continue devoloping this project. My future projection is to make a workflow to provide people for them to make their own digital photobook. 
 
Please visit my blog for detailed pictures and videos: https://madma.kefe.co.uk/category/agm33/

---
## [GNOME/gimp](https://github.com/GNOME/gimp)@[7123b6c466...](https://github.com/GNOME/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Monday 2022-03-28 12:52:04 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [IlDucci/duckstation](https://github.com/IlDucci/duckstation)@[603e1bfbeb...](https://github.com/IlDucci/duckstation/commit/603e1bfbeba02d0743fcf626117a2a873993e934)
#### Monday 2022-03-28 12:58:34 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Monday 2022-03-28 13:27:46 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [LandenSisk/FastDriveVex](https://github.com/LandenSisk/FastDriveVex)@[4ecb675ffb...](https://github.com/LandenSisk/FastDriveVex/commit/4ecb675ffb52d2595e721fcb895598e4318b0359)
#### Monday 2022-03-28 13:37:33 by Landen Sisk

Fuck you

YOu supid ad pitch, fuk u and I d ur mum.

---
## [RMX1801/android_kernel_realme_sdm660](https://github.com/RMX1801/android_kernel_realme_sdm660)@[703a84a21e...](https://github.com/RMX1801/android_kernel_realme_sdm660/commit/703a84a21e9fd6c3fae3ed920196eb0e7a03204e)
#### Monday 2022-03-28 14:57:29 by Maciej Żenczykowski

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
## [sidyadav3/crawl](https://github.com/sidyadav3/crawl)@[9e681642b6...](https://github.com/sidyadav3/crawl/commit/9e681642b6851451cbfcbc7a92e7de4b97106055)
#### Monday 2022-03-28 15:28:59 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

---
## [avar/git](https://github.com/avar/git)@[9951d92176...](https://github.com/avar/git/commit/9951d92176eafb714b3bb294560b170b82b79211)
#### Monday 2022-03-28 15:30:56 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [EasyCorp/EasyAdminBundle](https://github.com/EasyCorp/EasyAdminBundle)@[f3a4b13382...](https://github.com/EasyCorp/EasyAdminBundle/commit/f3a4b13382f6d96f85b0b1d8dfe329f40a39d32c)
#### Monday 2022-03-28 16:51:16 by Javier Eguiluz

minor #5139 Disable UX-Turbo (Lustmored)

This PR was merged into the 4.x branch.

Discussion
----------

Disable UX-Turbo

In all my projects with EasyAdmin I am sharing Stimulus controllers between EasyAdmin and frontend (I need them sometimes and it's just simpler). Since enabling Turbo on some projects I need to overwrite EasyAdmin layout just to disable it.

Currently EA is very unfriendly towards Turbo - there are JavaScripts in body, DOMContentLoaded listeners and so on. Refactoring everything to be turbo-compatible would be titanic effort with little benefit (it's not really needed in CRUD dashboards in my opinion), while adding this single attribute will make life easier for probably more consumers than just myself :)

Commits
-------

735b2397 Disable UX-Turbo

---
## [cgaebel/magic-trace](https://github.com/cgaebel/magic-trace)@[218950a0a3...](https://github.com/cgaebel/magic-trace/commit/218950a0a3e46aa98f09b2697026a43113dccff3)
#### Monday 2022-03-28 17:06:34 by Clark Gaebel

Rework trigger modes

Replace `-symbol` with a "trigger mode" option. To quote my own help
text:

1) If you do not provide `-trigger`, magic-trace takes a snapshot
   when either it or the application under trace ends. You can Ctrl+C
   magic-trace to manually trigger a snapshot.

2) If you provide `-trigger $`, magic-trace will open up a
   fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide `-trigger <FUNCTION NAME>`, magic-trace will
   snapshot when the application being traced calls the given
   function. This takes the fully-mangled name, so if you're using
   anything except C, fuzzy-find mode will probably be easier to
   use.

`-trigger .` is a shorthand for `-trigger magic_trace_stop_indicator`.

This also removes three command-line arguments that are, in my opinion,
a mix of unnecessary and probably a bad idea to expose:

- `-delay-thresh` can be replicated by an applicationg doing this
  measurement itself. It's a very cheap operation for an application
  to add, I don't think that magic-trace is adding very much here.

- `-duration-thresh` is in the same boat as `-delay-thresh`.

- `-immediate-stop` causes issues on some kernels. Let's just remove
  it for now and revisit it in a couple years. If people actually
  want their trace to end exactly when the trigger fires, we can
  postprocess the trace output.

Please play around with this! I think it's a easier to to use... but
that's just like my opinion, man.

Fixes #60 and #69.

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[fb5a531e78...](https://github.com/k21971/EvilHack/commit/fb5a531e78639b5cab93b26cd96de110d018d155)
#### Monday 2022-03-28 17:28:47 by k21971

Tortle as a playable race.

Another new race for EvilHack, added at the request of amateurhour.
Tortles are humanoid tortoise-like beings. They are large, and have a
hard shell on their back which they can retreat into when threatened.
They have several armor restrictions due to their size and body shape.
Tortles are typically lawful in alignment, but are sometimes neutral as
well. To get an idea of what a tortle looks like, along with several
other characteristics, check out their Forgotten Realms entry online.

The specifications:

* Tortles can play as either an Archeologist, Barbarian, Healer, Monk,
Priest, Tourist, or a Wizard
* They can max their strength to 19 and wisdom to 20. Dexterity is
capped at 10, charisma is capped at 14
* They can be either gender, alignment choices are lawful or neutral
* Tortles start with the ability to swim, and have magical breathing
(can hold their breath for a ridiculously long time). They gain warning
at experience level 5, and hungerless regeneration at experience level
12
* Tortles start with a naked AC of 0 due to their hard shell, but are
very limited in what kind of armor they can wear
* Tortles cannot wear body armor, cloaks, t-shirts or boots (body
size/shape). They can wear gloves and helms, but only if their material
is made of something that isn't hard or rigid. Any type of shield is
fine, as are rings and amulets
* Tortles are the slowest of the player races, with a speed of 8
* A new type of helm was created - the toque (think Jayne from the show
'Firefly'). Like the fedora, it is made of cloth, does not grant any
extra AC, does not spawn randomly, and will only appear as a tortles
starting gear depending on what role they choose. It can also be wished
for. One special quality it has - it can protect the wearer from sonic
attacks (those goofy earflaps have a function after all)

There's more to do with the Tortle, this is just the initial commit to
get it in. What still needs to be done: giving the tortle the ability to
hide in its own shell, and figure out and implement the pros and cons to
doing that - player monster tortles - stand alone tortles as a monster
the player could encounter. And of course other little tweaks and
changes that haven't been thought of yet.

This should be a fun but challenging race to play once it's complete.

---
## [dmachaj/terminal](https://github.com/dmachaj/terminal)@[855e1360c0...](https://github.com/dmachaj/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Monday 2022-03-28 18:34:02 by Mike Griese

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
## [ThomasThePencil/tModLoader](https://github.com/ThomasThePencil/tModLoader)@[674f11a4d7...](https://github.com/ThomasThePencil/tModLoader/commit/674f11a4d757a00eee3cefa43636d18b58e804ae)
#### Monday 2022-03-28 18:44:26 by ThomasThePencil

if you like whips, you are officially cringe

because Red, magnificent bastard that he is, made whips god-awful to work with

- cleaned up a couple of methods that were actually larger than they needed to be
- new exception grammar things because...I'm not sure why these are important, actually
- moved StatInheritanceData to its own file, removed its default constructor, added two new presets for it (Full and None), which function about as you'd expect, and made it so that all parameters for a new StatInheritanceData instance MUST be defined, rather than defaultin' to 0f
- new damage class for whips which makes use of the new. it benefits from everything for Generic and Summon, and benefits from Melee's useAnimation and useSpeed bonuses
- all things which previously checked against item.summon and ItemID.Sets.SummonerWeaponThatScalesWithAttackSpeed[item.type] (I'm not kiddin', it's actually this retardedly long) now check against the new damage class instead
- made Player.whipUseTimeMultiplier internal and made it reference the new attack speed fields so that I don't wanna DIE
- removed DamageClassLoader.RebuildStatInheritanceCache since it's not actually used and wouldn't complement the new design well anyway

---
## [GABRlEL/payday2.pw-Mods](https://github.com/GABRlEL/payday2.pw-Mods)@[fb4f41f7ca...](https://github.com/GABRlEL/payday2.pw-Mods/commit/fb4f41f7ca631567b8635c1408bbeaa6f5716ecd)
#### Monday 2022-03-28 18:44:46 by Gabriel

Big 2022 Update Part 2

Part 2 of the Big 2022 Update is finally here!

Intro:
I added a _didntwork directory for every mod I tried creating but which ended up not working.
Most of the mods here are unchecked so I can produce more mods. I appreciate every testing. Most mods work right away anyways though.
The checked mods might not be tested a lot.

Added unchecked mods:
_didntwork\Increase explosive & projectile damage: I tried to increase grenade and projectile damage here.
All difficulty achievements on Normal: Changes achievement tweak data to allow achievements to be achieved (no pun intended) on all difficulties.
Anti-Taser: Reduces Taser duration and recovery time to 0
Crime Spree score multiplier in other lobbies: Enables Catchup bonus at all times in other lobbies and increases it by a lot
Crits on projectiles & grenade launchers: Allows crits for grenades & grenade launchers etc.
Death Sentence XP on every difficulty: Changes the XP multiplier for every heist to be on Death Sentence
Disable medic healing: Medics no longer heal anything
Dont lose money on civilian kills: Self-explanatory
Drills no longer jam: Drills no longer jam by themself
Enable ammo pickup for explosive arrows: Arrows no longer disappear on impact
Enemies no longer steal loot: Self-explanatory
Free masks (and styling): Masks and their styling no longer cost money
Free perk decks: Perk Decks are free
Free skills (Alternative version - On infamy): After going infamous once, all skills will be free
Free skills (UNDETECTED Beta): (This was added in a seperate patch already.) Undetected Beta for Free skills, this might bypass some third-party anti cheat mods.
Free weapon and mask slots: Weapon and mask slots no longer cost anything
Free weapons: Weapons no longer cost anything
Full XP on job failure: You receive regular XP on job fail
Full XP on job finish in custody: No XP reduction, if you're in custody on job end
God Mode (Lobbywide): NPCs no longer deal damage to anyone in the lobby
High Jump: Jump higher
Increase stealth XP bonus: Increases the stealth XP bonus after missions by a lot
Infinite deployables: 99 of every deployable
Insane holdout rewards: Higher rewards and all additional rewards already on wave 3
Loot drop increaser (On infamy): Increases loot drops after 1 infamy level
Multilingual meth helper: German & English version of meth helper
No bag value reductions: Difficulty and alive players dont impact bag value
No fall damage: Self-explanatory
No flash: Removes effect of flashbangs and concussion grenades
No special enemies in holdout: No shields, medics, taser, dozers and cloakers
No wave ramp up in holdout: Waves don't get more difficult
No weapon damage falloff: Self-explanatory, doesn't display in HUD
No weather: Self-explanatory
OP Crime Spree assets: All Crime Spree gage assets have been dramatically improved
Remove timers + Always interact: Self-explanatory
Weapon laser defaults to full strength: Laser put on new weapons is automatically set to 1 Alpha
Wipe money + Offshore: This variant also wipes offshore cash.
XP increaser (On gage package pickup): Self-explanatory
XP increaser (On job fail): Self-explanatory
XP increaser (+ loot drop increaser) (On infamy): Increases XP (and loot drops) after 1 infamy level

Added checked mods:
Always interact: Allows you to interact with things like windows (to barricade) without having the required item.
Double tick rate: Doubles network tickrate and other network-related stuff for a smoother experience. (Please report any bugs, I have no clue about network-related stuff)
Instant holdout waves: Waves go by a lot faster
Money increaser (Bag value): Increases bag value
XP increaser (On mission end): Self-explanatory

Changed unchecked mods:
Anti modding detection: Properly clarified, that the mod code was made by Dr.Newbie & changed capitalization
Crime Spree difficulty changers: Properly clarified, that I'm not the original author of the mod code
No drill timers (& Compatibility version): Reduced mod code by a lot
Remove timers (& Compatibility version): Reduced mod code by a lot
Wipe money: Added mask sell

Changed mod.txts:
Add 900 gage packages on every difficulty: Updated description
Bag speed: Changed capitalization
Better Aim Assist for controller: Changed capitalization
Better bipods: Changed capitalization
Better Exploding Enemies mutator: Changed capitalization
Crime Spree adder ( & Auto updater): Changed capitalization
Crime Spree unlocker: Changed capitalization
Dont lose Crime Spree on crash: Changed capitalization
ECM jammer rebalance for Loud: Changed capitalization
Free Crime Spree assets: Changed capitalization
Free Crime Spree reroll: Changed capitalization
Free mission assets: Changed capitalization
Free preplanning: Changed capitalization
Free safehouse upgrades: Updated description and changed capitalization
Free skill sets: Changed capitalization
Free skills: Changed capitalization
German meth helpers: Changed capitalization
God Mode mutator: Changed capitalization
Infinite Ammo Bag charges: Changed capitalization
Infinite Body Bag charges: Changed capitalization
Infinite Doctor Bag charges: Changed capitalization
Infinite Messiah charges: Changed capitalization
Infinite Sentry ammo: Changed capitalization
Infinite stamina: Changed capitalization
Insane Crime Spree cashout (& Alternative version): Changed capitalization
Instant equip deployment: Changed capitalization
Instant win: Changed capitalization
Invulnerable sentries: Changed capitalization
Money increaser (On sell): Updated name and changed capitalization
No Crime Spree modifiers: Changed capitalization
No Crime Spree rewards: Changed capitalization
No custody: Changed capitalization
No drill timers (& Compatibility version): Changed capitalization
No flash (Skill-based): Updated name and changed capitalization
No mutator penalty: Changed capitalization
No pagers: Changed capitalization
No skin wear: Changed capitalization
No skins: Changed capitalization
No special enemies: Changed capitalization
One Hit mutator: Changed capitalization
OP ECM jammer: Changed capitalization
Perk deck points giver: Changed capitalization
Remove difficulty level locks: Changed capitalization
Set Crime Spree level: Changed capitalization
Surefire Skill infinite magazine: Changed capitalization
Trash turrets: Changed capitalization
Unlock all Raid jobs: Changed capitalization
Unlock all safehouse trophies: Changed capitalization
Unlock all skill tiers: Changed capitalization
Wipe Crime Spree winning spree: Changed capitalization
Wipe money: Changed capitalization
XP increaser (Alternative version - Skill-based): Updated name and changed capitalization

Notes:
Free infamy skills will stay permanently removed due to the new infamy system.
The mods will be uploaded to the website over a time-span of around 1 week to prevent google safe-browsing from flagging the website. The Github repository will always be updated.

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[12be627921...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/12be6279214f9a1b2d5afe92fbeaa04ec27fe9da)
#### Monday 2022-03-28 18:55:45 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d3b1440646...](https://github.com/mrakgr/The-Spiral-Language/commit/d3b1440646071f817a400e6d088fb8ca9f55926e)
#### Monday 2022-03-28 20:12:03 by Marko Grdinić

"12:05pm. I got up really late today. If it was the usual it would have been 11am. I'll skip the morning session.

I do not whether I'll be able to do this. I'll give it my best shot, but I've always been a slowpoke when it comes to making stuff. Programming is suited for slow and methodical planning which I am good at. Churning stuff at a rapid clip is not something I am used to. But I'll try to develop this kind of skill.

Let me eat.

12:40pm. Done with breakfast. I do not need to do the chores today. Let me finish the latest Rose Garten and Knight Run chapters and then I will start.

Learning is hell. The urge to retreat into the safety of money and laziness is overwhelming. Yet, if I want to prove my worth as a superior human, I need to embrace it.

12:55pm. Now that I think about it, a story like Knight Run would really benefit from being done in 3d. It has a huge number of large scale battles. It is just difficult to put in all the detail by hand. This kind of work would be a lot easier when you have scattering capabilities.

In terms of storytelling, I find the latest arc confusing with all the new characters fighting all of a sudden, but the previous arc was which was just a side story was a 10/10 masterpiece.

1pm. Forget that. I am going to give it a try. Let me deal with the props and then I will get properly lazy. Once I get to actual writing, things should be easier for me.

Let me start by exporting what I did yesterday. After I closed for the day, I felt like doing a little. I put some displacement cloud noise on the top of the tesk to match my own.

Oh right. Before I export, let me create the UVs.

1:45pm. I playing around with it in Blender, and it really has decent functionality. It has pins and straightening. It is no problem. This impressed me in Houdini, but Blender has it as well.

There are various packing modes, but UV unwrapping is all I need. Right now I am just messing with cylindrical unwrapping a little.

UV unwrapping seemed really complicated when I first learned about it, but after a few days of focusing on it, I see that there isn't much to it. What the various things do is self explanatory.

Right now I am ready to export. Let me just take a short break first.

2:10pm. Let me resume.

I unwrapped some of the objects by hand and the rest by using auto unwrapping. I haven't put too much effort in it.

Let me finally export it as USD and I will shade it in Clarisse.

That having said, I want to paint a mask. There is a lot of paint peeling in front, but not much on the sides and I want to capture that pattern.

2:20pm. Ah, damn. Blender's remesher wrecks the UVs. Unlike Houdini, it does not have the option to preserve the old edges.

Let me remove the noise then. Painting the mask is more important. I am playing with bump and it really looks very nice.

...Agh, let me take a break again.

2:35pm. Let me resume for good.

Let me just play with texture painting for a while. I need to figure out how to both paint and export the stuff out. I watch some vids on it, but never tried it.

3:05pm. Ok, I have the necessary masks. How do I export them?

I have to say, now that I am looking at the brush functionality, it is all there. Everything that I'd want is present. Hmmm, I am not sure if it has layers, but the masking is there, so that is one main thing down.

I could do good work in Blender even if it is just texture painting.

Exports! How do I export the textures?

First let me try exporting everything as USD. Maybe it will get captured. If not I'll have to look at the docs.

...Oh, it has the export textures option.

3:25pm. It is so annoying to snap in Clarisse. It is hard to snap the manipulator to the bottom of the bounding box.

3:35pm. Hmmm, the USD import is still as nasty as ever in Clarisse.

A week ago I got advice to use the hierarchy view, but I can't see a way to narrow it down to a particular asset. I'll have to ask again.

4pm. Yeah, if I parent the desk to an empty it starts showing me the correct hierarchy. That works.

4:05pm. For some reason the cylinder is colored black in Clarisse.

Where are the textures supposed to be?

4:10pm. Hmmm, the reason it is black might be because of the normals being messed up.

Yeah, the normals were the problem.

4:15pm. It seems there is a difference between resync and reload resources for some reason.

Nevermind that.

Now focus me. Where are the textures?

Ah, right. I must be retarded. The export said well enough that it would export them to the textures folder in the same place as the USD file. Let me import them in Clarisse and slap them on.

4:25pm. Ok, the first one is the hardest. Let me use the texture as mask for the fractal noise.

4:35pm. The soft borders look like this. I should have made the mask 1,0 exclusively.

Rather than going back and fixing things, I can just ramp up the contrast to max instead.

5:10pm. I ran into a problem I did not anticipate and now I am thinking what to do about it. I want to distort the borders of the mask. What I did was add UV noise and then realized there are seams. Well of course there would be. I am distoring in 2d space when I should be doing it in 3d space.

I wonder if the V-Ray distortion nodes could do this correctly? Maybe there is a reason they have specialized nodes for that instead of adding UV noise like here.

Forget distortion.

I can't change the UVs because that would mess up the texture.

5:25pm. I need to do some research. Maybe I should check out texturing specialized programs for how to do the border. Or maybe there could be OSL distortion nodes?

https://render.otoy.com/forum/viewtopic.php?f=30&t=75477

I wonder if there is a site that collects these shaders somewhere. They are weirdly hard to find.

A projecting distortion shader would solve my problem here. But I wonder if there are alternatives?

5:35pm. Let me close Clarisse. Change of plans. I am going to study Mari. I really need something to blur the mask otherwise it will look like crap. it is the little things that matter the most in order to get it to look good. I need to trick the brain into thinking the noisy grunge around the borders looks good. If it is just a flat line, it will look cartoony.

I want the gritty feel when I want it and the cartoony feel when I want it. If I start feeling lazy when I run into a problem I will never improve.

The problem I have here would not have been an issue if I were using solely 3d textures or just multiplying 2d textures with noise, but I really need the distortion.

https://www.youtube.com/results?search_query=mari+tutorial

Let me watch some of these.

5:45pm. I guess I'll 'get' Mari as well. For the past few days I've been so wrapped up in my own thoughts that I completely forgot about the Creative Shrimp course. I only have two parts left to download.

Mari is split into 4 parts, but they are only 300mb each. Piece of cake.

https://youtu.be/LArgA2QR2vo
Introduction to Mari - Getting Started with Texturing

Let me check this out while the thing downloads.

Yeah, I am not exactly too comfortable with the Clarisse shaders. It works, but I can't help but wonder whether I have the right workflow.

https://youtu.be/LArgA2QR2vo?t=906

This is interesting.

Thought Mari might be overkill for my needs.

well, there is nothing wrong with watching the video and downloading it.

https://youtu.be/LArgA2QR2vo?t=1219

> If you want to do straight up 3d painting, substance of Z brush is a better alternative in that regard.

6:15pm. Hmmm, the brush jitter looks a bit like distortion. It is an interesting alternative that I should consider, but I'd really like to be able to distort the 2d texture in 3d. I think that Mari might be the wrong program for this. Substance painter? I'll check out the tutorial for it as well.

https://youtu.be/LArgA2QR2vo?t=1283

This thing where they are getting small errors due to the brush acting like a spray feels like a significant issue. Just why is Mari so highly regarded?

6:25pm. I think I've grasped something important. Rather than the distortion effect, the problem is that Blender only has a regular brush. Imagine if it had something like real pencil in Clip Studio. That would really make things easy for me. I've been obsessed with noise textures, but they aren't the easiest thing to work with.

https://youtu.be/LArgA2QR2vo?t=1600

These are good patterns.

https://youtu.be/LArgA2QR2vo?t=1666

Another good pattern. I could get a lot more variety using this than trying to squeeze noise textures into this framework.

https://youtu.be/LArgA2QR2vo?t=1708

Come to think of it, I've forgotten how to switch to the eraser mode in CSP. I'll have to refresh my memory, but it does not matter right now.

https://youtu.be/LArgA2QR2vo?t=1861

This stuff is a bit closer to my 2d art education. It has been a long time since I did any of that. I am convinced - I should try to paint the desk using texturing tools rather than messing with noise. I think that some program will allow me to start with a noise texture and then allow me to work my way from there.

I'll want to find some nice randomized brushes, Blender allows textures, but that is not enough for me.

https://youtu.be/LArgA2QR2vo?t=1950

If it has this, then it will definitely have the gradient maps that I need.

6:55pm. Had to leave for lunch. Let me finish the Mari tutorial today and maybe I'll watch a bit of the Substance Painter one after that.

There some open source programs for this kind of thing as well.

https://youtu.be/LArgA2QR2vo?t=2192

Oh, here are the noise patterns. As expected.

https://youtu.be/LArgA2QR2vo?t=2909

He says that the Blur tool is useful for bluring seams.

https://youtu.be/LArgA2QR2vo?t=2997

This is pretty cool.

7:35pm. Ok, I get it. Mari is like 3d Photoshop.

This has some appeal for me.

What about Substance Painter?

https://youtu.be/RQ-hRk0WHJ8
Introduction to Substance Painter - Ultimate Beginners Guide

Here is another tutorial by the same guys.

https://youtu.be/RQ-hRk0WHJ8?t=78

PBR guides? I'll consider them.

https://www.youtube.com/results?search_query=substance+painter+vs+mari

Let me watch one of these.

https://youtu.be/LGY-NMSehAg
Substance Painter vs Mari which is Better

This one is pretty interesting.

8pm. Ugh, you know what, since I got the first two parts, I might as well get the last two and go with Mari. The video above makes it sound like SP is easier to use, but it a 2x larger download and has 5 parts so I'd need the to spend the entirety of tomorrow waiting for it to finish.

The texturing I need to do is quite simple, but kind of beyond the scope of what I can do with shader nodes. Even if I could do it in Blender, I am not sure that I can spend time hunting down various brushes. I like what I saw in the FlippedNormals introduction.

https://youtu.be/LGY-NMSehAg?t=353

Ah, substance designer is the procedural tool, right. I've been confusing it and painter wondering whether they are the same thing.

https://youtu.be/LGY-NMSehAg?t=479
> Vastly superior texture projection techniques.

I see that often mentioned.

8:10pm. Damn it, I forgot to type in the captcha in time. I'll have to try it again in an hour.

https://youtu.be/smiEZinVuF4
Substance Painter Vs Blender | for Texturing Your Models

https://youtu.be/smiEZinVuF4?t=143

He says that anything that can be done in SP can also be done Blender, but that Blender has a complex node and baking system. Not what I expected. Then could I actually texture the thing in Blender somehow?

https://youtu.be/gF3MifkvESc
Mari VS Substance Painter - What's the Best Texturing Tool?

Let me watch this as well.

Yeah, it is clear to me - I had a brief phase where I wanted to use noise textures for everything, but I should move on from that if I want to progress.

https://youtu.be/gF3MifkvESc?t=341

This is a good video, that one by the Chinese girls was useless in comparison. Here they hammer it home that Mari was designed to handle a lot of data while SP was designed for ease of use.

They keep saying that Mari needs powerful hardware though. Maybe my GTX 970 will suffice? If not I'll just get SP.

https://youtu.be/gF3MifkvESc?t=446
> This stroke here you actually could not do (in SP.)

They talking not about seams, but about painting across texture sets.

Maybe things have changed in the last 3 years

https://youtu.be/gF3MifkvESc?t=499
> It is very hard to hand pain on a mesh when you are not hand painting on a mesh.

They mention that since Mari was designed for film, they will mostly be using photographic references for textures.

Yeah, I'll just get both programs. SP will have built in materials. But I'll give Mari a try tomorrow. Damn this desk is such a handful.

https://youtu.be/gF3MifkvESc?t=600

They mention they are using a GTX 980 Ti, but it still takes a while to create a layer. Wow, that is some demand.

https://youtu.be/gF3MifkvESc?t=1140

He mentions that a lot of people are using Mari for masks now while they make and preview the textures in Substance Painter and Designer.

https://youtu.be/gF3MifkvESc?t=1412

He mentions grunge maps being easy in Painter. This is of interest to me for environments.

https://youtu.be/gF3MifkvESc?t=1471

Here they are comparing grunge maps with procedurals. I think I am learning significantly towards Painter at this point. Since it is powered by Designer, these things could be a big boon for me.

https://youtu.be/gF3MifkvESc?t=1495

Ok, this clinches it for me. I have no idea what I was thinking when I focused so much on procedural textures when this should be way better. If I want to learn texturing this is what I should be studying. I am not going to be aiming for film level quality. Plus if it is UDIMs, Painter got thme 1.5 years ago. It is way cheaper that Mari too.

https://youtu.be/gF3MifkvESc?t=1725
> If Painter gets proper UDIM support then the balance changes dramatically.

9:10pm. Holy shit, when I miss a captcha, RapidGator will make me wait for 3 hours. It says to come back an hour later and then makes me wait another 120 minutes!

I should have just waited for the 3m to run out.

And you know what, I am downloading everything from CGPersia, but if is Painter, I should be able to find it on random pirate sites.

Ah, fuck. I downloaded part 3 of Mari twice! Damn!

https://allpcworlds.com/adobe-substance-painter-7-free-download/

Let me just get this. It is close enough to the latest version anyway. This is not the same situation like when I was trying to pirate 3rd party renderers with Houdini, that was a nightmare.

400kb/s. I guess I'll be starting out with SP after all. It should finish in 2h.

9:25pm. Right now I do not feel like studying SP tutorials. Instead what I will do is watch this...

https://youtu.be/KMXpmsmZy38
The Ultimate Guide to Substance for Beginners - Painter/Designer/Alchemist EXPLAINED

...and then close for the day. What is Alchemist, this is the first time I heard about it.

https://youtu.be/KMXpmsmZy38?t=163

Ah, this wood pattern is quite similar to what I need to do for my deck. I had a plan how to do it using noise and gradient maps, but no doubt Substance Painter will give me a better way.

https://youtu.be/KMXpmsmZy38?t=651

So Alchemist is for creating materials from photographs and scans.

https://youtu.be/KMXpmsmZy38?t=1016

He says that Blender is an alternative to Substance Designer.

> I would add that using substance designer is very handy to know if you want to do environments mainly without unique uv's

10pm. Even if I wanted to use Blender, the lack of layers, and the fact that SP gives me procedural textures beyond just noise is too much of a good thing to pass up.

I really went down the wrong path since mid-January. This is the disadvantage of doing it on your own. But I should be able to make rapid progress once I establish my texturing workflow.

I0:05pm. Let me close here. Tomorrow, I think I should have a chance to break out the stylus for the first in a long while. That pen tablet has not seen use for far too long.

I've been getting too fancy with learning Houdini. Rather than Houdini, I need to streamline the basics."

---
## [jasminappleby/100DaysOfCode](https://github.com/jasminappleby/100DaysOfCode)@[c25f52c0c7...](https://github.com/jasminappleby/100DaysOfCode/commit/c25f52c0c75a601e8e6d1938d421d1cf57f7ad0d)
#### Monday 2022-03-28 20:32:34 by jasminappleby

you just gotta feel bad for jada, everyone laughed and she didnt find it funny. she was sad, and i wouldnt be too happy if my husband did that

---
## [nicholas-dougherty/zillow-regression-project](https://github.com/nicholas-dougherty/zillow-regression-project)@[8674b1ed97...](https://github.com/nicholas-dougherty/zillow-regression-project/commit/8674b1ed971e1978d8d12c1e494c159a4c7f3324)
#### Monday 2022-03-28 20:50:46 by Nicholas Dougherty

After pulling an all-nighter, I made it through
the day and even had a successful meeting with
someone I'll call my coach: SS. Not THAT SS...
I've spent a little too much time dillying and dallying.
I have definitely obsessed too much over the finest details
in this project. I just so badly want to reealllly understand
what I am implementing and WHY.

I tried some cool stuff using counties separately, and may
continue along that path. Not sure how to approach it.
I'll head home and go to sleep for a few hours, and then
awaken with a refreshed mind and complete willingness
to accomplish all that I can in this project.

Godspeed you, reader.

---
## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[d82eb30191...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/d82eb30191e90da326979cf3df6a3634772a4ab6)
#### Monday 2022-03-28 21:18:12 by Peter Zijlstra

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

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[41aa1d2ee4...](https://github.com/Tastyfish/Skyrat-tg/commit/41aa1d2ee421161505284504f4d6f76faf51b0f7)
#### Monday 2022-03-28 21:25:46 by SkyratBot

[MIRROR] Adds a colorblind accessability testing tool [MDB IGNORE] (#11995)

* Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a colorblind accessability testing tool

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [UltraFormula1/Python-2022](https://github.com/UltraFormula1/Python-2022)@[8018fe9e9b...](https://github.com/UltraFormula1/Python-2022/commit/8018fe9e9b4d062f5fd8c0f42949ae1b4f3877fe)
#### Monday 2022-03-28 22:41:43 by UltraFormula1

Game V.1.0

City's breaking down on a camel's back
They just have to go, 'cause they don't know wack
So while you fill the streets, it's appealing to see
You won't get out the county, 'cause you're bad and free
You got a new horizon, it's ephemeral style
A melancholy town where we never smile
And all I wanna hear is the message beep
My dreams, they got a kissing
'Cause I don't get sleep, no
Windmill, windmill for the land
Turn forever hand in hand
Take it all in on your stride
It is ticking, falling down
Love forever, love is freely
Turned forever, you and me
Windmill, windmill for the land
Is everybody in?
Laughin' gas these hazmats, fast cats
Linin' 'em up like ass cracks
Play these ponies at the track
It's my chocolate attack
Shit, I'm steppin' in the heart of this here (yeah)
Care Bear rappin' in harder this year (yeah)
Watch me as I gravitate, ha-ha-ha-ha-ha
Yo, we gon' ghost town this Motown
With yo' sound, you in the blink
Gon' bite the dust, can't fight with us
With yo' sound, you kill the Inc.
So don't stop, get it, get it (Get it)
Until you're cheddar headed
And watch the way I navigate
Ha-ha-ha-ha-ha
Sha, sha-ba-da, sha-ba-da-ca, feel good
Sha, sha-ba-da, sha-ba-da-ca, feel good
Sha, sha-ba-da, sha-ba-da-ca, feel good
Sha, sha-ba-da, sha-ba-da-ca, feel good
Windmill, windmill for the land
Turn forever hand in hand
Take it all in on your stride
It is ticking, falling down
Love forever, love is freely
Turned forever, you and me
Windmill, windmill for the land
Is everybody in?
Don't stop, get it, get it
Peep how your captain's in it
Steady, watch me navigate
Ha-ha-ha-ha-ha
Don't stop, get it, get it
Peep how your captain's in it
Steady, watch me navigate
Ha-ha-ha-ha-ha

---
## [UltraFormula1/Python-2022](https://github.com/UltraFormula1/Python-2022)@[80fd520b7a...](https://github.com/UltraFormula1/Python-2022/commit/80fd520b7a9eeb78f1883c9c877165cd33f50211)
#### Monday 2022-03-28 22:41:43 by UltraFormula1

Other tasks (python)

Imagine there's no heaven
It's easy if you try
No hell below us
Above us, only sky
Imagine all the people
Livin' for today
Ah
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion, too
Imagine all the people
Livin' life in peace
You
You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will be as one
Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people
Sharing all the world
You
You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one

---

