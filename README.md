## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-17](docs/good-messages/2022/2022-10-17.md)


2,233,990 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,233,990 were push events containing 3,335,207 commit messages that amount to 264,594,075 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [scionalu/lobotomy-corp13](https://github.com/scionalu/lobotomy-corp13)@[0220bde488...](https://github.com/scionalu/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Monday 2022-10-17 00:36:20 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [Darknesshaz/tgstation](https://github.com/Darknesshaz/tgstation)@[3b2cf65d59...](https://github.com/Darknesshaz/tgstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Monday 2022-10-17 02:06:58 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [SuperHarmony910/superharmony-polls](https://github.com/SuperHarmony910/superharmony-polls)@[4f4f8fc4d3...](https://github.com/SuperHarmony910/superharmony-polls/commit/4f4f8fc4d31b4755261a08fb54066a3950bfd8ac)
#### Monday 2022-10-17 02:07:08 by SuperHarmony910

Finally. the options work. Removed polls/id/post btw. Started more work on Discord token thingy, fixed typescript issues
IM SO HAPPY BUT IM WRITING THIS IN THE OTHER COMMIT MESSAG EHAFJKMASDJLDLSFJKSLAJK
lmfao for the typescript issues it was just not having `.env` at all bcs im at school in science and i do my coding usually on my pc...
keybase >>>>>
thank you keybase for letting me transfer my files across between my desktop computer and laptop easily
Also thank myself for remembering to put it into keybase
thank you for reading this :)

---
## [MajManatee/Yogstation](https://github.com/MajManatee/Yogstation)@[9118cab4fd...](https://github.com/MajManatee/Yogstation/commit/9118cab4fda02a964b40895aa7aedf3dd55580ef)
#### Monday 2022-10-17 02:59:56 by Redmoogle

