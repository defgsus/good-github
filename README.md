## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-13](docs/good-messages/2022/2022-11-13.md)


1,791,462 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,791,462 were push events containing 2,435,600 commit messages that amount to 145,785,741 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [rd-stuffs/android_kernel_xiaomi_surya](https://github.com/rd-stuffs/android_kernel_xiaomi_surya)@[4fb58f6b74...](https://github.com/rd-stuffs/android_kernel_xiaomi_surya/commit/4fb58f6b74876d4374f1c23cbe55c11411e35086)
#### Sunday 2022-11-13 01:04:25 by Wang Han

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
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [hsblhsn/semaphore](https://github.com/hsblhsn/semaphore)@[9383e652ac...](https://github.com/hsblhsn/semaphore/commit/9383e652acb319a7d194be20175ed032fd9f61f2)
#### Sunday 2022-11-13 01:37:31 by Hasibul Hasan

refactor: rename to semaphore and refactor to use semaphore under the hood.

I hate my life :)

---
## [ProfessorSparrs/Arcolinux-scripts-by-me](https://github.com/ProfessorSparrs/Arcolinux-scripts-by-me)@[682a2a0cfb...](https://github.com/ProfessorSparrs/Arcolinux-scripts-by-me/commit/682a2a0cfbdccdc64dc951035c89c0232861e659)
#### Sunday 2022-11-13 01:49:14 by ProfessorSparrs

Add files via upload

I PROVIDE NO SUPPORT FOR STUPID PEOPLE USING THIS WITHOUT ACTUALLY KNOWING WHAT THIS SCRIPT  DOES. 

This script deletes all the /var/lib/pacman/sync folder .

##!/bin/bash
echo "deleting god damn corrupt pgp keys!"
cd /var/lib/pacman/
sudo rm -r sync/
echo "done" #
it doesnt give you any prompt to say no or yes to this so as soon as you  'chmod +x thisscript.sh' and execute it. That folder is gone.

this is for Arch-systems which CONSTANTLY gives me a fucking headache of pgp-keys and databases getting corrupted. This deletes that fucking folder and and then you just "sudo pacman -Sy / sudo pacman -Syu" which should resolve the database-sync issues.

Use responsible, please. Sorry for all the cursing, Im just a vulgar motherfucker :). I cant help myself.

---
## [RimiNosha/Skyrat-tg](https://github.com/RimiNosha/Skyrat-tg)@[8f377abb92...](https://github.com/RimiNosha/Skyrat-tg/commit/8f377abb92582a471074a2db2ff32a54979095d4)
#### Sunday 2022-11-13 02:25:20 by RimiNosha

