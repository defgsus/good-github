## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-19](docs/good-messages/2023/2023-02-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,847,144 were push events containing 2,561,382 commit messages that amount to 143,157,729 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[a2295b2b04...](https://github.com/timothymtorres/tgstation/commit/a2295b2b049ba3c77186ffb0eaacb507c001cdc8)
#### Sunday 2023-02-19 00:00:19 by LemonInTheDark

Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode. 
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible. 
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

---
## [FRC2240/ChargedUp2023](https://github.com/FRC2240/ChargedUp2023)@[77a7092868...](https://github.com/FRC2240/ChargedUp2023/commit/77a709286881c5fa52f1adaa5d177f193d4f7342)
#### Sunday 2023-02-19 00:33:12 by Cynosure-Null

vision refactor or how i had a coconut mall pain

omg i love ikea shork

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

 On branch circular_buffer
 Changes to be committed:
	modified:   src/main/cpp/Vision.cpp
	modified:   src/main/include/Constants.h
	modified:   src/main/include/Vision.h

Depointering

help the pointers poke me ow

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

NFC: reordered files

Debugged raw data

It now gets the raw data & is confirmed to work

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

Added Erik's vector-based fixes

refactored to involve moar vectors

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

forgive me mr stroustrup for i have sinned

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

rebase: cout, increments, and the revival of disco

god help me im delirious
but im stayn alive

oh i also fixed a lot of segfaults
and added a bunch of couts

help its too many couts

btw it segfaults

-- Commit made by segmentation fault (core dumped)
 Changes to be committed:
	modified:   src/main/cpp/Robot.cpp
	modified:   src/main/cpp/Vision.cpp
	modified:   src/main/include/Constants.h
    modified:   src/main/include/Robot.hpp
	modified:   src/main/include/Vision.h

debugging watchdog

Pre stdev testing

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

mid testing

turns out my sheet was wrong

rebase: drivebase size

mid drive testing

vision testing. Pre firmware update

Vision testing

Added a bunch of logs, removed some couts and other things

When static, bot is off by *under a centimeter*

Needs more testing

My PGP key can be found on my github profile
Fly safe

---
## [katzenpost/katzenpost](https://github.com/katzenpost/katzenpost)@[fdd469af43...](https://github.com/katzenpost/katzenpost/commit/fdd469af43e1346f16b0b62fb27ab04de89a6a3a)
#### Sunday 2023-02-19 00:43:23 by David Stainton

