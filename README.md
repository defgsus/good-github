## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-01](docs/good-messages/2022/2022-10-01.md)


1,787,994 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,787,994 were push events containing 2,533,689 commit messages that amount to 169,884,496 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [asutherland/mozsearch](https://github.com/asutherland/mozsearch)@[9565bf657f...](https://github.com/asutherland/mozsearch/commit/9565bf657feb010d38ae23da371df68f5f00d007)
#### Saturday 2022-10-01 00:09:06 by Andrew Sutherland

Bug 1783761 - Overhaul the per-file info pipeline.

This does not yet replace JS templating of output directories, but is
a large atomic set of changes to overhaul how we do per-file info data
aggregation.

At a high level:
- `derive-per-file-info.rs` is now gone; crossref.rs now handles the
  ingestion process, with the bulk of the logic existing in
  `repo_data_ingestion.rs`.
- There is now a `config_defaults` directory which we fall back to
  when looking for per-config files.  The idea is to avoid having to
  duplicate the same config file in every directory or to add a ton
  of symlinks (which can complicate windows support).
   - config.rs has been moved for clarity and some of its helpers
     have been moved to be impls for the classes rather than helpers
     that take a config.
   - The config.json files now specify their CONFIG_REPO root, which
     may feel a little weird, but was a simple way to use the
     existing data-flow.  I'll land mozsearch-mozilla changes
     concurrently with this, but it would be great if we could make
     this more clean.
- `per-file-info.toml` is our new config file that allows us to:
   - Define `path_kind` heuristics and rules so we no longer have to
     have the logic be hardcoded in router.py and potentially the
     front-end JS.  This is not yet hooked up to router.py, but that
     will be a logical near-term step.
   - Define text file ingestion like `.eslintignore` so we can
     tag/un-tag files based on their presence in such a list.  In our
     initial landing here, we tag files with "eslint-ignored" if the
     tree has an `.eslintignore` in the root.  we don't bother to
     understand them at any other level of the tree, but it's a thing
     we could do in the future.  This was just an MVP.
   - Define JSON file ingestion to replace what was previously
     hand-rolled data ingestion in `derive-per-file-info.rs`.
      - Practically speaking I generalized the existing logic and
        because of the many ways this data can be nested, we actually
        have 4 different `nesting` algorithms for the 4 different JSON
        files we ingest, and we'll probably have to add more.  Things
        are somewhat more sane now though because we just use a hashmap
        by path for lookup.  Previously we tried to build a nested
        hierarchy that imitated one of our input files and that was a
        mess.
      - These JSON ingestion files allow us to explicitly set the
        path_kind (or other arbitrary metadata) based on the JSON files.
        This means that our path_kinds for tests can be based on them
        existing in a manifest rather than based on a filename
        heuristic!
- Our test info box rendering is moved from being hardcoded in
  `output-file.rs` to being defined as a liquid template.  Honestly,
  the HTML formatting in rust wasn't horrible for our strongly typed
  data models, but a big change here is moving to having a generic,
  extensible pipeline for the JSON ingestion, and it is a major
  boilerplate nightmare to deal with un-typed JSON in the rust code.
  Also our existing HTML rendering felt like it was really at its
  scaling limits and could not reasonably allow, for example, webkit
  to customize stuff without interfering with mozilla-central.
- A related change to that is that we also use liquid templating for
  the WPT dashboard link.  This is potentially a baby step to moving
  some other panels too, but it's not a high priority.
- I added a `liquid-templating-cheatsheet.md` file since, while liquid
  as a templating language is pretty sane and the `liquid-rust` crate
  is amazing (thank you liquid-rust team, you rock!!), there are still
  some rough edges.  (And I think we can probably help improve the
  rust crate if we want to improve the situation.  It's really well
  engineered.)
- I have standardized our use of Ustr at least in crossref so that
  any file path, file path segment, symbol, or pretty identifier
  string is expected to be a Ustr.  Part of this logic is being
  careful to not try and intern a string into a Ustr until we're sure
  that it actually corresponds to something that should be interned.
  For example, if we get symbols from a query, we try and look them up
  from our crossref database first and then we only intern the string
  if it matched.
   - This is done primarily the benefit of graph processing and our
     future work in that space where there are potentially quite
     significant performance and resource wins from being able to do
     fast equality tests and have pre-computed hashes.
- cmd_search_files and the local index remote server and its backend
  have been changed to operate off of the concise info database which
  we eagerly load into memory.  The search-files results will now
  contain all the concise info we have on a file, but we still have a
  separate detailed info for larger hunks of data that only need to be
  available when rendering the file or at other times when it makes
  sense to load it as needed.
- The tentative plan has also been to include the file information in
  the crossref database under the `FILE_` symbol for consistency, but
  that was mainly something I thought was reasonable when I wasn't
  sure whether we should still have the concise-per-file-info.json
  file or not and load it at the start of the server.  But in the end
  it seemed clear that our file searching patterns could benefit from
  pre-computation/indexing of any relevant queries, and just loading
  a flat file from disk is going to be faster to feed that than doing
  N binary searches in the crossref, etc. etc.
   - It could still make sense to store the information in the
     crossref info for the files, but tha can be implemented as
     needed.

---
## [AcademySoftwareFoundation/OpenShadingLanguage](https://github.com/AcademySoftwareFoundation/OpenShadingLanguage)@[e4e5088ed6...](https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/commit/e4e5088ed6dcd4eb636430dcce9fe815e435b1a6)
#### Saturday 2022-10-01 00:12:00 by Larry Gritz

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
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[1eab5a8364...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/1eab5a8364114dce9f63c97852461b6e4f27d7b0)
#### Saturday 2022-10-01 00:44:58 by SkyratBot

[MIRROR] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix [MDB IGNORE] (#16486)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

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

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tastyfish <crazychris32@gmail.com>

---
## [RCP-2001/Compilers](https://github.com/RCP-2001/Compilers)@[775c43d399...](https://github.com/RCP-2001/Compilers/commit/775c43d39958cae0d5556bff6f7b9343b7546ceb)
#### Saturday 2022-10-01 01:12:07 by RCP-2001

Got some troubles that these drugs cant fix.
We might struggle because life's a bitch
and your happy when yo ass get rich

---
## [IN2-Moist/2Take1-Moist-Script](https://github.com/IN2-Moist/2Take1-Moist-Script)@[e7302080bb...](https://github.com/IN2-Moist/2Take1-Moist-Script/commit/e7302080bbbd1ddd45bdec43fa1d04b345174bd8)
#### Saturday 2022-10-01 01:17:00 by IN2_Moist

3.0.0.4

Updated 2.0.6.8 Included

Fixed: Frame Lag caused by Player History saving to file

Update: Train Mod - Will now toggle on enable train spawn with it off or when you have switched session to prevent any self crashes

Added: Session Griefing

  MultiDirectional Player Snipe : <Distance value Modifier>

  Updated: Grief Others (Frame Player)
        Framed Session Orbital Strike & Orbital Player:
          Both Now use Actual Orbital Cannon Sounds, PTFX and Explosions.

  Added: Script Events
        Remove GOD Mode!
            Script event to attempt removal of god mode

  Updated/Added: Unlock Minimap Zoom
    Toggle enables Zoom and unhides a Value Modifier with manual input when value is not changed and activated a second time,
    precision modifier value used now.

  Added: Player Options
    Player Waypoint
       While Toggled on updates the Waypoint to the players location

Added: Settings

  Get Player Killers
    WIP Rework of my old Combat tracker currently only gives a notifty of who killed who if it was a player

  Auto Whitelist Friends
    Toggles on the Manual Modder Detection Whitelist option on friends

  Enable Sub Missile Detection
     Does as the name states, detects any missile launch and adds a blip on radar/map when in range of you

  Enable RC Vehicle Detection
     Again Name says it all Detects Activation of RC Tank & RC Bandito also adds [RC] tag to the players name in the player bar

  Log Session Joins
      Outputs a daily Session Player Join CSV with all their info

  Anti Orbital Protection
        No Function Yet this is built into the main script for now and will disable any players ability to use the orbital cannon on you
        while they are in the orbital room. They just will never find you in the player list preventing any orbital.

  Added: Entity Functions & Tools

  Added: Try to Cleanup Script Spawns & blips
      Removes any entities created by script functions & any Blips if Control over them can be achieved

  Added: Cleanup Session World
      Attempts to clean the world of all entities using 2 native methods (quick removal) followed by Moists Method which will take a little longer but will try to remove it outside of the map to delete it.

  Update: Portable Defence Spheres
     All Function Names Updated

  Added: Waypoint Anti Player Ped
     Sets a Defence Sphere at current way points location

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[bdfccf66a4...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/bdfccf66a44e9d970f772e3946c266595986b839)
#### Saturday 2022-10-01 01:32:10 by silicons

[MDB IGNORE] erases d1/d2 varedits from *most* cables (#4463)

* e

* e

* e

* more

* y'all weird

* fuck you

* FUCK YOU THE INTEGRATION TEST IS GOING ON

* fine that goes off

Co-authored-by: VM_USER <VM_USER>

---
## [Cyborg2017/android_kernel_nubia_sdm660-oss](https://github.com/Cyborg2017/android_kernel_nubia_sdm660-oss)@[1ed008ab3e...](https://github.com/Cyborg2017/android_kernel_nubia_sdm660-oss/commit/1ed008ab3efb470a969c9410a8bc3616cf89e7bb)
#### Saturday 2022-10-01 03:17:52 by Christian Brauner

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
## [Wyste/hekili](https://github.com/Wyste/hekili)@[6023ecd8b5...](https://github.com/Wyste/hekili/commit/6023ecd8b56aad73c9b5a3bd5c53aabab94a4290)
#### Saturday 2022-10-01 05:00:18 by Wyste

Update prot war for build 45779

- Talents regenerated from skeleton
- Avatar from 20 to 15 rage gen
- Thunderous roar gens 10 rage (was previously nothing in my version, but should have been 20)
- Piercing Verdict talent modifies Spear of Bastion ability:  went from 50% extra rage gen to 100%
- Shield Slam now gets CD reduction from Honed Reflexes
- Pummel now gets CD reduction from Honed Reflexes (in addition to Concussive Blows too!)

Renames:
- Outburst (talent) renamed to Violent Outburst ( verified spellID did not change )
- Quick Thinking renamed to Wild Strikes (talent)
- The Wall renamed to Impenetrable Wall (talent)
- Spiked Shield renamed to Tough as Nails (talent)
- Siphoning Strikes renamed to Leeching Strikes (talent)

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[7c6fb70c1e...](https://github.com/rust-lang-ci/rust/commit/7c6fb70c1efe59fbf97066f1e7b756fe0cef5ef9)
#### Saturday 2022-10-01 06:37:10 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [Biki-das/react-1](https://github.com/Biki-das/react-1)@[b6978bc38f...](https://github.com/Biki-das/react-1/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-10-01 07:03:54 by Andrew Clark

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
## [baala7781/EMOTIONAL-INTELLIGENCE-QUOTIENT-PREDICTION-IN-RECRUITMENT-PROCESS](https://github.com/baala7781/EMOTIONAL-INTELLIGENCE-QUOTIENT-PREDICTION-IN-RECRUITMENT-PROCESS)@[39eb2a74f3...](https://github.com/baala7781/EMOTIONAL-INTELLIGENCE-QUOTIENT-PREDICTION-IN-RECRUITMENT-PROCESS/commit/39eb2a74f36ef90c5a1d3514220c63ee29857070)
#### Saturday 2022-10-01 07:07:34 by S BALASAGAR GOUD

Note: Use Jupyter Notebook; it is effective.

 Steps to run the code:

  #Step 1

 By executing the following pip instructions in a jupyter notebook environment, you can import all of the aforementioned modules. 
                 pip install numpy
                 pip install pandas 
                 pip install tkinter 
                 pip install sklearn 

 #Step2  

Then execute the section 1 code in a fresh Jupyter notebook cell. The reading, loading, and modification of the data set are all contained in this Section 1 code. also educating the model.  

 #Step 3  

Then execute section 2 code in the newly created cell that is interfaced to take the test and provide the necessary data.      
fill the given fields first (age,area,age)       
         Age should be between 22-19      
         Area should be either Rural or Urban       
        Gender should be Male or Female 
        after filling the details click submit  
note: don't forget to click after immediate filling of details then take the following psychometric test(15 Questions) 
note: Answer the questions with the understanding that a fresher will be taking the test. then close the gui   

Step 4:

 run the section 4 code in new cell  which is having testing part and finding accuracy of the model  

Step 5:

 then Run the next section code that is section 5. which opens a new GUI which will display the predicted emotional intelligence quotient of a person.

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[f0ceecff46...](https://github.com/Gofawful5/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Saturday 2022-10-01 07:15:35 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[e7230e8b4a...](https://github.com/Gofawful5/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Saturday 2022-10-01 07:15:35 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Prashant-Bhapkar/free-programming-books](https://github.com/Prashant-Bhapkar/free-programming-books)@[5fd70502a0...](https://github.com/Prashant-Bhapkar/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Saturday 2022-10-01 09:26:30 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[d34fa4c642...](https://github.com/vincentiusvin/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Saturday 2022-10-01 10:23:16 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [searayeah/HSE-micro](https://github.com/searayeah/HSE-micro)@[cffd388b18...](https://github.com/searayeah/HSE-micro/commit/cffd388b18cf5fd2e83c7ca7d1503d6d3056fd2b)
#### Saturday 2022-10-01 10:32:29 by searayeah

FUCKING BULLSHIT SHIT I FUCKING CANT DO  THIS ANYMORE THIS IS INSANE

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[8a54f55b25...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/8a54f55b250f882929d29ea69f80317fe6df79f2)
#### Saturday 2022-10-01 11:42:31 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Albert I <kras@raphielgang.org>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [Lord-KA/tarantool](https://github.com/Lord-KA/tarantool)@[66ca6252c4...](https://github.com/Lord-KA/tarantool/commit/66ca6252c428ca7a369e24faaa833e3520e809d6)
#### Saturday 2022-10-01 12:09:27 by Alexander Turenko

console: don't mix stdout/stderr with readline prompt

The idea is borrowed from [1]: hide and save prompt, user's input and
cursor position before writing to stdout/stderr and return everything
back afterwards.

Not every stdout/stderr write is handled this way: only tarantool's
logger (when it writes to stderr) and tarantool's print() Lua function
performs the prompt hide/show actions. For example,
`io.stdout:write(<...>)` Lua call or `write(STDOUT_FILENO, <...>)` C
call may mix readline's prompt with actual output. However the logger
and print() is likely enough for the vast majority of usages.

The readline's interactive search state (usually invoked by Ctrl+R) is
not covered by this patch. Sadly, I didn't find a way to properly save
and restore readline's output in this case.

Implementation details
----------------------

Several words about the allocation strategy. On the first glance it may
look worthful to pre-allocate a buffer to store prompt and user's input
data and reallocate it on demand. However rl_set_prompt() already
performs free() plus malloc() at each call[^1], so avoid doing malloc()
on our side would not change the picture much. Moreover, this code
interacts with a human, which is on many orders of magnitude slower that
a machine and will not notice a difference. So I decided to keep the
code simpler.

[^1]: Verified on readline 8.1 sources. However it worth to note that
      rl_replace_line() keeps the buffer and performs realloc() on
      demand.

The code is organized to make say and print modules calling some
callbacks without knowledge about its origin and dependency on the
console module (or whatever else module would implement this interaction
with readline). The downside here is that console needs to know all
places to set the callbacks. OTOH, it offers explicit list of such
callbacks in one place and, at whole, keep the relevant code together.

We can redefine the print() function from every place in the code, but I
prefer to make it as explicit as possible, so added the new internal
print.lua module.

We could redefine _G.print on demand instead of setting callbacks for a
function assigned to _G.print once. The downside here is that if a user
save/capture the old _G.print value, it'll use the raw print() directly
instead of our replacement. Current implementation seems to be more
safe.

Alternatives considered
-----------------------

I guess we can clear readline's prompt and user input manually and don't
let readline know that something was changed (and restore the
prompt/user input afterwards). It would save allocations and string
copying, but likely would lean on readline internals too much and repeat
some of its functionality. I considered this option as unstable and
declined.

We can redefine behavior for all writes to stdout and stderr. There are
different ways to do so:

1. Redefine libc's write() with our own implementation, which will call
   the original libc's write()[^2]. It is defined as a weak symbol in
   libc (at least in glibc), so there is no problem to do so.
2. Use pipe(), dup() and dup2() to execute our own code at
   STDOUT_FILENO, STDERR_FILENO writes.

[^2]: There is a good article about pitfalls on this road: [2]. It is
      about LD_PRELOAD, but I guess everything is very similar with
      wrapping libc's function from an executable.

In my opinion, those options are dangerous, because they implicitly
change behavior of a lot of code, which unlikely expects something of
this kind. The second option (use pipe()) adds more user space/kernel
space context switches, more copying and also would add possible
implicit fiber yield at any `write(STD*_FILENO, <...>)` call -- unlikely
all user's code is ready for that.

Fixes #7169

[1]: https://metacpan.org/dist/AnyEvent-ReadLine-Gnu/source/Gnu.pm
[2]: https://tbrindus.ca/correct-ld-preload-hooking-libc/

NO_DOC=this patch prevents mixing of output streams on a terminal and it
       is what a user actually expects; no reason to describe how bad
       would be his/her life without it

---
## [ThatHypedPerson/jChat](https://github.com/ThatHypedPerson/jChat)@[560de26c07...](https://github.com/ThatHypedPerson/jChat/commit/560de26c076ff3351cfeec58072f8198d35cfbe7)
#### Saturday 2022-10-01 13:16:52 by ThatHypedPerson

Implement YouTube chat messages.
OH MY GOD IT WORKS HOLY
i mean yeah i expected that
need to do some further testing and distinguish yt and twitch messages, but other than that it works so well

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a5bd83b7a3...](https://github.com/treckstar/yolo-octo-hipster/commit/a5bd83b7a352868b9ff5398116d052f744adb524)
#### Saturday 2022-10-01 13:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[428dfbfefb...](https://github.com/Conga0/Mo_Creeps/commit/428dfbfefb220ba8d10103b40c1e108ee3ce7641)
#### Saturday 2022-10-01 14:24:41 by Conga Lyne

New Creep, various balance changes, new settings

Updated Big Tentacler's sprite to not jitter
Updated music stone & other music related items to be more mod compatible.
Optimised ghosts.
Added option to toggle Conjurer Compatibility mode (on by default)
Added optional message of the day
Some enemies who sucked at hitting you now attempt to predict movement
Hisii Engineers are now smarter
Holy Orbs should now pierce through projectile immunity if they didn't already
Increased Big Tentacler's spawn chance in Fungal Caverns
Fixed incorrect Tentacler being spawned in Overgrowth
Further adjusted rare enemy spawns in Fungal biomes
Updated Rocket Shotgun Hisii's sprite again
Fixed Tesla Turret committing hate crimes against Hisii kind
Fixed Tesla Turret having low health in the power plant.
Slightly buffed Mini Drone in Power Plant.. They felt somewhat fragile in comparison to other Power Plant enemies.
Slightly reduced chance for Wand of Wonders to appear in overgrowth wand pedestals.
Slightly reduced big tentacler's health in the fungal caverns

New Creep: Greater Swampling

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[f8d776887d...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/f8d776887df96eda9762c89bf7aec5b7be75b308)
#### Saturday 2022-10-01 16:06:06 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [Reycko/FNFBot](https://github.com/Reycko/FNFBot)@[524b0208df...](https://github.com/Reycko/FNFBot/commit/524b0208dfd8ce9852d941a6ac2584cf3f12dd01)
#### Saturday 2022-10-01 16:31:32 by Kade M

Merge pull request #54 from Kiffolisk/patch-5

to people who make useless issues: fuck you all

---
## [Barefooot/wus.U5R2.mods](https://github.com/Barefooot/wus.U5R2.mods)@[d825211ad1...](https://github.com/Barefooot/wus.U5R2.mods/commit/d825211ad19281a5f21df7a79bca536b85dbd596)
#### Saturday 2022-10-01 16:43:23 by Barefoot

(Major) Updates 220930

- Buyer 🪙 merchant removed. REASON: collides with DUSK-Combat, we can live without it, but DUSK is a must, so...
++ DUSKombat ⚔️ works and enabled
-- Skill can be lost on death 💀  - please use resurrection 💎 stones to prevent death skill 🤹  lost (please check the mod-setup regards).

+ Armoury 🛡️ enabled: enableItemMaterialChanges, enableWeaponMaterialChanges
-- sickle damage fixed to be same as small-axe 🪓

+ Alchemy 🍶

+ Awakening-Mod
++ can now Lower-Cave-Ceiling
++ using Leaderboard 📋 which is more PvP style (Wyvern Leaderboard disabled).
++ Player-body-Settings:
+++ can enable PvP  so others will know you are PvP-player.
+++ Mayer can setup his deed to Farm-Growth-When-Tended or per server-farm-tick.
++ Farm-tick 👩‍🌾 is relative to Midnight-GMT (server-resets won't affect farm-ticks, only server-time).
++ Offspring-Names of any breed-animal.
++ Kingdoms-May-Ally against common enemy 👑 .
++ Prevent dropping dirt to pass dirt walls or moats 🌉  . Instead, raiders have to use siege engines ♈ and climb dirt walls, which makes warfare more historically realistic (good deed anyway have closed-reinforced-mine-doors to do the same)..
-- preventing willows 🌲 and oak to kill all trees in the area and spread infinitely - taking over the whole map given time.
++ Can now Allow-Everyone in permissions, so even enemy can enter (mostly for GM 🙂 special places ).
++ Highway roads 🛣️ need to be blessed by priests to be operational, and now powered by the gods favor (need to bless cats-eye and way-stone.
++ Server-Lags 🕑 will be reported when detected.
++ Locks 🔐 of abandoned carts/boats/houses (45-days owner didn't logged) will start decay, and when 100-damaged will be removed so others can loot/claim them, carts/ships with no lock can be commanded to become the new owner.

+ auto pollDepotTime per ~7d6h, so if GM forgot - it'll spawn randomly in the world.
- enableBountyModule=false, was true -> damage player items on death FIXED!!
- Summer-Hats ⛑️ removed from craftables (and inventory) - too easy to make and traders-costly,  can get HQ ones from skull/medallion-traders
+ hand-Mirror 🪞 added to traders, so one can change his look (hair-cut, facial-hair change and such.. - 10s
+ increasedLegendaryFrequency=3 (was x2)

-- Removed some leftover prop-files.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[91f02f2a6b...](https://github.com/tgstation/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Saturday 2022-10-01 16:47:54 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [Shadowy888Hacker/ShadowHacker](https://github.com/Shadowy888Hacker/ShadowHacker)@[191fa05d09...](https://github.com/Shadowy888Hacker/ShadowHacker/commit/191fa05d09138ba105660a476057316ae1ce24b3)
#### Saturday 2022-10-01 17:15:10 by Shadowy888Hacker

I will hack all of you who have read this message and expose nall your secrets you have. Especially the lesbian girls and the gay boys in our our school. We don't entertain this kind f shit in our school. Let dram begin. I am going to expose all kind of secrets including those who have more than 2 boyfriends and girlfrinds. As long as i have your number i wil be going to unleash the drama. Join the whatsapp i created. I will share the link on various whatsapp groups

---
## [FlacoFF/test_tgstation](https://github.com/FlacoFF/test_tgstation)@[ee1aba7a32...](https://github.com/FlacoFF/test_tgstation/commit/ee1aba7a32d73a32694fcf904e166e7985df6676)
#### Saturday 2022-10-01 17:41:11 by John Willard

pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[6f99bd4d2d...](https://github.com/GeoB99/reactos/commit/6f99bd4d2d693213a3d2048132c4f54bd66c60b2)
#### Saturday 2022-10-01 18:07:49 by George Bișoc

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
## [ThakaSartu/huma](https://github.com/ThakaSartu/huma)@[1aff1764ca...](https://github.com/ThakaSartu/huma/commit/1aff1764cabf32a7518b198ed614730d28dd9031)
#### Saturday 2022-10-01 18:12:31 by ThakaSartu

[![.github/workflows/ci.yaml](https://github.com/pages-themes/hacker/actions/workflows/ci.yaml/badge.svg)](https://github.com/pages-themes/hacker/actions/workflows/ci.yaml)

# Quran: 4. Surat An-Nisa (The Women)

```
وَإِنْ خِفْتُمْ أَلَّا تُقْسِطُوا۟ فِى ٱلْيَتَـٰمَىٰ فَٱنكِحُوا۟ مَا طَابَ لَكُم مِّنَ ٱلنِّسَآءِ مَثْنَىٰ وَثُلَـٰثَ وَرُبَـٰعَ ۖ فَإِنْ خِفْتُمْ أَلَّا تَعْدِلُوا۟ فَوَٰحِدَةً أَوْ مَا مَلَكَتْ أَيْمَـٰنُكُمْ ۚ ذَٰلِكَ أَدْنَىٰٓ أَلَّا تَعُولُوا۟
```
```
وَٱبْتَلُوا۟ ٱلْيَتَـٰمَىٰ حَتَّىٰٓ إِذَا بَلَغُوا۟ ٱلنِّكَاحَ فَإِنْ ءَانَسْتُم مِّنْهُمْ رُشْدًۭا فَٱدْفَعُوٓا۟ إِلَيْهِمْ أَمْوَٰلَهُمْ ۖ وَلَا تَأْكُلُوهَآ إِسْرَافًۭا وَبِدَارًا أَن يَكْبَرُوا۟ ۚ وَمَن كَانَ غَنِيًّۭا فَلْيَسْتَعْفِفْ ۖ وَمَن كَانَ فَقِيرًۭا فَلْيَأْكُلْ بِٱلْمَعْرُوفِ ۚ فَإِذَا دَفَعْتُمْ إِلَيْهِمْ أَمْوَٰلَهُمْ فَأَشْهِدُوا۟ عَلَيْهِمْ ۚ وَكَفَىٰ
```

Indeed, those who unjustly consume orphans’ wealth ˹in fact˺ consume nothing but fire into their bellies. And they will be burned in a blazing Hell!

إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَـٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا

Give orphans their wealth ˹when they reach maturity˺, and do not exchange your worthless possessions for their valuables, nor cheat them by mixing their wealth with your own. For this would indeed be a great sin.

If you fear you might fail to give orphan women their ˹due˺ rights ˹if you were to marry them˺, then marry other women of your choice—two, three, or four. But if you are afraid you will fail to maintain justice, then ˹content yourselves with˺ one1 or those ˹bondwomen˺ in your possession.2 This way you are less likely to commit injustice.

Do not entrust the incapable ˹among your dependants˺ with your wealth which Allah has made a means of support for you—but feed and clothe them from it, and speak to them kindly.

Test ˹the competence of˺ the orphans until they reach a marriageable age. Then if you feel they are capable of sound judgment, return their wealth to them. And do not consume it wastefully and hastily before they grow up ˹to demand it˺. If the guardian is well-off, they should not take compensation; but if the guardian is poor, let them take a reasonable provision. When you give orphans back their property, call in witnesses. [And sufficient is Allah as a ˹vigilant˺ Reckoner.](https://aleteia.org/2017/09/01/10-bible-verses-that-will-enable-you-to-place-your-problems-in-gods-hands/)


 [![Gem Version](https://badge.fury.io/rb/jekyll-theme-hacker.svg)](https://badge.fury.io/rb/jekyll-theme-hacker)

---
## [Tiktodz/kernel_asus_sdm660](https://github.com/Tiktodz/kernel_asus_sdm660)@[c12fb8997e...](https://github.com/Tiktodz/kernel_asus_sdm660/commit/c12fb8997e5d8a08ab480c43b487f5e2cc204513)
#### Saturday 2022-10-01 18:42:36 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Change-Id: Iac0a8b6392036e35509a609ee0800301915a885e
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [Ne1ran/Chemistry-Modeling](https://github.com/Ne1ran/Chemistry-Modeling)@[e759a8f8e2...](https://github.com/Ne1ran/Chemistry-Modeling/commit/e759a8f8e2559f9a3cb64c5d0aa50572ea7c57a7)
#### Saturday 2022-10-01 19:12:59 by Neiran

I... conceded thinking of normalising of DB. I created another table, modified it and used. Now, when experimentScreen opens up it gets info from DB about substances it uses and uploads there textures with rectangles on the field. Work nearly from the first time (third, silly mistake). I am honestly impressed. Also added a bunch of constants and some methods in dbhandler.

---
## [santirona/tp4](https://github.com/santirona/tp4)@[6dda2d1ae1...](https://github.com/santirona/tp4/commit/6dda2d1ae192c220037fd08252fa28027f2e8545)
#### Saturday 2022-10-01 19:19:05 by santirona

ITS FUCKING DONE BITCH LAST TP OF THE YEAR LETS FUCKING GO DALE QUE SOMOS INGENIEROS PAPA NUNCA DUDES DE VOS MISMO JAMAS

---
## [GrodanBool/Outrun-Steam-Deck-Theme](https://github.com/GrodanBool/Outrun-Steam-Deck-Theme)@[3ad7aa06a6...](https://github.com/GrodanBool/Outrun-Steam-Deck-Theme/commit/3ad7aa06a637a18ec1a9b2df326873067d4b4e0e)
#### Saturday 2022-10-01 20:47:30 by GrodanBool

added colors, beta 1.1 commence

god i hate myself

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[c0a07b7b4e...](https://github.com/san7890/bruhstation/commit/c0a07b7b4efa129e6280dc22f35d96261481c61f)
#### Saturday 2022-10-01 21:48:23 by san7890

TOML System Mega-Commit

* Implements the TOML System (warning, uses unreleased rust-g.dll. I'll update this in a later commit and bump dependencies.sh)

* Implements jobconfig.toml! Also includes validation for this file on SSconfiguration's initialize, very nifty.

* Code will now respect the non-existence of jobconfig.toml and will no longer write to the `config/` directory at all. Instead, we will send an FTP prompt when someone runs the verb to generate the TOML file (because editing this shit manually sucks fucking cock and balls), and that'll still migrate from older versions of jobconfig.toml / jobs.txt

* Adds admin verb to generate the TOML file. Please let me know if you want it in a different category.

* That should be it? Let me know if there's some critical feedback that I missed out on that I should listen to. I'm starting to approach the end of passion for this project, and I don't know how much longer I can soldier though.

---
## [Eugene1qd2/FreelancePlatform](https://github.com/Eugene1qd2/FreelancePlatform)@[2a6edb8e65...](https://github.com/Eugene1qd2/FreelancePlatform/commit/2a6edb8e655b200db41bdb94521c3efc450abd9e)
#### Saturday 2022-10-01 22:46:19 by Eugene

Remade EnterWindow.
Started MVVM structure.
Dear diary, I cannot put into words the pain of disappointment in WPF technology and MVVM structure. I've never been so wrong. I sincerely repent. I have already redone all the styles for the umpteenth time, just so that the login form works. May Microsoft bless me for completing this fucking project.

---

