## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-07](docs/good-messages/2023/2023-02-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,262,525 were push events containing 3,509,941 commit messages that amount to 288,672,530 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [TheSylphIsIn/pokeemerald](https://github.com/TheSylphIsIn/pokeemerald)@[fe12de74dd...](https://github.com/TheSylphIsIn/pokeemerald/commit/fe12de74dd44fedbdef30366d294b41db9b686cb)
#### Tuesday 2023-02-07 01:23:15 by TheSylphIsIn

Overworld Sprites batch 1

Adds the following overworld sprites:
- male protag walking
- male protag running
- male protag surfing
- male protag mach bike
- male protag field move
- female protag walking
- female protag running
- female protag surfing
- female protag mach bike
- female protag field move
- zombie boy
- zombie girl
- flying head
- demon corpse

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[c9a7611c75...](https://github.com/Kapu1178/daedalusdock/commit/c9a7611c75ca8d6fbbe413cc52607ab495017cb8)
#### Tuesday 2023-02-07 01:23:43 by Kapu1178

Fixes asset caching (#69852) (#193)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [FRC-Team3484/X23_RobotCode](https://github.com/FRC-Team3484/X23_RobotCode)@[b59131dcc2...](https://github.com/FRC-Team3484/X23_RobotCode/commit/b59131dcc2baf9a2b434310e35fe871c2b8d665d)
#### Tuesday 2023-02-07 02:05:18 by Programmer1

My Funny alex Friend said to me "You understand where parameters are, not what they do yet. I am beating your brain." he also put in a FPD loop because the I scared him and he likes giving me more work to do. I am afraid of deer, chickens and feeling my ribcage. -p <3

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[06a7e74790...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/06a7e74790b3b05b7f4fb522ff55858ef0d66418)
#### Tuesday 2023-02-07 02:35:26 by Unit2E

Changes the hypno flash to work on unconscious people (#73025)

## About The Pull Request

The hypno flash is a really fun and flavourful item that is both strong
while allowing for gimmicks. However, personally, I've always been a bit
confused as to what counted for hypnosis, until looking into the
specifics. I also know that I'm probably not alone in this, because
various people have told me over the years that sleep doesn't work,
while it definitely does. This PR hopes to change this by somewhat
buffing the hypno flash, by making unconsciousness work for hypnosis.

## Why It's Good For The Game

Unconsciousness looks very similar to sleep, and in a lot of cases it is
really just the same effect... except for hypnosis, where there is no
effect on unconscious people. Personally, I don't think this is the best
UX and it limits the options there are for hypnotising people, which is
a shame, as I think it's very interesting. This may or may not be too
strong (think using the hypno flash with the micro-laser), but I still
think this is preferable to only working with sleep specifically or
hypnosis, might warrant a TC up if people otherwise agree with the
change. Also, just to note, unconsciousness is also still separate from
crit. This does not let you hypnotise people for free because they're in
crit.

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[a155df74a0...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/a155df74a09c075efe1339cd1cd24e5cc189fc12)
#### Tuesday 2023-02-07 02:35:26 by Rhials

Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

---
## [underst11d/donkstation](https://github.com/underst11d/donkstation)@[0631fe5bde...](https://github.com/underst11d/donkstation/commit/0631fe5bde73a68b4c12bdfa633c30b2cee442d5)
#### Tuesday 2023-02-07 02:36:08 by Jacquerel

Add Croissants & Traitorous Baking Techniques (#72232)

## About The Pull Request

This is my Christmas present to mimes everywhere.

First of all this adds Croissants, because I thought they already
existed and was shocked to learn that they did not.

![image](https://user-images.githubusercontent.com/7483112/209454610-4e69563f-b83d-465b-b28e-7e0b482ff01b.png)
Here's a croissant and an unbaked croissant.
In terms of food they are GRAIN, DAIRY, and BREAKFAST and made fairly
simply from sugar, dough, and butter.

Secondly it adds this pack of traitor gear, exclusively for Mimes and
Chefs.

![image](https://user-images.githubusercontent.com/7483112/209454613-059759b2-774c-45e2-9e1e-97adb43f75f1.png)
The contents of this pack are:
- One combat baguette, indistinguishable from a regular baguette. If
wielded as a sword it gains a 50% block chance (equal to the Captain's
sabre) and does 20 damage.
- Two throwing croissants, which do 20 throwing damage and return to
your hand like boomerangs.
- A cookbook which teaches you the secret to turning croissaints into
deadly boomerang weapons.

You make a croissant into a throwing croissant simply by inserting an
expertly bent iron rod into it.
The chef can't make any use of the baguette unless they also gain the
ability to mime, but they can use it to make food.


https://user-images.githubusercontent.com/7483112/209454703-feafcf4c-6d0a-4e9a-ac4a-d3e2fc7c0ffb.mp4

Watch me here struggle to use them to kill an ape (they don't return to
your hands if thrown at an adjacent tile).

## Why It's Good For The Game

It's insane that croissants aren't already in the game.
This gives mimes an "invisible" sword to go with their invisible gun (it
announces to everyone nearby when you're about to use it, but they can't
know if it's just a _regular_ baguette).
It's funny to throw bread at people.

## Changelog

:cl:
add: You can now bake croissants to add to your breakfast.
add: Traitorous chefs can bake dangerous throwing croissants, Mimes can
do this and gain the additional benefit of a deadly combat baguette.
/:cl:

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[ffac8f0df0...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/ffac8f0df07c8473e26420a8fe3c1acf6bd20dbf)
#### Tuesday 2023-02-07 02:38:26 by SkyratBot

[MIRROR] Fixes critical plane masters improperly not being readded in show_to [MDB IGNORE] (#19060)

Fixes critical plane masters improperly not being readded in show_to (#72604)

## About The Pull Request

[Adds support for pulling z offset context from an atom's
plane](https://github.com/tgstation/tgstation/commit/9f215c5316e5cfdbedf6a23ff97dfee0e523354b)

This is needed to fix paper bins, since the object we plane set there
isn't actually on a z level.
Useful elsewhere too!

[Fixes compiler errors that came from asserting that plane spokesmen had
a plane
var](https://github.com/tgstation/tgstation/commit/b830002443f2fbe230e9ff00236d7a46a9f2eec7)

[Ensures lighting backdrops ALWAYS exist for each lighting
plane.](https://github.com/tgstation/tgstation/commit/0e931169f7c5336333bc6f41353c82f603fc1170)

They can't float becuase we can see more then one plane at once yaknow?

[Fixes parallax going to shit if a mob moved zs without having a
client](https://github.com/tgstation/tgstation/commit/244b2b25baecfc644505a3ea1e348e0cb97a04e0)

Issue lies with how is_outside_bounds just blocked any plane readding
It's possible for a client to not be connected during z moves, so we
need to account for them rejoining in show_to, instead of just blocking
any of our edge cases.

Fixing this involved having parallax override blocks for show_plane and
anything with the right critical flags ensuring mobs have JUST the right
PMs and relays.
It's duped logic but I'm unsure of how else to handle it and frankly
this stuff is just kinda depressing.
Might refactor later

[show_to can be called twice successfully with no hide_from
call.](https://github.com/tgstation/tgstation/commit/092581a5c06f7f884f48d41c96fa9300327ef214)

Ensures no runtimes off the registers from this

## Why It's Good For The Game

Fixes #72543
Fixes lighting looking batshit on multiz. None reported this I cry into
the night.

## Changelog
:cl:
fix: Fixes parallax showing up ABOVE the game if you moved z levels
while disconnected
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [Logg-y/the-frozen-north](https://github.com/Logg-y/the-frozen-north)@[6c25ebf280...](https://github.com/Logg-y/the-frozen-north/commit/6c25ebf28045e7109fae867cf4e5665060ff4fa4)
#### Tuesday 2023-02-07 03:01:31 by Logg-y

Belial, Treasure maps, Looted placeables persist, and much more

The big:

Added the Belial ending to Castle Jhareg.
Added treasure maps to the game. These can be found in random loot, but especially from bosses/semibosses, and in Marauder's Bay. You might need to pick up a shovel from random loot or local stores to complete these. (If a surface isn't diggable, try checking your map in the right spot!) For a more complete overview, see https://docs.google.com/document/d/1MuobXGEgmDkli41MOa0MP3_f9WqZEI0bc1aZkjuPsM4/edit?usp=sharing - at the time of writing there are 647 possible locations these can take you
Looted placeables no longer disappear, but instead become unusable for those who don't have anything left in them.
It should now be possible to conduct a barter without the UI closing itself every 6 seconds.
Container items (magic bags, large boxes) can now be renamed by using their new activate option. The activate itemproperty will be applied to existing containers, too.
Bless now affects the caster when cast from an item or potion.

The small:

Examining an item will now display its minimum level requirement if you already meet it.
Significantly reduced the difficulty of the fight at the altar in the Heart of the Forest. The rest of the area is however filled with more Shadow Druids.
Doubled the length of time the Spirit of the Wood is held after the death of a shadow druid.
Creatures no longer move to investigate distant creatures they can hear but can't see. This should hopefully reduce the amount of enemies that rush to help in interior areas such as Helm's Hold.
Added a visual notifier that you can pull the puzzle completion lever in the Underdark tile puzzle.
Fixed both Jhareg quarters containing the same journal text.
Fixed punctuation in the name of the Watchmen's Demise dagger.
Fixed Neverwinter North Gate having no challenge rating.
Fixed enemies being able to rest while petrified (which would remove their petrification in the process).
Fixed an edge case that could make NPCs not talk after combat. This is unrelated to the prior NPC inactivity bug.
Resting at home when at 100% rested XP no longer triggers the cooldown for resting at home.
Fix towards henchmen standing unresponsive next to dead players, oblivious to enemies attacking them.
Tidied up lots of custom tokens internally. This shouldn't change anything, but there is a small risk that bugs have been introduced to certain conversations: these will now display wrong prices or unrelated text.
The adventurer handbook now displays a player's respawn location.
Added some feedback on when your progess isn't being saved continuously, and resting or entering a new area should bypass this regardless. (This is likely a NWNX bug which says your character is bartering constantly even when you aren't)
Slightly reduced the challenge rating of Skeleton Archers and Warriors. This makes them drop a bit less loot and reward less experience, as they made the Valley of the Dead and related areas disproportionately good for experience and loot relative to their difficulty.
Reduced the area CR of the Underdark Spider tunnels.
Reduced the experience reward of the Formian bounty.
Increased the save DC of Fire Elemental auras from 2 to 8, but a successful save now negates all damage instead of halving it.
Increased bone ring save vs negative energy from 1 to 2. Existing rings are not changed.
Certain clutter items no longer require identification.
Ansal in Thundertree now directs players towards Charwood and the strange events happening there.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[38ae1d4785...](https://github.com/pytorch/pytorch/commit/38ae1d4785a677ef0734105dad2fd904270aca46)
#### Tuesday 2023-02-07 03:53:31 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [ShivaD173/pokemon-showdown](https://github.com/ShivaD173/pokemon-showdown)@[5cbb317a4c...](https://github.com/ShivaD173/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Tuesday 2023-02-07 03:57:54 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Darmanitan-Galar's Choice Band set (#9354)

* Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

* Update data/mods/gen8/factory-sets.json

---------

Co-authored-by: Kris Johnson <11083252+KrisXV@users.noreply.github.com>

---
## [xyz-mocha/kernel_xiaomi_sdm660](https://github.com/xyz-mocha/kernel_xiaomi_sdm660)@[de3ee0be25...](https://github.com/xyz-mocha/kernel_xiaomi_sdm660/commit/de3ee0be251e7024121a238744f2410389a7d004)
#### Tuesday 2023-02-07 05:46:48 by Christian Brauner

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
## [mosoft521/guava](https://github.com/mosoft521/guava)@[8a676ade61...](https://github.com/mosoft521/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Tuesday 2023-02-07 08:18:29 by cpovirk

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4ebea2a206...](https://github.com/treckstar/yolo-octo-hipster/commit/4ebea2a20648685a1a14d2cd5b411a039bab2f7e)
#### Tuesday 2023-02-07 08:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Tuesday 2023-02-07 09:35:28 by Ævar Arnfjörð Bjarmason

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Tuesday 2023-02-07 09:55:50 by Romain Derie

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

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[ef335f7d1f...](https://github.com/Jacquerel/orbstation/commit/ef335f7d1f33d196062a5a285c7f7216df2302a6)
#### Tuesday 2023-02-07 10:39:58 by Rhials

It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#73018)

## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[5f78464e25...](https://github.com/harryob/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Tuesday 2023-02-07 13:28:04 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[f6005e27d2...](https://github.com/rust-lang-ci/rust/commit/f6005e27d21dc675f50fe61b6992a431700cefe5)
#### Tuesday 2023-02-07 13:50:43 by bors

Auto merge of #107760 - thomcc:utf8dfa, r=<try>

Rewrite libcore's UTF-8 validation for performance

This optimizes the `core::str::from_utf8` function significantly (initial measurements indicates that it's often 1.5x faster, especially for non-ASCII, where it can be up to 3x faster).

It does this mostly by leveraging the [shift-based DFA](https://gist.github.com/pervognsen/218ea17743e1442e59bb60d29b1aa725) technique (a recent obsession), but also it adding SIMD to the ASCII fast path (and really just completely rewrites and restructures how the validation is done).

For prior art: shift-DFAs are now used for UTF-8 validation in [PostgreSQL](https://github.com/postgres/postgres/blob/aa6954104644334c53838f181053b9f7aa13f58c/src/common/wchar.c#L1753), and seems to be in progress or under consideration for use in [Julia](https://github.com/JuliaLang/julia/pull/47880) and perhaps [Go](https://github.com/golang/go/issues/47120). Of these, PG's impl is the most similar to this one, at least at a high level[^pg].

[^pg]: The main similarity is that PG also uses 32bit rows in the transition table, and has a special case for ASCII (even if the way we special case it is very different). Beyond that, the impls are really totally different (theirs has fewer optimizations, doesn't need tracking any info for error positions, uses a different UTF8 automaton, and is just completely different code).

---

This PR is not quite ready for review. I'm mostly getting this up now so I can check some perf runs and such. Assuming they (or further benchmarks) don't reveal issues, I believe the approach is basically complete, but the PR needs the following work to be ready for review I intend to:

- [ ] Add more comments/docs, it's totally impossible to follow at the moment.
- [ ] Rewrite the code for the table so that it's comprehensible instead of a total black box, and include a link to a generator the constants use.
- [ ] Rewrite the ASCII scan loop (which is pretty clownshoes at the moment, and probably should still handle alignment after the first load).
- [ ] Ensure the tests cover all the optimized cases (both short/long strings).
- [ ] Integrate some of my benchmarks[^bench].

[^bench]: The benchmarks I have locally have too much PII to be published as-is, since I derived them from real use including browser history, but that's a temporary situation. Some preliminary benchmarks based on the `simdutf8` corpus are [here](https://gist.github.com/thomcc/1d03d323aecfed570c77c060e2e1cb63). It demonstrates a speedup in basically every case (across all string sizes and character compositions), although the real-world improvement seems to be even higher (the current impl has branch misprediction issues for non-ASCII, which are not reflected in these benchmarks).

I'm deliberately leaving anything that touches other functions as follow-up work that I'll do after this lands. That includes improving `String::from_utf8_lossy` or sharing any logic with `is_ascii`

(Note: some stuff came up in $dayjob so it may be a week or two before I finish all this, just wanted to get this up in the meantime so that it's not really in the back of my mind as much)

## Appendix: FAQ

### Potential Drawbacks

- Weird algo involving a magic table. I will document this way better so that this drawback goes away.
- Slightly slower in the invalid UTF-8 path, as we may re-validate up to 16 bytes. I'll probably fix this for truncation, but even so it is pretty minimal. It's very likely that if the error isn't right at the start of the string, this is version is still much faster.
- Probably worse on some machines, including ones slow (slower than doing scalar operations) unaligned loads, and slow dynamic right shifts (slower than branching).
- Additional 8kb table, although I'm very careful not to touch it for the pure-ASCII path (doing this without eliminating the benefit of the shift-DFA was hard).
- Need `const_eval_select`. This is both because LLVM was doing worse on the `while ...` version of some of the loops, and because `core::simd` isn't const-compatible (trait usage). The function we call would still exist either way though.

### Why not `simdutf8`'s algorithm?

Short version:
- Can't use algos requiring new instructions in libcore for various reasons. Not worth it to maintain just for `-Zbuild-std` users (okay, and `aarch64` users).
- This impl is pretty small, mostly portable (a couple special cases in the ASCII handling, but nothing complex or conditionally compiled), and does not require much target-specific complexity.
- On the bright side, we're faster for strings up to around 40-120 bytes anyway. At least on my machines.

Long version: <https://gist.github.com/thomcc/f153a122f680023f937f2c912978b8e6>.

---
## [dbutenhof/pbench](https://github.com/dbutenhof/pbench)@[1fd8835f63...](https://github.com/dbutenhof/pbench/commit/1fd8835f63b3486d842589d660a699b39e20f5a6)
#### Tuesday 2023-02-07 14:29:52 by David Butenhof

Fix operation synchronization

PBENCH-993

This is fairly large, but yet much smaller than it started out. This solves
two problems in Pbench Server task scheduling:

1. The default SQLAlchemy transaction model is to start a transaction on any
   SELECT and end it on any UPDATE or INSERT; this means there's no potential
   for atomic update. This impacts the management of all internal context, but
   serious problems have been observed with the "operation" and "state" of the
   datasets.
2. I began the dataset with the concept of a "state", as the dataset
   progresses through upload, backup, unpack, index, and delete. I quickly
   discovered that this wasn't ideal, but had trouble backing off completely
   from the concept. When I added the DB-based "operation" to replace the old
   filesystem links, the relationship between "operation" and "state" became
   even messier.

The primary change here is to divorce the `Sync` class entirely from general
metadata. (I originally set out to make `Metadata` management atomic, and the
fan-out was enormous: I'll tackle that again later, but while important in the
long run, getting `Sync` working is immediately critical.)

There is a new `Operation` DB object associated with a `Dataset`, and this is
entirely managed within the `Sync` class. For visibility, `Dataset.as_json`
will collect associated rows just as it does for `dataset.metalog`, but this
doesn't require any special transactional management. (It's a snapshot.)

I've completely *removed* the `Dataset.state` column (and its associated "last
transition" timestamp). "State" is tracked and observed by the various `Operation`
rows created and managed by `Sync`. This corresponds to the previous
dataset.status` sub-object managed by the old `Sync`: each named operation
(`OperationName` enum) that's been associated to a dataset will have a row with
`state` and `message` columns. The `state` can be advanced through `READY`, `WORKING`, `OK`, and `FAILED`, and a message can be associated with each
row (on error via `Sync.error` or as part of transition via `Sync.update`).

While I was modifying the Dataset schema, I also removed the `created` column;
it's really redundant with `dataset.metalog.pbench.date`, and we'll need to
understand that for "non-Pbench-standard" tarballs we might not be able to get
this anyway. This wasn't quite as "easy" as I'd thought, because it meant that
I had to refactor date-range operations to work on `uploaded` (perhaps they
should have been that way originally).

`Sync.__init__`: Construct a sync object for a particular named operation.
`Sync.next`: Return a list of datasets which have `Operation` rows for the
   sync component that are in `READY` state.
`Sync.update`: Change the state of the sync component's `Operation`,
   optionally add a message to that `Operation`, and set a list of named
   operations for that dataset to `READY`.
`Sync.error`: Change the state of the sync component's `Operation` to `FAILED`
   and record an explanatory message for the failure.

To avoid rippling massive SQLAlchemy transaction model changes across all our
code, I've added a second session factory in `Database` with the most strict
integrity level, `SERIALIZABLE`. (In fact, I *think* that `"REPEATABLE READ"`
would be enough, and slightly more efficient, but sqlite3 doesn't support that
and I don't think I want to trust the weaker model it does support.)

*Only* the `Sync` class in `sync.py` currently uses that alternate session
factory. To avoid conflicts and confusions with autoflush and autocommit and
other SQLAlchemy "help", I'm creating new sessions on-the-fly for each call
and retiring them after commit/rollback. Note that the idiom
`with Database.maker.begin() as session:` constructs a new session with fresh
state, allows a sequence of session operations, and then implicitly tears down
the session after it commits on success or rolls back on an exception.

To avoid multiple `SELECT` statements within our transaction, `Sync.update`
fetches all relevant rows in a single `SELECT`, and then organizes them for
selective updates. This ensures we have no `SELECT` following the update of any
proxy object, which confuses SQLAlchemy in normal configuration.

`Sync.update` and `Sync.error` will loop up to 10 times on commit failure to
re-try with fresh data. Note that I've observed the retry logic in dozens of
functional test runs; and while I wonder vaguely whether I should be concerned
with the constant 10, I rarely see more than one or two retries since I added
a small delay to minimize thrashing.

---
## [thordarsen/AzerothCore-wotlk-with-NPCBots](https://github.com/thordarsen/AzerothCore-wotlk-with-NPCBots)@[ef949f9ff0...](https://github.com/thordarsen/AzerothCore-wotlk-with-NPCBots/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Tuesday 2023-02-07 15:04:37 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [fabiocannizzo/Stockfish](https://github.com/fabiocannizzo/Stockfish)@[cb9c2594fc...](https://github.com/fabiocannizzo/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Tuesday 2023-02-07 15:57:53 by Tomasz Sobczyk

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
## [rwp0/perl5](https://github.com/rwp0/perl5)@[fe5492d916...](https://github.com/rwp0/perl5/commit/fe5492d916201ce31a107839a36bcb1435fe7bf0)
#### Tuesday 2023-02-07 17:00:17 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at
the very least. Given that the perl internals code is somewhat poorly
abstracted from the regexp engine, with parts of the abstraction leaking out,
I think this is acceptable. If we want to make plug in regexp engines work
properly IMO we need to add some more hooks that they need to implement than
we currently do. For instance mg.c does more work than it should. Given there
are only a few plug in regexp engines and that it is specialized work, I
think this is acceptable. We can work with the authors to refine the API
properly later.

---
## [MMMiracles/tgstation](https://github.com/MMMiracles/tgstation)@[6de1258bd3...](https://github.com/MMMiracles/tgstation/commit/6de1258bd3fb5919bb45f3dac3ae801d4b3bc8d6)
#### Tuesday 2023-02-07 17:11:36 by Jacquerel

Admins can now choose where fish go (#73109)

## About The Pull Request

I've pigeonholed myself as the fish guy now. It seems like someone made
events easier to add admin controls for so I thought I'd add some to the
event I most recently touched.

Instead of letting the RNG choose admins can now direct a circle of carp
to converge upon a specific location, or even a trail of specific
locations if they want the carp to just sort of swim in a circle around
the space station (although the ones on the far side of the station from
the starting point will travel all the way through it to get there).
This also works with magicarp.
They don't really move fast enough for you to use this to punish a
specific person but you can use it to annoy a specific location full of
people.

Plausibly there's no reason the code _wouldn't_ work for a specified
atom instead of a turf (as long as it sticks to one z level) but I
couldn't think of an elegant way of selecting that whereas "use my
current ghost location" is very intuitive, so I didn't add one.

## Why It's Good For The Game

Plausibly this permits admins do more fun things.

## Changelog

:cl:
admin: Admins can direct where carp (or magicarp) are interested in
going when manually triggering the event
/:cl:

---
## [ExeCute42/Hello-World-Collection-](https://github.com/ExeCute42/Hello-World-Collection-)@[1c27596bc2...](https://github.com/ExeCute42/Hello-World-Collection-/commit/1c27596bc27a745ddea86b71183cd2587f90c752)
#### Tuesday 2023-02-07 17:21:47 by Cherry

Create _READ THE FUCKING NOTE.txt

i hate my stupid life

---
## [Calypso-Station/Skyrat-tg](https://github.com/Calypso-Station/Skyrat-tg)@[635aee8e34...](https://github.com/Calypso-Station/Skyrat-tg/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Tuesday 2023-02-07 17:38:11 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Tomoms/android_frameworks_base](https://github.com/Tomoms/android_frameworks_base)@[d851f7764b...](https://github.com/Tomoms/android_frameworks_base/commit/d851f7764bcf3a425788925d3898cdb7b2769546)
#### Tuesday 2023-02-07 17:49:54 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

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

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [AaronCasas/rdk](https://github.com/AaronCasas/rdk)@[66cdb282a1...](https://github.com/AaronCasas/rdk/commit/66cdb282a1ab2130f9bfd9d3fda12feac5298c9f)
#### Tuesday 2023-02-07 18:23:48 by Alan Davidson

[RSDK-923] Make GPS-RTK code more robust, remove bad test (#1679)

Changes include:
- Migrate go statements to `utils.PanicCapturingGo()`
- Don't start the background goroutine unless the rest of startup succeeds (to prevent leaking goroutines)
- Lock the mutex whenever you read or write any data that is also read/written from a different goroutine (this was the actual cause of the race conditions!)
- Remove the test that sometimes fails due to a bug in third-party code. It sucks that it sometimes fails, but all the problems are down in the bowels of https://github.com/de-bkg/gognss, and not in code we own.

Things I kinda wanted to change but didn't: 
 - `RTKMovementSensor.GetStream()` is nearly identical to `ntripCorrectionSource.GetStream()`, and the only times you call the RTK version, you always pass in the same state stored in an ntrip object. Unfortunately, it's a _different_ ntrip object defined in the same file as `ntripCorrectionSource`. Should the function be moved to that class instead, or removed entirely? I dunno. Something in here is redundant, but I couldn't remove the duplication without thinking a lot more.

I ran the tests 1,000 times: no failures. It's possible I'm being overly cautious with the mutex, and if you have specific ones you want me to remove, I'm happy to do so. It's possible I'm writing non-idiomatic Go code, and I'm happy to rewrite this whole thing if you have a different style I should match.

---
## [Sheits/fulpstation](https://github.com/Sheits/fulpstation)@[ca0fedc60f...](https://github.com/Sheits/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Tuesday 2023-02-07 19:13:00 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [WonderfulK-JGithub/Bloom](https://github.com/WonderfulK-JGithub/Bloom)@[da235eb91c...](https://github.com/WonderfulK-JGithub/Bloom/commit/da235eb91ca93755be52b6ddbef3c43af87d3c51)
#### Tuesday 2023-02-07 20:31:41 by Max

An oil is any nonpolar chemical substance that is composed primarily of hydrocarbons and is hydrophobic (does not mix with water) & lipophilic (mixes with other oils). Oils are usually flammable and surface active. Most oils are unsaturated lipids that are liquid at room temperature.  The general definition of oil includes classes of chemical compounds that may be otherwise unrelated in structure, properties, and uses. Oils may be animal, vegetable, or petrochemical in origin, and may be volatile or non-volatile.[1] They are used for food (e.g., olive oil), fuel (e.g., heating oil), medical purposes (e.g., mineral oil), lubrication (e.g. motor oil), and the manufacture of many types of paints, plastics, and other materials. Specially prepared oils are used in some religious ceremonies and rituals as purifying agents.  Etymology First attested in English 1176, the word oil comes from Old French oile, from Latin oleum,[2] which in turn comes from the Greek ἔλαιον (elaion), "olive oil, oil"[3] and that from ἐλαία (elaia), "olive tree", "olive fruit".[4][5] The earliest attested forms of the word are the Mycenaean Greek 𐀁𐀨𐀺, e-ra-wo and 𐀁𐁉𐀺, e-rai-wo, written in the Linear B syllabic script.[6]  Types Organic oils Organic oils are produced in remarkable diversity by plants, animals, and other organisms through natural metabolic processes. Lipid is the scientific term for the fatty acids, steroids and similar chemicals often found in the oils produced by living things, while oil refers to an overall mixture of chemicals. Organic oils may also contain chemicals other than lipids, including proteins, waxes (class of compounds with oil-like properties that are solid at common temperatures) and alkaloids.  Lipids can be classified by the way that they are made by an organism, their chemical structure and their limited solubility in water compared to oils. They have a high carbon and hydrogen content and are considerably lacking in oxygen compared to other organic compounds and minerals; they tend to be relatively nonpolar molecules, but may include both polar and nonpolar regions as in the case of phospholipids and steroids.[7]  Mineral oils Main article: Mineral oil Crude oil, or petroleum, and its refined components, collectively termed petrochemicals, are crucial resources in the modern economy. Crude oil originates from ancient fossilized organic materials, such as zooplankton and algae, which geochemical processes convert into oil.[8] The name "mineral oil" is a misnomer, in that minerals are not the source of the oil—ancient plants and animals are. Mineral oil is organic. However, it is classified as "mineral oil" instead of as "organic oil" because its organic origin is remote (and was unknown at the time of its discovery), and because it is obtained in the vicinity of rocks, underground traps, and sands. Mineral oil also refers to several specific distillates of crude oil.[citation needed]  Applications Cooking Main article: Cooking oil Several edible vegetable and animal oils, and also fats, are used for various purposes in cooking and food preparation. In particular, many foods are fried in oil much hotter than boiling water. Oils are also used for flavoring and for modifying the texture of foods (e.g. stir fry). Cooking oils are derived either from animal fat, as butter, lard and other types, or plant oils from olive, maize, sunflower and many other species.[9]  Cosmetics Oils are applied to hair to give it a lustrous look, to prevent tangles and roughness and to stabilize the hair to promote growth. See hair conditioner.[citation needed]  Religion Oil has been used throughout history as a religious medium. It is often considered a spiritually purifying agent and is used for anointing purposes. As a particular example, holy anointing oil has been an important ritual liquid for Judaism[10] and Christianity.[11]  Painting Main article: Oil painting Color pigments are easily suspended in oil, making it suitable as a supporting medium for paints. The oldest known extant oil paintings date from 650 AD.[12]  Heat transfer See also: Transformer oil Oils are used as coolants in oil cooling, for instance in electric transformers. Heat transfer oils are used both as coolants (see oil cooling), for heating (e.g. in oil heaters) and in other applications of heat transfer.[citation needed]  Lubrication  Synthetic motor oil Given that they are non-polar, oils do not easily adhere to other substances. This makes them useful as lubricants for various engineering purposes. Mineral oils are more commonly used as machine lubricants than biological oils are. Whale oil is preferred for lubricating clocks, because it does not evaporate, leaving dust, although its use was banned in the USA in 1980.[13]  It is a long-running myth that spermaceti from whales has still been used in NASA projects such as the Hubble Space Telescope and the Voyager probe because of its extremely low freezing temperature. Spermaceti is not actually an oil, but a mixture mostly of wax esters, and there is no evidence that NASA has used whale oil.[14]  Fuel Main article: Fuel oil Some oils burn in liquid or aerosol form, generating light, and heat which can be used directly or converted into other forms of energy such as electricity or mechanical work. In order to obtain many fuel oils, crude oil is pumped from the ground and is shipped via oil tanker or a pipeline to an oil refinery. There, it is converted from crude oil to diesel fuel (petrodiesel), ethane (and other short-chain alkanes), fuel oils (heaviest of commercial fuels, used in ships/furnaces), gasoline (petrol), jet fuel, kerosene, benzene (historically), and liquefied petroleum gas. A 42-US-gallon (35 imp gal; 160 L) barrel of crude oil produces approximately 10 US gallons (8.3 imp gal; 38 L) of diesel, 4 US gallons (3.3 imp gal; 15 L) of jet fuel, 19 US gallons (16 imp gal; 72 L) of gasoline, 7 US gallons (5.8 imp gal; 26 L) of other products, 3 US gallons (2.5 imp gal; 11 L) split between heavy fuel oil and liquified petroleum gases,[15] and 2 US gallons (1.7 imp gal; 7.6 L) of heating oil. The total production of a barrel of crude into various products results in an increase to 45 US gallons (37 imp gal; 170 L).[15]  In the 18th and 19th centuries, whale oil was commonly used for lamps, which was replaced with natural gas and then electricity.[16]  Chemical feedstock  This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed. (November 2017) (Learn how and when to remove this template message) Crude oil can be refined into a wide variety of component hydrocarbons. Petrochemicals are the refined components of crude oil[17] and the chemical products made from them. They are used as detergents, fertilizers, medicines, paints, plastics, synthetic fibers, and synthetic rubber.  Organic oils are another important chemical feedstock, especially in green chemistry.

---
## [Fireye04/TGS-Spotify-Project](https://github.com/Fireye04/TGS-Spotify-Project)@[3f66b1e74a...](https://github.com/Fireye04/TGS-Spotify-Project/commit/3f66b1e74aa5d8e6d216a91d8e591653a11c3ff1)
#### Tuesday 2023-02-07 20:55:40 by Jack

My build requests are fine, thank you very much.

In fact, they're the greatest build requests of all time. No one understands build requests quite like me.
I mean, what do they even do? Nobody knows. But I know. I know what they do. I know more than anyone ever, ask anyone. They'll tell you.
Really... If I'm being honest with everyone... I'm the smartest individual alive. I mean, seriously, people- you think I need better build requests? No- in fact, no one has ever said that ever. One time I met the Pope- great guy, really great guy, probably one of the best people I've ever met- and he looked at my pull request and I tell you now that he looked at me and he said: "This is the most intelligent, well written, and descriptive pull request of all time. Truly great work."
If the Pope saying that my pull requests are the best there are doesn't convince you, I don't know what will... and frankly, the only people saying that are the people that hate America. I hate to say it; truly, I do. But it is the sad truth.

One time, when I was a little boy (still very intelligent, mind you), I made a pull request. My teacher walked over to my desk and told me, and I mean this: "Donald, your pull request is the best request I've ever seen. Truly wonderful. A+. In fact, I think we should bring in John F. Kennedy to look at this pull request as soon as possible." After she said that, everyone clapped.
Just two days later, President Kennedy walked into my classroom. He shook my hand, told me: "Son, I'm proud of what you've done. Great stuff, really. You'll go far." Everyone clapped again, and after I signed his shirt (since he was such a big fan), he left for Washington, telling me that one day I'd be President.

So yeah. I have the greatest pull requests around. Don't say otherwise, please. In fact, maybe YOU should learn a thing or two from ME.

---
## [min-jean-cho/pytorch](https://github.com/min-jean-cho/pytorch)@[5c6f5439b7...](https://github.com/min-jean-cho/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Tuesday 2023-02-07 21:03:58 by Edward Z. Yang

Implement SymBool (#92149)

We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyang@meta.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/92149
Approved by: https://github.com/albanD, https://github.com/Skylion007

---
## [enze-l/smart-plug-research](https://github.com/enze-l/smart-plug-research)@[9db1fa9f14...](https://github.com/enze-l/smart-plug-research/commit/9db1fa9f146c1797424577c266324cd0feba2b04)
#### Tuesday 2023-02-07 21:18:51 by enze-l

Integrate korrektion from my lovely girlfriend till API

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[484f40d680...](https://github.com/mrakgr/The-Spiral-Language/commit/484f40d6805179aad99b99add211984cb79ff7ff)
#### Tuesday 2023-02-07 21:30:06 by Marko Grdinić

"8:55pm. I figured out how the C# compilation works. It is simpler than it seems.

```cs
builder.RootComponents.Add<Qwe>("#appqwe");
```

Let me try this as my last experiment. And in

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>BlazorApp1</title>
    <base href="/" />
    <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet" />
    <link href="css/app.css" rel="stylesheet" />
    <link href="BlazorApp1.styles.css" rel="stylesheet" />
</head>

<body>
    <div id="appqwe">Loading...</div>

    <div id="blazor-error-ui">
        An unhandled error has occurred.
        <a href="" class="reload">Reload</a>
        <a class="dismiss">🗙</a>
    </div>
    <script src="_framework/blazor.webassembly.js"></script>
</body>

</html>
```

I wonder if this is how it works.

...Yep. I understand it. I finally understand the structure of a Blazor project!

Let me go back a bit to the old thing.

9:25pm. Yeah, the old ASP.NET `.chtml` stuff is a wreck. What was MS thinking?

9:40pm. ASP.NET MVC is a pile of shit. No wonder I had trouble understanding it!

It takes quite a lot more to express than the new Blazor can. And in the latest .NET it seems it has been streamlined quite a bit. There has never been a better time to go into web development.

10pm. I am overdoing it. But I understand why I was confused back in 2020. Razor pages (.cshtml) I like a third of a reactive language. It buries me in the irrelevant, and has no power, so it is no wonder I got confused.

https://grpc.io/docs/what-is-grpc/introduction/

While looking at the docs I saw gRPC in ASP.NET, and decided to search for it on the JS. And what do I find, but this!

Yeah, this is something I could have used instead of ZeroMq.

It seems to have proper support than essentially being abandonware.

10:10am. Damn it, what am I going to do about Hopac. If anyone is going to bring it up to .NET Core 7 compability, that would have to be me. Hopefully it will work as is.

10:15pm. Well, I'll cross that bridge when I come to it.

At this point I am confused as to ASP.NET is. It is not Razor pages or Blazor. It is a...framework on which those two are built?

I can only interpret it like that.

https://github.com/giraffe-fsharp/Giraffe

https://dusted.codes/functional-aspnet-core

I think it is just about now that I can start to think about Giraffe.

> Ultimately I would like to build a web application in ASP.NET Core with a functional framework which does not only benefit from Kestrel but also from the entire ASP.NET Core eco system, including other middleware such as static files, authentication, authorization, security, the flexibility of the config system, logging or simply being able to retrieve information from the current hosting environment and more.

I do not really understand what this middleware is or what it offers me. I really have a while to go until I've made it as a webdev.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-7.0

These fundamentals are something I haven't seen before.

This thing actually explains what that startup stuff in ASP.NET does!

> Think of it like this, ASP.NET Core is a web platform which sets the ground work for building any web application and MVC is a framework on top of the platform, which enables building web applications with an object oriented Model-View-Controller design pattern. Ideally as an F# developer I would like to replace the object oriented MVC framework with a functional equivalent, but keep the rest of ASP.NET Core's offering at the same time. This is very difficult with Suave at the moment.

This explains a lot. In order to really pass through to the door to the other side, I need to study these fundamentals.

> Kestrel is extremely fast and the Microsoft team is working hard on making it even faster.

I thought the Kestrel was something different than ASP.NET.

https://dusted.codes/functional-aspnet-core

This is a long article, I won't read it now. Let me close for real this time.

I am convinced now. If I want to understand ASP.NET, I should study Giraffe and then go from there. Though I need to do it as I study the fundamentals."

---
## [MDproductions-dev/mdproductions-v2](https://github.com/MDproductions-dev/mdproductions-v2)@[c7884779c8...](https://github.com/MDproductions-dev/mdproductions-v2/commit/c7884779c8448dde55b778d68f5ceb5a4056ef0b)
#### Tuesday 2023-02-07 21:59:47 by MDproductions_dev

fix video on safari cause they don't support transperant webm video (fuck you)

---
## [kubouch/nushell](https://github.com/kubouch/nushell)@[3d65fd7cc4...](https://github.com/kubouch/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Tuesday 2023-02-07 22:32:10 by Doru

Expose filtering by file type in glob (#7834)

# Description

Add flags for filtering the output of `glob` by file type. I find myself
occasionally wanting to do this, and getting a file's
[file_type](https://docs.rs/wax/latest/wax/struct.WalkEntry.html#method.file_type)
is presumably fast to do as it doesn't have to go through the fallible
metadata method.

The design of the signature does concern me; it's not as readable as a
filter or "include" type list would be. They have to be filtered one by
one, which can be annoying if you only want files `-D -S`, or only want
folders `-F -S`, or only want symlinks `--butwhy?`. I considered
SyntaxShape::Keyword for this but I'll just defer to comments on this PR
if they pop up.

I'd also like to bring up performance since including these flags
technically incurs a `.filter` penalty on all glob calls, which could be
optimized out if we added a branch for the no-filters case. But in
reality I'd expect the file system to be the bottleneck and the flags to
be pretty branch predictor friendly, so eh

# User-Facing Changes
Three new flags when using `glob` and a slightly more cluttered help
page. No breaking changes, I hope.

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [anju-coco/rice-hiroko](https://github.com/anju-coco/rice-hiroko)@[a75d950649...](https://github.com/anju-coco/rice-hiroko/commit/a75d9506496c21b9b6e5fd897830493ed3e122b8)
#### Tuesday 2023-02-07 22:37:59 by 野田浩子

Create 本当に死なないで往生際の悪いマリーアントワネットやるつもりだったんですか??

Surprised judgment... Hiromiya-sama didn't go to Seventh...
My father kept the word and then died... what do you mean??
本当に私が死なない往生際が悪いそのマリーアントワネットでやるの
Charles III of England posted on the Internet that his daughter and Emperor showa were on friendly terms after his father died...it certainly doesn't seem to be Elizabeth II of my lineage...but that's good...
Well, I was surprised by Japan... Reiwa... That emperor what something father after my father died.I'm Marie Antoinette and don't die easily
In other words, Trump's scheme to fabricate?? Even though Showa emperor not responsible for the war... that stupid emperor...
IT want money with a child from Salzburg, but...salzburg is which countory using. that's why He is a Korean of the Japanese emperor.
Prince Anne's daughter?? Her father died in Emperor Showa...
I am dissatisfied with the country's decision...
so it doesn't fit unless 103 years old, right??
The dwarf's DNA matched... that's right... so there's no reason why Dad's DNA doesn't match... so they're all ninth right to live... what does it mean that dad doesn't have a right to live number? That's right... what should I say?? Even to that Yoshiko-san... I wonder if the grandfather was raising a dwarf... but those days weren't exactly unnatural... Dad's face ・・・

---
## [jbjdb9/TotMaandag_Othello](https://github.com/jbjdb9/TotMaandag_Othello)@[f507fd89c5...](https://github.com/jbjdb9/TotMaandag_Othello/commit/f507fd89c55410d406d566a58db8f391f1eeaccf)
#### Tuesday 2023-02-07 22:38:03 by BuildTools

Why are we still here, just to suffer? i cant feel my arms, my legs. Every night i wonder... Why are we still here. Oh ja hij doet t wel goed nu lappe baap oh my god dipper

---
## [vercel/next.js](https://github.com/vercel/next.js)@[268dd6e80b...](https://github.com/vercel/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Tuesday 2023-02-07 22:58:57 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [830008/abyss-browser](https://github.com/830008/abyss-browser)@[9fa00e07fd...](https://github.com/830008/abyss-browser/commit/9fa00e07fd2633bc16776653987abcc05673910f)
#### Tuesday 2023-02-07 23:16:58 by pxstaa

ur ugly as fuck go away bitchhhh

yeahhh uhhh anyway go die

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fedf2f3a26...](https://github.com/tgstation/tgstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Tuesday 2023-02-07 23:37:20 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[fc12508d01...](https://github.com/Floofies/Skyrat-tg/commit/fc12508d01830198416938d9fe0766d2b83101ad)
#### Tuesday 2023-02-07 23:44:18 by SkyratBot

[MIRROR] STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows [MDB IGNORE] (#18775)

* STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

* STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---