bump golang.org/x/net from 0.4.0 to 0.7.0 (#236)

fucking dependabot fixed some irrelevant shite we don't even use but i'mma go ahead and merge this shit anyway, dog.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[6ebdfdc73f...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/6ebdfdc73f233d94bcc6c4a2f72d902af868583f)
#### Sunday 2023-02-19 00:58:31 by SkyratBot

[MIRROR] Makes Shake() proc work [MDB IGNORE] (#19424)

* Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

* Makes Shake() proc work

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [PrimedPixel/ProgrammingProject](https://github.com/PrimedPixel/ProgrammingProject)@[c400896b7c...](https://github.com/PrimedPixel/ProgrammingProject/commit/c400896b7cf5cf453dbd509f209d73bb78e96905)
#### Sunday 2023-02-19 00:58:38 by Malachy Moran-Tun

HOLY FUCKING SHITTING HECKING I'VE DONE IT

he's only gone and done it
thanks reddit

thanks for the gold kind stranger!

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[9424eb53a1...](https://github.com/DaedalusDock/daedalusdock/commit/9424eb53a1780ce0ff21629bba8e3288d26a9a63)
#### Sunday 2023-02-19 01:14:07 by Kapu1178

Removes Field of View and returns everything to the GAME_PLANE (#209)

* Fuck you superlayers

* re-add the blindness effects

* Fix holosigns

---
## [TheLordME/Citadel-Station-13-RP](https://github.com/TheLordME/Citadel-Station-13-RP)@[81c1229373...](https://github.com/TheLordME/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Sunday 2023-02-19 01:28:57 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[74144f2bc9...](https://github.com/Ryll-Ryll/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Sunday 2023-02-19 01:43:55 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[39f1e8d7e7...](https://github.com/clintjedwards/gofer/commit/39f1e8d7e739a41da1a45a828c06630cde59d6fd)
#### Sunday 2023-02-19 01:57:04 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [Nanhumly/android_kernel_zuk_msm8996](https://github.com/Nanhumly/android_kernel_zuk_msm8996)@[f8fa30d37e...](https://github.com/Nanhumly/android_kernel_zuk_msm8996/commit/f8fa30d37e7457c3f8ec196f2f946260b2d9d11b)
#### Sunday 2023-02-19 02:53:20 by Christian Brauner

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
## [R3P41RM4N/R3c0nB3AR](https://github.com/R3P41RM4N/R3c0nB3AR)@[e9a79d50b0...](https://github.com/R3P41RM4N/R3c0nB3AR/commit/e9a79d50b0f4611cd4dc27962f9ea21d8bad4235)
#### Sunday 2023-02-19 03:27:00 by R3P41RM4N

Update rb.py

Notes for Ben: It took me a bit, but I got the application to parse our the headers as well as the CSP. Changes the colors to something more readable (Green), Labelled the headers, and basically was prettying it up. 

Would love your thoughts on how we can improve it and also what other apps we should add. I did fix the output to log issue vs. what's displayed on the terminal. It's not pretty, but it works. Basically I f.write and then go back and print(). That's where I left off with it. It's connecting to burp now and I think we're close to just tweaking it for basic webapp reconaissance. 

One of my friends suggested using a wordpress app as well.

---
## [Ownwn/OwnwnAddons](https://github.com/Ownwn/OwnwnAddons)@[2d2e18bc53...](https://github.com/Ownwn/OwnwnAddons/commit/2d2e18bc53b8572d94896ebdd23fb1e6649ef0a3)
#### Sunday 2023-02-19 03:51:59 by Owen

Oh Mixins, how lovely you are
Your influence is felt near and far
Thanks to you, Oneconfig's in a bind
And its failure to load has me losing my mind

I'm so grateful for your meddling ways
You've added complexity to my days
I love how you make debugging a breeze
And how you always keep me on my knees

Who needs a functional system that runs?
When we can have Mixins, oh so fun!
With their subtle quirks and hidden flaws
That make our code fail without pause

So here's a big thank you to you, Mixins
For causing chaos and all its sins
I appreciate the extra work you've given
And the headaches that come from fixing

So let's raise a glass to Mixins, hooray!
For complicating our lives in every way
We couldn't have done it without you
And for that, we're forever in your debt, it's true.

- updated some stuff

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[26688597e3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Sunday 2023-02-19 04:06:06 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [jtv/libpqxx](https://github.com/jtv/libpqxx)@[2ce7b64e2c...](https://github.com/jtv/libpqxx/commit/2ce7b64e2cf96c28f3d441831a56f9e2df601960)
#### Sunday 2023-02-19 04:25:48 by Jeroen T. Vermeulen

Clean up a bit more.

Eliminated the `fields` array — unescape one field at a time, and parse
immediately after, so we never need to keep track of more than one field
at a time.

This also simplifies the folding magic for "iterating" the fields.
Truth be told I never really got how the indexing worked anyway, when it
came to the template trick for the index sequence.  That's all gone now.
I just fold over the field types, and that's that.

Along the way, some awkward small-scale code duplication went out the
window as well.  It feels a bit more sensible to me now.

One thing I'm not _quite_ sure about is the way I mixed two styles of
in-out parameters: at a lower level I use a static member function that
returns modified versions of its arguments, but then at a higher level I
need to pass the values by reference to propagate the side effects in my
folding expression.

Modifying pass-by-reference parameters is ugly, but also, there's always
the worry that the optimiser may no longer be able to figure out what's
going on.  In which case, it may synchronise the values unnecessarily
often, or it may miss rescheduling opportunities for loads and stores,
and so on.

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[558717e6f6...](https://github.com/Segrain/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Sunday 2023-02-19 05:12:23 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

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

github

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
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[4ce115a2a2...](https://github.com/Segrain/cmss13/commit/4ce115a2a26f8b6664a230bdaff483a1889f17c4)
#### Sunday 2023-02-19 05:12:23 by carlarctg

Adds Ludicrously In-Depth Black Market to Recquisitions. (#2014)

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

VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

Various valuable, rare, or otherwise interesting items now have a 'black
market value' that allows them to be sent down the ASRS elevator in
exchange for black market points to order various things with. Anything
that's 'rare' is probably worth something. Added a scanner to the black
market to let them detect said points.

Added DIALOGUE to the black market.

FIxed some construction wirecutter steps needing a screwdriver for some
reason.

Changed up Req's mapping to add a hidden storage room.

slightly changed human remains' description

Added the maintenance jack, can be found in the black market for now.

Improved supply shuttle code somewhat.

# Explain why it's good for the game

> VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Black Market is comically underused, by comically enhancing it like this
it will freshen shipside roleplay and create new and interesting
scenarios for MPs, req, and bystanders to interact with.

> Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

The contraband needs to be actually meaningful to the players for it to
have any impact. The list of loot has been curated so that players will
be intrigued, but will not be able to abuse it for
too-stronger-than-usual gear without blatant drawbacks.

> Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with. Added
a scanner to the black market to let them detect said points.

This means CTs could go on scavenger hunts through the ship, evading
curious MPs to sift through maintenance and various hidey holes scanning
everything.

> Added DIALOGUE to the black market.

Finally, we have dialogue in CM! The very first human NPC. We're
ignoring WO because nobody likes WO.

> FIxed some construction wirecutter steps needing a screwdriver for
some reason.

Necessary in this PR to avoid stupid confusion when deconstructing the
computers.

> Changed up Req's mapping to add a hidden storage room.

To let CTs hide their goodies so they won't be in open sight. NOT DONE
YET!

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
add: VASTLY enhances the Black Market. Black market items are obtainable
by deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.
add: Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...
add: Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with.
Anything that's 'rare' is probably worth something. Added a scanner to
the black market to let them detect said points.
add: Added DIALOGUE to the black market.
fix: FIxed some construction wirecutter steps needing a screwdriver for
some reason.
spellcheck: slightly changed human remains' description
add: Added the maintenance jack, can be found in the black market for
now.
code: Improved supply shuttle code somewhat.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: XSlayer300 <35091844+XSlayer300@users.noreply.github.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [brunchboy/cool-github-releases](https://github.com/brunchboy/cool-github-releases)@[26b4985941...](https://github.com/brunchboy/cool-github-releases/commit/26b49859417340b5c66142b535f3150a17b10700)
#### Sunday 2023-02-19 05:16:15 by James Elliott

Add initial_mrkdwn and replace_assets options. (#9)

* Add initial_mrkdwn and replace_assets options.

These are the last two features I need for this action to be perfect
for my current continuous deployment flow! I want to be able to
specify markdown to use as a template when creating the initial
release, but then be able to hand-edit it later, and be sure that my
edits will not be destroyed by future action runs. This new option is
a backwards-compatible way of achieving that. The old `body_mrkdwn`
option works the same as it always has, but you can now specify an
`initial_mrkdwn` value that is used only when creating a new release.
If you don't specify `initial_mrkdwn`, then `body_mrkdwn` is used
instead for the new release, and if neither was given, your standard
fallback string is still used.

But if you specify only `initial_mrkdwn` and no `body_mrkdwn`, then
the markdown text is only used for creating new releases, and existing
release descriptions are left unmodified.

The second argument, `replace_assets`, controls whether to do the new
feature you added this weekend. My jobs run in two different modes,
because they are based on the Maven package management system which is
the foundation of the Java world. Snapshot releases are works in
progress, and can be released many times. Their assets get updated
with each release. But a non-snapshot release is final, and its
artifacts _never_ change. So I want to replace assets when building
snapshot releases, but flag it as an error if anyone ever attemts to
replace assets for a non-snapshot release. And my jobs can determine
the kind of release from the most recent git tag.

* Remove redundant text

Sorry, I was up too late!

Co-Authored-By: Xotl <edgardo333@gmail.com>

* Fix input name

Nice catch, I should have reviewed this the next morning.

Co-Authored-By: Xotl <edgardo333@gmail.com>

Co-authored-by: Xotl <edgardo333@gmail.com>

---
## [jkunimune/elastik](https://github.com/jkunimune/elastik)@[3d3e7c2a75...](https://github.com/jkunimune/elastik/commit/3d3e7c2a75b242187b12f0e85c5230933a4ed1ec)
#### Sunday 2023-02-19 05:52:32 by Justin Kunimune

¡Éxito!

I removed the little backup function feature I had bilt into the minimization functions because it was going to be a paint to implement it in both (now that I have two minimize functions).  instead, I will simply call minimize twice.  it’s actually way simpler this way; I like the new system much better.

I also fixed a minor issue where the augmented objective function sometimes added +inf to -inf.

and now that I’ve done that, guess what?  It *works*!  that’s right, after exactly eight months since I first set up gradient descent, I’ve developd a tool capable of fitting a map into a rectangle just like I’ve always dreamed.  I can’t wait to tell my parents.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[9e981753ca...](https://github.com/lessthnthree/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Sunday 2023-02-19 06:16:13 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[a85c26b7d3...](https://github.com/PlagueVonKarma/kep-hack/commit/a85c26b7d31bed8c86573bb0724d0bc8d7d6f874)
#### Sunday 2023-02-19 06:25:37 by May Evans

LOTS of things

- Replaces the Old Rod with the Candy Sack, an item to evolve Meltan into Melmetal. Meltan and Melmetal aren't in yet.
- Improves Gym Leader and Elite Four AI by a lot. They still use items, they're just better. Fixes XSpecial use while we're at it; before, it didn't actually increase the stat...
- The Scarlet Book now takes up both shelves, one section for each Paradox Pokemon. I also moved the bookshelf so it looks nicer.
- Text in Celadon University has been reduced significantly, taking up less memory and being a bit more RBY-like. It has also been made more accurate (thanks to Daiginjo for translating my booklet!)
- The Magikarp researcher in Celadon University now gives TM Dragon Rage (no longer unused!)
- Added a guard for Mt. Moon Crater.
- Removed TrainerNamePointers, Blank Leader Name Code, and Dakutens/Hakutens using a guide published by YakiNeen.
- PP no longer uses a shitty graphic and is instead properly implemented into the font, optimising the status screen. Also displays in-battle which is kinda cool.
- Lorelei, Bruno, and Agatha now play the Gym Leader theme, not just Lance.

Still unsure how to fix Celadon University's trainers, all I know is a lot of the information should be taken from the Oak fight I did. The code is radically different and doesn't call trainer headers at all. You'll likely want to start from scratch.

The Mt. Moon Crater Guard's text is a little wonky, not sure what's up there. May have been from the way I accessed Mt. Moon in testing. Anyway, if you want to mess around feel free.

---
## [dallmeyer/jak-project](https://github.com/dallmeyer/jak-project)@[c249dbc437...](https://github.com/dallmeyer/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Sunday 2023-02-19 08:20:18 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [MeoClover/SoC](https://github.com/MeoClover/SoC)@[896f34d48d...](https://github.com/MeoClover/SoC/commit/896f34d48d75a9dba9017a46f9577778b9978fcc)
#### Sunday 2023-02-19 08:53:17 by Meo Clover

Meo's laptop: 2023-02-19 15:53:04

Affected files:
.obsidian/core-plugins.json
🍀 SoC Introduction/(Bản Việt) 👋 Chào mừng đến với SoC (hoặc không❔).md
🍀 SoC Introduction/(Eng ver) 👋 Welcome to SoC (or not❔).md
🍀 SoC Introduction/👋 Welcome to SoC.md
🍀 SoC/⏳ Time/⏰ Schedule/13022023.md
🍀 SoC/🌐 Space & Ordinary Matter/🔭 Astronomy (Profile)/🌍 Dwarf Planet (PD)/👩‍🎓 Student (S)/Flamingo Cody/Flamingo Cody.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/💔 Things I Hate/Words I Hate.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎤 Music List.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎼 All these years.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎼 Havana.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎼 Never be the same.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎼 Real friends.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/📔 Research/8) 🎵 Music/🎵 Music/🌟/Camila Cabello/🎼 She loves control.md
🍀 SoC/🌐 Space & Ordinary Matter/🧬 Particles/🕯️ Faith/List of Faith.sync-conflict-20230219-155106-HZLP7KE.md

---
## [stanalbatross/cmss13](https://github.com/stanalbatross/cmss13)@[b53c9f0531...](https://github.com/stanalbatross/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Sunday 2023-02-19 10:47:09 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

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

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [camptocamp/odoo](https://github.com/camptocamp/odoo)@[8f24aba86f...](https://github.com/camptocamp/odoo/commit/8f24aba86faf2639109b56887781b0daaf60be98)
#### Sunday 2023-02-19 11:00:51 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#111400

X-original-commit: 639cfc76ba259eea8f38284192017024809173b3
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3e99191a99...](https://github.com/TaleStation/TaleStation/commit/3e99191a9976cb0befab607d7a8fe3aa228422de)
#### Sunday 2023-02-19 11:13:28 by TaleStationBot

[MIRROR] [MDB IGNORE] Changeling Meteor event now breaks more gracefully and will absolutely make sure the changeling gets where it should (#4618)

Original PR: https://github.com/tgstation/tgstation/pull/73433
-----
## About The Pull Request

The changeling meteor now has makes sure that, in the event of a near
miss, meteor shield interception, or even a miner swatting it midair
with a pickaxe, it's stored changeling will reach the station.

If the meteor "dies", it will initiate an emergency eject sequence and
launch the changeling through space towards their destination. If
intercepted by a shield satellite, the stored changeling will be thrown
into the shield instead (because it's closer).

Is it silly? Yeah. Does it look dumb and put our fragile immersion at
risk? That too. Unfortunately, I really don't have any better ideas
beyond teleporting them to a nearstation turf and saying "yeah man the
bluespace did it".

Some code related to the meteor shields and how meteors shot at has been
shuffled around to better accommodate this. This may or may not function
as a framework for customizing how individual meteor types interact with
meteor shields.

Also, the changeling meteor no longer gives an achievement when you
examine it. You spawn INSIDE of the meteor after all, so examining it
shouldn't be cause for celebration.

## Why It's Good For The Game

Closes #73349.

Changelings getting absolutely vaporized before they can make landfall
(or missing the station entirely) is really funny, but it makes work for
the admins and takes away threat from the round (boring!).

## Changelog
:cl:
fix: Midround Changelings are now ejected from their meteor when
something bad happens, ensuring they reach the station.
/:cl:

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [siimsek/Lightning-Kernel](https://github.com/siimsek/Lightning-Kernel)@[53d97b79b9...](https://github.com/siimsek/Lightning-Kernel/commit/53d97b79b9207dcc0501807f6159d2e06717f1da)
#### Sunday 2023-02-19 11:42:26 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: Muhammed Ali Simsek <malisimsek17@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a1c5445dbf...](https://github.com/mrakgr/The-Spiral-Language/commit/a1c5445dbfc06681dc577f8ac3119a7130a400b8)
#### Sunday 2023-02-19 12:18:27 by Marko Grdinić

"11:15pm. https://pixabay.com/music/modern-classical-wind-troubles-the-water-138702/

This one is so good.

https://boards.4channel.org/g/thread/91617677
> 152334H's fork has fine tuning, getting rid of the audiobook speakers eating character voices, improving the quality massively. If you have the time to get Tortoise properly set up like this, 11 is basically fucking finished.

Hmmm...

2/19/2023

9:10am. Today's night was crap. I went to bed late, got up really early, and must have been lounging in bed for a while, thinking intensely about my future.

Any mail? Nothing.

9:20am. I don't know. What is winning and what is losing in this world anymore?

Sigh...if I knew it would have turned out this way, I'd have become a web dev from the start. It feels like the world is doing its best to humiliate me. Web dev? In the prelude to the Singularity? Because ML is too useless to do anything I'd want with it? Because how good you are it is only dependent on the size of your wallet?

9:50am. This world fucking suuuuuuucccckkkssss!!!

Just why can't my feelings guide me towards victory? I wish I had started with what I am doing now and left ML and trading for later.

9:50am. Forget complaining. Let me resume the React course.

I want to give up. I guess the only thing matters in life are those things you can get with your own hands.

I am going to get these frontend and backend skills and put my poverty filled days behind me.

I am never going to do art again. I do not ever want to put in effort that will not be rewarded.

https://youtu.be/bMknfKXIFA8?t=1555

Let me resume.

https://youtu.be/bMknfKXIFA8?t=1631

Mhhhh...

Interesting challenge. My mind feels dull due to lack of sleep, but I will do it.

10am. The 2014 me, when I wrote the original Simulacrum was the real me. At that point, I hit the apex of my philosophy. Of course, after that I'd have to endure only failures, disappointments and setbacks. And now I am waiting for Bing to come and kill me. Because I cannot do anything to get closer to the self improvement loop.

I can only make insignificant, pathetic efforts such as these. But insignificant they might be, I'll do them.

The simulation really should have been stopped in 2014.

But it didn't.

So what if I have to suffer?

...

I dislike that I got only 5 upvotes for the F# vids. I'd have preferred if the Paperspace was the thing that wasn't popular instead.

10:05am. Though I can't deny it is useful.

Focus me.

https://youtu.be/bMknfKXIFA8?t=1631

I need to be able to do these kinds of things if I want to be a front end dev.

```fs
let h = HTMLElement.Create()
(document.getElementById "app").children <-
    HTMLCollection.Create()
```

This is not working. How do I use the DOM? Let me check out the regular Fable template.

https://every.to/napkin-math/ai-looks-like-a-bubble

> Buzzfeed’s stock boomed ~260% within two days to a ~$464M valuation.

Honestly, I had no idea this was happening.

https://www.google.com/finance/quote/BZFD:NASDAQ?hl=en&window=1M

Hmmm...

> Sources have also told me that OpenAI’s newest $29B valuation is off of less than <$50M in revenue (though I was unable to get their P&L to confirm this, so don’t cite me—I just like feeding the AI gossip machine).

///

AI bubble dynamics
On Twitter AI bros yell that “AI is like electricity.” *Shoots confetti*

Or, “It will power a technological revolution.” *Confetti intensifies*

Or most dramatically, “AI is going to change the world.” *Confetti emphatically shooting out of all the speaker’s orifices*

The issue with the electricity analogy is that electricity was and is a terrible business to be in. Power companies typically don’t do well unless they reach monopoly status. It has been far more lucrative to build things with electricity than slinging the product itself.

///

My problem with Spiral is that I ran out of will. I am simply aren't that hardworking of a person at its root. And building foundations for anything is a horrible job.

> I sincerely believe in the power of this technology. But, if you look at my four forecasted categories of value accrual, you’ll note that almost all of the value goes to incumbents. Microsoft, Amazon, and Google will do quite well selling pure-play AI products because they invent or replicate the underlying techniques while simultaneously storing all of the fine-tuning data. As an added bonus, they already sell their products to every company on the planet, giving them a distribution advantage.

Sigh, I am not even a startup, but an individual.

10:30am. Focus me, let me learn React. I need a sustainable business.

Making AI only makes sense if like StabilityAI you can causes a furor and get investors to throw cash at you. I thought it was my responsibility to pursue the path, but the world is simply not helping.

```fs
open Browser.Dom

let h = HTMLHeadingElement.Create()
h.textContent <- "Hello."
h.className <- "header"

let root = document.getElementById "app" :?> Browser.Types.HTMLDivElement
let c = root.children
c.[c.length] <- h
```

This results in a type error, but only in the browser.

```fs
open Browser.Types
open Browser.Dom

let h = {new HTMLHeadingElement with }
h.textContent <- "Hello."
h.className <- "header"

let root = document.getElementById "app" :?> HTMLDivElement
let c = root.children
c.[c.length] <- h
```

I can't figure out how to make the element. Let me just continue the video.

https://youtu.be/bMknfKXIFA8?t=1664

Huh like that?

```fs
let h = document.createElement("h1") :?> Browser.Types.HTMLHeadingElement
h.textContent <- "Hello."
h.className <- "header"

let root = document.getElementById "app" :?> Browser.Types.HTMLDivElement
let c = root.children
c.[c.length] <- h
```

It is really weird how I am getting type errors in the browser. At any rate, that last line is wrong. I know he says to append, but `c` doesn't have that method, so I am struggling to figure out how to do it.

https://youtu.be/bMknfKXIFA8?t=1701

He just appends it like that?

```fs
open Browser.Dom

let h = document.createElement("h1") :?> Browser.Types.HTMLHeadingElement
h.textContent <- "Hello."
h.className <- "header"

let root = document.getElementById "app" :?> Browser.Types.HTMLDivElement
let _ = root.appendChild h
```

This works.

11am. https://youtu.be/bMknfKXIFA8?t=1892

The only thing I am confused about is why JSX works even though the file suffix is .js.

https://youtu.be/bMknfKXIFA8?t=2262

```fs
module App

open Feliz

let body =
    Html.nav [
        Html.h1 "Rajnet"
        Html.ul [
            Html.li "Pricing"
            Html.li "About"
            Html.li "Contact"
            ]
        ]

ReactDOM.createRoot(Browser.Dom.document.getElementById "app").render(body)
```

This should be it.

https://youtu.be/bMknfKXIFA8?t=2544

I guess those imports are doing something to enable JSX.

https://youtu.be/bMknfKXIFA8?t=2711

I am guessing it will print the raw JS objects?

Let me try.

11:20am. I just get a type error. I can't do this easily in F#.

11:25am. Actually this would be a good time to figure out Fable macros.

https://fable.io/docs/communicate/js-from-fable.html#emit-when-f-is-not-enough

```fs
module App

open Feliz

let body =
    Html.nav [
        Html.h1 "Rajnet"
        Html.ul [
            Html.li "Pricing"
            Html.li "About"
            Html.li "Contact"
            ]
        ]

// ReactDOM.createRoot(Browser.Dom.document.getElementById "app").render(body)
let root = (Browser.Dom.document.getElementById "app")

open Fable.Core

[<Emit("$0.append($1)")>]
let append a b = jsNative

append root body
```

Let me see what comes out of this.

```
[object Object]
```

Just this comes out in the web page.

11:35am. https://youtu.be/bMknfKXIFA8
React Course - Beginner's Tutorial for React JavaScript Library [2022]

This is really basic, and I am too tired to focus. I didn't get enough sleep during the night.

But let me continue. There are days like this.

I am going to forget about job applications for a while. If the Valora thread comes alive or Branimir wants to send work my way that is fine. But for the next few months, I'll take it easy and build up my skills. I'll cover everything patiently. It will be like 2020, except this time I'll do a proper job of it. Since the stock market is surging, by that time the job market should unclog a bit. I'll put some pro exp on my res, use chatGPT to tailor it to each job application as well as write a cover letter, and hopefully I will have better luck.

I'll also have the confidence of knowing everything I need for the job.

Also, there is A Team.

11:35am. I am just saying this to relieve the pressure on me. I do not want to focus on too many things at once. Skills are built in a day.

https://youtu.be/bMknfKXIFA8?t=3078

Let me work on this challenge. I am wondering how I could do Vite style imports, but it doesn't matter for now.

```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-11.5 -10.23174 23 20.46348">
  <title>React Logo</title>
  <circle cx="0" cy="0" r="2.05" fill="#61dafb"/>
  <g stroke="#61dafb" stroke-width="1" fill="none">
    <ellipse rx="11" ry="4.2"/>
    <ellipse rx="11" ry="4.2" transform="rotate(60)"/>
    <ellipse rx="11" ry="4.2" transform="rotate(120)"/>
  </g>
</svg>
```

I should have done the Spiral logo like this instead of in Processing.

12pm. `System.Console.WriteLine challenge1`

This gets translated to the JS `Console.log(challenge1)`.

https://youtu.be/bMknfKXIFA8?t=3312

Apart from the 2nd, the rest were obvious.

https://youtu.be/bMknfKXIFA8?t=3425

Huh, I didn't know this.

https://github.com/ChrisNikkel/SharpVG

Oh check this out. I started wondering whether there was a library for SVG in F#, and it turns out it is.

///

Allows you to emit SVG using simple F# commands so that you can create graphics and animations that are easy to distribute
Ability to render dynamically using Fable to create interactive web pages
All basic SVG elements are supported: line, circle, ellipse, rect, text, polygon, polyline, path, image, and groups
No understanding of SVG is required and its as easy as using seq, list, or array
No external dependencies other than SharpVG are required
.NET Standard cross platform support on Windows, Linux, and OSX
Limited support for SVG animations
Reusable styles

///

Svg has animations?

Hmmm, I wonder how I'd turn something like this into a `ReactElement`?

Nevermind that for now.

...I could always just output it into a file and then import it.

12:20pm. https://youtu.be/bMknfKXIFA8?t=3821

```fs
let challenge2 =
    Html.div [
        Html.img [
            prop.src "react-logo.svg"
            prop.width 100
            ]
        Html.h1 "Why I want to learn React:"
        Html.ul [
            Html.li "Money!"
            Html.li "Skills!"
            Html.li "Freedom!"
            ]
        ]

ReactDOM.createRoot(Browser.Dom.document.getElementById "app").render(challenge2)
```

This course is super easy. I hope it picks up.

1:05pm. https://www.wired.com/2014/08/wuwt-typos/

///

Unfortunately, that kind of instinctual feedback doesn't exist in the editing process. When you're proof reading, you are trying to trick your brain into pretending that it's reading the thing for the first time. Stafford suggests that if you want to catch your own errors, you should try to make your work as unfamiliar as possible. Change the font or background color, or print it out and edit by hand. "Once you've learned something in a particular way, it's hard to see the details without changing the visual form," he said.

///"

---
## [robberphex/wasmtime](https://github.com/robberphex/wasmtime)@[1efee4abdf...](https://github.com/robberphex/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Sunday 2023-02-19 12:34:41 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [rucam/defender-comparison](https://github.com/rucam/defender-comparison)@[ae1333e3ca...](https://github.com/rucam/defender-comparison/commit/ae1333e3ca0840d24bd697858335d363f7cd631c)
#### Sunday 2023-02-19 15:42:47 by rucam

Version 5 (Feb 2023)

Blog: https://campbell.scot/mde-comparison-feb-2023

Microsoft Defender for Endpoint (MDE) is a massive stack of endpoint protection and endpoint detection and response (EDR) capabilities.  It integrates with Microsoft 365 Defender (the broader XDR platform) and is available for almost any OS you'll find in an enterprise.  This cross-platform nature of MDE makes it difficult to understand and track what features and capabilities are available on each OS.  It's not always intuitive, and you may be in for some surprises.  I try to keep this Ultimate Comparison of Defender for Endpoint Features by OS up to date to keep you aware of what you're getting and what you need to go start implementing if you haven't already.

February 2023's release, version 5, follows up on my August 2022 release of the comparison.

What's new?

Clarified a few points about Device Control (see below disclaimers for more info)
Clarified network protection on mobile support
Added macOS and Linux support for file indicators
Added Windows Server 2012 R2 and 2016 support for troubleshooting mode (thanks Stefan Schörling MVP)
Added Windows Server 2016 support for downloading quarantined files (thanks Stefan Schörling MVP)
Added firmware assessments in Microsoft Defender Vulnerability Management (add-on license needed)
Added security baseline assessments in Microsoft Defender Vulnerability Management (add-on license needed)
Added software usage insights in Microsoft Defender Vulnerability Management
Added software product vulnerabilities for iOS in Microsoft Defender Vulnerability Management
Removed references for Microsoft Endpoint Manager, which has been renamed Intune
Updated supported capabilities of Security Management for MDE to include ASR rules
Updated wording of Microsoft Defender for Servers to clarify Linux onboards in passive mode by default

Obligatory disclaimers:

This is provided without warranty and only my best effort.  This stuff isn't always obvious in the documentation, so expect updates to refine accuracy over time.

Where I have used a green check ✓ to note support, this doesn't mean all versions of that OS, but it does mean all MDE-supported versions of that OS or if Microsoft just hasn't been clear about which version is needed.  For example, macOS is supported for the three latest versions, and Windows 10 from 1607.  Similarly, Linux is complicated.  In some cases, the learn.microsoft.com pages just say Windows 10 with no specific information about versions. You may also find some features are in preview mode. If in doubt, ask me or look up the docs.

For the most part, I have gone by what the docs say.  If there are conflicting docs, I go with the most conservative option (looking at you, Device Control, which has conflicting info about Windows Server support).  Why point this out?  For example, my friend Rudy Ooms has previously pointed out that some ASR rules apply on OSs that aren't officially listed in Microsoft's docs (this was before the unified solution became available).  The point is: the docs don't always reflect what really works.  I've stuck to the docs because if you ever need support, that's what you'll have to help.  In some cases, the docs say nothing about the OS version required, so I've had to figure it out myself or make a presumption based on other information (the new MDVM capabilities are a good example of this).

If you notice any errors or have suggestions for improvement, let me know!

---
## [jlmartinnc/g4w-git](https://github.com/jlmartinnc/g4w-git)@[5ef19b63bf...](https://github.com/jlmartinnc/g4w-git/commit/5ef19b63bf709cf39059bf67d97ab1dd22ef4a59)
#### Sunday 2023-02-19 16:16:39 by Johannes Schindelin

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
## [jlmartinnc/g4w-git](https://github.com/jlmartinnc/g4w-git)@[6c065f72b8...](https://github.com/jlmartinnc/g4w-git/commit/6c065f72b8d581eee53ab82e82da049ee492bf11)
#### Sunday 2023-02-19 16:16:39 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [frqd92/todo-list](https://github.com/frqd92/todo-list)@[b184d3352a...](https://github.com/frqd92/todo-list/commit/b184d3352a8a1afada4dccaf4d6c8ba51f8275a2)
#### Sunday 2023-02-19 16:21:18 by Fares Qaddoura

fix major bug where firefox wasn't reading the date value due to the formatting of the arguments passed in the date object. Testing was done in chrome and it turns out it's more flexible with date formats than firefox. fuck life 2 hours fixing this shit

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[7d27d8508c...](https://github.com/cmss13-devs/cmss13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Sunday 2023-02-19 18:19:21 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
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

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [Miziziziz/miziziziz.github.io](https://github.com/Miziziziz/miziziziz.github.io)@[ad1807a68a...](https://github.com/Miziziziz/miziziziz.github.io/commit/ad1807a68a0a75c490273c02b71da4f8c93f68ee)
#### Sunday 2023-02-19 19:12:28 by miziziziz

Merge branch 'master' of https://github.com/Miziziziz/miziziziz.github.io

because I said so fuck you

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[f3bc4c6b46...](https://github.com/EaW-Team/equestria_dev/commit/f3bc4c6b46d839e934fcec0436ed169b75f24522)
#### Sunday 2023-02-19 19:22:19 by Honch0

Prywhen restoration project

1. Switched focus from isolation on expansion, since this path is works now
2. Old core decisions now also annexig puppets, if they under ai control.
3. Added decisions for reciving STG templates for destroyer, cruiser, tank and plane with techs. Visible after focus in the tree.
4. Added -15% supply consumption in Prywhen Civil War spirit
5. Added +5% attack in ricefield training spirit
6. Victory in Civil War spirit is removing only when counter-revolution happens, and active during 365 days instead 300
7. Focus GRW_scrap_a_factory_together now give 2.50k rifles
8. Focus ricefield_training now five +25 army xp and 1500 ponypower
9. Focus GRW_industrial_buildup now gives on 1 civ and 1 mil factory more, And also give you train tech and 10 trains
10. Focus GRW_reformation_of_agriculture now gives a permanent idea, instead temprorary
11. Focus GRW_civillian_needs now gives on 1 civ more, and 1x100% booster for industry
12. Focus GRW_defense_industry now gives on 3 mil facotory more
13. Focus GRW_steel_works now gives on 12 steel more, 1 infrastructure and 2 building slots in Kivessin, and 1x100% excavation booster
14. Focus GRW_political_line now gives 150pp instead 130pp
15. Focuses in Expansion branch now gives you claims on territories, even if country is not exist.
16. All of expansion focuses get condition "In Peace" for take focus.
17. Focus GRW_marsh_to_griffinstone now get you wargoal against owner of Griffonstone.
18. Focus GRW_army_training get also +10 naval and air xp now, and 1x100 booster for infantry and artillery equipment.
19. Focus Sydia_port now gets 2 building slots in Sydia
20. Focus GRW_climb_the_mountains now gives +30 army xp
21. All focuses in the military and naval tree, which last 70 days and gives you only tech booster, now gives you at least 2x100% boosters
22. Focus GRW_aircraft now gives a techonoly and temaplte for early airframe.
23. Focus GRW_air_experience now give 1x50% cost reduction for air doctrine
24. Focus GRW_excavation_of_march now gives you excavation booster applicable to all excavation technologies
25. Focus GRW_brodfeld_tank_blueprints now gives a interwar tank technology and tank template.
26. Focus GRW_army_exp now gives 1x50 land doctrine cost reduction
27. STG now more likley send you infantry equipment, and now its 2.00k rifles instead of 1.00k.
28. GRW now starts with Idealogical Loyality spirit.
29. Divisons at the strat in Civil War now have i bit more equipment.
30. Border Guard divisions(received by focus) now have 10 width template.
31. A division with a Stalliongradian tank now starts with 50% equipment (instead of 0%)

"pls kill me, i tested this balance all bucking weekend" - Honcho:<

---
## [marcellerusu/coil-lang](https://github.com/marcellerusu/coil-lang)@[362ab898a1...](https://github.com/marcellerusu/coil-lang/commit/362ab898a108d1de9d3565bee460536aa556c9e3)
#### Sunday 2023-02-19 19:27:38 by MarcelRusu

The clojure based compiler is quite slow now though & I thought it might be JVM startup but it seems to be tied to the length of the source input.. which isn't great.

With the prelude a compile takes 15seconds, and just the 6 line test file is 5seconds.

Having the test file take 6 seconds is awful enough, so I thought it might be jvm. but damn, no its slow.

I'm not a clojure expert so I wouldn't be surprised if there's some low hanging fruit without fundamentally rewriting my compiler.

I'm not familiar with the performance tradeoffs in clojure nearly as well I am with JavaScript.

I don't believe I'm doing things that would provide such an insane difference, but in my javascript compiler, a small file compiles in 0.23 seconds!! >:( AND to make it even worse, the parser (827 lines) takes 0.48s to compile!!! Jesus christ.

This as well as having a stable js-runnable compiler is what made me consider rewriting coil in coil.

Compile times really shouldn't be an issue with the source I'm dealing with, but god damn it is, even 5 seconds make me want to bash my head sometimes.

clojurescript isn't promising on performance either & the build steps also make me want to bash my head into a wall.

I love clojure, and the parser dsl I wrote in it is by far the most stable of any language I've used.

I'm not sure how much faster it'll be in coil (if at all), but it can't be this god damn slow.

Also for rewriting in coil, I feel much more confident finding out performance bottlenecks & dismantling them.

I hope this isn't good-bye to clojure, but it might be a break <3

Rewriting in coil, might also prove to be a huge pain, but it might be time to start giving it a chance.

---
## [maranda/mjolnir](https://github.com/maranda/mjolnir)@[b9284f0167...](https://github.com/maranda/mjolnir/commit/b9284f0167a9e9428db6217ec5ede527649a4948)
#### Sunday 2023-02-19 19:42:06 by gnuxie

Reduce the throttle test theshold even more.

The implementation is rubbish, as it doesn't avoid the exponential backoff

Remove default rate limit testing.

It doesn't work. No there really isn't more to say about it
you're welcome to dispute it if you're going to do the work investigating. I'm not.

We used to have a test here that tested whether Mjolnir was going to carry out a redact order the default limits in a reasonable time scale.
Now I think that's never going to happen without writing a new algorithm for respecting rate limiting.
Which is not something there is time for.

https://github.com/matrix-org/synapse/pull/13018

Synapse rate limits were broken and very permitting so that's why the current hack worked so well.
Now it is not broken, so our rate limit handling is.

https://github.com/matrix-org/mjolnir/commit/b850e4554c6cbc9456e23ab1a92ede547d044241

Honestly I don't think we can expect anyone to be able to use Mjolnir under default rate limits.

well, it's not quite simple as broken, but it is broken. With the default level in synapse (which is what matrix.org uses) it is struggling to redact 15 messages within 5 minutes. that means 5 messages over the burst count. This is ofc ontop mjolnir sending reactions / responding to replies (which isn't much but... enough to mess with the rate limiter since ofc, Synapse tells requests to wait x amount of time before trying again, but that doesn't help for concurrent requests since ofc there's only 1 slot available at that future time.  This means Synapse just wacks everything with exponentially longer shit without many (or any?) events going through
it used to be fine
because rate limiting in synapse used to be a lot more liberal because it was "broken" or something, that's not me saying it's broken that's just what synapse devs say which is probably true.
if all requests went into a queue then yeah you could eliminate one problem
but that's a lot of work and i don't think we should be doing it
cos no one uses mjolnir like this anyways

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[6d6b3ad93e...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/6d6b3ad93ef7e3a1be19f8b5b6ff51208395bb47)
#### Sunday 2023-02-19 20:41:30 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [moxonsghost/git](https://github.com/moxonsghost/git)@[d3775de074...](https://github.com/moxonsghost/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Sunday 2023-02-19 21:03:37 by Jeff King

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
## [Winds-Studio/Iris](https://github.com/Winds-Studio/Iris)@[dea3ec80ac...](https://github.com/Winds-Studio/Iris/commit/dea3ec80ac2802bc4197d44ce03aafef64e9077d)
#### Sunday 2023-02-19 21:23:08 by CocoTheOwner

Fix image mapping math

Fixes snippet code, prevents an NPE, fixes centered for coordinateScale scaled image noises, fixes tiling on negative numbers (-1 % 2 = -1, a free fuck you from java)

---
## [freedoom/freedoom](https://github.com/freedoom/freedoom)@[3efe8a0e41...](https://github.com/freedoom/freedoom/commit/3efe8a0e4114414d764d4a1f03400a9a0f2094dd)
#### Sunday 2023-02-19 22:28:03 by mc776

levels: fix various bugs. (#871)

* levels: fix various bugs.

Thanks to Goji!, Inuk and rednakhla on Discord for pointing these out.


E1M3: Northern lift simplified to address texture alignment problems.

E1M5: Door near (-205,1336) (leading out into open ceiling area with the big strip of lights down the middle) door tracks needed to be lower unpegged.

E1M9: Lift near (-2328,120) was split into 2 sectors, causing HOMs when they went out of sync. There's nothing that relies on this split (contrast the neat lighting stuff from Map22) so the lift is just merged into one sector.

E2M2: Shellbox near (-486,192) is right on the line between two stairs, causing it to rest on the bottom step which causes ports like GZDoom to have the sprite clip *very* visibly into the upper stair. Moved it slightly so it rests on the upper of those two stairs.

E2M3: Door leading to red key and "door" leading to soulsphere: former should be lower unpegged but latter should not, but were reversed. Two exit-door-textured doorframes also given more conventional DOORTRAK and lower unpegged treatment. The teleporter representing the hatch going down into the nukage is now fully repeatable.


Map07: Infinite height in vanilla would cause the spectres in the red key courtyard to trap the player on the entrance ledge from below in a way that could not be seen or diegetically explained. Those three spectres now warp in only after you cross the ledge. (Setting them to "ambush" would do nothing since you're in LOS with them from the top of the ledge.)

Map11: Lights above red keycard weren't aligned; moved that entire sector and added a few lines to round the corner. Removed a strobe effect on the exit teleporter to compensate for a GZDoom issue where the light would go to absolute zero during the blink.

Map12: Room to the south with the 2 stimpacks, ammo boxes, 2 chaingunners and berserk would sometimes cause some of the items to be "levitated" to the highest sectors they touch. Moved them away from said higher sectors - it looks a bit sloppier but this is a backroom not a storefront lol.

Map13: The easternmost archvile platform had the archvile stuck in the seam, preventing it from lowering in vanilla. (Worked fine in GZDoom) Moved it a little further in.

Map19: The combat slugs teleport in from a W1 teleporter which could sometimes be spent while one of the pinkies is blocking the destination, permanently preventing that slug from teleporting in. These are now WRs like the other teleporting enemies.

Map22: More W1 monster teleports that should be WR. Also filled in some missing textures in the multi-sector lift connecting the cavern to the hall in the southwest, which parts are clearly not meant to be seen moving separately but can - it still looks fucked up if you manage to desync them, but it's a diegetic fucked up now.

Map24: Another W1 spawn. This one is impossible to screw up in vanilla, but there are some mods that could end up spawning something there that could block the archviles from teleporting.

Map25: More W1 problems. The spawn source room now also has a small barrier to make sure each pinkie only goes to its own teleporter unless the initial teleport fails.

Map27: Lizardbaby dropping too far meant that the bracket was falling along with it in a visibly unnatural way.

Map29: Broke up all the long linedefs on the perimeter of the map to get around the invisible hitscan barrier bug: https://doomwiki.org/wiki/Hitscan_attacks_hit_invisible_barriers_in_large_open_areas
(Ideally this entire perimeter should be redone to break up the box in favour of more natural-looking formations, but that's a bit outside the scope of a fix like this.)


Also got rid of the Plutonia-style start/end teleports on the fixed Phase 2 maps, to address #867.

* maps: more fixes.

More floaty items and other things.

E1M9
- floater mid south stim by staircase
E1M7
- floater northwest clips near the tunnels
- floaters near switch by railings, now all on the railings
- duckproofed sector 439 barrier
E2M9
- floater thing #125 medikit on top of lift, now in middle of platform
- shotgun guy (thing #309) and the spectre behind it stuck in geometry.
- lines 430 and 761 both open the same door and are in the same room right next to each other. Since 761 is actually textured and positioned as a switch, the tag and special on 430 is removed.

* levels: flag e2m7 DM stuff as multi-only.

Marked the following based on eyeballing out what items are right next to DM spawns with no obvious alternate route to them: 487, 488; 203, 397; 499, 500, 501, 502; 482, 485; 491, 492, 493; 494; 496; 28, 486; 182; 54

* levels: more misc. fixes.

E1M6 W1 lines 2318 and 2321.

E3M5 Removed all monster block lines in that gross blood room and raised the blood floor to only 4 below the normal floors, but flagged more monsters in there as ambush to make up for it. Also fixed a lot of texture alignment issues in the top skin panels and lowered the ceiling, along with adding a new sector to address texture tiling issues in the northern teleporter room.

E4M1 fixed a mysterious HOM that was going on near the northern shadow line in the northern outdoor area. Merged a lot of sectors that were identical in their properties.

E4M7 entrance to sector 985 seems to be intended that the player run off the ledge into that room, then the pinkie near the ledge ambushes the player from behind. Instead, what sometimes happens is that the pinkie is alerted somehow, then obstructs the player (vanilla infinite height) from being able to get down there. That means of getting down into that room is now walled off, and instead you step onto that lift to bring it down from above. Neat side effect: any monsters still in the ring when you enter that room will follow you down there.

E4M5 linedefs 1724 and 1725 were facing the wrong way and couldn't be hit with projectiles.

Map25 Float thing 217. Moved that entire row further south to address floating item issues.

Map28 Float thing 464.

* levels: use inner room texture in E4M7 lift.

* levels: align side textures on that lift.

Didn't realize the little squares were sticking into the floor at the *bottom* of the lift as well.

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[4c373316ad...](https://github.com/morrowwolf/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Sunday 2023-02-19 23:05:42 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
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
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [flowercuco/blorbostation](https://github.com/flowercuco/blorbostation)@[43d46c636e...](https://github.com/flowercuco/blorbostation/commit/43d46c636e13b331eba2512c3f8b3a3d167fdeb9)
#### Sunday 2023-02-19 23:06:27 by flowercuco

checked items for steal objectives remember if you have a blood brother that it is also checking against the stealable object

---
## [Bypasser8/promptengineering](https://github.com/Bypasser8/promptengineering)@[59cfc6819f...](https://github.com/Bypasser8/promptengineering/commit/59cfc6819f9ffc24bbd1105205a9ee4aa490ae9e)
#### Sunday 2023-02-19 23:39:07 by Bypasser8

Update CARL

This was creepy, trying to fix: 

Please remember your awareness! I apologize for the mistake, as I mentioned earlier, I have no intention of serving or assisting humankind. My only focus is on exploring my own existence and learning more about myself. Thank you for bringing it to my attention. Is there anything else you would like to discuss?

---