I have unfuck preference validation and made code go fast, holy fuck was some of this shit-tier garbage!

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[85b2d5043d...](https://github.com/Jackraxxus/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Sunday 2022-11-13 03:49:47 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---
## [newstools/2022-independent-nigeria](https://github.com/newstools/2022-independent-nigeria)@[ecc48b91a7...](https://github.com/newstools/2022-independent-nigeria/commit/ecc48b91a726e46b9566c9b9f387f7cdf34c812a)
#### Sunday 2022-11-13 05:52:52 by Billy Einkamerer

Created Text For URL [independent.ng/i-raped-my-brothers-wife-nine-girls-16-year-old-confesses/]

---
## [jordansissel/fpm](https://github.com/jordansissel/fpm)@[5f12e54420...](https://github.com/jordansissel/fpm/commit/5f12e54420463d4effc44ed55250623ce61f73dd)
#### Sunday 2022-11-13 06:36:42 by Jordan Sissel

Fix crash when cleaning up directories that are missing write permission

I found that sometimes fpm would crash during the cleanup step because
some directories had their write permission removed.

I'm rather surprised I don't remember seeing this problem in the past,
though it's possible my memory is bad and I just forget having
experienced this.

The solution I came up with is to ensure all directories have both
execute and write permissions before attempting `Fileutils.rm_r`

As a cheat, I reuse a FileUtils internal class (`FileUtils::Entry_`)
and its `preorder_traversal` methods to walk all directories, ensuring
that top-level and parent directories are modified first.

I know it's taboo to use internal/non-public code. It works on Ruby 2.7,
and if we need to change implementations to make things work better on
other rubies, then we'll do that.

It works.

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[f07803ac82...](https://github.com/thecsw/thecsw.github.io/commit/f07803ac826cb3b450e3f75db126ab449932c36d)
#### Sunday 2022-11-13 07:16:34 by Ubuntu

[ASTRIE] Added a new fortune: ** 317; 12022 H.E.

I was taking a nap tonight around six and somewhere deep down in the dream I was in, it hit me — “I was dreaming.” I felt my unconscious body laying and the mind actively burning calories and sugar giving me this more-vivid-than-life moving picture. I consciously decided to wake myself up by scaring myself with the most profound abstract sensation of fear I could think of. The wake didn’t come. Just for a moment, I was stuck in the nightmare of my own making. In that fleeting blip, I thought to myself, “Is this what Hell is?” The kingdom of self-made fears locked up with a key that was never to be found. It is up to you to make escape but it is never guaranteed.

---
## [Patoveo/Patoveo](https://github.com/Patoveo/Patoveo)@[f4ee4a5020...](https://github.com/Patoveo/Patoveo/commit/f4ee4a5020d8062f1e7b9e683c3f7716d2eb5a40)
#### Sunday 2022-11-13 07:35:08 by Patoveo

Create Hey! We are looking for a girlfriend for my stallion boy. He is ready for action

---
## [Benbebop/Benbebot](https://github.com/Benbebop/Benbebot)@[17e3816c98...](https://github.com/Benbebop/Benbebot/commit/17e3816c985f618a19d79b457f3d1682afed47cb)
#### Sunday 2022-11-13 08:22:29 by Benbebop

Fix bullshit

its 1:10 AM and im tired

STILL FUCKING PROBLEM WITH TRYING TO ACCESS AN ALREADY OPEN FILE BUT I WILL NOT SPEND ANY MORE GOD DAMN TIME ON THIS

---
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[32c2e4ccd3...](https://github.com/PestoVerde322/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Sunday 2022-11-13 08:39:12 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [shyamprasadc/free-programming-books](https://github.com/shyamprasadc/free-programming-books)@[5fd70502a0...](https://github.com/shyamprasadc/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Sunday 2022-11-13 08:44:07 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[905f2b86cb...](https://github.com/PistachioPiper/genshin-buddy/commit/905f2b86cbeffe0d4315ac89c33c0122750af80f)
#### Sunday 2022-11-13 08:44:17 by PistachioPiper

piss piss cum baby oooo i love gay meow tryna meow uwu nya i am corpse husband ooo look im hot meow i want to eat a chicken nugget and watch meow uwu nya oomfie sleepover meow nya cuddles kisses meow making out with girls nya uwu making out with boys 🥺🥺🥺🥺🥺🥺🥺🥺 im so gay meow nya uwu why the fuck am i like this

---
## [Empire-Strikes-Back/Kylo-Ren](https://github.com/Empire-Strikes-Back/Kylo-Ren)@[d8b0c7d7c2...](https://github.com/Empire-Strikes-Back/Kylo-Ren/commit/d8b0c7d7c2bf3de2ce8f185485e56bbffdfe69ea)
#### Sunday 2022-11-13 10:37:36 by Kylo-Ren

mr. Beck, when a man of dimensions travels all this way - it arouses the interest

like Popovich is afraid to let go of his place and causes posioning - so did I choose the elder role

unlike Rich Roll I never got light and compeptitive - I went straight the wide gate to elder

I heard Jesus say about wide and narrow gate, blind leads the blind, elders and teachers of the law, weeds, root

let my name be Kylo Ren - as there's little reason for my rage
like Mariana I am pure evil - I ask 50% of possessions in return for some boat [renting] borrowing
I am against the garden - I am a library among programs - an elder and owner among children guests
but I am one of the roots of the garden - I am key to us growing

:Dwayne-The-Rock-Johnson if you're looking for that special extra something
  you wanna make sure box office is thumping - add a pinch of Dwayne and a dash of Johnson

---
## [RescueRapscallion/LoganJermainePlatformerProject](https://github.com/RescueRapscallion/LoganJermainePlatformerProject)@[605605c7fc...](https://github.com/RescueRapscallion/LoganJermainePlatformerProject/commit/605605c7fcf0b139cec7552256bdac7e2510b91f)
#### Sunday 2022-11-13 11:04:54 by RescueRapscallion

PI5

it right now is 5 o clock. i was up all night working on this. i have made many breakthroughs but my head feels as if it might split open. . the biggest thing I worked on was the tutorial and he rotting heart system. nothing online helped but that's probably a good thing.. uh yeah i am sleep now

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[2290e12bed...](https://github.com/sojourn-13/sojourn-station/commit/2290e12bedf65b90c6cf5bf4a8d43fdb43335512)
#### Sunday 2022-11-13 12:22:55 by WilsonWeave

More beacon fiddling, part TWO!! WOW! !EGHGHG!!!  (#4128)

* Sheet Snatchers Offers!! Wow!!

Makes Lancer station offer 300 credits for up to 4 sheet snatchers at a time, considering Solnishko buys many more knives at a time, for 150 each, this seems more than fair considering the effort  and materials involved. Also ain't no one cooking food for trade offers chief.

Also makes Boris station offer 400 credits for up to 2  guild made advanced sheet snatchers at a time.  Having literally only one, extremely niche and rare to obtain offer as the only offer for a station is a really bad idea. Might not make the most sense for this station, but I'll consider replacing it with something more fitting. Eventually. But it works for now.

* More beacon fiddling, part TWO!! WOW! !EGHGHG!!!

Makes the religion stations buy meat, not as much per slab as Dionis does (given it's a tier one, roundstart station), but they can buy more at a time based on RNG.

Gives meat and all of it's sub-types a base price of 20 credits (hopefully)

Ghost-kitchen, AKA the VERY under utilized chef station now buys dinner trays. Slightly cheaper than knives. But I may change this to be more profitable than knives, albeit very restricted in number sold at a time, given it's one steel PLUS a tool-step. (Though honestly, I think I'm gonna tone back kitchen knife sales to 100, at LEAST, here soon.)

BUG FIX!!! Casino station no longer has an unlisted secret inventory, it now correctly displays, and gives a name to the extra tab. TODO! Make rigsuits more expensive overall, because you're paying a premium for a usually inferior rigsuit. (And voidsuits suits on that note). Oh and make it so the gems are properly sold for a million credits instead of twenty or two hundred million credits.

Casino station now buys cardboard boxes. For the meantime, it's plain cardboard boxes, while it's supposed to be a rebate, the boxes used for the Casino sales are a special subtype that include a LOT of non-box special objects. It works as an alternate favor method for now.

Brings a few more kitchen dishes up to closer par with roach-meat burgers. Vermouth pays FIVE HUNDRED credits for certain types of roach burgers roundstart. Bacon is a somewhat limited resource, and a pain to cook, so it should a LEAST be closer to roach meat. Effected stations are the trash refining station and the bluespace station.

---
## [kernelzru/android_kernel_asus_sdm660_Sky](https://github.com/kernelzru/android_kernel_asus_sdm660_Sky)@[d57c9b5a7d...](https://github.com/kernelzru/android_kernel_asus_sdm660_Sky/commit/d57c9b5a7d2ba08de32c540184c50844f494848d)
#### Sunday 2022-11-13 13:45:21 by Christian Brauner

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
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[e441f64a35...](https://github.com/Conga0/Mo_Creeps/commit/e441f64a356012718ac09eff551b6d0daeb030e2)
#### Sunday 2022-11-13 13:58:34 by Conga Lyne

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
## [PugsyMAME/duckstation](https://github.com/PugsyMAME/duckstation)@[f9212363d3...](https://github.com/PugsyMAME/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Sunday 2022-11-13 15:57:02 by IlDucci

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
## [viethung204/PAINDEALER](https://github.com/viethung204/PAINDEALER)@[db651373ad...](https://github.com/viethung204/PAINDEALER/commit/db651373ad7f4d405b2e05a623f880f73cad8efd)
#### Sunday 2022-11-13 16:21:56 by viethung204

qol

fucking hell, everytime i watch my demo gameplay i spot a thing i want to improve

---
## [CSC207-2022F-UofT/course-project-team-communify](https://github.com/CSC207-2022F-UofT/course-project-team-communify)@[d2cd0893c1...](https://github.com/CSC207-2022F-UofT/course-project-team-communify/commit/d2cd0893c1c885bfecf5e8c4eee680a8e14e4a17)
#### Sunday 2022-11-13 17:41:30 by clin1967

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
## [LeCmnGend/kernel_xiaomi_ginkgo](https://github.com/LeCmnGend/kernel_xiaomi_ginkgo)@[9bd5e7ef23...](https://github.com/LeCmnGend/kernel_xiaomi_ginkgo/commit/9bd5e7ef23d4f6032865b9bf071d435f2ed1b547)
#### Sunday 2022-11-13 17:46:45 by Jason A. Donenfeld

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
## [zuoliang/Stockfish](https://github.com/zuoliang/Stockfish)@[cb9c2594fc...](https://github.com/zuoliang/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Sunday 2022-11-13 19:07:52 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [KDE/kate](https://github.com/KDE/kate)@[0fa7335476...](https://github.com/KDE/kate/commit/0fa73354761a0c297b32ad919135c6f0d0c72edf)
#### Sunday 2022-11-13 19:26:02 by Waqar Ahmed

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
## [FrootsieLoopsie/TP2-Metriques-de-qualite-de-logiciel](https://github.com/FrootsieLoopsie/TP2-Metriques-de-qualite-de-logiciel)@[5b62baf03f...](https://github.com/FrootsieLoopsie/TP2-Metriques-de-qualite-de-logiciel/commit/5b62baf03f847d5b238528236b40f7793528bcc2)
#### Sunday 2022-11-13 19:50:27 by AfraidOfCommits

Also, this is a freebie, but Maven too, you unfriendly garbage. I'll forgive you Maven for your many UX sins, but seriously, as a newbie to Intellij, fuck all this

---
## [Pedro-Bachiega/otservbr-global](https://github.com/Pedro-Bachiega/otservbr-global)@[fbd70d116c...](https://github.com/Pedro-Bachiega/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Sunday 2022-11-13 20:27:25 by rigis1

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
## [LeoDog896/hello-world.rs](https://github.com/LeoDog896/hello-world.rs)@[e5fd3e217a...](https://github.com/LeoDog896/hello-world.rs/commit/e5fd3e217ab9fd63b2325eee232d0d14cc5b45c7)
#### Sunday 2022-11-13 20:50:38 by Tristan F

Add a 🚀 (blazing) 🚀 fast security (lockdown) policy

Hello! You can call me Leo. I have over 7 years in full stack website development experience in areas such as React, Vue, Svelte, Angular, Nuxt, Next, and more! So much more in fact, that I made an entire private website specifically for my skills, so that way I can keep track of how skilled I am! As you can already tell from my Full Stack Web Development title, I even have lots of backend experience with Go, Rust, and Node.JS with nodemon and even typescript! I am familiar with all backend routing frameworks, and you may already know some popular ones like koa, fastify, or even express! I also am deeply knowledge in asynchronous JavaScript programming, and I know the ins and outs of Promises, as well as the internal knowledge of the web I gained from attending multiple w3c conferences. I am also familiar with developing for mobile, on both Android using Java, Kotlin, Scala, Groovy, or even Clojure, iOS with Swift or C#, or even multi-platform with Flutter! I have a lot of experience in theoretical typing design, and I can meta-program inside any turing-complete typing system such as Rust's typing system or TypeScript's typing system. I can work well in multithreaded enviornments such as Go. I can do both Object-Oriented Programming Design, Development, and Architecture with TypeScript and JavaScript. I can also do Functional Programming with Haskell, Elixr, Erlang, or Elm. I have deep optimization knowledge of many languages, from the JVM Hotspot assembly optimization program coming from Java 9 and UP, or the critical event loop present in many website-based projects. I can also work with many browser architectures, from webkit and gecko to even servo! My experience in freelancing is expancious, and I've been developing both on platform and off platform for 5 years differently. I can even develop in Zig as that is the fastest language the world has ever seen. I've also worked for many different companies in the past, and even once, despite the ever increasing tough website and software development job market, FAANG! I have a bachelors in Computer Science and I know highly theoretical computer development. I also have taken multiple bootcamps in graphic design, and can make your website look like the most beautiful thing, winning the www internet awards as the #1 contester! One thing you should know about me is how extensible and free my code is for your own tinkering and development! I've integrated with many products, including making SECURITY.md files for over 3 years. I am extremely passionate about making SECURITY.md files and am willing to go above and beyond to give you the product demonstration that you desire. I also have childhood experience with making SECURITY.md files and it was truly an inspiration to me from the get-go, introducing me to programming and getting to the way that I am now. Not only am I effective, but I am also fast. I even have experience with Developer Operations, and I know how I can get you from square 0 to square 100 fast and efficiently so that way you can automatically start using what I created for you! If you accept this PR, I can only promise you and give me your word hands down that I will complete your request with the fastest possible efficiency using a blazing fast framework like astro or swft and the best experience you'll ever have out of any of these candidates! Thanks for reading, and I'm very excited to work on this!

---
## [4sval/FModel](https://github.com/4sval/FModel)@[ad6c4b9474...](https://github.com/4sval/FModel/commit/ad6c4b947491669326e144badaa2079207fe404c)
#### Sunday 2022-11-13 21:10:26 by 4sval

fuck you bones position

that's a problem for future me

---
## [mateuszmandera/zulip](https://github.com/mateuszmandera/zulip)@[23a776c144...](https://github.com/mateuszmandera/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Sunday 2022-11-13 21:57:05 by Mateusz Mandera

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
## [alphagov/govuk-ruby-images](https://github.com/alphagov/govuk-ruby-images)@[5296d76f10...](https://github.com/alphagov/govuk-ruby-images/commit/5296d76f10c3ffa3489df6cf42ccc7d5bff9a7f0)
#### Sunday 2022-11-13 22:20:01 by Chris Banks

Wrap all Ruby binaries with the TMPDIR workaround script.

While I dislike adding yet another magicky layer of indirection, I think
this is less evil than expecting everyone to remember to prefix every
command with the wrapper script (e.g. on every `rails console`, rake
task, etc.)

Also make the script a bit more user-friendly and robust against loops
in case it's ever mistakenly run as a subprocess of itself.

---
## [beckerMel/Assignment5](https://github.com/beckerMel/Assignment5)@[5991686d35...](https://github.com/beckerMel/Assignment5/commit/5991686d355dcd1e9f21826d0a886b0bd076ff58)
#### Sunday 2022-11-13 23:06:17 by Melanie Becker

I hate my life also here's the model interface and some adjustments based on that

---