ports fake viruses from tgstation (#15412)

* fakevirus

* fuck you too byond

* Update code/datums/status_effects/debuffs.dm

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

---
## [woodsts/linux-stable-rt](https://github.com/woodsts/linux-stable-rt)@[7112098b69...](https://github.com/woodsts/linux-stable-rt/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Monday 2022-10-17 03:33:38 by Jason A. Donenfeld

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
## [water-sucks/nixed](https://github.com/water-sucks/nixed)@[dc2cd0558f...](https://github.com/water-sucks/nixed/commit/dc2cd0558fcd5a3b7fcab2ee6e2909d7536a493d)
#### Monday 2022-10-17 03:42:34 by Varun Narravula

Remove digga entirely and replace with flake-parts

This is a rather large commit, because of all of the refactoring;
while I hate large commits, because you can't really bisect them,
this one was a sad necessity to keep things atomic, in a sense that
my commits are ideally supposed to be working revisions I can switch
to at any time if I wish to.

- Remove flake-utils and all digga flake inputs
- Add flake-parts input
- Update nix-darwin input so it would stop complaining about runCommand
- Create custom lib with functions to generate modules for
  profiles/users
- Replace all invocations of specialArgs with profiles/suites to use
  generated modules with genModules
- Fix boot issues by moving out Plymouth configuration into a profile
  and manually allowing redistributable firmware
- Replace systemd-boot with grub (sadly, I found this to be a much
  easier path to troubleshooting stuff if booting goes haywire)
- Change hm-system-defaults to user-defaults and set home-manager
  options there
- Replace weird override mechanism for mixing different nixpkgs
  inputs with a simple overlay
- Override nvim configuration to be use stable versions of broken
  plugins (in line with previous)
- Move nix settings into a single common profile
- Add single argument to all profiles so that they can be
  imported and called as functions by genProfileOption
- Rekey secrets (agenix gave me hell about this and wouldn't let
  me log in, presumably because the hashing changed?)
- Move rofi-power-menu into separate profile to prevent callback hell

---
## [michaelherold/pyIsEmail](https://github.com/michaelherold/pyIsEmail)@[46c1d9d310...](https://github.com/michaelherold/pyIsEmail/commit/46c1d9d310c90007628d2cb7583785d32d81157d)
#### Monday 2022-10-17 03:59:26 by Michael Herold

Switch to use Hatch to manage the project

Hatch seems like it has enough mind share and compatibility that it
makes sense to switch to it as a project management tool. It reduces the
number of configuration files to one, can manage multiple Pythons and
multiple execution environments, and generally has all of the
affordances I feel that we need to manage things.

This change was spurred by my needing to look up once again how to
release the library. This was the last straw because I don't spend much
time working in Python these days and can't remember how to do it every
time I want to release a new version.

This should be a major quality of life improvement for anyone wanting to
work on the project.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b66f50bd48...](https://github.com/san7890/bruhstation/commit/b66f50bd48be4077389bc8b9d2ad1c4124441754)
#### Monday 2022-10-17 04:11:29 by san7890

ALVIN WHO THE FUCK DID BYOND REGEX (third iteration)

okay the regex thing is partially my fault because it was a bit shit ngl

it still sucks though. buncha re-organization of Run()

---
## [eddysanoli/infinito27.com](https://github.com/eddysanoli/infinito27.com)@[168984b040...](https://github.com/eddysanoli/infinito27.com/commit/168984b04004c7bb330ecc609f589e187eac2544)
#### Monday 2022-10-17 04:22:41 by Eduardo Santizo

New Readme and TTL for DNS

Documented all the new nuances of the new deployment setup in the Readme file. I also did a sanity check and tore down the entire application, just to have it set back up using both Terraform and the provisioner. Had to implement new changes because of this:
- Removed the "hosts" file from the repo. I have changed the IP associated with my site so the presence of a previous version of the file doesn't really matter.
- Made it so that "hosts.tpl" now empties the hosts file and then adds the new webservers instead of just appending text at the end of the existing file.
- Discovered the existence of DNS caching. When I changed the IP associated with my domain name, I realized that the address "www.infinito27.com" kept resolving to the previous IP. Dissapointed, I went ahead and tried to solve this but the solution was to "wait". Who has that kind of time?? So I went ahead and tried to speed it up by including a TTL value for the cache found in the DNS server and its associated domains (inside of "main.tf"). Waited the 30 seconds that I set them to and voila! Nothing... fuck me. Apparently DNS servers take the TTL value as more of a suggestion than an actual order so now I have to wait between 3 to 24 hours to see changes. DAMN YOU DNS CACHING!

---
## [ghostabyssnet/barbara_engine](https://github.com/ghostabyssnet/barbara_engine)@[a98f715830...](https://github.com/ghostabyssnet/barbara_engine/commit/a98f71583034b14897d50fd714d912600af574c4)
#### Monday 2022-10-17 06:10:59 by ghost

holy fuck this abomination WORKS it WORKS goddamnit

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[0ecdccb774...](https://github.com/iandol/Psychtoolbox-3/commit/0ecdccb774ab08cbd27b69ac681420ca4827279e)
#### Monday 2022-10-17 08:05:18 by Mario Kleiner

PsychVulkan/Linux: Add new bug fix for Mesa Vulkan direct display bug.

As of current Mesa 22.3-devel git snapshot and earlier versions, running
in fullscreen Vulkan direct-display mode only works the first time in a
session. On successive runs, the driver will error in vkQueuePresentKHR()
with a VK_ERROR_SURFACE_LOST error, and we are dead with a hard hang!

This only happens if the RandR output which we lease and switch to Vulkan
direct display mode has a non-zero (x,y) top-left corner viewport offset,
not on a single-display setup, a mirror setup, or a one video output per
X-Screen multi-X-Screen/multi-Display setup, as in those configs, the
viewport offset is always (0,0). Multi-output on single X-Screen however
dies for all but the one output at (0,0).

I tracked this down to a Mesa/Vulkan/WSI/DirectDisplay state caching bug,
developed and tested a bug fix and will upstream that fix soon. Basically
the WSI internal wsi_display_connector->active state for the used output
does not get reset to false == Inactive at the end of a session when the
display gets released back to the Window server / X-Server at call to
vkReleaseDisplay(). So if the same output is switched to direct display
mode again in the next session, with the same video mode, WSI thinks the
output is still active and at proper video mode and skips a full modeset,
instead directly goes to pageflip submission. This goes ok for a output
with RandR viewport (0,0, fbwidth, fbheight), but on a RandR output with
non-zero (x,y) offsets, the X-Server will have set a mode with corresponding
offsets into the X-Screens big shared (across all RandR outputs / crtcs).
The current Vulkan WSI has a framebuffer per VKDisplay and requires a
viewport offset of (0,0), so the viewport fits into the Vulkan framebuffer.
This is violated if WSI skips the modeset to (0,0) offset, and the kernel
subsequently aborts the pageflip with a -ENOSPACE error code, which itself
puts the Vulkan swapchain into VK_ERROR_SURFACE_LOST state and game over!

Error handling as recommended by spec (destroy and recreate the swapchain)
would not help, as connector state is cached at VkInstance level, not at
swapchain level.

A proper fix is to reset WSI connector logical state to inactive at
vkReleaseDisplay() time - Fix to be upstreamsn.

Our hacky workaround is to detect the trigger condition fullscreen on
output with non-zero (x,y) offset on a Mesa Vulkan driver with a Mesa
version before the properly fixed version, and then schedule a
'clear PsychVulkanCore' between runs to completely destroy the Vulkan
instance, thereby get rid of the stale connector state cache. This
resolves the bug for now. Ergo reenable that ugly needsMesaDDMWa=1 full
driver shutdown workaround again on Linux + Fullscreen + Mesa < 30.0.0,
until my bug fix makes it into a Mesa bug fix upstream release.

-> With this workaround, the PsychImaging 'MirrorDisplayTo2ndOutputHead'
   display mirroring with Vulkan for primary stimulus window and standard
   Screen OpenGL for the experimenter feedback "Mirror" slave window now
   works as tested on a single-X-Screen, dual-display setup under both
   Ubuntu 20.04.5-LTS, X-Server 1.20.13 with Intel Kabylake gpu and on
   Ubuntu 22.04.1-LTS, X-Server 21 with AMD Polaris gpu, where the main
   Vulkan onscreen window is fullscreen on a 120 Hz refresh video output,
   and the OpenGL mirror slave window is windowed on a standard 60 Hz
   standard KDE or Ubuntu desktop GUI. Main stimulation runs unthrottled
   with perfect timing at full 120 fps on 120 Hz display, whereas the
   mirror window tears on the 60 Hz display, as expected, with effects
   more spectacular when the desktop compositor is off than when it is on.

   Testing on macOS 12.6 on same setup with AMD Polaris showed that it
   works as well, both in Vulkan mode and OpenGL native mode, and the
   framerate is improved with slave window vsync off, but the improvement
   is more modest and performance of the same hardware under macOS 12 is
   much worse than under Ubuntu 22.04.1-LTS. But this is due to macOS
   deficiency, not problems with our mirroring approach.

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[5e67e1c1c6...](https://github.com/iandol/Psychtoolbox-3/commit/5e67e1c1c696a2f5912a9e033cb8e78fa041f3bc)
#### Monday 2022-10-17 08:05:18 by Mario Kleiner

Screen/Linux/GLX: Rewrite PsychOSSetVBLSyncLevel() for best vsync control.

Mesa supports GLX_EXT_swap_control since Mesa 20.3.0, and the proprietary
drivers from NVidia since 2011, from ATI since 2013, so any non-ancient
Linux distro should have it for the same functionality as our previously
used GLX_MESA_swap_control on MESA, but more efficient, as it saves an
OpenGL context switch, and cross-vendor OSS and proprietary.

We keep the GLX_MESA_swap_control fallback, which should work on all
FOSS drivers since around 2003. For completeness also support the very
limited lowest common denominator fallback GLX_SGI_swap_control from before
the year 2000, assuming we'll never hit it ever again. It doesn't allow
query of actual swap interval, and worse, it doesn't allow zero swap
interval, so one can't programmatically disable vsync for benchmarking,
certain debugging and diagnostics, windowed NetWM timing or for
mirror mode with high efficiency - all thing that need vsync disable.

Now we fully rely on GLEW for detecting and setting up extensions instead
of a mix of GLEW, own extension queries and function pointer hackery. This
also removes that weird bug where vsync can't get disabled during the first
session after startup or clear Screen, clear all etc, but only on followup
runs. Turned out on first run, glXSwapIntervalSGI() was bound, which would
error out on vsync disable requests, but on successive runs, the proper
glXSwapIntervalMESA() was bound to the glXSwapIntervalSGI function pointer.
Weird, but true, as long debugging with the debugger showed. It baffles me
how this is possible at all?!? Probably weird interactions between our
pointer assignments, GLEW, and possible GL vendor neutral dispatch??

Anyway, this rewrite makes us more efficient and clean and fixes that
annoying bug.

We should get optimal swap control this way on MESA back to the year 2003,
and on NVidia/ATI proprietary back to the years 2011 (NVidia) and 2013 (AMD).

Tested on Intel + Mesa 21.2.6 Ubuntu 20.04.5-LTS so far.

---
## [RaghuVarma331/android_kernel_nokia_FIH-SDM660](https://github.com/RaghuVarma331/android_kernel_nokia_FIH-SDM660)@[91000fb010...](https://github.com/RaghuVarma331/android_kernel_nokia_FIH-SDM660/commit/91000fb0109cecb5716036a7cc7535748141e9fb)
#### Monday 2022-10-17 08:13:04 by Christian Brauner

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
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[79a64d0ef9...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/79a64d0ef99f386f584bb5297ef3fe9b2a34ecdd)
#### Monday 2022-10-17 08:17:40 by petrero

21.6 Pagination

  Styling the Pagination Links
  - Though, this is still super ugly. Fortunately, the bundle does give us a way to control the markup that's used for the pagination links. And it even comes with automatic support for Bootstrap CSS-friendly markup. We just need to tell the bundle to use that.

  So... we need to configure the bundle. But... the bundle didn't give us any new config files when it was installed. That's okay! Not all new bundles give us config files. But as soon as you need one, create one! Since this bundle's called BabdevPagerfantaBundle, I'm going to create a new file called babdev_pagerfanta.yaml. As we learned in the last tutorial, the name of these files aren't important. What's important is the root key, which should be babdev_pagerfanta. To change how the pagination renders, add default_view: twig and then default_twig_template set to @BabDevPagerfanta/twitter_bootstrap5.html.twig.

  Like any other config, there's no way you would know that this is the correct configuration just by guessing. You need to check out the docs.

  If we go back and refresh... huh, nothing changed. This is a little bug that you sometimes run into in Symfony when you create a new configuration file. Symfony didn't notice it... and so it didn't know it needed to rebuild its cache. This is a super rare situation, but if you ever think it might be happening, it's easy enough to manually clear the cache by running:

    php bin/console cache:clear
  And... oh... it explodes. You probably noticed why. I love this error!

    There is no extension able to load the configuration for "baberdev_pagerfanta"

  It's supposed to be babdev_pagerfanta. Whoops! And now... perfect! It's happy. And when we refresh... it sees it! In a real project, we'll probably want to add some extra CSS to make this "dark mode"... but we've got it.

  Okay team, we're basically done! As a bonus, we're going to refactor this pagination into a JavaScript-powered forever scroll... except plot twist! We're going to do that without writing a single line of JavaScript. That's next.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[f3f67e81b4...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/f3f67e81b401cf017cdacdb88febd8c63b0a7f23)
#### Monday 2022-10-17 08:17:40 by petrero

21.4 Pagination

  Back in our template, find the {% endfor %}, and right after, say {{ pagerfanta() }}, passing it the pager object.

  Check it out! When we refresh... we have links at the bottom! They're... ugly, but we'll fix that in a minute.

  If you click the "Next" link, up in our URL, we see ?page=2. Though... the results don't actually change. We're still seeing the same results from Page 1. And... that makes sense. Remember, back in VinylController, I hardcoded the current page to 1. So even though we have ?page=2 up here, Pagerfanta still thinks we're on Page 1.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[608cf397d5...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/608cf397d5c34a9909650433996cc5d96c8a1451)
#### Monday 2022-10-17 08:17:40 by petrero

18.2 Clean URLs with Sluggable

  Adding the Slug Property
  - First, we need a slug property on our entity. To add it, at your terminal, run:

    php bin/console make:entity
  Update VinylMix to add a new slug field. This will be a string, and let's limit it to a 100 characters. Also make this not nullable: it should be required in the database. And that's it! Hit enter one more time to finish.

  That, not surprisingly, added a slug property.. plus getSlug() and setSlug() methods at the bottom.

  One thing the make:entity command doesn't ask you is whether or not you want a property to be unique in the database. In slug's case, we do want it to be unique, so add unique: true. That will add a unique constraint in the database to make sure that we never get duplicates.

  Before we think about any sluggable magic, generate a migration for the new property:

    symfony console make:migration
  As usual, I'll open up that new file to make sure it looks okay. And... it does! It adds slug including a UNIQUE INDEX for slug. And when we run it with

    symfony console doctrine:migrations:migrate
  it explodes... for the same reason as last time: Not null violation. We're adding a new slug column to our table that is not null... which means that any existing records won't work. As I said in the previous chapter, if your database is already on production, you would need to fix this. But since ours is not, we can cheat and reset the database like we did before:

    symfony console doctrine:database:drop --force
  Then:

    symfony console doctrine:database:create
  Finally re-run all of the migrations from the very beginning:

    symfony console doctrine:migrations:migrate
  And... yes! 4 migrations executed.

---
## [fabiankohlhaas/website](https://github.com/fabiankohlhaas/website)@[01fa91aa50...](https://github.com/fabiankohlhaas/website/commit/01fa91aa50ac0b65d57bfc88e0c97da27819895c)
#### Monday 2022-10-17 09:25:24 by Fabian Kohlhaas

Add polar bear attribution link

Bitters chillwave mustache master cleanse kickstarter chia literally forage fingerstache pabst direct trade yr kitsch neutra copper mug. Lumbersexual thundercats godard, activated charcoal gentrify affogato hell of ramps shabby chic DSA chillwave chartreuse farm-to-table. Ascot actually unicorn, cornhole yr church-key try-hard roof party pour-over distillery freegan. Ethical retro unicorn distillery street art live-edge offal enamel pin poutine typewriter literally 90's. Bespoke biodiesel cold-pressed fixie jianbing helvetica banh mi kale chips dreamcatcher pabst.

---
## [SSparks31/ED2](https://github.com/SSparks31/ED2)@[76ccdaebb3...](https://github.com/SSparks31/ED2/commit/76ccdaebb3fc8a1f6fdb7ddcdbe694e9b597f2d0)
#### Monday 2022-10-17 09:36:10 by SSparks31

Stupid ass intersection test lmao what the fuck am I doing with my life

---
## [ardianta/anime-for-dev](https://github.com/ardianta/anime-for-dev)@[d621f8de0f...](https://github.com/ardianta/anime-for-dev/commit/d621f8de0f4427a22286d034e7fd9b9c43a30148)
#### Monday 2022-10-17 10:49:36 by Gourav Dutta

Add Mob Psycho 100

**Title**: Mob Psycho 100
 **Link**: https://myanimelist.net/anime/32182/Mob_Psycho_100

**Why this anime should watched by developer?**

This anime is about a psychic middle school boy who tries to live a normal life and keep his growing powers under control, even though he constantly gets into trouble.As he grows he wants to find his purpose in life and wants to live a happy life.This anime teaches us many values on finding purpose in life and live a happy life.Also this anime has a good sense of humour in it and helps us to relax after completing a busy day.

---
## [avar/git](https://github.com/avar/git)@[2c77ed38d9...](https://github.com/avar/git/commit/2c77ed38d9006de161288106a3fb39fb6120ab0a)
#### Monday 2022-10-17 11:10:49 by Ævar Arnfjörð Bjarmason

submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior, even when that behavior is stupid. Some
of it we'll fix in subsequent commits, but let's first faithfully
reproduce the behavior.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

The pattern of using "define BUILTIN_" macros here isn't needed for
now, but as we'll move code out of "builtin/submodule--helper.c" we'll
want to re-use these strings. See 8757b35d443 (commit-graph: define
common usage with a macro, 2021-08-23) and 1e91d3faf6c (reflog: move
"usage" variables and use macros, 2022-03-17) for prior art using this
pattern.

The "(argc < 2 || !strcmp(argv[1], "-h"))" path at the top of
cmd_submodule__helper() could now be a "(argc < 2)" if not for
t0012-help.sh (which invokes all built-ins manually with "-h"). Let's
leave it for now, eventually we'll consolidate the two.

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [ZeroCool940711/stable-diffusion-webui](https://github.com/ZeroCool940711/stable-diffusion-webui)@[468d468fbb...](https://github.com/ZeroCool940711/stable-diffusion-webui/commit/468d468fbb4c48f213db38ebbc1be9809cbfc6be)
#### Monday 2022-10-17 11:35:31 by Ruslan Sheptolut

Don't ask about restoring stash if nothing was stashed (#1533)

# Description

Minor quality of life update.

Recently launching the webui.bat became a bit more annoying, as it
always asks about restoring changes, even if I have none, and then it
needs another interaction for no reason (pause>nul).

This change makes sure the interaction is only needed when there were
changes stashed, and removes the second pause.

Yesterday I double clicked the shortcut to start the Stable Horde worker
overnight, and even noticed the "Y/N" prompt, but went to bed not
realizing it also does the (pause>nul) after that... No reason to be
this intrusive.

Closes: #1532

# Checklist:

- [X] I have changed the base branch to `dev`
- [X] I have performed a self-review of my own code
- [X] I have commented my code in hard-to-understand areas
- [X] I have made corresponding changes to the documentation

---
## [Parsifal-M/opa](https://github.com/Parsifal-M/opa)@[965301f90e...](https://github.com/Parsifal-M/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Monday 2022-10-17 11:54:31 by Stephan Renatus

ast: support dotted heads (#4660)

This change allows rules to have string prefixes in their heads -- we've
come to call them "ref heads".

String prefixes means that where before, you had

    package a.b.c
    allow = true

you can now have

    package a
    b.c.allow = true

This allows for more concise policies, and different ways to structure
larger rule corpuses.

Backwards-compatibility:

- There are code paths that accept ast.Module structs that don't necessarily
  come from the parser -- so we're backfilling the rule's Head.Reference
  field from the Name when it's not present.
  This is exposed through (Head).Ref() which always returns a Ref.

  This also affects the `opa parse` "pretty" output:

  With x.rego as

    package x
    import future.keywords
    a.b.c.d if true
    e[x] if true

  we get

    $ opa parse x rego
    module
     package
      ref
       data
       "x"
     import
      ref
       future
       "keywords"

     rule
      head
       ref
        a
        "b"
        "c"
        "d"
       true
      body
       expr index=0
        true
     rule
      head
       ref
        e
        x
       true
      body
       expr index=0
        true

  Note that

    Name: e
    Key: x

  becomes

    Reference: e[x]

  in the output above (since that's how we're parsing it, back-compat edge cases aside)

- One special case for backcompat is `p[x] { ... }`:

    rule                    | ref   | key | value | name
    ------------------------+-------+-----+-------+-----
    p[x] { ... }            | p     | x   | nil   | "p"
    p contains x if { ... } | p     | x   | nil   | "p"
    p[x] if { ... }         | p[x]  | nil | true  | ""

  For interpreting a rule, we now have the following procedure:

  1. if it has a Key, it's a multi-value rule; and its Ref defines the set:

     Head{Key: x, Ref: p} ~> p is a set
     ^-- we'd get this from `p contains x if true`
         or `p[x] { true }` (back compat)

  2. if it has a Value, it's a single-value rule; its Ref may contain vars:

     Head{Ref: p.q.r[s], Value: 12} ~> body determines s, `p.q.r.[s]` is 12
     ^-- we'd get this from `p.q.r[s] = 12 { s := "whatever" }`

     Head{Key: x, Ref: p[x], Value: 3} ~> `p[x]` has value 3, `x` is determined
                                          by the rule body
     ^-- we'd get this from `p[x] = 3 if x := 2`
         or `p[x] = 3 { x := 2 }` (back compat)

     Here, the Key isn't used, it's present for backwards compatibility: for ref-
     less rule heads, `p[x] = 3` used to be a partial object: key x, value 3,
     name "p"

- The destinction between complete rules and partial object rules disappears.
  They're both single-value rules now.

- We're now outputting the refs of the rules completely in error messages, as
  it's hard to make sense of "rule r" when there's rule r in package a.b.c and
  rule b.c.r in package a.

Restrictions/next steps:

- Support for ref head rules in the REPL is pretty poor so far. Anything that
  works does so rather accidentally. You should be able to work with policies
  that contain ref heads, but you cannot interactively define them.
  
  This is because before, we'd looked at REPL input like

      p.foo.bar = true

  and noticed that it cannot be a rule, so it's got to be a query. This is no
  longer the case with ref heads.

- Currently vars in Refs are only allowed in the last position. This is expected
 to change in the future.

- Also, for multi-value rules, we can not have a var at all -- so the following
  isn't supported yet:

      p.q.r[s] contains t if { ... }

-----

Most of the work happens when the RuleTree is derived from the ModuleTree -- in
the RuleTree, it doesn't matter if a rule was `p` in `package a.b.c` or `b.c.p`
in `package a`.

As such, the planner and wasm compiler hasn't seen that many adaptations:

- We're putting rules into the ruletree _including_ the var parts, so

  p.q.a = 1
  p.q.[x] = 2 { x := "b" }

  end up in two different leaves:

  p
  `-> q
       `-> a = 1
       `-> [x] = 2`

- When planing a ref, we're checking if a rule tree node's children have
  var keys, and plan "one level higher" accordingly:

  Both sets of rules, p.q.a and p.q[x] will be planned into one function
  (same as before); and accordingly return an object {"a": 1, "b": 2}

- When we don't have vars in the last ref part, we'll end up planning
  the rules separately. This will have an effect on the IR.

  p.q = 1
  p.r = 2

  Before, these would have been one function; now, it's two. As a result,
  in Wasm, some "object insertion" conflicts can become "var assignment
  conflicts", but that's in line with the now-new view of "multi-value"
  and "single-value" rules, not partial {set/obj} vs complete.
* planner: only check ref.GroundPrefix() for optimizations

In a previous commit, we've only mapped

    p.q.r[7]

as p.q.r;  and as such, also need to lookup the ref

    p.q.r[__local0__]

via p.q.r

(I think. Full disclosure: there might be edge cases here that are unaccounted
for, but right now, I'm aiming for making the existing tests green...)


New compiler stage:

In the compiler, we're having a new early rewriting step to ensure that the
RuleTree's keys are comparible. They're ast.Value, but some of them cause us
grief:

- ast.Object cannot be compared structurally; so

      _, ok := map[ast.Value]bool{ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")}): true}[ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")})]

  `ok` will never be true here.

- ast.Ref is a slice type, not hashable, so adding that to the RuleTree would
  cause a runtime panic:

      p[y.z] { y := input }

  is now rewritten to

    p[__local0__] { y := input; __local0__ := y.z }

This required moving the InitLocalVarGen stage up the chain, but as it's still
below ResolveRefs, we should be OK.

As a consequence, we've had to adapt `oracle` to cope with that rewriting:

1. The compiler rewrites rule head refs early because the rule tree expects
   only simple vars, no refs, in rule head refs. So `p[x.y]` becomes
   `p[local] { local = x.y }`
2. The oracle circles in on the node it's finding the definition for based
   on source location, and the logic for doing that depends on unaltered
   modules.

So here, (2.) is relaxed: the logic for building the lookup node stack can
now cope with generated statements that have been appended to the rule bodies.


There is a peculiarity about ref rules and extents:

See the added tests: having a ref rule implies that we get an empty object
in the full extent:

    package p
    foo.bar if false

makes the extent of data.p: {"foo": {}}

This is somewhat odd, but also follows from the behaviour we have right now
with empty modules:

    package p.foo
    bar if false

this also gives data.p the extent {"foo": {}}.

This could be worked around by recording, in the rule tree, when a node was
added because it's an intermediary with no values, but only children.

Signed-off-by: Stephan Renatus <stephan.renatus@gmail.com>

---
## [AndASM/buildah](https://github.com/AndASM/buildah)@[2adbe2a58a...](https://github.com/AndASM/buildah/commit/2adbe2a58a77b014be59c68abf58b682ad5e5c20)
#### Monday 2022-10-17 12:49:45 by Ed Santiago

System test cleanup: document, clarify, fix

Primary purpose: fix "preconfigured TARGETARCH/etc" test so
it will work under podman and on multiarch.

Root cause of it not working: I mistakenly advised @flouthoc,
in #4310, to write a containerfile in $TEST_SCRATCH_DIR. I
thought it was an empty directory. Big, big mistake. (Sorry,
Aditya). Document this near the variable definition, and
fix the test once again.

@nalind pointed out that the containerfile doesn't need to
be generated on-the-fly, so, use a static one. In the spirit
of DIE, read the TARGETxxx vars from it. Not that we're
expecting more variables, but, it's just cleaner.

Also, as long as I'm here: in run_buildah, when logging the
command being run, use #/$ prompt for root/rootless. I was
getting too confused looking at logs of root runs.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [thierrylach/NetHack](https://github.com/thierrylach/NetHack)@[4c98ba493b...](https://github.com/thierrylach/NetHack/commit/4c98ba493bb7eaa7c556c4b720a7b6df7ea74d0e)
#### Monday 2022-10-17 12:50:40 by Michael Meyer

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[38565e79f8...](https://github.com/cockroachdb/cockroach/commit/38565e79f832bcf5a9ad90028b796380dc73319f)
#### Monday 2022-10-17 13:20:25 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [erikgrinaker/cockroach](https://github.com/erikgrinaker/cockroach)@[f50670b344...](https://github.com/erikgrinaker/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Monday 2022-10-17 13:32:17 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [hexagontruth/hexagontruth](https://github.com/hexagontruth/hexagontruth)@[ea1de447db...](https://github.com/hexagontruth/hexagontruth/commit/ea1de447db6cc2132a1f2ae12a0f5366fbfb000d)
#### Monday 2022-10-17 16:03:38 by graham

Various final changes

- This sort of sucks
  - Well short of where I would like to be vis-a-vis shader-driven visual elements
  - Hampered by weird bugs and inconsistencies across browsers, as well as to be frank basic user hardware concerns
    - Tho everything I've done so far (including the abortive videos-thru-shader-layer thing) works fine on all my machines
  - Have already spent too much time on this
- Moved media to separate GP repo
  - Add whole-ass Express server for local static media
  - Will squash all remaining media files out of master branch I think
  - Is not ideal, and requires hard-coding non-development static port number in the client files
    - Must be a better way to do this?
- The background was only meant to be a placeholder, but now I have doubts as to whether it can even support a full two-layer CA program
  - Will probably try anyway

---
## [sailfishos-mirror/glib](https://github.com/sailfishos-mirror/glib)@[b8e1ecdd6b...](https://github.com/sailfishos-mirror/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Monday 2022-10-17 16:17:43 by Michael Catanzaro

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
## [SwedishKaito/Lost-Era-Modpack](https://github.com/SwedishKaito/Lost-Era-Modpack)@[300d72c910...](https://github.com/SwedishKaito/Lost-Era-Modpack/commit/300d72c9100474130a177c853b3bf9aef4d0eefa)
#### Monday 2022-10-17 17:41:46 by TechnoParadox

v1.5.3

-The modpack will check for the user RAM before launch
-Waystones work interdimensionally (includes scrolls)
-Re-enabled thaumcraft 4 metal transmutations
-Disabled Wizardry's Disarmament spells on players
-Disabled unnecessary update checkers
-Reduced the deafening from Waystones by 60%
-Increased visibility while under the night sky
-Gardens are now spreadable but only drop seeds
-Buffed weak food value of some foods
-Hunger is now easier on lower difficulties
-Healing no longer consumes hunger
-GT4 Ores now have tooltips indicating where these are found
-Completely reworked Project Red pipes into Thaumcraft 4 including Thaumonomicon entries
-Added TC4 aspects for dozens of mobs and blocks
-Added dozens of entries to TC4 Crop and meat duplication
-NEI item visibility now handled by INPure
-Nerfed Mek's wind generation at higher altitude but buffed at lower ones
-Buffed Mek's Energy Storage multiblock
-Rework energy consumption of every Mek Machine (mostly lower consumption)
-Minechem can now decompose farmable materials
-Totem of Undying can now be found as loot
-Whitestone is now made from Totem of Undying
-Volcanos are now made of obsidian
-Reduced Grow Light consumption
-Fixed potential Potion ID conflicts
-Fixed Bees spawning harmful flora
-Buffed GT4 ore distribution in specific scenarios
-Fixed GT4 ore generation in the Nether
-Reworked Extra TiC compatibility
-Buffed weak fuels for the Compression and Energizing Dynamos
-Metallurgy metal and Tinker Metals now share the same stats
-Buffed Gas and RF capacity of Compact Machines
-Blacklisted XP Phial from Loonium
-Phantom Hands have a running cost of 10 LP
-Reworked Dagger of Sacrifice and Sacrificial Dagger
-Every instance of Ghast and Blaze now shed their items overtime
-Blaze Lamp cannot be used as furnace fuels anymore as a result of the above
-Soul Campfire no longer can be automated with hoppers
-Buffed TC4 Magic Biomes occurrences
-Disabled Ender Collector (unfixable dupe)
-Disabled Ender Dragon Girl
-Disabled Magnetic Force
-Disabled AE2 quartz tools
-Buffed Ars Magica 2 recipes
-Fixed End Crystal exploit
-Food records no longer persist through death
-Added missing recipes for AE2 Cards
-Extra TiC's Mana Steel parts are obtained by throwing iron parts in a mana pool
-Extra TiC's Thaumium parts are obtained by throwing iron parts in a cauldron with Praecantatio
-Extra TiC's magic materials can no longer be crafted in the Tool Table
-Added Smeltery integration to Extra TiC's magic materials
-Cheaper QED
-Snails are no longer fishes
-Wild Barley has been nerfed to be worst than barley (still grows 3x faster)
-Salt is now created by cooking water buckets
-Additional foods from the drying rack
-Cheaper Safari nets and Porta Spawners
-You can now empty Nuclearcraft capsules
-Remove the necessity of plates in the RF technological tree
-Removed needlesss microcrafting form Steve's Carts

---
## [postgres/postgres](https://github.com/postgres/postgres)@[8272749e8c...](https://github.com/postgres/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Monday 2022-10-17 18:02:21 by Tom Lane

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
## [usdigitalresponse/univaf](https://github.com/usdigitalresponse/univaf)@[d4d0162723...](https://github.com/usdigitalresponse/univaf/commit/d4d01627230554f2bb38f84f281622110f2eae5f)
#### Monday 2022-10-17 18:51:42 by Rob Brackett

Use more smaller API server instances

One lesson from rebuilding things on AWS is that we just don't use much memory in the API server. We can't reduce RAM without also cutting the CPU in half, but my working theory is that we can just double the instances and it should be fine. We'll follow the charts and see how this goes (honestly I think a baseline of more instances might make the whole thing more stable anyway).

---
## [alexhb1/mapUON](https://github.com/alexhb1/mapUON)@[e6372d4c4c...](https://github.com/alexhb1/mapUON/commit/e6372d4c4c09ea610a0b8fb9d402ba0599ff4510)
#### Monday 2022-10-17 19:00:46 by PennSylvannia

holy fuck its october

my life is slipping away like sand through an hour glass
its exceptionally unpleasant and wedged in my ass

---
## [gnprice/zulip-mobile](https://github.com/gnprice/zulip-mobile)@[e117df5f73...](https://github.com/gnprice/zulip-mobile/commit/e117df5f7375eecf6d50156038e6f699e3a6c04c)
#### Monday 2022-10-17 19:25:44 by Greg Price

Fix major startup lag, by using Animated.loop instead of giant duration

This was always a silly-looking hack: what we really want is for
this animation to loop indefinitely, and we do that by saying it
runs for 1000 seconds.

It turns out that doing that makes it extremely slow to start up!
Specifically, in my desktop Android emulator (which is typically
1x-2x the speed of my physical Pixel 4), it takes about 500ms.

Worse: it blocks the entire JS thread while it does that.  So
the app's whole UI is stalled.

Because we use this at startup (in LoadingIndicator), it's been
adding that 500ms of lag (likely more like 1000ms on many devices)
to our startup time since forever.  Moreover, we use
LoadingIndicator in the "Connecting..." banner... which there's
*four* of, one on each of the app's main-screen tabs.  So when we
start loading -- which is promptly after each startup, if you're
already logged in -- the UI hangs for another 2000ms, or more
depending on device.

There are a number of things we could do here.  It seems like a
performance bug in RN's `Animated`.  Also we could shorten the
1000 seconds to like 100 seconds, or 50 seconds -- better that
you occasionally see a stopped spinner, if you've already waited
a long time, than that you find the app completely stuck for a
full second or more every time you start it.

But in fact a very simple solution is available: if you take a look
at the upstream docs for Animated:
  https://reactnative.dev/docs/animated
there is built-in support for just explicitly having a loop.
There's no need for this hack at all.  Even in RN v0.47.2, the
version we were using when this hack was introduced in 2017 in
6594f8ebc, there was an `Animated.loop` and there was no need
for this hack.

So use that.

---
## [SOROM2/rc-configs](https://github.com/SOROM2/rc-configs)@[4a0a283b1d...](https://github.com/SOROM2/rc-configs/commit/4a0a283b1d98c7435c3fe3697e94a51ef7453d7f)
#### Monday 2022-10-17 19:39:14 by Mason

move to i3, fuckloads of changes can't remember sorry

---
## [chellmuth/OpenShadingLanguage](https://github.com/chellmuth/OpenShadingLanguage)@[e4e5088ed6...](https://github.com/chellmuth/OpenShadingLanguage/commit/e4e5088ed6dcd4eb636430dcce9fe815e435b1a6)
#### Monday 2022-10-17 21:51:03 by Larry Gritz

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
## [serd2011/terminal](https://github.com/serd2011/terminal)@[b4b6636b49...](https://github.com/serd2011/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Monday 2022-10-17 21:52:19 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [MortonArb-ForestEcology/MANDIFORE_modeling](https://github.com/MortonArb-ForestEcology/MANDIFORE_modeling)@[8685935580...](https://github.com/MortonArb-ForestEcology/MANDIFORE_modeling/commit/86859355805bcf0aa392573b7dc1b37b4057cd64)
#### Monday 2022-10-17 22:04:04 by LucienFitzpatrick

Attempt at visualizing multiple comparison

This is honestly driving me crazy. Any premade solutions don't work with the way we have our models run and data organized so I've been trying to write out a loop that will allow us to assign groups. I've gotten close but the final steps of how to identify the groups and paste on labels is driving me up a wall. I've spent more than 4 hours today trying to solve this and so I think it's going to be punted until later in the graphics cleaning process because I'm struggling and need to make progress elsewhere

---
## [Francesco149/cubecalc-ui](https://github.com/Francesco149/cubecalc-ui)@[0d7a47a57f...](https://github.com/Francesco149/cubecalc-ui/commit/0d7a47a57f3ba829d285b5e82f9cc0da5822538d)
#### Monday 2022-10-17 23:37:16 by Franc[e]sco

fucking shit ass tags not sorting properly so now I have to change the CI shit

---

